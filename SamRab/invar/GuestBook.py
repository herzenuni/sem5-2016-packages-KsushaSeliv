class GuestBook:

    def __init__(self):
        self.guests = list()


    def add(self, name, surname, age, country):
        self.guests.append({"guests_name": name,
           "guests_surname": surname,
           "guests_age": age,
           "guests_country": country})
    
    def udal(self, name):
        for guests in self.guests:
            if guests.get("guests_country") == country: 
                self.guests.remove(guests) 

    def zapis(self):
        import json
        with open("./new_file.json", 'a') as file:
            json_data = { "all_guests": self.guests }
            file.write(json.dumps(json_data, indent=4))
            
if __name__ == "__main__":
    GuestBook = GuestBook()
    GuestBook.add("Ksenia", "Selivanova", 20, "ms.ksus@gmail.com")
    GuestBook.add("Ktoto", "Esho", 25, "ktoto@gmail.com")
    GuestBook.zapis()

