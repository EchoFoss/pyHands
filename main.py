import mediapipe as mp
import cv2
import time

mpHands = mp.solutions.hands
hands = mpHands.Hands()

mpDraw = mp.solutions.drawing_utils

cam = cv2.VideoCapture(0)
x = []
y = []

text = ""
k = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

idset = ["", '1', "12", "123", "1234", "01234"]
