
import os
from datetime import datetime
import logging

#LOG_FILE=f"{datetime.now()}.log"
LOG_FILE=f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
log_path=os.path.join(os.getcwd(),"logs")
os.makedirs(log_path,exist_ok=True)
LOG_FILEPATH=os.path.join(log_path,LOG_FILE)

logging.basicConfig(level=logging.INFO,filename=LOG_FILEPATH,
                format="[%(asctime)s]   %(lineno)d  %(name)s - %(levelname)s  %(message)s")




if __name__=="__main__":
    logging.info("i am testing")