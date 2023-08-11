algebra = input("Input your algebraic expression in the format (x^2): ")
caret_loc = ''
deriv = ''
coeff = ''
power = ''
x = ''
if '^' in algebra:
    caret_loc = algebra.index('^')
power = algebra[caret_loc+1:]
coeff = algebra[:caret_loc]
coeff_num = ''
for i in range(len(coeff)):
    if coeff[i].isdigit():
        coeff_num = coeff_num + coeff[i]
    elif coeff[i].isalpha:
        x = x + coeff[i]        
coeff_num = str(int(coeff_num)*int(power))
power = str(int(power) - 1)
deriv = deriv + coeff_num + x + '^' + power
print(f"The derivative of {algebra} is {deriv}")