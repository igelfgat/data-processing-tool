from tkinter import *
from tkinter import ttk, filedialog
import pandas as pd

def set_window(root):
    root.title("Pet project")
    root.resizable(True, True)
    w=200
    h=150

    ws = root.winfo_screenwidth()
    wh = root.winfo_screenheight()

    x = int(ws / 2 - w / 2)
    y = int(wh / 2 - h / 2)
    root.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))


def open_csv():
    # Prompt user to select the CSV file
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

    if not file_path:
        return  # User canceled the file selection

    try:
        # Read data from the selected CSV files
        data = pd.read_csv(file_path, encoding='ISO-8859-1')
        print(data)
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}")

root = Tk()
root.configure(background='white')
set_window(root)

# Create a button for opening CSV files and bind it to the open_csv function
open_csv_button = Button(root, text="Open CSV Files", command=open_csv, highlightbackground="white")
open_csv_button.pack(pady=20)

# Create a label to display the result
result_label = Label(root, text="", font=("Helvetica", 10), bg="white")
result_label.pack()

mainloop()