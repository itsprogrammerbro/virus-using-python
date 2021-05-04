import subprocess
from time import sleep
while True:
    subprocess.Popen('notepad') #use artificial multithreading
    subprocess.Popen('calc')  #use artificial multithreading
    subprocess.Popen('mspaint')  #use artificial multithreading
    subprocess.Popen('explorer')  #use artificial multithreading
    subprocess.Popen('write')  #use artificial multithreading
    sleep(.05)




