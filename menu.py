import os
import subprocess
import tkinter as tk

# === CONFIGURATION ===
FOLDER = "are"

# Customize colors
BACKGROUND_COLOR = "#FF45A5"
BUTTON_COLOR = "#1CFFD2"
TEXT_COLOR = "#000000"
FONT = ("Segoe UI", 12)

# List of tools (filename : button label)
TOOLS = {
    "roblox.bat": "Roblox",
    "youtube.bat": "YouTube",
    "discord.bat": "Discord"
}

# === FUNCTIONS ===
def run_tool(filename):
    path = os.path.join(FOLDER, filename)
    if os.path.exists(path):
        subprocess.Popen(path, shell=True)
    else:
        print(f"File not found: {path}")

# === GUI ===
root = tk.Tk()
root.title("Repair Tool Launcher")
root.configure(bg=BACKGROUND_COLOR)
root.geometry("400x300")

for filename, label in TOOLS.items():
    btn = tk.Button(
        root,
        text=label,
        command=lambda f=filename: run_tool(f),
        bg=BUTTON_COLOR,
        fg=TEXT_COLOR,
        font=FONT,
        relief=tk.RAISED,
        padx=10,
        pady=5
    )
    btn.pack(pady=10, fill="x", padx=20)

root.mainloop()
