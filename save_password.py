import json
from tkinter import messagebox

from password import password_checker


class SavePassword:
    def __init__(self, website, username, password, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.website = website
        self.username = username
        self.password = password
        self.data = {self.website: {
            "Email": self.username,
            "Password": self.password
        }}
        self.validation()

    def validation(self):
        if len(self.website) == 0 or len(self.password) == 0 or len(self.username) == 0:
            messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
        # elif
        else:
            pass

    def json_data(self):
        if password_checker(self.password):

            self.save_to_file()
        else:
            is_true = messagebox.askyesno(title="Weak Password",
                                          message=f"The password is not strong enough.\n\n"
                                                  f"Do you really want to save this password?")
            if is_true:
                self.save_to_file()

    def save_to_file(self):
        is_ok = messagebox.askokcancel(title=self.website, message=f"These are the details entered:"
                                                                   f"\n\nEmail: {self.username}\n\nPassword: "
                                                                   f"{self.password}\n\n "
                                                                   f"Is it ok to save?")
        if is_ok:
            try:
                with open(f"Json_files/{self.first_name}_{self.last_name}.json", mode="r")as text:
                    # getting the old data
                    json_data = json.load(text)
                    if self.website not in json_data:
                        # getting old data and adding the new data
                        json_data.update(self.data)
                        with open(f"Json_files/{self.first_name}_{self.last_name}.json", mode="w")as text_data:
                            # getting the updated data
                            json.dump(json_data, text_data, indent=4)
                    else:
                        is_yes = messagebox.askyesno(title="Update Data",
                                                     message=f"Do you want to Update {self.website} Data")
                        if is_yes:
                            json_data[self.website]["Email"] = self.username
                            json_data[self.website]["Password"] = self.password
                            with open(f"Json_files/{self.first_name}_{self.last_name}.json", mode="w")as text_data:
                                # getting the updated data
                                json.dump(json_data, text_data, indent=4)

            except (FileNotFoundError, json.decoder.JSONDecodeError):
                # when the file is not created or when the file is empty
                with open(f"Json_files/{self.first_name}_{self.last_name}.json", mode="w")as text:
                    json.dump(self.data, text, indent=4)
