import serial
import re
import time
from PyQt5 import QtCore
from GPS_PAGE.gps import PlotMap
from TABLE_DATA_PAGE.table_data_csv import Appender
from custom_widgets.compassDial import CompassDial

class HostConnectButton:
    def __init__(self, host_connect_button, host_disconnect_button, flight_file_upload_button, flight_data_export_button, data_upload_button, stackedWidget, Tab1_btn, Tab2_btn, Tab3_btn, Tab4_btn, graphs_stackedWidget, RSSI_value, hp_temperature_disp, packet_count_text, mission_time_text, hp_alt_label, notif_alt_label, hp_gpsSpeed_label, accelerometer_value_x, accelerometer_value_y, accelerometer_value_z, hp_pressure_label, hp_voltage_label, gyrometer_value_x, gyrometer_value_y, gyrometer_value_z, pitch, yaw, roll, GPS_hp_lat, GPS_hp_lon, gps_heading_disp, SATS_value, table_data_csv_display, notif_press_label, notif_velocity_label, notif_voltage_label, notif_Velocity_label, notif_GPSspeed_label, notif_alt_label_2, notif_GPSalt_label, notif_gyro_label, notif_acc_label, gps_heading_label, mag_heading_label, GPS_SATSno_label, GPS_lat_label, GPS_lon_label, GPS_altitude_label, GPS_speed_label, altAx1, altCanvas1, altAx2, altCanvas2, speedAx, speedCanvas, pressAx1, pressCanvas1, pressAx2, pressCanvas2, voltAx1, voltCanvas1, voltAx2, voltCanvas2, accAx, accCanvas, gyroAx, gyroCanvas, velAx, velCanvas, altVgpsaltAx, altVgpsaltCanvas, gpsspeedVvelAx, gpsspeedVvelCanvas, download_file_btn, trigger_value, map_display, map_display_GPS_page, horizontalLayout_31, horizontalLayout_35, altitude_label_graphs_sidepanel, velocity_label_graphs_sidepanel, temperature_label_graphs_sidepanel, acc_x_label_graphs_sidepanel, acc_y_label_graphs_sidepanel, acc_z_label_graphs_sidepanel, gyro_x_label_graphs_sidepanel, gyro_y_label_graphs_sidepanel, gyro_z_label_graphs_sidepanel, rocket_mesh, w, pitch_label_rkt, yaw_label_pkt, roll_label_rkt, acc_x_rkt, acc_y_rkt, acc_z_rkt, gyro_x_rkt, gyro_y_rkt, gyro_z_rkt, portName):

        def get_run_counter():

            with open(r"C:\Users\iqras\OneDrive\Documents\Team Sammard\Team_Sammard\SA_CUP_2024\SA_CUP_2024_GUI_Final\SA_CUP_2024-dev_samigang2final\SA_CUP_2024-dev_samigang2\TABLE_DATA_PAGE\counter.txt", "r") as f:
                    counter = int(f.read().strip())

            return counter

        self.counter = get_run_counter()
        
        self.rocket_mesh = rocket_mesh
        self.w = w

        self.pitch_label_rkt = pitch_label_rkt
        self.yaw_label_pkt = yaw_label_pkt 
        self.roll_label_rkt = roll_label_rkt
        self.acc_x_rkt = acc_x_rkt
        self.acc_y_rkt = acc_y_rkt
        self.acc_z_rkt = acc_z_rkt
        self.gyro_x_rkt = gyro_x_rkt
        self.gyro_y_rkt = gyro_y_rkt
        self.gyro_z_rkt = gyro_z_rkt
        
        self.flight_file_upload_btn = flight_file_upload_button
        self.flight_data_export_btn = flight_data_export_button
        self.data_upload_btn = data_upload_button
        
        self.altitude_label_graphs_sidepanel = altitude_label_graphs_sidepanel
        self.velocity_label_graphs_sidepanel = velocity_label_graphs_sidepanel
        self.temperature_label_graphs_sidepanel = temperature_label_graphs_sidepanel
        self.acc_x_label_graphs_sidepanel = acc_x_label_graphs_sidepanel
        self.acc_y_label_graphs_sidepanel = acc_y_label_graphs_sidepanel
        self.acc_z_label_graphs_sidepanel = acc_z_label_graphs_sidepanel
        self.gyro_x_label_graphs_sidepanel = gyro_x_label_graphs_sidepanel
        self.gyro_y_label_graphs_sidepanel = gyro_y_label_graphs_sidepanel
        self.gyro_z_label_graphs_sidepanel = gyro_z_label_graphs_sidepanel
         
        self.host_connect_button = host_connect_button
        self.host_disconnect_button = host_disconnect_button
        self.download_file_btn = download_file_btn
        self.RSSI_value = RSSI_value
        self.trigger_value = trigger_value
        self.hp_temperature_disp = hp_temperature_disp

        self.serialInst = None
        # self.run = True
        self.disconnect_flag = 0

        self.packet_count_text = packet_count_text
        self.mission_time_text = mission_time_text

        self.map_display = map_display
        self.map_display_GPS_page = map_display_GPS_page

        self.stackedWidget = stackedWidget
        self.graphs_stackedWidget = graphs_stackedWidget
        graphs_stackedWidget.setCurrentIndex(0)

        self.portName = portName

        self.Tab1_btn = Tab1_btn
        self.Tab2_btn = Tab2_btn
        self.Tab3_btn = Tab3_btn
        self.Tab4_btn = Tab4_btn

        ######################################################################
        self.horizontalLayout_35 = horizontalLayout_35
        self.horizontalLayout_31 = horizontalLayout_31

        self.compass_dial_GPS_heading = CompassDial()
        self.compass_dial_mag_heading = CompassDial()

        self.horizontalLayout_31.addWidget(self.compass_dial_GPS_heading)
        self.horizontalLayout_35.addWidget(self.compass_dial_mag_heading)
        ######################################################################

        print(f"ACTIVE PORT: {self.portName}")

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
        ## TEMPERATURE
        # self.notif_temp_label = notif_temp_label

        # self.tempAx = tempAx
        # self.tempCanvas = tempCanvas

        # self.temp_line, = self.tempAx.plot([],[],
        #      label ="Temperature",
        #      color ="#1f77b4",
        #      linewidth = 2,
        #      linestyle ='-')
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

        self.host_connect_button.clicked.connect(self.read_data)
        try:
            Tab1_btn.clicked.connect(lambda: graphs_stackedWidget.setCurrentIndex(0))
            Tab2_btn.clicked.connect(lambda: graphs_stackedWidget.setCurrentIndex(1))
            Tab3_btn.clicked.connect(lambda: graphs_stackedWidget.setCurrentIndex(2))
            Tab4_btn.clicked.connect(lambda: graphs_stackedWidget.setCurrentIndex(3))
        except:
            graphs_stackedWidget.setCurrentIndex(0)

    def disconnect_host(self, serialInst):
        try:
            try:
                self.flight_file_upload_btn.setDisabled(False)
                self.data_upload_btn.setDisabled(False)
                self.flight_data_export_btn.setDisabled(False)
                print("All buttons enabled!!")

            except Exception as e:
                print(e.args)
                print("buttons could not get enabled")

            if serialInst is not None and serialInst.is_open:

                serialInst.close()
                self.disconnect_flag = 1

                if self.disconnect_flag == 1:

                    self.Timer.stop()
                    a = self.download_file_btn.clicked.connect(lambda: Appender.download_file(self.table_data_csv_display))
                    print("*************************")
                    print("HOST DISCONNECTED")
                
            else:
                pass
                
        except Exception as e:
            print("Error occurred while disconnecting:", e)


    def read_data(self):
        start_time = time.time()
        ##########################################################
        #Disabling all other buttons#
        try:
            self.flight_file_upload_btn.setDisabled(True)
            self.data_upload_btn.setDisabled(True)
            self.flight_data_export_btn.setDisabled(True)

        except Exception as e:
            print(e.args)
            print("failed to disable buttons")
        ##########################################################
 
        try:
            # print("HERE")
            self.serialInst = serial.Serial(f"{self.portName}", 115200)
            data_dict = {
                "A": [], "B": [], "C": [], "D": [], "E": [], "F": [], "G": [],
                "H": [], "I": [], "J": [], "K": [], "L": [], "M": [], "N": [],
                "O": [], "P": [], "Q": [], "R": [], "S": [], "T": [], "U": [],
                "V": [], "W": [], "X": [], "Y": [], "Z": [], "AB": [], "BC": [],
                "GARBAGE": []
            }
            self.data_dict_counter = 0
            self.total_keys = len(data_dict)

            self.time = []
            self.altitude = []
            self.temperature = []
            self.speed = [] #GPS
            self.pressure = []
            self.voltage = []
            self.velocity = []
            self.GPS_altitude = []
            self.gyro_x = []
            self.gyro_y = []
            self.gyro_z = []
            self.acc_x = []
            self.acc_y = []
            self.acc_z = [] 
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
            self.w.mousePressEvent = lambda event: None
            self.w.mouseReleaseEvent = lambda event: None
            self.w.mouseMoveEvent = lambda event: None

            # self.disconnect_flag = 0
            print("HC PRESSED")

        except Exception as e:
            print('Failed to connect to host')
            print(e.args)

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
            # hdc = HostDisconnectButton(self.host_disconnect_button)
            try:
                if self.serialInst.is_open:
                    self.host_disconnect_button.clicked.connect(lambda: self.disconnect_host(self.serialInst))
                
            except Exception as e:
                print("No active connection\n")
                print(e.args)

            NOT_AVAILABLE_TEXT = "n/a"
            self.gps_lat_lon_counter = 0

            def update_data():

                try:
                    # print("HERE1")
                    if self.serialInst.in_waiting > 0 :
                        
                        data = self.serialInst.readline()
                        data = str(data)
                        line = data.strip()
                        line = re.sub(r"b|'|\\r|\\n", "", line)
                        line = line.split(",", 1)
                        print(line)

                        if (len(line) < 2) :
                            data_dict["GARBAGE"].append(line)
                            # print(data_dict["GARBAGE"][-1])
                        else:
                    
                            value_ID = line[0]
                            value = line[1]
                            # print(line)
                            if (value_ID not in data_dict) or (value == ""):
                                data_dict["GARBAGE"].append(value)
                                # print(data_dict["GARBAGE"][-1])

                            data_dict[value_ID].append(value)

                        
                        self.data_dict_counter += 1

                        if self.data_dict_counter == self.total_keys:
                            try:
                                pkt_count = str(data_dict["A"][-1]) if data_dict["A"] else None
                            except:
                                pkt_count = None
                            try:
                                mission_time = str(data_dict["B"][-1]) if data_dict["B"] else None
                            except:
                                mission_time = None
                            try:
                                current_altitude = float(data_dict["C"][-1]) if data_dict["C"] else None
                            except:
                                current_altitude = None
                            try:
                                current_pressure = float(data_dict["D"][-1]) if data_dict["D"] else None
                            except:
                                current_pressure = None
                            try:
                                current_temperature = float(data_dict["E"][-1]) if data_dict["E"] else None
                            except:
                                current_temperature = None
                            try:
                                GPS_lat = float(data_dict["F"][-1]) if data_dict["F"] else None
                            except:
                                GPS_lat = None
                            try:
                                GPS_lon = float(data_dict["G"][-1]) if data_dict["G"] else None
                            except:
                                GPS_lon = None
                            try:
                                current_GPS_alt = float(data_dict["H"][-1]) if data_dict["H"] else None
                            except:
                                current_GPS_alt = None
                            try:
                                current_speed = float(data_dict["I"][-1]) if data_dict["I"] else None
                            except:
                                current_speed = None
                            try:
                                GPS_heading = int(data_dict["J"][-1]) if data_dict["J"] else None
                            except:
                                GPS_heading = None
                            try:
                                GPS_time = str(data_dict["K"][-1]) if data_dict["K"] else None
                            except:
                                GPS_time = None
                            try:
                                GPS_date = str(data_dict["L"][-1]) if data_dict["L"] else None
                            except:
                                GPS_time = None
                            try:
                                sats = int(data_dict["M"][-1]) if data_dict["M"] else None
                            except:
                                sats = None
                            try:
                                current_acc_x = float(data_dict["N"][-1]) if data_dict["N"] else None
                            except:
                                current_acc_x = None
                            try:
                                current_acc_y = float(data_dict["O"][-1]) if data_dict["O"] else None
                            except:
                                current_acc_y = None
                            try:
                                current_acc_z = float(data_dict["P"][-1]) if data_dict["P"] else None
                            except:
                                current_acc_z = None
                            try:
                                current_gyro_x = float(data_dict["Q"][-1]) if data_dict["Q"] else None
                            except:
                                current_gyro_x = None
                            try:
                                current_gyro_y = float(data_dict["R"][-1]) if data_dict["R"] else None
                            except:
                                current_gyro_y = None
                            try:
                                current_gyro_z = float(data_dict["S"][-1]) if data_dict["S"] else None
                            except:
                                current_gyro_z = None
                            try:
                                current_velocity = float(data_dict["T"][-1]) if data_dict["T"] else None
                            except:
                                current_velocity = None
                            try:
                                pitch = float(data_dict["U"][-1]) if data_dict["U"] else None
                            except:
                                pitch = None
                            try:
                                yaw = float(data_dict["V"][-1]) if data_dict["V"] else None
                            except:
                                yaw = None
                            try:
                                roll = float(data_dict["W"][-1]) if data_dict["W"] else None
                            except:
                                roll = None
                            try:
                                mag_heading = int(data_dict["X"][-1]) if data_dict["X"] else None
                            except:
                                mag_heading = None
                            try:
                                current_voltage = float(data_dict["Y"][-1]) if data_dict["Y"] else None
                            except:
                                current_voltage = None
                            try:
                                flight_state = str(data_dict["Z"][-1]) if data_dict["Z"] else None
                            except:
                                flight_state = None
                            try:
                                trigger = str(data_dict["AB"][-1]) if data_dict["AB"] else None
                            except:
                                trigger = None
                            try:
                                RSSI = int(data_dict["BC"][-1]) if data_dict["BC"] else None
                            except:
                                RSSI = None
                            try:
                                elapsed_time = time.time() - start_time
                                current_time = float(f"{elapsed_time:.2f}")          
                            except:
                                current_time = None

                            garbage = data_dict["GARBAGE"]
                                
                            line_str = f"{current_time}team_sammardʘpacket_sepʘteam_sammard{pkt_count}team_sammardʘpacket_sepʘteam_sammard{mission_time}team_sammardʘpacket_sepʘteam_sammard{current_altitude}team_sammardʘpacket_sepʘteam_sammard{current_pressure}team_sammardʘpacket_sepʘteam_sammard{current_temperature}team_sammardʘpacket_sepʘteam_sammard{GPS_lat}team_sammardʘpacket_sepʘteam_sammard{GPS_lon}team_sammardʘpacket_sepʘteam_sammard{current_GPS_alt}team_sammardʘpacket_sepʘteam_sammard{current_speed}team_sammardʘpacket_sepʘteam_sammard{GPS_heading}team_sammardʘpacket_sepʘteam_sammard{GPS_time}team_sammardʘpacket_sepʘteam_sammard{GPS_date}team_sammardʘpacket_sepʘteam_sammard{sats}team_sammardʘpacket_sepʘteam_sammard{current_acc_x}team_sammardʘpacket_sepʘteam_sammard{current_acc_y}team_sammardʘpacket_sepʘteam_sammard{current_acc_z}team_sammardʘpacket_sepʘteam_sammard{current_gyro_x}team_sammardʘpacket_sepʘteam_sammard{current_gyro_y}team_sammardʘpacket_sepʘteam_sammard{current_gyro_z}team_sammardʘpacket_sepʘteam_sammard{current_velocity}team_sammardʘpacket_sepʘteam_sammard{pitch}team_sammardʘpacket_sepʘteam_sammard{yaw}team_sammardʘpacket_sepʘteam_sammard{roll}team_sammardʘpacket_sepʘteam_sammard{mag_heading}team_sammardʘpacket_sepʘteam_sammard{current_voltage}team_sammardʘpacket_sepʘteam_sammard{flight_state}team_sammardʘpacket_sepʘteam_sammard{trigger}team_sammardʘpacket_sepʘteam_sammard{RSSI}"
                            line = line_str.strip().split("team_sammardʘpacket_sepʘteam_sammard")

                            # print(line)
                            ##########################################################
                            self.time.append(current_time)
                            self.altitude.append(current_altitude)
                            self.temperature.append(current_temperature)
                            self.speed.append(current_speed)
                            self.pressure.append(current_pressure)
                            self.voltage.append(current_voltage)
                            self.velocity.append(current_velocity)
                            self.GPS_altitude.append(current_GPS_alt)
                            self.gyro_x.append(current_gyro_x)
                            self.gyro_y.append(current_gyro_y)
                            self.gyro_z.append(current_gyro_z)
                            self.acc_x.append(current_acc_x)
                            self.acc_y.append(current_acc_y)
                            self.acc_z.append(current_acc_z)            
                            ##########################################################
                            try:    
                                self.mission_time_text.setText(mission_time)
                            except:
                                self.mission_time_text.setText(NOT_AVAILABLE_TEXT)                           
                            try:
                                self.packet_count_text.setText(str(pkt_count))
                            except:
                                self.packet_count_text.setText(NOT_AVAILABLE_TEXT)    
                            try:
                                self.mag_heading_label.setText(f"(R)MAG HEADING: {str(mag_heading)}°")
                            except:
                                self.mag_heading_label.setText(f"(R)MAG HEADING: {NOT_AVAILABLE_TEXT}")
                            try:
                                self.gps_heading_label.setText(f"(L)GPS HEADING: {str(GPS_heading)}°")
                            except:
                                self.gps_heading_label.setText(f"(L)GPS HEADING: {NOT_AVAILABLE_TEXT}")
                            try:
                                self.GPS_SATSno_label.setText(f"SATS NO.: {sats}")
                            except:
                                self.GPS_SATSno_label.setText(f"SATS NO.: {NOT_AVAILABLE_TEXT}")
                            try:
                                self.GPS_lat_label.setText(f"LATITUDE: {str(GPS_lat)}°")
                            except:
                                self.GPS_lat_label.setText(f"LATITUDE: {NOT_AVAILABLE_TEXT}")
                            try:
                                self.GPS_lon_label.setText(f"LONGITUDE: {str(GPS_lon)}°")
                            except:
                                self.GPS_lon_label.setText(f"LONGITUDE: {NOT_AVAILABLE_TEXT}")
                            try:
                                self.GPS_altitude_label.setText(f"ALTITUDE: {current_GPS_alt} feet")
                            except:
                                self.GPS_altitude_label.setText(f"ALTITUDE: {NOT_AVAILABLE_TEXT}")
                            try:
                                self.GPS_speed_label.setText(f"SPEED: {current_speed} m/h")
                            except:
                                self.GPS_speed_label.setText(f"SPEED: {NOT_AVAILABLE_TEXT}")

                            if self.stackedWidget.currentIndex() == 3:
                                try:
                                    self.pitch_label_rkt.setText(f"PITCH (X-Red): {str(pitch)}°")
                                except:
                                    self.pitch_label_rkt.setText(f"PITCH (X-Red): {NOT_AVAILABLE_TEXT}°")
                                
                                try:
                                    self.yaw_label_pkt.setText(f"YAW (Y-Green): {str(yaw)}°")
                                except:
                                    self.yaw_label_pkt.setText(f"YAW (Y-Green): {NOT_AVAILABLE_TEXT}°")
    
                                try:
                                    self.roll_label_rkt.setText(f"ROLL (Z-Blue): {str(roll)}°")
                                except:
                                    self.roll_label_rkt.setText(f"ROLL (Z-Blue): {NOT_AVAILABLE_TEXT}°")

                                try:
                                    self.acc_x_rkt.setText(f"ACC_X: {str(current_acc_x)} ft/s²")
                                except:
                                    self.acc_x_rkt.setText(f"ACC_X: {NOT_AVAILABLE_TEXT} ft/s²")
                                try:
                                    self.acc_y_rkt.setText(f"ACC_Y: {str(current_acc_y)} ft/s²")
                                except:
                                    self.acc_y_rkt.setText(f"ACC_Y: {NOT_AVAILABLE_TEXT} ft/s²")
                                try:
                                    self.acc_z_rkt.setText(f"ACC_Z: {str(current_acc_z)} ft/s²")
                                except:
                                    self.acc_z_rkt.setText(f"ACC_Z: {NOT_AVAILABLE_TEXT} ft/s²")

                                try:
                                    self.gyro_x_rkt.setText(f"GYRO_X: {str(current_gyro_x)} °/s")
                                except:
                                    self.gyro_x_rkt.setText("GYRO_X: n/a °/s")
                                try:
                                    self.gyro_y_rkt.setText(f"GYRO_Y: {str(current_gyro_y)} °/s")
                                except:
                                    self.gyro_y_rkt.setText(f"GYRO_Y: {NOT_AVAILABLE_TEXT} °/s")
                                try:
                                    self.gyro_z_rkt.setText(f"GYRO_Z: {str(current_gyro_z)} °/s")
                                except:
                                    self.gyro_z_rkt.setText(f"GYRO_Z: {NOT_AVAILABLE_TEXT} °/s")
                                    
                                try:
                                    self.rocket_mesh.rotate(pitch, 1, 0, 0) #X-axis (pitch)
                                except:
                                    self.rocket_mesh.rotate(0, 1, 0, 0)
                                try:
                                    self.rocket_mesh.rotate(yaw, 0, 1, 0)   #Y-axis (yaw)
                                except:
                                    self.rocket_mesh.rotate(0, 0, 1, 0)
                                try:
                                    self.rocket_mesh.rotate(roll, 0, 0, 1)  #Z-axis (roll)
                                except:
                                    self.rocket_mesh.rotate(0, 0, 0, 1)

                            try:
                                appender_obj = Appender(self.table_data_csv_display, line, self.counter)
                                csvObj = appender_obj.append_to_table()

                            except Exception as e:
                                print(e.args)

                            if self.gps_lat_lon_counter == 50:
                                self.gps_lat_lon_counter = 0
                                try:
                                    GPS_lat = float(GPS_lat)
                                    GPS_lon = float(GPS_lon)
                                    plot_map = PlotMap(self.map_display, self.map_display_GPS_page, self.stackedWidget, GPS_lat, GPS_lon)
                                except:
                                    plot_map = PlotMap(self.map_display, self.map_display_GPS_page, self.stackedWidget, None, None)
                            else:
                                pass
                            self.gps_lat_lon_counter += 1

                            try:
                                self.compass_dial_GPS_heading.updateHeading(GPS_heading)
                            except:
                                self.compass_dial_GPS_heading.updateHeading(None)
                            try:
                                self.compass_dial_mag_heading.updateHeading(mag_heading)
                            except:
                                self.compass_dial_mag_heading.updateHeading(None)

                            if self.stackedWidget.currentIndex() == 0:
                                try:
                                    self.accelerometer_value_x.setText(f"{str(current_acc_x)} ft/s²")
                                except:
                                    self.accelerometer_value_x.setText(NOT_AVAILABLE_TEXT)
                                try:
                                    self.accelerometer_value_y.setText(f"{str(current_acc_y)} ft/s²")
                                except:
                                    self.accelerometer_value_y.setText(NOT_AVAILABLE_TEXT)
                                try:
                                    self.accelerometer_value_z.setText(f"{str(current_acc_z)} ft/s²")
                                except:
                                    self.accelerometer_value_z.setText(NOT_AVAILABLE_TEXT)
                                try:
                                    self.gyrometer_value_x.setText(f"{str(current_gyro_x)} °/s")
                                except:
                                    self.gyrometer_value_x.setText(NOT_AVAILABLE_TEXT)
                                try:
                                    self.gyrometer_value_y.setText(f"{str(current_gyro_y)} °/s")
                                except:
                                    self.gyrometer_value_y.setText(NOT_AVAILABLE_TEXT)
                                try:
                                    self.gyrometer_value_z.setText(f"{str(current_gyro_z)} °/s")
                                except:
                                    self.gyrometer_value_z.setText(NOT_AVAILABLE_TEXT)
                                try:
                                    self.pitch.setText(f"{str(pitch)} °")
                                except:
                                    self.pitch.setText(NOT_AVAILABLE_TEXT)
                                try:
                                    self.yaw.setText(f"{str(yaw)} °")
                                except:
                                    self.yaw.setText(NOT_AVAILABLE_TEXT)
                                try:
                                    self.roll.setText(f"{str(roll)} °")
                                except:
                                    self.roll.setText(NOT_AVAILABLE_TEXT)
                                try:
                                    self.GPS_hp_lat.setText(f"Lat: {str(line[6])} °")
                                except:
                                    self.GPS_hp_lat.setText(f"Lat: {NOT_AVAILABLE_TEXT}")
                                try:
                                    self.GPS_hp_lon.setText(f"Lon: {str(line[7])} °")
                                except:
                                    self.GPS_hp_lon.setText(f"Lon: {NOT_AVAILABLE_TEXT}")
                                try:
                                    self.hp_temperature_disp.setText(str(current_temperature))
                                except:
                                    self.hp_temperature_disp.setText(NOT_AVAILABLE_TEXT)
                                try:
                                    self.gps_heading_disp.setText(str(line[10]))
                                except:
                                    self.gps_heading_disp.setText(NOT_AVAILABLE_TEXT)
                                #############################################################################################
                                try:
                                    try:
                                        self.hp_alt_label.setText(f"ALTITUDE: {str(current_altitude)} feet")
                                    except:
                                        self.hp_alt_label.setText(f"ALTITUDE: {NOT_AVAILABLE_TEXT}")
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
                                        self.hp_gpsSpeed_label.setText(f"GPS SPEED: {NOT_AVAILABLE_TEXT}")
                                    try:
                                        plotSpeed = plot_data(self.speed_line, self.speedAx, self.speedCanvas, self.time, self.speed)
                                    except:
                                        plotSpeed = plot_data(self.speed_line, self.speedAx, self.speedCanvas, None, None)
                                except Exception as e:
                                    print("error in plotSpeed")
                                    print(e.args)

                                try:
                                    try:
                                        self.hp_pressure_label.setText(f"PRESSURE: {str(current_pressure)} Pascal")
                                    except:
                                        self.hp_pressure_label.setText(f"PRESSURE: {NOT_AVAILABLE_TEXT}")
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
                                        self.hp_voltage_label.setText(f"VOLTAGE: {NOT_AVAILABLE_TEXT}")
                                    try:
                                        plotVoltage = plot_data(self.volt_line1, self.voltAx1, self.voltCanvas1, self.time, self.voltage)
                                    except:
                                        plotVoltage = plot_data(self.volt_line1, self.voltAx1, self.voltCanvas1, None, None)
                                except Exception as e:
                                    print("error in plotVoltage")
                                    print(e.args)

                            elif self.stackedWidget.currentIndex() == 1:
                                try:
                                    self.altitude_label_graphs_sidepanel.setText(f"ALTITUDE: {current_altitude} Feet (AGL)")
                                    self.velocity_label_graphs_sidepanel.setText(f"SPEED: {current_velocity} m/h")
                                    self.temperature_label_graphs_sidepanel.setText(f"TEMPERATURE: {str(current_temperature)}°C")

                                    self.acc_x_label_graphs_sidepanel.setText(f"ACC_X: {str(current_acc_x)} ft/s²")
                                    self.acc_y_label_graphs_sidepanel.setText(f"ACC_Y: {str(current_acc_y)} ft/s²")
                                    self.acc_z_label_graphs_sidepanel.setText(f"ACC_Z: {str(current_acc_z)} ft/s²")

                                    self.gyro_x_label_graphs_sidepanel.setText(f"GYRO_X: {str(current_gyro_x)} °/s")
                                    self.gyro_y_label_graphs_sidepanel.setText(f"GYRO_Y: {str(current_gyro_y)} °/s")
                                    self.gyro_z_label_graphs_sidepanel.setText(f"GYRO_Z: {str(current_gyro_z)} °/s")
                                except Exception as e:
                                    print(e.args)
                                if self.graphs_stackedWidget.currentIndex() == 0:
                                    try:
                                        try:
                                            self.notif_alt_label.setText(f"ALTITUDE: {str(current_altitude)} feet")
                                        except:
                                            self.notif_alt_label.setText(f"ALTITUDE: {NOT_AVAILABLE_TEXT}")
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
                                            self.notif_press_label.setText(f"PRESSURE: {NOT_AVAILABLE_TEXT}")
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
                                            self.notif_voltage_label.setText(f"VOLTAGE: {NOT_AVAILABLE_TEXT}")
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
                                            self.notif_velocity_label.setText(f"VELOCITY: {NOT_AVAILABLE_TEXT}")
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
                                        str_GPSspeed = NOT_AVAILABLE_TEXT
                                    try:
                                        str_velocity = str(current_velocity)
                                    except:
                                        str_velocity = NOT_AVAILABLE_TEXT

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
                                        str_alt = NOT_AVAILABLE_TEXT
                                    try:
                                        str_gpsalt = str(current_GPS_alt)
                                    except:
                                        str_gpsalt = NOT_AVAILABLE_TEXT

                                    plotalt_text = f"ALTITUDE: {str_alt} Feet (AGL)" 
                                    plotGPSAlt_text = f"GPS ALTITUDE: {str_gpsalt} Feet (AGL)"
                                    self.notif_GPSalt_label.setText(plotGPSAlt_text)
                                    self.notif_alt_label_2.setText(plotalt_text)

                                    try:
                                        plotNotifaltGPSalt = plot_vs_graphs(self.altVgpsalt_line1, self.altVgpsalt_line2, self.altVgpsaltAx, self.altVgpsaltCanvas, self.time, self.altitude, self.GPS_altitude)
                                    except:
                                        plotNotifaltGPSalt = plot_vs_graphs(self.altVgpsalt_line1, self.altVgpsalt_line2, self.altVgpsaltAx, self.altVgpsaltCanvas, None, None, None)


                                elif self.graphs_stackedWidget.currentIndex() == 3:

                                    try:
                                        str_gyroX = str(current_gyro_x)
                                    except:
                                        str_gyroX = NOT_AVAILABLE_TEXT
                                    try:
                                        str_gyroY = str(current_gyro_y)
                                    except:
                                        str_gyroY = NOT_AVAILABLE_TEXT
                                    try:
                                        str_gyroZ = str(current_gyro_z)
                                    except:
                                        str_gyroZ = NOT_AVAILABLE_TEXT

                                    gyro_text = f"X: {str_gyroX} °/s, Y: {str_gyroY} °/s, Z: {str_gyroZ} °/s"
                                    self.notif_gyro_label.setText(gyro_text)

                                    try:
                                        plotGyroscope = plot_triple_graphs(self.gyro_x_line, self.gyro_y_line, self.gyro_z_line, self.gyroAx, self.gyroCanvas, self.time, self.gyro_x, self.gyro_y, self.gyro_z)
                                    except:
                                        plotGyroscope = plot_triple_graphs(self.gyro_x_line, self.gyro_y_line, self.gyro_z_line, self.gyroAx, self.gyroCanvas, None, None, None, None)

                                    try:
                                        str_accX = str(current_acc_x)
                                    except:
                                        str_accY = NOT_AVAILABLE_TEXT
                                    try:
                                        str_accY = str(current_acc_y)
                                    except:
                                        str_accY = NOT_AVAILABLE_TEXT
                                    try:
                                        str_accZ = str(current_acc_z)
                                    except:
                                        str_accZ = NOT_AVAILABLE_TEXT

                                    acc_text = f"X: {str_accX} ft/s², Y: {str_accY} ft/s², Z: {str_accZ} ft/s²"
                                    self.notif_acc_label.setText(acc_text)
                                    try:
                                        plotAccelerometer = plot_triple_graphs(self.acc_x_line, self.acc_y_line, self.acc_z_line, self.accAx, self.accCanvas, self.time, self.acc_x, self.acc_y, self.acc_z)
                                    except:
                                        plotAccelerometer = plot_triple_graphs(self.acc_x_line, self.acc_y_line, self.acc_z_line, self.accAx, self.accCanvas, None, None, None, None)

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
                                self.RSSI_value.setText(NOT_AVAILABLE_TEXT)

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
                                self.SATS_value.setMarkdown(NOT_AVAILABLE_TEXT)
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
                                        self.trigger_value.setMarkdown(f"TRIGGER: {NOT_AVAILABLE_TEXT}")

                            except:
                                self.trigger_value.setMarkdown(f"TRIGGER: {NOT_AVAILABLE_TEXT}")

                            ############################################################
                            
                            if len(self.time) == 30:
                                
                                self.time = self.time[-5:]

                                self.altitude = self.altitude[-5:]
                       

                                self.speed = self.speed[-5:]
                          

                                self.pressure = self.pressure[-5:]

                                self.voltage = self.voltage[-5:]

                                self.velocity = self.velocity[-5:]

                                self.temperature = self.temperature[-5:]
                             

                                self.GPS_altitude = self.GPS_altitude[-5:]
        

                                self.gyro_x = self.gyro_x[-5:]
                                self.gyro_y = self.gyro_y[-5:]
                                self.gyro_z = self.gyro_z[-5:]

                                self.acc_x = self.acc_x[-5:]
                                self.acc_y = self.acc_y[-5:]
                                self.acc_z = self.acc_z[-5:]
                            ############################################################
                            self.data_dict_counter = 0
                            
                        # else:
                        #     print("no data")

                except Exception as e:
                    print()
                    print("Could not read line")
                    print(e.args)

            self.Timer=QtCore.QTimer()
            self.Timer.setInterval(0)
            if self.serialInst.is_open:
                self.Timer.timeout.connect(update_data)
                self.Timer.start()
                

        except Exception as e:
            print()
            print(e.args)   
        
                
        