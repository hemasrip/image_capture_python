from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk

captcha = Tk()

captcha.geometry('400x525')
captcha.resizable(False, False)
captcha.title('Image Captcha')

l=[]

def click(event):
    b1.config(image = correct)
    x=str('py1')
    l.append(x)
    
    
def click1(event):
    b3.config(image = correct)
    x=str('py1')
    l.append(x)
    
    
def click2(event):
    b4.config(image = correct)
    x=str('py1')
    l.append(x)
    
    
def click3(event):
    b5.config(image = correct)
    x=str('py1')
    l.append(x)
    
    
def click4(event):
    b9.config(image = correct)
    x=str('py1')
    l.append(x)
    
    
def on(event):
    b2.config(image = correct)
    x=str('py2')
    l.append(x)
    
    
def sel1(event):
    b7.config(image = correct)
    x=str('py3')
    l.append(x)
    
    
def sel2(event):
    b6.config(image = correct)
    x=str('py4')
    l.append(x)
    
    
def sel3(event):
    b8.config(image = correct)
    x=str('py5')
    l.append(x)
    
    
def check():
    
    if('py1' in l):
        print("captcha is incorrect")
        messagebox.showinfo("captcha","Captcha incorrect")
        l.clear()
        
    elif('py2' in l and 'py3' in l and 'py4' in l and 'py5' in l ):
        print("captcha is correct")
        messagebox.showinfo("captcha","Captcha correct")
        l.clear()
        
    else:
        print('invalid captcha')
        messagebox.showinfo("captcha","Captcha incorrect")
        l.clear()
    captcha.destroy()

    
fr1 = Frame(captcha , height = 50 , width = 120)
fr1.pack(fill = 'x')
fr1.pack_propagate(False)


fr2 = Frame(captcha , height = 450)
fr2.pack(fill = 'x')
fr2.pack_propagate(False)


lg = PhotoImage(file = 'car.png')
c = Image.open('car.png')
d = c.resize((50, 50))
lg = ImageTk.PhotoImage(d)


label = Label(fr1,bg = 'white',image=lg ,height = 95, width = 50)
label.grid(row = 0,column = 1)


x = Label(fr1 , bg = 'white' , height = 5 , width = 35 , text = 'Select all the Images with Cars' , font = ('Calibri 12'))
x.grid(row = 0,column = 2)


a = Image.open('Recaptchlogo.png')
b = a.resize((50, 50))
re = ImageTk.PhotoImage(b)


captcha.wm_iconbitmap('icon.ico')


m = Label(fr1,bg = 'white',image = re,height = 95, width = 50)
m.grid(row = 0,column = 3)


image = Image.open('car4.png')
g = image.resize((125, 120))
img1 = ImageTk.PhotoImage(g)


e = Image.open('car1.png')
f = e.resize((125, 120))
img2 = ImageTk.PhotoImage(f)


h = Image.open('car2.png')
i = h.resize((125, 120))
img3 =ImageTk.PhotoImage(i)


j = Image.open('car3.png')
k = j.resize((120, 120))
img4 = ImageTk.PhotoImage(k)


n = Image.open('bike3.png')
o = n.resize((125, 120))
img5 = ImageTk.PhotoImage(o)


p = Image.open('cy1.png')
q = p.resize((125, 120))
img6 = ImageTk.PhotoImage(q)


r = Image.open('tc1.png')
s = r.resize((125, 120))
img7 = ImageTk.PhotoImage(s)


u = Image.open('lr1.png')
v = u.resize((125, 120))
img8 = ImageTk.PhotoImage(v)


w = Image.open('bike2.png')
x = w.resize((125, 120))
img9 = ImageTk.PhotoImage(x)


ab = Image.open('correct1.png')
cd = ab.resize((125, 120))
correct = ImageTk.PhotoImage(ab)



b1 = Button(fr2, image = img5, width = 125, height = 120)#1

b1.grid(row = 1,column = 1)
b1.bind('<Button-1>', click)


b2 = Button(fr2, image = img1, width = 125, height = 120)

b2.grid(row = 1,column = 2)#2
b2.bind('<Button-1>', on)


b3 = Button(fr2, image = img6, width = 125, height = 120)

b3.grid(row = 1,column = 3)#3
b3.bind('<Button-1>', click1)


b4 = Button(fr2, image = img7, width = 125, height = 120)

b4.grid(row = 2,column = 1)#4
b4.bind('<Button-1>', click2)


b5 = Button(fr2, image = img8, width = 125, height = 120)

b5.grid(row = 2,column = 2)#5
b5.bind('<Button-1>', click3)


b6 = Button(fr2, image = img3, width = 125, height = 120)

b6.grid(row = 2,column = 3)#6
b6.bind('<Button-1>', sel2)


b7 = Button(fr2, image = img2, width = 125, height = 120)

b7.grid(row = 3,column = 1)#7
b7.bind('<Button-1>', sel1)


b8 = Button(fr2, image = img4, width = 125, height = 120)

b8.grid(row = 3,column = 2)#8
b8.bind('<Button-1>', sel3)


b9 = Button(fr2, image = img9, width = 125, height = 120)

b9.grid(row = 3,column = 3)#9
b9.bind('<Button-1>', click4)


Button(fr2, bg = 'lightblue',text = "Verify",width = 17,command = check).grid(row = 4,column = 3)
    
captcha.mainloop()