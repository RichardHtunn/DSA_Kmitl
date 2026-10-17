def can_check(c, k, weights):
    """Check capacity c while preserving the order of the items."""
    if k <= 0 or c < 0:
        return False

    boxes_needed = 1
    current_box_weight = 0

    for weight in weights:
        if weight < 0 or weight > c:
            return False

        if current_box_weight + weight <= c:
            current_box_weight += weight
        else:
            boxes_needed += 1
            current_box_weight = weight

            if boxes_needed > k:
                return False

    return True


def find_min_capacity(weights, boxes):
    if not weights:
        raise ValueError("at least one item weight is required")
    if boxes <= 0:
        raise ValueError("the number of boxes must be positive")
    if any(weight < 0 for weight in weights):
        raise ValueError("item weights must be nonnegative")

    lower = max(weights)
    upper = sum(weights)

    while lower < upper:
        middle = (lower + upper) // 2

        if can_check(middle, boxes, weights):
            upper = middle
        else:
            lower = middle + 1

    return lower


def main():
    try:
        items_weight, boxes = input("Enter Input : ").split("/")
        weights = list(map(int, items_weight.split()))
        boxes = int(boxes)
        capacity = find_min_capacity(weights, boxes)
    except ValueError as error:
        print("Invalid input:", error)
        return

    # Preserve the original spelling for compatibility with quiz output.
    print(f"Minimum weigth for {boxes} box(es) = {capacity}")


if __name__ == "__main__":
    main()
