import tkinter.ttk as ttk
import tkinter as tk
import tkinter.scrolledtext as st
import tkinter.filedialog as dlg
from PIL import Image, ImageTk
import sys
sys.path.append('../')

def savefile(self):
  typ = [('テキストファイル', '*.txt')]
  savefilename = dlg.asksaveasfilename(filetypes=typ)
  with open(savefilename, 'w', encoding='utf-8') as f:
    f.write(self)

if __name__ == '__main__':
  savefile('テキスト')


  
    