# Process Forge

A C/C++ systems repository covering Unix processes, program execution, inter-process communication, POSIX threads, synchronization, and a Unix-style shell.

The code is organized by subsystem, with component-level usage guidance and automated compilation checks.

## Contents

| Area | Systems |
|---|---|
| Processes | [Command-line arguments](processes/command-line-arguments), [`fork` factorial](processes/fork-factorial), [child-process array sorting](processes/fork-array-sorting), and [`exec` string reversal](processes/exec-string-reversal) |
| IPC | [Named pipes](ipc/named-pipes) and [unnamed pipes](ipc/unnamed-pipes) |
| Concurrency | [Producer-consumer](concurrency/producer-consumer), [ticket-selling mutex](concurrency/ticket-selling), [withdraw/deposit mutex](concurrency/withdraw-deposit), [thread joins](concurrency/thread-joins), and [threaded Sudoku validation](concurrency/threaded-sudoku-validator) |
| Shell | The [`gbsh` Unix-style shell](shell/gbsh) |

## Platform

The implementations target a POSIX environment such as Linux. Most programs can be compiled with `g++` and pthread support:

```bash
g++ -std=c++17 -pthread main.cpp -o program
```

Refer to each component README for its exact file layout and usage.

## Provenance and licensing

See [PROVENANCE.md](PROVENANCE.md) for source history and licensing. Existing component licenses are retained; no blanket license is applied to previously unlicensed programs.
