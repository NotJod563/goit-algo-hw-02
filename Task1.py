import queue
import os

# Створення черги заявок
request_queue = queue.Queue()

# Лічильник для генерації унікальних ідентифікаторів заявок
request_id = 1

# Функція для очищення консолі
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Функція для додавання заявки до черги
def add_request():
    global request_id
    new_request = f"Заявка #{request_id}"
    request_queue.put(new_request)
    print(f"Додано: {new_request}")
    request_id += 1

# Функція для обробки однієї або більше заявок
def process_requests(count):
    if request_queue.empty():
        print("Черга порожня. Немає заявок для обробки.")
    else:
        actual_count = min(count, request_queue.qsize())  # Не більше, ніж залишилось у черзі
        processed_requests = []
        for _ in range(actual_count):
            request = request_queue.get()
            processed_requests.append(request)
        
        print(f"\n{actual_count} заявок оброблено.")
        print("Послідовність обробки заявок:")
        for request in processed_requests:
            print(f" - {request}")

# Функція для відображення черги заявок
def display_queue():
    if request_queue.empty():
        print("Черга порожня.")
    else:
        print("Поточна черга заявок:")
        for request in list(request_queue.queue):
            print(f" - {request}")

# Головний цикл програми
def main():
    while True:
        clear_console()  # Очищення консолі перед кожним відображенням меню
        display_queue()  # Відображення черги перед меню
        print("\nМеню:")
        print("1 - Додати заявку в чергу")
        print("2 - Обробити одну або більше заявок")
        print("3 - Вийти з програми\n")
        
        choice = input("Оберіть дію (1/2/3): ")

        if choice == '1':
            clear_console()
            add_request()
        elif choice == '2':
            if request_queue.empty():
                print("Черга порожня.")
            else:
                try:
                    count = int(input("Скільки заявок обробити? "))
                    if count > 0:
                        clear_console()
                        process_requests(count)
                    else:
                        print("Число має бути більше нуля.")
                except ValueError:
                    print("Введіть коректне число.")
        elif choice == '3':
            print("Завершення програми.")
            break
        else:
            print("Некоректний вибір. Спробуйте ще раз.")

        # Показуємо чергу та пропонуємо продовжити після виконання будь-якої дії
        print()
        display_queue()
        input("\nНатисніть Enter, щоб продовжити...")

if __name__ == "__main__":
    main()
