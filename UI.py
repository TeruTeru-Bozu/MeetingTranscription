import tkinter.ttk as ttk
import tkinter as tk
import tkinter.scrolledtext as st
import tkinter.filedialog as dlg
from PIL import Image, ImageTk
import sys
sys.path.append('../')
import transcription

def EndButtonPressed(event):
    global  is_Transcription
    is_Transcription = False
    

def draw_window():

    global root, textfield, realtime
    #Windowの生成
    root = tk.Tk()
    root.title("MeetingTranscription")
    root.geometry("480x560")

    #テキストボックス（複数行、スクロールバー付）の生成
    labal1 = tk.Label(text="議事録")
    labal1.pack()

    textfield = st.ScrolledText(root, height=15)
    textfield.configure(state='normal')
    textfield.pack(fill="both", expand=True)

    #リアルタイムボックス
    labal2 = tk.Label(text="リアルタイム編集")
    labal2.pack()

    realtime = st.ScrolledText(root, height=5)
    realtime.configure(state='normal')
    realtime.pack(fill="both", expand=True)

    #要約
    labal3 = tk.Label(root, text="要約")
    labal3.pack()

    summary = st.ScrolledText(root, height=5)
    summary.configure(state='normal')
    summary.pack(fill="both", expand=True)

    canvas = tk.Canvas(root, width=480, height=160, bg="white")
    canvas.pack()

    ###図形###
    endbutton = Image.open("stop.png")
    tkimg = ImageTk.PhotoImage(endbutton)
    canvas.create_image(64, 64, image=tkimg, tags="endbutton")
    canvas.tag_bind("endbutton", "<ButtonPress-1>", EndButtonPressed)


    root.mainloop()
