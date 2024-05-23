class Name:
    def __init__(self, fname, lname):
        self.fname = fname.capitalize()
        self.lname = lname.capitalize()
    def fullname(self):
        return f"{self.fname} {self.lname}"
    def initials(self):
        return f"{self.fname[0]}. {self.lname[0]}."
al = Name("john", "SMITH")
print(al.fname)
print(al.lname)
print(al.fullname)
print(al.initials)
