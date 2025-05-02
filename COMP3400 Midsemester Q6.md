## Question 6
```haskell
[g y | y <- ys, p y]
```

```haskell
fmap g $ filter p $ ys
```