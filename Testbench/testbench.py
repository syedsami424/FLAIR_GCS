import serial
import serial.tools.list_ports
import re

# data = ["b'952", 'hh:mm:ss', '1264.600', '2435.300', '27.90', '-1.04', '-130.31', '3559.800', '443.300', 'gps_HEADING', 'hh:mm:ss', 'dd/mm/yyyy', '14', '3.92', '1.06', '7.98', '25.40', '10.75', '-9.78', '2475.800', '-56.90', '162.78', '78.79', 'magnetometer heading', '3.39', '1.00', '0000', "3162\\r\\n'"]

# filtered_data = [re.sub(r"['b\\\\r\\n]", "", item) for item in data]

# print(filtered_data)

# from datetime import datetime
# import time

# import time
# start_time = time.time()

# try:
#     while True:
#         elapsed_time = time.time() - start_time
#         formatted_time = float(f"{elapsed_time:.2f}")
#         print(type(formatted_time))
#         # print(formatted_time, end='\r')
        
#         # time.sleep(0.01)
# except KeyboardInterrupt:
#     print("\nStopwatch stopped.")

# line = "b'X,magnetometer heading\r\n'"
# line = re.sub(r"b|'|\\r|\\n", "", line)
# print(line)

# print()

# a = str(None)
# print(type(a))
# print()

# packet_structure = r"^(A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|AB|BC),[^,\s]+$"
# value_structure = 

# pkt = "BC,-7882.600"
# if (re.match(packet_structure,pkt)):
#     print("match")
# else:
#     print("no match")
import sys
import io
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# ser1 = serial.Serial('COM3', 115200)
# data_dict = {
#     "A": [], "B": [], "C": [], "D": [], "E": [], "F": [], "G": [],
#     "H": [], "I": [], "J": [], "K": [], "L": [], "M": [], "N": [],
#     "O": [], "P": [], "Q": [], "R": [], "S": [], "T": [], "U": [],
#     "V": [], "W": [], "X": [], "Y": [], "Z": [], "AB": [], "BC": [],
#     "GARBAGE": []
# }
# counter = 0
# total_keys = len(data_dict)

# while True:
#     try:
#         data = ser1.readline()
#         data = str(data)
#         line = data.strip()
#         line = re.sub(r"b|'|\\r|\\n", "", line)
#         line = line.split(",", 1)
#         # print(line)

#         if (len(line) < 2) :
#             data_dict["GARBAGE"].append(line)
#             # print(data_dict["GARBAGE"][-1])
#         else:
    
#             value_ID = line[0]
#             value = line[1]
#             # print(line)
#             if (value_ID not in data_dict) or (value == ""):
#                 data_dict["GARBAGE"].append(value)
#                 # print(data_dict["GARBAGE"][-1])

#             data_dict[value_ID].append(value)

        
#         counter += 1

#         if counter == total_keys:
#             pkt_count = data_dict["A"][-1] if data_dict["A"] else ""
#             mission_time = data_dict["B"][-1] if data_dict["B"] else ""
#             altitude = data_dict["C"][-1] if data_dict["C"] else ""
#             pressure = data_dict["D"][-1] if data_dict["D"] else ""
#             temperature = data_dict["E"][-1] if data_dict["E"] else ""
#             gps_lat = data_dict["F"][-1] if data_dict["F"] else ""
#             gps_lon = data_dict["G"][-1] if data_dict["G"] else ""
#             gps_altitude = data_dict["H"][-1] if data_dict["H"] else ""
#             gps_speed = data_dict["I"][-1] if data_dict["I"] else ""
#             gps_heading = data_dict["J"][-1] if data_dict["J"] else ""
#             gps_time = data_dict["K"][-1] if data_dict["K"] else ""
#             gps_date = data_dict["L"][-1] if data_dict["L"] else ""
#             gps_SATS = data_dict["M"][-1] if data_dict["M"] else ""
#             acc_x = data_dict["N"][-1] if data_dict["N"] else ""
#             acc_y = data_dict["O"][-1] if data_dict["O"] else ""
#             acc_z = data_dict["P"][-1] if data_dict["P"] else ""
#             gyro_x = data_dict["Q"][-1] if data_dict["Q"] else ""
#             gyro_y = data_dict["R"][-1] if data_dict["R"] else ""
#             gyro_z = data_dict["S"][-1] if data_dict["S"] else ""
#             velocity = data_dict["T"][-1] if data_dict["T"] else ""
#             pitch = data_dict["U"][-1] if data_dict["U"] else ""
#             yaw = data_dict["V"][-1] if data_dict["V"] else ""
#             roll = data_dict["W"][-1] if data_dict["W"] else ""
#             mag_heading = data_dict["X"][-1] if data_dict["X"] else ""
#             voltage = data_dict["Y"][-1] if data_dict["Y"] else ""
#             flight_state = data_dict["Z"][-1] if data_dict["Z"] else ""
#             trigger = data_dict["AB"][-1] if data_dict["AB"] else ""
#             rssi = data_dict["BC"][-1] if data_dict["BC"] else ""

#             garbage = data_dict["GARBAGE"]
                
