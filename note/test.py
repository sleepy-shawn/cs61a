class Kangaroo:
    def __init__(self):
        self.content = []
    def put_in_pouch(self, new):
        if new in self.content:
            print ("object already in pouch")
            return
        else:
            self.content.append(new)
    def __str__(self):
        if not self.content:
            print ("The kangraoo's pouch is empty")
        else:
            print("The kangrapp's pouch is" + str(self.content))
            



            

