import numpy as np
import matplotlib.pyplot as plt

start = -np.pi
stop = np.pi

b = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

""" start = 0
stop = 100
dt = 0.01
steps = (stop-start)/dt
t = np.linspace(start, stop, dt) #time
b = np.zeros(steps)
 """


def sinesum(t,b):
    sum = np.zeros(len(t))
    for i in range(1,len(t)+1):
        print(i)
        sum[i-1] += sum[:i-1].sum() + b[i-1]*np.sin(i*t[i-1])
        print(sum[i-1])
    return sum

def test_sinesum():
    t = np.array([-np.pi*0.5, np.pi*0.25])
    steps = 2
    b = np.array([4,-3])
    test = sinesum(t,b)
    print(f'{test = }')
    test_sum = test[-1]
    print(f'{test_sum = }')
    if test_sum == -7:
        return True
    else:
        return False

def plot_compare(f,N,M):
    """
    f is the analytic function
    N is the number of summing terms
    M is the number of time coordinates
    """
    dt = (stop-start)/M
    t = np.linspace(start,stop,M)
    analytic = np.zeros(M)
    numeric = sinesum(t, b)
    print(len(analytic), len(numeric), len(t))
    for i in range(N):
        analytic[i] += f(t[i])


    fig = plt.figure()
    l1, l2 = plt.plot(t, analytic, t, numeric)
    fig.legend((l1, l2), ('analytic', 'numeric'))
    plt.xlabel('time')
    plt.show()

def error(b, f, M):
    return 0

def function(t):
    return np.sin(t)


if __name__ == "__main__":
    test_sinesum()
    plot_compare(function,10,11)