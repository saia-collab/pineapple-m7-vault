#!/usr/bin/env python3
import subprocess
import sys

try:
    subprocess.run([sys.executable, "-m", "litellm.proxy.main", "--config", "./config.yaml"], check=True)
except Exception as e:
    print(f"Error: {e}")
    print("Trying alternative method...")
    from litellm import Router, mock_completion
    from litellm.proxy.main import start_proxy
    start_proxy(config_file="./config.yaml")
