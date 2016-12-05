import pygame
from pygame.locals import *

pygame.init()
screensize=(640, 480)
screen = pygame.display.set_mode(screensize)
clock = pygame.time.Clock()
background_color=(0,100,150)

class Step1:
    def __init__(self, screensize):
        self.screensize=screensize
        # self.sentence1=sentence1
        # self.sentence2=sentence2
        self.color=(255,255,255)
        self.word_color = (255, 255, 255)
        self.sound= pygame.mixer.Sound("welcome.wav")
    def title(self,big_text):
        self.big_text=big_text
        self.font = pygame.font.Font(None,50)
        text = self.font.render(self.big_text, True, self.word_color)
        self.text_rect = text.get_rect(center=(self.screensize[0] / 2, self.screensize[1] / 2))
        screen.blit(text, self.text_rect)

    def sub_title(self,sentence):
        self.sentence=sentence
        self.font = pygame.font.Font(None, 30)
        text = self.font.render(self.sentence, True, self.word_color)
        self.text_rect = text.get_rect(center=(self.screensize[0] / 2, (self.screensize[1] / 2)+30))
        screen.blit(text, self.text_rect)

    def sentence(self,word):
        self.word=word
        self.font = pygame.font.Font(None, 30)
        text = self.font.render(self.word, True, self.word_color)
        self.text_rect = text.get_rect(center=(self.screensize[0] / 2, (self.screensize[1] / 2)))
        screen.blit(text, self.text_rect)



    # def sound(self,file):
    #     self.sound = pygame.mixer.Sound(file)
    #     self.mixer.sound.play(1)
    # def fadeout(self):
    #     self.list=[]
    #     for i in self.word_color:
    #         list.append(
    #
    #     for i in range(0,226):
    #         screen.fill(background_color)
    #         self.list[0]





#class Step2:



#animation1 = Step1(screensize,"Welcome to BLAST", "Basic Local Alignment Search Tool")
animation1=Step1(screensize)
running = True

while running:
    #fps limiting/reporting phase
    clock.tick(64)
    #event handling phase
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            running = False

        screen.fill(background_color)
        #animation1.sound("welcome.wav")
        animation1.title("Welcome to BLAST")
        animation1.sub_title("Basic Local Alignment Search Tool")
        if event.type==KEYDOWN:
            if event.key == K_SPACE:
                screen.fill(background_color)
        if event.type == KEYUP:
            screen.fill(background_color)
            animation1.sub_title("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras nisi est, interdum eu tortor id, interdum egestas lectus")
        




                #animation1.sentence("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras nisi est, interdum eu tortor id, interdum egestas lectus")








                # keys=key.get_pressed()
        # if event.key == K_SPACE:
        #     screen.fill(background_color)
        #     animation1.sub_title("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras nisi est, interdum eu tortor id, interdum egestas lectus")






    pygame.display.update()