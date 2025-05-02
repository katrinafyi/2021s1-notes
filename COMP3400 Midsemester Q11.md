## Question 11
```haskell
rev :: [a] -> [a]
rev = h_rev []
  where
    h_rev :: [a] -> [a] -> [a]
    h_rev ys [] = ys
    h_rev ys (x:xs) = h_rev (x:ys) xs
```

The **invariant** for the helper is
```haskell
h_rev ys xs == reverse xs ++ ys
```
where `reverse` is a function which returns `xs` in reverse order. (The exact implementation of reverse is irrelevant, we only use it for reasoning about the algorithm.)

Therefore, 
```haskell
rev xs == h_rev [] xs == reverse xs ++ [] == reverse xs
```
as required.

The **bound value** for `h_rev ys xs` is `length xs`.
