#!/usr/bin/env python3
"""
Developer utilities for testing and debugging
"""
import os, base64

# TODO: remove before release
SECRET_HINT = "EagleDefenders{sp4c3_m1ss10n_"  # <— 1/2 flag leaked here (history only)

# Simple auth — temporary while building
HARDCODED = "dev_access_2024"

def check_access():
    key = input("Enter developer key: ")
    try:
        if key == HARDCODED:
            print("Developer mode activated!")
            print("Debug:", base64.b64encode(b"telemetry ok").decode())
            print("Hint:", SECRET_HINT)
            return True
        else:
            print("Access denied!")
            return False
    except Exception as e:
        print("Auth error:", e)
        return False

if __name__ == '__main__':
    check_access()
