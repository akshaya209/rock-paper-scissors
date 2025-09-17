import tkinter as tk

class Ui:
    def __init__(self):
        self.window=tk.Tk()
        self.window.title("Rock-Paper-Scissor")
        self.window.geometry("900x600")
        self.canvas=tk.Canvas(self.window,width=900,height=600)
        self.canvas.pack()
        bg_img = tk.PhotoImage(file="./bgimg.png")
        self.canvas.bg = bg_img
        self.canvas.create_image(0, 0, image=bg_img, anchor="nw")

        self.heading=self.canvas.create_text(455,50,text="Rock🪨-Paper🗒️-Scissor✂️",
                                             font=("Arial",35,"bold italic"),
                                             fill="white")
        self.photoimage=[]
        self.image={}
        self.button_window=[]
        self.button={}
    def define_rules(self):
        rules_heading=self.canvas.create_text(400,400,text="🎮 Rock – Paper – Scissors Rules",font=("Arial",20),fill="navy",tag="rules_heading")
        rules = self.canvas.create_text(
            450, 450,
            text="""
        1.Rock 🪨 beats Scissors ✂️ (Rock crushes Scissors).
        2.Paper 🗒️ beats Rock 🪨 (Paper covers Rock).
        3.Scissors ✂️ beats Paper 🗒️ (Scissors cut Paper).
        4.If both you choose the same → It is a tie 🤝""",
            font=("Arial", 16),
            fill="white",tag="rules"
        )
    def start_screen(self):
        self.canvas.delete("rules")
        self.canvas.delete("rules_heading")
        #create rock paper and scissor images 
        img_rock=tk.PhotoImage(file="./images/rock.png")
        self.photoimage.append(img_rock)
        self.image['rock']=self.canvas.create_image(100,180,image=self.photoimage[-1])
        img_paper=tk.PhotoImage(file="./images/paper.png")
        self.photoimage.append(img_paper)
        self.image['paper']=self.canvas.create_image(400,180,image=self.photoimage[-1])
        img_scissor=tk.PhotoImage(file="./images/scissor.png")
        self.photoimage.append(img_scissor)
        self.image['scissor']=self.canvas.create_image(700,180,image=self.photoimage[-1])
        #create buttons below them
        self.button['rock']=tk.Button(text="Rock",fg="navy",highlightthickness=0)
        self.button['paper']=tk.Button(text="Paper",fg="navy",highlightthickness=0)
        self.button['scissor']=tk.Button(text="Scissor",fg="navy",highlightthickness=0)
        x=self.canvas.create_window(100,300,window=self.button['rock'])
        self.button_window.append(x)
        x=self.canvas.create_window(400,300,window=self.button['paper'])
        self.button_window.append(x)
        x=self.canvas.create_window(700,300,window=self.button['scissor'])
        self.button_window.append(x)
    def game_on(self,user_choice,computer_choice):
        for item_id in list(self.image.values()):
            try:
                self.canvas.delete(item_id)
            except Exception:
                pass
        for i in self.button_window:
            try:
                self.canvas.delete(i)
            except Exception:
                pass
        
        
        self.image.clear()
        image=tk.PhotoImage(file=f"./images/{user_choice}.png")
        self.photoimage.append(image)
        self.canvas.create_text(100,500,text="Your move",font=("Arial",35),fill="white")
        self.image[f"{user_choice}"]=self.canvas.create_image(100,180,image=self.photoimage[-1])
        image=tk.PhotoImage(file=f"./images/{computer_choice}.png")
        self.canvas.create_text(400,180,text="Vs",font=("Arial",35),fill="white")
        self.canvas.create_text(700,500,text="Computer move",font=("Arial",35),fill="white")
        self.photoimage.append(image)
        self.image[f"{computer_choice}"]=self.canvas.create_image(700,180,image=self.photoimage[-1])
        
        
        
