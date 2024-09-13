import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, scrolledtext
import os
import zipfile
import time
import shutil
import tempfile
import threading
import ctypes
import subprocess
import webbrowser
import platform
import random
import string  # Import the string module

print("Welcome To NightlyBuildEffiCompress")


def randomize_files_in_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        try:
            for filename in os.listdir(folder_path):
                old_file_path = os.path.join(folder_path, filename)
                if os.path.isfile(old_file_path):
                    # Generate a random string of 8 characters
                    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
                    new_filename = f"{random_string}_{filename}"
                    new_file_path = os.path.join(folder_path, new_filename)
                    os.rename(old_file_path, new_file_path)
                    print(f"Renamed {old_file_path} to {new_file_path}")
            messagebox.showinfo("Success", "All files have been randomized.")
        except Exception as e:
            print(f"Error randomizing files: {e}")
            messagebox.showerror("Error", f"An error occurred while randomizing files: {e}")


def select_compression_type():
    root = tk.Tk()
    root.title("Select Compression Type")
    root.geometry("300x600")

    def on_selection(selection):
        root.destroy()

    tk.Button(root, text="Randomize Files", command=randomize_files_in_folder).pack(pady=5)
    # tk.Button(root, text="MobileAccess", command=grant_mobile_access).pack(pady=5)
    # tk.Button(root, text="Open PVZUtil", command=open_pvzutil).pack(pady=5)

    root.mainloop()

# Define other functions (check_version_and_output, open_donation_page, etc.) here

if __name__ == "__main__":
    select_compression_type()
