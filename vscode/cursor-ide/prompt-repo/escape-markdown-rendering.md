To deal with the automatic rendering of markdown format of your outputs, I defined those three outputs.

1. The underlying output, e.g.


(output starts)
- import re
    ```python
    import re
    ```
- and then do xxx
    ```python
    xxx
    ```
(output ends)

2. The rendered output in the previous case: I cannot see 

```python

or 

```, but only: 

(output starts)
import re
import re
and then do xxx
xxx
(output ends)

This is caused by markdown format rendering, during which the second `import re` statement will be wrapped in a code block, but those backquotes will not be rendered so that I cannot directly copy them.

3. The escaped output which simply replaces every backquote ` in The underlying output with \`, and then wraps everything in ``` ```. The purpose is described as follows: 
( don't escape any other char like []<>\ )


- If the escaped output is

(output starts)
```
\`\`\`cpp
#include <iostream>
\`\`\`
- test
```
(output ends)


- Then because of the markdown rendering I can only see this part

(output starts)
\`\`\`cpp
#include <iostream>
\`\`\`
- test
(output ends)


- Then I can copy this part to my own editor and replace every \` to be `, which gives me

(output starts)
```cpp
#include <iostream>
```
- test
(output ends)


- Given those definitions, Please remember that if I want you to be in the "escaping mode" please always print the escaped output instead of the underlying one.