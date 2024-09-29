from collections import deque

def is_palindrome(s):
    # Перетворюємо рядок на нижній регістр і видаляємо всі пробіли та небуквені символи
    s = ''.join(char.lower() for char in s if char.isalnum())

    # Створюємо двосторонню чергу
    d = deque(s)

    # Порівнюємо символи з обох кінців черги
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False  # Якщо символи не збігаються, рядок не є паліндромом

    return True  # Якщо всі символи збігаються, рядок є паліндромом

# Отримуємо вхідний рядок від користувача
input_str = input("Введіть рядок: ")

# Перевіряємо, чи є рядок паліндромом
if is_palindrome(input_str):
    print(f'"{input_str}" є паліндромом.')
else:
    print(f'"{input_str}" не є паліндромом.')
