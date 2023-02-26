import cv2, numpy, pyautogui, time
from colorama import Fore, Style

def screen_size(width: int, height: int):
    screen_size_var = (width, height)
    return screen_size_var

def screen_fps(fps: int):
    fps_var = fps

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(
    "output.avi",
    fourcc,
    20.0,
    screen_size(1920, 1080)
)

fps = screen_fps(fps=60)

