#-*-coding:utf-8-*-
#Modüller
from os import system
import mechanize

#Renkler
bold = "\033[1m"
underline = "\033[4m"
green = "\033[92m"
blue = "\033[94m"
yellow = "\033[93m"
red = "\033[91m"
endcolor = "\033[0m"

sqlerror = ["error in your SQL syntax", "Query failed", "supplied argument is not a valid MySQL result resource in", "You have an error in your SQL syntax",
"ORDER BY", "mysql_num_rows()", "SQL query failed", "Microsoft JET Database Engine error '80040e14'", "Microsoft OLE DB Provider for Oracle",
"Error:unknown", "Fatal error", "mysql_fetch", "Syntax error"]

sqllist = []

#Tarayıcı
browser = mechanize.Browser()
browser.set_handle_robots(False)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)')]

#Fonskyionlar
def logo():
	system("clear")
	print bold+"\t\t\t---------------------------"+endcolor
	print "\t\t\t--==[ Bug Researchers ]==--"
	print "\t\t\t--==[  {}Cyber-Warrior{}  ]==--".format(green, endcolor)
	print "\t\t\t--==[    {}ExitStars{}    ]==--".format(blue, endcolor)
	print bold+"\t\t\t---------------------------"+endcolor

def help():
	print "~~ BugMan | Cyber-Warrior | Bug Researchers  ~~"
	print bold+"Kullanım // Komutlar"+endcolor
	print yellow+"~ quit "+endcolor+" Çıkış"
	print yellow+"~ help "+endcolor+" Yardım Bilgisi"
	print yellow+"~ search sql dork "+endcolor+" Verilen Dork İle SQL Taraması Yapar"
	print yellow+"~ search xss dork "+endcolor+" Verilen Dork İle XSS Taraması Yapar"
	print yellow+"~ generate dork "+endcolor+" Dork Oluşturma Aracı"
	print ""
	print bold+"Yazılım Hakkında"+endcolor
	print "Yazan: ExitStars"
	print "Sürüm: V2"

def sqlhunter(link):
	try:
		site_source_code = browser.open(link+"'").read()
		for error in sqlerror:
			if error in site_source_code:
				print link
				sqllist.append(link)
			else:
				pass
	except:
		pass

def xsshunter():
	pass

def search(dork, bug):
	first = 1
	while first <= 10:
		source_code = browser.open("http://www.bing.com/search?q={}&first={}".format(dork, first)).read()
		for link in browser.links():
			if "http://" in link.url or "https://" in link.url:
				if bug == "sql":
					if link.url in sqllist:
						pass
					else:
						sqlhunter(link.url)
				elif bug == "xss":
					xsshunter()
				else:
					pass
		first += 1

#Ana Program
logo()
while True:
	command = raw_input(bold+yellow+"bughunter@escoder ~ "+endcolor)
	if command.startswith("help"):
		help()
	elif command.startswith("search"):
		if command[7:10] == "sql":
			dork = command[11:]
			search(dork, "sql")
		elif command[7:10] == "xss":
			dork = command[11:]
			search(dork, "xss")
		else:
			print "{} Taraması Yapılamıyor.".format(command[7:10])
	elif command.startswith("generate"):
		if command[9:13] == "dork":
			print command[14:]
		else:
			print "{} Oluşturulamıyor.".format(command[8:13])
	else:
		print "Böyle Bir Komut Bulunmamakta!"
