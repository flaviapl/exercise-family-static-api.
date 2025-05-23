
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
                {
                "id" : self._generateId(),
                "first_name" :  "John Jackson",
                "age" : 33,
                "lucky_numbers": [7, 13, 22]
                },
                {
                "id" : self._generateId(),
                "first_name" :  "Jane Jackson",
                "age" : 35,
                "lucky_numbers": [10, 14, 3]
                },
                {
                "id" : self._generateId(),
                "first_name" :  "Jimmy Jackson",
                "age" : 5,
                "lucky_numbers": [1]
                }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    # member = {
    #             "first_name" :  "Superman",
    #             "age" : 30,
    #             "lucky_numbers": [7, 1, 22]
    #             },

    def add_member(self, member):
        if "id" not in member:
            member["id"] = self._generateId()
        if "last_name" not in member:
            member["last_name"] = self.last_name
        self._members.append(member)
        return member
        


    def delete_member(self, id):
        # fill this method and update the return
        for index, member in enumerate(self._members):
            if member.get("id") == id:
                deleted_member = self._members.pop(index)
                return deleted_member
        return None

    def get_member(self, id):

        for member in self._members:
            if member["id"] == id:                          # Accesso diretto alla chiave "id" di member(che è un oggetto)
                return member
        return None
        
        pass

    # Restituisce la lista con tutti i membri della famiglia
    def get_all_members(self):
        return self._members
    

