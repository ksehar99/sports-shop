import tkinter as tk
from tkinter import ttk
from tkinter import Label, Frame, PhotoImage,Button, IntVar, OptionMenu, StringVar
from update_cart import UpdateCart


class Window(tk.Tk):  # class window created and is inheriting from built-in class tk.Tk of tkinter
    def __init__(self, update):  # constructor created for the class
        super().__init__()

        self['background'] = "grey"
        self.title("Sports website")
        self.geometry('600x470+150+50')
        self.sports = Label(text="Welcome to the Online Sports Shop", bg="grey", fg="black", font=("Calibre", 20))
        self.sports.pack()

        # Create a frame for the second label and the dropdown menu
        self.label_dropdown_frame = Frame(self, bg="black")
        self.label_dropdown_frame.pack(pady=10)

        self.sports2 = Label(self.label_dropdown_frame, text="Do you wish to update your sports gear? You are at the right place!",
                             bg="black", fg="white", font=("Arial", 10), relief="raised")
        self.sports2.pack(side="left", padx=10)

        # Options for the dropdown menu
        self.options = ["update_cart"]

        # Datatype of menu text
        self.clicked = StringVar()

        # Initial menu text
        self.clicked.set("other options")

        # Create Dropdown menu
        self.drop = OptionMenu(self.label_dropdown_frame, self.clicked, *self.options)
        self.drop.pack(side="left")

        # Create a frame for the image
        self.image_frame = Frame(self, bg="#AEC6CF")
        self.image_frame.pack()

        self.img3 = PhotoImage(file='S&K (2).png')
        self.img_lab2 = Label(self.image_frame, image=self.img3)
        self.img_lab2.pack()

        self.tabs = Tabs(self, update)   # instantiating the tab class within the Window class to demonstrate composition relationship

        self.button = Button(self, text='Proceed', command=lambda: self.proceed_and_destroy)
        self.button.pack()

    def proceed_and_destroy(self):
        self.update.save_cart()
        self.destroy()


