class UI:
	Elements = []
	Values = []
	def __init__(self):
		print("EasyGUI - simply and fast library for creating UI")
		addDraw(self.drawUI)
	def addButton(self, name, x, y, w, h):
		self.Elements.append((name, x, y, w, h, "Button"))
		self.Values.append(True)
	def drawUI(self):
		oldFill = getFill()
		oldFont, oldFontSize = getFont(true)
		setFont("/home/alexey/Downloads/Inkfree.ttf", 20)
		for elem in self.Elements:
			fill((54,66,242))
			if mouseIn(elem[1], elem[2], elem[3], elem[4]):
				setFontSize(25)
			fill((0, 0, 0))
			text(elem[0], elem[1]+elem[3]/2, elem[2]+elem[4]/2)
		fill(oldFill)
		setFont(oldFont, oldFontSize)