#!/usr/bin/env python3
"""  Python script that provides some stats about Nginx logs stored in MongoDB:"""
from pymongo import MongoClient

if __name__ == "__main__":
    """  Python script that provides some stats about Nginx logs stored in MongoDB:"""
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    numberOfDocuments = nginx_collection.count_documents({})
    print(f'{numberOfDocuments} logs')
    print('Methods:')
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f'\tmethod {method}: {count}')

    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f'{status_check} status check')
