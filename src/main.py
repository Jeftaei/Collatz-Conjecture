import time


class Node:
    def __init__(self, parent, value) -> None:
        self.parent: Node | None = parent
        self.value: int = value


class CollatzAlgorithm:
    def __init__(self, value: int, stopAfter: int = 5000) -> None:
        self.curValue = value
        self.originalValue = value
        self.node: Node = None
        self.NodeList: list[int] = ...

        self.stopAfter = stopAfter

    def Step(self):
        # convert to int so we dont have a trailing 0 every time because division always returns a float
        self.curValue = int(
            self.curValue / 2 if self.curValue % 2 == 0 else (self.curValue * 3) + 1
        )

        self.node = Node(None if not self.node else self.node, self.curValue)

    def checkNodesForRepetition(self) -> bool:
        # if the value is 4 or 1 then it will ALWAYS be put into infinite repetition, assuming all the values are positive whole numbers
        return True if self.node.value in (4, 1) else False

    def gatherNodeValues(self) -> list[int]:
        vals = []

        node = self.node
        while node.parent != None:
            vals.append(node.value)
            node = node.parent

        # have to reverse the list since we are going from the last node to the first to get values
        vals.reverse()
        self.NodeList = vals

    def startSim(self):
        start = time.time()

        stopAfter = self.stopAfter

        idx = 0

        while idx < stopAfter:
            self.Step()

            if self.checkNodesForRepetition():
                break

            idx += 1

        self.gatherNodeValues()

        return f"""
            Finished At: {idx}/{stopAfter} Loops
            Took: {time.time() - start}
            Starting Value: {self.originalValue}
            Ending Value: {self.curValue}
            All Values (cut ver.): [{', '.join([str(i) for i in self.NodeList[0:15]]) + (', ...' if len(self.NodeList) > 15 else '')}] See CollatzAlgorithm.NodeList for full\n\n
            """


while True:
    num = int(input("Pick any random whole number: "))

    c = CollatzAlgorithm(num)
    print("Starting Sim...")
    output = c.startSim()
    print(f"Finished!\n\n{output}")

    full = input("Would you like to see the full NodeList? ")
    if full.lower().strip() in ["yes", "y"]:
        print(c.NodeList, "\n\n")

    yn = input("Would you like to try another number? ")
    if yn.lower().strip() in ["yes", "y"]:
        continue
    else:
        break
