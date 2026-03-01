from manim import *
from numpy import *
class H1(Scene):

    Container = VGroup()

    def textConstructor(self, text, color=WHITE, font_size=20, font_name="Consolas"):
        return Text(text, font=font_name, font_size=font_size, color=color)

    def getText(self,text,initial=False,moveGroup=True,colors=WHITE,moveAmount=0.2,index=-1):
  

        if initial:
            initial_Text = self.textConstructor("C:\\Users\\Lucas\\>",color=colors)
            initial_Text.next_to(self.Container[-1], DOWN, aligned_edge=LEFT, buff=0.15)
            

            line = self.textConstructor(text,color=colors)
            line.next_to(initial_Text, RIGHT, buff=0.15)

            if moveGroup:
                self.play(self.Container.animate.shift(UP*moveAmount), run_time=.1)

            self.add(initial_Text)
            self.Container.add(initial_Text)
            self.Container.add(line)

          

            return line
        else:
            line = self.textConstructor(text,color=colors)
            try:
                line.next_to(self.Container.submobjects[index], DOWN, aligned_edge=LEFT, buff=0.15)
            except IndexError:
                line.next_to(self.Container.submobjects[-1], DOWN, aligned_edge=LEFT, buff=0.15)
            
            if moveGroup:
                self.play(self.Container.animate.shift(UP*moveAmount), run_time=.1)
            self.Container.add(line)

        return line
    

    def scene1(self):
        #initialization of line
        line1 = self.textConstructor("SYSTEM [Version 10.0.1200.8985] ")
        line1.move_to(LEFT * 3 + UP * 2)
        self.Container.add(line1)
        self.add(line1)

        #line 2 using get text function
        line2 = self.getText("(c) Cyber Nivio. All rights reserved",moveGroup=False)
        self.add(line2)



 
        cursor = Rectangle(
            color = GREY_A,
            fill_color = GREY_A,
            fill_opacity = 1.0,
            height = line1.get_height(),
            width =  line1.get_width() * 0.015,
        ).move_to(line1[0]) # Position the cursor

        # when user types

        text1 =self.getText("T2TR_CRACK_INSTALLER.exe", initial=True,moveGroup=True,moveAmount=0.4)
        cursor.move_to(text1)
        cursor.set_opacity(1)
        self.play(TypeWithCursor(text1, cursor))
        self.play(Blink(cursor, blinks=1))
        
      

        # when system responds

        text2 =self.getText("Welcome to Manim.", initial=False,index=-2)
        cursor.set_opacity(0)

        self.add(text2)

        text3 =self.getText("Welcome to Manim.", initial=False)
        cursor.set_opacity(0)

        self.add(text3)

        #storyboard

        #user:
        text1 =self.getText("hi.exe", initial=True,moveGroup=True,moveAmount=0.4)
        cursor.move_to(text1)
        cursor.set_opacity(1)
        self.play(TypeWithCursor(text1, cursor))
        self.play(Blink(cursor, blinks=1))
        


    def construct(self):
        self.scene1()
        self.wait(1)








#  self.play(self.Container.animate.shift(UP), run_time=.1)

#         text2 =self.textConstructor("Welcome to Manim.", color=GREEN)
        
#         text2.next_to(self.Container[-1], DOWN, aligned_edge=LEFT, buff=0.15)
        
#         cursor.move_to(text2)
#         self.play(TypeWithCursor(text2, cursor))
#         self.play(Blink(cursor, blinks=2))
#         self.Container.add(text2)
      