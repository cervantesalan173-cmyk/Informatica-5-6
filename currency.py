def main():
    pesos = input("What do you have left in pesos? ")
    soles = input("What do you have left in soles? ")
    reais = input("What do you have left in reais? ")
    usd = pesos*0.00032 + soles*0.30+ reais*0.19
    print(f"USD:{usd}")

if __name__ == "__main__":
    main()
