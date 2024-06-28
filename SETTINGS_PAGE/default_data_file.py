from PyQt5.QtWidgets import *
import pandas as pd
# import os
from SETTINGS_PAGE.change_units import ChangeUnits

class SettingsModule:
    def __init__(self, browse_for_folders_btn, data_file_folder_name, apply_all_changes, vel_mph, vel_kmph, tempC, tempF, Alt_feet, Alter_meters, gyro_dps, gyro_rps, eulers_deg, eulers_rad, GPS_alt_feet, GPS_alt_meters, GPS_speed_mph, GPS_speed_kmph, acc_fps, acc_mps ):

        self.browse_for_folders_btn = browse_for_folders_btn
        self.data_file_folder_name = data_file_folder_name

        self.vel_mph = vel_mph
        self.vel_kmph = vel_kmph

        self.tempC = tempC
        self.tempF = tempF

        self.Alt_feet = Alt_feet
        self.Alter_meters = Alter_meters

        self.gyro_dps = gyro_dps
        self.gyro_rps = gyro_rps

        self.eulers_deg = eulers_deg
        self.eulers_rad = eulers_rad

        self.GPS_alt_feet = GPS_alt_feet
        self.GPS_alt_meters = GPS_alt_meters

        self.GPS_speed_mph = GPS_speed_mph
        self.GPS_speed_kmph = GPS_speed_kmph

        self.acc_fps = acc_fps
        self.acc_mps = acc_mps

        self.apply_all_changes = apply_all_changes

        browse_for_folders_btn.clicked.connect(self.get_file)

    def get_file(self):

        self.file_path, _ = QFileDialog.getOpenFileName(
            None,
            "Select a CSV File",
            "",
            "CSV Files (*.csv)",
        )

        self.data_file_folder_name.setText(self.file_path)
        
        # file_name = os.path.basename(self.file_path)
        print("FILE SET")
        try:
            df = pd.read_csv(self.file_path)
            # obj = ChangeUnits(df)
            
            vel = df["VELOCITY (m/h)"]
            temp = df["TEMPERATURE (C)"]
            alt = df["ALTITUDE (Feet(AGL))"]

            gyro_X = df["GYRO_X (deg/s)"]
            gyro_Y = df["GYRO_Y (deg/s)"]
            gyro_Z = df["GYRO_Z (deg/s)"]

            pitch = df["PITCH (deg)"]
            yaw = df["YAW (deg)"]
            roll = df["ROLL (deg)"]

            GPS_alt = df["GPS_ALTITUDE (Feet(AGL))"]
            GPS_speed = df["GPS_SPEED (m/h)"]
            
            acc_X = df["ACCELERATION_X (ft/s sq)"]
            acc_Y = df["ACCELERATION_Y (ft/s sq)"]
            acc_Z = df["ACCELERATION_Z (ft/s sq)"]

        except Exception as e:
            print("COULD NOT READ CSV FILE")
            print(e.args)

        try:
            self.vel_mph.clicked.connect(lambda: ChangeUnits.velocity_units(vel, df, flag = "m/h"))
        except Exception as e:
            print("ISSUE IN VELOCITY m/h RADIO BUTTON")
            print(e.args)
        
        try:
            self.vel_kmph.clicked.connect(lambda: ChangeUnits.velocity_units(vel, df, flag = "km/h"))
        except Exception as e:
            print("ISSUE IN VELOCITY km/h RADIO BUTTON")
            print(e.args)    

        try:
            self.GPS_speed_mph.clicked.connect(lambda: ChangeUnits.GPS_speed_units(GPS_speed, df, flag = "m/h"))
        except Exception as e:
            print("ISSUE IN GPS SPEED km/h RADIO BUTTON")
            print(e.args)    

        try:
            self.GPS_speed_kmph.clicked.connect(lambda: ChangeUnits.GPS_speed_units(GPS_speed, df, flag = "km/h"))
        except Exception as e:
            print("ISSUE IN GPS SPEED km/h RADIO BUTTON")
            print(e.args)  

        try:
            self.tempC.clicked.connect(lambda: ChangeUnits.temperature_units(temp, df, flag = "C"))
        except Exception as e:
            print("ISSUE IN TEMPERATURE C RADIO BUTTON")
            print(e.args)

        try:
            self.tempF.clicked.connect(lambda: ChangeUnits.temperature_units(temp, df, flag = "F"))
        except Exception as e:
            print("ISSUE IN TEMPERATURE F RADIO BUTTON")
            print(e.args)

        try:
            self.Alt_feet.clicked.connect(lambda: ChangeUnits.altitude_units(alt, df, flag = "Feet (AGL)"))
        except Exception as e:
            print("ISSUE IN ALTITUDE FEET(AGL) RADIO BUTTON")
            print(e.args)
        
        try:
            self.Alter_meters.clicked.connect(lambda: ChangeUnits.altitude_units(alt, df, flag = "Meters (AGL)"))
        except Exception as e:
            print("ISSUE IN ALTITUDE METERS(AGL) RADIO BUTTON")
            print(e.args)

        try:
            self.gyro_dps.clicked.connect(lambda: ChangeUnits.gyro_units(gyro_X, gyro_Y, gyro_Z, df, flag = "deg"))
        except Exception as e:
            print("ISSUE IN GYRO DPS RADIO BUTTON")
            print(e.args)

        try:
            self.gyro_rps.clicked.connect(lambda: ChangeUnits.gyro_units(gyro_X, gyro_Y, gyro_Z, df, flag = "rad"))
        except Exception as e:
            print("ISSUE IN GYRO RPS RADIO BUTTON")
            print(e.args)
        
        try:
            self.eulers_deg.clicked.connect(lambda: ChangeUnits.euler_units(pitch, yaw, roll, df, flag = "deg"))
        except Exception as e:
            print("ISSUE IN EULER'S ANGLE DEGREES RADIO BUTTON")
            print(e.args)

        try:
            self.eulers_rad.clicked.connect(lambda: ChangeUnits.euler_units(pitch, yaw, roll, df, flag = "rad"))
        except Exception as e:
            print("ISSUE IN EULER'S ANGLE RAD RADIO BUTTON")
            print(e.args)

        try:
            self.GPS_alt_feet.clicked.connect(lambda: ChangeUnits.GPS_altitude_units(GPS_alt, df, flag = "Feet (AGL)"))
        except Exception as e:
            print("ISSUE IN GPS ALTITUDE FEET RADIO BUTTON")
            print(e.args)

        try:
            self.GPS_alt_meters.clicked.connect(lambda: ChangeUnits.GPS_altitude_units(GPS_alt, df, flag = "Meters (AGL)"))
        except Exception as e:
            print("ISSUE IN GPS ALTITUDE METERS RADIO BUTTON")
            print(e.args)  

        try:
            self.acc_fps.clicked.connect(lambda: ChangeUnits.accelerometer_units(acc_X, acc_Y, acc_Z, df, flag = "ft/s²"))
        except Exception as e:
            print("ISSUE IN ACCELEROMETER ft/s² RADIO BUTTON")
            print(e.args)

        try:
            self.acc_mps.clicked.connect(lambda: ChangeUnits.accelerometer_units(acc_X, acc_Y, acc_Z, df, flag = "m/s²"))
        except Exception as e:
            print("ISSUE IN ACCELEROMETER m/s² RADIO BUTTON")
            print(e.args)   

        try:
            self.apply_all_changes.clicked.connect(lambda: ChangeUnits.apply_all(df, self.file_path))
        except Exception as e:
            print("ISSUE IN APPLY ALL CHANGES BUTTON")
            print(e.args)
