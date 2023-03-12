#!/usr/bin/python3


#******************************************************************************
#**** Copyright (C) 2023  Ken Williams GW3TMH (ken@kensmail.uk)            ****
#****                                                                      ****
#**** This library is free software; you can redistribute it and/or        ****
#**** modify it under the terms of the GNU Lesser General Public           ****
#**** License as published by the Free Software Foundation; either         ****
#**** version 3 of the License, or (at your option) any later version.     ****
#****                                                                      ****
#**** This library is distributed in the hope that it will be useful,      ****
#**** but WITHOUT ANY WARRANTY; without even the implied warranty of       ****
#**** MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU    ****
#**** Lesser General Public License for more details.                      ****
#****                                                                      ****
#**** You should have received a copy of the GNU Lesser General Public     ****
#**** License along with this library; if not, write to the                ****
#**** Free Software Foundation, Inc.                                       ****
#**** 59 Temple Place, Suite 330                                           ****
#**** Boston, MA  02111-1307  USA                                          ****
#******************************************************************************

LINGO_00 = "B=Back C=Check R=Reset Space=Next Esc=Exit"
LINGO_01 = "Kellys eye its number one."
LINGO_02 = "One little duck its number two."
LINGO_03 = "One little flea its number three."
LINGO_04 = "On the floor its number four."
LINGO_05 = "Man alive its number five."
LINGO_06 = "Tom Mix its number six."
LINGO_07 = "On its own lucky seven."
LINGO_08 = "Sexy Kate its number eight."
LINGO_09 = "Doctors orders number nine."
LINGO_10 = "Downing street number ten."
LINGO_11 = "Those legs eleven."
LINGO_12 = "One and two one dozen."
LINGO_13 = "Unlucky for some thirteen."
LINGO_14 = "Valentines day fourteen."
LINGO_15 = "Stroppy teen its fifteen."
LINGO_16 = "Sweet sixteen."
LINGO_17 = "Dancing Queen its seventeen."
LINGO_18 = "Coming of age eighteen."
LINGO_19 = "Goodbye teens its nineteen."
LINGO_20 = "Getting plenty its number twenty."
LINGO_21 = "Key of the door twenty one."
LINGO_22 = "Two little ducks its twenty two."
LINGO_23 = "A duck and a flea its twenty three."
LINGO_24 = "Want some more its twenty four."
LINGO_25 = "Duck and dive its twenty five."
LINGO_26 = "Pick and mix its twenty six."
LINGO_27 = "Gateway to heaven its twenty seven."
LINGO_28 = "A duck and its mate its twenty eight."
LINGO_29 = "In your prime its twenty nine."
LINGO_30 = "Dirty Gertie its number thirty."
LINGO_31 = "Get up and run its thirty one."
LINGO_32 = "Buckle my shoe its thirty two."
LINGO_33 = "All the threes dirty knees."
LINGO_34 = "Ask for more its thirty four."
LINGO_35 = "Jump and jive its thirty five."
LINGO_36 = "Three and six three dozen."
LINGO_37 = "A flea in heaven its thirty seven."
LINGO_38 = "Christmas cake its thirty eight."
LINGO_39 = "Those thirty nine steps."
LINGO_40 = "Four oh blind forty."
LINGO_41 = "Time for fun its forty one."
LINGO_42 = "Winnie the pooh its forty two."
LINGO_43 = "Down on your knee its forty three."
LINGO_44 = "All the fours droopy drawers."
LINGO_45 = "Half way there forty five."
LINGO_46 = "Up to tricks its forty six."
LINGO_47 = "Four and seven its forty seven."
LINGO_48 = "Four and eight four dozen."
LINGO_49 = "Rise and shine its forty nine."
LINGO_50 = "Five oh blind fifty."
LINGO_51 = "Tweak of the thumb its fifty one."
LINGO_52 = "Chicken vindaloo its fifty two."
LINGO_53 = "Stuck in a tree its fifty three."
LINGO_54 = "Five and four clean the floor."
LINGO_55 = "All the fives snakes alive."
LINGO_56 = "Five and six fifty six."
LINGO_57 = "Five and seven Heinz varieties."
LINGO_58 = "Make them wait its fifty eight."
LINGO_59 = "Five and nine the Brighton line."
LINGO_60 = "Six oh blind sixty."
LINGO_61 = "Bakers bun its sixty one."
LINGO_62 = "Tickety boo its sixty two."
LINGO_63 = "Tickle me its sixty three."
LINGO_64 = "Red and raw its sixty four."
LINGO_65 = "Six and five pension day."
LINGO_66 = "All the sixies clickety click."
LINGO_67 = "Made in heaven its sixty seven."
LINGO_68 = "Saving Grace its sixty eight."
LINGO_69 = "Any way up its sixty nine."
LINGO_70 = "Seven Oh blind seventy."
LINGO_71 = "Bang on the drum its seventy one."
LINGO_72 = "A crutch and a duck seventy two."
LINGO_73 = "A crutch and a flea its seventy three."
LINGO_74 = "Seven and four the candy store."
LINGO_75 = "On the skive its seventy five."
LINGO_76 = "Seven and six was she worth it."
LINGO_77 = "Seventy seven sunset strip."
LINGO_78 = "Heavens gate its seventy eight."
LINGO_79 = "One more time its seventy nine."
LINGO_80 = "There you go matey its number eighty."
LINGO_81 = "Stop and run its eighty one."
LINGO_82 = "Straight on through its eighty two."
LINGO_83 = "Time for tea its eighty three."
LINGO_84 = "Eight and four seven dozen."
LINGO_85 = "Staying alive its eighty five."
LINGO_86 = "Between the sticks its eighty six."
LINGO_87 = "Torquay in Devon its eighty seven."
LINGO_88 = "Two fat ladies eighty eight."
LINGO_89 = "Almost there its eighty nine."
LINGO_90 = "Top of the shop nine oh ninety."

TOTAL_CALLS = "Number of calls"
LAST_NUMBER = "last number called"

RESET_GAME = "Reset game?"


import os
import time
import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox
#from lang import *
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
