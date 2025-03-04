class cli:


    def greetings() -> str:
        return '''Привет, ты запустил консольное приложение для трекинга своих задач'''


    def kaka(s):
        return f'Ты ввёл: {s}'


if __name__ == '__main__':
    
    print(cli.greetings())