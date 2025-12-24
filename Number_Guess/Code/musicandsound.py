import pygame
class Music_and_sound:
    def __init__(self):
        self.clicked_button_sound=pygame.mixer.Sound("Sounds/clicked menu and level.wav")
        self.click_correct=pygame.mixer.Sound("Sounds/correct.wav")
        self.click_correct.set_volume(1)
        self.click_wrong=pygame.mixer.Sound("Sounds/wrong.wav")
        self.click_wrong.set_volume(1)
        self.freeze_sound=pygame.mixer.Sound("Sounds/freeze.wav")

    # Music
    def music_menu_and_level(self):
        pygame.mixer.music.load("Sounds/music_menu&level.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

    # Game music
    def music_game(self):
        pygame.mixer.music.load("Sounds/music_game.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

    # Stop music
    def stop_music(self):
        pygame.mixer.music.stop()

    # Click button on menu or level
    def clicked_any_button_sound(self):
        self.clicked_button_sound.play()

    # Play correct click
    def play_correct_click(self):
        self.click_correct.play()

    # Freeze sound
    def play_freeze_sound(self):
        self.freeze_sound.play()

    # Play wrong click
    def play_wrong_click(self):
        self.click_wrong.play()