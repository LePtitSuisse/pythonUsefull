import time
import re

def getWords(s_text):
	return re.compile('\w+').findall(s_text)

s_text = open('text.txt', 'r').read()
text = getWords(s_text)

speed = int(input("Entre la vitesse de lecture (en WPM): "))

for i in range(0,len(text)):
        print("                                            "+text[i]+"                       ", end="\r")
        time.sleep(60/speed)
