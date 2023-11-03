- code
    ```cpp
    #include <iostream>
    int main(int argc, char** argv) {
        std::cout << "Number of command line arguments: " << argc << std::endl;
        std::cout << "Command line arguments:" << std::endl;
        for (int i = 0; i < argc; i++) {
            std::cout << "Argument " << i << ": " << argv[i] << std::endl;
        }
        return 0;
    }
    ```
- [[linux-cpp-compilers]]
  - `g++ <file>.cpp -o <file>`
- run [[binary-executable]]
  - `./command_line_args arg1 arg2 arg3`
- 进阶：和[[gflags]]共用
