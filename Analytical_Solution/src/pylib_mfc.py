# ===========================================================================
#                                                                           #
#  PYLIB_MFC : A simple collection of function solving compressible flows   #
#  ----------------------------------------------------------------------   #
#                                                                           #
#  Released: 2021b (J-C Chassaing, 2021)                                    #
#                                                                           #
#  Last mod. bug fixed in func_laval_isentropic and func_laval_massflow     #
#                                                                           #
#                                                                           #
# REFERENCES                                                                #
# ----------                                                                #
# [1] J.-C. Chassaing, Class Notebooks in Compressible flows,               #
#     Master in Fluid Mechanics, Sorbonne Université, March 2021            #
# [2] J.D. Anderson, "Modern Compressible Flow with Historical Perspective, #
#     Third Edition", McGRAW-HILL Ed.,ISBN 0-07-112161-7, 2003              #
#                                                                           #
# Send bugs : jean-camille.chassaing@sorbonne-universite.fr                 #
# ===========================================================================
from scipy.optimize  import fsolve
from pylab           import *
import               numpy as np

# =========================
# ISENTROPIC FLOW RELATIONS
# =========================
def func_Tt_T(gam,M):
    """Return the total to static temperature ratio given gamma and the Mach number"""
    out =  (1+0.5*(gam-1)*M**2)
    return out
#
def func_Pt_P(gam,M):
    """Return the total to static pressure ratio  given gamma and the Mach number"""
    out =  (1+0.5*(gam-1)*M**2)**(gam/(gam-1))
    return out
#
def func_Rt_R(gam,M):
    """Return the total to static density ratio  given gamma and the Mach number"""
    out =  (1+0.5*(gam-1)*M**2)**(1/(gam-1))
    return out
#
def func_inv_Tt_T(x,gam,Tt_T):
    """Implicit function used by fsolve to find the Mach number given the total to static temperature ratio """
    out =  Tt_T - (1+0.5*(gam-1)*x**2)
    return out
#
def func_inv_Pt_P(x,gam,Pt_P):
    """Implicit function used by fsolve to find the Mach number given the total to static pressure ratio """
    out =  Pt_P - (1+0.5*(gam-1)*x**2)**(gam/(gam-1))
    return out
#
def func_inv_Rt_R(x,gam,rt_r):
    """Implicit function used by fsolve to find the Mach number given the total to static density ratio """
    out =  rt_r - (1+0.5*(gam-1)*x**2)**(1/(gam-1))
    return out
#
def func_A_Ac(x,gam,A_Ac):
    """Implicit function used by fsolve to find the Mach number given the A/Ac ratio """
    out =  A_Ac - 1./x * ( 2./(gam+1.) *(1. + 0.5*(gam-1)*x**2))**(0.5*(gam+1)/(gam-1))  
    return out
#
def func_laval_isentropic(x, gam, r, m_dot, Tt0, Rt0, A):
    """Implicit function used by fsolve to find the Mach number given the test section and the massflow """
    c2= -0.5*(gam+1.)/(gam-1.)
    out =  m_dot - x * (1.+0.5*(gam-1)*x**2)**c2 * A * np.sqrt(gam*r*Tt0)*Rt0
    return out
#
def func_laval_massflow(gam, r, M, Tt0, Rt0, A):
    """Compute the massflow in a Laval nozzle given the Mach number at a given section and total quantities"""
    c2= -0.5*(gam+1.)/(gam-1.)
    out =  M * (1.+0.5*(gam-1)*M**2)**c2 * A * np.sqrt(gam*r*Tt0)*Rt0
    return out


# ===========================
# NORMAL SHOCK JUMP RELATIONS
# ===========================
def func_M2_jump(gam,M1):
    """Return the downstream Mach number across a normal shock given the upstream Mach number and gamma"""
    out =  np.sqrt((2+(gam-1)*M1**2)/(2*gam*M1**2+1-gam))
    return out
