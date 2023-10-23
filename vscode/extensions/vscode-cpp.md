- 前置
  - [[vscode-extensions]]
- `C/C++`
- `CMake Tools`
- [[settings-json]]
  - 自动[[formatting]]等等
     - 这个[[formatting]]还自动带上[[markdown]]

    ```json
    {
        "editor.formatOnSave": true,
        // cmake 
        "cmake.configureOnEdit": true,
        "cmake.configureOnOpen": true,
        // C_Cpp
        "C_Cpp.formatting": "clangFormat",
        "C_Cpp.clang_format_style": "file",
        "C_Cpp.clang_format_fallbackStyle": "{ BasedOnStyle: Google, ColumnLimit: 100 }",
        "C_Cpp.clang_format_sortIncludes": true,
        "C_Cpp.default.includePath": [
            "~/.conan/data/**",
            "${workspaceFolder}/include",
            "${workspaceFolder}/src",
            "${workspaceFolder}",
            "/usr/local/include",
            "/usr/include"
        ],
        "C_Cpp.default.compilerPath": "/usr/bin/g++",
        "C_Cpp.default.cppStandard": "c++20",
        "C_Cpp.default.cStandard": "c17"
    }
    ```