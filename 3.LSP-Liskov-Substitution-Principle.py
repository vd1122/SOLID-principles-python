"""
LSP --> Liskov Substitution Principle

"If S is a subtype of T, then objects of type T may be replaced with objects of type S without altering the correctness
of the program."

i.e. Child class objects should be able to replace parent class objects without breaking the integrity of the
application.

"""

"""
Example of LS principle violation
"""


class Batsman:
    def __init__(self, batsman_code: str, batsman_name: str):
        self.batsman_code = batsman_code
        self.batsman_name = batsman_name

    def get_batsman_name(self) -> str:
        return self.batsman_name

    def get_batting_side(self) -> tuple:
        return "N/A" "Unknown"


class RightHandBatsman(Batsman):
    def __init__(self):
        super().__init__("RHB", "Right hand batsman")

    def get_batting_side(self) -> str:
        return "RHB"


class LeftHandBatsman(Batsman):
    def __init__(self):
        super().__init__("LHB", "Left hand batsman")

    def get_batting_side(self) -> str:
        return "LHB"


batsmen = [Batsman(), RightHandBatsman(), LeftHandBatsman()]


for batsman in batsmen:
    # Will error as return type is list vs str as it breaks LSP
    print(batsmen.get_batsman_feature()[0])


"""
Example of LS principle implementation
"""


class Batsman:
    def __init__(self, batsman_code: str, batsman_name: str):
        self.batsman_code = batsman_code
        self.batsman_name = batsman_name

    def get_batsman_name(self) -> str:
        return self.batsman_name

    def get_batting_side(self) -> tuple:
        return ("N/A", "Unknown")


class RightHandBatsman(Batsman):
    def __init__(self):
        super().__init__("RHB", "Right hand batsman")

    def get_batting_side(self) -> tuple:
        return ("RHB", "Right handed batsman")


class LeftHandBatsman(Batsman):
    def __init__(self):
        super().__init__("LHB", "Left hand batsman")

    def get_batting_side(self) -> tuple:
        return ("LHB", "Left handed batsman")


batsmen = [Batsman(), RightHandBatsman(), LeftHandBatsman()]

for batsman in batsmen:
    print(batsmen.get_batsman_feature()[0])
