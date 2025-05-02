## Question 3
foo and bar both take a Bool first argument and return the second argument if the boolean is true, or the third argument if it is false.

Both foo and bar require the second and third arguments to be the same type because they must have the same return type regardless of the Bool given.
```haskell
Prelude> :t foo
foo :: Bool -> p -> p -> p
Prelude> :t bar
bar :: Bool -> p -> p -> p
```

They are functionally identical. 

```haskell
Prelude> foo True 1 2
1
Prelude> foo False 1 2
2
Prelude> bar True 1 2
1
Prelude> bar False 1 2
2
```
They are polymorphic in the second and third arguments (provided they are the same type).
```haskell
Prelude> foo True 'a' 'b'
'a'
Prelude> bar True 'a' 'b'
'a'
```
Furthermore, they are both lazily evaluated so will only evaluate the argument corresponding to the boolean. The boolean is always evaluated.
```haskell
Prelude> foo undefined 1 2
*** Exception: Prelude.undefined
Prelude> bar True 1 undefined
1
Prelude> foo True 1 undefined
1
Prelude> foo False 1 undefined
*** Exception: Prelude.undefined
Prelude> bar False 1 undefined
*** Exception: Prelude.undefined
```
If you wanted, you could write this as
$$
f (\bot, x, y) = \bot, \quad f(\text{True}, x, \bot)=x, \quad f(\text{False}, \bot, y)=y, \quad \forall x,y.
$$