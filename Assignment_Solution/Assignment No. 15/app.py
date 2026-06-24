import sys
from datetime import datetime

def main():
    print(f"Python Version: {sys.version}")
    print(f"Current Date and Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()