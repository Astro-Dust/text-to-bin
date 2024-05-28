from tkinter import filedialog
import tkinter as tk
import os

current_path = os.getcwd()

def text_to_bin():
    filename = filedialog.askopenfile()
    if filename:
        filename = str(filename).split(' ')[1].replace('name=', '')
        final_filename = filename.replace("'", '')
        return final_filename

    else:
        print('No file selected.')

root = tk.Tk()
root.title('Text to binary translator')

button = tk.Button(root, text='Search txt file', command=text_to_bin)
button.pack(pady=20)

txt_file = text_to_bin()

with open(txt_file) as file:
    for line in file:
        line_bin = ' '.join(format(ord(char), '08b') for char in line.strip())
        print(line_bin)
file.close()

root.mainloop()

# with open(filename) as file:
#     for line in file:
#         line_bin = ' '.join(format(ord(char), '08b') for char in line.strip())
#         print(line_bin)

# file.close()
