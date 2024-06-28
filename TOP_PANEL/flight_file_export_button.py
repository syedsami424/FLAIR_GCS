# import sys
# import csv
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QVBoxLayout, QWidget

# class FlightFileExportButton:
#     def __init__(self, flightfileexportbtn):
#         self.flightfileexportbtn = flightfileexportbtn
        
#         try:  
#             print("hiiiiiiiiii")      
#             self.flightfileexportbtn.clicked.connect(self.fileexport)
#         except Exception as e:
#             print(e.args)
        
#     def fileexport(self):
#         try:
#             file_path = "C:/Users/DELL/Downloads/merge_data.csv"
#             csv_data = self.read_csv_file(file_path)
#         except Exception as e:
#             print(e.args)
        
#         if not csv_data:
#             print("No data to save.")
#             return

#         # Open a file dialog to select a location to save the file
#         options = QFileDialog.Options()
#         save_path, _ = QFileDialog.getSaveFileName(self, "Save Flight File", "", "CSV Files (*.csv);;All Files (*)", options=options)
#         if save_path:
#             self.write_csv_file(save_path, csv_data)


import sys
import csv
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QVBoxLayout, QWidget

class FlightFileExportButton:
    def __init__(self, flightfileexportbtn):
        self.flightfileexportbtn = flightfileexportbtn
        
        try:  
            print("hiiiiiiiiii")      
            self.flightfileexportbtn.clicked.connect(self.fileexport)
        except Exception as e:
            print(e.args)
        
    def fileexport(self):
        try:
            file_path = "C:/Users/DELL/Downloads/merge_data.csv"
            csv_data = self.read_csv_file(file_path)
        except Exception as e:
            print(e.args)
        
        if not csv_data:
            print("No data to save.")
            return

        # Open a file dialog to select a location to save the file
        options = QFileDialog.Options()
        save_path, _ = QFileDialog.getSaveFileName(None, "Save Flight File", "", "CSV Files (*.csv);;All Files (*)", options=options)
        if save_path:
            self.write_csv_file(save_path, csv_data)
    
    def read_csv_file(self, file_path):
        """Read the CSV file and return the data."""
        try:
            with open(file_path, mode='r', newline='') as file:
                reader = csv.reader(file)
                csv_data = [row for row in reader]
            return csv_data
        except Exception as e:
            print(f"Error reading file: {e}")
            return None

    def write_csv_file(self, save_path, csv_data):
        """Write the CSV data to the specified file."""
        try:
            with open(save_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(csv_data)
            print(f"File saved successfully to {save_path}")
        except Exception as e:
            print(f"Error writing file: {e}")
