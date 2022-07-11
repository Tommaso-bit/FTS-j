#FTS
import time
from tkinter import *
from tkinter import messagebox
import os
#import 

messagebox.showerror("Windows 10", "FATAL ERROR")
#first message

messagebox.showwarning("Warning", "Riavviare il sistema")
#second message

time.sleep(5) 
#wait time 5s

os.system ("shutdown /r")
#code for shutdown executed in CMD

mainloop()
#end

