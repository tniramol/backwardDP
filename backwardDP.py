import numpy as np
N = 5 #timestep size
target = 8
t = {i: {} for i in range(N+1)}
u = []
w = np.array([0,1,2,1,0])
    

#terminal
S = {}
for s in range(6,9,1):
        S[s] = {-0.2*(s-target)**2}
        
        
t[N]['J'] = S
print(t)
print(t[5]['J'][6])