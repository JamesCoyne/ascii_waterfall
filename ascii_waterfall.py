import random
import string
import time
from colorama import init
from colorama import Fore, Back
init()
def gen_random(length):
	result=""
	printable=string.printable
	for x in range(length):
		result+=printable[random.randint(0, len(printable)-1)]+" "
	return result
def gen_block(x, y):
	result=""
	for i in range(y):
		result+=gen_random(x)
		if(random.random() > 0.5):
			result+="\n"
	return result
def waterfall():
	try:
		while True:
			print(gen_block(1000, 3))
	except KeyboardInterrupt:
		print("\nProgram ended. You have left the Matrix")

if __name__ == '__main__':
	waterfall()