import logging
import os

# Ensure the logs directory exists
os.makedirs("logs", exist_ok=True)

# Configure logging settings
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    handlers=[
        logging.FileHandler("logs/backend.log"),  # Save logs to logs/ folder
        logging.StreamHandler()  # Print logs to the console
    ]
)

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info("Logger is set up correctly!")
