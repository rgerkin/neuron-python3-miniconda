# Adapted from https://neuron.yale.edu/neuron/static/docs/neuronpython/firststeps.html
from neuron import h
h.load_file('stdrun.hoc')
soma = h.Section(name='soma')
soma.insert('pas')
asyn = h.AlphaSynapse(soma(0.5))
asyn.onset = 20
asyn.gmax = 1
h.psection()
v_vec = h.Vector()             # Membrane potential vector
t_vec = h.Vector()             # Time stamp vector
v_vec.record(soma(0.5)._ref_v)
t_vec.record(h._ref_t)
h.tstop = 40.0
h.run()
# Pickle
import pickle
with open('t_vec.p', 'w') as t_vec_file:
    pickle.dump(t_vec.to_python(), t_vec_file)
with open('v_vec.p', 'w') as v_vec_file:
    pickle.dump(v_vec.to_python(), v_vec_file)
