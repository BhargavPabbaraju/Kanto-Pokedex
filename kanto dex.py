import pygame as pg

colors={
'maroon':[(220,10,45),(137,6,28)],
'blue':[(40,170,253),(25,106,158),(161,218,254)],
'yellow':[(253,223,24),(159,139,15),(255,242,158)],
'white':[(222,222,222),(163,164,164)],
'red':[(255,0,41),(157,0,27),(255,141,159)],
'green':[(79,174,93),(52,112,61),(178,219,184),(81,174,95)],
'black':[(35,35,35),(0,49,43)],

}

SIZE = 64

box_sizes = [[6,8],[5,6]]

WIDTH = (box_sizes[0][0]+box_sizes[1][0])*SIZE
HEIGHT = box_sizes[0][1]*SIZE
pg.init()
window = pg.display.set_mode((WIDTH,HEIGHT),pg.SRCALPHA)





def draw_circle(radius,color,width=0,draw_top_right=True,draw_top_left=True,
                draw_bottom_left=True,draw_bottom_right=True):
    surf = pg.Surface((radius*2,radius*2),pg.SRCALPHA)
    pg.draw.circle(surf,color,(radius,radius),radius,width=width,draw_top_right=draw_top_right,draw_top_left=draw_top_left,
                   draw_bottom_left=draw_bottom_left,draw_bottom_right=draw_bottom_right)
    return surf



