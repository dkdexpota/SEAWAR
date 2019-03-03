from tkinter import*
import random
c=[[0 for i in range(0,12)]for j in range(0,12)]
import copy
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
    x=random.randint(1,10)
    y=random.randint(1,10)
    if(c[x][y]==0)and(c[x-1][y]!=1)and(c[x-1][y-1]!=1)and(c[x-1][y+1]!=1)and(c[x][y-1]!=1)and(c[x][y+1]!=1)and(c[x+1][y-1]!=1)and(c[x+1][y]!=1)and(c[x+1][y+1]!=1):
        g+=1
        c[x][y]=1


root=Tk()
display_text=StringVar()
display_text.set('0')
chet=Label(root,textvariable=display_text, width=4, height=2, font='Arial 35', fg='gray')
chet.grid(row=11,column=11)

up=StringVar()
up.set('0')
chetup=Label(root,textvariable=up)

slovo0=Label(root, text='Р', fg='gray', font='Arial 35')
slovo0.grid(row=11,column=1)
slovo1=Label(root, text='е', fg='gray', font='Arial 35')
slovo1.grid(row=11,column=2)
slovo2=Label(root, text='з', fg='gray', font='Arial 35')
slovo2.grid(row=11,column=3)
slovo3=Label(root, text='у', fg='gray', font='Arial 35')
slovo3.grid(row=11,column=4)
slovo4=Label(root, text='л', fg='gray', font='Arial 35')
slovo4.grid(row=11,column=5)
slovo5=Label(root, text='ь', fg='gray', font='Arial 35')
slovo5.grid(row=11,column=6)
slovo6=Label(root, text='т', fg='gray', font='Arial 35')
slovo6.grid(row=11,column=7)
slovo7=Label(root, text='а', fg='gray', font='Arial 35')
slovo7.grid(row=11,column=8)
slovo8=Label(root, text='т', fg='gray', font='Arial 35')
slovo8.grid(row=11,column=9)
slovo9=Label(root, text=':', fg='gray', font='Arial 35')
slovo9.grid(row=11,column=10)

def kill1(i,j):
    if c[i+1][j]==0:
        c[i+1][j]=4
        k[i][j-1].but.unbind('<ButtonPress>')
        k[i][j-1].but.configure(bg='red')
    if c[i][j+1]==0:
        c[i][j+1]=4
        k[i-1][j].but.unbind('<ButtonPress>')
        k[i-1][j].but.configure(bg='red')
    if c[i][j-1]==0:
        c[i][j-1]=4
        k[i-1][j-2].but.unbind('<ButtonPress>')
        k[i-1][j-2].but.configure(bg='red')
    if c[i-1][j]==0:
        c[i-1][j]=4
        k[i-2][j-1].but.unbind('<ButtonPress>')
        k[i-2][j-1].but.configure(bg='red')