#             line_str = f"{pkt_count}team_sammardʘpacket_sepʘteam_sammard{mission_time}team_sammardʘpacket_sepʘteam_sammard{altitude}team_sammardʘpacket_sepʘteam_sammard{pressure}team_sammardʘpacket_sepʘteam_sammard{temperature}team_sammardʘpacket_sepʘteam_sammard{gps_lat}team_sammardʘpacket_sepʘteam_sammard{gps_lon}team_sammardʘpacket_sepʘteam_sammard{gps_altitude}team_sammardʘpacket_sepʘteam_sammard{gps_speed}team_sammardʘpacket_sepʘteam_sammard{gps_heading}team_sammardʘpacket_sepʘteam_sammard{gps_time}team_sammardʘpacket_sepʘteam_sammard{gps_date}team_sammardʘpacket_sepʘteam_sammard{gps_SATS}team_sammardʘpacket_sepʘteam_sammard{acc_x}team_sammardʘpacket_sepʘteam_sammard{acc_y}team_sammardʘpacket_sepʘteam_sammard{acc_z}team_sammardʘpacket_sepʘteam_sammard{gyro_x}team_sammardʘpacket_sepʘteam_sammard{gyro_y}team_sammardʘpacket_sepʘteam_sammard{gyro_z}team_sammardʘpacket_sepʘteam_sammard{velocity}team_sammardʘpacket_sepʘteam_sammard{pitch}team_sammardʘpacket_sepʘteam_sammard{yaw}team_sammardʘpacket_sepʘteam_sammard{roll}team_sammardʘpacket_sepʘteam_sammard{mag_heading}team_sammardʘpacket_sepʘteam_sammard{voltage}team_sammardʘpacket_sepʘteam_sammard{flight_state}team_sammardʘpacket_sepʘteam_sammard{trigger}team_sammardʘpacket_sepʘteam_sammard{rssi}"
#             line = line_str.strip().split("team_sammardʘpacket_sepʘteam_sammard")

#             # line_str = f"{pkt_count}<==packet_sep==>{mission_time}<==packet_sep==>{altitude}<==packet_sep==>{pressure}<==packet_sep==>{temperature}<==packet_sep==>{gps_lat}<==packet_sep==>{gps_lon}<==packet_sep==>{gps_altitude}<==packet_sep==>{gps_speed}<==packet_sep==>{gps_heading}<==packet_sep==>{gps_time}<==packet_sep==>{gps_date}<==packet_sep==>{gps_SATS}<==packet_sep==>{acc_x}<==packet_sep==>{acc_y}<==packet_sep==>{acc_z}<==packet_sep==>{gyro_x}<==packet_sep==>{gyro_y}<==packet_sep==>{gyro_z}<==packet_sep==>{velocity}<==packet_sep==>{pitch}<==packet_sep==>{yaw}<==packet_sep==>{roll}<==packet_sep==>{mag_heading}<==packet_sep==>{voltage}<==packet_sep==>{flight_state}<==packet_sep==>{trigger}<==packet_sep==>{rssi}"
#             # line = line_str.strip().split("<==packet_sep==>")

#             print(line)
#             counter = 0
#     except (Exception, UnicodeEncodeError) as e:
#         print(e.args)



# l = ['PKT_COUNT', 'MISSION_TIME', 'ALTITUDE', 'PRESSURE', 'TEMPERATURE', 'GPS_LATITUDE', 'GPS_LONGITUDE', 'GPS_ALTITUDE', 'GPS_SPEED', 'GPS_HEADING', 'GPS_TIME', 'GPS_DATE', 'GPS_SATS', 'ACCELERATION_X', 'ACCELERATION_Y', 'ACCELERATION_Z', 'GYRO_X', 'GYRO_Y', 'GYRO_Z', 'VELOCITY', 'PITCH', 'YAW', 'ROLL', 'MAGNETOMETER_HEADING', 'VOLTAGE', 'FLIGHT_STATE', 'RSSI']
# print(len(l))
        
# port_data = serial.tools.list_ports.comports()

# if len(port_data) == 0:
#     print("Make sure ESP is connected")
# else:
#     print(port_data)
#     print("hello")

# import sys
# from PyQt5.QtWidgets import QApplication, QDial, QWidget, QVBoxLayout
# from PyQt5.QtGui import QPainter, QFont, QPen, QBrush
# from PyQt5.QtCore import Qt, QPoint

# class CompassDial(QDial):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setMinimum(0)
#         self.setMaximum(360)
#         self.setNotchesVisible(False)

#     def paintEvent(self, event):
#         painter = QPainter(self)
#         painter.setRenderHint(QPainter.Antialiasing)

#         # Draw the dial background
#         rect = self.rect()
#         painter.setBrush(QBrush(Qt.white))
#         painter.setPen(QPen(Qt.black, 2))
#         painter.drawEllipse(rect)

#         # Draw the direction labels
#         directions = {0: "N", 45: "NE", 90: "E", 135: "SE", 180: "S",
#                       225: "SW", 270: "W", 315: "NW"}
#         font = QFont(self.font())
#         font.setPointSize(10)
#         painter.setFont(font)
        
#         for angle, label in directions.items():
#             painter.save()
#             painter.translate(rect.center())
#             painter.rotate(-angle)
#             painter.drawText(-10, -rect.height() // 2 + 10, 20, 20, Qt.AlignCenter, label)
#             painter.restore()

#         # Draw the needle
#         painter.save()
#         painter.translate(rect.center())
#         painter.rotate(-self.value())
#         needle = [QPoint(0, -rect.height() // 2 + 10), QPoint(5, 0), QPoint(-5, 0)]
#         painter.setBrush(QBrush(Qt.red))
#         painter.drawPolygon(*needle)
#         painter.restore()

# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('Compass Dial')
#         self.setGeometry(100, 100, 300, 300)

#         layout = QVBoxLayout()
#         self.compass_dial = CompassDial(self)
#         layout.addWidget(self.compass_dial)
#         self.setLayout(layout)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
# from PyQt5.QtGui import QPainter, QBrush, QColor, QPen, QPainterPath
# from PyQt5.QtCore import Qt, QRectF, QTimer


# class Speedometer(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.speed = 0
#         self.speed_increment = 5  # Speed increment value
#         self.setMinimumSize(200, 200)
#         self.setWindowTitle('Speedometer')
#         self.timer = QTimer(self)
#         # self.timer.timeout.connect(self.update_speed)
#         # self.timer.start(00)  # Update every second

