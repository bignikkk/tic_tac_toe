### Игра "Крестики-нолики"

"Крестики-нолики" - классическая игра, реализованная на Python с использованием библиотеки Pygame. Два игрока по очереди ставят крестики и нолики на поле размером 3×3. Первый игрок, который сможет выстроить три своих знака по горизонтали, вертикали или диагонали, выигрывает. Результаты игры сохраняются в файл results.txt.

### Автор:

Автор: Nikita Blokhin
GitHub: github.com/bignikkk

### Технологии:

Python
Pygame
ООП

### Как развернуть проект локально:

```
git clone https://github.com/bignikkk/tic_tac_toe
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Запустить игру командой:

```
python3 copy_game.py
```