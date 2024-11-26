# **The Asymmetric Simple Exclusion Process**

The Asymmetric Simple Exclusion Process (ASEP) is a one-dimensional interacting particle system in physics first introducted in 1970 by Frank Spitzer. Currently it serves as the default model for transport dynamics in stochastic models.

Consider the integer line ℤ and initially fix a finite number of particles on it with locations $x_1 < ... < x_N$. Each particle waits a random amount of time having the distribution of an exponential random variable with mean one and then attempts a jump, one site to the right with probability p and one site to the left with probability q, where $p+q=1$. However, if two particles are neighbouring eachother then the left particle cannot jump to the right and the right particle cannot jump to the left, this is called the simple exclusion condition. Every particle $x_i$ evolves according to the above rules independently of eachother. For $p \neq q$ the system is asymmetric.

To learn more about The Asymmetric Simple Exclusion Process please see the oringial 1970 scientific paper, *Interaction of Markov Processes* by Frank Spitzer.

[1970 Frank Spitzer.](https://www.sciencedirect.com/science/article/pii/0001870870900344?via%3Dihub)
___

# **About this code**
The following file contains code to simulate The Asymmetric Simple Exclusion Process.

- ASEP_simulation.py
___

# **Pip Install Packages**
The following needs to be installed for the code to run.
- numpy
- matplotlib
___

# **Explanation of Files and Output**

**1. <u> ASEP_simulation.py** </u>\
Run this file to simulate The Asymmetric Simple Exclusion Process. There are four parameters to fix:


* The probability to hop to the right: p
* The probability to hop to the left: q
* The initial state $x_1<...<x_N$: np.array(range($x_1$, $x_N$ ))
* The time of simulation: T

Output data:
* A space-time diagram showing the evolution of the initial state $x_1<...<x_N$ over time $T$.

