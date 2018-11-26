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
		out = "" + self.mantisse.numerator.__str__()
		if self.exponent != 0 :
			out += "E" +  self.exponent.__str__()
		if self.mantisse.denominator != 1 :
			out += "/" + self.mantisse.denominator.__str__()
		return (out)

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
		
	def periodic (self) :
		merkA = []
		z=self.mantisse.numerator
		n=self.mantisse.denominator
		out = "" + (z//n).__str__() + ",p"
		z=10*(z%n)
		
		while True :
			ganz = z//n
			bleibt = z%n
			if bleibt in merkA :
				break 
			out += ganz.__str__()
			merkA.append(bleibt) 
			z=bleibt*10
			
		if self.exponent != 0 :		
			out += "e" + self.exponent.__str__()
		return(out)
		
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
			while self.mantisse.denominator % 2 == 0 :
				self.mantisse *= 10
				self.exponent -= 1 

			while self.mantisse.denominator % 5 == 0 :
				self.mantisse *= 10
				self.exponent -= 1 

			num = self.mantisse.numerator
			while num%10 == 0:
				num//=10
				self.exponent+=1
				
			den = self.mantisse.denominator
			while den%10 == 0:
				den//=10
				self.exponent-=1
			self.mantisse = Fraction(num, den)
