import csv

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
