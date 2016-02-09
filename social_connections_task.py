__author__ = 'Paul'

class Friends:
    def __init__(self, connections):
        self.connections = connections

    def add(self, connection):
        if connection not in self.connections:
            self.connections = list(self.connections)
            self.connections.append(connection)
            return True
        return False

    def remove(self, connection):
        if connection in self.connections:
            self.connections = list(self.connections)
            self.connections.remove(connection)
            return True
        return False

    def names(self):
        names_set = {element for i in self.connections for element in i}
        return names_set

    def connected(self, name):
        con_names = set()
        for item in self.connections:
            if name in item:
                for contact in item:
                    if name != contact:
                        con_names.add(contact)
        return con_names

# not mine solution and I don't even fully understand it

class Friends(set):
    def __init__(self, pairs=set()):
        super().__init__(map(frozenset, pairs))
?
    def add(self, pair):
        if pair in self: return False
        super().add(frozenset(pair))
        return True
?
    def remove(self, pair):
        if pair not in self: return False
        super().remove(pair)
        return True
?
    def names(self):
        return set().union(*self)
?
    def connected(self, name):
        return Friends(filter({name}.issubset, self)).names() - {name}

# other cool solution that I don't really understand

class Friends():
    def __init__(self, connections):
        self.all_connection = list(connections)
?
    def add(self, connection):
        if connection in self.all_connection:
            return False
        else:
            self.all_connection.append(connection)
            return True
?
    def remove(self, connection):
        if connection in self.all_connection:
            self.all_connection.remove(connection)
            return True
        else:
            return False
?
    def names(self):
        return reduce(lambda a,b: a.union(b), self.all_connection)

    def connected(self, name):
        related = [pair for pair in self.all_connection if name in pair]
        if related:
            related = reduce(lambda a,b: a.union(b), related)
            related.remove(name)
            return related
        else:
            return set([])




