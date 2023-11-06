- Static libraries, also known as archive libraries, are collections of object files that are linked directly into an [[binary-executable]] at compile time.
  - E.g. `.a`
  - [[linux-cpp-compilers]] commands: `g++ <file>.cpp <lib>.a -o <file>`
- Compared to [[cpp-so]]
  - Unlike dynamic libraries, static libraries are included in the final executable, resulting in a standalone executable that does not require external dependencies at runtime.
  - They provide faster startup times and better performance compared to dynamic libraries.
  - However
    - Static libraries can result in larger [[binary-executable]] sizes.
    - 不灵活