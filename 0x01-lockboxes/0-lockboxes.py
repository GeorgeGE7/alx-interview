#!/usr/bin/python3
'''A module for working with lockboxes tasks.
'''


def canUnlockAll(boxes):
    '''check for boxes in a list boxes
    '''
    boxes_len = len(boxes)
    shown_boxes = set([0])
    unshown_boxes = set(boxes[0]).difference(set([0]))
    while len(unshown_boxes) > 0:
        boxIdx = unshown_boxes.pop()
        if not boxIdx or boxIdx >= boxes_len or boxIdx < 0:
            continue
        if boxIdx not in shown_boxes:
            unshown_boxes = unshown_boxes.union(boxes[boxIdx])
            shown_boxes.add(boxIdx)
    return boxes_len == len(shown_boxes)
