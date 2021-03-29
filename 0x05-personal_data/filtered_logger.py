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
        filter the log message
        """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """
    Obfuscates a log message

    Args:
        fields:       fields to obfuscate
        redaction:    redaction
        message:      log message to obfuscate
        separator:    a string representing by which character
    Returns:
    -------
        Protected log message
    """
    for field in fields:
        message = re.sub(rf"{field}=.*?{separator}",
                         f"{field}={redaction}{separator}", message)
    return message
