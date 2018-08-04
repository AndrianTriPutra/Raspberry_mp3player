#viasystem.py
#sudo apt-get install mpg321

import os
import RPi.GPIO as GPIO
import time
import subprocess

soundfile='Oasis.mp3'

pushbutton=26

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(pushbutton,GPIO.IN,pull_up_down=GPIO.PUD_UP)

"""
#cara recomended
subprocess.Popen(['mpg123','Oasis.mp3'])#for play
try:
	while True:
		input_state = GPIO.input(pushbutton)
		if input_state == False:
			subprocess.call(['killall', 'mpg123'])#for kill all
except KeyboardInterrupt:
	pass
GPIO.cleanup()
#cara recomended
"""

"""
#ke terminal jadi aneh
player=subprocess.Popen(['mpg123',soundfile])#for play
try:
	while True:
		input_state = GPIO.input(pushbutton)
		if input_state == False:
			player.kill()
except KeyboardInterrupt:
	pass
GPIO.cleanup()
##ke terminal jadi aneh
"""


subprocess.Popen(['mpg123','Terpukau.mp3'])#for play
if __name__ == "__main__":
        while True:
				input_state = GPIO.input(pushbutton)
				if input_state == False:
					subprocess.call(['killall', 'mpg123'])#for kill all

#CATATAN

#jika langsung
#os.system('mpg123 -q Oasis.mp3 &')##for play


#jika subproses
#subprocess.Popen(['mpg123','Oasis.mp3'])#for play
#subprocess.call(['killall', 'mpg123'])#for kill all

#jika pake variabel
#player=subprocess.Popen(['mpg123',soundfile])#for play
#player.kill()#for kill all	
