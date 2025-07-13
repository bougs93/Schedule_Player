'''
<설정 기능>

-> 설정/음원파일 하위 폴더에 있는 경우, 상대경로로 위치 저장하고, 상대 경로 로딩하기

항상 top
색상 알림시 top
색상알람시, 소리, 출력장치, 음원 선택 기능, 볼륨 선택
tray icon 기능


요일별 자동로딩
설정 방법 고민

OK 파일 로드시, SAVE DATA 추가 오늘날짜가 아닌 경우, played 체크 해제
OK 폴더 변경시, 우선 현재 폴더 검색후, 파일 검사 -> 확인 요망
OK 자체 MP3 플레이어 테스트 및 추가하기



'''

import copy
import os, sys, datetime, pickle, webbrowser, subprocess
import ssl
import pathlib
import time

from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtTest import *
from PySide6.QtGui import *
from PySide6.QtCore import *

from functools import partial

## .ui -> .py ##
from pyside6_uic import PySide6Ui
from ui_menu_main import Ui_MainWindow
from ui_schedule_line import Ui_Form
from ui_about import Ui_About_From

##
from musicplayer import musicplayer

_VER = 'v0.91'
_UPDATE = '2022.06.12'
_MAKE = '정원길'
_MAME = 'Schedule Player'
_HOMEPAGE = 'https://techclass.tistory.com/'
WIN_DATA_FINE_NAME = 'schedule_player.dat'

PLAYER_DEFAULT_PATH = 'C:\Program Files'


SCHEDULE_DEFAULT = (None, None, None, None, None, 1, None, None, None, None, None, 0)
# SEL_PLAYER_NUM = 1 ( in Player ), 2 ( win Player ), 3 ( usr Player )

# self.schedule_data_list[][0-11]
ENABLE = 0; TIME_REMAINING = 1; LABLE_NAME = 2; SET_TIME = 3; BEFORE_TIME = 4; SEL_PLAYER_NUM = 5; 
AUTO_PLAY_FG = 6; SET_PLAYER = 7; SET_MP3_FILE = 8; REAL_ALARM_TIME = 9; PLAYED_DAY_CHECK = 10; WARNING_COLOR = 11; 
#### 데이터 구조 정의 #########
#     0    ,   1       ,   2   ,     3     ,      4    ,     5   ,   6   ,         7     ,    8
#   남은시간 ,  제목     , 설정시간,  미리알림시간, 자동재생여부, 플레이이름, 파일이름,     실제동작시간,  재생여부
# [ timeRemaining, labelName, setTime, beforTime, autoPlayFg, setPlayer, setMp3File, setRealTime, playedCheck ]
# [ TIME_REMAINING, LABLE_NAME, SET_TIME, BEFORE_TIME, AUTO_PLAY_FG, SET_PLAYER, SET_MP3_FILE, SET_REAL_TIME, PLAYED_DAY_CHECK]

# SCHECHDULE LINE WARNING_COLOR
TIME_COLOR_CODE0_STYLE = ''
TIME_COLOR_CODE1_STYLE = 'background-color: rgb(255, 255, 127);'
TIME_COLOR_CODE2_STYLE = 'background-color: rgb(0, 214, 0)'
TIME_COLOR_CODE3_STYLE = 'background-color: rgb(255, 170, 0);'
TIME_COLOR_CODE4_STYLE = 'background-color: rgb(255, 136, 0);'

FILE_COLOR_CODE0_STYLE = ''
FILE_COLOR_CODE1_STYLE = 'background-color: rgb(230, 230, 230);'
FILE_COLOR_CODE2_STYLE = 'background-color: rgb(220, 220, 220);'
FILE_COLOR_CODE3_STYLE = 'background-color: rgb(210, 210, 210);'
FILE_COLOR_CODE4_STYLE = 'background-color: rgb(200, 200, 200);'

SET_TIME_DEFAULT = QTime(0, 0)
BEFORE_TIME_DEFAULT = QTime(0, 0, 3)

GRAY_STYLE = "color: rgb(154, 154, 154);"

TIME_REMAINING_VIEW3 = 3*60 # 초
TIME_REMAINING_VIEW2 = 2*60 # 초
TIME_REMAINING_VIEW1 = 1*60 # 초
TIME_REMAINING_VIEW0 = 10 # 초
TIME_REMAINING_COUNTDOWN = 3 # 초    # 재생을 위한 카운트 다운, 카운트가 된 경우만, 자동 재생 (playerActive_list[])


MUSIC_PLAYER_FULL_SIZE = 160
MUSIC_PLAYER_MINI_SIZE = 80
HIGH_DIFF = MUSIC_PLAYER_FULL_SIZE - MUSIC_PLAYER_MINI_SIZE

