def input_schedule():
    import PySimpleGUI as sg

    # Setup the window
    layout = [
        [sg.Text("予定csv作成:")],
        [sg.Text("Date", size=(15, 1)), sg.InputText(key="date")],
        [sg.Text("Task", size=(15, 1)), sg.InputText(key="task")],
        [sg.Text("Name", size=(15, 1)), sg.InputText(key="name")],
        [sg.Button("Submit")]
    ]

    window = sg.Window("予定").Layout(layout)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Submit":
            # Format input
            date = datetime.datetime.strptime(values["date"], "%b %d %Y")

            # Create an object
            entry = RecordEntry(date, values["task"], values["name"])
