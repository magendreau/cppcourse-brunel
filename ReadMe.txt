Program presentation:

This program allows us to make a model of a neuron and its interactions with the rest of the brain and other neurons. Each neuron has some features that determine its action and reaction. There are two types of neurons considered: some excitatory and some inhibitory. Both are described in the same way apart from their type which is either excitatory or inhibitory (attribute of the class neuron).
There also is a class Network which models a network in the brain with all neurons. It allows to create random connections between synapses and neurons that will interact with each other (inhibition or activation). 
Neurons can be in the refractory state so they have a membrane potential equal to 0, or spiking so a spike is emitted at a time t.
In all other cases the membrane potential increases also with the random noise background coming from the rest of the brain. Neurons that receive a stimulation (spike) respond after a delay.

Compilation and running:

The program can be compiled with cmake as a CmakeList is provided and in the terminal in the right repertory write:
" cmake .
  make
  ./Neuron "
to run the program; if python and jupyter are present on the computer at the end of the execution a graph will open to show how spikes of the neurons are modelled.
To create the doxygen file type in the terminal:
" doxygen -g Doxyfile.in
  doxygen Doxyfile.in
  make
  make doc "
And finally, to run the tests with unittest:
" make
  ./Neuron_unittest "

My program is a bit slow for the update part of the main and there are too many spikes for the graphs.

Using the program:

Four graphs are proposed:
- to generate graph (a):
	etha=2.0 and g=3.0
	in the pythonScript.py change the value of the limit for the y axis to 10000
- to generate graph (b):
	etha=4.0 and g=6.0
	in the pythonScript.py change the value of the limit for the y axis to 2000
- to generate graph (c):
	etha=2.0 and g=5.0
	in the pythonScript.py change the value of the limit for the y axis to 1000
- to generate graph (d):
	etha=0.9 and g=4.5
	in the pythonScript.py change the value of the limit for the y axis to 800
