from data_storage.enums.sex import Sex


class CleanDataService:
    @staticmethod
    def clean_float_string(dirty_string):
        cleaned_float_string = dirty_string.replace(",", '.')
        return cleaned_float_string

    @staticmethod
    def detect_sex(sex_as_string):
        if sex_as_string == 'M':
            return Sex.Male.value
        if sex_as_string == 'F':
            return Sex.Female.value
        return Sex.Unknown.value
