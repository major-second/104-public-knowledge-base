- 前置
  - [[github-pr]]
  - [[github-issues]]
  - [[git-basics/branch]]
- local merge: `git merge ...`
- [[github]] merge: [[github-pr]], [[github-issues]]等。协作方式。通过各种检查、review后你的[[github-pr]]往往被`main` branch merge
  - 如果`git merge origin main`则默认有弹窗需要`Ctrl X`（即`^X`）退出，此时[[commit]] message是自动生成的
- 协作中，merge 非 main branch可能导致你的[[github-pr]]充满了别人的code modifications，从而增大review难度