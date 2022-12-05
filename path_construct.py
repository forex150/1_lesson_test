import os
import pprint
import sys
import subprocess

print('Это не ошибка',file=sys.stdout)
print('Это ошибка',file=sys.stderr)

#print(sys.argv)

e = subprocess.run(['python','lesson6.py'])
print(e.returncode)
#user = os.environ['USERNAME']
#print("Привет",user)
