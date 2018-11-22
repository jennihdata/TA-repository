from pygame import *
from time import sleep
import sys

init()
mixer.init(44100, -16, 2, 4096)
window = display.set_mode((750, 400))
clock = time.Clock()
black = (0, 0, 0)
lightgrey = (234, 234, 234)
white = (255, 255, 255)
lightred=(204,0,0)
Font = font.SysFont("arial", 20)

class Button:
    def __init__(self, id, num, shift, file, key1):
        self.id = id
        self.num = int(num)
        self.shift = int(shift)
        self.file = file
        self.key1 = key1

    def draw(self):
        #Call this function to draw white and black keys as a button
        if self.shift == 0:  # draw white keys as Button
            draw.rect(window, white, Rect((self.num - 1) * 50, 1, 49, 298),
                      0)  # rect(Surface, color, Rect(left, top, width, height), width=0)
        elif self.shift == 1:  # draw black keys as Button
            draw.rect(window, black, Rect((self.num - 1) * 50 + 37, 1, 25, 150), 0)

    def play(self, piano):
        #Call this function to play the sound and prints id that is pressed
        #Channel is created for controlling playback
        mixer.Channel(piano.channel).play(mixer.Sound(self.file))
        print(self.id)
        # If piano is recoding, open the file record.txt and write the id
        if piano.record:
            piano.recordfile.write(str(self.id))
            piano.lastkey = str(self.id)
        #draw the pressed effect
        if self.shift == 0:
            draw.rect(window, lightgrey, Rect((self.num - 1) * 50, 1, 49, 298), 0)
        elif self.shift == 1:
            draw.rect(window, lightgrey, Rect((self.num -1 ) * 50 + 37, 1, 25, 150), 0)
        display.flip()
        piano.channel = piano.channel + 1
        # max number of channel is 8, if it's 8 restart from 0
        if piano.channel == 8:
            piano.channel= 0

class Piano:
    def __init__(self):
        self.channel = 0
        self.keys = []
        self.recordbutton = Recordbutton()
        self.playbutton = Playbutton()
        self.quitbutton = Quitbutton()
        self.record = False
        self.lastkey = " "
        self.speed = 0.3
        self.recordfile = open("record.txt","w")

        file = open("list.dat")
        for line in file:
            col = line.split()
            if len(col) == 5: #so that index wont be out of range
                self.keys.append(Button(col[0], col[1], col[2], col[3], col[4]))

    def draw(self):
        #call this function to call the whole piano
        window.fill(black)
        self.recordbutton.draw()
        self.playbutton.draw()
        self.quitbutton.draw()

        for key in self.keys:
            if key.shift == 0:
                key.draw()
        for key in self.keys:
            if key.shift == 1:
                key.draw()

    def recording(self):
        # if silent then print " "
        if self.record:
            silent = True
            for i in range(8):
                # check if chanel is active, if active return (1) true, else: false
                if mixer.Channel(i).get_busy() == True:
                    silent = False
            if silent:
                self.recordfile.write(" ")
                self.lastkey = " "


class Recordbutton:
    def __init__(self):
        self.x = 100
        self.y = 330
        self.h = 40
        self.w = 150

    def draw(self):
        #call this function to draw the record button
        #if mouse position is inside the button lightred, else white

        if mouse.get_pos()[0] > self.x and mouse.get_pos()[0] < self.x + self.w and mouse.get_pos()[1] > self.y and \
                mouse.get_pos()[1] < self.y + self.h:
            draw.rect(window, lightred, Rect(self.x, self.y, self.w, self.h), 2)
        else:
            draw.rect(window, white, Rect(self.x, self.y, self.w, self.h), 2)
        text = Font.render("        Record", True, white)
        window.blit(text, (self.x + 5, self.y + 6))

    def click(self):
        if mouse.get_pressed()[0]:
            if mouse.get_pos()[0] > self.x and mouse.get_pos()[0] < self.x + self.w and mouse.get_pos()[1] > self.y and mouse.get_pos()[1] < self.y + self.h:
                return True

    def event(self, piano):
        if self.click() and piano.record:
            piano.record = not piano.record
            piano.recordfile.close()
            print("Recording Stop!")
        # elif not self.click() and piano.record:
        #     piano.record = piano.record
        elif self.click() and not piano.record:
            piano.recordfile = open("record.txt", 'w')
            piano.record = not piano.record
            print("Recording Start!")

