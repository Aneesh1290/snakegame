import streamlit as st
import random

class Food:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.refresh()

    def refresh(self):
        self.x = random.randint(-280, 280)
        self.y = random.randint(-280, 280)
        st.session_state["food_position"] = (self.x, self.y)  # Store position in session state
        st.markdown(f"### 🍎 Food Position: ({self.x}, {self.y})")
