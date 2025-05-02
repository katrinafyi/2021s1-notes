# Types

#definition A **type** is _just_ a set of objects.

#definition Names of **concrete types** and concrete types correspond to exactly one set.

#definition **Abstract types** are type variables and are not capitalised. They are made concrete through type inference.

## Constructors

```haskell
data Bool = False | True
```
Here, 
- Bool is the *type constructor* (which must be capitalised),
- True and False are *data constructors*,
- the pipe `|` is an "or" separator.

Data constructors can take arguments or even be recursive.

## Pattern Matching
The below assigns "bluey" to name.
```haskell
Dog name = Dog "bluey"
```

## Function Type
The arrow `->` is also a type constructor for functions in Haskell.

## Type Classes

A typeclass is a collection of types with similar functionality. For example, the `Ord` class has instances providing <, >, and =.