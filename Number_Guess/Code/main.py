import pygame
import random
from musicandsound import Music_and_sound
#Window awal
class Game:
    pygame.init()
    def __init__(self):
        self.music=Music_and_sound()
        self.screen=pygame.display.set_mode((1280,720), pygame.RESIZABLE)
        self.running=True
        self.state="menu"
        self.music_state="menu or level"
        self.music_previous_state=None
        self.font=pygame.font.Font("Assets/GentySans-Regular.ttf", 36)
        self.flower_generated=False
        self.WIDTH, self.HEIGHT = 1280, 720

    #Main menu  
        # Background
        self.background=pygame.image.load("Assets/menu.png")
        self.background=pygame.transform.scale(self.background,(self.WIDTH, self.HEIGHT))

        # Credit
        self.credit=pygame.font.Font("Assets/GentySans-Regular.ttf", 20).render("By: Group 5", True, (0,0,0))
        self.name_credit_1=pygame.font.Font("Assets/GentySans-Regular.ttf", 20).render("Name : STEVEN JAYANTO LIWANG", True, (0,0,0))
        self.NIM_credit_1=pygame.font.Font("Assets/GentySans-Regular.ttf", 20).render("NIM : 25031554147", True, (0,0,0))
        self.name_credit_2=pygame.font.Font("Assets/GentySans-Regular.ttf", 20).render("Name : ADILA NURHIDAYATI", True, (0,0,0))
        self.NIM_credit_2=pygame.font.Font("Assets/GentySans-Regular.ttf", 20).render("NIM : 25031554249", True, (0,0,0))
        self.bottom_credit_rect=self.credit.get_rect(center=(self.WIDTH // 2, self.HEIGHT -130))
        self.name_credit_1_rect=self.name_credit_1.get_rect(center=(self.WIDTH // 2-200, self.HEIGHT -100))
        self.NIM_credit_1_rect=self.NIM_credit_1.get_rect(center=(self.WIDTH // 2-200, self.HEIGHT -50))
        self.name_credit_2_rect=self.name_credit_2.get_rect(center=(self.WIDTH // 2+200, self.HEIGHT -100))
        self.NIM_credit_2_rect=self.NIM_credit_2.get_rect(center=(self.WIDTH // 2+200, self.HEIGHT -50))
        
        # Play button
        self.play_img=pygame.image.load("Assets/play.png")
        self.play_img=pygame.transform.scale(self.play_img,(270,130))
        self.play_rect=self.play_img.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2 + 7))
        
        # Exit button
        self.exit_img=pygame.image.load("Assets/exit.png")
        self.exit_img=pygame.transform.scale(self.exit_img,(270,140))
        self.exit_rect=self.exit_img.get_rect(center=(self.WIDTH // 1.98, self.HEIGHT // 2 + 150))

    # Level 
        # Background
        self.level_img=pygame.image.load("Assets/level.png")
        self.level_img=pygame.transform.scale(self.level_img,(self.WIDTH, self.HEIGHT))
        self.screen.blit(self.level_img,(0,0))

        # Easy button
        self.easy_img=pygame.image.load("Assets/easy.png").convert_alpha()
        self.easy_img=pygame.transform.scale(self.easy_img,(300,70))
        self.easy_rect=self.easy_img.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2 - 100 ))
        self.screen.blit(self.easy_img,self.easy_rect)

        # Medium button
        self.medium_img=pygame.image.load("Assets/medium.png").convert_alpha()
        self.medium_img=pygame.transform.scale(self.medium_img,(300,70))
        self.medium_rect=self.medium_img.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2))
        self.screen.blit(self.medium_img,self.medium_rect)

        # Hard button
        self.hard_img=pygame.image.load("Assets/hard.png").convert_alpha()
        self.hard_img=pygame.transform.scale(self.hard_img,(300,70))
        self.hard_rect=self.hard_img.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2 + 100))
        self.screen.blit(self.hard_img,self.hard_rect)

        # Home button
        self.home_img=pygame.image.load("Assets/home.png")
        self.home_img=pygame.transform.scale(self.home_img,(150,99))
        self.home_rect=self.home_img.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2 + 250))

    #Atribute for all mode
        # Home button and skip button
        self.home_button=pygame.image.load("Assets/home.png").convert_alpha()
        self.home_button=pygame.transform.scale(self.home_button,(93,65))
        self.home_button_easy_rect=self.home_button.get_rect(topright=(self.WIDTH - 20, 5))

        self.skip_button=pygame.image.load("Assets/skip.png").convert_alpha()
        self.skip_button=pygame.transform.scale(self.skip_button,(65,50))
        self.skip_button_rect=self.skip_button.get_rect(topright=(self.WIDTH - 115, 12))

        # HP
        self.lives=3
        self.HP_img=pygame.image.load("Assets/HP.png").convert_alpha()
        self.HP_img=pygame.transform.scale(self.HP_img,(130,90))

        # Time
        self.time=30

        #Notes bilangan habis dibagi
        self.thenumber=random.randint(2,10)
        self.spin_number()

        #Flower
        self.flower=pygame.sprite.Group()

    # Bonus or power up
        self.time_is_freeze=False
        self.time_freeze=5
        self.trigerred_freeze=0
        self.freeze_effect=pygame.image.load("Assets/freeze_effect.png").convert_alpha()
        self.freeze_effect = pygame.transform.scale(self.freeze_effect, (self.WIDTH, self.HEIGHT))
        self.freeze_effect_rect=self.freeze_effect.get_rect(topleft=(0,0))
        self.minimal_combo_freeze=0

        self.triggered_bonus_HP=0
        self.active_notif_HP=False 
        self.time_notif_HP=0.3 
        self.notif_HP_text=self.font.render("+1", True, (0,0,0)) 
        self.minimal_combo_bonus_HP=0
        self.clock_img=pygame.image.load("Assets/clock.png").convert_alpha()
        self.clock_img=pygame.transform.scale(self.clock_img,(50,50))

    #Easy game
        # Background
        self.easy_level_img=pygame.image.load("Assets/easy_level.png")
        self.easy_level_img=pygame.transform.scale(self.easy_level_img,(self.WIDTH, self.HEIGHT))

        #Flower
        self.easy_flower_img=pygame.image.load("Assets/easy flower.png").convert_alpha()
        self.easy_flower_img=pygame.transform.scale(self.easy_flower_img,(180,180))

    # Medium game
        # Background
        self.medium_level_img=pygame.image.load("Assets/medium_level.png")
        self.medium_level_img=pygame.transform.scale(self.medium_level_img,(self.WIDTH, self.HEIGHT))

        #Flower
        # Medium flower images
        self.medium_flower_imgs = [
            pygame.transform.scale(pygame.image.load("Assets/blue.png").convert_alpha(), (250,150)),
            pygame.transform.scale(pygame.image.load("Assets/pink.png").convert_alpha(), (250,150)),
            pygame.transform.scale(pygame.image.load("Assets/purple.png").convert_alpha(), (250,150)),
            pygame.transform.scale(pygame.image.load("Assets/orange.png").convert_alpha(), (250,150)),
]

        

   # Hard game
        # Background dan papan
        self.hard_level_img=pygame.image.load("Assets/hard_level.png")
        self.hard_level_img=pygame.transform.scale(self.hard_level_img,(self.WIDTH, self.HEIGHT))
        self.board_img=pygame.image.load("Assets/hard board.png").convert_alpha()
        self.board_img=pygame.transform.scale(self.board_img,(403, 280))

        #Flower
        self.hard_flower_imgs = [
            pygame.transform.scale(pygame.image.load("Assets/pink_2.png").convert_alpha(), (160,110)),
            pygame.transform.scale(pygame.image.load("Assets/purple_2.png").convert_alpha(), (160,110)),
            pygame.transform.scale(pygame.image.load("Assets/biru.png").convert_alpha(), (160,110)),
            pygame.transform.scale(pygame.image.load("Assets/blue_2.png").convert_alpha(), (160, 110)),        
            pygame.transform.scale(pygame.image.load("Assets/cream.png").convert_alpha(), (160, 110)),        
]
    # Win lose atribute
        # Play again and exit
        self.play_again_img=pygame.image.load("Assets/play again win lose.png")
        self.play_again_rect=self.play_again_img.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2 + +100))

        self.exit_img_winlose=pygame.image.load("Assets/exit win lose.png")
        self.exit_rect_winlose=self.exit_img_winlose.get_rect(center=(self.WIDTH // 1.98, self.HEIGHT // 2 + 250))
        
        # Win
        self.win_background=pygame.image.load("Assets/You win.png")
        self.win_background=pygame.transform.scale(self.win_background,(self.WIDTH, self.HEIGHT))

        # Lose
        self.lose_background=pygame.image.load("Assets/You lose.png")
        self.lose_background=pygame.transform.scale(self.lose_background,(self.WIDTH, self.HEIGHT))
            
# All evennt
    # Clicked method
    def run(self):
        while self.running:
            self.handle_events()
            self.draw()
            pygame.display.flip()
            self.clock=pygame.time.Clock()
            self.handle_music()
            self.difference()

    # Handle music
    def handle_music(self):
        if self.music_state != self.music_previous_state:
            if self.music_state == "menu or level":
                self.music.music_menu_and_level()
            elif self.music_previous_state == "menu or level":
                self.music.stop_music()
                self.music.music_game()
            self.music_previous_state = self.music_state

    def draw (self):
        if self.state=="menu":
            self.draw_menu()
        elif self.state=="level":
            self.draw_level()
        elif self.state=="easy":
            self.draw_easy()
        elif self.state=="medium":
            self.draw_medium()
        elif self.state=="hard":
            self.draw_hard()
        elif self.state=="win":
            self.draw_win()
        elif self.state=="lose":
            self.draw_lose()

    # Handle event
    def handle_events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.running=False

                #resize
            if event.type == pygame.VIDEORESIZE:
                self.WIDTH, self.HEIGHT = event.w, event.h
                self.screen = pygame.display.set_mode(
                    (self.WIDTH, self.HEIGHT), pygame.RESIZABLE
            )

            if event.type==pygame.MOUSEBUTTONDOWN:
                if self.state=="menu":
                    self.click_on_menu(event) 
                elif self.state=="level":
                    self.click_on_level(event)
                elif self.state=="easy":
                    self.click_on_easy(event)
                elif self.state=="medium":
                    self.click_on_medium(event)
                elif self.state=="hard":
                    self.click_on_hard(event)
                elif self.state=="win" or self.state=="lose":
                    self.click_on_winlose(event)

    #Main Menu
    def draw_menu(self):
        pygame.display.set_caption("Game Menu")
        self.screen.blit(self.background,(0,0))
        self.screen.blit(self.play_img,self.play_rect)
        self.screen.blit(self.exit_img,self.exit_rect)
        self.screen.blit(self.credit,self.bottom_credit_rect)
        self.screen.blit(self.name_credit_1,self.name_credit_1_rect)
        self.screen.blit(self.name_credit_2,self.name_credit_2_rect)
        self.screen.blit(self.NIM_credit_1,self.NIM_credit_1_rect)
        self.screen.blit(self.NIM_credit_2,self.NIM_credit_2_rect)

    #Handle mouse click for menu
    def click_on_menu(self, event):
        if self.play_rect.collidepoint(event.pos):
            self.state="level"
            self.music.clicked_any_button_sound()
            self.draw_level()
        elif self.exit_rect.collidepoint(event.pos):
            self.music.clicked_any_button_sound()
            self.running=False

    # Level Menu
    def draw_level(self):
        pygame.display.set_caption("Game Level")
        self.screen.blit(self.level_img,(0,0))
        self.screen.blit(self.easy_img,self.easy_rect)
        self.screen.blit(self.medium_img,self.medium_rect)
        self.screen.blit(self.hard_img,self.hard_rect)
        self.screen.blit(self.home_img,self.home_rect)
        
    #Handle mouse click for level
    def click_on_level(self, event):
        if self.easy_rect.collidepoint(event.pos):
            self.state="easy"
            self.music_state="easy"
            self.music.clicked_any_button_sound()
        elif self.medium_rect.collidepoint(event.pos):
            self.state="medium"
            self.music_state="medium"
            self.music.clicked_any_button_sound()
        elif self.hard_rect.collidepoint(event.pos):
            self.state="hard"
            self.music_state="hard"
            self.music.clicked_any_button_sound()
        elif self.home_rect.collidepoint(event.pos):
            self.state="menu"
            self.music.clicked_any_button_sound()

    #Draw easy level
    def draw_easy(self):
        pygame.display.set_caption("Easy Level")
        self.screen.blit(self.easy_level_img,(0,0))
        self.screen.blit(self.text1, (self.WIDTH//2 - 160, 100))
        self.screen.blit(self.text2, (self.WIDTH//2 - 160, 145))
        self.screen.blit(self.home_button, self.home_button_easy_rect)
        self.screen.blit(self.skip_button, self.skip_button_rect)

        # TIme
        self.time_label=self.font.render(str(int(self.time)), True, (0, 0, 0))
        self.screen.blit(self.clock_img, (self.WIDTH//2-6, 0))
        self.screen.blit(self.time_label, (self.WIDTH//2, 10))

        # Flower image
        self.flower.draw(self.screen)
        
        # Flower place and color
        self.flower_data = [
                        (57, 623), (199, 655), (354, 642), (493, 656), (633, 647), (786, 644), (945, 637), (1100, 683),
                        (1203, 583), (1117, 495), (955, 519), (813, 503), (657, 513), (495, 526), (353, 505), (216, 516), (105, 475),
                    ]
                    
        self.flower_colors = [
    (255, 80, 80),   # merah terang
    (80, 255, 80),   # hijau terang
    (80, 80, 255),   # biru terang
    (255, 255, 80),  # kuning terang
    (255, 120, 255), # pink terang
]
        
        #Generate flower
        if self.flower_generated == False:
            self.generate_flower(self.easy_flower_img)
            self.flower_generated=True

        # HP
        self.generate_HP()
        self.time_left()
        self.notification_HP()

    # Click on easy
    def click_on_easy(self, event):
        if self.home_button_easy_rect.collidepoint(event.pos):
            self.state = "level"
            self.music_state="menu or level"
            self.clear_all_status()
            self.music.clicked_any_button_sound()

        elif self.skip_button_rect.collidepoint(event.pos):
            self.spin_number()
            self.music.clicked_any_button_sound()
        else:
            self.click_on_flower(event)

   #Draw medium level
    def draw_medium(self):
        pygame.display.set_caption("Medium Level")
        self.screen.blit(self.medium_level_img,(0,0))
        text1_rect = self.text1.get_rect(center=(self.WIDTH//2 + 40, 120))
        text2_rect = self.text2.get_rect(center=(self.WIDTH//2 + 40, 160))
        self.screen.blit(self.text1, text1_rect)
        self.screen.blit(self.text2, text2_rect)
        self.screen.blit(self.home_button, self.home_button_easy_rect)
        self.screen.blit(self.skip_button, self.skip_button_rect)

        # TIme
        self.time_label=self.font.render(str(int(self.time)), True, (0, 0, 0))
        self.screen.blit(self.clock_img, (self.WIDTH//2-6, 0))
        self.screen.blit(self.time_label, (self.WIDTH//2, 10))

        # Flower image
        self.flower.draw(self.screen)
        
        # Flower place and color
        self.flower_data = [
                        (77, 414),
                        (271, 430),
                        (225, 539),
                        (427, 554),
                        (460, 437),
                        (637, 422),
                        (583, 589),
                        (707, 515),
                        (866, 436),
                        (817, 617),
                        (954, 545),
                        (1057, 429),
                        (1197, 471),
                        (1122, 579),
                    ]
                    
        self.flower_colors = [
                        (255, 214, 214),  # pastel pink
                        (255, 239, 204),  # pastel peach / cream
                        (255, 255, 204),  # pastel kuning lembut
                        (214, 245, 214),  # pastel hijau mint
                        (204, 236, 255),  # pastel biru langit
                        (229, 214, 255),  # pastel lavender
                        (255, 220, 235),  # pastel rose
                        (210, 240, 255),  # pastel baby blue
                        (240, 255, 240),  # pastel hijau pucat (honeydew)
                        (255, 228, 235),  # pastel pink pucat
                        (245, 225, 255),  # pastel lilac
                        (255, 242, 225),  # pastel apricot muda
                    ]
        
        #Generate flower
        if self.flower_generated == False:
            self.generate_flower()
            self.flower_generated=True

        # HP
        self.generate_HP()
        self.time_left()
        self.notification_HP()

    # Click on medium
    def click_on_medium(self, event):
        if self.home_button_easy_rect.collidepoint(event.pos):
            self.state = "level"
            self.music_state="menu or level"
            self.clear_all_status()
            self.music.clicked_any_button_sound()

        elif self.skip_button_rect.collidepoint(event.pos):
            self.spin_number()
            self.music.clicked_any_button_sound()
        else:
            self.click_on_flower(event)

   #Draw hard level
    def draw_hard(self):
        pygame.display.set_caption("Hard Level")
        self.screen.blit(self.hard_level_img,(0,0))
        self.screen.blit(self.board_img,(681,0))
        self.screen.blit(self.text1, (self.WIDTH//2 + 80, 150))
        self.screen.blit(self.text2, (self.WIDTH//2 + 80, 195))
        self.screen.blit(self.home_button, self.home_button_easy_rect)
        self.screen.blit(self.skip_button, self.skip_button_rect)

        # TIme
        self.time_label=self.font.render(str(int(self.time)), True, (0, 0, 0))
        self.screen.blit(self.clock_img, (self.WIDTH//2-6, 0))
        self.screen.blit(self.time_label, (self.WIDTH//2, 10))

        # Flower image
        self.flower.draw(self.screen)
        
        # Flower place and color
        self.flower_data = [
                    (48, 678), (158, 656), (280, 647), (389, 669), (519, 666), (639, 670), (753, 645), (865, 665),
                    (990, 661), (1092, 659), (1217, 644), (1157, 574), (1041, 565), (917, 552), (782, 544), (663, 555),
                    (537, 559), (415, 559), (299, 543), (183, 551), (57, 560),
                    ]
                    
        
        #Generate flower
        if self.flower_generated == False:
            self.generate_flower()
            self.flower_generated=True

        # HP
        self.generate_HP()
        self.time_left()
        self.notification_HP()

    # Click on hard
    def click_on_hard(self, event):
        if self.home_button_easy_rect.collidepoint(event.pos):
            self.state = "level"
            self.music_state="menu or level"
            self.clear_all_status()
            self.music.clicked_any_button_sound()

        elif self.skip_button_rect.collidepoint(event.pos):
            self.spin_number()
            self.music.clicked_any_button_sound()
        else:
            self.click_on_flower(event)
        
#Easy, medium, hard method
    # Difference
    def difference(self):
        if self.state == "easy":
            self.minimal_combo_freeze=2
            self.minimal_combo_bonus_HP=3
        elif self.state == "medium":
            self.minimal_combo_freeze=3
            self.minimal_combo_bonus_HP=4
        elif self.state == "hard":
            self.minimal_combo_freeze=5
            self.minimal_combo_bonus_HP=6

    # Power up (Time and freeze)
    def time_left(self):
        if self.time > 0 and self.time_is_freeze==False:
            self.time-=self.clock.tick(60)/1000
        elif self.time > 0 and self.time_is_freeze==True:
            if self.time_freeze > 0:
                self.time_freeze-=self.clock.tick(60)/1000
                self.screen.blit(self.freeze_effect,self.freeze_effect_rect)
            else:
                self.time_is_freeze=False
                self.time_freeze=5
                self.trigerred_freeze=0
        else:
            self.state = "lose"
            self.music_state="menu or level"
            self.clear_all_status()

    # Power up (Bonus HP)
    def bonus_HP(self):
        self.lives += 1
        self.active_notif_HP=True
        self.generate_HP()

    # Notification +1 HP
    def notification_HP(self): 
        if self.active_notif_HP==True and self.time_notif_HP>0:
            self.time_notif_HP-=self.clock.tick(60)/1000
            self.screen.blit(self.HP_img, (20, self.HEIGHT // 2 - 100))
            self.screen.blit(self.notif_HP_text, (25, self.HEIGHT //2 - 100))
        else:
            self.active_notif_HP=False
            self.time_notif_HP=0.3

    #Generate HP
    def generate_HP(self):
        HP_coordinat=[(5, 3), (100, 3), (200, 3)]
        for x in range(self.lives):
            self.screen.blit(self.HP_img,(HP_coordinat[x]))

    # Generate flower
    def generate_flower(self, theflower=None):
        # Random number for each flower
        if self.state == "easy":
            self.time=60
        elif self.state == "medium":
            self.time=45
        elif self.state == "hard":
            self.time=30
        number=[]
        for x in range(len(self.flower_data)):
            number.append(random.randint(1,10)*random.randint(1,10))

        # Collab the number
        for z, (x,y) in enumerate(self.flower_data):
            if self.state == "medium":
                flower_img = random.choice(self.medium_flower_imgs)
                color=None
            elif self.state == "hard":  # random untuk hard
                flower_img = random.choice(self.hard_flower_imgs)
                color = None
            else:
                flower_img = theflower
                flower_colors = [
                        (255, 214, 214),  # pastel pink
                        (255, 239, 204),  # pastel peach / cream
                        (255, 255, 204),  # pastel kuning lembut
                        (214, 245, 214),  # pastel hijau mint
                        (204, 236, 255),  # pastel biru langit
                        (229, 214, 255),  # pastel lavender
                        (255, 220, 235),  # pastel rose
                        (210, 240, 255),  # pastel baby blue
                        (240, 255, 240),  # pastel hijau pucat (honeydew)
                        (255, 228, 235),  # pastel pink pucat
                        (245, 225, 255),  # pastel lilac
                        (255, 242, 225),  # pastel apricot muda
                    ]
                color = random.choice(flower_colors)
            f = Flower(x, y, number[z], color=color, flower_img=flower_img)
            self.flower.add(f)


    # Flower clicked
    def click_on_flower(self, event):
        self.time_left()
        for f in list(self.flower):
            if f.rect.collidepoint(event.pos):
                if f.value % self.thenumber == 0:  # klik benar
                    f.kill()   # bunga hilang
                    self.music.play_correct_click()
                    self.spin_number()
                    self.trigerred_freeze+=1
                    self.triggered_bonus_HP+=1
                    # Power up
                    if self.trigerred_freeze==self.minimal_combo_freeze and self.time_is_freeze==False:
                        self.time_is_freeze=True
                        self.trigerred_freeze=0
                        self.music.play_freeze_sound()
                    
                    if self.lives < 3:
                        if self.triggered_bonus_HP==self.minimal_combo_bonus_HP:
                            self.bonus_HP()
                            self.triggered_bonus_HP=0

                else:  # klik salah
                    self.lives -= 1
                    self.music.play_wrong_click()
                    self.trigerred_freeze=0
                    self.triggered_bonus_HP=0
                    self.spin_number()

                # WIn
                if len(self.flower)==0:
                    self.state = "win"
                    self.music_state="menu or level"
                    self.clear_all_status()
                break
        if self.lives <= 0:
            self.state = "lose"
            self.music_state="menu or level"
            self.clear_all_status()
    
    # Spin number
    def spin_number(self):
        self.thenumber=random.randint(2,10)
        self.text1= self.font.render(f"pilihlah bilangan", True, (255,255,255))
        self.text2= self.font.render(f"kelipatan {self.thenumber}", True, (255,255,255))

    # CLear all status
    def clear_all_status(self):
        self.flower.empty()
        self.flower_generated = False
        self.lives=3
        self.time=30
        self.clear_trigerred_and_bonus()

    # Clear trigerred and bonus
    def clear_trigerred_and_bonus(self):
        self.trigerred_freeze=0
        self.triggered_bonus_HP=0
        self.time_is_freeze=False
        self.active_notif_HP=False
        self.time_notif_HP=2 
        self.time_freeze=5

    # Draw win
    def draw_win(self):
        self.screen.blit(self.win_background, (0, 0))
        self.screen.blit(self.play_again_img, self.play_again_rect)
        self.screen.blit(self.exit_img_winlose, self.exit_rect_winlose)
    
    def draw_lose(self):
        self.screen.blit(self.lose_background, (0, 0))
        self.screen.blit(self.play_again_img, self.play_again_rect)
        self.screen.blit(self.exit_img_winlose, self.exit_rect_winlose)

    def click_on_winlose(self,event):
        if self.play_again_rect.collidepoint(event.pos):
            self.state="level"
            self.music_state="menu or level"
            self.music.clicked_any_button_sound()
            self.clear_all_status()
        elif self.exit_rect_winlose.collidepoint(event.pos):
            self.state="menu"
            self.music_state="menu or level"
            self.music.clicked_any_button_sound()
            self.clear_all_status()

#Class untuk gambarnya
class Flower(pygame.sprite.Sprite):
    def __init__(self, x, y, value, color, flower_img):
        super().__init__()
        # salin gambar dasar
        self.image = flower_img.copy()

        # tint warna
        if color is not None:
            tint = pygame.Surface(self.image.get_size(), pygame.SRCALPHA)
            tint.fill(color)
            self.image.blit(tint, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
         # tulis angka
        font = pygame.font.Font ("Assets/GentySans-Regular.ttf", 25
                                 )
        text = font.render(str(value), True, (120, 80, 40))
        rect_text = text.get_rect(center=(flower_img.get_width()//2, flower_img.get_height()//2))
        self.image.blit(text, rect_text)
        self.rect = self.image.get_rect(center=(x, y))
        self.value = value
        
Game().run()