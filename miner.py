import pygame
import random
import sys


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((900, 750))

        self.count_of_mines = 40
        
        self.field = []
        self.fill_empty_field()
        self.fill_mines()
        self.fill_other_types()

    def start(self):
        self.draw()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pos = event.pos
                        self.open_cell(pos[0]//50,
                                       pos[1]//50 - 1)
                    elif event.button == 3:
                        pos = event.pos
                        self.set_flag(pos[1]//50 - 1,
                                      pos[0]//50)
                        
                self.draw()
            pygame.display.flip()

    def set_flag(self, x, y):
        if not self.field[x][y].is_open:
            self.field[x][y].sprite = pygame.image.load('image/flag.png')
            self.field[x][y].is_open = True
            self.field[x][y].is_flag = True
        elif self.field[x][y].is_flag:
            self.field[x][y].sprite = pygame.image.load('image/closen_empty.png')
            self.field[x][y].is_flag = False
            self.field[x][y].is_open = False

            
    def open_cell(self, y, x):
        if x < 0 or y < 0 or \
           x > 13 or y > 17:
            return
        #print(self.field[x][y].type)
        for i in range(1, 9):
            if self.field[x][y].type == str(i):
                self.field[x][y].sprite = pygame.image.load(f'image/{i}.png')
                self.field[x][y].is_open = True
                self.field[x][y].is_flag = False
        if self.field[x][y].type == 'mine':
            self.field[x][y].sprite = pygame.image.load('image/lose_mine.png')
            self.field[x][y].is_open = True
            self.field[x][y].is_flag = False
        elif self.field[x][y].type == '0':
            self.field[x][y].sprite = pygame.image.load('image/empty.png')
            self.field[x][y].is_open = True
            self.field[x][y].is_flag = False
        #print(self.field[x][y].type)
            
            

    def fill_empty_field(self):
        x = 0
        y = 50
        for i in range(14):
            self.field.append([])
            for j in range(18):
                self.field[i].append(Cell(x, y))
                x += 50
            x = 0
            y += 50

    def fill_mines(self):
        for i in range(self.count_of_mines):
            while True:
                x = random.randint(0, 13)
                y = random.randint(0, 17)
                if self.field[x][y].type == None:
                    self.field[x][y].type = 'mine'
                    break

    def fill_other_types(self):
        for i in range(len(self.field)):
            for j in range(len(self.field[0])):
                if self.field[i][j].type == None:
                    self.field[i][j].type = self.get_type(i, j)
                    #print(self.field[i][j].type)

    def get_type(self, x, y):
        res = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                new_x = dx + x
                new_y = dy + y
                if new_x < 0 or new_y < 0 or \
                   new_x > 13 or new_y > 17:
                    continue
                #print(x, y, new_x, new_y)
                if self.field[new_x][new_y].type == 'mine':
                    res += 1
        return str(res)

    def draw(self):
        for i in self.field:
            for j in i:
                self.screen.blit(j.sprite, (j.x, j.y))
                                     

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = None
        self.sprite = pygame.image.load('image/closen_empty.png')
        self.width = 50
        self.height = 50
        self.is_open = False
        self.is_flag = False


game = Game()
game.start()
