"""
Join the following sets into one, called my_set_3:

{1, 2, "three", "four"}

{"three", 4, 5}

======================================================

Une los siguientes sets en uno solo, llamado mi_set_3:

{1, 2, "tres", "cuatro"}

{"tres", 4, 5}
"""

my_set_1 = {1, 2, "three", "four"}
my_set_2 = {"three", 4, 5}
my_set_3 = my_set_1.union(my_set_2)

print("************")
mi_set_1 = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5}
mi_set_3 = mi_set_1.union(mi_set_2)