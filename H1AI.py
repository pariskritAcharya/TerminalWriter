from manim import *

class H1(MovingCameraScene):
    Container = VGroup()

    def textConstructor(self, text, color=WHITE, font_size=20, font_name="Consolas"):
        return Text(text, font=font_name, font_size=font_size, color=color)

    def getText(self, text, initial=False, colors=WHITE, moveAmount=0.6, index=-1):
        if len(self.Container) > 0 and self.Container[-1].get_bottom()[1] < -0.5:
            self.play(self.Container.animate.shift(UP * moveAmount), run_time=0.15)

        if initial:
            prompt_text = "C:\\Users\\Luan\\Downloads>"
            initial_Text = self.textConstructor(prompt_text, color=colors)
            if len(self.Container) == 0:
                initial_Text.to_corner(UL, buff=0.5)
            else:
                initial_Text.next_to(self.Container[-1], DOWN, aligned_edge=LEFT, buff=0.2)
            
            line = self.textConstructor(text, color=colors)
            line.next_to(initial_Text, RIGHT, buff=0.15)
            self.play(FadeIn(initial_Text, run_time=0.4))
            self.Container.add(initial_Text)
            self.Container.add(line)
            return line
        else:
            line = self.textConstructor(text, color=colors)
            line.next_to(self.Container.submobjects[index], DOWN, aligned_edge=LEFT, buff=0.2)
            self.Container.add(line)
            return line

    def construct(self):
        green, red, white = "#60F017", "#FF3333", "#CCCCCC"
        
        # --- PHASE 1: THE BAIT ---
        line1 = self.textConstructor("SYSTEM [Version 10.0.22621.2428]", color=white)
        line1.to_corner(UL, buff=0.5)
        self.Container.add(line1)
        self.add(line1)

        cursor = Rectangle(
            color = GREY_A,
            fill_color = GREY_A,
            fill_opacity = 1.0,
            height = line1.get_height(),
            width =  line1.get_width() * 0.015,
        ).move_to(line1[0]) # Position the cursor


        self.add(self.getText("(c) Cyber Nivio. All rights reserved.", colors=white))
        self.add(self.getText("______________________________________________________", colors=white))
        
     
        t1 =self.getText("T2TR_CRACK_INSTALLER.exe", initial=True,moveAmount=0.12)
        cursor.move_to(t1[0])
        cursor.set_opacity(1)
        self.play(Blink(cursor, blinks=1))
        self.play(TypeWithCursor(t1, cursor))
      
        cursor.set_opacity(0)   
        self.wait(0.5)
        self.add(self.getText("Bypassing security certificate...", index=-2))
        self.wait(1.2)
        self.add(self.getText("CRITICAL ERROR: REMOTE INTRUSION DETECTED.", colors=red, index=-1))
        self.wait(0.8)

        # --- PHASE 2: THE HIJACK ---
        self.play(
            self.camera.frame.animate.shift(RIGHT*0.3),
            self.Container.animate.set_color(red),
            run_time=0.1
        )
        cursor.color = white
        self.play(self.camera.frame.animate.shift(LEFT*0.6), run_time=0.05)
        self.play(self.camera.frame.animate.shift(RIGHT*0.3), run_time=0.05)
        
        self.wait(1.5) # The silence after the crash
        self.play(FadeIn(self.getText("HACKER: You still have that habit of clicking things you shouldn't.", colors=green, index=-1), run_time=0.4))
    

        t2 = self.getText("Who is this? How did you get through my proxy?", initial=True)#error
        t2.set_opacity(0)
        cursor.move_to(t2[0])
        cursor.set_opacity(1)
        self.play(Blink(cursor, blinks=1))
        t2.set_opacity(1)
        self.play(TypeWithCursor(t2, cursor))
        cursor.set_opacity(0)   

        self.play(FadeIn(self.getText("HACKER: Proxies can't hide you from the past, Luan.", colors=green, index=-2), run_time=0.4))
        self.wait(0.8)
        self.play(FadeIn(self.getText("HACKER: I've been watching you since the smoke cleared in 2022.", colors=green, index=-1), run_time=0.4))

        t3 = self.getText("The highway accident? That was 4 years ago. Who ARE you?", initial=True)

        cursor.move_to(t3[0])
        cursor.set_opacity(1)
        self.play(Blink(cursor, blinks=2))
        self.play(TypeWithCursor(t3, cursor))
        cursor.set_opacity(0)   

        self.wait(1)
        self.play(FadeIn(self.getText("HACKER: It wasn't an accident. It was a deletion.", colors=green, index=-2), run_time=0.4))
        self.wait(0.8)
        self.play(FadeIn(self.getText("HACKER: They think I'm offline. They think they're safe.", colors=green, index=-1), run_time=0.4))
        self.wait(1.5)
        
        self.add(self.getText("UPLOADING: 'PROJECT_SILENCE.pkg'...", colors=red, index=-1))
        self.wait(0.2)
        self.add(self.getText(" > UNREDACTED_AUTOPSY_01.pdf", colors=red, index=-1))
        self.add(self.getText(" > POLICE_PAYOFF_LOGS.dat", colors=red, index=-1))
        self.add(self.getText(" > THE_BRAKE_MODIFICATION_SPECS.jpg", colors=red, index=-1))
        self.wait(3) # Give viewer time to read the filenames

        self.play(FadeIn(self.getText("HACKER: I've left the backdoor open for you. Only you.", colors=green, index=-1), run_time=0.4))
        self.wait(1)
        self.play(FadeIn(self.getText("HACKER: Use the code. Find the ones who held the matches.", colors=green, index=-1), run_time=0.4))
        self.wait(2)

        t4 = self.getText("I don't understand... you sound like... wait...", initial=True)#error
        t4.set_opacity(0)
        cursor.move_to(t4[0])
        cursor.set_opacity(1)
        self.play(Blink(cursor, blinks=1))
        t4.set_opacity(1)
        self.play(TypeWithCursor(t4, cursor))
        cursor.set_opacity(0)

        self.play(FadeIn(self.getText("HACKER: Don't look for a ghost. Look for the truth.", colors=green, index=-2), run_time=0.4))
        self.wait(0.8)
        self.play(FadeIn(self.getText("HACKER: They're here. You must go. And be careful. 15943 remember!!", colors=green, index=-1), run_time=0.4))
        self.wait(1.5)

        # --- PHASE 3: THE DISCONNECT ---
        self.add(self.getText("--- SIGNAL LOST: ENCRYPTION KEY TRANSFERRED ---", colors=red, index=-1))
        self.add(self.getText("C:\\Users\\Luan\\Desktop>", colors=white, index=-1))
        self.wait(2)

        # --- OUTRO ---
        self.play(
            self.Container.animate.set_opacity(0.1).shift(UP*1.5),
            self.camera.frame.animate.scale(0.8),
            run_time=3
        )
        
        final = Text("FINISH THE MISSION", font="Consolas", color=red).scale(1.3)
        self.play(FadeIn(final))
        self.wait(3)



        



        #cursor script

        # cursor.move_to(t1)
        # cursor.set_opacity(1)
        # self.play(TypeWithCursor(t1, cursor))
        # self.play(Blink(cursor, blinks=1))
        #cursor.set_opacity(0)