import datetime

TODAY = datetime.datetime.now().date()


class ValidateDate:
    """
        A class to validate date formats.

        Attributes:
            date (str): The date string to be validated.
        Methods:
            validate_date():
                Validates the input date format (YYYY-MM-DD).
                Returns True if the date is in the correct format, False otherwise.
        """

    def __init__(self, date: str):
        """
            Initialize ValidateDate object with a date string.

            Args:
                date (str): The date string to be validated.
        """
        self.date = date

    def validate_date(self):
        """
            Validate the date format.

            Returns:
                bool: True if the date is in the correct format (YYYY-MM-DD), False otherwise.
        """
        try:
            datetime.date.fromisoformat(self.date)
        except ValueError:
            print("Incorrect data format, should be YYYY-MM-DD")
            return False
        return True