#
def func_jump_P(gam,M1):
    """Return the static pressure jump across a normal shock given the upstream Mach number and gamma"""
    out =  1 + 2*gam/(gam+1)*(M1**2-1.)
    return out
#
def func_jump_T(gam,M1):
    """Return the static temperature jump across a normal shock given the upstream Mach number and gamma"""
    out =  (1 + 2*gam/(gam+1)*(M1**2-1.)) / (( (gam+1)*M1**2)/((gam-1)*M1**2+2) )
    return out
#
def func_jump_rho(gam,M1):
    """Return the static density jump across a normal shock given the upstream Mach number and gamma"""
    out =  ( (gam+1)*M1**2)/((gam-1)*M1**2+2)
    return out
#
def func_inv_jump_P(x,gam,P2_P1):
    """Implicit function used by fsolve to compute the upstream Mach number of a normal shock, given the static pressure jump
       Input variables: 
         - Gamma  : polytropic coefficient
         - P2_P1  : Static pressure jump
    """
    out =  P2_P1 - (1 + 2*gam/(gam+1)*(x**2-1.))
    return out
#
def func_inv_jump_T(x,gam,T2_T1):
    """Implicit function used by fsolve to compute the upstream Mach number of a normal shock, given the static temperature jump
       Input variables: 
         - Gamma  : polytropic coefficient
         - T2_T1  : Static temperature jump
    """
    out =  T2_T1 - (1 + 2*gam/(gam+1)*(x**2-1.)) / (( (gam+1)*x**2)/((gam-1)*x**2+2) )
    return out
#
def func_inv_jump_rho(x,gam,R2_R1):
    """Implicit function used by fsolve to compute the upstream Mach number of a normal shock, given the static density jump
       Input variables: 
         - Gamma  : polytropic coefficient
         - T2_T1  : Static density jump
    """
    out =  R2_R1 - ( (gam+1)*x**2)/((gam-1)*x**2+2)
    return out
#
def func_jump_Pt(gam,M1):
    """Return the total pressure jump across a normal shock
       Input variables: 
         - M1     : upstream Mach number
         - Gamma  : polytropic coefficient
    """
    M2      = np.sqrt(((gam-1)*M1**2+2)/(2*gam*M1**2-gam+1))
    pt2_p2  = (1+0.5*(gam-1)*M2**2)**(gam/(gam-1))
    p1_pt1  = (1+0.5*(gam-1)*M1**2)**(-gam/(gam-1))
    jump_P  = 1 + 2*gam/(gam+1)*(M1**2-1)
    out     = pt2_p2*jump_P*p1_pt1
    return out
#
def func_jump_ds(gam,r,M1):
    """Return the entropy jump across a normal shock
       Input variables: 
         - M1     : upstream Mach number
         - Gamma  : polytropic coefficient
         - r      : Gaz constant (287 J/Kg/K for air)
    """
    x1 = (2*gam*M1**2+1-gam)/(gam+1)
    x2 = (2+(gam-1)*M1**2)/(gam+1)/M1**2
    out =  r/(gam-1)*log(x1*x2**gam)
    return out

 
# =======================
# OBLIQUE SHOCK RELATIONS
# =======================
def func_ODCo_up_nrm_Mach(Mach,beta):
    """Return the normal upstream Mach number over an oblique shock wave
       Input variables: 
         - Mach : upstream Mach number
         - beta : shock wave angle     (rad)
    """
    Mn1 = Mach*sin(beta)
    return Mn1
#
def func_ODCo_dn_nrm_Mach(Mnrm,beta,delta):
    """Return the downstream Mach number over an oblique shock wave
       Input variables: 
         - Mnrm : normal Mach number downstream of the shockwave
         - beta : shock wave angle     (rad)
         - delta: flow deviation angle (rad)  
    """
    M2 = Mnrm/sin(beta-delta)
    return M2
