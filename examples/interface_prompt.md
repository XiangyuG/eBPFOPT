=== USER-SPECIFIED ORIGINAL PROGRAM INTERFACE ===

Original input variables:
- ctx: struct xdp_md *, XDP program argument, packet/context metadata
- control_flag: __u32, BPF map value at key 0 in the control map, enables counter update when present and nonzero
- counter_0: __u64, BPF map value at key 0 in the counter map, current counter value if the entry exists

Original output variables / observable outputs:
- return_value: int, XDP program return value, always XDP_PASS
- counter_0: __u64, BPF map value at key 0 in the counter map, incremented by 1 only when control_flag exists and is nonzero and counter_0 exists

=== END USER-SPECIFIED ORIGINAL PROGRAM INTERFACE ===
