from tkinter import filedialog
import tkinter as tk

def text_to_bin():
    filename = filedialog.askopenfile()
    if filename:
        print(filename)
    else:
        print('No file selected.')

root = tk.Tk()
root.title('Text to binary translator')

button = tk.Button(root, text='Search txt file', command=text_to_bin)
button.pack(pady=20)

root.mainloop()

# with open(filename) as file:
#     for line in file:
#         line_bin = ' '.join(format(ord(char), '08b') for char in line.strip())
#         print(line_bin)

# file.close()
