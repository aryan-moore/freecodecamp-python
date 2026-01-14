class HashTable:

    def __init__(self):
        self.collection = {}

    #Basic Hashing Method
    def hash(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total

    def add(self, key, value):
        hashed = self.hash(key)
        print(hashed)
        if hashed not in self.collection:
            self.collection[hashed] = {key: value}
        else:
            self.collection[hashed][key] = value

    def remove(self, key):
        hashed = self.hash(key)
        if hashed in self.collection:
            self.collection[hashed].pop(key, None)

    def lookup(self, key):
        hashed = self.hash(key)
        if hashed in self.collection:
                return self.collection.get(hashed).get(key)
        return None

#Testing
def main():
    col = HashTable()
    print(col.hash('pepper'))
    col.add('dear', 'pot')
    col.add('read', 'chalupa')
    print(col.collection)
    col.lookup('golf')
    print(col.lookup('read'))

main()
