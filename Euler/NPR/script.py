#=======================================================================#
#									#
#	Script to extrac data from files				#
#	and plot the data       					#
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
#       2) NPR = 1.3
#	===============
	
infile = open("npr_1p3.csv", 'r')
m = 0
for line in infile:
    m += 1

infile.close()
x_3 = np.zeros(m-1)
M_3 = np.zeros(m-1)
T_3 = np.zeros(m-1)
P_3 = np.zeros(m-1)
r_3 = np.zeros(m-1)


infile = open("npr_1p3.csv", 'r')
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
#       3) npr_1p4
#	===============

infile = open("npr_1p4.csv", 'r')
m = 0
for line in infile:
    m += 1

infile.close()
x_4 = np.zeros(m-1)
M_4 = np.zeros(m-1)
T_4 = np.zeros(m-1)
P_4 = np.zeros(m-1)
r_4 = np.zeros(m-1)

infile = open("npr_1p4.csv", 'r')
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
#       4) npr = 1.5
#	===============

infile = open("npr_1p5.csv", 'r')
m = 0
for line in infile:
    m += 1

infile.close()
x_5 = np.zeros(m-1)
M_5 = np.zeros(m-1)
T_5 = np.zeros(m-1)
P_5 = np.zeros(m-1)
r_5 = np.zeros(m-1)


infile = open("npr_1p5.csv", 'r')
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
#       5) npr = 1.6
#	===============

infile = open("npr_1p6.csv", 'r')
m = 0
for line in infile:
    m += 1

infile.close()
x_6 = np.zeros(m-1)
M_6 = np.zeros(m-1)
T_6 = np.zeros(m-1)
P_6 = np.zeros(m-1)
r_6 = np.zeros(m-1)


infile = open("npr_1p6.csv", 'r')
i = 0
infile.readline()
for line in infile:
    data = line.split(',')
    x_6[i] = float(data[-3])
    M_6[i] = float(data[0])
    P_6[i] = float(data[5])
    T_6[i] = float(data[1]) 
    i += 1
    
infile.close()


#	===============
#       6) npr = 1.7
#	===============

infile = open("npr_1p7.csv", 'r')
m = 0
for line in infile:
    m += 1

infile.close()
x_7 = np.zeros(m-1)
M_7 = np.zeros(m-1)
T_7 = np.zeros(m-1)
P_7 = np.zeros(m-1)
r_7 = np.zeros(m-1)


infile = open("npr_1p7.csv", 'r')
i = 0
infile.readline()
for line in infile:
    data = line.split(',')
    x_7[i] = float(data[-3])
    M_7[i] = float(data[0])
    P_7[i] = float(data[5])
    T_7[i] = float(data[1]) 
    i += 1
    
infile.close()

#	===============
#       7) npr = 1.8
#	===============

infile = open("npr_1p8.csv", 'r')
m = 0
for line in infile:
    m += 1

infile.close()
x_8 = np.zeros(m-1)
M_8 = np.zeros(m-1)
T_8 = np.zeros(m-1)
P_8 = np.zeros(m-1)
r_8 = np.zeros(m-1)


infile = open("npr_1p8.csv", 'r')
i = 0
infile.readline()
for line in infile:
    data = line.split(',')
    x_8[i] = float(data[-3])
    M_8[i] = float(data[0])
    P_8[i] = float(data[5])
    T_8[i] = float(data[1]) 
    i += 1
    
infile.close()

#	===============
#       8) Plots
#	===============

# Plot data:
plt.plot(x_3, P_3, label="NPR=1.3")
plt.plot(x_4, P_4, label="NPR=1.4")
plt.plot(x_5, P_5, label="NPR=1.5")
plt.plot(x_6, P_6, label="NPR=1.6")
plt.plot(x_7, P_7, label="NPR=1.7")
plt.plot(x_8, P_8, label="NPR=1.8")

plt.xlabel("x position")
plt.ylabel("Pressure distribution")
plt.grid(True)
plt.legend()
plt.show()
