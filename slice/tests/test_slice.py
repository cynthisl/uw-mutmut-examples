from slice import MutSlice

class TestMutSlice:

    def test_sum(self):
        ms = MutSlice()
        arr = [1, 2, 3, 4, 5]
        result = ms.sum(arr)
        
        # assert result == 15, "test failed"

    def test_sum_except_last_2(self):
        ms = MutSlice()
        arr = [1, 2, 3, 4, 5]
        result = ms.sum_except_last_2(arr)
        
        # assert result == 6, "test failed"

    def test_sum_except_first_2(self):
        ms = MutSlice()
        arr = [1, 2, 3, 4, 5]
        result = ms.sum_except_first_2(arr)
        
        # assert result == 12, "test failed"

    def test_sum_except_ends(self):
        ms = MutSlice()
        arr = [1, 2, 3, 4, 5]
        result = ms.sum_except_ends(arr)
        
        # assert result == 3, "test failed"

