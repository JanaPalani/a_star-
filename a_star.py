import pygame 
pygame.init()
plot = pygame.display.set_mode((1000,700))
class Node:
    def __init__(self,pos):
        self.data = pos
        self.value = None
        self.last = None
    
class Grid:
    def __init__(self):
        self.openlist = []
        self.closedlist = []
    
    
    def startnode(self,point):
        start = Node(point)

        start.value = 'start'
    
    def endnode(self,point):
        end = Node(point)
        end.value = 'end'
    
    def obstaclenode(self,point):
        obs = Node(point)
        obs.value = 1

startnod =  None
endnod = None 
run = True
obj= Grid()
while run :
    plot.fill((0,0,0))


    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            run = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if not startnod:
                startnod = Node((pos[0]//20,pos[1]//20))
                print(startnod.data)
            elif not endnod:
                endnod = Node((pos[0]//20,pos[1]//20))
                print(endnod.data)
    




    obj.drawplot() 
    for i in range(35):
        for j in range(50):
            pygame.draw.rect(plot,(150,150,150),pygame.Rect(j*20,i*20,20,20),2)
        


    pygame.display.update()






        

        


        


