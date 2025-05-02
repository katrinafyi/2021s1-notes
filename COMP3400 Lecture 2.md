# Haskell First Steps
`:` denotes a REPL command in ghci. Here are some basic ones:
```
:quit   :q
:info   :i
:type   :t
:load   :l
:reload :r
```

## Files
It is good practice to name modules the same as as the filename but capitalised. Variables and functions are not capitalised.

## Prompt
We can replace the default `Prelude>` prompt with
```
:set prompt "\lambda> "
```

## Operators
Suppose we have a function $\oplus : A \to B \to C$. Remember that we only have univariate functions and $\oplus$ actually returns a function $B \to C$. 

A function of two variables can be written infix or prefix. Infix operators can be made prefix by using parentheses.

## Integer arithmetic
mod returns a number with the same sign as its second argument.

## Functions
The lambda expression $(\lambda x.\lambda y.x-y)\ 3\ 2$ can be written in Haskell as
```
(\x -> \y -> x - y) 3 2
```
or using a short form for multiple variables,
```
(\x y -> x - y) 3 2
```

We can also name it and omit the lambdas:
```
f x y = x - y
```

### Sectioning

Infix operators can be sectioned. The following are all equivalent.
```
1 + 2
(+) 1 2
(+1) 2
```

## Apply
The `$` infix operator is defined as `f $ a = f a`. It is useful because it can reduce the number of brackets in an expression by having the lowest possible precedence.

## Let and where
```
x = y * z
    where
        y = 2
        z = 3

t = let
    y = 2
    z = 2
  in
    y * z