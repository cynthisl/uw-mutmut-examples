# Loop example

## For Loop Mutations

### Mutation 4

Loop runs 0 times

```
-        for i in input_list: 
+        for i in []: 
             output_list.append(i)
         return output_list
```

### Mutation 5

Loop only runs once

```
         for i in input_list: 
             output_list.append(i)
+            break
         return output_list

```

## List Comprehension For Loop Muation

### Mutation 11

Loop runs 0 times

```
-        output_list = [y+1 for y in input_list]
+        output_list = [y+1 for y in []]
```

## While Loop Mutations

### Mutation 18

Loop runs 0 times

```
         while i < x:
+            break
             output_list.append(i)
             i += 1
```

### Mutation 19

Loop runs only once

```
         while i < x:
             output_list.append(i)
             i += 1
+            break
         return output_list
 
```
