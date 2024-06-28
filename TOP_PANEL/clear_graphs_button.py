class ClearGraphsButton:
    def __init__(self, clear_graph_btn, altAx1, altAx2, speedAx, pressAx1, pressAx2, voltAx1, voltAx2, accAx, gyroAx, velAx, altVgpsaltAx, gpsspeedVvelAx, rocket_mesh):
        
        self.clear_graph_btn = clear_graph_btn
        self.altAx1 = altAx1
        self.altAx2 = altAx2 
        self.speedAx = speedAx
        self.pressAx1 = pressAx1
        self.pressAx2 = pressAx2 
        self.voltAx1 = voltAx1
        self.voltAx2 = voltAx2
        self.accAx = accAx 
        self.gyroAx = gyroAx 
        self.velAx = velAx
        self.altVgpsaltAx = altVgpsaltAx
        self.gpsspeedVvelAx = gpsspeedVvelAx
        self.rocket_mesh = rocket_mesh
        
        self.clear_graph_btn.clicked.connect(self.cleargraphs)
        
    def cleargraphs(self):
        # print("Clear graphs clicked")
        axes_list = [
            self.altAx1, self.altAx2, self.speedAx, self.pressAx1, self.pressAx2,
            self.voltAx1, self.voltAx2, self.accAx, self.gyroAx, self.velAx,
            self.altVgpsaltAx, self.gpsspeedVvelAx
        ]
        
        for ax in axes_list:
            try:
                ax.clear()
                ax.figure.canvas.draw()
            except:
                pass
        print("*****Axes cleared*****")

        self.rocket_mesh.resetTransform()
        self.rocket_mesh.translate(0, 0, -100)
        self.rocket_mesh.scale(0.1, 0.1, 0.1)
