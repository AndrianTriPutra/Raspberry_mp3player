#python2
#mp3player.py
#created by gondril

import os
import subprocess
import RPi.GPIO as GPIO
import time
import datetime
import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

#declare input pushbutton
PB_PLAY=21
PB_STOP=26
PB_UP=16
PB_DOWN=20

# Raspberry Pi hardware SPI config:
DC = 23
RST = 24
SPI_PORT = 0
SPI_DEVICE = 0

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


GPIO.setup(PB_PLAY,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(PB_STOP,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(PB_UP,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(PB_DOWN,GPIO.IN,pull_up_down=GPIO.PUD_UP)

i=0
playlist=['Terpukau.mp3','Oasis.mp3','AkuBisa.mp3']

##################### SCREEN #####################
################## picture  #####################
def picture():
	# Hardware SPI usage:
	disp = LCD.PCD8544(DC, RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=4000000))

	# Initialize library.
	disp.begin(contrast=60)

	# Clear display.
	disp.clear()
	disp.display()

	# Create blank image for drawing.
	# Make sure to create image with mode '1' for 1-bit color.
	image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))

	# Get drawing object to draw on image.
	draw = ImageDraw.Draw(image)
		
	#part picture
	image = Image.open('LogoIP_2.png').convert('1')

	# Display image.
	disp.image(image)
	disp.display()
################## picture  #####################

################## Text  #####################
def Text(jam,date,data):
	# Hardware SPI usage:
	disp = LCD.PCD8544(DC, RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=4000000))

	# Initialize library.
	disp.begin(contrast=60)

	# Clear display.
	disp.clear()
	disp.display()

	# Create blank image for drawing.
	# Make sure to create image with mode '1' for 1-bit color.
	image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))

	# Get drawing object to draw on image.
	draw = ImageDraw.Draw(image)

	# Draw a white filled box to clear the image.
	draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)

	# Load default font.
	font = ImageFont.load_default()
			
	# Write some text.	
	draw.text((0,0),'{}'.format(jam),font=font)#Line 1
	draw.text((0,10),'{}'.format(date),font=font)#Line 2			
	draw.text((0,25),'Pilih Lagu:',font=font)#Line 4
	draw.text((0,35),'{}'.format(data),font=font)#Line 5

	# Display image.
	disp.clear()
	disp.image(image)
	disp.display()						
################## Text  #####################	
##################### SCREEN #####################
picture()
time.sleep(2);

#Text(playlist[i])



try:
	while True:
		IN_PLAY = GPIO.input(PB_PLAY)
		IN_STOP = GPIO.input(PB_STOP)
		IN_UP = GPIO.input(PB_UP)
		IN_DOWN = GPIO.input(PB_DOWN)
		waktu = datetime.datetime.now()
		jam  = (waktu.strftime("%H:%M:%S"))	
		date = (waktu.strftime("%d/%m/%Y"))
		Text(jam,date,playlist[i])	
		time.sleep(0.5)
		if IN_UP == False:#arah atas for pilih lagu			
			i+=1
			if i>=3:
				i=0									
		if IN_DOWN == False:#arah bawah for pilih lagu						
			if i==0:
				i=2
			else :
				i-=1
		if IN_PLAY == False:#for play lagu
			subprocess.call(['killall', 'mpg123'])#for kill all			
			subprocess.Popen(['mpg123',playlist[i]])#for play			
		if IN_STOP == False:#for stop lagu	
			subprocess.call(['killall', 'mpg123'])#for kill all	
except KeyboardInterrupt:
	pass
GPIO.cleanup()





