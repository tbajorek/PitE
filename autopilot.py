# -*- coding: utf-8 -*-

import math
import threading
import time
import random

u"""Klasa reprezentująca lecący samolot oraz kąt i kierunek jego przechylenia"""
class Samolot:
	def __init__(self):
		self.__kat=0.0
		self.__kierunek=0
		self.__komunikat=""
	def mierz(self):
		return (self.__kat, self.__kierunek)
	def odchyl(self):
		if random.random() < 0.5:
			k = -1
		else:
			k = 1
		if self.__kierunek == k:
			granica = 20-self.__kat
		else:
			granica = 20
		self.__kat = random.random()*granica
		self.__kierunek = k
		self.__komunikat = "\033[2J\033[H\033[91mturbulencja!: "+str(self.__kierunek*self.__kat)+" stopni\033[0m"

	def koryguj(self, kat):
		if self.__kat < 0:
			self.__kat += kat
		else:
			self.__kat -= kat
		if abs(self.__kat) < 0.00001:
			self.__kierunek = 0
		return self.mierz()
	def komunikat(self):
		return self.__komunikat

u"""Klasa wątku, który co jakiś czas przechyla losowo samolot"""
class Turbulencja(threading.Thread):
	def __init__(self, samolot):
		threading.Thread.__init__(self)
		self.__samolot = samolot
		self.__warunek = True
	def run(self):
		while self.__warunek:
			self.__samolot.odchyl()
			print self.__samolot.komunikat()
			time.sleep(4.7)
	def zakoncz(self):
		self.__warunek = False

u"""Klasa wątku autopilota.
Wykrywa on, jeżeli turbulencja przechyliła samolot
i stara się go stosunkowo płynnie wyprostować."""
class Autopilot(threading.Thread):
	def __init__(self, samolot):
		threading.Thread.__init__(self)
		self.__samolot = samolot
		self.__warunek = True
	def run(self):
		while self.__warunek:
			pomiar = self.__samolot.mierz()
			while abs(pomiar[0]) > 0.00001 and self.__warunek:
				if abs(pomiar[0])>0.25:
					korekta = math.sqrt(abs(pomiar[0]))
				else:
					korekta = abs(pomiar[0])/1.05
				pomiar = self.__samolot.koryguj(korekta)
				print self.__samolot.komunikat()
				print "\033[33mkoryguje...\033[0m"
				print "\33[33mpo korekcie: %f stopni\033[0m" % (pomiar[0])
				time.sleep(0.3)
			time.sleep(0.1)
			if self.__warunek:
				print '\033[2J\033[H\033[32m' + 'brak odchylenia' + '\033[0m'
	def zakoncz(self):
		self.__warunek = False
u"""Główna część programu.
Aby zakończyć jego działanie, należy wcisnąć Ctrl+C"""
if __name__ == '__main__':
	samolot = Samolot()
        turbulencja = Turbulencja(samolot)
	autopilot = Autopilot(samolot)
       	turbulencja.start()
	autopilot.start()
	while True:
		try:
			if threading.Event().isSet():
				raise KeyboardInterrupt
		except KeyboardInterrupt:
			turbulencja.zakoncz()
			autopilot.zakoncz()
			time.sleep(0.02)
			print "\033[2J\033[H\033[34mZakończyłeś działanie autopilota!\033[0m"
			exit()
