#!/usr/bin/env python3
"""
0x04-pagination
Holberton Web Stack programming Spec ― Back-end
"""
import requests

URL = 'https://holbertonintranet.s3.amazonaws.com/uploads/misc/2019/11/a2e00974ce6b41460425.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210326%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210326T145452Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=36952ee3f35af2eb184cbb09380fe33db1d517cb96e143513b757c756d38abcd'

DATA_FILE = "user_data.csv"


def download_csv(URL: str, FILENAME: str):
    """
    Helper method that downloads csv data from URL
    and saves content in to a file
    """
    req = requests.get(URL)
    content = req.content
    with open(DATA_FILE, 'wb') as csv_file:
        csv_file.write(content)


download_csv(URL, DATA_FILE)
