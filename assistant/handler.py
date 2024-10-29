from .notebook import *

# handling errors through decorators
def input_error(func):
    def inner(*args, **kwars):
        try:
            return func(*args, **kwars)
        except NotFoundException as e:
            return f"{e}"
        except ValidationException as e:
            return f"{e}"
        except ValueError:
            return "Give me the correct data please."
        except IndexError:
            return "Enter user name."
        except KeyError:
            return "Please, enter the correct arguments for the command."

    return inner


@input_error
def parse_input(user_input: str) -> tuple[str, list]:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()

    return cmd, *args


@input_error
def add_contact(args: list, book: AddressBook) -> str:
    name, phone, *_ = args
    record = book.find(name, True)
    operation_type = "updated"

    if record is None:
        record = Record(name)
        book.add_record(record)
        operation_type = "added"
    
    if phone:
        record.add_phone(phone)

    return f"Contact {operation_type}."

@input_error
def add_birthday(args: list, book: AddressBook) -> str:
    name, birthday, *_ = args
    record = book.find(name)
    
    record.add_birthday(birthday)
    
    return f"Birthday adedd."
    
@input_error
def show_birthday(args: list, book: AddressBook) -> str:
    name, *_ = args
    record = book.find(name)

    return f"{record.birthday.value if record.birthday else 'Empty'}"

@input_error
def change_contact(args: list, book: AddressBook) -> str:
    name, original_phone, new_phone, *_ = args
    record = book.find(name)

    record.edit_phone(original_phone, new_phone)
        
    return "Contact updated."


@input_error
def show_contact(args: list, book: AddressBook) -> str:
    name, *_ = args
    record = book.find(name)

    phones = '\n'.join(p.value for p in record.phones)

    return f"{phones}"


@input_error
def show_all_contacts(book: AddressBook) -> str:
    data = "\n".join([f"{value}\n" for value in book.values()])

    return data if len(data) else 'Empty' 

@input_error
def show_all_birthdays(book: AddressBook) -> str:
    data = book.get_upcoming_birthdays()

    return data if len(data) else 'Empty'
