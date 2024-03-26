import os

#the sys module is essential for tasks related to interacting with the Python interpreter, 
# accessing system-specific information, and managing script execution
import sys
import logging

# This variable defines the format of log messages "logging_str"
# %(asctime)s for the timestamp, %(levelname)s for the log level, 
# %(module)s for the module name, and %(message)s for the log message itself.
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# log_dir variable specifies the directory where log files will be stored.
log_dir = "logs"

log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level= logging.INFO,
    format= logging_str,
    handlers = [
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
    
)

logger = logging.getLogger("textSummarierLogger")