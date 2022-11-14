# importing the necessary modules 
import pygame 
from copy import deepcopy as dp 

# initialising the pygame 
pygame.init()
# setting the display 
plot=pygame.display.set_mode((1000,700))

# some global variables to be used in the code 
run = True

last,closedlist,openlist,s_sel,obstacle =[],[],[],[],[]
f_dict,g_dict,last_dict,dict_plot={},{},{},{}
itsstart = True 
startnode,drop,getpath,starttrav  = False,False,False,False
choice = 0
make = 'notstart'
final=[]
neighbours =[(1,0),(-1,0),(0,1),(0,-1)]
f_dict_copy = dp(f_dict)
obtained =  None
# the heuristic function to determine the heuristic value
def heusristic(coord):
    value = abs(s_sel[1][0]-coord[0])+ abs(s_sel[1][1]-coord[1])
    return value



# traversing the cell and move to the next cell
def traverse(start,prev=None):

    if start == s_sel[0]:

        last_dict[start]=prev    
        g_dict[start] = 0 
        f_dict[start] =heusristic(s_sel[0])+g_dict[start]
        f_dict_copy[start] = heusristic(s_sel[0])+g_dict[start]
        return [f_dict_copy[start],g_dict[start],heusristic(s_sel[0])]
    else:
        
        temp = g_dict[prev]+1
        h = heusristic(start)
        f = h+temp 
        g = [f,temp,h]
        return g

               
        
# code to traverse the path at the last  
def start_path(a):
    if a != s_sel[0]:
        final.append(a)
        a = last_dict[a]
        start_path(a)

# setting the cells with default values in the pygame grid 
def createplot():
    global dict_plot
    for i in range(0,35):
        for j in range(0,50):
            dict_plot[(j,i)] = 0

# pygame module starts
while run:
    plot.fill((0,0,0))

    # capturing the every event 
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            run = False
        
        # the code to select the first and last node 
        if not startnode and len(s_sel) <= 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                pos = pygame.mouse.get_pos()
                if dict_plot[(pos[0]//20,pos[1]//20)] != 'se':
                    s_sel.append((pos[0]//20,pos[1]//20))
                    dict_plot[(pos[0]//20,pos[1]//20)] = 'se'

        # the variable set up to start the path traverse 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                getpath = True 
                drop  = True
        if len(s_sel) == 2:
            startnode = True 
        
        # code to set the variables to drop the obstacles in the plot 
        if startnode:
            if event.type == pygame.MOUSEBUTTONDOWN:
                starttrav = True
            if event.type == pygame.MOUSEBUTTONUP:
                starttrav = False
        
        # the code to drop the obstacles and the values to filled as 1
        if starttrav and not drop:
            
            if pygame.mouse.get_pressed:
                poso = pygame.mouse.get_pos()
                if (poso[0]//20,poso[1]//20) not in obstacle and (poso[0]//20,poso[1]//20) not in s_sel:
                    obstacle.append((poso[0]//20,poso[1]//20))
                    dict_plot[(poso[0]//20,poso[1]//20)] = 1

#   after the space bar pressed the traersing of the cell occurs and this is the code for it 
    if getpath:
        

        if not itsstart:
            a = min(f_dict.values())
            for i in f_dict.keys():
                if f_dict[i] == a:
                    openlist.append(i)

            for b in openlist:
                if b == s_sel[1]:
                    getpath = False
                    start_path(b)
                else:
                    f_dict.pop(b)
                    closedlist.append(b)
                    for i in neighbours:
                        new = (b[0]+i[0],b[1]+i[1])
                        if new not in obstacle and new[0]<50 and new[0] >=0 and new[1]<35 and new[1]>=0:
                            obtained = traverse(new,b)
                            if new not in f_dict_copy.keys():
                                f_dict[new] = obtained[0]
                                f_dict_copy[new] = obtained[0]
                                last_dict[new] = b
                                g_dict[new] = obtained[1]       
                            else:
                                if f_dict_copy[new]> obtained[0]:
                                    f_dict[new] = obtained[0]
                                    f_dict_copy[new]
                                    last_dict[new] = b
                                    g_dict[new] = obtained[1]     
                        else:
                            pass  
            openlist=[]
        if itsstart :
            point = s_sel[0]
            traverse(point)
            itsstart=False


    if make=='notstart':
        createplot()
        make = 'start'
    # the diagram to create the cells in window 
    for point in dict_plot.keys():
        pygame.draw.rect(plot,(150,150,150),pygame.Rect(point[0]*20,point[1]*20,20,20),2)
    # code to draw the obstacles 
    for obs in obstacle:
        pygame.draw.rect(plot,(150,150,150),pygame.Rect(obs[0]*20,obs[1]*20,20,20))
    # code to color the cells that are traversed 
    for points in closedlist:
        pygame.draw.rect(plot,(0,150,150),pygame.Rect(points[0]*20,points[1]*20,20,20))
    # code to color the cells that are final 
    for i in final:
        pygame.draw.rect(plot,(250,150,0),pygame.Rect(i[0]*20,i[1]*20,20,20))
    try :
        pygame.draw.rect(plot,(225,0,0),pygame.Rect((s_sel[0][0])*20,(s_sel[0][1])*20,20,20))
        pygame.draw.rect(plot,(0,225,0),pygame.Rect((s_sel[1][0])*20,(s_sel[1][1])*20,20,20))
    except Exception:
        pass
    pygame.display.update()
