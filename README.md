# Systems and Concurrency

A curated C/C++ lab covering Unix processes, program execution, inter-process communication, POSIX threads, synchronization, and a small shell implementation.

The programs remain close to their original learning implementations. This repository organizes them by concept, preserves their provenance, and adds automated compilation checks.

## Contents

| Area | Exercises |
|---|---|
| Processes | Command-line arguments, `fork`, child-process array sorting, and `exec` |
| IPC | Named and unnamed pipes |
| Concurrency | Producer-consumer, mutex exercises, thread joins, and threaded Sudoku validation |
| Shell | A small Unix-style shell implementation |

## Platform

The exercises target a POSIX environment such as Linux. Most examples can be compiled with `g++` and pthread support:

```bash
g++ -std=c++17 -pthread main.cpp -o demo
```

Refer to each exercise README for its exact file layout and usage.

## Provenance and licensing

See [PROVENANCE.md](PROVENANCE.md) for the original repositories. Per-project license files are retained where they existed; no blanket license is applied to previously unlicensed exercises.
