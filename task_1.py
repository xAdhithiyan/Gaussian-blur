
from numpy import *
from tkinter import *
from PIL import Image,ImageTk

#enter image directory here
#
imtoblurr=r"srmth-task-1\images\Image-File-icon.jpg"
#imtoblurr=r"task1\images\lol.jpg"
a = Image.open(f"{imtoblurr}")#r is raw string
spix = a.load()#loads pixel data
pix=a.size
kermat = array(
    [[0,0,0,0,0,0,0],
    [0,0,0.01,0.01,0.01,0,0],
    [0,0.01,0.05,0.11,0.05,0.01,0],
    [0,0.01,0.11,0.25,0.11,0.01,0],
    [0,0.01,0.05,0.11,0.05,0.01,0],
    [0,0,0.01,0.01,0.01,0,0],
    [0,0,0,0,0,0,0],
    ])
k=0
def pixmatrix():
    finalist=[]
    for i in range(1,pix[0]):#i and j are x and y coordinate of the pixal 
        if not (i>3 and i<pix[0]-3):#since kernal matrix is 7 --> 3 on each side from center
            continue;
        for j in range(1,pix[1]):
            if not (j>3 and j<pix[1]-3):
                continue;
            
            for k in range(0,3):#cause x,y,z for rgb
                ll=[]
                for x in range(i-3,i+4):
                    b=[]
                    for y in range(j-3,j+4):
                        c=spix[x,y]
                        b.append(c[k])
                    ll.append(b)
                cal(ll,finalist)
            for p in range(len(finalist)):
                finalist[p]=int(finalist[p])
            finalist=tuple(finalist)
            spix[i,j]=finalist
            finalist=[]
def cal(ll,finalist):
    mma=array(ll)
    #matrix multiplication is not done. we place and one matrix over the other and multiply the correspoding values of both the matrix-->array multiplication
    mm=sum(kermat*mma)
    finalist.append(mm)
    return 0


pixmatrix()
a.save(r"srmth-task-1\images\blurred_image.jpg")


def exit_():
    screen2.destroy()
    screen.destroy()

def screen2():
    global screen2
    screen2=Toplevel(screen)
    screen2.geometry("640x480")
    screen2.title("screen2")
    myl=Label(screen2,image=myim)
    myl.place(x=0,y=0)
    l11=Label(screen2,text="Orignal Image",font=("Calibri",25))
    l11.place(x=50,y=30)
    l12=Label(screen2,image=myim1)
    l12.place(x=20,y=100)
    l21=Label(screen2,text="Blurred Image",font=("Calibri",25))
    l21.place(x=390,y=30)
    #final image
    finalblur=Image.open(r"srmth-task-1\images\blurred_image.jpg")
    im5=finalblur.resize((250,250))
    myim5 = ImageTk.PhotoImage(im5)
    myl5=Label(screen2,image=myim5)
    myl5.photo= myim5  #anchor the image to the object
    myl5.place(x=360,y=100)
    b2= Button(screen2,text="Exit",font=("Calibri",20),command=exit_)
    b2.place(x=280,y=380)
    
#tkinter part
def screen():
    global screen
    global myim
    global myim1
    screen=Tk()
    cc='#369DA2'
    screen.geometry("640x480")
    #bg image
    image=Image.open(r"srmth-task-1\images\gradiant.jfif")
    im=image.resize((640,480))
    myim = ImageTk.PhotoImage(im)
    myl =Label(screen,image=myim)
    myl.pack()
    #display image to be blurred
    a=Label(screen,text="IMAGE",font=("Calibri",25)).place(x=270,y=20)
    image1=Image.open(f"{imtoblurr}")
    im1=image1.resize((250,250))
    myim1=ImageTk.PhotoImage(im1)
    myl1=Label(screen,image=myim1)
    myl1.place(x=190,y=100)
    #button
    but=Button(screen,text="Blur the Image",font=("Calibri",13),command=screen2)
    but.place(x=260,y=390)
    screen.mainloop()

screen()