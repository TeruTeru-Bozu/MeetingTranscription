import tkinter.ttk as ttk
import tkinter as tk
import tkinter.scrolledtext as st
import tkinter.filedialog as dlg
from PIL import Image, ImageTk

def pressed(event):
    global  is_Transcription
    is_Transcription = False
    print("クリックされました")
    

def draw_window():

    global root, textfield, realtime
    #Windowの生成
    root = tk.Tk()
    root.title("MeetingTranscription")
    root.geometry("480x560")

    #テキストボックス（複数行、スクロールバー付）の生成
    textfield = st.ScrolledText(root, width = 64, height=32)
    textfield.configure(state='normal')
    textfield.pack()

    realtime = st.ScrolledText(root, width = 64, height=5)
    realtime.configure(state='normal')
    realtime.pack()

    canvas = tk.Canvas(root, width=480, height=160, bg="white")
    canvas.pack()

    ###図形###
    img = Image.open("test.png")
    tkimg = ImageTk.PhotoImage(img)
    canvas.create_image(64, 64, image=tkimg, tags="img")
    canvas.tag_bind("img", "<ButtonPress-1>", pressed)
    root.mainloop()
