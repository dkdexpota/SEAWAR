from tkinter import*
import random
c=[[0 for i in range(0,12)]for j in range(0,12)]

x=random.randint(1,9)
y=random.randint(1,9)

for i in range(12):
    c[i][0]=2
for i in range(12):
    c[i][11]=2
for i in range(12):
    c[0][i]=2
for i in range(12):
    c[11][i]=2


a=[]

if x<=4:
    a.append(1)
if x>4:
    a.append(2)
if x<=7:
    a.append(1)
if x>7:
    a.append(2)

if y<=4:
    a.append(3)
if y>4:
    a.append(4)
if y<=7:
    a.append(3)
if y>7:
    a.append(4)

l=random.choice(a)

if l==1:
    c[x][y]=1
    c[x+1][y]=1
    c[x+2][y]=1
    c[x+3][y]=1
elif l==2:
    c[x][y]=1
    c[x-1][y]=1
    c[x-2][y]=1
    c[x-3][y]=1
elif l==3:
    c[x][y]=1
    c[x][y+1]=1
    c[x][y+2]=1
    c[x][y+3]=1
elif l==4:
    c[x][y]=1
    c[x][y-1]=1
    c[x][y-2]=1
    c[x][y-3]=1
a.clear()
g=0
while g!=2:
    x=random.randint(1,9)
    y=random.randint(1,9)
    if(c[x][y]==0)and(c[x-1][y]!=1)and(c[x-1][y-1]!=1)and(c[x-1][y+1]!=1)and(c[x][y-1]!=1)and(c[x][y+1]!=1)and(c[x+1][y-1]!=1)and(c[x+1][y]!=1)and(c[x+1][y+1]!=1):
        if x<=3:
            if(c[x+2][y]==0)and(c[x+2][y-1]!=1)and(c[x+2][y+1]!=1)and(c[x+3][y]==0)and(c[x+3][y-1]!=1)and(c[x+3][y+1]!=1):
                a.append(1)
        if x>3:
            if(c[x-2][y]==0)and(c[x-2][y-1]!=1)and(c[x-2][y+1]!=1)and(c[x-3][y]==0)and(c[x-3][y-1]!=1)and(c[x-3][y+1]!=1):
                a.append(2)
        if x<=8:
            if(c[x+2][y]==0)and(c[x+2][y-1]!=1)and(c[x+2][y+1]!=1)and(c[x+3][y]==0)and(c[x+3][y-1]!=1)and(c[x+3][y+1]!=1):
                a.append(1)
        if x>8:
            if(c[x-2][y]==0)and(c[x-2][y-1]!=1)and(c[x-2][y+1]!=1)and(c[x-3][y]==0)and(c[x-3][y-1]!=1)and(c[x-3][y+1]!=1):
                a.append(2)

        if y<=3:
            if(c[x][y+2]==0)and(c[x-1][y+2]!=1)and(c[x+1][y+2]!=1)and(c[x][y+3]==0)and(c[x+1][y+3]!=1)and(c[x-1][y+3]!=1):
                a.append(3)
        if y>3:
            if(c[x][y-2]==0)and(c[x-1][y-2]!=1)and(c[x+1][y-2]!=1)and(c[x][y-3]==0)and(c[x+1][y-3]!=1)and(c[x-1][y-3]!=1):
                a.append(4)
        if y<=8:
            if(c[x][y+2]==0)and(c[x-1][y+2]!=1)and(c[x+1][y+2]!=1)and(c[x][y+3]==0)and(c[x+1][y+3]!=1)and(c[x-1][y+3]!=1):
                a.append(3)
        if y>8:
            if(c[x][y-2]==0)and(c[x-1][y-2]!=1)and(c[x+1][y-2]!=1)and(c[x][y-3]==0)and(c[x+1][y-3]!=1)and(c[x-1][y-3]!=1):
                a.append(4)

        if(len(a)>0):
            l=random.choice(a)
            g+=1
            if l==1:
                c[x][y]=1
                c[x+1][y]=1
                c[x+2][y]=1
            elif l==2:
                c[x][y]=1
                c[x-1][y]=1
                c[x-2][y]=1
            elif l==3:
                c[x][y]=1
                c[x][y+1]=1
                c[x][y+2]=1
            elif l==4:
                c[x][y]=1
                c[x][y-1]=1
                c[x][y-2]=1
            a.clear()

