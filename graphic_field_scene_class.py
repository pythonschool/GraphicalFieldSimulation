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