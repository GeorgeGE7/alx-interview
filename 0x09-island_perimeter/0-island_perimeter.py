#!/usr/bin/python3
"""0x09. Island Perimeter:
Returns the perimeter of the island described in grid"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island described in a grid.

    Args:
        grid (List[List[int]]): A 2D grid representing the island.

    Returns:
        int: The perimeter of the island.

    The function iterates over each square in the grid and checks if it is part of an island. If a square is part of an island, it counts the number of sides that are not part of the island. The function considers the sides of the square as follows:
    - Left and right sides: If the square is on the left or right edge of the grid, it checks if the adjacent square to the left or right is not part of the island. If it is not part of the island, it increments the counter.
    - Top and bottom sides: If the square is on the top or bottom edge of the grid, it checks if the adjacent square above or below is not part of the island. If it is not part of the island, it increments the counter.

    The function returns the total number of sides that are not part of the island, which represents the perimeter of the island.
    """

    numm = 0
    numm_max = len(grid) - 1  # index of the last list in the grid
    max_lst = len(grid[0]) - 1  # index of the last square in list

    for index_lst, endd in enumerate(grid):
        for index_land, land_l in enumerate(endd):
            if land_l == 1:
                if index_land == 0:
                    numm += 1

                    if endd[index_land + 1] == 0:
                        numm += 1
                elif index_land == max_lst:
                    if endd[index_land - 1] == 0:
                        numm += 1

                    numm += 1
                else:
                    if endd[index_land - 1] == 0:
                        numm += 1

                    if endd[index_land + 1] == 0:
                        numm += 1

                if index_lst == 0:
                    numm += 1

                    if grid[index_lst + 1][index_land] == 0:
                        numm += 1
                elif index_lst == numm_max:
                    if grid[index_lst - 1][index_land] == 0:
                        numm += 1

                    numm += 1
                else:
                    if grid[index_lst - 1][index_land] == 0:
                        numm += 1

                    if grid[index_lst + 1][index_land] == 0:
                        numm += 1

    return numm
