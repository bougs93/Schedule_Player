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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTimeEdit,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(931, 33)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(0, 33))
        Form.setMaximumSize(QSize(16777215, 33))
        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(3, 0, 921, 32))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl_before = QLabel(self.horizontalLayoutWidget)
        self.lbl_before.setObjectName(u"lbl_before")
        sizePolicy.setHeightForWidth(self.lbl_before.sizePolicy().hasHeightForWidth())
        self.lbl_before.setSizePolicy(sizePolicy)
        self.lbl_before.setMinimumSize(QSize(50, 28))
        self.lbl_before.setMaximumSize(QSize(50, 28))
        self.lbl_before.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.lbl_before)

        self.btn_play = QPushButton(self.horizontalLayoutWidget)
        self.btn_play.setObjectName(u"btn_play")
        self.btn_play.setMaximumSize(QSize(25, 16777215))

        self.horizontalLayout.addWidget(self.btn_play)

        self.le_name = QLineEdit(self.horizontalLayoutWidget)
        self.le_name.setObjectName(u"le_name")
        self.le_name.setMinimumSize(QSize(150, 0))
        self.le_name.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout.addWidget(self.le_name)

        self.te_setTime = QTimeEdit(self.horizontalLayoutWidget)
        self.te_setTime.setObjectName(u"te_setTime")
        self.te_setTime.setMinimumSize(QSize(80, 0))
        self.te_setTime.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout.addWidget(self.te_setTime)

        self.te_beforeTime = QTimeEdit(self.horizontalLayoutWidget)
        self.te_beforeTime.setObjectName(u"te_beforeTime")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.te_beforeTime.sizePolicy().hasHeightForWidth())
        self.te_beforeTime.setSizePolicy(sizePolicy1)
        self.te_beforeTime.setMinimumSize(QSize(0, 0))
        self.te_beforeTime.setMaximumSize(QSize(16777215, 16777215))
        self.te_beforeTime.setBaseSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.te_beforeTime)

        self.label_3 = QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.label_3)

        self.cb_autoPlay = QCheckBox(self.horizontalLayoutWidget)
        self.cb_autoPlay.setObjectName(u"cb_autoPlay")
        sizePolicy1.setHeightForWidth(self.cb_autoPlay.sizePolicy().hasHeightForWidth())
        self.cb_autoPlay.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.cb_autoPlay)

        self.btn_setPlayer = QPushButton(self.horizontalLayoutWidget)
        self.btn_setPlayer.setObjectName(u"btn_setPlayer")
        sizePolicy1.setHeightForWidth(self.btn_setPlayer.sizePolicy().hasHeightForWidth())
        self.btn_setPlayer.setSizePolicy(sizePolicy1)
        self.btn_setPlayer.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout.addWidget(self.btn_setPlayer)

        self.lbl_setPlayer = QLabel(self.horizontalLayoutWidget)
        self.lbl_setPlayer.setObjectName(u"lbl_setPlayer")
        self.lbl_setPlayer.setMinimumSize(QSize(80, 0))
        self.lbl_setPlayer.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout.addWidget(self.lbl_setPlayer)

        self.btn_setFile = QPushButton(self.horizontalLayoutWidget)
        self.btn_setFile.setObjectName(u"btn_setFile")
        sizePolicy1.setHeightForWidth(self.btn_setFile.sizePolicy().hasHeightForWidth())
        self.btn_setFile.setSizePolicy(sizePolicy1)
        self.btn_setFile.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout.addWidget(self.btn_setFile)

        self.lbl_setFile = QLabel(self.horizontalLayoutWidget)
        self.lbl_setFile.setObjectName(u"lbl_setFile")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lbl_setFile.sizePolicy().hasHeightForWidth())
        self.lbl_setFile.setSizePolicy(sizePolicy2)
        self.lbl_setFile.setMinimumSize(QSize(0, 0))
        self.lbl_setFile.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.lbl_setFile)

        self.btn_curDel = QPushButton(self.horizontalLayoutWidget)
        self.btn_curDel.setObjectName(u"btn_curDel")
        sizePolicy1.setHeightForWidth(self.btn_curDel.sizePolicy().hasHeightForWidth())
        self.btn_curDel.setSizePolicy(sizePolicy1)
        self.btn_curDel.setMaximumSize(QSize(30, 16777215))
        self.btn_curDel.setBaseSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.btn_curDel)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lbl_before.setText(QCoreApplication.translate("Form", u"3\ubd8400\ucd08", None))
        self.btn_play.setText(QCoreApplication.translate("Form", u"\u25b7", None))
        self.le_name.setText(QCoreApplication.translate("Form", u"\uc77c\uc815 \uc81c\ubaa9", None))
        self.te_setTime.setDisplayFormat(QCoreApplication.translate("Form", u"ap hh:mm", None))
        self.te_beforeTime.setDisplayFormat(QCoreApplication.translate("Form", u"m:ss", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\ucd08 \uc804", None))
        self.cb_autoPlay.setText(QCoreApplication.translate("Form", u"\uc7ac\uc0dd", None))
        self.btn_setPlayer.setText(QCoreApplication.translate("Form", u"PLAYER", None))
        self.lbl_setPlayer.setText(QCoreApplication.translate("Form", u"\ud50c\ub808\uc774\uc5b4 \uc774\ub984", None))
        self.btn_setFile.setText(QCoreApplication.translate("Form", u"\ud30c\uc77c", None))
        self.lbl_setFile.setText(QCoreApplication.translate("Form", u"\uc7ac\uc0dd\ud560 mp3 \ud30c\uc77c \uc774\ub984", None))
        self.btn_curDel.setText(QCoreApplication.translate("Form", u"DEL", None))
    # retranslateUi

