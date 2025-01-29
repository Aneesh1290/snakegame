import streamlit as st
import pygame
import time

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
MOVE_DISTANCE = 20
UP, DOWN, LEFT, RIGHT = (0, -MOVE_DISTANCE), (0, MOVE_DISTANCE), (-MOVE_DISTANCE, 0), (MOVE_DISTANCE, 0)

class Snake:
    def __init__(self):
        self.segments = [(300, 300), (280, 300), (260, 300)]
        self.direction = RIGHT
    
    def move(self):
        new_head = (self.segments[0][0] + self.direction[0], self.segments[0][1] + self.direction[1])
        self.segments = [new_head] + self.segments[:-1]
    
    def grow(self):
        self.segments.append(self.segments[-1])
    
    def set_direction(self, direction):
        if (self.direction[0] + direction[0], self.direction[1] + direction[1]) != (0, 0):
            self.direction = direction

# Streamlit UI
st.title("Snake Game with Streamlit")
snake = Snake()

if 'running' not in st.session_state:
    st.session_state.running = True

def move_snake():
    if st.session_state.running:
        snake.move()
        st.session_state.segments = snake.segments
        time.sleep(0.1)

def change_direction(direction):
    snake.set_direction(direction)

st.button("Up", on_click=change_direction, args=(UP,))
st.button("Down", on_click=change_direction, args=(DOWN,))
st.button("Left", on_click=change_direction, args=(LEFT,))
st.button("Right", on_click=change_direction, args=(RIGHT,))

while st.session_state.running:
    move_snake()
    st.write(snake.segments)