#     def paintEvent(self, event):
#         painter = QPainter(self)
#         painter.setRenderHint(QPainter.Antialiasing)

#         side = min(self.width(), self.height())
#         painter.setViewport((self.width() - side) // 2, (self.height() - side) // 2, side, side)
#         painter.setWindow(-100, -100, 200, 200)

#         painter.setBrush(QBrush(Qt.blue))
#         painter.setPen(QPen(Qt.black, 2))

#         # Draw the outer circle
#         painter.drawEllipse(-90, -90, 180, 180)

#         # Draw the inner circle
#         painter.setBrush(QBrush(Qt.white))
#         painter.drawEllipse(-80, -80, 160, 160)

#         # Draw the speedometer needle
#         painter.setBrush(QBrush(Qt.red))
#         painter.setPen(QPen(Qt.red, 4))
#         painter.save()
#         painter.rotate(-135 + 2.7 * self.speed)  # 2.7 is the angle per km/h

#         path = QPainterPath()
#         path.moveTo(0, 0)
#         path.lineTo(-3, -70)
#         path.lineTo(3, -70)
#         path.lineTo(0, 0)
#         painter.drawPath(path)
#         painter.restore()

#     def update_speed(self):
#         self.speed += self.speed_increment
#         if self.speed > 200:  # Reset speed when it reaches 200 km/h
#             self.speed = 0
#         self.update()


# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle('Speedometer Example')
#         self.setGeometry(100, 100, 300, 300)

#         layout = QVBoxLayout()
#         self.speedometer = Speedometer()
#         layout.addWidget(self.speedometer)
#         self.setLayout(layout)

#         self.speed_label = QLabel('Current Speed: 0 km/h')
#         layout.addWidget(self.speed_label)

#         self.show()

#     def update_speed(self, speed):
#         self.speedometer.set_speed(speed)
#         self.speed_label.setText(f'Current Speed: {speed} km/h')


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     sys.exit(app.exec_())

# import plotly.graph_objects as go

# fig = go.Figure(go.Indicator(
#     domain = {'x': [0, 1], 'y': [0, 1]},
#     value = 450,
#     mode = "gauge+number+delta",
#     title = {'text': "Speed"},
#     delta = {'reference': 380},
#     gauge = {'axis': {'range': [None, 500]},
#              'steps' : [
#                  {'range': [0, 250], 'color': "lightgray"},
#                  {'range': [250, 400], 'color': "gray"}],
#              'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 490}}))

# fig.show()

# import sys
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import QApplication, QWidget
# from PyQt5.QtWidgets import QApplication, QComboBox, QDateEdit, QDateTimeEdit, QDoubleSpinBox, QGroupBox, QHBoxLayout, QLabel, QSpinBox, QTimeEdit, QVBoxLayout, QWidget
# from PyQt5 import QtWidgets, QtCore, QtGui
# # from mainwindow import Ui_MainWindow
# from PyQt5.QtGui import QPainter, QPolygon, QFont, QFontMetricsF, QPen, QPalette, QColor
# from PyQt5.QtCore import QPoint, Qt


# class CompassWidget(QtWidgets.QLabel):

#     def __init__(self, parent):
#         super(CompassWidget, self).__init__(parent)

#         self.setStyleSheet('QFrame {background-color:(239,100,100);}')
#         self.resize(230, 230)
#         self._angle = 0.0
#         self._margins = 10
#         self._pointText = {0: "N", 45: "NE", 90: "E", 135: "SE", 180: "S",
#                            225: "SW", 270: "W", 315: "NW"}

#     def paintEvent(self, event):

#         painter = QPainter()
#         painter.begin(self)
#         painter.setRenderHint(QPainter.Antialiasing)
#         painter.setPen(QColor(168, 34, 3))
#         painter.fillRect(event.rect(), self.palette().brush(QPalette.Window))
#         self.drawMarkings(painter)
#         self.drawNeedle(painter)
#         painter.end()

#     def drawMarkings(self, painter):

#         painter.save()
#         painter.translate(self.width() / 2, self.height() / 2)
#         scale = min((self.width() - self._margins) / 120.0,
#                     (self.height() - self._margins) / 120.0)
#         painter.scale(scale, scale)

#         font = QFont(self.font())
#         font.setPixelSize(10)
#         metrics = QFontMetricsF(font)

#         painter.setFont(font)
#         painter.setPen(self.palette().color(QPalette.Shadow))

#         i = 0
#         while i < 360:
#             if i % 45 == 0:
#                 painter.drawLine(0, -40, 0, -50)
#                 painter.drawText(-metrics.width(self._pointText[i]) / 2.0, -52,
#                                  self._pointText[i])
#             else:
#                 painter.drawLine(0, -45, 0, -50)

#             painter.rotate(15)
#             i += 15

#         painter.restore()

#     def drawNeedle(self, painter):

#         painter.save()
#         painter.translate(self.width() / 2, self.height() / 2)
#         painter.rotate(self._angle)
#         scale = min((self.width() - self._margins) / 120.0,
#                         (self.height() - self._margins) / 120.0)
#         painter.scale(scale, scale)

#         painter.setPen(QPen(Qt.NoPen))
#         painter.setBrush(self.palette().brush(QPalette.Shadow))

#         painter.drawPolygon(
#             QPolygon([QPoint(-10, 0), QPoint(0, -45), QPoint(10, 0),
#             QPoint(0, 45), QPoint(-10, 0)])
#             )

#         painter.setBrush(self.palette().brush(QPalette.Highlight))

#         painter.drawPolygon(
#             QPolygon([QPoint(-5, -25), QPoint(0, -45), QPoint(5, -25),
#             QPoint(0, -30), QPoint(-5, -25)])
#             )

#         painter.restore()

#     #def sizeHint(self):
#     #    return QSize(150, 150)

#     #def angle(self):
#     #    return self._angle

