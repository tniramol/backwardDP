import numpy as np
import itertools

def performance_idx(combo, terminal):
    """Performance Index function (J)"""
    for sub_t in terminal:
        if combo[1] == sub_t[1]:
            energy_related = energy_func(combo[0][0],combo[0][1])
            return energy_related - sub_t[2]

def calculate_possible_state(state_func, t_next, *sets):
    combinations = itertools.product(*sets)
    S_min = min(sub_t[0][0] for sub_t in t_next)
    S_max = max(sub_t[0][0] for sub_t in t_next)
    results = [[(combination), state_func(*combination)] for combination in combinations]
    
    filtered_results = [result for result in results if S_min <= result[1] <= S_max]
    return filtered_results


def state_func(*args):
    return np.sum(args)

def energy_func(*args):
    return 0.1 * args[0] * args[1]


def main():
    #initialization
    N = 5 #timestep size
    target = 8
    t = [None]*(N+1)
    S = []
    u = []
    w = np.array([0,1,2,1,0])
    
    
    

    #terminal
    for s in range(6,9,1):
        S.append([(s,None,None),s,-0.2*(s-target)**2])
    t[N] = S
    print(t)
    #iteeration
    for k in range(N-1, -1, -1):

        #constraints
        S_min = 3
        S_max = 8
        S_step = 1
        u_min = 0
        u_max = 2
        u_step = 1
        w_min = w[k]
        w_max = w[k]
        w_step = 1

        print("k=",k)
        S_k = np.arange(S_min, S_max+1, S_step)
        u_k = np.arange(u_min, u_max+1, u_step)
        w_k = np.arange(w_min, w_max+1, w_step)
        print(S_k, S_min, S_max)
        possible_state_combo = calculate_possible_state(state_func, t[k+1], S_k, -1*u_k, w_k)
        performance_state_combo = possible_state_combo.copy()
        for i, combo in enumerate(possible_state_combo):
            performance_state_combo[i].append(performance_idx(combo, t[k+1]))
        t[k] = performance_state_combo
        print("t(k)=",t[k])
        print("-----"*10)
        

# Check if this file is run as the main program
if __name__ == "__main__":
    main()