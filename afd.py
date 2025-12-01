ACCEPTED = 0
SYMBOL_ERROR = 1
STATE_ERROR = 2
NOT_FINAL_ERROR = 3

class DFA ():

    def __init__(self, states, alphabet, transitions, initial_state, final_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.initial_state = initial_state
        self.final_states = final_states


    def validate_input(self, input_string):
        current_state = self.initial_state
        state_steps = [current_state]
        
        for symbol in input_string:
            if symbol not in self.alphabet:
                return SYMBOL_ERROR, state_steps
            
            
            current_state = self.transitions[current_state][symbol]
            
            if current_state is None:
                return STATE_ERROR, state_steps
            
            state_steps.append(current_state)
        
        if current_state not in self.final_states:
            return NOT_FINAL_ERROR, state_steps
        

        return ACCEPTED, state_steps

