class indent:
    def __init__(self,attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2

    def test(self):
        print(self.attr2, self.attr2)

CIndent = indent("Attr1", "Attr2")