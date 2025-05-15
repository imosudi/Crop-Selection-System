
#!/usr/bin/python3

import os
import sys

# Add your project directory to the path
project_home = '/home/mosud/dev/agroselect/Crop-Selection-System'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Activate virtual environment
activate_this = os.path.join(project_home, 'venv/bin/activate_this.py')
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

from app import app as application