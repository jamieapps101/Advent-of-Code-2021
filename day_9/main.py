#! /usr/bin/env python3

from pprint import pprint
from typing import List

# FILE_PATH = "day_9/data/test_input.txt"
FILE_PATH = "day_9/data/input.txt"

def get_data(file_path: str):
    line_data = []
    with open(file_path) as fp:
        for line in fp:
            line = line.rstrip()
            digit_data = []
            for digit in line:
                number = int(digit)
                digit_data.append(number)
            line_data.append(digit_data)
    return line_data

def create_label_dim(depth_data: List[List[int]]) -> List[List[dict]]:
    '''Replace each integer depth measurement with a dictionary containing
    the depth, and an optional label value'''
    for y in range(len(depth_data)):
        for x in range(len(depth_data[0])):
            depth = depth_data[y][x]
            depth_data[y][x] = {
                "depth": depth,
                "label": None
            }
    return depth_data



def path_finder(depth_data: List[List[int]]) -> List[List[dict]]:
    all_points = []
    for y in range(len(depth_data)):
        for x in range(len(depth_data[0])):
            # we're looking for places to explore
            # so we need to ignore places we have been
            # already, or cant go.
            if depth_data[y][x] != 9:
                all_points.append({"x":x,"y":y})
    # all_points is now a list containing all valid points we can travel to

    basins = []
    while len(all_points) > 0:
        # now we begin A* search!
        start_point = all_points.pop()
        to_explore = [start_point]
        explored = []
        while len(to_explore) != 0:
            current_point = to_explore.pop()
            explored.append(current_point)
            # find candidates points to explore
            # by looking for points adjacent to our current one
            for offset in [(0,-1), (0,1), (-1,0), (1,0)]:
                candidate = {
                    "x":current_point["x"]+offset[0],
                    "y":current_point["y"]+offset[1]
                }
                if candidate in all_points:
                    all_points.remove(candidate)
                    to_explore.append(candidate)
        basins.append(explored)
    basin_size_count = [len(basin_points) for basin_points in basins]
    return basin_size_count


def basin_finder(depth_data: List[List[int]]) -> List[List[dict]]:
    depth_data = create_label_dim(depth_data)
    basin_counter = 0
    basin_size_count = []

    for y in range(len(depth_data)):
        for x in range(len(depth_data[0])):
            print(f"depth: {depth_data[y][x]['depth']} | ",end="")
            if depth_data[y][x]["depth"] < 9:
                # ie we're in a basin
                # determine if there is an adjacent label, and store
                # it in adjacent_label if present
                above = None if y==0 else depth_data[y-1][x]["label"]
                below = None if y==len(depth_data)-1 else depth_data[y+1][x]["label"]
                left  = None if x==0 else depth_data[y][x-1]["label"]
                right = None if x==len(depth_data[0])-1 else depth_data[y][x+1]["label"]
                adjacent_labels = [above, below, left, right]
                adjacent_label = None
                for l in adjacent_labels:
                    if l is not None:
                        adjacent_label = l
                        break
                print(f"adjacent_label: {adjacent_label} | adjacent_labels: {adjacent_labels}")

                if adjacent_label is None:
                    # ie there are no other basin measurements nearby,
                    # so we must be in a new basin
                    depth_data[y][x]["label"] = basin_counter
                    basin_size_count.append(1)
                    basin_counter += 1
                else:
                    # there is an adject basin nearby! we'll copy the label that we identified
                    depth_data[y][x]["label"] = adjacent_label
                    basin_size_count[adjacent_label] += 1
            else:
                # ie we're not in a basin, so do nothing
                print("")
                pass
        print("<new row>")

    return depth_data,basin_size_count

def main():
    data = get_data(FILE_PATH)

    # _depth_data,basin_size_count = basin_finder(data)
    basin_size_count = path_finder(data)

    basin_size_count = sorted(basin_size_count,reverse=True)

    top_three_basin_sizes = basin_size_count[0:3]
    multiplied_sizes = 1
    for size in top_three_basin_sizes:
        multiplied_sizes *= size

    print(f"multiplied_sizes: {multiplied_sizes}")



if __name__ == "__main__":
    main()

