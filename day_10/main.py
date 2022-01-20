#! /usr/bin/env python3

from typing import List, Optional, Dict
from enum import Enum

FILE_PATH = "./day_10/data/input.txt"

OPENERS = ["{","(","<","["]
CLOSERS = ["}",")",">","]"]

CLOSER_SCORE = {
    ")": 3, "]": 57,
    "}": 1197, ">": 25137
}

def get_closer_score(c:str):
    return CLOSER_SCORE[c]

def is_opener(c: str) -> bool:
    return c in OPENERS

def get_opener_index(c: str) -> int:
    return OPENERS.index(c)

def is_closer(c: str) -> bool:
    return c in CLOSERS

def get_closer_index(c: str) -> int:
    return CLOSERS.index(c)

class ChunkStatus(Enum):
    COMPLETE=0
    INCOMPLETE=1
    CORRUPT=2

# This is replaced with the below class to make the return type annotations clearer
# def return_state(status: ChunkStatus, c: str, score: Optional[int] = None) -> Dict:
#     '''Helper function to wrap up data into one convinient dict'''
#     return {"status": status, "c":c, "score": score}

class LineStatus():
    '''Helper function to wrap up data into one convinient class'''
    def __init__(self,status: ChunkStatus, c: str, score: Optional[int] = None):
        self.status = status
        self.c = c
        self.score = score

    def is_corrupt(self) -> bool:
        return self.status == ChunkStatus.CORRUPT

def parse_line(line: str) -> LineStatus:
    '''Parses over line, and checks for correct chunking across line'''
    chunk_stack = []
    for c in line:
        if is_opener(c):
            chunk_stack.append(get_opener_index(c))
        elif is_closer(c):
            closer_index = get_closer_index(c)
            if closer_index == chunk_stack[-1]:
                # ie the corresponding closer is used
                chunk_stack.pop()
            else:
                # this is a corruption!
                return LineStatus(ChunkStatus.CORRUPT,c,get_closer_score(c))
    # end of line reached here
    if len(chunk_stack) == 0:
        return LineStatus(ChunkStatus.COMPLETE,c)
    else:
        return LineStatus(ChunkStatus.INCOMPLETE,c)

def read_data(path: str) -> List[str]:
    '''Reads in lines from file specified by path, and returns as
    list of string'''
    return_data = []
    with open(path) as fp:
        return_data = [line for line in fp]
    return return_data

def main():
    data = read_data(FILE_PATH)
    statuses = [parse_line(line) for line in data]
    score = sum([status.score for status in statuses if status.is_corrupt()])
    print(f"score: {score}")

if __name__=="__main__":
    main()