import subprocess
import os
import zipfile
import urllib.request
import shutil

u = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
z = "ffmpeg.zip"
t = "ffmpeggers"
p = "C:\\ffmpeg"

urllib.request.urlretrieve(u, z)
with zipfile.ZipFile(z, 'r') as f:
    f.extractall(t)

e = os.path.join(t, os.listdir(t)[0])
if os.path.exists(p):
    shutil.rmtree(p)
shutil.move(e, p)

b = os.path.join(p, "bin")

c = subprocess.run(['powershell', '-Command', '[Environment]::GetEnvironmentVariable("Path", "User")'], capture_output=True, text=True).stdout.strip()
n = f"{b};{c}"
subprocess.run(['powershell', '-Command', f'[Environment]::SetEnvironmentVariable("Path", "{n}", "User")'], shell=True)

os.remove(z)
shutil.rmtree(t)

print("done")
