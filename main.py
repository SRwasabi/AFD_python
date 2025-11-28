import tkinter as tk
from tkinter import messagebox
import afd

ACCEPTED = 0
SYMBOL_ERROR = 1
STATE_ERROR = 2
NOT_FINAL_ERROR = 3

def center_window(window, width, height):
    window.update_idletasks() 
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

def run_dfa_button():
    try:
        states_list = [state.strip() for state in states.get().split(',')]
        alphabet_list = [symbol.strip() for symbol in alphabet.get().split(',')]
        
        transitions_dict = {}
        transitions_input = transitions.get("1.0", tk.END).strip().split('\n')

        # (q0, 1) = q1
        for line in transitions_input:
            parts = line.split('=')
            if len(parts) == 2:
                left, right = parts
                state_symbol = left.strip().strip().split(',')
                
                if len(state_symbol) == 2:
                    state = state_symbol[0].strip()
                    symbol = state_symbol[1].strip()
                    next_state = right.strip()
                    if (state, symbol) in transitions_dict:
                        raise Exception(f"Warning: Transition for ({state}, {symbol}) is being overwritten.\n\nThis is not allowed in a DFA.")
                    transitions_dict[(state, symbol)] = next_state

        initial = initial_state.get().strip()
        final_states_list = [state.strip() for state in final_states.get().split(',')]
        input_str = input_string.get().strip()

        dfa_instance = afd.DFA(states_list, alphabet_list, transitions_dict, initial, final_states_list)
        status, steps = dfa_instance.validate_input(input_str)
        step_text = " → ".join(steps)

        if status == ACCEPTED:
            result_label.config(text=f"ACCEPTED ✅\n\nPath:\n{step_text}")
        elif status == SYMBOL_ERROR:
            result_label.config(text=f"REJECTED ❌\n(Invalid symbol)\n\nPath:\n{step_text}")
        elif status == STATE_ERROR:
            result_label.config(text=f"REJECTED ❌\n(Missing transition)\n\nPath:\n{step_text}")
        elif status == NOT_FINAL_ERROR:
            result_label.config(text=f"REJECTED ❌\n(Did not end in final state)\n\nPath:\n{step_text}")
        else:
            result_label.config(text="An unexpected error occurred.")

    except Exception as e:
        messagebox.showerror("Error", str(e))
        return

# --- Main Window ---
room = tk.Tk()
room.title("DFA Simulator")
window_width = 800
window_height = 600
center_window(room, window_width, window_height)

room.grid_rowconfigure(0, weight=1)
room.grid_columnconfigure(0, weight=1)

# --- Centered Frame ---
frame = tk.Frame(room)
frame.grid(row=0, column=0)
for i in range(2):  # two columns: labels + entries
    frame.grid_columnconfigure(i, weight=1)

# --- Helper function ---
def add_label_widget(row, label_text, widget_class=tk.Entry, **kwargs):
    label = tk.Label(frame, text=label_text, anchor="e", justify="right")
    label.grid(row=row, column=0, sticky="e", padx=5, pady=5)
    widget = widget_class(frame, **kwargs)
    widget.grid(row=row, column=1, sticky="we", padx=5, pady=5)
    return widget

# --- Create the form ---
states = add_label_widget(0, "States (comma separated):", width=40)
alphabet = add_label_widget(1, "Alphabet (comma separated):", width=40)
transitions = add_label_widget(2, "Transitions (one per line):", widget_class=tk.Text, height=6, width=40)
initial_state = add_label_widget(3, "Initial State:", width=40)
final_states = add_label_widget(4, "Final States (comma separated):", width=40)
input_string = add_label_widget(5, "Input String:", width=40)

# --- Run button ---
run_button = tk.Button(frame, text="Run DFA", command=run_dfa_button)
run_button.grid(row=6, column=0, columnspan=2, pady=10)

# --- Result label ---
result_label = tk.Label(frame, text="", justify="center")
result_label.grid(row=7, column=0, columnspan=2, pady=10)

room.mainloop()


