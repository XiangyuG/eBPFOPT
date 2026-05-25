#include <linux/bpf.h>
#include <bpf/bpf_helpers.h>

struct {
  __uint(type, BPF_MAP_TYPE_ARRAY);
  __uint(max_entries, 1);
  __type(key, __u32);
  __type(value, __u32);
} control_map SEC(".maps");

struct {
  __uint(type, BPF_MAP_TYPE_ARRAY);
  __uint(max_entries, 1);
  __type(key, __u32);
  __type(value, __u64);
} counter_map SEC(".maps");

SEC("xdp")
int xdp_prog(struct xdp_md *ctx) {
  __u32 key = 0;
  __u32 *flag = bpf_map_lookup_elem(&control_map, &key);

  if (!flag || *flag == 0) {
    return XDP_PASS;
  }

  __u64 *counter = bpf_map_lookup_elem(&counter_map, &key);
  if (counter) {
    __sync_fetch_and_add(counter, 1);
  }

  return XDP_PASS;
}

char _license[] SEC("license") = "GPL";
