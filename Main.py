from tkinter import *
from tkinter import ttk, filedialog
import pandas as pd

class UserWindow:
    def __init__(self, root, title, width, height):
        # Constructor to initialize the UserWindow instance
        self.root = root
        self.title = title
        self.width = width
        self.height = height
        self.set_window()  # Call the set_window method to configure the window

    def set_window(self):
        # Method to configure the window
        self.root.title(self.title)
        self.root.resizable(True, True)
        ws = self.root.winfo_screenwidth()
        wh = self.root.winfo_screenheight()
        x = int(ws / 2 - self.width / 2)
        y = int(wh / 2 - self.height / 2)
        self.root.geometry("{0}x{1}+{2}+{3}".format(self.width, self.height, x, y))
        # Set the window geometry (size and position)

def open_csv():
    # Create a new Tkinter window for the CSV editor
    editor_window = Toplevel(root)
    editor = UserWindow(editor_window, "CSV file", 400, 200)

    # Prompt user to select the CSV file
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

    if not file_path:
        return  # User canceled the file selection

    try:
        # Read data from the selected CSV files
        csv_data = pd.read_csv(file_path, encoding='ISO-8859-1')
        create_window_with_csv_data(csv_data, editor_window)  # Pass the editor window
        editor_window.mainloop()  # Start the CSV editor window's event loop
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}")

def create_window_with_csv_data(data, window):
    # Create labels for column names
    for j, column_name in enumerate(data.columns):
        label = Label(window, text=column_name)
        label.grid(row=0, column=j)

    # Create labels for all data elements
    for i in range(len(data)):
        for j, column_name in enumerate(data.columns):
            cell_value = data.iat[i, j]
            label = Label(window, text=cell_value)
            label.grid(row=i + 1, column=j)

    # Create Entry widgets for the "Price" column
    for i in range(len(data)):
        # Get the value from the "Price" column in the CSV data
        cell_value = data.iat[i, data.columns.get_loc("Price")]

        # Create an Entry widget for editing the "Price" column
        entry = Entry(window, width=15)
        entry.insert(0, str(cell_value))  # Insert the cell value into the Entry widget
        entry.grid(row=i + 1, column=data.columns.get_loc("Price"))  # Place the Entry widget in the grid

root = Tk()
root.configure(background='white')

# Create an instance of the CustomWindow class to set up the main window
main_window = UserWindow(root, "Main Window", 200, 150)  # Customize title and size

# Create a button for opening CSV files and bind it to the open_csv function
open_csv_button = Button(root, text="Open CSV Files", command=open_csv, highlightbackground="white")
open_csv_button.pack(pady=20)

# Create a label to display the result
result_label = Label(root, text="", font=("Helvetica", 10), bg="white")
result_label.pack()

root.mainloop()
