from tkinter import *
v=Tk()
v.title("Mario")
can = Canvas(v,width=1600,height=720)
can.focus_set()
can.config(bg="black")
can.pack()


mapaI = PhotoImage(file="mapaf.png")

#menu
menu1I = PhotoImage(file="menu1.gif")
menu2I = PhotoImage(file="menu2.gif")
playI = PhotoImage(file="play.gif")
opcI = PhotoImage(file="opciones.gif")

#mario
m0= PhotoImage(file="m00.png")
m1= PhotoImage(file="m0.png")
m2= PhotoImage(file="m1.png")
m3 = PhotoImage(file="m2.png")
m4= PhotoImage(file="m3.png")
m5= PhotoImage(file="m33.png")
m6 = PhotoImage(file="m6.png")
m7 = PhotoImage(file="m7.png")

#borrar
##M=[0,0,0,0,0,0,0,0]
##M[0]=Label(can,image=m0,bg="black")
##M[1]=Label(can,image=m1,bg="black")
##M[2]=Label(can,image=m2,bg="black")
##M[3]=Label(can,image=m3,bg="black")
##M[4]=Label(can,image=m4,bg="black")
##M[5]=Label(can,image=m5,bg="black")
##M[6]=Label(can,image=m6,bg="black")
##M[7]=Label(can,image=m7,bg="black")

#enemigo
ec0=PhotoImage(file="EC0.png")
ec1=PhotoImage(file="EC1.png")
ec2=PhotoImage(file="EC2.png")
ec3=PhotoImage(file="EC3.png")
ec4=PhotoImage(file="EC4.png")


est = 3
#juego
mx = 100
my = 425
mar=0
ya = False
st=False
ys = 0
E=[]
def Menu():
    global v,can,menu1I,menu2I,x1,x2,menu1,menu2,botoJ,botoO
    menu1.destroy()
    menu2.destroy()
    x1 += 10
    x2 -= 10
    menu1= Label(can,image=menu1I)
    menu1.place(x=x1,y=0)
    menu2= Label(can,image=menu2I)
    menu2.place(x=x2,y=0)
    if(x1<0):
        v.after(2,Menu)
    else:
        botoJ = Button(can,command=Play,image=playI)
        botoJ.place(x=570,y=300)
        botoO = Button(can, command=Play,image=opcI)
        botoO.place(x=570,y=450)


def Play():
    global v,can,menu1I,menu2I,M,mar,E
    mapa = Label(can,image=mapaI)
    mapa.pack()
    y=0
    while y <= 1600:
        Label(can,text=y).place(x=y,y=5)
        y+= 20
    mar=Label(can,image=m3,bg="black")
    mar.place(x=100,y=425)
    E.append([2,80,116])
    E[0].append(Label(can,image=ec2,bg="black"))
    E[0][3].place(x=E[0][1],y=E[0][2])
    
    E.append([0,450,116])
    E[1].append(Label(can,image=ec0,bg="black"))
    E[1][3].place(x=E[1][1],y=E[1][2])
    #M[2].place_forget()


