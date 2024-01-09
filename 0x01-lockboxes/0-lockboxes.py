#!/usr/bin/python3
""" A script for lockboxes."""

from collections import deque


def canUnlockAll(boxes):
    """ Function that checks if all boxes can be opened."""
    my_boxes = set()
    queue = deque([0])

    while queue:
        current_box = queue.popleft()
        my_boxes.add(current_box)

        for key in boxes[current_box]:
            if key not in my_boxes:
                queue.append(key)

    return len(my_boxes) == len(boxes)
