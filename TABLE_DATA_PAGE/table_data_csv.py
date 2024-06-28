from PyQt5.QtWidgets import *
import csv
import shutil

class Appender:
    def __init__(self, table_data_csv_display, line, counter):

        self.table_data_csv_display = table_data_csv_display
        self.line = line
        self.counter = counter

    def append_to_table(self):
        try:
            row_position = self.table_data_csv_display.rowCount()
            self.table_data_csv_display.setRowCount(row_position + 1)

            for j, value in enumerate(self.line):
                item = QTableWidgetItem(str(value))
                self.table_data_csv_display.setItem(row_position, j, item)

        except Exception as e:
            print()
            print("EXCEPTION OCCURRED IN TABLE DATA CSV MODULE")
            print(e.args)
        
        try:
            filename = f"Data_{self.counter}.csv"
            with open(filename, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(self.line)

        except Exception as e:
            print()
            print("EXCEPTION OCCURRED IN WRITING TO CSV FILE")
            print(e.args)

    def download_file(table_data_csv_display):
        try:
            with open("DEFAULT_DATA.csv", 'w', newline='') as file:
                writer = csv.writer(file)
                
                headers = []
                for j in range(table_data_csv_display.columnCount()):
                    headers.append(table_data_csv_display.horizontalHeaderItem(j).text())
                # print(headers)
                writer.writerow(headers)

                for row in range(table_data_csv_display.rowCount()):
                    row_data = []
                    for col in range(table_data_csv_display.columnCount()):
                        item = table_data_csv_display.item(row, col)
                        if item is not None:
                            row_data.append(item.text())
                        else:
                            row_data.append("")
                    writer.writerow(row_data)

                print("File downloaded")

            # src = r"C:\Users\iqras\OneDrive\Documents\Team Sammard\Team_Sammard\SA_CUP_2024\FLAIR_GUI\DEFAULT_DATA.csv"
            # dest1 = r"C:\Users\iqras\OneDrive\Documents\Team Sammard\Team_Sammard\SA_CUP_2024\FLAIR_GUI\backups\backup1.csv"
            # dest2 = r"C:\Users\iqras\OneDrive\Documents\Team Sammard\Team_Sammard\SA_CUP_2024\FLAIR_GUI\backups\backup2.csv"
            # dest3 = r"C:\Users\iqras\OneDrive\Documents\Team Sammard\Team_Sammard\SA_CUP_2024\FLAIR_GUI\backups\backup3.csv"

            # shutil.copyfile(src, dest1)
            # shutil.copyfile(src, dest2)
            # shutil.copyfile(src, dest3)

            # print("Backups created")

        except Exception as e:
            print()
            print("EXCEPTION OCCURRED WHILE SAVING FILE")
            print(e.args)