class Tabs: # class designated for creating tabs
    def __init__(self, parent, update):
        self.notebook = ttk.Notebook(parent)
        self.tabs = [
            ('Cricket Gear', '#000080'),
            ('Football Gear', '#000080'),
            ('Basketball Gear', '#000080'),
            ('Baseball Gear', '#000080'),
            ('Soccer Gear', '#000080'),
            ('Tennis Gear', '#000080'),
            ('Hockey Gear', '#000080'),
            ('Other Gear', '#000080')
        ]

        self.create_tabs()
        self.notebook.pack(fill='both', expand=True)

        self.update = update

    def create_tabs(self):
        for tab_text, tab_color in self.tabs:
            tab = ttk.Frame(self.notebook)
            self.notebook.add(tab, text=tab_text)

            # Create a frame to contain the buttons and checkboxes within the tabs
            button_frame = Frame(tab, bg='#d3d3d3')
            button_frame.pack(side='top', fill='x')

            if tab_text == "Cricket Gear":
                var1 = IntVar()
                self.create_label_with_buttons(button_frame, "Helmet", 2000, var1, 0)

                var2 = IntVar()
                self.create_label_with_buttons(button_frame, "Shoes", 4000, var2, 1)

                var3 = IntVar()
                self.create_label_with_buttons(button_frame, "Jersey", 1800, var3, 2)

                var4 = IntVar()
                self.create_label_with_buttons(button_frame, "Ball", 600, var4, 3)

                var5 = IntVar()
                self.create_label_with_buttons(button_frame, "Bat", 1200, var5, 4)

            if tab_text == "Football Gear":
                var6 = IntVar()
                self.create_label_with_buttons(button_frame, "Football", 1500, var6, 5)

                var7 = IntVar()
                self.create_label_with_buttons(button_frame, "Football Jersey", 1800, var7, 6)

                var8 = IntVar()
                self.create_label_with_buttons(button_frame, "Football shoes", 3500, var8, 7)

                var9 = IntVar()
                self.create_label_with_buttons(button_frame, "Football nets", 2500, var9, 8)

                var10 = IntVar()
                self.create_label_with_buttons(button_frame, "Football T-Shirt", 1500, var10, 9)

            if tab_text == "Basketball Gear":
                var11 = IntVar()
                self.create_label_with_buttons(button_frame, "Basketball", 2000, var11, 10)

                var12 = IntVar()
                self.create_label_with_buttons(button_frame, "Crew socks", 500, var12, 11)

                var13 = IntVar()
                self.create_label_with_buttons(button_frame, "Shooter sleeves", 800, var13, 12)

                var14 = IntVar()
                self.create_label_with_buttons(button_frame, "Backpack", 2500, var14, 13)

                var15 = IntVar()
                self.create_label_with_buttons(button_frame, "Skinny hairband", 300, var15, 14)

            if tab_text == "Baseball Gear":
                var16 = IntVar()
                self.create_label_with_buttons(button_frame, "Baseball Cleats", 3500, var16, 15)

                var17 = IntVar()
                self.create_label_with_buttons(button_frame, "Baseball leg guards", 1500, var17, 16)

                var18 = IntVar()
                self.create_label_with_buttons(button_frame, "Baseball chest protector", 2000, var18, 17)

                var19 = IntVar()
                self.create_label_with_buttons(button_frame, "Baseball T-shirt", 1200, var19, 18)

                var20 = IntVar()
                self.create_label_with_buttons(button_frame, "Baseball bat", 2500, var20, 19)

            if tab_text == "Soccer Gear":
                var21 = IntVar()
                self.create_label_with_buttons(button_frame, "Soccer Cleats", 3000, var21, 20)

                var22 = IntVar()
                self.create_label_with_buttons(button_frame, "Soccer Shoes", 2800, var22, 21)

                var23 = IntVar()
                self.create_label_with_buttons(button_frame, "Soccer pants", 1500, var23, 22)

                var24 = IntVar()
                self.create_label_with_buttons(button_frame, "Soccer T-Shirt", 1000, var24, 25)

                var25 = IntVar()
                self.create_label_with_buttons(button_frame, "Soccer ball", 700, var25, 26)

            if tab_text == "Tennis Gear":
                var26 = IntVar()
                self.create_label_with_buttons(button_frame, "Tennis ball", 600, var26, 27)

                var27 = IntVar()
                self.create_label_with_buttons(button_frame, "Tennis T-shirt", 1200, var27, 28)

                var28 = IntVar()
                self.create_label_with_buttons(button_frame, "Tennis shoes", 3500, var28, 29)

                var29 = IntVar()
                self.create_label_with_buttons(button_frame, "Tennis rackets", 4500, var29, 30)

                var30 = IntVar()
                self.create_label_with_buttons(button_frame, "Tennis P-cap", 500, var30, 31)

            if tab_text == "Hockey Gear":
                var31 = IntVar()
                self.create_label_with_buttons(button_frame, "Hockey Jersey", 1800, var31, 32)

                var32 = IntVar()
                self.create_label_with_buttons(button_frame, "Hockey Hat", 400, var32, 33)

                var33 = IntVar()
                self.create_label_with_buttons(button_frame, "Hockey Stick", 3000, var33, 34)

                var34 = IntVar()
                self.create_label_with_buttons(button_frame, "Hockey ball", 600, var34, 35)

                var35 = IntVar()
                self.create_label_with_buttons(button_frame, "Hockey shoes", 3500, var35, 36)

            if tab_text == "Other Gear":
                var36 = IntVar()
                self.create_label_with_buttons(button_frame, "T-shirts", 1200, var36, 37)

                var37 = IntVar()
                self.create_label_with_buttons(button_frame, "Shorts", 800, var37, 38)

                var38 = IntVar()
                self.create_label_with_buttons(button_frame, "Jackets", 2500, var38, 39)

                var39 = IntVar()
                self.create_label_with_buttons(button_frame, "Hoddie", 2000, var39, 40)

                var40 = IntVar()
                self.create_label_with_buttons(button_frame, "Cleats", 3000, var40, 41)



    def increase(self, var): # function created to increase the quantity on clicking the + button
        var.set(var.get() + 1)

    def decrease(self, var): # function created to decrease the quantity on clicking the - button
        if var.get()>0:
            var.set(var.get() - 1)

    def create_label_with_buttons(self, parent, text, price, var, row):
        Label(parent, text=text, fg='black', bg='#d3d3d3', anchor='w').grid(row=row, column=0, sticky='w', padx=5)
        Label(parent, text=f'Rs {price}', fg='black', bg='#d3d3d3', anchor='w').grid(row=row, column=1, padx=5)
        Button(parent, text="+", command=lambda: self.increase(var), fg='black', bg='#d3d3d3').grid(row=row, column=2, padx=5)
        Label(parent, textvariable=var, fg='black', bg='#d3d3d3', width=3, anchor='e').grid(row=row, column=3, padx=5)
        Button(parent, text="-", command=lambda: self.decrease(var), fg='black', bg='#d3d3d3').grid(row=row, column=4, padx=5)


u = UpdateCart()
window = Window(u)
window.mainloop()

# from view_cart import ViewCart
#
# ViewCart()
