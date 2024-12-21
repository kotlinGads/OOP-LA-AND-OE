class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def __str__(self):
        return f"{self.brand} {self.model} {self.price}"

phones = []

while True:
    print("\nMenu:")
    print("1. Create Phone")
    print("2. Modify Phone")
    print("3. Delete Phone")
    print("4. View Phones")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        brand = input("Enter brand: ")
        model = input("Enter model: ")
        price = (input("Enter price: "))
        phones.append(Phone(brand, model, price))
    elif choice == '2':
        if not phones:
            print("No phones to modify.")
            continue
        for cp, phone in enumerate(phones):
            print(f"{cp+1}. {phone}")
        index = int(input("Enter phone number to modify: ")) - 1
        if 0 <= index < len(phones):
            phones[index].brand = input("Enter new brand (leave blank to keep): ") or phones[index].brand
            phones[index].model = input("Enter new model (leave blank to keep): ") or phones[index].model
            new_price = input("Enter new price (leave blank to keep): ")
            phones[index].price = (new_price) if new_price else phones[index].price

        else:
            print("Invalid phone number.")

    elif choice == '3':
        if not phones:
            print("No phones to delete.")
            continue
        for cp, phone in enumerate(phones):
            print(f"{cp+1}. {phone}")
        index = int(input("Enter phone number to delete: ")) - 1
        if 0 <= index < len(phones):
            del phones[index]
        else:
            print("Invalid phone number.")
    elif choice == '4':
        if not phones:
            print("No phones in the list.")
        else:
            for phone in phones:
                print(phone)
    elif choice == '5':
        break
    else:
        print("Invalid choice.")