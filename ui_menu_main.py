# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_menu_main.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QRadioButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1008, 444)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionLoad = QAction(MainWindow)
        self.actionLoad.setObjectName(u"actionLoad")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_As = QAction(MainWindow)
        self.actionSave_As.setObjectName(u"actionSave_As")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout1 = QVBoxLayout()
        self.verticalLayout1.setObjectName(u"verticalLayout1")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gb_timeView = QGroupBox(self.centralwidget)
        self.gb_timeView.setObjectName(u"gb_timeView")
        self.gb_timeView.setMinimumSize(QSize(330, 0))
        self.gb_timeView.setMaximumSize(QSize(330, 100))
        self.gb_timeView.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.horizontalLayout_2 = QHBoxLayout(self.gb_timeView)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.wg_timeView = QWidget(self.gb_timeView)
        self.wg_timeView.setObjectName(u"wg_timeView")
        self.horizontalLayout_3 = QHBoxLayout(self.wg_timeView)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbl_time1 = QLabel(self.wg_timeView)
        self.lbl_time1.setObjectName(u"lbl_time1")
        sizePolicy.setHeightForWidth(self.lbl_time1.sizePolicy().hasHeightForWidth())
        self.lbl_time1.setSizePolicy(sizePolicy)
        self.lbl_time1.setMinimumSize(QSize(0, 0))
        self.lbl_time1.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(40)
        font.setBold(True)
        self.lbl_time1.setFont(font)
        self.lbl_time1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lbl_time1)

        self.lbl_time2 = QLabel(self.wg_timeView)
        self.lbl_time2.setObjectName(u"lbl_time2")
        self.lbl_time2.setMinimumSize(QSize(0, 55))
        self.lbl_time2.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setPointSize(25)
        font1.setBold(True)
        self.lbl_time2.setFont(font1)
        self.lbl_time2.setStyleSheet(u"color: rgb(0, 0, 255);")
        self.lbl_time2.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.horizontalLayout_3.addWidget(self.lbl_time2)


        self.horizontalLayout_2.addWidget(self.wg_timeView)


        self.gridLayout.addWidget(self.gb_timeView, 0, 0, 2, 1)

        self.btn_reload = QPushButton(self.centralwidget)
        self.btn_reload.setObjectName(u"btn_reload")
        self.btn_reload.setMaximumSize(QSize(60, 16777215))

        self.gridLayout.addWidget(self.btn_reload, 1, 4, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 6, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 12, 1, 1)

        self.cb_timeColor = QCheckBox(self.centralwidget)
        self.cb_timeColor.setObjectName(u"cb_timeColor")

        self.gridLayout.addWidget(self.cb_timeColor, 1, 1, 1, 1)

        self.btn_add = QPushButton(self.centralwidget)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setMaximumSize(QSize(45, 16777215))

        self.gridLayout.addWidget(self.btn_add, 1, 13, 1, 1)

        self.btn_save = QPushButton(self.centralwidget)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setMaximumSize(QSize(60, 16777215))

        self.gridLayout.addWidget(self.btn_save, 1, 5, 1, 1)

        self.btn_del = QPushButton(self.centralwidget)
        self.btn_del.setObjectName(u"btn_del")
        self.btn_del.setMaximumSize(QSize(45, 16777215))

        self.gridLayout.addWidget(self.btn_del, 1, 14, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.btn_reset = QPushButton(self.centralwidget)
        self.btn_reset.setObjectName(u"btn_reset")
        self.btn_reset.setMinimumSize(QSize(50, 0))
        self.btn_reset.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.btn_reset, 1, 2, 1, 1)

        self.rb_selFullPlayer = QRadioButton(self.centralwidget)
        self.rb_selFullPlayer.setObjectName(u"rb_selFullPlayer")
        self.rb_selFullPlayer.setMaximumSize(QSize(35, 16777215))
        self.rb_selFullPlayer.setCheckable(True)

        self.gridLayout.addWidget(self.rb_selFullPlayer, 1, 10, 1, 1)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 0))
        self.groupBox_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lbl_schName = QLabel(self.groupBox_2)
        self.lbl_schName.setObjectName(u"lbl_schName")
        font2 = QFont()
        font2.setPointSize(15)
        self.lbl_schName.setFont(font2)

        self.verticalLayout_3.addWidget(self.lbl_schName)


        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 6)

        self.rb_selMiniPlayer = QRadioButton(self.centralwidget)
        self.rb_selMiniPlayer.setObjectName(u"rb_selMiniPlayer")
        self.rb_selMiniPlayer.setMaximumSize(QSize(35, 16777215))
        self.rb_selMiniPlayer.setCheckable(True)

        self.gridLayout.addWidget(self.rb_selMiniPlayer, 1, 9, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 11, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 7, 1, 2)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(250, 0))
        self.groupBox_3.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.verticalLayout = QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_today = QLabel(self.groupBox_3)
        self.lbl_today.setObjectName(u"lbl_today")
        font3 = QFont()
        font3.setPointSize(22)
        font3.setBold(True)
        self.lbl_today.setFont(font3)
        self.lbl_today.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_today)


        self.gridLayout.addWidget(self.groupBox_3, 0, 7, 1, 8)


        self.verticalLayout1.addLayout(self.gridLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout1)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 971, 258))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.verticalLayout2 = QVBoxLayout()
        self.verticalLayout2.setObjectName(u"verticalLayout2")

        self.verticalLayout_2.addLayout(self.verticalLayout2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1008, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_setup = QMenu(self.menubar)
        self.menu_setup.setObjectName(u"menu_setup")
        self.menuabout = QMenu(self.menubar)
        self.menuabout.setObjectName(u"menuabout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_setup.menuAction())
        self.menubar.addAction(self.menuabout.menuAction())
        self.menu.addAction(self.actionNew)
        self.menu.addAction(self.actionLoad)
        self.menu.addAction(self.actionSave)
        self.menu.addAction(self.actionSave_As)
        self.menu.addSeparator()
        self.menu.addAction(self.actionExit)
        self.menuabout.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)
        self.btn_add.clicked.connect(MainWindow.schAdd)
        self.btn_del.clicked.connect(MainWindow.schDel)
        self.btn_reset.clicked.connect(MainWindow.playedReset)
        self.btn_reload.clicked.connect(MainWindow.btnFileLoad)
        self.btn_save.clicked.connect(MainWindow.btnFileSave)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"From", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionLoad.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionSave_As.setText(QCoreApplication.translate("MainWindow", u"Save as", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"\uc815\ubcf4", None))
        self.gb_timeView.setTitle(QCoreApplication.translate("MainWindow", u"\ud604\uc7ac\uc2dc\uac04", None))
        self.lbl_time1.setText(QCoreApplication.translate("MainWindow", u"AM 12:00", None))
        self.lbl_time2.setText(QCoreApplication.translate("MainWindow", u".00", None))
        self.btn_reload.setText(QCoreApplication.translate("MainWindow", u"RELOAD", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\uc77c\uc815:", None))
        self.cb_timeColor.setText(QCoreApplication.translate("MainWindow", u"\uc0c9\uc0c1\uc54c\ub78c", None))
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"SAVE", None))
        self.btn_del.setText(QCoreApplication.translate("MainWindow", u"DEL", None))
        self.btn_reset.setText(QCoreApplication.translate("MainWindow", u"\u25cf\u2192\u25b7", None))
        self.rb_selFullPlayer.setText(QCoreApplication.translate("MainWindow", u"\u25bd", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\ud604\uc7ac \uc2a4\ucf00\uc904", None))
        self.lbl_schName.setText(QCoreApplication.translate("MainWindow", u"\uc774\ub984 \uc5c6\uc74c", None))
        self.rb_selMiniPlayer.setText(QCoreApplication.translate("MainWindow", u"\u25b3", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\uc778 \ud50c\ub808\uc774\uc5b4", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"today", None))
        self.lbl_today.setText(QCoreApplication.translate("MainWindow", u"DATE", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c", None))
        self.menu_setup.setTitle(QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
        self.menuabout.setTitle(QCoreApplication.translate("MainWindow", u"?", None))
    # retranslateUi

