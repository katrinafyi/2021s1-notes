## Question 4

```haskell
Prelude> :t exists
exists :: [a] -> (a -> Bool) -> Bool
```

`exists [] p` should return False for all p because there is no $x \in X$ which satisfies $P(x)$ (there is, in fact, no $x \in X$ at all).

This will also help us formulate the function recursively as
```haskell
exists [] _ = False
exists (x:xs) p = p x || exists xs p
```
because False is the identity for boolean or.