#     def setAngle(self, angle):
#         # print(self._angle)
#         if angle != self._angle:
#             self._angle = angle
#             self.update()


# if __name__ == "__main__":

#     app = QApplication(sys.argv)
    
#     window = QWidget()
#     compass = CompassWidget()
#     spinBox = QSpinBox()
#     spinBox.setRange(0, 359)
#     spinBox.valueChanged.connect(compass.setAngle)
    
#     layout = QVBoxLayout()
#     layout.addWidget(compass)
#     layout.addWidget(spinBox)
#     window.setLayout(layout)
    
#     window.show()
#     sys.exit(app.exec_())

#############################################################################################################
# from PyQt5 import QtCore, QtWidgets
# import pyqtgraph.opengl as gl
# import numpy as np

# app = QtWidgets.QApplication([])
# w = gl.GLViewWidget()
# w.opts['distance'] = 20
# w.show()
# w.setWindowTitle('pyqtgraph example: GLScatterPlotItem')

# g = gl.GLGridItem()
# w.addItem(g)

# # First example is a set of points with pxMode=False
# pos = np.empty((53, 3))
# size = np.empty((53))
# color = np.empty((53, 4))
# pos[0] = (1, 0, 0); size[0] = 0.5; color[0] = (1.0, 0.0, 0.0, 0.5)
# pos[1] = (0, 1, 0); size[1] = 0.2; color[1] = (0.0, 0.0, 1.0, 0.5)
# pos[2] = (0, 0, 1); size[2] = 2./3.; color[2] = (0.0, 1.0, 0.0, 0.5)

# z = 0.5
# d = 6.0
# for i in range(3, 53):
#     pos[i] = (0, 0, z)
#     size[i] = 2./d
#     color[i] = (0.0, 1.0, 0.0, 0.5)
#     z *= 0.5
#     d *= 2.0

# sp1 = gl.GLScatterPlotItem(pos=pos, size=size, color=color, pxMode=False)
# sp1.translate(5, 5, 0)
# w.addItem(sp1)

# # Second example shows a volume of points with rapidly updating color and pxMode=True
# pos = np.random.random(size=(100000, 3))
# pos *= [10, -10, 10]
# pos[0] = (0, 0, 0)
# color = np.ones((pos.shape[0], 4))
# d2 = (pos**2).sum(axis=1)**0.5
# size = np.random.random(size=pos.shape[0])*10
# sp2 = gl.GLScatterPlotItem(pos=pos, color=(1, 1, 1, 1), size=size)
# phase = 0.

# w.addItem(sp2)

# # Third example shows a grid of points with rapidly updating position and pxMode=False
# pos3 = np.zeros((100, 100, 3))
# pos3[:, :, :2] = np.mgrid[:100, :100].transpose(1, 2, 0) * [-0.1, 0.1]
# pos3 = pos3.reshape(10000, 3)
# d3 = (pos3**2).sum(axis=1)**0.5

# sp3 = gl.GLScatterPlotItem(pos=pos3, color=(1, 1, 1, .3), size=0.1, pxMode=False)
# w.addItem(sp3)

# def update():
#     global phase, sp2, d2, sp3, d3, pos3

#     # Update volume colors
#     s = -np.cos(d2*2+phase)
#     color = np.empty((len(d2), 4), dtype=np.float32)
#     color[:, 3] = np.clip(s * 0.1, 0, 1)
#     color[:, 0] = np.clip(s * 3.0, 0, 1)
#     color[:, 1] = np.clip(s * 1.0, 0, 1)
#     color[:, 2] = np.clip(s ** 3, 0, 1)
#     sp2.setData(color=color)
#     phase -= 0.1

#     # Update surface positions and colors
#     z = -np.cos(d3*2+phase)
#     pos3[:, 2] = z
#     color = np.empty((len(d3), 4), dtype=np.float32)
#     color[:, 3] = 0.3
#     color[:, 0] = np.clip(z * 3.0, 0, 1)
#     color[:, 1] = np.clip(z * 1.0, 0, 1)
#     color[:, 2] = np.clip(z ** 3, 0, 1)
#     sp3.setData(pos=pos3, color=color)

# t = QtCore.QTimer()
# t.timeout.connect(update)
# t.start(50)

# if __name__ == '__main__':
#     import sys
#     if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
#         QtWidgets.QApplication.instance().exec_()
#############################################################################################################

# from PyQt5 import QtCore, QtGui, QtWidgets
# import pyqtgraph.opengl as gl
# import numpy as np

# app = QtWidgets.QApplication([])
# w = gl.GLViewWidget()
# w.opts['distance'] = 20
# w.show()
# w.setWindowTitle('Rocket Model Example')

# g = gl.GLGridItem()
# w.addItem(g)

# # Load the rocket model
# meshdata = gl.MeshData.sphere(rows=10, cols=20)  # Example mesh, replace with your rocket model
# rocket = gl.GLMeshItem(meshdata=meshdata, smooth=True, color=(1, 0, 0, 1), shader='shaded', drawEdges=True)
# rocket.translate(0, 0, 0)
# w.addItem(rocket)

# if __name__ == '__main__':
#     import sys
#     if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
#         QtWidgets.QApplication.instance().exec_()




# from PyQt5 import QtCore, QtGui, QtWidgets
# import pyqtgraph.opengl as gl
# import numpy as np
# import pyassimp

# app = QtWidgets.QApplication([])
# w = gl.GLViewWidget()
# w.opts['distance'] = 20
# w.show()
# w.setWindowTitle('Rocket Model Viewer')

# g = gl.GLGridItem()
# w.addItem(g)

# # Function to load a 3D model using pyassimp
# def load_mesh(filename):
#     scene = pyassimp.load(filename)
#     if not scene.meshes:
#         raise ValueError(f"File {filename} does not contain any meshes")
#     mesh = scene.meshes[0]
#     verts = mesh.vertices
#     faces = mesh.faces
#     return verts, faces

