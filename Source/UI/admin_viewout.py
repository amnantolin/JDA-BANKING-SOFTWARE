# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_viewout.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import res

class Ui_admin_viewout(object):
    def setupUi(self, admin_viewout):
        admin_viewout.setObjectName("admin_viewout")
        admin_viewout.resize(660, 600)
        admin_viewout.setMinimumSize(QtCore.QSize(660, 600))
        admin_viewout.setMaximumSize(QtCore.QSize(660, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(':/images/icon.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        admin_viewout.setWindowIcon(icon)
        admin_viewout.setStyleSheet("QWidget#centralwidget{\n"
"border-image: url(':/images/ad.png');\n"
"}\n"
"\n"
"QPushButton{\n"
"background: transparent;\n"
"background-color: white;\n"
"border: 2px solid black;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(30, 30, 30);\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"font: bold;\n"
"}\n"
"\n"
"QLabel#labela,#labelb,#labelc,#labeld,#labele,#labelf,#labelg,#labelh,#labeli,#labelj{\n"
"background-color: white;\n"
"border: 2px solid black;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(admin_viewout)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 155, 471))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label1_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label1_2.setFont(font)
        self.label1_2.setObjectName("label1_2")
        self.verticalLayout.addWidget(self.label1_2)
        self.label2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.verticalLayout.addWidget(self.label2)
        self.label3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label3.setFont(font)
        self.label3.setObjectName("label3")
        self.verticalLayout.addWidget(self.label3)
        self.label4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label4.setFont(font)
        self.label4.setObjectName("label4")
        self.verticalLayout.addWidget(self.label4)
        self.label5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label5.setFont(font)
        self.label5.setObjectName("label5")
        self.verticalLayout.addWidget(self.label5)
        self.label6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label6.setFont(font)
        self.label6.setObjectName("label6")
        self.verticalLayout.addWidget(self.label6)
        self.label7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label7.setFont(font)
        self.label7.setObjectName("label7")
        self.verticalLayout.addWidget(self.label7)
        self.label8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label8.setFont(font)
        self.label8.setObjectName("label8")
        self.verticalLayout.addWidget(self.label8)
        self.label9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label9.setFont(font)
        self.label9.setObjectName("label9")
        self.verticalLayout.addWidget(self.label9)
        self.label9_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label9_2.setFont(font)
        self.label9_2.setObjectName("label9_2")
        self.verticalLayout.addWidget(self.label9_2)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(190, 20, 461, 471))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labela = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labela.setFont(font)
        self.labela.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.labela.setText("")
        self.labela.setObjectName("labela")
        self.verticalLayout_2.addWidget(self.labela)
        self.labelb = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelb.setFont(font)
        self.labelb.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.labelb.setText("")
        self.labelb.setObjectName("labelb")
        self.verticalLayout_2.addWidget(self.labelb)
        self.labelc = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelc.setFont(font)
        self.labelc.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.labelc.setText("")
        self.labelc.setObjectName("labelc")
        self.verticalLayout_2.addWidget(self.labelc)
        self.labeld = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labeld.setFont(font)
        self.labeld.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.labeld.setText("")
        self.labeld.setObjectName("labeld")
        self.verticalLayout_2.addWidget(self.labeld)
        self.labele = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labele.setFont(font)
        self.labele.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.labele.setText("")
        self.labele.setObjectName("labele")
        self.verticalLayout_2.addWidget(self.labele)
        self.labelf = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelf.setFont(font)
        self.labelf.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.labelf.setText("")
        self.labelf.setObjectName("labelf")
        self.verticalLayout_2.addWidget(self.labelf)
        self.labelg = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelg.setFont(font)
        self.labelg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.labelg.setText("")
        self.labelg.setObjectName("labelg")
        self.verticalLayout_2.addWidget(self.labelg)
        self.labelh = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelh.setFont(font)
        self.labelh.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.labelh.setText("")
        self.labelh.setObjectName("labelh")
        self.verticalLayout_2.addWidget(self.labelh)
        self.labeli = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labeli.setFont(font)
        self.labeli.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.labeli.setText("")
        self.labeli.setObjectName("labeli")
        self.verticalLayout_2.addWidget(self.labeli)
        self.labelj = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelj.setFont(font)
        self.labelj.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.labelj.setText("")
        self.labelj.setObjectName("labelj")
        self.verticalLayout_2.addWidget(self.labelj)
        self.sys_back = QtWidgets.QPushButton(self.centralwidget)
        self.sys_back.setGeometry(QtCore.QRect(470, 530, 171, 33))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sys_back.setFont(font)
        self.sys_back.setObjectName("sys_back")
        self.verticalLayoutWidget.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.sys_back.raise_()
        self.label9.raise_()
        admin_viewout.setCentralWidget(self.centralwidget)

        self.retranslateUi(admin_viewout)
        QtCore.QMetaObject.connectSlotsByName(admin_viewout)

    def retranslateUi(self, admin_viewout):
        _translate = QtCore.QCoreApplication.translate
        admin_viewout.setWindowTitle(_translate("admin_viewout", "View Account"))
        self.label1_2.setText(_translate("admin_viewout", "<html><head/><body><p><span style=\" color:#ffffff;\">First Name:</span></p></body></html>"))
        self.label2.setText(_translate("admin_viewout", "<html><head/><body><p><span style=\" color:#ffffff;\">Middle Name:</span></p></body></html>"))
        self.label3.setText(_translate("admin_viewout", "<html><head/><body><p><span style=\" color:#ffffff;\">Last Name:</span></p></body></html>"))
        self.label4.setText(_translate("admin_viewout", "<html><head/><body><p><span style=\" color:#ffffff;\">Address:</span></p></body></html>"))
        self.label5.setText(_translate("admin_viewout", "<html><head/><body><p><span style=\" color:#ffffff;\">Age:</span></p></body></html>"))
        self.label6.setText(_translate("admin_viewout", "<html><head/><body><p><span style=\" color:#ffffff;\">Contact #:</span></p></body></html>"))
        self.label7.setText(_translate("admin_viewout", "<html><head/><body><p><span style=\" color:#ffffff;\">Email:</span></p></body></html>"))
        self.label8.setText(_translate("admin_viewout", "<html><head/><body><p><span style=\" color:#ffffff;\">Card Number:</span></p></body></html>"))
        self.label9.setText(_translate("admin_viewout", "<html><head/><body><p><span style=\" color:#ffffff;\">Account Number:</span></p></body></html>"))
        self.label9_2.setText(_translate("admin_viewout", "<html><head/><body><p><span style=\" color:#ffffff;\">Balance:</span></p></body></html>"))
        self.sys_back.setText(_translate("admin_viewout", "BACK"))

