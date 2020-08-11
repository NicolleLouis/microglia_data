class CleanDataService:
    @staticmethod
    def clean_float_string(dirty_string):
        cleaned_float_string = dirty_string.replace(",", '.')
        return cleaned_float_string
