import numpy as np
import math

"""
Script to compute the differential rotation coefficients for 1-curl and 2-curl equations.

Implemented :  
    - Coefficients for the modified Coriolis term
"""


def c1_1curl(l, m, w) : 
    if l > 2 : 
        c = ((3*np.sqrt(l*(1 + l))*np.sqrt(6 - 5*l + l**2)
            * ( np.sqrt(6 - 5*l + l**2)*np.sqrt(((1 + l)*(-2 + l - m)*(-1 + l - m)*(l - m)*(-2 + l + m)*(-1 + l + m)*(l + m))/l) 
            - np.sqrt(((-3 - 2*l + l**2)*(-2 + l - m)*(-1 + l - m)*(l - m)*(-2 + l + m)*(-1 + l + m)*(l + m))/((-2 + l)*l)))*w)/(2*(-5 + 2*l)*(-3 + 2*l)*(-1 + 2*l)))
    else : 
        c = 0

    return c

def c2_1curl(l, m, w) : 
    if l > 1 : 
        c = (((((-1 + l)**2)*(1 + l)*np.sqrt(l**2 - m**2))/(-1 + 2*l)) 
        + (((2 + l)*(-1 + l**2)*np.sqrt(l**2 - m**2)*w)/(5 - 10*l))
        - (3*np.sqrt((-1 + l)*l)*np.sqrt(l*(1 + l))*(-1 + l**2 - 5*m**2)*(((3*(-6 + l**2)*np.sqrt((l**2 - m**2)/(-1 + l**2)))/l) 
        - np.sqrt((-1 + l)*l)*(6 + l)*np.sqrt((l**2 - m**2)/(l + l**2)))*w)/(10*(9 - 18*l - 4*l**2 + 8*l**3)))
    else : 
        c = 0

    return c 

def c3_1curl(l, m, w) : 
    c = ((1/5)*(-(((5*l*(2 + l)**2)*np.sqrt(1 + 2*l + l**2 - m**2))/(3 + 2*l)) 
        + ((-1 + l)*l*(2 + l)*np.sqrt(1 + 2*l + l**2 - m**2)*w)/(3 + 2*l) 
        - (3/2)*np.sqrt(l*(1 + l))*np.sqrt(2 + 3*l + l**2)*(2*l + l**2 - 5*m**2)
        *(((-5 + l)*np.sqrt(2 + 3*l + l**2)*np.sqrt((1 + 2*l + l**2 - m**2)/(l + l**2)))/(-15 + 14*l + 28*l**2 + 8*l**3) 
        + (3*(-5 + 2*l + l**2)*np.sqrt((1 + 2*l + l**2 - m**2)/(2*l + l**2)))/((1 + l)*(-1 + 2*l)*(3 + 2*l)*(5 + 2*l)))*w))

    return c

def c4_1curl(l, m, w) : 
    c = -((3*np.sqrt(l*(1 + l))*np.sqrt(12 + 7*l + l**2)
        *( (np.sqrt(12 + 7*l + l**2)*np.sqrt((l*(1 + l - m)*(2 + l - m)*(3 + l - m)*(1 + l + m)*(2 + l + m)*(3 + l + m))/(1 + l))) 
        + (np.sqrt((l*(4 + l)*(1 + l - m)*(2 + l - m)*(3 + l - m)*(1 + l + m)*(2 + l + m)*(3 + l + m))/((1 + l)*(3 + l))))  )*w)/(2*(3 + 2*l)*(5 + 2*l)*(7 + 2*l)))

    return c

def c5_1curl(l, m, w) : 
    if l > 2 : 
        c = -1j*((9*np.sqrt(l*(1 + l))*np.sqrt(2 - 3*l + l**2)*m
           *np.sqrt(((-1 + l - m)*(l - m)*(-1 + l + m)*(l + m))/((-2 + l)*(-1 + l)*l*(1 + l)))*w)/(6 - 16*l + 8*l**2))

    else : 
        c = 0

    return c

def c6_1curl(l, m, w) : 
    c = -1j*((m*(l*(4 + 7*w) + (l**2)*(4 + 7*w) - 3*(1 + w + 3*w*m**2)))/(-3 + 4*l + 4*l**2))

    return c

