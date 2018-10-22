from functools import wraps


def be_polite(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print("What a pleasure to meet you!")
        return fn(*args, **kwargs)

    return wrapper


@be_polite
def greet():
    print("My name is Matt.")


def main():
    greet()


if __name__ == '__main__':
    main()
