from random import random
from numpy import mean, std, var, float64

# Automata for 'HTT'
# This should be an algorithm that creates the automata given string
automata = dict()
automata[('q0','-')] = 'q0'
automata[('q0','H')] = 'q1'
automata[('q0','T')] = 'q0'
automata[('q1','H')] = 'q1'
automata[('q1','T')] = 'q2'
automata[('q2','H')] = 'q1'
automata[('q2','T')] = 'qf'

# Experiment #1
experiments = 20000
HTT = []

for exp in range(experiments):
    state = ('q0','-')
    steps = 0
    while automata[state] != 'qf':
        steps += 1
        coin = 'H' if random() < 0.5 else 'T'       
        state = (automata[state], coin)
    HTT.append(steps)
    
print("HTT: ",mean(HTT), var(HTT))
    
# Automata for 'HTH'
# This should be an algorithm that creates the automata given string

automata = dict()
automata[('q0','-')] = 'q0'
automata[('q0','H')] = 'q1'
automata[('q0','T')] = 'q0'
automata[('q1','H')] = 'q1'
automata[('q1','T')] = 'q2'
automata[('q2','H')] = 'qf'
automata[('q2','T')] = 'q0'

# Experiment #1
experiments = 200000
HTH = []

for exp in range(experiments):
    state = ('q0','-')
    steps = 0
    while automata[state] != 'qf':
        steps += 1
        coin = 'H' if random() < 0.5 else 'T'       
        state = (automata[state], coin)
    HTH.append(steps)
    
print('HTH: ',mean(HTH, dtype=float64), var(HTH, dtype=float64))
