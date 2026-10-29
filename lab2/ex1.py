S = "ATCGCGTA"

A = S.count("A")
T = S.count("T")
C = S.count("C")
G = S.count("G")

Tm = 4 * (G + C) + 2 * (A + T)


print("S =", S)
print("A =", A, " T =", T, " C =", C, " G =", G)
print("Tm = 4 *", G + C, "+ 2 *", A + T, "=", Tm, "°C")