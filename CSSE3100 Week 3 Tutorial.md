# Exercise 3.5
```c
method StudyPlan(n: nat)
    requires n <= 40
    decreases 40 - n 
{ 
    if n == 40 { // done } 
    else { 
        var hours := RequiredStudyTime(n); 
        Learn(n, hours); 
    } 
} 

method Learn(n: nat, h: nat) 
    requires n < 40 
    decreases 40 - n, h 
{ 
    if h == 0 { StudyPlan(n + 1); } 
    else { Learn(n, h - 1); } 
}
```

```c
method Outer(a: nat) {
    if a != 0 { 
        var b := RequiredStudyTime(a - 1); 
        Inner(a, b); 
    } 
} 

method Inner(a: nat, b: nat) 
    requires a != 0 
{ 
    if b == 0 { Outer(a - 1); } 
    else { Inner(a, b - 1); } 
}
```

Because outer calls inner with more parameters, we can try something like a truncated tuple (recall that a shorter tuple compares greater than a longer tuple with the same prefix). This would be `decreases a` on Outer.

Then, a `decreases a, b` on Inner would suffice to handle the Inner recursive calls.

-----

```c
method Outer(a: nat) 
    decreases a, 10
{ 
    if a != 0 { 
        var b := RequiredStudyTime(a - 1); 
        Inner(a - 1, b); 
    } 
} 

method Inner(a: nat, b: nat)
    decreases a, b + 10
{ 
    if b == 0 { 
        Outer(a); 
    } else { 
        Inner(a, b - 1); 
    } 
}
```