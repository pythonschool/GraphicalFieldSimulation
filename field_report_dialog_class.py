try:
    from PyQt4.QtGui import *
except:
    from PyQt5.QtWidgets import *

class FieldReportDialog(QDialog):
    """this class creates a report for the field in dialog form"""

    #constructor
    def __init__(self,report):
        super().__init__()
        self.setWindowTitle("Field Report")

        #labels for the crop statistics
        self.crop_type_label = QLabel("Crop Type")
        self.crop_status_label = QLabel("Crop Status")
        self.crop_days_growing_label = QLabel("Days Growing")
        self.crop_growth_label = QLabel("Growth")

        #labels for the animal statistics
        self.animal_type_label = QLabel("Animal Type")
        self.animal_status_label = QLabel("Animal Status")
        self.animal_days_growing_label = QLabel("Days Growing")
        self.animal_weight_label = QLabel("Weight")

        #labels for other cases
        self.no_crops_label = QLabel("There are no crops in this field")
        self.no_animals_label = QLabel("There are no animals in this field")
        self.nothing_label = QLabel("The field is empty")

        self.close_button = QPushButton("Dismiss Report")

        #layouts
        self.report_layout = QGridLayout()
        self.layout = QVBoxLayout()

        row = 1

        if len(report["crops"]) == 0 and len(report["animals"]) == 0:
            self.report_layout.addWidget(self.nothing_label,0,0)
        else:
            if len(report["crops"]) > 0:
                self.report_layout.addWidget(self.crop_type_label,0,0)
                self.report_layout.addWidget(self.crop_status_label,0,1)
                self.report_layout.addWidget(self.crop_days_growing_label,0,2)
                self.report_layout.addWidget(self.crop_growth_label,0,3)
                #create crop report details
                for crop in report["crops"]:
                    self.report_layout.addWidget(QLabel(str(crop["type"])),row,0)
                    self.report_layout.addWidget(QLabel(str(crop["status"])),row,1)
                    self.report_layout.addWidget(QLabel(str(crop["days growing"])),row,2)
                    self.report_layout.addWidget(QLabel(str(crop["growth"])),row,3)
                    row += 1
            else:
                self.report_layout.addWidget(self.no_crops_label,0,0)
            if len(report["animals"]) > 0:
                self.report_layout.addWidget(self.animal_type_label,row,0)
                self.report_layout.addWidget(self.animal_status_label,row,1)
                self.report_layout.addWidget(self.animal_days_growing_label,row,2)
                self.report_layout.addWidget(self.animal_weight_label,row,3)
                row += 1
                for animal in report["animals"]:
                    self.report_layout.addWidget(QLabel(str(animal["type"])),row,0)
                    self.report_layout.addWidget(QLabel(str(animal["status"])),row,1)
                    self.report_layout.addWidget(QLabel(str(animal["days growing"])),row,2)
                    self.report_layout.addWidget(QLabel(str(animal["weight"])),row,3)
                    row += 1
            else:
                self.report_layout.addWidget(self.no_animals_label,row,0)

        self.layout.addLayout(self.report_layout)
        self.layout.addWidget(self.close_button)
        self.setLayout(self.layout)

        #connections
        self.close_button.clicked.connect(self.close)
