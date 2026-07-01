#Dictionary Methods

Dictionary = {
    "Name": "John",
    "Age": 30,
    "City": "New York"
}

print("Name" in Dictionary.keys()) # Here it will check whether the key "Name" is present in the dictionary or not.
                                # It will return True if the key is present, otherwise it will return False.

print("John" in Dictionary.values())  # Here it will check whether the value "John" is present in the dictionary or not.

print("City" in Dictionary.items()) # Here it will check whether the item "City" is present in the dictionary or not.
                                    # it will inculde both keys and values in the check.
                                     # It will return True if the item is present, otherwise it will return False.

print(Dictionary.clear()) #. clear() - Removes all items from the dictionary

print(Dictionary.pop("Name")) #. pop() - Removes the item with the specified key name

print(Dictionary.popitem()) #. popitem() - Removes the last inserted item (in versions before 3.7, it removes an arbitrary item)

print(Dictionary.get("Age")) #. get() - Returns the value of the specified key

print(Dictionary.update({"Country": "USA"})) #. update() - Updates the dictionary with the specified key-value pairs