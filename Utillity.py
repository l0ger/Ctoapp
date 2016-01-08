class Utility:
    # write dictionary as record
    @staticmethod
    def write_dict_record(file_name, data):
        f = open(file_name, 'w')
        record = Utility.implode(data, ";")
        f.write(record + "\n")
        f.close()

    @staticmethod
    def read_test(file_name):
        f = open(file_name, 'r')
        return f.read()

    @staticmethod
    def implode(data, seperator):
        record = ""
        for key in data:
            record += unicode.encode(data[key]) + seperator

        return record.strip(seperator)
