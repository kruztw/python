# 參考 : https://cuiqingcai.com/8947.html

import os
from environs import Env

os.environ["VAR1"] = "1"             # must be string
print(os.environ['PWD'])             # error if not exist
print(os.environ.get('VAR1'))        # none  if not exist
print(os.getenv('VAR1', 'default'))
print(int(os.getenv('VAR1', 1)))     # type: int   (no good)


env = Env()
env.read_env()                       # read .env file, if it exists
print(env("PWD"))

print(env.int("VAR1"))               # type: int (good)
print(env.bool("VAR2", False))

