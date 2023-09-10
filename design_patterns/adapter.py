# Legacy Logger (Old Interface)
class LegacyLogger:
    def log(self, message):
        print(f"Legacy Logger: {message}")

# Modern Logger (New Interface)
from abc import abstractmethod
import logging

class ModernLogger:
    def log_message(self, message):
        logging.info(f"Modern Logger: {message}")

# Adapter to make the Legacy Logger work with Modern Logger
class LegacyLoggerAdapter(ModernLogger):
    def __init__(self, legacy_logger):
        self.legacy_logger = legacy_logger

    def log_message(self, message):
        adapted_message = f"Adapted: {message}"
        self.legacy_logger.log(adapted_message)

# Usage
legacy_logger = LegacyLogger()
modern_logger = ModernLogger()

# Trying to use the Legacy Logger with the Modern Logger's interface (won't work without an adapter)
# modern_logger.log_message("This is a modern log message")  # This would work

# Now, use the adapter to make the Legacy Logger compatible with the Modern Logger
legacy_logger_adapter = LegacyLoggerAdapter(legacy_logger)
legacy_logger_adapter.log_message("This is a legacy log message adapted to modern")

# Now both legacy_logger and modern_logger can be used interchangeably


# MySQL Database Driver
class MySQLDriver:
    def connect(self, host, username, password, database):
        # MySQL-specific connection code
        print("Connected to MySQL")

    def execute_query(self, query):
        # MySQL-specific query execution code
        print("Executing MySQL query:", query)

# PostgreSQL Database Driver
class PostgreSQLDriver:
    def connect(self, host, username, password, database):
        # PostgreSQL-specific connection code
        print("Connected to PostgreSQL")

    def execute_query(self, query):
        # PostgreSQL-specific query execution code
        print("Executing PostgreSQL query:", query)

# Database Adapter Interface
class DatabaseAdapter:
    def __init__(self, driver):
        self.driver = driver

    @abstractmethod
    def connect(self, config):
        pass
    
    @abstractmethod
    def execute_query(self, query):
        pass

# MySQL Adapter
class MySQLAdapter(DatabaseAdapter):
    def connect(self, config):
        host, username, password, database = config
        self.driver.connect(host, username, password, database)

    def execute_query(self, query):
        self.driver.execute_query(query)

# PostgreSQL Adapter
class PostgreSQLAdapter(DatabaseAdapter):
    def connect(self, config):
        host, username, password, database = config
        self.driver.connect(host, username, password, database)

    def execute_query(self, query):
        self.driver.execute_query(query)

# Usage
mysql_driver = MySQLDriver()
postgresql_driver = PostgreSQLDriver()

mysql_adapter = MySQLAdapter(mysql_driver)
postgresql_adapter = PostgreSQLAdapter(postgresql_driver)

mysql_config = ("mysql.example.com", "user", "password", "mydb")
postgresql_config = ("postgresql.example.com", "user", "password", "mydb")

mysql_adapter.connect(mysql_config)
mysql_adapter.execute_query("SELECT * FROM users")

postgresql_adapter.connect(postgresql_config)
postgresql_adapter.execute_query("SELECT * FROM customers")
