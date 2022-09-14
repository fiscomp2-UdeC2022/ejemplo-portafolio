"""Copyright (c) 2022 Dr. Roberto Navarro <roberto.navarro@udec.cl>

Este script calcula integrales de la forma
.. math::
    I_n = \int_0^1 dx x^n \sin x

Para ello, se usan dos estrategias, una basada en la regla trapezoidal
y otra en una relación de recurrencia.
"""

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(4, 3))
# Numero de integrales I0, I1, ..., IN
N = 11


################################################################################
# (A) Relación de recurrencia
#     I_n = n*\sin(1) - \cos(1) - n*(n-1)*I_{n-2}
#
#    donde I_0=1-\cos(1) e I_1=\sin(1)-\cos(1).

# siempre es bueno pre-calcular funciones
cos1 = np.cos(1)
sin1 = np.sin(1)

# reserva memoria para los N valores I0, I1, ..., IN
In = np.zeros(N)

# evalua las semillas para la relacion de recurrencia
In[0] = 1 - cos1
In[1] = sin1 - cos1

# evalua I_n para n>1
for n in range(2,N):
    In[n] = n*sin1 - cos1 - n*(n-1)*In[n-2]


# grafica los resultados con circulos
plt.plot(In, 'o', label="Series")

# notar que no se usa plt.show() aun
# esto para crear un solo grafico del resultado de ambos metodos


################################################################################
# (B) La regla trapezoidal
#    .. math::
#        I_n \approx (1/N) [ (f_0 + f_1)/2 + \sum_{k=1}^N f_k
#
#    donde f_k = f(x_k) y x_k=k/N, con f(x) = sin(x) x^n.

# elige Nx valores entre 0 < x < 1
Nx = 100
x = np.linspace(0, 1, Nx)  

# guarda el valor de sin(x) para no volver a evaluarlo
sinx = np.sin(x)

# reserva memoria para evaluar I0, I1, ..., IN
In_trapz = np.zeros(N)

# para cada n, usa regla trapezoidal
for n in range(N):
    f = sinx * x**n             # evalua integrando

    In_trapz[n] = (0.5*(f[0] + f[-1]) + np.sum(f[1:-1])) / Nx


# grafica los resultados
plt.plot(In_trapz, 'x', label="Trapezoide")


# configura el grafico
plt.xlabel(r"$n$")
plt.ylabel(r"$I_n$")
plt.legend()
plt.tight_layout()

plt.savefig("In_series_trapz.pdf", bbox_inches='tight')
# plt.show()

# plt.plot(In-In_trapz)
# plt.show()
