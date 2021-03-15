# install python libs
pip3 install --user -r docker/requirements.txt

# load SSH keys
apt install -y openssh-server
cp /workspaces/Elastic/SSH/key1 ~/.ssh/key1
cp /workspaces/Elastic/SSH/config ~/.ssh/config 
chmod 600 ~/.ssh/key1

# add remote context
docker context create remote --docker "host=ssh://ubuntu@192.168.178.7"