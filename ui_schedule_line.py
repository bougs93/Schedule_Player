# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_schedule_line.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QTimeEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(964, 30)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(0, 30))
        Form.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 0, 961, 31))
        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(2, 0, 961, 32))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(4, 0, 4, 0)
        self.cb_enable = QCheckBox(self.horizontalLayoutWidget)
        self.cb_enable.setObjectName(u"cb_enable")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cb_enable.sizePolicy().hasHeightForWidth())
        self.cb_enable.setSizePolicy(sizePolicy1)
        self.cb_enable.setMinimumSize(QSize(50, 20))
        self.cb_enable.setMaximumSize(QSize(50, 20))
        self.cb_enable.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.cb_enable)

        self.btn_play = QPushButton(self.horizontalLayoutWidget)
        self.btn_play.setObjectName(u"btn_play")
        self.btn_play.setMaximumSize(QSize(25, 16777215))

        self.horizontalLayout.addWidget(self.btn_play)

        self.le_name = QLineEdit(self.horizontalLayoutWidget)
        self.le_name.setObjectName(u"le_name")
        self.le_name.setMinimumSize(QSize(90, 0))
        self.le_name.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout.addWidget(self.le_name)

        self.te_setTime = QTimeEdit(self.horizontalLayoutWidget)
        self.te_setTime.setObjectName(u"te_setTime")
        self.te_setTime.setMinimumSize(QSize(80, 0))
        self.te_setTime.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout.addWidget(self.te_setTime)

        self.lbl_before = QLabel(self.horizontalLayoutWidget)
        self.lbl_before.setObjectName(u"lbl_before")
        sizePolicy1.setHeightForWidth(self.lbl_before.sizePolicy().hasHeightForWidth())
        self.lbl_before.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.lbl_before.setFont(font)

        self.horizontalLayout.addWidget(self.lbl_before)

        self.te_beforeTime = QTimeEdit(self.horizontalLayoutWidget)
        self.te_beforeTime.setObjectName(u"te_beforeTime")
        sizePolicy1.setHeightForWidth(self.te_beforeTime.sizePolicy().hasHeightForWidth())
        self.te_beforeTime.setSizePolicy(sizePolicy1)
        self.te_beforeTime.setMinimumSize(QSize(0, 0))
        self.te_beforeTime.setMaximumSize(QSize(16777215, 16777215))
        self.te_beforeTime.setBaseSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.te_beforeTime)

        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.btn_autoPlay = QPushButton(self.horizontalLayoutWidget)
        self.btn_autoPlay.setObjectName(u"btn_autoPlay")
        self.btn_autoPlay.setMaximumSize(QSize(25, 16777215))
        self.btn_autoPlay.setCheckable(True)

        self.horizontalLayout.addWidget(self.btn_autoPlay)

        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.rb_selInPlayer = QRadioButton(self.horizontalLayoutWidget)
        self.rb_selInPlayer.setObjectName(u"rb_selInPlayer")

        self.horizontalLayout.addWidget(self.rb_selInPlayer)

        self.rb_selWinPlayer = QRadioButton(self.horizontalLayoutWidget)
        self.rb_selWinPlayer.setObjectName(u"rb_selWinPlayer")

        self.horizontalLayout.addWidget(self.rb_selWinPlayer)

        self.rb_selUserPlayer = QRadioButton(self.horizontalLayoutWidget)
        self.rb_selUserPlayer.setObjectName(u"rb_selUserPlayer")

        self.horizontalLayout.addWidget(self.rb_selUserPlayer)

        self.btn_setPlayer = QPushButton(self.horizontalLayoutWidget)
        self.btn_setPlayer.setObjectName(u"btn_setPlayer")
        sizePolicy1.setHeightForWidth(self.btn_setPlayer.sizePolicy().hasHeightForWidth())
        self.btn_setPlayer.setSizePolicy(sizePolicy1)
        self.btn_setPlayer.setMaximumSize(QSize(33, 16777215))

        self.horizontalLayout.addWidget(self.btn_setPlayer)

        self.lbl_setPlayer = QLabel(self.horizontalLayoutWidget)
        self.lbl_setPlayer.setObjectName(u"lbl_setPlayer")
        self.lbl_setPlayer.setMinimumSize(QSize(90, 0))
        self.lbl_setPlayer.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout.addWidget(self.lbl_setPlayer)

        self.btn_setFile = QPushButton(self.horizontalLayoutWidget)
        self.btn_setFile.setObjectName(u"btn_setFile")
        sizePolicy1.setHeightForWidth(self.btn_setFile.sizePolicy().hasHeightForWidth())
        self.btn_setFile.setSizePolicy(sizePolicy1)
        self.btn_setFile.setMaximumSize(QSize(33, 16777215))

        self.horizontalLayout.addWidget(self.btn_setFile)

        self.lbl_setFile = QLabel(self.horizontalLayoutWidget)
        self.lbl_setFile.setObjectName(u"lbl_setFile")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lbl_setFile.sizePolicy().hasHeightForWidth())
        self.lbl_setFile.setSizePolicy(sizePolicy2)
        self.lbl_setFile.setMinimumSize(QSize(0, 0))
        self.lbl_setFile.setMaximumSize(QSize(16777215, 20))
        self.lbl_setFile.setStyleSheet(u"")
        self.lbl_setFile.setMargin(4)

        self.horizontalLayout.addWidget(self.lbl_setFile)

        self.btn_clear = QPushButton(self.horizontalLayoutWidget)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout.addWidget(self.btn_clear)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle("")
        self.cb_enable.setText(QCoreApplication.translate("Form", u"00:00", None))
        self.btn_play.setText(QCoreApplication.translate("Form", u"\u25b7", None))
        self.le_name.setText(QCoreApplication.translate("Form", u"\uc77c\uc815 \uc81c\ubaa9", None))
        self.te_setTime.setDisplayFormat(QCoreApplication.translate("Form", u"ap hh:mm", None))
        self.lbl_before.setText(QCoreApplication.translate("Form", u"-", None))
        self.te_beforeTime.setDisplayFormat(QCoreApplication.translate("Form", u"m:ss", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\ucd08", None))
        self.btn_autoPlay.setText(QCoreApplication.translate("Form", u"A", None))
        self.label.setText("")
        self.rb_selInPlayer.setText(QCoreApplication.translate("Form", u"I", None))
        self.rb_selWinPlayer.setText(QCoreApplication.translate("Form", u"W", None))
        self.rb_selUserPlayer.setText(QCoreApplication.translate("Form", u"U", None))
        self.btn_setPlayer.setText(QCoreApplication.translate("Form", u"PLY", None))
        self.lbl_setPlayer.setText(QCoreApplication.translate("Form", u"\ud50c\ub808\uc774\uc5b4 \uc774\ub984", None))
        self.btn_setFile.setText(QCoreApplication.translate("Form", u"File", None))
        self.lbl_setFile.setText(QCoreApplication.translate("Form", u"\uc7ac\uc0dd\ud560 mp3 \ud30c\uc77c \uc774\ub984", None))
        self.btn_clear.setText(QCoreApplication.translate("Form", u"CLR", None))
    # retranslateUi

