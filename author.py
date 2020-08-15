class Author:

    def __init__(self, id, name, university, email, count_Publications):
        self.id = id
        self.name = name
        self.university = university
        self.email = email
        self.count_Publications = count_Publications
        self.contributions = []

    def id_author(self):
        return self.id

    def set_id_author(self, id_author):
        self.id = id_author

    def name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
    
    def university(self):
        return self.university
    
    def set_university(self, university):
        self.university = university

    def email(self):
        return self.email
    
    def set_email(self, email):
        self.email = email

    def calculate_average(self):
        pass

    def check_qualification(self, contribution):
       if self.contribution.id_author.id == self.id:
           self.contributions.append(contribution)
           self.count_Publications = len(self.contribuciones)
    
        print("This contribution obtained a note of {}".format(contribution.qu))

