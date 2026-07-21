import logging
# this is the root logger
logger = logging.getLogger()
formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)
# global level
def setup_logging():
    logger.setLevel(logging.INFO)
    # if u want console(terminal) log then we use 'StreamHandler()'
    console = logging.StreamHandler()
    # if we want logging in a file we use 'FileHandler(filepath)'
    file = logging.FileHandler("logs/agent.log")
    # specifying the level for handlers too
    console.setLevel(logging.INFO)
    file.setLevel(logging.INFO)
    #setting the formatter
    file.setFormatter(formatter)
    console.setFormatter(formatter)
    # adding the handlers
    logger.addHandler(file)
    logger.addHandler(console)