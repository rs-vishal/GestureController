import tkinter as tk
from tkinter import messagebox

# Global variable for active mode
active_mode = "Mouse"  # Default mode

def switch_mode(mode):
    global active_mode
    active_mode = mode
    messagebox.showinfo("Mode Changed", f"Mode switched to: {mode}")

def get_active_mode():
    return active_mode

def start_gui():
    root = tk.Tk()
    root.title("Gesture Controller")
    root.geometry("300x200")

    tk.Label(root, text="Gesture Controller", font=("Arial", 16)).pack(pady=10)

    tk.Button(root, text="Mouse Control (Always On)", state="disabled").pack(pady=5)
    tk.Button(root, text="Control PowerPoint", command=lambda: switch_mode("PPT")).pack(pady=5)
    tk.Button(root, text="Control Media", command=lambda: switch_mode("Media")).pack(pady=5)

    root.mainloop()
