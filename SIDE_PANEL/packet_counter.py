import csv
from PyQt5.QtCore import QTimer
from PyQt5 import *

f=open("C:/Users/iqras/OneDrive/Documents/Team Sammard/Team_Sammard/SA_CUP_2024/FLAIR_GUI","r")
r=csv.reader(f)
columns=next(r)
row=next(r)

class PacketCountDisplay:
    def __init__(self, packet_count_text):

        self.packet_count_text=packet_count_text
        def update_plot():
            row=next(r)

            packet_count_text.setText(row[2])

        self.Timer=QtCore.QTimer()
        self.Timer.setInterval(1000)
        self.Timer.timeout.connect(update_plot)
        self.Timer.start()