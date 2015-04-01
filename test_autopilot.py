# -*- coding: utf-8 -*-

import unittest
from autopilot import Samolot
from autopilot import Turbulencja
from autopilot import Autopilot

class SamolotTest(unittest.TestCase):
	def setUp(self):
		self.__instance = Samolot()
	def test_mierz(self):
		self.assertEqual((0.0, 0), self.__instance.mierz(), u"samolot leci krzywo bez turbulencji")
	def test_odchyl(self):
		self.__instance.odchyl()
		self.assertNotEqual((0.0, 0), self.__instance.mierz(), u"po odchyleniu samolot nie jest odchylony"u"u")
	"""Nie wiem dlaczego pisze, że nie istnieje metoda assertGreater(a,b)"""
	def test_koryguj(self):
		self.__instance.odchyl()
		(kat, kierunek) = self.__instance.mierz()
		self.__instance.koryguj(kat/10.0)
		(kat2, kierunek2) = self.__instance.mierz()
		self.assertGreater(abs(kat), abs(kat2), u"po korekcie przechylenie samolotu jest jeszcze większe")

if __name__ == '__main__':
	unittest.main()
