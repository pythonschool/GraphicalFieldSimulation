from graphic_animal_item_class import *
from cow_class import *

import field_resources

class CowGraphicsPixmapItem(AnimalGraphicsPixmapItem):
    """this class provides a graphical representation of a cow"""

    #constructor
    def __init__(self):
        self.available_graphics = [":/cow_baby.png", ":/cow_poor.png",":/cow_fine.png",":/cow_prime.png"]
        super().__init__(self.available_graphics)

        self.animal = Cow("")