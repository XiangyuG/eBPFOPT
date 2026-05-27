#include <linux/bpf.h>
#include <bpf/bpf_helpers.h>

struct {
  __uint(type, BPF_MAP_TYPE_ARRAY);
  __uint(max_entries, 1);
  __type(key, __u32);
  __type(value, __u32);
} state_map SEC(".maps");

SEC("xdp")
int xdp_prog(struct xdp_md *ctx) {
  __u32 key = 0;
  __u32 *value = bpf_map_lookup_elem(&state_map, &key);

  if (value) {
    __u32 next = *value + 1;
    *value = next;
    return next;
  }

  return XDP_PASS;
}

char _license[] SEC("license") = "GPL";