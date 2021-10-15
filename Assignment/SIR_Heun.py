import numpy as np
import matplotlib.pyplot as plt
# Time unit: 1 h
β = 10./(40*8*24)
γ = 3./(15*24)
dt = 10 # 6 min
D = 30 # Simulate for D days
N_t = int(D*24/dt) # Corresponding no. of time steps
t = np.linspace(0, N_t*dt, N_t+1)
S = np.zeros(N_t+1)
I = np.zeros(N_t+1)
R = np.zeros(N_t+1)
S_heun = np.zeros(N_t+1)
I_heun = np.zeros(N_t+1)
R_heun = np.zeros(N_t+1) 
# Initial conditions
S[0] = 50
S_heun[0] = 50
I[0] = I_heun[0] = 1
R[0] = R_heun[0] = 0
#differential equations
def diff_susceptible(S, I):
    return -β*S*I

def diff_infectious(S,I):
    return β*S*I - γ*I

def diff_recovered(I):
    return γ*I

# Step equations forward in time
for n in range(N_t):
    S[n+1] = S[n] + dt*diff_susceptible(S[n], I[n])
    I[n+1] = I[n] + dt*diff_infectious(S[n], I[n])
    R[n+1] = R[n] + dt*diff_recovered(I[n])

# Step equations heun
for n in range(N_t):
    #next y = current y + half_timestep * (differentiated_current+approx_differentiated_next)
    #y[i+1] = y[i] + (h/2)*(y'(x[i],y[i]) + y'(x[i]+h,y[i]+h*y'(x[i],y[i])))
    S_diff_n = diff_susceptible(S_heun[n], I_heun[n])
    I_diff_n = diff_infectious(S_heun[n], I_heun[n])
    R_diff_n = diff_recovered(I_heun[n])
    S_diff_next = diff_susceptible(S_heun[n]+dt*S_diff_n, I_heun[n]+dt*I_diff_n)
    I_diff_next = diff_infectious(S_heun[n]+dt*S_diff_n, I_heun[n]+dt*I_diff_n)
    R_diff_next = diff_recovered(I_heun[n]+dt*I_diff_n)
    S_heun[n+1] = S_heun[n] + (dt/2)*(S_diff_n+S_diff_next)
    I_heun[n+1] = I_heun[n] + (dt/2)*(I_diff_n+I_diff_next)
    R_heun[n+1] = R_heun[n] + (dt/2)*(R_diff_n+R_diff_next)


fig = plt.figure()
l1, l2, l3, l4, l5, l6 = plt.plot(t, S, t, I, t, R, t, S_heun, t, I_heun, t, R_heun)
fig.legend((l1, l2, l3, l4,l5,l6), ('S', 'I', 'R', 'S_heun', 'I_heun', 'R_heun'), 'center right')
plt.xlabel('hours')

plt.savefig('tmp.svg')
plt.show()

