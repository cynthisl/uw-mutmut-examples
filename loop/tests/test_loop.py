from loop import MutLoop

KILL_ZERO_FOR = False  # mutant 4
KILL_ONE_FOR = False  # mutant 5
KILL_INLINE = False  # mutant 11
KILL_ZERO_WHILE = False  # mutant 19
KILL_ONE_WHILE = False  # mutant 20

class TestMutLoop:
    
    def test_simpleFor(self):
        ml = MutLoop()
        assert ml.simpleFor(0) == []

    def test_killZeroFor(self):
        if not KILL_ZERO_FOR:
            return
        ml = MutLoop()
        assert ml.simpleFor(1) == [0]

    def test_killOneFor(self):
        if not KILL_ONE_FOR:
            return
        ml = MutLoop()
        assert ml.simpleFor(2) == [0, 1]

    def test_inlineFor(self):
        ml = MutLoop()
        assert ml.inlineFor(0) == []

    def test_killZeroInlineFor(self):
        if not KILL_INLINE:
            return
        ml = MutLoop()
        assert ml.inlineFor(1) == [1]

    def test_simpleWhile(self):
        ml = MutLoop()
        assert ml.simpleWhile(0) == []

    def test_killZeroWhile(self):
        if not KILL_ZERO_WHILE:
            return
        ml = MutLoop()
        assert ml.simpleWhile(1) == [0]

    def test_killOneWhile(self):
        if not KILL_ONE_WHILE:
            return
        ml = MutLoop()
        assert ml.simpleWhile(2) == [0, 1]
