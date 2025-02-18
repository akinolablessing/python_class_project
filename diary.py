class Diary:
    def __init__(self):
        self.entries = []

    def addEntry(self, entry):
        self.entries.append(entry)

    def getEntries(self):
        return self.entries

    def deleteDiary(self, diary):
        if diary in self.entries:
            self.entries.remove(diary)



