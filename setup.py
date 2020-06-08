# Create python3
# 
import urllib.request  as urllib2 
import re
import sys,os
import subprocess
import random

os.system("xdg-open https://www.youtube.com/channel/UCmiZfr9dgRCkwHa_GXSa97A/")

H = '\033[95m'
B = '\033[94m'
G = '\033[92m'
W = '\033[93m'
F = '\033[91m'
E = '\033[0m'
U = '\033[4m'
O = '\033[33m'
BAR = "\033[41m"
cb = "\33[34m"
cy = "\33[33m"

def head():
    os.system('clear')
def a():
	os.system('clear')
	os.system(H+'''apt update -y && apt upgrade -y'''+H)
	os.system('clear')
	soal = input("The SQLMap installation will begin, continued [y/n] ?")
	if soal == 'y':
	    os.system('pkg install sqlmap')
	else :
	    os.system('clear')
	print('Im Sadewa, dont forget to follow My Facebook Sadewa Dewa')
	print('See you next time, Bye.')
	z()	
def b():
	os.system('clear')
	os.system(H+'''apt update -y && apt upgrade -y && apt install git -y'''+H)
	os.system('clear')
	soal = input("The SQLMap installation will begin, continued [y/n] ?")
	if soal == 'y':
	    os.system('git clone https://github.com/sqlmapproject/sqlmap && mv sqlmap /data/data/com.termux/files/usr/opt/ && rm -rf sqlmap')
	else :
	    os.system('clear')
	print('CTRL + C')
	print('Copy Paste this code : ')
	
def z():
    os.system('clear')
    os.system('exit')
def solution():
    os.system("xdg-open https://www.youtube.com/")
	
def Main_Menu():
	print(E+H+'''
╔═════════════════════════════════════╗
║ '''+B+'''╔═╗╔═╗ ╦  ╦┌┐┌┌─┐┌┬┐┌─┐┬  ┬  ┌─┐┬─┐'''+E+H+''' ║
║ '''+B+'''╚═╗║═╬╗║  ║│││└─┐ │ ├─┤│  │  ├┤ ├┬┘'''+E+H+''' ║
║ '''+B+'''╚═╝╚═╝╚╩═╝╩┘└┘└─┘ ┴ ┴ ┴┴─┘┴─┘└─┘┴└─'''+E+H+''' ║
║         '''+cb+'''Coded BY Sarc'''+E+H+'''          ╔════╝
║ ═══════════ '''+cy+'''v 1.0'''+H+''' ════════════ ║ '''+BAR+G+'''SARC'''+H+'''
'''+H+'''║'''+E+''' YouTube   : MR WH5'''+E+H+'''             ╚════╗'''+E+H+'''
║'''+H+E+''' Facebook  : Sadewa Dewa'''+E+H+'''             ║'''+E+H+'''
║'''+H+E+''' Instagram : @sadewa_sarc'''+E+H+'''            ║'''+E+H+'''
║ ══════════ '''+cy+'''SOSMED'''+H+''' ═════════════════ ║'''+E+H+'''
║'''+H+F+''' Select your versi android :'''+E+H+'''         ║
║'''+G+''' 1]'''+W+''' Android 7.0+'''+E+H+'''                     ║
║'''+G+''' 2]'''+W+''' Android 5.0 - 6.0'''+E+H+'''                ║
║                                     ║
╚════════════ '''+cy+'''MR WH5'''+E+H+''' ═════════════════╝
	'''+E)
	try:
		v = input('Type according to number ⫸ ')
	except:
		print(' Good by Bro ')
		exit()
	
	if v == '':
		solution()
	elif int(v) == 0:
		z()
	elif int(v) == 1:
		a()
	elif int(v) == 2:
		b()
	else:
		print(F+'[!]'+' Sorry Bro, Invalid input '+E)
		os.system('clear')
		os.system('python setup.py')
head()
Main_Menu()