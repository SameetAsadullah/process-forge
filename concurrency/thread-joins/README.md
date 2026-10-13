<h1 align="center">Reverse and Uppercase String Using Thread Joins</h1>

### Description
Two C++ thread pipelines that reverse and uppercase text while coordinating execution order with joins:
1) A pipeline using global thread identifiers (`global_thread_pipeline.cpp`)
2) A pipeline passing thread identifiers between stages (`local_thread_pipeline.cpp`)

### Manual
1) Use any of the following command to `Compile the Code`:
    ```
    g++ -pthread global_thread_pipeline.cpp -o global-thread-pipeline
    ```
    
    ```
    g++ -pthread local_thread_pipeline.cpp -o local-thread-pipeline
    ```

2) Use the following command to `Run the Code`:
    ```
    ./a.out
    ```
