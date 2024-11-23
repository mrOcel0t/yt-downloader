from pytube import YouTube
from tkinter import *
from tkinter.ttk import *
import threading
import tkinter.messagebox  as mb
import pyperclip
import os


def on_progress(stream, data_chunk, bytes_remaining):
    downloaded = stream.filesize - bytes_remaining
    downloaded_percents = downloaded / stream.filesize * 100
    progressbar['value'] = round(downloaded_percents)



def on_complete(stream, filepath):
    lbl.configure(text="Видео скачано")
    progressbar.destroy()

# механика кнопки Скачать
def dload(u):
    # пробуем скачать видео по ссылке
    try:
        # yt = YouTube(u, on_progress_callback=on_progress, on_complete_callback=on_complete)
        # stream = yt.streams.get_by_itag(22)
        # stream.download()
        yt = YouTube(u,on_progress_callback=on_progress, on_complete_callback=on_complete)
        #stream = yt.streams.get_highest_resolution()
        video = yt.streams.filter(progressive=True).desc().first()
        #stream = yt.streams.get_by_itag(22)
        video.download() 
        # выводим результат
        Result="Загрузка завершена"
        mb.showinfo("Готово",Result)
    # если скачать не получилось
    except:
        # выводим сообщение об ошибке
        lbl.configure(text="Ошибка")
        progressbar.destroy()
        Result="Ссылка не работает"
        mb.showerror("Ошибка",Result)
# def prosba1():
    # # d1 = "Неуказана ссылка. Введите её пожалуйста"
    # # mb.showwarning(title="Ошибка",message=d1)
    # # mb.OK
    # lbl.configure(text="Error")
    # btn.destroy()
    # url.destroy()
    # abc.destroy()
    #lbl1.destroy()

    

# def prosba2():
#     # d2 = "Неуказано месот сохранения. Введите его пожалуйста"
#     # mb.showwarning(title="Ошибка",message=d2)
#     # mb.OK
#     lbl.configure(text="Error")
#     btn.destroy()
#     url.destroy()
#     abc.destroy()
#     lbl1.destroy()    
# def error(u,g):   
#       g = "Неправильно введена ссылка.Попробуйе ещё раз"
#       mb.showerror("Ошибка", g)
#       lbl.configure(text='Ошибка')
       
    
def clicked():
    u = url.get()
    #pyperclip.paste(url)
    btn.destroy()
    url.destroy()
    lbl.configure(text="Видео скачивается")
    dload(u)
    


window = Tk()
window.title("YT-download")
window.geometry('400x200')
icon = PhotoImage(file = 'loco.png')
window.iconphoto(False, icon)
lbl = Label(window, text="Введите ссылку для скачивания:", font=("Arial Bold", 12))
lbl.grid(column=0, row=0)
url = Entry(window, width=10)
url.grid(column=0, row=1)
btn = Button(window, text='Скачать', command=threading.Thread(target=clicked).start)
btn.grid(column=0, row=4)
# value_var = IntVar(value=on_prog)
progressbar = Progressbar()
progressbar.place(x=165, y=140)
# er_b= Button(text="Ошибка",command=erroe)
# er_b.pack()
# label = ttk.Label(textvariable=value_var)
# label.pack(anchor=NW, padx=6, pady=6)
# pb1 = ttk.Progressbar(window, orient= HORIZONTAL,length=100).grid(row=value_var())
window.mainloop()
