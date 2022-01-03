#
# Windows Web App Maker
#
# Thankyou for using Windows Web App Maker
# This source is maked by using python 3 and protected by python protecter 
# 
# (c) Windows Web App Maker. all right reserved.
#

import sys, random
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtNetwork import QNetworkCookie
from PyQt5.QtNetwork import QNetworkDiskCache
from typing import cast

def start():
	print("Windows Web App Maker [Free Veresion]")
	print("(c) Windows Web App Maker. all right reserved.")
	print("\nThis program is builted with Windows Web App Maker Free")
	print("Commercial use with Windows Web App Maker Free is not Allowed")

start()

def data_load():
	global height2
	global link
	global titled
	global width2

	# Load url
	url = open("data/a62812e1d8712ca4f21ffeadbb61985f", 'r')
	link = url.readline()
	url.close()

	# Load title
	title = open("data/086bf0bf5c8a6b6557c0d5391236d6bd", 'r')
	titled = title.readline()
	title.close()

	# Load width
	width = open("data/136a62946c6331eaba24f584efc3e1df", 'r')
	width2 = width.readline()
	width.close()

	# Load height
	height = open("data/622eeaa4b5f88517b76a3da5fcf1b1a3", 'r') 
	height2 = height.readline()
	height.close()

data_load()

def security_check():
	free = open("data/be28c1c33b979e6650f67e7800dc0662", 'r')
	security_data = free.readline()
	free.close()
	if security_data == "Windows Web App Maker [Free Veresion]" :
		print(f"\nsecurity_check_{random.randrange(10000,99999)} ... ok")
	else:
		print(f"\nsecurity_check_{random.randrange(10000,99999)} ... error")
		exit()

security_check()

def data_load_print():
	print(f"\ndata_title_{random.randrange(10000,99999)} ... {titled}")
	print(f"data_width_{random.randrange(10000,99999)} ... {width2}")
	print(f"data_height_{random.randrange(10000,99999)} ... {height2}")
	print(f"data_link_{random.randrange(10000,99999)} ... {link}")

data_load_print()

class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		
		# release in v2
		# self.cache = QNetworkDiskCache().setCacheDirectory('cache')
		#self.cookie = QNetworkCookie()
		#QWebEngineProfile.defaultProfile().cookieStore().deleteCookie(self.cookie)

		self.webapp = QWebEngineView()
		self.webapp.setUrl(QUrl(link))
		self.setCentralWidget(self.webapp)

app = QApplication(sys.argv)
QApplication.setApplicationName(titled)
window = MainWindow()
if width2 == "-1" and height2 == "-1":
	window.setFixedSize(510, 890)
else:
	window.resize(int(width2), int(height2))
window.show()
app.exec_()