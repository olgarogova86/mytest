# created by Rogova Olga 24/10/2018
class FileReader:
    def __init__(self, path):
        self.path = path

    def read(self):
        result = ""
        try:
            with open(self.path) as f:
                result = (''.join(f.readlines())).replace('\n', '')
        except IOError:
            # print("Exception")
            pass
        return result


# reader = FileReader("D:\example2.txt")
# print(reader.read())
