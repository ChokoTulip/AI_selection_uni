
import numpy as np
import random
# obousmerna fronta - deque
from collections import deque


def diffevol(func, dim, lim, NP, F, CR, max_iter, max_iter_eps, epsilon):
    """
    Differential Evolution
    https://en.wikipedia.org/wiki/Differential_evolution
    :param func: objective function
    :param dim: problem dimension
    :param lim: limits - 2 values
    :param NP: population size
    :param F: differential weight 0 <= F <= 2
    :param CR: crossover probability 0 <= CR <= 1
    :param max_iter: maximum number of iterations
    :param max_iter_eps: maximum number of iterations where fval
                         does not change by epsilon
    :param epsilon: value for max_iter_eps
    :return: x_out:vector, fval:function value in x_out
    """
    # choice cache - mas mnozinu vsech mnozin 1-n, kde chybi prvek J,
    # protoze vybiras 3 prvky, ktere se lisi od aktual. prvku
    choices_cache = [set(range(NP)) - {j} for j in range(NP)]
    # init solution

    # od, do, (NP,dim)- NP radku, dim sloupcu
    x = np.random.uniform(lim[0], lim[1], (NP, dim))
    y = np.zeros((NP, dim))  # trials
    fx = func(x)

    # double ended queue, max kapacita = jednosmerna fronta - prekrocis kapacitu, prvek vzpadava
    fval_hist = deque(maxlen=max_iter_eps)

    for iter in range(1, max_iter+1):
        fval_idx = np.argmin(fx)  # index of best agent
        fval = fx[fval_idx]
        x_out = x[fval_idx, :]  # vsechny sloupce
        print('fval: ', fval)
        fval_hist.append(fval)
        if len(fval_hist) == fval_hist.maxlen:
            max_diff = np.max(np.abs(np.diff(fval_hist)))
            if max_diff < epsilon:
                break

        # neni vcetne last prvku (dim)
        R = np.random.randint(0, dim, NP)
        r = np.random.uniform(0, 1, (NP, dim))
        y[:, :] = x[:, :]  # pro kopirovani na pametova mista bez alokace. predpokladas, ze nedoslo ke crossoveru
        for j in range(NP):  # for each agent x in population:
            # picking 3 agents
            a_idx, b_idx, c_idx = random.sample(choices_cache[j], 3)  # unpacking = when na prave strane iterable, leva strana se postupne naplni
            a = x[a_idx, :]; b = x[b_idx, :]; c = x[c_idx, :];
            for i in range(dim):
                if r[j, i] < CR or i is R[j]:  # crossover
                    d_i = a[i] + F * (b[i] - c[i])
                    if lim[0] <= d_i <= lim[1]:
                        y[j, i] = d_i
                    else:
                        y[j, i] = np.random.uniform(lim[0], lim[1])
        fy = func(y)
        is_better = fy < fx  # vektor true, falsu
        fx[is_better] = fy[is_better]
        x[is_better, :] = y[is_better, :]

    print('terminated after iteration: ', iter)

    return x_out, fval
