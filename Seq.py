def count_letter(arg1, arg2):
    n_characters = 0   # Counter for the characters
    for b in arg1:
        if b == arg2:
            n_characters += 1
    return n_characters

class Seq:
    def __init__(self, strbases):

        self.strbases = strbases
        if strbases[0] == ">":
            aux_var = self.strbases
            aux_var = aux_var.splitlines()
            aux_var = aux_var[1:]
            aux_var = "".join(aux_var)
            self.strbases = aux_var

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)

    def complement(self):
        ns = []
        for b in self.strbases:
            if b == "A":
                ns.append("T")
            elif b == "T":
                ns.append("A")
            elif b == "C":
                ns.append("G")
            elif b == "G":
                ns.append("C")
        ns = "".join(ns)
        return ns

    def reverse(self):
        ns = []
        for i in range((-1)*(len(self.strbases)-1),0):
            ns.append(self.strbases[(-1)*i])
        ns = "".join(ns)
        return ns

    def count(self, base):
        return count_letter(self.strbases, base)

    def perc(self, base):
        return round((count_letter(self.strbases, base) * 100 / len(self.strbases)), 1)

    def checker(self):
        boolean = True
        for b in self.strbases:
            if b == "A" or b == "T" or b == "G" or b == "C": boolean = True
            else:
                boolean = False
                break
        return boolean

