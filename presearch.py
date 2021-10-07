#!/usr/bin/env python -*- coding: utf-8 -*-

"""
https://presearch.org/signup?rid=2716074

"""

import time
import os
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())


def busqueda(palabra):

	#time.sleep(10)

	print("Navegando a presearch... \n")

	driver.get("https://www.presearch.org/?utm_source=extcr")
	
	try:
	    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "search")))
	finally:
		print("Buscando... " + palabra + "\n")
		element.send_keys(palabra, Keys.ENTER)
	time.sleep(50)		 



import random
numero = 0

while numero <= 300:
	lines = open('search.txt').read().splitlines()
	myline =random.choice(lines)
	busqueda(myline)
	numero = numero + 1

driver.close()
