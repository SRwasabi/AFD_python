import tkinter as tk
from tkinter import messagebox
import afn_func as fn
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


def send_status(status, step_text):
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


def run_dfa_button():
    #try:
        states_list = [state.strip() for state in states.get().split(',')]
        alphabet_list = [symbol.strip() for symbol in alphabet.get().split(',')]
        initial = initial_state.get().strip()
        final_states_list = [state.strip() for state in final_states.get().split(',')]
        input_str = input_string.get().strip()
        
        transitions_dict = {}
        transitions_input = transitions.get("1.0", tk.END).strip().split('\n')

        # (q0, 1) = q1
        fn.get_initial_transitions(transitions_input, transitions_dict)

        while True:
            stop = fn.convert(transitions_dict, final_states_list, states_list)
            if stop == True:
                break

        print("pre")
        print(transitions_dict)
        fn.concatenating(transitions_dict)
        print("\npos")
        print(transitions_dict)
        print("\nstates:",states_list)
        print(final_states_list)
        dfa_instance = afd.DFA(states_list, alphabet_list, transitions_dict, initial, final_states_list)
        status, steps = dfa_instance.validate_input(input_str)
        step_text = " → ".join(steps)
        send_status(status, step_text)
        automat_label.config(text=f"States - {dfa_instance.states}\nAlphabet - {dfa_instance.alphabet}\nInitial State - {dfa_instance.initial_state}\nFinal States - {dfa_instance.final_states}\nTransitions Dictonary - {dfa_instance.transitions}")

    #except Exception as e:
     #   messagebox.showerror("Error", str(e))
      #  return



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

dummy_focus = tk.Label(room)
dummy_focus.grid(row=0, column=0)
dummy_focus.lower()  # Send it to back

def remove_focus(event):
    widget = event.widget
    # If clicked widget is not an input widget, move focus to dummy
    if widget not in (states, alphabet, transitions, initial_state, final_states, input_string):
        dummy_focus.focus_set()

room.bind("<Button-1>", remove_focus)

for i in range(2):  # two columns: labels + entries
    frame.grid_columnconfigure(i, weight=1)

# --- Helper function ---
def add_label_widget(row, label_text, widget_class=tk.Entry, placeholder="", **kwargs):
    label = tk.Label(frame, text=label_text, anchor="e", justify="right")
    label.grid(row=row, column=0, sticky="e", padx=5, pady=5)

    widget = widget_class(frame, **kwargs)
    widget.grid(row=row, column=1, sticky="we", padx=5, pady=5)

    # Function to add placeholder behavior
    def on_focus_in(event):
        if widget_class == tk.Entry:
            if widget.get() == placeholder:
                widget.delete(0, tk.END)
                widget.config(fg="black")
        elif widget_class == tk.Text:
            if widget.get("1.0", tk.END).strip() == placeholder:
                widget.delete("1.0", tk.END)
                widget.config(fg="black")

    def on_focus_out(event):
        if widget_class == tk.Entry:
            if widget.get() == "":
                widget.insert(0, placeholder)
                widget.config(fg="grey")
        elif widget_class == tk.Text:
            if widget.get("1.0", tk.END).strip() == "":
                widget.insert("1.0", placeholder)
                widget.config(fg="grey")

    widget.bind("<FocusIn>", on_focus_in)
    widget.bind("<FocusOut>", on_focus_out)

    # Set initial placeholder
    if widget_class == tk.Entry:
        widget.insert(0, placeholder)
        widget.config(fg="grey")
    elif widget_class == tk.Text:
        widget.insert("1.0", placeholder)
        widget.config(fg="grey")

    return widget

# --- Create the form ---
states = add_label_widget(0, "States (comma separated):", width=40,  placeholder="q0, q1, q2, q3, q4")
alphabet = add_label_widget(1, "Alphabet (comma separated):", width=40, placeholder="0, 1, a, b")
transitions = add_label_widget(2, "Transitions (one per line):", widget_class=tk.Text, height=6, width=40, placeholder="q0, 0=q1\nq1, 1=q2\nq2, a=q3\nq3, b=q4")
initial_state = add_label_widget(3, "Initial State:", width=40,  placeholder="q0")
final_states = add_label_widget(4, "Final States (comma separated):", width=40, placeholder="q4")
input_string = add_label_widget(5, "Input String:", width=40, placeholder="01ab")

# --- Run button ---
run_button = tk.Button(frame, text="Run DFA", command=run_dfa_button)
run_button.grid(row=6, column=0, columnspan=2, pady=10)

# --- Result label ---
automat_label = tk.Label(
    frame,
    text="",
    justify="left",
    wraplength=600,   
    anchor="w"        
)
automat_label.grid(row=7, column=0, columnspan=2, pady=10)

result_label = tk.Label(
    frame,
    text="",
    justify="left",
    wraplength=600,   
    anchor="w"        
)
result_label.grid(row=8, column=0, columnspan=2, pady=10)



room.mainloop()


