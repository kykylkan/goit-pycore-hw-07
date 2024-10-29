from .Fields import *
from ..exceptions import *

class Record:
    def __validation(self, name):
        if not len(name):
            raise ValidationException("Name is required")

    def __init__(self, name: str) -> None:
        self.__validation(name)

        self.name = Name(name)
        self.phones: list[Record] = []
        self.birthday = None

    # add bortdhay in the record
    def add_birthday(self, value: str) -> None:
        if not value:
            raise ValidationException('Birthday is empty')

        if self.birthday == None:
            self.birthday = Birthday(value)
        else:
            raise ValidationException('Birthday already exists')

    # add phone in the list
    def add_phone(self, value: str) -> None:
        self.phones.append(Phone(value))

    # remove phone object from list
    def remove_phone(self, phone: str) -> bool:
        phoneIndex = None

        # find the phone position
        for key, item in enumerate(self.phones):
            if item.value == phone:
                phoneIndex = key
                break

        # remove phone by his position outside the loop
        if phoneIndex != None:
            del self.phones[phoneIndex]

            print(f"Phone {phone} was removed")
            return

        raise NotFoundException(f"Phone {phone} was not found")

    # update phone by number with a new one
    def edit_phone(self, original_phone: str, new_phone: str) -> bool:
        is_updated = False

        # manually go through the phones and update the correct one directly in phone object
        for key, item in enumerate(self.phones):
            if item.value == original_phone:
                self.phones[key] = Phone(new_phone)
                is_updated = True

                print(f"Phone {original_phone} was updated")
                break

        # I think this variant, is not good from in terms of perfomance
        # self.phones = list(map(lambda item: Phone(new_phone) if item.value == original_phone else Phone(item.value), self.phones))

        if not is_updated:
            raise NotFoundException(f"Phone {original_phone} was not found")

    # find and return phone(truthy) or False
    def find_phone(self, phone: str) -> str | bool:

        # in a huge list I think the best way it is a simple loop
        phoneItem = list(filter(lambda item: item.value == phone, self.phones))

        if len(phoneItem):
            return phoneItem.pop()

        raise NotFoundException(f"Phone {phoneItem} was not found")

    def __str__(self) -> str:
        birthday = self.birthday.value if self.birthday != None else '-'
        phones = '; '.join(p.value for p in self.phones)

        return f"Contact name: {self.name.value}, birthday: {birthday} phones: {phones}"