def c7_1curl(l, m, w) : 
    c = -1j*((9*np.sqrt(l*(1 + l))*np.sqrt((2 + l)*(3 + l))*m*np.sqrt(((1 + l - m)*(2 + l - m)*(1 + l + m)*(2 + l + m))/(l*(1 + l)*(2 + l)*(3 + l)))*w)/(2*(3 + 2*l)*(5 + 2*l)))

    return c

def c8_1curl(l, m, w) : 
    if l > 2 : 
        c = -((3*np.sqrt(l*(1 + l))*np.sqrt(6 - 5*l + l**2)*np.sqrt((1/((-2 + l)*l))*(-3 - 2*l + l**2)*(-2 + l - m)*(-1 + l - m)*(l - m)*(-2 + l + m)*(-1 + l + m)*(l + m))*w)
          /(2*(-5 + 2*l)*(-3 + 2*l)*(-1 + 2*l)))
    else : 
        c = 0

    return c

def c9_1curl(l, m, w) : 
    if l > 1 : 
        c = -(((-1 + l**2)*np.sqrt(l**2 - m**2))/(-1 + 2*l)) + (2*(-1 + l**2)*np.sqrt(l**2 - m**2)*w)/(5 - 10*l) - (9*np.sqrt((-1 + l)*l)*np.sqrt(l*(1 + l))*(-6 + l**2)
        *(-1 + l**2 - 5*m**2)*np.sqrt((l**2 - m**2)/(-1 + l**2))*w)/(10*l*(9 - 18*l - 4*l**2 + 8*l**3))
    else : 
        c = 0
        
    return c

def c10_1curl(l, m, w) : 
    c = ( (l/(10*(3 + 2*l))) * ( (-10*(2 + l)*np.sqrt(1 + 2*l + l**2 - m**2)) - (4*(2 + l)*np.sqrt(1 + 2*l + l**2 - m**2)*w) 
        - ( (9*(-5 + 2*l + l**2)*np.sqrt(2 + 3*l + l**2)*(2*l + l**2 - 5*m**2)*np.sqrt((1 + 2*l + l**2 - m**2)/(2*l + l**2))*w)/(np.sqrt(l*(1 + l))*(-5 + 8*l + 4*l**2)))))

    return c

def c11_1curl(l, m, w) : 
    c = -((3*np.sqrt(l*(1 + l))*np.sqrt((3 + l)*(4 + l))*np.sqrt(1/((1 + l)*(3 + l))*l*(4 + l)*(1 + l - m)*(2 + l - m)*(3 + l - m)*(1 + l + m)*(2 + l + m)*(3 + l + m))*w)
          /(2*(3 + 2*l)*(5 + 2*l)*(7 + 2*l)))

    return c

def c_1curl(l, m, w) : 
    """
    Coefficients for the 1-curl modified Coriolis term.

        c1  -> P[l-3]/r
        c2  -> P[l-1]/r
        c3  -> P[l+1]/r
        c4  -> P[l+3]/r
        c5  -> T[l-2]
        c6  -> T[l]
        c7  -> T[l+2]
        c8  -> P'[l-3]
        c9  -> P'[l-1]
        c10 -> P'[l+1]
        c11 -> P'[l+3]
    """
    return np.array((c1_1curl(l, m, w), c2_1curl(l, m, w), c3_1curl(l, m, w), c4_1curl(l, m, w), c5_1curl(l, m, w), c6_1curl(l, m, w), c7_1curl(l, m, w), c8_1curl(l, m, w), c9_1curl(l, m, w), c10_1curl(l, m, w), c11_1curl(l, m, w)))



# 2-curl 

def c1_2curl(l, m , w) :
    if l > 2 :  
        c = (-1.5j * np.sqrt((-2 + l) * (-1 + l)) * l * (1 + l) * m *
        np.sqrt((l**2 - 2*l**3 + l**4 - m**2 + 2*l*m**2 - 2*l**2*m**2 + m**4) / (2 - 3*l + l**2)) * w) / (3 - 8*l + 4*l**2)
    else : 
        c = 0
    return c 

