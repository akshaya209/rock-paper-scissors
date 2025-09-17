from ui import Ui
import tkinter as tk
from tkinter import messagebox
import random
import pandas as pd
class Game(Ui):
    def __init__(self):
        super().__init__()
        self.user_score = 0
        self.computer_score = 0
        self.draws = 0
        self.score_text = None
        self.moves=['rock','paper','scissor']
        self.user_choice=None
        self.computer_choice=None
        self.start_screen()
        self.link_button()
    def link_button(self):
        for i in self.button:
            if i=="rock" or i=="paper" or i=="scissor":
                self.button[i].config(command=lambda choice=i: self.get_user_choice(choice))
    def get_user_choice(self,user_choice):
        self.user_choice=user_choice
        for i in self.button:
            if i!=self.user_choice:
                self.button[i].config(state="disabled")
        self.play_game()
    def play_game(self):
        self.computer_choice=random.choice(self.moves)
        self.game_on(self.user_choice,self.computer_choice)
        rules = {
            "rock": "scissor",
            "paper": "rock",
            "scissor": "paper"
            }
        if self.user_choice == self.computer_choice:
            result = "It's a draw 🤝"
            self.draws += 1
        elif rules[self.user_choice] == self.computer_choice:
            result = "Hurray!!! You win 🎉"
            self.user_score += 1
        else:
            result = "Oops You lose 😥"
            self.computer_score += 1
        self.canvas.itemconfig(self.heading, text=result)
        self.canvas.itemconfig(self.heading, text=result)
        self.update_scoreboard()
        self.canvas.update()
        self.window.after(1000, self.reset_game)
        
    def update_scoreboard(self):
        if self.score_text:
            self.canvas.delete(self.score_text)
        self.score_text = self.canvas.create_text(
            450, 550,
            text=f"Score → You: {self.user_score} | Computer: {self.computer_score} | Draws: {self.draws}",
            font=("Arial", 18, "bold"),
            fill="white"
        )
        
    def reset_game(self):
        play_again=messagebox.askyesno(title="Replay",message="Do you wanna play again?")
        if play_again:
            self.canvas.delete("all")
            bg_img = tk.PhotoImage(file="./bgimg.png")
            self.canvas.bg = bg_img
            self.canvas.create_image(0, 0, image=bg_img, anchor="nw")
            self.heading=self.canvas.create_text(455,50,text="Rock🪨-Paper🗒️-Scissor✂️",
                                             font=("Arial",35,"bold italic"),
                                             fill="white")
            self.start_screen()
            self.link_button()
        else:
            self.window.destroy()
        
        

