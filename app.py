import customtkinter as ctk 
import tkinter as ttk 
from pytube import YouTube 
import moviepy.editor as mpe
import os 

def download_video():
    print('clicked')

#Create a root Window 
root = ctk.CTk()
ctk.set_appearance_mode("system")
ctk.set_appearance_mode("dark")
ctk.set_appearance_mode("dark")

#title 
root.title("Youtube-Downloader!")

#set min and max 
root.geometry("720x480")
root.minsize(720 , 480)
root.maxsize(1080 , 720)

#frame #1 
content_frame = ctk.CTkFrame(root)
content_frame.pack(fill = ctk.BOTH, expand=True , padx=10 , pady=10)

#create a label w entry widget 
url_label = ctk.CTkLabel(content_frame, text="Enter the youtube URL: ")
entry_url = ctk.CTkEntry(content_frame, width=400 , height=40)
url_label.pack(pady=10)
entry_url.pack(pady=10)

#Create a download Button
download_button = ctk.CTkButton(content_frame, text="Download" , command=download_video)
download_button.pack(pady=10)

#create resolution drop down list 
resolutions = ["720p" , "480p" , "360p"]
resolution_var = ttk.StringVar()


resolution_dropdown =ctk.CTkComboBox(content_frame , values= resolutions ,variable=resolution_var)
resolution_dropdown.pack(pady=10)
resolution_dropdown.set("720p")

#create aa progress bar 
progress_bar = ctk.CTkLabel(content_frame, text="0%")
#progress_bar.pack(pady=10)

progress_bar = ctk.CTkProgressBar(content_frame , width=400)
progress_bar.set(0.6)
#progress_bar.pack(pady=10)

#create a status label 
status_label = ctk.CTkLabel(content_frame, text="Downloaded")
#status_label.pack(pady=10)

#start  z
root.mainloop()