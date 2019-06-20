#Write a function that takes two arguments, an amount in dollars and a tax percentage. Return an array with the tax amount in cents.

def tax_calc(dollar, tax):
    
    if tax and dollar == int or float:
        result_string = str((dollar * (tax/100)) * 100)
        tax_res = []
        j = 0
        for l in result_string:
            tax_res.append(l)
            j += 1
        return print(tax_res)

tax_calc(800, 25)