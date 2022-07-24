from node import Node

# CHANGE
WATERLEVELS = [5, 0, 3]  # Adjust starting water levels
WATERLEVELTARGET = 4  # Adjust goal amount in middle bucket
Node.maxLevels = [5, 8, 3]  # Adjust maximum water levels


def main():
    startingNode = Node(*WATERLEVELS, "starting")
    q = [startingNode]
    movesToReachGoal = []
    find = False

    while q:
        node = q.pop()
        node.calculateOutcome()
        for i in node.outcomes:
            q.append(i)

            if WATERLEVELTARGET == i.currentContainerLevel[1]:
                movesToReachGoal = i.move
                find = True
                break

        if find:
            break

    if movesToReachGoal:
        print(movesToReachGoal)

    else:
        print(f"Reach {WATERLEVELTARGET} is impossible")


if __name__ == "__main__":
    main()
