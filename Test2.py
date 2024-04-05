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
def display_question(screen, question, options):
    font = pygame.font.Font(None, 36)
    text = font.render(question, True, (255, 255, 255))
    screen.blit(text, (50, 50))
    for i, option in enumerate(options):
        text = font.render(option, True, (255, 255, 255))
        screen.blit(text, (50, 100 + i * 50))

# Main function
def main():
    screen = init_pygame()
    question = "What is the capital of France?"
    options = ["A. London", "B. Paris", "C. Rome", "D. Berlin"]
    correct_answer = "B. Paris"

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Resize the frame to match the Pygame window size
        frame = cv2.resize(frame, (800, 600))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                cap.release()
                return

        screen.fill((0, 0, 0))
        # Display camera feed
        pygame.surfarray.blit_array(screen, np.rot90(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
        display_question(screen, question, options)
        pygame.display.flip()

    pygame.quit()
    cap.release()

if __name__ == "__main__":
    main()
