class Address():
    def __init__(self, line1, line2, city, state, zip, country):
        self.line1 = line1
        self.line2 = line2
        self.city = city
        self.state = state
        self.zip = zip
        self.country = country


def main():
    # This creates the address
    my_address = Address("701 N. C Street",
                         "Carver Science Building",
                         "Indianola",
                         "IA",
                         "50125",
                          "USA")


main()
print(Address())