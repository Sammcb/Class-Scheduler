#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
import sys
import os
import json
import uuid
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from CommonWindowFunctions import *
from NewTeacher import *

class EnterTeacher(QWidget):

	def __init__(self, planner, school):
		super().__init__()

		self.initUI(planner, school)

	def initUI(self, planner, school):

		self.planner = planner
		self.school = school

		self.nameBox = QLineEdit(self)
		self.nameBox.setPlaceholderText("Teacher name")
		self.add = QPushButton("Add", self)
		self.add.clicked.connect(self.sendTeacher)
		self.nameBox.returnPressed.connect(self.add.click)

		self.hbox = QHBoxLayout()
		self.hbox.addWidget(self.nameBox)

		self.hbox2 = QHBoxLayout()
		self.hbox2.addStretch(1)
		self.hbox2.addWidget(self.add)

		self.vbox = QVBoxLayout()
		self.vbox.addLayout(self.hbox)
		self.vbox.addStretch(1)
		self.vbox.addLayout(self.hbox2)

		self.setLayout(self.vbox)
		self.setGeometry(0, 0, 400, 200)
		centerWindow(self)
		self.setWindowTitle("Enter a new teacher")
		self.show()

	def sendTeacher(self):

		self.id = str(uuid.uuid4())

		if (self.nameBox.text().isspace() or self.nameBox.text() == ""):

			self.teacherEntry = NewTeacher("(Unnamed)", self.id)

		else:

			self.teacherEntry = NewTeacher(self.nameBox.text(), self.id)

		self.school.teachers.append(self.teacherEntry.returnAsDict())

		with open(self.school.id + ".json", mode = "w+") as f:
			f.write(json.dumps(self.school.data, indent = 2))
			f.flush()
			os.fsync(f)

		self.planner.mainWidgets.addTeachersToTree()
		self.close()