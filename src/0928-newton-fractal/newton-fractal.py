"""Copyright (c) 2022 Dr. Roberto Navarro <roberto.navarro@udec.cl>

Este script grafica el fractal de Newton para polinomios de la forma z**N==1, el cual tiene N soluciones complejas de modulo unitario si N es entero. 

El fractal se construye resolviendo z**n==1 usando el metodo de
Newton-Raphson:

  z[i+1] = z[i] - f(z[i]) / f'(z[i])

En este caso, f(z)=z**n-1, por lo que el metodo se reduce a:
  
  z[i+1] = z[i] * (1-1/N) + z[i]**(1-N) / N

Dependiendo de la semilla inicial z[0], el metodo convergera solo a una de las N soluciones. Asi, el objetivo es estudiar como converge el metodo dependiendo de z[0] en el plano complejo. 
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

def newton(semilla, N=3, maxerr=1e-3):
    z   = semilla
    err = maxerr+1
    it = 0
    while np.abs(err)>maxerr:
        err = (z-z**(1-N)) / N
        z = z - err
        it = it + 1

    return z, it
    

xmin, xmax = -2, 2
ymin, ymax = -2, 2

Nx, Ny = 512, 512

sol = np.array([[ newton(semilla=complex(xi,yi), N=3)
                  for yi in np.linspace(ymin, ymax, Ny)]
                for xi in np.linspace(xmin, xmax, Nx)])

z = sol[:,:,0]
it = sol[:,:,1].real


fig, ax = plt.subplots(1,2, figsize=(8.6,4), sharey=True)

ang = ax[0].imshow(np.angle(z).T, extent=(xmin, xmax, ymin, ymax),
                   origin="lower", aspect="auto", cmap="viridis")

niter = ax[1].imshow(it.T, extent=(xmin, xmax, ymin, ymax),
                     origin="lower", aspect="auto", cmap="viridis" )


ax[0].set_ylabel(r"Im($z$)")

plt.colorbar(ang, ax=ax[0])
plt.colorbar(niter, ax=ax[1])

for a in ax:
    a.scatter(z.real, z.imag, color="red")
    a.set_ylim(ymin, ymax)
    a.set_xlim(xmin, xmax)
    a.set_xlabel(r"Re($z$)")

plt.tight_layout()
plt.show()
