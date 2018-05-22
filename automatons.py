from automaton import machines
#references:
#    https://pypi.org/project/automaton/
#    https://docs.openstack.org/automaton/latest/user/examples.html
states = ['q0', 'q1', 'q2', 'q3', 'q4',
        'q5','q6', 'q7', 'q8', 'q9',
        'q10', 'q11', 'q12', 'q13', 'q14', 'q15',
        'q16', 'q17', 'q18', 'q19', 'q20', 'q21', 'q22', 'q23']

        #q6 final state
q = machines.FiniteMachine()
i = 0

while i<len(states):
    q.add_state(states[i])
    i = i+1

q.add_transition(states[0], states[1], 'f')
q.add_transition(states[0], states[2], 'r')
q.add_transition(states[0], states[3], 'e')
q.add_transition(states[0], states[4], 'p')
q.add_transition(states[0], states[5], 'i')
q.add_transition(states[1], states[7], 'o')
q.add_transition(states[2], states[12], 'a')
q.add_transition(states[3], states[14], 'l')
q.add_transition(states[4], states[9], 'o')
q.add_transition(states[4], states[15], 'r')
q.add_transition(states[5], states[19], 'm')
q.add_transition(states[5], states[17], 'n')
q.add_transition(states[5], states[6], 'f')
q.add_transition(states[7], states[6], 'r')
q.add_transition(states[8], states[6], 'e')
q.add_transition(states[9], states[6], 'p')
q.add_transition(states[10], states[6], 't')
q.add_transition(states[11], states[6], 'x')
q.add_transition(states[12], states[13], 'n')
q.add_transition(states[13], states[8], 'g')
q.add_transition(states[14], states[8], 's')
q.add_transition(states[15], states[16], 'i')
q.add_transition(states[16], states[10], 'n')
q.add_transition(states[17], states[22], 's')
q.add_transition(states[17], states[23], 'p')
q.add_transition(states[17], states[18], 'd')
q.add_transition(states[18], states[11], 'e')
q.add_transition(states[19], states[20], 'p')
q.add_transition(states[20], states[21], 'o')
q.add_transition(states[21], states[10], 'r')
q.add_transition(states[22], states[21], 'e')
q.add_transition(states[23], states[10], 'u')


q.default_start_state = 'q0'
print(q.pformat())
