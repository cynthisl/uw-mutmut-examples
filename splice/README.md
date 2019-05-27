# Splice example

### Mutation 9

Add a splice operand: [ : x ] to [ 1 : x]

```
-        arr = arr[:-2]
+        arr = arr[1:-2]
         sum = 0
         for elt in arr:
             sum += elt
```

### Mutation 10

Remove a splice operand: [ a : b] to [ a : ]

```
     def sum_except_last_2(self, arr):
-        arr = arr[:-2]
+        arr = arr[:]
         sum = 0
         for elt in arr:
             sum += elt
```
