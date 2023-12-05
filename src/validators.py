from methods import InvalidInputError

# string validation helper class
class Validate:
    def string_length(self, input: str, min: int, max: int):
        if len(input) < min or len(input) > max:
            return False
        return True
    
    @staticmethod
    def year(self, input):
        if input.isalpha():
            raise InvalidInputError("Vuosi väärin!")
        year = int(input)
        if year < 0 or year > 3000:
            raise InvalidInputError("Vuosi väärin!")
        return True

    @staticmethod
    def username(self, input):
        if not self.string_length(input, 0, 100):
            raise InvalidInputError("Liian pitkä username syöte!")
        return True
    
    @staticmethod
    def author(self, input):
        if not self.string_length(input, 0, 100):
            raise InvalidInputError("Liian pitkä author syöte!")
        return True
    
    @staticmethod
    def title(self, input):
        if not self.string_length(input, 0, 100):
            raise InvalidInputError("Liian pitkä title syöte!")
        return True
    
    @staticmethod
    def publisher(self, input):
        if not self.string_length(input, 0, 100):
            raise InvalidInputError("Liian pitkä publisher syöte!")
        return True
    
    @staticmethod
    def volume(self, input):
        if not self.string_length(input, 0, 100):
            raise InvalidInputError("Liian pitkä volume syöte!")
        return True
    
    @staticmethod
    def series(self, input):
        if not self.string_length(input, 0, 100):
            raise InvalidInputError("Liian pitkä series syöte!")
        return True
    
    @staticmethod
    def address(self, input):
        if not self.string_length(input, 0, 100):
            raise InvalidInputError("Liian pitkä address syöte!")
        return True
    
    @staticmethod
    def edition(self, input):
        if not self.string_length(input, 0, 100):
            raise InvalidInputError("Liian pitkä edition syöte!")
        return True
    
    @staticmethod
    def note(self, input):
        if not self.string_length(input, 0, 100):
            raise InvalidInputError("Liian pitkä note syöte!")
        return True
    
    @staticmethod
    def month(self, input):
        if not self.string_length(input, 0, 3):
            raise InvalidInputError("Syötä kuukausi tyylillä 'jan', 'feb' jne.")
        return True
    