# # Load rocket model
# rocket_file = 'path_to_your_rocket_model.obj'  # Replace with the path to your model
# verts, faces = load_mesh(rocket_file)

# # Create the GLMeshItem
# rocket_mesh = gl.GLMeshItem(vertexes=verts, faces=faces, drawEdges=True, edgeColor=(1, 1, 1, 1), drawFaces=True, smooth=False)
# rocket_mesh.scale(0.1, 0.1, 0.1)  # Adjust scaling if needed
# w.addItem(rocket_mesh)

# # Optional: Rotate the rocket model
# rocket_mesh.rotate(90, 1, 0, 0)

# if __name__ == '__main__':
#     import sys
#     if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
#         QtWidgets.QApplication.instance().exec_()



# from PyQt5 import QtCore, QtGui, QtWidgets
# import pyqtgraph.opengl as gl
# import numpy as np

# app = QtWidgets.QApplication([])
# w = gl.GLViewWidget()
# w.opts['distance'] = 20
# w.show()
# w.setWindowTitle('Rocket Model Viewer')

# g = gl.GLGridItem()
# w.addItem(g)

# # Define the rocket body (cylinder)
# body_height = 5
# body_radius = 1
# num_segments = 20

# body_vertices = []
# body_faces = []

# for i in range(num_segments):
#     angle = 2 * np.pi * i / num_segments
#     x = np.cos(angle) * body_radius
#     y = np.sin(angle) * body_radius
#     body_vertices.append([x, y, 0])
#     body_vertices.append([x, y, body_height])

# for i in range(num_segments):
#     next_i = (i + 1) % num_segments
#     body_faces.append([2 * i, 2 * i + 1, 2 * next_i + 1])
#     body_faces.append([2 * i, 2 * next_i + 1, 2 * next_i])

# # Define the rocket nose (cone)
# nose_height = 2
# nose_vertices = [[0, 0, body_height + nose_height]]
# nose_faces = []

# for i in range(num_segments):
#     angle = 2 * np.pi * i / num_segments
#     x = np.cos(angle) * body_radius
#     y = np.sin(angle) * body_radius
#     nose_vertices.append([x, y, body_height])

# for i in range(num_segments):
#     next_i = (i + 1) % num_segments
#     nose_faces.append([0, i + 1, next_i + 1])

# # Combine body and nose vertices and faces
# vertices = np.array(body_vertices + nose_vertices)
# faces = np.array(body_faces + nose_faces)

# # Create the GLMeshItem
# rocket_mesh = gl.GLMeshItem(vertexes=vertices, faces=faces, drawEdges=True, edgeColor=(1, 1, 1, 1), drawFaces=True, smooth=False)
# rocket_mesh.scale(0.1, 0.1, 0.1)  # Adjust scaling if needed
# w.addItem(rocket_mesh)

# # Optional: Rotate the rocket model
# # rocket_mesh.rotate(90, 1, 0, 0)

# if __name__ == '__main__':
#     import sys
#     if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
#         QtWidgets.QApplication.instance().exec_()


# from PyQt5 import QtCore, QtGui, QtWidgets
# import pyqtgraph.opengl as gl
# import numpy as np
# import serial

# app = QtWidgets.QApplication([])

# # Serial communication setup (adjust port and baudrate as needed)
# serial_port = 'COM3'  # Example port, update as per your system
# baud_rate = 115200

# serial_data = serial.Serial(serial_port, baud_rate)

# w = gl.GLViewWidget()
# w.opts['distance'] = 20
# w.show()
# w.setWindowTitle('Rocket Model Viewer')

# g = gl.GLGridItem()
# w.addItem(g)

# # Define the rocket body (cylinder)
# body_height = 5
# body_radius = 1
# num_segments = 20

# body_vertices = []
# body_faces = []
# body_colors = []  # Color array for the cylinder

# # Assign colors to vertices based on their position
# for i in range(num_segments):
#     angle = 2 * np.pi * i / num_segments
#     x = np.cos(angle) * body_radius
#     y = np.sin(angle) * body_radius
#     body_vertices.append([x, y, 0])
#     body_vertices.append([x, y, body_height])

#     # Assign orange color to one side and white to the other side
#     if x >= 0:
#         body_colors.append([1.0, 0.5, 0.0, 1.0])  # Orange color
#     else:
#         body_colors.append([1.0, 1.0, 1.0, 1.0])  # White color

# for i in range(num_segments):
#     next_i = (i + 1) % num_segments
#     body_faces.append([2 * i, 2 * i + 1, 2 * next_i + 1])
#     body_faces.append([2 * i, 2 * next_i + 1, 2 * next_i])

# # Define the rocket nose (cone)
# nose_height = 2
# nose_vertices = [[0, 0, body_height + nose_height]]
# nose_faces = []

# for i in range(num_segments):
#     angle = 2 * np.pi * i / num_segments
#     x = np.cos(angle) * body_radius
#     y = np.sin(angle) * body_radius
#     nose_vertices.append([x, y, body_height])

# for i in range(num_segments):
#     next_i = (i + 1) % num_segments
#     nose_faces.append([0, i + 1, next_i + 1])

# # Combine body and nose vertices and faces
# vertices = np.array(body_vertices + nose_vertices)
# faces = np.array(body_faces + nose_faces)
# colors = np.array(body_colors * 2)  # Duplicate colors for all vertices

# # Create the GLMeshItem
# rocket_mesh = gl.GLMeshItem(vertexes=vertices, faces=faces, vertexColors=colors, drawEdges=True, edgeColor=(1, 1, 1, 1), drawFaces=True, smooth=False)
# rocket_mesh.scale(0.1, 0.1, 0.1)  # Adjust scaling if needed
# w.addItem(rocket_mesh)

