
class FooException(Exception):
    pass

def func(raise_exception=True):
    i = 0
    print("before try")
    try:
        i += 1
        if raise_exception:
            i += 2
            print("raising FooException")
            raise FooException("foo")
    except FooException as e:
        # i += 4
        print("except FooException block")
    except Exception as e:
        # i += 8
        print("except Exception block")
    else:
        # i += 16
        print("else block")
    finally:
        # i += 32
        print("finally block")

    i += 64
    print("after all blocks, i is {}".format(i));
    return i

if __name__ == "__main__":
    func()
    func(raise_exception=False)

