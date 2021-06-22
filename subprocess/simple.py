import subprocess
from subprocess import Popen, PIPE

subprocess.run(["ls", "-l"], shell=True,encoding="utf-8",timeout=1, check=True) # check 檢查 return 是否 0

with Popen(["ls"], stdout=PIPE) as proc:
    print(proc.stdout.read(), proc.returncode)

print( subprocess.check_output("ls", stderr=subprocess.STDOUT, shell=True) )

subp = Popen("ls", shell=True, stdout=PIPE, stderr=PIPE, cwd=".", encoding="utf-8")
subp.wait(2) # wait until 'ls' finish
if subp.poll() == 0:
    print(subp.communicate()[0])
else:
    print("failed")

subp = Popen(['ls'], shell=True, stdout=PIPE, stderr=PIPE, encoding="utf-8")
subp.wait(2) # wait until 'ls' finish
if subp.poll() == 0:
    print(subp.communicate()[0])
else:
    print("failed")

try:
    subprocess.run(['sleep', '10'], timeout=1, shell=False)
except subprocess.TimeoutExpired:
    print("Timeout")
    
