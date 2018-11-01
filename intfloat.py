#!/usr/bin/python3

from fractions import Fraction

class IntFloat:
	mantisse = Fraction(int(0))
	exponent = int(0)
	
	def __init__(self, a=0, b=0):
		self.mantisse = Fraction(a)
		self.exponent = int(b)
		self.normalize()

	def __str__(self):
		return ("" + self.mantisse.__str__() + "e" +  self.exponent.__str__())

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
			
		while diff > 0 :
			diff-=1
			gross*=10
				
		b = IntFloat(gross+klein, exp)
			
		b.normalize()
		return(b)
		
	def negate (self) :
		self.mantisse *= -1 
		
	def __sub__(self, a) :
		tmp = IntFloat(a.mantisse, a.exponent)
		tmp.negate()
		
		return(self+tmp)
		
	def __mul__(self,a):
		b = IntFloat(self.mantisse*a.mantisse, self.exponent+a.exponent)
		b.normalize()
		return (b)
		
	def __truediv__(self,a):
		b = IntFloat(self.mantisse/a.mantisse, self.exponent-a.exponent)
		b.normalize()
		return (b)

	def normalize(self):
		if self.mantisse == 0 :
			self.exponent = 0
		else :
			while self.mantisse%10 == 0:
				self.mantisse//=10
				self.exponent+=1
