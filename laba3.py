import numpy as np

# Параметры генератора
a = 1664525        # множитель
c = 1013904223     # приращение
m = 2**32          # модуль
X0 = 123456789     # начальное значение (seed)

def lcg(n, X0, a, c, m):
    """Генератор псевдослучайных чисел на основе ЛКГ."""
    numbers = []
    X = X0
    for _ in range(n):
        X = (a * X + c) % m
        numbers.append(X / m)  # Нормализуем значения в диапазон [0, 1]
    return np.array(numbers)

# Генерация чисел
N = 1_000_000
generated_numbers = lcg(N, X0, a, c, m)

# 1. Определение длины периода
unique_numbers = set()
for num in generated_numbers:
    if num in unique_numbers:
        break
    unique_numbers.add(num)
period_length = len(unique_numbers)

# 2. Характеристики распределения (для нашего генератора)
mean = np.mean(generated_numbers)
variance = np.var(generated_numbers)

# 3. Частотный тест для диапазона [0.5 - delta, 0.5 + delta]
delta = 0.2887  # Ширина интервала 0.577
interval_min = 0.5 - delta
interval_max = 0.5 + delta
in_interval_count = np.sum((generated_numbers >= interval_min) & (generated_numbers <= interval_max))
frequency_test_result = (in_interval_count / N) * 100

# 4. Вероятность попадания в [0, 0.5] и [0.5, 1] (для нашего генератора)
lower_half_prob = np.sum(generated_numbers < 0.5) / N
upper_half_prob = np.sum(generated_numbers >= 0.5) / N

# Генерация чисел встроенным генератором numpy
python_generated = np.random.rand(N)

# Показатели для встроенного генератора
python_mean = np.mean(python_generated)
python_variance = np.var(python_generated)

# Частотный тест для встроенного генератора в диапазоне [0.5 - delta, 0.5 + delta]
python_in_interval_count = np.sum((python_generated >= interval_min) & (python_generated <= interval_max))
python_frequency_test_result = (python_in_interval_count / N) * 100

# Вероятность попадания в [0, 0.5] и [0.5, 1] для встроенного генератора
python_lower_half_prob = np.sum(python_generated < 0.5) / N
python_upper_half_prob = np.sum(python_generated >= 0.5) / N

# Вывод результатов
print(f"Длина периода (наш генератор): {period_length}")
print(f"Математическое ожидание (наш генератор): {mean}")
print(f"Дисперсия (наш генератор): {variance}")
print(f"Частотный тест для диапазона [{interval_min}, {interval_max}]: {frequency_test_result}% (Ожидалось около 57.7%)")
print(f"Чисел попало в интервал [{interval_min}, {interval_max}]: {in_interval_count}")
print(f"Вероятность для [0, 0.5] (наш генератор): {lower_half_prob}")
print(f"Вероятность для [0.5, 1] (наш генератор): {upper_half_prob}")

print("\n--- Сравнение со встроенным генератором ---")
print(f"Математическое ожидание (встроенный генератор): {python_mean}")
print(f"Дисперсия (встроенный генератор): {python_variance}")
print(f"Частотный тест для диапазона [{interval_min}, {interval_max}] (встроенный генератор): {python_frequency_test_result}%")
print(f"Чисел попало в интервал [{interval_min}, {interval_max}]: {python_in_interval_count}")
print(f"Вероятность для [0, 0.5] (встроенный генератор): {python_lower_half_prob}")
print(f"Вероятность для [0.5, 1] (встроенный генератор): {python_upper_half_prob}")
