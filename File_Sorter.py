import os
import shutil
import tkinter
from tkinter import filedialog

fileTypes = {
    'pics': ['jpg', 'jpeg', 'png', 'tiff', 'psd', 'raw', 'gif'],
    'audio': ['wav', 'flac', 'aiff', 'aif', 'mp3'],
    'video': ['mp4', 'mov', 'flv', 'mpeg-2', 'wmv', 'avi'],
    'docs': ['txt', 'pdf', 'docx', 'doc', 'xlsx', 'xml', 'xls', 'xltx', 'xls', 'csv'],
    'archives': ['zip', 'rar'],
}

sourceDirs = ['archives', 'video', 'audio', 'docs', 'pics', 'others']


def browse_button():
    path = filedialog.askdirectory()
    list_ = os.listdir(path)
    print(os.path.abspath(path))
    for file_ in list_:
        name, ext = os.path.splitext(file_)
        ext = ext[1:]

        for fileType, fileExtensions in fileTypes.items():
            file_destination = f'{path}/{file_}'
            is_file_found = os.path.exists(file_destination)
            new_destination = f'{path}/{fileType}/{file_}'

            if ext in fileExtensions and is_file_found:
                if os.path.exists(f'{path}/{fileType}'):
                    shutil.move(file_destination, new_destination)
                else:
                    os.mkdir(f'{path}/{fileType}')
                    shutil.move(file_destination, new_destination)


top = tkinter.Tk()
top.title('File Sorter')
button2 = tkinter.Button(text="Select folder to organize", command=browse_button)
button2.grid(row=0, column=3)
# Code to add widgets will go here...
top.mainloop()





