ip=`ifconfig | grep 'inet\s' | grep -v '127.0' | awk '{print $2}'`
tmp_file=~/tmp.sh
echo "echo $ip" > $tmp_file
tail -n 1 $tmp_file
bash $tmp_file
rm $tmp_file
echo "I can use \`, ' and \" here"