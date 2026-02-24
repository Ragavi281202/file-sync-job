import requests
import logging

logger = logging.getLogger(__name__)

def run(config: dict) -> bool:
    try:
        logger.info("Running File Sync Job")
        logger.info("Requests version: %s", requests.__version__)

        file_name = config.get("file_name")
        directory = config.get("directory", "/tmp")

        if not file_name:
            raise ValueError("file_name is required")

        full_path = f"{directory}/{file_name}"

        with open(full_path, "w") as f:
            f.write("Hello from File Sync Job")

        logger.info("File created at: %s", full_path)

        return True

    except Exception as e:
        logger.error("Error occurred: %s", str(e))
        return False
