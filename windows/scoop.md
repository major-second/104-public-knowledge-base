- 前置
  - [[run-ps1]]
  - [[administrator-powershell]]
-   ```powershell
    (base) PS C:\WINDOWS\system32> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    (base) PS C:\WINDOWS\system32> Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
    Initializing...
    Downloading ...
    Creating shim...
    Adding ~\scoop\shims to your path.
    Scoop was installed successfully!
    Type 'scoop help' for instructions.
    (base) PS C:\WINDOWS\system32>
    ```
- 简单软件[[CRUD]]：`scoop install`, `scoop uninstall`