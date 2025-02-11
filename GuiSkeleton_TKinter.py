import tkinter as tk
from tkinter import ttk

class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set the title of our application
        self.title("My Minimal GUI")

        # Create a frame for widgets to sit in
        main_frame = ttk.Frame(self, padding="3 3 12 12")
        main_frame.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        # Add a label widget
        self.label = ttk.Label(main_frame, text="Enter some text:")
        self.label.grid(column=0, row=0, sticky=tk.W)

        # Add a text entry (or text field) widget
        self.entry = ttk.Entry(main_frame, width=30)
        self.entry.grid(column=1, row=0, sticky=(tk.W, tk.E))

        # Add a button widget
        self.button = ttk.Button(main_frame, text="Print to console", command=self.print_to_console)
        self.button.grid(column=1, row=1, sticky=(tk.W, tk.E))

    def print_to_console(self):
        # Get the text from the entry widget and print it to the console
        text = self.entry.get()
        print(text)

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()

