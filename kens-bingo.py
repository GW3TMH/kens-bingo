#!/usr/bin/python3

import os
import time
import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from lang import *
#from PIL import Image
#from PIL import ImageTk

ProgramName = "Kens Bingo"

# Gradient colours
Colour1 = "#6496FF"
Colour2 = "#FFFFFF"

# Place for randomly generated numbers
number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
60, 61, 62, 63, 64, 65, 66, 67, 68, 69,
70, 71, 72, 73, 74, 75, 76, 77, 78, 79,
80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
90]

# Used by calls checker screen
checks = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
60, 61, 62, 63, 64, 65, 66, 67, 68, 69,
70, 71, 72, 73, 74, 75, 76, 77, 78, 79,
80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
90]

# Lingo displayed under number
lingo = [LINGO_00,
LINGO_01,LINGO_02,LINGO_03,LINGO_04,LINGO_05,LINGO_06,LINGO_07,LINGO_08,LINGO_09,LINGO_10,
LINGO_11,LINGO_12,LINGO_13,LINGO_14,LINGO_15,LINGO_16,LINGO_17,LINGO_18,LINGO_19,LINGO_20,
LINGO_21,LINGO_22,LINGO_23,LINGO_24,LINGO_25,LINGO_26,LINGO_27,LINGO_28,LINGO_29,LINGO_30,
LINGO_31,LINGO_32,LINGO_33,LINGO_34,LINGO_35,LINGO_36,LINGO_37,LINGO_38,LINGO_39,LINGO_40,
LINGO_41,LINGO_42,LINGO_43,LINGO_44,LINGO_45,LINGO_46,LINGO_47,LINGO_48,LINGO_49,LINGO_50,
LINGO_51,LINGO_52,LINGO_53,LINGO_54,LINGO_55,LINGO_56,LINGO_57,LINGO_58,LINGO_59,LINGO_60,
LINGO_61,LINGO_62,LINGO_63,LINGO_64,LINGO_65,LINGO_66,LINGO_67,LINGO_68,LINGO_69,LINGO_70,
LINGO_71,LINGO_72,LINGO_73,LINGO_74,LINGO_75,LINGO_76,LINGO_77,LINGO_78,LINGO_79,LINGO_80,
LINGO_81,LINGO_82,LINGO_83,LINGO_84,LINGO_85,LINGO_86,LINGO_87,LINGO_88,LINGO_89,LINGO_90]


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        
#        self.img = ''
#        self.PicName = ''
#        self.PicFlag = 0
        
        # Get the size of the screen
        self.MainWidth = self.master.winfo_screenwidth()
        self.MainHeight = self.master.winfo_screenheight()
 
#         # Read the picture file if it exists
#        self.PicName = ProgramName + '.png'
#        exists = os.path.isfile(self.PicName)
#        if exists:
#            self.PicFlag = 1
#            self.img = Image.open(self.PicName)
#            self.img = self.img.resize((self.MainWidth,self.MainHeight), Image.ANTIALIAS)
#            self.img =  ImageTk.PhotoImage(self.img)   
        
        # Create the Main window
        self.master.attributes('-fullscreen', True)
        self.master.title(ProgramName)
                
        # Add a frame 
        myframe = Frame(self.master)
        myframe.pack(fill=BOTH, expand=YES)
        
        self.myCanvas = Canvas(myframe, bg = "white", height = int(self.MainHeight), width = int(self.MainWidth)) 
        self.myCanvas.pack()
        
#        # Trap window being closed
#        self.master.protocol('WM_DELETE_WINDOW', self.OnClosingMain)

        self.mode = 0
        self.calls = 0
        self.number = 0
        
        # Create key press event
        self.master.bind("<KeyPress>", self.OnKeyPress)
        
        self.ResetGame()
        self.DrawWindow() 
        
        # Set up key pressed delay timer
        self.TimeThen = time.time()


    def OnKeyPress(self, event):
        # Key pressed delay timer (1 second)
        TimeNow = time.time()
        TimeElapsed = TimeNow - self.TimeThen
        if TimeElapsed > 1:
            self.TimeThen = time.time()
            
            if event.char == 'b' or event.char == 'B':
                # Step backwards & print screen
                if (self.mode == 0):
                    if (self.calls > 0):
                        self.calls = self.calls - 1
                self.DrawWindow()
                return True        
                
            if event.char == 'c' or event.char == 'C':
                # Show check screen
                if (self.mode == 0):
                    self.mode = 1
                elif (self.mode == 1):
                    self.mode = 0
                self.DrawWindow()
                return True    
                
            if event.char == 'r' or event.char == 'R':
                # Ask if we can reset game
                if (self.mode == 1):
                    result = messagebox.askokcancel(ProgramName,"Are you sure\nyou want to\nReset Game ?")
                    if result == True:
                        self.ResetGame()
                        self.mode = 0
                self.DrawWindow()
                return True        
                
            if event.char == ' ':
                # Show next number
                self.mode = 0
                if (self.calls < 90):
                    self.calls = self.calls + 1
                    checks[number[self.calls]] = number[self.calls]
                self.DrawWindow()
                return True   
                
            if (ord(event.char)) == 27:
				# Escape Key
                self.OnClosingMain()
                return True 
        
        return False

        
    def ResetGame(self):
        # Reset the game
        self.NumbersNeeded = 15
        # set arrays to zero's
        for i in range (0,91):
            checks[i] = 0
            number[i] = 0

        self.calls = 0

        while True:
            x = random.randint(1,90)
            for i in range (1,91):
                if (number[i] == x):
                    break
                if (number[i] == 0):
                    number[i] = x
                    if (i == 90):
                        return
                    break

        return False


