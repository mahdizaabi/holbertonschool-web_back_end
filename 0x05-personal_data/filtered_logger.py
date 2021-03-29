#!/usr/bin/env python3
"""
Module for filtered_logger
0x05-personal_data
Holberton Web Stack programming Spec ― Back-end
"""

import re
import logging
import os
from typing import List
import mysql.connector

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """
        Method that filters values in incoming log records using `filter_datum`
        """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """
    Obfuscates a message according to PII fields
    Args:
        fields:       fields to obfuscate
        redaction:    represents by what the field will be obfuscated
        message:      the log line
        separator:    string by which character is separating all fields
                      in the log line (message)
    Returns:
    -------
        obfuscated log message
    """
    for field in fields:
        message = re.sub(rf"{field}=.*?{separator}",
                         f"{field}={redaction}{separator}", message)
    return message


def get_logger() -> logging.Logger:
    """[Function that create a Logger]

    Returns:
        [logging.logger]: [a Logger that only log up to logging.INFO level
                            it has a streamHandler with a customised formatter]
    """

    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    logStreamHandler = logging.StreamHandler()
    logStreamHandler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(logStreamHandler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """[Function that create a MySQLConnection object ]

    Returns:
        mysql.connector.connection.MySQLConnection: [db object connector]
    """

    dbName = os.environ.get("PERSONAL_DATA_DB_NAME")
    dbUserName = os.environ.get("PERSONAL_DATA_DB_USERNAME")
    dbUserPassword = os.environ.get("PERSONAL_DATA_DB_PASSWORD")
    dbHost = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")

    dbConnector = mysql.connector.connect(user=dbUserName, password=dbUserPassword,
                                          host=dbHost,
                                          database=dbName)
    dbConnector.close()
    return dbConnector
