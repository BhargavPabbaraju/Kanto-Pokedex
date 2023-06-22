import pygame as pg

colors={
'maroon':[(220,10,45),(137,6,28)],
'blue':[(40,170,253),(25,106,158),(161,218,254)],
'yellow':[(253,223,24),(159,139,15),(255,242,158)],
'white':[(222,222,222),(163,164,164)],
'red':[(255,0,41),(157,0,27),(255,141,159)],
'green':[(79,174,93),(52,112,61),(178,219,184)],
'black':[(35,35,35),(0,49,43)],

}

WIDTH = 1000
HEIGHT = 800
pg.init()
window = pg.display.set_mode((WIDTH,HEIGHT))

SIZE = 64

box_sizes = [[6,8],[5,6]]



def draw_circle(radius,color,width=0,draw_top_right=True,draw_top_left=True,
                draw_bottom_left=True,draw_bottom_right=True):
    surf = pg.Surface((radius*2,radius*2),pg.SRCALPHA)
    pg.draw.circle(surf,color,(radius,radius),radius,width=width,draw_top_right=draw_top_right,draw_top_left=draw_top_left,
                   draw_bottom_left=draw_bottom_left,draw_bottom_right=draw_bottom_right)
    return surf


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
        for i in range(2):
            pg.draw.rect(self.window,colors['black'][0],[x+i*SIZE,y,SIZE-12,12],border_radius=16)
            pg.draw.rect(self.window,(0,0,0),[x+i*SIZE,y,SIZE-12,12],width=2,border_radius=16)
        
        x=self.x+16+0*(w//5+1)
        y=self.y+SIZE*3+32+16
        for i in range(2):
            pg.draw.rect(self.window,colors['black'][0],[x+i*SIZE,y,SIZE-12,12],border_radius=16)
            pg.draw.rect(self.window,(0,0,0),[x+i*SIZE,y,SIZE-12,12],width=2,border_radius=16)

    def draw(self):
        self.background()

        self.top_lines()

        #Display screen
        pg.draw.rect(self.window,colors['black'][0],[self.x+16,self.y+SIZE,self.size[0]*SIZE-SIZE//2,SIZE+16],border_radius=4)
        #outline
        pg.draw.rect(self.window,(0,0,0),[self.x+16,self.y+SIZE,self.size[0]*SIZE-SIZE//2,SIZE+16],width=2,border_radius=4)
        
        self.blue_grid()

        self.misc_buttons()
        
    


def draw():
    window.fill(-1)
    X=100
    Y=100

    #Left Side Box
    ls = LeftSide(window,X,Y)
    ls.draw()
    

    #Right Side Box
    rs = RightSide(window,X+SIZE*ls.size[0],Y+SIZE*(ls.size[1]-box_sizes[1][1])-16)
    rs.draw()
    

    
def loop():
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return


        draw()
        pg.display.flip()


loop()
    