class MyApp(QMainWindow, Ui_MainWindow):
    sel_full_size_player_fg_signal = Signal(bool)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init()
        self.show()
        # self.musicPlayer.groupBox.hide()

    def init(self):
        self.setWindowTitle(f'{_MAME} {_VER} {_UPDATE}')

        self.TIME_WARNING_COLOR_FG = True
        self.cb_timeColor.setChecked(self.TIME_WARNING_COLOR_FG)



        self.setWindowIcon(QIcon('schedule_player.ico'))

        # D1 ~ D4, D5 자료로 구성됨.
        self.schedule_data_list = []    ###> D1.
        self.schedule_widget_list = []  ###> D2.
        self.playerActive_list = []     ###> D3. TIME_REMAINING_COUNTDOWN 재생을 위한 카운트 다운, 카운트가 된 경우만, 자동 재생
        self.schedule_default = list(SCHEDULE_DEFAULT)
  
        # 스크롤 위젯에 위젯 추가
        # https://stackoverflow.com/questions/9624281/how-to-associate-a-horizontal-scrollbar-to-multiple-groupbox
        '''
        scroll = QScrollArea().setWidget
          scrollwidget = QWidget().setLayout
            scrolllayout = QVBoxLayout().addWidget()
        '''
        # vbox.count                     ###> D4.
        self.vbox = QVBoxLayout()               # 1. QVBoxLayout()
        self.vbox.setAlignment(Qt.AlignTop)
        self.scrollwidget = QWidget()           # 2. QWidget()
                                                # 3. QScrollArea
        self.scrollwidget.setLayout(self.vbox)
        self.scrollArea.setWidget(self.scrollwidget)

        # 인 플레이어
        self.musicPlayer = musicplayer()

        self.verticalLayout2.addWidget(self.musicPlayer)

        #
        self._timer()   # 타이머 실행
        self.schNew(3)  # 초기, 새로운 스케줄 리스트 생성

        # 인 플레이어 사이즈 (기본)
        self.SEL_FULL_SIZE_PLYAER_FG = False

        ##############################################
        self.actionNew.triggered.connect(self.actNew)
        self.actionLoad.triggered.connect(self.actLoad)
        self.actionSave.triggered.connect(self.btnFileSave)
        self.actionSave_As.triggered.connect(self.actSaveAs)
        self.actionExit.triggered.connect(QCoreApplication.instance().quit)
        self.actionAbout.triggered.connect(self._aboutWindow)

        # self.btn_test.clicked.connect(self.music_list_reload)
        self.cb_timeColor.clicked.connect(self.cb_timeColor_clicked)

        self.rb_selFullPlayer.clicked.connect(partial(self.rb_selPlayerSize_clicked, True))
        self.rb_selMiniPlayer.clicked.connect(partial(self.rb_selPlayerSize_clicked, False))
        
        ##############################################
        self.sel_full_size_player_fg_signal.connect(self.musicPlayer.playerSize_slot)

        ##############################################

        # 데이터 로드
        self.winDataLoad()
        self.btnFileLoad()
        self.music_list_reload()

        # 인 플레이어 사이즈 설정
        # if self.SEL_FULL_SIZE_PLYAER_FG == True:
        #     self.rb_selFullPlayer.setChecked(True)
        #     self.musicPlayerFullSize()
        # else:
        #     self.rb_selMiniPlayer.setChecked(True)
        #     self.musicPlayerMiniSize()
        # self.sel_full_size_player_fg_signal.emit(self.SEL_FULL_SIZE_PLYAER_FG)

        # 상태표시줄
        # https://wikidocs.net/21928
        self.statusbar.showMessage(f'{_MAME} {_VER} {_UPDATE} / {_MAKE}')

        # toolTop
        self.btn_reset.setToolTip('"[●]재생된 상태" → "[▷]미재생 상태"로 변경하기')

    def musicPlayerMiniSize(self):
        self.musicPlayer.gb_fullPlayer1.hide()
        self.musicPlayer.gb_fullPlayer2.hide()
        self.musicPlayer.gb_miniPlayer.show()
        self.musicPlayer.setFixedHeight(MUSIC_PLAYER_MINI_SIZE)
        # 윈도우 사이즈 축소
        wsize = self.size()
        wsize.setHeight(self.size().height() - HIGH_DIFF)
        self.resize(wsize)
        print('| musicPlayerMiniSize |')
    
    def musicPlayerFullSize(self):
        self.musicPlayer.gb_fullPlayer1.show()
        self.musicPlayer.gb_fullPlayer2.show()
        self.musicPlayer.gb_miniPlayer.hide()
        self.musicPlayer.setFixedHeight(MUSIC_PLAYER_FULL_SIZE)
        # 윈도우 사이즈 확장
        wsize = self.size()
        wsize.setHeight(self.size().height() + HIGH_DIFF)
        self.resize(wsize)
        print('| musicPlayerFullSize |')
        

    def _timer(self):
        # https://hyunjung-choe.tistory.com/94
        self.timer = QTimer()
        self.timer.timeout.connect(self.displayDateTime)
        self.timer.start(1000)

    def displayDateTime(self):
        # # debug
        # print(f'D1. schedule_data_list = {len(self.schedule_data_list)}')         # D1
        # print(f'D2. schedule_widget_list = {len(self.schedule_widget_list)}')     # D2
        # print(f'D3. playerActive_list = {len(self.playerActive_list)}')           # D3
        # print(f'D4. vbox.count = {self.vbox.count()}')                            # D4

        # idx = 0
        # print(f' played [{idx}], {self.schedule_data_list[idx][PLAYED_DAY_CHECK]}')

        # 1. 시계 디스플레이
        # https://wikidocs.net/37460
        cur_time = QTime.currentTime()
        time_tmp = cur_time.toString("AP hh:mm ss")
        time_text1 = time_tmp[:8]
        time_text2 = "."+time_tmp[-2:]
        self.lbl_time1.setText(time_text1)
        self.lbl_time2.setText(time_text2)

        #   시계 디스플레이 색상 검사
        if self.TIME_WARNING_COLOR_FG:
            time_warning_color = 0
            for idx in range(len(self.schedule_data_list)):
                line_warning_color = self.schedule_data_list[idx][WARNING_COLOR]
                if line_warning_color > time_warning_color:
                    time_warning_color = line_warning_color
            if time_warning_color == 1:
                self.wg_timeView.setStyleSheet(TIME_COLOR_CODE1_STYLE)
            elif time_warning_color == 2:
                self.wg_timeView.setStyleSheet(TIME_COLOR_CODE2_STYLE)
            elif time_warning_color == 3:
                self.wg_timeView.setStyleSheet(TIME_COLOR_CODE3_STYLE)
            elif time_warning_color == 4:
                self.wg_timeView.setStyleSheet(TIME_COLOR_CODE4_STYLE)
            else:
                self.wg_timeView.setStyleSheet(TIME_COLOR_CODE0_STYLE)
        else:
            self.wg_timeView.setStyleSheet(TIME_COLOR_CODE0_STYLE)

        # 2. 오늘 날짜 디스플레이
        # https://wikidocs.net/22074#_1
        # https://kkumalog.tistory.com/42
        # https://wikidocs.net/37459
        t = ['','월', '화', '수', '목', '금', '토', '일',]
        today = QDate.currentDate()
        # print(today.toString('yyyy. M. d.'))
        # print(today.dayOfWeek())
        # print(str(t[today.dayOfWeek()]))
        str_today = today.toString('yyyy. M. d. (') + str(t[today.dayOfWeek()]) +')'
        self.lbl_today.setText(str_today)

        # 3. 항목별 남은 시간 계산
        for idx in range(len(self.schedule_widget_list)):
            self.timeRemaing(idx)

        # 4. [PLAYED_DAY_CHECK] 검사
        for idx in range(len(self.schedule_widget_list)):
            self.playedCheck(idx)


    def slot_enableChk(self, idx, e):
        if self.schedule_widget_list[idx].cb_enable.isChecked() == True:
            self.schedule_widget_list[idx].btn_play.setEnabled(True)
            self.schedule_widget_list[idx].le_name.setEnabled(True)
            self.schedule_widget_list[idx].te_setTime.setEnabled(True)
            self.schedule_widget_list[idx].lbl_before.setEnabled(True)
            self.schedule_widget_list[idx].te_beforeTime.setEnabled(True)
            self.schedule_widget_list[idx].btn_autoPlay.setEnabled(True)
            # self.schedule_widget_list[idx].btn_autoPlay.setStyleSheet('color: rgb(0, 95, 184); font: 700;')
            self.schedule_widget_list[idx].rb_selInPlayer.setEnabled(True)
            self.schedule_widget_list[idx].rb_selWinPlayer.setEnabled(True)
            self.schedule_widget_list[idx].rb_selUserPlayer.setEnabled(True)
            if self.schedule_widget_list[idx].rb_selUserPlayer.isChecked() == True:
                self.schedule_widget_list[idx].btn_setPlayer.setEnabled(True)
            self.schedule_widget_list[idx].lbl_setPlayer.setEnabled(True)
            self.schedule_widget_list[idx].lbl_setPlayer.setStyleSheet("color: rgb(0, 0, 0);")
            self.schedule_widget_list[idx].btn_setFile.setEnabled(True)
            self.schedule_widget_list[idx].lbl_setFile.setEnabled(True)
            self.schedule_widget_list[idx].btn_clear.setEnabled(True)
        else:
            self.schedule_widget_list[idx].btn_play.setDisabled(True)
            self.schedule_widget_list[idx].le_name.setDisabled(True)
            self.schedule_widget_list[idx].te_setTime.setDisabled(True)
            self.schedule_widget_list[idx].te_beforeTime.setDisabled(True)
            self.schedule_widget_list[idx].lbl_before.setDisabled(True)
            self.schedule_widget_list[idx].btn_autoPlay.setDisabled(True)
            # self.schedule_widget_list[idx].btn_autoPlay.setStyleSheet('')
            self.schedule_widget_list[idx].rb_selInPlayer.setDisabled(True)
            self.schedule_widget_list[idx].rb_selWinPlayer.setDisabled(True)
            self.schedule_widget_list[idx].rb_selUserPlayer.setDisabled(True)
            
            self.schedule_widget_list[idx].btn_setPlayer.setDisabled(True)
            self.schedule_widget_list[idx].lbl_setPlayer.setDisabled(True)
            self.schedule_widget_list[idx].lbl_setPlayer.setStyleSheet(GRAY_STYLE)
            self.schedule_widget_list[idx].btn_setFile.setDisabled(True)
            self.schedule_widget_list[idx].lbl_setFile.setDisabled(True)
            self.schedule_widget_list[idx].btn_clear.setDisabled(True)

        self.schedule_data_list[idx][ENABLE] = self.schedule_widget_list[idx].cb_enable.isChecked()

    def slot_nameEdit(self, idx, text):
        self.schedule_data_list[idx][LABLE_NAME] = text

    def slot_setTime(self, idx, time):
        self.schedule_data_list[idx][SET_TIME] = time
        self.realAlarmTime(idx)

    def slot_beforeTime(self, idx, time):
        self.schedule_data_list[idx][BEFORE_TIME] = time
        self.realAlarmTime(idx)

    def slot_autoPlay(self, idx, e):
        # if self.schedule_widget_list[idx].btn_autoPlay.isChecked():
        #     self.schedule_data_list[idx][AUTO_PLAY_FG] = self.schedule_widget_list[idx].btn_autoPlay.isChecked()
        # else:
        #     self.schedule_data_list[idx][AUTO_PLAY_FG] = self.schedule_widget_list[idx].btn_autoPlay.isChecked()
        
        if self.schedule_widget_list[idx].btn_autoPlay.isChecked():
            ### True ###
            self.btn_autoPlay_On(idx)
        else:
            ### False ###
            self.btn_autoPlay_Off(idx)

        self.schedule_data_list[idx][AUTO_PLAY_FG] = self.schedule_widget_list[idx].btn_autoPlay.isChecked()


    def slot_inPlayer(self, idx):
        # _widget_list -> _data_list
        if self.schedule_widget_list[idx].btn_inPlayer.isChecked():
            # True
            self.btn_inPlay_On(idx)
            self.schedule_data_list[idx][SEL_PLAYER_NUM] = True
        else:
            # Not True
            self.btn_inPlay_Off(idx)
            self.schedule_data_list[idx][SEL_PLAYER_NUM] = None 

    def slot_play(self, idx):
        mp3FilePath = self.schedule_data_list[idx][SET_MP3_FILE]
        if mp3FilePath == None:
             self.statusbar.showMessage(f'재생할 파일(File)이 지정되지 않았습니다.')
             return

        # (I)인 플레이어
        if self.schedule_data_list[idx][SEL_PLAYER_NUM] == 1:

            self.p_file = pathlib.Path(mp3FilePath)
            print("인 플레이어 재생 path=", end = " " )
            print(mp3FilePath)

            self.statusbar.showMessage(f'"(I)인 플레이어"로 "{self.p_file.name}" 파일을 재생합니다.')
            self.music_play(self.schedule_data_list[idx][SET_MP3_FILE])  # False 재생후 파일이름 지우기

        # (W)윈도우 연결프로그램
        # if self.schedule_data_list[idx][SET_PLAYER] == None:
        elif self.schedule_data_list[idx][SEL_PLAYER_NUM] == 2:

            # 메시지 만들기
            self.p_file = pathlib.Path(mp3FilePath)
            self.statusbar.showMessage(f'(W)윈도우 기본 플레이어로 "{self.p_file.name}" 파일을 재생합니다.')

            # <파일명, 상대 경로 여부 검사>
            if mp3FilePath.find(':/') == -1:
                # 상대 경로 이면 > 절대 경로 추가하여 실행
                localPath = os.getcwd().replace('\\','/')
                mp3FilePath = f'{localPath + mp3FilePath[1:]}'
            else:
                # 절대 경로 이면 > 그대로 실행
                pass

            # 윈도우 기본 플레이어로 실행
            print(f'\n윈도우 기본 파일 열기 : {mp3FilePath}')
            # https://hello-bryan.tistory.com/249
            os.startfile(mp3FilePath)

        # (U)사용자 선택
        elif self.schedule_data_list[idx][SEL_PLAYER_NUM] == 3:
            if self.schedule_data_list[idx][SET_PLAYER] == None:
                self.statusbar.showMessage(f'(U)사용자 선택 플레이어가 선택되지 않았습니다.')
                return
            # https://codechacha.com/ko/python-run-shell-script/
            # https://www.aimp.ru/
            playerPath = self.schedule_data_list[idx][SET_PLAYER]
            mp3FilePath = self.schedule_data_list[idx][SET_MP3_FILE]
            # player = 'C:/Program Files (x86)/AIMP/AIMP.exe'

            # <파일명, 상대 경로 여부 검사>
            if mp3FilePath.find(':/') == -1:
                # 상대 경로 이면 > 절대 경로 추가하여 실행
                localPath = os.getcwd().replace('\\','/')
                cmd = f'"{playerPath}" "{localPath + mp3FilePath[1:]}"'
            else:
                # 절대 경로 이면 > 그대로 실행
                cmd = f'"{playerPath}" "{mp3FilePath}"'
  
            print(f'\n명령어 실행 : {cmd}')
            # os.system(cmd)  # 메모리 상주
            # subprocess.run(cmd)

            # 메시지 만들기
            self.p_file = pathlib.Path(mp3FilePath)
            self.p_player = pathlib.Path(playerPath)

            self.statusbar.showMessage(f'(U)사용자가 선택한 "{self.p_player.name}" 플레이어로 "{self.p_file.name}" 파일을 재생합니다.')

            # http://daplus.net/python-파이썬에서-백그라운드-프로세스를-시작하는-방/
            subprocess.Popen(cmd)

        # self.schedule_widget_list[idx].btn_play.setText("○")
        self.schedule_widget_list[idx].btn_play.setText("●")
        self.schedule_data_list[idx][PLAYED_DAY_CHECK] = QDate.currentDate()
        print(self.schedule_data_list[idx])


    ###
    def slot_setPlayer(self, idx):
        if self.schedule_data_list[idx][SET_PLAYER] == None:
            if idx == 0:
                filePath = PLAYER_DEFAULT_PATH                  # str
            else:
                if self.schedule_data_list[idx-1][SET_PLAYER] != None:
                    filePath = self.schedule_data_list[idx-1][SET_PLAYER] # str
                else:
                    filePath = PLAYER_DEFAULT_PATH
        else:
            filePath = self.schedule_data_list[idx][SET_PLAYER]          # str

        p_file = pathlib.Path(filePath)
        if p_file.is_file():     # 디렉토리 경로 확인 https://engineer-mole.tistory.com/191
            pass
        else:
            filePath = './'

        getFile = QFileDialog.getOpenFileName(self, "Player file", filePath, '실행 파일(*.exe *.com)')

        if getFile[0] != '':
            # data_list SAVE
            self.schedule_data_list[idx][SET_PLAYER] = getFile[0]

            # filePath = str(filePath.parent).replace('\\', '/')  # 문자 변환
            # print(p_file.parent)    # dirtory
            # print(p_file.name)      # filename
            # p_file.is_dir()

            # 화면 표시
            p_file = pathlib.Path(getFile[0])
            self.schedule_widget_list[idx].lbl_setPlayer.setStyleSheet('')
            self.schedule_widget_list[idx].lbl_setPlayer.setText(p_file.name)


    def slot_setFile(self, idx):
        if self.schedule_data_list[idx][SET_MP3_FILE] == None:
            if idx == 0:
                filePath = './'                  # str
            else:
                if self.schedule_data_list[idx-1][SET_MP3_FILE] != None:
                    filePath = self.schedule_data_list[idx-1][SET_MP3_FILE] # str
                else:
                    filePath = './'
        else:
            filePath = self.schedule_data_list[idx][SET_MP3_FILE]          # str

        p_file = pathlib.Path(filePath)
        if p_file.is_file():     # 디렉토리 경로 확인 https://engineer-mole.tistory.com/191
            pass
        else:
            filePath = './'

        getFile = QFileDialog.getOpenFileName(self, "Media file", filePath, '미디어 파일(*.mp3 *.wav)')

        if getFile[0] != '':
            # data_list SAVE
            self.schedule_data_list[idx][SET_MP3_FILE] = getFile[0]

            # filePath = str(filePath.parent).replace('\\', '/')  # 문자 변환
            # print(p_file.parent)    # dirtory
            # print(p_file.name)      # filename
            # p_file.is_dir()

            # 화면에 파일명 표시
            p_file = pathlib.Path(getFile[0])
            self.schedule_widget_list[idx].lbl_setFile.setStyleSheet('')
            self.schedule_widget_list[idx].lbl_setFile.setText(p_file.name)     # 파일명 표시하기
            self.schedule_widget_list[idx].btn_play.setToolTip(f'"{p_file.name}"파일을 재생합니다.')     # 툴팁 이름 바꾸기

            # music player(인 플레이어) 리스트에 추가하기
            # self.music_list_add(getFile[0])
            self.music_list_reload()

            # AutoPlay enable
            self.schedule_data_list[idx][AUTO_PLAY_FG] = True
            self.schedule_widget_list[idx].btn_autoPlay.setChecked(True)

            # 실제 알람시간 계산
            self.realAlarmTime(idx)

    def slot_clear(self, idx):
        self.schedule_widget_list[idx].te_setTime.setTime(SET_TIME_DEFAULT)
        self.schedule_widget_list[idx].te_beforeTime.setTime(BEFORE_TIME_DEFAULT)

        self.schedule_data_list[idx][LABLE_NAME] = None
        self.schedule_data_list[idx][SET_PLAYER] = None
        self.schedule_data_list[idx][SET_MP3_FILE] = None

        self.schedule_data_list[idx][SET_TIME] = None
        self.schedule_data_list[idx][BEFORE_TIME] = None
        self.schedule_data_list[idx][REAL_ALARM_TIME] = None


        # self.schedule_default2 = list(SCHEDULE_DEFAULT)
        # print( self.schedule_default2 )
        # list_B = copy.deepcopy(self.schedule_default2)
        # self.schedule_data_list[idx] = list_B
        print( f'slot_clear = {self.schedule_data_list[idx]}')


        self.displayScheduleLine(idx)

        self.music_list_reload()

    def displayScheduleLine(self, idx):
        # 로드 >    _data_list -> _widget_list
        # print(self.schedule_data_list[idx])

        # 0. enable check / ENABLE 
        if self.schedule_data_list[idx][ENABLE] == None:
            self.schedule_widget_list[idx].cb_enable.setChecked(True)
        elif self.schedule_data_list[idx][ENABLE] == True:
            self.schedule_widget_list[idx].cb_enable.setChecked(True)
        else:
            self.schedule_widget_list[idx].cb_enable.setChecked(False)

        # 1. 남은 시간 / TIME_REMAINING
        if self.schedule_data_list[idx][TIME_REMAINING] == None:
            self.schedule_widget_list[idx].cb_enable.setText('')

        ## 2. 일정 제목 / LABLE_NAME
        if self.schedule_data_list[idx][LABLE_NAME] == None:
            self.schedule_widget_list[idx].le_name.setText(str(idx+1))
        else:
            self.schedule_widget_list[idx].le_name.setText(self.schedule_data_list[idx][LABLE_NAME])

        ## 3. 시간 설정 / SET_TIME
        if self.schedule_data_list[idx][SET_TIME] == None:
            self.schedule_widget_list[idx].te_setTime.setTime(SET_TIME_DEFAULT)
        else:
            self.schedule_widget_list[idx].te_setTime.setTime(self.schedule_data_list[idx][SET_TIME])

        ## 4. 미리 알림시간 / BEFORE_TIME
        if self.schedule_data_list[idx][BEFORE_TIME] == None:
            self.schedule_data_list[idx][BEFORE_TIME] = BEFORE_TIME_DEFAULT
            self.schedule_widget_list[idx].te_beforeTime.setTime(BEFORE_TIME_DEFAULT)
        else:
            self.schedule_widget_list[idx].te_beforeTime.setTime(self.schedule_data_list[idx][BEFORE_TIME])

        ## 5. 자동 재생여부 / AUTO_PLAY_FG 
        if self.schedule_data_list[idx][AUTO_PLAY_FG] == None or self.schedule_data_list[idx][AUTO_PLAY_FG] == False:
            ### False ###
            self.schedule_widget_list[idx].btn_autoPlay.setChecked(False)
            self.btn_autoPlay_Off(idx)
        else:
            ### True ###
            self.schedule_widget_list[idx].btn_autoPlay.setChecked(True)
            self.btn_autoPlay_On(idx)


        ## 7. 플레이어 이름 / SET_PLAYER 
        if self.schedule_data_list[idx][SET_PLAYER] == None:
            # if self.schedule_data_list[idx][SEL_PLAYER_NUM] != True:
            #     # self.schedule_widget_list[idx].lbl_setPlayer.setText("None")
            #     self.schedule_widget_list[idx].lbl_setPlayer.setText(" 연결 프로그램1")
            #     self.schedule_widget_list[idx].lbl_setPlayer.setStyleSheet(GRAY_STYLE)
            pass
        else:
            filePath = self.schedule_data_list[idx][SET_PLAYER]
            p_file = pathlib.Path(filePath)
            # 경로 점검
            if p_file.is_file(): # 파일 존재 유무 확인 https://engineer-mole.tistory.com/191
                # 경로에 정상 / 화면표시
                self.schedule_widget_list[idx].lbl_setPlayer.setStyleSheet("color: rgb(0, 0, 0);")
                self.schedule_widget_list[idx].lbl_setPlayer.setText(p_file.name)
            else:
                # 경로에 에러시, 기본 플레이어 설정
                self.schedule_data_list[idx][SET_PLAYER] == None
                self.schedule_widget_list[idx].lbl_setPlayer.setText(" Error")
                # self.schedule_widget_list[idx].lbl_setPlayer.setText("None")
                self.schedule_widget_list[idx].lbl_setPlayer.setStyleSheet(GRAY_STYLE)

        ## 6. 플레이어 선택 / SEL_PLAYER_NUM 
        # .sch 로딩시 lbl_setFile.setText 에 파일 이름이 표시되는 것을 방지하기 위해 7. 다음 순서에
        num = self.schedule_data_list[idx][SEL_PLAYER_NUM]
        self.slot_selNum(idx, num)

        ## 8. 미디어 파일 이름 / SET_MP3_FILE 
        if self.schedule_data_list[idx][SET_MP3_FILE] == None:
            self.schedule_widget_list[idx].lbl_setFile.setText("None")
            self.schedule_widget_list[idx].btn_play.setToolTip("")  # 툴팁 이름 바꾸기
            self.schedule_widget_list[idx].lbl_setFile.setStyleSheet(GRAY_STYLE)
        else:
            filePath = self.schedule_data_list[idx][SET_MP3_FILE]

            # 기존 파일의 절대 경로 > 상대경로 변환.(이전 v0.87 버전의 호환성 유지)
            # self.schedule_data_list[idx][SET_MP3_FILE] = r_path

            p_file = pathlib.Path(filePath)
            # https://engineer-mole.tistory.com/191
            
            # 1) 경로에 파일이 존재하는 경우,
            #   if p_file.exists():  # 디렉토리 경로 확인 
            #   if p_file.is_file(): # 파일 존재 유무 확인
            if p_file.is_file():
                # 파일 정상
                self.schedule_widget_list[idx].lbl_setFile.setStyleSheet("color: rgb(0, 0, 0);")
                self.schedule_widget_list[idx].lbl_setFile.setText(p_file.name)     # 화면 표시
                self.schedule_widget_list[idx].btn_play.setToolTip(f'"{p_file.name}"파일을 재생합니다.')     # 툴팁 이름 바꾸기
            # 2) 경로에 파일이 없는 경우,
            else:
                # 3) 현재 폴더에서 파일이 있는지 검사
                cur_path = pathlib.Path(f'./{p_file.name}')
                if cur_path.is_file():
                    # 파일이 있으면,
                    self.schedule_widget_list[idx].lbl_setFile.setStyleSheet("color: rgb(0, 0, 0);")
                    self.schedule_widget_list[idx].lbl_setFile.setText(cur_path.name)   # 화면 표시
                    self.schedule_widget_list[idx].btn_play.setToolTip(f'"{p_file.name}"파일을 재생합니다.')
                    # 현재 폴더 경로를 _data_list에 저장
                    self.schedule_data_list[idx][SET_MP3_FILE] = cur_path.name  # 이름만 저장(현재 폴더)
                else:
                    # 파일이 없으면
                    self.schedule_data_list[idx][SET_MP3_FILE] == None
                    self.schedule_widget_list[idx].lbl_setFile.setText("None")
                    self.schedule_widget_list[idx].btn_play.setToolTip("")      # 툴팁 이름 바꾸기
                    self.schedule_widget_list[idx].lbl_setFile.setStyleSheet(GRAY_STYLE)
                    # _data_list 지우기
                    self.schedule_data_list[idx][SET_MP3_FILE] = None

        ## 9. Played_Check
        # print(self.schedule_data_list[idx][PLAYED_DAY_CHECK], end = ' ')
        # print( QDate.currentDate(), end =' ')
        # print(self.schedule_data_list[idx][PLAYED_DAY_CHECK] == QDate.currentDate())
        self.playedCheck(idx)

    def playedCheck(self, idx):
        # 재생 날짜가 다른 경우
        if self.schedule_data_list[idx][PLAYED_DAY_CHECK] == None or self.schedule_data_list[idx][PLAYED_DAY_CHECK] != QDate.currentDate():
            self.schedule_widget_list[idx].btn_play.setText('▷')
            # print(idx, '▷')
            self.schedule_data_list[idx][PLAYED_DAY_CHECK] = None   # 미 재생 상태로 Clear
        else:
            # if { self.schedule_data_list[idx][PLAYED_DAY_CHECK] == QDate.currentDate() }
            self.schedule_widget_list[idx].btn_play.setText("●")
            # print(idx, "●")

    def schClear(self):
        # 로드 전에 clear
        self.schedule_data_list = []    # D1
        self.schedule_widget_list = []  # D2
        self.playerActive_list = []     # D3

        # 기존 display widget 지우기      # D4

        # # (.count = 0 안됨 - 실패) -> err 발생
        # https://www.pythonfixing.com/2022/01/fixed-clear-all-widgets-in-layout-in.html
        # for i in reversed(range(self.vbox.count())):
        #     self.vbox.itemAt(i).widget().deleteLater()

        # # (.count = 0 안됨 - 실패) -> err 발생
        # for i in range(self.vbox.count()):
        #     item = self.vbox.itemAt(i)
        #     widget = item.widget()
        #     widget.deleteLater()

        # (.count = 0 초기화됨, 그러나 멈춤)
        # https://python-forum.io/thread-25544.html
        # for i in reversed(range(self.vbox.count())):
        #     self.vbox.removeItem(self.vbox.itemAt(i))

        #  (.count = 0 초기화됨) -> 성공적 동작
        #  https://tousu.in/qa/?qa=547910/
        if self.vbox is not None:
            while self.vbox.count():
                item = self.vbox.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())

    # 새로운 스케줄 리스트 생성
    def schNew(self, number):
        self.schClear()
        self.musicPlayer.list_music.clear()

        # 생성하기
        for i in range(number):
            self.schAdd()

    # 다아니믹 위젯 추가
    # https://ymt-lab.com/en/post/2021/pyqt5-delete-widget-test/
    def schAdd(self):
        count = self.vbox.count()   # for문과 비교해서 추가되는 부분

        # schAdd_data (D1)
        self.schAdd_data()
        # schAdd_widget (D2~D4)
        self.schAdd_widget(count)

    def schAdd_data(self):
        # D1. data_list insert
        list_A = copy.deepcopy(self.schedule_default)
        self.schedule_data_list.append(list_A)                 # schedule_data_list


    def schAdd_widget(self, count):
        # D2. widget_list insert
        self.schedule_widget_list.append(ScheduleLine())
        self.schedule_widget_list[count].le_name.setText(str(count + 1))      # Lable Name TEXT

        # D3. playerActive_list insert
        self.playerActive_list.append(False)

        # D4. display_widget insert
        self.vbox.addWidget(self.schedule_widget_list[count])
        self.displayScheduleLine(count)

        # singnal & slot
        # for문의 lambda 전송 문제
        # https://yogyui.tistory.com/entry/PyQt5-Connect-pyqtSignal-in-For-loop-lambda-problem
        # self.schedule_widget_list[i].btn_selDel.clicked.connect( partial(self.schSelectDel, i) )

        # 4. connect
        self.schedule_widget_list[count].cb_enable.stateChanged.connect(partial(self.slot_enableChk, count))
        self.schedule_widget_list[count].le_name.textEdited.connect(partial(self.slot_nameEdit, count))
        self.schedule_widget_list[count].te_setTime.timeChanged.connect(partial(self.slot_setTime, count))
        self.schedule_widget_list[count].te_beforeTime.timeChanged.connect(partial(self.slot_beforeTime, count))
        self.schedule_widget_list[count].btn_autoPlay.toggled.connect(partial(self.slot_autoPlay, count))

        # 5. signal_slot
        self.schedule_widget_list[count].rb_selInPlayer.clicked.connect(partial(self.slot_selNum, count, 1))
        self.schedule_widget_list[count].rb_selWinPlayer.clicked.connect(partial(self.slot_selNum, count, 2))
        self.schedule_widget_list[count].rb_selUserPlayer.clicked.connect(partial(self.slot_selNum, count, 3))

        self.schedule_widget_list[count].btn_setPlayer.clicked.connect(partial(self.slot_setPlayer, count))
        self.schedule_widget_list[count].btn_setFile.clicked.connect(partial(self.slot_setFile, count))
        self.schedule_widget_list[count].btn_play.clicked.connect(partial(self.slot_play, count))
        self.schedule_widget_list[count].btn_clear.clicked.connect(partial(self.slot_clear, count))

        # setToolTip
        self.schedule_widget_list[count].rb_selInPlayer.setToolTip('내장된 음원 Player로 재생합니다.')
        self.schedule_widget_list[count].rb_selWinPlayer.setToolTip('윈도우에서 설정된 기본 Player로 재생합니다.')
        self.schedule_widget_list[count].rb_selUserPlayer.setToolTip('사용자가 선택한 Player로 재생합니다.')
        self.schedule_widget_list[count].btn_autoPlay.setToolTip('[A]활성화시 자동 재생. 주의: [●]재생된 상태에서는 자동으로 재생되지 않음')

        self.schedule_widget_list[count].btn_setPlayer.setToolTip('음원을 재생할 사용자 Player파일 선택')
        self.schedule_widget_list[count].btn_setFile.setToolTip('재생(Play)할 음원 선택')

        self.schedule_widget_list[count].btn_clear.setToolTip('내용 지우기')
        self.schedule_widget_list[count].te_beforeTime.setToolTip('미리 재생할 시간(분:초)')
        
    # 다이나믹 위젯 삭제
    # https://ymt-lab.com/en/post/2021/pyqt5-delete-widget-test/
    def schDel(self):
        count = self.vbox.count()
        # print(count)
        if count == 1:
            return

        self.schedule_data_list.pop()       # D1. data_list DEL
        self.schedule_widget_list.pop()     # D2. widget_list DEL
        self.playerActive_list.pop()        # D3. playerActive_list DEL

        item = self.vbox.itemAt(count - 1)  # D4. display_widget DEL
        widget = item.widget()
        widget.deleteLater()

    def realAlarmTime(self, idx):
        ### te_setTime, te_beforeTime 값 불러오기
        # setTime = self.schedule_widget_list[idx].te_setTime.time()
        # beforeTime = self.schedule_widget_list[idx].te_beforeTime.time()
        # print(setTime, beforeTime)
        if self.schedule_data_list[idx][SET_TIME] == None:
            return

        self.schedule_data_list[idx][SET_TIME] = self.schedule_widget_list[idx].te_setTime.time()
        self.schedule_data_list[idx][BEFORE_TIME] = self.schedule_widget_list[idx].te_beforeTime.time()

        if self.schedule_data_list[idx][SET_TIME] != None and  self.schedule_data_list[idx][BEFORE_TIME] != None:
            setTime = self.schedule_data_list[idx][SET_TIME]
            beforeTime = self.schedule_data_list[idx][BEFORE_TIME]

            #   (1) QTime -> timedelta 로 변환
            _setTime = datetime.timedelta(hours=setTime.hour(), minutes=setTime.minute(), seconds=setTime.second())
            _beforeTime = datetime.timedelta(hours=beforeTime.hour(), minutes=beforeTime.minute(),
                                             seconds=beforeTime.second())

            #   (2) 시간계산
            _realAlarmTime = _setTime - _beforeTime
            print(_realAlarmTime)
            #  정상 결과      ['12', '57', '00']
            #  에러 발생 결과  ['-1 day, 23', '55', '00']
            # err : - day 발생하는 경우, 오류가 발생함.
            #       AM 12:00 이전 -05:00 => 경우 -1 DAY 발생
            if _realAlarmTime < datetime.timedelta(days=0):
                self.schedule_widget_list[idx].te_beforeTime.setTime(QTime(0, 0, 0))

                self.schedule_widget_list[idx].te_setTime.setToolTip("")
                return

            # 2) datetime.timedelta -> QTime
            #   (3) 문자 배열로 분리
            _realAlarmTime_list = str(_realAlarmTime).split(':')
            print(_realAlarmTime_list)
            #   (4) list -> QTime -> list SAVE
            realAlarmTime = QTime(int(_realAlarmTime_list[0]), int(_realAlarmTime_list[1]), int(_realAlarmTime_list[2]))
            self.schedule_data_list[idx][REAL_ALARM_TIME] = realAlarmTime
            #
            time_tmp = realAlarmTime.toString("AP hh:mm.ss")
            self.schedule_widget_list[idx].te_setTime.setToolTip(f"예정 {time_tmp}")
            # print(f'realAlarmTime = {realAlarmTime}')
            print(self.schedule_data_list[idx])     # load error

    def timeRemaing(self, idx):
        errCode = 0
        if self.schedule_data_list[idx][REAL_ALARM_TIME] != None:
            realAlarmTime = self.schedule_data_list[idx][REAL_ALARM_TIME]
            curTime = QTime.currentTime()
            setTime = self.schedule_data_list[idx][SET_TIME]
            
            # error 검사 / cb_enable 에 표시
            #   음원 파일이 지정되지 않으면
            if self.schedule_data_list[idx][SET_MP3_FILE] == None:
                errCode =+ 1

            #   (3. User player 상태 and 플레이어 미지정시)
            if self.schedule_data_list[idx][SEL_PLAYER_NUM] == 3 and self.schedule_data_list[idx][SET_PLAYER] == None:
                errCode =+ 2
            if errCode != 0:
                self.schedule_widget_list[idx].cb_enable.setText("ERR")
                self.schedule_widget_list[idx].cb_enable.setStyleSheet("")
                self.schedule_widget_list[idx].cb_enable.setToolTip("ERR: '음원 플레이어' 또는 '음악 파일'이 지정되지 않았습니다. ")
                return

            # if self.schedule_widget_list[idx].cb_enable.isChecked() == False:
            #     return

            #   (1) QTime -> datetime.timedelta
            _realAlarmTime = datetime.timedelta(hours=realAlarmTime.hour(), minutes=realAlarmTime.minute(),
                                                seconds=realAlarmTime.second())
            _curTime = datetime.timedelta(hours=curTime.hour(), minutes=curTime.minute(), seconds=curTime.second())
            _setTime = datetime.timedelta(hours=setTime.hour(), minutes=setTime.minute(), seconds=setTime.second())

            #   (2) 남은 시간 = 알림시간- 현재시간
            _timeRemaing = _realAlarmTime - _curTime
            # print(_timeRemaing)

            #   (3) 비교하기  표시하기
            cur_day = _timeRemaing > datetime.timedelta(days=0)    # 아직 시간이 날짜가 지난 경우 "-1 day" 검사

            # - 시간이 지나버린 경우
            if (_setTime - _curTime) < datetime.timedelta(days=0):
                self.schedule_widget_list[idx].cb_enable.setText('pass')
                # self.schedule_widget_list[idx].cb_enable.setStyleSheet("")
                self.schedule_widget_list[idx].cb_enable.setToolTip('pass: 이미 지난 일정 입니다.')
            
            if self.schedule_widget_list[idx].cb_enable.isChecked() == False:
                self.schedule_widget_list[idx].cb_enable.setStyleSheet("")

                # 비활성화시 지우지 않을 text 코드
                text = self.schedule_widget_list[idx].cb_enable.text()
                if text == 'pass' or text == 'NOT' or text == "ERR":
                    pass
                else:
                    self.schedule_widget_list[idx].cb_enable.setText('')
                    self.schedule_widget_list[idx].cb_enable.setToolTip('남은 시간: A--:--:-- ')
                return

            # 시간이 일치하는 경우 플레이어 실행
            # if cur_day and _timeRemaing < datetime.timedelta(seconds=0):
            if _timeRemaing < datetime.timedelta(days=0):
                # 아직 미 재생인 경우
                # print(f'self.playerActive_list[idx] = {self.playerActive_list[idx]}')
                if self.schedule_data_list[idx][PLAYED_DAY_CHECK] == None or self.schedule_data_list[idx][PLAYED_DAY_CHECK] != QDate.currentDate():
                    if self.schedule_data_list[idx][AUTO_PLAY_FG] == True and self.playerActive_list[idx] == True:
                        print('Auto Play')
                        self.slot_play(idx) ## 재생 ##
                        self.playerActive_list[idx] = False     # 재생 비활성화

            # - TIME_REMAINING_COUNTDOWN 이내인 경우 (3초)
            if cur_day and _timeRemaing < datetime.timedelta(seconds=TIME_REMAINING_COUNTDOWN):
                self.playerActive_list[idx] = True  # 재생 활성화
                print(f'self.playerActive_list[{idx}] = {self.playerActive_list[idx]}')

            # - REMAINING_VIEW0 이내인 경우 (10초)
            elif cur_day and _timeRemaing < datetime.timedelta(seconds=TIME_REMAINING_VIEW0):
                # WARNING_COLOR = 4
                self.schedule_data_list[idx][WARNING_COLOR] = 4
            # - REMAINING_VIEW1 이내인 경우 (1분)
            elif cur_day and _timeRemaing < datetime.timedelta(seconds=TIME_REMAINING_VIEW1):
                # WARNING_COLOR = 3
                self.schedule_data_list[idx][WARNING_COLOR] = 3
            # - REMAINING_VIEW2 이내인 경우 (2분)
            elif cur_day and _timeRemaing < datetime.timedelta(seconds=TIME_REMAINING_VIEW2):
                # WARNING_COLOR = 2
                self.schedule_data_list[idx][WARNING_COLOR] = 2
            # - REMAINING_VIEW3 이내인 경우 (3분)
            elif cur_day and _timeRemaing < datetime.timedelta(seconds=TIME_REMAINING_VIEW3):
                # WARNING_COLOR = 1
                self.schedule_data_list[idx][WARNING_COLOR] = 1
            # - 1시간 이내인 경우
            elif cur_day and _timeRemaing < datetime.timedelta(hours=1):
                # WARNING_COLOR = 0
                self.schedule_data_list[idx][WARNING_COLOR] = 0

            #시간 표시
            if cur_day and _timeRemaing < datetime.timedelta(hours=1):
                _timeRemaing_list = str(_timeRemaing).split(':')
                # print(f'{_timeRemaing_list[1]}분{_timeRemaing_list[2]}초')
                self.schedule_widget_list[idx].cb_enable.setText(f'{int(_timeRemaing_list[1])}:{_timeRemaing_list[2]}')
                self.schedule_widget_list[idx].cb_enable.setToolTip(f'남은 시간: {int(_timeRemaing_list[1])}분 {_timeRemaing_list[2]}초 ')
            else:
                # timeRemaing 시간이 아닌 setTime 에서 색상 clear
                if (_setTime - _curTime) < datetime.timedelta(days=0):
                    # WARNING_COLOR = 0
                    self.schedule_data_list[idx][WARNING_COLOR] = 0
                    self.playerActive_list[idx] = False     # 재생 비활성화
                else:
                    self.schedule_widget_list[idx].cb_enable.setText('')
                    # self.schedule_widget_list[idx].cb_enable.setToolTip(f'남은 시간: {int(_timeRemaing_list[0])}시간 {int(_timeRemaing_list[1])}분 {_timeRemaing_list[2]}초 ')

        # self.schedule_data_list[idx][REAL_ALARM_TIME] == None
        else:
            # clear
            self.schedule_widget_list[idx].cb_enable.setText('NOT')
            self.schedule_widget_list[idx].cb_enable.setToolTip('NOT: 시간이 설정되지 않았습니다.')
            # WARNING_COLOR = 0
            self.schedule_data_list[idx][WARNING_COLOR] = 0


        # SCHECHDULE LINE WARNING_COLOR
        if self.schedule_data_list[idx][WARNING_COLOR] == 0:
            # color_code = 0
            self.schedule_widget_list[idx].cb_enable.setStyleSheet(TIME_COLOR_CODE0_STYLE)
            self.schedule_widget_list[idx].lbl_setFile.setStyleSheet(FILE_COLOR_CODE0_STYLE)
        elif self.schedule_data_list[idx][WARNING_COLOR] == 1:
            # color_code = 1
            self.schedule_widget_list[idx].cb_enable.setStyleSheet(TIME_COLOR_CODE1_STYLE)
            self.schedule_widget_list[idx].lbl_setFile.setStyleSheet(FILE_COLOR_CODE1_STYLE)
        elif self.schedule_data_list[idx][WARNING_COLOR] == 2:
            # color_code = 2
            self.schedule_widget_list[idx].cb_enable.setStyleSheet(TIME_COLOR_CODE2_STYLE)
            self.schedule_widget_list[idx].lbl_setFile.setStyleSheet(FILE_COLOR_CODE2_STYLE)

        elif self.schedule_data_list[idx][WARNING_COLOR] == 3:
            # color_code = 3
            self.schedule_widget_list[idx].cb_enable.setStyleSheet(TIME_COLOR_CODE3_STYLE)
            self.schedule_widget_list[idx].lbl_setFile.setStyleSheet(FILE_COLOR_CODE3_STYLE)

        elif self.schedule_data_list[idx][WARNING_COLOR] == 4:
            # color_code = 4
            self.schedule_widget_list[idx].cb_enable.setStyleSheet(TIME_COLOR_CODE4_STYLE)
            self.schedule_widget_list[idx].lbl_setFile.setStyleSheet(FILE_COLOR_CODE4_STYLE)

    def playedReset(self):
        for i in range(len(self.schedule_widget_list)):
            self.schedule_widget_list[i].btn_play.setText('▷')
            self.schedule_data_list[i][PLAYED_DAY_CHECK] = None

    ###########################################

    def btn_autoPlay_On(self, idx):
        self.schedule_widget_list[idx].btn_autoPlay.setText("A")
        self.schedule_widget_list[idx].btn_autoPlay.setStyleSheet('color: rgb(0, 95, 184); font: 700;') # Blue
    
    def btn_autoPlay_Off(self, idx):
        self.schedule_widget_list[idx].btn_autoPlay.setText("A")
        # self.schedule_widget_list[idx].btn_autoPlay.setText("")
        self.schedule_widget_list[idx].btn_autoPlay.setStyleSheet('color: rgb(226, 226, 226);') # lite Gray

    # def btn_inPlay_On(self, idx):
    #     self.schedule_widget_list[idx].btn_inPlayer.setStyleSheet('color: rgb(0, 95, 184); font: 700;') # Blue
    #     self.schedule_widget_list[idx].btn_inPlayer.setChecked(True)

    #     self.schedule_widget_list[idx].btn_setPlayer.setDisabled(True)
    #     self.schedule_widget_list[idx].lbl_setPlayer.setText(' 인 플레이어')
    #     self.schedule_widget_list[idx].lbl_setPlayer.setStyleSheet('color: black;')

    # def btn_inPlay_Off(self, idx):
    #     self.schedule_widget_list[idx].btn_inPlayer.setStyleSheet('color: rgb(226, 226, 226);') # lite Gray
    #     self.schedule_widget_list[idx].btn_inPlayer.setChecked(False)

    #     self.schedule_widget_list[idx].btn_setPlayer.setEnabled(True)
    #     self.schedule_widget_list[idx].lbl_setPlayer.setText(" 연결 프로그램")
    #     self.schedule_widget_list[idx].lbl_setPlayer.setStyleSheet('color: gray;')
    
    def cb_timeColor_clicked(self):
        if self.cb_timeColor.isChecked():
            self.TIME_WARNING_COLOR_FG = True
        else:
            self.TIME_WARNING_COLOR_FG = False
    
    def rb_selPlayerSize_clicked(self, fg):
        print(f'rb_selPlayerSize_clicked = {fg}')
        if fg == True and self.SEL_FULL_SIZE_PLYAER_FG == False:
            self.SEL_FULL_SIZE_PLYAER_FG = True
            self.musicPlayerFullSize()
        elif fg == False and self.SEL_FULL_SIZE_PLYAER_FG == True:
            self.SEL_FULL_SIZE_PLYAER_FG = False
            self.musicPlayerMiniSize()

        if fg == True:
            self.rb_selFullPlayer.setChecked(True)
        else:
            self.rb_selMiniPlayer.setChecked(True)

        self.sel_full_size_player_fg_signal.emit(fg)

    ###########################################

    def slot_selNum(self, idx, num):
        if num == 1:
            self.schedule_widget_list[idx].rb_selInPlayer.setChecked(True)
            # self.schedule_widget_list[idx].rb_selWinPlayer.setChecked(False)
            # self.schedule_widget_list[idx].rb_selUserPlayer.setChecked(False)

            self.schedule_widget_list[idx].lbl_setPlayer.setText('(I)인 플레이어')
            self.schedule_widget_list[idx].lbl_setPlayer.setStyleSheet("color: rgb(0, 0, 0);")
            self.schedule_widget_list[idx].btn_setPlayer.setEnabled(False)
            
        elif num == 2:
            # self.schedule_widget_list[idx].rb_selInPlayer.setChecked(False)
            self.schedule_widget_list[idx].rb_selWinPlayer.setChecked(True)
            # self.schedule_widget_list[idx].rb_selUserPlayer.setChecked(False)

            self.schedule_widget_list[idx].lbl_setPlayer.setText("(W)연결프로그램")
            self.schedule_widget_list[idx].lbl_setPlayer.setStyleSheet("color: rgb(0, 0, 0);")
            self.schedule_widget_list[idx].btn_setPlayer.setEnabled(False)

        elif num == 3:
            # self.schedule_widget_list[idx].rb_selInPlayer.setChecked(False)
            # self.schedule_widget_list[idx].rb_selWinPlayer.setChecked(False)
            self.schedule_widget_list[idx].rb_selUserPlayer.setChecked(True)
            if self.schedule_data_list[idx][SEL_PLAYER_NUM] == None or self.schedule_data_list[idx][SET_PLAYER] == None:
                self.schedule_widget_list[idx].lbl_setPlayer.setText("(U)사용자 선택")
            else:
                filePath = self.schedule_data_list[idx][SET_PLAYER]
                print(f'CCC filePath = {filePath}')
                p_file = pathlib.Path(filePath)
                if p_file.is_file(): 
                    # 경로에 정상 / 화면표시
                    self.schedule_widget_list[idx].lbl_setPlayer.setText(p_file.name)
                else:
                    # 경로에 에러시, 기본 플레이어 설정
                    self.schedule_data_list[idx][SET_PLAYER] =None
                    self.schedule_widget_list[idx].lbl_setPlayer.setText("(U)사용자 선택")
            self.schedule_widget_list[idx].lbl_setPlayer.setStyleSheet("color: rgb(0, 0, 0);")
            self.schedule_widget_list[idx].btn_setPlayer.setEnabled(True)

        # .connect() 로 호출한 경우, 데이터 저장
        self.schedule_data_list[idx][SEL_PLAYER_NUM] = num

    ##################################################################
    # NEW
    ## action
    def actNew(self):
        self.schNew(3)
        ## debug
        # self.schClear()
        # print(f'schedule_data_list = {len(self.schedule_data_list)}')  # D1
        # print(f'schedule_widget_list = {len(self.schedule_widget_list)}')  # D2
        # print(f'playerActive_list = {len(self.playerActive_list)}')  # D3
        # print(f'vbox.count = {self.vbox.count()}')  # D4
    ##################################################################
    ####> .sch 저장 <#### 
    ## action
    def actSaveAs(self):
        getFile = QFileDialog.getSaveFileName(self, '스케줄 파일 저장', filter='*.sch')
        if getFile[0] != '':
            self._filePath = getFile[0]
            self.fileSave(getFile[0])

    ####>  file save  <####
    def fileSave(self, filePath):
        if filePath != None:
            # print(f'file save => {filePath}')

            # 저장 전 전처리
            for idx in range(len(self.schedule_data_list)):
                # 1) 임시 색상값 지우기
                #  WARNING_COLOR CLEAR
                self.schedule_data_list[idx][WARNING_COLOR] = 0
                # 2) mp3file Path 절대경로 > 상대 경로로 바꾸기
                mp3FilePath = self.schedule_data_list[idx][SET_MP3_FILE]
                if mp3FilePath != None:
                    r_mp3FilePath = self.relativePachCheck(mp3FilePath)
                    self.schedule_data_list[idx][SET_MP3_FILE] = r_mp3FilePath 

            # 파일이름 처리
            self.p_file = pathlib.Path(filePath)
            fileName = str(self.p_file.name).split('.')
            self.scheduleName = fileName[0]
            self.lbl_schName.setText(self.scheduleName)

            # 실제 데이터가 저장되는 부분
            # with open(f'{self.scheduleName}.sch', 'wb') as file:
            with open(f'{filePath}', 'wb') as file:
                pickle.dump(self.schedule_data_list, file)  # D1. 스케쥴 데이터 저장
                pickle.dump(self.playerActive_list, file)   # D3. 재생 활성화 리스트

            self.statusbar.showMessage(f'스케줄 "{filePath}" 파일이 저장되었습니다')
            print(f'스케줄 "{filePath}" 파일이 저장되었습니다')
            print(self.schedule_data_list)

            self.winDataSave()  # 윈도우 정보도 저장

    def btnFileSave(self):
        try:
            # 기존의 값이 있으면 바로 로드
            if self._filePath != '':
                # print(self._filePath)
                self.fileSave(self._filePath)
        except:
            # 에러가 발생하는 경우 탐색창에서 파일 선택
            self.actSaveAs()

    ##################################################################
    # LOAD
    ## action
    def actLoad(self):
        # https://codetorial.net/pyqt5/basics/toolbar.html
        getFile = QFileDialog.getOpenFileName(self, '스케줄 파일 열기', filter='*.sch')
        if getFile[0] != '':
            self._filePath = getFile[0]
            self.fileLoad(getFile[0])

    ####> file load <####
    def fileLoad(self, filePath):
        if filePath != None:
            self.p_file = pathlib.Path(filePath)
            fileName = str(self.p_file.name).split('.')
            self.scheduleName = fileName[0]
            self.lbl_schName.setText(self.scheduleName)

            ### 로드 전에 clear (D1 ~ D4 : DEL)
            self.schClear()

            with open(f'{filePath}', 'rb') as file:
                self.schedule_data_list = pickle.load(file)     # D1. data_list LOAD
                self.playerActive_list = pickle.load(file)      # D3. playerActive_list LOAD

                # self.statusbar.showMessage(f'스케줄 "{self.p_file.name}" 파일을 읽어왔습니다.')
                self.statusbar.showMessage(f'스케줄 "{filePath}" 파일을 읽어왔습니다.')
                print(f'load - {self.schedule_data_list}')

            # Load
            count = len(self.schedule_data_list)
            for idx in range(count):
                self.schAdd_widget(idx)                         # D2. widget_list CREATE
                self.displayScheduleLine(idx)                   # D4. display_widget CREATE

                # enable check
                self.slot_enableChk(idx, 2)

                # 실제 알람시간 툴팁에 보여주기 : te_setTime.setToolTeip
                if self.schedule_data_list[idx][REAL_ALARM_TIME] != None:
                    realAlarmTime = self.schedule_data_list[idx][REAL_ALARM_TIME] 
                    time_tmp = realAlarmTime.toString("AP hh:mm.ss")
                    self.schedule_widget_list[idx].te_setTime.setToolTip(f"예정 {time_tmp}")
                #

            print(f'스케줄 파일 "{filePath}"을 로드 했습니다.')

            self.music_list_reload()

    ## btn
    def btnFileLoad(self):
        try:
            # 기존의 값이 있으면 바로 로드
            if self._filePath != '':
                print(f'스케줄 파일 = {self._filePath}')
                self.fileLoad(self._filePath)
        except:
            # 에러가 발생하는 경우 탐색창에서 파일 선택
            print("sch 파일 읽기 오류")
            self.actLoad()

    ##################################################################
    ####> WIN_DATA_FINE_NAME.dat 저장 <#### 
    def winDataSave(self):
        # WIN_DATA_FINE_NAME.dat저장 할 때 : .sch 파일이 하위 경로에 있는 경우, 상대 경로로 변경
        r_filePath = self.relativePachCheck(self._filePath)

        with open(f'{WIN_DATA_FINE_NAME}', 'wb') as file:
            wsize = self.size()
            if self.SEL_FULL_SIZE_PLYAER_FG == True:
                wsize.setHeight(self.size().height() - HIGH_DIFF)
            else:
                wsize.setHeight(self.size().height() + HIGH_DIFF)
            pickle.dump(wsize, file)                        # 1) 현재 창 크기 저장
            # pickle.dump(self.size(), file) #오류 1) 현재 창 크기 저장(확장된 창 사이즈 미포함)
            # pickle.dump(self._filePath, file)               # 2) 현재 schedule 이름&경로 저장
            pickle.dump(r_filePath, file)               # 2) 현재 schedule 이름&경로 저장
            pickle.dump(self.TIME_WARNING_COLOR_FG, file)   # 3) Time Colokr check
            pickle.dump(self.SEL_FULL_SIZE_PLYAER_FG, file)    # 4) 인 플레이어 사이즈

            # print(f' winDataSave - r_filePath => {r_filePath}')

    def winDataLoad(self):
        try:
            with open(f'{WIN_DATA_FINE_NAME}', 'rb') as file:
                self.resize(pickle.load(file))                  # 1) 현재 창 크기 로드
                self._filePath = pickle.load(file)              # 2) 현재 schedule 이름 로드
                self.TIME_WARNING_COLOR_FG = pickle.load(file)  # 3) Time Colokr check
                self.SEL_FULL_SIZE_PLYAER_FG = pickle.load(file)   # 4) 인 플레이어 사이즈
                print(self._filePath)

                self.cb_timeColor.setChecked(self.TIME_WARNING_COLOR_FG)

                # 인 플레이어 사이즈
                if self.SEL_FULL_SIZE_PLYAER_FG == True:
                    self.rb_selFullPlayer.setChecked(True)
                    self.musicPlayerFullSize()
                    
                else:
                    self.rb_selMiniPlayer.setChecked(True)
                    self.musicPlayerMiniSize()

                self.sel_full_size_player_fg_signal.emit(self.SEL_FULL_SIZE_PLYAER_FG)
                
        except:
            pass

    ##################################################################

    def music_list_reload(self):
        # 삭제하기
        self.musicPlayer.songs_list.clear()
        self.musicPlayer.list_music.clear()
        # 검색하여 리스트 갱신하기
        if len(self.schedule_data_list) > 0:
            for idx in range(len(self.schedule_data_list)):
                filePath = self.schedule_data_list[idx][SET_MP3_FILE]
                if filePath != None:
                    self.music_list_add(filePath)

    def music_list_add(self, filePath):
        # 문제점) mp3file 를 교체하는 경우 반영되지 않고 계속 추가만 됨.
        # 노래 파일에 중복 여부 검사
        # if len(self.musicPlayer.songs_list) > 0:
        lst = [i[1] for i in self.musicPlayer.songs_list] # [파일명, 경로와 파일명]
        if filePath not in lst:
            # (+)노래 파일 리스트에 추가 songs_list = [[이름, 경로패스], []]
            p_path = pathlib.Path(filePath)
            self.musicPlayer.songs_list.append([p_path.name, filePath])     # song data list
            self.musicPlayer.list_music.addItem(p_path.name)                # widget list

    def music_list_del(self, filePath):

        # 2차원 배열에서 특정 열(column) 추출하기 https://maktubi.tistory.com/93
        lst = [i[1] for i in self.musicPlayer.songs_list]
        if filePath in lst:
            row = lst.index(filePath)       # 리스트 요소 삭제 https://wikidocs.net/16040
            del self.musicPlayer.songs_list[row]
            self.musicPlayer.list_music.takeItem(row)
            print(self.musicPlayer.songs_list)
        else:
            return


    def music_play(self, filePath): # playEndAct = False : 재생후 파일 목록 지우기
        self.musicPlayer.playLineMusicPath(filePath)
    
    def relativePachCheck(self, filePath):
        # 현재 폴더의 하위에 있으면, 상대폴더로 변환

        # 절대경로, 상대 경로 https://ai-creator.tistory.com/539
        # 문자열 찾기 https://codechacha.com/ko/python-find-str-in-str/
        localPath = os.getcwd().replace('\\','/')
        # print(f'localPath = {localPath}')

        # filePath.
        # print(f'현재 실행 경로> {localPath}')
        # print(f'현재 파일 경로> {filePath}')

        # print(filePath.find(localPath))

        if filePath.find(localPath) == 0:
            # print(filePath.replace(localPath, '.'))
            # print('true')
            return filePath.replace(localPath, '.') # 상대 경로 리턴
        else:
            # print('false')
            return filePath # 원본 경로 리턴


    ##################################################################

    def closeEvent(self, QCloseEvent):
        self.winDataSave()          # 윈도우 창 정보 저장
        replay = QMessageBox.question(self, "종료 확인", "종료 하시겠습니까?",
                                              QMessageBox.Yes | QMessageBox.No)

        if replay == QMessageBox.Yes:
            self.btnFileSave()      # 종료시 스케줄 정보 저장
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()    # 종료 이벤트를 무시

    ##################################################################
    def _aboutWindow(self):
        # 두번째 윈도우 열기 main(.. Ui_about ) 미포함하고 열기
        #   https://www.youtube.com/watch?v=R5N8TA0KFxc
        # self.window = QWidget()
        # self.ui = Ui_AboutWindow()
        # self.ui.setupUi(self.window)
        # self.window.show()

        # 두번째 윈도우 열기 main(.. Ui_about ) 포함여부 무관
        #  class AboutWindow() 만들어서 생성시
        self.ui_about = AboutWindow()
        self.ui_about.show()


# Qt Designer 로 된 파일을 위젯에 포함시키는 방법
class ScheduleLine(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # ui_quiz_before.Ui_select_quiz
        # self.show()


class AboutWindow(QWidget, Ui_About_From):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.btn_close.clicked.connect(self.close)
        self.btn_homePage.clicked.connect(self.homePage)
        self.btn_homePage.setText(f'{_HOMEPAGE}')

        self.lbl_ver.setText(f'{_VER}')
        self.lbl_maker.setText(f'{_MAKE}')
        # self.lbl_programName.setText()
        self.lbl_update.setText(f'{_UPDATE}')

    def homePage(self):
        webbrowser.open(f'{_HOMEPAGE}')

    def close(self):
        self.hide()



if __name__ == '__main__':
    # PySide6Ui('ui_menu_main.ui').toPy()
    # PySide6Ui('ui_schedule_line.ui').toPy()
    # PySide6Ui('ui_mp3player.ui').toPy()
    # PySide6Ui('ui_about.ui').toPy()

    app = QApplication(sys.argv)
    ex = MyApp()
    # app.setStyle('Fusion')
    # 출처: https://freeprog.tistory.com/333 [취미로 하는 프로그래밍 !!!]

    sys.exit(app.exec())
