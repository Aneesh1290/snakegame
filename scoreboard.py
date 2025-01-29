import streamlit as st

class Scoreboard:
    def __init__(self):
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        st.markdown(f"## Score: {self.score}")

    def game_over(self):
        st.markdown("## GAME OVER")

    def increase_score(self):
        self.score += 1
        st.experimental_rerun()  # Reruns the script to refresh the scoreboard
