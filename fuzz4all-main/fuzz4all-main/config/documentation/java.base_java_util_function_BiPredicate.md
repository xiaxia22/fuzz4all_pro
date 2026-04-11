# Interface BiPredicate<T,​U>

**Source:** `java.base\java\util\function\BiPredicate.html`

### Class Description

```java
@FunctionalInterface

public interface
BiPredicate<T,​U>
```

Represents a predicate (boolean-valued function) of two arguments. This is
the two-arity specialization of

Predicate

.

This is a

functional interface

whose functional method is

test(Object, Object)

.

**Type Parameters:** T

- the type of the first argument to the predicate
**Type Parameters:** U

- the type of the second argument the predicate

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean test​(
T
t,

U
u)

Evaluates this predicate on the given arguments.

**Parameters:**
- t

- the first input argument
- u

- the second input argument

**Returns:**
- true

if the input arguments match the predicate,
otherwise

false

---

#### default
BiPredicate
<
T
,​
U
> and​(
BiPredicate
<? super
T
,​? super
U
> other)

Returns a composed predicate that represents a short-circuiting logical
AND of this predicate and another. When evaluating the composed
predicate, if this predicate is

false

, then the

other

predicate is not evaluated.

Any exceptions thrown during evaluation of either predicate are relayed
to the caller; if evaluation of this predicate throws an exception, the

other

predicate will not be evaluated.

**Parameters:**
- other

- a predicate that will be logically-ANDed with this
predicate

**Returns:**
- a composed predicate that represents the short-circuiting logical
AND of this predicate and the

other

predicate

**Throws:**
- NullPointerException

- if other is null

---

#### default
BiPredicate
<
T
,​
U
> negate()

Returns a predicate that represents the logical negation of this
predicate.

**Returns:**
- a predicate that represents the logical negation of this
predicate

---

#### default
BiPredicate
<
T
,​
U
> or​(
BiPredicate
<? super
T
,​? super
U
> other)

Returns a composed predicate that represents a short-circuiting logical
OR of this predicate and another. When evaluating the composed
predicate, if this predicate is

true

, then the

other

predicate is not evaluated.

Any exceptions thrown during evaluation of either predicate are relayed
to the caller; if evaluation of this predicate throws an exception, the

other

predicate will not be evaluated.

**Parameters:**
- other

- a predicate that will be logically-ORed with this
predicate

**Returns:**
- a composed predicate that represents the short-circuiting logical
OR of this predicate and the

other

predicate

**Throws:**
- NullPointerException

- if other is null

---

### Additional Sections

#### Interface BiPredicate<T,​U>

**Type Parameters:** T

- the type of the first argument to the predicate
**Type Parameters:** U

- the type of the second argument the predicate

**Functional Interface:** This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

```java
@FunctionalInterface

public interface
BiPredicate<T,​U>
```

Represents a predicate (boolean-valued function) of two arguments. This is
the two-arity specialization of

Predicate

.

This is a

functional interface

whose functional method is

test(Object, Object)

.

**Since:** 1.8
**See Also:** Predicate

@FunctionalInterface

public interface

BiPredicate<T,​U>

Represents a predicate (boolean-valued function) of two arguments. This is
the two-arity specialization of

Predicate

.

This is a

functional interface

whose functional method is

test(Object, Object)

.

This is a

functional interface

whose functional method is

test(Object, Object)

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

default

BiPredicate

<

T

,​

U

>

and

​(

BiPredicate

<? super

T

,​? super

U

> other)

Returns a composed predicate that represents a short-circuiting logical
AND of this predicate and another.

default

BiPredicate

<

T

,​

U

>

negate

()

Returns a predicate that represents the logical negation of this
predicate.

default

BiPredicate

<

T

,​

U

>

or

​(

BiPredicate

<? super

T

,​? super

U

> other)

Returns a composed predicate that represents a short-circuiting logical
OR of this predicate and another.

boolean

test

​(

T

t,

U

u)

Evaluates this predicate on the given arguments.

Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

default

BiPredicate

