from pulp import LpMaximize, LpProblem, LpVariable, lpSum

# Створення моделі
model = LpProblem(name="maximize-production", sense=LpMaximize)

# Змінні
x1 = LpVariable(name="lemonade", lowBound=0, cat="Continuous")  # Кількість виробленого лимонаду
x2 = LpVariable(name="fruit_juice", lowBound=0, cat="Continuous")  # Кількість виробленого фруктового соку

# Цільова функція
model += lpSum([x1, x2]), "Total Production"

# Обмеження на ресурси
model += (2*x1 + 1*x2 <= 100), "Water constraint"
model += (1*x1 <= 50), "Sugar constraint"
model += (1*x1 <= 30), "Lemon juice constraint"
model += (2*x2 <= 40), "Fruit puree constraint"

# Розв'язання задачі
model.solve()

# Виведення результатів
print(f"Максимальна кількість лимонаду: {x1.value()}")
print(f"Максимальна кількість фруктового соку: {x2.value()}")
print(f"Загальна кількість продуктів: {x1.value() + x2.value()}")
