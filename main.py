import config 
from app import app


if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=config.PORT,debug=config.DEBUG, host=config.HOST)