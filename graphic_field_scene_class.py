from PyQt4.QtGui import *

from field_class import *
from graphic_wheat_item_class import *
from graphic_potato_item_class import *
from graphic_cow_item_class import *
from graphic_sheep_item_class import *

import field_resources

class FieldGraphicsScene(QGraphicsScene):
	"""this class provides a scene to manage items in the field"""

	#constructor
	def __init__(self,max_crops,max_animals):
		super().__init__()
		
		self.field = Field(max_crops,max_animals)

		self.background_brush = QBrush()
		self.background_picture = QPixmap(":/field_background.png")
		self.background_brush.setTexture(self.background_picture)
		self.setBackgroundBrush(self.background_brush)

	#this method overrides the parent method
	def dragEnterEvent(self,event):
		#what to do if an object is dragged into the scene
		event.accept()

	#this method overrides the parent method
	def dragMoveEvent(self,event):
		event.accept()

	#this method overrides the parent method
	def dropEvent(self,event):
		event.accept()

		#what to do if an object is dropped on the scene
		if event.mimeData().hasFormat("application/x-wheat"):
			print("wheat")
		elif event.mimeData().hasFormat("application/x-potato"):
			print("potato")
		elif event.mimeData().hasFormat("application/x-cow"):
			print("cow")
		elif event.mimeData().hasFormat("application/x-sheep"):
			print("sheep")
		else:
			print("not recognised")