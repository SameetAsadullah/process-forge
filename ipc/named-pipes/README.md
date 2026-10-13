# Bidirectional IPC with Named Pipes

A C++ inter-process communication implementation using two POSIX named pipes for bidirectional messaging between peers.

## Build and run

Compile both peers from `src`:

```bash
g++ -std=c++17 peer_a.cpp -o peer-a
g++ -std=c++17 peer_b.cpp -o peer-b
```

Run `./peer-a` and `./peer-b` in separate terminals. The programs create their FIFOs at runtime.
    
## Screenshot
<div align="center">
  <img src = "https://github.com/SameetAsadullah/Inter-Process-Communication-Using-Named-Pipes/blob/main/extras/working-ss.png" alt = "" width="900px"/>
</div>
