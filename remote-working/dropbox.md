# Basics
- Prerequisites
  - [[curl-wget]]
  - [[CLI]]
  - [[net-disk]]
- Dropbox is a commonly used, reasonably priced, mainstream cloud storage service with a mature and user-friendly [[CLI]]
  - [[pricing]]
- Official website: https://dropbox.com

# Usage
## Sync Folder
- [[CLI]] [documentation](https://help.dropbox.com/installs/linux-commands)
  - Note: When downloading from [this link](https://linux.dropboxstatic.com/packages/ubuntu/), maybe you should avoid some later versions as it may not be compatible with [[apt]].
    - [[general-software-technical/upgrade]], [[compatibility]]
  - Installation: Use `wget ...` to download the .deb file, then use `sudo apt update`, `sudo apt install ./<filename>.deb` to install the .deb file.
    - [[deb]]
  - Run `dropbox start -i` to install Dropbox.
  - Run `dropbox start` to start Dropbox (you may need to perform some operations to connect your account).
- then `~/Dropbox` is the default sync directory.
- Exclude (`dropbox exclude`) operations ([[CRUD]]):
  - `dropbox exclude`
  - `dropbox exclude add`
    - Common scenario: If you want to upload files without occupying local space, use `dropbox exclude add`.
  - `dropbox exclude remove`
  - Note: Using `*` here matches (all the contents that the local `ls` command and `*` can match), not only the `dropbox exclude`-ed part.
    - Example: Suppose you have two files named `1` and `2` in your current directory, and in your Dropbox exclude list, you have files named `3` and `4`. If you want to remove all the files from the Dropbox exclude list (i.e., `3` and `4`), you might be tempted to use a wildcard (`*`) to match all files. However, the wildcard will actually match the results of the `ls` command in your current directory (i.e., `1` and `2`), not the files in the Dropbox exclude list. Therefore, to remove files `3` and `4` from the Dropbox exclude list, you should specify them explicitly in the `dropbox exclude remove` command, like so: `dropbox exclude remove 3`.
    - [[shell-expansion]]
## Raw content download
- To generate a raw content sharing link, follow these steps:
  - Right-click on the file in your Dropbox account.
  - Click on 'Share'.
  - Click on 'Create a link'.
  - Once the link is created, click on 'Copy link'.
- The copied link will lead to a preview page. To make it a direct download link
  - replace the `www.dropbox` at the beginning of the URL with `dl.dropboxusercontent`.
  - delete `&dl=x` at the end
- This is similar to [[github-raw]], where you can directly download a single file without needing a client [[git-installation]].
  - For folders, you can't create such links directly
  - but, [[zip-unzip]]
- [Reference](https://www.dropboxforum.com/t5/Create-upload-and-share/public-links-to-raw-files/td-p/110391)
  - > A share link with "www" at the beginning will open in the preview page.
  - > A share link with "dl" at the beginning will tell your browser to handle the file as it sees fit (display in the browser, open in a configured application, or present it for download).
  - > A share link with "dl" at the beginning and "?dl=1" at the end will force your browser to download the file.