from sympy import symbols, cos, sin, series, solveset, Interval, S, N

x = symbols('x')

cos_series = series(cos(x), x, 0, 20).removeO()
sin_series = series(sin(x), x, 0, 20).removeO()

equation = cos_series - sin_series

section_1 = 5

section_2 = 10

real_solutions = solveset(equation, x, domain=S.Reals).intersection(Interval(section_1, section_2))

numerical_solutions = [N(sol) for sol in real_solutions]

print("ok")

f = open('points.txt', 'a', encoding='UTF-8')

text = f"""
x区間{section_1}~{section_2}の共有点

共有点
{real_solutions}

数値変換共有点
{numerical_solutions}

----------------------
"""

f.write(text)
f.close()
