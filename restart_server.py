#!/usr/bin/python3
import requests
import subprocess
import sys


def stop_server():
    subprocess.run(["pkill", "python3"], capture_output=False)


def run_server(uri):
    try:
        res = subprocess.run(["python3", "-m", f"{uri}"],
                             text=True, capture_output=False)
    except KeyboardInterrupt:
        print()
        stop_server()

if len(sys.argv) == 1:
    print(f"usage: {sys.argv[0]} ['web'|'app']")
    sys.exit(1)

if sys.argv[1] == "api":
   uri = "api.v1.app"
elif sys.argv[1] == "web":
   uri = "web_dynamic.0-hbnb"
else:
    print(f"usage: {sys.argv[0]} ['web'|'app']")
    sys.exit(1)


try:
    # response = requests.get("http://0.0.0.0:5000/api/v1/states")
    stop_server()
    run_server(uri)
except requests.ConnectionError:
    run_server(uri)
    sys.exit(0)
