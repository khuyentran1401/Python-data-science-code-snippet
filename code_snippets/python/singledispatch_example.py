from functools import singledispatch

# Without singledispatch


def process_data(data):
    if isinstance(data, dict):
        process_dict(data)

    else:
        process_list(data)


def process_dict(data: dict):
    print("Dict is processed")


def process_list(data: list):
    print("List is processed")


# ---------------------------------------------------------------------------- #
# With singledispatch


@singledispatch
def process_data2(data):
    raise NotImplementedError("Please implement process_data2")


@process_data2.register
def process_dict2(data: dict):
    print("Dict is processed")


@process_data2.register
def process_list2(data: list):
    print("List is processed")


data = {"a": [1, 2, 3], "b": [4, 5, 6]}
data2 = [{"a": [1, 2, 3]}, {"b": [4, 5, 6]}]

process_data2(data)
"""Dict is processed"""

process_data2(data2)
"""List is processed"""
