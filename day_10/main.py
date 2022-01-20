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

SUFFIX_CLOSER_SCORE = {
        ")": 1, "]": 2,
        "}": 3, ">": 4,
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
    def __init__(self,status: ChunkStatus, c: str,
        score: Optional[int] = None, suffix: Optional[str]=None):
        self.status = status
        self.c = c
        self.score = score
        self.suffix = suffix

    def is_corrupt(self) -> bool:
        return self.status == ChunkStatus.CORRUPT

    def calculate_suffix_score(self) -> int:
        if self.status != ChunkStatus.INCOMPLETE:
            return 0
        score = 0
        for c in self.suffix:
            score *= 5
            score += SUFFIX_CLOSER_SCORE[c]
        return score


def rebuild_line(line: str) -> LineStatus:
    '''Parses over line, and checks for correct chunking across line'''
    chunk_stack = []
    suffix_string = ""
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
        chunk_stack.reverse()
        for index in chunk_stack:
            suffix_string += CLOSERS[index]
        return LineStatus(ChunkStatus.INCOMPLETE,c,suffix=suffix_string)

def read_data(path: str) -> List[str]:
    '''Reads in lines from file specified by path, and returns as
    list of string'''
    return_data = []
    with open(path) as fp:
        return_data = [line for line in fp]
    return return_data

def main():
    data = read_data(FILE_PATH)
    statuses = [rebuild_line(line) for line in data]

    ncl_scores = [status.calculate_suffix_score() for status in statuses if not status.is_corrupt()]
    ncl_scores.sort()
    ncl_score_count = len(ncl_scores)
    median_index = int((ncl_score_count-1)/2)
    median_score = ncl_scores[median_index]
    print(f"median_score: {median_score}")



if __name__=="__main__":
    main()