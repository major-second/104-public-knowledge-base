- 前置
  - [[memory]]

Heap memory, also known as dynamic memory, is a region of a computer's memory that is used for dynamic memory allocation. It is managed by the programmer, and it allows for variables to be allocated and deallocated on the fly ([[online]]) and for data structures to be changed in size.

In C++, heap memory is allocated using the `new` keyword and deallocated using the `delete` keyword. For example:

```cpp
int* p = new int; // Allocates memory for an integer on the heap and returns a pointer to it
*p = 5; // Assigns the value 5 to the memory location pointed to by p
delete p; // Deallocates the memory previously allocated for the integer
```

It's important to note that failing to deallocate memory that has been allocated on the heap can lead to [[memory-leak]]s, where memory is consumed but not released, potentially leading to an application running out of memory.
