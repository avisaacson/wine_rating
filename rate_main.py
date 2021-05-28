class Wine:
	def __init__(self, color, appellation, producer, bottling, vintage, deliciousness, aroma, balance, complexity, intensity, length, typicity, ageability, extra=None):
		self.color = color
		self.appellation = appellation
		self.producer = producer
		self.bottling = bottling
		self.vintage = vintage

		self.deliciousness = deliciousness
		self.aroma = aroma
		self.balance = balance
		self.complexity = complexity
		self.intensity = intensity
		self.length = length
		self.typicity = typicity
		self.ageability = ageability

		self.extra = extra

	def get_rating(self):
		rating = ((
			(self.deliciousness * 2) + 
			(self.aroma * 1) + 
			(self.balance * 5) + 
			(self.complexity * 4) + 
			(self.intensity * 3) +
			(self.length * 3) + 
			(self.typicity * 1) +
			(self.ageability * 1)) 
		/ 2)
		return rating

def show_rate_scale():
	print("\n============================================================")
	print(  "                        Rating Scale                        ")
	print(  "============================================================")
	print(  "\n")
	print(  "  (10) - World-Class")
	print(  "   (9) - Exemplary")
	print(  "   (8) - Great")
	print(  "   (7) - Good")
	print(  "   (6) - Well Done")
	print(  "   (5) - Middle of the Road")
	print(  "   (4) - Just Fine")
	print(  "   (3) - Poorly Done")
	print(  "   (2) - Bad Quality")
	print(  "   (1) - Flawed or Undrinkable")
	print("\n============================================================")

	
show_rate_scale()

my_wine = Wine("X", "X", "X", "X", "X", 9, 8, 10, 9, 9, 9, 10, 10, "X")
print(round(my_wine.get_rating()))
