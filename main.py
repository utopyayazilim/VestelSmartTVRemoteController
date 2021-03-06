import sys
from PyQt5 import QtWidgets, uic, QtCore, QtGui
from PyQt5.QtGui import QCursor, QIcon
from PyQt5.QtWidgets import QMessageBox, QMenu
import VestelTV
import channelDialog
import db
import settingsDialog
import volumeDialog
from VestelTV import VestelRemoteController


class Ui(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui, self).__init__()

        tv = VestelRemoteController()

        uic.loadUi("Templates/main.ui", self)

        settings_action = self.findChild(QtWidgets.QAction, 'actionSettings')
        settings_action.triggered.connect(self.openSettingsDialog)

        close_action = self.findChild(QtWidgets.QAction, 'actionQuit')
        close_action.triggered.connect(sys.exit)

        channel_action = self.findChild(QtWidgets.QAction, 'actionChannel')
        channel_action.triggered.connect(self.openChannelDialog)

        netflix_action = self.findChild(QtWidgets.QAction, 'actionNetflix')
        netflix_action.triggered.connect(tv.NetflixButton)

        youtube_action = self.findChild(QtWidgets.QAction, 'actionYouTube')
        youtube_action.triggered.connect(tv.YouTubeButton)

        volume_action = self.findChild(QtWidgets.QAction, 'actionVolume')
        volume_action.triggered.connect(self.openVolumeDialog)

        self.button = self.findChild(QtWidgets.QPushButton, 'btn1')
        self.button.clicked.connect(tv.btnOne)

        self.button = self.findChild(QtWidgets.QPushButton, 'btn2')
        self.button.clicked.connect(tv.btnTwo)

        self.button = self.findChild(QtWidgets.QPushButton, 'btn3')
        self.button.clicked.connect(tv.btnThree)

        self.button = self.findChild(QtWidgets.QPushButton, 'btn4')
        self.button.clicked.connect(tv.btnFour)

        self.button = self.findChild(QtWidgets.QPushButton, 'btn5')
        self.button.clicked.connect(tv.btnFive)

        self.button = self.findChild(QtWidgets.QPushButton, 'btn6')
        self.button.clicked.connect(tv.btnSix)

        self.button = self.findChild(QtWidgets.QPushButton, 'btn7')
        self.button.clicked.connect(tv.btnSeven)

        self.button = self.findChild(QtWidgets.QPushButton, 'btn8')
        self.button.clicked.connect(tv.btnEight)

        self.button = self.findChild(QtWidgets.QPushButton, 'btn9')
        self.button.clicked.connect(tv.btnNine)

        self.button = self.findChild(QtWidgets.QPushButton, 'btn0')
        self.button.clicked.connect(tv.btnZero)

        self.button = self.findChild(QtWidgets.QPushButton, 'okButton')
        self.button.clicked.connect(tv.OK)

        self.button = self.findChild(QtWidgets.QPushButton, 'VolumeUpButton')
        self.button.clicked.connect(tv.VolumeUp)

        self.button = self.findChild(QtWidgets.QPushButton, 'VolumeDownButton')
        self.button.clicked.connect(tv.VolumeDown)

        self.button = self.findChild(QtWidgets.QPushButton, 'backButton')
        self.button.clicked.connect(tv.Back)

        self.button = self.findChild(QtWidgets.QPushButton, 'ExitButton')
        self.button.clicked.connect(tv.Exit)

        self.button = self.findChild(QtWidgets.QPushButton, 'muteButton')
        self.button.clicked.connect(tv.Mute)

        self.button = self.findChild(QtWidgets.QPushButton, 'ProgramUpButton')
        self.button.clicked.connect(tv.pUp)

        self.button = self.findChild(QtWidgets.QPushButton, 'ProgramDownButton')
        self.button.clicked.connect(tv.pDown)

        self.button = self.findChild(QtWidgets.QPushButton, 'upButton')
        self.button.clicked.connect(tv.UpButton)

        self.button = self.findChild(QtWidgets.QPushButton, 'downButton')
        self.button.clicked.connect(tv.DownButton)

        self.button = self.findChild(QtWidgets.QPushButton, 'leftButton')
        self.button.clicked.connect(tv.LeftButton)

        self.button = self.findChild(QtWidgets.QPushButton, 'rightButton')
        self.button.clicked.connect(tv.RightButton)

        self.button = self.findChild(QtWidgets.QPushButton, 'powerButton')
        self.button.clicked.connect(tv.powerOnOffButton)

        self.button = self.findChild(QtWidgets.QPushButton, 'qMenuButton')
        self.button.clicked.connect(tv.OpenQMenu)

        self.button = self.findChild(QtWidgets.QPushButton, 'changeButton')
        self.button.clicked.connect(tv.changeButton)

        self.button = self.findChild(QtWidgets.QPushButton, 'btn3D')
        self.button.clicked.connect(tv.ThreeD)

        self.button = self.findChild(QtWidgets.QPushButton, 'menuButton')
        self.button.clicked.connect(tv.ThreeD)

        self.button = self.findChild(QtWidgets.QPushButton, 'sourceButton')
        self.button.clicked.connect(tv.ThreeD)

        self.button = self.findChild(QtWidgets.QPushButton, 'infoButton')
        self.button.clicked.connect(tv.InfoButton)

        self.button = self.findChild(QtWidgets.QPushButton, 'internetButton')
        self.button.clicked.connect(tv.InternetButton)

        self.button = self.findChild(QtWidgets.QPushButton, 'backwardButton')
        self.button.clicked.connect(tv.backwardButton)

        self.button = self.findChild(QtWidgets.QPushButton, 'recButton')
        self.button.clicked.connect(tv.recButton)

        self.button = self.findChild(QtWidgets.QPushButton, 'stopButton')
        self.button.clicked.connect(tv.stopButton)

        self.button = self.findChild(QtWidgets.QPushButton, 'playButton')
        self.button.clicked.connect(tv.playButton)

        self.button = self.findChild(QtWidgets.QPushButton, 'pauseButton')
        self.button.clicked.connect(tv.pauseButton)

        self.button = self.findChild(QtWidgets.QPushButton, 'forwardButton')
        self.button.clicked.connect(tv.forwardButton)

        self.button = self.findChild(QtWidgets.QPushButton, 'mediaButton')
        self.button.clicked.connect(tv.mediaButton)

        self.button = self.findChild(QtWidgets.QPushButton, 'subtitleButton')
        self.button.clicked.connect(tv.subtitleButton)

        self.button = self.findChild(QtWidgets.QPushButton, 'languageButton')
        self.button.clicked.connect(tv.languageButton)

        self.button = self.findChild(QtWidgets.QPushButton, 'epgButton')
        self.button.clicked.connect(tv.epgButton)

        self.button = self.findChild(QtWidgets.QPushButton, 'teletextButton')
        self.button.clicked.connect(tv.teletextButton)

        self.button = self.findChild(QtWidgets.QPushButton, 'redButton')
        self.button.clicked.connect(tv.redButton)

        self.button = self.findChild(QtWidgets.QPushButton, 'yellowButton')
        self.button.clicked.connect(tv.yellowButton)

        self.button = self.findChild(QtWidgets.QPushButton, 'blueButton')
        self.button.clicked.connect(tv.blueButton)

        self.button = self.findChild(QtWidgets.QPushButton, 'greenButton')
        self.button.clicked.connect(tv.greenButton)

        self.button = self.findChild(QtWidgets.QPushButton, 'NetflixButton')
        self.button.clicked.connect(tv.NetflixButton)

        self.button = self.findChild(QtWidgets.QPushButton, 'YouTubeButton')
        self.button.clicked.connect(tv.YouTubeButton)

        self.show()

        self.checkConfig()

    def contextMenuEvent(self, event):
        contextMenu = QMenu(self)
        contextMenu.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        volume = contextMenu.addAction("Volume")
        volume.setIcon(QtGui.QIcon('Templates/img/volume-up.png'))

        goto_channel = contextMenu.addAction("Go to channel")
        goto_channel.setIcon(QtGui.QIcon('Templates/img/channel.png'))

        settings = contextMenu.addAction("Settings")
        settings.setIcon(QtGui.QIcon('Templates/img/settings.png'))

        quitAct = contextMenu.addAction("Quit")
        quitAct.setIcon(QtGui.QIcon('Templates/img/quit.png'))

        action = contextMenu.exec_(self.mapToGlobal(event.pos()))
        if action == quitAct:
            sys.exit()
        elif action == volume:
            self.openVolumeDialog()
        elif action == settings:
            self.openSettingsDialog()
        elif action == goto_channel:
            self.openChannelDialog()
        else:
            pass

    def checkConfig(self):
        ip_address = db.select_ip()
        if ip_address is None or ip_address == "":
            settingsDialog.SettingsDialog(self).exec()
        else:
            if VestelTV.tv_accessible_check(ip_address):
                pass
            else:
                self.messageBox()

    def messageBox(self):
        QMessageBox().setIcon(QMessageBox.Information)
        QMessageBox.information(self, "Warning", "TV is not accessible, please check your TV or network!")
        settingsDialog.SettingsDialog(self).exec()

    def openSettingsDialog(self):
        settingsDialog.SettingsDialog(self).exec()

    def openChannelDialog(self):
        channelDialog.channelDialog(self).exec()

    def openVolumeDialog(self):
        volumeDialog.volumeDialog(self).exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
