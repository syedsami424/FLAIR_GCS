class sidePanelButtonModule:
    def __init__(self, stackedWidget, home_button, graphs_button, GPS_button, tabledata_button, settings_button, rkt_model_button, home_button_frame, graphs_button_frame, GPS_button_frame, tabledata_button_frame, settings_button_frame, RKTmodel_button_frame):

        self.stackedWidget = stackedWidget
        stackedWidget.setCurrentIndex(0)

        self.home_button = home_button
        self.graphs_button = graphs_button
        self.GPS_button = GPS_button
        self.rkt_model_button = rkt_model_button
        self.tabledata_button = tabledata_button
        self.settings_button = settings_button


        self.home_button_frame = home_button_frame
        self.graphs_button_frame = graphs_button_frame
        self.GPS_button_frame = GPS_button_frame
        self.RKTmodel_button_frame = RKTmodel_button_frame
        self.tabledata_button_frame = tabledata_button_frame
        self.settings_button_frame = settings_button_frame


        home_button.clicked.connect(lambda: self.change_frame_stylesheet(self.home_button, self.home_button_frame))
        graphs_button.clicked.connect(lambda: self.change_frame_stylesheet(self.graphs_button, self.graphs_button_frame))
        GPS_button.clicked.connect(lambda: self.change_frame_stylesheet(self.GPS_button, self.GPS_button_frame))
        rkt_model_button.clicked.connect(lambda: self.change_frame_stylesheet(self.rkt_model_button, self.RKTmodel_button_frame))
        tabledata_button.clicked.connect(lambda: self.change_frame_stylesheet(self.tabledata_button, self.tabledata_button_frame))
        settings_button.clicked.connect(lambda: self.change_frame_stylesheet(self.settings_button, self.settings_button_frame))
        

        home_button.clicked.connect(lambda: self.change_tab(0))
        graphs_button.clicked.connect(lambda: self.change_tab(1))
        GPS_button.clicked.connect(lambda: self.change_tab(2))
        rkt_model_button.clicked.connect(lambda: self.change_tab(3))
        tabledata_button.clicked.connect(lambda: self.change_tab(4))
        settings_button.clicked.connect(lambda: self.change_tab(5))


        home_button.clicked.connect(lambda: self.change_button_stylesheet(self.home_button))
        graphs_button.clicked.connect(lambda: self.change_button_stylesheet(self.graphs_button))
        GPS_button.clicked.connect(lambda: self.change_button_stylesheet(self.GPS_button))
        rkt_model_button.clicked.connect(lambda: self.change_button_stylesheet(self.rkt_model_button))
        tabledata_button.clicked.connect(lambda: self.change_button_stylesheet(self.tabledata_button))
        settings_button.clicked.connect(lambda: self.change_button_stylesheet(self.settings_button))


        self.buttons_frames = {
            home_button: home_button_frame,
            graphs_button: graphs_button_frame,
            GPS_button: GPS_button_frame,
            rkt_model_button: RKTmodel_button_frame,            
            tabledata_button: tabledata_button_frame,
            settings_button: settings_button_frame,
            
        }

    def change_frame_stylesheet(self, button, frame):
        for current_button, current_frame in self.buttons_frames.items():
            if current_button == button:
                new_stylesheet = "QFrame {\n" \
                                 "    background: white;\n" \
                                 "    border-top: 2px solid black;\n" \
                                 "    border-top-left-radius: 25px;\n" \
                                 "    border-bottom-left-radius: 25px;\n" \
                                 "    border-left: 2px solid black;\n" \
                                 "    border-bottom: 2px solid black;\n" \
                                 "}\n"
                current_frame.setStyleSheet(new_stylesheet)
            else:
                current_frame.setStyleSheet("    QFrame {\n"
                                           "    background-color: transparent;\n"
                                           "    border: none;\n"
                                           "}\n"
                                           "    QFrame:hover {\n"
                                           "    background: white;\n"
                                           "    border-top: 2px solid black;\n"
                                           "    border-top-left-radius: 25px;\n"
                                           "    border-bottom-left-radius: 25px;\n"
                                           "    border-left: 2px solid black;\n"
                                           "    border-bottom: 2px solid black;\n"
                                           "}\n")

    def change_button_stylesheet(self, button):
        button_name = button.objectName()

        for current_button, current_frame in self.buttons_frames.items():

            if current_button == button:
                if button_name == "home_button":
                    image_name = "home1.png"
                    image_name2 = "home2.png"

                elif button_name == "graphs_button":
                    image_name = "graphs1.png"
                    image_name2 = "graphs2.png"

                elif button_name == "GPS_button":
                    image_name = "GPS1.png"
                    image_name2 = "GPS2.png"

                elif button_name == "rkt_model_button":
                    image_name = "RKT_MODEL1.png"
                    image_name2 = "RKT_MODEL2.png"

                elif button_name == "tabledata_button":
                    image_name = "table_data1.png"
                    image_name2 = "table_data2.png"

                elif button_name == "settings_button":
                    image_name = "settings2.png"
                    image_name2 = "settings1.png"

                elif button_name == "notif_button":
                    image_name = "notif1.png"
                    image_name2 = "notif2.png"

                new_stylesheet = f"QPushButton{{" \
                                 f"   border-image: url(:/Side_panel/Image_resources/sidePanel/{image_name});" \
                                 "    border-top: 0px;" \
                                 "    border-top-left-radius: 25px;" \
                                 "    border-bottom-left-radius: 25px;" \
                                 "    border-bottom-right-radius: 0px;" \
                                 "}}" \

                current_button.setStyleSheet(new_stylesheet)
            else:
                if current_button.objectName() == "home_button":
                    image_name = "home2.png"
                    image_name1 = "home1.png"

                elif current_button.objectName() == "graphs_button":
                    image_name = "graphs2.png"
                    image_name1 = "graphs1.png"

                elif current_button.objectName() == "GPS_button":
                    image_name = "GPS2.png"
                    image_name1 = "GPS1.png"

                elif current_button.objectName() == "rkt_model_button":
                    image_name = "RKT_MODEL2.png"
                    image_name1 = "RKT_MODEL1.png"

                elif current_button.objectName() == "tabledata_button":
                    image_name = "table_data2.png"
                    image_name1 = "table_data1.png"

                elif current_button.objectName() == "settings_button":
                    image_name = "settings1.png"
                    image_name1 = "settings2.png"

                elif current_button.objectName() == "notif_button":
                    image_name = "notif2.png"
                    image_name1 = "notif1.png"

                current_stylesheet = f"QPushButton{{" \
                                     f"   border-image: url(:/Side_panel/Image_resources/sidePanel/{image_name});" \
                                     "    border-top:0px;" \
                                     "    border-top-left-radius: 25px;" \
                                     "    border-bottom-left-radius: 25px;" \
                                     "    border-bottom-right-radius: 0px;" \
                                     "}}" \
                                     f"QPushButton:hover{{" \
                                     f"   border-image: url(:/Side_panel/Image_resources/sidePanel/{image_name1});" \
                                     "    border-top:0px;" \
                                     "    border-top-left-radius: 25px;" \
                                     "    border-bottom-left-radius: 25px;" \
                                     "    border-bottom-right-radius: 0px;" \
                                     "}}" \


                current_button.setStyleSheet(current_stylesheet)

    def change_tab(self, index):
        self.stackedWidget.setCurrentIndex(index)
