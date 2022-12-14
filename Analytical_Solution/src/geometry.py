#=======================================================================#
#									#
#	Geometry.py: A library to compute the nozzle geometry		#
#-----------------------------------------------------------------------#
#									#
#	Released: 2022 (Louenas Zemmour, 2022)				#
#									#
#=======================================================================#

# Import the librairies

import numpy as np 
import matplotlib.pyplot as plt
#	================
#	1) Nozzle points
#	================
#
xa, ya = 0., 0.352
xb, yb = 0.2, 0.352
xc, yc = 0.4329, 0.2954
xd, yd = 0.705, 0.1552
xe, ye = 0.8081, 0.1405
xf, yf = 1.3557, 0.2468
#
#	================
#	2) Arcs centers
#	================
#
xg, yg = 0.2, -0.1559
xh, yh = 0.8081, 0.5094013605
#
#	================
#   3) Arcs radius and lines coeff
#	================
#
r1 =np.sqrt((xg - xb)**2 + (yg - yb)**2)
r2 =np.sqrt((xh - xe)**2 + (yh - ye)**2)
#
a1 = (yd - yc)/(xd - xc)
b1 = yd - xd*(yd - yc)/(xd - xc) 
#
a2 = (yf - ye)/(xf - xe)
b2 = yf - xf*(yf - ye)/(xf - xe)
#
#	================
#    4) Upper geom of nozzle
#	===============
#
def upperwall(x):
	y = np.zeros(len(x))
	for i in range(len(x)):
		if (x[i] <= xb):
			y[i]= ya
		elif(xb <= x[i] <= xc):
			y[i] = yg + np.sqrt(r1**2 - (x[i] - xg)**2) 
		elif(xc <= x[i] <= xd):
			y[i] = a1*x[i] + b1
		elif(xd <= x[i] <= xe):
			y[i] = yh - np.sqrt(r2**2 - (x[i] - xh)**2)
		elif(xe <= x[i] <= xf):
			y[i] = a2*x[i] + b2
	return y
#
#	End Library 