def c2_2curl(l, m , w) : 
    if l > 2 : 
        c = 1j * np.sqrt(2) * l * (1 + l) * np.sqrt(l * (1 + l)) *(-((m * (1 - w / 5.)) / (np.sqrt(2) * np.sqrt(l * (1 + l)))) +(3 * m * (1 - 3*l - 3*l**2 + 5*m**2) * w) / (5. * np.sqrt(2) * np.sqrt(l * (1 + l)) * (-3 + 4*l + 4*l**2)))
    
    elif l == 2 : 
        c = 12j*np.sqrt(3)*(-0.5*((-1)**(2*m)*m*(1 - w/5.))/np.sqrt(3) + (12*(-1)**m*np.sqrt(3)*m*w)/(35.*math.factorial(2 - m)*math.factorial(2 + m)))

    elif l == 1 : 
        c = -2j*((-1)**(2*m))*m*(1 - w/5.)

    return c 

def c3_2curl(l, m , w) : 
    if l > 2 : 
        c = c = -6j * l * (1 + l) * np.sqrt((2 + l) * (3 + l)) * m *np.sqrt((4 + 6*l**3 + l**4 - 5*m**2 + m**4 + l**2*(13 - 2*m**2) - 6*l*(-2 + m**2)) /(6 + 5*l + l**2)) * w / (60 + 64*l + 16*l**2)
    
    elif l == 2 : 
        c = (-1j/7.)*m*np.sqrt(144 - 25*m**2 + m**4)*w

    elif l == 1 : 
        c = (144/35)*1j*((-1)**m)*m*w*np.sqrt(1/(math.factorial(1-m)*math.factorial(3-m)*math.factorial(1+m)*math.factorial(3+m)))

    return c 

def c4_2curl(l, m , w) : 
    if l > 2 : 
        c = (3*(np.sqrt((-3 + l)/(-2 + l))*l*(1 + l) - np.sqrt(((1 + l)*(-3 - 2*l + l**2))/(-2 + l)))*np.sqrt((-3 + l)*(-2 + l)*(-2 + l - m)*(-1 + l - m)*(l - m)*(-2 + l + m)*(-1 + l + m)*(l + m))*w)/(2.*(-5 + 2*l)*(-3 + 2*l)*(-1 + 2*l))
    
    else : 
        c = 0

    return c 

def c5_2curl(l, m , w) :
    if l > 2 : 
        c = np.sqrt(2)*l*np.sqrt((-1 + l)*l)*(1 + l)*((np.sqrt(((-1 + l)*(l**2 - m**2))/l)*(1 - w/5.))/(np.sqrt(2)*(-1 + 2*l)) + (3*(-6 + l)*(-1 + l**2 - 5*m**2)*np.sqrt((l**2 - m**2)/((-1 + l)*l))*w)/
        (10.*np.sqrt(2)*(9 - 18*l - 4*l**2 + 8*l**3))) - np.sqrt((-1 + l)*l)*np.sqrt(l*(1 + l))*(-((np.sqrt((-1 + l**2)*(l**2 - m**2))*(1 + (2*w)/5.))/(l - 2*l**2)) + (9*(-6 + l**2)*(-1 + l**2 - 5*m**2)*np.sqrt((l**2 - m**2)/(-1 + l**2))*w)/
        (10.*l*(9 - 18*l - 4*l**2 + 8*l**3)))
    
    elif l == 2 and np.abs(m) < 2 : 
        c = (12*((np.sqrt(4 - m**2)*(1 - w/5.)/6.) - (12*(((-1)**m)*w*np.sqrt(1/(math.factorial(1 - m)*math.factorial(2 - m)*math.factorial(1 + m)*math.factorial(2 + m))))/35.))) - (2*np.sqrt(3)*((((-1)**(2*m)*np.sqrt(4 - m**2)*(1 + (2*w)/5.))/(2.*np.sqrt(3))) - ((6*((-1)**m)*np.sqrt(3)*w*np.sqrt(1/(math.factorial(1 - m)*math.factorial(2 - m)*math.factorial(1 + m)*math.factorial(2 + m))))/35.)))
        
    else : 
        c = 0

    return c 

