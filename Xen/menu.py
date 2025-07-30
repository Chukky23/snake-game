import pygame



class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = -100


    def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0,0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.GameModex, self.GameModey = self.mid_w, self.mid_h + 50
        self.Highscorex, self.Highscorey = self.mid_w, self.mid_h + 70
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Main Menu', 20, self.game.DISPLAY_W /2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text("Start Game", 20, self.startx, self.starty)
            self.game.draw_text("Game Mode", 20, self.GameModex, self.GameModey)
            self.game.draw_text("High score", 20, self.Highscorex, self.Highscorey)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == "Start":
                self.cursor_rect.midtop = (self.GameModex + self.offset, self.GameModey)
                self.state = "Game Mode"
            elif self.state == "Game Mode":
                self.cursor_rect.midtop = (self.Highscorex + self.offset, self.Highscorey)
                self.state = "High Score"
            elif self.state == "High Score":
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = "Start"
        elif self.game.UP_KEY:
            if self.state == "Start":
                self.cursor_rect.midtop = (self.Highscorex + self.offset, self.Highscorey)
                self.state = "High Score"
            elif self.state == "Game Mode":
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = "Start"
            elif self.state == "High Score":
                self.cursor_rect.midtop = (self.GameModex + self.offset, self.GameModey)
                self.state = "Game Mode"

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == "Start":
                self.game.playing = True
            elif self.state == "Game Mode":
                self.game.curr_menu = self.game.game_mode
            elif self.state == "High Score":
                self.game.curr_menu = self.game.high_score
            self.run_display = False


class GameModeMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Classic'
        self.classicx, self.classicy = self.mid_w, self.mid_h + 20
        self.adventurex, self.adventurey = self.mid_w, self.mid_h + 40
        self.beatclockx, self.beatclocky = self.mid_w, self.mid_h + 60
        self.cursor_rect.midtop = (self.classicx + self.offset, self.classicy)


    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text("Game Mode", 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            self.game.draw_text('Classic', 15, self.classicx, self.classicy)
            self.game.draw_text('Adventure', 15, self.adventurex, self.adventurey)
            self.game.draw_text('Beat the Clock', 15, self.beatclockx, self.beatclocky)
            self.draw_cursor()
            self.blit_screen()


    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY:
            if self.state == 'Classic':
                self.state = 'Beat the Clock'
                self.cursor_rect.midtop = (self.beatclockx + self.offset, self.beatclocky)
            elif self.state == 'Adventure':
                self.state = 'Classic'
                self.cursor_rect.midtop = (self.classicx + self.offset, self.beatclocky)
            elif self.state == 'Beat the clock':
                self.state = 'Adventure'
                self.cursor_rect.midtop = (self.adventurex + self.offset, self.adventurey)
        elif self.game.DOWN_KEY:
            if self.state == 'Classic':
                self.state = 'Adventure'
                self.cursor_rect.midtop = (self.adventurex + self.offset, self.adventurey)
            elif self.state == 'Adventure':
                self.state = 'Beat the Clock'
                self.cursor_rect.midtop = (self.beatclockx + self.offset, self.beatclocky)
            elif self.state == 'Beat the Clock':
                self.state = 'Classic'
                self.cursor_rect.midtop = (self.classicx + self.offset, self.classicy)
        elif self.game.START_KEY:
            pass
                
class HighScoreMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('High Score', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H /2 - 20)
            self.blit_screen()
