import cv2
import numpy as np
import pygame

# Function to initialize Pygame
def init_pygame():
    pygame.init()
    # Set up Pygame window
    window_size = (800, 600)
    return pygame.display.set_mode(window_size)

# Function to display question and options
def display_question(screen, question, options, selected_option):
    font = pygame.font.Font(None, 36)
    text = font.render(question, True, (255, 255, 255))
    screen.blit(text, (50, 50))
    for i, option in enumerate(options):
        text = font.render(option, True, (255, 255, 255))
        color = (0, 255, 0) if i == selected_option else (255, 255, 255)
        screen.blit(text, (50, 100 + i * 50), special_flags=pygame.BLEND_RGB_ADD)

# Function to detect hand using cascade classifier
def detect_hand(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hand_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_hand.xml')
    hands = hand_cascade.detectMultiScale(gray, 1.1, 5)
    return hands

# Main function
def main():
    screen = init_pygame()
    question = "What is the capital of France?"
    options = ["A. London", "B. Paris", "C. Rome", "D. Berlin"]
    correct_answer = "B. Paris"

    cap = cv2.VideoCapture(0)

    selected_option = None

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        hands = detect_hand(frame)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                cap.release()
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 50 <= x <= 400 and 100 <= y <= 300:
                    selected_option = (y - 100) // 50

        screen.fill((0, 0, 0))
        display_question(screen, question, options, selected_option)
        pygame.display.flip()

    pygame.quit()
    cap.release()

if __name__ == "__main__":
    main()