<

T

,​

U

>

and

​(

BiPredicate

<? super

T

,​? super

U

> other)

Returns a composed predicate that represents a short-circuiting logical
AND of this predicate and another.

default

BiPredicate

<

T

,​

U

>

negate

()

Returns a predicate that represents the logical negation of this
predicate.

default

BiPredicate

<

T

,​

U

>

or

​(

BiPredicate

<? super

T

,​? super

U

> other)

Returns a composed predicate that represents a short-circuiting logical
OR of this predicate and another.

boolean

test

​(

T

t,

U

u)

Evaluates this predicate on the given arguments.

---

#### Method Summary

Returns a composed predicate that represents a short-circuiting logical
AND of this predicate and another.

Returns a predicate that represents the logical negation of this
predicate.

Returns a composed predicate that represents a short-circuiting logical
OR of this predicate and another.

Evaluates this predicate on the given arguments.

============ METHOD DETAIL ==========

- Method Detail

- test

```java
boolean test​(
T
t,

U
u)
```

Evaluates this predicate on the given arguments.

**Parameters:** t

- the first input argument
**Parameters:** u

- the second input argument
**Returns:** true

if the input arguments match the predicate,
otherwise

false

- and

```java
default
BiPredicate
<
T
,​
U
> and​(
BiPredicate
<? super
T
,​? super
U
> other)
```

Returns a composed predicate that represents a short-circuiting logical
AND of this predicate and another. When evaluating the composed
predicate, if this predicate is

false

, then the

other

predicate is not evaluated.

Any exceptions thrown during evaluation of either predicate are relayed
to the caller; if evaluation of this predicate throws an exception, the

other

predicate will not be evaluated.

**Parameters:** other

- a predicate that will be logically-ANDed with this
predicate
**Returns:** a composed predicate that represents the short-circuiting logical
AND of this predicate and the

other

predicate
**Throws:** NullPointerException

- if other is null

- negate

```java
default
BiPredicate
<
T
,​
U
> negate()
```

Returns a predicate that represents the logical negation of this
predicate.

**Returns:** a predicate that represents the logical negation of this
predicate

- or

```java
default
BiPredicate
<
T
,​
U
> or​(
BiPredicate
<? super
T
,​? super
U
> other)
```

Returns a composed predicate that represents a short-circuiting logical
OR of this predicate and another. When evaluating the composed
predicate, if this predicate is

true

, then the

other

predicate is not evaluated.

Any exceptions thrown during evaluation of either predicate are relayed
to the caller; if evaluation of this predicate throws an exception, the

other

predicate will not be evaluated.

**Parameters:** other

- a predicate that will be logically-ORed with this
predicate
**Returns:** a composed predicate that represents the short-circuiting logical
OR of this predicate and the

other

predicate
**Throws:** NullPointerException

- if other is null

Method Detail

- test

```java
boolean test​(
T
t,

U
u)
```

Evaluates this predicate on the given arguments.

**Parameters:** t

- the first input argument
**Parameters:** u

- the second input argument
**Returns:** true

if the input arguments match the predicate,
otherwise

false

- and

```java
default
BiPredicate
<
T
,​
U
> and​(
BiPredicate
<? super
T
,​? super
U
> other)
```

Returns a composed predicate that represents a short-circuiting logical
AND of this predicate and another. When evaluating the composed
predicate, if this predicate is

false

, then the

other

predicate is not evaluated.

Any exceptions thrown during evaluation of either predicate are relayed
to the caller; if evaluation of this predicate throws an exception, the

other

predicate will not be evaluated.

**Parameters:** other

- a predicate that will be logically-ANDed with this
predicate
**Returns:** a composed predicate that represents the short-circuiting logical
AND of this predicate and the

other

predicate
**Throws:** NullPointerException

- if other is null

- negate

```java
default
BiPredicate
<
T
,​
U
> negate()
```

Returns a predicate that represents the logical negation of this
predicate.

**Returns:** a predicate that represents the logical negation of this
predicate

- or

