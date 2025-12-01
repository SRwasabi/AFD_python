def concatenating(transitions_dict):
    for state in list(transitions_dict.keys()):
        for symbol in list(transitions_dict[state].keys()):
            concatenated_states = transitions_dict[state][symbol]
            concatenated_states.sort()
            concatenated = "".join(concatenated_states)
            transitions_dict[state][symbol] = concatenated



def convert(transitions_dict, final_states_list, states_list):
    stop = True

    for state in list(transitions_dict.keys()):
        for symbol in list(transitions_dict[state].keys()):
            concatenated_states = transitions_dict[state][symbol]
            concatenated_states.sort()

            if isinstance(concatenated_states, str):
                concatenated_states = [concatenated_states]

            concatenated = "".join(concatenated_states)

            if concatenated not in transitions_dict:
                transitions_dict[concatenated] = {}

            for sub_states in concatenated_states:
                for sub_symbols, next_states in transitions_dict[sub_states].items():
                    for next_state in next_states:
                        add_transitions(concatenated, sub_symbols, next_state, transitions_dict)

            if any(possible_state in final_states_list for possible_state in concatenated_states) and concatenated not in final_states_list:
                final_states_list.append(concatenated)


            if concatenated not in states_list:
                states_list.append(concatenated)
                stop = False

    return stop



def get_initial_transitions(transitions_input, transitions_dict):
    for line in transitions_input:
        parts = line.split('=')
        if len(parts) == 2:
            left, right = parts
            state_symbol = left.strip().strip().split(',')
            
            if len(state_symbol) == 2:
                state = state_symbol[0].strip()
                symbol = state_symbol[1].strip()
                next_state = right.strip()
                add_transitions(state, symbol, next_state, transitions_dict)


def add_transitions(state, symbol, next_state, transitions_dict):
    if state not in transitions_dict:
        transitions_dict[state] = {}

    if symbol in transitions_dict[state]:
        if next_state not in transitions_dict[state][symbol]:
            transitions_dict[state][symbol].append(next_state)
            transitions_dict[state][symbol].sort()

    else:
        transitions_dict[state][symbol] = [next_state]

