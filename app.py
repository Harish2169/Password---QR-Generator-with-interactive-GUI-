import customtkinter as ctk 
import tkinter as ttk 
import os 

def converted_link():
    global status_label  
    url = entry_url.get()
    print(url)
    if url: 
        # Open a new window for displaying QR code and copy button
        qr_window = ctk.CTk()
        qr_window.title("QR Code")
        qr_window.geometry("400x400")
        
        qr_label = ctk.CTkLabel(qr_window, text="QR Code will be displayed here")
        qr_label.pack(pady=10)
        
        copy_button = ctk.CTkButton(qr_window, text="Copy", command=copy_password)
        copy_button.pack(pady=10)
        
        qr_window.mainloop()

    else : 
        status_label.configure(text="Pls Input URL")

def find_pw():
    # Open a new window for displaying QR code and copy button
    pw_window = ctk.CTk()
    pw_window.title("Find PW")
    pw_window.geometry("400x400")
    
    qr_label = ctk.CTkLabel(pw_window, text="Enter keyword")
    qr_label.pack(pady=10)

    entry_get = ctk.CTkEntry(pw_window, width=100, height=20)
    entry_get.pack(pady=10)

    status_label = ctk.CTkLabel(pw_window , text="Status")
    status_label.pack(pady=10)

    copy_button = ctk.CTkButton(pw_window, text="Submit", command=get_pw)
    copy_button.pack(pady=10)

    copy_button = ctk.CTkButton(pw_window, text="Copy", command=copy_password)
    copy_button.pack(pady=10)
    
    pw_window.mainloop()

def get_pw():
    print("clicked")

def generate_pw():
    print('clicked')

def copy_password():
    print('clicked')

#Create a root Window 
root = ctk.CTk()
ctk.set_appearance_mode("system")
ctk.set_appearance_mode("dark")
ctk.set_appearance_mode("dark")

#title 
root.title("Password Generator")

#set min and max 
root.geometry("720x480")
root.minsize(720 , 480)
root.maxsize(1080 , 720)

#frame #1 
content_frame = ctk.CTkFrame(root)
content_frame.pack(fill = ctk.BOTH, expand=True , padx=10 , pady=10)

#create a label w entry widget  
url_label = ctk.CTkLabel(content_frame, text= "Enter your URL: ")
entry_url = ctk.CTkEntry(content_frame, width=400 , height=40)
url_label.pack(pady=10)
entry_url.pack(pady=10)

status_label = ctk.CTkLabel(content_frame , text="")
status_label.pack(pady=10)

#Create a download Button
download_button = ctk.CTkButton(content_frame, text="Convert" , command=converted_link)
download_button.pack(pady=10)

#Create a download Button
download_button = ctk.CTkButton(content_frame, width=150 , height=50 , text="Generate Password" , command=generate_pw)
download_button.pack(pady=15)

#Password Generator
pw_label = ctk.CTkLabel(content_frame, text="Your Password is :")
entry_pw = ctk.CTkEntry(content_frame, width=300, height=50)
pw_label.pack(pady=5)
entry_pw.pack(pady=10)

#Copy Password
copy_button = ctk.CTkButton(content_frame, text="Copy Password", command=copy_password)
copy_button.pack(padx=5)

#Copy Password
find_password = ctk.CTkButton(content_frame, text="Get Password", command=find_pw)
find_password.pack(side = ttk.LEFT , pady = 10)

#start  z
root.mainloop()