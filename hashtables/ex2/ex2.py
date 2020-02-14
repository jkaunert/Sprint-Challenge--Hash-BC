#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    for index in range(0, length):
        if tickets[index].source is "NONE":
            route[0] = tickets[index].destination

        hash_table_insert(hashtable, tickets[index].source, tickets[index].destination)

    for index in range(0, length):
        if route[index - 1] is not None:
            route[index] = hash_table_retrieve(hashtable, route[index-1])

    return route[:-1]
