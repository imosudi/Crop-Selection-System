import config 
from app import app

import os, time, platform
import sys



if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=config.PORT,debug=config.DEBUG, host=config.HOST)