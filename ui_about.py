# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_about.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_About_From(object):
    def setupUi(self, About_From):
        if not About_From.objectName():
            About_From.setObjectName(u"About_From")
        About_From.resize(372, 433)
        self.verticalLayout = QVBoxLayout(About_From)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 6, 1, 1)

        self.lbl_programName = QLabel(About_From)
        self.lbl_programName.setObjectName(u"lbl_programName")
        font = QFont()
        font.setPointSize(18)
        self.lbl_programName.setFont(font)
        self.lbl_programName.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbl_programName, 0, 0, 1, 9)

        self.label_3 = QLabel(About_From)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.label_3, 1, 7, 1, 1)

        self.btn_close = QPushButton(About_From)
        self.btn_close.setObjectName(u"btn_close")

        self.gridLayout.addWidget(self.btn_close, 5, 0, 1, 9)

        self.lbl_update = QLabel(About_From)
        self.lbl_update.setObjectName(u"lbl_update")
        self.lbl_update.setMinimumSize(QSize(100, 0))

        self.gridLayout.addWidget(self.lbl_update, 1, 8, 1, 1)

        self.label_6 = QLabel(About_From)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 2)

        self.textBrowser = QTextBrowser(About_From)
        self.textBrowser.setObjectName(u"textBrowser")

        self.gridLayout.addWidget(self.textBrowser, 4, 0, 1, 9)

        self.label_7 = QLabel(About_From)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.label_7, 2, 7, 1, 1)

        self.lbl_maker = QLabel(About_From)
        self.lbl_maker.setObjectName(u"lbl_maker")

        self.gridLayout.addWidget(self.lbl_maker, 2, 2, 1, 5)

        self.label_2 = QLabel(About_From)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)

        self.lbl_ver = QLabel(About_From)
        self.lbl_ver.setObjectName(u"lbl_ver")

        self.gridLayout.addWidget(self.lbl_ver, 1, 2, 1, 4)

        self.btn_homePage = QPushButton(About_From)
        self.btn_homePage.setObjectName(u"btn_homePage")

        self.gridLayout.addWidget(self.btn_homePage, 2, 8, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(About_From)

        QMetaObject.connectSlotsByName(About_From)
    # setupUi

    def retranslateUi(self, About_From):
        About_From.setWindowTitle(QCoreApplication.translate("About_From", u"About", None))
        self.lbl_programName.setText(QCoreApplication.translate("About_From", u"Schedule Player", None))
        self.label_3.setText(QCoreApplication.translate("About_From", u"Update :", None))
        self.btn_close.setText(QCoreApplication.translate("About_From", u"\ub2eb \uae30", None))
        self.lbl_update.setText(QCoreApplication.translate("About_From", u"2022.06.12", None))
        self.label_6.setText(QCoreApplication.translate("About_From", u"\uc81c\uc791\uc790 :", None))
        self.textBrowser.setHtml(QCoreApplication.translate("About_From", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'\ub9d1\uc740 \uace0\ub515'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- \uc81c\uc791 \ud6c4\uae30</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> \uac1c\ubc1c \uae30\uac04\uc740 \uacf5\ubd80\ud558\uba74\uc11c \uc2e4\ud328\ud55c \ud504\ub85c\uc81d\ud2b8\ub97c \ud3ec\ud568\ud574\uc11c 6\uac1c\uc6d4 \uc815\ub3c4 \uac78\ub838\uc2b5\ub2c8\ub2e4.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\uac1c"
                        "\uc778\uc801\uc778 \uc218\uc5c5\uacfc \ubc29\uc1a1 \uc5c5\ubb34\ub97c \uc704\ud574 \uac1c\ubc1c\uc744 \uc2dc\uc791\ud558\uc600\uc9c0\ub9cc, \uac1c\ubc1c \uae30\uac04 \ub3d9\uc548 \uc0b4\uc744 \uae4e\uc544\ub0b4\ub294 \uace0\ud1b5\uc744 \uc218\ubc18\ud558\ub294 \ud798\ub4e0 \uacfc\uc815\uc774\ub77c\ub294 \uac83\uc744 \uae68\ub2ec\uc558\uc2b5\ub2c8\ub2e4. \uc2e4\uc81c, \uc774 \uacfc\uc815 \ub3d9\uc548 \ub450\ud1b5\uc5d0 \uc2dc\ub2ec\ub9ac\uace0 \uccb4\uc911\ub3c4 \ub9ce\uc774 \uc904\uc5b4\ub4e4\uc5b4 \ud798\ub4e4\uc5c8\uc2b5\ub2c8\ub2e4. \uc18c\ud504\ud2b8\uc6e8\uc5b4 \uac1c\ubc1c\uc5d0 \uc885\uc0ac\ud558\uc2dc\ub294 \ubaa8\ub4e0 \ubd84\uaed8 \uc874\uacbd\uc744 \ud45c\ud569\ub2c8\ub2e4.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- \uc54c\ub824\uc9c4 \ubc84\uadf8</p>\n"
""
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> \ud55c\uae00 \uc30d\uc790\uc74c \uc785\ub825 \ubc84\uadf8\uac00 \uc788\uc2b5\ub2c8\ub2e4. Pyside6 \ubaa8\ub4c8 \uc790\uccb4\uc758 \ubb38\uc81c\ub85c Pyside \uc7ac\ub2e8 \uce21\uc5d0\uc11c \ubb38\uc81c\ub97c \uc778\uc2dd\ud558\uace0 \ud574\uacb0\ud558\uc9c0 \uc54a\ub294 \uc774\uc0c1 \ud574\uacb0 \ubc29\ubc95\uc774 \uc5c6\uc5b4\uc11c \uae30\ub2e4\ub9ac\ub294 \uc218\ubc16\uc5d0 \uc5c6\uc2b5\ub2c8\ub2e4.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- \uac1c\ubc1c\ud658\uacbd : VS code, Python 3.10, Pyside 6.3</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- \ub77c\uc774\uc120"
                        "\uc2a4 : MIT License</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- 2022. 06. 12 \uace0\uc2e4\uc911\ud559\uad50\uc5d0\uc11c</p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("About_From", u"\ud648\ud398\uc774\uc9c0:", None))
        self.lbl_maker.setText(QCoreApplication.translate("About_From", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("About_From", u"Ver :", None))
        self.lbl_ver.setText(QCoreApplication.translate("About_From", u"TextLabel", None))
        self.btn_homePage.setText(QCoreApplication.translate("About_From", u"Text", None))
    # retranslateUi