def salto():
    global v,can,M,mar,mx,my,est,ya,st,ys,est
    v1 = ( (ys <= 130 and st== False) and ((my>=425-35 or (mx>=200 and mx<=330 and my>=285)or(my<=315 and my>= 285)or (mx>=50 and mx<=115 and my>=150 and my<=315)or(my<=315 and my>=100 and mx>=415 and mx<=470)or(my>=180 and my<=205)or(my<=100 and my >=0)or(my<=205 and my >=0 and mx>=230 and mx<=290))))
    v2 = ((my<=425 and my!=315 and my != 205 and my!=100)or(my<=315 and my > 205 and (mx>=200 and mx<=330))or(my<=205 and (mx>=50 and mx<=115)and my>=115)or(my<=205 and (mx>=415 and mx<=470)and my>=115)or(my<=205 and (mx>=230 and mx<=290)or(my<=100 and my>=0 )))
    if(est==1 or est==0):
        mar.destroy()
        if(v1):
            my-=5
            mx-=3
            ys+=5
        else:
            if(v2):
                my+=5
            mx-=3
            ys-=5
            st= True
        mar=Label(can,image=m6,bg="black")
        mar.place(x=mx,y=my) 
        
        
    elif(est== 2):
        mar.destroy()
        if( v1):
            my-=5
            ys+=5
        else:
            if(v2):
                my+=5
            ys-=5
            st= True
        mar=Label(can,image=m6,bg="black")
        mar.place(x=mx,y=my) 
        
    elif(est== 3):
        mar.destroy()
        if( v1):
            my-=5
            ys+=5
        else:
            if(v2):
                my+=5
            ys-=5
            st= True
        mar=Label(can,image=m7,bg="black")
        mar.place(x=mx,y=my)
        
    elif(est==4 or est==5):
        mar.destroy()
        if( v1):
            my-=5
            mx+=3
            ys+=5
        else:
            if(v2):
                my+=5
            mx+=3
            ys-=5
            st= True
        mar=Label(can,image=m7,bg="black")
        mar.place(x=mx,y=my) 

    if(ya == True and ys>0 and (my != 315 or (mx>=200 and mx<=330 and my >= 275))and(my != 205 or ((mx>=50 and mx<=115 and my>=100 and my<= 205)or(mx>=415 and mx<=470 and my>=100 and my<= 205)))and(my != 100 or (mx>=230 and mx<=290 and my >= 0 and my <= 100))):
        v.after(20,salto)
    else:
        ya=False
        st=False
        ys= 0
        if(est==0 or est ==1 or est == 2):
            mar.destroy()
            mar=Label(can,image=m2,bg="black")
            mar.place(x=mx,y=my)
            est=2
        else:
            mar.destroy()
            mar=Label(can,image=m3,bg="black")
            mar.place(x=mx,y=my)
            est=3
            
def parado():
    global v,can,M,mx,my,mar,est,ya
    if((est==1 or est == 0) and ya==False):
        mar.destroy()
        mar = Label(can,image=m2,bg="black")
        mar.place(x=mx,y=my)
        est==2
    elif((est==4 or est==5) and ya==False):
        mar.destroy()
        mar = Label(can,image=m3,bg="black")
        mar.place(x=mx,y=my)
        est=3
    v.after(800,parado)

def key(event):
    global v,can,M,mx,my,mar,est,ya
    tecla = repr(event.char)
    if(ya == False):
        if(my <= 500 and my >= 320):
            my = 425
        elif(my < 320 and my >= 210):
            my = 315
        elif(my < 210 and my >= 105):
            my = 205
        elif(my<105):
            my = 100
        
    if(tecla == "'a'" and ((mx > 75 and my==425)or(mx>5 and my==315)or(mx>5 and my==205)or(mx>=100 and my==100)) and ya == False):
        mx -= 10
        mar.destroy()
        if(est!=0):
            mar = Label(can,image=m0,bg="black")
            mar.place(x=mx,y=my)
            est=0
        else:
            mar = Label(can,image=m1,bg="black")
            mar.place(x=mx,y=my)
            est=1
    if(tecla == "'d'" and ((mx <450 and my==425)or(mx<500 and my==315)or(mx<500 and my==205)or (mx<=400 and my==100)) and ya == False):
        mx += 10
        mar.destroy()
        if(est!=5):
            mar = Label(can,image=m5,bg="black")
            mar.place(x=mx,y=my)
            est=5
        else:
            mar = Label(can,image=m4,bg="black")
            mar.place(x=mx,y=my)
            est=4

    if(tecla == "'w'" and ya == False):
        ya = True
        salto()

