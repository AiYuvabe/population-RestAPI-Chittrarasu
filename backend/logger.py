import logging

# Configure logging settings
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    handlers=[
        logging.FileHandler("backend.log"),  # Save logs to a file
        logging.StreamHandler()  # Print logs to the console
    ]
)

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info("Logger is set up correctly!")
