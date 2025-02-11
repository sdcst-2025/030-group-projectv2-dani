#!python3
# Volume Calculator
# Feel free to rename your variables
import math

def title():
    # Will display a title screen
    # input parameters: none needed
    # output parameters: None
    # Author: Copper
    # Modified:
    # title

    print("Welcome to The Calculator!\n")
    print("This calculator includes the option to find the volume of a sphere, the volume of a cylinder,\namount of money accumulated after n years (including interest), the surface area of a sphere, and the area of a circle.\n")
    print ("Would you like to get started and listen to instructions? If yes, type YES, if you don't you will go straight to menu options.\n")
    return None

def instructions():
    # Will display instructions
    # input parameters: none needed
    # output parameters: None
    # Author:
    # Modified:
    z = False

    while z==False:
         print("After reading the instructions, you will be prompted to either choose a calculation to make or to exit.\n")

         print("These are the requirements for each calculation:")
         print("Finding the volume of a sphere requires a radius.")
         print("Finding the volume of a cylinder requires a radius and a height.")
         print("Finding the money accumulated with compound interest requires the starting amount, the interest rate (in decimals),\nthe number of times the interest is applied in the time period, and the amount of time periods elapsed.")
         print("Finding the surface area of a sphere requires a radius.")
         print("Finding the area of a circle requires a radius")

         print("If you understand, type OK")
         ok = input()

         if ok == "OK":
            z=True
    pass

    return None

def sphere(r):
    vsphere = (4/3)*math.pi*(r**3)
    vsphere = round (vsphere,2)
    print (f"Your volume is {vsphere}")
    return None

def cylinder(r,h):
    vcylinder = math.pi*(r**2)*h
    vcylinder = round(vcylinder, 2)
    print (f"Your volume is {vcylinder}")
    return None


def compound(P, r, n, t):
    A = P*(1+(r/n))**(n*t)
    A = round(A,2)
    print(f"Your accumulated amount is {A}")
    return None


def sasphere(r):
    surfacesphere = 4*math.pi*(r**2)
    surfacesphere = round(surfacesphere,2)
    print(f"Your surface area is {surfacesphere}")
    return None


def circle(r):
    acircle = math.pi*(r**2)
    acircle = round(acircle,2)
    print(f"Your area is {acircle}")
    return None



def main():
    """
    main block of code that will run your program and control program flow
    You will need to include a while loop to keep repeating the commands until
    the user chooses to exit
    """
    l = True

    title()
    instoption = input()
    if instoption == "YES":
        instructions()
    
    while l == True:
        # keep giving options to choose menu options until they choose to exit
        print("Would you like to find the volume of a sphere? If you do, type SPHERE")
        print("Would you like to find the volume of a cylinder? If you do, type CYLINDER")
        print("Would you like to find the amount of money accumulated with compound interest? If you do, type COMPOUND")
        print("Would you like to find the surface area of a sphere? If you do, type SASPHERE")
        print("Would you like to find area of a circle? If you do, type CIRCLE")
        print("Would you like to look at the instructions again? If you do, type INSTRUCTIONS")
        print("If you'd like to exit, type EXIT")
        x = input()
        x = str(x)
        if x == "EXIT":
            l = False
        elif x == "SPHERE":
            try:
                r = input("Enter a radius: ")
                r = float(r)
                sphere(r)
                print("Thanks for calculating, you will now be given the same options as earlier.\n")
            except:
                print("\nError. Try again.\n")
        elif x == "CYLINDER":
            try:
                r = input("Enter a radius: ")
                r = float(r)
                h = input("Enter a height: ")
                h = float(h)
                cylinder(r, h)
                print("Thanks for calculating, you will now be given the same options as earlier.\n")
            except:
                print("\nError. Try again.\n")
        elif x == "COMPOUND":
            try:
                P = input("Enter an initial principal balance: ")
                P = float(P)
                r = input("Enter an interest rate (decimal): ")
                r = float(r)
                n = input("Enter the number of times interest is applied per time period: ")
                n = float(n)
                t = input("Enter the number of time periods elapsed: ")
                t = float(t)
                compound(P, r, n, t)
                print("Thanks for calculating, you will now be given the same options as earlier.\n")
            except:
                print("\nError. Try again.\n")    
        elif x == "SASPHERE":
            try:
                r = input("Enter a radius: ")
                r = float(r)
                sasphere(r)
                print("Thanks for calculating, you will now be given the same options as earlier.\n")
            except:
                print("\nError. Try again.\n")
        elif x == "CIRCLE":
            try:
                r = input("Enter a radius: ")
                r = float(r)
                circle(r)
                print("Thanks for calculating, you will now be given the same options as earlier.\n")
            except:
                print("\nError. Try again.\n")
        elif x == "INSTRUCTIONS":
            instructions()
        else:
            print("\n\nError. Try again.\n\n")
    pass

    print("\nThanks for using The Calculator!")

if __name__ == "__main__":
    main()
