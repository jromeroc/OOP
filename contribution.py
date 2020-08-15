class Contribution(Author):

    def __init__(self, id, title, id_author, quality):
        self.id = id
        self.title = title
        self.id_author = id_author
        self.quality = quality
    
    def update_author(self, author):
        self.id_author = author

    def id_num(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def title(self):
        return self.title

    def set_title(self, title):
        self.title = title
    
    def quality(self):
        return self.quality
    
    def set_quality(self, qu):
        self.quality = qu

    

