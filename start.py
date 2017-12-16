import os, subprocess
import platform

#Get Operating System
operating_system = platform.system()

# Shell Command to start the application
if (operating_system == "Linux"):
    os.system("sudo docker-compose up")
else:
    os.system("sudo docker-compose up")


# Run when ended
print("-----I F E L I G H T ------- \n")
print("The Server has been Stopped")