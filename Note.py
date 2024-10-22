

class Note:
    def __init__(self, textNote):
        self.textNote = textNote
        self.deleted = False
    
    def delete_note(self):
        self.deleted = True