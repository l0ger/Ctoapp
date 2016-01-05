class Utility:
    # write dictionary as record
    @staticmethod
    def write_dict_record(file_name, data):
        f = open(file_name, 'w')
        record = Utility.implode(data, ";")
        f.write(record+"\n")
        f.close()

    @staticmethod
    def implode(data, seperator):
        record = ""
        for key in data:
            record += unicode.encode(data[key]) + seperator

        return record.strip(seperator)
