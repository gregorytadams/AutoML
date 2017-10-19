import tkinter as tk
from tkinter import filedialog
import pandas as pd
import AutoCleaning

# To do:
#     Comment each function
#     Encapsulate more code in functions
#     Start documentation file
#     Pull from github to get example data

class Application(tk.Frame):

    def __init__(self, master=None):
        # Init top level 
        super().__init__(master)
        self.pack()

        # Top-level variables
        self.model_list = ["Logistic Regression", "Decision Tree", "Random Forest", "Support Vector Machine"]
        self.models_selected = []
        self.df = None

        # Top-level functions (buttons, file-upload, things to interact with)
        self.create_click_me()
        self.create_file_upload_group()
        self.create_list_of_choices_group()
        # self.create_list_of_choices()
        # self.create_print_all_selections() # test button
        self.create_quit_button()


# General Utility Functions (did I use that term right?):
    def create_instruction_text(self, text_to_display):
        instruction = tk.Label(self, text = text_to_display)
        instruction.pack(side="top")

    # def print_to_user(self, text):
    #     text_to_print = tk.Text(text=)

# Generate Button Functions 
    def create_click_me(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = lambda: print("Say Hello!")
        self.hi_there.pack(side="top")

    def create_file_upload_group(self):

        def create_file_upload_button():

            self.browse_button = tk.Button(self, text="Browse")
            self.browse_button["command"] = initiate_file_upload
            self.browse_button.pack(side="top")

        def initiate_file_upload():
            file = filedialog.askopenfile(parent=root,mode='rb',title='Choose a file')
            self.df = pd.read_csv(file)
            print(AutoCleaning.detect_variables(self.df))
            check_variable_detection_ok(self.df, AutoCleaning.detect_variables(self.df))

        def check_variable_detection_ok(df, type_dict):
            string_to_print = "File uploaded successfully. \n Please check that the following variable types are accurate. If they are not, please resubmit your data \n"
            for col in df.columns:
                string_to_print += f"{col} is a {type_dict[col]} variable \n"
            self.create_instruction_text(string_to_print)

        self.create_instruction_text("Upload your data")
        create_file_upload_button()


    def create_list_of_choices_group(self):

        def create_list_of_choices():
            self.my_multiple_choice = tk.Listbox(self, selectmode="multiple")
            for option in self.model_list:
                self.my_multiple_choice.insert(0, option)
            self.my_multiple_choice.pack()
            self.submit_button = tk.Button(self, text="Submit")
            self.submit_button["command"] = lambda: self.models_selected.append(self.selection_get().split('\n'))
            self.submit_button.pack(side="top")
            # self.destroy()

        def create_print_all_selections():
            self.my_new_button = tk.Button(self)
            self.my_new_button["text"] = "print all selections"
            self.my_new_button["command"] = lambda: print(self.models_selected)
            self.my_new_button.pack()

        self.create_instruction_text("Select which models you want to try")
        create_list_of_choices()
        create_print_all_selections()

    def create_quit_button(self):
        self.quit = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
        self.quit.pack(side="bottom")


if __name__ == "__main__":
    root = tk.Tk()
    # width x height + x_offset + y_offset:
    root.geometry("300x400+30+30") 
    app = Application(master=root)
    app.mainloop()