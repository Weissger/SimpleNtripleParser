__author__ = 'tmy'

COMMENT_INDICATOR = '#'
URI_INDICATOR = '<'


class NTripleLineParser():
    def __init__(self, separator):
        self.separator = separator

    @staticmethod
    def __is_comment_line(line):
        return line.startswith(COMMENT_INDICATOR)

    @staticmethod
    def __strip_uri_indicator(uri):
        if uri.startswith(URI_INDICATOR):
            return uri[1:-1]
        else:
            return uri

    def is_comment_line(self, line):
        line = line.strip()
        return self.__is_comment_line(line)

    def get_subject(self, line):
        line = line.strip()
        if self.__is_comment_line(line):
            return None
        else:
            return line.split(self.separator, 1)[0][1:-1]

    def get_predicate(self, line):
        line = line.strip()
        if self.__is_comment_line(line):
            return None
        else:
            return line.split(self.separator, 2)[1][1:-1]

    def get_object(self, line):
        line = line.strip()
        if self.__is_comment_line(line):
            return None
        else:
            obj = line.split(self.separator, 3)[2]
            obj = obj[1:obj.index(">")]
            return obj

    def get_triple(self, line):
        split_line = line.split(self.separator)
        if split_line[0].strip().startswith("#"):
            return None
        else:
            obj = split_line[2]
            obj = obj[1:obj.index(">")]
            return {"subject": split_line[0][1:-1], "predicate": split_line[1][1:-1],
                    "object": obj}