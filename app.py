import customtkinter as ctk 
import os 
import pyqrcode 
import random
import string
import pyperclip

password_dict = {}

def converted_link():
    global status_label, entry_url
    
    # Get input from the entry widget
    url = entry_url.get()
    if url: 
        # Generate QR code
        qr_code = pyqrcode.create(url)
        
        # Specify a file path
        file_path = r"INSERT YOUR FILE PATH"
        file_name = "qr_code.svg"
        file_full_path = os.path.join(file_path, file_name)
        
        #Save QR code to a file
        qr_code.svg(file_full_path, scale=8)  
        
        #Event Status update 
        status_label.configure(text=f"QR Code Generated")

        #Open the QR Code
        os.startfile(file_full_path)
    else: 
        #Event Status update
        status_label.configure(text="Pls Input URL")

def generate_pw():
    global password_dict
    #Random Password Generator Logic
    if download_button is not None: 
        all_characters = string.ascii_letters + string.digits + string.punctuation
        generated_password = ''.join(random.choices(all_characters, k=12))
        entry_pw.delete(0 , 'end')
        entry_pw.insert(0 , generated_password)
        password_dict["generated_password"] = generated_password
    else : 
        pass

def copy_password():
    global password_dict
    # Copy the generated password
    if copy_button is not None: 
        generated_password = password_dict.get("generated_password", "")  
        if generated_password:  
            pyperclip.copy(str(generated_password))  
    else: 
        pass

#Create a root Window 
root = ctk.CTk()
ctk.set_appearance_mode("system")
ctk.set_appearance_mode("dark")
ctk.set_appearance_mode("dark")

#title 
root.title("Password Generator & QR Converter")

#set min and max size for the window
root.geometry("720x480")
root.minsize(720 , 480)
root.maxsize(1080 , 720)

#Main Frame 
content_frame = ctk.CTkFrame(root)
content_frame.pack(fill = ctk.BOTH, expand=True , padx=10 , pady=10)

#create a label with entry widget  
url_label = ctk.CTkLabel(content_frame, text= "Enter your URL: ")
entry_url = ctk.CTkEntry(content_frame, width=400 , height=40)
url_label.pack(pady=10)
entry_url.pack(pady=10)

#Status Update Label
status_label = ctk.CTkLabel(content_frame , text="")
status_label.pack(pady=10)

#Create a convert Button
download_button = ctk.CTkButton(content_frame, text="Convert" , command=converted_link)
download_button.pack(pady=10)

#Create a generate password button
download_button = ctk.CTkButton(content_frame, width=150 , height=50 , text="Generate Password" , command=generate_pw)
download_button.pack(pady=15)

#Password generator label 
pw_label = ctk.CTkLabel(content_frame, text="Your Password is :")
entry_pw = ctk.CTkEntry(content_frame, width=300, height=50)
pw_label.pack(pady=5)
entry_pw.pack(pady=10)

#Create a copy password button
copy_button = ctk.CTkButton(content_frame, text="Copy Password", command=copy_password)
copy_button.pack(padx=5)

#start
root.mainloop()