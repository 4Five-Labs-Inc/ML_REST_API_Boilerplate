import csv
class Utility:
    """
        <helper>
        expand_abbreviations expands all abbreviations
        :param word: any string
        :return: string/None
    """
    def expand_abbreviations(self, word):
        # loads the abbrevation data
        with open('src/models/abbrevation.csv') as abbrevation:
            abbrevation_data = csv.reader(abbrevation)
            for row in abbrevation_data:
                # if the word matches any abbrevations
                if word.upper() == row[0]:
                    return row[1].lower()
            abbrevation.close()
        return
