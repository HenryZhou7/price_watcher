#This file is for the study of class in python

class ComplexNumber:
	

	def __init__(self, real, imag):
		self.__real = real
		self.imag = imag
		
	def updateReal(self, real):
		self.__real = real
		
	def updateImag(self, imag):
		self.__imag = imag
		
	def printComplex(self):
		print "%f + %f i" % (self.__real, self.__imag)
		
x = ComplexNumber(4.4, 7.7)
y = ComplexNumber(4.4, 7.7)
z = ComplexNumber(4.4, 7.7)

tempList = []

tempList.append(x)
tempList.append(y)
tempList.append(z)

print tempList[1].__real