def Caida():
    global v,can,M,mx,my,mar,est,ya
    if(ya == False and (((mx>=200 and mx<=330 and my >= 215)or(((mx>=50 and mx<=115)or(mx>=415 and mx<=475)) and (my < 315 and my >110))or(my<205 and (mx>=230 and mx<=290)))and my < 425)):
        my += 5
        mar.destroy()
        if(est ==0 or est==1 or est==2):
            mar = Label(can,image=m2,bg="black")
            mar.place(x=mx,y=my)
            v.after(20,Caida)
        else:
            mar = Label(can,image=m3,bg="black")
            mar.place(x=mx,y=my)
            v.after(20,Caida)
    else:
        if(mx <= 5):
            mx=485
        if(mx>=490):
            mx=10
        if(my<=100):
            if(mx<=105):
                mx=440
                my=425
                ya = False
            elif(mx>=395):
                mx=90
                my=425
                ya = False
        if(my<=425 and my >= 320):
            if(mx<=80):
                mx=390
                my=100
                ya = False
            if(mx>=445):
                mx=90
                my=100
                ya = False
        v.after(100,Caida)

def Enemigos():
    global v,can,M,mx,my,mar,est,ya,E,dif
    x=0
    while x < len(E):
        if(E[x][0] != 4):
            if(E[x][0] == 2 or E[x][0] == 3):
                if(E[x][1] < 500): 
                    E[x][1]+=dif
                    if(E[x][0] == 2):
                        E[x][3].destroy()
                        E[x][3]= Label(can,image=ec2,bg="black")
                        E[0][3].place(x=E[x][1],y=E[x][2])
                        E[x][0] = 3
                    elif(E[x][0] == 3):
                        E[x][3].destroy()
                        E[x][3]= Label(can,image=ec3,bg="black")
                        E[x][3].place(x=E[x][1],y=E[x][2])
                        E[x][0] = 2
                else:
                    E[x][1]=5
                 
            elif(E[x][0] == 0 or E[x][0] == 1):
                if(E[x][1] > 5): 
                    E[x][1]-=dif
                    if(E[x][0] == 0):
                        E[x][3].destroy()
                        E[x][3]= Label(can,image=ec0,bg="black")
                        E[x][3].place(x=E[x][1],y=E[x][2])
                        E[x][0] = 1
                    elif(E[x][0] == 1):
                        E[x][3].destroy()
                        E[x][3]= Label(can,image=ec1,bg="black")
                        E[x][3].place(x=E[x][1],y=E[x][2])
                        E[x][0] = 0
                else:
                    E[x][1]= 500
            if(E[x][2]>=116 and E[x][1] >=230 and E[x][1] <= 290 and E[x][2] < 221 ):
                    E[x][2]+=min(221-E[x][2],10)
            if((E[x][2]>=221 and E[x][2] < 332)and((E[x][1] >=415 and E[x][1] <= 475)or(E[x][1] >=50 and E[x][1] <= 115))  ):
                    E[x][2]+=min(332-E[x][2],10)
            if(E[x][2]>=332 and E[x][1] >=200 and E[x][1] <= 330 and E[x][2] < 441 ):
                    E[x][2]+=min(441-E[x][2],10)
            if(E[x][2]<=116):
                if(E[x][1]<80):
                    E[x][1]=450
                    E[x][2]=441
                elif(E[x][1]>450):
                    E[x][1]=80
                    E[x][2]=441
            if(E[x][2]<=441 and E[x][2] >= 340):
                if(E[x][1]<80):
                    E[x][1]=450
                    E[x][2]=116
                if(E[x][1]>450):
                    E[x][1]=80
                    E[x][2]=116
        x+=1
    v.after(80,Enemigos)
dif=5
x1 = -1020
x2 = 1740
menu1= Label(can,image=menu1I)
menu1.place(x=x1,y=0)
menu2= Label(can,image=menu2I)
menu2.place(x=x2,y=0)
botoJ=0
botoO=0
Play()
Enemigos()
Caida()
parado()
can.bind("<Key>",key)

v.mainloop()


