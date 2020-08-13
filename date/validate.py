
class ValidDate(object):

    @classmethod
    def special_char(self,char):
        """Check to see if char is in a list of special date chars
        """
        if(char == '-'):
            return True
        else:
            return False

    @classmethod
    def check_and_store(self,char):
        """Check to see if each char is a number or a special char in my list.
        """
        if(char.isnumeric()):
            return True
        else:
            if(self.special_char(char)):
                return True
            else:
                return False

### Look at each char and if its not a number
### or one of my special chars then delete it
### and keep going...
    @classmethod
    def remove_unwanted_chars(self,date):
        """ Check each char and store the good ones and drop the bad ones
        """
        localstore = []
        for elem in date:
            bval = self.check_and_store(elem)
            if bval:
                localstore.append(elem)
        result = ''.join(localstore)
        return result

if __name__ == "__main__":
    testcases = ['123','2020-04-01>>','2020-05-07>>','456']
    vd = ValidDate()
    for ex in testcases:
        print(ex)
        result = vd.remove_unwanted_chars(ex)
        print(result)
