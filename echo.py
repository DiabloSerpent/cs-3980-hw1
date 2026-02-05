def echo(text: str, repetitions: int = 3) -> str:
    o = ""
    l = len(text)
    for r in range(repetitions, 0, -1):
        o += text[-r:l] + "\n"
    return o + "."


if __name__ == "__main__":
    text = input("Yell smth at a mountain: ")
    print(echo(text))
