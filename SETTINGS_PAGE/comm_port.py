import serial.tools.list_ports

class AddToComboBox:
    def __init__(self, comboBox):

        self.comboBox = comboBox

    def add_to_comboBox(self):
        port_data = serial.tools.list_ports.comports()

        if len(port_data) == 0:
            print("Make sure ESP is connected")

        else:
            for i in range(len(port_data)):
                comport = port_data[i]
                self.comboBox.addItem(str(comport))