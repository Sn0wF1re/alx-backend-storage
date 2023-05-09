#!/usr/bin/env python3
"""
Write a Python script that provides some stats
about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


def log_stats():
    """provides some stats about Nginx logs stored in MongoDB"""
    client = MongoClient()
    nginx = client.logs.nginx

    print(f"{nginx.count_documents({})} logs")

    print("Methods:")

    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = nginx.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))
    count = nginx.count_documents({"method": "GET", "path": "/status"})
    print(f"{count} status check")


if __name__ == "__main__":
    log_stats()
