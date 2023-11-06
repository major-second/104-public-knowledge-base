- Prerequisites
  - Official Website (Download): [cursur.sh](https://www.cursor.sh/)
  - [[chatgpt]]
    - [[gpt-4]] is available
      - Can be selected from the bottom right corner of the pop-up window during Edit or Chat
  - Add the following at the gear icon next to the minimize button
    - [[openai-account]]
    - [[openai-api]]
      - 202309 [Refer to this](https://zhuanlan.zhihu.com/p/639956119), the programmer might have written something in reverse
      - Therefore, you need to turn off [[openai-api]], set it to `Not Using Key`
- References
  - [[git-basics/basics]]
  - Included in [[editor-index]]
  - Understanding [[vscode]] is helpful
    - [[vscode-cursor]]
# Basic Usage
- The free version will reach maximum capacity, at this point you need [[aggregation]]
- `Ctrl+M Ctrl+O` to open a folder
## edit
- `Ctrl+K` Edit
  - Function
    - Edit based on existing code
      - Can even translate
    - Turn [[comment]], [[pseudo-code]] or partially incomplete code into code
    - Code refactoring
  - During the process, you can also
    - multiple times of interactions
      - Press enter to confirm each time
    - "Quick question", ask related questions during the process
- `Ctrl+/` to toggle whether to use [[gpt-4]]
- `Ctrl+Backspace` `Ctrl+N` to reject
  - Therefore, when editing requires [[keys]], you may need to use `Ctrl+Delete` instead of `Ctrl+Backspace`
  
- `Ctrl+Enter` `Ctrl+Shift+Y` to accept
## chat
- `Ctrl+L` (New) Chat
  - Explain, chat
  - does not change the current code
  - But you can also iteratively generate and refine code blocks, and then copy them over
  - Pressing each time will [[refresh]] the chat thread
- `@` can be used to mention something (e.g. file)
- `Ctrl+Shift+Y` to follow up
## Note
- Remember to copy the prompts in time (to avoid intermittent server errors causing loss of information)
- When running AI generation, it can run in the background while you do other things
