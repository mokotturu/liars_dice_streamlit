import tkinter as tk
from tkinter import font

import ttkbootstrap as ttk


class PlayerFrame(ttk.Frame):
	def __init__(self, root, player_name, game_status, **kwargs):
		super().__init__(root, **kwargs)
		self.configure(borderwidth=2, relief="groove", padding=10)

		self.player_name = player_name
		self.heading = ttk.Label(self, text=self.player_name, font=("Arial", 16))
		self.heading.pack(pady=10)

		self.game_status = ttk.Label(self, text=f"Game Status: {game_status}", font=("Arial", 12))
		self.game_status.pack(pady=10)


if __name__ == "__main__":
	'''
	Layout of the game
	+------------------------------------------+
	|  +----+          +----+          +----+  |
	|  |    |          |    |          |    |  |
	|  | c1 |          | c2 |          | r1 |  |
	|  |    |          |    |          |    |  |
	|  +----+          +----+          +----+  |
	|                                          |
	|  +------------------------------------+  |
	|  |                                    |  |
	|  |                 p1                 |  |
	|  |                                    |  |
	|  +------------------------------------+  |
	|  +------------------------------------+  |
	|  |                                    |  |
	|  |              Text Box              |  |
	|  |                                    |  |
	|  +------------------------------------+  |
	+------------------------------------------+
	'''

	root = ttk.Window(themename="cosmo", title="Liar's Dice Game")
	root.grid_rowconfigure(0, weight=1)
	root.grid_columnconfigure(0, weight=1)

	inner_frame = ttk.Frame(root, border=2, relief="groove")
	inner_frame.grid(row=0, column=0, padx=10, pady=10)

	heading = ttk.Label(inner_frame, text="Liar's Dice Game", font=("Arial", 24))
	heading.grid(row=0, column=0, pady=10)

	current_turn = ttk.Label(inner_frame, text=f"Current Turn: Confederate 1", font=("Arial", 16))
	current_turn.grid(row=1, column=0, pady=10)

	players_container = ttk.Frame(inner_frame)
	players_container.grid(row=2, column=0)
	
	c1_frame = PlayerFrame(players_container, "Confederate 1", "h i d d e n")
	c2_frame = PlayerFrame(players_container, "Confederate 2", "h i d d e n")
	r1_frame = PlayerFrame(players_container, "Robot", "h i d d e n")
	p1_frame = PlayerFrame(inner_frame, "You", "s h o w n")
	robotmsg = tk.StringVar()
	msg_label = ttk.Label(inner_frame, text=f"Robot says: ", font=("Arial", 12))

	c1_frame.grid(row=0, column=0, sticky="news", pady=10, padx=(0, 10))
	c2_frame.grid(row=0, column=1, sticky="news", pady=10, padx=(10, 10))
	r1_frame.grid(row=0, column=2, sticky="news", pady=10, padx=(10, 0))
	p1_frame.grid(row=3, column=0, sticky="news", pady=10)
	msg_label.grid(row=4, column=0, pady=10)

	root.mainloop()