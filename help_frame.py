from tkinter import *

FONT = ("Arial", 12, "bold")
Title_FONT = ("Arial", 30, "bold")
SUB_TITLE = ("Arial", 18, "bold")
background_colour = "#000000"
foreground_colour = "#ffffff"
DARK_GREEN = "#007500"
BUTTON_FONT = ("Arial", 10, "bold")
gray = "#808080"
ROWS, COLS = 100, 3  # Size of grid.
ROWS_LENGTH = 60  # Number of rows to display.
COLS_LENGTH = 3  # Number of columns to display.


def help(about_image, join, password_record_screen, my_screen):
    window = Toplevel(my_screen)
    # set the titlebar icon of the toplevel window
    photo = PhotoImage(file="images/new_logo_resize.png")
    window.iconphoto(False, photo)

    main_frame = Frame(window, bg=background_colour, relief=RIDGE)
    window.title("About PassReg")
    window.resizable(width=False, height=False)
    window.config(bg=background_colour)
    # window.resizable(width=False, height=False)
    main_frame.grid(row=3, column=0, sticky=NW)
    explanation = """"PassReg" is a dedicated
Password Register.It was
built to help people keep
their passwords secure."""
    canvas = Canvas(main_frame, bg=background_colour)
    canvas.grid(row=0, column=0)

    # Add a canvas in that frame
    vs_bar = Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
    vs_bar.grid(row=0, column=1, sticky=NS)
    canvas.configure(yscrollcommand=vs_bar.set)
    buttons_frame = Frame(canvas, bg=background_colour, bd=2)

    topic_label = Label(buttons_frame, justify=CENTER,
                        padx=10,
                        text="PassReg", font=Title_FONT, fg=foreground_colour, bg=background_colour)
    topic_label.grid(column=0, row=1, sticky='news')
    modified_label = Label(buttons_frame, justify=CENTER,
                           pady=10,
                           text="Last modified: 27 July 2021", font=FONT, fg=foreground_colour, bg=background_colour)
    modified_label.grid(column=0, row=2, sticky='news')
    about_label = Label(buttons_frame, image=about_image, fg=background_colour, bg=background_colour)
    about_label.grid(column=1, row=3, sticky='news')

    description = Label(buttons_frame, justify=LEFT,
                        pady=10,
                        text=explanation, font=FONT, fg=foreground_colour, bg=background_colour)
    description.grid(column=0, row=3, sticky='news')

    first = Label(buttons_frame, justify=LEFT,
                  text="How It Works", font=SUB_TITLE, fg=foreground_colour, bg=background_colour)
    first.grid(column=0, row=4, sticky='news')
    signup = Label(buttons_frame,
                   text="""Create your account:
\n\nCreate your PassReg account by
entering your email address and 
setting a master password.The 
master password secures your
data.It's one password you need
to remember.\n\n""", font=FONT,
                   fg=foreground_colour, bg=background_colour, justify=LEFT)
    signup.grid(column=0, row=5, sticky='news')
    step_1_label = Label(buttons_frame, image=join, fg=background_colour, bg=background_colour)
    step_1_label.grid(column=1, row=5, sticky='news')

    second = Label(buttons_frame, justify=LEFT,
                   text="""Add or Create
stronger passwords:
\n\nYou can add your passwords
manually, or get the help of
PassReg's random password
generator to create strong 
and unique passwords for
each site.Manage passwords
with one click. You can find,
edit or delete yours
records using  PassReg.\n\n\n""", font=FONT, fg=foreground_colour, bg=background_colour)
    second.grid(column=0, row=6, sticky='news')
    step_2_label = Label(buttons_frame, image=password_record_screen, fg=background_colour, bg=background_colour)
    step_2_label.grid(column=1, row=6, sticky='news')
    third = Button(buttons_frame, justify=LEFT, font=FONT, text="Exit", width=10, command=window.destroy)
    third.grid(column=0, row=7)

    vs_bar = Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
    vs_bar.grid(row=0, column=1, sticky=NS)
    canvas.configure(yscrollcommand=vs_bar.set)
    canvas.create_window((0, 0), window=buttons_frame, anchor=NW)
    buttons_frame.update_idletasks()
    bbox = canvas.bbox(ALL)
    w, h = bbox[2] - bbox[1], bbox[3] - bbox[1]
    dw, dh = int((w / COLS) * COLS_LENGTH), int((h / ROWS) * ROWS_LENGTH)
    canvas.configure(scrollregion=bbox, width=dw, height=dh)
