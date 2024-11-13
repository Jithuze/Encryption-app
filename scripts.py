import subprocess

try:
    subprocess.run("anydesk", shell=True, check=True)
    subprocess.run("playit", shell=True, check=True)
except subprocess.CalledProcessError as e:
    print(f"Error executing Startup command: {e}")