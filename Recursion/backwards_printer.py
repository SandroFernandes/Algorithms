def backwards_printer(text):
    if len(text) == 0:
        return
    else:
        backwards_printer(text[1:])
        print(text[0], end="")


if __name__ == '__main__':
    while True:
        text = input('Type exit to exit\nEnter text to print backwards: ')
        if text == 'exit':
            break
        backwards_printer(text)
        print()
