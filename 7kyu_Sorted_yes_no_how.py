def is_sorted_and_how(arr):
    rasc = sorted(arr)
    rdsc = sorted(arr,reverse=True)
    if arr == rasc: return "yes, ascending"
    if arr == rdsc: return "yes, descending"
    return "no"

print(is_sorted_and_how([15, 7, 3, -8]))