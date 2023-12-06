class InvalidInputError(Exception):
    pass

# string validation helper class
class Validate:
    @staticmethod
    def string_length(input: str, min: int, max: int):
        if len(input) < min or len(input) > max:
            return False
        return True
    
    @staticmethod
    def year(input):
        if input.isalpha():
            raise InvalidInputError("Vuosi väärin!")
        year = int(input)
        if year < 0 or year > 3000:
            raise InvalidInputError("Vuosi väärin!")
        return True

    @staticmethod
    def username(input):
        if not Validate.string_length(input, 0, 100):
            raise InvalidInputError("Liian pitkä username syöte!")
        return True
    
    @staticmethod
    def author(input):
        if not Validate.string_length(input, 0, 100):
            raise InvalidInputError("Liian pitkä author syöte!")
        return True
    
    @staticmethod
    def title(input):
        if not Validate.string_length(input, 0, 100):
            raise InvalidInputError("Liian pitkä title syöte!")
        return True
    
    @staticmethod
    def publisher(input):
        if not Validate.string_length(input, 0, 100):
            raise InvalidInputError("Liian pitkä publisher syöte!")
        return True
    
    @staticmethod
    def volume(input):
        if not Validate.string_length(input, 0, 100):
            raise InvalidInputError("Liian pitkä volume syöte!")
        return True
    
    @staticmethod
    def series(input):
        if not Validate.string_length(input, 0, 100):
            raise InvalidInputError("Liian pitkä series syöte!")
        return True
    
    @staticmethod
    def address(input):
        if not Validate.string_length(input, 0, 100):
            raise InvalidInputError("Liian pitkä address syöte!")
        return True
    
    @staticmethod
    def edition(input):
        if not Validate.string_length(input, 0, 100):
            raise InvalidInputError("Liian pitkä edition syöte!")
        return True
    
    @staticmethod
    def note(input):
        if not Validate.string_length(input, 0, 100):
            raise InvalidInputError("Liian pitkä note syöte!")
        return True
    
    @staticmethod
    def month(input):
        if not Validate.string_length(input, 0, 3):
            raise InvalidInputError("Syötä kuukausi tyylillä 'jan', 'feb' jne.")
        return True
    
    @staticmethod
    def school(input):
        if not Validate.string_length(input, 0, 100):
            raise InvalidInputError("Liian pitkä school syöte!")
        return True

    @staticmethod
    def type(input):
        if not Validate.string_length(input, 0, 100):
            raise InvalidInputError("Liian pitkä type syöte!")
        return True
    