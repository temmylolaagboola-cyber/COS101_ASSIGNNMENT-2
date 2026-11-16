
def newton_law():
    m = float(input("Enter mass:"))
    a = float(input("Enter acceleration: "))
    print("Force =",m * a)

def kinetic_energy():
    m = float(input("Enter mass:"))
    v = float(input("Enter velocity:"))
    print("Kinetic Energy =", 0.5 *m * v ** 2)

def velocity():
    u = float(input("Enter initial velocity: "))
    a = float(input("Enter acceleration: "))
    t = float(input("Enter time:"))
    print("Final Velocity =", u + a * t)

def potential_energy():
    m = float(input("Enter mass:"))
    g = float(input("Enter gravity: "))
    h = float(input("Enter height:"))
    print("Potential Energy =", m * g * h)

def ohms_law():
    I =  float(input("Enter current:"))
    R = float(input("Enter resistance: "))
    print("Voltage =". I * R)

while True:
    print("\nPHYSICS CALCULATOR")
    print("1. Newton's Second Law")
    print("2 .Kinetic Energy")
    print("3. Gravitational Potential Energy")
    print("5. Ohm's Law")
    choice = input("choose a formula (1-5):")

    if choice =="1":
       newton_law()
    elif choice =="2":
         kinetic_energy()
    elif choice =="3":
         velocity()
    elif choice =="4":
         potential energy()
    elif choice =="5":
         ohms law()
    else:
         print("Invalid choice!")
    again = input("Continue? (yes/no):")
    
    if again.lower() !="yes":
       print("program ended.")
       break