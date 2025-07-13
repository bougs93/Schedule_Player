# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mini_mp3player.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_mini_mp3player(object):
    def setupUi(self, mini_mp3player):
        if not mini_mp3player.objectName():
            mini_mp3player.setObjectName(u"mini_mp3player")
        mini_mp3player.resize(1004, 80)
        self.verticalLayout_2 = QVBoxLayout(mini_mp3player)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(mini_mp3player)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(35, 0))
        self.label_2.setMaximumSize(QSize(35, 16777215))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.lbl_audioOut = QLabel(self.groupBox)
        self.lbl_audioOut.setObjectName(u"lbl_audioOut")
        self.lbl_audioOut.setMinimumSize(QSize(100, 0))
        self.lbl_audioOut.setMaximumSize(QSize(400, 16777215))

        self.horizontalLayout.addWidget(self.lbl_audioOut)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(35, 0))
        self.label.setMaximumSize(QSize(35, 16777215))
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.lbl_playFile = QLabel(self.groupBox)
        self.lbl_playFile.setObjectName(u"lbl_playFile")
        self.lbl_playFile.setMinimumSize(QSize(200, 0))

        self.horizontalLayout.addWidget(self.lbl_playFile)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.lbl_startTime = QLabel(self.groupBox)
        self.lbl_startTime.setObjectName(u"lbl_startTime")
        self.lbl_startTime.setMinimumSize(QSize(30, 0))
        self.lbl_startTime.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_2.addWidget(self.lbl_startTime)

        self.slider = QSlider(self.groupBox)
        self.slider.setObjectName(u"slider")
        self.slider.setMinimumSize(QSize(300, 0))
        self.slider.setMaximumSize(QSize(300, 16777215))
        self.slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.slider)

        self.lbl_endTime = QLabel(self.groupBox)
        self.lbl_endTime.setObjectName(u"lbl_endTime")
        self.lbl_endTime.setMinimumSize(QSize(30, 0))
        self.lbl_endTime.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_2.addWidget(self.lbl_endTime)


        self.horizontalLayout.addLayout(self.horizontalLayout_2)

        self.btn_play = QPushButton(self.groupBox)
        self.btn_play.setObjectName(u"btn_play")
        self.btn_play.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout.addWidget(self.btn_play)

        self.btn_stop = QPushButton(self.groupBox)
        self.btn_stop.setObjectName(u"btn_stop")
        self.btn_stop.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout.addWidget(self.btn_stop)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.groupBox)


        self.retranslateUi(mini_mp3player)

        QMetaObject.connectSlotsByName(mini_mp3player)
    # setupUi

    def retranslateUi(self, mini_mp3player):
        mini_mp3player.setWindowTitle(QCoreApplication.translate("mini_mp3player", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("mini_mp3player", u"(I)\uc778 \ud50c\ub808\uc774\uc5b4 (Mini)", None))
        self.label_2.setText(QCoreApplication.translate("mini_mp3player", u"\ucd9c\ub825:", None))
        self.lbl_audioOut.setText(QCoreApplication.translate("mini_mp3player", u"output file", None))
        self.label.setText(QCoreApplication.translate("mini_mp3player", u"\ud30c\uc77c:", None))
        self.lbl_playFile.setText("")
        self.lbl_startTime.setText(QCoreApplication.translate("mini_mp3player", u"00:00", None))
        self.lbl_endTime.setText(QCoreApplication.translate("mini_mp3player", u"00:00", None))
        self.btn_play.setText(QCoreApplication.translate("mini_mp3player", u"Play", None))
        self.btn_stop.setText(QCoreApplication.translate("mini_mp3player", u"Stop", None))
    # retranslateUi

