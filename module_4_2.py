
# Определение внешней функции test_function
def test_function():
    # Определение внутренней функции inner_function
    def inner_function():
        print("Я в области видимости функции test_function")

    # Вызов внутренней функции внутри test_function
    inner_function()


# Вызов функции test_function
test_function()

# Попытка вызвать внутреннюю функцию вне test_function
try:
    inner_function()  # Это вызовет ошибку, потому что inner_function не видима за пределами test_function
except NameError as e:
    print(f"Ошибка: {e}")