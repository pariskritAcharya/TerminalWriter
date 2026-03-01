# Terminal Writer in manim

### FILES

* H1.py is the system logic it contains core logic behind the system
* H1AI.py is the actual use of the system but I used AI to do the job for the animation. The animation: [youtube](https://youtu.be/D-i60c0msoY?si=qRnm2jJQl4wktpqM)

### HOW DOES THIS WORK?

1. First there is a text constructer ` textConstructor(self, text, color=WHITE, font_size=20, font_name="Consolas") ` which can change color, font, and size of the text you can add more parameters depending on the use 
   This function is used when ever I need to make a Text, simply  ` Text() ` could be used but I dont want to make redundancy in my code as I am working with default fonts and all but also making sure I can change depending on my use

2. Then, there is this ` getText(self,text,initial=False,moveGroup=True,colors=WHITE,moveAmount=0.2,index=-1) ` this ` getText ` is now actually used by the user as there is many handy functions to use.
   while above function `textConstructor` just returns the ` Text ` this new function is short and full of parameters that generates terminal effect. I will explain in detail:
   Example: `text1 =self.getText("Hello World!", initial=True,moveGroup=True,moveAmount=0.4)`
   Here, Parameters:
      * `text` : string that would be printed in the screen
      * `initial` : initial refers to the initial texts like `C:\User\download>` in terminal. If its `False` it wont display it else initial is displayed already but the text is not displayed
      * `moveGroup` : every thing displayed in the screen is kept in a `VGroup` and when you need terminal to scroll up you can just turn this parameter on
      * `color` : color of the line
      * `moveAmount` : the amount by which `VGroup` scrolls if `moveGroup` is active
      * `index`: now index is the main thing. As I said everything is added to `Vgroup` and I am placing each text in respect to element in the Vgroup `-1` refers to last element placed in `VGeoup` while `-2` refers to the second last
                 Note that, `initial` and `text` are seperately placed in `VGroup`. You need to manually set index to ensure which element you are currently refering to position text with respect to
                 if index not set properly text may overwrite or, shift to the right. This could be made automatic but, this just gives flexibility to make multiline Terminal effect. Sometimes you may want to use `-3` or more depending on the use
      * To make cursor effect, you need to have this set before hand
   ```
         cursor = Rectangle(
            color = GREY_A,
            fill_color = GREY_A,
            fill_opacity = 1.0,
            height = line1.get_height(),
            width =  line1.get_width() * 0.015,
        ).move_to(line1[0]) # Position the cursor
    ```

   Then, you make a variable say `text1` set its parameters.
   Next, youset position of cursor to the first letter of the `text1` and then  use `self.play(TypeWithCursor(text1, cursor))` and text is only displayed after this not before. If you want to display text without typewriter effect you can use default text display functions.
   You may want to use `self.play(Blink(cursor, blinks=1))` to give cursor blinking effect 
   You need to set opacity on and off so that cursor is not visible when not typing.


### Note:
  1. This was just the logic behind the system. But in `H1AI.py` this same logic has be modified slightly to make it easier to use. 
  2. ```
         line1 = self.textConstructor("SYSTEM [Version 10.0.1200.8985] ")
        line1.move_to(LEFT * 3 + UP * 2)
        self.Container.add(line1)
        self.add(line1)
     ```
     This is just to set first line in some part of screen and with reference to this position all the other texts are displayed.



### Examples:
  ```
  line2 = self.getText("(c) Cyber Nivio. All rights reserved",moveGroup=False)
  self.add(line2)
  ```

  ```
  text1 =self.getText("T2TR_CRACK_INSTALLER.exe", initial=True,moveGroup=True,moveAmount=0.4)
  cursor.move_to(text1)
  cursor.set_opacity(1)
  self.play(TypeWithCursor(text1, cursor))
  self.play(Blink(cursor, blinks=1))
  ```

      







