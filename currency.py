def main():
    pesos = float(input("What do you have left in pesos? "))
    soles = float(input("What do you have left in soles? "))
    reais = float(input("What do you have left in reais? "))
    usd = pesos*0.00032 + soles*0.30 + reais*0.19
    mxn = pesos*183.87 + soles/0.20 + reais/0.31
    print(f"USD:{round(usd,2)}")
    print(f"mxn:{round(mxn,2)}")
if __name__ == "__main__":
    main()
