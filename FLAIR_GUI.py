from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
from flair_resources_files import resources3

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from PyQt5.QtSerialPort import QSerialPortInfo

from TOP_PANEL.host_connect import HostConnectButton
from TOP_PANEL.flight_file_upload_button_2 import FlightFileUploadButton
from TOP_PANEL.data_upload_button_2 import DataUploadButton
from TOP_PANEL.flight_file_export_button import FlightFileExportButton
from TOP_PANEL.clear_graphs_button import ClearGraphsButton

from SIDE_PANEL.side_panel_buttons2 import sidePanelButtonModule

from SETTINGS_PAGE.default_data_file import SettingsModule

import pyqtgraph.opengl as gl
import numpy as np

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1707, 954)
        MainWindow.setStyleSheet("background:#1c2b38;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 20, 20, 0)
        self.horizontalLayout.setSpacing(11)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.side_panel = QtWidgets.QFrame(self.centralwidget)
        self.side_panel.setMaximumSize(QtCore.QSize(207, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.side_panel.setFont(font)
        self.side_panel.setStyleSheet("QFrame#side_panel {\n"
"    background:#7ca6c0;\n"
"    border-top-right-radius: 25px;\n"
"    border-bottom-right-radius:25px;\n"
"    border: 2px solid;\n"
"}")
        self.side_panel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.side_panel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.side_panel.setObjectName("side_panel")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.side_panel)
        self.verticalLayout_5.setContentsMargins(4, 4, 0, 0)
        self.verticalLayout_5.setSpacing(13)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.side_panel_1 = QtWidgets.QFrame(self.side_panel)
        self.side_panel_1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.side_panel_1.setStyleSheet("background: transparent;")
        self.side_panel_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.side_panel_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.side_panel_1.setObjectName("side_panel_1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.side_panel_1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.team_logo_2 = QtWidgets.QFrame(self.side_panel_1)
        self.team_logo_2.setMinimumSize(QtCore.QSize(147, 159))
        self.team_logo_2.setMaximumSize(QtCore.QSize(16777215, 175))
        self.team_logo_2.setStyleSheet("QFrame#team_logo_2{\n"
"    background:transparent;\n"
"    background-image: url(:/team_logo/team_sammard_logo_resize2.png);\n"
"    border-top-right-radius: 25px;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}")
        self.team_logo_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.team_logo_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.team_logo_2.setObjectName("team_logo_2")
        self.verticalLayout_4.addWidget(self.team_logo_2)
        self.teamID_frame = QtWidgets.QFrame(self.side_panel_1)
        self.teamID_frame.setMinimumSize(QtCore.QSize(0, 50))
        self.teamID_frame.setMaximumSize(QtCore.QSize(16777215, 62))
        self.teamID_frame.setStyleSheet("background: white;\n"
"border-radius: 25px;\n"
"border: 2px solid black;")
        self.teamID_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.teamID_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.teamID_frame.setObjectName("teamID_frame")
        self.horizontalLayout_41 = QtWidgets.QHBoxLayout(self.teamID_frame)
        self.horizontalLayout_41.setContentsMargins(5, 0, 0, 0)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName("horizontalLayout_41")
        self.teamID = QtWidgets.QLabel(self.teamID_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.teamID.sizePolicy().hasHeightForWidth())
        self.teamID.setSizePolicy(sizePolicy)
        self.teamID.setMinimumSize(QtCore.QSize(0, 0))
        self.teamID.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.teamID.setFont(font)
        self.teamID.setStyleSheet("background: transparent;\n"
"border-radius: 25px;\n"
"border: 0px solid black;")
        self.teamID.setAlignment(QtCore.Qt.AlignCenter)
        self.teamID.setObjectName("teamID")
        self.horizontalLayout_41.addWidget(self.teamID)
        self.verticalLayout_4.addWidget(self.teamID_frame)
        self.mission_time_frame = QtWidgets.QFrame(self.side_panel_1)
        self.mission_time_frame.setMaximumSize(QtCore.QSize(16777215, 110))
        self.mission_time_frame.setStyleSheet("background: white;\n"
"border-radius: 15px;\n"
"border: 2px solid black;")
        self.mission_time_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mission_time_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mission_time_frame.setObjectName("mission_time_frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.mission_time_frame)
        self.gridLayout_2.setContentsMargins(6, 9, 0, 9)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.mission_time_icon = QtWidgets.QLabel(self.mission_time_frame)
        self.mission_time_icon.setStyleSheet("background: transparent;\n"
"border-radius: 15px;\n"
"border: 0px solid black;")
        self.mission_time_icon.setText("")
        self.mission_time_icon.setPixmap(QtGui.QPixmap("C:\\Users\\iqras\\OneDrive\\Documents\\Team Sammard\\Team_Sammard\\SA_CUP_2024\\SA_CUP_2024_GUI_Final\\SA_CUP_2024-dev_samigang2final\\SA_CUP_2024-dev_samigang2\\Image_resources/sidePanel/Time.png"))
        self.mission_time_icon.setAlignment(QtCore.Qt.AlignCenter)
        self.mission_time_icon.setObjectName("mission_time_icon")
        self.gridLayout_2.addWidget(self.mission_time_icon, 1, 0, 1, 1, QtCore.Qt.AlignTop)
        self.mission_time_label = QtWidgets.QLabel(self.mission_time_frame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mission_time_label.setFont(font)
        self.mission_time_label.setStyleSheet("background: transparent;\n"
"border-radius: 15px;\n"
"border: 0px solid black;")
        self.mission_time_label.setAlignment(QtCore.Qt.AlignCenter)
        self.mission_time_label.setObjectName("mission_time_label")
        self.gridLayout_2.addWidget(self.mission_time_label, 0, 0, 1, 2, QtCore.Qt.AlignBottom)
        self.mission_time = QtWidgets.QFrame(self.mission_time_frame)
        self.mission_time.setStyleSheet("background: transparent;\n"
"border-radius: 15px;\n"
"border: 0px solid black;")
        self.mission_time.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mission_time.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mission_time.setObjectName("mission_time")
        self.verticalLayout_67 = QtWidgets.QVBoxLayout(self.mission_time)
        self.verticalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_67.setObjectName("verticalLayout_67")
        self.mission_time_text = QtWidgets.QTextEdit(self.mission_time)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mission_time_text.sizePolicy().hasHeightForWidth())
        self.mission_time_text.setSizePolicy(sizePolicy)
        self.mission_time_text.setMinimumSize(QtCore.QSize(118, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mission_time_text.setFont(font)
        self.mission_time_text.setStyleSheet("background:transparent;")
        self.mission_time_text.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.mission_time_text.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.mission_time_text.setReadOnly(True)
        self.mission_time_text.setObjectName("mission_time_text")
        self.verticalLayout_67.addWidget(self.mission_time_text)
        self.gridLayout_2.addWidget(self.mission_time, 1, 1, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 2)
        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setRowStretch(1, 2)
        self.verticalLayout_4.addWidget(self.mission_time_frame)
        self.packet_count_frame = QtWidgets.QFrame(self.side_panel_1)
        self.packet_count_frame.setMinimumSize(QtCore.QSize(179, 0))
        self.packet_count_frame.setMaximumSize(QtCore.QSize(16777215, 110))
        self.packet_count_frame.setStyleSheet("background: white;\n"
"border-radius: 15px;\n"
"border: 2px solid black;")
        self.packet_count_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.packet_count_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.packet_count_frame.setObjectName("packet_count_frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.packet_count_frame)
        self.gridLayout_3.setContentsMargins(6, 9, 0, 9)
        self.gridLayout_3.setHorizontalSpacing(6)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.packet_count_icon = QtWidgets.QLabel(self.packet_count_frame)
        self.packet_count_icon.setStyleSheet("background: transparent;\n"
"border-radius: 15px;\n"
"border: 0px solid black;")
        self.packet_count_icon.setText("")
        self.packet_count_icon.setPixmap(QtGui.QPixmap("C:\\Users\\iqras\\OneDrive\\Documents\\Team Sammard\\Team_Sammard\\SA_CUP_2024\\SA_CUP_2024_GUI_Final\\SA_CUP_2024-dev_samigang2final\\SA_CUP_2024-dev_samigang2\\Image_resources/sidePanel/Abacus.png"))
        self.packet_count_icon.setAlignment(QtCore.Qt.AlignCenter)
        self.packet_count_icon.setObjectName("packet_count_icon")
        self.gridLayout_3.addWidget(self.packet_count_icon, 1, 0, 1, 1, QtCore.Qt.AlignTop)
        self.packet_count_label = QtWidgets.QLabel(self.packet_count_frame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.packet_count_label.setFont(font)
        self.packet_count_label.setStyleSheet("background: transparent;\n"
"border-radius: 15px;\n"
"border: 0px solid black;")
        self.packet_count_label.setObjectName("packet_count_label")
        self.gridLayout_3.addWidget(self.packet_count_label, 0, 0, 1, 2, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.packet_count = QtWidgets.QFrame(self.packet_count_frame)
        self.packet_count.setMaximumSize(QtCore.QSize(16777215, 51))
        self.packet_count.setStyleSheet("background: transparent;\n"
"border-radius: 15px;\n"
"border: 0px solid black;")
        self.packet_count.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.packet_count.setFrameShadow(QtWidgets.QFrame.Raised)
        self.packet_count.setObjectName("packet_count")
        self.verticalLayout_77 = QtWidgets.QVBoxLayout(self.packet_count)
        self.verticalLayout_77.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_77.setObjectName("verticalLayout_77")
        self.packet_count_text = QtWidgets.QTextEdit(self.packet_count)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.packet_count_text.sizePolicy().hasHeightForWidth())
        self.packet_count_text.setSizePolicy(sizePolicy)
        self.packet_count_text.setMinimumSize(QtCore.QSize(118, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.packet_count_text.setFont(font)
        self.packet_count_text.setStyleSheet("background:transparent;")
        self.packet_count_text.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.packet_count_text.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.packet_count_text.setReadOnly(True)
        self.packet_count_text.setObjectName("packet_count_text")
        self.verticalLayout_77.addWidget(self.packet_count_text)
        self.gridLayout_3.addWidget(self.packet_count, 1, 1, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setRowStretch(0, 1)
        self.verticalLayout_4.addWidget(self.packet_count_frame)
        self.trigger_frame = QtWidgets.QFrame(self.side_panel_1)
        self.trigger_frame.setMinimumSize(QtCore.QSize(0, 50))
        self.trigger_frame.setMaximumSize(QtCore.QSize(16777215, 62))
        self.trigger_frame.setStyleSheet("background: white;\n"
"border-radius: 25px;\n"
"border: 2px solid black;")
        self.trigger_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.trigger_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.trigger_frame.setObjectName("trigger_frame")
        self.verticalLayout_78 = QtWidgets.QVBoxLayout(self.trigger_frame)
        self.verticalLayout_78.setContentsMargins(0, 6, 0, 0)
        self.verticalLayout_78.setSpacing(0)
        self.verticalLayout_78.setObjectName("verticalLayout_78")
        self.trigger_value = QtWidgets.QTextEdit(self.trigger_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.trigger_value.sizePolicy().hasHeightForWidth())
        self.trigger_value.setSizePolicy(sizePolicy)
        self.trigger_value.setMinimumSize(QtCore.QSize(0, 0))
        self.trigger_value.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.trigger_value.setFont(font)
        self.trigger_value.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.trigger_value.setAutoFillBackground(False)
        self.trigger_value.setStyleSheet("background: transparent;\n"
"border-radius: 25px;\n"
"border: 0px solid black;")
        self.trigger_value.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.trigger_value.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.trigger_value.setReadOnly(True)
        self.trigger_value.setPlaceholderText("")
        self.trigger_value.setObjectName("trigger_value")
        self.verticalLayout_78.addWidget(self.trigger_value, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_4.addWidget(self.trigger_frame)
        self.verticalLayout_5.addWidget(self.side_panel_1)
        self.side_panel_2 = QtWidgets.QFrame(self.side_panel)
        self.side_panel_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.side_panel_2.setStyleSheet("background: transparent;\n"
"border-top: 2px solid black;")
        self.side_panel_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.side_panel_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.side_panel_2.setObjectName("side_panel_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.side_panel_2)
        self.verticalLayout_6.setContentsMargins(0, -1, 0, 50)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.home_button_frame = QtWidgets.QFrame(self.side_panel_2)
        self.home_button_frame.setMinimumSize(QtCore.QSize(0, 0))
        self.home_button_frame.setMaximumSize(QtCore.QSize(16777215, 55))
        self.home_button_frame.setStyleSheet("QFrame {\n"
"    border-top:0px;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QFrame:hover {\n"
"    background: transparent;\n"
"    border-top: 2px solid black;\n"
"    border-top-left-radius: 25px;\n"
"    border-bottom-left-radius: 25px;\n"
"    border-left: 2px solid black;\n"
"    border-bottom: 2px solid black;\n"
"}\n"
"")
        self.home_button_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.home_button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.home_button_frame.setObjectName("home_button_frame")
        self.verticalLayout_86 = QtWidgets.QVBoxLayout(self.home_button_frame)
        self.verticalLayout_86.setContentsMargins(2, 2, 0, 2)
        self.verticalLayout_86.setSpacing(0)
        self.verticalLayout_86.setObjectName("verticalLayout_86")
        self.home_button = QtWidgets.QPushButton(self.home_button_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.home_button.sizePolicy().hasHeightForWidth())
        self.home_button.setSizePolicy(sizePolicy)
        self.home_button.setMinimumSize(QtCore.QSize(0, 50))
        self.home_button.setMaximumSize(QtCore.QSize(16777215, 55))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.home_button.setFont(font)
        self.home_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.home_button.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border-top-left-radius: 25px;\n"
"    border-bottom-left-radius: 25px;\n"
"    border-image:url(:/Side_panel/Image_resources/sidePanel/home2.png);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-image: url(:/Side_panel/Image_resources/sidePanel/home1.png);\n"
"    border-top-left-radius: 25px;\n"
"    border-bottom-left-radius: 25px;\n"
"    border-bottom-right-radius:0px;\n"
"}\n"
"QPushButton:Pressed{\n"
"    background-color: transparent;\n"
"    border-top-left-radius: 25px;\n"
"    border-bottom-left-radius: 25px;\n"
"    border-image:url(:/Side_panel/Image_resources/sidePanel/home2.png);\n"
"    border: none;\n"
"}")
        self.home_button.setText("")
        self.home_button.setDefault(False)
        self.home_button.setFlat(False)
        self.home_button.setObjectName("home_button")
        self.verticalLayout_86.addWidget(self.home_button)
        self.verticalLayout_6.addWidget(self.home_button_frame)
        self.graphs_button_frame = QtWidgets.QFrame(self.side_panel_2)
        self.graphs_button_frame.setMinimumSize(QtCore.QSize(0, 55))
        self.graphs_button_frame.setMaximumSize(QtCore.QSize(16777215, 55))
        self.graphs_button_frame.setStyleSheet("QFrame {\n"
"    border-top:0px;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QFrame:hover {\n"
"    background: transparent;\n"
"    border-top: 2px solid black;\n"
"    border-top-left-radius: 25px;\n"
"    border-bottom-left-radius: 25px;\n"
"    border-left: 2px solid black;\n"
"    border-bottom: 2px solid black;\n"
"}\n"
"")
        self.graphs_button_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.graphs_button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.graphs_button_frame.setObjectName("graphs_button_frame")
        self.verticalLayout_85 = QtWidgets.QVBoxLayout(self.graphs_button_frame)
        self.verticalLayout_85.setContentsMargins(2, 2, 0, 2)
        self.verticalLayout_85.setSpacing(0)
        self.verticalLayout_85.setObjectName("verticalLayout_85")
        self.graphs_button = QtWidgets.QPushButton(self.graphs_button_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphs_button.sizePolicy().hasHeightForWidth())
        self.graphs_button.setSizePolicy(sizePolicy)
        self.graphs_button.setMinimumSize(QtCore.QSize(0, 50))
        self.graphs_button.setMaximumSize(QtCore.QSize(16777215, 55))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.graphs_button.setFont(font)
        self.graphs_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.graphs_button.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border-top-left-radius: 25px;\n"
"    border-bottom-left-radius: 25px;\n"
"    border-image: url(:/Side_panel/Image_resources/sidePanel/graphs2.png);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-image: url(:/Side_panel/Image_resources/sidePanel/graphs1.png);\n"
"    border-top-left-radius: 25px;\n"
"    border-bottom-left-radius: 25px;\n"
"    border-bottom-right-radius:0px;\n"
"}\n"
"\n"
"QPushButton:Pressed {\n"
"    background-color: transparent;\n"
"    border-top-left-radius: 25px;\n"
"    border-bottom-left-radius: 25px;\n"
"    border-image: url(:/Side_panel/Image_resources/sidePanel/graphs2.png);\n"
"    border: none;\n"
"}")
        self.graphs_button.setText("")
        self.graphs_button.setDefault(False)
        self.graphs_button.setFlat(False)
        self.graphs_button.setObjectName("graphs_button")
        self.verticalLayout_85.addWidget(self.graphs_button)
        self.verticalLayout_6.addWidget(self.graphs_button_frame)
        self.GPS_button_frame = QtWidgets.QFrame(self.side_panel_2)
        self.GPS_button_frame.setMinimumSize(QtCore.QSize(0, 0))
        self.GPS_button_frame.setMaximumSize(QtCore.QSize(16777215, 55))
        self.GPS_button_frame.setStyleSheet("QFrame {\n"
"    border-top:0px;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QFrame:hover {\n"
"    background: transparent;\n"
"    border-top: 2px solid black;\n"
"    border-top-left-radius: 25px;\n"
"    border-bottom-left-radius: 25px;\n"
"    border-left: 2px solid black;\n"
"    border-bottom: 2px solid black;\n"
"}\n"
"")
        self.GPS_button_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.GPS_button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.GPS_button_frame.setObjectName("GPS_button_frame")
        self.verticalLayout_84 = QtWidgets.QVBoxLayout(self.GPS_button_frame)
        self.verticalLayout_84.setContentsMargins(2, 2, 0, 2)
        self.verticalLayout_84.setSpacing(0)
        self.verticalLayout_84.setObjectName("verticalLayout_84")
        self.GPS_button = QtWidgets.QPushButton(self.GPS_button_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GPS_button.sizePolicy().hasHeightForWidth())
        self.GPS_button.setSizePolicy(sizePolicy)
        self.GPS_button.setMinimumSize(QtCore.QSize(0, 50))
        self.GPS_button.setMaximumSize(QtCore.QSize(16777215, 55))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.GPS_button.setFont(font)
        self.GPS_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.GPS_button.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border-top-left-radius: 25px;\n"
"    border-bottom-left-radius: 25px;\n"
"    border-image: url(:/Side_panel/Image_resources/sidePanel/GPS2.png);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-image: url(:/Side_panel/Image_resources/sidePanel/GPS1.png);\n"
"    border-top-left-radius: 25px;\n"
"    border-bottom-left-radius: 25px;\n"
"    border-bottom-right-radius:0px;\n"
"}\n"
"\n"
"QPushButton:Pressed {\n"
"    background-color: transparent;\n"
"    border-top-left-radius: 25px;\n"
"    border-bottom-left-radius: 25px;\n"
"    border-image: url(:/Side_panel/Image_resources/sidePanel/GPS2.png);\n"
"    border: none;\n"
"}")
        self.GPS_button.setText("")
        self.GPS_button.setDefault(False)
        self.GPS_button.setFlat(False)
        self.GPS_button.setObjectName("GPS_button")
        self.verticalLayout_84.addWidget(self.GPS_button)
        self.verticalLayout_6.addWidget(self.GPS_button_frame)
        self.RKTmodel_button_frame = QtWidgets.QFrame(self.side_panel_2)
        self.RKTmodel_button_frame.setMinimumSize(QtCore.QSize(0, 55))
        self.RKTmodel_button_frame.setMaximumSize(QtCore.QSize(16777215, 55))
        self.RKTmodel_button_frame.setStyleSheet("QFrame {\n"
"    border-top:0px;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QFrame:hover {\n"
"    background: transparent;\n"
"    border-top: 2px solid black;\n"
"    border-top-left-radius: 25px;\n"
"    border-bottom-left-radius: 25px;\n"
"    border-left: 2px solid black;\n"
"    border-bottom: 2px solid black;\n"
"}\n"
"")
        self.RKTmodel_button_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.RKTmodel_button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.RKTmodel_button_frame.setObjectName("RKTmodel_button_frame")
        self.verticalLayout_83 = QtWidgets.QVBoxLayout(self.RKTmodel_button_frame)
        self.verticalLayout_83.setContentsMargins(2, 2, 0, 2)
        self.verticalLayout_83.setSpacing(0)
        self.verticalLayout_83.setObjectName("verticalLayout_83")
        self.rkt_model_button = QtWidgets.QPushButton(self.RKTmodel_button_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rkt_model_button.sizePolicy().hasHeightForWidth())
        self.rkt_model_button.setSizePolicy(sizePolicy)
        self.rkt_model_button.setMinimumSize(QtCore.QSize(0, 50))
        self.rkt_model_button.setMaximumSize(QtCore.QSize(16777215, 55))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.rkt_model_button.setFont(font)
        self.rkt_model_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rkt_model_button.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border-top-left-radius: 25px;\n"
"    border-bottom-left-radius: 25px;\n"
"    border-image: url(:/Side_panel/Image_resources/sidePanel/RKT_MODEL2.png);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-image: url(:/Side_panel/Image_resources/sidePanel/RKT_MODEL1.png);\n"
"    border-top-left-radius: 25px;\n"
"    border-bottom-left-radius: 25px;\n"
"    border-bottom-right-radius:0px;\n"
"}\n"
"\n"
"QPushButton:Pressed {\n"
"    background-color: transparent;\n"
"    border-top-left-radius: 25px;\n"
"    border-bottom-left-radius: 25px;\n"
"    border-image: url(:/Side_panel/Image_resources/sidePanel/RKT_MODEL2.png);\n"
"    border: none;\n"
"}\n"
"")
        self.rkt_model_button.setText("")
        self.rkt_model_button.setDefault(False)
        self.rkt_model_button.setFlat(False)
        self.rkt_model_button.setObjectName("rkt_model_button")
        self.verticalLayout_83.addWidget(self.rkt_model_button)
        self.verticalLayout_6.addWidget(self.RKTmodel_button_frame)
        self.tabledata_button_frame = QtWidgets.QFrame(self.side_panel_2)
        self.tabledata_button_frame.setMinimumSize(QtCore.QSize(0, 0))
        self.tabledata_button_frame.setMaximumSize(QtCore.QSize(16777215, 55))
        self.tabledata_button_frame.setStyleSheet("QFrame {\n"
"    border-top:0px;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QFrame:hover {\n"
"    background: transparent;\n"
"    border-top: 2px solid black;\n"
"    border-top-left-radius: 25px;\n"
"    border-bottom-left-radius: 25px;\n"
"    border-left: 2px solid black;\n"
"    border-bottom: 2px solid black;\n"
"}\n"
"")
        self.tabledata_button_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tabledata_button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tabledata_button_frame.setObjectName("tabledata_button_frame")
        self.verticalLayout_82 = QtWidgets.QVBoxLayout(self.tabledata_button_frame)
        self.verticalLayout_82.setContentsMargins(2, 2, 0, 2)
        self.verticalLayout_82.setSpacing(0)
        self.verticalLayout_82.setObjectName("verticalLayout_82")
        self.tabledata_button = QtWidgets.QPushButton(self.tabledata_button_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabledata_button.sizePolicy().hasHeightForWidth())
        self.tabledata_button.setSizePolicy(sizePolicy)
        self.tabledata_button.setMinimumSize(QtCore.QSize(0, 50))
        self.tabledata_button.setMaximumSize(QtCore.QSize(16777215, 55))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.tabledata_button.setFont(font)
        self.tabledata_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tabledata_button.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border-top-left-radius: 25px;\n"
"    border-bottom-left-radius: 25px;\n"
"    border-image: url(:/Side_panel/Image_resources/sidePanel/table_data2.png);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-image: url(:/Side_panel/Image_resources/sidePanel/table_data1.png);\n"
"    border-top-left-radius: 25px;\n"
"    border-bottom-left-radius: 25px;\n"
"    border-bottom-right-radius:0px;\n"
"}\n"
"\n"
"QPushButton:Pressed {\n"
"    background-color: transparent;\n"
"    border-top-left-radius: 25px;\n"
"    border-bottom-left-radius: 25px;\n"
"    border-image: url(:/Side_panel/Image_resources/sidePanel/table_data2.png);\n"
"    border: none;\n"
"}\n"
"")
        self.tabledata_button.setText("")
        self.tabledata_button.setDefault(False)
        self.tabledata_button.setFlat(False)
        self.tabledata_button.setObjectName("tabledata_button")
        self.verticalLayout_82.addWidget(self.tabledata_button)
        self.verticalLayout_6.addWidget(self.tabledata_button_frame)
        self.settings_button_frame = QtWidgets.QFrame(self.side_panel_2)
        self.settings_button_frame.setMinimumSize(QtCore.QSize(0, 0))
        self.settings_button_frame.setMaximumSize(QtCore.QSize(16777215, 55))
        self.settings_button_frame.setStyleSheet("QFrame {\n"
"    border-top:0px;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QFrame:hover {\n"
"    background: transparent;\n"
"    border-top: 2px solid black;\n"
"    border-top-left-radius: 25px;\n"
"    border-bottom-left-radius: 25px;\n"
"    border-left: 2px solid black;\n"
"    border-bottom: 2px solid black;\n"
"}\n"
"")
        self.settings_button_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.settings_button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.settings_button_frame.setObjectName("settings_button_frame")
        self.verticalLayout_79 = QtWidgets.QVBoxLayout(self.settings_button_frame)
        self.verticalLayout_79.setContentsMargins(2, 2, 0, 2)
        self.verticalLayout_79.setSpacing(0)
        self.verticalLayout_79.setObjectName("verticalLayout_79")
        self.settings_button = QtWidgets.QPushButton(self.settings_button_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settings_button.sizePolicy().hasHeightForWidth())
        self.settings_button.setSizePolicy(sizePolicy)
        self.settings_button.setMinimumSize(QtCore.QSize(0, 50))
        self.settings_button.setMaximumSize(QtCore.QSize(16777215, 55))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.settings_button.setFont(font)
        self.settings_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.settings_button.setStyleSheet("QPushButton {    \n"
"    border-image: url(:/Side_panel/Image_resources/sidePanel/settings1.png);\n"
"    background-color: transparent;\n"
"    border-top-left-radius: 25px;\n"
"    border-bottom-left-radius: 25px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-image: url(:/Side_panel/Image_resources/sidePanel/settings2.png);\n"
"    border-top-left-radius: 25px;\n"
"    border-bottom-left-radius: 25px;\n"
"    border-bottom-right-radius:0px;\n"
"}\n"
"\n"
"QPushButton:Pressed {    \n"
"    border-image: url(:/Side_panel/Image_resources/sidePanel/settings1.png);\n"
"    background-color: transparent;\n"
"    border-top-left-radius: 25px;\n"
"    border-bottom-left-radius: 25px;\n"
"    border: none;\n"
"}")
        self.settings_button.setText("")
        self.settings_button.setDefault(False)
        self.settings_button.setFlat(False)
        self.settings_button.setObjectName("settings_button")
        self.verticalLayout_79.addWidget(self.settings_button)
        self.verticalLayout_6.addWidget(self.settings_button_frame)
        self.verticalLayout_5.addWidget(self.side_panel_2)
        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 1)
        self.horizontalLayout.addWidget(self.side_panel)
        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setStyleSheet("background:transparent;")
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.main_frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_11 = QtWidgets.QFrame(self.main_frame)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(130)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frame_21 = QtWidgets.QFrame(self.frame_11)
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_21)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.team_logo = QtWidgets.QLabel(self.frame_21)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.team_logo.setFont(font)
        self.team_logo.setStyleSheet("color:white;")
        self.team_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.team_logo.setObjectName("team_logo")
        self.horizontalLayout_8.addWidget(self.team_logo)
        self.horizontalLayout_10.addWidget(self.frame_21)
        self.frame_22 = QtWidgets.QFrame(self.frame_11)
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_22)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.team_logo_3 = QtWidgets.QLabel(self.frame_22)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.team_logo_3.setFont(font)
        self.team_logo_3.setStyleSheet("color:white;")
        self.team_logo_3.setAlignment(QtCore.Qt.AlignCenter)
        self.team_logo_3.setObjectName("team_logo_3")
        self.horizontalLayout_9.addWidget(self.team_logo_3, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout_10.addWidget(self.frame_22)
        self.horizontalLayout_10.setStretch(0, 1)
        self.verticalLayout.addWidget(self.frame_11)
        self.button_frame = QtWidgets.QFrame(self.main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_frame.sizePolicy().hasHeightForWidth())
        self.button_frame.setSizePolicy(sizePolicy)
        self.button_frame.setMinimumSize(QtCore.QSize(0, 63))
        self.button_frame.setMaximumSize(QtCore.QSize(16777215, 63))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(72)
        self.button_frame.setFont(font)
        self.button_frame.setStyleSheet("background:#60A7E4;\n"
"border-radius: 15px;\n"
"")
        self.button_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.button_frame.setObjectName("button_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.button_frame)
        self.horizontalLayout_2.setContentsMargins(100, 0, 100, 0)
        self.horizontalLayout_2.setSpacing(28)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.host_connect_button = QtWidgets.QPushButton(self.button_frame)
        self.host_connect_button.setMinimumSize(QtCore.QSize(215, 52))
        self.host_connect_button.setMaximumSize(QtCore.QSize(230, 52))
        self.host_connect_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.host_connect_button.setStyleSheet("QPushButton {\n"
"    color:white;\n"
"    border-image: url(:/Top_panel/Image_resources/topPanel/host_connect2.png);\n"
"    background:#242A33;\n"
"    border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    border-image: url(:/Top_panel/Image_resources/topPanel/host_connect1.png);\n"
"    background: white;\n"
"    border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-image: url(:/Top_panel/Image_resources/topPanel/host_connect2.png);\n"
"    background: white;\n"
"    border-radius: 25px;\n"
"}")
        self.host_connect_button.setText("")
        self.host_connect_button.setObjectName("host_connect_button")
        self.horizontalLayout_2.addWidget(self.host_connect_button)
        self.flight_file_upload_button = QtWidgets.QPushButton(self.button_frame)
        self.flight_file_upload_button.setMinimumSize(QtCore.QSize(215, 52))
        self.flight_file_upload_button.setMaximumSize(QtCore.QSize(230, 52))
        self.flight_file_upload_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.flight_file_upload_button.setStyleSheet("QPushButton {\n"
"    color:white;\n"
"    border-image: url(:/Top_panel/Image_resources/topPanel/flight_file_upload2.png);\n"
"    background:#242A33;\n"
"    border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    border-image: url(:/Top_panel/Image_resources/topPanel/flight_file_upload1.png);\n"
"    background: white;\n"
"    border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-image: url(:/Top_panel/Image_resources/topPanel/flight_file_upload2.png);\n"
"    background: white;\n"
"    border-radius: 25px;\n"
"}")
        self.flight_file_upload_button.setText("")
        self.flight_file_upload_button.setObjectName("flight_file_upload_button")
        self.horizontalLayout_2.addWidget(self.flight_file_upload_button)
        self.data_upload_button = QtWidgets.QPushButton(self.button_frame)
        self.data_upload_button.setMinimumSize(QtCore.QSize(215, 52))
        self.data_upload_button.setMaximumSize(QtCore.QSize(230, 52))
        self.data_upload_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.data_upload_button.setStyleSheet("QPushButton {\n"
"    border-image: url(:/Top_panel/Image_resources/topPanel/data_upload2.png);\n"
"    background:#242A33;\n"
"    border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-image: url(:/Top_panel/Image_resources/topPanel/data_upload1.png);\n"
"    background: white;\n"
"    border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-image: url(:/Top_panel/Image_resources/topPanel/data_upload2.png);\n"
"    background: white;\n"
"    border-radius: 25px;\n"
"}")
        self.data_upload_button.setText("")
        self.data_upload_button.setObjectName("data_upload_button")
        self.horizontalLayout_2.addWidget(self.data_upload_button)
        self.flight_data_export_button = QtWidgets.QPushButton(self.button_frame)
        self.flight_data_export_button.setMinimumSize(QtCore.QSize(215, 52))
        self.flight_data_export_button.setMaximumSize(QtCore.QSize(230, 52))
        self.flight_data_export_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.flight_data_export_button.setStyleSheet("QPushButton {\n"
"    \n"
"    border-image: url(:/Top_panel/Image_resources/topPanel/flight_data_export2.png);\n"
"    background:#242A33;\n"
"    border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    border-image: url(:/Top_panel/Image_resources/topPanel/flight_data_export1.png);\n"
"    background: white;\n"
"    border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-image: url(:/Top_panel/Image_resources/topPanel/flight_data_export2.png);\n"
"    background: white;\n"
"    border-radius: 25px;\n"
"}")
        self.flight_data_export_button.setText("")
        self.flight_data_export_button.setObjectName("flight_data_export_button")
        self.horizontalLayout_2.addWidget(self.flight_data_export_button)
        self.host_disconnect_button = QtWidgets.QPushButton(self.button_frame)
        self.host_disconnect_button.setMinimumSize(QtCore.QSize(215, 52))
        self.host_disconnect_button.setMaximumSize(QtCore.QSize(230, 52))
        self.host_disconnect_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.host_disconnect_button.setStyleSheet("QPushButton {\n"
"    border-image: url(:/Top_panel/Image_resources/topPanel/host_disconnect2.png);\n"
"    background:#242A33;\n"
"    border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-image: url(:/Top_panel/Image_resources/topPanel/host_disconnect1.png);\n"
"    background: white;\n"
"    border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-image: url(:/Top_panel/Image_resources/topPanel/host_disconnect2.png);\n"
"    background: white;\n"
"    border-radius: 25px;\n"
"}")
        self.host_disconnect_button.setText("")
        self.host_disconnect_button.setObjectName("host_disconnect_button")
        self.horizontalLayout_2.addWidget(self.host_disconnect_button)
        self.pushButton = QtWidgets.QPushButton(self.button_frame)
        self.pushButton.setMinimumSize(QtCore.QSize(52, 52))
        self.pushButton.setMaximumSize(QtCore.QSize(52, 52))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background:red;\n"
"    border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: red;\n"
"    background: white;\n"
"    border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    background: white;\n"
"    border-radius: 25px;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.button_frame)
        self.data_view_frame = QtWidgets.QFrame(self.main_frame)
        self.data_view_frame.setMinimumSize(QtCore.QSize(0, 0))
        self.data_view_frame.setStyleSheet("background:transparent;")
        self.data_view_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.data_view_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.data_view_frame.setObjectName("data_view_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.data_view_frame)
        self.horizontalLayout_3.setContentsMargins(8, 8, 8, 0)
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.data_view_frame)
        self.stackedWidget.setStyleSheet("background:transparent;")
        self.stackedWidget.setObjectName("stackedWidget")
        self.home_page = QtWidgets.QWidget()
        self.home_page.setObjectName("home_page")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.home_page)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 20)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.data_view_frame_2 = QtWidgets.QFrame(self.home_page)
        self.data_view_frame_2.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.data_view_frame_2.setFont(font)
        self.data_view_frame_2.setStyleSheet("background:#141414;")
        self.data_view_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.data_view_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.data_view_frame_2.setObjectName("data_view_frame_2")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.data_view_frame_2)
        self.horizontalLayout_11.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout_11.setSpacing(20)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.data_view_frame1 = QtWidgets.QFrame(self.data_view_frame_2)
        self.data_view_frame1.setMaximumSize(QtCore.QSize(763, 16777215))
        self.data_view_frame1.setStyleSheet("background:transparent;")
        self.data_view_frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.data_view_frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.data_view_frame1.setObjectName("data_view_frame1")
        self.gridLayout = QtWidgets.QGridLayout(self.data_view_frame1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.alt_graph_frame = QtWidgets.QFrame(self.data_view_frame1)
        self.alt_graph_frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.alt_graph_frame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.alt_graph_frame.setMouseTracking(False)
        self.alt_graph_frame.setStyleSheet("background:#60A7E4;\n"
"border-radius: 15px;")
        self.alt_graph_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.alt_graph_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.alt_graph_frame.setObjectName("alt_graph_frame")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.alt_graph_frame)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.hp_alt_label = QtWidgets.QLabel(self.alt_graph_frame)
        self.hp_alt_label.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.hp_alt_label.setFont(font)
        self.hp_alt_label.setStyleSheet("background:transparent;\n"
"border-top-left-radius:15px;\n"
"border-top-right-radius:0px;")
        self.hp_alt_label.setAlignment(QtCore.Qt.AlignCenter)
        self.hp_alt_label.setObjectName("hp_alt_label")
        self.verticalLayout_12.addWidget(self.hp_alt_label)
        self.alt_graph = QtWidgets.QFrame(self.alt_graph_frame)
        self.alt_graph.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.alt_graph.setStyleSheet("background:white;\n"
"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;")
        self.alt_graph.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.alt_graph.setFrameShadow(QtWidgets.QFrame.Raised)
        self.alt_graph.setObjectName("alt_graph")
        self.verticalLayout_31 = QtWidgets.QVBoxLayout(self.alt_graph)
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 15)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.alt_graph_temp = QtWidgets.QFrame(self.alt_graph)
        self.alt_graph_temp.setStyleSheet("background:transparent;")
        self.alt_graph_temp.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.alt_graph_temp.setFrameShadow(QtWidgets.QFrame.Raised)
        self.alt_graph_temp.setObjectName("alt_graph_temp")
        self.verticalLayout_31.addWidget(self.alt_graph_temp)
        self.verticalLayout_12.addWidget(self.alt_graph)
        self.verticalLayout_12.setStretch(1, 15)
        self.gridLayout.addWidget(self.alt_graph_frame, 0, 0, 1, 1)
        self.speed_graph_frame = QtWidgets.QFrame(self.data_view_frame1)
        self.speed_graph_frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.speed_graph_frame.setStyleSheet("background:#60A7E4;\n"
"border-radius: 15px;")
        self.speed_graph_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.speed_graph_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.speed_graph_frame.setObjectName("speed_graph_frame")
        self.verticalLayout_80 = QtWidgets.QVBoxLayout(self.speed_graph_frame)
        self.verticalLayout_80.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_80.setSpacing(0)
        self.verticalLayout_80.setObjectName("verticalLayout_80")
        self.speed_label = QtWidgets.QFrame(self.speed_graph_frame)
        self.speed_label.setMinimumSize(QtCore.QSize(0, 0))
        self.speed_label.setStyleSheet("background:#60A7E4;\n"
"border-bottom-left-radius: 0px solid;\n"
"border-bottom-right-radius: 0px solid;")
        self.speed_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.speed_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.speed_label.setObjectName("speed_label")
        self.horizontalLayout_51 = QtWidgets.QHBoxLayout(self.speed_label)
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_51.setObjectName("horizontalLayout_51")
        self.hp_gpsSpeed_label = QtWidgets.QLabel(self.speed_label)
        self.hp_gpsSpeed_label.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.hp_gpsSpeed_label.setFont(font)
        self.hp_gpsSpeed_label.setStyleSheet("background:transparent;\n"
"border-top-left-radius:15px;\n"
"border-top-right-radius:0px;")
        self.hp_gpsSpeed_label.setAlignment(QtCore.Qt.AlignCenter)
        self.hp_gpsSpeed_label.setObjectName("hp_gpsSpeed_label")
        self.horizontalLayout_51.addWidget(self.hp_gpsSpeed_label)
        self.verticalLayout_80.addWidget(self.speed_label)
        self.speed_graph = QtWidgets.QFrame(self.speed_graph_frame)
        self.speed_graph.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.speed_graph.setStyleSheet("background:white;\n"
"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;")
        self.speed_graph.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.speed_graph.setFrameShadow(QtWidgets.QFrame.Raised)
        self.speed_graph.setObjectName("speed_graph")
        self.verticalLayout_81 = QtWidgets.QVBoxLayout(self.speed_graph)
        self.verticalLayout_81.setContentsMargins(0, 0, 0, 15)
        self.verticalLayout_81.setSpacing(0)
        self.verticalLayout_81.setObjectName("verticalLayout_81")
        self.speed_graph_temp = QtWidgets.QFrame(self.speed_graph)
        self.speed_graph_temp.setStyleSheet("background:transparent;")
        self.speed_graph_temp.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.speed_graph_temp.setFrameShadow(QtWidgets.QFrame.Raised)
        self.speed_graph_temp.setObjectName("speed_graph_temp")
        self.verticalLayout_81.addWidget(self.speed_graph_temp)
        self.verticalLayout_80.addWidget(self.speed_graph)
        self.verticalLayout_80.setStretch(1, 5)
        self.gridLayout.addWidget(self.speed_graph_frame, 0, 1, 1, 1)
        self.pressure_graph_frame = QtWidgets.QFrame(self.data_view_frame1)
        self.pressure_graph_frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pressure_graph_frame.setStyleSheet("background:#60A7E4;\n"
"border-radius: 15px;")
        self.pressure_graph_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pressure_graph_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pressure_graph_frame.setObjectName("pressure_graph_frame")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.pressure_graph_frame)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.pressure_label = QtWidgets.QFrame(self.pressure_graph_frame)
        self.pressure_label.setMinimumSize(QtCore.QSize(0, 0))
        self.pressure_label.setStyleSheet("background:#60A7E4;\n"
"border-bottom-left-radius: 0px solid;\n"
"border-bottom-right-radius: 0px solid;")
        self.pressure_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pressure_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pressure_label.setObjectName("pressure_label")
        self.horizontalLayout_44 = QtWidgets.QHBoxLayout(self.pressure_label)
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_44.setObjectName("horizontalLayout_44")
        self.hp_pressure_label = QtWidgets.QLabel(self.pressure_label)
        self.hp_pressure_label.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.hp_pressure_label.setFont(font)
        self.hp_pressure_label.setStyleSheet("background:transparent;\n"
"border-top-left-radius:15px;\n"
"border-top-right-radius:0px;")
        self.hp_pressure_label.setAlignment(QtCore.Qt.AlignCenter)
        self.hp_pressure_label.setObjectName("hp_pressure_label")
        self.horizontalLayout_44.addWidget(self.hp_pressure_label)
        self.verticalLayout_13.addWidget(self.pressure_label)
        self.pressure_graph = QtWidgets.QFrame(self.pressure_graph_frame)
        self.pressure_graph.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pressure_graph.setStyleSheet("background:white;\n"
"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;")
        self.pressure_graph.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pressure_graph.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pressure_graph.setObjectName("pressure_graph")
        self.verticalLayout_33 = QtWidgets.QVBoxLayout(self.pressure_graph)
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 15)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.pressure_graph_temp = QtWidgets.QFrame(self.pressure_graph)
        self.pressure_graph_temp.setStyleSheet("background:transparent;")
        self.pressure_graph_temp.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pressure_graph_temp.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pressure_graph_temp.setObjectName("pressure_graph_temp")
        self.verticalLayout_33.addWidget(self.pressure_graph_temp)
        self.verticalLayout_13.addWidget(self.pressure_graph)
        self.verticalLayout_13.setStretch(1, 5)
        self.gridLayout.addWidget(self.pressure_graph_frame, 1, 0, 1, 1)
        self.voltage_graph_frame = QtWidgets.QFrame(self.data_view_frame1)
        self.voltage_graph_frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.voltage_graph_frame.setStyleSheet("background:#60A7E4;\n"
"border-radius: 15px;")
        self.voltage_graph_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.voltage_graph_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.voltage_graph_frame.setObjectName("voltage_graph_frame")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.voltage_graph_frame)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.voltage_label = QtWidgets.QFrame(self.voltage_graph_frame)
        self.voltage_label.setMinimumSize(QtCore.QSize(0, 0))
        self.voltage_label.setStyleSheet("background:#60A7E4;\n"
"border-bottom-left-radius: 0px solid;\n"
"border-bottom-right-radius: 0px solid;")
        self.voltage_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.voltage_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.voltage_label.setObjectName("voltage_label")
        self.horizontalLayout_45 = QtWidgets.QHBoxLayout(self.voltage_label)
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_45.setObjectName("horizontalLayout_45")
        self.hp_voltage_label = QtWidgets.QLabel(self.voltage_label)
        self.hp_voltage_label.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.hp_voltage_label.setFont(font)
        self.hp_voltage_label.setStyleSheet("background:transparent;\n"
"border-top-left-radius:15px;\n"
"border-top-right-radius:0px;")
        self.hp_voltage_label.setAlignment(QtCore.Qt.AlignCenter)
        self.hp_voltage_label.setObjectName("hp_voltage_label")
        self.horizontalLayout_45.addWidget(self.hp_voltage_label)
        self.verticalLayout_14.addWidget(self.voltage_label)
        self.voltage_graph = QtWidgets.QFrame(self.voltage_graph_frame)
        self.voltage_graph.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.voltage_graph.setStyleSheet("background:white;\n"
"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;")
        self.voltage_graph.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.voltage_graph.setFrameShadow(QtWidgets.QFrame.Raised)
        self.voltage_graph.setObjectName("voltage_graph")
        self.verticalLayout_34 = QtWidgets.QVBoxLayout(self.voltage_graph)
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 15)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.voltage_graph_temp = QtWidgets.QFrame(self.voltage_graph)
        self.voltage_graph_temp.setStyleSheet("background:transparent;")
        self.voltage_graph_temp.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.voltage_graph_temp.setFrameShadow(QtWidgets.QFrame.Raised)
        self.voltage_graph_temp.setObjectName("voltage_graph_temp")
        self.verticalLayout_34.addWidget(self.voltage_graph_temp)
        self.verticalLayout_14.addWidget(self.voltage_graph)
        self.verticalLayout_14.setStretch(1, 5)
        self.gridLayout.addWidget(self.voltage_graph_frame, 1, 1, 1, 1)
        self.horizontalLayout_11.addWidget(self.data_view_frame1)
        self.data_view_frame2 = QtWidgets.QFrame(self.data_view_frame_2)
        self.data_view_frame2.setMinimumSize(QtCore.QSize(662, 0))
        self.data_view_frame2.setStyleSheet("background:transparent;")
        self.data_view_frame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.data_view_frame2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.data_view_frame2.setObjectName("data_view_frame2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.data_view_frame2)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(20)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.data_1 = QtWidgets.QFrame(self.data_view_frame2)
        self.data_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.data_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.data_1.setObjectName("data_1")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.data_1)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(20)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.frame_13 = QtWidgets.QFrame(self.data_1)
        self.frame_13.setMinimumSize(QtCore.QSize(150, 0))
        self.frame_13.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_13.setStyleSheet("background:white;\n"
"border-radius: 15px;")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_37 = QtWidgets.QLabel(self.frame_13)
        self.label_37.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_37.setFont(font)
        self.label_37.setStyleSheet("background:transparent;\n"
"background:#60A7E4;\n"
"border-top-left-radius: 15px;\n"
"border-top-right-radius: 15px;\n"
"border-bottom-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;")
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.verticalLayout_17.addWidget(self.label_37)
        self.frame_55 = QtWidgets.QFrame(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_55.sizePolicy().hasHeightForWidth())
        self.frame_55.setSizePolicy(sizePolicy)
        self.frame_55.setStyleSheet("border-top:1.5px solid black;\n"
"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;")
        self.frame_55.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_55.setObjectName("frame_55")
        self.horizontalLayout_47 = QtWidgets.QHBoxLayout(self.frame_55)
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_47.setSpacing(0)
        self.horizontalLayout_47.setObjectName("horizontalLayout_47")
        self.frame_93 = QtWidgets.QFrame(self.frame_55)
        self.frame_93.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_93.setStyleSheet("background:transparent;\n"
"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;\n"
"border-top:0px solid black;")
        self.frame_93.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_93.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_93.setObjectName("frame_93")
        self.verticalLayout_65 = QtWidgets.QVBoxLayout(self.frame_93)
        self.verticalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_65.setSpacing(9)
        self.verticalLayout_65.setObjectName("verticalLayout_65")
        self.label_45 = QtWidgets.QLabel(self.frame_93)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_45.setFont(font)
        self.label_45.setStyleSheet("")
        self.label_45.setAlignment(QtCore.Qt.AlignCenter)
        self.label_45.setObjectName("label_45")
        self.verticalLayout_65.addWidget(self.label_45)
        self.label_47 = QtWidgets.QLabel(self.frame_93)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_47.setFont(font)
        self.label_47.setAlignment(QtCore.Qt.AlignCenter)
        self.label_47.setObjectName("label_47")
        self.verticalLayout_65.addWidget(self.label_47)
        self.label_46 = QtWidgets.QLabel(self.frame_93)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_46.setFont(font)
        self.label_46.setAlignment(QtCore.Qt.AlignCenter)
        self.label_46.setObjectName("label_46")
        self.verticalLayout_65.addWidget(self.label_46)
        self.horizontalLayout_47.addWidget(self.frame_93)
        self.frame_94 = QtWidgets.QFrame(self.frame_55)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_94.sizePolicy().hasHeightForWidth())
        self.frame_94.setSizePolicy(sizePolicy)
        self.frame_94.setMinimumSize(QtCore.QSize(120, 0))
        self.frame_94.setStyleSheet("background:transparent;\n"
"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;\n"
"border-bottom-left-radius:0px;\n"
"border-top:0px solid black;")
        self.frame_94.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_94.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_94.setObjectName("frame_94")
        self.verticalLayout_66 = QtWidgets.QVBoxLayout(self.frame_94)
        self.verticalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_66.setObjectName("verticalLayout_66")
        self.frame_92 = QtWidgets.QFrame(self.frame_94)
        self.frame_92.setMaximumSize(QtCore.QSize(120, 16777215))
        self.frame_92.setStyleSheet("background:transparent;\n"
"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;\n"
"border-left:1.5px solid black;")
        self.frame_92.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_92.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_92.setObjectName("frame_92")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_92)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setHorizontalSpacing(0)
        self.gridLayout_7.setVerticalSpacing(9)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.accelerometer_value_y = QtWidgets.QTextEdit(self.frame_92)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.accelerometer_value_y.sizePolicy().hasHeightForWidth())
        self.accelerometer_value_y.setSizePolicy(sizePolicy)
        self.accelerometer_value_y.setMinimumSize(QtCore.QSize(118, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.accelerometer_value_y.setFont(font)
        self.accelerometer_value_y.setStyleSheet("border-left:0px;\n"
"background:transparent;")
        self.accelerometer_value_y.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.accelerometer_value_y.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.accelerometer_value_y.setReadOnly(True)
        self.accelerometer_value_y.setPlaceholderText("")
        self.accelerometer_value_y.setObjectName("accelerometer_value_y")
        self.gridLayout_7.addWidget(self.accelerometer_value_y, 1, 0, 1, 1)
        self.accelerometer_value_z = QtWidgets.QTextEdit(self.frame_92)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.accelerometer_value_z.sizePolicy().hasHeightForWidth())
        self.accelerometer_value_z.setSizePolicy(sizePolicy)
        self.accelerometer_value_z.setMinimumSize(QtCore.QSize(118, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.accelerometer_value_z.setFont(font)
        self.accelerometer_value_z.setStyleSheet("background:transparent;\n"
"border-bottom-right-radius: 15px;\n"
"border-left:0px;\n"
"")
        self.accelerometer_value_z.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.accelerometer_value_z.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.accelerometer_value_z.setReadOnly(True)
        self.accelerometer_value_z.setObjectName("accelerometer_value_z")
        self.gridLayout_7.addWidget(self.accelerometer_value_z, 2, 0, 1, 1)
        self.accelerometer_value_x = QtWidgets.QTextEdit(self.frame_92)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.accelerometer_value_x.sizePolicy().hasHeightForWidth())
        self.accelerometer_value_x.setSizePolicy(sizePolicy)
        self.accelerometer_value_x.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.accelerometer_value_x.setFont(font)
        self.accelerometer_value_x.setStyleSheet("background:transparent;\n"
"border-top:0px solid black;\n"
"border-left:0px;")
        self.accelerometer_value_x.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.accelerometer_value_x.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.accelerometer_value_x.setReadOnly(True)
        self.accelerometer_value_x.setPlaceholderText("")
        self.accelerometer_value_x.setObjectName("accelerometer_value_x")
        self.gridLayout_7.addWidget(self.accelerometer_value_x, 0, 0, 1, 2)
        self.verticalLayout_66.addWidget(self.frame_92)
        self.horizontalLayout_47.addWidget(self.frame_94)
        self.verticalLayout_17.addWidget(self.frame_55)
        self.verticalLayout_17.setStretch(1, 1)
        self.horizontalLayout_12.addWidget(self.frame_13)
        self.frame_15 = QtWidgets.QFrame(self.data_1)
        self.frame_15.setMinimumSize(QtCore.QSize(150, 0))
        self.frame_15.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_15.setStyleSheet("background:white;\n"
"border-radius: 15px;")
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_58 = QtWidgets.QVBoxLayout(self.frame_15)
        self.verticalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_58.setSpacing(0)
        self.verticalLayout_58.setObjectName("verticalLayout_58")
        self.label_38 = QtWidgets.QLabel(self.frame_15)
        self.label_38.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_38.setFont(font)
        self.label_38.setStyleSheet("background:transparent;\n"
"background:#60A7E4;\n"
"border-top-left-radius: 15px;\n"
"border-top-right-radius: 15px;\n"
"border-bottom-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;")
        self.label_38.setAlignment(QtCore.Qt.AlignCenter)
        self.label_38.setObjectName("label_38")
        self.verticalLayout_58.addWidget(self.label_38)
        self.frame_57 = QtWidgets.QFrame(self.frame_15)
        self.frame_57.setStyleSheet("border-top:1.5px solid black;\n"
"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;")
        self.frame_57.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_57.setObjectName("frame_57")
        self.horizontalLayout_48 = QtWidgets.QHBoxLayout(self.frame_57)
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_48.setSpacing(0)
        self.horizontalLayout_48.setObjectName("horizontalLayout_48")
        self.frame_95 = QtWidgets.QFrame(self.frame_57)
        self.frame_95.setStyleSheet("background:transparent;\n"
"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;\n"
"border-top:0px;")
        self.frame_95.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_95.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_95.setObjectName("frame_95")
        self.verticalLayout_70 = QtWidgets.QVBoxLayout(self.frame_95)
        self.verticalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_70.setObjectName("verticalLayout_70")
        self.label_54 = QtWidgets.QLabel(self.frame_95)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_54.setFont(font)
        self.label_54.setStyleSheet("")
        self.label_54.setAlignment(QtCore.Qt.AlignCenter)
        self.label_54.setObjectName("label_54")
        self.verticalLayout_70.addWidget(self.label_54)
        self.label_55 = QtWidgets.QLabel(self.frame_95)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_55.setFont(font)
        self.label_55.setAlignment(QtCore.Qt.AlignCenter)
        self.label_55.setObjectName("label_55")
        self.verticalLayout_70.addWidget(self.label_55)
        self.label_56 = QtWidgets.QLabel(self.frame_95)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_56.setFont(font)
        self.label_56.setAlignment(QtCore.Qt.AlignCenter)
        self.label_56.setObjectName("label_56")
        self.verticalLayout_70.addWidget(self.label_56)
        self.horizontalLayout_48.addWidget(self.frame_95)
        self.frame_96 = QtWidgets.QFrame(self.frame_57)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_96.sizePolicy().hasHeightForWidth())
        self.frame_96.setSizePolicy(sizePolicy)
        self.frame_96.setMinimumSize(QtCore.QSize(120, 0))
        self.frame_96.setMaximumSize(QtCore.QSize(120, 16777215))
        self.frame_96.setStyleSheet("background:transparent;\n"
"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;\n"
"border-bottom-left-radius:0px;\n"
"border-left:1.5px solid black;\n"
"border-top:0px;")
        self.frame_96.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_96.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_96.setObjectName("frame_96")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_96)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setHorizontalSpacing(0)
        self.gridLayout_9.setVerticalSpacing(7)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gyrometer_value_z = QtWidgets.QTextEdit(self.frame_96)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gyrometer_value_z.sizePolicy().hasHeightForWidth())
        self.gyrometer_value_z.setSizePolicy(sizePolicy)
        self.gyrometer_value_z.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gyrometer_value_z.setFont(font)
        self.gyrometer_value_z.setStyleSheet("background:transparent;\n"
"border-bottom-right-radius: 15px;\n"
"border-left:0px;\n"
"")
        self.gyrometer_value_z.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.gyrometer_value_z.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.gyrometer_value_z.setReadOnly(True)
        self.gyrometer_value_z.setObjectName("gyrometer_value_z")
        self.gridLayout_9.addWidget(self.gyrometer_value_z, 2, 0, 1, 1)
        self.gyrometer_value_x = QtWidgets.QTextEdit(self.frame_96)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gyrometer_value_x.sizePolicy().hasHeightForWidth())
        self.gyrometer_value_x.setSizePolicy(sizePolicy)
        self.gyrometer_value_x.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gyrometer_value_x.setFont(font)
        self.gyrometer_value_x.setStyleSheet("background:transparent;\n"
"border-top:0px solid black;\n"
"border-left:0px;")
        self.gyrometer_value_x.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.gyrometer_value_x.setReadOnly(True)
        self.gyrometer_value_x.setObjectName("gyrometer_value_x")
        self.gridLayout_9.addWidget(self.gyrometer_value_x, 0, 0, 1, 2)
        self.gyrometer_value_y = QtWidgets.QTextEdit(self.frame_96)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gyrometer_value_y.sizePolicy().hasHeightForWidth())
        self.gyrometer_value_y.setSizePolicy(sizePolicy)
        self.gyrometer_value_y.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gyrometer_value_y.setFont(font)
        self.gyrometer_value_y.setStyleSheet("background:transparent;\n"
"border-left:0px;")
        self.gyrometer_value_y.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.gyrometer_value_y.setReadOnly(True)
        self.gyrometer_value_y.setObjectName("gyrometer_value_y")
        self.gridLayout_9.addWidget(self.gyrometer_value_y, 1, 0, 1, 2)
        self.horizontalLayout_48.addWidget(self.frame_96)
        self.verticalLayout_58.addWidget(self.frame_57)
        self.verticalLayout_58.setStretch(1, 1)
        self.horizontalLayout_12.addWidget(self.frame_15)
        self.frame_16 = QtWidgets.QFrame(self.data_1)
        self.frame_16.setMinimumSize(QtCore.QSize(150, 0))
        self.frame_16.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_16.setStyleSheet("background:white;\n"
"border-radius: 15px;")
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.verticalLayout_59 = QtWidgets.QVBoxLayout(self.frame_16)
        self.verticalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_59.setSpacing(0)
        self.verticalLayout_59.setObjectName("verticalLayout_59")
        self.label_39 = QtWidgets.QLabel(self.frame_16)
        self.label_39.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_39.setFont(font)
        self.label_39.setStyleSheet("background:transparent;\n"
"background:#60A7E4;\n"
"border-top-left-radius: 15px;\n"
"border-top-right-radius: 15px;\n"
"border-bottom-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;")
        self.label_39.setAlignment(QtCore.Qt.AlignCenter)
        self.label_39.setObjectName("label_39")
        self.verticalLayout_59.addWidget(self.label_39)
        self.frame_62 = QtWidgets.QFrame(self.frame_16)
        self.frame_62.setStyleSheet("border-top:1.5px solid black;\n"
"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;")
        self.frame_62.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_62.setObjectName("frame_62")
        self.horizontalLayout_49 = QtWidgets.QHBoxLayout(self.frame_62)
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_49.setSpacing(0)
        self.horizontalLayout_49.setObjectName("horizontalLayout_49")
        self.frame_103 = QtWidgets.QFrame(self.frame_62)
        self.frame_103.setStyleSheet("background:transparent;\n"
"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;\n"
"border-top:0px;")
        self.frame_103.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_103.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_103.setObjectName("frame_103")
        self.verticalLayout_72 = QtWidgets.QVBoxLayout(self.frame_103)
        self.verticalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_72.setObjectName("verticalLayout_72")
        self.label_57 = QtWidgets.QLabel(self.frame_103)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_57.setFont(font)
        self.label_57.setStyleSheet("")
        self.label_57.setAlignment(QtCore.Qt.AlignCenter)
        self.label_57.setObjectName("label_57")
        self.verticalLayout_72.addWidget(self.label_57)
        self.label_58 = QtWidgets.QLabel(self.frame_103)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_58.setFont(font)
        self.label_58.setAlignment(QtCore.Qt.AlignCenter)
        self.label_58.setObjectName("label_58")
        self.verticalLayout_72.addWidget(self.label_58)
        self.label_59 = QtWidgets.QLabel(self.frame_103)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_59.setFont(font)
        self.label_59.setAlignment(QtCore.Qt.AlignCenter)
        self.label_59.setObjectName("label_59")
        self.verticalLayout_72.addWidget(self.label_59)
        self.horizontalLayout_49.addWidget(self.frame_103)
        self.frame_104 = QtWidgets.QFrame(self.frame_62)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_104.sizePolicy().hasHeightForWidth())
        self.frame_104.setSizePolicy(sizePolicy)
        self.frame_104.setMinimumSize(QtCore.QSize(105, 0))
        self.frame_104.setMaximumSize(QtCore.QSize(120, 16777215))
        self.frame_104.setStyleSheet("background:transparent;\n"
"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;\n"
"border-bottom-left-radius:0px;\n"
"border-left:1.5px solid black;\n"
"border-top:0px;")
        self.frame_104.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_104.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_104.setObjectName("frame_104")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_104)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setHorizontalSpacing(0)
        self.gridLayout_10.setVerticalSpacing(7)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.pitch = QtWidgets.QTextEdit(self.frame_104)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pitch.sizePolicy().hasHeightForWidth())
        self.pitch.setSizePolicy(sizePolicy)
        self.pitch.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pitch.setFont(font)
        self.pitch.setStyleSheet("background:transparent;\n"
"border-top:0px solid black;\n"
"border-left:0px;")
        self.pitch.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pitch.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pitch.setReadOnly(True)
        self.pitch.setObjectName("pitch")
        self.gridLayout_10.addWidget(self.pitch, 0, 0, 1, 1)
        self.yaw = QtWidgets.QTextEdit(self.frame_104)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yaw.sizePolicy().hasHeightForWidth())
        self.yaw.setSizePolicy(sizePolicy)
        self.yaw.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.yaw.setFont(font)
        self.yaw.setStyleSheet("border-left:0px;\n"
"background:transparent;")
        self.yaw.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.yaw.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.yaw.setReadOnly(True)
        self.yaw.setObjectName("yaw")
        self.gridLayout_10.addWidget(self.yaw, 1, 0, 1, 1)
        self.roll = QtWidgets.QTextEdit(self.frame_104)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.roll.sizePolicy().hasHeightForWidth())
        self.roll.setSizePolicy(sizePolicy)
        self.roll.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.roll.setFont(font)
        self.roll.setStyleSheet("border-left:0px;\n"
"background:transparent;")
        self.roll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.roll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.roll.setReadOnly(True)
        self.roll.setObjectName("roll")
        self.gridLayout_10.addWidget(self.roll, 2, 0, 1, 1)
        self.horizontalLayout_49.addWidget(self.frame_104)
        self.verticalLayout_59.addWidget(self.frame_62)
        self.verticalLayout_59.setStretch(1, 1)
        self.horizontalLayout_12.addWidget(self.frame_16)
        self.frame_17 = QtWidgets.QFrame(self.data_1)
        self.frame_17.setMinimumSize(QtCore.QSize(150, 0))
        self.frame_17.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_17.setStyleSheet("background:white;\n"
"border-radius: 15px;")
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.verticalLayout_60 = QtWidgets.QVBoxLayout(self.frame_17)
        self.verticalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_60.setSpacing(0)
        self.verticalLayout_60.setObjectName("verticalLayout_60")
        self.label_40 = QtWidgets.QLabel(self.frame_17)
        self.label_40.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_40.setFont(font)
        self.label_40.setStyleSheet("background:transparent;\n"
"background:#60A7E4;\n"
"border-top-left-radius: 15px;\n"
"border-top-right-radius: 15px;\n"
"border-bottom-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;")
        self.label_40.setAlignment(QtCore.Qt.AlignCenter)
        self.label_40.setObjectName("label_40")
        self.verticalLayout_60.addWidget(self.label_40)
        self.frame_81 = QtWidgets.QFrame(self.frame_17)
        self.frame_81.setMinimumSize(QtCore.QSize(120, 0))
        self.frame_81.setStyleSheet("border-top:1.5px solid black;\n"
"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;")
        self.frame_81.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_81.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_81.setObjectName("frame_81")
        self.verticalLayout_68 = QtWidgets.QVBoxLayout(self.frame_81)
        self.verticalLayout_68.setObjectName("verticalLayout_68")
        self.RSSI_value = QtWidgets.QTextEdit(self.frame_81)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RSSI_value.sizePolicy().hasHeightForWidth())
        self.RSSI_value.setSizePolicy(sizePolicy)
        self.RSSI_value.setMinimumSize(QtCore.QSize(0, 0))
        self.RSSI_value.setMaximumSize(QtCore.QSize(145, 16777215))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.RSSI_value.setFont(font)
        self.RSSI_value.setStyleSheet("background:transparent;\n"
"border-top:0px solid black;\n"
"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;")
        self.RSSI_value.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.RSSI_value.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.RSSI_value.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.RSSI_value.setReadOnly(True)
        self.RSSI_value.setObjectName("RSSI_value")
        self.verticalLayout_68.addWidget(self.RSSI_value, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_60.addWidget(self.frame_81)
        self.verticalLayout_60.setStretch(1, 1)
        self.horizontalLayout_12.addWidget(self.frame_17)
        self.verticalLayout_7.addWidget(self.data_1)
        self.homepage_map = QtWidgets.QFrame(self.data_view_frame2)
        self.homepage_map.setStyleSheet("background:green;\n"
"border-radius: 15px;")
        self.homepage_map.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.homepage_map.setFrameShadow(QtWidgets.QFrame.Raised)
        self.homepage_map.setObjectName("homepage_map")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.homepage_map)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.map_display = QtWebEngineWidgets.QWebEngineView(self.homepage_map)
        self.map_display.setStyleSheet("background:transparent;\n"
"border-radius: 15px;")
        self.map_display.setObjectName("map_display")
        self.verticalLayout_15.addWidget(self.map_display)
        self.verticalLayout_7.addWidget(self.homepage_map)
        self.data_2 = QtWidgets.QFrame(self.data_view_frame2)
        self.data_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.data_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.data_2.setObjectName("data_2")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.data_2)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setSpacing(20)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.frame_23 = QtWidgets.QFrame(self.data_2)
        self.frame_23.setMinimumSize(QtCore.QSize(150, 0))
        self.frame_23.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_23.setStyleSheet("background:white;\n"
"border-radius: 15px;")
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.verticalLayout_32 = QtWidgets.QVBoxLayout(self.frame_23)
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.label_48 = QtWidgets.QLabel(self.frame_23)
        self.label_48.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_48.setFont(font)
        self.label_48.setStyleSheet("background:transparent;\n"
"background:#60A7E4;\n"
"border-top-left-radius: 15px;\n"
"border-top-right-radius: 15px;\n"
"border-bottom-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;")
        self.label_48.setAlignment(QtCore.Qt.AlignCenter)
        self.label_48.setObjectName("label_48")
        self.verticalLayout_32.addWidget(self.label_48)
        self.frame_56 = QtWidgets.QFrame(self.frame_23)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_56.sizePolicy().hasHeightForWidth())
        self.frame_56.setSizePolicy(sizePolicy)
        self.frame_56.setStyleSheet("border-top:1.5px solid black;\n"
"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;")
        self.frame_56.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_56.setObjectName("frame_56")
        self.horizontalLayout_50 = QtWidgets.QHBoxLayout(self.frame_56)
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_50.setSpacing(0)
        self.horizontalLayout_50.setObjectName("horizontalLayout_50")
        self.frame_97 = QtWidgets.QFrame(self.frame_56)
        self.frame_97.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_97.setStyleSheet("background:transparent;\n"
"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;\n"
"border-top:0px solid black;")
        self.frame_97.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_97.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_97.setObjectName("frame_97")
        self.verticalLayout_71 = QtWidgets.QVBoxLayout(self.frame_97)
        self.verticalLayout_71.setContentsMargins(9, 0, 0, 0)
        self.verticalLayout_71.setSpacing(9)
        self.verticalLayout_71.setObjectName("verticalLayout_71")
        self.GPS_hp_lat = QtWidgets.QLabel(self.frame_97)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.GPS_hp_lat.setFont(font)
        self.GPS_hp_lat.setStyleSheet("")
        self.GPS_hp_lat.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.GPS_hp_lat.setObjectName("GPS_hp_lat")
        self.verticalLayout_71.addWidget(self.GPS_hp_lat)
        self.GPS_hp_lon = QtWidgets.QLabel(self.frame_97)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.GPS_hp_lon.setFont(font)
        self.GPS_hp_lon.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.GPS_hp_lon.setObjectName("GPS_hp_lon")
        self.verticalLayout_71.addWidget(self.GPS_hp_lon)
        self.horizontalLayout_50.addWidget(self.frame_97)
        self.verticalLayout_32.addWidget(self.frame_56)
        self.verticalLayout_32.setStretch(1, 1)
        self.horizontalLayout_13.addWidget(self.frame_23)
        self.frame_24 = QtWidgets.QFrame(self.data_2)
        self.frame_24.setMinimumSize(QtCore.QSize(150, 0))
        self.frame_24.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_24.setStyleSheet("background:white;\n"
"border-radius: 15px;")
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.verticalLayout_61 = QtWidgets.QVBoxLayout(self.frame_24)
        self.verticalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_61.setSpacing(0)
        self.verticalLayout_61.setObjectName("verticalLayout_61")
        self.label_51 = QtWidgets.QLabel(self.frame_24)
        self.label_51.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_51.setFont(font)
        self.label_51.setStyleSheet("background:transparent;\n"
"background:#60A7E4;\n"
"border-top-left-radius: 15px;\n"
"border-top-right-radius: 15px;\n"
"border-bottom-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;")
        self.label_51.setAlignment(QtCore.Qt.AlignCenter)
        self.label_51.setObjectName("label_51")
        self.verticalLayout_61.addWidget(self.label_51)
        self.frame_61 = QtWidgets.QFrame(self.frame_24)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_61.sizePolicy().hasHeightForWidth())
        self.frame_61.setSizePolicy(sizePolicy)
        self.frame_61.setStyleSheet("border-top:1.5px solid black;\n"
"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;")
        self.frame_61.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_61.setObjectName("frame_61")
        self.horizontalLayout_52 = QtWidgets.QHBoxLayout(self.frame_61)
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_52.setSpacing(0)
        self.horizontalLayout_52.setObjectName("horizontalLayout_52")
        self.frame_101 = QtWidgets.QFrame(self.frame_61)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_101.sizePolicy().hasHeightForWidth())
        self.frame_101.setSizePolicy(sizePolicy)
        self.frame_101.setMinimumSize(QtCore.QSize(150, 0))
        self.frame_101.setStyleSheet("background:transparent;\n"
"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;\n"
"border-bottom-left-radius:0px;\n"
"border-top:0px solid black;")
        self.frame_101.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_101.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_101.setObjectName("frame_101")
        self.verticalLayout_88 = QtWidgets.QVBoxLayout(self.frame_101)
        self.verticalLayout_88.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_88.setObjectName("verticalLayout_88")
        self.frame_102 = QtWidgets.QFrame(self.frame_101)
        self.frame_102.setMaximumSize(QtCore.QSize(150, 16777215))
        self.frame_102.setStyleSheet("background:transparent;\n"
"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;")
        self.frame_102.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_102.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_102.setObjectName("frame_102")
        self.verticalLayout_69 = QtWidgets.QVBoxLayout(self.frame_102)
        self.verticalLayout_69.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_69.setObjectName("verticalLayout_69")
        self.hp_temperature_disp = QtWidgets.QTextEdit(self.frame_102)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hp_temperature_disp.sizePolicy().hasHeightForWidth())
        self.hp_temperature_disp.setSizePolicy(sizePolicy)
        self.hp_temperature_disp.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.hp_temperature_disp.setFont(font)
        self.hp_temperature_disp.setStyleSheet("background:transparent;\n"
"border-top:0px solid black;\n"
"border-left:0px;\n"
"border-right:0px solid black;\n"
"border-bottom-right-radius:0px;\n"
"")
        self.hp_temperature_disp.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.hp_temperature_disp.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.hp_temperature_disp.setReadOnly(True)
        self.hp_temperature_disp.setPlaceholderText("")
        self.hp_temperature_disp.setObjectName("hp_temperature_disp")
        self.verticalLayout_69.addWidget(self.hp_temperature_disp, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_88.addWidget(self.frame_102, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_52.addWidget(self.frame_101)
        self.verticalLayout_61.addWidget(self.frame_61)
        self.verticalLayout_61.setStretch(1, 1)
        self.horizontalLayout_13.addWidget(self.frame_24)
        self.frame_19 = QtWidgets.QFrame(self.data_2)
        self.frame_19.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_19.setStyleSheet("background:white;\n"
"border-radius: 15px;")
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.verticalLayout_63 = QtWidgets.QVBoxLayout(self.frame_19)
        self.verticalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_63.setSpacing(0)
        self.verticalLayout_63.setObjectName("verticalLayout_63")
        self.label_43 = QtWidgets.QLabel(self.frame_19)
        self.label_43.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_43.setFont(font)
        self.label_43.setStyleSheet("background:transparent;\n"
"background:#60A7E4;\n"
"border-top-left-radius: 15px;\n"
"border-top-right-radius: 15px;\n"
"border-bottom-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;")
        self.label_43.setAlignment(QtCore.Qt.AlignCenter)
        self.label_43.setObjectName("label_43")
        self.verticalLayout_63.addWidget(self.label_43)
        self.frame_88 = QtWidgets.QFrame(self.frame_19)
        self.frame_88.setStyleSheet("border-top:1.5px solid black;\n"
"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;")
        self.frame_88.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_88.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_88.setObjectName("frame_88")
        self.verticalLayout_75 = QtWidgets.QVBoxLayout(self.frame_88)
        self.verticalLayout_75.setObjectName("verticalLayout_75")
        self.gps_heading_disp = QtWidgets.QTextEdit(self.frame_88)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gps_heading_disp.sizePolicy().hasHeightForWidth())
        self.gps_heading_disp.setSizePolicy(sizePolicy)
        self.gps_heading_disp.setMinimumSize(QtCore.QSize(0, 0))
        self.gps_heading_disp.setMaximumSize(QtCore.QSize(145, 16777215))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.gps_heading_disp.setFont(font)
        self.gps_heading_disp.setStyleSheet("background:transparent;\n"
"border-top:0px solid black;\n"
"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;")
        self.gps_heading_disp.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.gps_heading_disp.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.gps_heading_disp.setReadOnly(True)
        self.gps_heading_disp.setObjectName("gps_heading_disp")
        self.verticalLayout_75.addWidget(self.gps_heading_disp, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_63.addWidget(self.frame_88)
        self.verticalLayout_63.setStretch(1, 1)
        self.horizontalLayout_13.addWidget(self.frame_19)
        self.frame_18 = QtWidgets.QFrame(self.data_2)
        self.frame_18.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_18.setStyleSheet("background:white;\n"
"border-radius: 15px;")
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.verticalLayout_64 = QtWidgets.QVBoxLayout(self.frame_18)
        self.verticalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_64.setSpacing(0)
        self.verticalLayout_64.setObjectName("verticalLayout_64")
        self.label_44 = QtWidgets.QLabel(self.frame_18)
        self.label_44.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_44.setFont(font)
        self.label_44.setStyleSheet("background:transparent;\n"
"background:#60A7E4;\n"
"border-top-left-radius: 15px;\n"
"border-top-right-radius: 15px;\n"
"border-bottom-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;")
        self.label_44.setAlignment(QtCore.Qt.AlignCenter)
        self.label_44.setObjectName("label_44")
        self.verticalLayout_64.addWidget(self.label_44)
        self.frame_89 = QtWidgets.QFrame(self.frame_18)
        self.frame_89.setStyleSheet("border-top:1.5px solid black;\n"
"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;")
        self.frame_89.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_89.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_89.setObjectName("frame_89")
        self.verticalLayout_76 = QtWidgets.QVBoxLayout(self.frame_89)
        self.verticalLayout_76.setObjectName("verticalLayout_76")
        self.SATS_value = QtWidgets.QTextEdit(self.frame_89)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SATS_value.sizePolicy().hasHeightForWidth())
        self.SATS_value.setSizePolicy(sizePolicy)
        self.SATS_value.setMinimumSize(QtCore.QSize(0, 0))
        self.SATS_value.setMaximumSize(QtCore.QSize(145, 16777215))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.SATS_value.setFont(font)
        self.SATS_value.setStyleSheet("border-top:0px solid black;")
        self.SATS_value.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.SATS_value.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.SATS_value.setReadOnly(True)
        self.SATS_value.setObjectName("SATS_value")
        self.verticalLayout_76.addWidget(self.SATS_value, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_64.addWidget(self.frame_89)
        self.verticalLayout_64.setStretch(1, 1)
        self.horizontalLayout_13.addWidget(self.frame_18)
        self.verticalLayout_7.addWidget(self.data_2)
        self.verticalLayout_7.setStretch(0, 1)
        self.verticalLayout_7.setStretch(1, 3)
        self.verticalLayout_7.setStretch(2, 1)
        self.horizontalLayout_11.addWidget(self.data_view_frame2)
        self.horizontalLayout_14.addWidget(self.data_view_frame_2)
        self.stackedWidget.addWidget(self.home_page)
        self.graphs_page = QtWidgets.QWidget()
        self.graphs_page.setObjectName("graphs_page")
        self.horizontalLayout_43 = QtWidgets.QHBoxLayout(self.graphs_page)
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_43.setSpacing(0)
        self.horizontalLayout_43.setObjectName("horizontalLayout_43")
        self.graphs_page_frame = QtWidgets.QFrame(self.graphs_page)
        self.graphs_page_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.graphs_page_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.graphs_page_frame.setObjectName("graphs_page_frame")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.graphs_page_frame)
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_24.setSpacing(20)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.graph_and_control_panel = QtWidgets.QFrame(self.graphs_page_frame)
        self.graph_and_control_panel.setStyleSheet("background-color:transparent\n"
"\n"
"")
        self.graph_and_control_panel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.graph_and_control_panel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.graph_and_control_panel.setObjectName("graph_and_control_panel")
        self.verticalLayout_47 = QtWidgets.QVBoxLayout(self.graph_and_control_panel)
        self.verticalLayout_47.setContentsMargins(0, 63, 0, 10)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName("verticalLayout_47")
        self.frame_115 = QtWidgets.QFrame(self.graph_and_control_panel)
        self.frame_115.setMinimumSize(QtCore.QSize(775, 0))
        self.frame_115.setMaximumSize(QtCore.QSize(16777215, 65))
        self.frame_115.setStyleSheet("background: black;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius:0px;\n"
"border-top-right-radius: 5px;\n"
"border-top-left-radius:5px;\n"
"")
        self.frame_115.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_115.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_115.setObjectName("frame_115")
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout(self.frame_115)
        self.horizontalLayout_29.setContentsMargins(10, 10, 10, 0)
        self.horizontalLayout_29.setSpacing(5)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.Tab1_btn = QtWidgets.QPushButton(self.frame_115)
        self.Tab1_btn.setMinimumSize(QtCore.QSize(80, 55))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Tab1_btn.setFont(font)
        self.Tab1_btn.setStyleSheet("QPushButton {\n"
"    color:black;\n"
"    \n"
"    background:#7CA6C0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    \n"
"    background: #60A7E4;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    background: #60A7E4;\n"
"    border-radius: 5px;\n"
"}")
        self.Tab1_btn.setObjectName("Tab1_btn")
        self.horizontalLayout_29.addWidget(self.Tab1_btn)
        self.Tab2_btn = QtWidgets.QPushButton(self.frame_115)
        self.Tab2_btn.setMinimumSize(QtCore.QSize(80, 55))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Tab2_btn.setFont(font)
        self.Tab2_btn.setStyleSheet("QPushButton {\n"
"    color:black;\n"
"    \n"
"    background:#7CA6C0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    \n"
"    background: #60A7E4;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    background: #60A7E4;\n"
"    border-radius: 5px;\n"
"}")
        self.Tab2_btn.setObjectName("Tab2_btn")
        self.horizontalLayout_29.addWidget(self.Tab2_btn)
        self.Tab3_btn = QtWidgets.QPushButton(self.frame_115)
        self.Tab3_btn.setMinimumSize(QtCore.QSize(80, 55))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Tab3_btn.setFont(font)
        self.Tab3_btn.setStyleSheet("QPushButton {\n"
"    color:black;\n"
"    \n"
"    background:#7CA6C0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    \n"
"    background: #60A7E4;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    background: #60A7E4;\n"
"    border-radius: 5px;\n"
"}")
        self.Tab3_btn.setObjectName("Tab3_btn")
        self.horizontalLayout_29.addWidget(self.Tab3_btn)
        self.Tab4_btn = QtWidgets.QPushButton(self.frame_115)
        self.Tab4_btn.setMinimumSize(QtCore.QSize(80, 55))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Tab4_btn.setFont(font)
        self.Tab4_btn.setStyleSheet("QPushButton {\n"
"    color:black;\n"
"    \n"
"    background:#7CA6C0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    \n"
"    background: #60A7E4;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    background: #60A7E4;\n"
"    border-radius: 5px;\n"
"}")
        self.Tab4_btn.setObjectName("Tab4_btn")
        self.horizontalLayout_29.addWidget(self.Tab4_btn)
        self.verticalLayout_47.addWidget(self.frame_115, 0, QtCore.Qt.AlignHCenter)
        self.graphs_stackedWidget = QtWidgets.QStackedWidget(self.graph_and_control_panel)
        self.graphs_stackedWidget.setMaximumSize(QtCore.QSize(16777215, 542))
        self.graphs_stackedWidget.setStyleSheet("background:black;\n"
"border-bottom-left-radius:15px;\n"
"border-bottom-right-radius:15px;\n"
"border-top-left-radius:15px;\n"
"border-top-right-radius:15px;")
        self.graphs_stackedWidget.setObjectName("graphs_stackedWidget")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab1)
        self.horizontalLayout_5.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_5 = QtWidgets.QFrame(self.tab1)
        self.frame_5.setStyleSheet("background:transparent;\n"
"border-right: 0.5px solid white;\n"
"border-bottom-right-radius:0px;\n"
"border-top-right-radius:0px;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_41 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_41.setObjectName("verticalLayout_41")
        self.notif_alt_graph_frame = QtWidgets.QFrame(self.frame_5)
        self.notif_alt_graph_frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.notif_alt_graph_frame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.notif_alt_graph_frame.setMouseTracking(False)
        self.notif_alt_graph_frame.setStyleSheet("background:#60A7E4;\n"
"border-radius: 15px;\n"
"border-right:0px solid;")
        self.notif_alt_graph_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.notif_alt_graph_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.notif_alt_graph_frame.setObjectName("notif_alt_graph_frame")
        self.verticalLayout_104 = QtWidgets.QVBoxLayout(self.notif_alt_graph_frame)
        self.verticalLayout_104.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_104.setSpacing(0)
        self.verticalLayout_104.setObjectName("verticalLayout_104")
        self.alt_label_11 = QtWidgets.QFrame(self.notif_alt_graph_frame)
        self.alt_label_11.setMinimumSize(QtCore.QSize(0, 0))
        self.alt_label_11.setStyleSheet("background:#60A7E4;\n"
"border-bottom-left-radius: 0px solid;\n"
"border-bottom-right-radius: 0px solid;")
        self.alt_label_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.alt_label_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.alt_label_11.setObjectName("alt_label_11")
        self.horizontalLayout_58 = QtWidgets.QHBoxLayout(self.alt_label_11)
        self.horizontalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_58.setObjectName("horizontalLayout_58")
        self.notif_alt_label = QtWidgets.QLabel(self.alt_label_11)
        self.notif_alt_label.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.notif_alt_label.setFont(font)
        self.notif_alt_label.setStyleSheet("background:transparent;\n"
"border-top-left-radius:15px;\n"
"border-top-right-radius:0px;")
        self.notif_alt_label.setAlignment(QtCore.Qt.AlignCenter)
        self.notif_alt_label.setObjectName("notif_alt_label")
        self.horizontalLayout_58.addWidget(self.notif_alt_label)
        self.verticalLayout_104.addWidget(self.alt_label_11)
        self.notif_alt_graph = QtWidgets.QFrame(self.notif_alt_graph_frame)
        self.notif_alt_graph.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.notif_alt_graph.setStyleSheet("background:white;\n"
"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;")
        self.notif_alt_graph.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.notif_alt_graph.setFrameShadow(QtWidgets.QFrame.Raised)
        self.notif_alt_graph.setObjectName("notif_alt_graph")
        self.verticalLayout_87 = QtWidgets.QVBoxLayout(self.notif_alt_graph)
        self.verticalLayout_87.setContentsMargins(0, 0, 0, 15)
        self.verticalLayout_87.setSpacing(0)
        self.verticalLayout_87.setObjectName("verticalLayout_87")
        self.notif_alt_graph_temp = QtWidgets.QFrame(self.notif_alt_graph)
        self.notif_alt_graph_temp.setStyleSheet("background:transparent;")
        self.notif_alt_graph_temp.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.notif_alt_graph_temp.setFrameShadow(QtWidgets.QFrame.Raised)
        self.notif_alt_graph_temp.setObjectName("notif_alt_graph_temp")
        self.verticalLayout_87.addWidget(self.notif_alt_graph_temp)
        self.verticalLayout_104.addWidget(self.notif_alt_graph)
        self.verticalLayout_104.setStretch(1, 5)
        self.verticalLayout_41.addWidget(self.notif_alt_graph_frame)
        self.horizontalLayout_5.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.tab1)
        self.frame_6.setStyleSheet("background:transparent;\n"
"border-left: 0.5px solid white;\n"
"border-bottom-left-radius:0px;\n"
"border-top-left-radius:0px;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_46 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_46.setObjectName("verticalLayout_46")
        self.notif_pressure_graph_frame = QtWidgets.QFrame(self.frame_6)
        self.notif_pressure_graph_frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.notif_pressure_graph_frame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.notif_pressure_graph_frame.setMouseTracking(False)
        self.notif_pressure_graph_frame.setStyleSheet("background:#60A7E4;\n"
"border-radius: 15px;\n"
"border-left:0px solid;")
        self.notif_pressure_graph_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.notif_pressure_graph_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.notif_pressure_graph_frame.setObjectName("notif_pressure_graph_frame")
        self.verticalLayout_107 = QtWidgets.QVBoxLayout(self.notif_pressure_graph_frame)
        self.verticalLayout_107.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_107.setSpacing(0)
        self.verticalLayout_107.setObjectName("verticalLayout_107")
        self.alt_label_12 = QtWidgets.QFrame(self.notif_pressure_graph_frame)
        self.alt_label_12.setMinimumSize(QtCore.QSize(0, 0))
        self.alt_label_12.setStyleSheet("background:#60A7E4;\n"
"border-bottom-left-radius: 0px solid;\n"
"border-bottom-right-radius: 0px solid;")
        self.alt_label_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.alt_label_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.alt_label_12.setObjectName("alt_label_12")
        self.horizontalLayout_60 = QtWidgets.QHBoxLayout(self.alt_label_12)
        self.horizontalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_60.setObjectName("horizontalLayout_60")
        self.notif_press_label = QtWidgets.QLabel(self.alt_label_12)
        self.notif_press_label.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.notif_press_label.setFont(font)
        self.notif_press_label.setStyleSheet("background:transparent;\n"
"border-top-left-radius:15px;\n"
"border-top-right-radius:0px;")
        self.notif_press_label.setAlignment(QtCore.Qt.AlignCenter)
        self.notif_press_label.setObjectName("notif_press_label")
        self.horizontalLayout_60.addWidget(self.notif_press_label)
        self.verticalLayout_107.addWidget(self.alt_label_12)
        self.notif_pressure_graph = QtWidgets.QFrame(self.notif_pressure_graph_frame)
        self.notif_pressure_graph.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.notif_pressure_graph.setStyleSheet("background:white;\n"
"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;")
        self.notif_pressure_graph.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.notif_pressure_graph.setFrameShadow(QtWidgets.QFrame.Raised)
        self.notif_pressure_graph.setObjectName("notif_pressure_graph")
        self.verticalLayout_90 = QtWidgets.QVBoxLayout(self.notif_pressure_graph)
        self.verticalLayout_90.setContentsMargins(0, 0, 0, 15)
        self.verticalLayout_90.setSpacing(0)
        self.verticalLayout_90.setObjectName("verticalLayout_90")
        self.notif_pressure_graph_temp = QtWidgets.QFrame(self.notif_pressure_graph)
        self.notif_pressure_graph_temp.setStyleSheet("background:transparent;")
        self.notif_pressure_graph_temp.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.notif_pressure_graph_temp.setFrameShadow(QtWidgets.QFrame.Raised)
        self.notif_pressure_graph_temp.setObjectName("notif_pressure_graph_temp")
        self.verticalLayout_90.addWidget(self.notif_pressure_graph_temp)
        self.verticalLayout_107.addWidget(self.notif_pressure_graph)
        self.verticalLayout_107.setStretch(1, 5)
        self.verticalLayout_46.addWidget(self.notif_pressure_graph_frame)
        self.horizontalLayout_5.addWidget(self.frame_6)
        self.graphs_stackedWidget.addWidget(self.tab1)
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.tab2)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_14 = QtWidgets.QFrame(self.tab2)
        self.frame_14.setStyleSheet("background:transparent;\n"
"border-right: 0.5px solid white;\n"
"border-bottom-right-radius:0px;\n"
"border-top-right-radius:0px;")
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_53 = QtWidgets.QVBoxLayout(self.frame_14)
        self.verticalLayout_53.setObjectName("verticalLayout_53")
        self.notif_voltage_graph_frame = QtWidgets.QFrame(self.frame_14)
        self.notif_voltage_graph_frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.notif_voltage_graph_frame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.notif_voltage_graph_frame.setMouseTracking(False)
        self.notif_voltage_graph_frame.setStyleSheet("background:#60A7E4;\n"
"border-radius: 15px;\n"
"border-right:0px solid;")
        self.notif_voltage_graph_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.notif_voltage_graph_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.notif_voltage_graph_frame.setObjectName("notif_voltage_graph_frame")
        self.verticalLayout_111 = QtWidgets.QVBoxLayout(self.notif_voltage_graph_frame)
        self.verticalLayout_111.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_111.setSpacing(0)
        self.verticalLayout_111.setObjectName("verticalLayout_111")
        self.alt_label_14 = QtWidgets.QFrame(self.notif_voltage_graph_frame)
        self.alt_label_14.setMinimumSize(QtCore.QSize(0, 0))
        self.alt_label_14.setStyleSheet("background:#60A7E4;\n"
"border-bottom-left-radius: 0px solid;\n"
"border-bottom-right-radius: 0px solid;")
        self.alt_label_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.alt_label_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.alt_label_14.setObjectName("alt_label_14")
        self.horizontalLayout_65 = QtWidgets.QHBoxLayout(self.alt_label_14)
        self.horizontalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_65.setObjectName("horizontalLayout_65")
        self.notif_voltage_label = QtWidgets.QLabel(self.alt_label_14)
        self.notif_voltage_label.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.notif_voltage_label.setFont(font)
        self.notif_voltage_label.setStyleSheet("background:transparent;\n"
"border-top-left-radius:15px;\n"
"border-top-right-radius:0px;")
        self.notif_voltage_label.setAlignment(QtCore.Qt.AlignCenter)
        self.notif_voltage_label.setObjectName("notif_voltage_label")
        self.horizontalLayout_65.addWidget(self.notif_voltage_label)
        self.verticalLayout_111.addWidget(self.alt_label_14)
        self.notif_voltage_graph = QtWidgets.QFrame(self.notif_voltage_graph_frame)
        self.notif_voltage_graph.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.notif_voltage_graph.setStyleSheet("background:white;\n"
"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;")
        self.notif_voltage_graph.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.notif_voltage_graph.setFrameShadow(QtWidgets.QFrame.Raised)
        self.notif_voltage_graph.setObjectName("notif_voltage_graph")
        self.verticalLayout_94 = QtWidgets.QVBoxLayout(self.notif_voltage_graph)
        self.verticalLayout_94.setContentsMargins(0, 0, 0, 15)
        self.verticalLayout_94.setSpacing(0)
        self.verticalLayout_94.setObjectName("verticalLayout_94")
        self.notif_voltage_graph_temp = QtWidgets.QFrame(self.notif_voltage_graph)
        self.notif_voltage_graph_temp.setStyleSheet("background:transparent;")
        self.notif_voltage_graph_temp.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.notif_voltage_graph_temp.setFrameShadow(QtWidgets.QFrame.Raised)
        self.notif_voltage_graph_temp.setObjectName("notif_voltage_graph_temp")
        self.verticalLayout_94.addWidget(self.notif_voltage_graph_temp)
        self.verticalLayout_111.addWidget(self.notif_voltage_graph)
        self.verticalLayout_111.setStretch(1, 5)
        self.verticalLayout_53.addWidget(self.notif_voltage_graph_frame)
        self.horizontalLayout_7.addWidget(self.frame_14)
        self.frame_20 = QtWidgets.QFrame(self.tab2)
        self.frame_20.setStyleSheet("background:transparent;\n"
"border-left: 0.5px solid white;\n"
"border-bottom-left-radius:0px;\n"
"border-top-left-radius:0px;")
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.verticalLayout_54 = QtWidgets.QVBoxLayout(self.frame_20)
        self.verticalLayout_54.setObjectName("verticalLayout_54")
        self.notif_velocity_graph_frame = QtWidgets.QFrame(self.frame_20)
        self.notif_velocity_graph_frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.notif_velocity_graph_frame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.notif_velocity_graph_frame.setMouseTracking(False)
        self.notif_velocity_graph_frame.setStyleSheet("background:#60A7E4;\n"
"border-radius: 15px;\n"
"border-left:0px solid;")
        self.notif_velocity_graph_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.notif_velocity_graph_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.notif_velocity_graph_frame.setObjectName("notif_velocity_graph_frame")
        self.verticalLayout_109 = QtWidgets.QVBoxLayout(self.notif_velocity_graph_frame)
        self.verticalLayout_109.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_109.setSpacing(0)
        self.verticalLayout_109.setObjectName("verticalLayout_109")
        self.alt_label_13 = QtWidgets.QFrame(self.notif_velocity_graph_frame)
        self.alt_label_13.setMinimumSize(QtCore.QSize(0, 0))
        self.alt_label_13.setStyleSheet("background:#60A7E4;\n"
"border-bottom-left-radius: 0px solid;\n"
"border-bottom-right-radius: 0px solid;")
        self.alt_label_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.alt_label_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.alt_label_13.setObjectName("alt_label_13")
        self.horizontalLayout_63 = QtWidgets.QHBoxLayout(self.alt_label_13)
        self.horizontalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_63.setObjectName("horizontalLayout_63")
        self.notif_velocity_label = QtWidgets.QLabel(self.alt_label_13)
        self.notif_velocity_label.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.notif_velocity_label.setFont(font)
        self.notif_velocity_label.setStyleSheet("background:transparent;\n"
"border-top-left-radius:15px;\n"
"border-top-right-radius:0px;")
        self.notif_velocity_label.setAlignment(QtCore.Qt.AlignCenter)
        self.notif_velocity_label.setObjectName("notif_velocity_label")
        self.horizontalLayout_63.addWidget(self.notif_velocity_label)
        self.verticalLayout_109.addWidget(self.alt_label_13)
        self.notif_velocity_graph = QtWidgets.QFrame(self.notif_velocity_graph_frame)
        self.notif_velocity_graph.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.notif_velocity_graph.setStyleSheet("background:white;\n"
"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;")
        self.notif_velocity_graph.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.notif_velocity_graph.setFrameShadow(QtWidgets.QFrame.Raised)
        self.notif_velocity_graph.setObjectName("notif_velocity_graph")
        self.verticalLayout_92 = QtWidgets.QVBoxLayout(self.notif_velocity_graph)
        self.verticalLayout_92.setContentsMargins(0, 0, 0, 15)
        self.verticalLayout_92.setSpacing(0)
        self.verticalLayout_92.setObjectName("verticalLayout_92")
        self.notif_velocity_graph_temp = QtWidgets.QFrame(self.notif_velocity_graph)
        self.notif_velocity_graph_temp.setStyleSheet("background:transparent;")
        self.notif_velocity_graph_temp.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.notif_velocity_graph_temp.setFrameShadow(QtWidgets.QFrame.Raised)
        self.notif_velocity_graph_temp.setObjectName("notif_velocity_graph_temp")
        self.verticalLayout_92.addWidget(self.notif_velocity_graph_temp)
        self.verticalLayout_109.addWidget(self.notif_velocity_graph)
        self.verticalLayout_109.setStretch(1, 5)
        self.verticalLayout_54.addWidget(self.notif_velocity_graph_frame)
        self.horizontalLayout_7.addWidget(self.frame_20)
        self.graphs_stackedWidget.addWidget(self.tab2)
        self.tab3 = QtWidgets.QWidget()
        self.tab3.setObjectName("tab3")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.tab3)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.frame_25 = QtWidgets.QFrame(self.tab3)
        self.frame_25.setStyleSheet("background:transparent;\n"
"border-right: 0.5px solid white;\n"
"border-bottom-right-radius:0px;\n"
"border-top-right-radius:0px;")
        self.frame_25.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_25.setObjectName("frame_25")
        self.verticalLayout_55 = QtWidgets.QVBoxLayout(self.frame_25)
        self.verticalLayout_55.setObjectName("verticalLayout_55")
        self.notif_GPSspeedVelocity_graph_frame = QtWidgets.QFrame(self.frame_25)
        self.notif_GPSspeedVelocity_graph_frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.notif_GPSspeedVelocity_graph_frame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.notif_GPSspeedVelocity_graph_frame.setMouseTracking(False)
        self.notif_GPSspeedVelocity_graph_frame.setStyleSheet("background:#60A7E4;\n"
"border-radius: 15px;\n"
"border-right:0px solid;")
        self.notif_GPSspeedVelocity_graph_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.notif_GPSspeedVelocity_graph_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.notif_GPSspeedVelocity_graph_frame.setObjectName("notif_GPSspeedVelocity_graph_frame")
        self.verticalLayout_117 = QtWidgets.QVBoxLayout(self.notif_GPSspeedVelocity_graph_frame)
        self.verticalLayout_117.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_117.setSpacing(0)
        self.verticalLayout_117.setObjectName("verticalLayout_117")
        self.alt_label_15 = QtWidgets.QFrame(self.notif_GPSspeedVelocity_graph_frame)
        self.alt_label_15.setMinimumSize(QtCore.QSize(0, 45))
        self.alt_label_15.setStyleSheet("background:#60A7E4;\n"
"border-bottom-left-radius: 0px solid;\n"
"border-bottom-right-radius: 0px solid;")
        self.alt_label_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.alt_label_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.alt_label_15.setObjectName("alt_label_15")
        self.verticalLayout_50 = QtWidgets.QVBoxLayout(self.alt_label_15)
        self.verticalLayout_50.setContentsMargins(0, 10, 0, 10)
        self.verticalLayout_50.setObjectName("verticalLayout_50")
        self.notif_Velocity_label = QtWidgets.QLabel(self.alt_label_15)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.notif_Velocity_label.setFont(font)
        self.notif_Velocity_label.setStyleSheet("background:transparent;\n"
"border-top-left-radius:15px;\n"
"border-top-right-radius:0px;")
        self.notif_Velocity_label.setAlignment(QtCore.Qt.AlignCenter)
        self.notif_Velocity_label.setObjectName("notif_Velocity_label")
        self.verticalLayout_50.addWidget(self.notif_Velocity_label)
        self.notif_GPSspeed_label = QtWidgets.QLabel(self.alt_label_15)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.notif_GPSspeed_label.setFont(font)
        self.notif_GPSspeed_label.setStyleSheet("background:transparent;\n"
"border-top-left-radius:15px;\n"
"border-top-right-radius:0px;")
        self.notif_GPSspeed_label.setAlignment(QtCore.Qt.AlignCenter)
        self.notif_GPSspeed_label.setObjectName("notif_GPSspeed_label")
        self.verticalLayout_50.addWidget(self.notif_GPSspeed_label)
        self.verticalLayout_117.addWidget(self.alt_label_15)
        self.notif_GPSspeedVelocity_graph = QtWidgets.QFrame(self.notif_GPSspeedVelocity_graph_frame)
        self.notif_GPSspeedVelocity_graph.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.notif_GPSspeedVelocity_graph.setStyleSheet("background:white;\n"
"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;")
        self.notif_GPSspeedVelocity_graph.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.notif_GPSspeedVelocity_graph.setFrameShadow(QtWidgets.QFrame.Raised)
        self.notif_GPSspeedVelocity_graph.setObjectName("notif_GPSspeedVelocity_graph")
        self.verticalLayout_100 = QtWidgets.QVBoxLayout(self.notif_GPSspeedVelocity_graph)
        self.verticalLayout_100.setContentsMargins(0, 0, 0, 15)
        self.verticalLayout_100.setSpacing(0)
        self.verticalLayout_100.setObjectName("verticalLayout_100")
        self.notif_GPSspeedVelocity_graph_temp = QtWidgets.QFrame(self.notif_GPSspeedVelocity_graph)
        self.notif_GPSspeedVelocity_graph_temp.setStyleSheet("background:transparent;")
        self.notif_GPSspeedVelocity_graph_temp.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.notif_GPSspeedVelocity_graph_temp.setFrameShadow(QtWidgets.QFrame.Raised)
        self.notif_GPSspeedVelocity_graph_temp.setObjectName("notif_GPSspeedVelocity_graph_temp")
        self.verticalLayout_100.addWidget(self.notif_GPSspeedVelocity_graph_temp)
        self.verticalLayout_117.addWidget(self.notif_GPSspeedVelocity_graph)
        self.verticalLayout_117.setStretch(1, 5)
        self.verticalLayout_55.addWidget(self.notif_GPSspeedVelocity_graph_frame)
        self.horizontalLayout_15.addWidget(self.frame_25)
        self.frame_26 = QtWidgets.QFrame(self.tab3)
        self.frame_26.setStyleSheet("background:transparent;\n"
"border-left: 0.5px solid white;\n"
"border-bottom-left-radius:0px;\n"
"border-top-left-radius:0px;")
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.verticalLayout_56 = QtWidgets.QVBoxLayout(self.frame_26)
        self.verticalLayout_56.setObjectName("verticalLayout_56")
        self.notif_altGPSalt_graph_frame = QtWidgets.QFrame(self.frame_26)
        self.notif_altGPSalt_graph_frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.notif_altGPSalt_graph_frame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.notif_altGPSalt_graph_frame.setMouseTracking(False)
        self.notif_altGPSalt_graph_frame.setStyleSheet("background:#60A7E4;\n"
"border-radius: 15px;\n"
"border-left:0px solid;")
        self.notif_altGPSalt_graph_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.notif_altGPSalt_graph_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.notif_altGPSalt_graph_frame.setObjectName("notif_altGPSalt_graph_frame")
        self.verticalLayout_120 = QtWidgets.QVBoxLayout(self.notif_altGPSalt_graph_frame)
        self.verticalLayout_120.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_120.setSpacing(0)
        self.verticalLayout_120.setObjectName("verticalLayout_120")
        self.alt_label_16 = QtWidgets.QFrame(self.notif_altGPSalt_graph_frame)
        self.alt_label_16.setMinimumSize(QtCore.QSize(0, 0))
        self.alt_label_16.setStyleSheet("background:#60A7E4;\n"
"border-bottom-left-radius: 0px solid;\n"
"border-bottom-right-radius: 0px solid;")
        self.alt_label_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.alt_label_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.alt_label_16.setObjectName("alt_label_16")
        self.verticalLayout_51 = QtWidgets.QVBoxLayout(self.alt_label_16)
        self.verticalLayout_51.setContentsMargins(0, 10, 0, 10)
        self.verticalLayout_51.setSpacing(6)
        self.verticalLayout_51.setObjectName("verticalLayout_51")
        self.notif_alt_label_2 = QtWidgets.QLabel(self.alt_label_16)
        self.notif_alt_label_2.setMinimumSize(QtCore.QSize(0, 0))
        self.notif_alt_label_2.setMaximumSize(QtCore.QSize(16777215, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.notif_alt_label_2.setFont(font)
        self.notif_alt_label_2.setStyleSheet("background:transparent;\n"
"border-top-left-radius:15px;\n"
"border-top-right-radius:0px;")
        self.notif_alt_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.notif_alt_label_2.setObjectName("notif_alt_label_2")
        self.verticalLayout_51.addWidget(self.notif_alt_label_2)
        self.notif_GPSalt_label = QtWidgets.QLabel(self.alt_label_16)
        self.notif_GPSalt_label.setMinimumSize(QtCore.QSize(0, 0))
        self.notif_GPSalt_label.setMaximumSize(QtCore.QSize(16777215, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.notif_GPSalt_label.setFont(font)
        self.notif_GPSalt_label.setStyleSheet("background:transparent;\n"
"border-top-left-radius:15px;\n"
"border-top-right-radius:0px;")
        self.notif_GPSalt_label.setAlignment(QtCore.Qt.AlignCenter)
        self.notif_GPSalt_label.setObjectName("notif_GPSalt_label")
        self.verticalLayout_51.addWidget(self.notif_GPSalt_label)
        self.verticalLayout_120.addWidget(self.alt_label_16)
        self.notif_altGPSalt_graph = QtWidgets.QFrame(self.notif_altGPSalt_graph_frame)
        self.notif_altGPSalt_graph.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.notif_altGPSalt_graph.setStyleSheet("background:white;\n"
"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;")
        self.notif_altGPSalt_graph.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.notif_altGPSalt_graph.setFrameShadow(QtWidgets.QFrame.Raised)
        self.notif_altGPSalt_graph.setObjectName("notif_altGPSalt_graph")
        self.verticalLayout_96 = QtWidgets.QVBoxLayout(self.notif_altGPSalt_graph)
        self.verticalLayout_96.setContentsMargins(0, 0, 0, 15)
        self.verticalLayout_96.setSpacing(0)
        self.verticalLayout_96.setObjectName("verticalLayout_96")
        self.notif_altGPSalt_graph_temp = QtWidgets.QFrame(self.notif_altGPSalt_graph)
        self.notif_altGPSalt_graph_temp.setStyleSheet("background:transparent;")
        self.notif_altGPSalt_graph_temp.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.notif_altGPSalt_graph_temp.setFrameShadow(QtWidgets.QFrame.Raised)
        self.notif_altGPSalt_graph_temp.setObjectName("notif_altGPSalt_graph_temp")
        self.verticalLayout_96.addWidget(self.notif_altGPSalt_graph_temp)
        self.verticalLayout_120.addWidget(self.notif_altGPSalt_graph)
        self.verticalLayout_120.setStretch(1, 5)
        self.verticalLayout_56.addWidget(self.notif_altGPSalt_graph_frame)
        self.horizontalLayout_15.addWidget(self.frame_26)
        self.graphs_stackedWidget.addWidget(self.tab3)
        self.tab4 = QtWidgets.QWidget()
        self.tab4.setObjectName("tab4")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.tab4)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.frame_27 = QtWidgets.QFrame(self.tab4)
        self.frame_27.setStyleSheet("background:transparent;\n"
"border-right: 0.5px solid white;\n"
"border-bottom-right-radius:0px;\n"
"border-top-right-radius:0px;")
        self.frame_27.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.verticalLayout_48 = QtWidgets.QVBoxLayout(self.frame_27)
        self.verticalLayout_48.setObjectName("verticalLayout_48")
        self.notif_gyro_graph_frame = QtWidgets.QFrame(self.frame_27)
        self.notif_gyro_graph_frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.notif_gyro_graph_frame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.notif_gyro_graph_frame.setMouseTracking(False)
        self.notif_gyro_graph_frame.setStyleSheet("background:#60A7E4;\n"
"border-radius: 15px;\n"
"border-right:0px solid;")
        self.notif_gyro_graph_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.notif_gyro_graph_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.notif_gyro_graph_frame.setObjectName("notif_gyro_graph_frame")
        self.verticalLayout_122 = QtWidgets.QVBoxLayout(self.notif_gyro_graph_frame)
        self.verticalLayout_122.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_122.setSpacing(0)
        self.verticalLayout_122.setObjectName("verticalLayout_122")
        self.alt_label_17 = QtWidgets.QFrame(self.notif_gyro_graph_frame)
        self.alt_label_17.setMinimumSize(QtCore.QSize(0, 0))
        self.alt_label_17.setStyleSheet("background:#60A7E4;\n"
"border-bottom-left-radius: 0px solid;\n"
"border-bottom-right-radius: 0px solid;")
        self.alt_label_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.alt_label_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.alt_label_17.setObjectName("alt_label_17")
        self.verticalLayout_52 = QtWidgets.QVBoxLayout(self.alt_label_17)
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_52.setObjectName("verticalLayout_52")
        self.label_2 = QtWidgets.QLabel(self.alt_label_17)
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background:transparent;\n"
"border-top-left-radius:15px;\n"
"border-top-right-radius:0px;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_52.addWidget(self.label_2)
        self.notif_gyro_label = QtWidgets.QLabel(self.alt_label_17)
        self.notif_gyro_label.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.notif_gyro_label.setFont(font)
        self.notif_gyro_label.setStyleSheet("background:transparent;\n"
"border-top-left-radius:15px;\n"
"border-top-right-radius:0px;")
        self.notif_gyro_label.setAlignment(QtCore.Qt.AlignCenter)
        self.notif_gyro_label.setObjectName("notif_gyro_label")
        self.verticalLayout_52.addWidget(self.notif_gyro_label)
        self.verticalLayout_122.addWidget(self.alt_label_17)
        self.notif_gyro_graph = QtWidgets.QFrame(self.notif_gyro_graph_frame)
        self.notif_gyro_graph.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.notif_gyro_graph.setStyleSheet("background:white;\n"
"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;")
        self.notif_gyro_graph.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.notif_gyro_graph.setFrameShadow(QtWidgets.QFrame.Raised)
        self.notif_gyro_graph.setObjectName("notif_gyro_graph")
        self.verticalLayout_98 = QtWidgets.QVBoxLayout(self.notif_gyro_graph)
        self.verticalLayout_98.setContentsMargins(0, 0, 0, 15)
        self.verticalLayout_98.setSpacing(0)
        self.verticalLayout_98.setObjectName("verticalLayout_98")
        self.notif_gyro_graph_temp = QtWidgets.QFrame(self.notif_gyro_graph)
        self.notif_gyro_graph_temp.setStyleSheet("background:transparent;")
        self.notif_gyro_graph_temp.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.notif_gyro_graph_temp.setFrameShadow(QtWidgets.QFrame.Raised)
        self.notif_gyro_graph_temp.setObjectName("notif_gyro_graph_temp")
        self.verticalLayout_98.addWidget(self.notif_gyro_graph_temp)
        self.verticalLayout_122.addWidget(self.notif_gyro_graph)
        self.verticalLayout_122.setStretch(1, 5)
        self.verticalLayout_48.addWidget(self.notif_gyro_graph_frame)
        self.horizontalLayout_16.addWidget(self.frame_27)
        self.frame_31 = QtWidgets.QFrame(self.tab4)
        self.frame_31.setStyleSheet("background:transparent;\n"
"border-left: 0.5px solid white;\n"
"border-bottom-left-radius:0px;\n"
"border-top-left-radius:0px;")
        self.frame_31.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_31.setObjectName("frame_31")
        self.verticalLayout_49 = QtWidgets.QVBoxLayout(self.frame_31)
        self.verticalLayout_49.setObjectName("verticalLayout_49")
        self.notif_acc_graph_frame = QtWidgets.QFrame(self.frame_31)
        self.notif_acc_graph_frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.notif_acc_graph_frame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.notif_acc_graph_frame.setMouseTracking(False)
        self.notif_acc_graph_frame.setStyleSheet("background:#60A7E4;\n"
"border-radius: 15px;\n"
"border-left:0px solid;")
        self.notif_acc_graph_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.notif_acc_graph_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.notif_acc_graph_frame.setObjectName("notif_acc_graph_frame")
        self.verticalLayout_124 = QtWidgets.QVBoxLayout(self.notif_acc_graph_frame)
        self.verticalLayout_124.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_124.setSpacing(0)
        self.verticalLayout_124.setObjectName("verticalLayout_124")
        self.alt_label_18 = QtWidgets.QFrame(self.notif_acc_graph_frame)
        self.alt_label_18.setMinimumSize(QtCore.QSize(0, 0))
        self.alt_label_18.setStyleSheet("background:#60A7E4;\n"
"border-bottom-left-radius: 0px solid;\n"
"border-bottom-right-radius: 0px solid;")
        self.alt_label_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.alt_label_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.alt_label_18.setObjectName("alt_label_18")
        self.verticalLayout_62 = QtWidgets.QVBoxLayout(self.alt_label_18)
        self.verticalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_62.setObjectName("verticalLayout_62")
        self.label_3 = QtWidgets.QLabel(self.alt_label_18)
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background:transparent;\n"
"border-top-left-radius:15px;\n"
"border-top-right-radius:0px;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_62.addWidget(self.label_3)
        self.notif_acc_label = QtWidgets.QLabel(self.alt_label_18)
        self.notif_acc_label.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.notif_acc_label.setFont(font)
        self.notif_acc_label.setStyleSheet("background:transparent;\n"
"border-top-left-radius:15px;\n"
"border-top-right-radius:0px;")
        self.notif_acc_label.setAlignment(QtCore.Qt.AlignCenter)
        self.notif_acc_label.setObjectName("notif_acc_label")
        self.verticalLayout_62.addWidget(self.notif_acc_label)
        self.verticalLayout_124.addWidget(self.alt_label_18)
        self.notif_acc_graph = QtWidgets.QFrame(self.notif_acc_graph_frame)
        self.notif_acc_graph.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.notif_acc_graph.setStyleSheet("background:white;\n"
"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;")
        self.notif_acc_graph.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.notif_acc_graph.setFrameShadow(QtWidgets.QFrame.Raised)
        self.notif_acc_graph.setObjectName("notif_acc_graph")
        self.verticalLayout_102 = QtWidgets.QVBoxLayout(self.notif_acc_graph)
        self.verticalLayout_102.setContentsMargins(0, 0, 0, 15)
        self.verticalLayout_102.setSpacing(0)
        self.verticalLayout_102.setObjectName("verticalLayout_102")
        self.notif_acc_graph_temp = QtWidgets.QFrame(self.notif_acc_graph)
        self.notif_acc_graph_temp.setStyleSheet("background:transparent;")
        self.notif_acc_graph_temp.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.notif_acc_graph_temp.setFrameShadow(QtWidgets.QFrame.Raised)
        self.notif_acc_graph_temp.setObjectName("notif_acc_graph_temp")
        self.verticalLayout_102.addWidget(self.notif_acc_graph_temp)
        self.verticalLayout_124.addWidget(self.notif_acc_graph)
        self.verticalLayout_124.setStretch(1, 5)
        self.verticalLayout_49.addWidget(self.notif_acc_graph_frame)
        self.horizontalLayout_16.addWidget(self.frame_31)
        self.graphs_stackedWidget.addWidget(self.tab4)
        self.verticalLayout_47.addWidget(self.graphs_stackedWidget)
        self.custom_widget_frame = QtWidgets.QFrame(self.graph_and_control_panel)
        self.custom_widget_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.custom_widget_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.custom_widget_frame.setObjectName("custom_widget_frame")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout(self.custom_widget_frame)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.verticalLayout_47.addWidget(self.custom_widget_frame)
        self.horizontalLayout_24.addWidget(self.graph_and_control_panel)
        self.graph_page_side_panel_frame = QtWidgets.QFrame(self.graphs_page_frame)
        self.graph_page_side_panel_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.graph_page_side_panel_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.graph_page_side_panel_frame.setObjectName("graph_page_side_panel_frame")
        self.verticalLayout_57 = QtWidgets.QVBoxLayout(self.graph_page_side_panel_frame)
        self.verticalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_57.setSpacing(0)
        self.verticalLayout_57.setObjectName("verticalLayout_57")
        self.frame_7 = QtWidgets.QFrame(self.graph_page_side_panel_frame)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_57.addWidget(self.frame_7)
        self.graph_page_side_panel = QtWidgets.QFrame(self.graph_page_side_panel_frame)
        self.graph_page_side_panel.setStyleSheet("background:#7CA6C0;\n"
"border-top-left-radius:25px;\n"
"border-bottom-left-radius:25px;\n"
"border-bottom-right-radius:25px;\n"
"border-top-right-radius:25px;")
        self.graph_page_side_panel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.graph_page_side_panel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.graph_page_side_panel.setObjectName("graph_page_side_panel")
        self.verticalLayout_112 = QtWidgets.QVBoxLayout(self.graph_page_side_panel)
        self.verticalLayout_112.setContentsMargins(0, 18, 0, 10)
        self.verticalLayout_112.setSpacing(30)
        self.verticalLayout_112.setObjectName("verticalLayout_112")
        self.label_27 = QtWidgets.QLabel(self.graph_page_side_panel)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("background:transparent;")
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_112.addWidget(self.label_27)
        self.frame_58 = QtWidgets.QFrame(self.graph_page_side_panel)
        self.frame_58.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_58.setObjectName("frame_58")
        self.verticalLayout_113 = QtWidgets.QVBoxLayout(self.frame_58)
        self.verticalLayout_113.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_113.setSpacing(10)
        self.verticalLayout_113.setObjectName("verticalLayout_113")
        self.frame_60 = QtWidgets.QFrame(self.frame_58)
        self.frame_60.setMinimumSize(QtCore.QSize(306, 42))
        self.frame_60.setStyleSheet("background:white;\n"
"border-top-left-radius:15px;\n"
"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:15px;\n"
"border-top-right-radius:0px;")
        self.frame_60.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_60.setObjectName("frame_60")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_60)
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.altitude_label_graphs_sidepanel = QtWidgets.QLabel(self.frame_60)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.altitude_label_graphs_sidepanel.setFont(font)
        self.altitude_label_graphs_sidepanel.setText("")
        self.altitude_label_graphs_sidepanel.setObjectName("altitude_label_graphs_sidepanel")
        self.horizontalLayout_6.addWidget(self.altitude_label_graphs_sidepanel)
        self.verticalLayout_113.addWidget(self.frame_60)
        self.frame_134 = QtWidgets.QFrame(self.frame_58)
        self.frame_134.setMinimumSize(QtCore.QSize(168, 42))
        self.frame_134.setStyleSheet("background:white;\n"
"border-top-left-radius:15px;\n"
"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:15px;\n"
"border-top-right-radius:0px;")
        self.frame_134.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_134.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_134.setObjectName("frame_134")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame_134)
        self.horizontalLayout_17.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.velocity_label_graphs_sidepanel = QtWidgets.QLabel(self.frame_134)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.velocity_label_graphs_sidepanel.setFont(font)
        self.velocity_label_graphs_sidepanel.setText("")
        self.velocity_label_graphs_sidepanel.setObjectName("velocity_label_graphs_sidepanel")
        self.horizontalLayout_17.addWidget(self.velocity_label_graphs_sidepanel)
        self.verticalLayout_113.addWidget(self.frame_134)
        self.frame_227 = QtWidgets.QFrame(self.frame_58)
        self.frame_227.setMinimumSize(QtCore.QSize(168, 42))
        self.frame_227.setStyleSheet("background:white;\n"
"border-top-left-radius:15px;\n"
"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:15px;\n"
"border-top-right-radius:0px;")
        self.frame_227.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_227.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_227.setObjectName("frame_227")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.frame_227)
        self.horizontalLayout_18.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.temperature_label_graphs_sidepanel = QtWidgets.QLabel(self.frame_227)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.temperature_label_graphs_sidepanel.setFont(font)
        self.temperature_label_graphs_sidepanel.setText("")
        self.temperature_label_graphs_sidepanel.setObjectName("temperature_label_graphs_sidepanel")
        self.horizontalLayout_18.addWidget(self.temperature_label_graphs_sidepanel)
        self.verticalLayout_113.addWidget(self.frame_227)
        self.verticalLayout_112.addWidget(self.frame_58)
        self.frame_228 = QtWidgets.QFrame(self.graph_page_side_panel)
        self.frame_228.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_228.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_228.setObjectName("frame_228")
        self.verticalLayout_114 = QtWidgets.QVBoxLayout(self.frame_228)
        self.verticalLayout_114.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_114.setSpacing(10)
        self.verticalLayout_114.setObjectName("verticalLayout_114")
        self.frame_229 = QtWidgets.QFrame(self.frame_228)
        self.frame_229.setMinimumSize(QtCore.QSize(168, 42))
        self.frame_229.setStyleSheet("background:white;\n"
"border-top-left-radius:15px;\n"
"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:15px;\n"
"border-top-right-radius:0px;")
        self.frame_229.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_229.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_229.setObjectName("frame_229")
        self.verticalLayout_73 = QtWidgets.QVBoxLayout(self.frame_229)
        self.verticalLayout_73.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_73.setObjectName("verticalLayout_73")
        self.acc_x_label_graphs_sidepanel = QtWidgets.QLabel(self.frame_229)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.acc_x_label_graphs_sidepanel.setFont(font)
        self.acc_x_label_graphs_sidepanel.setText("")
        self.acc_x_label_graphs_sidepanel.setObjectName("acc_x_label_graphs_sidepanel")
        self.verticalLayout_73.addWidget(self.acc_x_label_graphs_sidepanel)
        self.verticalLayout_114.addWidget(self.frame_229)
        self.frame_230 = QtWidgets.QFrame(self.frame_228)
        self.frame_230.setMinimumSize(QtCore.QSize(168, 42))
        self.frame_230.setStyleSheet("background:white;\n"
"border-top-left-radius:15px;\n"
"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:15px;\n"
"border-top-right-radius:0px;")
        self.frame_230.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_230.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_230.setObjectName("frame_230")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.frame_230)
        self.horizontalLayout_19.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.acc_y_label_graphs_sidepanel = QtWidgets.QLabel(self.frame_230)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.acc_y_label_graphs_sidepanel.setFont(font)
        self.acc_y_label_graphs_sidepanel.setText("")
        self.acc_y_label_graphs_sidepanel.setObjectName("acc_y_label_graphs_sidepanel")
        self.horizontalLayout_19.addWidget(self.acc_y_label_graphs_sidepanel)
        self.verticalLayout_114.addWidget(self.frame_230)
        self.frame_231 = QtWidgets.QFrame(self.frame_228)
        self.frame_231.setMinimumSize(QtCore.QSize(168, 42))
        self.frame_231.setStyleSheet("background:white;\n"
"border-top-left-radius:15px;\n"
"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:15px;\n"
"border-top-right-radius:0px;")
        self.frame_231.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_231.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_231.setObjectName("frame_231")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.frame_231)
        self.horizontalLayout_25.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.acc_z_label_graphs_sidepanel = QtWidgets.QLabel(self.frame_231)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.acc_z_label_graphs_sidepanel.setFont(font)
        self.acc_z_label_graphs_sidepanel.setText("")
        self.acc_z_label_graphs_sidepanel.setObjectName("acc_z_label_graphs_sidepanel")
        self.horizontalLayout_25.addWidget(self.acc_z_label_graphs_sidepanel)
        self.verticalLayout_114.addWidget(self.frame_231)
        self.verticalLayout_112.addWidget(self.frame_228)
        self.frame_232 = QtWidgets.QFrame(self.graph_page_side_panel)
        self.frame_232.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_232.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_232.setObjectName("frame_232")
        self.verticalLayout_115 = QtWidgets.QVBoxLayout(self.frame_232)
        self.verticalLayout_115.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_115.setSpacing(10)
        self.verticalLayout_115.setObjectName("verticalLayout_115")
        self.frame_233 = QtWidgets.QFrame(self.frame_232)
        self.frame_233.setMinimumSize(QtCore.QSize(168, 42))
        self.frame_233.setStyleSheet("background:white;\n"
"border-top-left-radius:15px;\n"
"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:15px;\n"
"border-top-right-radius:0px;")
        self.frame_233.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_233.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_233.setObjectName("frame_233")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.frame_233)
        self.horizontalLayout_26.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.gyro_x_label_graphs_sidepanel = QtWidgets.QLabel(self.frame_233)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gyro_x_label_graphs_sidepanel.setFont(font)
        self.gyro_x_label_graphs_sidepanel.setText("")
        self.gyro_x_label_graphs_sidepanel.setObjectName("gyro_x_label_graphs_sidepanel")
        self.horizontalLayout_26.addWidget(self.gyro_x_label_graphs_sidepanel)
        self.verticalLayout_115.addWidget(self.frame_233)
        self.frame_234 = QtWidgets.QFrame(self.frame_232)
        self.frame_234.setMinimumSize(QtCore.QSize(168, 42))
        self.frame_234.setStyleSheet("background:white;\n"
"border-top-left-radius:15px;\n"
"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:15px;\n"
"border-top-right-radius:0px;")
        self.frame_234.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_234.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_234.setObjectName("frame_234")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.frame_234)
        self.horizontalLayout_27.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.gyro_y_label_graphs_sidepanel = QtWidgets.QLabel(self.frame_234)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gyro_y_label_graphs_sidepanel.setFont(font)
        self.gyro_y_label_graphs_sidepanel.setText("")
        self.gyro_y_label_graphs_sidepanel.setObjectName("gyro_y_label_graphs_sidepanel")
        self.horizontalLayout_27.addWidget(self.gyro_y_label_graphs_sidepanel)
        self.verticalLayout_115.addWidget(self.frame_234)
        self.frame_235 = QtWidgets.QFrame(self.frame_232)
        self.frame_235.setMinimumSize(QtCore.QSize(168, 42))
        self.frame_235.setStyleSheet("background:white;\n"
"border-top-left-radius:15px;\n"
"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:15px;\n"
"border-top-right-radius:0px;")
        self.frame_235.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_235.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_235.setObjectName("frame_235")
        self.verticalLayout_74 = QtWidgets.QVBoxLayout(self.frame_235)
        self.verticalLayout_74.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_74.setObjectName("verticalLayout_74")
        self.gyro_z_label_graphs_sidepanel = QtWidgets.QLabel(self.frame_235)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gyro_z_label_graphs_sidepanel.setFont(font)
        self.gyro_z_label_graphs_sidepanel.setText("")
        self.gyro_z_label_graphs_sidepanel.setObjectName("gyro_z_label_graphs_sidepanel")
        self.verticalLayout_74.addWidget(self.gyro_z_label_graphs_sidepanel)
        self.verticalLayout_115.addWidget(self.frame_235)
        self.verticalLayout_112.addWidget(self.frame_232)
        self.verticalLayout_112.setStretch(1, 1)
        self.verticalLayout_112.setStretch(2, 1)
        self.verticalLayout_112.setStretch(3, 1)
        self.verticalLayout_57.addWidget(self.graph_page_side_panel)
        self.frame_66 = QtWidgets.QFrame(self.graph_page_side_panel_frame)
        self.frame_66.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_66.setObjectName("frame_66")
        self.verticalLayout_57.addWidget(self.frame_66)
        self.verticalLayout_57.setStretch(0, 1)
        self.verticalLayout_57.setStretch(2, 2)
        self.horizontalLayout_24.addWidget(self.graph_page_side_panel_frame)
        self.horizontalLayout_24.setStretch(0, 4)
        self.horizontalLayout_24.setStretch(1, 1)
        self.horizontalLayout_43.addWidget(self.graphs_page_frame)
        self.stackedWidget.addWidget(self.graphs_page)
        self.GPS_page = QtWidgets.QWidget()
        self.GPS_page.setObjectName("GPS_page")
        self.horizontalLayout_84 = QtWidgets.QHBoxLayout(self.GPS_page)
        self.horizontalLayout_84.setContentsMargins(0, 0, 0, 20)
        self.horizontalLayout_84.setSpacing(20)
        self.horizontalLayout_84.setObjectName("horizontalLayout_84")
        self.gpsmaps_2 = QtWidgets.QFrame(self.GPS_page)
        self.gpsmaps_2.setStyleSheet("background-color:black;\n"
"border-radius:15px;\n"
"")
        self.gpsmaps_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gpsmaps_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gpsmaps_2.setObjectName("gpsmaps_2")
        self.verticalLayout_103 = QtWidgets.QVBoxLayout(self.gpsmaps_2)
        self.verticalLayout_103.setObjectName("verticalLayout_103")
        self.map_display_GPS_page = QtWebEngineWidgets.QWebEngineView(self.gpsmaps_2)
        self.map_display_GPS_page.setStyleSheet("background:transparent;\n"
"border-radius: 15px;")
        self.map_display_GPS_page.setObjectName("map_display_GPS_page")
        self.verticalLayout_103.addWidget(self.map_display_GPS_page)
        self.horizontalLayout_84.addWidget(self.gpsmaps_2)
        self.frame_213 = QtWidgets.QFrame(self.GPS_page)
        self.frame_213.setStyleSheet("background:transparent;")
        self.frame_213.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_213.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_213.setObjectName("frame_213")
        self.verticalLayout_105 = QtWidgets.QVBoxLayout(self.frame_213)
        self.verticalLayout_105.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_105.setSpacing(0)
        self.verticalLayout_105.setObjectName("verticalLayout_105")
        self.RKT_model_panel_4 = QtWidgets.QFrame(self.frame_213)
        self.RKT_model_panel_4.setStyleSheet("background:black;\n"
"border-top-left-radius:25px;\n"
"border-bottom-left-radius:25px;\n"
"border-bottom-right-radius:25px;\n"
"border-top-right-radius:25px;")
        self.RKT_model_panel_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.RKT_model_panel_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.RKT_model_panel_4.setObjectName("RKT_model_panel_4")
        self.verticalLayout_116 = QtWidgets.QVBoxLayout(self.RKT_model_panel_4)
        self.verticalLayout_116.setContentsMargins(0, 18, 0, 10)
        self.verticalLayout_116.setSpacing(0)
        self.verticalLayout_116.setObjectName("verticalLayout_116")
        self.label_31 = QtWidgets.QLabel(self.RKT_model_panel_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("background:transparent;\n"
"color:white;")
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.verticalLayout_116.addWidget(self.label_31)
        self.frame_237 = QtWidgets.QFrame(self.RKT_model_panel_4)
        self.frame_237.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_237.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_237.setObjectName("frame_237")
        self.verticalLayout_118 = QtWidgets.QVBoxLayout(self.frame_237)
        self.verticalLayout_118.setContentsMargins(-1, 9, -1, -1)
        self.verticalLayout_118.setSpacing(43)
        self.verticalLayout_118.setObjectName("verticalLayout_118")
        self.frame_240 = QtWidgets.QFrame(self.frame_237)
        self.frame_240.setMinimumSize(QtCore.QSize(168, 42))
        self.frame_240.setStyleSheet("background:white;\n"
"border-top-left-radius:25px;\n"
"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:25px;\n"
"border-top-right-radius:0px;")
        self.frame_240.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_240.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_240.setObjectName("frame_240")
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout(self.frame_240)
        self.horizontalLayout_34.setContentsMargins(-1, 0, 0, 0)
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.GPS_SATSno_label = QtWidgets.QLabel(self.frame_240)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.GPS_SATSno_label.setFont(font)
        self.GPS_SATSno_label.setStyleSheet("color:black;\n"
"background:transparent;")
        self.GPS_SATSno_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.GPS_SATSno_label.setObjectName("GPS_SATSno_label")
        self.horizontalLayout_34.addWidget(self.GPS_SATSno_label)
        self.horizontalLayout_34.setStretch(0, 1)
        self.verticalLayout_118.addWidget(self.frame_240)
        self.frame_69 = QtWidgets.QFrame(self.frame_237)
        self.frame_69.setMinimumSize(QtCore.QSize(306, 42))
        self.frame_69.setStyleSheet("background:white;\n"
"border-top-left-radius:25px;\n"
"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:25px;\n"
"border-top-right-radius:0px;")
        self.frame_69.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_69.setObjectName("frame_69")
        self.horizontalLayout_36 = QtWidgets.QHBoxLayout(self.frame_69)
        self.horizontalLayout_36.setContentsMargins(-1, 0, 0, 0)
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.GPS_lat_label = QtWidgets.QLabel(self.frame_69)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.GPS_lat_label.setFont(font)
        self.GPS_lat_label.setStyleSheet("color:black;\n"
"background:transparent;")
        self.GPS_lat_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.GPS_lat_label.setObjectName("GPS_lat_label")
        self.horizontalLayout_36.addWidget(self.GPS_lat_label)
        self.horizontalLayout_36.setStretch(0, 1)
        self.verticalLayout_118.addWidget(self.frame_69)
        self.frame_68 = QtWidgets.QFrame(self.frame_237)
        self.frame_68.setMinimumSize(QtCore.QSize(306, 42))
        self.frame_68.setStyleSheet("background:white;\n"
"border-top-left-radius:25px;\n"
"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:25px;\n"
"border-top-right-radius:0px;")
        self.frame_68.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_68.setObjectName("frame_68")
        self.horizontalLayout_38 = QtWidgets.QHBoxLayout(self.frame_68)
        self.horizontalLayout_38.setContentsMargins(-1, 0, 0, 0)
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        self.GPS_lon_label = QtWidgets.QLabel(self.frame_68)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.GPS_lon_label.setFont(font)
        self.GPS_lon_label.setStyleSheet("color:black;\n"
"background:transparent;")
        self.GPS_lon_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.GPS_lon_label.setObjectName("GPS_lon_label")
        self.horizontalLayout_38.addWidget(self.GPS_lon_label)
        self.horizontalLayout_38.setStretch(0, 1)
        self.verticalLayout_118.addWidget(self.frame_68)
        self.frame_70 = QtWidgets.QFrame(self.frame_237)
        self.frame_70.setMinimumSize(QtCore.QSize(306, 42))
        self.frame_70.setStyleSheet("background:white;\n"
"border-top-left-radius:25px;\n"
"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:25px;\n"
"border-top-right-radius:0px;")
        self.frame_70.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_70.setObjectName("frame_70")
        self.horizontalLayout_39 = QtWidgets.QHBoxLayout(self.frame_70)
        self.horizontalLayout_39.setContentsMargins(-1, 0, 0, 0)
        self.horizontalLayout_39.setObjectName("horizontalLayout_39")
        self.GPS_altitude_label = QtWidgets.QLabel(self.frame_70)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.GPS_altitude_label.setFont(font)
        self.GPS_altitude_label.setStyleSheet("color:black;\n"
"background:transparent;")
        self.GPS_altitude_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.GPS_altitude_label.setObjectName("GPS_altitude_label")
        self.horizontalLayout_39.addWidget(self.GPS_altitude_label)
        self.horizontalLayout_39.setStretch(0, 1)
        self.verticalLayout_118.addWidget(self.frame_70)
        self.frame_71 = QtWidgets.QFrame(self.frame_237)
        self.frame_71.setMinimumSize(QtCore.QSize(306, 42))
        self.frame_71.setStyleSheet("background:white;\n"
"border-top-left-radius:25px;\n"
"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:25px;\n"
"border-top-right-radius:0px;")
        self.frame_71.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_71.setObjectName("frame_71")
        self.horizontalLayout_40 = QtWidgets.QHBoxLayout(self.frame_71)
        self.horizontalLayout_40.setContentsMargins(-1, 0, 0, 0)
        self.horizontalLayout_40.setObjectName("horizontalLayout_40")
        self.GPS_speed_label = QtWidgets.QLabel(self.frame_71)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.GPS_speed_label.setFont(font)
        self.GPS_speed_label.setStyleSheet("color:black;\n"
"background:transparent;")
        self.GPS_speed_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.GPS_speed_label.setObjectName("GPS_speed_label")
        self.horizontalLayout_40.addWidget(self.GPS_speed_label)
        self.horizontalLayout_40.setStretch(0, 1)
        self.verticalLayout_118.addWidget(self.frame_71)
        self.frame_239 = QtWidgets.QFrame(self.frame_237)
        self.frame_239.setMinimumSize(QtCore.QSize(168, 42))
        self.frame_239.setStyleSheet("background:white;\n"
"border-top-left-radius:25px;\n"
"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:25px;\n"
"border-top-right-radius:0px;")
        self.frame_239.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_239.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_239.setObjectName("frame_239")
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout(self.frame_239)
        self.horizontalLayout_33.setContentsMargins(-1, 0, 0, 0)
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.gps_heading_label = QtWidgets.QLabel(self.frame_239)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.gps_heading_label.setFont(font)
        self.gps_heading_label.setStyleSheet("color:black;\n"
"background:transparent;")
        self.gps_heading_label.setObjectName("gps_heading_label")
        self.horizontalLayout_33.addWidget(self.gps_heading_label)
        self.verticalLayout_118.addWidget(self.frame_239)
        self.frame_238 = QtWidgets.QFrame(self.frame_237)
        self.frame_238.setMinimumSize(QtCore.QSize(168, 42))
        self.frame_238.setStyleSheet("background:white;\n"
"border-top-left-radius:25px;\n"
"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:25px;\n"
"border-top-right-radius:0px;")
        self.frame_238.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_238.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_238.setObjectName("frame_238")
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout(self.frame_238)
        self.horizontalLayout_32.setContentsMargins(9, 0, 0, 0)
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.mag_heading_label = QtWidgets.QLabel(self.frame_238)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.mag_heading_label.setFont(font)
        self.mag_heading_label.setStyleSheet("color:black;\n"
"background:transparent;")
        self.mag_heading_label.setObjectName("mag_heading_label")
        self.horizontalLayout_32.addWidget(self.mag_heading_label)
        self.verticalLayout_118.addWidget(self.frame_238)
        self.verticalLayout_116.addWidget(self.frame_237)
        self.verticalLayout_105.addWidget(self.RKT_model_panel_4)
        self.frame_224 = QtWidgets.QFrame(self.frame_213)
        self.frame_224.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_224.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_224.setObjectName("frame_224")
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout(self.frame_224)
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.frame_10 = QtWidgets.QFrame(self.frame_224)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.frame_33 = QtWidgets.QFrame(self.frame_10)
        self.frame_33.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_33.setObjectName("frame_33")
        self.horizontalLayout_31.addWidget(self.frame_33)
        self.horizontalLayout_30.addWidget(self.frame_10)
        self.frame_32 = QtWidgets.QFrame(self.frame_224)
        self.frame_32.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_32.setObjectName("frame_32")
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout(self.frame_32)
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.frame_34 = QtWidgets.QFrame(self.frame_32)
        self.frame_34.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_34.setObjectName("frame_34")
        self.horizontalLayout_35.addWidget(self.frame_34)
        self.horizontalLayout_30.addWidget(self.frame_32)
        self.verticalLayout_105.addWidget(self.frame_224)
        self.verticalLayout_105.setStretch(1, 1)
        self.horizontalLayout_84.addWidget(self.frame_213)
        self.horizontalLayout_84.setStretch(0, 4)
        self.horizontalLayout_84.setStretch(1, 1)
        self.stackedWidget.addWidget(self.GPS_page)
        self.RKT_model_page = QtWidgets.QWidget()
        self.RKT_model_page.setObjectName("RKT_model_page")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.RKT_model_page)
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 20)
        self.horizontalLayout_20.setSpacing(20)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.model_frame = QtWidgets.QFrame(self.RKT_model_page)
        self.model_frame.setStyleSheet("background:#16222d;\n"
"border-radius: 25px;")
        self.model_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.model_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.model_frame.setObjectName("model_frame")
        self.horizontalLayout_37 = QtWidgets.QHBoxLayout(self.model_frame)
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        self.frame_35 = QtWidgets.QFrame(self.model_frame)
        self.frame_35.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_35.setObjectName("frame_35")
        self.horizontalLayout_37.addWidget(self.frame_35)
        self.horizontalLayout_20.addWidget(self.model_frame)
        self.panel_temp_frame = QtWidgets.QFrame(self.RKT_model_page)
        self.panel_temp_frame.setMinimumSize(QtCore.QSize(326, 0))
        self.panel_temp_frame.setStyleSheet("background:transparent;")
        self.panel_temp_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.panel_temp_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.panel_temp_frame.setObjectName("panel_temp_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.panel_temp_frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget = QtWidgets.QWidget(self.panel_temp_frame)
        self.widget.setObjectName("widget")
        self.verticalLayout_3.addWidget(self.widget)
        self.rkt_model_right_panel = QtWidgets.QFrame(self.panel_temp_frame)
        self.rkt_model_right_panel.setStyleSheet("background:#7CA6C0;\n"
"border-top-left-radius:25px;\n"
"border-bottom-left-radius:25px;\n"
"border-bottom-right-radius:25px;\n"
"border-top-right-radius:25px;")
        self.rkt_model_right_panel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rkt_model_right_panel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rkt_model_right_panel.setObjectName("rkt_model_right_panel")
        self.verticalLayout_119 = QtWidgets.QVBoxLayout(self.rkt_model_right_panel)
        self.verticalLayout_119.setContentsMargins(0, 18, 0, 10)
        self.verticalLayout_119.setSpacing(30)
        self.verticalLayout_119.setObjectName("verticalLayout_119")
        self.label_28 = QtWidgets.QLabel(self.rkt_model_right_panel)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("background:transparent;")
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.verticalLayout_119.addWidget(self.label_28)
        self.frame_59 = QtWidgets.QFrame(self.rkt_model_right_panel)
        self.frame_59.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_59.setObjectName("frame_59")
        self.verticalLayout_121 = QtWidgets.QVBoxLayout(self.frame_59)
        self.verticalLayout_121.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_121.setSpacing(10)
        self.verticalLayout_121.setObjectName("verticalLayout_121")
        self.frame_63 = QtWidgets.QFrame(self.frame_59)
        self.frame_63.setMinimumSize(QtCore.QSize(306, 42))
        self.frame_63.setStyleSheet("background:white;\n"
"border-top-left-radius:15px;\n"
"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:15px;\n"
"border-top-right-radius:0px;")
        self.frame_63.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_63.setObjectName("frame_63")
        self.horizontalLayout_42 = QtWidgets.QHBoxLayout(self.frame_63)
        self.horizontalLayout_42.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_42.setSpacing(0)
        self.horizontalLayout_42.setObjectName("horizontalLayout_42")
        self.pitch_label_rkt = QtWidgets.QLabel(self.frame_63)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pitch_label_rkt.setFont(font)
        self.pitch_label_rkt.setText("")
        self.pitch_label_rkt.setObjectName("pitch_label_rkt")
        self.horizontalLayout_42.addWidget(self.pitch_label_rkt)
        self.verticalLayout_121.addWidget(self.frame_63)
        self.frame_135 = QtWidgets.QFrame(self.frame_59)
        self.frame_135.setMinimumSize(QtCore.QSize(168, 42))
        self.frame_135.setStyleSheet("background:white;\n"
"border-top-left-radius:15px;\n"
"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:15px;\n"
"border-top-right-radius:0px;")
        self.frame_135.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_135.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_135.setObjectName("frame_135")
        self.horizontalLayout_46 = QtWidgets.QHBoxLayout(self.frame_135)
        self.horizontalLayout_46.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_46.setObjectName("horizontalLayout_46")
        self.yaw_label_pkt = QtWidgets.QLabel(self.frame_135)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.yaw_label_pkt.setFont(font)
        self.yaw_label_pkt.setText("")
        self.yaw_label_pkt.setObjectName("yaw_label_pkt")
        self.horizontalLayout_46.addWidget(self.yaw_label_pkt)
        self.verticalLayout_121.addWidget(self.frame_135)
        self.frame_236 = QtWidgets.QFrame(self.frame_59)
        self.frame_236.setMinimumSize(QtCore.QSize(168, 42))
        self.frame_236.setStyleSheet("background:white;\n"
"border-top-left-radius:15px;\n"
"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:15px;\n"
"border-top-right-radius:0px;")
        self.frame_236.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_236.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_236.setObjectName("frame_236")
        self.horizontalLayout_53 = QtWidgets.QHBoxLayout(self.frame_236)
        self.horizontalLayout_53.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_53.setObjectName("horizontalLayout_53")
        self.roll_label_rkt = QtWidgets.QLabel(self.frame_236)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.roll_label_rkt.setFont(font)
        self.roll_label_rkt.setText("")
        self.roll_label_rkt.setObjectName("roll_label_rkt")
        self.horizontalLayout_53.addWidget(self.roll_label_rkt)
        self.verticalLayout_121.addWidget(self.frame_236)
        self.verticalLayout_119.addWidget(self.frame_59)
        self.frame_241 = QtWidgets.QFrame(self.rkt_model_right_panel)
        self.frame_241.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_241.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_241.setObjectName("frame_241")
        self.verticalLayout_123 = QtWidgets.QVBoxLayout(self.frame_241)
        self.verticalLayout_123.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_123.setSpacing(10)
        self.verticalLayout_123.setObjectName("verticalLayout_123")
        self.frame_242 = QtWidgets.QFrame(self.frame_241)
        self.frame_242.setMinimumSize(QtCore.QSize(168, 42))
        self.frame_242.setStyleSheet("background:white;\n"
"border-top-left-radius:15px;\n"
"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:15px;\n"
"border-top-right-radius:0px;")
        self.frame_242.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_242.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_242.setObjectName("frame_242")
        self.verticalLayout_89 = QtWidgets.QVBoxLayout(self.frame_242)
        self.verticalLayout_89.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_89.setObjectName("verticalLayout_89")
        self.acc_x_rkt = QtWidgets.QLabel(self.frame_242)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.acc_x_rkt.setFont(font)
        self.acc_x_rkt.setText("")
        self.acc_x_rkt.setObjectName("acc_x_rkt")
        self.verticalLayout_89.addWidget(self.acc_x_rkt)
        self.verticalLayout_123.addWidget(self.frame_242)
        self.frame_243 = QtWidgets.QFrame(self.frame_241)
        self.frame_243.setMinimumSize(QtCore.QSize(168, 42))
        self.frame_243.setStyleSheet("background:white;\n"
"border-top-left-radius:15px;\n"
"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:15px;\n"
"border-top-right-radius:0px;")
        self.frame_243.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_243.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_243.setObjectName("frame_243")
        self.horizontalLayout_54 = QtWidgets.QHBoxLayout(self.frame_243)
        self.horizontalLayout_54.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_54.setObjectName("horizontalLayout_54")
        self.acc_y_rkt = QtWidgets.QLabel(self.frame_243)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.acc_y_rkt.setFont(font)
        self.acc_y_rkt.setText("")
        self.acc_y_rkt.setObjectName("acc_y_rkt")
        self.horizontalLayout_54.addWidget(self.acc_y_rkt)
        self.verticalLayout_123.addWidget(self.frame_243)
        self.frame_244 = QtWidgets.QFrame(self.frame_241)
        self.frame_244.setMinimumSize(QtCore.QSize(168, 42))
        self.frame_244.setStyleSheet("background:white;\n"
"border-top-left-radius:15px;\n"
"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:15px;\n"
"border-top-right-radius:0px;")
        self.frame_244.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_244.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_244.setObjectName("frame_244")
        self.horizontalLayout_55 = QtWidgets.QHBoxLayout(self.frame_244)
        self.horizontalLayout_55.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_55.setObjectName("horizontalLayout_55")
        self.acc_z_rkt = QtWidgets.QLabel(self.frame_244)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.acc_z_rkt.setFont(font)
        self.acc_z_rkt.setText("")
        self.acc_z_rkt.setObjectName("acc_z_rkt")
        self.horizontalLayout_55.addWidget(self.acc_z_rkt)
        self.verticalLayout_123.addWidget(self.frame_244)
        self.verticalLayout_119.addWidget(self.frame_241)
        self.frame_245 = QtWidgets.QFrame(self.rkt_model_right_panel)
        self.frame_245.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_245.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_245.setObjectName("frame_245")
        self.verticalLayout_125 = QtWidgets.QVBoxLayout(self.frame_245)
        self.verticalLayout_125.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_125.setSpacing(10)
        self.verticalLayout_125.setObjectName("verticalLayout_125")
        self.frame_246 = QtWidgets.QFrame(self.frame_245)
        self.frame_246.setMinimumSize(QtCore.QSize(168, 42))
        self.frame_246.setStyleSheet("background:white;\n"
"border-top-left-radius:15px;\n"
"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:15px;\n"
"border-top-right-radius:0px;")
        self.frame_246.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_246.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_246.setObjectName("frame_246")
        self.horizontalLayout_56 = QtWidgets.QHBoxLayout(self.frame_246)
        self.horizontalLayout_56.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_56.setObjectName("horizontalLayout_56")
        self.gyro_x_rkt = QtWidgets.QLabel(self.frame_246)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gyro_x_rkt.setFont(font)
        self.gyro_x_rkt.setText("")
        self.gyro_x_rkt.setObjectName("gyro_x_rkt")
        self.horizontalLayout_56.addWidget(self.gyro_x_rkt)
        self.verticalLayout_125.addWidget(self.frame_246)
        self.frame_247 = QtWidgets.QFrame(self.frame_245)
        self.frame_247.setMinimumSize(QtCore.QSize(168, 42))
        self.frame_247.setStyleSheet("background:white;\n"
"border-top-left-radius:15px;\n"
"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:15px;\n"
"border-top-right-radius:0px;")
        self.frame_247.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_247.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_247.setObjectName("frame_247")
        self.horizontalLayout_57 = QtWidgets.QHBoxLayout(self.frame_247)
        self.horizontalLayout_57.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_57.setObjectName("horizontalLayout_57")
        self.gyro_y_rkt = QtWidgets.QLabel(self.frame_247)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gyro_y_rkt.setFont(font)
        self.gyro_y_rkt.setText("")
        self.gyro_y_rkt.setObjectName("gyro_y_rkt")
        self.horizontalLayout_57.addWidget(self.gyro_y_rkt)
        self.verticalLayout_125.addWidget(self.frame_247)
        self.frame_248 = QtWidgets.QFrame(self.frame_245)
        self.frame_248.setMinimumSize(QtCore.QSize(168, 42))
        self.frame_248.setStyleSheet("background:white;\n"
"border-top-left-radius:15px;\n"
"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:15px;\n"
"border-top-right-radius:0px;")
        self.frame_248.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_248.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_248.setObjectName("frame_248")
        self.verticalLayout_91 = QtWidgets.QVBoxLayout(self.frame_248)
        self.verticalLayout_91.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_91.setObjectName("verticalLayout_91")
        self.gyro_z_rkt = QtWidgets.QLabel(self.frame_248)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gyro_z_rkt.setFont(font)
        self.gyro_z_rkt.setText("")
        self.gyro_z_rkt.setObjectName("gyro_z_rkt")
        self.verticalLayout_91.addWidget(self.gyro_z_rkt)
        self.verticalLayout_125.addWidget(self.frame_248)
        self.verticalLayout_119.addWidget(self.frame_245)
        self.verticalLayout_119.setStretch(1, 1)
        self.verticalLayout_119.setStretch(2, 1)
        self.verticalLayout_119.setStretch(3, 1)
        self.verticalLayout_3.addWidget(self.rkt_model_right_panel)
        self.frame_120 = QtWidgets.QFrame(self.panel_temp_frame)
        self.frame_120.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_120.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_120.setObjectName("frame_120")
        self.verticalLayout_3.addWidget(self.frame_120)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(2, 5)
        self.horizontalLayout_20.addWidget(self.panel_temp_frame)
        self.horizontalLayout_20.setStretch(0, 6)
        self.horizontalLayout_20.setStretch(1, 1)
        self.stackedWidget.addWidget(self.RKT_model_page)
        self.table_data_page = QtWidgets.QWidget()
        self.table_data_page.setObjectName("table_data_page")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.table_data_page)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 20)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.frame = QtWidgets.QFrame(self.table_data_page)
        self.frame.setStyleSheet("background:white;\n"
"border-radius:15px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.table_data_csv_display = QtWidgets.QTableWidget(self.frame)
        font = QtGui.QFont()
        font.setFamily("Sitka Display Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.table_data_csv_display.setFont(font)
        self.table_data_csv_display.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 63 10pt \"Sitka Display Semibold\";\n"
"color: rgb(0, 0, 0);\n"
"border-radius:15px;")
        self.table_data_csv_display.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.table_data_csv_display.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_data_csv_display.setShowGrid(True)
        self.table_data_csv_display.setGridStyle(QtCore.Qt.SolidLine)
        self.table_data_csv_display.setObjectName("table_data_csv_display")
        self.table_data_csv_display.setColumnCount(29)
        self.table_data_csv_display.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_data_csv_display.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data_csv_display.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data_csv_display.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data_csv_display.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data_csv_display.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data_csv_display.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data_csv_display.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data_csv_display.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data_csv_display.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data_csv_display.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data_csv_display.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data_csv_display.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data_csv_display.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data_csv_display.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data_csv_display.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data_csv_display.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data_csv_display.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data_csv_display.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data_csv_display.setHorizontalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data_csv_display.setHorizontalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data_csv_display.setHorizontalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data_csv_display.setHorizontalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data_csv_display.setHorizontalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data_csv_display.setHorizontalHeaderItem(23, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data_csv_display.setHorizontalHeaderItem(24, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data_csv_display.setHorizontalHeaderItem(25, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data_csv_display.setHorizontalHeaderItem(26, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data_csv_display.setHorizontalHeaderItem(27, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data_csv_display.setHorizontalHeaderItem(28, item)
        self.verticalLayout_2.addWidget(self.table_data_csv_display)
        self.verticalLayout_16.addWidget(self.frame)
        self.stackedWidget.addWidget(self.table_data_page)
        self.settings_page = QtWidgets.QWidget()
        self.settings_page.setObjectName("settings_page")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.settings_page)
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 20)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.frame_2 = QtWidgets.QFrame(self.settings_page)
        self.frame_2.setMinimumSize(QtCore.QSize(1387, 764))
        self.frame_2.setStyleSheet("background:#16222d;\n"
"border-radius: 25px;\n"
"border: 2px solid gray;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_4.setStyleSheet("border:0px")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_19.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_19.setSpacing(20)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.frame_9 = QtWidgets.QFrame(self.frame_4)
        self.frame_9.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(20)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.eulersAngle_units = QtWidgets.QFrame(self.frame_9)
        self.eulersAngle_units.setStyleSheet("border:2px solid gray;\n"
"border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;")
        self.eulersAngle_units.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.eulersAngle_units.setFrameShadow(QtWidgets.QFrame.Raised)
        self.eulersAngle_units.setObjectName("eulersAngle_units")
        self.verticalLayout_42 = QtWidgets.QVBoxLayout(self.eulersAngle_units)
        self.verticalLayout_42.setObjectName("verticalLayout_42")
        self.label_22 = QtWidgets.QLabel(self.eulersAngle_units)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("border:0px;color:white;")
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_42.addWidget(self.label_22)
        self.frame_50 = QtWidgets.QFrame(self.eulersAngle_units)
        self.frame_50.setStyleSheet("color:white;\n"
"border:0px;")
        self.frame_50.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_50.setObjectName("frame_50")
        self.verticalLayout_37 = QtWidgets.QVBoxLayout(self.frame_50)
        self.verticalLayout_37.setContentsMargins(98, -1, -1, -1)
        self.verticalLayout_37.setObjectName("verticalLayout_37")
        self.eulers_deg = QtWidgets.QRadioButton(self.frame_50)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.eulers_deg.setFont(font)
        self.eulers_deg.setObjectName("eulers_deg")
        self.verticalLayout_37.addWidget(self.eulers_deg)
        self.eulers_rad = QtWidgets.QRadioButton(self.frame_50)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.eulers_rad.setFont(font)
        self.eulers_rad.setObjectName("eulers_rad")
        self.verticalLayout_37.addWidget(self.eulers_rad)
        self.verticalLayout_42.addWidget(self.frame_50)
        self.verticalLayout_42.setStretch(1, 1)
        self.gridLayout_4.addWidget(self.eulersAngle_units, 1, 1, 1, 1)
        self.speed_units = QtWidgets.QFrame(self.frame_9)
        self.speed_units.setStyleSheet("border:2px solid gray;\n"
"border-top-left-radius: 0px;\n"
"border-top-right-radius: 15px;\n"
"border-bottom-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;")
        self.speed_units.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.speed_units.setFrameShadow(QtWidgets.QFrame.Raised)
        self.speed_units.setObjectName("speed_units")
        self.verticalLayout_44 = QtWidgets.QVBoxLayout(self.speed_units)
        self.verticalLayout_44.setObjectName("verticalLayout_44")
        self.label_24 = QtWidgets.QLabel(self.speed_units)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("border:0px;color:white;")
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_44.addWidget(self.label_24)
        self.frame_52 = QtWidgets.QFrame(self.speed_units)
        self.frame_52.setStyleSheet("color:white;\n"
"border:0px;")
        self.frame_52.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_52.setObjectName("frame_52")
        self.verticalLayout_39 = QtWidgets.QVBoxLayout(self.frame_52)
        self.verticalLayout_39.setContentsMargins(98, -1, -1, -1)
        self.verticalLayout_39.setObjectName("verticalLayout_39")
        self.GPS_speed_mph = QtWidgets.QRadioButton(self.frame_52)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.GPS_speed_mph.setFont(font)
        self.GPS_speed_mph.setObjectName("GPS_speed_mph")
        self.verticalLayout_39.addWidget(self.GPS_speed_mph)
        self.GPS_speed_kmph = QtWidgets.QRadioButton(self.frame_52)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.GPS_speed_kmph.setFont(font)
        self.GPS_speed_kmph.setObjectName("GPS_speed_kmph")
        self.verticalLayout_39.addWidget(self.GPS_speed_kmph)
        self.verticalLayout_44.addWidget(self.frame_52)
        self.verticalLayout_44.setStretch(1, 1)
        self.gridLayout_4.addWidget(self.speed_units, 0, 2, 1, 1)
        self.GPS_altitude_units = QtWidgets.QFrame(self.frame_9)
        self.GPS_altitude_units.setStyleSheet("border:2px solid gray;\n"
"border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;")
        self.GPS_altitude_units.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.GPS_altitude_units.setFrameShadow(QtWidgets.QFrame.Raised)
        self.GPS_altitude_units.setObjectName("GPS_altitude_units")
        self.verticalLayout_43 = QtWidgets.QVBoxLayout(self.GPS_altitude_units)
        self.verticalLayout_43.setObjectName("verticalLayout_43")
        self.label_23 = QtWidgets.QLabel(self.GPS_altitude_units)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("border:0px;color:white;")
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_43.addWidget(self.label_23)
        self.frame_51 = QtWidgets.QFrame(self.GPS_altitude_units)
        self.frame_51.setStyleSheet("color:white;\n"
"border:0px;")
        self.frame_51.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_51.setObjectName("frame_51")
        self.verticalLayout_38 = QtWidgets.QVBoxLayout(self.frame_51)
        self.verticalLayout_38.setContentsMargins(98, -1, -1, -1)
        self.verticalLayout_38.setObjectName("verticalLayout_38")
        self.GPS_alt_feet = QtWidgets.QRadioButton(self.frame_51)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.GPS_alt_feet.setFont(font)
        self.GPS_alt_feet.setObjectName("GPS_alt_feet")
        self.verticalLayout_38.addWidget(self.GPS_alt_feet)
        self.GPS_alt_meters = QtWidgets.QRadioButton(self.frame_51)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.GPS_alt_meters.setFont(font)
        self.GPS_alt_meters.setObjectName("GPS_alt_meters")
        self.verticalLayout_38.addWidget(self.GPS_alt_meters)
        self.verticalLayout_43.addWidget(self.frame_51)
        self.verticalLayout_43.setStretch(1, 1)
        self.gridLayout_4.addWidget(self.GPS_altitude_units, 2, 1, 1, 1)
        self.gyrometer_units = QtWidgets.QFrame(self.frame_9)
        self.gyrometer_units.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.gyrometer_units.setStyleSheet("border:2px solid gray;\n"
"border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;")
        self.gyrometer_units.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gyrometer_units.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gyrometer_units.setObjectName("gyrometer_units")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout(self.gyrometer_units)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.label_19 = QtWidgets.QLabel(self.gyrometer_units)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("border:0px;color:white;")
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_29.addWidget(self.label_19)
        self.frame_46 = QtWidgets.QFrame(self.gyrometer_units)
        self.frame_46.setStyleSheet("color:white;\n"
"border:0px;")
        self.frame_46.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_46.setObjectName("frame_46")
        self.verticalLayout_30 = QtWidgets.QVBoxLayout(self.frame_46)
        self.verticalLayout_30.setContentsMargins(98, -1, -1, -1)
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.gyro_dps = QtWidgets.QRadioButton(self.frame_46)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gyro_dps.setFont(font)
        self.gyro_dps.setObjectName("gyro_dps")
        self.verticalLayout_30.addWidget(self.gyro_dps)
        self.gyro_rps = QtWidgets.QRadioButton(self.frame_46)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gyro_rps.setFont(font)
        self.gyro_rps.setObjectName("gyro_rps")
        self.verticalLayout_30.addWidget(self.gyro_rps)
        self.verticalLayout_29.addWidget(self.frame_46)
        self.verticalLayout_29.setStretch(1, 1)
        self.gridLayout_4.addWidget(self.gyrometer_units, 0, 1, 1, 1)
        self.accelerometer_units = QtWidgets.QFrame(self.frame_9)
        self.accelerometer_units.setStyleSheet("border:2px solid gray;\n"
"border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;")
        self.accelerometer_units.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.accelerometer_units.setFrameShadow(QtWidgets.QFrame.Raised)
        self.accelerometer_units.setObjectName("accelerometer_units")
        self.verticalLayout_45 = QtWidgets.QVBoxLayout(self.accelerometer_units)
        self.verticalLayout_45.setObjectName("verticalLayout_45")
        self.label_25 = QtWidgets.QLabel(self.accelerometer_units)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("border:0px;color:white;")
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_45.addWidget(self.label_25)
        self.frame_53 = QtWidgets.QFrame(self.accelerometer_units)
        self.frame_53.setStyleSheet("color:white;\n"
"border:0px;")
        self.frame_53.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_53.setObjectName("frame_53")
        self.verticalLayout_40 = QtWidgets.QVBoxLayout(self.frame_53)
        self.verticalLayout_40.setContentsMargins(98, -1, -1, -1)
        self.verticalLayout_40.setObjectName("verticalLayout_40")
        self.acc_fps = QtWidgets.QRadioButton(self.frame_53)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.acc_fps.setFont(font)
        self.acc_fps.setObjectName("acc_fps")
        self.verticalLayout_40.addWidget(self.acc_fps)
        self.acc_mps = QtWidgets.QRadioButton(self.frame_53)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.acc_mps.setFont(font)
        self.acc_mps.setObjectName("acc_mps")
        self.verticalLayout_40.addWidget(self.acc_mps)
        self.verticalLayout_45.addWidget(self.frame_53)
        self.verticalLayout_45.setStretch(1, 1)
        self.gridLayout_4.addWidget(self.accelerometer_units, 1, 2, 1, 1)
        self.velocity_units = QtWidgets.QFrame(self.frame_9)
        self.velocity_units.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.velocity_units.setStyleSheet("border:2px solid gray;\n"
"border-top-left-radius: 15px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;")
        self.velocity_units.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.velocity_units.setFrameShadow(QtWidgets.QFrame.Raised)
        self.velocity_units.setObjectName("velocity_units")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.velocity_units)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_14 = QtWidgets.QLabel(self.velocity_units)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("border: 0px;\n"
"color:white;")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_20.addWidget(self.label_14)
        self.frame_41 = QtWidgets.QFrame(self.velocity_units)
        self.frame_41.setStyleSheet("border:0px;")
        self.frame_41.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_41.setObjectName("frame_41")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.frame_41)
        self.verticalLayout_21.setContentsMargins(98, -1, -1, -1)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.vel_mph = QtWidgets.QRadioButton(self.frame_41)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.vel_mph.setFont(font)
        self.vel_mph.setStyleSheet("color:white;")
        self.vel_mph.setObjectName("vel_mph")
        self.verticalLayout_21.addWidget(self.vel_mph)
        self.vel_kmph = QtWidgets.QRadioButton(self.frame_41)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.vel_kmph.setFont(font)
        self.vel_kmph.setStyleSheet("color:white;")
        self.vel_kmph.setObjectName("vel_kmph")
        self.verticalLayout_21.addWidget(self.vel_kmph)
        self.verticalLayout_20.addWidget(self.frame_41)
        self.verticalLayout_20.setStretch(1, 1)
        self.gridLayout_4.addWidget(self.velocity_units, 0, 0, 1, 1)
        self.temperature_units = QtWidgets.QFrame(self.frame_9)
        self.temperature_units.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.temperature_units.setStyleSheet("border:2px solid gray;\n"
"border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;")
        self.temperature_units.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.temperature_units.setFrameShadow(QtWidgets.QFrame.Raised)
        self.temperature_units.setObjectName("temperature_units")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.temperature_units)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.label_15 = QtWidgets.QLabel(self.temperature_units)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("border:0px;\n"
"color:white;")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_22.addWidget(self.label_15)
        self.frame_43 = QtWidgets.QFrame(self.temperature_units)
        self.frame_43.setStyleSheet("border:0px;")
        self.frame_43.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_43.setObjectName("frame_43")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.frame_43)
        self.verticalLayout_23.setContentsMargins(98, -1, -1, -1)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.tempC = QtWidgets.QRadioButton(self.frame_43)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tempC.setFont(font)
        self.tempC.setStyleSheet("color:white;")
        self.tempC.setObjectName("tempC")
        self.verticalLayout_23.addWidget(self.tempC)
        self.tempF = QtWidgets.QRadioButton(self.frame_43)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tempF.setFont(font)
        self.tempF.setStyleSheet("color:white;")
        self.tempF.setObjectName("tempF")
        self.verticalLayout_23.addWidget(self.tempF)
        self.verticalLayout_22.addWidget(self.frame_43)
        self.verticalLayout_22.setStretch(1, 1)
        self.gridLayout_4.addWidget(self.temperature_units, 1, 0, 1, 1)
        self.altitude_units = QtWidgets.QFrame(self.frame_9)
        self.altitude_units.setMinimumSize(QtCore.QSize(0, 162))
        self.altitude_units.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.altitude_units.setStyleSheet("border:2px solid gray;\n"
"border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;")
        self.altitude_units.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.altitude_units.setFrameShadow(QtWidgets.QFrame.Raised)
        self.altitude_units.setObjectName("altitude_units")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.altitude_units)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.label_16 = QtWidgets.QLabel(self.altitude_units)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("border:0px;\n"
"color:white;")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_24.addWidget(self.label_16)
        self.frame_44 = QtWidgets.QFrame(self.altitude_units)
        self.frame_44.setStyleSheet("border:0px;")
        self.frame_44.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_44.setObjectName("frame_44")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.frame_44)
        self.verticalLayout_25.setContentsMargins(98, -1, -1, -1)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.Alt_feet = QtWidgets.QRadioButton(self.frame_44)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Alt_feet.setFont(font)
        self.Alt_feet.setStyleSheet("color:white;")
        self.Alt_feet.setObjectName("Alt_feet")
        self.verticalLayout_25.addWidget(self.Alt_feet)
        self.Alter_meters = QtWidgets.QRadioButton(self.frame_44)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Alter_meters.setFont(font)
        self.Alter_meters.setStyleSheet("color:white;")
        self.Alter_meters.setObjectName("Alter_meters")
        self.verticalLayout_25.addWidget(self.Alter_meters)
        self.verticalLayout_24.addWidget(self.frame_44)
        self.verticalLayout_24.setStretch(1, 1)
        self.gridLayout_4.addWidget(self.altitude_units, 2, 0, 1, 1)
        self.frame_47 = QtWidgets.QFrame(self.frame_9)
        self.frame_47.setStyleSheet("border:2px solid gray;\n"
"border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;")
        self.frame_47.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_47.setObjectName("frame_47")
        self.verticalLayout_35 = QtWidgets.QVBoxLayout(self.frame_47)
        self.verticalLayout_35.setObjectName("verticalLayout_35")
        self.apply_all_changes = QtWidgets.QCheckBox(self.frame_47)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.apply_all_changes.setFont(font)
        self.apply_all_changes.setStyleSheet("color:white;\n"
"border:0px solid;")
        self.apply_all_changes.setObjectName("apply_all_changes")
        self.verticalLayout_35.addWidget(self.apply_all_changes, 0, QtCore.Qt.AlignHCenter)
        self.download_file_btn = QtWidgets.QPushButton(self.frame_47)
        self.download_file_btn.setMinimumSize(QtCore.QSize(195, 0))
        self.download_file_btn.setMaximumSize(QtCore.QSize(242, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.download_file_btn.setFont(font)
        self.download_file_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(57, 62, 70);\n"
"    color:white;\n"
"    border-radius:25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background:white;\n"
"    color:black;\n"
"    border-radius:25px;\n"
"}\n"
"\n"
"QPushButton:pressed { \n"
"    border:2px solid gray;\n"
"    background-color: rgb(57, 62, 70);\n"
"    color:white;\n"
"    border-radius:25px;\n"
"}")
        self.download_file_btn.setObjectName("download_file_btn")
        self.verticalLayout_35.addWidget(self.download_file_btn, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout_4.addWidget(self.frame_47, 2, 2, 1, 1)
        self.verticalLayout_19.addWidget(self.frame_9)
        self.default_data_file_folder_frame = QtWidgets.QFrame(self.frame_4)
        self.default_data_file_folder_frame.setStyleSheet("border:0px solid white;\n"
"border-radius:0px;\n"
"background:transparent;")
        self.default_data_file_folder_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.default_data_file_folder_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.default_data_file_folder_frame.setObjectName("default_data_file_folder_frame")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.default_data_file_folder_frame)
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_23.setSpacing(20)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.frame_3 = QtWidgets.QFrame(self.default_data_file_folder_frame)
        self.frame_3.setStyleSheet("border:2px solid gray;\n"
"border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-left-radius: 15px;\n"
"border-bottom-right-radius: 0px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_36 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_36.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_36.setSpacing(20)
        self.verticalLayout_36.setObjectName("verticalLayout_36")
        self.label_21 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("border:0px;\n"
"color:white;")
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_36.addWidget(self.label_21)
        self.frame_49 = QtWidgets.QFrame(self.frame_3)
        self.frame_49.setStyleSheet("border:0px solid;\n"
"background:transparent;")
        self.frame_49.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_49.setObjectName("frame_49")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_49)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.data_file_folder_name = QtWidgets.QTextEdit(self.frame_49)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.data_file_folder_name.sizePolicy().hasHeightForWidth())
        self.data_file_folder_name.setSizePolicy(sizePolicy)
        self.data_file_folder_name.setMinimumSize(QtCore.QSize(696, 50))
        self.data_file_folder_name.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.data_file_folder_name.setFont(font)
        self.data_file_folder_name.setStyleSheet("background: white;\n"
"border-radius: 15px;\n"
"border: 0px solid black;")
        self.data_file_folder_name.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.data_file_folder_name.setReadOnly(True)
        self.data_file_folder_name.setMarkdown("")
        self.data_file_folder_name.setPlaceholderText("")
        self.data_file_folder_name.setObjectName("data_file_folder_name")
        self.horizontalLayout_4.addWidget(self.data_file_folder_name)
        self.browse_for_folders_btn = QtWidgets.QPushButton(self.frame_49)
        self.browse_for_folders_btn.setMinimumSize(QtCore.QSize(192, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.browse_for_folders_btn.setFont(font)
        self.browse_for_folders_btn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.browse_for_folders_btn.setStyleSheet("QPushButton {\n"
"    border:2px solid gray;\n"
"    background-color: rgb(57, 62, 70);\n"
"    color:white;\n"
"    border-radius:25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border:2px solid gray;\n"
"    background:white;\n"
"    color:black;\n"
"    border-radius:25px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border:2px solid gray;\n"
"    background-color: rgb(57, 62, 70);\n"
"    color:white;\n"
"    border-radius:25px;\n"
"}")
        self.browse_for_folders_btn.setIconSize(QtCore.QSize(44, 37))
        self.browse_for_folders_btn.setObjectName("browse_for_folders_btn")
        self.horizontalLayout_4.addWidget(self.browse_for_folders_btn)
        self.horizontalLayout_4.setStretch(0, 1)
        self.verticalLayout_36.addWidget(self.frame_49)
        self.verticalLayout_36.setStretch(1, 1)
        self.horizontalLayout_23.addWidget(self.frame_3)
        self.frame_8 = QtWidgets.QFrame(self.default_data_file_folder_frame)
        self.frame_8.setMinimumSize(QtCore.QSize(300, 0))
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_8.setStyleSheet("border:2px solid gray;\n"
"border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"border-bottom-right-radius: 15px;")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.label_17 = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("border:0px;\n"
"color:white;")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_26.addWidget(self.label_17)
        self.frame_42 = QtWidgets.QFrame(self.frame_8)
        self.frame_42.setStyleSheet("border:0px;")
        self.frame_42.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_42.setObjectName("frame_42")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.frame_42)
        self.verticalLayout_27.setContentsMargins(40, -1, 40, 0)
        self.verticalLayout_27.setSpacing(6)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.label_18 = QtWidgets.QLabel(self.frame_42)
        self.label_18.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color:white;")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_27.addWidget(self.label_18)
        self.comboBox = QtWidgets.QComboBox(self.frame_42)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 0))
        self.comboBox.setStyleSheet("background:white;\n"
"border-bottom-left-radius:0px;")
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout_27.addWidget(self.comboBox)
        self.frame_45 = QtWidgets.QFrame(self.frame_42)
        self.frame_45.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_45.setObjectName("frame_45")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout(self.frame_45)
        self.verticalLayout_28.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.verticalLayout_27.addWidget(self.frame_45)
        self.verticalLayout_27.setStretch(1, 1)
        self.verticalLayout_26.addWidget(self.frame_42)
        self.verticalLayout_26.setStretch(1, 1)
        self.horizontalLayout_23.addWidget(self.frame_8)
        self.frame_12 = QtWidgets.QFrame(self.default_data_file_folder_frame)
        self.frame_12.setStyleSheet("border:0px solid white;\n"
"background:transparent;")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18.setSpacing(20)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.horizontalLayout_23.addWidget(self.frame_12)
        self.horizontalLayout_23.setStretch(0, 1)
        self.verticalLayout_19.addWidget(self.default_data_file_folder_frame)
        self.verticalLayout_19.setStretch(0, 1)
        self.horizontalLayout_22.addWidget(self.frame_4)
        self.horizontalLayout_22.setStretch(0, 2)
        self.horizontalLayout_21.addWidget(self.frame_2)
        self.stackedWidget.addWidget(self.settings_page)
        self.horizontalLayout_3.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.data_view_frame)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.horizontalLayout.addWidget(self.main_frame)
        self.horizontalLayout.setStretch(0, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(3)
        self.graphs_stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #################################################################################
        try:
                available_ports = QSerialPortInfo.availablePorts()

                if available_ports:
                        for port in available_ports:
                                portName = port.portName()
                                self.comboBox.addItem(portName)
                else:
                        portName = "No available ports"
                        self.comboBox.addItem(portName)
                
        except Exception as e:
                print(e.args)
                print("Error in fetching active comports")
        #################################################################################
        self.w = gl.GLViewWidget()
        self.w.opts['distance'] = 650

        file_path = r"C:\Users\iqras\OneDrive\Documents\Team Sammard\Team_Sammard\SA_CUP_2024\SA_CUP_2024_GUI_Final\SA_CUP_2024-dev_samigang2final\SA_CUP_2024-dev_samigang2\flair_resources_files\Agneya Chamatkar.obj"
        shape_data = load_shape_from_obj(file_path)
        vertices = np.array(shape_data["vertices"])
        faces = np.array(shape_data["faces"])
        self.rocket_mesh = gl.GLMeshItem(vertexes=vertices, faces=faces, drawEdges=True, edgeColor=(1, 1, 1, 1), drawFaces=True, smooth=True)
        self.rocket_mesh.scale(0.1, 0.1, 0.1)
        self.rocket_mesh.translate(0, 0, -100)
        self.w.addItem(self.rocket_mesh)
        axis_length = 200

        x_axis = gl.GLLinePlotItem(pos=np.array([[0, 0, 0], [axis_length, 0, 0]]), color=(1, 0, 0, 1), width=5)
        y_axis = gl.GLLinePlotItem(pos=np.array([[0, 0, 0], [0, axis_length, 0]]), color=(0, 1, 0, 1), width=5)
        z_axis = gl.GLLinePlotItem(pos=np.array([[0, 0, 0], [0, 0, axis_length]]), color=(0, 0, 1, 1), width=5)
        
        self.w.addItem(x_axis)
        self.w.addItem(y_axis)
        self.w.addItem(z_axis)

        self.w.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_37.addWidget(self.w)

        #################################################################################
        ## ALTITUDE
        self.altFig1, self.altAx1 = plt.subplots()
        self.altCanvas1 = FigureCanvas(self.altFig1)        
        self.verticalLayout_31.addWidget(self.altCanvas1)

        self.altFig2, self.altAx2 = plt.subplots()
        self.altCanvas2 = FigureCanvas(self.altFig2) 
        self.verticalLayout_87.addWidget(self.altCanvas2)
        #################################################################################
        ## TEMPERATURE
        # self.tempFig, self.tempAx = plt.subplots()
        # self.tempCanvas = FigureCanvas(self.tempFig)
        # self.verticalLayout_69.addWidget(self.tempCanvas)
        #################################################################################
        ## SPEED
        self.speedFig, self.speedAx = plt.subplots()
        self.speedCanvas = FigureCanvas(self.speedFig)
        self.verticalLayout_81.addWidget(self.speedCanvas)
        #################################################################################
        ## PRESSURE
        self.pressFig1, self.pressAx1 = plt.subplots()
        self.pressCanvas1 = FigureCanvas(self.pressFig1)

        self.pressFig2, self.pressAx2 = plt.subplots()
        self.pressCanvas2 = FigureCanvas(self.pressFig2)        

        self.verticalLayout_33.addWidget(self.pressCanvas1)
        self.verticalLayout_90.addWidget(self.pressCanvas2)
        #################################################################################
        ## VOLTAGE
        self.voltFig1, self.voltAx1 = plt.subplots()
        self.voltCanvas1 = FigureCanvas(self.voltFig1)

        self.voltFig2, self.voltAx2 = plt.subplots()
        self.voltCanvas2 = FigureCanvas(self.voltFig2)

        self.verticalLayout_34.addWidget(self.voltCanvas1)
        self.verticalLayout_94.addWidget(self.voltCanvas2)
        #################################################################################
        ## ACCELEROMETER
        self.accFig, self.accAx = plt.subplots()
        self.accCanvas = FigureCanvas(self.accFig)
        self.verticalLayout_102.addWidget(self.accCanvas)        
        #################################################################################
        ## GYROMETER
        self.gyroFig, self.gyroAx = plt.subplots()
        self.gyroCanvas = FigureCanvas(self.gyroFig)
        self.verticalLayout_98.addWidget(self.gyroCanvas)
        #################################################################################
        ## VELOCITY
        self.velFig, self.velAx = plt.subplots()
        self.velCanvas = FigureCanvas(self.velFig)
        self.verticalLayout_92.addWidget(self.velCanvas)                
        #################################################################################
        ## ALTITUDE VS GPS ALTITUDE
        self.altVgpsaltFig, self.altVgpsaltAx = plt.subplots()
        self.altVgpsaltCanvas = FigureCanvas(self.altVgpsaltFig)
        self.verticalLayout_96.addWidget(self.altVgpsaltCanvas)
        #################################################################################
        ## GPS SPEED VS VELOCITY
        self.gpsspeedVvelFig, self.gpsspeedVvelAx = plt.subplots()
        self.gpsspeedVvelCanvas = FigureCanvas(self.gpsspeedVvelFig)
        self.verticalLayout_100.addWidget(self.gpsspeedVvelCanvas)
        #################################################################################
        self.stackedWidget.setCurrentIndex(0)
        #################################################################################
        ## TOP PANEL
        self.host_connect_btn = HostConnectButton(self.host_connect_button, self.host_disconnect_button, self.flight_file_upload_button, self.flight_data_export_button, self.data_upload_button, self.stackedWidget, 
                                                  self.Tab1_btn, self.Tab2_btn, self.Tab3_btn, self.Tab4_btn,
                                                  self.graphs_stackedWidget, 
                                                  self.RSSI_value, #new
                                                  self.hp_temperature_disp, #new
                                                  self.packet_count_text, self.mission_time_text, 
                                                  self.hp_alt_label, self.notif_alt_label, 
                                                  self.hp_gpsSpeed_label, 
                                                  self.accelerometer_value_x, self.accelerometer_value_y, self.accelerometer_value_z,
                                                  self.hp_pressure_label, self.hp_voltage_label, 
                                                  self.gyrometer_value_x, self.gyrometer_value_y, self.gyrometer_value_z,
                                                  self.pitch, self.yaw, self.roll,
                                                  self.GPS_hp_lat, self.GPS_hp_lon, self.gps_heading_disp, self.SATS_value, #gps_heading_disp -> new
                                                  self.table_data_csv_display, 
                                                  self.notif_press_label, 
                                                  self.notif_velocity_label,
                                                  self.notif_voltage_label,
                                                  self.notif_Velocity_label, #new
                                                  self.notif_GPSspeed_label, #new
                                                  self.notif_alt_label_2, #new
                                                  self.notif_GPSalt_label, #new
                                                  self.notif_gyro_label, 
                                                  self.notif_acc_label, #new
                                                  self.gps_heading_label, self.mag_heading_label, 
                                                  self.GPS_SATSno_label, self.GPS_lat_label, self.GPS_lon_label, 
                                                  self.GPS_altitude_label, self.GPS_speed_label, 
                                                  self.altAx1, self.altCanvas1, self.altAx2, self.altCanvas2, 
                                                  self.speedAx, self.speedCanvas, 
                                                  self.pressAx1, self.pressCanvas1, self.pressAx2, self.pressCanvas2, 
                                                  self.voltAx1, self.voltCanvas1, self.voltAx2, self.voltCanvas2, 
                                                  self.accAx, self.accCanvas, 
                                                  self.gyroAx, self.gyroCanvas, 
                                                  self.velAx, self.velCanvas, 
                                                  self.altVgpsaltAx, self.altVgpsaltCanvas, 
                                                  self.gpsspeedVvelAx, self.gpsspeedVvelCanvas,
                                                  self.download_file_btn, self.trigger_value,
                                                  self.map_display, self.map_display_GPS_page, 
                                                  self.horizontalLayout_31, self.horizontalLayout_35, self.altitude_label_graphs_sidepanel, self.velocity_label_graphs_sidepanel, self.temperature_label_graphs_sidepanel, self.acc_x_label_graphs_sidepanel, self.acc_y_label_graphs_sidepanel, self.acc_z_label_graphs_sidepanel, self.gyro_x_label_graphs_sidepanel, self.gyro_y_label_graphs_sidepanel, self.gyro_z_label_graphs_sidepanel,
                                                  self.rocket_mesh, self.w,
                                                  self.pitch_label_rkt, self.yaw_label_pkt, self.roll_label_rkt,
                                                  self.acc_x_rkt, self.acc_y_rkt, self.acc_z_rkt,
                                                  self.gyro_x_rkt, self.gyro_y_rkt, self.gyro_z_rkt,
                                                  portName = portName)

        self.flight_file_upload_btn = FlightFileUploadButton(self.flight_file_upload_button, self.stackedWidget,
                                                  self.graphs_stackedWidget, 
                                                  self.RSSI_value, #new
                                                  self.hp_temperature_disp, #new
                                                  self.packet_count_text, self.mission_time_text, 
                                                  self.hp_alt_label, self.notif_alt_label, 
                                                  self.hp_gpsSpeed_label, 
                                                  self.accelerometer_value_x, self.accelerometer_value_y, self.accelerometer_value_z,
                                                  self.hp_pressure_label, self.hp_voltage_label, 
                                                  self.gyrometer_value_x, self.gyrometer_value_y, self.gyrometer_value_z,
                                                  self.pitch, self.yaw, self.roll,
                                                  self.GPS_hp_lat, self.GPS_hp_lon, self.gps_heading_disp, self.SATS_value, 
                                                  self.table_data_csv_display, 
                                                  self.notif_press_label, 
                                                  self.notif_velocity_label,
                                                  self.notif_voltage_label,
                                                  self.notif_Velocity_label, 
                                                  self.notif_GPSspeed_label, 
                                                  self.notif_alt_label_2, 
                                                  self.notif_GPSalt_label, 
                                                  self.notif_gyro_label, 
                                                  self.notif_acc_label, 
                                                  self.gps_heading_label, self.mag_heading_label, 
                                                  self.GPS_SATSno_label, self.GPS_lat_label, self.GPS_lon_label, 
                                                  self.GPS_altitude_label, self.GPS_speed_label, 
                                                  self.altAx1, self.altCanvas1, self.altAx2, self.altCanvas2, 
                                                  self.speedAx, self.speedCanvas, 
                                                  self.pressAx1, self.pressCanvas1, self.pressAx2, self.pressCanvas2, 
                                                  self.voltAx1, self.voltCanvas1, self.voltAx2, self.voltCanvas2, 
                                                  self.accAx, self.accCanvas, 
                                                  self.gyroAx, self.gyroCanvas, 
                                                  self.velAx, self.velCanvas, 
                                                  self.altVgpsaltAx, self.altVgpsaltCanvas, 
                                                  self.gpsspeedVvelAx, self.gpsspeedVvelCanvas,
                                                  self.trigger_value,
                                                  self.map_display, self.map_display_GPS_page, 
                                                  self.horizontalLayout_31, self.horizontalLayout_35, self.altitude_label_graphs_sidepanel, self.velocity_label_graphs_sidepanel, self.temperature_label_graphs_sidepanel, self.acc_x_label_graphs_sidepanel, self.acc_y_label_graphs_sidepanel, self.acc_z_label_graphs_sidepanel, self.gyro_x_label_graphs_sidepanel, self.gyro_y_label_graphs_sidepanel, self.gyro_z_label_graphs_sidepanel)

        self.data_upload_btn = DataUploadButton(self.data_upload_button, 
                                                self.altAx1, self.altCanvas1, self.altAx2, self.altCanvas2,
                                                self.speedAx, self.speedCanvas,
                                                self.pressAx1, self.pressCanvas1, self.pressAx2, self.pressCanvas2,
                                                self.voltAx1, self.voltCanvas1, self.voltAx2, self.voltCanvas2,
                                                # self.tempAx, self.tempCanvas,
                                                self.accAx, self.accCanvas,
                                                self.gyroAx, self.gyroCanvas,
                                                self.velAx, self.velCanvas,
                                                self.altVgpsaltAx, self.altVgpsaltCanvas,
                                                self.gpsspeedVvelAx, self.gpsspeedVvelCanvas,self.RSSI_value, 
                                                self.hp_temperature_disp, 
                                                self.packet_count_text, self.mission_time_text, 
                                                self.hp_alt_label, self.notif_alt_label, 
                                                self.hp_gpsSpeed_label, 
                                                self.accelerometer_value_x, self.accelerometer_value_y, self.accelerometer_value_z,
                                                self.hp_pressure_label, self.hp_voltage_label, 
                                                self.gyrometer_value_x, self.gyrometer_value_y, self.gyrometer_value_z,
                                                self.pitch, self.yaw, self.roll,
                                                self.GPS_hp_lat, self.GPS_hp_lon, self.gps_heading_disp, self.SATS_value, 
                                                self.table_data_csv_display, 
                                                self.notif_press_label, 
                                                self.notif_velocity_label,
                                                self.notif_voltage_label,
                                                self.notif_Velocity_label, 
                                                self.notif_GPSspeed_label, 
                                                self.notif_alt_label_2, 
                                                self.notif_GPSalt_label, 
                                                self.notif_gyro_label, 
                                                self.notif_acc_label, 
                                                self.GPS_SATSno_label, self.GPS_lat_label, self.GPS_lon_label, 
                                                self.GPS_altitude_label, self.GPS_speed_label, self.altitude_label_graphs_sidepanel, self.velocity_label_graphs_sidepanel, self.temperature_label_graphs_sidepanel, self.acc_x_label_graphs_sidepanel, self.acc_y_label_graphs_sidepanel, self.acc_z_label_graphs_sidepanel, self.gyro_x_label_graphs_sidepanel, self.gyro_y_label_graphs_sidepanel, self.gyro_z_label_graphs_sidepanel, self.gps_heading_label, self.mag_heading_label, self.trigger_value)
        
        self.flight_file_export_btn = FlightFileExportButton(self.flight_data_export_button)
        
        self.clear_graphs_btn = ClearGraphsButton(self.pushButton, self.altAx1, self.altAx2, self.speedAx, 
                                                  self.pressAx1, self.pressAx2, 
                                                  self.voltAx1, self.voltAx2, 
                                                  self.accAx, 
                                                  self.gyroAx, 
                                                  self.velAx, 
                                                  self.altVgpsaltAx, 
                                                  self.gpsspeedVvelAx,
                                                  self.rocket_mesh)
        ## SIDE PANEL
        self.sidePanel_button_module = sidePanelButtonModule(self.stackedWidget,
                                          self.home_button, self.graphs_button, self.GPS_button, self.tabledata_button, self.settings_button, self.rkt_model_button,
                                          self.home_button_frame, self.graphs_button_frame, self.GPS_button_frame, self.tabledata_button_frame, self.settings_button_frame, self.RKTmodel_button_frame)
                                          
        ## SETTINGS PAGE
        self.settings = SettingsModule(self.browse_for_folders_btn, self.data_file_folder_name,
                                       self.apply_all_changes, 
                                       self.vel_mph, self.vel_kmph,
                                       self.tempC, self.tempF,
                                       self.Alt_feet, self.Alter_meters,
                                       self.gyro_dps, self.gyro_rps,
                                       self.eulers_deg, self.eulers_rad,
                                       self.GPS_alt_feet, self.GPS_alt_meters,
                                       self.GPS_speed_mph, self.GPS_speed_kmph,
                                       self.acc_fps, self.acc_mps)
        #################################################################################
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.teamID.setText(_translate("MainWindow", "TEAM ID: 145"))
        self.mission_time_label.setText(_translate("MainWindow", "MISSION TIME"))
        self.packet_count_label.setText(_translate("MainWindow", "PACKET COUNT"))
        self.trigger_value.setMarkdown(_translate("MainWindow", "**TRIGGER:**\n"
"\n"
""))
        self.trigger_value.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:8px; margin-bottom:8px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">TRIGGER:</p></body></html>"))
        self.team_logo.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/team_logo/team_label.png\"/></p></body></html>"))
        self.team_logo_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/team_logo/FLAIR_LOGO.png\"/></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "×"))
        self.hp_alt_label.setText(_translate("MainWindow", "ALTITUDE:"))
        self.hp_gpsSpeed_label.setText(_translate("MainWindow", "GPS SPEED:"))
        self.hp_pressure_label.setText(_translate("MainWindow", "PRESSURE: "))
        self.hp_voltage_label.setText(_translate("MainWindow", "VOLTAGE: "))
        self.label_37.setText(_translate("MainWindow", "ACCELEROMETER"))
        self.label_45.setText(_translate("MainWindow", "X:"))
        self.label_47.setText(_translate("MainWindow", "Y:"))
        self.label_46.setText(_translate("MainWindow", "Z:"))
        self.accelerometer_value_x.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_38.setText(_translate("MainWindow", "GYROSCOPE"))
        self.label_54.setText(_translate("MainWindow", "X:"))
        self.label_55.setText(_translate("MainWindow", "Y:"))
        self.label_56.setText(_translate("MainWindow", "Z:"))
        self.label_39.setText(_translate("MainWindow", "EULER\'S ANGLE"))
        self.label_57.setText(_translate("MainWindow", "Pitch:"))
        self.label_58.setText(_translate("MainWindow", "Yaw:"))
        self.label_59.setText(_translate("MainWindow", "Roll:"))
        self.label_40.setText(_translate("MainWindow", "RSSI"))
        self.RSSI_value.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:36pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">n/a</p></body></html>"))
        self.label_48.setText(_translate("MainWindow", "GPS COORDINATES"))
        self.GPS_hp_lat.setText(_translate("MainWindow", "Lat:"))
        self.GPS_hp_lon.setText(_translate("MainWindow", "Lon:"))
        self.label_51.setText(_translate("MainWindow", "TEMPERATURE (C)"))
        self.hp_temperature_disp.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:36pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">n/a</p></body></html>"))
        self.label_43.setText(_translate("MainWindow", "COURSE (GPS)"))
        self.gps_heading_disp.setMarkdown(_translate("MainWindow", "n/a\n"
"\n"
""))
        self.gps_heading_disp.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:22pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:14px; margin-bottom:14px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">n/a</p></body></html>"))
        self.label_44.setText(_translate("MainWindow", "SATS"))
        self.SATS_value.setMarkdown(_translate("MainWindow", "n/a\n"
"\n"
""))
        self.SATS_value.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:36pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:24px; margin-bottom:24px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">n/a</p></body></html>"))
        self.Tab1_btn.setText(_translate("MainWindow", "TAB-1"))
        self.Tab2_btn.setText(_translate("MainWindow", "TAB-2"))
        self.Tab3_btn.setText(_translate("MainWindow", "TAB-3"))
        self.Tab4_btn.setText(_translate("MainWindow", "TAB-4"))
        self.notif_alt_label.setText(_translate("MainWindow", "ALTITUDE:"))
        self.notif_press_label.setText(_translate("MainWindow", "PRESSURE:"))
        self.notif_voltage_label.setText(_translate("MainWindow", "VOLTAGE:"))
        self.notif_velocity_label.setText(_translate("MainWindow", "VELOCITY:"))
        self.notif_Velocity_label.setText(_translate("MainWindow", "VELOCITY:"))
        self.notif_GPSspeed_label.setText(_translate("MainWindow", "GPS SPEED: "))
        self.notif_alt_label_2.setText(_translate("MainWindow", "ALTITUDE:"))
        self.notif_GPSalt_label.setText(_translate("MainWindow", "GPS ALTITUDE:"))
        self.label_2.setText(_translate("MainWindow", "GYROSCOPE:"))
        self.notif_gyro_label.setText(_translate("MainWindow", "X, Y, Z"))
        self.label_3.setText(_translate("MainWindow", "ACCELEROMETER:"))
        self.notif_acc_label.setText(_translate("MainWindow", "X, Y, Z"))
        self.label_27.setText(_translate("MainWindow", "FLIGHT DATA"))
        self.label_31.setText(_translate("MainWindow", "GPS DATA"))
        self.GPS_SATSno_label.setText(_translate("MainWindow", "SATS NO.:"))
        self.GPS_lat_label.setText(_translate("MainWindow", "LATITUDE:"))
        self.GPS_lon_label.setText(_translate("MainWindow", "LONGITUDE:"))
        self.GPS_altitude_label.setText(_translate("MainWindow", "ALTITUDE:"))
        self.GPS_speed_label.setText(_translate("MainWindow", "SPEED:"))
        self.gps_heading_label.setText(_translate("MainWindow", "(L)GPS HEADING:"))
        self.mag_heading_label.setText(_translate("MainWindow", "(R)MAG HEADING:"))
        self.label_28.setText(_translate("MainWindow", "FLIGHT DATA"))
        item = self.table_data_csv_display.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "time_stamp"))
        item = self.table_data_csv_display.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "PKT"))
        item = self.table_data_csv_display.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "MISSION_TIME"))
        item = self.table_data_csv_display.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "ALTITUDE (Feet(AGL))"))
        item = self.table_data_csv_display.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "PRESSURE (Pascal)"))
        item = self.table_data_csv_display.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "TEMPERATURE (C)"))
        item = self.table_data_csv_display.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "GPS_LATITUDE"))
        item = self.table_data_csv_display.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "GPS_LONGITUDE"))
        item = self.table_data_csv_display.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "GPS_ALTITUDE (Feet(AGL))"))
        item = self.table_data_csv_display.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "GPS_SPEED (m/h)"))
        item = self.table_data_csv_display.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "GPS_HEADING (deg)"))
        item = self.table_data_csv_display.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "GPS_TIME"))
        item = self.table_data_csv_display.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "GPS_DATE"))
        item = self.table_data_csv_display.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "GPS_SATS"))
        item = self.table_data_csv_display.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "ACCELERATION_X (ft/s sq)"))
        item = self.table_data_csv_display.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "ACCELERATION_Y (ft/s sq)"))
        item = self.table_data_csv_display.horizontalHeaderItem(16)
        item.setText(_translate("MainWindow", "ACCELERATION_Z (ft/s sq)"))
        item = self.table_data_csv_display.horizontalHeaderItem(17)
        item.setText(_translate("MainWindow", "GYRO_X (deg/s)"))
        item = self.table_data_csv_display.horizontalHeaderItem(18)
        item.setText(_translate("MainWindow", "GYRO_Y (deg/s)"))
        item = self.table_data_csv_display.horizontalHeaderItem(19)
        item.setText(_translate("MainWindow", "GYRO_Z (deg/s)"))
        item = self.table_data_csv_display.horizontalHeaderItem(20)
        item.setText(_translate("MainWindow", "VELOCITY (m/h)"))
        item = self.table_data_csv_display.horizontalHeaderItem(21)
        item.setText(_translate("MainWindow", "PITCH (deg)"))
        item = self.table_data_csv_display.horizontalHeaderItem(22)
        item.setText(_translate("MainWindow", "YAW (deg)"))
        item = self.table_data_csv_display.horizontalHeaderItem(23)
        item.setText(_translate("MainWindow", "ROLL (deg)"))
        item = self.table_data_csv_display.horizontalHeaderItem(24)
        item.setText(_translate("MainWindow", "MAGNETOMETER_HEADING (deg)"))
        item = self.table_data_csv_display.horizontalHeaderItem(25)
        item.setText(_translate("MainWindow", "VOLTAGE (Volts)"))
        item = self.table_data_csv_display.horizontalHeaderItem(26)
        item.setText(_translate("MainWindow", "FLIGHT_STATE"))
        item = self.table_data_csv_display.horizontalHeaderItem(27)
        item.setText(_translate("MainWindow", "TRIGGER"))
        item = self.table_data_csv_display.horizontalHeaderItem(28)
        item.setText(_translate("MainWindow", "RSSI"))
        self.label_22.setText(_translate("MainWindow", "Euler\'s Angle Units"))
        self.eulers_deg.setText(_translate("MainWindow", "Degrees (°)"))
        self.eulers_rad.setText(_translate("MainWindow", "Radian (Rad)"))
        self.label_24.setText(_translate("MainWindow", "GPS Speed Units"))
        self.GPS_speed_mph.setText(_translate("MainWindow", "Miles per hour (m/h)"))
        self.GPS_speed_kmph.setText(_translate("MainWindow", "Kilometers per hour (km/h)"))
        self.label_23.setText(_translate("MainWindow", "GPS Altitude Units"))
        self.GPS_alt_feet.setText(_translate("MainWindow", "Feet (AGL)"))
        self.GPS_alt_meters.setText(_translate("MainWindow", "Meters (AGL)"))
        self.label_19.setText(_translate("MainWindow", "Gyrometer Units"))
        self.gyro_dps.setText(_translate("MainWindow", "Degrees per second (°/s)"))
        self.gyro_rps.setText(_translate("MainWindow", "Radian per second (rad/s)"))
        self.label_25.setText(_translate("MainWindow", "Accelerometer Units"))
        self.acc_fps.setText(_translate("MainWindow", " Feet per second squared (ft/s²)"))
        self.acc_mps.setText(_translate("MainWindow", " Meters per second squared (m/s²)"))
        self.label_14.setText(_translate("MainWindow", "Velocity Units"))
        self.vel_mph.setText(_translate("MainWindow", "Miles per hour (m/h)"))
        self.vel_kmph.setText(_translate("MainWindow", "Kilometers per hour (km/h)"))
        self.label_15.setText(_translate("MainWindow", "Temperature Units"))
        self.tempC.setText(_translate("MainWindow", "°C"))
        self.tempF.setText(_translate("MainWindow", "°F"))
        self.label_16.setText(_translate("MainWindow", "Altitude Units"))
        self.Alt_feet.setText(_translate("MainWindow", "Feet (AGL)"))
        self.Alter_meters.setText(_translate("MainWindow", "Meters (AGL)"))
        self.apply_all_changes.setText(_translate("MainWindow", "APPLY ALL CHANGES"))
        self.download_file_btn.setText(_translate("MainWindow", "DOWNLOAD FILE"))
        self.label_21.setText(_translate("MainWindow", "Default Data File Folder"))
        self.data_file_folder_name.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.browse_for_folders_btn.setText(_translate("MainWindow", "Browse for Folder"))
        self.label_17.setText(_translate("MainWindow", "Comm Link"))
        self.label_18.setText(_translate("MainWindow", "Active Comm Port"))


