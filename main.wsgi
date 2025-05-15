
#!/usr/bin/python3

import os
import sys

# Add the site-packages of the virtual environment
site.addsitedir('/home/mosud/dev/agroselect/Crop-Selection-System/venv/lib/python3.12/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.insert(0, '/home/mosud/dev/agroselect/Crop-Selection-System')

from app import app as application