from cv2 import rectangle, line, circle, ellipse, polylines
from Animator import Animator
import random
an = Animator()
class MySketch:

    def __init__(self):
        an.start_loop(self.setup, self.draw)  

    def setup(self):
        print("setup")
        #x1 = 100
        #y1 = 100
        #x2 = 200
        #y2 = 200

        #color = (244,34,134)

        #line(an.canvas,(x1,y1), (x2,y2),color,11)
        #These two bits of code are the same!

        #Arguments in place
        #rectangle(an.canvas, (0,0), (100,100), (0,0,255), -1)

        #Arguments stored in named variables first
        
        
        
        
       
    def draw(self):
        #an.background((200,34,56))
        color = (255,255,255)
        color1 = (234,22,121)
        if an.frame % 60 > 60 & an.mouse_y < an.height/2:
            color = (56,23,211)
            circle(an.canvas, (50,50), 50, color1,-1)  
        
            
        if an.mouse_x > an.width/2:

            color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            #d = random.radiant(5,9)

          
        circle(an.canvas, (an.mouse_x,an.mouse_y), int(5*random.randint(1,8)), color,-1)
        
        return

MySketch()          