def load_shape_from_obj(file_path):
    try:
        vertices = []
        faces = []
        with open(file_path) as f:
            for line in f:
                parts = line.strip().split()
                if not parts:
                    continue
                if parts[0] == "v":
                    vertex = list(map(float, parts[1:4]))  # Take only x, y, z components
                    vertices.append(vertex)
                elif parts[0] == "f":
                    face = [int(part.split('/')[0]) - 1 for part in parts[1:4]]  # Convert to 0-based index
                    faces.append(face)

        shape_data = {"vertices": vertices, "faces": faces}

        return shape_data

    except FileNotFoundError:
        print(f"{file_path} not found.")

def get_run_counter():
      with open(r"C:\Users\iqras\OneDrive\Documents\Team Sammard\Team_Sammard\SA_CUP_2024\SA_CUP_2024_GUI_Final\SA_CUP_2024-dev_samigang2final\SA_CUP_2024-dev_samigang2\TABLE_DATA_PAGE\counter.txt", "r") as f:
            counter = int(f.read().strip())

      return counter

def update_counter(counter):
      with open(r"C:\Users\iqras\OneDrive\Documents\Team Sammard\Team_Sammard\SA_CUP_2024\SA_CUP_2024_GUI_Final\SA_CUP_2024-dev_samigang2final\SA_CUP_2024-dev_samigang2\TABLE_DATA_PAGE\counter.txt", "w") as f:
            f.write(str(counter))

if __name__ == "__main__":
    counter = get_run_counter()
    counter += 1
    update_counter(counter)
    print(f"RUN COUNT: {counter}")
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