#    def DrawLogo(self):
#		# Try and draw a logo
#        if self.PicFlag == 1: 
#            self.myCanvas.create_image(0,0, image=self.img, anchor='nw')
#        return False        


    def DrawWindow(self):
        self.myCanvas.delete(tk.ALL)  # <---- Delete all the item created in the canvas.
        # Colour of Big Number = BigColour
        BigColour = 'black'
        
        # Create gradient background
        limit = int(self.MainHeight)
        (r1,g1,b1) = self.myCanvas.winfo_rgb(Colour1)
        (r2,g2,b2) = self.myCanvas.winfo_rgb(Colour2)
        r_ratio = float(r2-r1) / limit
        g_ratio = float(g2-g1) / limit
        b_ratio = float(b2-b1) / limit
        for i in range(limit):
            nr = int(r1 + (r_ratio * i))
            ng = int(g1 + (g_ratio * i))
            nb = int(b1 + (b_ratio * i))
            Colour = "#%4.4x%4.4x%4.4x" % (nr,ng,nb)
            self.myCanvas.create_line(0,i,int(self.MainWidth),i, tags=("gradient",), fill=Colour)

#        self.DrawLogo()
                    
        if self.mode == 0:
            # Large Number
            self.myCanvas.create_text(int(self.MainWidth/2), int(self.MainHeight/10 * 4), tags=("gradient",), text = "%d" % (number[self.calls]), font=('Arialbd', int(self.MainHeight/10 * 6), 'bold'), fill = BigColour)
        
            # Bingo Lingo
            self.myCanvas.create_text(int(self.MainWidth/2), int(self.MainHeight/10 * 8), tags=("gradient",), text = lingo[number[self.calls]], font=('Arial', int(self.MainHeight/25), 'bold'))

        if self.mode == 1:
            # Check Screen
            i = 0
            for r in range(1, 10):
                for c in range(1, 11):
                    i = i + 1
                    if checks[i] != 0:
                        self.myCanvas.create_text(int(self.MainWidth/12 * c) + int(self.MainWidth/22), int(self.MainHeight/50 * 6) + int(r * self.MainHeight/14) - int(self.MainHeight/14), tags=("gradient",), text = "%d" % (checks[i]), font=('Arial', int(self.MainHeight/25), 'bold'))
                    else:
                        self.myCanvas.create_text(int(self.MainWidth/12 * c) + int(self.MainWidth/22), int(self.MainHeight/50 * 6) + int(r * self.MainHeight/14) - int(self.MainHeight/14), tags=("gradient",), text = '-', font=('Arial', int(self.MainHeight/25), 'bold'))                        

        # Draw Line
        self.myCanvas.create_line(int(self.MainWidth/10),int(self.MainHeight/10 * 8.8),int(self.MainWidth-self.MainWidth/10),int(self.MainHeight/10 * 8.8), tags=("gradient",), fill="black", width=int(self.MainHeight/150))   

        # Number Of Calls
        self.myCanvas.create_text(int(self.MainWidth/2), int(self.MainHeight/10 * 9.5), tags=("gradient",), text = "%s %d %s %d." % (TOTAL_CALLS, self.calls, LAST_NUMBER, number[self.calls]), font=('Arial', int(self.MainHeight/25), 'bold'))

        return False            


    def OnClosingMain(self):
        # Confirm shut down
        result = messagebox.askokcancel(ProgramName,"Are you sure\nyou want to\nExit Game ?")
        if result == False:
            return False
        
        self.master.destroy()


root = tk.Tk()
app = Application(master=root)
app.mainloop()
