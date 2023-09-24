"""
Logging Best Practices:

Use different log levels to distinguish between different types of messages 
(e.g., debugging, informational, warning, error).

Log important events, errors, and exceptions.
Avoid using print() for debugging; prefer logging.

Log important context information, such as function names, module names, or timestamps.
Configure logging to meet your application's requirements, including log rotation and 
log file management.
"""
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)

logger = logging.getLogger('app')

logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')


def main():
    try:
        raise Exception('BIG EXCEPTION')
    except Exception as e:
        logger.error('An exception occurred: %s', str(e), exc_info=True)

if __name__ == "__main__":
    main()