```java
default
BiPredicate
<
T
,​
U
> or​(
BiPredicate
<? super
T
,​? super
U
> other)
```

Returns a composed predicate that represents a short-circuiting logical
OR of this predicate and another. When evaluating the composed
predicate, if this predicate is

true

, then the

other

predicate is not evaluated.

Any exceptions thrown during evaluation of either predicate are relayed
to the caller; if evaluation of this predicate throws an exception, the

other

predicate will not be evaluated.

**Parameters:** other

- a predicate that will be logically-ORed with this
predicate
**Returns:** a composed predicate that represents the short-circuiting logical
OR of this predicate and the

other

predicate
**Throws:** NullPointerException

- if other is null

---

#### Method Detail

test

```java
boolean test​(
T
t,

U
u)
```

Evaluates this predicate on the given arguments.

**Parameters:** t

- the first input argument
**Parameters:** u

- the second input argument
**Returns:** true

if the input arguments match the predicate,
otherwise

false

---

#### test

boolean test​(

T

t,

U

u)

Evaluates this predicate on the given arguments.

and

```java
default
BiPredicate
<
T
,​
U
> and​(
BiPredicate
<? super
T
,​? super
U
> other)
```

Returns a composed predicate that represents a short-circuiting logical
AND of this predicate and another. When evaluating the composed
predicate, if this predicate is

false

, then the

other

predicate is not evaluated.

Any exceptions thrown during evaluation of either predicate are relayed
to the caller; if evaluation of this predicate throws an exception, the

other

predicate will not be evaluated.

**Parameters:** other

- a predicate that will be logically-ANDed with this
predicate
**Returns:** a composed predicate that represents the short-circuiting logical
AND of this predicate and the

other

predicate
**Throws:** NullPointerException

- if other is null

---

#### and

default

BiPredicate

<

T

,​

U

> and​(

BiPredicate

<? super

T

,​? super

U

> other)

Returns a composed predicate that represents a short-circuiting logical
AND of this predicate and another. When evaluating the composed
predicate, if this predicate is

false

, then the

other

predicate is not evaluated.

Any exceptions thrown during evaluation of either predicate are relayed
to the caller; if evaluation of this predicate throws an exception, the

other

predicate will not be evaluated.

Any exceptions thrown during evaluation of either predicate are relayed
to the caller; if evaluation of this predicate throws an exception, the

other

predicate will not be evaluated.

negate

```java
default
BiPredicate
<
T
,​
U
> negate()
```

Returns a predicate that represents the logical negation of this
predicate.

**Returns:** a predicate that represents the logical negation of this
predicate

---

#### negate

default

BiPredicate

<

T

,​

U

> negate()

Returns a predicate that represents the logical negation of this
predicate.

or

```java
default
BiPredicate
<
T
,​
U
> or​(
BiPredicate
<? super
T
,​? super
U
> other)
```

Returns a composed predicate that represents a short-circuiting logical
OR of this predicate and another. When evaluating the composed
predicate, if this predicate is

true

, then the

other

predicate is not evaluated.

Any exceptions thrown during evaluation of either predicate are relayed
to the caller; if evaluation of this predicate throws an exception, the

other

predicate will not be evaluated.

**Parameters:** other

- a predicate that will be logically-ORed with this
predicate
**Returns:** a composed predicate that represents the short-circuiting logical
OR of this predicate and the

other

predicate
**Throws:** NullPointerException

- if other is null

---

#### or

default

BiPredicate

<

T

,​

U

> or​(

BiPredicate

<? super

T

,​? super

U

> other)

Returns a composed predicate that represents a short-circuiting logical
OR of this predicate and another. When evaluating the composed
predicate, if this predicate is

true

, then the

other

predicate is not evaluated.

Any exceptions thrown during evaluation of either predicate are relayed
to the caller; if evaluation of this predicate throws an exception, the

other

predicate will not be evaluated.

Any exceptions thrown during evaluation of either predicate are relayed
to the caller; if evaluation of this predicate throws an exception, the

other

predicate will not be evaluated.

---

