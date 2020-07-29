# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plugin_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AltibasePluginDialogBase(object):
    def setupUi(self, AltibasePluginDialogBase):
        AltibasePluginDialogBase.setObjectName("AltibasePluginDialogBase")
        AltibasePluginDialogBase.resize(400, 300)
        self.button_box = QtWidgets.QDialogButtonBox(AltibasePluginDialogBase)
        self.button_box.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")

        self.retranslateUi(AltibasePluginDialogBase)
        self.button_box.accepted.connect(AltibasePluginDialogBase.accept)
        self.button_box.rejected.connect(AltibasePluginDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(AltibasePluginDialogBase)

    def retranslateUi(self, AltibasePluginDialogBase):
        _translate = QtCore.QCoreApplication.translate
        AltibasePluginDialogBase.setWindowTitle(_translate("AltibasePluginDialogBase", "Altibase Plugin"))