def c6_2curl(l, m , w) :
    if l > 2 : 
        c = -(np.sqrt(l*(1 + l))*np.sqrt((1 + l)*(2 + l))*((np.sqrt(l*(2 + l)*(1 + l - m)*(1 + l + m))*(1 + (2*w)/5.))/((1 + l)*(3 + 2*l)) 
        + (9*(-5 + 2*l + l**2)*np.sqrt(((1 + l - m)*(1 + l + m))/(l*(2 + l)))*(2*l + l**2 - 5*m**2)*w)
        /(10.*(1 + l)*(-1 + 2*l)*(3 + 2*l)*(5 + 2*l)))) + np.sqrt(2)*l*(1 + l)*np.sqrt((1 + l)*(2 + l))*(-((np.sqrt(((2 + l)*(1 + 2*l + l**2 - m**2))/(1 + l))*(1 - w/5.))/(np.sqrt(2)*(3 + 2*l))) - (3*(7 + l)*(2*l + l**2 - 5*m**2)*np.sqrt((1 + 2*l + l**2 - m**2)/(2 + 3*l + l**2))*w)/(10.*np.sqrt(2)*(-15 + 14*l + 28*l**2 + 8*l**3)))

    elif l == 2 : 
        c = -(6*np.sqrt(2)*((2*np.sqrt(2)*np.sqrt(9 - m**2)*(1 + (2*w)/5.))/21. - (6*(-1)**m*np.sqrt(2)*(-2 + 3*m**2)*w*np.sqrt(1/(math.factorial(2 - m)*math.factorial(3 - m)*math.factorial(2 + m)*math.factorial(3 + m))))/35.)) + (12*np.sqrt(6)*(-(np.sqrt(6 - (2*m**2)/3.)*(1 - w/5.))/7. + (6*(-1)**m*np.sqrt(6)*(-2 + 3*m**2)*w*np.sqrt(1/(math.factorial(2 - m)*math.factorial(3 - m)*math.factorial(2 + m)*math.factorial(3 + m))))/35.))


    elif l == 1 : 
        c = (4*np.sqrt(3)*((-np.sqrt(3)*np.sqrt(4 - m**2)*(1 - w/5.))/10. - (24*(-1)**m*np.sqrt(3)*w*np.sqrt(1/(math.factorial(1 - m)*math.factorial(2 - m)*math.factorial(1 + m)*math.factorial(2 + m))))/175.)) - (2*np.sqrt(3)*((np.sqrt(3)*np.sqrt(4 - m**2)*(1 + (2*w)/5.))/10. - (18*(-1)**m*np.sqrt(3)*w*np.sqrt(1/(math.factorial(1 - m)*math.factorial(2 - m)*math.factorial(1 + m)*math.factorial(2 + m))))/175.))

    return c 


def c7_2curl(l, m , w) :
    if l > 2 : 
        c = (-3*l*(1 + l)*np.sqrt((3 + l)*(4 + l))
        *np.sqrt(((4 + l)*(1 + l - m)*(2 + l - m)*(3 + l - m)*(1 + l + m)*(2 + l + m)*(3 + l + m))
        /(3 + l))*w)/(2.*(3 + 2*l)*(5 + 2*l)*(7 + 2*l)) -(3*np.sqrt(l*(1 + l))*np.sqrt((3 + l)*(4 + l))
        *np.sqrt((l*(4 + l)*(1 + l - m)*(2 + l - m)*(3 + l - m)*(1 + l + m)*(2 + l + m)*(3 + l + m))
        /((1 + l)*(3 + l)))*w)/(2.*(3 + 2*l)*(5 + 2*l)*(7 + 2*l))
    
    elif l == 2 : 
        c = (-8*np.sqrt(-((-5 + m)*(-4 + m)*(-3 + m)*(3 + m)*(4 + m)*(5 + m)))*w)/77.

    elif l == 1 : 
        c = -(1/14.)*np.sqrt(576 - 244*m**2 + 29*m**4 - m**6)*w

    return c 


