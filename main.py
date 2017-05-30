from bfs.algorithm import find
from bfs.Node import Node

claire = Node('claire')
garold = Node('garold')
sergio = Node('sergio')
andrew = Node('andrew')
alice = Node('alice')
peggy = Node('peggy')
anton = Node('anton')
johny = Node('johny')
anuj = Node('anuj')
thom = Node('thom')
you = Node('you')
bob = Node('bob')

"""
(andrew) -- (sergio)
                 |
                 |
             (garold) (anton)
                 |    /
                 |   /
    ⊢---------- (peggy)    (anuj)
    |               |        /
    |               |       /
    |             (bob) ---
    |               |
 (alice) -------- (you) --------- (claire)
    |               |               /   |
    |               |              /    |
    |               ⊢--------- (johny) (thom)
    |                             |
    ⊢----------------------------⊣
"""

you.set_neighbors([
    bob.set_neighbors([
        anuj, peggy.set_neighbors([
            anton, garold.set_neighbors([
                sergio.set_neighbors([
                    andrew
                ])
            ])
        ])
    ]),
    claire.set_neighbors([
        johny, thom
    ]),
    alice.set_neighbors([
        peggy, johny
    ]),
    johny
])

value = 'andrew'
path = find(you, value)  # type: {}

print(path)