def kill2(i,j):
    if c[i+1][j]==3:
        if c[i+2][j]==3:
            if c[i+3][j]==3:
                if c[i-1][j]!=2:
                    c[i-1][j]=4
                    k[i-2][j-1].but.unbind('<ButtonPress>')
                    k[i-2][j-1].but.configure(bg='red')
                if c[i+4][j]!=2:
                    c[i+4][j]=4
                    k[i+3][j-1].but.unbind('<ButtonPress>')
                    k[i+3][j-1].but.configure(bg='red')


            elif c[i-1][j]==3:
                if c[i+2][j]!=2:
                    c[i+2][j]=4
                    k[i+1][j-1].but.unbind('<ButtonPress>')
                    k[i+1][j-1].but.configure(bg='red')
                if c[i-2][j]!=2:
                    c[i-2][j]=4
                    k[i-3][j-1].but.unbind('<ButtonPress>')
                    k[i-3][j-1].but.configure(bg='red')

            elif c[i-1][j]!=1 and c[i+3][j]!=1:
                if c[i-1][j]!=2:
                    c[i-1][j]=4
                    k[i-2][j-1].but.unbind('<ButtonPress>')
                    k[i-2][j-1].but.configure(bg='red')
                if c[i+3][j]!=2:
                    c[i+3][j]=4
                    k[i+2][j-1].but.unbind('<ButtonPress>')
                    k[i+2][j-1].but.configure(bg='red')

        elif c[i-1][j]==3:
            if c[i-2][j]==3:
                if c[i-3][j]!=2:
                    c[i-3][j]=4
                    k[i-4][j-1].but.unbind('<ButtonPress>')
                    k[i-4][j-1].but.configure(bg='red')
                if c[i+2][j]!=2:
                    c[i+2][j]=4
                    k[i+1][j-1].but.unbind('<ButtonPress>')
                    k[i+1][j-1].but.configure(bg='red')

            elif c[i-2][j]!=1 and c[i+2][j]!=1:
                if c[i-2][j]!=2:
                    c[i-2][j]=4
                    k[i-3][j-1].but.unbind('<ButtonPress>')
                    k[i-3][j-1].but.configure(bg='red')
                if c[i+2][j]!=2:
                    c[i+2][j]=4
                    k[i+1][j-1].but.unbind('<ButtonPress>')
                    k[i+1][j-1].but.configure(bg='red')

        elif c[i+2][j]!=1 and c[i-1][j]!=1:
            if c[i+2][j]!=1 and c[i-1][j]!=1 :
                if c[i+2][j]!=2:
                    c[i+2][j]=4
                    k[i+1][j-1].but.unbind('<ButtonPress>')
                    k[i+1][j-1].but.configure(bg='red')
                if c[i-1][j]!=2:
                    c[i-1][j]=4
                    k[i-2][j-1].but.unbind('<ButtonPress>')
                    k[i-2][j-1].but.configure(bg='red')



    elif c[i][j+1]==3:
        if c[i][j+2]==3:
            if c[i][j+3]==3:
                if c[i][j-1]!=2:
                    c[i][j-1]=4
                    k[i-1][j-2].but.unbind('<ButtonPress>')
                    k[i-1][j-2].but.configure(bg='red')
                if c[i][j+4]!=2:
                    c[i][j+4]=4
                    k[i-1][j+3].but.unbind('<ButtonPress>')
                    k[i-1][j+3].but.configure(bg='red')


            elif c[i][j-1]==3:
                if c[i][j+2]!=2:
                    c[i][j+2]=4
                    k[i-1][j+1].but.unbind('<ButtonPress>')
                    k[i-1][j+1].but.configure(bg='red')
                if c[i][j-2]!=2:
                    c[i][j-2]=4
                    k[i-1][j-3].but.unbind('<ButtonPress>')
                    k[i-1][j-3].but.configure(bg='red')

            elif c[i][j-1]!=1 and c[i][j+3]!=1:
                if c[i][j-1]!=2:
                    c[i][j-1]=4
                    k[i-1][j-2].but.unbind('<ButtonPress>')
                    k[i-1][j-2].but.configure(bg='red')
                if c[i][j+3]!=2:
                    c[i][j+3]=4
                    k[i-1][j+2].but.unbind('<ButtonPress>')
                    k[i-1][j+2].but.configure(bg='red')

        elif c[i][j-1]==3:
            if c[i][j-2]==3:
                if c[i][j-3]!=2:
                    c[i][j-3]=4
                    k[i-1][j-4].but.unbind('<ButtonPress>')
                    k[i-1][j-4].but.configure(bg='red')
                if c[i][j+2]!=2:
                    c[i][j+2]=4
                    k[i-1][j+1].but.unbind('<ButtonPress>')
                    k[i-1][j+1].but.configure(bg='red')

            elif c[i][j-2]!=1 and c[i][j+2]!=1:
                if c[i][j-2]!=2:
                    c[i][j-2]=4
                    k[i-1][j-1].but.unbind('<ButtonPress>')
                    k[i-1][j-1].but.configure(bg='red')
                if c[i][j+2]!=2:
                    c[i][j+2]=4
                    k[i-1][j+1].but.unbind('<ButtonPress>')
                    k[i-1][j+1].but.configure(bg='red')

        elif c[i][j+2]!=1 and c[i][j-1]!=1:
            if c[i][j+2]!=2:
                c[i][j+2]=4
                k[i-1][j+1].but.unbind('<ButtonPress>')
                k[i-1][j+1].but.configure(bg='red')
            if c[i][j-1]!=2:
                c[i][j-1]=4
                k[i-1][j-2].but.unbind('<ButtonPress>')
                k[i-1][j-2].but.configure(bg='red')


    elif c[i-1][j]==3:
        if c[i-2][j]==3:
            if c[i-3][j]==3:
                if c[i+1][j]!=2:
                    c[i+1][j]=4
                    k[i][j-1].but.unbind('<ButtonPress>')
                    k[i][j-1].but.configure(bg='red')
                if c[i-4][j]!=2:
                    c[i-4][j]=4
                    k[i-5][j-1].but.unbind('<ButtonPress>')
                    k[i-5][j-1].but.configure(bg='red')

            elif c[i+1][j]!=1 and c[i-3][j]!=1:
                if c[i+1][j]!=2:
                    c[i+1][j]=4
                    k[i][j-1].but.unbind('<ButtonPress>')
                    k[i][j-1].but.configure(bg='red')
                if c[i-3][j]!=2:
                    c[i-3][j]=4
                    k[i-4][j-1].but.unbind('<ButtonPress>')
                    k[i-4][j-1].but.configure(bg='red')

        elif c[i+1][j]!=1 and c[i-2][j]!=1:
            if c[i-2][j]!=2:
                c[i-2][j]=4
                k[i-3][j-1].but.unbind('<ButtonPress>')
                k[i-3][j-1].but.configure(bg='red')
            if c[i+1][j]!=2:
                c[i+1][j]=4
                k[i][j-1].but.unbind('<ButtonPress>')
                k[i][j-1].but.configure(bg='red')


    elif c[i][j-1]==3:
        if c[i][j-2]==3:
            if c[i][j-3]==3:
                if c[i][j+1]!=2:
                    c[i][j+1]=4
                    k[i-1][j].but.unbind('<ButtonPress>')
                    k[i-1][j].but.configure(bg='red')
                if c[i][j-4]!=2:
                    c[i][j-4]=4
                    k[i-1][j-5].but.unbind('<ButtonPress>')
                    k[i-1][j-5].but.configure(bg='red')

            elif c[i][j+1]!=1 and c[i][j-3]!=1:
                if c[i][j+1]!=2:
                    c[i][j+1]=4
                    k[i-1][j].but.unbind('<ButtonPress>')
                    k[i-1][j].but.configure(bg='red')
                if c[i][j-3]!=2:
                    c[i][j-3]=4
                    k[i-1][j-4].but.unbind('<ButtonPress>')
                    k[i-1][j-4].but.configure(bg='red')

        elif c[i][j-2]!=1 and c[i][j+1]!=1 :
            if c[i][j-2]!=2:
                c[i][j-2]=4
                k[i-1][j-3].but.unbind('<ButtonPress>')
                k[i-1][j-3].but.configure(bg='red')
            if c[i][j+1]!=2:
                c[i][j+1]=4
                k[i-1][j].but.unbind('<ButtonPress>')
                k[i-1][j].but.configure(bg='red')

