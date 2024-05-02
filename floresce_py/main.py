import tkinter as TK

import cv2 as CV
from PIL import Image, ImageTk


class App:
    W, H = 800, 450
    VC = CV.VideoCapture(0)

    filters = {
        "RGB": CV.COLOR_BGR2RGB,
        "GRAY": CV.COLOR_BGR2GRAY,
    }

    def __init__(self) -> None:
        self.app = TK.Tk(className="Test")
        self.app.bind("<Escape>", lambda _: self.app.quit())

        controls = TK.Frame(self.app)
        controls.grid()
        TK.Label(controls, text="Filter:").grid(column=0, row=0)

        self.filter = TK.StringVar(controls, "RGB")
        change_filter = TK.OptionMenu(controls, self.filter, *self.filters.keys())
        change_filter.grid(column=1, row=0)

        self.label = TK.Label(self.app)
        self.label.grid()

        self.open_camera()

    def open_camera(self):
        _, frame = self.VC.read()
        frame = CV.resize(frame, (800, 450))
        frame = CV.cvtColor(frame, self.filters[self.filter.get()])

        image = Image.fromarray(frame)
        image = ImageTk.PhotoImage(image=image)
        self.label.photo_image = image
        self.label.configure(image=image)
        self.label.after(20, self.open_camera)


app = App().app
app.mainloop()



