from gameparts import Board
from gameparts.exceptions import CellOccupiedError, FieldIndexError

def save_result(result):
    with open ('results.txt', 'a') as file:
        file.write(result + '\n')

def main():
    game = Board()
    # Первыми ходят крестики.
    current_player = 'X'
    # Это флаговая переменная. По умолчанию игра запущена и продолжается.
    running = True
    game.display()
    # Тут запускается основной цикл игры.
    while running:
        print(f'Ход делают {current_player}')
        # В этом блоке содержатся операции, которые могут вызвать исключение.
        # Запускается бесконечный цикл.
        while True:
            try:
                # Пользователь вводит значение номера строки.
                row = int(input('Введите номер строки: '))
                # Если введённое число меньше 0 или больше
                # или равно game.field_size...
                if row < 0 or row >= game.field_size:
                # ...выбрасывается собственное исключение FieldIndexError.
                    raise FieldIndexError
                column = int(input('Введите номер столбца: '))
                # Если введённое число меньше 0 или больше
                # или равно game.field_size...
                if column < 0 or column >= game.field_size:
                # ...выбрасывается собственное исключение FieldIndexError.
                    raise FieldIndexError
                if game.board[row][column] != ' ':
                    # Вот тут выбрасывается новое исключение.
                    raise CellOccupiedError
                # Если возникает исключение FieldIndexError...
            except FieldIndexError:
            # ...выводятся сообщения...
                print(
                    'Значение должно быть неотрицательным и меньше '
                    f'{game.field_size}.'
                )
                print('Пожалуйста, введите значения для строки и столбца заново.')
                # ...и цикл начинает свою работу сначала,
                # предоставляя пользователю ещё одну попытку ввести данные.
                continue
                # Если в блоке try исключения не возникло...
            except ValueError:
                print ('Буквы вводить нельзя. Только числа.')
                print ('Пожалуйста, введите значения для строки и столбца заново.')

                continue
            except Exception as e:
                print(f'Возникла ошибка: {e}')
            else:
            # ...значит, введённые значения прошли все проверки
            # и могут быть использованы в дальнейшем.
            # Цикл прерывается.
                break
        game.make_move(row, column, current_player)
        game.display()
        # После каждого хода надо делать проверку на победу и на ничью.
        if game.check_win(current_player):
            result = f'Победили {current_player}'
            print(result)
            save_result(result)
            running = False
            
        elif game.is_board_full():
            result = 'Ничья!'
            print(result)
            save_result(result)
            running = False
        # Тернарный оператор, через который реализована смена игроков.
        # Если current_player равен X, то новым значением будет O,
        # иначе — новым значением будет X.
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == '__main__':
    main()