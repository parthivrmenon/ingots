
class BookDto:
    """
    A data transfer helper class that converts a request_form (dict)
    into an object that encapsulates 'Book' attributes.
    """
    def __init__(self, request_form:dict ):
        self.id = None
        self.title = request_form["title"]
        self.author = request_form["author"]
        self.category = request_form["category"]
        self.tags = request_form["tags"]
        
        

    

