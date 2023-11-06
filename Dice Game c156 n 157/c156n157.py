from tkinter import*
from PIL import ImageTk, Image
import random

root = Tk()
root.geometry('7000x5000')
root.title('Dice Game')
root.configure(background='light blue')


imagedice = ImageTk.PhotoImage(Image.open("dice.png"))

lp1 = Label(root, text = "Player 1", bg = "dark blue", fg="gold")

lp1.place(relx = 0.15, rely = 0.3, anchor=CENTER)

lp2 = Label(root, text = "Player 2", bg = "dark blue", fg="gold")

lp2.place(relx = 0.85, rely = 0.3, anchor=CENTER)

lsc1 = Label(root, bg = "dark blue", fg="gold")

lsc1.place(relx = 0.15, rely = 0.4, anchor=CENTER)

lsc2 = Label(root, bg = "dark blue", fg="gold")

lsc2.place(relx = 0.85, rely = 0.4, anchor=CENTER)

lr = Label(root, bg = "navy blue", fg="gold")

lr.place(relx = 0.5, rely = 0.7, anchor=CENTER)



p1sc = 0

p2sc = 0

def p1fun():
    global p1sc
    num1 = random.randint(1,6)
    lr["text"] = "Player 1 number is : " + str(num1)
    p1sc = p1sc + num1
    lsc1["text"] = str(p1sc)
    
    
def p2fun():
    global p2sc
    num2 = random.randint(1,6)
    lr["text"] = "Player 2 number is : " + str(num2)
    p2sc = p2sc + num2
    lsc2["text"] = str(p2sc)
    
btnp1 = Button(root, image = imagedice, command = p1fun)

btnp1.place(relx = 0.15, rely = 0.7, anchor=CENTER)

btnp2 = Button(root, image = imagedice, command = p2fun)

btnp2.place(relx = 0.85, rely = 0.7, anchor=CENTER)
    
    


root.mainloop()
