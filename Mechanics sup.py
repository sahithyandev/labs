import math
def adsin(value):
    angle=math.asin((value))
    rd=180/math.pi
    return round(angle*rd,10)
def dsin(angle):
    dd=math.pi/180
    return round(math.sin((angle)*dd),10)
def adcos(value):
    angle=math.acos((value))
    rd=180/math.pi
    return round(angle*rd,10)
def dcos(angle):
    dd=math.pi/180
    return round(math.cos((angle)*dd),10)
def dtan(angle):
    dd=math.pi/180
    return round(math.tan((angle)*dd),10)
def adtan(value):
    angle=math.atan((value))
    rd=180/math.pi
    return round(angle*rd,10)

AB=eval(input('Enter AB:'))
BC=eval(input('Enter BC:'))
CD=eval(input('Enter CD:'))
AD=eval(input('Enter AD:'))

Omega=eval(input('Enter Angular Velocity:'))

for theeta in range(0,360):
    g=90-theeta
    if theeta==180 or theeta==0:continue
    alpha=adtan((AB*dsin(theeta))/(AD-AB*dcos(theeta)))
    BD=(AB*dsin(theeta))/dsin(alpha)
    gamma=adcos((BD**2+CD**2-BC**2)/(2*BD*CD))
    O_Angle=180-(alpha+gamma)
    p=90-O_Angle
    m_1=adsin((CD*dsin(O_Angle)-(AB*dsin(theeta)))/BC)
    m=90-m_1
    Vbe=Omega*(AB/100)
    Vcb=(Vbe*dsin(g)-dtan(p)*Vbe*dcos(g))/(dtan(p)*dcos(m)-dsin(m))
    Vce=(Vcb*dcos(m)+Vbe*dcos(g))/dcos(p)
    print(f'Input Angle: {theeta} Output Angle : {O_Angle} Vce : {Vce} Vcb : {Vcb}')
