'''
Pyqt5 realizes a simple music player (upgrade to V2 version)
출처 : https://chowdera.com/2021/05/20210506082607288s.html
'''

from audioop import mul
import os, sys, time, datetime, pickle, webbrowser, subprocess
import pathlib

from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtTest import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtMultimedia import *

## .ui -> .py ##
from pyside6_uic import PySide6Ui
from ui_mp3player import Ui_mp3player


TIME_REFLASH = 500 #

class musicplayer(QWidget, Ui_mp3player):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # ui_quiz_before.Ui_select_quiz
        self.init()
    
    def init(self):

        self.song_formats = ['mp3', 'm4a', 'flac', 'wav', 'ogg']
        self.songs_list = []
        self.cur_playing_song = ''
        self.is_pause = True
        self.playEndfileClear_fg = False

        # bten
        # self.btn_open.clicked.connect(self.openMusicFolder)
        self.btn_play.clicked.connect(self.playCurMusic)
        self.btn_stop.clicked.connect(self.playStop)
        self.btn_next.clicked.connect(self.nextMusic)
        self.btn_pre.clicked.connect(self.preMusic)

        # self.btn_mplay.clicked.connect(self.playCurMusic)
        self.btn_mplay.clicked.connect(self.playLineMusic)
        self.btn_mstop.clicked.connect(self.playStop)
        # self.btn_mnext.clicked.connect(self.nextMusic)
        # self.btn_mpre.clicked.connect(self.preMusic)

        # 1. Add for playback / New members of the pause function ：
        #   https://doc.qt.io/qtforpython/PySide6/QtMultimedia/QMediaPlayer.html
        self.musicPlayer = QMediaPlayer()
        # # 2. 오디오 장치 선택 / 현재 기본 장치
        self.audio_output = QAudioOutput()
        self.musicPlayer.setAudioOutput(self.audio_output)
        self.musicPlayer.positionChanged.connect(self.positionChanged)

        
        self.lbl_audioOut.setText(f'{QMediaDevices.defaultAudioOutput().description()}')    # full
        text = QMediaDevices.defaultAudioOutput().description().split('(')
        self.lbl_maudioOut.setText(f'{text[0]}')   # mini
        # print(type(QMediaDevices.defaultAudioOutput().id()))

        self.mediaDevice = QMediaDevices()
        self.mediaDevice.audioOutputsChanged.connect(self.audioOutputChanged)

        self.list_music.currentRowChanged.connect(self.currentChanged)
        self.slider_progress.valueChanged.connect(self.valueChanged)     # full
        self.slider_mprogress.valueChanged.connect(self.valueChanged)    # mini
        

        ### 중요 문제점 해결 ( )###
        #  > 오디오 출력 설정 : "QMediaPlayer().setAudioOutput(QAudioOutput())"
        # 1. 1회 오디오 출력설정시 => 스피커 <-> 이어폰 전환시, 출력 방향 전환이 되지 않음.
        # 2. 매번 플레이 전 오디오 출력설정시 => 파일 1회 재생후 재생 못하는 버그
        # 3. 해결 방안 => 장치 변경 여부를 검사하여 변경시에만, >오디오 출력 설정을 변경 시키기
        #  
        # QMediaDEvice - > QAudioOutput
        #   https://doc.qt.io/qtforpython/PySide6/QtMultimedia/QAudioOutput.html#PySide6.QtMultimedia.PySide6.QtMultimedia.QAudioOutput
        #
        #   PySide6.QtMultimedia.QAudioOutput(device[, parent=None])
        #
        #       https://doc.qt.io/qtforpython/PySide6/QtMultimedia/QAudioOutput.html
        #       https://doc.qt.io/qtforpython-6/PySide6/QtMultimedia/QMediaDevices.html
        #
        #       print(QMediaDevices.audioOutputs())                        # 오디오 출력 가능한 장치 리스트 목록 출력
        #       print(QMediaDevices.defaultAudioOutput())                  # 현재 출력장치
        #
        # print(f'1 > {type(self.audio_output)} {self.audio_output}')
        # print(f'2 > {type(QAudioOutput(QMediaDevices.audioOutputs()[0]))} {QMediaDevices.audioOutputs()}')

        self.is_switching = False

        # self.timer = QTimer()
        # self.timer.start(TIME_REFLASH)
        # self.timer.timeout.connect(self.playByMode)

        # TEST
        # self.openStartFoler()


    # device changed
    # @Slot()
    def audioOutputChanged(self):
        
        print('오디오 변경 >' , end =' ') 
        # print(QMediaDevices.defaultAudioOutput().description())
        # for i in QMediaDevices.audioOutputs():
        #     print(i.description(), end = ', ')
        # print('')

        if self.musicPlayer.playbackState() != QMediaPlayer.StoppedState:
            self.audio_output.setDevice(QMediaDevices.defaultAudioOutput())
        else:
            ### 버그 : 출력장치 변경시, 1회 재생못하는 문제 해결책 ###
            del self.audio_output   # 객체 삭제후 재생성하여 사용
            del self.musicPlayer

            self.musicPlayer = QMediaPlayer()
            self.audio_output = QAudioOutput()
            self.musicPlayer.setAudioOutput(self.audio_output)
            self.musicPlayer.positionChanged.connect(self.positionChanged)
        
        self.lbl_audioOut.setText(f'{QMediaDevices.defaultAudioOutput().description()}')    # full
        text = QMediaDevices.defaultAudioOutput().description().split('(')
        self.lbl_maudioOut.setText(f'{text[0]}')   # mini
    
    # Tips
    def tips(self, message):
        QMessageBox.about(self, ' Tips', message)

    # PyQt6
    # https://stackoverflow.com/questions/69415713/playing-sounds-with-pyqt6

    def currentChanged(self, row):
        if self.musicPlayer.playbackState() == QMediaPlayer.StoppedState:
            self.cur_playing_song = self.songs_list[self.list_music.currentRow()][-1]
            self.lbl_playFile.setText(f'{self.songs_list[self.list_music.currentRow()][0]}')    # full
            # self.lbl_mplayFile.setText(f'{self.songs_list[self.list_music.currentRow()][0]}')   # mini
            ## test
            self.sliderMax()

    # Full "Play"
    def playCurMusic(self):
        self.playEndfileClear_fg = False
        if self.list_music.count() == 0:
            self.Tips(' There is no music file to play in the current path ')
            return
        if self.musicPlayer.playbackState() == QMediaPlayer.StoppedState:
            self.slider_progress.setValue(0); self.slider_mprogress.setValue(0)
            self.musicPlayer.stop() # 출력 전환시 재생 
            # self.musicPlayer.setPosition(0)
            # 재생
            self.selCurPlaying()
            # "일시정지"로 표시
            self.btn_play.setText('Pause')
            self.btn_mplay.setText('Pause'); self.btn_mplay.setEnabled(True)

        elif self.musicPlayer.playbackState() == QMediaPlayer.PlayingState:
            # 일시정지
            self.musicPlayer.pause()
            # "플레이"로 표시
            self.btn_play.setText('Play')
            self.btn_mplay.setText('Play'); self.btn_mplay.setEnabled(True)

        elif self.musicPlayer.playbackState() == QMediaPlayer.PausedState:
            # 재생
            self.musicPlayer.play()
            # "일시정지"
            self.btn_play.setText('Pause')
            self.btn_mplay.setText('Pause'); self.btn_mplay.setEnabled(True)
    # Write and play the currently set music function 
    def selCurPlaying(self):
        # 기본 오디오 장치 변경 여부 검사하기
        self.cur_playing_song = self.songs_list[self.list_music.currentRow()][-1]
        self.musicPlayer.setSource(QUrl.fromLocalFile(self.cur_playing_song))
        self.lbl_playFile.setText(f'{self.songs_list[self.list_music.currentRow()][0]}')    # full
        self.lbl_mplayFile.setText(f'{self.songs_list[self.list_music.currentRow()][0]}')   # mini
        self.audio_output.setVolume(50)
        self.musicPlayer.play()
        print('sel CurPlaying play')

    # mini "mPlay()" 버튼을 누르는 경우
    def playLineMusic(self):
        if self.musicPlayer.playbackState() == QMediaPlayer.StoppedState:
            self.slider_progress.setValue(0); self.slider_mprogress.setValue(0)

        elif self.musicPlayer.playbackState() == QMediaPlayer.PlayingState:
            # 일시정지
            self.musicPlayer.pause()
            # "플레이"로 표시
            self.btn_play.setText('Play')
            self.btn_mplay.setText('Play'); self.btn_mplay.setEnabled(True)
        elif self.musicPlayer.playbackState() == QMediaPlayer.PausedState:
            # 재생
            self.musicPlayer.play()
            # "일시정지"
            self.btn_play.setText('Pause')
            self.btn_mplay.setText('Pause')
        # self.playEndfileClear_fg = True
        # self.musicPlayer.setSource(QUrl.fromLocalFile(filePath))
        # p_file = pathlib.Path(filePath)
        # # mini
        # self.lbl_playFile.setText(f'{p_file.name}'); self.lbl_mplayFile.setText(f'{p_file.name}')
        # self.musicPlayer.play()
        # print('play Line Music play')
        # self.btn_play.setText('Pause'); self.btn_mplay.setText('Pause')

    # "Play(filePath)" main.py 로 부터 Line 재생 명령을 받는 경우
    def playLineMusicPath(self, filePath):
        self.playEndfileClear_fg = True
        self.musicPlayer.setSource(QUrl.fromLocalFile(filePath))
        p_file = pathlib.Path(filePath)
        # full
        self.lbl_playFile.setText(f'{p_file.name}'); self.lbl_mplayFile.setText(f'{p_file.name}')
        # if self.musicPlayer.playbackState() == QMediaPlayer.PausedState:
        self.musicPlayer.stop()
        self.musicPlayer.play()

        self.btn_play.setText('Pause')
        self.btn_mplay.setText('Pause');self.btn_mplay.setEnabled(True)

    def playStop(self):
        self.musicPlayer.stop()
        self.btn_play.setText('Play')
        self.btn_mplay.setText('Play');self.btn_mplay.setDisabled(True)
        if self.playEndfileClear_fg == True:  # 
            # False 파일명 지우기
            self.cur_playing_song = None
            self.lbl_playFile.setText(f'')    # full
            self.lbl_mplayFile.setText(f'')   # mini
        else:
            # True 파일명 그대로 두기
            pass

    def preMusic(self):
        self.musicPlayer.stop()
        self.slider_progress.setValue(0); self.slider_mprogress.setValue(0)
        if self.list_music.count() == 0:
            self.Tips(' There is no music file to play in the current path ')
            return
        pre_row = self.list_music.currentRow()-1 if self.list_music.currentRow() != 0 else self.list_music.count() - 1
        self.list_music.setCurrentRow(pre_row)

        ## test
        self.sliderMax()

    def nextMusic(self):
        self.musicPlayer.stop()
        self.slider_progress.setValue(0); self.slider_mprogress.setValue(0)
        if self.list_music.count() == 0:
            self.Tips(' There is no music file to play in the current path ')
            return
        next_row = self.list_music.currentRow()+1 if self.list_music.currentRow() != self.list_music.count()-1 else 0
        self.list_music.setCurrentRow(next_row)

        ## test
        self.sliderMax()

    def valueChanged(self, position):
        self.musicPlayer.setPosition(position)


    def positionChanged(self, position):
        # full
        self.slider_progress.setMinimum(0); self.slider_mprogress.setMinimum(0)
        self.slider_progress.setMaximum(self.musicPlayer.duration()); self.slider_mprogress.setMaximum(self.musicPlayer.duration())
        
        # self.SEL_FULL_SIZE_PLYAER_FG 변수가 있는지 확인
        #    https://www.delftstack.com/ko/howto/python/python-check-if-variable-exists/
        if 'self.SEL_FULL_SIZE_PLYAER_FG' in locals():
            # 변수가 있으면
            # <문제점>
            # mp3파일 재생 > slider_progress 진행막대 진행시, 소리 늘어짐 발생
            if self.SEL_FULL_SIZE_PLYAER_FG:
                self.slider_progress.setValue(position);     # full
            else:
                self.slider_mprogress.setValue(position)     # mini
        else:
            # 변수가 없으면
            self.slider_progress.setValue(position);     # full
            self.slider_mprogress.setValue(position)     # mini

        # full
        self.lbl_startTime.setText(time.strftime('%M:%S', time.localtime(self.musicPlayer.position()/1000)))
        self.lbl_endTime.setText(time.strftime('%M:%S', time.localtime(self.musicPlayer.duration()/1000)))
        # mini
        self.lbl_mstartTime.setText(time.strftime('%M:%S', time.localtime(self.musicPlayer.position()/1000)))
        self.lbl_mendTime.setText(time.strftime('%M:%S', time.localtime(self.musicPlayer.duration()/1000)))

        if self.musicPlayer.duration() == position:
            self.btn_play.setText('Play')
            self.btn_mplay.setText('Play'); self.btn_mplay.setDisabled(True)

            if self.playEndfileClear_fg == True:
                # False 파일명 지우기
                self.cur_playing_song = None
                self.lbl_playFile.setText(f'')    # full
                self.lbl_mplayFile.setText(f'')   # mini
            else:
                # True 파일명 그대로 두기
                self.lbl_mplayFile.setText(f'')   # mini

    def sliderMax(self):
        self.cur_playing_song = self.songs_list[self.list_music.currentRow()][-1]
        self.musicPlayer.setSource(QUrl.fromLocalFile(self.cur_playing_song))
        # full
        self.slider_progress.setMaximum(self.musicPlayer.duration()); self.slider_progress.setMaximum(self.musicPlayer.duration())


    # def playByMode(self):
    #     #  Refresh progress bar
    #     if self.musicPlayer.playbackState() == QMediaPlayer.PlayingState:
    #         self.slider.setMinimum(0)
    #         self.slider.setMaximum(self.musicPlayer.duration())
    #         self.slider.setValue(self.slider.value() + TIME_REFLASH)
            
    #     self.lbl_startTime.setText(time.strftime('%M:%S', time.localtime(self.musicPlayer.position()/1000)))
    #     self.lbl_endTime.setText(time.strftime('%M:%S', time.localtime(self.musicPlayer.duration()/1000)))

    #     if self.musicPlayer.position() == self.musicPlayer.duration():
    #         self.btn_play.setText('Play')


    # test용 start open foler
    # open foler
    def openStartFoler(self):
        self.cur_path =('./')
        self.showMusicList()
        self.cur_playing_song=''
        self.lbl_startTime.setText('00:00')
        self.lbl_endTime.setText('00:00')
        self.slider_progress.setSliderPosition(0); self.slider_mprogress.setSliderPosition(0)
        self.is_pause = True
        self.btn_play.setText('Play')
        self.btn_mplay.setText('Play')
    

    # open foler
    def openMusicFolder(self):
        self.cur_path = QFileDialog.getExistingDirectory(self, "Select the music folder", './')
        if self.cur_path:
            print(self.cur_path)
            self.showMusicList()
            self.cur_playing_song=''
            self.lbl_startTime.setText('00:00')
            self.lbl_endTime.setText('00:00')
            self.slider_progress.setSliderPosition(0); self.slider_mprogress.setSliderPosition(0)
            self.is_pause = True
            self.btn_play.setText('Play')
            self.btn_mplay.setText('Play'); self.btn_mplay.setEnabled(True)
    
    # show misic list
    def showMusicList(self):
        self.list_music.clear()
        for song in os.listdir(self.cur_path):  # 특정 폴더의 파일 리스트 가져오기
            if song.split('.')[-1] in self.song_formats:
                self.songs_list.append([song, os.path.join(self.cur_path, song).replace('\\', '/')])
                self.list_music.addItem(song)
        self.list_music.setCurrentRow(0)
        if self.songs_list:
            self.cur_playing_song = self.songs_list[self.list_music.currentRow()][-1] # -1 리스트 마지막 요소 접근

    # slot
    @Slot(bool)
    def playerSize_slot(self, fg):
        self.SEL_FULL_SIZE_PLYAER_FG = fg
        print(f'Signal = {fg}')


# # Qt Designer 로 된 파일을 위젯에 포함시키는 방법
# class mp3player(QWidget, Ui_Form):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)  # ui_quiz_before.Ui_select_quiz
#         # self.show()


if __name__ == '__main__':
    PySide6Ui('ui_mp3player.ui').toPy()

    app = QApplication(sys.argv)
    ex = musicplayer()
    ex.openStartFoler()
    # app.setStyle('Fusion')
    # 출처: https://freeprog.tistory.com/333 [취미로 하는 프로그래밍 !!!]
    ex.show()

    sys.exit(app.exec())
