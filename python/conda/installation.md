Go to Anaconda's official website "https://www.anaconda.com/" and copy the link of "download for linux"
And input 
```sh
bash Anaconda3-5.0.1-Linux-x86_64.sh
```
in the terminal.
After that，we 'll change the configure for anaconda.
Add the install path to .bashrc 
```sh
export PATH=$PATH:your anaconda path` and run`source ~/.bashrc
```
to make the change activate.
Then we can run
```sh 
conda --version
```
to check.
