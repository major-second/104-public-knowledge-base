- In the context of Bash scripting, the `&` operator and the `wait` command are powerful tools for managing background processes.
  - Bash Manual on Job Control: [GNU.org](https://www.gnu.org/software/bash/manual/html_node/Job-Control-Basics.html)
  - https://linuxize.com/post/bash-wait/
- Ref
  - [[async-programming]]
# demos
- Using `&` for Background Execution
  - ```shell
    # Start a process in the background
    sleep 1 &
    # Print the process ID of the last background process started
    echo $!
    ```
- Using `wait` for [[blocking-run]]
  - ```shell
    # Start a process in the background
    sleep 1 &
    # Store the process ID of the last background process started
    pid=$!
    # Wait for the process to complete
    wait $pid
    # Print a message after the process completes
    echo "Process $pid has completed."
    ```
- Using `wait` without an argument
  - ```shell
    # Start multiple processes in the background
    sleep 2 &
    sleep 1 &
    # Wait for all background processes to complete
    wait
    # Print a message after all processes complete
    echo "All processes have completed."
    ```