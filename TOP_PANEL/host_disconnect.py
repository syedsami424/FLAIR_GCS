import serial
class HostDisconnectButton:
    def __init__(self, host_disconnect_button):
        self.serialInst = None
        self.host_disconnect_button = host_disconnect_button
        self.host_disconnect_button.clicked.connect(self.disconnect_host)

    def disconnect_host(self, serialInst):
        self.serialInst=serialInst
        try:
            if self.serialInst is not None and self.serialInst.is_open:
                self.serialInst.close()
                print("Host disconnected")
            else:
                print("No active connection to disconnect")
        except Exception as e:
            print("Error occurred while disconnecting:", e)