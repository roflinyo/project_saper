from tkinter import *
import random
import copy



class TryAgain( Frame):

    def __init__(self, master):
        super().__init__(master)
        self.sct = 0
        self.create_widget()

    def create_widget(self):
        self.bttn = Button(self)
        self.bttn['command'] =  self.update_count
        self.bttn['background'] = "blue"
        self.bttn['height'] = 3
        self.bttn['width'] = 11
        self.bttn['text'] = 'try again'
        #self.bttn['pady'] = 28
        self.bttn.grid()
    def update_count(self):
        global mas, tr, per, z, scht
        for i in range(z):
            for ii in range(z):
                mas[i][ii].ochistka()
        scht = 0
        per = 1
        tr = 1




#random.seed(1)
class Application( Frame):

    def __init__(self, master,x,y,r,r2):
        super().__init__(master)
        self.grid()
        #self.bttn_clicks = 0
        self.ox = x
        self.oy = y
        self.bomb = 0
        self.numb = 0
        self.razm = r
        self.razm2 = r2
        #gg = 0
        #self.act = 0
        self.create_widget()

    def create_widget(self):
        self.bttn = Button(self)
        self.bttn['command'] =  self.update_count
        self.bttn['background'] = "#555"
        self.bttn['height'] = self.razm
        self.bttn['width'] = self.razm2
        #self.bttn['padx'] = 35
        #self.bttn['pady'] = 28
        self.bttn.grid()


    def update_count(self):            
        global tr, per

        if per == 1:
            if tr == 1:
                self.begin()    
            elif self.bomb == 1:
                pole.gg()    
            elif self.numb!=0:
                self.bttn['background'] = "white"
                self.bttn['text'] = '{0}'.format(self.numb)
             
                
            else:
                if self.bttn['background'] == '#555':
                   
                    pole.rutin(self.ox, self.oy)
        

    def begin(self):  
        global tr, mas

        pole( mas,self.ox, self.oy )
        tr = 0
        pole.rutin(self.ox, self.oy)

    def boom(self):
        self.bttn['background'] = "red"
        self.bttn['text'] = '*'

    def boom2(self):
        self.bttn['background'] = "green"
        self.bttn['text'] = '*'

    def prst(self):

        self.bttn['background'] = "white"
        if self.numb != 0:
            self.bttn['text'] = '{0}'.format(self.numb)

    def ochistka(self):
        self.bomb = 0
        self.numb = 0
        self.bttn['background'] = "#555"
        self.bttn['text'] = ""

