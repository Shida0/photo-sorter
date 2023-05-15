import os
import threading

from tkinter import messagebox
import customtkinter as ctk

from sorter import sort_

ctk.set_default_color_theme("green")
ctk.set_appearance_mode("dark")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.dir_ = None
        self.lenght = None
        self.formats = ["jpeg", "jpg", "png"]

        #create interface
        self.label = ctk.CTkLabel(self, text="choose a folder", font=ctk.CTkFont(size=35),)
        self.label.pack(anchor="center", pady=(100, 50))

        self.btn1 = ctk.CTkButton(self, text="choose", height=25, font=ctk.CTkFont(size=20),
                                  command=self.folder)
        self.btn1.pack(anchor="center", pady=(0, 100))

        self.btn2 = ctk.CTkButton(self, text="start", height=25, font=ctk.CTkFont(size=20),
                                  command=self.start)
        self.btn2.pack(anchor="center")

        self.label2 = ctk.CTkLabel(self, text="", font=ctk.CTkFont(size=20),)
        self.label2.pack(anchor="s", side="bottom", pady=(0, 30))

        self.geometry("700x600")

    #function to set folder
    def folder(self):
        try:
            path = ctk.filedialog.askdirectory(title="Select a folder")
            os.chdir(path)
            self.label.configure(text=path)
            self.dir_ = path
            self.lenght = len(self.find_img(path))
        except Exception:
            er = messagebox.showerror(title="error", message="choose a folder please!")    

    #function which return a list of images
    def find_img(self, path):
        files = []
        for filename in os.listdir(path):
            try:
                if filename.split(".")[1] in self.formats:
                    files.append(filename)             
            except IndexError:
                pass

        return files

    #function starting sort images
    def start(self):        
        t1 = threading.Thread(target=sort_, args=(self.dir_, self.label2, self.lenght, self.find_img,)).start()
   

if __name__ == "__main__":
    app = App()
    app.mainloop()