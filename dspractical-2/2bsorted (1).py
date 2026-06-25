print("~~~~~~~~~~~~2b. Sort a nested tuple using sorted()~~~~~~~~~~~~~~~~")


nested_tuple = ((3, 1, 2), (9, 7, 8), (6, 4, 5))


sorted_inner = tuple(sorted(t) for t in nested_tuple)
print("Inner tuples sorted:", sorted_inner)


sorted_outer = tuple(sorted(nested_tuple, key=lambda x: x[0]))
print("Outer tuple sorted by first element:", sorted_outer)


sorted_outer_full = tuple(sorted(nested_tuple))
print("Outer tuple sorted lexicographically:", sorted_outer_full)
