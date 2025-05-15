import config 
from app import app

import os, time, platform
import sys


py_vers = (".").join(platform.python_version().split(".")[:2])
dir_path = os.path.dirname(os.path.realpath(__file__)).strip("app")
python_path = os.path.join(dir_path, f"venv/lib/python{py_vers}/site-packages")

print(py_vers, dir_path, python_path)

#sys.path.insert(0, 'venv/lib/python3.8/site-packages')
#sys.path.insert(0, f'{dir_path}')
sys.path.insert(0, f'{python_path}')

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=config.PORT,debug=config.DEBUG, host=config.HOST)