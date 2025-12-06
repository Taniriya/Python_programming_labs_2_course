import asyncio
import time
from datetime import datetime


async def scheduled_task(name, priority, duration):
    """
    Задача с приоритетом и временем выполнения

    Параметры:
    name (str): название задачи
    priority (int): приоритет (1 - высший)
    duration (float): время выполнения
    """
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Задача '{name}' (приоритет {priority}) начата")
    await asyncio.sleep(duration)
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Задача '{name}' завершена")
    return f"Результат {name}"


async def task6_async_scheduler():
    """
    Задача: Создайте асинхронный планировщик задач.

    Задачи:
    1. "Экстренная задача" - приоритет 1, длительность 1 сек
    2. "Важная задача" - приоритет 2, длительность 2 сек
    3. "Обычная задача A" - приоритет 3, длительность 3 сек
    4. "Обычная задача B" - приоритет 3, длительность 2 сек
    5. "Фоновая задача" - приоритет 4, длительность 5 сек

    Требуется:
    - Запустить задачи в порядке приоритета
    - Обеспечить выполнение высокоприоритетных задач первыми
    - Реализовать ограничение на одновременное выполнение (не более 2 задач)
    - Вывести порядок завершения задач
    """
    tasks_with_priority = [
        ("Экстренная задача", 1, 1),
        ("Важная задача", 2, 2),
        ("Обычная задача A", 3, 3),
        ("Обычная задача B", 3, 2),
        ("Фоновая задача", 4, 5)
    ]

    # Отсортируйте задачи по приоритету
    tasks_with_priority.sort(key=lambda x: x[1])

    # Реализуйте семафор для ограничения одновременного выполнения
    semaphore = asyncio.Semaphore(2)

    async def worker(task_info):
        async with semaphore:
            return await scheduled_task(*task_info)

    # Запустите задачи и соберите результаты
    tasks = [worker(task) for task in tasks_with_priority]
    results = await asyncio.gather(*tasks)

    print("\nВсе задачи завершены!")
    print("Результаты:", results)


asyncio.run(task6_async_scheduler())