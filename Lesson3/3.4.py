def x_pow_fun (x, y):
    try:
        res = x ** y
    except TypeError:
        return "Enter a float number and a negative power"
    return res
print(x_pow_fun(x=float(input("enter x: ")), y=int(input("enter -y: "))))
