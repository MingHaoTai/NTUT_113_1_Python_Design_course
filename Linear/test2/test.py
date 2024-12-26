from sympy import symbols, Eq, solve

# 定義變數
x = symbols('x')

# 定義方程式
eq = Eq(x**2 - 5*x + 6, 0)

# 求解方程式
solutions = solve(eq, x)

print("解：")
for sol in solutions:
    print(f"x = {sol}")
