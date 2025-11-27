import tkinter as tk
import afd

room = tk.Tk()
room.title("AFD Simulator")
room.geometry("1024x800")

# States
states_label = tk.Label(room, text="States (comma separated):")
states_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)

states = tk.Entry(room, width=50)
states.grid(row=0, column=1, padx=10, pady=10)
states.focus()

# Alphabet
alphabet_label = tk.Label(room, text="Alphabet (comma separated):")
alphabet_label.grid(row=1, column=0, sticky="w", padx=10, pady=10)

alphabet = tk.Entry(room, width=50)
alphabet.grid(row=1, column=1, padx=10, pady=10)
alphabet.focus()

# Transitions
transitions_label = tk.Label(room, text="Transitions (one per line):")
transitions_label.grid(row=2, column=0, sticky="nw", padx=10, pady=10)

transitions = tk.Text(room, height=10, width=50)
transitions.grid(row=2, column=1, padx=10, pady=10)
transitions.focus()

# Initial State
initial_state_label = tk.Label(room, text="Initial State:")
initial_state_label.grid(row=3, column=0, sticky="w", padx=10, pady=10)

initial_state = tk.Entry(room, width=50)
initial_state.grid(row=3, column=1, padx=10, pady=10)
initial_state.focus()

# Final States
final_states_label = tk.Label(room, text="Final States (comma separated):")
final_states_label.grid(row=4, column=0, sticky="w", padx=10, pady=10)

final_states = tk.Entry(room, width=50)
final_states.grid(row=4, column=1, padx=10, pady=10)
final_states.focus()

# Input String
input_string_label = tk.Label(room, text="Input String:")
input_string_label.grid(row=5, column=0, sticky="w", padx=10, pady=10)

input_string = tk.Entry(room, width=50)
input_string.grid(row=5, column=1, padx=10, pady=10)
input_string.focus()

# button callback
run_button = tk.Button(room, text="Run AFD")
run_button.grid(row=6, column=1, padx=10, pady=10)

room.mainloop()





'''
if __name__ == "__main__":

  
    states = ['q0', 'q1', 'q2']
    alphabet = ['0', '1']
    transitions = {
        ('q0', '0'): 'q0',
        ('q0', '1'): 'q1',
        ('q1', '0'): 'q2',
        ('q1', '1'): 'q1',
        ('q2', '0'): 'q0',
        ('q2', '1'): 'q1',
    }
    initial_state = 'q0'
    final_states = ['q1']

    afd_instance = afd.AFD(states, alphabet, transitions, initial_state, final_states)
    #afd_instance.run_afd()'''