# # Optional: Rotate the rocket model
# # rocket_mesh.rotate(90, 1, 0, 0)

# def updateRocketOrientation():
#     global rocket_mesh, serial_data

#     # Read serial data in format "x,y,z"
#     if serial_data.in_waiting > 0:
#         line = serial_data.readline().decode().strip()
#         data = line.split(',')
#         if len(data) == 3:
#             pitch, yaw, roll = map(float, data)
#             # Update rocket orientation based on pitch, yaw, roll
#             rocket_mesh.resetTransform()
#             rocket_mesh.rotate(0, 1, 0, 0)  # Rotate around X-axis (pitch)
#             rocket_mesh.rotate(0, 0, 1, 0)    # Rotate around Y-axis (yaw)
#             rocket_mesh.rotate(roll, 0, 0, 1)   # Rotate around Z-axis (roll)

# t = QtCore.QTimer()
# t.timeout.connect(updateRocketOrientation)
# t.start(500)  # Update orientation every 0 ms

# if __name__ == '__main__':
#     import sys
#     if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
#         QtWidgets.QApplication.instance().exec_()


# from PyQt5 import QtCore, QtGui, QtWidgets
# import pyqtgraph.opengl as gl
# import numpy as np
# import serial

# app = QtWidgets.QApplication([])

# # Serial communication setup (adjust port and baudrate as needed)
# serial_port = 'COM3'  # Example port, update as per your system
# baud_rate = 115200

# serial_data = serial.Serial(serial_port, baud_rate)

# w = gl.GLViewWidget()
# w.opts['distance'] = 20
# w.show()
# w.setWindowTitle('Rocket Model Viewer')

# g = gl.GLGridItem()
# w.addItem(g)

# # Define the rocket body (cylinder)
# body_height = 5
# body_radius = 1
# num_segments = 20

# body_vertices = []
# body_faces = []
# body_colors = []  # Color array for the cylinder

# # Assign colors to vertices based on their position
# for i in range(num_segments):
#     angle = 2 * np.pi * i / num_segments
#     x = np.cos(angle) * body_radius
#     y = np.sin(angle) * body_radius
#     body_vertices.append([x, y, 0])
#     body_vertices.append([x, y, body_height])

#     # Assign orange color to one side and white to the other side
#     if x >= 0:
#         body_colors.append([1.0, 0.5, 0.0, 1.0])  # Orange color
#     else:
#         body_colors.append([1.0, 1.0, 1.0, 1.0])  # White color

# for i in range(num_segments):
#     next_i = (i + 1) % num_segments
#     body_faces.append([2 * i, 2 * i + 1, 2 * next_i + 1])
#     body_faces.append([2 * i, 2 * next_i + 1, 2 * next_i])

# # Define the rocket nose (cone)
# nose_height = 2
# nose_vertices = [[0, 0, body_height + nose_height]]
# nose_faces = []

# for i in range(num_segments):
#     angle = 2 * np.pi * i / num_segments
#     x = np.cos(angle) * body_radius
#     y = np.sin(angle) * body_radius
#     nose_vertices.append([x, y, body_height])

# for i in range(num_segments):
#     next_i = (i + 1) % num_segments
#     nose_faces.append([0, i + 1, next_i + 1])

# # Combine body and nose vertices and faces
# vertices = np.array(body_vertices + nose_vertices)
# faces = np.array(body_faces + nose_faces)

# # Assign colors to the nose vertices (white for simplicity)
# nose_colors = [[1.0, 1.0, 1.0, 1.0]] * len(nose_vertices)
# colors = np.array(body_colors + nose_colors)

# # Create the GLMeshItem
# rocket_mesh = gl.GLMeshItem(vertexes=vertices, faces=faces, vertexColors=colors, drawEdges=True, edgeColor=(1, 1, 1, 1), drawFaces=True, smooth=False)
# rocket_mesh.scale(0.1, 0.1, 0.1)  # Adjust scaling if needed
# w.addItem(rocket_mesh)

# # Optional: Rotate the rocket model
# # rocket_mesh.rotate(90, 1, 0, 0)

# def updateRocketOrientation():
#     global rocket_mesh, serial_data

#     # Read serial data in format "x,y,z"
#     if serial_data.in_waiting > 0:
#         line = serial_data.readline().decode().strip()
#         data = line.split(',')
#         if len(data) == 3:
#             pitch, yaw, roll = map(float, data)
#             # Update rocket orientation based on pitch, yaw, roll
#             rocket_mesh.resetTransform()
#             rocket_mesh.rotate(0, 1, 0, 0)  # Rotate around X-axis (pitch)
#             rocket_mesh.rotate(0, 0, 1, 0)    # Rotate around Y-axis (yaw)
#             rocket_mesh.rotate(0, 0, 0, 1)   # Rotate around Z-axis (roll)

# t = QtCore.QTimer()
# t.timeout.connect(updateRocketOrientation)
# t.start(50)  # Update orientation every 50 ms

# if __name__ == '__main__':
#     import sys
#     if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
#         QtWidgets.QApplication.instance().exec_()

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
    except Exception as e:
        print(f"An error occurred while loading the shape: {e}")

from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph.opengl as gl
import numpy as np
import serial

app = QtWidgets.QApplication([])

# Serial communication setup (adjust port and baudrate as needed)
serial_port = 'COM3'  # Example port, update as per your system
baud_rate = 115200

serial_data = serial.Serial(serial_port, baud_rate)

w = gl.GLViewWidget()
w.opts['distance'] = 20
w.show()
w.setWindowTitle('Rocket Model Viewer')

g = gl.GLGridItem()
w.addItem(g)

