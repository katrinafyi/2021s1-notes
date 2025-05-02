## Question 5
```haskell
a = [(x,y) | x <- [1,2], y <- [3,4]]
```

```haskell
b = [flip (,) y | y <- [3, 4]]
c = concat [fmap ($x) b | x <- [1,2]]
```
Then, `c == a`. I'm very sorry.