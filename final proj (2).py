from turtle import *

pen1=Pen()
pen2=Pen()


pen1.screen.bgcolor("#B51108")

pen1.color("#FFFFFF")
pen2.color("#532222")

pen2.up()
pen2.goto(-50,50)
pen2.down()
pen1.begin_fill()
pen1.circle(100)
pen1.end_fill()
pen2.write("KP",font=('Candara',70))

pen1.up()
pen1.goto(-250,-150)
pen1.down()
pen1.write("""1. Blackjack
2. Lucky 7
3. Amazing Pattern""",font=("Candara",20))  

import Tkinter as logo
import webbrowser
print "check our logo out"
def callback(event):
    webbrowser.open_new(event.widget.cget("text"))

root = logo.Tk()
lbl = logo.Button(root, text=r"Social.html", fg="red", cursor="target")
lbl.pack()
lbl.bind("<Button-1>", callback)
root.mainloop()
while True:
    k=input('enter choice') 
    if k==1:
        import blackjack
    elif k==2:
        import lucky7

    else:
        import triangle
    print ""
    x=raw_input('you want to continue here (y/n)?')
    if x=='n':
        break
    else:
        True
