#!/usr/bin/python3

from fractions import Fraction

class IntFloat:
	mantisse = Fraction(int(0))
	exponent = int(0)
	
	def __init__(self, a=0, b=0):
		self.mantisse = Fraction(a)
		self.exponent = int(b)

	def __str__(self):
		return ("" + self.mantisse.__str__() + "e" +  self.exponent.__str__())

	def __add__(self, a):
		if self.exponent > a.exponent:
			tmp = IntFloat(self.mantisse, self.exponent)
			diff = self.exponent - a.exponent
			tmp.exponent = a.exponent
			
			while diff > 0 :
				diff-=1
				tmp.mantisse*=10
				
			b = IntFloat(tmp.mantisse+a.mantisse, a.exponent)

		if self.exponent < a.exponent:
			tmp = IntFloat(a.mantiss, self.exponent)
			diff = a.exponent - self.exponent
			tmp.exponent = self.exponent
			
			while diff > 0 :
				diff-=1
				tmp.mantisse*=10
				
			b = IntFloat(tmp.mantisse+self.mantisse, self.exponent)

		if self.exponent == a.exponent:
			b = IntFloat(a.mantisse+self.mantisse, self.exponent)
			
		self.normalize(b)
		return(b)
		
	def negate (self) :
		self.mantisse *= -1 
		
	def __sub__(self, a) :
		tmp = IntFloat(a.mantisse, a.exponent)
		tmp.negate()
		
		return(self+tmp)
		
	def __mul__(self,a):
		b = IntFloat(self.mantisse*a.mantisse, self.exponent+a.exponent)
		self.normalize(b)
		return (b)
		
	def __truediv__(self,a):
		b = IntFloat(self.mantisse/a.mantisse, self.exponent-a.exponent)
		self.normalize(b)
		return (b)

	def normalize(self,a):
		while a.mantisse%10 == 0:
			a.mantisse//=10
			a.exponent+=1