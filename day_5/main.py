#! /usr/bin/env python3

from __future__ import annotations
from typing import List

FILE_PATH = "./day_5/data/input.txt"

class Point:
    def __init__(self,x:int,y:int):
        self.x = x
        self.y = y

    def sub(self,other:Point) -> Point:
        return Point(
            self.x - other.x,
            self.y - other.y,
        )

    def add(self,other:Point) -> Point:
        return Point(
            self.x + other.x,
            self.y + other.y,
        )

    def __format__(self, __format_spec: str) -> str:
        return f"({self.x},{self.y})"

class Vector:
    def __init__(self,p0:Point,p1:Point):
        self.p0 = p0
        self.p1 = p1

    @staticmethod
    def from_coords(x0:int,y0:int,x1:int,y1:int):
        p0 = Point(x0,y0)
        p1 = Point(x1,y1)
        v  = Vector(p0,p1)
        return v

    def is_horizontal(self) -> bool:
        return self.p0.y == self.p1.y

    def is_vertical(self) -> bool:
        return self.p0.x == self.p1.x

    def get_points(self) -> List[Point]:
        points = []
        if self.is_horizontal():
            start = self.p0.x
            stop = self.p1.x
            step = 1 if start<=stop else -1
            stop += step
            for x in range(start,stop,step):
                points.append(Point(x,self.p0.y))
        elif self.is_vertical():
            start = self.p0.y
            stop = self.p1.y
            step = 1 if start<=stop else -1
            stop += step
            for y in range(start,stop,step):
                points.append(Point(self.p0.x,y))
        else:
            # aka this is a diagonal
            # print("aka this is a diagonal")
            m = (self.p1.y-self.p0.y)/(self.p1.x-self.p0.x)
            c = self.p0.y - m*self.p0.x

            start = self.p0.x
            stop  = self.p1.x
            step  = 1 if start<=stop else -1
            stop += step

            for x in range(start,stop,step):
                y = m*x+c
                points.append(Point(int(x),int(y)))

        return points

    def __format__(self, __format_spec: str) -> str:
        return f"{self.p0}->{self.p1}"

class Map:
    def __init__(self, max_size: Point):
        self.size = max_size
        self.data = [ [0 for _row_index in range(max_size.y+1)] for _col_index in range(max_size.x+1) ]

    def add_to_point(self, p: Point):
        self.data[p.x][p.y] += 1

    def get_points_with_count_above(self, thresh: int) -> int:
        point_count = 0
        for x in range(self.size.x):
            for y in range(self.size.y):
                if self.data[x][y]>thresh:
                    point_count += 1
        return point_count


def get_max_point(vectors: List[Vector]) -> Point:
    max_point = Point(0,0)
    for v in vectors:
        for p in [v.p0,v.p1]:
            if p.x > max_point.x:
                max_point.x = p.x
            if p.y > max_point.y:
                max_point.y = p.y
    return max_point

def read_data(file_path: str) -> List[Vector]:
    input_vectors = []
    with open(file_path) as fp:
        for line in fp:
            arrow_split = line.split(" -> ")
            comma_split = [n.split(",") for n in arrow_split]
            first_x_coordinate  = int(comma_split[0][0])
            first_y_coordinate  = int(comma_split[0][1])
            second_x_coordinate = int(comma_split[1][0])
            second_y_coordinate = int(comma_split[1][1])
            input_vectors.append(Vector.from_coords(
                first_x_coordinate,
                first_y_coordinate,
                second_x_coordinate,
                second_y_coordinate
            ))
    return input_vectors


def main():
    vectors = read_data(FILE_PATH)
    # filtered_vectors = [v for v in vectors if v.is_vertical() or v.is_horizontal()]
    map_size = get_max_point(vectors)
    print(f"map_size: {map_size}")
    map = Map(map_size)
    for v in vectors:
        v_points = v.get_points()
        for p in v_points:
            map.add_to_point(p)
    point_count = map.get_points_with_count_above(1)
    print(f"point_count: {point_count}")


if __name__=="__main__":
    main()