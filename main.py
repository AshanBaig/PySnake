from tkinter import Tk,PhotoImage,Button,Label,Canvas
import time
import random
def start():
    global food_there,px,py,current_direction,score
    r=Tk()
    r.geometry('1300x650+0+0')
    r.resizable(False,False)
    r.state('zoom')
    px=20+100
    py=200
    current_direction='right'
    snake_width_1block=25
    snake_height_1block=25
    photo_bg=PhotoImage(file='snake_bgnewEditing.png')
    photo_L=Label(r,image=photo_bg).pack()
    block_place_x=100
    block_place_y=200
    #ang=0 #angle =ang
    snake_mouth_x=10
    snake_mouth_y=12
    
    food_there=False
    score=0
    def food():
        global c_food
        place_food_x=random.randrange(60,1200)
        place_food_y=random.randrange(80,580)
        c_food= Canvas(r, bg="blue", width=5, height=5)
        c_food.place(x=place_food_x,y=place_food_y)
        score_label=Label(text=score,bg='black',fg='white',font='halvetica 20 bold').place(x=265,y=650)
        return place_food_x,place_food_y 
    def out():
                def exit():
                     r2.destroy()
                def playagain():
                     r2.destroy()
                     begin(False)
                L=Label(text='X',fg='red',bg='white',font=',,bold',width=2)
                L.place(x=px,y=py)
                r.update()
                time.sleep(1) 
                r.destroy()
                r2=Tk()
                r2.geometry('1300x650+0+0')
                r2.resizable(False,False)
                r2.state('zoom')
                photo_bg=PhotoImage(file='snake_bgnew.png')
                photo_L=Label(r2,image=photo_bg).pack()
                L_gameover=Label(text='GAME OVER',font='halvetica 40 bold',fg='white',bg='black').place(x=500,y=100)
                L_score=Label(text=f'SCORE: {score}',font='halvetica 40 bold',fg='white',bg='black').place(x=500,y=300)
                L_playagain=Button(text='PLAY AGAIN',font='halvetica 40 bold',fg='white',bg='black',command=playagain).place(x=250,y=450)
                L_EXIT=Button(text=f'EXIT',font='halvetica 40 bold',fg='white',bg='black',width=12,command=exit).place(x=700,y=450)
                r2.update()
                
                r2.mainloop()    
    def block_adjusment(p1x,p1y,block_name):
            global Num_blocks
            if  current_direction=='up':
                p1y=py+(30*(block_name-1))
            elif current_direction=='down':
                p1y=py-(30*(block_name-1))
            elif current_direction=='left':
                p1x=px+(30*(block_name-1))
            else:
                p1x=px-(30*(block_name-1))
            return p1x,p1y
    def   func_direction(px,py):    
            if current_direction=='up':
                py-=15
            elif current_direction=='down':
                py+=15
            elif current_direction=='right':
                px+=15
            elif current_direction=='left':
                px-=15
            return px,py
    def movement(block_place_x,block_place_y):
        global chck,score,current_direction,food_there,p1x,p1y,px,py,canvas1
        while True:
            
            if food_there==False:
                
                tpl=food()
                food_there=True
            #time.sleep(0.3)
            #white se change kr rha
            if current_direction=='down':
                 ang=270
            elif current_direction=='right':
                 ang=0
            elif current_direction=='up':
                 ang=90
            else:
                 ang=180
            canvas1= Canvas(r, bg="white", width=snake_width_1block, height=snake_height_1block)
            canvas1.place(x=block_place_x,y=block_place_y)
            canvas1.create_text(snake_mouth_x,snake_mouth_y, text='  >',font='ariel,0',fill='red',angle=ang)
            canvas1.place_configure(x=px,y=py) #is se move kr rha
            r.update()
            if px<=20 or py<=59 or px>=1234 or py>=625: #touching on border
                out()
            #white se change kr rha
            p1x,p1y=block_adjusment(px,py,block_name=2)
            canvas2= Canvas(r, bg="white", width=snake_width_1block, height=snake_height_1block)
            canvas2.place(x=block_place_x-30,y=block_place_y)
            canvas2.create_text(snake_mouth_x,snake_mouth_y, text='  ',font='ariel,0',angle=ang) 
            canvas2.place_configure(x=p1x,y=p1y) #is se move kr rha
            r.update()
            p1x,p1y=block_adjusment(px,py,block_name=3)
            canvas3=Canvas(r, bg="white", width=snake_width_1block, height=snake_height_1block)
            canvas3.place(x=block_place_x-60,y=block_place_y)
            canvas3.create_text(snake_mouth_x,snake_mouth_y, text=' ',font='ariel,0',angle=ang) 
            canvas3.place_configure(x=p1x,y=p1y) #is se move kr rha  #px me - + krwa do bsss for new block
            r.update()
            
            px,py=func_direction(px,py)
            #print(tpl[0],p1x,p1y,tpl[1],px,py)
            surrounding_x=15
            surrounding_y=15
            if current_direction=='up' or current_direction=='down':
                surrounding_y=20
                surrounding_x=20
            #print(px>=tpl[0]-10 and px<=tpl[0]+10)
            #print(p1y+15>=tpl[1]-10 and p1y<=tpl[1]+10)
            if (px>=tpl[0]-surrounding_x and px<=tpl[0]+surrounding_x) and (p1y+15>=tpl[1]-surrounding_y and p1y-15<=tpl[1]+surrounding_y):
                food_there=False
                score+=8
                c_food.destroy()
            canvas1.destroy()
            time.sleep(0.001)  #speed yaha se kro control
            time.sleep(0.0025)
            canvas2.destroy()
            time.sleep(0.0025)
            canvas3.destroy()
            
    def  up(*args): #Snake Mouth text
        global py,ang,current_direction,snake_mouth_x,snake_mouth_y
        if current_direction!='up' and current_direction!='down':
            current_direction='up'
            #ang=90
            py-=10
            snake_mouth_x=12
            snake_mouth_y=14
    def  down(*args): #Snake Mouth text
        global py,ang,current_direction,snake_mouth_x,snake_mouth_y
        if current_direction!='down' and current_direction!='up':
            current_direction='down'
            
            py+=10
            snake_mouth_x=14
            snake_mouth_y=14
    def  right(*args): #Snake Mouth text
        global px,ang,current_direction,snake_mouth_x,snake_mouth_y
        if current_direction!='right' and current_direction!='left':
            current_direction='right'
            px+=10
            #ang=0
            
            snake_mouth_x=10
            snake_mouth_y=12
    def  left(*args): #Snake Mouth text
        global px,ang,current_direction,snake_mouth_x,snake_mouth_y
        if current_direction!='left' and current_direction!='right':    
            current_direction='left'
            px-=10
            #ang=180
            snake_mouth_x=15
            snake_mouth_y=14
    def f_exit(*args):
        print('a')
        r.destroy()
    r.bind('<Up>',up)
    r.bind('<Down>',down)
    r.bind('<Right>',right)
    r.bind('<Left>',left)
    r.bind('<E>',f_exit)
    r.bind('<e>',f_exit)
    def xy_cordinates(event):
        print(event.x,',',event.y,'click me')
    r.bind('<Button-1>',xy_cordinates)
    movement(block_place_x,block_place_y)
    r.mainloop()
    
#start()
def begin(firsttime=True):
    if firsttime:
        start_up.destroy()
    start()
start_up=Tk()
start_up.geometry('1300x650+0+0')
start_up.resizable(False,False)
start_up.state('zoom')
photo_bg=PhotoImage(file='snake_bg.png')
photo_L=Label(start_up,image=photo_bg).pack()
b1=Button(text='START',fg='white',bg='black',font='timesnewroman 30 bold',width=25,height=2,command=begin)
b1.place(x=150+150+20,y=300-50)
start_up.mainloop()