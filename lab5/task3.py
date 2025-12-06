import multiprocessing
import time
import math


def calculate_factorial(n):
    """
    Вычисляет факториал числа (CPU-intensive операция)
    """
    print(f"Начало вычисления факториала {n}!")
    result = math.factorial(n)
    print(f"Завершено вычисление факториала {n}! = {result}")
    return result


def calculate_prime(n):
    """
    Проверяет, является ли число простым
    """
    print(f"Начало проверки числа {n} на простоту")

    if n < 2:
        result = False
    else:
        result = all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))

    print(f"Число {n} простое: {result}")
    return result


def worker(func_arg_pair):
    """Вспомогательная функция для выполнения задачи в процессе"""
    func, arg = func_arg_pair
    return func(arg)


def task3_multiprocess_calculations():
    """
    Задача: Реализуйте многопроцессные вычисления.
    Вычисления:
    1. Факториал 10000
    2. Факториал 8000
    3. Проверка числа 10000019 на простоту
    4. Проверка числа 10000033 на простоту

    Требуется:
    - Выполнить вычисления в отдельных процессах
    - Сравнить время с последовательным выполнением
    - Собрать и вывести результаты
    """
    calculations = [
        (calculate_factorial, 10000),
        (calculate_factorial, 8000),
        (calculate_prime, 10000019),
        (calculate_prime, 10000033)
    ]

    # Многопроцессное выполнение
    print("=== МНОГОПРОЦЕССНОЕ ВЫПОЛНЕНИЕ ===")
    start_time = time.time()

    # Используем ProcessPoolExecutor для более удобного управления
    with multiprocessing.Pool(processes=4) as pool:
        multiprocess_results = pool.map(worker, calculations)

    end_time = time.time()
    multiprocess_time = end_time - start_time

    # Синхронное выполнение для сравнения
    print("\n=== СИНХРОННОЕ ВЫПОЛНЕНИЕ ===")
    start_time = time.time()

    sync_results = []
    for func, arg in calculations:
        sync_results.append(func(arg))

    end_time = time.time()
    sync_time = end_time - start_time

    print(f"\nСравнение времени:")
    print(f"Многопроцессное: {multiprocess_time:.2f} сек")
    print(f"Синхронное: {sync_time:.2f} сек")
    if multiprocess_time > 0:
        print(f"Ускорение: {sync_time / multiprocess_time:.2f}x")
    else:
        print("Ускорение: N/A (время многопроцессного выполнения равно 0)")
    print(f"Результаты многопроцессного выполнения: {multiprocess_results}")
    print(f"Результаты синхронного выполнения: {sync_results}")


# Запуск задачи
if __name__ == "__main__":
    task3_multiprocess_calculations()