import tkinter as tk
from tkinter import ttk
from main3 import recognize_sign  # Import the recognize_sign function

class HandSignRecognitionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hand Sign Recognition")

        # Variables for hand sign recognition
        self.recognition_callback = None

        # Landing Page
        self.landing_frame = ttk.Frame(root, padding=(20, 20, 20, 20))
        self.landing_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        project_label = ttk.Label(self.landing_frame, text="Hand Sign Recognition Project", font=('Helvetica', 20, 'bold'))
        project_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        start_button = ttk.Button(self.landing_frame, text="Start Recognition", command=self.start_recognition)
        start_button.grid(row=1, column=0, columnspan=2, pady=(0, 20))

        # Recognition Frame
        self.recognition_frame = ttk.Frame(root, padding=(20, 20, 20, 20))
        self.video_label = ttk.Label(self.recognition_frame)
        self.video_label.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    def set_recognition_callback(self, callback):
        self.recognition_callback = callback

    def start_recognition(self):
        if self.recognition_callback:
            self.landing_frame.grid_remove()
            self.recognition_frame.grid()

            # Execute the recognition callback
            self.recognition_callback()

if __name__ == "__main__":
    root = tk.Tk()
    app = HandSignRecognitionApp(root)

    # Set the recognition callback
    app.set_recognition_callback(lambda: recognize_sign(root, app.recognition_frame))

    root.mainloop()
