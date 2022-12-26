def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except IndexError:
            return "Give me name and phone please"
        except ValueError:
            return "Incorrectly entered command"
        except KeyError:
            return "Enter user name"

    return wrapper


def greeting(*args):
    return "Hello! How can I help you?"


def to_exit(*args):
    return "Good bye!"


contacts = {}


@input_error
def add_contact(*args):
    name = args[0]
    phone = args[1]
    contacts[name] = phone
    return f"This is ADD, name {name}, phone {phone}"


@input_error
def change_phone(*args):
    name = args[0]
    phone = args[1]
    if name in contacts:
        contacts[name] = phone
        return f"{name} has new number - {phone}"
    else:
        return f"{name} name not exist in contacts"


@input_error
def find_phone(*args):
    return contacts[args[0]]


@input_error
def show_all(*args):
    return "\n".join([f"{key}: {value}" for key, value in contacts.items()]) if len(
        contacts) > 0 else 'Contacts are empty'


COMMANDS = {
    greeting: "hello",
    add_contact: "add",
    change_phone: "change",
    find_phone: "phone",
    show_all: "show all",
    to_exit: "exit"
}


def command_parser(user_input: str):
    for command, key_word in COMMANDS.items():
        if user_input.startswith(key_word):
            return command, user_input.replace(key_word, "").strip().split(" ")
    return None, None


def main():
    while True:
        user_input = input(">>>")
        if user_input == ".":
            break
        command, data = command_parser(user_input)

        if not command:
            print("Sorry, unknown command")
        else:
            print(command(*data))


if __name__ == "__main__":
    main()
