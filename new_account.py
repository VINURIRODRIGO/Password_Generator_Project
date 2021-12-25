import json
from tkinter import *
from tkinter import messagebox

FONT = ("Arial", 12, "bold")
background_colour = "#000000"
foreground_colour = "#ffffff"
DARK_GREEN = "#007500"
BUTTON_FONT = ("Arial", 10, "bold")


def crate_new_account(email_address, user_password, F_name, L_name):
    new_data = {email_address: {
        "Password": user_password,
        "First Name": F_name,
        "Last Name": L_name}}
    try:
        with open("Json_files/customer_data.json", mode="r") as text:
            json_data = json.load(text)
            with open("Json_files/customer_data.json", mode="w") as text_data:
                # getting the updated data
                json.dump(json_data, text_data, indent=4)
            if email_address not in json_data:
                json_data.update(new_data)
                with open("Json_files/customer_data.json", mode="w") as text_data:
                    # getting the updated data
                    json.dump(json_data, text_data, indent=4)
            else:
                messagebox.showinfo(title="Update Data",
                                    message=f"Already registered")
                is_yes = messagebox.askyesno(title="Update Data",
                                             message=f"Do you want to Sign in")
                if is_yes:
                    return "sign in"
                else:
                    return "clear"
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        # when the file is not created or when the file is empty
        with open("Json_files/customer_data.json", mode="w") as text:
            json.dump(new_data, text, indent=4)


class NewAccount:
    def __init__(self, frame, image, main_screen):
        super().__init__()
        self.frame_3 = frame
        self.image = image
        self.F_name_entry = Entry(self.frame_3, width=20, font=FONT)
        self.L_name_entry = Entry(self.frame_3, width=20, font=FONT)
        self.email_address_entry = Entry(self.frame_3, width=20, font=FONT)
        self.conform_password_entry = Entry(self.frame_3, width=20, font=FONT, show="*")
        self.user_password_entry = Entry(self.frame_3, width=20, font=FONT, show="*")
        self.main_screen = main_screen

    def registration_data(self):

        # Frames
        self.main_screen.geometry("560x650")
        canvas_1 = Canvas(self.frame_3, width=252, height=252, highlightthickness=0, bg=background_colour)
        canvas_1.create_image(100, 100, image=self.image)
        canvas_1.grid(column=0, row=0, columnspan=2)

        # Labels
        F_name = Label(self.frame_3, text="First Name*:", justify="left", fg=foreground_colour, font=FONT,
                       bg=background_colour)
        F_name.grid(column=0, row=1, pady=(0, 5), ipady=5)
        self.F_name_entry.grid(column=1, row=1, columnspan=2, sticky="ew", ipady=5, pady=5)
        self.F_name_entry.focus()
        L_name = Label(self.frame_3, text="Last Name*: ", fg=foreground_colour, font=FONT, bg=background_colour)
        L_name.grid(column=0, row=2, pady=(0, 5), ipady=5)
        email_address = Label(self.frame_3, text="Email address*: ", fg=foreground_colour, font=FONT,
                              bg=background_colour)
        email_address.grid(column=0, row=3, pady=(0, 5), ipady=5)
        user_password = Label(self.frame_3, text="Password*: ", fg=foreground_colour, font=FONT, bg=background_colour)
        user_password.grid(column=0, row=4, pady=(0, 5), ipady=5)
        conform_password = Label(self.frame_3, text="Conform Password*: ", fg=foreground_colour, font=FONT,
                                 bg=background_colour)
        conform_password.grid(column=0, row=5, pady=(0, 5), ipady=5)
        password_length = Label(self.frame_3, text="For Password use 8 or more characters with a mix of letters, "
                                                   "numbers & symbols",
                                justify="center", fg=DARK_GREEN, font=("Arial", 10, "bold"), bg=background_colour)
        password_length.grid(column=0, row=6, padx=5, sticky="ew", pady=10, columnspan=2)

        # Entries
        self.L_name_entry.grid(column=1, row=2, columnspan=2, sticky="ew", ipady=5, pady=5)
        self.email_address_entry.grid(column=1, row=3, columnspan=2, sticky="ew", ipady=5, pady=5)
        self.user_password_entry.grid(column=1, row=4, columnspan=2, sticky="ew", ipady=5, pady=5)

        self.conform_password_entry.grid(column=1, row=5, columnspan=2, sticky="ew", ipady=5, pady=5)
