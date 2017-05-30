class Node(object):
    def __init__(self, value, neighbors=None):
        if neighbors is None:
            neighbors = []

        self.value = value
        self.neighbors = neighbors

    def get_value(self):
        return self.value

    def get_neighbors(self):
        return self.neighbors

    def set_neighbors(self, neighbors):
        self.neighbors = neighbors

        return self
