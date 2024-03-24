class Text:
	
	def __init__(self, text="jon snow"):
		self.text = text
	
	def pascalcase(self):
		return ''.join([x.title() for x in self.text.split(" ")])

	def camelcase(self):
		a = self.text.split(" ")[0]
		return a+''.join([x.title() for x in self.text.split(" ")[1::]])

	def snakecase(self):
		return self.text.replace(" ","_").lower()

	def kebabcase(self):
		return self.text.replace(" ","-").lower()

	def flatcase(self):
		return self.text.replace(" ","").lower()

	def traincase(self):
		return '-'.join([x.title() for x in self.text.split(" ")])

	def cobolcase(self):
		return '-'.join([x.upper() for x in self.text.split(" ")])
"""
t = Text("tugberk kocatekin")
# print test
print(t.camelcase())
print(t.flatcase())
print(t.traincase())
print(t.cobolcase())
print(t.pascalcase())
print(t.kebabcase())
"""
