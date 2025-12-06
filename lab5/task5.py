import time
import threading
import multiprocessing
import asyncio
import requests


def io_task(name, duration):
    """I/O-bound задача"""
    time.sleep(duration)
    return f"{name} completed"


async def async_io_task(name, duration):
    """Асинхронная I/O-bound задача"""
    await asyncio.sleep(duration)
    return f"{name} completed"


def sync_execution(tasks):
    """Синхронное выполнение"""
    results = []
    for name, duration in tasks:
        results.append(io_task(name, duration))
    return results


def threaded_execution(tasks):
    """Многопоточное выполнение"""
    results = []
    lock = threading.Lock()

    def worker(name, duration):
        result = io_task(name, duration)
        with lock:
            results.append(result)

    threads = []
    for name, duration in tasks:
        thread = threading.Thread(target=worker, args=(name, duration))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return results


def multiprocess_execution(tasks):
    """Многопроцессное выполнение"""
    with multiprocessing.Pool() as pool:
        results = pool.starmap(io_task, tasks)
    return results


async def async_execution(tasks):
    """Асинхронное выполнение"""
    async_tasks = [async_io_task(name, duration) for name, duration in tasks]
    return await asyncio.gather(*async_tasks)


def task5_performance_comparison():
    """
    Задача: Сравните производительность разных подходов.

    Набор I/O-bound задач (имитация):
    1. "Task1" - 2 секунды
    2. "Task2" - 3 секунды
    3. "Task3" - 1 секунда
    4. "Task4" - 2 секунды
    5. "Task5" - 1 секунда

    Требуется:
    - Реализовать выполнение одним потоком
    - Реализовать выполнение несколькими потоками
    - Реализовать выполнение несколькими процессами
    - Реализовать асинхронное выполнение
    - Сравнить время выполнения каждого подхода
    - Сделать выводы о эффективности
    """
    tasks = [("Task1", 2), ("Task2", 3), ("Task3", 1), ("Task4", 2), ("Task5", 1)]

    # Синхронное выполнение
    print("=== СИНХРОННОЕ ВЫПОЛНЕНИЕ ===")
    start_time = time.time()
    sync_results = sync_execution(tasks)
    sync_time = time.time() - start_time
    print(f"Время: {sync_time:.2f} сек")
    print(f"Результаты: {sync_results}")

    # Многопоточное выполнение
    print("\n=== МНОГОПОТОЧНОЕ ВЫПОЛНЕНИЕ ===")
    start_time = time.time()
    thread_results = threaded_execution(tasks)
    thread_time = time.time() - start_time
    print(f"Время: {thread_time:.2f} сек")
    print(f"Результаты: {thread_results}")

    # Многопроцессное выполнение
    print("\n=== МНОГОПРОЦЕССНОЕ ВЫПОЛНЕНИЕ ===")
    start_time = time.time()
    process_results = multiprocess_execution(tasks)
    process_time = time.time() - start_time
    print(f"Время: {process_time:.2f} сек")
    print(f"Результаты: {process_results}")

    # Асинхронное выполнение
    print("\n=== АСИНХРОННОЕ ВЫПОЛНЕНИЕ ===")
    start_time = time.time()
    async_results = asyncio.run(async_execution(tasks))
    async_time = time.time() - start_time
    print(f"Время: {async_time:.2f} сек")
    print(f"Результаты: {async_results}")

    print("\n=== АНАЛИЗ РЕЗУЛЬТАТОВ ===")
    print(f"Синхронное время: {sync_time:.2f} сек")
    print(f"Многопоточное время: {thread_time:.2f} сек")
    print(f"Многопроцессное время: {process_time:.2f} сек")
    print(f"Асинхронное время: {async_time:.2f} сек")

    print("\n=== ВЫВОДЫ ===")
    print("Для I/O-bound задач (ожидание ввода-вывода):")
    print(
        "1. Асинхронное выполнение наиболее эффективно, так как позволяет переключаться между задачами во время ожидания")
    print("2. Многопоточное выполнение также эффективно благодаря возможности параллельного ожидания")
    print("3. Многопроцессное выполнение менее эффективно из-за накладных расходов на создание процессов")
    print("4. Синхронное выполнение наименее эффективно, так как задачи выполняются последовательно")


# Запуск задачи
if __name__ == "__main__":
    task5_performance_comparison()