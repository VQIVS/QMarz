import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

# Set urllib3 logging level to WARNING to suppress detailed request logs
logging.getLogger("urllib3").setLevel(logging.WARNING)

app_logger = logging.getLogger("app_logger")

def get_logger(name):
    return logging.getLogger(name)
