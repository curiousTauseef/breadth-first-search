from collections import deque
from .exceptions import NotNodeInstance
from .Node import Node


def _compose_path_from_walked_path(walked_path, wanted_value, result=None):
    """
    :type walked_path: dict
    :type wanted_value: str
    :type result: list
    :return:
    """
    if result is None:
        result = [wanted_value]

    for node_value in walked_path:
        if wanted_value in walked_path[node_value]:
            result.append(node_value)
            _compose_path_from_walked_path(walked_path, node_value, result)
            break

    return result


def find(start, value):
    """
    :type start: Node
    :type value: string
    :return:
    """

    if not isinstance(start, Node):
        raise NotNodeInstance

    search_queue = deque()
    search_queue.append(start)

    checked_nodes = {}
    walked_path = {}

    while search_queue:
        node = search_queue.pop()  # type: Node

        walked_path[node.get_value()] = []

        checked_nodes[node.get_value()] = 1

        if node.get_value() == value:
            _path = _compose_path_from_walked_path(walked_path, value)
            _path.reverse()

            return _path
        else:
            neighbors = node.get_neighbors()

            for neighbor in neighbors:  # type: Node
                if (neighbor.get_value() in checked_nodes) is False:

                    if not isinstance(node, Node):
                        raise NotNodeInstance

                    walked_path[node.get_value()].append(neighbor.get_value())

                    search_queue.append(neighbor)

    return []
