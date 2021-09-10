import re
import json


def read_file(name_file):
    result = []

    file1 = open(name_file, 'r')
    lines = file1.readlines()

    for line in lines:
        tmp = regex(line)
        result.append(tmp)

    return result


# function for tube instagram comment betta
def regex(data):
    x = re.search(r"^(\d.*\d{2}\s)(.*)(\sto.*)", data)
    return x.group(2)


# function for tube instagram post
# def regex(data):
#     x = re.search(r"^([A-z]+[^\s]+)(\s)(\d+)", data)
#     group1 = x.group(1)
#     group2 = x.group(3)
#     return "{0},{1}".format(group1, group2)

# function for printed news push manual
# def regex(data):
#     x = re.search(r"^([\d]+)(\s)(\d+)", data)
#     group1 = x.group(1)
#     group2 = x.group(3)
#     return "{0},{1}".format(group1,group2)


# function for tube fb page feed
# def regex(data):
#     return data.replace("\n", "")


def body_formatted(field, value):
    return '{ "' + field + '": "' + value + '" }'


def formatted_dict(data):
    return json.dumps(data)