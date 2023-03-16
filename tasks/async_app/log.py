from loguru import logger

logger.add("mylog.log", format="{time} {level} {message}", level="DEBUG", rotation="100 KB", compression=zip)
