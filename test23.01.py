class Actions:
    def add (var1, var2) -> float:
        return var1 + var2

    def div (var1, var2: float) -> float:
        return var1 / var2

    def sub (var1, var2):
        return var1 - var2

    def mul (var1, var2):
        return var1 * var2

while True:
    znak = input("Podaj znak działania < +, -, *, / >: ")
    if znak == "+":
        var1 = float(input("Podaj pierwsza liczbe: "))
        var2 = float(input("Podaj druga liczbe: "))
        print(f"{Actions.add(var1, var2)}")
    elif znak == "-":
        var1 = float(input("Podaj pierwsza liczbe: "))
        var2 = float(input("Podaj druga liczbe: "))
        print(f"{Actions.sub(var1, var2)}")
    elif znak == "/":
        var1 = float(input("Podaj pierwsza liczbe: "))
        var2 = float(input("Podaj druga liczbe: "))
        while var2 == 0:
            var2 = float(input("Podaj druga liczbe, nie może to być zero: "))
        else:
            print(f"{Actions.div(var1, var2)}")
    elif znak == "*":
        var1 = float(input("Podaj pierwsza liczbe: "))
        var2 = float(input("Podaj druga liczbe: "))
        print(f"{Actions.mul(var1, var2)}")
    else:
        print(f"Wprowadzono błędny znak.")
    
    var3 = input(f"Czy chcesz wykonać kolejne działanie (y/n)?\n")
    if var3 != "y":
        break

print(f"Koniec")