#
def func_Theta_Beta_Mach(gam,beta,M):
    """Return the flow deviation angle Theta in rad from the Oblique Shock relation
       Input variables: 
         - Gamma  : polytropic coefficient
         - beta   : shock wave angle     (rad) 
         - M      : upstream Mach number
     """
  # Theta_Beta_Mach function
  # beta (input) : shock wave angle     (rad)
  # M    (input) : upstream Mach number
  # theta(ouput) : flow deviation angle (rad)  
    tan_theta = 2.*cos(beta)/sin(beta)*(M**2*(sin(beta))**2-1)/(2.+M**2*(gam+cos(2*beta)))
    theta  = arctan(tan_theta)
    return theta
#
def func_inv_OSR(gam,theta,M1,typesol):
    """Return the angle of the oblique shock in deg.
       Input variables: 
         - Gamma  : polytropic coefficient
         - typesol: 'weak' -> weak shock solution; 'strong'-> strong shock solution
         - M1     : upstream Mach number
         - theta  : flow deviation angle in Radian (rad) 
     """
  # Exact solution for the Oblique Shock Relation 
  # Hartley et al., NASA CR 187173, 1991
    b = -gam * sin(theta)**2 - 1 - 2./M1**2
    d = -cos(theta)**2/M1**4
    c = (1+2*M1**2)/M1**4 + (0.25*(gam+1)**2 + (gam-1.)/M1**2)*sin(theta)**2
    Q = (3*c-b**2)/9
    R = (9*b*c - 27*d - 2*b**3)/54
    D = Q**3 + R**2
    if R < 0:
        dlt = pi
    else:
        dlt = 0.
    phi = 1./3.*(arctan(np.sqrt(-D)/R)+dlt)
    Xs  = -b/3 + 2*np.sqrt(-Q)*cos(phi)
    Xw  = -b/3 - np.sqrt(-Q)*(cos(phi)-np.sqrt(3)*sin(phi))
    beta_weak   = arctan(np.sqrt(Xw/(1.-Xw)))*180./pi
    beta_strong = arctan(np.sqrt(Xs/(1.-Xs)))*180./pi
    if typesol=='weak':
        beta=beta_weak
    else:
        beta=beta_strong
    return beta

 
# =======================
# FAN EXPANSION RELATIONS
# =======================
#
def func_PM(gam,M):
    """Return the Prandtl-Meyer function nu(M) in deg as a function of gamma and Mach number"""
    c2   = np.sqrt((gam-1.)/(gam+1.))
    out =  (arctan(c2*np.sqrt(M**2-1.))/c2 - arctan(np.sqrt(M**2-1.)))*180./pi
    return out
#
# Fonction de Prandtl-Meyer
def fun_PM(x,gam,nu_deg):
    """Implicit function used by fsolve to compute the Mach number from the  Prandtl-Meyer function,
       given gamma and nu in deg."""
    c2  = np.sqrt((gam-1.)/(gam+1.))
    out = (arctan(c2*np.sqrt(x**2-1.))/c2 - arctan(np.sqrt(x**2-1.)))*180./pi - nu_deg
    return out
#
def func_inv_PM_approx(gam,nu_deg):
    """Return the approximated Mach number of the Prandtl-Meyer function given gamma and nu in deg."""
    # Analytic approximation of the inverse PM function
    # Reference : [2] Hartley et al., NASA CR 187173, 1991
    # Return the Mach number as a function of nu and gamma
    A     = 1.3604
    B     = 0.0962
    C     =-0.5127
    D     =-0.6722
    E     =-0.3278
    nu_inf=0.5*pi*(np.sqrt(6)-1.)/pi*180.
    y     = (nu_deg/nu_inf)**(2./3.)
    out   = (1+A*y + B*y**2. + C*y**3.)/(1+D*y+E*y**2.)
    return out
#----
# EOF
#----
