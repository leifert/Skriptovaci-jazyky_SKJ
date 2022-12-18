import math


class Person:
    def __init__(self, time_stamp, username, x, y, z):
        self.time_stamp = time_stamp
        self.username = username
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return self.username


def find_dangerous_contacts(file: str, max_distance: float):
    my_records = []
    with open(file, 'rt', encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        row = line.split(": ")
        my_parts = row[1].split(" ")
        time_stamp = int(row[0])
        username = my_parts[0]
        x = int(my_parts[1])
        y = int(my_parts[2])
        z = int(my_parts[3])
        my_records.append(Person(time_stamp, username, x, y, z))

    contacts_result = []

    for record in my_records:
        contacts = [item for item in my_records if item.username != record.username and item.time_stamp == record.time_stamp]
        for contact in contacts:
            contact_dist = math.sqrt(((contact.x - record.x) ** 2) + ((contact.y - record.y) ** 2) + ((contact.z - record.z) ** 2))
            if contact_dist <= max_distance:
                contacts_result.append((record.username, contact.username))
    contacts_result.sort()
    result = []
    for contact in contacts_result:
        if contact not in result and (contact[1], contact[0]) not in result:
            result.append(contact)
    return result



print(find_dangerous_contacts("contacts.txt", 5.0))


class VaccinationCenter:
    def __init__(self, vac_rooms, wait_rooms):
        self.vac_rooms = vac_rooms
        self.wait_rooms = wait_rooms
        self.patients_vac_room = []
        self.patients_wait_room = []
        self.patients_finished = []

    def vaccination_room_count(self):
        return len(self.patients_vac_room)

    def waiting_room_count(self):
        return len(self.patients_wait_room)

    def patient_finished_count(self):
        return len(self.patients_finished)

