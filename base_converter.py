
class Convert_Base():
	'''A class to convert numbers from one base to another. Supports bases from 2 to 36. Please remember to put numbers with letters in quotes, e.g. '156A' for base 11.'''
	num = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A':10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G':16, 'H':17, 'I':18, 'J':19, 'K':20, 'L':21, 'M':22, 'N':23, 'O':24, 'P':25, 'Q':26, 'R':27, 'S':28, 'T':29, 'U':30, 'V':31, 'W':32, 'X':33, 'Y':34, 'Z':35}
	def __init__(self, num, sub, main = 10):#num is the number to be converted, sub is the base of the number, main is the base to convert to (default is 10)        
		self.num = num
		self.sub = sub
		self.main = main

	def __repr__(self):
		'''Converts the number from base 'sub' to base 'main' and returns it as a string.'''
		if self.sub < 2 or self.sub > 36 or self.main < 2 or self.main > 36:
			raise ValueError("Base must be between 2 and 36.")
		if not (isinstance(self.num, int) or  self.num.isalnum() or isinstance(self.num, str)):
			raise TypeError("Number must be a string or int .")
		return self.from_ten(self.to_ten())
		
	
	def solve(self):# same as __repr__, but returns the converted number
		decimal_value = self.to_ten()
		return self.from_ten(decimal_value)()

	def to_ten(self):# Converts the number from the base 'sub' to base 10
		r = str(self.num)
		if self.sub > 10:
			try:
				if int(self.num) <= 10:
					return self.num
			except ValueError:
				return sum((Convert_Base.num[r[i]])* (self.sub **(len(r)-(i+1))) for i in range(len(r)))
		return sum((int(r[i]))* (self.sub **(len(r)-(i+1))) for i in range(len(r)))

	def from_ten(self, d_v):# Converts the number from base 10 to the base 'main', u is 
		rnum = {k:v for v,k in Convert_Base.num.items() if k < self.main}
		i = self.main
		t = []
		if d_v < self.main:
			return rnum[d_v]
		else:
			while d_v >= self.main:
					q = d_v % i
					t.append(q)
					d_v //= self.main
					if d_v < self.main:
						t.append(d_v)
			return ''.join(rnum[o] for o in reversed(t))
if __name__ == '__main__':
	p = Convert_Base('1ABD6', 18, 3)
	print(p)  # This will call __repr__ method which converts to base 10 and then from base 10 to the specified base
	print(p.to_ten())
	print(p.from_ten(22142))  # This will convert 1562 from base 10 to base 30