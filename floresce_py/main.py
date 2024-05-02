import tkinter as TK

import cv2 as CV
from PIL import Image, ImageTk


class App:
    W, H = 800, 450
    VC = CV.VideoCapture(0)

    def __init__(self) -> None:
        self.app = TK.Tk(className="Test")
        self.app.bind("<Escape>", lambda _: self.app.quit())

        change_filter = TK.Button(self.app, text="Change Filter")
        change_filter.pack()

        self.label = TK.Label(self.app)
        self.label.pack()

        self.open_camera()

    def open_camera(self):
        _, frame = self.VC.read()
        frame = CV.resize(frame, (800, 450))
        frame = CV.cvtColor(frame, CV.COLOR_BGR2RGB)

        image = Image.fromarray(frame)
        image = ImageTk.PhotoImage(image=image)
        self.label.photo_image = image
        self.label.configure(image=image)
        self.label.after(20, self.open_camera)


app = App().app
app.mainloop()