a.clear()
g=0
while g!=3:
    x=random.randint(1,9)
    y=random.randint(1,9)
    if(c[x][y]==0)and(c[x-1][y]!=1)and(c[x-1][y-1]!=1)and(c[x-1][y+1]!=1)and(c[x][y-1]!=1)and(c[x][y+1]!=1)and(c[x+1][y-1]!=1)and(c[x+1][y]!=1)and(c[x+1][y+1]!=1):
        if x<=3:
            if(c[x+2][y]==0)and(c[x+2][y-1]!=1)and(c[x+2][y+1]!=1):
                a.append(1)
        if x>3:
            if(c[x-2][y]==0)and(c[x-2][y-1]!=1)and(c[x-2][y+1]!=1):
                a.append(2)
        if x<=8:
            if(c[x+2][y]==0)and(c[x+2][y-1]!=1)and(c[x+2][y+1]!=1):
                a.append(1)
        if x>8:
            if(c[x-2][y]==0)and(c[x-2][y-1]!=1)and(c[x-2][y+1]!=1):
                a.append(2)

        if y<=3:
            if(c[x][y+2]==0)and(c[x-1][y+2]!=1)and(c[x+1][y+2]!=1):
                a.append(3)
        if y>3:
            if(c[x][y-2]==0)and(c[x-1][y-2]!=1)and(c[x+1][y-2]!=1):
                a.append(4)
        if y<=8:
            if(c[x][y+2]==0)and(c[x-1][y+2]!=1)and(c[x+1][y+2]!=1):
                a.append(3)
        if y>8:
            if(c[x][y-2]==0)and(c[x-1][y-2]!=1)and(c[x+1][y-2]!=1):
                a.append(4)

        if(len(a)>0):
            l=random.choice(a)
            g+=1
            if l==1:
                c[x][y]=1
                c[x+1][y]=1
            elif l==2:
                c[x][y]=1
                c[x-1][y]=1
            elif l==3:
                c[x][y]=1
                c[x][y+1]=1
            elif l==4:
                c[x][y]=1
                c[x][y-1]=1
            a.clear()

g=0
while g!=4:
    x=random.randint(1,9)
    y=random.randint(1,9)
    if(c[x][y]==0)and(c[x-1][y]==0)and(c[x-1][y-1]==0)and(c[x-1][y+1]==0)and(c[x][y-1]==0)and(c[x][y+1]==0)and(c[x+1][y-1]==0)and(c[x+1][y]==0)and(c[x+1][y+1]==0):
        g+=1
        c[x][y]=1





root=Tk()
display_text=StringVar()
display_text.set('0')
chet=Label(root,textvariable=display_text, width=4, height=2, font='Arial 35', fg='gray')
chet.grid(row=10,column=10)


slovo0=Label(root, text='Р', fg='gray', font='Arial 35')
slovo0.grid(row=10,column=0)
slovo1=Label(root, text='е', fg='gray', font='Arial 35')
slovo1.grid(row=10,column=1)
slovo2=Label(root, text='з', fg='gray', font='Arial 35')
slovo2.grid(row=10,column=2)
slovo3=Label(root, text='у', fg='gray', font='Arial 35')
slovo3.grid(row=10,column=3)
slovo4=Label(root, text='л', fg='gray', font='Arial 35')
slovo4.grid(row=10,column=4)
slovo5=Label(root, text='ь', fg='gray', font='Arial 35')
slovo5.grid(row=10,column=5)
slovo6=Label(root, text='т', fg='gray', font='Arial 35')
slovo6.grid(row=10,column=6)
slovo7=Label(root, text='а', fg='gray', font='Arial 35')
slovo7.grid(row=10,column=7)
slovo8=Label(root, text='т', fg='gray', font='Arial 35')
slovo8.grid(row=10,column=8)
slovo9=Label(root, text=':', fg='gray', font='Arial 35')
slovo9.grid(row=10,column=9)

class pole():

    def __init__(self,i,j):


        self.back='blue'
        self.but = Label(root, text='', bg='gray', width=9, height=4)


        self.but.grid(row=i, column=j, padx=1, pady=1)

        def lox(event):

            if(c[i+1][j+1]==0):

                self.count=display_text.get()
                m=int(self.count)
                m-=1
                self.count=m
                display_text.set(self.count)
                self.but.unbind('<ButtonPress>')
                self.but.configure(bg='red')

            if(c[i+1][j+1]==1):
                self.count=display_text.get()
                m=int(self.count)
                m+=1
                self.count=m
                display_text.set(self.count)
                self.but.unbind('<ButtonPress>')
                self.but.configure(bg='#0b0')

        self.but.bind('<ButtonPress>', lox)


k=[[pole(i,j) for i in range(10)]for j in range(10)]

root.mainloop()