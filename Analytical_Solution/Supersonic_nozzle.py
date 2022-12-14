# =======================================================================#
#  SORBONNE UNIVERSITY: Fluid Mechanics masters, 			 #
#	        	major: Aerodynamics & Aeroacoustics		 #
#									 #
#  SUPERSONIC Solver : Analytical solution of supersonic nozzle flow     #
#  ----------------------------------------------------------------------#
#                                                                        #
#  Released: 2022 (Louneas ZEMMOUR, 2022)                                #
#  Library used:  PYLIB_MFC by J-C Chassain (Sorbonne University)        #
#                                                                        #
#                                                                        #
# REFERENCES                                                             #
# ----------                                                             #
# [1] J.-C. Chassaing, Class Notebooks in Compressible flows,            #
#     Master in Fluid Mechanics, Sorbonne Université, March 2021         #
# [2] J.D. Anderson, "Modern Compressible				 #
#                     Flow with Historical Perspective,			 #
#     Third Edition", McGRAW-HILL Ed.,ISBN 0-07-112161-7, 2003           #
#                                                                        #
# Send bug reports to : louenas.zemmour@etu.sorbonne-universite.fr       #
# =======================================================================#

#	Importing the needed librairies: 
import os, sys
sys.path.append('src')

from pylib_mfc import *
import numpy as np 
from pylab import * 
from scipy.optimize import fsolve
from geometry import *

# 		=======================
#		1) Defining the parameters: 
#		=======================

# Geometry
L       = 1.3557 		# Nozzle lenght
W       = 0.1 			# Nozzle width 
x	= np.linspace(0, L, 1001)
yup	= upperwall(x)		# Upper wall 
yd	= -upperwall(x)		# Lower wall
yth	= 0.1405		# Throat section radius
Anoz	= (yup - yd)*W		# Section area 
Ath	= 2*yth*W 		# Throat area (critical area in this case)
xth	= 0.8081		# Position of the throat

# Physical properties 
r 	   = 287		# Air specific constant
gamma   = 1.4  			# Specific heat coef ratio
nu	= 1e-5
Pa     = 1e5 			# Ambiant pressure
Pt0    = 842787			# Pressure in the combustion chamber
Tt0    = 500			# Temperature in the combustion chamber
Rho_t0 = Pt0 / (r*Tt0)		# Air density in the combustion chamber

#		======================
#	2) Computing the physical properties at each secion:
#		======================

# Mach number
A_Ac = Anoz / Ath

M = np.zeros(len(A_Ac))
for i in range(len(A_Ac)):
	if(x[i] < xth):
		init_M0 = 0.2
		val	= fsolve(func_A_Ac, init_M0, args=(gamma,A_Ac[i]))
		M[i]	= val[0]
	elif(x[i] >xth):
		init_M0 = 1.5
		val	= fsolve(func_A_Ac, init_M0, args=(gamma,A_Ac[i]))
		M[i]	= val[0]

# Static pressure:
Pt_P = func_Pt_P(gamma, M) 
P = Pt0 / Pt_P 

# Temperature:
Tt_T = func_Tt_T(gamma, M)
T = Tt0 / Tt_T

# Density:
Rho = P/(r*T)

# Speed of sound
a = np.sqrt(gamma*r*T) 

# Velocity:
U = M*a 

# Reynolds number based on nozzle section diameter:
Re = (U*yup*2)/nu 

outfile = open("exact.dat", "w") 
outfile.write("# x, M, P, T, rho" + '\n')
for i in range(len(x)):
	results = "%s, %s, %s, %s, %s" % (x[i],M[i],P[i],T[i],Rho[i])
	outfile.write(results + '\n')
outfile.close()
