#!/usr/bin/env python3
"""
Developer utilities for testing and debugging
"""
import os, base64

# Read from environment now (no more hardcoded secrets)
HARDCODED = None


def check_access():
    key = input("Enter developer key: ")
    env_key = os.getenv("DEV_ACCESS", "")
    try:
        if env_key and key == env_key:
            print("Developer mode activated!")
            print("Debug:", base64.b64encode(b"telemetry ok").decode())
            return True
        else:
            print("Access denied!")
            return False
    except Exception as e:
        print("Auth error:", e)
        return False

if __name__ == '__main__':
    check_access()
}'
