import logging

logging.basicConfig(
    filename= "app.log",
    level = logging.WARNING,
    format= "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logging.debug("this wont show - below INFO level")
logging.info("server started")
logging.warning("disk space low")
logging.error("failed to connect to DB")

