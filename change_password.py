from tkinter import *

small_font = ("Arial", 10, "bold")
FONT = ("Arial", 12, "bold")
background_colour = "#000000"
foreground_colour = "#ffffff"
DARK_GREEN = "#007500"
BUTTON_FONT = ("Arial", 10, "bold")


class ChangePassword:
    def __init__(self, frame, image, main_screen):
        self.frame_5 = frame
        self.image = image
        self.new_password_entry = ""
        self.conf_new_password_entry = ""
        self.verification_details()
        main_screen.geometry("600x450")

    def verification_details(self):

        # frames
        self.frame_5.grid(column=0, row=0)
        canvas = Canvas(self.frame_5, width=189, height=189, highlightthickness=0, bg=background_colour)
        # Displaying the logo
        canvas.create_image(95, 95, image=self.image)
        canvas.grid(column=0, row=0, columnspan=2)

        new_password = Label(self.frame_5, text="Create password*: ", fg=foreground_colour, font=FONT,
                             bg=background_colour)
        new_password.grid(column=0, row=1, pady=(0, 5), ipady=5)
        self.new_password_entry = Entry(self.frame_5, width=20, font=FONT, show="*")
        self.new_password_entry.grid(column=1, row=1, columnspan=2, sticky="ew", ipady=5, pady=5)
        self.new_password_entry.focus()
        conf_new_password = Label(self.frame_5, text="Confirm password*:", fg=foreground_colour, font=FONT,
                                  bg=background_colour)
        conf_new_password.grid(column=0, row=2, pady=(0, 5), ipady=5)
        self.conf_new_password_entry = Entry(self.frame_5, width=20, font=FONT, show="*")
        self.conf_new_password_entry.grid(column=1, row=2, columnspan=2, sticky="ew", ipady=5, pady=5)
        password_length = Label(self.frame_5, text="Use 8 or more characters with a mix of letters, numbers & symbols",
                                justify="center", fg=DARK_GREEN, font=FONT, bg=background_colour)
        password_length.grid(column=0, row=3, padx=5, sticky="ew", pady=10, columnspan=2)
