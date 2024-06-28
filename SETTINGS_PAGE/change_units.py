import math

class ChangeUnits:
    
    def velocity_units(value, df, flag):

        if flag == "m/h":
            try:
                df["VELOCITY (m/h)"] = value
                # df.to_csv('DEFAULT_DATA.csv', index=False)
                print("VELOCITY UNITS SET TO m/h")

            except Exception as e:
                print("AN ERROR OCCURED")
                print(e.args)

        elif flag == "km/h":
            try:
                value_kmph = value.apply(lambda x: f"{x * 1.60934:.3f}")
                df["VELOCITY (m/h)"] = value_kmph
                # df.to_csv('DEFAULT_DATA.csv', index=False)
                print("VELOCITY UNITS SET TO km/h")

            except Exception as e:
               print("AN ERROR OCCURED")
               print(e.args)

    def GPS_speed_units(value, df, flag):

        if flag == "m/h":
            try:
                df["GPS_SPEED (m/h)"] = value
                # df.to_csv('DEFAULT_DATA.csv', index=False)
                print("GPS SPEED UNITS SET TO m/h")

            except Exception as e:
                print(e.args)

        elif flag == "km/h":
            try:
                value_kmph = value.apply(lambda x: f"{x * 1.60934:.3f}")
                df["GPS_SPEED (m/h)"] = value_kmph
                # df.to_csv('DEFAULT_DATA.csv', index=False)
                print("GPS SPEED UNITS SET TO km/h")

            except Exception as e:
                print(e.args)
            
            # print(value_kmph)

    def temperature_units(temp, df, flag):
        
        if flag == "C":
            try:
                df["TEMPERATURE (C)"] = temp
                # df.to_csv('DEFAULT_DATA.csv', index=False)
                print("TEMPERATURE UNITS SET TO CELCIUS")
            except Exception as e:
                print(e.args)

        elif flag == "F":
            try:
                temp_df_fahrenheit = temp.apply(lambda x: f"{(9/5) * x + 32:.3f}")
                df["TEMPERATURE (C)"] = temp_df_fahrenheit
                # df.to_csv('DEFAULT_DATA.csv', index=False)
                print("TEMPERATURE UNITS SET TO FARENHEIT")
            except Exception as e:
                print(e.args)

    def altitude_units(alt, df, flag):

        if flag == "Feet (AGL)":
            try:
                df["ALTITUDE (Feet(AGL))"] = alt
                # df.to_csv('DEFAULT_DATA.csv', index=False)
                print("ALTITUDE UNITS SET TO FEET")
            except Exception as e:
                print(e.args)

        elif flag == "Meters (AGL)":
            try:
                alt_meters = alt.apply(lambda x: f"{x * 0.3048:.3f}")
                df["ALTITUDE (Feet(AGL))"] = alt_meters
                # df.to_csv('DEFAULT_DATA.csv', index=False)
                print("ALTITUDE UNITS SET TO METERS")
            except Exception as e:
                print(e.args)            


    def GPS_altitude_units(alt, df, flag):

        if flag == "Feet (AGL)":
            try:
                df["GPS_ALTITUDE (Feet(AGL))"] = alt
                # df.to_csv('DEFAULT_DATA.csv', index=False)
                print("GPS ALTITUDE UNITS SET TO FEET")
            except Exception as e:
                print(e.args)            

        elif flag == "Meters (AGL)":
            try:
                alt_meters = alt.apply(lambda x: f"{x * 0.3048:.3f}")
                df["GPS_ALTITUDE (Feet(AGL))"] = alt_meters
                # df.to_csv('DEFAULT_DATA.csv', index=False)
                print("GPS ALTITUDE UNITS SET TO METERS")
            except Exception as e:
                print(e.args)            

    
    def gyro_units(X, Y, Z, df, flag):

        if flag == "deg":
            try:
                df["GYRO_X (deg/s)"] = X
                df["GYRO_Y (deg/s)"] = Y
                df["GYRO_Z (deg/s)"] = Z
                # df.to_csv('DEFAULT_DATA.csv', index=False)
                print("GYRO UNITS SET TO DEGREES")
            except Exception as e:
                print(e.args)

        elif flag == "rad":
            try:
                rad_X = X.apply(lambda x: f"{x * (math.pi / 180):.3f}")
                rad_Y = Y.apply(lambda x: f"{x * (math.pi / 180):.3f}")
                rad_Z = Z.apply(lambda x: f"{x * (math.pi / 180):.3f}")
                df["GYRO_X (deg/s)"] = rad_X
                df["GYRO_Y (deg/s)"] = rad_Y
                df["GYRO_Z (deg/s)"] = rad_Z
                # df.to_csv('DEFAULT_DATA.csv', index=False)
                print("GYRO UNITS SET TO RADIAN")
            except Exception as e:
                print(e.args)

    def euler_units(X, Y, Z, df, flag):

        if flag == "deg":
            try:
                df["PITCH (deg)"] = X
                df["YAW (deg)"] = Y
                df["ROLL (deg)"] = Z
                # df.to_csv('DEFAULT_DATA.csv', index=False)
                print("EULER'S ANGLE UNITS SET TO DEGREES")
            except Exception as e:
                print(e.args)

        elif flag == "rad":
            try:
                rad_X = X.apply(lambda x: f"{x * (math.pi / 180):.3f}")
                rad_Y = Y.apply(lambda x: f"{x * (math.pi / 180):.3f}")
                rad_Z = Z.apply(lambda x: f"{x * (math.pi / 180):.3f}")
                df["PITCH (deg)"] = rad_X
                df["YAW (deg)"] = rad_Y
                df["ROLL (deg)"] = rad_Z
                # df.to_csv('DEFAULT_DATA.csv', index=False)
                print("EULER'S ANGLE UNITS SET TO RADIAN")
            except Exception as e:
                print(e.args)

    def accelerometer_units(X, Y, Z, df, flag):

        if flag == "ft/s²":
            try:
                df["ACCELERATION_X (ft/s sq)"] = X
                df["ACCELERATION_Y (ft/s sq)"] = Y
                df["ACCELERATION_Z (ft/s sq)"] = Z
                # df.to_csv('DEFAULT_DATA.csv', index=False)
                print("ACCELEROMETER UNITS SET TO ft/s²")
            except Exception as e:
                print(e.args)
    
        elif flag == "m/s²":
            try:
                acc_X = X.apply(lambda x: f"{x * 0.3048:.3f}")
                acc_Y = Y.apply(lambda x: f"{x * 0.3048:.3f}")
                acc_Z = Z.apply(lambda x: f"{x * 0.3048:.3f}")
                df["ACCELERATION_X (ft/s sq)"] = acc_X
                df["ACCELERATION_Y (ft/s sq)"] = acc_Y
                df["ACCELERATION_Z (ft/s sq)"] = acc_Z
                # df.to_csv('DEFAULT_DATA.csv', index=False)
                print("ACCELEROMETER UNITS SET TO m/s²")
            except Exception as e:
                print(e.args)

    def apply_all(df, file_path):
        df.to_csv(file_path, index=False)
        print("===================================")
        print("All settings applied")