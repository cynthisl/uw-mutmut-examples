# Exceptions Mutations

## Raise

### Mutation 7

Change raise to pass

```
     @classmethod
     def absAvg(cls, numbers):
         if numbers is None or len(numbers) == 0:
-            raise Exception("numbers must not be null or empty.")
+            pass
 
         sum = 0
```

## Try block mutations

### Mutation 16

Replace exception handler block with pass

```
             i += 2
             print("raising FooException")
             raise FooException("foo")
-    except FooException as e:
-        # i += 4
-        print("except FooException block")
+    except FooException as e: pass
     except Exception as e:
         # i += 8
         print("except Exception block")

```

### Mutation 19

Replace exception handler block with raise

```
     except FooException as e:
         # i += 4
         print("except FooException block")
-    except Exception as e:
-        # i += 8
-        print("except Exception block")
+    except Exception as e: raise
     else:
         # i += 16
         print("else block")
```

### Mutation 20

Replace else block with pass

```
     except Exception as e:
         # i += 8
         print("except Exception block")
-    else:
-        # i += 16
-        print("else block")
+    else: pass
     finally:
         # i += 32
         print("finally block")
```

### Mutation 21

Replace finally block with pass

```
     else:
         # i += 16
         print("else block")
-    finally:
-        # i += 32
-        print("finally block")
+    finally: pass

     i += 64
     print("after all blocks, i is {}".format(i));
```


## Exception handling examples

### Raise -> pass

```
pip install pytest  # one time
cd exceptions/raise
mutmut run
mutmut show 7
```

### Raise -> pass code and test fixed

```
cd exceptions/raise-fixed
mutmut run
mutmut show
```

### Mutate exception catch, else, finally blocks

```
cd exceptions/tryblock
mutmut run
# except block -> pass
mutmut show 16 # or 18
# except block -> raise 
mutmut show 17 # or 19
# else block -> pass
mutmut show 20
# finally block -> pass
mutmut show 21
```

