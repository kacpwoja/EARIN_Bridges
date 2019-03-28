from tree import Tree
from boardstate import BoardState


def board_mass(board: BoardState):
    """Function for evaluating the mass of given board

    define bridge mass BM as:
        BM = i_n + i_k
        where i is the value of the island n and k consecutively, connected to each other
        REMARK: if i_n = 1, then i_k cannot be 1.

    args:
        BoardState object

    Returns:
        mass of the board
    """

    mass = 0

    for island in board.islands:
        for i in range(len(island.connections)):
            mass += island.connections[i] * (island.bridges_expected + board.islands[i].bridges_expected)

    return mass/2


def board_cost(board: BoardState):
    """Function for evaluating cost of the given board

        define board cost C as:
            C = n - x
            where n is the number of all islands, and x is the biggest number of islands forming a path

        args:
            BoardState object

        Returns:
            cost of the board
    """

    islands_num = 0
    paths = [[]]

    #TODO: zrobić to bo jestem zjebany

    cost = islands_num - len(max(paths))
    return cost

