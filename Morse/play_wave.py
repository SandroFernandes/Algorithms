import numpy as np
import pygame


pygame.mixer.init(size=32)

buffer = np.sin(2 * np.pi * np.arange(44100) * 700 / 44100).astype(np.float32)
sound = pygame.mixer.Sound(buffer)

sound.play(0)
pygame.time.wait(int(sound.get_length() * 100))