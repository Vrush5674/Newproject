import math


class calci(object):

    def add(self, num1, num2):
        result = num1 + num2
        print("{0} + {1} = {2}".format(num1, num2, result))

    def sub(self, num1, num2):
        result = num1 - num2
        print("{0} - {1} = {2}".format(num1, num2, result))

    def mul(self, num1, num2):
        result = num1 * num2
        print("{0} * {1} = {2}".format(num1, num2, result))

    def div(self, num1, num2):
        result = num1 / num2
        print("{0} / {1} = {2}".format(num1, num2, result))

    def sinrad(self, num):
        result = math.sin(num)
        print("Sine (%f) = %f" % (num, result))

    def cosrad(self, num):
        result = math.cos(num)
        print("Cosine(%f) = %f" % (num, result))

    def tanrad(self, num):
        result = math.tan(num)
        print("Tan(%f) = %f" % (num, result))

    def cosecrad(self, num):
        result = 1 / (math.sin(num))
        print("Sine(%f = %f" % (num, result))

    def secrad(self, num):
        result = 1 / (math.cos(num))
        print("Sec(%f) = %f" % (num, result))

    def cotrad(self, num):
        result = 1 / (math.tan(num))
        print("Cot(%f) = %f" % (num, result))

    def sindeg(self, num):
        result = math.sin(math.radians(num))
        print("Sin(%f) in degrees = %f" % (num, result))

    def cosdeg(self, num):
        result = math.cos(math.radians(num))
        print("Cos(%f) in degrees = %f" % (num, result))

    def tandeg(self, num):
        result = math.tan(math.radians(num))
        print("Tan(%f) in degrees = %f" % (num, result))

    def cosecdeg(self, num):
        result = 1 / (math.sin(math.radians(num)))
        print("Cosec(%f) in degrees = %f" % (num, result))

    def secdeg(self, num):
        result = 1 / (math.cos(math.radians(num)))
        print("Sec(%f) in degrees = %f" % (num, result))

    def cotdeg(self, num):
        result = 1 / (math.tan(math.radians(num)))
        print("Cot(%f) in degrees = %f" % (num, result))

    def ln(self, num):
        result = math.log(num)
        print("ln(%f) = %f" % (num, result))

    def logten(self, num):
        result = math.log10(num)
        print("log10(%f) = %f" % (num, result))

    def logbasex(self, num, x):
        result = math.log(num, x)
        print("log base(%f)(%f) = %f" % (x, num, result))

    def squareroot(self, num):
        result = math.sqrt(num)
        print("Square Root(%f) = %f " % (num, result))

    def pie(self):
        print('pi = ', math.pi)

    def powerof(self, num, raiseby):
        result = math.pow(num, raiseby)
        print("%f ^ (%f) = %f" % (num, raiseby, result))


calc = calci()
print('welcome to casio')
print("Here's a list of choices")
print('*' * 60)
print("1 : Addition  \t\t\t\t12 : Sine in degrees")
print("2 : Subtraction \t\t\t13 : Cosine in degrees")
print("3 : Multiplication\t\t\t14 : Tan in degrees")
print("4 : Division  \t\t\t\t15 : Cosecant in degrees")
print("5 : Sine in radians\t\t\t16 : Secant in degrees")
print("6 : Coisne in radians\t\t17 : Cot in degrees")
print("7 : Tan in radians\t\t\t18 : Natural log")
print("8 : Cosecant in radians\t\t19 : Base 10 log")
print("9 : Secant in radians\t\t20 : Log base 'x'")
print("10 : Cot in radians\t\t\t21 : Square root")
print("11 : pi \t\t\t\t\t22 : Power of")
print('-' * 40, '*' * 60, '-' * 40)
choice = ""
while True:
    try:
        choice = int(input('enter a number of your choice from the above list : '))
    except:
        print("Enter a valid number")

    if choice == 1:
        n1 = float(input('enter the first number to add : '))
        n2 = float(input('enter the second number to add : '))
        calc.add(n1, n2)
    elif choice == 2:
        n1 = float(input('enter the first number to subtract : '))
        n2 = float(input('enter the second number to subtract : '))
        calc.sub(n1, n2)
    elif choice == 3:
        n1 = float(input('enter the first number to multiply : '))
        n2 = float(input('enter the second number to multiply : '))
        calc.mul(n1, n2)
    elif choice == 4:
        n1 = float(input('enter the first number to divide : '))
        n2 = float(input('enter the second number to divide : '))
        calc.div(n1, n2)
    elif choice == 5:
        n = float(input('enter a number to find its sine in rad: '))
        calc.sinrad(n)
    elif choice == 6:
        n = float(input('enter a number to find its cos in rad: '))
        calc.cosrad(n)
    elif choice == 7:
        n = float(input('enter a number to find its tan in rad : '))
        calc.tanrad(n)
    elif choice == 8:
        n = float(input('enter a number to find its cosec in rad : '))
        calc.cosecrad(n)
    elif choice == 9:
        n = float(input('enter a number to find its sec in rad : '))
        calc.secrad(n)
    elif choice == 10:
        n = float(input('enter a number to find its cot in rad : '))
        calc.cotrad(n)
    elif choice == 11:
        calc.pie()
    elif choice == 12:
        n = float(input('enter a number to find its sine in deg : '))
        calc.sindeg(n)
    elif choice == 13:
        n = float(input('enter a number to find its cos in deg : '))
        calc.cosdeg(n)
    elif choice == 14:
        n = float(input('enter a number to find its tan in deg : '))
        calc.tandeg(n)
    elif choice == 15:
        n = float(input('enter a number to find its cosec in deg : '))
        calc.cosecdeg(n)
    elif choice == 16:
        n = float(input('enter a number to find its sec in deg : '))
        calc.secdeg(n)
    elif choice == 17:
        n = float(input('enter a number to find its cot in deg : '))
        calc.cotdeg(n)
    elif choice == 18:
        n = float(input('enter a number to find its natural deg : '))
        calc.ln(n)
    elif choice == 19:
        n = float(input('enter a number to find its log to base 10 : '))
        calc.logten(n)
    elif choice == 20:
        base = float(input('enter base value : '))
        n = float(input('enter a number to find its log to the given base value: '))
        calc.logbasex(n, base)
    elif choice == 21:
        n = float(input('enter a number to find its square root : '))
        calc.squareroot(n)
    elif choice == 22:
        n = float(input('enter a number  : '))
        po = float(input('enter its power : '))
        calc.powerof(n, po)

    else:
        print("WARNING : Enter a valid input from the list above")