# Replace the file_path with the path to your .obj file
file_path = r"C:\Users\iqras\OneDrive\Documents\Team Sammard\Team_Sammard\SA_CUP_2024\SA_CUP_2024_GUI_Final\SA_CUP_2024-dev_samigang2final\SA_CUP_2024-dev_samigang2\flair_resources_files\Agneya Chamatkar.obj"
shape_data = load_shape_from_obj(file_path)

vertices = np.array(shape_data["vertices"])
faces = np.array(shape_data["faces"])

# Create the GLMeshItem
rocket_mesh = gl.GLMeshItem(vertexes=vertices, faces=faces, drawEdges=True, edgeColor=(1, 1, 1, 1), drawFaces=True, smooth=True)
rocket_mesh.scale(0.1, 0.1, 0.1)  # Adjust scaling if needed
w.addItem(rocket_mesh)

def updateRocketOrientation():
    global rocket_mesh, serial_data

    # Read serial data in format "x,y,z"
    if serial_data.in_waiting > 0:
        line = serial_data.readline().decode().strip()
        data = line.split(',')
        if len(data) == 3:
            pitch, yaw, roll = map(float, data)
            # Update rocket orientation based on pitch, yaw, roll
            rocket_mesh.resetTransform()
            rocket_mesh.rotate(pitch, 1, 0, 0)  # Rotate around X-axis (pitch)
            rocket_mesh.rotate(yaw, 0, 1, 0)    # Rotate around Y-axis (yaw)
            rocket_mesh.rotate(roll, 0, 0, 1)   # Rotate around Z-axis (roll)

t = QtCore.QTimer()
t.timeout.connect(updateRocketOrientation)
t.start(50)  # Update orientation every 50 ms

if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtWidgets.QApplication.instance().exec_()


# from PyQt5 import QtCore, QtGui, QtWidgets
# import pyqtgraph.opengl as gl
# import numpy as np

# # Function to load shape data from an OBJ file
# def load_shape_from_obj(file_path):
#     try:
#         vertices = []
#         faces = []
#         with open(file_path) as f:
#             for line in f:
#                 parts = line.strip().split()
#                 if not parts:
#                     continue
#                 if parts[0] == "v":
#                     vertex = list(map(float, parts[1:4]))  # Take only x, y, z components
#                     vertices.append(vertex)
#                 elif parts[0] == "f":
#                     face = [int(part.split('/')[0]) - 1 for part in parts[1:4]]  # Convert to 0-based index
#                     faces.append(face)

#         shape_data = {"vertices": vertices, "faces": faces}
#         return shape_data

#     except FileNotFoundError:
#         print(f"{file_path} not found.")
#     except Exception as e:
#         print(f"An error occurred while loading the shape: {e}")

# class MainWindow(QtWidgets.QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('Rocket Model Viewer')
#         self.central_widget = QtWidgets.QWidget()
#         self.setCentralWidget(self.central_widget)
        
#         self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.central_widget)
        
#         self.initUI()

#     def initUI(self):
#         # Create GLViewWidget
#         self.w = gl.GLViewWidget()
#         self.w.opts['distance'] = 20
        
#         # Add grid item to GLViewWidget
#         self.g = gl.GLGridItem()
#         self.w.addItem(self.g)
        
#         # Add GLViewWidget to horizontalLayout_20
#         self.horizontalLayout_20.addWidget(self.w)
        
#         # Replace with your OBJ file path
#         file_path = r"C:\Users\iqras\OneDrive\Documents\Team Sammard\Team_Sammard\SA_CUP_2024\SA_CUP_2024_GUI_Final\SA_CUP_2024-dev_samigang2final\SA_CUP_2024-dev_samigang2\flair_resources_files\Agneya Chamatkar.obj"
        
#         # Load shape data from OBJ file
#         shape_data = load_shape_from_obj(file_path)
#         vertices = np.array(shape_data["vertices"])
#         faces = np.array(shape_data["faces"])

#         # Create GLMeshItem for the rocket model
#         self.rocket_mesh = gl.GLMeshItem(vertexes=vertices, faces=faces, drawEdges=True, edgeColor=(1, 1, 1, 1), drawFaces=True, smooth=True)
#         self.rocket_mesh.scale(0.1, 0.1, 0.1)  # Adjust scaling if needed
#         self.w.addItem(self.rocket_mesh)

# if __name__ == '__main__':
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     mainWindow = MainWindow()
#     mainWindow.show()
#     sys.exit(app.exec_())


#########################################################################################################

# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# import numpy as np
# import pandas as pd
# from matplotlib.animation import FuncAnimation

# # Read the CSV file
# csv_file = r"C:\Users\iqras\OneDrive\Documents\Team Sammard\Team_Sammard\SA_CUP_2024\SA_CUP_2024_GUI_Final\SA_CUP_2024-dev_samigang2final\SA_CUP_2024-dev_samigang2\Testbench\ccvf.csv"
# data_df = pd.read_csv(csv_file)


# fig = plt.figure(figsize=(10, 10))
# ax = fig.add_subplot(111, projection='3d')

# # Create axis
# axes = [5, 5, 5]

# # Create Data
# data = np.ones(axes)

# # Control Transparency
# alpha = 0.9

# # Control color
# colors = np.empty(axes + [4])
# colors[0] = [1, 0, 0, alpha]  # red
# colors[1] = [0, 1, 0, alpha]  # green
# colors[2] = [0, 0, 1, alpha]  # blue
# colors[3] = [1, 1, 0, alpha]  # yellow
# colors[4] = [1, 1, 1, alpha]  # grey

# def get_rotation_matrix(pitch, yaw, roll):
#     """Calculate the rotation matrix from pitch, yaw, and roll (in degrees)."""
#     pitch = np.radians(pitch)
#     yaw = np.radians(yaw)
#     roll = np.radians(roll)

