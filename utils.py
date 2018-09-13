class Utils:

    def find_longest_string(self, list_of_strings):

        longest_string = None
        for item in list_of_strings:
            if longest_string != None:
                if len(item) > len(longest_string):
                    longest_string = item
            else:
                longest_string = item

        return longest_string
