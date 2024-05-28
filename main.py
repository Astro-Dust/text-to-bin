from tkinter import filedialog
import tkinter as tk
import os

newFileName = 'binary_translation.txt'

def file_path():
    filename = filedialog.askopenfile()
    if filename:
        filename = str(filename).split(' ')[1].replace('name=', '')
        final_filename = filename.replace("'", '')
        return final_filename

    else:
        print('No file selected.')

root = tk.Tk()
root.title('Text to binary translator')

button = tk.Button(root, text='Search txt file', command=file_path)
button.pack(pady=20)

txt_file = file_path()
newFile = open(newFileName, 'w')

with open(txt_file) as file:
    for line in file:
        line_bin = ' '.join(format(ord(char), '08b') for char in line.strip())
        newFile.write(line_bin)

file.close()

# CORRIGIR
# i = 1
# while os.path.isfile(newFileName):
#     newFileName = f'{newFileName}({i})'
#     i += 1

root.mainloop()
