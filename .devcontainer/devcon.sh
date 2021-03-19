# install python libs
pip3 install --user -r docker/requirements.txt

SSH_FOLDER="$PWD/SSH"
SRC_FOLDER="$PWD/src"
KEY_FILE=~/.ssh/id_rsa
KEY_PRO_FILE="$PWD/SSH/id_rsa"


if ! test -d "${SSH_FOLDER}"; then
    mkdir "${SSH_FOLDER}"
fi

# load SSH keys
apt install -y openssh-server
if test -f "${KEY_PRO_FILE}"; then
    # key already exist
    cp "$KEY_PRO_FILE" "${KEY_FILE}"
    echo "there is already a key"
else
    # key is needed to creat
    ssh-keygen -f "${KEY_FILE}"
    cp "${KEY_FILE}.pub" "$KEY_PRO_FILE.pub"
    cp "${KEY_FILE}" "$KEY_PRO_FILE"
    echo -e "\nyou have generated an key for SSH. the public key need to be on your remote machine"
fi
chmod 600 "${KEY_FILE}"

eval "$(ssh-agent -s)"
ssh-add

# add remote context
docker context create remote --docker "host=ssh://ubuntu@192.168.178.7"

# add for testing
chmod +x "$PWD/src/tests/runTests.sh"
# install packages
pip install -e "${SRC_FOLDER}"
pip install -e "${SRC_FOLDER}/pyserver/"

# delete .egg
find ${SRC_FOLDER} | grep  .egg | xargs rm -fr