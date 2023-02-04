sudo apt update
curl get.docker.com | sh
sudo usermod -aG docker $USER
newgrp docker
sudo apt install docker-compose