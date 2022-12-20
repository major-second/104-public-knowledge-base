`awk`, `cut`用来做简单字符串操作，和[[find-grep]], [[sed]]常常一起使用
## 例1
- [[4-more-commands]]中`ppid=$(ps -ef | grep 'sleep 3' | grep -v grep | awk '{print $3}')`
## 例2
- 较复杂，使用了[[find-grep]]以及[[11-basic-scripting-partB]]中`expr`等技术
- 需求：把
```text
python310_numpy-1.23.4
python310_torch-1.12.1
python310_pandas-1.5.2
```
转化为
```text
numpy==1.23.4
torch==1.12.1
pandas==1.5.2
```
- 则
```sh
for module in $(cat modules.txt)
do
    module=$(echo $module | awk -F_ '{print $2}')
    version_index=$(echo $module | grep -bo '[0-9]' | head -n 1 | awk -F: '{print $1}')
    version_index=$(expr $version_index + 1)
    modulename_end_index=$(expr $version_index - 2)
    modulename=$(echo $module | cut -c1-$modulename_end_index)
    version=$(echo $module | cut -c$version_index-)
    module="$modulename==$version"
    echo $module
done
```
- 注意[[algorithm/trivial-mistakes]]的差一问题！`cut`是1开始，左右都包括，而`grep -bo`是0开始