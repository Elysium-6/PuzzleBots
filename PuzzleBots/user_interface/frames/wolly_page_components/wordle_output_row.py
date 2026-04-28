import tkinter as tk


class wordle_output_row(tk.Canvas):

    def __init__(self, master, width, height):
        tk.Canvas.__init__(self, master=master, width=width, height=height)

        self.squares = []
        self.square_size = height * 0.8
        self.spacing = height * 0.1
        self.start_x = height * 0.2

        for i in range(5):
            x1 = self.start_x + i * (self.square_size + self.spacing)
            x2 = x1 + self.square_size
            square = self.create_rectangle(
                x1, 10, x2, 10 + self.square_size,
                fill="white",
                outline="black",
                width=2
            )
            self.squares.append({
                'id': square,
                'color_index': 0,
                'x1': x1,
                'y1': 10,
                'x2': x2,
                'y2': 10 + self.square_size
            })

    def show_word(self, word, score):

        for i in range(5):

            ##for the colours
            quotient = score // (3 ** (4 - i))
            score = score % (3 ** (4 - i))
            if quotient == 2:
                self.itemconfig(self.squares[4-i]['id'], fill="green")
            elif quotient == 1:
                self.itemconfig(self.squares[4-i]['id'], fill="yellow")
            else:
                self.itemconfig(self.squares[4-i]['id'], fill="grey")

            ##for the letters
            center_x = (self.squares[i]["x1"] + self.squares[i]['x2']) / 2
            center_y = (self.squares[i]["y1"] + self.squares[i]["y2"]) / 2

            self.create_text(
                center_x, center_y,
                text=word[i],
                font=("Arial", 20, "bold"),
                fill="black"
            )

    def reset(self):
        pass