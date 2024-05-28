from tkinter import filedialog
import tkinter as tk
import os

newFileName = 'binary_translation.txt'

def file_path():
    filename = filedialog.askopenfile()
    if filename:
        filename = filename.name
        return filename

    else:
        print('No file selected.')

root = tk.Tk()
root.title('Text to binary translator')

button = tk.Button(root, text='Search txt file', command=file_path)
button.pack(pady=20)

txt_file = file_path()

if txt_file:

    base_name, extension = os.path.splitext(newFileName)
    i = 1
    finalFileName = newFileName

    while os.path.isfile(finalFileName):
        finalFileName = f'{base_name}{i}{extension}'
        i += 1

    with open(finalFileName, 'w') as newFile, open(txt_file) as file:
        for line in file:
            line_bin = ' '.join(format(ord(char), '08b') for char in line.strip())
            newFile.write(line_bin + '\n')
            
    file.close()

    print('File saved successfully!')

root.mainloop()
