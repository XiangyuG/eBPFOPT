#define XDP_DROP 1
#define XDP_PASS 2

struct xdp_md {
  unsigned int data;
  unsigned int data_end;
};

int xdp_prog(struct xdp_md *ctx) {
  unsigned long data = ctx->data;
  unsigned long data_end = ctx->data_end;

  if (data_end - data < 14)
    return XDP_DROP;

  return XDP_PASS;
}