import subprocess
try:
    subprocess.check_output(["sudo", "docker"], shell= True)
except subprocess.CalledProcessError:
    print("error occured")
else:
    print("No error occured")