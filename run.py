import time
import math
import subprocess
while True:
    seconds = time.time()
    if math.ceil(seconds) % 150 == 0:
        subprocess.run(["python", "main.py"])