#!/usr/bin/python3

# (C) 2ß18 Emil Obermayr
# Die Klasse IntFloat erweitert die Klasse Fraction um eine Zehnerpotenz
# um Zahlen wie "3/4 Million" praktisch 1:1 abbilden zu können.

# https://github.com/nobswolf/PythonIntFloat 

from fractions import *
from decimal import *

class IntFloat:
	mantisse = Fraction(int(0))
	exponent = int(0)
	
	# Initialisiere per Default mit 0
	def __init__(self, a=0, b=0):
		self.mantisse = Fraction(a)
		self.exponent = int(b)
		self.normalize()

	# Darstellung als String ähnlich der wissenschaftlichen Darstellung	
	def __str__(self):
		if self.mantisse.denominator == 1 :
			out = (Decimal(self.mantisse.numerator) * 10**Decimal(self.exponent)).__str__()
		else : 
			out = "" + self.mantisse.numerator.__str__()
			if self.exponent != 0 :
				out += "E" +  self.exponent.__str__()
			if self.mantisse.denominator != 1 :
				out += "/" + self.mantisse.denominator.__str__()
		return (out)

	# Für die Addition werden beide Zahlen auf die kleinere Potenz gebracht	
	def __add__(self, a):
		if self.exponent >= a.exponent:
			gross = self.mantisse
			klein = a.mantisse
			exp = a.exponent
			diff = self.exponent - a.exponent
		else :
			gross = a.mantisse 
			klein = self.mantisse
			exp = self.exponent
			diff = a.exponent - self.exponent
			
		gross*= 10**diff
				
		b = IntFloat(gross+klein, exp)
			
		b.normalize()
		return(b)
	
	# erzeuge einen Dezimalbruch, ggf unter Angabe der Periode
	def periodic (self) :
		merkA = []
		z=self.mantisse.numerator
		n=self.mantisse.denominator
		# ganzzahliger Anteil
		out = "" + (z//n).__str__() 
		z=10*(z%n)
		period = ""
		
		# "schriftliche" Division
		while True :
			ganz = z//n
			bleibt = z%n
			# hatten wir diesen Rest schon -> Periode gefunden
			if bleibt in merkA :
				break 
			period += ganz.__str__()
			merkA.append(bleibt) 
			z=bleibt*10
			
		if period != "0" :
			out += ",p" + period
			
		if self.exponent != 0 :		
			out += "E" + self.exponent.__str__()
		return(out)
	
	# negatives Vorzeichen
	def negate (self) :
		self.mantisse *= -1 
		
	# Subtraktion als Addition mit negativem Vorzeichen 	
	def __sub__(self, a) :
		tmp = IntFloat(a.mantisse, a.exponent)
		tmp.negate()
		
		return(self+tmp)
	
	# Multiplikaton komponentenweise
	def __mul__(self,a):
		b = IntFloat(self.mantisse*a.mantisse, self.exponent+a.exponent)
		b.normalize()
		return (b)
	
	# Division über Fraction als Mutterklasse
	def __truediv__(self,a):
		b = IntFloat(self.mantisse/a.mantisse, self.exponent-a.exponent)
		b.normalize()
		return (b)

	# erzeuge einheitliche Darstellung
	def normalize(self):
		# eindeutige 0
		if self.mantisse == 0 :
			self.exponent = 0
		else :
			# wenn Nenner durch 2 teilbar mit 5 erweitern und die 10 in den Exponenten
			while self.mantisse.denominator % 2 == 0 :
				self.mantisse *= 10
				self.exponent -= 1 

			# Wenn Nenner duch 5 teilbar mit 2 erweitern und die 10 in den Exponenten 
			while self.mantisse.denominator % 5 == 0 :
				self.mantisse *= 10
				self.exponent -= 1 

			# 10 im Zähler in den Exponenten
			num = self.mantisse.numerator
			while num%10 == 0:
				num//=10
				self.exponent+=1
				
			# 10 im Nenner in den Exponenten 
			den = self.mantisse.denominator
			while den%10 == 0:
				den//=10
				self.exponent-=1
				
			self.mantisse = Fraction(num, den)
