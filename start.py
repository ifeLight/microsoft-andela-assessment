import os, subprocess
import platform

#Check wether docker is installed
docker_installed = False
try:
    docker_status = subprocess.check_output(["docker"])
    docker_installed = True
except subprocess.CalledProcessError:
    sys.exit("Problem running Docker package")
except OSError :
    sys.exit("Docker may not be installed")


# Check Wether Docker-compose is installed
docker_compose_installed = False
try:
    docker_status = subprocess.check_output(["docker"])
    docker_compose_installed = True
except subprocess.CalledProcessError:
    sys.exit("Problem running Docker package")
except OSError:
    sys.exit("Docker-compose may not be installed")


#Advice to install necessary packages
if not docker_compose_installed:
    print("Docker not Installed \n")
    print("Install docker to comtinue set up \n")
if not docker_compose_installed:
    print("Docker-compose not Installed \n")
    print("Install docker-compose to comtinue set up \n")

#Get Operating System
operating_system = platform.system()

# Shell Command to start the application
if docker_compose_installed and docker_installed:
    if (operating_system == "Linux"):
        os.system("sudo docker-compose up")
    else:
        os.system("docker-compose up")


# Run when ended
print("\n-----I F E L I G H T ------- \n")
print("The Server has been Stopped")