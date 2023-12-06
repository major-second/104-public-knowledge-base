- [[shell-type]]
  - [[interactive-terminal]] [[shrc]]
  - 但其它的不自动
- If you want to ensure that certain scripts are sourced both in interactive and non-interactive shells, you can add the source commands to ~/.bash_profile or ~/.bash_login (for login shells), or ~/.bashrc (for non-login shells). However, as mentioned earlier, ~/.bashrc is typically not sourced in non-interactive shells.
- A common practice is to put environment variable definitions, function definitions, and other settings that should apply to both interactive and non-interactive shells in a separate file, such as ~/.bash_env. You can then source this file from both ~/.bash_profile and ~/.bashrc: