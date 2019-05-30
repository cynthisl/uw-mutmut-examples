class MutSlice(object):

    def sum(self, arr):
        arr = arr[:]
        sum = 0
        for elt in arr:
            sum += elt
        return sum

    def sum_except_last_2(self, arr):
        arr = arr[:-2]
        sum = 0
        for elt in arr:
            sum += elt
        return sum

    def sum_except_first_2(self, arr):
        arr = arr[2:]
        sum = 0
        for elt in arr:
            sum += elt
        return sum

    def sum_except_ends(self, arr):
        arr = arr[2:-2]
        sum = 0
        for elt in arr:
            sum += elt
        return sum


