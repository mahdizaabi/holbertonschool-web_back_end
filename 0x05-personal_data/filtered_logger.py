#!/usr/bin/env python3
"""
0. Regex-ing
"""

import re
import logging
from typing import List


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """ returns the log message obfuscated """

    for field in fields:
        message = re.sub(
            '(?<={:s}=)[^;]*'.format(field), redaction, message, 1)
    return re.sub(";", separator, message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        NotImplementedError

        formatted = logging.Formatter(self.FORMAT).format(record)
        return filter_datum(self.fields, self.__class__.REDACTION, formatted, self.__class__.SEPARATOR)