#     Rx = np.array([
#         [1, 0, 0],
#         [0, np.cos(pitch), -np.sin(pitch)],
#         [0, np.sin(pitch), np.cos(pitch)]
#     ])

#     Ry = np.array([
#         [np.cos(yaw), 0, np.sin(yaw)],
#         [0, 1, 0],
#         [-np.sin(yaw), 0, np.cos(yaw)]
#     ])

#     Rz = np.array([
#         [np.cos(roll), -np.sin(roll), 0],
#         [np.sin(roll), np.cos(roll), 0],
#         [0, 0, 1]
#     ])

#     R = np.dot(Rz, np.dot(Ry, Rx))  # Combined rotation matrix
#     return R

# def update_plot(frame):
#     print("done")
#     if frame < len(data_df):
#         # Get the current row of data
#         row = data_df.iloc[frame]
#         pitch = row['Orientation X']
#         yaw = row['Orientation Y']
#         roll = row['Orientation Z']
#         print("hi")
#         # Get the rotation matrix
#         R = get_rotation_matrix(pitch, yaw, roll)

#         # Create a 3D grid for the positions of the voxels
#         x, y, z = np.indices(np.array(axes) + 1)

#         # Flatten the grid arrays and combine them into a single array of coordinates
#         coords = np.vstack([x.ravel(), y.ravel(), z.ravel()])

#         # Apply the rotation matrix to the coordinates
#         rotated_coords = np.dot(R, coords).reshape((3,) + x.shape)

#         # Extract the rotated x, y, z coordinates
#         x_rot = rotated_coords[0]
#         y_rot = rotated_coords[1]
#         z_rot = rotated_coords[2]

#         # Clear the previous plot
#         ax.clear()
#         #plt.axis('off')
#         print("yo")
#         # Voxels is used for customizations of the sizes, positions, and colors.
#         ax.voxels(x_rot, y_rot, z_rot, data, facecolors=colors)

#         # Optionally adjust the camera angle
#         ax.view_init(elev=20, azim=30)
#     else:
#         print("here")

# # Create an animation
# ani = FuncAnimation(fig, update_plot, frames=len(data_df), interval=100, repeat=False)

# plt.show()



# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow
# from PyQt5.QtCore import QTimer, QUrl
# from PyQt5 import Qt3DCore
# from PyQt5 import Qt3DExtras
# from PyQt5.QtGui import QVector3D
# from PyQt5.QtCore import QSize

# class MainWindow(QMainWindow):
#     def _init_(self):
#         super()._init_()
#         self.setWindowTitle('3D Model Viewer')
#         self.setGeometry(100, 100, 800, 600)

#         # Qt 3D Scene
#         scene = Qt3DCore.QEntity()

#         # 3D Model Component
#         model_entity = Qt3DCore.QEntity(scene)
#         model_transform = Qt3DCore.QTransform()
#         model_transform.setScale3D(QVector3D(0.1, 0.1, 0.1))  # Adjust scale as needed
#         model_entity.addComponent(model_transform)

#         model_loader = Qt3DExtras.QGltf2Importer(scene)
#         model_loader.setSource(QUrl.fromLocalFile(r"C:\Users\iqras\OneDrive\Documents\Team Sammard\Team_Sammard\SA_CUP_2024\SA_CUP_2024_GUI_Final\SA_CUP_2024-dev_samigang2final\SA_CUP_2024-dev_samigang2\flair_resources_files\Agneya Chamatkar.obj"))  # Replace with your 3D model path
#         model_entity.addComponent(model_loader)

#         # Qt 3D View
#         view = Qt3DExtras.Qt3DWindow()
#         view.setRootEntity(scene)
#         container = self.createWindowContainer(view)
#         self.setCentralWidget(container)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())





# def load_shape_from_obj(self, file_path):
#         try:
#             vertices = []
#             faces = []
#             with open(file_path) as f:
#                 for line in f:
#                     if line[0] == "v":
#                         vertex = list(map(float, line[2:].strip().split()))
#                         vertices.append(vertex)
#                     elif line[0] == "f":
#                         face = list(map(int, line[2:].strip().split()))
#                         faces.append(face)

#             shape_data = {"vertices": vertices, "faces": faces}

#             return shape_data

#         except FileNotFoundError:
#             print(f"{file_path} not found.")
#         except:
#             print("An error occurred while loading the shape.")


# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow
# from PyQt5 import Qt3DCore
# from PyQt5 import Qt3DExtras
# from PyQt5.QtGui import QVector3D
# from PyQt5.QtCore import QTimer, QUrl
# from PyQt5.QtCore import QSize

# class MainWindow(QMainWindow):
#     def _init_(self):
#         super()._init_()
#         self.setWindowTitle('3D Model Viewer')
#         self.setGeometry(100, 100, 800, 600)

#         # Qt 3D Scene
#         scene = Qt3DCore.QEntity()

#         # 3D Model Component
#         model_entity = Qt3DCore.QEntity(scene)
#         model_transform = Qt3DCore.QTransform()
#         model_transform.setScale3D(QVector3D(0.1, 0.1, 0.1))  # Adjust scale as needed
#         model_entity.addComponent(model_transform)

#         model_loader = Qt3DExtras.QGltf2Importer(scene)
#         model_loader.setSource(QUrl.fromLocalFile(r"C:\Users\iqras\OneDrive\Documents\Team Sammard\Team_Sammard\SA_CUP_2024\SA_CUP_2024_GUI_Final\SA_CUP_2024-dev_samigang2final\SA_CUP_2024-dev_samigang2\flair_resources_files\Agneya Chamatkar.obj"))  # Replace with your 3D model path
#         model_entity.addComponent(model_loader)

#         # Qt 3D View
#         view = Qt3DExtras.Qt3DWindow()
#         view.setRootEntity(scene)
#         container = self.createWindowContainer(view)
#         self.setCentralWidget(container)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())