def c8_2curl(l, m , w) :
    if l > 2 : 
        c = ((-1.5j*np.sqrt((-2 + l)*(-1 + l))*l*(1 + l)*m*np.sqrt((l**2 - 2*(l**3) + l**4 - m**2 + 2*l*(m**2) - 2*(l**2)*(m**2) + m**4)/(2 - 3*l + l**2))*w) / (3 - 8*l + 4*(l**2))) - (1j*np.sqrt((-2 + l)*(-1 + l))*np.sqrt(l*(1 + l))*(((-18*m*np.sqrt(((-1 + l - m)*(l - m)*(-1 + l + m)*(l + m))/((-2 + l)*(-1 + l)*l*(1 + l)))*w) / (6 - 16*l + 8*(l**2)))
        - ((3*np.sqrt((-2 + l)*(-1 + l))*m*np.sqrt((l**2 - 2*(l**3) + l**4 - m**2 + 2*l*(m**2) - 2*(l**2)*(m**2) + m**4)/(l + l**2))*w)/ (2*(3 - 8*l + 4*(l**2))))))        
    
    else : 
        c = 0

    return c 

def c9_2curl(l, m , w) : 
    if l > 2 : 
        c = (1j * np.sqrt(2) * l * (1 + l) * np.sqrt(l * (1 + l)) * 
        (-((m * (1 - w / 5)) / (np.sqrt(2) * np.sqrt(l * (1 + l)))) + 
         (3 * m * (1 - 3 * l - 3 * l**2 + 5 * m**2) * w) / 
         (5. * np.sqrt(2) * np.sqrt(l * (1 + l)) * (-3 + 4 * l + 4 * l**2))) - 
        1j * l * (1 + l) * 
        (-(np.sqrt(2) * np.sqrt(l * (1 + l)) * 
           ((m * (1 - w / 5)) / (np.sqrt(2) * np.sqrt(l * (1 + l))) + 
            (3 * m * (-1 + 3 * l + 3 * l**2 - 5 * m**2) * w) / 
            (5. * np.sqrt(2) * np.sqrt(l * (1 + l)) * (-3 + 4 * l + 4 * l**2)))) + 
         2 * (-(m * (1 + (2 * w) / 5)) / (l + l**2) + 
              (9 * m * (1 - 3 * l - 3 * l**2 + 5 * m**2) * w) / 
              (5. * l * (-3 + l + 8 * l**2 + 4 * l**3)))))
    
    elif l == 2 : 
        c = -6j*(2*(-(1/6.)*((-1)**(2*m)*m*(1 + (2*w)/5.)) 
        + (36*(-1)**m*m*w)/(35.*math.factorial(2 - m)*math.factorial(2 + m))) 
        - 2*np.sqrt(3)*(((-1)**(2*m)*m*(1 - w/5.))/(2.*np.sqrt(3)) - (12*(-1)**m*np.sqrt(3)*m*w)
        /(35.*math.factorial(2 - m)*math.factorial(2 + m)))) + 12j*np.sqrt(3)*(-0.5*((-1)**(2*m)*m*(1 - w/5.))/np.sqrt(3) + (12*(-1)**m*np.sqrt(3)*m*w)/(35.*math.factorial(2 - m)*math.factorial(2 + m)))
    
    elif l == 1 : 
        c = -2j*(-((-1)**(2*m)*m*(1 - w/5.)) - (-1)**(2*m)*m*(1 + (2*w)/5.)) - 2j*(-1)**(2*m)*m*(1 - w/5.)

    return c 


