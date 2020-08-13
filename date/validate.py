
class ValidDate(object):

### Look at each char and if its not a number
### or one of my special chars then delete it
### and keep going...
    @classmethod
    def remove_unwanted_chars(self,date):
        print(date)
        for elem in date:
            print(elem)

if __name__ == "__main__":
    testcases = ['123','2020-04-01>>','2020-05-07>>']
    vd = ValidDate()
    for ex in testcases:
        vd.remove_unwanted_chars(ex)
