import csv
import PySimpleGUI as sg
from datetime import datetime
import logging



def input_schedule():


    # Setup the window
    layout = [
        [sg.Text("予定csv作成:")],
        [sg.Text("Date", size=(15, 1)), sg.InputText(key="date")],
        [sg.Text("Task", size=(15, 1)), sg.InputText(key="task")],
        [sg.Text("Name", size=(15, 1)), sg.InputText(key="name")],
        [sg.Text("test")]
        [sg.Button("Submit")],

    ]

    window = sg.Window("予定").Layout(layout)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Submit":
            # Format input
            date = datetime.strptime(values["date"], "%b %d %Y")

            # Create an object
            # entry = RecordEntry(date, values["task"], values["name"])

class RecordManagement:
    def __init__(self):
        self.data = []

    def add_entry(self, date, task, name):
        entry = {
            "date": date,

            "task": task,
            "name": name
        }
        self.data.append(entry)

    def write_csv(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["date", "task", "name"])
            writer.writeheader()
            for record in self.data:
                writer.writerow(record)

# Create the object
records = RecordManagement()

# Adding entries
records.add_entry("Jul 17 2020", "Testing", "John Doe")
records.add_entry("Jul 18 2020", "Coding", "Jane Doe")

# Writing to a CSV file
records.write_csv("records.csv")


def main():
    input_schedule()

if __name__ == "__main__":
    main()
