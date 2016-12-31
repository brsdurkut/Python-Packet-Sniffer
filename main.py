# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/tut1.ui'
#
# Created: Thu Dec 29 06:08:30 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from rules.rule import Rule
from sniffer import Sniffer


class Communicate(QtCore.QObject):
    speakNumber = QtCore.Signal(int)

class Ui_MainWindow(object):

    def init(self):
        self.r = Rule()
        self.s = Sniffer(self.r)
        self.c = Communicate()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(738, 706)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(738, 706))
        MainWindow.setMaximumSize(QtCore.QSize(738, 706))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QtGui.QGridLayout(self.tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.listWidget = QtGui.QListWidget(self.tab)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_3.addWidget(self.listWidget, 0, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_start = QtGui.QPushButton(self.tab)
        self.btn_start.setObjectName("btn_start")
        self.btn_start.clicked.connect(self.start)
        self.verticalLayout.addWidget(self.btn_start)
        self.btn_pause = QtGui.QPushButton(self.tab)
        self.btn_pause.setObjectName("btn_pause")
        self.btn_pause.clicked.connect(self.pause)
        self.verticalLayout.addWidget(self.btn_pause)
        self.btn_stop = QtGui.QPushButton(self.tab)
        self.btn_stop.setObjectName("btn_stop")
        self.btn_stop.clicked.connect(self.stop)
        self.verticalLayout.addWidget(self.btn_stop)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_6 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tableWidget = QtGui.QTableWidget(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.gridLayout_5.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.btn_add = QtGui.QPushButton(self.tab_2)
        self.btn_add.setObjectName("btn_add")
        self.btn_add.clicked.connect(self.add_rule)
        self.verticalLayout_2.addWidget(self.btn_add)
        self.btn_del = QtGui.QPushButton(self.tab_2)
        self.btn_del.setObjectName("btn_del")
        self.btn_del.clicked.connect(self.delete_selected)
        self.verticalLayout_2.addWidget(self.btn_del)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.btn_load = QtGui.QPushButton(self.tab_2)
        self.btn_load.setObjectName("btn_load")
        self.btn_load.clicked.connect(self.load_rules)
        self.verticalLayout_2.addWidget(self.btn_load)
        self.btn_save = QtGui.QPushButton(self.tab_2)
        self.btn_save.setObjectName("btn_save")
        self.btn_save.clicked.connect(self.save_rules)
        self.verticalLayout_2.addWidget(self.btn_save)
        self.verticalLayout_2.setStretch(0, 3)
        self.gridLayout_6.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 738, 27))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuAbout.menuAction())

        self.c.speakNumber.connect(self.update_list)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Dummy Firewall", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_start.setText(QtGui.QApplication.translate("MainWindow", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_pause.setText(QtGui.QApplication.translate("MainWindow", "Pause", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_stop.setText(QtGui.QApplication.translate("MainWindow", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Sniffer", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "Src IP", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "Src Port", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("MainWindow", "Dest IP", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("MainWindow", "Dest Port", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("MainWindow", "Flags", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_add.setText(QtGui.QApplication.translate("MainWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_del.setText(QtGui.QApplication.translate("MainWindow", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_load.setText(QtGui.QApplication.translate("MainWindow", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_save.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Rules", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbout.setTitle(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))

    def update_list(self):
        item = self.s.packet_list[-1]
        self.listWidget.addItem(item["details"].get_str())

    def start(self):
        print("start clicked")
        self.listWidget.clear()
        self.s.start(self.c)

    def pause(self):
        pass

    def stop(self):
        print("stop clicked")
        self.s.stop()
        print([p["details"].get_summary() for p in self.s.packet_list])

    def load_rules(self):
        self.r._load("data/rules")
        self.refresh()

    def save_rules(self):
        self.r._save()

    def add_rule(self):
        text, ok = QtGui.QInputDialog.getText(self.centralwidget, 'Add New Rule', 'e.g. \"192.168.1.100 80 123.22.33.121 8080 ACK\"')

        if ok:
            self.r._add_rule(text)
            self.refresh()

    def delete_selected(self):
        curr = self.tableWidget.currentRow()
        print("Current Row: {}".format(str(curr)))
        if self.tableWidget.currentRow() != -1:
            self.r._del_rule(curr)
            self.refresh()

    def clear(self):
        self.tableWidget.setRowCount(0)
        """
        for index in self.tableWidget.rowCount():
            self.tableWidget.removeRow(index)
        """

    def refresh(self):
        self.tableWidget.setRowCount(0)
        for i in self.r._get_rules():
            item = QtGui.QTableWidgetItem()
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(rowPosition , 0, QtGui.QTableWidgetItem(i["src_ip"]))
            self.tableWidget.setItem(rowPosition , 1, QtGui.QTableWidgetItem(i["src_port"]))
            self.tableWidget.setItem(rowPosition , 2, QtGui.QTableWidgetItem(i["dst_ip"]))
            self.tableWidget.setItem(rowPosition , 3, QtGui.QTableWidgetItem(i["dst_port"]))
            self.tableWidget.setItem(rowPosition , 4, QtGui.QTableWidgetItem(i["flg"]))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.init()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