class LeftInterior:
    def __init__(self,window,x,y):
        self.window = window
        self.x = x
        self.y = y


    def black_plus(self):
        #black plus shadow
        #bottom rectangle
        x = self.x+SIZE*5-16
        y = self.y+SIZE*6+32+16+6
        pg.draw.rect(self.window,colors['black'][0],[x,y,32+4,32+8+8],border_bottom_left_radius=8,border_bottom_right_radius=8)
        pg.draw.rect(self.window,(0,0,0),[x,y,32+4,32+8+8],width=2,border_bottom_left_radius=8,border_bottom_right_radius=8)

        #left rectangle
        x = self.x+SIZE*5-32-16
        y = self.y+SIZE*6+32
        pg.draw.rect(self.window,colors['black'][0],[x,y,32+8,32+4+8],border_top_left_radius=8,border_bottom_left_radius=8)
        pg.draw.rect(self.window,(0,0,0),[x,y,32+8,32+4+8],width=2,border_top_left_radius=8,border_bottom_left_radius=8)

        #right rectangle
        x = self.x+SIZE*5+16-4
        y = self.y+SIZE*6+32
        pg.draw.rect(self.window,colors['black'][0],[x,y,32+8,32+4+8],border_top_right_radius=8,border_bottom_right_radius=8)
        pg.draw.rect(self.window,(0,0,0),[x,y,32+8,32+4+8],width=2,border_top_right_radius=8,border_bottom_right_radius=8)

        #top rectangle
        x = self.x+SIZE*5-16
        y = self.y+SIZE*6+4
        pg.draw.rect(self.window,colors['black'][0],[x,y,32+4+4,32+4],border_top_left_radius=8,border_top_right_radius=8)
        pg.draw.rect(self.window,(0,0,0),[x,y,32+4+4,32+4],width=2,border_top_left_radius=8,border_top_right_radius=8)

        #the black plus
        

        #bottom rectangle
        x = self.x+SIZE*5-16
        y = self.y+SIZE*6+32+16+6
        pg.draw.rect(self.window,colors['black'][1],[x,y,32+4,32+8],border_bottom_left_radius=8,border_bottom_right_radius=8)
        pg.draw.rect(self.window,(0,0,0),[x,y,32+4,32+8],width=2,border_bottom_left_radius=8,border_bottom_right_radius=8)

        #left rectangle
        x = self.x+SIZE*5-32-16
        y = self.y+SIZE*6+32
        pg.draw.rect(self.window,colors['black'][1],[x,y,32+8,32+4],border_top_left_radius=8,border_bottom_left_radius=8)
        pg.draw.rect(self.window,(0,0,0),[x,y,32+8,32+4],width=2,border_top_left_radius=8,border_bottom_left_radius=8)

        #right rectangle
        x = self.x+SIZE*5+16-4
        y = self.y+SIZE*6+32
        pg.draw.rect(self.window,colors['black'][1],[x,y,32+8,32+4],border_top_right_radius=8,border_bottom_right_radius=8)
        pg.draw.rect(self.window,(0,0,0),[x,y,32+8,32+4],width=2,border_top_right_radius=8,border_bottom_right_radius=8)

        #top rectangle
        x = self.x+SIZE*5-16
        y = self.y+SIZE*6+4
        pg.draw.rect(self.window,colors['black'][1],[x,y,32+4,32+8],border_top_left_radius=8,border_top_right_radius=8)
        pg.draw.rect(self.window,(0,0,0),[x,y,32+4,32+8],width=2,border_top_left_radius=8,border_top_right_radius=8)
        
        #circle
        x = self.x+SIZE*5
        y = self.y+SIZE*6+32+16
        circle = draw_circle(16+8,colors['black'][1])
        window.blit(circle,circle.get_rect(center=(x,y)))


        #elipse in the plus
        w=12
        h = 16
        x = self.x+SIZE*5-w//2
        y = self.y+SIZE*6+32+16 - h//2
        pg.draw.ellipse(self.window,(0,0,0),[x,y,w,h],width=2)



    def black_buttons(self):
        #left circle
        x = self.x+SIZE
        y = self.y+SIZE*6+16

        circle = draw_circle(16+8,colors['black'][1])
        window.blit(circle,circle.get_rect(center=(x,y)))
        circle = draw_circle(16+8,(0,0,0),width=2)
        window.blit(circle,circle.get_rect(center=(x,y)))


        self.black_plus()
        
    def misc_buttons(self):
        #capsule buttons
        x = self.x+SIZE+32+16
        y = self.y+SIZE*6-8
        
        pg.draw.rect(self.window,colors['red'][0],[x,y,SIZE-16,8],border_radius=16)
        pg.draw.rect(self.window,(0,0,0),[x,y,SIZE-16,8],width=2,border_radius=16)

        pg.draw.rect(self.window,colors['blue'][1],[x+SIZE+16,y,SIZE-16,8],border_radius=16)
        pg.draw.rect(self.window,(0,0,0),[x+SIZE+16,y,SIZE-16,8],width=2,border_radius=16)

        #green display
        pg.draw.rect(self.window,colors['green'][3],[x,y+32,SIZE*2,SIZE+4],border_radius=8)
        pg.draw.rect(self.window,(0,0,0),[x,y+32,SIZE*2,SIZE+4],width=2,border_radius=8)

    
    def display(self):
        #black display
        pg.draw.rect(self.window,colors['black'][0],[self.x+SIZE+16,self.y+SIZE*3,SIZE*3+32,SIZE*2],border_radius=8)
        pg.draw.rect(self.window,(0,0,0),[self.x+SIZE+16,self.y+SIZE*3,SIZE*3+32,SIZE*2],width=2,border_radius=8)

        #top red circles
        x = self.x+SIZE*2+32+8
        y = self.y+SIZE*3-16
        gap = 32+16
        for i in range(2):
            circle = draw_circle(7,colors['red'][0])
            window.blit(circle,circle.get_rect(center=(x+i*gap,y)))

            circle = draw_circle(7,(0,0,0),width=2)
            window.blit(circle,circle.get_rect(center=(x+i*gap,y)))

        #bottom red circle
        x = self.x+SIZE+32+16
        y = self.y+SIZE*3+SIZE*2+16-2
        circle = draw_circle(10,colors['red'][0])
        window.blit(circle,circle.get_rect(center=(x,y)))
        circle = draw_circle(10,(0,0,0),width=2)
        window.blit(circle,circle.get_rect(center=(x,y)))

        #vertical bars
        x=self.x+SIZE+16+SIZE*3
        y=self.y+SIZE*3+SIZE*2+4+1
        gap = 6
        for i in range(4):
            pg.draw.rect(self.window,colors['black'][1],[x,y+i*gap,32,2],border_radius=16)


    
    def display_exterior(self):

        #shadow connection to wedge on right
        pg.draw.rect(self.window,colors['white'][1],[self.x+SIZE*2-32,self.y+SIZE*4+32,SIZE*3+32+16,SIZE+8],border_bottom_right_radius=8)
        pg.draw.rect(self.window,(0,0,0),[self.x+SIZE*2-32,self.y+SIZE*4+32,SIZE*3+32+16,SIZE+8],width=2,border_bottom_right_radius=8)


        #rectangle to cover shadow 
        pg.draw.rect(self.window,colors['white'][1],[self.x+SIZE-16,self.y+SIZE*4+32*2,32,8])
        pg.draw.line(self.window,(0,0,0),(self.x+SIZE-16,self.y+SIZE*4+32*2),(self.x+SIZE-16,self.y+SIZE*4+32*2+8),width=2)
        pg.draw.line(self.window,colors['white'][1],(self.x+SIZE*2-32,self.y+SIZE*5+32+6),(self.x+SIZE*2-32,self.y+SIZE*5+32-6),width=2)

        #shadow wedge
        pg.draw.polygon(self.window,colors['white'][1],[(self.x+SIZE-16,self.y+SIZE*4+32*2+8),(self.x+SIZE*2-32,self.y+SIZE*5+32-1+8),(self.x+SIZE*2-32,self.y+SIZE*4+32*2)])
        pg.draw.line(self.window,(0,0,0),(self.x+SIZE-16,self.y+SIZE*4+32*2+8),(self.x+SIZE*2-32,self.y+SIZE*5+32-1+8),width=2)
       

        #big white bg
        pg.draw.rect(self.window,colors['white'][0],[self.x+SIZE-16,self.y+SIZE*2+32,SIZE*4+32,SIZE*2+32],border_top_left_radius=8,border_top_right_radius=8)
        pg.draw.rect(self.window,(0,0,0),[self.x+SIZE-16,self.y+SIZE*2+32,SIZE*4+32,SIZE*2+32],width=2,border_top_left_radius=8,border_top_right_radius=8)

        #connection to wedge on right
        pg.draw.rect(self.window,colors['white'][0],[self.x+SIZE*2-32,self.y+SIZE*4+32,SIZE*3+32+16,SIZE],border_bottom_right_radius=8)
        pg.draw.rect(self.window,(0,0,0),[self.x+SIZE*2-32,self.y+SIZE*4+32,SIZE*3+32+16,SIZE],width=2,border_bottom_right_radius=8)

        #wedge
        pg.draw.polygon(self.window,colors['white'][0],[(self.x+SIZE-16,self.y+SIZE*4+32*2),(self.x+SIZE*2-32,self.y+SIZE*5+32-1),(self.x+SIZE*2-32,self.y+SIZE*4+32*2)])
        pg.draw.line(self.window,(0,0,0),(self.x+SIZE-16,self.y+SIZE*4+32*2),(self.x+SIZE*2-32,self.y+SIZE*5+32-1),width=2)


        #rectangles to cover up the outlines
        pg.draw.rect(self.window,colors['white'][0],[self.x+SIZE*2-32-2,self.y+SIZE*4+32,SIZE*3+32+16,16])
        pg.draw.rect(self.window,colors['white'][0],[self.x+SIZE-16+2,self.y+SIZE*4+32+16,32*2,16])
        pg.draw.rect(self.window,colors['white'][0],[self.x+SIZE*2-32,self.y+SIZE*5,32*2,30])


    def draw(self):
        self.display_exterior()

        self.display()

        self.misc_buttons()

        self.black_buttons()

