## Question 8
```haskell
foo :: [Int] -> [Int]
foo []       = []
foo [x]      = [abs x]
foo (x:y:xs) = (abs x) : y : foo xs

bar :: [Int] -> [Int]
bar []       = []
bar [x]      = [x+1]
bar (x:y:xs) = (x+1) : y : bar xs
```

```haskell
vrb :: (a -> a) -> [a] -> [a]
vrb _ [] = []
vrb f [x] = [f x]
vrb f (x:y:xs) = f x : y : vrb f xs
```