class pole1():
    def __init__(self,i,j):

        if(c[i][j]==0):
            self.but = Label(root, text='', bg='#710000', width=9, height=4)
            self.but.grid(row=i, column=j, padx=1, pady=1)

        elif(c[i][j]==1):
            self.but = Label(root, text='', bg='#007100', width=9, height=4)
            self.but.grid(row=i, column=j, padx=1, pady=1)

        elif(c[i][j]==3):
            self.but = Label(root, text='', bg='#0b0', width=9, height=4)
            self.but.grid(row=i, column=j, padx=1, pady=1)

        elif(c[i][j]==4):
            self.but = Label(root, text='', bg='red', width=9, height=4)
            self.but.grid(row=i, column=j, padx=1, pady=1)

def hit(i,j):
    if c[i+1][j+1]==0:
        c[i+1][j+1]=4
        k[i][j].but.unbind('<ButtonPress>')
        k[i][j].but.configure(bg='red')
    if c[i+1][j-1]==0:
        c[i+1][j-1]=4
        k[i][j-2].but.unbind('<ButtonPress>')
        k[i][j-2].but.configure(bg='red')
    if c[i-1][j+1]==0:
        c[i-1][j+1]=4
        k[i-2][j].but.unbind('<ButtonPress>')
        k[i-2][j].but.configure(bg='red')
    if c[i-1][j-1]==0:
        c[i-1][j-1]=4
        k[i-2][j-2].but.unbind('<ButtonPress>')
        k[i-2][j-2].but.configure(bg='red')