class Playbutton:
    def __init__(self):
        self.x = 500
        self.y = 330
        self.h = 40
        self.w = 150
        self.playing = False
        self.num = 0
        self.line = " "

    def draw(self):
        if mouse.get_pos()[0] > self.x and mouse.get_pos()[0] < self.x + self.w and mouse.get_pos()[1] > self.y and mouse.get_pos()[1] < self.y + self.h:
            draw.rect(window, lightred, Rect(self.x, self.y, self.w, self.h), 2)
        else:
            draw.rect(window, white, Rect(self.x, self.y, self.w, self.h), 2)
        text = Font.render("      Play", True, white)
        window.blit(text, (self.x + 5, self.y + 6))

    def click(self):
        if mouse.get_pressed()[0]:
            if mouse.get_pos()[0] > self.x and mouse.get_pos()[0] < self.x + self.w and mouse.get_pos()[1] > self.y and mouse.get_pos()[1] < self.y + self.h:
                return True

    def event(self, piano):
        #open the recordfile and read the file so that it can be played
        if self.click() and not self.playing:
            self.file = open("record.txt")
            self.num = 0
            #to eliminate the left side white spaces in the line
            self.line = self.file.readline().lstrip()
            print("Your Song = ",self.line)
            #take the id one bye one from the line
            c = self.line[self.num]
            for k in piano.keys:
                if c == str(k.id):
                    k.play(piano)
                    sleep(piano.speed)
                elif c == " ":
                    sleep(piano.speed)
                    break
            self.num += 1
            self.playing = True

        elif self.click() and self.playing:
            self.playing = False
        #if piano already click and playimg
        elif not self.click() and self.playing:
            if self.num < len(self.line):
                c = self.line[self.num]
                for k in piano.keys:
                    if c == str(k.id):
                        k.play(piano)
                        sleep(piano.speed)
                    elif c == " ":
                        sleep(piano.speed)
                        break
                self.num = self.num + 1
            #reset it so that we can play it again
            else:
                self.num = 0
                self.line = self.file.readline().lstrip()
        #adds whitespace every word so there is some delay
        elif self.line == "":
            self.playing = False
            self.line = " "

class Startbutton():
    def __init__(self):
        self.color = white
        self.x = 250
        self.y = 150
        self.width = 250
        self.height = 100
        self.text = "START"

    def draw(self, window, outline = None):
        # Call this method to draw the button on the screen
        if outline:
            draw.rect(window, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        draw.rect(window, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            # Font = font.SysFont('comicsans', 60)
            text = Font.render(self.text, 1, (0, 0, 0))
            window.blit(text, (
            self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def click(self):
        if pos[0] > self.x and pos [0] < self.x +self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
               return True
        return False

class Quitbutton:
    def __init__(self):
        self.x = 300
        self.y = 330
        self.h = 40
        self.w = 150

    def draw(self):
        if mouse.get_pos()[0] > self.x and mouse.get_pos()[0] < self.x + self.w and mouse.get_pos()[1] > self.y and \
                mouse.get_pos()[1] < self.y + self.h:
            draw.rect(window, lightred, Rect(self.x, self.y, self.w, self.h), 2)
        else:
            draw.rect(window, white, Rect(self.x, self.y, self.w, self.h), 2)
        text = Font.render("        Quit", True, white)
        window.blit(text, (self.x + 5, self.y + 6))

    def click(self):
        if mouse.get_pressed()[0]:
            if mouse.get_pos()[0] > self.x and mouse.get_pos()[0] < self.x + self.w and mouse.get_pos()[1] > self.y and mouse.get_pos()[1] < self.y + self.h:
                return True

    def event(self,piano):
        if self.click():
            sys.exit()



def main():
    piano = Piano()
    end = False
    while not end:
        piano.draw()
        for z in event.get():
            if z.type == QUIT:
                end = True

            if z.type == KEYDOWN:
                #piano speed is increased it means slower playing speed
                if z.key == K_DOWN:
                    piano.speed = piano.speed + 0.1

                #piano speed is decreased it means faster playing speed
                if z.key == K_UP:
                    piano.speed = piano.speed - 0.1
                    if piano.speed <= 0.1:
                        piano.speed = 0.1

            for k in piano.keys:
                if z.type == KEYDOWN:
                    if z.key == int(k.key1) and key.get_mods() & KMOD_SHIFT and k.shift == 1:
                        k.play(piano)
                    if z.key == int(k.key1) and not key.get_mods() & KMOD_SHIFT and k.shift == 0:
                        k.play(piano)
        piano.recording()
        piano.playbutton.event(piano)
        piano.recordbutton.event(piano)
        piano.quitbutton.event(piano)
        display.flip()
        clock.tick(7.5)

def drawwindow():
    window.fill(white)
    startbutton.draw(window,(black))
    myfont = font.SysFont("comicsans", 70)
    textsurface = myfont.render("PIANO SIMULATOR",False,(0,0,0))
    window.blit(textsurface,(150,80))

run = True
startbutton = Startbutton()
while run:
    drawwindow()
    display.update()

    for events in event.get():
        pos = mouse.get_pos()

        if events.type == MOUSEBUTTONDOWN:
                main()

        if events.type == MOUSEMOTION:
            if startbutton.click():
                startbutton.color = (255,0,0)
            else:
                startbutton.color = (0,255,0)
