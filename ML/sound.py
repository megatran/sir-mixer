import subprocess, os, sys
import threading

def my_process():
    a1 = "arecord -D plughw:1,0 -f cd -d 5 test.wav Recording WAVE 'test.wav'"
    subprocess.call(a1,shell= True)
thread = threading.Thread(target=my_process)
thread.start()
print("Audio record is only for 10sec")
