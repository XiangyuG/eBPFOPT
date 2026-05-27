# Demo Programs

This directory contains small C programs for optimization and equivalence-checking experiments.

Generate LLVM IR with `clang`:

```bash
cd demo
clang -S -emit-llvm <name>.c -o <name>.ll
```

Generated `.ll` files are intentionally ignored and should be regenerated locally.
