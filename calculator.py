import pygtk
pygtk.require('2.0')
import gtk

class Calc:
	def add():
		print("add")
	def sub():
		print("sub")

	def __init__(self):
		print("init")
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

		self.vcontainer = gtk.VBox(True,0)

		self.resultline = gtk.HBox(True,0)
		self.result = gtk.Label("Result")
		self.result.show()
		self.resultline.add(self.result)
		self.resultline.show()
		self.vcontainer.add(self.resultline)

		self.line1 = gtk.HBox(True,0)
		self.plusbutton = gtk.Button("+")
		self.minbutton = gtk.Button("-")
		self.eqbutton = gtk.Button("=")		
		self.line1.pack_start(self.plusbutton,True,True,0)
		self.line1.pack_start(self.minbutton,True,True,0)
		self.line1.pack_start(self.eqbutton,True,True,0)
		self.plusbutton.show()
		self.minbutton.show()
		self.eqbutton.show()
		self.line1.show()
		self.vcontainer.add(self.line1)

		self.line2 = gtk.HBox(True,0)
		self.multbtn = gtk.Button("*")
		self.dividebtn = gtk.Button("/")
		self.powerbtn = gtk.Button("^")
		self.line2.pack_start(self.multbtn,True,True,0)
		self.line2.pack_start(self.dividebtn,True,True,0)
		self.line2.pack_start(self.powerbtn,True,True,0)
		self.multbtn.show()
		self.dividebtn.show()
		self.powerbtn.show()
		self.line2.show()
		self.vcontainer.add(self.line2)

		self.line3 = gtk.HBox(True,0)
		self.onebtn = gtk.Button("1")
		self.twobtn = gtk.Button("2")
		self.threebtn = gtk.Button("3")
		self.line3.pack_start(self.onebtn,True,True,0)
		self.line3.pack_start(self.twobtn,True,True,0)
		self.line3.pack_start(self.threebtn,True,True,0)
		self.onebtn.show()
		self.twobtn.show()
		self.threebtn.show()
		self.line3.show()
		self.vcontainer.add(self.line3)


		self.line4 = gtk.HBox(True,0)
		self.fourbtn = gtk.Button("4")
		self.fivebtn = gtk.Button("5")
		self.sixbtn = gtk.Button("6")
		self.line4.pack_start(self.fourbtn,True,True,0)
		self.line4.pack_start(self.fivebtn,True,True,0)
		self.line4.pack_start(self.sixbtn,True,True,0)
		self.fourbtn.show()
		self.fivebtn.show()
		self.sixbtn.show()
		self.line4.show()
		self.vcontainer.add(self.line4)


		self.line5 = gtk.HBox(True,0)
		self.sevenbtn = gtk.Button("7")
		self.eightbtn = gtk.Button("8")
		self.ninebtn = gtk.Button("9")
		self.line5.pack_start(self.sevenbtn,True,True,0)
		self.line5.pack_start(self.eightbtn,True,True,0)
		self.line5.pack_start(self.ninebtn,True,True,0)
		self.sevenbtn.show()
		self.eightbtn.show()
		self.ninebtn.show()
		self.line5.show()
		self.vcontainer.add(self.line5)

		self.line6 = gtk.HBox(True,0)
		self.xbtn = gtk.Button("X")
		self.zerobtn = gtk.Button("0")
		self.ybtn = gtk.Button("Y")
		self.line6.pack_start(self.xbtn,True,True,0)
		self.line6.pack_start(self.zerobtn,True,True,0)
		self.line6.pack_start(self.ybtn,True,True,0)
		self.xbtn.show()
		self.zerobtn.show()
		self.ybtn.show()
		self.line6.show()
		self.vcontainer.add(self.line6)

		self.vcontainer.show();
		self.window.add(self.vcontainer)
		self.window.show()


	def main(self):
		print("main")
		gtk.main()




if __name__=="__main__":
	calc = Calc()
	calc.main()