def c10_2curl(l, m , w) : 
    if l > 2 : 
        c = (-6j * l * (1 + l) * np.sqrt((2 + l) * (3 + l)) * m *
        np.sqrt((4 + 6*l**3 + l**4 - 5*m**2 + m**4 + l**2*(13 - 2*m**2) - 6*l*(-2 + m**2)) / (6 + 5*l + l**2)) * w
        ) / (60 + 64*l + 16*l**2)-1j * np.sqrt(l * (1 + l)) * np.sqrt((2 + l) * (3 + l)) *(
        (-9 * m * np.sqrt(((1 + l - m) * (2 + l - m) * (1 + l + m) * (2 + l + m)) /
                          (l * (1 + l) * (2 + l) * (3 + l))) * w) / ((3 + 2*l) * (5 + 2*l))
        -(6 * np.sqrt((2 + l) * (3 + l)) * m *
        np.sqrt((4 + 6*l**3 + l**4 - 5*m**2 + m**4 + l**2*(13 - 2*m**2) - 6*l*(-2 + m**2)) / (l * (1 + l))) * w)
        / (60 + 64*l + 16*l**2))    
    
    elif l == 2 : 
        c = -(1j/7.)*m*np.sqrt(144 - 25*m**2 + m**4)*w - 2j*np.sqrt(30)*((-(1/21.))*(np.sqrt(5/6.))*m*np.sqrt(144 - 25*m**2 + m**4)*w 
        - (m*np.sqrt(144 - 25*m**2 + m**4)*w)/(14.*np.sqrt(30)))

    elif l == 1 : 
        c = -(1152/35.)*1j*(-1)**m*m*w*np.sqrt(1/(math.factorial(1 - m)*math.factorial(3 - m)*math.factorial(1 + m)*math.factorial(3 + m)))

    return c 

def c11_2curl(l, m , w) : 
    if l > 2 : 
        c = (
        -3 * np.sqrt((-3 + l) * (-2 + l)) * np.sqrt(l * (1 + l)) *
        np.sqrt(
            ((-3 - 2 * l + l**2) * (-2 + l - m) * (-1 + l - m) * (l - m) *
             (-2 + l + m) * (-1 + l + m) * (l + m)) /
            ((-2 + l) * l)
        ) * w
        ) / (2. * (-5 + 2 * l) * (-3 + 2 * l) * (-1 + 2 * l))
    
    else : 
        c = 0

    return c 


def c12_2curl(l, m , w) : 
    if l > 2 : 
        c = - np.sqrt((-1 + l) * l) * np.sqrt(l * (1 + l)) *(-(np.sqrt((-1 + l**2) * (l**2 - m**2)) * (1 + (2 * w) / 5.)) / (l - 2 * l**2) 
        +(9 * (-6 + l**2) * (-1 + l**2 - 5 * m**2) * np.sqrt((l**2 - m**2) / (-1 + l**2)) * w) / (10. * l * (9 - 18 * l - 4 * l**2 + 8 * l**3))
    )

    elif l == 2 and np.abs(m) < 2: 
        c = -2*np.sqrt(3)*(((-1)**(2*m)*np.sqrt(4 - m**2)*(1 + (2*w)/5.))/(2.*np.sqrt(3)) 
        -(6*(-1)**m*np.sqrt(3)*w*np.sqrt(1/(math.factorial(1 - m)*math.factorial(2 - m)*math.factorial(1 + m)*math.factorial(2 + m))))/35.)

    else : 
        c = 0

    return c 


def c13_2curl(l, m , w) : 
    if l > 2 : 
        c =-(np.sqrt(l*(1 + l))*np.sqrt((1 + l)*(2 + l))*((np.sqrt(l*(2 + l)*(1 + l - m)*(1 + l + m))*(1 + (2*w)/5.))/((1 + l)*(3 + 2*l)) + 
        (9*(-5 + 2*l + l**2)*np.sqrt(((1 + l - m)*(1 + l + m))/(l*(2 + l)))*(2*l + l**2 - 5*m**2)*w)/
        (10.*(1 + l)*(-1 + 2*l)*(3 + 2*l)*(5 + 2*l))))
    
    elif l == 2 : 
        c = -6*np.sqrt(2)*((2*np.sqrt(2)*np.sqrt(9 - m**2)*(1 + (2*w)/5.))/21. 
        -(6*(-1)**m*np.sqrt(2)*(-2 + 3*m**2)*w*np.sqrt(1/(math.factorial(2 - m)*math.factorial(3 - m)*math.factorial(2 + m)*math.factorial(3 + m))))/35.)

    elif l == 1 : 
        c = -2*np.sqrt(3)*((np.sqrt(3)*np.sqrt(4 - m**2)*(1 + (2*w)/5.))/10. 
            - (18*(-1)**m*np.sqrt(3)*w*np.sqrt(1/(math.factorial(1 - m)*math.factorial(2 - m)*math.factorial(1 + m)*math.factorial(2 + m))))/175.)

    return c 


