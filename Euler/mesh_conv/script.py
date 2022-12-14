#=======================================================================#
#									#
#	Script to extrac data from files				#
#	Computes error and pltos data					#
#									#
#	Louenas Zemmour (2022)						#
#	Send bug reports to: louenas.zemmour@				#
#				etu.sorbonne-universite.fr		#
#									#
#=======================================================================#

# Import libraries
import numpy as np
import matplotlib.pyplot as plt 

#	===============
#    1)Read analytical data 
#	===============

infile = open("exact.dat", 'r')
m = 0
for line in infile:
    m += 1
print(m)
infile.close()
x_ex = np.zeros(m-1)
M_ex = np.zeros(m-1)
T_ex = np.zeros(m-1)
P_ex = np.zeros(m-1)
r_ex = np.zeros(m-1)


infile = open("exact.dat", 'r')
i = 0
infile.readline()
for line in infile:
    data = line.split(',')
    x_ex[i] = float(data[0])
    M_ex[i] = float(data[1])
    P_ex[i] = float(data[2])
    T_ex[i] = float(data[3])
    r_ex[i] = float(data[4])
    i += 1
    
infile.close()

#	===============
#    2) First mesh data
#	===============
	
infile = open("M_mesh_1.csv", 'r')
m = 0
for line in infile:
    m += 1

infile.close()
x_1 = np.zeros(m-1)
M_1 = np.zeros(m-1)
T_1 = np.zeros(m-1)
P_1 = np.zeros(m-1)
r_1 = np.zeros(m-1)


infile = open("M_mesh_1.csv", 'r')
i = 0
infile.readline()
for line in infile:
    data = line.split(',')
    x_1[i] = float(data[-3])
    M_1[i] = float(data[0])
    P_1[i] = float(data[5])
    T_1[i] = float(data[1]) 
    i += 1
    
infile.close()

#	===============
#    3) Second Mesh data
#	===============

infile = open("M_mesh_2.csv", 'r')
m = 0
for line in infile:
    m += 1

infile.close()
x_2 = np.zeros(m-1)
M_2 = np.zeros(m-1)
T_2 = np.zeros(m-1)
P_2 = np.zeros(m-1)
r_2 = np.zeros(m-1)


infile = open("M_mesh_2.csv", 'r')
i = 0
infile.readline()
for line in infile:
    data = line.split(',')
    x_2[i] = float(data[-3])
    M_2[i] = float(data[0])
    P_2[i] = float(data[5])
    T_2[i] = float(data[1])
    i += 1
    
infile.close()

#	===============
#    4) Third Mesh data
#	===============

infile = open("M_mesh_3.csv", 'r')
m = 0
for line in infile:
    m += 1

infile.close()
x_3 = np.zeros(m-1)
M_3 = np.zeros(m-1)
T_3 = np.zeros(m-1)
P_3 = np.zeros(m-1)
r_3 = np.zeros(m-1)


infile = open("M_mesh_3.csv", 'r')
i = 0
infile.readline()
for line in infile:
    data = line.split(',')
    x_3[i] = float(data[-3])
    M_3[i] = float(data[0])
    P_3[i] = float(data[5])
    T_3[i] = float(data[1]) 
    i += 1
    
infile.close()

#	===============
#    5) Fourth Mesh data
#	===============

infile = open("M_mesh_4.csv", 'r')
m = 0
for line in infile:
    m += 1

infile.close()
x_4 = np.zeros(m-1)
M_4 = np.zeros(m-1)
T_4 = np.zeros(m-1)
P_4 = np.zeros(m-1)
r_4 = np.zeros(m-1)


infile = open("M_mesh_4.csv", 'r')
i = 0
infile.readline()
for line in infile:
    data = line.split(',')
    x_4[i] = float(data[-3])
    M_4[i] = float(data[0])
    P_4[i] = float(data[5])
    T_4[i] = float(data[1]) 
    i += 1
    
infile.close()


#	===============
#    6) Fifth Mesh data
#	===============

infile = open("M_mesh_5.csv", 'r')
m = 0
for line in infile:
    m += 1

infile.close()
x_5 = np.zeros(m-1)
M_5 = np.zeros(m-1)
T_5 = np.zeros(m-1)
P_5 = np.zeros(m-1)
r_5 = np.zeros(m-1)


infile = open("M_mesh_5.csv", 'r')
i = 0
infile.readline()
for line in infile:
    data = line.split(',')
    x_5[i] = float(data[-3])
    M_5[i] = float(data[0])
    P_5[i] = float(data[5])
    T_5[i] = float(data[1]) 
    i += 1
    
infile.close()


#	===============
#	6) Errors and plots
#	===============

# Compute the relative errors
#err1 = np.abs(M_1 - M_ex)/M_ex
#err2 = np.abs(M_2 - M_ex)/M_ex
#err3 = np.abs(M_3 - M_ex)/M_ex
#err4 = np.abs(M_4 - M_ex)/M_ex

# Plot data:
plt.plot(x_ex, M_ex, label="Analytical solution")
plt.plot(x_1, M_1, label="Mesh 1")
plt.plot(x_5, M_5, label="Mesh 5")
#plt.plot(x_3, M_3, label="Mesh 3")
#plt.plot(x_4, M_4, label="Mesh 4")
plt.xlabel("x position")
plt.ylabel("Mach number")
plt.legend()
plt.show()
