class AFD ():

    states = []
    alphabet = []
    transitions = {} #nested dictionary
    initial_state = None
    final_states = []

    def __init__(self, states, alphabet, transitions, initial_state, final_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.initial_state = initial_state
        self.final_states = final_states


    def validate_input(self, input_string):
        current_state = self.initial_state

        for symbol in input_string:
            print(f"Current State: {current_state}")
            if symbol not in self.alphabet:
                return False
            
            current_state = self.transitions.get((current_state, symbol))
            if current_state is None:
                return False
        
        if current_state not in self.final_states:
            return False
        
        return True
            

    def run_afd (self):
        input_string = input("Enter the input string: ")

        status = self.validate_input(input_string)

        if status == False:
            print("The input string is not valid.")
            return