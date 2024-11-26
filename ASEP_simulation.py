import numpy as np
import matplotlib.pyplot as plt

p=1
q=1
#state with occupations
state = np.array(range(-10,0))
#state = np.array(range(1))

#initial and final times
t = 0
T = 20

#fluc=[]
x_list=[]
t_list=[]

while t < T:

    #print(t)
    #print(state)
    #print((np.average(state)-10)/t**(1/3))

    #fluc.append((np.average(state)-state[0])/t**(1/3))
    #fluc.append((np.average(state)-20)/t**(1/2))
    x_list.append(list(np.transpose(state)))
    t_list.append(t)

    clocks = []

    for x in state:
        #left jumps
        #uniform random number 0<a<1
        al=np.random.random_sample()
        if q == 0:
            bl = 10**3
        else:
            bl = -1 * np.log(1-al)/q

        #right jumps
        #uniform random number 0<a<1
        ar=np.random.random_sample()
        if p == 0:
            br = 10**3
        else:
            br = -1 * np.log(1-ar)/p

        clocks.append([bl,br])

    #check for neighbouring particles on left
    exclude_left = []
    for i in range(len(state)-1):
        if state[i] == state[i+1]-1:
            exclude_left.append(i+1)


    #check for neighbouring particles on right
    exclude_right = []
    for i in range(len(state)-1):
        if state[i+1] == state[i]+1:
            exclude_right.append(i)

    #exclude the neightbouring particles from left jumping
    for i in exclude_left:
        [tl,tr] = clocks[i]
        tl = 10**3
        clocks[i] = [tl,tr]

    #exclude the neightbouring particles from right jumping
    for i in exclude_right:
        [tl,tr] = clocks[i]
        tr = 10**3
        clocks[i] = [tl,tr]

    #redefine clocks as a numpy array
    clocks = np.array(clocks)

    #find minimum jump time
    t_jump = np.amin(clocks)
    i = 0
    for x in clocks:
        if x[0] == t_jump:
            state[i] = state [i] - 1
        elif x[1] == t_jump:
            state[i] = state [i] + 1
        i = i+1

    #update time
    t = t + t_jump

#print(state)
#print(np.average(state))

#plt.scatter(t_list, fluc)
#plt.show()
x_list = np.transpose(x_list)

#print(x_list)

plt.figure()
for x in x_list:
    plt.plot(x,t_list,"r")
plt.xlabel("position")
plt.ylabel("time")
plt.title("Space-time ASEP Simulation")
plt.show()

print(state)
print(np.average(state)/T)
