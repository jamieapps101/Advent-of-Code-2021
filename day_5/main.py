#! /usr/bin/env python3

from __future__ import annotations
from typing import List

FILE_PATH = "./day_5/data/input.txt"

class Point:
    def __init__(self,x,y):
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
        self.p0.y == self.p1.y

    def is_vertical(self) -> bool:
        self.p0.x == self.p1.x

    def get_points(self) -> List[Point]:
        pass


def read_data(file_path: str):
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
    read_data(FILE_PATH)

if __name__=="__main__":
    main()