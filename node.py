from itertools import permutations


class Node:
    maxLevels = []
    previousMoves = []

    def __init__(self, a: int, b: int, c: int, move: str) -> None:
        self.outcomes = []
        self.currentContainerLevel = [a, b, c]
        self.move = move

    def calculateOutcome(self) -> None:
        for containerFromI, containerToI in permutations((0, 1, 2), 2):

            waterLevels = self.__calculateWaterLevels(containerFromI, containerToI)

            if waterLevels == None or waterLevels in Node.previousMoves:
                continue
            self.previousMoves.append(waterLevels)
            self.outcomes.append(
                Node(
                    *waterLevels,
                    self.move
                    + f"\n{self.currentContainerLevel} -> {waterLevels} | {containerFromI} -> {containerToI}",
                )
            )

    def __calculateWaterLevels(self, containerFromI: int, containerToI: int) -> list:

        containerCopy = self.currentContainerLevel.copy()
        containersSum = containerCopy[containerToI] + containerCopy[containerFromI]

        if (
            containerCopy[containerFromI] <= 0
            or containerCopy[containerToI] >= Node.maxLevels[containerToI]
        ):
            return None

        containerCopy[containerToI] = min(
            Node.maxLevels[containerToI],
            containersSum,
        )
        containerCopy[containerFromI] = max(
            0, containersSum - containerCopy[containerToI]
        )
        return containerCopy