class LeftSide:
    def __init__(self,window,x,y,size=box_sizes[0]):
        self.window = window
        self.x = x
        self.y = y
        self.size = size

    def background(self,color=colors['maroon'][0]):
        pg.draw.rect(self.window,color,[self.x,self.y,self.size[0]*SIZE,self.size[1]*SIZE],border_radius=16)
        

        #Outline
        pg.draw.rect(self.window,(0,0,0),[self.x,self.y,self.size[0]*SIZE,self.size[1]*SIZE],width=2,border_radius=16)
        

    def top_lines(self,line_gap=2):
        x_width = self.x+SIZE*self.size[0]
        lines_points = [(self.x,self.y+SIZE*line_gap),(self.x+SIZE*(self.size[0]//2),self.y+SIZE*line_gap),
                        (x_width-SIZE*line_gap,self.y+SIZE*(line_gap-1)),(x_width,self.y+SIZE*(line_gap-1))]
        pg.draw.lines(window,(0,0,0),False,lines_points,width=2)

    def big_circle(self):
        #Black outline 1
        circle = draw_circle(SIZE//2+16+2,(0,0,0),width=2)
        window.blit(circle,circle.get_rect(center=(self.x+SIZE,self.y+SIZE)))
        #White background circle
        circle = draw_circle(SIZE//2+16,colors['white'][0])
        window.blit(circle,circle.get_rect(center=(self.x+SIZE,self.y+SIZE)))
        #Big Blue circle
        circle = draw_circle(SIZE//2+8,colors['blue'][0])
        window.blit(circle,circle.get_rect(center=(self.x+SIZE,self.y+SIZE)))
        
        #Shadow circle
        circle = draw_circle(SIZE//2+2,colors['blue'][1])
        window.blit(circle,circle.get_rect(center=(self.x+SIZE+6,self.y+SIZE+6)))
        #Black outline 2
        circle = draw_circle(SIZE//2+8+2,(0,0,0),width=2)
        window.blit(circle,circle.get_rect(center=(self.x+SIZE,self.y+SIZE)))

        #Highlight circle 1
        circle = draw_circle(16+2,colors['blue'][0])
        window.blit(circle,circle.get_rect(center=(self.x+SIZE-6,self.y+SIZE-6)))

        #Highlight circle 2
        circle = draw_circle(8,colors['blue'][2])
        window.blit(circle,circle.get_rect(center=(self.x+SIZE-12,self.y+SIZE-12)))
        

    def top_circles(self):
        gap = 32+16
        for i in range(3):
            color = ['red','yellow','green'][i]
            #Main circle
            circle = draw_circle(10,colors[color][0])
            window.blit(circle,circle.get_rect(center=(self.x+SIZE*2+32+i*gap,self.y+32)))
            #Shade circle
            circle = draw_circle(8,colors[color][1])
            window.blit(circle,circle.get_rect(center=(self.x+SIZE*2+32+2+i*gap,self.y+32+2)))
            #Highlight circle 1
            circle = draw_circle(6,colors[color][0])
            window.blit(circle,circle.get_rect(center=(self.x+SIZE*2+30+i*gap,self.y+30)))
            #Highlight circle 2
            circle = draw_circle(4,colors[color][2])
            window.blit(circle,circle.get_rect(center=(self.x+SIZE*2+28+i*gap,self.y+28)))
            #Black outline
            circle = draw_circle(12,(0,0,0),width=2)
            window.blit(circle,circle.get_rect(center=(self.x+SIZE*2+32+i*gap,self.y+32)))


    def draw(self):
        self.background()

        self.top_lines()

        self.big_circle()

        self.top_circles()
    

class RightSide:
    def __init__(self,window,x,y,size=box_sizes[1]):
        self.window = window
        self.x = x
        self.y = y
        self.size = size

    def background(self,color=colors['maroon'][0]):
        #shadow
        pg.draw.rect(self.window,colors['maroon'][1],[self.x-1,self.y,self.size[0]*SIZE,self.size[1]*SIZE+8],border_radius=16,border_bottom_left_radius=0,border_top_left_radius=0)
        #shadow background
        pg.draw.rect(self.window,(0,0,0),[self.x-1,self.y,self.size[0]*SIZE,self.size[1]*SIZE+8],width=2,border_radius=16,border_bottom_left_radius=0,border_top_left_radius=0)

        #main background
        pg.draw.rect(self.window,color,[self.x,self.y,self.size[0]*SIZE,self.size[1]*SIZE],border_radius=16,border_bottom_left_radius=0,border_top_left_radius=0)
        #Outline
        pg.draw.rect(self.window,(0,0,0),[self.x,self.y,self.size[0]*SIZE,self.size[1]*SIZE],width=2,border_radius=16,border_bottom_left_radius=0,border_top_left_radius=0)

        

        

    def top_lines(self):
        

        line_gap = 32+16
        x_width = self.x+SIZE*self.size[0]
        lines_points = [(self.x,self.y-line_gap),(self.x+SIZE*(self.size[0]//2),self.y-line_gap),
                        (self.x+SIZE*(self.size[0]//2)+32,self.y),(self.x+SIZE*(self.size[0]//2)+32,self.y+32),(self.x,self.y+SIZE*self.size[1]-2)]
        
        #Draw a polygon to Fill the gap formed by line
        pg.draw.polygon(window,colors['maroon'][0],lines_points)

        lines_points = [(self.x,self.y-line_gap),(self.x+SIZE*(self.size[0]//2),self.y-line_gap),
                        (self.x+SIZE*(self.size[0]//2)+32,self.y),(self.x+SIZE*(self.size[0])-32,self.y)]
        pg.draw.lines(window,(0,0,0),False,lines_points,width=2)

        
    def blue_grid(self):
        w = self.size[0]*SIZE-SIZE//2
        pg.draw.rect(self.window,colors['blue'][0],[self.x+16,self.y+SIZE*2+32,w,SIZE+8])
        #shadow
        pg.draw.rect(self.window,colors['blue'][1],[self.x+16,self.y+SIZE*2+32+SIZE,w,6])
        #grid outline
        pg.draw.rect(self.window,(0,0,0),[self.x+16,self.y+SIZE*2+32,w,SIZE+8],width=2)
        #horizontal grid line
        pg.draw.line(window,(0,0,0),(self.x+16,self.y+SIZE*2+32+SIZE//2+4),(self.x+16+w-2,self.y+SIZE*2+32+SIZE//2+4),width=2)

        #vertical grid lines
        no = 5
        for i in range(no):
            pg.draw.line(window,(0,0,0),(self.x+16+i*(w//no+1),self.y+SIZE*2+32),(self.x+16+i*(w//no+1),self.y+SIZE*2+32+SIZE+6),width=2)


    def misc_buttons(self):
        w=self.size[0]*SIZE-SIZE//2
        x=self.x+16+3*(w//5+1)
        y=self.y+SIZE*3+32+16

        #right side black oval buttons
        for i in range(2):
            pg.draw.rect(self.window,colors['black'][0],[x+i*SIZE,y,SIZE-12,12],border_radius=16)
            pg.draw.rect(self.window,(0,0,0),[x+i*SIZE,y,SIZE-12,12],width=2,border_radius=16)
        

        #left side square white buttons
        x=self.x+16+0*(w//5+1)
        y=self.y+SIZE*4+16
        for i in range(2):
            bl,tl,tr,br = 4,4,4,4
            if i==1:
                bl= 0
                tl =0
            else:
                tr=0
                br=0
            pg.draw.rect(self.window,colors['white'][0],[x+i*(32+12-2),y,32+12,32+8],border_radius=4,border_bottom_left_radius=bl,border_bottom_right_radius=br,border_top_left_radius=tl,border_top_right_radius=tr)
            pg.draw.rect(self.window,colors['white'][1],[x+i*(32+12-2),y+32+2,32+12,4],border_radius=4,border_bottom_left_radius=bl,border_bottom_right_radius=br,border_top_left_radius=tl,border_top_right_radius=tr)
            pg.draw.rect(self.window,(0,0,0),[x+i*(32+12-2),y,32+12,32+8],width=2,border_radius=4,border_bottom_left_radius=bl,border_bottom_right_radius=br,border_top_left_radius=tl,border_top_right_radius=tr)


        x = self.x+32+4+4*(w//5+1)
        y = self.y+SIZE*4+32+16
        #right side yellow circle
        color='yellow'
        #Main circle
        circle = draw_circle(16,colors[color][0])
        window.blit(circle,circle.get_rect(center=(x,y)))
        #Shade circle
        circle = draw_circle(12,colors[color][1])
        window.blit(circle,circle.get_rect(center=(x+2,y+2)))
        #Highlight circle 1
        circle = draw_circle(8,colors[color][0])
        window.blit(circle,circle.get_rect(center=(x-2,y-2)))
        #Highlight circle 2
        circle = draw_circle(4,colors[color][2])
        window.blit(circle,circle.get_rect(center=(x-4,y-4)))
        #Black outline
        circle = draw_circle(16,(0,0,0),width=2)
        window.blit(circle,circle.get_rect(center=(x,y)))

    
    def type_display(self):
        w=self.size[0]*SIZE-SIZE//2
        x=self.x+16+0*(w//5+1)+8
        y=self.y+SIZE*5+16-2
        
        gap = SIZE*2+16
        for i in range(2):
            pg.draw.rect(self.window,colors['black'][0],[x+i*gap,y,SIZE+32+16,32+4],border_radius=4)
            pg.draw.rect(self.window,(0,0,0),[x+i*gap,y,SIZE+32+16,32+4],width=2,border_radius=4)



    def draw(self):
        self.background()

        self.top_lines()

        #Display screen
        pg.draw.rect(self.window,colors['black'][0],[self.x+16,self.y+SIZE,self.size[0]*SIZE-SIZE//2,SIZE+16],border_radius=4)
        #outline
        pg.draw.rect(self.window,(0,0,0),[self.x+16,self.y+SIZE,self.size[0]*SIZE-SIZE//2,SIZE+16],width=2,border_radius=4)
        
        self.blue_grid()

        self.misc_buttons()
        
        self.type_display()
    


def draw():
    window.fill(-1)
    X=0
    Y=0

    #Left Side Box
    ls = LeftSide(window,X,Y)
    ls.draw()

    li = LeftInterior(window,X,Y)
    li.draw()
    

    #Right Side Box
    rs = RightSide(window,X+SIZE*ls.size[0],Y+SIZE*(ls.size[1]-box_sizes[1][1])-16)
    rs.draw()
    

    
def loop():
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.image.save(window,'image.png')
                pg.quit()
                return


        draw()
        pg.display.flip()


loop()
    
