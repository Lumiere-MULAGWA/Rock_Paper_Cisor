import customtkinter as ctk
import random

class RockPaperScissorsApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Pierre, Feuille, Ciseau")
        self.geometry("400x300")
        self.configure(bg='#333333')

        self.user_choice = None
        self.computer_choice = None

        self.label = ctk.CTkLabel(self, text="Choisissez : Pierre, Feuille, ou Ciseau", font=("Arial", 16))
        self.label.pack(pady=20)

        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.pack(pady=10)

        self.rock_button = ctk.CTkButton(self.button_frame, text="Pierre", command=lambda: self.play("Pierre"))
        self.rock_button.grid(row=0, column=0, padx=10)

        self.paper_button = ctk.CTkButton(self.button_frame, text="Feuille", command=lambda: self.play("Feuille"))
        self.paper_button.grid(row=0, column=1, padx=10)

        self.scissors_button = ctk.CTkButton(self.button_frame, text="Ciseau", command=lambda: self.play("Ciseau"))
        self.scissors_button.grid(row=0, column=2, padx=10)

        self.result_label = ctk.CTkLabel(self, text="", font=("Arial", 16))
        self.result_label.pack(pady=20)

    def play(self, user_choice):
        self.user_choice = user_choice
        self.computer_choice = random.choice(["Pierre", "Feuille", "Ciseau"])
        self.determine_winner()

    def determine_winner(self):
        if self.user_choice == self.computer_choice:
            result = f"Égalité ! Vous avez tous deux choisi {self.user_choice}."
        elif (self.user_choice == "Pierre" and self.computer_choice == "Ciseau") or \
             (self.user_choice == "Feuille" and self.computer_choice == "Pierre") or \
             (self.user_choice == "Ciseau" and self.computer_choice == "Feuille"):
            result = f"Vous gagnez ! {self.user_choice} bat {self.computer_choice}."
        else:
            result = f"Vous perdez ! {self.computer_choice} bat {self.user_choice}."

        self.result_label.configure(text=result)

if __name__ == "__main__":
    app = RockPaperScissorsApp()
    app.mainloop()
