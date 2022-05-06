1.首先`git clone https://github.com/EGO4D/forecasting.git`这是forecasting的代码<br />
2.创建虚拟环境`conda create -n ego4d_forecasting python=3.7`<br />
3.`conda activate ego4d_forecasting`<br />
4.install requerements`cat requirements.txt | xargs -n 1 -L 1 pip install`，这一步要先翻墙<br />
5.为了让ego4d模块可以被加载，运行`export PYTHONPATH=$PWD:$PYTHONPATH`<br />
6.下载ego4d数据集和pretrained models，可以直接scp过来，在212的位置是`/raid/wuruihai/forecasting/data/long_term_anticipation/`，在16的位置是`/DATA/disk1/ego4d/long_term_anticipation/`<br />
7.新创建data文件夹并链接数据集和预训练模型过来
```sh
mkdir -p data/long_term_anticipation/annotations/ data/long_term_anticipation/clips_hq/
ln -s ${EGO4D_DIR}/v1/annotations/* data/long_term_anticipation/annotations/
ln -s ${EGO4D_DIR}/v1/clips/* data/long_term_anticipation/clips_hq/

mkdir -p pretrained_models
ln -s ${EGO4D_DIR}/v1/lta_models/* pretrained_models/
```
8.配置slurm.conf文件，具体操作如下面步骤所示<br />
9.换源`echo "deb http://archive.ubuntu.com/ubuntu bionic universe" | sudo tee -a /etc/apt/sources.list`<br />
10.`sudo apt update`<br />
11.安装slurm-wlm`sudo apt install slurm-wlm -y`<br />
12.安装文档目录，这个可以让它自己生成slurm.conf，当然也可以不用它自己生成，可选`sudo apt install slurm-wlm-doc -y`<br />
13.可以在`/usr/share/doc/slurm-wlm-doc/html/configurator.easy.html`里填写主机的信息然后点submit自动生成，其中可以用`slurmd -C`查看本机信息<br />
14.前两步可以不要，直接复制如下字段到`/etc/slurm-llnl/slurm.conf`里面
```conf
# instant slurm file, automatically generated
ClusterName=91fbdd9cdc6a40249207e96893677118
ControlMachine=localhost
SlurmdUser=root
SlurmctldPort=6817
SlurmdPort=6818
StateSaveLocation=/var/lib/slurm
SlurmdSpoolDir=/var/spool/slurm
SwitchType=switch/none
MpiDefault=none
SlurmctldPidFile=/var/run/slurmctld.pid
SlurmdPidFile=/var/run/slurmd.pid
ProctrackType=proctrack/pgid
SlurmctldTimeout=300
SlurmdTimeout=300
InactiveLimit=0
MinJobAge=300
KillWait=30
Waittime=0
SchedulerType=sched/builtin
FastSchedule=1
SlurmctldDebug=3
SlurmctldLogFile=/var/log/slurmctld.log
SlurmdDebug=3
SlurmdLogFile=/var/log/slurmd.log
JobCompType=jobcomp/none
PropagateResourceLimitsExcept=MEMLOCK
PartitionName=normal Nodes=localhost Default=YES MaxTime=UNLIMITED State=UP
NodeName=localhost Gres=gpu:4 CPUs=40 Boards=1 SocketsPerBoard=1 CoresPerSocket=20 ThreadsPerCore=2 RealMemory=257862
GresTypes=gpu
```
15.在forcasting目录下，运行`sbatch tools/long_term_anticipation/resize_clips.sh`即可，它会把抽好帧的视频存到`data/long_term_anticipation/clips/`里<br />
