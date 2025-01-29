import streamlit as st
import pygame
import random

# Initialize pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 20
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake and Food Initialization
snake = [(300, 300)]
direction = (0, -GRID_SIZE)  # Moving upwards initially
food = (random.randint(0, WIDTH // GRID_SIZE - 1) * GRID_SIZE, random.randint(0, HEIGHT // GRID_SIZE - 1) * GRID_SIZE)
score = 0
game_over = False

def move_snake():
    global snake, food, score, game_over
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    
    # Check for collisions
    if new_head in snake or new_head[0] < 0 or new_head[1] < 0 or new_head[0] >= WIDTH or new_head[1] >= HEIGHT:
        game_over = True
        return
    
    snake.insert(0, new_head)
    if new_head == food:
        score += 1
        food = (random.randint(0, WIDTH // GRID_SIZE - 1) * GRID_SIZE, random.randint(0, HEIGHT // GRID_SIZE - 1) * GRID_SIZE)
    else:
        snake.pop()

def change_direction(new_direction):
    global direction
    if (direction[0] == 0 and new_direction[0] == 0) or (direction[1] == 0 and new_direction[1] == 0):
        return  # Prevent moving in the opposite direction
    direction = new_direction

# Streamlit UI
st.title("🐍 Snake Game in Streamlit")
st.write(f"**Score:** {score}")

if st.button("Up"): change_direction((0, -GRID_SIZE))
if st.button("Down"): change_direction((0, GRID_SIZE))
if st.button("Left"): change_direction((-GRID_SIZE, 0))
if st.button("Right"): change_direction((GRID_SIZE, 0))

if not game_over:
    move_snake()
else:
    st.write("### Game Over! Refresh to Restart.")
