# PHONY in Makefile

In a makefile, a phony target is one that is not really the name of a file; rather it is just a name for a recipe to be executed when you make an explicit request. There are two reasons to use a phony target: to avoid a conflict with a file of the same name, and to improve performance.

For more information, you can refer to the following resources:
- [GNU Make Manual](https://www.gnu.org/software/make/manual/html_node/Phony-Targets.html)
- [StackOverflow Discussion](https://stackoverflow.com/questions/2145590/what-is-the-purpose-of-phony-in-a-makefile)

Here is an example of a phony target in a makefile:

```makefile
.PHONY: clean

clean:
   rm -f *.o
```

In this example, `clean` is a phony target. When you run `make clean`, it doesn't check for a file named `clean`. It just executes the recipe associated with `clean`, which is `rm -f *.o`.

