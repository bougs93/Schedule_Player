# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mp3player.ui'
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
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QVBoxLayout, QWidget)

class Ui_mp3player(object):
    def setupUi(self, mp3player):
        if not mp3player.objectName():
            mp3player.setObjectName(u"mp3player")
        mp3player.resize(1003, 226)
        self.verticalLayout_4 = QVBoxLayout(mp3player)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gb_miniPlayer = QGroupBox(mp3player)
        self.gb_miniPlayer.setObjectName(u"gb_miniPlayer")
        self.verticalLayout_5 = QVBoxLayout(self.gb_miniPlayer)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.gb_miniPlayer)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(35, 0))
        self.label_3.setMaximumSize(QSize(35, 16777215))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_3)

        self.lbl_maudioOut = QLabel(self.gb_miniPlayer)
        self.lbl_maudioOut.setObjectName(u"lbl_maudioOut")
        self.lbl_maudioOut.setMinimumSize(QSize(60, 0))
        self.lbl_maudioOut.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_6.addWidget(self.lbl_maudioOut)

        self.label_5 = QLabel(self.gb_miniPlayer)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.label_4 = QLabel(self.gb_miniPlayer)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(35, 0))
        self.label_4.setMaximumSize(QSize(35, 16777215))
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_4)

        self.lbl_mplayFile = QLabel(self.gb_miniPlayer)
        self.lbl_mplayFile.setObjectName(u"lbl_mplayFile")
        self.lbl_mplayFile.setMinimumSize(QSize(200, 0))
        self.lbl_mplayFile.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_6.addWidget(self.lbl_mplayFile)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_6 = QLabel(self.gb_miniPlayer)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_7.addWidget(self.label_6)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)

        self.lbl_mstartTime = QLabel(self.gb_miniPlayer)
        self.lbl_mstartTime.setObjectName(u"lbl_mstartTime")
        self.lbl_mstartTime.setMinimumSize(QSize(30, 0))
        self.lbl_mstartTime.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_7.addWidget(self.lbl_mstartTime)

        self.slider_mprogress = QSlider(self.gb_miniPlayer)
        self.slider_mprogress.setObjectName(u"slider_mprogress")
        self.slider_mprogress.setMinimumSize(QSize(250, 0))
        self.slider_mprogress.setMaximumSize(QSize(250, 16777215))
        self.slider_mprogress.setOrientation(Qt.Horizontal)

        self.horizontalLayout_7.addWidget(self.slider_mprogress)

        self.lbl_mendTime = QLabel(self.gb_miniPlayer)
        self.lbl_mendTime.setObjectName(u"lbl_mendTime")
        self.lbl_mendTime.setMinimumSize(QSize(30, 0))
        self.lbl_mendTime.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_7.addWidget(self.lbl_mendTime)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_7)

        self.btn_mplay = QPushButton(self.gb_miniPlayer)
        self.btn_mplay.setObjectName(u"btn_mplay")
        self.btn_mplay.setEnabled(False)
        self.btn_mplay.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_6.addWidget(self.btn_mplay)

        self.btn_mstop = QPushButton(self.gb_miniPlayer)
        self.btn_mstop.setObjectName(u"btn_mstop")
        self.btn_mstop.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_6.addWidget(self.btn_mstop)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)


        self.verticalLayout_4.addWidget(self.gb_miniPlayer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.gb_fullPlayer1 = QGroupBox(mp3player)
        self.gb_fullPlayer1.setObjectName(u"gb_fullPlayer1")
        self.gb_fullPlayer1.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.gb_fullPlayer1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.list_music = QListWidget(self.gb_fullPlayer1)
        self.list_music.setObjectName(u"list_music")

        self.verticalLayout_2.addWidget(self.list_music)


        self.horizontalLayout_4.addWidget(self.gb_fullPlayer1)

        self.gb_fullPlayer2 = QGroupBox(mp3player)
        self.gb_fullPlayer2.setObjectName(u"gb_fullPlayer2")
        self.gb_fullPlayer2.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.gb_fullPlayer2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.gb_fullPlayer2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(60, 0))
        self.label.setMaximumSize(QSize(60, 16777215))
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.lbl_playFile = QLabel(self.gb_fullPlayer2)
        self.lbl_playFile.setObjectName(u"lbl_playFile")

        self.horizontalLayout_3.addWidget(self.lbl_playFile)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.gb_fullPlayer2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(60, 0))
        self.label_2.setMaximumSize(QSize(60, 16777215))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_2)

        self.lbl_audioOut = QLabel(self.gb_fullPlayer2)
        self.lbl_audioOut.setObjectName(u"lbl_audioOut")
        self.lbl_audioOut.setMaximumSize(QSize(400, 16777215))

        self.horizontalLayout_5.addWidget(self.lbl_audioOut)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_startTime = QLabel(self.gb_fullPlayer2)
        self.lbl_startTime.setObjectName(u"lbl_startTime")

        self.horizontalLayout_2.addWidget(self.lbl_startTime)

        self.slider_progress = QSlider(self.gb_fullPlayer2)
        self.slider_progress.setObjectName(u"slider_progress")
        self.slider_progress.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.slider_progress)

        self.lbl_endTime = QLabel(self.gb_fullPlayer2)
        self.lbl_endTime.setObjectName(u"lbl_endTime")

        self.horizontalLayout_2.addWidget(self.lbl_endTime)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_pre = QPushButton(self.gb_fullPlayer2)
        self.btn_pre.setObjectName(u"btn_pre")
        self.btn_pre.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout.addWidget(self.btn_pre)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_play = QPushButton(self.gb_fullPlayer2)
        self.btn_play.setObjectName(u"btn_play")
        self.btn_play.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout.addWidget(self.btn_play)

        self.btn_stop = QPushButton(self.gb_fullPlayer2)
        self.btn_stop.setObjectName(u"btn_stop")
        self.btn_stop.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout.addWidget(self.btn_stop)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.btn_next = QPushButton(self.gb_fullPlayer2)
        self.btn_next.setObjectName(u"btn_next")
        self.btn_next.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout.addWidget(self.btn_next)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.horizontalLayout_4.addWidget(self.gb_fullPlayer2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)


        self.retranslateUi(mp3player)

        QMetaObject.connectSlotsByName(mp3player)
    # setupUi

    def retranslateUi(self, mp3player):
        mp3player.setWindowTitle(QCoreApplication.translate("mp3player", u"Form", None))
        self.gb_miniPlayer.setTitle(QCoreApplication.translate("mp3player", u"(I)\uc778 \ud50c\ub808\uc774\uc5b4 (Mini)", None))
        self.label_3.setText(QCoreApplication.translate("mp3player", u"\ucd9c\ub825:", None))
        self.lbl_maudioOut.setText("")
        self.label_5.setText("")
        self.label_4.setText(QCoreApplication.translate("mp3player", u"\ud30c\uc77c:", None))
        self.lbl_mplayFile.setText("")
        self.label_6.setText("")
        self.lbl_mstartTime.setText(QCoreApplication.translate("mp3player", u"00:00", None))
        self.lbl_mendTime.setText(QCoreApplication.translate("mp3player", u"00:00", None))
        self.btn_mplay.setText(QCoreApplication.translate("mp3player", u"Play", None))
        self.btn_mstop.setText(QCoreApplication.translate("mp3player", u"Stop", None))
        self.gb_fullPlayer1.setTitle(QCoreApplication.translate("mp3player", u"\uc74c\uc6d0 \ubaa9\ub85d", None))
        self.gb_fullPlayer2.setTitle(QCoreApplication.translate("mp3player", u"(I)\uc778 \ud50c\ub808\uc774\uc5b4 (Full)", None))
        self.label.setText(QCoreApplication.translate("mp3player", u"\ud30c\uc77c\uc774\ub984:", None))
        self.lbl_playFile.setText("")
        self.label_2.setText(QCoreApplication.translate("mp3player", u"\ucd9c\ub825\uc7a5\uce58:", None))
        self.lbl_audioOut.setText("")
        self.lbl_startTime.setText(QCoreApplication.translate("mp3player", u"00:00", None))
        self.lbl_endTime.setText(QCoreApplication.translate("mp3player", u"00:00", None))
        self.btn_pre.setText(QCoreApplication.translate("mp3player", u"Prev", None))
        self.btn_play.setText(QCoreApplication.translate("mp3player", u"Play", None))
        self.btn_stop.setText(QCoreApplication.translate("mp3player", u"Stop", None))
        self.btn_next.setText(QCoreApplication.translate("mp3player", u"Next", None))
    # retranslateUi