class pole():
    
    def __init__(self,lst,x,y):
        self.ttt = 0
        self.ox = x
        self.oy = y
        self.spisob = lst
        self.spis = self.bom()
        self.raspr()

    def bom(self):
        global bmlst, z, bomb
        bomlist = list()
        n = z - 1
        bombs = bomb
        for ik in range(bombs):
            while True:
                pr = random.randint(0,n)
                pr2 = random.randint(0,n)
                if pr != self.ox and pr2 != self.oy and [pr,pr2] not in bomlist:
                    bomlist.append([pr,pr2])
                    break
        
        
        bmlst = bomlist
        return bomlist



    def raspr(self):
        #print(self.spisob)
        global z
        for i in self.spisob:
            for i2 in i:
                for ii in self.spis:
                    if i2.ox == ii[0] and i2.oy == ii[1]:
                        i2.bomb = 1
                        
        n = z - 1
        for i in self.spis:
            if not ((i[0]+1 > n or i[0]+1 < 0) or (i[1] > n or i[1] < 0)):
                self.spisob[i[0]+1][i[1]].numb += 1
                
            if not ((i[0]+1 > n or i[0]+1 < 0) or (i[1]+1 > n or i[1]+1 < 0)):
                self.spisob[i[0]+1][i[1]+1].numb += 1
                
            if not ((i[0]+1 > n or i[0]+1 < 0) or (i[1]-1 > n or i[1]-1 < 0)):
                self.spisob[i[0]+1][i[1]-1].numb += 1
                
            if not ((i[0]-1 > n or i[0]-1 < 0) or (i[1] > n or i[1] < 0)):
                self.spisob[i[0]-1][i[1]].numb += 1
                
            if not ((i[0]-1 > n or i[0]-1 < 0) or (i[1]+1 > n or i[1]+1 < 0)):
                self.spisob[i[0]-1][i[1]+1].numb += 1
                
            if not ((i[0]-1 > n or i[0]-1 < 0) or (i[1]-1 > n or i[1]-1 < 0)):
                self.spisob[i[0]-1][i[1]-1].numb += 1
                
            if not ((i[0] > n or i[0] < 0) or (i[1]-1 > n or i[1]-1 < 0)):
                self.spisob[i[0]][i[1]-1].numb += 1
                
            if not ((i[0] > n or i[0] < 0) or (i[1]+1 > n or i[1]+1 < 0)):
                self.spisob[i[0]][i[1]+1].numb += 1
    

    def gg():
        global mas, bmlst, per, wh_kletki,z
        g = 0
        for i in range(len(mas)):
            for ii in range(z):
                if mas[i][ii].bttn['background'] == "white":
                    g += 1
        if g == wh_kletki:
            for i in bmlst:
                mas[i[0]][i[1]].boom2()
        else:
            for i in bmlst:
                mas[i[0]][i[1]].boom()
            per = 0



    def rutinend(lst):
        global mas
        for i in lst:
            mas[i[0]][i[1]].prst()

    def rutin(x,y):
        global mas, z, scht
        new_louris = list()
        louis = []
        lotis = [[x,y]]
        tst = []
        lotis2 = []
        n = z - 1
        if not mas[x][y].numb != 0:
        #if 1 == 1:
           
            while lotis != tst:
                for i in lotis:                               
                    if not ((i[0]+1 > n or i[0]+1 < 0) or (i[1] > n or i[1] < 0)):                    
                        if mas[i[0]+1][i[1]].numb !=0:
                            louis.append([i[0]+1,i[1]])
                        elif [i[0]+1,i[1]] not in louis:
                            lotis2.append([i[0]+1,i[1]])
                
                    if not ((i[0]+1 > n or i[0]+1 < 0) or (i[1]+1 > n or i[1]+1 < 0)):
                        if mas[i[0]+1][i[1]+1].numb !=0:
                            louis.append([i[0]+1,i[1]+1])
                        elif [i[0]+1,i[1]+1] not in louis:
                            lotis2.append([i[0]+1,i[1]+1])
                
                    if not ((i[0]+1 > n or i[0]+1 < 0) or (i[1]-1 > n or i[1]-1 < 0)):
                        if mas[i[0]+1][i[1]-1].numb !=0:
                            louis.append([i[0]+1,i[1]-1])
                        elif [i[0]+1,i[1]-1] not in louis:
                            lotis2.append([i[0]+1,i[1]-1])
                
                    if not ((i[0]-1 > n or i[0]-1 < 0) or (i[1] > n or i[1] < 0)):
                        if mas[i[0]-1][i[1]].numb !=0:
                            louis.append([i[0]-1,i[1]])
                        elif [i[0]-1,i[1]] not in louis:
                            lotis2.append([i[0]-1,i[1]])
                
                    if not ((i[0]-1 > n or i[0]-1 < 0) or (i[1]+1 > n or i[1]+1 < 0)):
                        if mas[i[0]-1][i[1]+1].numb !=0:
                            louis.append([i[0]-1,i[1]+1])
                        elif [i[0]-1,i[1]+1] not in louis:
                            lotis2.append([i[0]-1,i[1]+1])
                
                    if not ((i[0]-1 > n or i[0]-1 < 0) or (i[1]-1 > n or i[1]-1 < 0)):
                        if mas[i[0]-1][i[1]-1].numb !=0:
                            louis.append([i[0]-1,i[1]-1])
                        elif [i[0]-1,i[1]-1] not in louis:
                            lotis2.append([i[0]-1,i[1]-1])
                 
                    if not ((i[0] > n or i[0] < 0) or (i[1]-1 > n or i[1]-1 < 0)):
                        if mas[i[0]][i[1]-1].numb !=0:
                            louis.append([i[0],i[1]-1])
                        elif [i[0],i[1]-1] not in louis:
                            lotis2.append([i[0],i[1]-1])
                
                    if not ((i[0] > n or i[0] < 0) or (i[1]+1 > n or i[1]+1 < 0)):
                        if mas[i[0]][i[1]+1].numb !=0:
                            louis.append([i[0],i[1]+1])
                        elif [i[0],i[1]+1] not in louis:
                            lotis2.append([i[0],i[1]+1])

                    louis = louis + lotis2                             
                lotis = copy.deepcopy(lotis2)
            #print(lotis2)
                lotis2.clear()
            #print(lotis)
            #print(louis)
            #gg1 = input()
        
        louis.append([x,y])    
        for i in louis:
           if i not in new_louris:
              new_louris.append(i)
        del(lotis)
        del(lotis2)
        del(louis)
        pole.rutinend(new_louris)
        #print(new_louris)




root = Tk()
root.title("Click Counter")
print('новичок(1), любитель(2) или профессионал?(3)')
while True:
    dif = int(input())
    if dif == 1 or dif == 2 or dif == 3:
        break
#root.geometry('600x710')

if dif == 1:
    z = 9
    bomb = 12
    razm = 4
    razm2 = 8
    root.geometry('595x695')
elif dif == 2:
    z = 16
    bomb = 48
    razm = 2
    razm2 = 4
    root.geometry('610x715')
elif dif == 3:
    z = 25
    bomb = 110
    razm = 1
    razm2 = 2
    root.geometry('600x710')

mas = list()
wh_kletki = z*z - bomb
#z = 25
#bomb = 110
for k in range(z):
    mas.append(list())
    for l in range(z):
        mas[k].append(Application(root, k,l,razm,razm2))
for k in range(z):
    for l in range(z):        
        mas[k][l].grid( row=k, column=l,sticky = 'sw')
tr = 1
bmlst = 0
per = 1


gg1 = TryAgain(root)
gg1.place(relx = 0.42, rely = 0.92)
#gg.place(relx = 0.2, rely = 0.3)
#bomlist = [[0,0]]        
#print(bomlist)
#print(mas[3][18].numb)

while True:
    try:
        root.update()
    except:
        print("Спасибо за игру, надеюсь вам повезло больше чем другим...")
        break
