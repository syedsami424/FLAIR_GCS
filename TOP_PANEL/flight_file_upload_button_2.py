import csv
from PyQt5.QtWidgets import QFileDialog
import time
from PyQt5 import QtCore
from custom_widgets.compassDial import CompassDial
from GPS_PAGE.gps import PlotMap

class FlightFileUploadButton:
    def __init__(self, flight_file_upload_button, stackedWidget, graphs_stackedWidget, RSSI_value, hp_temperature_disp, packet_count_text, mission_time_text, hp_alt_label, notif_alt_label, hp_gpsSpeed_label, accelerometer_value_x, accelerometer_value_y, accelerometer_value_z, hp_pressure_label, hp_voltage_label, gyrometer_value_x, gyrometer_value_y, gyrometer_value_z, pitch, yaw, roll, GPS_hp_lat, GPS_hp_lon, gps_heading_disp, SATS_value, table_data_csv_display, notif_press_label, notif_velocity_label, notif_voltage_label, notif_Velocity_label, notif_GPSspeed_label, notif_alt_label_2, notif_GPSalt_label, notif_gyro_label, notif_acc_label, gps_heading_label, mag_heading_label, GPS_SATSno_label, GPS_lat_label, GPS_lon_label, GPS_altitude_label, GPS_speed_label, altAx1, altCanvas1, altAx2, altCanvas2, speedAx, speedCanvas, pressAx1, pressCanvas1, pressAx2, pressCanvas2, voltAx1, voltCanvas1, voltAx2, voltCanvas2, accAx, accCanvas, gyroAx, gyroCanvas, velAx, velCanvas, altVgpsaltAx, altVgpsaltCanvas, gpsspeedVvelAx, gpsspeedVvelCanvas, trigger_value, map_display, map_display_GPS_page, horizontalLayout_31, horizontalLayout_35, altitude_label_graphs_sidepanel, velocity_label_graphs_sidepanel, temperature_label_graphs_sidepanel, acc_x_label_graphs_sidepanel, acc_y_label_graphs_sidepanel, acc_z_label_graphs_sidepanel, gyro_x_label_graphs_sidepanel, gyro_y_label_graphs_sidepanel, gyro_z_label_graphs_sidepanel):
        
        self.flight_file_upload_button = flight_file_upload_button

        self.RSSI_value = RSSI_value
        self.trigger_value = trigger_value
        self.hp_temperature_disp = hp_temperature_disp

        self.packet_count_text = packet_count_text
        self.mission_time_text = mission_time_text

        self.map_display = map_display
        self.map_display_GPS_page = map_display_GPS_page

        self.stackedWidget = stackedWidget
        self.graphs_stackedWidget = graphs_stackedWidget
        graphs_stackedWidget.setCurrentIndex(0)
        
        self.altitude_label_graphs_sidepanel = altitude_label_graphs_sidepanel
        self.velocity_label_graphs_sidepanel = velocity_label_graphs_sidepanel
        self.temperature_label_graphs_sidepanel = temperature_label_graphs_sidepanel
        self.acc_x_label_graphs_sidepanel = acc_x_label_graphs_sidepanel
        self.acc_y_label_graphs_sidepanel = acc_y_label_graphs_sidepanel
        self.acc_z_label_graphs_sidepanel = acc_z_label_graphs_sidepanel
        self.gyro_x_label_graphs_sidepanel = gyro_x_label_graphs_sidepanel
        self.gyro_y_label_graphs_sidepanel = gyro_y_label_graphs_sidepanel
        self.gyro_z_label_graphs_sidepanel = gyro_z_label_graphs_sidepanel
        

        # self.portName = portName
        ######################################################################
        self.horizontalLayout_35 = horizontalLayout_35
        self.horizontalLayout_31 = horizontalLayout_31

        self.compass_dial_GPS_heading = CompassDial()
        self.compass_dial_mag_heading = CompassDial()
        ######################################################################
        ## SET UP LINES:-
        ########################################################################
        ##ALTITUDE
        self.hp_alt_label = hp_alt_label
        self.notif_alt_label = notif_alt_label

        self.altAx1 = altAx1
        self.altCanvas1 = altCanvas1

        self.altAx2 = altAx2
        self.altCanvas2 = altCanvas2
        ########################################################################
        ##SPEED

        self.hp_gpsSpeed_label = hp_gpsSpeed_label

        self.speedAx = speedAx
        self.speedCanvas = speedCanvas
        ########################################################################
        ##PRESSURE

        self.hp_pressure_label = hp_pressure_label
        self.notif_press_label = notif_press_label

        self.pressAx1 = pressAx1
        self.pressCanvas1 = pressCanvas1

        self.pressAx2 = pressAx2
        self.pressCanvas2 = pressCanvas2
        ########################################################################
        ##VOLTAGE

        self.hp_voltage_label = hp_voltage_label
        self.notif_voltage_label = notif_voltage_label

        self.voltAx1 = voltAx1
        self.voltCanvas1 = voltCanvas1

        self.voltAx2 = voltAx2
        self.voltCanvas2 = voltCanvas2
        ########################################################################
        ##ACCELEROMETER
        self.accelerometer_value_x = accelerometer_value_x
        self.accelerometer_value_y = accelerometer_value_y
        self.accelerometer_value_z = accelerometer_value_z

        self.notif_acc_label = notif_acc_label
        
        self.accAx = accAx
        self.accCanvas = accCanvas
        ########################################################################
        ##GYROMETER
        self.gyrometer_value_x = gyrometer_value_x
        self.gyrometer_value_y = gyrometer_value_y
        self.gyrometer_value_z = gyrometer_value_z

        self.notif_gyro_label = notif_gyro_label

        self.gyroAx = gyroAx
        self.gyroCanvas = gyroCanvas  
        ########################################################################
        ##EULER'S ANGLE
        self.pitch = pitch
        self.yaw = yaw
        self.roll = roll
        ########################################################################
        ##GPS COORDINATES
        self.GPS_hp_lat = GPS_hp_lat
        self.GPS_hp_lon = GPS_hp_lon
        ########################################################################
        ##GPS heading
        self.gps_heading_disp = gps_heading_disp
        ########################################################################
        ##SATS VALUE
        self.SATS_value = SATS_value
        ########################################################################
        self.table_data_csv_display = table_data_csv_display
        ########################################################################
        ##VELOCITY
        self.notif_velocity_label = notif_velocity_label

        self.velAx = velAx
        self.velCanvas = velCanvas      
        ########################################################################
        ## ALTITUDE VS GPS ALTITUDE
        self.notif_GPSalt_label = notif_GPSalt_label
        self.notif_alt_label_2 = notif_alt_label_2


        self.altVgpsaltAx = altVgpsaltAx
        self.altVgpsaltCanvas = altVgpsaltCanvas
        ########################################################################
        ## GPS SPEED VS VELOCITY
        self.notif_GPSspeed_label = notif_GPSspeed_label
        self.notif_Velocity_label = notif_Velocity_label

        self.gpsspeedVvelAx = gpsspeedVvelAx
        self.gpsspeedVvelCanvas = gpsspeedVvelCanvas
        ########################################################################
        self.mag_heading_label = mag_heading_label
        self.gps_heading_label = gps_heading_label
        self.GPS_SATSno_label = GPS_SATSno_label
        self.GPS_lat_label = GPS_lat_label
        self.GPS_lon_label = GPS_lon_label
        self.GPS_altitude_label = GPS_altitude_label
        self.GPS_speed_label = GPS_speed_label        
        ########################################################################

        self.time = []
        self.altitude = []
        self.temperature = []
        self.speed = [] #GPS
        self.pressure = []
        self.voltage = []
        self.velocity = []
        self.GPS_alt = []
        self.gyro_x = []
        self.gyro_y = []
        self.gyro_z = []
        self.acc_x = []
        self.acc_y = []
        self.acc_z = [] 

        self.flight_file_upload_button.clicked.connect(self.read_data)

    def read_data(self):

        try:
            self.file_path, _ = QFileDialog.getOpenFileName(None, "Open CSV File", "", "CSV files (*.csv)")
            
            if not self.file_path:
                print("No file selected.")
                return

            self.file=open(self.file_path,"r")
            self.reader = csv.reader(self.file)
            next(self.reader)

        except Exception as e:
            print('Failed to upload')
            print(e.args)

        ########################################################
        self.alt_line1, = self.altAx1.plot([],[],
            label ="Altitude",
            color ="#1f77b4",
            linewidth = 2,
            linestyle ='-')
        
        self.alt_line2, = self.altAx2.plot([],[],
            label ="Altitude",
            color ="#1f77b4",
            linewidth = 2,
            linestyle ='-') 
        
        self.speed_line, = self.speedAx.plot([],[],
            label ="Speed",
            color ="#1f77b4",
            linewidth = 2,
            linestyle ='-')
        
        self.press_line1, = self.pressAx1.plot([],[],
            label ="Pressure",
            color ="#1f77b4",
            linewidth = 2,
            linestyle ='-')

        self.press_line2, = self.pressAx2.plot([],[],
            label ="Pressure",
            color ="#1f77b4",
            linewidth = 2,
            linestyle ='-')

        self.volt_line1, = self.voltAx1.plot([],[],
            label ="Voltage",
            color ="#1f77b4",
            linewidth = 2,
            linestyle ='-')

        self.volt_line2, = self.voltAx2.plot([],[],
            label ="Voltage",
            color ="#1f77b4",
            linewidth = 2,
            linestyle ='-')

        self.acc_x_line, = self.accAx.plot([],[],
            label ="ACC-X",
            color ="#1f77b4",
            linewidth = 2,
            linestyle ='-')
        self.acc_y_line, = self.accAx.plot([],[],
            label ="ACC-Y",
            color ="#ff7f0e",
            linewidth = 2,
            linestyle ='-')
        self.acc_z_line, = self.accAx.plot([],[],
            label ="ACC-Z",
            color ="#2ca02c",
            linewidth = 2,
            linestyle ='-')

        self.acc_legend = self.accAx.legend(handles = [self.acc_x_line, self.acc_y_line, self.acc_z_line], loc ='lower right')
        self.accAx.add_artist(self.acc_legend)

        self.gyro_x_line, = self.gyroAx.plot([],[],
            label ="GYRO-X",
            color ="#1f77b4",
            linewidth = 2,
            linestyle ='-')
        self.gyro_y_line, = self.gyroAx.plot([],[],
            label ="GYRO-Y",
            color ="#ff7f0e",
            linewidth = 2,
            linestyle ='-')
        self.gyro_z_line, = self.gyroAx.plot([],[],
            label ="GYRO-Z",
            color ="#2ca02c",
            linewidth = 2,
            linestyle ='-')

        self.gyro_legend = self.gyroAx.legend(handles = [self.gyro_x_line, self.gyro_y_line, self.gyro_z_line], loc ='lower right')
        self.gyroAx.add_artist(self.gyro_legend)   

        self.velocity_line, = self.velAx.plot([],[],
            label ="Velocity",
            color ="#1f77b4",
            linewidth = 2,
            linestyle ='-')  

        self.altVgpsalt_line1, = self.altVgpsaltAx.plot([],[],
            label ="Altitude",
            color ="#1f77b4",
            linewidth = 2,
            linestyle ='-')
        self.altVgpsalt_line2, = self.altVgpsaltAx.plot([],[],
            label ="GPS Altitude",
            color ="#ff7f0e",
            linewidth = 2,
            linestyle ='-')
        
        self.altVgpsalt_legend = self.altVgpsaltAx.legend(handles = [self.altVgpsalt_line1, self.altVgpsalt_line2], loc ='lower right')
        self.altVgpsaltAx.add_artist(self.altVgpsalt_legend)  

        self.gpsspeedVvel_line1, = self.gpsspeedVvelAx.plot([],[],
            label ="GPS Speed",
            color ="#1f77b4",
            linewidth = 2,
            linestyle ='-')
        self.gpsspeedVvel_line2, = self.gpsspeedVvelAx.plot([],[],
            label ="Velocity",
            color ="#ff7f0e",
            linewidth = 2,
            linestyle ='-')
        
        self.gpsspeedVvel_legend = self.gpsspeedVvelAx.legend(handles = [self.gpsspeedVvel_line1, self.gpsspeedVvel_line2], loc ='lower right')
        self.gpsspeedVvelAx.add_artist(self.gpsspeedVvel_legend) 
        
        ########################################################
        try:
                                                        
            def plot_data(line, ax, plt_canvas, time, data):
                try:

                    line.set_data(time, data)
                    
                    ax.relim()
                    ax.autoscale_view()

                    plt_canvas.draw()
                    plt_canvas.flush_events()

                except Exception as e:
                    print(e.args)
                    print("an error ocurred in plot_data")

            def plot_vs_graphs(line1, line2, ax, plt_canvas, time, data1, data2):
                try:

                    line1.set_data(time, data1)
                    line2.set_data(time, data2)

                    ax.relim()
                    ax.autoscale_view()

                    plt_canvas.draw()
                    plt_canvas.flush_events()

                except Exception as e:
                    print(e.args)
                    print("an error ocurred in plot_vs_graphs")

            def plot_triple_graphs(line1, line2, line3, ax, plt_canvas, time, data1, data2, data3):
                try:

                    line1.set_data(time, data1)
                    line2.set_data(time, data2)
                    line3.set_data(time, data3)

                    ax.relim()
                    ax.autoscale_view()

                    plt_canvas.draw()
                    plt_canvas.flush_events()
                
                except Exception as e:
                    print(e.args)
                    print("an error ocurred in plot_triple_graphs")

            def update_data():

                try:
                    line = next(self.reader)

                    try:
                        try:
                            current_time = float(line[0])
                        except:
                            current_time = None
                        try:
                            pkt_count = str(line[1])
                        except:
                            pkt_count = None
                        try:
                            mission_time = str(line[2])
                        except:
                            mission_time = None
                        try:
                            current_altitude = float(line[3])
                        except:
                            current_altitude = None
                        try:
                            current_pressure = float(line[4])
                        except:
                            current_pressure = None
                        try:
                            current_temperature = float(line[5])
                        except:
                            current_temperature = None
                        try:
                            GPS_lat = float(line[6])
                        except:
                            GPS_lat = None
                        try:
                            GPS_lon = float(line[7])
                        except:
                            GPS_lon = None
                        try:
                            current_GPS_alt = float(line[8])
                        except:
                            current_GPS_alt = None
                        try:
                            current_speed = float(line[9])
                        except:
                            current_speed = None
                        try:
                            GPS_heading = int(line[10])
                        except:
                            GPS_heading = None
                        try:
                            GPS_time = str(line[11])
                        except:
                            GPS_time = None
                        try:
                            GPS_date = str(line[12])
                        except:
                            GPS_time = None
                        try:
                            sats = int(line[13])
                        except:
                            sats = None
                        try:
                            current_acc_x = float(line[14])
                        except:
                            current_acc_x = None
                        try:
                            current_acc_y = float(line[15])
                        except:
                            current_acc_y = None
                        try:
                            current_acc_z = float(line[16])
                        except:
                            current_acc_z = None
                        try:
                            current_gyro_x = float(line[17])
                        except:
                            current_gyro_x = None
                        try:
                            current_gyro_y = float(line[18])
                        except:
                            current_gyro_y = None
                        try:
                            current_gyro_z = float(line[19])
                        except:
                            current_gyro_z = None
                        try:
                            current_velocity = float(line[20])
                        except:
                            current_velocity = None
                        try:
                            pitch = float(line[21])
                        except:
                            pitch = None
                        try:
                            yaw = float(line[22])
                        except:
                            yaw = None
                        try:
                            roll = float(line[23])
                        except:
                            roll = None
                        try:
                            mag_heading = int(line[24])
                        except:
                            mag_heading = None
                        try:
                            current_voltage = float(line[25])
                        except:
                            current_voltage = None
                        try:
                            flight_state = str(line[26])
                        except:
                            flight_state = None
                        try:
                            trigger = str(line[27])
                        except:
                            trigger = None
                        try:
                            RSSI = int(line[28])
                        except:
                            RSSI = None 
                        ###############################################
                        self.time.append(current_time)
                        self.altitude.append(current_altitude)
                        self.temperature.append(current_temperature)
                        self.speed.append(current_speed)
                        self.pressure.append(current_pressure)
                        self.voltage.append(current_voltage)
                        self.velocity.append(current_velocity)
                        self.GPS_alt.append(current_GPS_alt)
                        self.gyro_x.append(current_gyro_x)
                        self.gyro_y.append(current_gyro_y)
                        self.gyro_z.append(current_gyro_z)
                        self.acc_x.append(current_acc_x)
                        self.acc_y.append(current_acc_y)
                        self.acc_z.append(current_acc_z) 
                            
                        try:    
                            self.mission_time_text.setText(mission_time)
                        except:
                            self.mission_time_text.setText("n/a")                           
                        try:
                            self.packet_count_text.setText(str(pkt_count))
                        except:
                            self.packet_count_text.setText("n/a")    

                        if self.stackedWidget.currentIndex() == 0:
                            try:
                                self.accelerometer_value_x.setText(f"{str(current_acc_x)} ft/s²")
                            except:
                                self.accelerometer_value_x.setText("n/a")
                            try:
                                self.accelerometer_value_y.setText(f"{str(current_acc_y)} ft/s²")
                            except:
                                self.accelerometer_value_y.setText("n/a")
                            try:
                                self.accelerometer_value_z.setText(f"{str(current_acc_z)} ft/s²")
                            except:
                                self.accelerometer_value_z.setText("n/a")
                            try:
                                self.gyrometer_value_x.setText(f"{str(current_gyro_x)} °/s")
                            except:
                                self.gyrometer_value_x.setText("n/a")
                            try:
                                self.gyrometer_value_y.setText(f"{str(current_gyro_y)} °/s")
                            except:
                                self.gyrometer_value_y.setText("n/a")
                            try:
                                self.gyrometer_value_z.setText(f"{str(current_gyro_z)} °/s")
                            except:
                                self.gyrometer_value_z.setText("n/a")
                            try:
                                self.pitch.setText(f"{str(line[21])} °")
                            except:
                                self.pitch.setText("n/a")
                            try:
                                self.yaw.setText(f"{str(line[22])} °")
                            except:
                                self.yaw.setText("n/a")
                            try:
                                self.roll.setText(f"{str(line[23])} °")
                            except:
                                self.roll.setText("n/a")
                            try:
                                self.GPS_hp_lat.setText(f"Lat: {str(line[6])} °")
                            except:
                                self.GPS_hp_lat.setText(f"Lat: n/a")
                            try:
                                self.GPS_hp_lon.setText(f"Lon: {str(line[7])} °")
                            except:
                                self.GPS_hp_lon.setText(f"Lon: n/a")
                            try:
                                self.hp_temperature_disp.setText(str(current_temperature))
                            except:
                                self.hp_temperature_disp.setText("n/a")
                            try:
                                self.gps_heading_disp.setText(str(line[10]))
                            except:
                                self.gps_heading_disp.setText("n/a")
                            #############################################################################################

                            try:
                                GPS_lat = float(GPS_lat)
                                GPS_lon = float(GPS_lon)
                                plot_map = PlotMap(self.map_display, self.map_display_GPS_page, self.stackedWidget, GPS_lat, GPS_lon)
                                # print("here1")
                            except:
                                plot_map = PlotMap(self.map_display, self.map_display_GPS_page, self.stackedWidget, None, None)

                            try:
                                try:
                                    self.hp_alt_label.setText(f"ALTITUDE: {str(current_altitude)} feet")
                                except:
                                    self.hp_alt_label.setText(f"ALTITUDE: n/a")
                                try:
                                    plotAlt = plot_data(self.alt_line1, self.altAx1, self.altCanvas1, self.time, self.altitude)
                                except:
                                    plotAlt = plot_data(self.alt_line1, self.altAx1, self.altCanvas1, None, None)
                            except Exception as e:
                                print("error in plotAlt")
                                print(e.args)
                            
                            try:
                                try:
                                    self.hp_gpsSpeed_label.setText(f"GPS SPEED: {str(current_speed)} m/h")
                                except:
                                    self.hp_gpsSpeed_label.setText(f"GPS SPEED: n/a")
                                try:
                                    plotSpeed = plot_data(self.speed_line, self.speedAx, self.speedCanvas, self.time, self.speed)
                                except:
                                    print("nothinggg")
                                    plotSpeed = plot_data(self.speed_line, self.speedAx, self.speedCanvas, None, None)
                            except Exception as e:
                                print("error in plotSpeed")
                                print(e.args)

                            try:
                                try:
                                    self.hp_pressure_label.setText(f"PRESSURE: {str(current_pressure)} Pascal")
                                except:
                                    self.hp_pressure_label.setText(f"PRESSURE: n/a")
                                try:
                                    plotPress = plot_data(self.press_line1, self.pressAx1, self.pressCanvas1, self.time, self.pressure)
                                except:
                                    plotPress = plot_data(self.press_line1, self.pressAx1, self.pressCanvas1, None, None)         
                            except Exception as e:
                                print("error in plotPress")
                                print(e.args)

                            try:
                                try:
                                    self.hp_voltage_label.setText(f"VOLTAGE: {str(current_voltage)} Volts")
                                except:
                                    self.hp_voltage_label.setText(f"VOLTAGE: n/a")
                                try:
                                    plotVoltage = plot_data(self.volt_line1, self.voltAx1, self.voltCanvas1, self.time, self.voltage)
                                except:
                                    plotVoltage = plot_data(self.volt_line1, self.voltAx1, self.voltCanvas1, None, None)
                            except Exception as e:
                                print("error in plotVoltage")
                                print(e.args)

                        elif self.stackedWidget.currentIndex() == 1:
                            self.altitude_label_graphs_sidepanel.setText(f"ALTITUDE: {current_altitude} Feet (AGL)")
                            self.velocity_label_graphs_sidepanel.setText(f"SPEED: {current_velocity} m/h")
                            self.temperature_label_graphs_sidepanel.setText(f"TEMPERATURE: {str(current_temperature)}°C")

                            self.acc_x_label_graphs_sidepanel.setText(f"ACC_X: {str(current_acc_x)} ft/s²")
                            self.acc_y_label_graphs_sidepanel.setText(f"ACC_Y: {str(current_acc_y)} ft/s²")
                            self.acc_z_label_graphs_sidepanel.setText(f"ACC_Z: {str(current_acc_z)} ft/s²")

                            self.gyro_x_label_graphs_sidepanel.setText(f"GYRO_X: {str(current_gyro_x)} °/s")
                            self.gyro_y_label_graphs_sidepanel.setText(f"GYRO_Y: {str(current_gyro_y)} °/s")
                            self.gyro_z_label_graphs_sidepanel.setText(f"GYRO_Z: {str(current_gyro_z)} °/s")
                            if self.graphs_stackedWidget.currentIndex() == 0:
                                try:
                                    try:
                                        self.notif_alt_label.setText(f"ALTITUDE: {str(current_altitude)} feet")
                                    except:
                                        self.notif_alt_label.setText(f"ALTITUDE: n/a")
                                    try:
                                        plotNotifAlt = plot_data(self.alt_line2, self.altAx2, self.altCanvas2, self.time, self.altitude)
                                    except:
                                        plotNotifAlt = plot_data(self.alt_line2, self.altAx2, self.altCanvas2, None, None) 
                                except Exception as e:
                                    print("error in plotNotifAlt")
                                    print(e.args)
                                
                                try:
                                    try:
                                        self.notif_press_label.setText(f"PRESSURE: {str(current_pressure)} Pascal")
                                    except:
                                        self.notif_press_label.setText(f"PRESSURE: n/a")
                                    try:
                                        plotNotifPressure = plot_data(self.press_line2, self.pressAx2, self.pressCanvas2, self.time, self.pressure)
                                    except:
                                        plotNotifPressure = plot_data(self.press_line2, self.pressAx2, self.pressCanvas2, None, None)
                                except Exception as e:
                                    print("error in plotNotifPressure")
                                    print(e.args)

                                # try:
                                #     self.notif_temp_label.setText(f"TEMPERATURE: {str(current_temperature)} °C")
                                #     plotNotifTemperature = plot_data(self.temp_line, self.tempAx, self.tempCanvas, self.time, self.temperature)

                                # except Exception as e:
                                #     print("error in plotNotifTemperature")
                                #     print(e.args)

                            elif self.graphs_stackedWidget.currentIndex() == 1:

                                try:
                                    try:
                                        self.notif_voltage_label.setText(f"VOLTAGE: {str(current_voltage)} Volts")
                                    except:
                                        self.notif_voltage_label.setText(f"VOLTAGE: n/a")
                                    try:
                                        plotNotifVoltage = plot_data(self.volt_line2, self.voltAx2, self.voltCanvas2, self.time, self.voltage)
                                    except:
                                        plotNotifVoltage = plot_data(self.volt_line2, self.voltAx2, self.voltCanvas2, None, None)
                                except Exception as e:
                                    print("error in plotNotifVoltage")
                                    print(e.args)
                                
                                try:
                                    try:
                                        self.notif_velocity_label.setText(f"VELOCITY: {str(current_velocity)} m/h")
                                    except:
                                        self.notif_velocity_label.setText(f"VELOCITY: n/a")
                                    try:
                                        plotNotifVelocity = plot_data(self.velocity_line, self.velAx, self.velCanvas, self.time, self.velocity)
                                    except:
                                        plotNotifVelocity = plot_data(self.velocity_line, self.velAx, self.velCanvas, None, None)                                        
                                except Exception as e:
                                    print("error in plotNotifVelocity")
                                    print(e.args)

                            elif self.graphs_stackedWidget.currentIndex() == 2:
                                try:
                                    str_GPSspeed = str(current_speed)
                                except:
                                    str_GPSspeed = "n/a"
                                try:
                                    str_velocity = str(current_velocity)
                                except:
                                    str_velocity = "n/a"

                                plotVelocity_text = f"VELOCITY: {str_velocity} m/h"
                                plotGPSSpeed_text = f"GPS Speed: {str_GPSspeed} m/h"
                                self.notif_GPSspeed_label.setText(plotGPSSpeed_text)                       
                                self.notif_Velocity_label.setText(plotVelocity_text)

                                try:
                                    plotGPSspeedVelocity = plot_vs_graphs(self.gpsspeedVvel_line1, self.gpsspeedVvel_line2, self.gpsspeedVvelAx, self.gpsspeedVvelCanvas, self.time, self.speed, self.velocity)
                                except:
                                    plotGPSspeedVelocity = plot_vs_graphs(self.gpsspeedVvel_line1, self.gpsspeedVvel_line2, self.gpsspeedVvelAx, self.gpsspeedVvelCanvas, None, None, None)

                                try:
                                    str_alt = str(current_altitude)
                                except:
                                    str_alt = "n/a"
                                try:
                                    str_gpsalt = str(current_GPS_alt)
                                except:
                                    str_gpsalt = "n/a"

                                plotalt_text = f"ALTITUDE: {str_alt} Feet (AGL)" 
                                plotGPSAlt_text = f"GPS ALTITUDE: {str_gpsalt} Feet (AGL)"
                                self.notif_GPSalt_label.setText(plotGPSAlt_text)
                                self.notif_alt_label_2.setText(plotalt_text)

                                try:
                                    plotNotifaltGPSalt = plot_vs_graphs(self.altVgpsalt_line1, self.altVgpsalt_line2, self.altVgpsaltAx, self.altVgpsaltCanvas, self.time, self.altitude, self.GPS_alt)
                                except:
                                    plotNotifaltGPSalt = plot_vs_graphs(self.altVgpsalt_line1, self.altVgpsalt_line2, self.altVgpsaltAx, self.altVgpsaltCanvas, None, None, None)


                            elif self.graphs_stackedWidget.currentIndex() == 3:

                                try:
                                    str_gyroX = str(current_gyro_x)
                                except:
                                    str_gyroX = "n/a"
                                try:
                                    str_gyroY = str(current_gyro_y)
                                except:
                                    str_gyroY = "n/a"
                                try:
                                    str_gyroZ = str(current_gyro_z)
                                except:
                                    str_gyroZ = "n/a"

                                gyro_text = f"X: {str_gyroX} °/s, Y: {str_gyroY} °/s, Z: {str_gyroZ} °/s"
                                self.notif_gyro_label.setText(gyro_text)

                                try:
                                    plotGyroscope = plot_triple_graphs(self.gyro_x_line, self.gyro_y_line, self.gyro_z_line, self.gyroAx, self.gyroCanvas, self.time, self.gyro_x, self.gyro_y, self.gyro_z)
                                except:
                                    plotGyroscope = plot_triple_graphs(self.gyro_x_line, self.gyro_y_line, self.gyro_z_line, self.gyroAx, self.gyroCanvas, None, None, None, None)

                                try:
                                    str_accX = str(current_acc_x)
                                except:
                                    str_accY = "n/a"
                                try:
                                    str_accY = str(current_acc_y)
                                except:
                                    str_accY = "n/a"
                                try:
                                    str_accZ = str(current_acc_z)
                                except:
                                    str_accZ = "n/a"

                                acc_text = f"X: {str_accX} ft/s², Y: {str_accY} ft/s², Z: {str_accZ} ft/s²"
                                self.notif_acc_label.setText(acc_text)
                                try:
                                    plotAccelerometer = plot_triple_graphs(self.acc_x_line, self.acc_y_line, self.acc_z_line, self.accAx, self.accCanvas, self.time, self.acc_x, self.acc_y, self.acc_z)
                                except:
                                    plotAccelerometer = plot_triple_graphs(self.acc_x_line, self.acc_y_line, self.acc_z_line, self.accAx, self.accCanvas, None, None, None, None)
                        elif self.stackedWidget.currentIndex() == 2:
                            try:
                                try:
                                    self.mag_heading_label.setText(f"(R)MAG HEADING: {str(mag_heading)}°")
                                except:
                                    self.mag_heading_label.setText(f"(R)MAG HEADING: n/a")
                                try:
                                    self.gps_heading_label.setText(f"(L)GPS HEADING: {str(GPS_heading)}°")
                                except:
                                    print("gps heading is none")
                                    self.gps_heading_label.setText(f"(L)GPS HEADING: n/a")
                                try:
                                    self.GPS_SATSno_label.setText(f"SATS NO.: {sats}")
                                except:
                                    self.GPS_SATSno_label.setText(f"SATS NO.: n/a")
                                try:
                                    self.GPS_lat_label.setText(f"LATITUDE: {str(GPS_lat)}°")
                                except:
                                    self.GPS_lat_label.setText(f"LATITUDE: n/a")
                                try:
                                    self.GPS_lon_label.setText(f"LONGITUDE: {str(GPS_lon)}°")
                                except:
                                    self.GPS_lon_label.setText(f"LONGITUDE: n/a")
                                try:
                                    self.GPS_altitude_label.setText(f"ALTITUDE: {current_GPS_alt} feet")
                                except:
                                    self.GPS_altitude_label.setText(f"ALTITUDE: n/a")
                                try:
                                    self.GPS_speed_label.setText(f"SPEED: {current_speed} m/h")
                                except:
                                    self.GPS_speed_label.setText(f"SPEED: n/a")
                            
                                try:
                                    self.compass_dial_GPS_heading.updateHeading(GPS_heading)
                                except:
                                    self.compass_dial_GPS_heading.updateHeading(None)
                                try:
                                    self.compass_dial_mag_heading.updateHeading(mag_heading)
                                except:
                                    self.compass_dial_mag_heading.updateHeading(None)
                            except Exception as e:
                                print(e.args)
                        # print("HERE")
                        ############################################################
                        ## RSSI 
                        try:
                            if RSSI >= -100:
                                self.RSSI_value.setStyleSheet("background:transparent;\n border-top:0px solid black;\n border-top-left-radius:0px;\n border-top-right-radius:0px;\n color:green;")

                            elif -115 <= RSSI < -100:
                                self.RSSI_value.setStyleSheet("background:transparent;\n border-top:0px solid black;\n border-top-left-radius:0px;\n border-top-right-radius:0px;\n color:rgb(241, 241, 13);")

                            elif RSSI < -115:
                                self.RSSI_value.setStyleSheet("background:transparent;\n border-top:0px solid black;\n border-top-left-radius:0px;\n border-top-right-radius:0px;\n color:red;")

                            self.RSSI_value.setText(str(RSSI))
                            self.RSSI_value.setHtml(f"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                    "p, li { white-space: pre-wrap; }\n"
                    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:36pt; font-weight:400; font-style:normal;\">\n"
                    f"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">{RSSI}</p></body></html>")
                            
                        except:
                            self.RSSI_value.setText("n/a")

                        ## SATS VALUE
                        try:
                            if sats <= 5:
                                self.SATS_value.setStyleSheet("border-top:0px solid black;\n color:red;")

                            elif sats > 5 and sats <= 10:
                                    self.SATS_value.setStyleSheet("border-top:0px solid black;\n color: rgb(241, 241, 13);")

                            elif sats > 10:
                                self.SATS_value.setStyleSheet("border-top:0px solid black;\n color:green;")

                            self.SATS_value.setMarkdown(str(sats))
                            self.SATS_value.setHtml(f"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                    "p, li { white-space: pre-wrap; }\n"
                                    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:36pt; font-weight:400; font-style:normal;\">\n"
                                    f"<p align=\"center\" style=\" margin-top:5px; margin-bottom:5px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">{sats}</p></body></html>")
                        except:
                            self.SATS_value.setMarkdown("n/a")
                        ## TRIGGER VALUE
                        try:
                            if (len(trigger)) == 4:
                                try:
                                    last_two_bits = trigger[-2:]
                                    # print(last_two_bits)
                                    if last_two_bits == "00":
                                        trigger_html = (
                                            f"TRIGGER: {trigger[:-2]}"
                                            f"<span style='color:red;'>{last_two_bits[0]}</span>"
                                            f"<span style='color:red;'>{last_two_bits[1]}</span>"
                                        )

                                    elif last_two_bits == "10":
                                        trigger_html = (
                                            f"TRIGGER: {trigger[:-2]}"
                                            f"<span style='color:green;'>{last_two_bits[0]}</span>"
                                            f"<span style='color:red;'>{last_two_bits[1]}</span>"
                                        )

                                    elif last_two_bits == "01":
                                        trigger_html = (
                                            f"TRIGGER: {trigger[:-2]}"
                                            f"<span style='color:red;'>{last_two_bits[0]}</span>"
                                            f"<span style='color:green;'>{last_two_bits[1]}</span>"
                                        )

                                    elif last_two_bits == "11":
                                        trigger_html = (
                                            f"TRIGGER: {trigger[:-2]}"
                                            f"<span style='color:green;'>{last_two_bits[0]}</span>"
                                            f"<span style='color:green;'>{last_two_bits[1]}</span>"
                                        )

                                    self.trigger_value.setMarkdown(f"TRIGGER: {str(trigger)}")
                                    self.trigger_value.setHtml(f"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                    "p, li { white-space: pre-wrap; }\n"
                                    "</style></head><body style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
                                    f"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">{trigger_html}</p></body></html>")
                                except:
                                    self.trigger_value.setMarkdown(f"TRIGGER: n/a")

                        except:
                            self.trigger_value.setMarkdown(f"TRIGGER: n/a")

                        ############################################################
                        
                        if len(self.time) == 30:
                            
                            self.time = self.time[-5:]

                            self.altitude = self.altitude[-5:]
                    

                            self.speed = self.speed[-5:]
                        

                            self.pressure = self.pressure[-5:]

                            self.voltage = self.voltage[-5:]

                            self.velocity = self.velocity[-5:]

                            self.temperature = self.temperature[-5:]
                            

                            self.GPS_alt = self.GPS_alt[-5:]


                            self.gyro_x = self.gyro_x[-5:]
                            self.gyro_y = self.gyro_y[-5:]
                            self.gyro_z = self.gyro_z[-5:]

                            self.acc_x = self.acc_x[-5:]
                            self.acc_y = self.acc_y[-5:]
                            self.acc_z = self.acc_z[-5:]
                        ############################################################

                    except Exception as e:
                        print("Could not read line")
                        print(e.args)

                except StopIteration:
                    self.Timer.stop()
                    # print("stopped")


            self.Timer=QtCore.QTimer()
            
            self.Timer.setInterval(0)
            self.Timer.timeout.connect(update_data)
            self.Timer.start()

        except Exception as e:
            print(e.args)
                