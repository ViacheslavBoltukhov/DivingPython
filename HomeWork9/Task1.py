'''
Вася совсем заскучал на работе и решил побаловаться с кодом проекта. Он
написал надоедливый декоратор, который при вызове декорируемой функции
спрашивает у пользователя «Как дела?», вне зависимости от ответа пишет что-то
вроде «А у меня не очень!» и только потом запускает саму функцию. Правда, после
такой выходки Васю чуть не уволили с работы.
Реализуйте такой же декоратор и проверьте его работу на нескольких функциях.
Пример кода:
@how_are_you
def test():
print('<Тут что-то происходит...>')
test()
Результат:
Как дела? Хорошо.
А у меня не очень! Ладно, держи свою функцию.
<Тут что-то происходит...>
'''
from functools import wraps
from typing import Callable, Any


def how_are_you(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        input('Как дела? ')
        print('А у меня не очень! Ладно, держи свою функцию.')
        result = func(*args, **kwargs)
        return result

    return wrapper


@how_are_you
def test() -> None:
    print('<Тут что-то происходит...>')


@how_are_you
def another_function() -> None:
    print('Еще один тестовый вывод.')


if __name__ == "__main__":
    test()
    another_function()
