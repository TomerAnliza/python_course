def main() -> None:
    print("Hello from demo!")

    i = 0
    while i < 3:
        i += 1
        if i == 4:
            print("4")
            break
    else:
        print("break was not triggered")


def my_empty_func():
    pass