import face_recognition

from tkinter import messagebox
import os
import threading

formats = ["jpeg", "jpg", "png"]

def sort_(path, label, lenght, find_img):    
    #create folders
    if not os.path.exists("landscapes"):
        os.mkdir("landscapes")

    if not os.path.exists("peoples"):
        os.mkdir("peoples")
        
    for img in os.listdir(path):
        text = f"{lenght - len(find_img(os.curdir))}/{lenght} is done!"
        print(text)
        label.configure(text=text)

        #sort images to folders
        try:
            if img.split(".")[1] in formats:
                rec_img = face_recognition.load_image_file(img)
                if face_recognition.face_locations(rec_img):
                    os.rename(img, f"peoples/{img}")  
                    print("person")                                    
                else:
                    os.rename(img, f"landscapes/{img}")  
                    print("landscape")                                     
        except IndexError:
            continue

        if len(find_img(os.curdir)) == 0:
                print("yes")
                info = messagebox.showinfo(message="Finish!")
                break