- Never return the address of a local variable from a function. The memory for local variables is allocated on the [[stack-栈区]] and is automatically deallocated when the function ends. Returning a pointer to a local variable leads to undefined behavior because the memory it points to is no longer valid.
  - If you need to return a complex data structure, consider dynamically allocating memory on the heap using `new`. This memory will persist until you explicitly `delete` it. For example, you can `return new string(some_string)`.
    - Note: Always remember to `delete` any memory you allocate with `new` to prevent memory leaks.
  - Alternatively, you can pass a pointer to a variable (that is in scope outside the function) as a parameter to the function. You can then modify the data at the address that this pointer points to. Since the variable is outside the function's scope, it will not be deallocated when the function ends.

- Here is an example of what not to do:

  ```cpp
  int* badFunction() {
    int a = 5;
    int *b = &a;
    return b; // This is a mistake! 'a' is a local variable and will be reclaimed after the function ends.
  }
  ```
