class Customer():
    def __init__(self, id, name, area, address,  customer_id, email = '', password = ''):
        self.id = id
        self.name = name
        self.area = area
        self.address = address
        self.email = email
        self.password = password
        self.customer_id = customer_id

new_customer = Customer(17, "Meh Boy", "Nashville East", "3729 Charlotte Pike", 17, 'meh@gmeh.com', 'password')
