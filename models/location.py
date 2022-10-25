class Location():
    def __init__(self, id, name, address, location_id, customer_id):
        self.id = id
        self.name = name
        self.address = address
        self.location_id = location_id
        self.customer_id = customer_id

new_location = Location(4, "Nashville", "4789 Wine Blvd", 4, 5)
