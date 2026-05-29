# Demo Programs

This directory contains small C programs for optimization and equivalence-checking experiments.

Examples:

- `add_src.c` / `add_tgt.c`: arithmetic simplification
- `src.c` / `tgt.c`: branch simplification
- `global_src.c` / `global_tgt.c`: return value and global-state equivalence
- `ebpf_map_src.c` / `ebpf_map_tgt.c`: return value and global map equivalence

Generate LLVM IR with `clang`:

```bash
cd demo
clang -S -emit-llvm <name>.c -o <name>.ll
```

For programs that include an external header and call a function defined in another `.c` file, compile each file to LLVM bitcode, link the helper definition into each side, then run Alive2 on the linked IR:

```bash
cd demo
clang -emit-llvm -c include_func_src.c -o include_func_src.bc
clang -emit-llvm -c include_func_tgt.c -o include_func_tgt.bc
clang -emit-llvm -c include_func_helper.c -o include_func_helper.bc
llvm-link-14 include_func_src.bc include_func_helper.bc -S -o src.linked.ll
llvm-link-14 include_func_tgt.bc include_func_helper.bc -S -o tgt.linked.ll
~/alive2/build/alive-tv --func=include_func_prog src.linked.ll tgt.linked.ll
```

Generated `.ll` files are intentionally ignored and should be regenerated locally.
