import math

def sphere(r):
    vsphere = (4/3)*math.pi*(r**3)
    vsphere = round (vsphere,2)
    print (vsphere)
    return vsphere


if __name__ == "__main__":
    assert sphere(2) == 33.51


def cylinder(r,h):
    vcylinder = math.pi*(r**2)*h
    vcylinder = round(vcylinder, 2)
    print (vcylinder)
    return vcylinder

if __name__ == "__main__":
    assert cylinder(2,2) == 25.13

def compound(P, r, n, t):
    A = P*(1+(r/n))**(n*t)
    A = round(A,2)
    print(A)
    return A

if __name__ == "__main__":
    assert compound(2,0.02,2,2) == 2.08

def sasphere(r):
    surfacesphere = 4*math.pi*(r**2)
    surfacesphere = round(surfacesphere,2)
    print(surfacesphere)
    return surfacesphere

if __name__ == "__main__":
    assert sasphere(2) == 50.27

def circle(r):
    acircle = math.pi*(r**2)
    acircle = round(acircle,2)
    print(acircle)
    return acircle

if __name__ == "__main__":
    assert circle(2) == 12.57