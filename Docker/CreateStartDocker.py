#!/usr/bin/python3
"""
__author__     = "Blaze Sanders"
__email__      = "dev@blazesanders.com"
__copyright__  = "Copyright 2024"
__license__    = "MIT License"
__status__     = "Development"
__deprecated__ = "False"
__version__    = "0.0.1"
"""
# Create a Docker image and then start a container running a compiled C file on a Red Hawk real-time Linux distro
# https://concurrent-rt.com/wp-content/uploads/2023/06/Creating-and-Running-Docker-Containers-on-RedHawk-Linux-Systems_rev4-1-1-1.pdf

## Standard Library
# Allow BASH commands to be run inside python code like this file
# https://docs.python.org/3/library/subprocess.html
#TODO REMOVE? from subprocess import Popen, PIPE
import subprocess
from subprocess import Popen, PIPE
from subprocess import check_call

# Determine which OS this code is running
# https://docs.python.org/3/library/sys.html
import sys

# TODO
from time import sleep


def create_file_structure(mainFilename: str='test.c'):
    """ Create the needed Docker folders and files needed to create an Docker image and container

    Arg(s):
        mailFilename (String): .c or .py file that will be the main() driver for code base
    """
    check_call("mkdir DockerBuild", shell=True)
    check_call("cd DockerBuild", shell=True)

    #TODO Check is mainFilename ends in .c
    check_call(f"nano {mainFilename}", shell=True)


def gcc_compile(exeName: str, mainFilename: str='test.c'):
    #TODO Check is mainFilename ends in .c
    check_call(f"gcc -o {exeName} -static {mainFilename}")    # gcc -o hello -static hello.c


def create_docker_file():
    pass
    # nano .dockerignore
    # nano Dockerfile


def build_docker_image():
    pass
    # sudo docker build -t hello-redhawk:latest ~/DockerBuild
    # sudo docker images
    # sudo docker container create -i -t --name TestContainer hello-redhawk
    # sudo docker ps -a

def start_docker_container():
    pass
    # sudo docker container start --attach -i TestContainer


if __name__ == "__main__":
    print("Starting software install inside CURRENT directory / folder in a virtual enviroment (venv) and performing system updates!")
    print("Press CTRL-Z now to cancel install and system updates")
    for countdown in range(10, 0, -1):
        print(countdown)
        sleep(1)
    print("LIFTOFF!")

    cCode = False
    pythonCode = False
    #TODO input()
    if cCode:
        check_call("sudo apt install gcc", shell=False)

    elif pythonCode:
        pass
    else:
        print("Installing both gcc and python3 to run your Docker container code")
        check_call("python3 -m venv .venv", shell=False)
        check_call("source .venv/bin/activate", shell=False)


    check_call("clear", shell=True)
    if sys.platform.startswith('darwin'):
        pass
    elif sys.platform.startswith('linux'):
        # Check and update your system
        check_call("sudo apt update", shell=True)
        check_call("sudo apt upgrade", shell=True)

        # Install Docker if not already installed
        check_call("sudo apt install docker.io", shell=True)
        check_call("sudo snap install docker", shell=True)

        create_file_structure()

    elif sys.platform.startswith('win'):
        print("FUCK OFF and stop using  Windows OS for software delevopment :)")
    else:
        print("ERROR: Running on an unknown operating system")
        quit()
