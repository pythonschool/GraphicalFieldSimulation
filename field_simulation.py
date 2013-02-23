from PyQt4.QtCore import *
from PyQt4.QtGui import *

from graphic_field_scene_class import *
from graphic_wheat_item_class import *
from graphic_potato_item_class import *
from graphic_cow_item_class import *
from graphic_sheep_item_class import *
from graphic_drag_label_class import *
from field_manual_grow_dialog_class import *
from field_report_dialog_class import *

import sys, random

class FieldWindow(QMainWindow):
    """this class creates a main window to observe the growth of a simulated field"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Field Simulation")

        #create toolbars
        self.crop_tool_bar = QToolBar()
        self.animal_tool_bar = QToolBar()

        #create toolbar labels
        self.wheat_label = WheatDragLabel()
        self.wheat_label.setToolTip("Add Wheat")

        self.potato_label = PotatoDragLabel()
        self.potato_label.setToolTip("Add Potato")

        self.cow_label = CowDragLabel()
        self.cow_label.setToolTip("Add Cow")

        self.sheep_label = SheepDragLabel()
        self.sheep_label.setToolTip("Add Sheep")

        #add labels to toolbars
        self.crop_tool_bar.addWidget(self.wheat_label)
        self.crop_tool_bar.addWidget(self.potato_label)

        self.animal_tool_bar.addWidget(self.cow_label)
        self.animal_tool_bar.addWidget(self.sheep_label)

        #add toolbars to window
        self.addToolBar(self.crop_tool_bar)
        self.addToolBar(self.animal_tool_bar)

        self.field_graphics_view = QGraphicsView()
        self.field_graphics_view.setScene(FieldGraphicsScene(1,5))

        self.field_graphics_view.setFixedHeight(400)
        self.field_graphics_view.setFixedWidth(400)
        self.field_graphics_view.setSceneRect(0,0,400,400)
        self.field_graphics_view.setHorizontalScrollBarPolicy(1)
        self.field_graphics_view.setVerticalScrollBarPolicy(1)

        self.field_report_button = QPushButton("Field Report")
        self.field_automatic_grow_button = QPushButton("Automatically Grow Field")
        self.field_manual_grow_button = QPushButton("Manually Grow Field")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.field_graphics_view)
        self.layout.addWidget(self.field_report_button)
        self.layout.addWidget(self.field_automatic_grow_button)
        self.layout.addWidget(self.field_manual_grow_button)

        self.main_widget = QWidget()
        self.main_widget.setLayout(self.layout)
        self.setCentralWidget(self.main_widget)

        #connections
        self.field_automatic_grow_button.clicked.connect(self.automatically_grow)
        self.field_manual_grow_button.clicked.connect(self.manually_grow)
        self.field_report_button.clicked.connect(self.report)

    def automatically_grow(self):
        for days in range(30):
            light = random.randint(1,10)
            water = random.randint(1,10)
            food = random.randint(1,100)
            self.field_graphics_view.scene().field.grow(light,food,water)
        self.field_graphics_view.scene().update_status()

    def manually_grow(self):
        dialog = ManualGrowDialog()
        dialog.exec_()
        light,water,food = dialog.get_values()
        self.field_graphics_view.scene().field.grow(light,food,water)
        self.field_graphics_view.scene().update_status()

    def report(self):
        current_report = self.field_graphics_view.scene().field.report_contents()
        report_dialog = FieldReportDialog(current_report)
        report_dialog.exec_()

def main():
    field_simulation = QApplication(sys.argv) #create new application
    field_window = FieldWindow() #create new instance of main window
    field_window.show() #make instance visible
    field_window.raise_() #raise instance to top of window stack
    field_simulation.exec_() #monitor application for events

if __name__ == "__main__":
    main()
