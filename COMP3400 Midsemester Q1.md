## Question 1
```haskell
f _ g bs b = fmap g (b:bs)
```

```
Prelude> :t f
f :: p -> (a -> b) -> [a] -> a -> [b]
```