print("Type the total amount of credit:")
CreditTotal = float(input())
print("Type the monthly payment:")
MonthlyPayment = float(input())
print("Type interest rate")
InterestRate = float(input())
Inf1 = 1.59282448436825
Inf2 = -0.453509101198007
Inf3 = 2.32467171712441
Inf4 = 1.26125440724877
Inf5 = 1.78252628571251
Inf6 = 2.32938454145522
Inf7 = 1.50222984223283
Inf8 = 1.78252628571251
Inf9 = 2.32884899407637
Inf10 = 0.616921348207244
Inf11 = 2.35229588637833
Inf12 = 0.337779545187098
Inf13 = 1.57703524727525
Inf14 = -0.292781442607648
Inf15 = 2.48619659017508
Inf16 = 0.267110317834564
Inf17 = 1.41795267229799
Inf18 = 1.05424326726375
Inf19 = 1.4805201044812
Inf20 = 1.57703524727525
Inf21 = -0.077420690314702
Inf22 = 1.16573339872354
Inf23 = -0.404186717638335
Inf24 = 1.49970852083123
CalcVar = CreditTotal/10

print("Month number 1:")
CreditLeft = (1 + ((Inf1 + InterestRate)/CalcVar)) * CreditTotal - MonthlyPayment
print(f"Your credit sum to pay is {CreditLeft}, it's {CreditTotal - CreditLeft} less than previous month").format(CreditLeft, CreditTotal - CreditLeft)
CreditTotal=CreditLeft