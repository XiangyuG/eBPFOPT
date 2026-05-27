# Demo Programs

This directory contains small C programs for optimization and equivalence-checking experiments.

Generate LLVM IR with `clang`:

```bash
clang -S -emit-llvm demo/src.c -o demo/src.ll
clang -S -emit-llvm demo/tgt.c -o demo/tgt.ll
clang -S -emit-llvm demo/add_src.c -o demo/add_src.ll
clang -S -emit-llvm demo/add_tgt.c -o demo/add_tgt.ll
clang -S -emit-llvm demo/ebpf_src.c -o demo/ebpf_src.ll
clang -S -emit-llvm demo/ebpf_tgt.c -o demo/ebpf_tgt.ll
```

Generated `.ll` files are intentionally ignored and should be regenerated locally.
