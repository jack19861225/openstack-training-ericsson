# 使用Devstack 一些问题的记录

```
安装运行create-stack-user.sh脚本时，当前目录不要是devstack
安装时如果提示pbr版本不对
运行pip install --upgrade pbr, pip install --upgrade setuptools
安装时提示下载超时，可以使用pip install --upgrade安装失败的包
安装时提示提示mysql没权限执行下列命令：
service mysqld stop
mysqld_safe --user=mysql --skip-grant-tables --skip-networking &
mysql -u root mysql
UPDATE user SET Password=PASSWORD() where USER='root';
FLUSH PRIVILEGES;
quit
service mysqld stop
devstack默认卷容量比较小（10G),安装时可以调整（stack用户下导入该环境变量）
export VOLUME_BACKING_FILE_SIZE=102500M
安装openstack需要访问pypi网站，超时失败的话
可以运行./unstack.sh, ./stack.sh解决
系统重启后，需要运行rejoin.sh，运行前需要重新恢复卷组
losetup -f /opt/stack/data/stack-volumes-backing-file
安装完成后发现卷容量较小，可以使用如下方法调整
devstack安装默认lvm后端容量为10G。
后续可以通过以下方式修改：
qemu-img create -f raw 100G
losetup -f
pvcreate
vgextend 
注：vg_name可以通过vgdisplay显示。
安装时pip显示”No module named pkg resources“错误
$ wget http://python-distribute.org/distribute_setup.py
$ python distribute_setup.py
详细参考http://stackoverflow.com/questions/7110360/easy-install-and-pip-doesnt-work
启动虚拟机失败，错误“some rules could not be created for interface vnet0”
原因：
关闭防火墙后没有重新启动libvirtd
解决办法：
重新启动libvirtd
控制节点意外掉电后重启，mysql启动失败，同时导致neutron-server无法启动
rm -rf /var/lib/mysql/mysql.sock然后重启节点
出现错误：failed to create /opt/stack/horizon/openstack_dashboard/local/
解决：执行setenforce 0
关闭devstack的所有screen
解决：screen -wipe

generate-subunit : command not found
sudo apt-get install python-pip

安装目录不能有任何内容

pip 太慢

需要修改成阿里源

root/ 

mkdir ~/.pip
vi pip.conf
[global]
index-url = http://mirrors.aliyun.com/pypi/simple
trusted-host= mirrors.aliyun.com

解决screen Cannot open your terminal
userB在 su - userA以后，执行如下命令即可:
script /dev/null


export OS_TENANT_NAME=admin
export OS_USERNAME=admin
export OS_PASSWORD=123456
export OS_AUTH_URL="http://192.168.6.131:5000/v2.0/"
 
source openrc demo demo
source openrc admin admin
 
```
