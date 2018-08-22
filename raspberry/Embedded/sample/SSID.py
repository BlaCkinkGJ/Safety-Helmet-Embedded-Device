import subprocess


def getSSID():
    args = ['/sbin/iwgetid', '-r']
    proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    (output, dummy) = proc.communicate()
    return output
