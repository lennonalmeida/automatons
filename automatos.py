from automaton import machines
m = machines.FiniteMachine()
m.add_state('up')
m.add_state('down')
m.add_transition('down', 'up', 'jump')
m.add_transition('up', 'down', 'fall')
m.default_start_state = 'down'
print(m.pformat())
