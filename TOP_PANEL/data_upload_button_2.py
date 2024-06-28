from PyQt5.QtWidgets import QFileDialog
import csv

class DataUploadButton:
    def __init__(self, data_upload_button, altAx1, altCanvas1, altAx2, altCanvas2, speedAx, speedCanvas, pressAx1, pressCanvas1, pressAx2, pressCanvas2, voltAx1, voltCanvas1, voltAx2, voltCanvas2, accAx, accCanvas, gyroAx, gyroCanvas, velAx, velCanvas, altVgpsaltAx, altVgpsaltCanvas, gpsspeedVvelAx, gpsspeedVvelCanvas, RSSI_value, hp_temperature_disp, #new
                                                  packet_count_text, mission_time_text, 
                                                  hp_alt_label, notif_alt_label, 
                                                  hp_gpsSpeed_label, 
                                                  accelerometer_value_x, accelerometer_value_y, accelerometer_value_z,
                                                  hp_pressure_label, hp_voltage_label, 
                                                  gyrometer_value_x, gyrometer_value_y, gyrometer_value_z,
                                                  pitch, yaw, roll,
                                                  GPS_hp_lat, GPS_hp_lon, gps_heading_disp, SATS_value, #gps_heading_disp -> new
                                                  table_data_csv_display, 
                                                  notif_press_label, 
                                                  notif_velocity_label,
                                                  notif_voltage_label,
                                                  notif_Velocity_label, #new
                                                  notif_GPSspeed_label, #new
                                                  notif_alt_label_2, #new
                                                  notif_GPSalt_label, #new
                                                  notif_gyro_label, 
                                                  notif_acc_label, #new
                                                # GPS_time_label, GPS_date_label, 
                                                  GPS_SATSno_label, GPS_lat_label, GPS_lon_label, 
                                                  GPS_altitude_label, GPS_speed_label, altitude_label_graphs_sidepanel, velocity_label_graphs_sidepanel, temperature_label_graphs_sidepanel, acc_x_label_graphs_sidepanel, acc_y_label_graphs_sidepanel, acc_z_label_graphs_sidepanel, gyro_x_label_graphs_sidepanel, gyro_y_label_graphs_sidepanel, gyro_z_label_graphs_sidepanel, gps_heading_label, mag_heading_label, trigger_value):

        self.data_upload_button = data_upload_button
        
        self.altitude_label_graphs_sidepanel = altitude_label_graphs_sidepanel
        self.velocity_label_graphs_sidepanel = velocity_label_graphs_sidepanel
        self.temperature_label_graphs_sidepanel = temperature_label_graphs_sidepanel
        self.acc_x_label_graphs_sidepanel = acc_x_label_graphs_sidepanel
        self.acc_y_label_graphs_sidepanel = acc_y_label_graphs_sidepanel
        self.acc_z_label_graphs_sidepanel = acc_z_label_graphs_sidepanel
        self.gyro_x_label_graphs_sidepanel = gyro_x_label_graphs_sidepanel
        self.gyro_y_label_graphs_sidepanel = gyro_y_label_graphs_sidepanel
        self.gyro_z_label_graphs_sidepanel = gyro_z_label_graphs_sidepanel
        
        self.gps_heading_label = gps_heading_label
        self.mag_heading_label = mag_heading_label
        self.trigger_value = trigger_value

        self.altAx1 = altAx1
        self.altCanvas1 = altCanvas1
        self.altAx2 = altAx2
        self.altCanvas2 = altCanvas2

        self.speedAx = speedAx
        self.speedCanvas = speedCanvas

        self.pressAx1 = pressAx1
        self.pressCanvas1 = pressCanvas1
        self.pressAx2 = pressAx2
        self.pressCanvas2 = pressCanvas2

        self.voltAx1 = voltAx1
        self.voltCanvas1 = voltCanvas1
        self.voltAx2 = voltAx2
        self.voltCanvas2 = voltCanvas2

        # self.tempAx = tempAx
        # self.tempCanvas = tempCanvas

        self.accAx = accAx
        self.accCanvas = accCanvas
        
        self.gyroAx = gyroAx
        self.gyroCanvas = gyroCanvas
        
        self.velAx = velAx
        self.velCanvas = velCanvas
        
        self.altVgpsaltAx = altVgpsaltAx
        self.altVgpsaltCanvas = altVgpsaltCanvas

        self.gpsspeedVvelAx = gpsspeedVvelAx
        self.gpsspeedVvelCanvas = gpsspeedVvelCanvas
        
        self.RSSI_value = RSSI_value #new
        self.hp_temperature_disp = hp_temperature_disp #new
        self.packet_count_text = packet_count_text
        self.mission_time_text = mission_time_text 
        self.hp_alt_label = hp_alt_label
        self.notif_alt_label = notif_alt_label
        self.hp_gpsSpeed_label = hp_gpsSpeed_label
        self.accelerometer_value_x = accelerometer_value_x
        self.accelerometer_value_y = accelerometer_value_y
        self.accelerometer_value_z = accelerometer_value_z
        self.hp_pressure_label = hp_pressure_label
        self.hp_voltage_label = hp_voltage_label
        self.gyrometer_value_x = gyrometer_value_x
        self.gyrometer_value_y = gyrometer_value_y
        self.gyrometer_value_z = gyrometer_value_z
        self.pitch = pitch
        self.yaw = yaw
        self.roll = roll
        self.GPS_hp_lat = GPS_hp_lat
        self.GPS_hp_lon = GPS_hp_lon
        self.gps_heading_disp = gps_heading_disp
        self.SATS_value = SATS_value #gps_heading_disp -> new
        self.table_data_csv_display = table_data_csv_display
        self.notif_press_label = notif_press_label 
        self.notif_velocity_label = notif_velocity_label
        self.notif_voltage_label = notif_voltage_label
        self.notif_Velocity_label = notif_Velocity_label #new
        self.notif_GPSspeed_label = notif_GPSspeed_label #new
        self.notif_alt_label_2 = notif_alt_label_2 #new
        self.notif_GPSalt_label = notif_GPSalt_label #new
        self.notif_gyro_label = notif_gyro_label 
        self.notif_acc_label = notif_acc_label #new
        # self.GPS_time_label = GPS_time_label
        # self.GPS_date_label = GPS_date_label
        self.GPS_SATSno_label = GPS_SATSno_label
        self.GPS_lat_label = GPS_lat_label
        self.GPS_lon_label = GPS_lon_label
        self.GPS_altitude_label = GPS_altitude_label
        self.GPS_speed_label = GPS_speed_label

        data_upload_button.clicked.connect(self.upload_data)

    def upload_data(self):
        # self.tempAx.clear()

        def plot_data(ax, plt_canvas, time, data, colour="b"):
            try:
                ax.plot(time, data)

                plt_canvas.draw()

            except Exception as e:
                print("Error in DataUploadButton ---> plot_data")
                print(e.args)

        def plot_vs_graphs(ax, plt_canvas, time, data1, data2, color="b"):
            try:
                ax.plot(time, data1)
                ax.plot(time, data2)

                plt_canvas.draw()

            except Exception as e:
                print("Error in DataUploadButton ---> plot_vs_graphs")
                print(e.args)

        def plot_triple_graphs(ax, plt_canvas, time, data1, data2, data3):
            try:
                ax.plot(time, data1)
                ax.plot(time, data2)
                ax.plot(time, data3)

                plt_canvas.draw()

            except Exception as e:
                print("Error in DataUploadButton ---> plot_triple_graphs")
                print(e.args)

        self.time = []
        self.altitude = []
        self.GPS_speed = []
        self.pressure = []
        self.voltage = []
        self.temperature = []
        self.acc_x = []
        self.acc_y = []
        self.acc_z = []
        self.gyro_x = []
        self.gyro_y = []
        self.gyro_z = []
        self.velocity = []
        self.gps_altitude = []
        self.states_value = []
        self.gps_time = []
        # self.gps_heading = []
        # self.magnetometer_heading = []
        
        self.time1 = []
        self.altitude1 = []
        self.GPS_speed1 = []
        self.pressure1 = []
        self.voltage1 = []
        self.temperature1 = []
        self.acc_x1 = []
        self.acc_y1 = []
        self.acc_z1 = []
        self.gyro_x1 = []
        self.gyro_y1 = []
        self.gyro_z1 = []
        self.velocity1 = []
        self.gps_altitude1 = []
        self.states_value1 = []
        # self.gps_heading1 = []
        # self.magnetometer_heading1 = []
        
        self.time_apog = []
        self.altitude_apog = []
        self.GPS_speed_apog = []
        self.pressure_apog = []
        self.voltage_apog = []
        self.temperature_apog = []
        self.acc_x_apog = []
        self.acc_y_apog = []
        self.acc_z_apog = []
        self.gyro_x_apog = []
        self.gyro_y_apog = []
        self.gyro_z_apog = []
        self.velocity_apog = []
        self.gps_altitude_apog = []
        self.states_value_apog = []
        # self.gps_heading_apog = []
        # self.magnetometer_heading_apog = []
        
        


        file_path, _ = QFileDialog.getOpenFileName(
            None,
            "Select a CSV File",
            "",
            "CSV Files (*.csv)",
        )
        # print(file_path)
        if not file_path:
            print("No file selected.")
            return

        if file_path:
            with open(file_path, "r") as f:

                reader_obj = csv.reader(f)
                next(reader_obj)
                n0=0
                n1=0
                n2=0
                n3=0
                i=0
                self.count=0
                self.ind=0
 
                
                for row in reader_obj:
                    if(float(row[25])==1.00) or (float(row[25])==2.00):
                        try:
                            current_pkt_count = str(row[1])
                        except (IndexError, ValueError) as e:
                            current_pkt_count = None
                        try:
                            time_text = str(row[0])
                        except (IndexError, ValueError) as e:
                            time_text = None
                        try:                        
                            GPS_time = str(row[11])
                        except (IndexError, ValueError) as e:
                            # print("hiii")
                            # print(e.args)
                            GPS_time = None
                        try:                    
                            GPS_date = str(row[12])
                        except (IndexError, ValueError) as e:
                            GPS_date = None
                        try:                 
                            sats = int(row[13])                        
                        except (IndexError, ValueError) as e:
                            sats = None
                        try:                        
                            RSSI = int(row[28])
                        except (IndexError, ValueError) as e:
                            RSSI = "n/a"                       
                        
                        try:
                            trigger_value = str(row[27])
                        except (IndexError, ValueError) as e:
                            trigger_value = "n/a"
                        try:
                            pitch_text = str(row[21])
                        except:
                            pitch_text = None
                        try:
                            yaw_text = str(row[22])
                        except:
                            yaw_text = None
                        try: 
                            roll_text = str(row[23])
                        except:
                            roll_text = None
                        try: 
                            gps_hp_lat_text = str(row[6])
                        except:
                            gps_hp_lat_text = None
                        try: 
                            gps_hp_lon_text = str(row[7])
                        except:
                            gps_hp_lon_text = None
                        try:
                            mag_heading = str(row[24])
                        except:
                            mag_heading = None
                        try:
                            GPS_heading = str(row[10])
                        except:
                            GPS_heading = None
                        
                        # try:
                        #     self.trigger_value.setText(str(f"TRIGGER: {trigger_value}"))
                        # except:
                        #     self.trigger_value.setText("n/a")             
                        try:
                            self.time.append(float(row[0]))
                        except:
                            self.time.append(None)
                        try:
                            self.altitude.append(float(row[3]))
                        except:
                            self.altitude.append(None)
                        try:
                            self.GPS_speed.append(float(row[9]))
                        except:
                            self.GPS_speed.append(None)
                        try:
                            self.pressure.append(float(row[4]))                        
                        except:
                            self.pressure.append(None)
                        try:
                            self.voltage.append(float(row[25]))
                        except:
                            self.voltage.append(None)
                        try:
                            self.temperature.append(float(row[5]))
                        except:
                            self.temperature.append(None)
                        try:
                            self.velocity.append(float(row[20]))
                        except:
                            self.velocity.append(None)
                        try:
                            self.gps_altitude.append(float(row[8]))
                        except:
                            self.gps_altitude.append(None)
                        try:
                            self.gyro_x.append(float(row[17]))
                        except:
                            self.gyro_x.append(None)
                        try:
                            self.gyro_y.append(float(row[18]))
                        except:
                            self.gyro_y.append(None)
                        try:
                            self.gyro_z.append(float(row[19]))
                        except:
                            self.gyro_z.append(None)

                        try:
                            self.acc_x.append(float(row[14]))
                        except:
                            self.acc_x.append(None)

                        try:
                            self.acc_y.append(float(row[15]))
                        except:
                            self.acc_y.append(None)
                        
                        try:
                            self.acc_z.append(float(row[16]))
                        except:
                            self.acc_z.append(None)
                        try:
                            self.states_value.append(float(row[26]))
                        except:
                            self.states_value.append(None)
                        try:
                            self.states_value.append(float(row[27]))
                        except:
                            self.states_value.append(None)
                        self.count+=1
                print(self.count)
                print("\n")
                        
                for l in range (0,self.count):
                    if(self.states_value[l]==2.00):
                        self.ind = l
                        break
                    
                for l in range (0,self.ind-1,10):
                    self.time1.append(self.time[l])
                    self.altitude1.append(self.altitude[l])
                    self.GPS_speed1.append(self.GPS_speed[l])
                    self.pressure1.append(self.pressure[l])
                    self.voltage1.append(self.voltage[l])
                    self.temperature1.append(self.temperature[l])
                    self.acc_x1.append(self.acc_x[l])
                    self.acc_y1.append(self.acc_y[l])
                    self.acc_z1.append(self.acc_z[l])
                    self.gyro_x1.append(self.gyro_x[l])
                    self.gyro_y1.append(self.gyro_y[l])
                    self.gyro_z1.append(self.gyro_z[l])
                    self.velocity1.append(self.velocity[l])
                    self.gps_altitude1.append(self.gps_altitude[l])
                    
                
                self.time1.append(self.time[self.ind-1])
                self.altitude1.append(self.altitude[self.ind-1])
                self.GPS_speed1.append(self.GPS_speed[self.ind-1])
                self.pressure1.append(self.pressure[self.ind-1])
                self.voltage1.append(self.voltage[self.ind-1])
                self.temperature1.append(self.temperature[self.ind-1])
                self.acc_x1.append(self.acc_x[self.ind-1])
                self.acc_y1.append(self.acc_y[self.ind-1])
                self.acc_z1.append(self.acc_z[self.ind-1])
                self.gyro_x1.append(self.gyro_x[self.ind-1])
                self.gyro_y1.append(self.gyro_y[self.ind-1])
                self.gyro_z1.append(self.gyro_z[self.ind-1])
                self.velocity1.append(self.velocity[self.ind-1])
                self.gps_altitude1.append(self.gps_altitude[self.ind-1])
                
                self.time_apog.append(self.time[self.ind-1])
                self.altitude_apog.append(0)
                self.GPS_speed_apog.append(0)
                self.pressure_apog.append(0)
                self.voltage_apog.append(0)
                self.temperature_apog.append(0)
                self.acc_x_apog.append(0)
                self.acc_y_apog.append(0)
                self.acc_z_apog.append(0)
                self.gyro_x_apog.append(0)
                self.gyro_y_apog.append(0)
                self.gyro_z_apog.append(0)
                self.velocity_apog.append(0)
                self.gps_altitude_apog.append(0)
                
                self.time_apog.append(self.time[self.ind-1])
                self.altitude_apog.append(self.altitude[self.ind-1])
                self.GPS_speed_apog.append(self.GPS_speed[self.ind-1])
                self.pressure_apog.append(self.pressure[self.ind-1])
                self.voltage_apog.append(self.voltage[self.ind-1])
                self.temperature_apog.append(self.temperature[self.ind-1])
                self.acc_x_apog.append(self.acc_x[self.ind-1])
                self.acc_y_apog.append(self.acc_y[self.ind-1])
                self.acc_z_apog.append(self.acc_z[self.ind-1])
                self.gyro_x_apog.append(self.gyro_x[self.ind-1])
                self.gyro_y_apog.append(self.gyro_y[self.ind-1])
                self.gyro_z_apog.append(self.gyro_z[self.ind-1])
                self.velocity_apog.append(self.velocity[self.ind-1])
                self.gps_altitude_apog.append(self.gps_altitude[self.ind-1])
                
                
                for l in range (self.ind,self.count,10):
                    self.time1.append(self.time[l])
                    self.altitude1.append(self.altitude[l])
                    self.GPS_speed1.append(self.GPS_speed[l])
                    self.pressure1.append(self.pressure[l])
                    self.voltage1.append(self.voltage[l])
                    self.temperature1.append(self.temperature[l])
                    self.acc_x1.append(self.acc_x[l])
                    self.acc_y1.append(self.acc_y[l])
                    self.acc_z1.append(self.acc_z[l])
                    self.gyro_x1.append(self.gyro_x[l])
                    self.gyro_y1.append(self.gyro_y[l])
                    self.gyro_z1.append(self.gyro_z[l])
                    self.velocity1.append(self.velocity[l])
                    self.gps_altitude1.append(self.gps_altitude[l])
                    
                self.lind = len(self.time1)-1
                # for l in range(0,len(self.time1)):
                #     print(self.time1[l])
                #     print("\n")
            try:
                DataUpload_altitude = plot_data(self.altAx1, self.altCanvas1, self.time1, self.altitude1, color="blue")
                DataUpload_notif_altitude = plot_data(self.altAx2, self.altCanvas2, self.time1, self.altitude1, colour="blue")
                DataUpload_altitude_apog = plot_data(self.altAx1, self.altCanvas1, self.time_apog, self.altitude_apog, color="red")
                DataUpload_notif_altitude_apog = plot_data(self.altAx2, self.altCanvas2, self.time_apog, self.altitude_apog, color="red")
            except Exception as e:
                print(e.args)

            DataUpload_speed = plot_data(self.speedAx, self.speedCanvas, self.time1, self.GPS_speed1)

            DataUpload_press = plot_data(self.pressAx1, self.pressCanvas1, self.time1, self.pressure1)
            DataUpload_notif_press = plot_data(self.pressAx2, self.pressCanvas2, self.time1, self.pressure1)

            DataUpload_voltage = plot_data(self.voltAx1, self.voltCanvas1, self.time1, self.voltage1)
            DataUpload_notif_voltage = plot_data(self.voltAx2, self.voltCanvas2, self.time1, self.voltage1)
            
            DataUpload_speed_apog = plot_data(self.speedAx, self.speedCanvas, self.time_apog, self.GPS_speed_apog)

            DataUpload_press_apog = plot_data(self.pressAx1, self.pressCanvas1, self.time_apog, self.pressure_apog)
            DataUpload_notif_press_apog = plot_data(self.pressAx2, self.pressCanvas2, self.time_apog, self.pressure_apog)

            DataUpload_voltage_apog = plot_data(self.voltAx1, self.voltCanvas1, self.time_apog, self.voltage_apog)
            DataUpload_notif_voltage_apog = plot_data(self.voltAx2, self.voltCanvas2, self.time_apog, self.voltage_apog)

            # DataUpload_temperature = plot_data(self.tempAx, self.tempCanvas, self.time, self.temperature)

            try:
                DataUpload_accelerometer = plot_triple_graphs(self.accAx, self.accCanvas, self.time1, self.acc_x1, self.acc_y1, self.acc_z1)
                DataUpload_accelerometer_apog = plot_triple_graphs(self.accAx, self.accCanvas, self.time_apog, self.acc_x_apog, self.acc_y_apog, self.acc_z_apog)
            except Exception as e:
                print(e.args)
            try:
                DataUpload_gyrometer = plot_triple_graphs(self.gyroAx, self.gyroCanvas, self.time1, self.gyro_x1, self.gyro_y1, self.gyro_z1)
                DataUpload_gyrometer = plot_triple_graphs(self.gyroAx, self.gyroCanvas, self.time_apog, self.gyro_x_apog, self.gyro_y_apog, self.gyro_z_apog)
            except Exception as e:
                print(e.args)

            DataUpload_velocity = plot_data(self.velAx, self.velCanvas, self.time1, self.velocity1)

            DataUpload_altVgpsalt = plot_vs_graphs(self.altVgpsaltAx, self.altVgpsaltCanvas, self.time1, self.altitude1, self.gps_altitude1)

            DataUpload_gpsspeedVvel = plot_vs_graphs(self.gpsspeedVvelAx, self.gpsspeedVvelCanvas, self.time1, self.GPS_speed1, self.velocity1)
            
            DataUpload_velocity_apog = plot_data(self.velAx, self.velCanvas, self.time_apog, self.velocity_apog)

            DataUpload_altVgpsalt_apog = plot_vs_graphs(self.altVgpsaltAx, self.altVgpsaltCanvas, self.time_apog, self.altitude_apog, self.gps_altitude_apog)

            DataUpload_gpsspeedVvel_apog = plot_vs_graphs(self.gpsspeedVvelAx, self.gpsspeedVvelCanvas, self.time_apog, self.GPS_speed_apog, self.velocity_apog)
            print(sats)
            self.mission_time_text.setText(time_text)
            self.packet_count_text.setText(current_pkt_count)
            print("set txt\n")
            try:
                self.RSSI_value.setText(str(RSSI))
            except:
                self.RSSI_value.setText("n/a")
            try:
                # self.GPS_time_label.setText(f"TIME: {GPS_time}")
                # self.GPS_date_label.setText(f"DATE: {GPS_date}")
                self.GPS_SATSno_label.setText(f"SATS NO.: {str(sats)}")
                self.GPS_lat_label.setText(f"LATITUDE: {gps_hp_lat_text} °")
                self.GPS_lon_label.setText(f"LONGITUDE: {gps_hp_lon_text} °")
                self.GPS_altitude_label.setText(f"ALTITUDE: {self.gps_altitude1[self.lind]} Feet (AGL)")
                self.GPS_speed_label.setText(f"SPEED: {self.GPS_speed1[self.lind]} m/h")
                try:
                    self.mag_heading_label.setText(f"(R)MAG HEADING: {str(mag_heading)}°")
                except:
                    self.mag_heading_label.setText(f"(R)MAG HEADING: n/a")
                try:
                    self.gps_heading_label.setText(f"(L)GPS HEADING: {str(GPS_heading)}°")
                except:
                    print("gps heading is none")
                    self.gps_heading_label.setText(f"(L)GPS HEADING: n/a")

                self.accelerometer_value_x.setText(f"{str(self.acc_x1[self.lind])} ft/s²")
                self.accelerometer_value_y.setText(f"{str(self.acc_y1[self.lind])} ft/s²")
                self.accelerometer_value_z.setText(f"{str(self.acc_z1[self.lind])} ft/s²")

                self.gyrometer_value_x.setText(f"{str(self.gyro_x1[self.lind])} °/s")
                self.gyrometer_value_y.setText(f"{str(self.gyro_y1[self.lind])} °/s")
                self.gyrometer_value_z.setText(f"{str(self.gyro_z1[self.lind])} °/s")

                self.pitch.setText(f"{str(pitch_text)} °")
                self.yaw.setText(f"{yaw_text} °")
                self.roll.setText(f"{roll_text} °")

                self.GPS_hp_lat.setText(f"Lat: {gps_hp_lat_text} °")
                self.GPS_hp_lon.setText(f"Lon: {gps_hp_lon_text} °")
                
                self.altitude_label_graphs_sidepanel.setText(f"ALTITUDE: {self.altitude1[self.lind]} Feet (AGL)")
                self.velocity_label_graphs_sidepanel.setText(f"SPEED: {self.velocity1[self.lind]} m/h")
                self.temperature_label_graphs_sidepanel.setText(f"TEMPERATURE: {str(self.temperature1[self.lind])}°C")

                self.acc_x_label_graphs_sidepanel.setText(f"ACC_X: {str(self.acc_x1[self.lind])} ft/s²")
                self.acc_y_label_graphs_sidepanel.setText(f"ACC_Y: {str(self.acc_y1[self.lind])} ft/s²")
                self.acc_z_label_graphs_sidepanel.setText(f"ACC_Z: {str(self.acc_z1[self.lind])} ft/s²")

                self.gyro_x_label_graphs_sidepanel.setText(f"GYRO_X: {str(self.gyro_x1[self.lind])} °/s")
                self.gyro_y_label_graphs_sidepanel.setText(f"GYRO_Y: {str(self.gyro_y1[self.lind])} °/s")
                self.gyro_z_label_graphs_sidepanel.setText(f"GYRO_Z: {str(self.gyro_z1[self.lind])} °/s")

                self.hp_temperature_disp.setText(str(self.temperature1[self.lind]))
                
                try:
                    if (len(trigger_value)) == 4:
                        try:
                            last_two_bits = trigger_value[-2:]
                            # print(last_two_bits)
                            if last_two_bits == "00":
                                trigger_html = (
                                    f"TRIGGER: {trigger_value[:-2]}"
                                    f"<span style='color:red;'>{last_two_bits[0]}</span>"
                                    f"<span style='color:red;'>{last_two_bits[1]}</span>"
                                )

                            elif last_two_bits == "10":
                                trigger_html = (
                                    f"TRIGGER: {trigger_value[:-2]}"
                                    f"<span style='color:green;'>{last_two_bits[0]}</span>"
                                    f"<span style='color:red;'>{last_two_bits[1]}</span>"
                                )

                            elif last_two_bits == "01":
                                trigger_html = (
                                    f"TRIGGER: {trigger_value[:-2]}"
                                    f"<span style='color:red;'>{last_two_bits[0]}</span>"
                                    f"<span style='color:green;'>{last_two_bits[1]}</span>"
                                )

                            elif last_two_bits == "11":
                                trigger_html = (
                                    f"TRIGGER: {trigger_value[:-2]}"
                                    f"<span style='color:green;'>{last_two_bits[0]}</span>"
                                    f"<span style='color:green;'>{last_two_bits[1]}</span>"
                                )

                            self.trigger_value.setMarkdown(f"TRIGGER: {str(trigger_value)}")
                            self.trigger_value.setHtml(f"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                            "p, li { white-space: pre-wrap; }\n"
                            "</style></head><body style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
                            f"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">{trigger_html}</p></body></html>")
                        except:
                            self.trigger_value.setMarkdown(f"TRIGGER: n/a")

                except:
                    self.trigger_value.setMarkdown(f"TRIGGER: n/a")
                            
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
                # self.gps_heading_disp.setText(str(line[]))

            except Exception as e:
                print(e.args)
