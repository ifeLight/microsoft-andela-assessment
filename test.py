from subprocess import check_output, CalledProcessError
import sys
try:
    numbers = check_output(["dockerss"])
    print (" succeeded,  succe")
except CalledProcessError as e:
    sys.exit(" failed, returned c")
except OSError as e:
    sys.exit("failed to execu")