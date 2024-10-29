from dataclasses import dataclass
import re
from datetime import datetime
from ..exceptions import *

PHONE_PATTERN = re.compile("\d{10}")
BIRTHDAY_PATTERN = re.compile("\d{2}\.\d{2}\.\d{4}")


@dataclass
class Field:
    value: str

    def __str__(self) -> str:
        return str(self.value)


class Birthday(Field):
    def __init__(self, value: str) -> None:

        try:
            result = re.fullmatch(BIRTHDAY_PATTERN, value)

            if result == None:
                raise ValidationException("Invalid date format. Use DD.MM.YYYY")

            # simply checking the correct date with correct days range
            datetime.strptime(result.group(), "%d.%m.%Y")
        except ValueError:
            raise ValidationException("Invalid date format. Use DD.MM.YYYY")

        # I don't see neccessary to convert date intoo object on this step
        # value = datetime.strptime(value, '%d.%m.%Y').date

        # store in str because of our parent class
        super().__init__(value)


class Name(Field):
    def __init__(self, value: str) -> None:
        super().__init__(value)


class Phone(Field):
    def __init__(self, value: str) -> None:

        result = re.fullmatch(PHONE_PATTERN, value)

        if result == None:
            raise ValidationException("Phone should has 10 numbers")

        super().__init__(value)
