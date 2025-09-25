def hello(name, lang):
    greetings={
        "English":"Hello",
        "Spanish":"Hola",
        "German":"Hallo"
    }
    msg = f"{greetings.get(lang, 'Hello')}, {name}!"
    print( args.lang.capitalize()) 
    print(msg)
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personal greeting."
    )

    parser.add_argument(
        "-n", "--name",metavar="name",
        required=True,
        help="the personal greeting"
    )
    parser.add_argument(
        "-l", "--lang",metavar="lang",
        required=True,choices=["English", "Spanish", "German"],
        help="the language of the greeting"
    )
    args = parser.parse_args()


    hello(args.name, args.lang)