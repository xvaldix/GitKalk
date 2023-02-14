class Actions:
    def add (var1, var2) -> float:
        return var1 + var2

    def div (var1, var2: float) -> float:
        return var1 / var2

    def sub (var1, var2):
        return var1 - var2

    def mul (var1, var2):
        return var1 * var2

class StrToFloat:
    def rep (var1):
        return float(var1.replace(",","."))

while True:
    znak = input("Podaj znak działania < +, -, *, / >: ")
    if znak == "+":
        var1 = input("Podaj pierwsza liczbe: ")
        var2 = input("Podaj druga liczbe: ")
        print(f"{(round(Actions.add(StrToFloat.rep(var1), StrToFloat.rep(var2)), 4))}")
    elif znak == "-":
        var1 = input("Podaj pierwsza liczbe: ")
        var2 = input("Podaj druga liczbe: ")
        print(f"{(round(Actions.sub(StrToFloat.rep(var1), StrToFloat.rep(var2)), 4))}")
    elif znak == "/":
        var1 = input("Podaj pierwsza liczbe: ")
        var2 = input("Podaj druga liczbe: ")
        while var2 == "0":
            var2 = input(str("Podaj druga liczbe, nie może to być zero: "))
        else:
            print(f"{(round(Actions.div(StrToFloat.rep(var1), StrToFloat.rep(var2)), 4))}")
    elif znak == "*":
        var1 = input("Podaj pierwsza liczbe: ")
        var2 = input("Podaj druga liczbe: ")
        print(f"{(round(Actions.mul(StrToFloat.rep(var1), StrToFloat.rep(var2)), 4))}")
    else:
        print(f"Wprowadzono błędny znak.")
    
    var3 = input(f"Czy chcesz wykonać kolejne działanie (y/n)?\n")
    if var3 != "y":
        break

print(f"Koniec")
