import folium
import io
from PyQt5.QtWidgets import QStackedWidget, QTextEdit

class PlotMap:
    def __init__(self, map_display: QTextEdit, map_display_GPS_page: QTextEdit, stackedWidget: QStackedWidget, gps_lat: float, gps_lon: float):
        self.map_display = map_display
        self.map_display_GPS_page = map_display_GPS_page
        self.stackedWidget = stackedWidget
        if not isinstance(gps_lat, float) or not isinstance(gps_lon, float):
            print()
            print(f"GPS COORDINATES INVALID: {gps_lat}, {gps_lon}")
            return
        else:
            self.map = folium.Map(location=[gps_lat, gps_lon], zoom_start=12)
            self.marker = folium.Marker(location=[gps_lat, gps_lon], icon=folium.Icon(color="red"), popup="RKT")
            self.map.add_child(self.marker)
            self.map_data = io.BytesIO()
            self.map.save(self.map_data, close_file=False)
            self.update_display()

    def update_map(self, gps_lat: float, gps_lon: float):
        if not isinstance(gps_lat, float) or not isinstance(gps_lon, float):
            print(f"GPS COORDINATES INVALID: {gps_lat}, {gps_lon}")
            return

        self.map.location = [gps_lat, gps_lon]
        self.marker.location = [gps_lat, gps_lon]
        self.map_data.seek(0)
        self.map.save(self.map_data, close_file=False)
        self.update_display()

    def update_display(self):
        if self.stackedWidget.currentIndex() in [0, 2]:
            self.map_display.setHtml(self.map_data.getvalue().decode())
            self.map_display_GPS_page.setHtml(self.map_data.getvalue().decode())