def c14_2curl(l, m , w) : 
    if l > 2 : 
        c =(-3*np.sqrt(l*(1 + l))*np.sqrt((3 + l)*(4 + l))*np.sqrt((l*(4 + l)*(1 + l - m)*(2 + l - m)*(3 + l - m)*(1 + l + m)*(2 + l + m)*
        (3 + l + m))/((1 + l)*(3 + l)))*w)/(2.*(3 + 2*l)*(5 + 2*l)*(7 + 2*l))
    
    elif l == 2 : 
        c = -2*np.sqrt(-((-5 + m)*(-4 + m)*(-3 + m)*(3 + m)*(4 + m)*(5 + m)))*w/77.

    elif l == 1 : 
        c = -(1/42.)*(np.sqrt(576 - 244*m**2 + 29*m**4 - m**6)*w)

    return c 


def c15_2curl(l, m , w) : 
    if l > 2 : 
        c = 9j * np.sqrt((-2 + l) * (-1 + l)) * np.sqrt(l * (1 + l)) * m *np.sqrt(
        ((-1 + l - m) * (l - m) * (-1 + l + m) * (l + m)) /
        ((-2 + l) * (-1 + l) * l * (1 + l))
        ) * w / (6 - 16 * l + 8 * l**2)
    
    else : 
        c = 0
        
    return c 



def c16_2curl(l, m , w) : 
    if l > 2 : 
        c = -1j * l * (1 + l) * (
        -((m * (1 + (2 * w) / 5.)) / (l + l**2)) +
        (9 * m * (1 - 3 * l - 3 * l**2 + 5 * m**2) * w) /
        (5. * l * (-3 + l + 8 * l**2 + 4 * l**3))
    )

    elif l == 2 : 
        c = -6j*((-(1/6.))*((-1)**(2*m)*m*(1 + (2*w)/5.)) + (36*(-1)**m*m*w)/(35.*math.factorial(2 - m)*math.factorial(2 + m)))

    elif l == 1 : 
        c = 1j*(-1)**(2*m)*m*(1 + (2*w)/5.)

    return c 


def c17_2curl(l, m , w) : 
    if l > 2 : 
        c = 4.5j * np.sqrt(l * (1 + l)) * np.sqrt((2 + l) * (3 + l)) * m *np.sqrt(
        ((1 + l - m) * (2 + l - m) * (1 + l + m) * (2 + l + m)) /
        (l * (1 + l) * (2 + l) * (3 + l))) * w / ((3 + 2 * l) * (5 + 2 * l))
    
    elif l == 2 : 
        c = (1j/14.)*m*np.sqrt(144 - 25*m**2 + m**4)*w

    elif l == 1 : 
        c = -(216j/35.)*(-1)**m*m*w*np.sqrt(1/(math.factorial(1 - m)*math.factorial(3 - m)*math.factorial(1 + m)*math.factorial(3 + m)))

    return c 


def c_2curl(l, m, w) : 
    """
    Coefficients for the 2-curl modified Coriolis term.

        c1  -> P[l-2]/r^2
        c2  -> P[l]/r^2
        c3  -> P[l+2]/r^2
        c4  -> T[l-3]/r
        c5  -> T[l-1]/r
        c6  -> T[l+1]/r
        c7  -> T[l+3]/r
        c8  -> P'[l-2]/r
        c9  -> P'[l]/r
        c10 -> P'[l+2]/r
        c11 -> T'[l-3]
        c12 -> T'[l-1]
        c13 -> T'[l+1]
        c14 -> T'[l+3]
        c15 -> P''[l-2]
        c16 -> P''[l]
        c17 -> P''[l+2]
    """

    return np.array((c1_2curl(l, m, w), c2_2curl(l, m, w), c3_2curl(l, m, w), c4_2curl(l, m, w), c5_2curl(l, m, w), c6_2curl(l, m, w), c7_2curl(l, m, w), c8_2curl(l, m, w), c9_2curl(l, m, w), c10_2curl(l, m, w), c11_2curl(l, m, w), c12_2curl(l, m, w), c13_2curl(l, m, w), c14_2curl(l, m, w), c15_2curl(l, m, w), c16_2curl(l, m, w), c17_2curl(l, m, w)))