def main():
    global image
    image = PhotoImage(file='16.png')
    label = Label(root, image=image)
    label.grid(row=8,column=11)

    slovo81=Label(root, text='↓↓↓', fg='gray', font='Arial 35')
    slovo81.grid(row=9,column=11)
    slovo91=Label(root, text='2k19', fg='gray', font='Arial 35')
    slovo91.grid(row=9,column=11)

class pole():

    def __init__(self,i,j):


        self.back='blue'
        self.but = Label(root, text='', bg='gray', width=9, height=4)
        self.but.grid(row=i, column=j, padx=1, pady=1)

        def lox(event):

            if(c[i][j]==0):
                c[i][j]=4
                self.count=display_text.get()
                m=int(self.count)
                m-=1
                self.count=m
                display_text.set(self.count)
                self.but.unbind('<ButtonPress>')
                self.but.configure(bg='red')
                if self.count-int(up.get())-int(up.get())==-45:
                    k=[[pole1(i,j) for j in range(1,11)]for i in range(1,11)]
                    slovo01=Label(root, text='L', fg='#f00', font='Courier 35')
                    slovo01.grid(row=1,column=11)
                    slovo01=Label(root, text='O', fg='#f00', font='Courier 35')
                    slovo01.grid(row=2,column=11)
                    slovo01=Label(root, text='S', fg='#f00', font='Courier 35')
                    slovo01.grid(row=3,column=11)
                    slovo01=Label(root, text='E', fg='#f00', font='Courier 35')
                    slovo01.grid(row=4,column=11)
                    slovo01=Label(root, text='(BAN)', fg='#f00', font='Courier 27')
                    slovo01.grid(row=5,column=11)




            if(c[i][j]==1):
                c[i][j]=3
                self.upcount=up.get()
                n=int(self.upcount)
                n+=1
                self.upcount=n
                up.set(self.upcount)
                self.count=display_text.get()
                m=int(self.count)
                m+=1
                self.count=m
                display_text.set(self.count)
                self.but.unbind('<ButtonPress>')
                self.but.configure(bg='#0b0')
                hit(i,j)
                if(c[i+1][j]==0 or c[i+1][j]==4 or c[i+1][j]==2)and(c[i][j+1]==0 or c[i][j+1]==4 or c[i][j+1]==2)and(c[i][j-1]==0 or c[i][j-1]==4 or c[i][j-1]==2)and(c[i-1][j]==0 or c[i-1][j]==4 or c[i-1][j]==2):
                    kill1(i,j)
                kill2(i,j)



                if self.upcount==20:
                    slovo01=Label(root, text='W', fg='#0f0', font='Courier 35')
                    slovo01.grid(row=1,column=11)
                    slovo01=Label(root, text='I', fg='#0f0', font='Courier 35')
                    slovo01.grid(row=2,column=11)
                    slovo01=Label(root, text='N', fg='#0f0', font='Courier 35')
                    slovo01.grid(row=3,column=11)
                    k=[[pole1(i,j) for j in range(1,11)]for i in range(1,11)]
                    main()




        self.but.bind('<ButtonPress>', lox)


global k
k=[[pole(i,j) for j in range(1,11)]for i in range(1,11)]

root.mainloop()