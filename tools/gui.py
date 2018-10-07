from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilenames
from PIL import Image, ImageTk
from circle import Circle


global bg_color, max_size
bg_color = "white"
max_size = (100, 100)


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
        # Should be renamed to 'path_of_image'
        self.chosen_image = str

    def init_window(self):
        self.master.title("*Give Name to Project*")
        self.pack(fill=BOTH, expand=1)

        # Image chooser button (For Processing)
        choose_img = Button(self,
                            text="Choose Image",
                            command=self.choose_image,
                            width=10)

        show_img = Button(self,
                          text="Show Image",
                          command=self.show_image,
                          width=10)

        choose_img.grid()
        show_img.grid()

    def choose_image(self):
        """Assign a tuple to /"chosen_image/" containing the paths for all chosen images."""
        self.chosen_image = askopenfilenames()

    def show_image(self):
        for path in self.chosen_image:
            circles = Circle(path)
            circles.detect_circles()
            load = Image.open("images/{}.png".format(circles.new_filename))
            load.thumbnail(max_size, Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)

            img = Label(self, bg=bg_color, text="Image", image=render)
            img.image = render
            img.grid(column=2)


root = Tk()
# Change attributes of window
root.configure(bg=bg_color)
root.geometry("800x800")
app = Window(root)
root.mainloop()
