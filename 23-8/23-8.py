class cat:

    def __init__(self, name):
        self.name = name

    def meow(self):
        print(f"{self.name} says meow")

cat = cat('whiskers')
cat.meow()