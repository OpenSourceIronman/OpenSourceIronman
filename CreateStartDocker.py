mkdir DockerBuild
cd DockerBuild
nano hello.c
sudo apt install gcc
gcc -o hello -static hello.c
nano hello.c
gcc -o hello -static hello.c
nano .dockerignore
nano Dockerfile
sudo docker build -t hello-redhawk:latest ~/DockerBuild
sudo docker images
sudo docker container create -i -t --name TestContainer hello-redhawk
sudo docker ps -a
sudo docker container start --attach -i TestContainer
