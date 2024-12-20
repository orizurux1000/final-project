import random
from fractions import Fraction

def main():
    for _ in range(50):
        a = round(random.uniform(1.0,10.0),2)
        b = round(random.uniform(1.0,10.0),2)
        if a.is_integer():
            a = int(a)
        if b.is_integer():
            b = int(b)
        ans = round(a * b, 4)
        if ans.is_integer():
            ans = int(ans)
        print("{\"question\": \"", ans, " / ", b, "\", \"answer\": \"", a, "\"},", sep="")


def fraction(fraction):
    numerators = "⁰¹²³⁴⁵⁶⁷⁸⁹"
    denominators = "₀₁₂₃₄₅₆₇₈₉"
    super_num = ""
    sub_denom = ""
    numerator = str(fraction.numerator)
    denominator = str(fraction.denominator)
    for digit in numerator:
        super_num = super_num + numerators[int(digit)]
    for digit in denominator:
        sub_denom = sub_denom + denominators[int(digit)]
    return(f"{super_num}/{sub_denom}")


if __name__ == "__main__":
    main()
