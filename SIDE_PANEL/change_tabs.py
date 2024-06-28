class ChangeTabs:
    def __init__(self, stackedWidget, home_button, graphs_button, GPS_button, rkt_model_button, tabledata_button, settings_button):

        self.stackedWidget = stackedWidget

        self.home_button = home_button
        self.graphs_button = graphs_button
        self.GPS_button = GPS_button
        self.rkt_model_button = rkt_model_button
        self.tabledata_button = tabledata_button
        self.settings_button = settings_button

        home_button.clicked.connect(lambda: self.change_tab(0))
        graphs_button.clicked.connect(lambda: self.change_tab(1))
        GPS_button.clicked.connect(lambda: self.change_tab(2))
        rkt_model_button.clicked.connect(lambda: self.change_tab(3))
        tabledata_button.clicked.connect(lambda: self.change_tab(4))
        settings_button.clicked.connect(lambda: self.change_tab(5))
        
    def change_tab(self, index):
        self.stackedWidget.setCurrentIndex(index)
