from .contribution import Contribution

class Presentation(Contribution):

    def __init__(self, id, title, id_author, quality, date, subject):
        super().__init__(id, title, id_author, quality)
        self.date = date
        self.subject = subject
    
    def publication_date(self):
        return self.date

    def set_publication_date(self, date):
        self.date = date
    
    def subject(self):
        return self.subject
    
    def set_subject(self, subject):
        self.subject = subject
