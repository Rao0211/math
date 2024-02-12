from sympy import symbols, cos, sin, series, solveset, Interval, S, N

x = symbols('x')

cos_series = series(cos(x), x, 0, 20).removeO()
sin_series = series(sin(x), x, 0, 20).removeO()

equation = cos_series - sin_series

real_solutions = solveset(equation, x, domain=S.Reals).intersection(Interval(5, 10))

numerical_solutions = [N(sol) for sol in real_solutions]

print("共有点:", real_solutions)
print("数値に変換した共有点:", numerical_solutions)