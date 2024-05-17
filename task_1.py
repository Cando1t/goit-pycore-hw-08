import pickle

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, name):
        self.contacts = [c for c in self.contacts if c.name != name]

    def get_contacts(self):
        return self.contacts

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()

def main():
    book = load_data()

    while True:
        print("\n1. Додати контакт")
        print("2. Видалити контакт")
        print("3. Вивести всі контакти")
        print("4. Вийти з програми")

        choice = input("Виберіть опцію: ")

        if choice == "1":
            name = input("Введіть ім'я контакту: ")
            phone = input("Введіть номер телефону: ")
            contact = Contact(name, phone)
            book.add_contact(contact)
            print("Контакт успішно додано!")

        elif choice == "2":
            name = input("Введіть ім'я контакту, який потрібно видалити: ")
            book.remove_contact(name)
            print("Контакт успішно видалено!")

        elif choice == "3":
            contacts = book.get_contacts()
            if contacts:
                print("Список контактів:")
                for contact in contacts:
                    print(f"{contact.name}: {contact.phone}")
            else:
                print("У вас немає контактів у списку.")

        elif choice == "4":
            save_data(book)
            print("Дані успішно збережено. До побачення!")
            break

        else:
            print("Неправильний вибір опції. Спробуйте ще раз.")

if __name__ == "__main__":
    main()