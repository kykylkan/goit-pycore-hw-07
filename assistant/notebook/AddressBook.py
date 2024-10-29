from collections import UserDict
from datetime import datetime, timedelta
from .Record import *

# store any record in book by user name
class AddressBook(UserDict):

    # store record
    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record

    # find record
    def find(self, name: str, can_create:bool=False) -> Record | None:
        if name in self.data:
            return self.data[name]
        elif not can_create:
            raise NotFoundException('Contact was not found')

    # delete record
    def delete(self, name: str) -> None:
        if name in self.data:
            del self.data[name]

    
    def get_upcoming_birthdays(self) -> list:
        birthdays = []
        today_date = datetime.today().date()

        for contact in self.data.values():
            if not contact.birthday:
                continue
            
            # set user birthday in current year
            contact_birthday = datetime.strptime(contact.birthday.value, "%d.%m.%Y").date().replace(year=today_date.year)

            # if birthday was, then skip it
            if(contact_birthday < today_date):
                continue

            day = contact_birthday.weekday()
            diff = (contact_birthday - today_date).days

            # checking birthday in next 7 days with current and collecting the data
            if(diff < 7):
                # set birthday on monday, if it will be on weekday 
                contact_birthday = contact_birthday + timedelta(days=(7 - day)) if day in [5,6] else contact_birthday
                birthdays.append({ 'name': contact.name.value, "birthday": datetime.strftime(contact_birthday, "%Y.%m.%d") })

        return birthdays
