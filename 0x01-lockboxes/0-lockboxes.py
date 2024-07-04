#!/usr/bin/python3

def canUnlockAll(boxes):
    if not boxes:
        return False

    keys = set(boxes[0])
    unlocked = set([0])

    while True:
        new_unlocked = set()
        for box_index in range(len(boxes)):
            if box_index in keys and box_index not in unlocked:
                new_unlocked.add(box_index)
                keys.update(boxes[box_index])
        if not new_unlocked:
            break
        unlocked.update(new_unlocked)

    return len(unlocked) == len(boxes)

