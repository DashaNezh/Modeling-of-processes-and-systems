import random

class CoffeeMachine:
    def __init__(self, transition_probabilities):
        # Состояния машины
        self.states = ['Покой', 'Ожидание ввода', 'Ожидание объема', 'Ожидание выбора напитка',
                       'Приготовление кофе']
        self.current_state = 'Покой'

        # Матрица переходов состояний с вероятностями
        self.transition_probabilities = transition_probabilities

    def process_signal(self, signal):
        # Переход к новому состоянию с учётом вероятностей
        if signal in self.transition_probabilities[self.current_state]:
            transitions = self.transition_probabilities[self.current_state][signal]
            # Случайный выбор состояния на основе вероятностей
            next_state = random.choices(list(transitions.keys()), weights=list(transitions.values()))[0]
            self.current_state = next_state
            print(f"Состояние изменилось на: {self.current_state} | Вероятность: {transitions[self.current_state]}")
        else:
            print(f"Сигнал '{signal}' не поддерживается в состоянии '{self.current_state}'.")

    def get_state(self):
        # Получить текущее состояние машины
        return self.current_state

    def get_probality(self):
        return transition_probabilities.get(self.current_state).values().mapping


# Пример данных из таблицы
transition_probabilities = {
    'Покой': {
        'включить капучино': {'Ожидание объема': 0.99, 'Ожидание выбора напитка': 0.01},
        'включить латте': {'Ожидание объема': 0.99, 'Ожидание выбора напитка': 0.01},
        'выбрать 200 мл': {'Ожидание выбора напитка': 0.8, 'Приготовление кофе': 0.2},
        'выбрать 320 мл': {'Ожидание выбора напитка': 0.9, 'Приготовление кофе': 0.1},
    },
    'Ожидание объема': {
        'выбрать 200 мл': {'Приготовление кофе': 1.0},
        'выбрать 320 мл': {'Приготовление кофе': 1.0}
    },
    'Ожидание выбора напитка': {
        'включить капучино': {'Приготовление кофе': 1.0},
        'включить латте': {'Приготовление кофе': 1.0}
    },
    'Приготовление кофе': {
        'начать': {'Покой': 1.0}
    }
}

if __name__ == "__main__":
    coffee_machine = CoffeeMachine(transition_probabilities)

    print("Добро пожаловать в систему кофемашины. Введите команду для управления машиной.")
    print(
        "Доступные сигналы: 'включить капучино', 'включить латте', 'выбрать 200 мл', 'выбрать 320 мл', 'начать', 'выход'.")

    while True:
        print(f"\nТекущее состояние: {coffee_machine.get_state()}")
        print("Доступные состояние машины и их вероятность:")
        for state in coffee_machine.get_probality():
            print(f"- Состояние: {state} | Вероятность: {coffee_machine.get_probality()[state]}")
        signal = input("Введите сигнал: ").strip().lower()

        if signal == 'выход':
            print("Выход из системы кофемашины.")
            break

        coffee_machine.process_signal(signal)
