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
