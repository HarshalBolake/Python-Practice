from dataclasses import dataclass

@dataclass
class Point:
    x : int
    y : int

P = Point(1,2)
print(P)