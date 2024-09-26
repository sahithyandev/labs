import math
import matplotlib.pyplot as plt


def adsin(value):
    angle = math.asin(value)
    rd = 180/math.pi
    return round(angle*rd, 10)


def dsin(angle):
    dd = math.pi/180
    return round(math.sin(angle*dd), 10)


def adcos(value):
    angle = math.acos(value)
    rd = 180/math.pi
    return round(angle*rd, 10)


def dcos(angle):
    dd = math.pi/180
    return round(math.cos(angle*dd), 10)


def dtan(angle):
    dd = math.pi/180
    return round(math.tan(angle*dd), 10)


def adtan(value):
    angle = math.atan(value)
    rd = 180/math.pi
    return round(angle*rd, 10)


index_no = input("Enter your index number (230---X): ")


# in cm
AB = 10
BC = 40 + int(index_no[3])
CD = 30 + int(index_no[4])
AD = 30 + int(index_no[5])


table_length = 45


def print_parameter(label: str, value, unit: str = ""):
    print(f"| {label}".ljust(table_length // 2) + " | " +
          (str(value) + " " + unit).ljust(table_length//2 - 4) + "|")


Omega = 0.1 * (1 + int(index_no[5]))
instantaneous_angle = int(index_no[4:6])

col_divider = ("-" * table_length)
print(col_divider)
print_parameter("Index No", index_no)
print_parameter("AB", AB, "cm")
print_parameter("BC", BC, "cm")
print_parameter("CD", CD, "cm")
print_parameter("AD", AD, "cm")
print_parameter("Omega", Omega, "rad/s")
print_parameter("Instantaneous angle", instantaneous_angle, "deg")
print(col_divider)

input_angles = []
output_angles = []
v_ce_values = []
v_be_values = []
v_cb_values = []

for theeta in range(0, 360):
    g = 90-theeta
    if theeta == 180 or theeta == 0:
        continue
    alpha = adtan((AB*dsin(theeta))/(AD-AB*dcos(theeta)))
    BD = (AB*dsin(theeta))/dsin(alpha)
    gamma = adcos((BD**2+CD**2-BC**2)/(2*BD*CD))
    O_Angle = 180-(alpha+gamma)
    p = 90-O_Angle
    m_1 = adsin((CD*dsin(O_Angle)-(AB*dsin(theeta)))/BC)
    m = 90-m_1

    Vbe = Omega*(AB/100)
    Vcb = (Vbe*dsin(g)-dtan(p)*Vbe*dcos(g))/(dtan(p)*dcos(m)-dsin(m))
    Vce = (Vcb*dcos(m)+Vbe*dcos(g))/dcos(p)

    input_angles.append(theeta)
    output_angles.append(round(O_Angle, 8))
    v_ce_values.append(round(Vce, 10))
    v_be_values.append(round(Vbe, 10))
    v_cb_values.append(round(Vcb, 10))

    print(
        f'Input Angle: {theeta} | Output Angle: {str(round(O_Angle, 8)).ljust(12, "0")} | V_ce: {str(round(Vce, 10)).ljust(15, "0")} | V_cb : {str(round(Vcb, 10)).ljust(15, "0")}')

plt.plot(input_angles, v_ce_values, label="V_ce")
plt.show()
