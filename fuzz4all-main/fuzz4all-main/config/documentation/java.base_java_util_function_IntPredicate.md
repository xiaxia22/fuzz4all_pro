# Interface IntPredicate

**Source:** `java.base\java\util\function\IntPredicate.html`

### Class Description

```java
@FunctionalInterface

public interface
IntPredicate
```

Represents a predicate (boolean-valued function) of one

int

-valued
argument. This is the

int

-consuming primitive type specialization of

Predicate

.

This is a

functional interface

whose functional method is

test(int)

.

**Functional Interface:** This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean test​(int value)

Evaluates this predicate on the given argument.

**Parameters:**
- value

- the input argument

**Returns:**
- true

if the input argument matches the predicate,
otherwise

false

---

#### default
IntPredicate
and​(
IntPredicate
other)

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
IntPredicate
negate()

Returns a predicate that represents the logical negation of this
predicate.

**Returns:**
- a predicate that represents the logical negation of this
predicate

---

#### default
IntPredicate
or​(
IntPredicate
other)

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

#### Interface IntPredicate

**Functional Interface:** This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

```java
@FunctionalInterface

public interface
IntPredicate
```

Represents a predicate (boolean-valued function) of one

int

-valued
argument. This is the

int

-consuming primitive type specialization of

Predicate

.

This is a

functional interface

whose functional method is

test(int)

.

**Since:** 1.8
**See Also:** Predicate

@FunctionalInterface

public interface

IntPredicate

Represents a predicate (boolean-valued function) of one

int

-valued
argument. This is the

int

-consuming primitive type specialization of

Predicate

.

This is a

functional interface

whose functional method is

test(int)

.

This is a

functional interface

whose functional method is

test(int)

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

IntPredicate

and

​(

IntPredicate

other)

Returns a composed predicate that represents a short-circuiting logical
AND of this predicate and another.

default

IntPredicate

negate

()

Returns a predicate that represents the logical negation of this
predicate.

default

IntPredicate

or

​(

IntPredicate

other)

Returns a composed predicate that represents a short-circuiting logical
OR of this predicate and another.

boolean

test

​(int value)

Evaluates this predicate on the given argument.

Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

default

IntPredicate

and

​(

IntPredicate

other)

Returns a composed predicate that represents a short-circuiting logical
AND of this predicate and another.

default

IntPredicate

negate

()

Returns a predicate that represents the logical negation of this
predicate.

default

IntPredicate

or

​(

IntPredicate

other)

Returns a composed predicate that represents a short-circuiting logical
OR of this predicate and another.

boolean

test

​(int value)

Evaluates this predicate on the given argument.

---

#### Method Summary

Returns a composed predicate that represents a short-circuiting logical
AND of this predicate and another.

Returns a predicate that represents the logical negation of this
predicate.

Returns a composed predicate that represents a short-circuiting logical
OR of this predicate and another.

Evaluates this predicate on the given argument.

============ METHOD DETAIL ==========

- Method Detail

- test

```java
boolean test​(int value)
```

Evaluates this predicate on the given argument.

**Parameters:** value

- the input argument
**Returns:** true

if the input argument matches the predicate,
otherwise

false

- and

```java
default
IntPredicate
and​(
IntPredicate
other)
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
IntPredicate
negate()
```

Returns a predicate that represents the logical negation of this
predicate.

**Returns:** a predicate that represents the logical negation of this
predicate

- or

```java
default
IntPredicate
or​(
IntPredicate
other)
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
boolean test​(int value)
```

Evaluates this predicate on the given argument.

**Parameters:** value

- the input argument
**Returns:** true

if the input argument matches the predicate,
otherwise

false

- and

```java
default
IntPredicate
and​(
IntPredicate
other)
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
IntPredicate
negate()
```

Returns a predicate that represents the logical negation of this
predicate.

**Returns:** a predicate that represents the logical negation of this
predicate

- or

```java
default
IntPredicate
or​(
IntPredicate
other)
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
boolean test​(int value)
```

Evaluates this predicate on the given argument.

**Parameters:** value

- the input argument
**Returns:** true

if the input argument matches the predicate,
otherwise

false

---

#### test

boolean test​(int value)

Evaluates this predicate on the given argument.

and

```java
default
IntPredicate
and​(
IntPredicate
other)
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

IntPredicate

and​(

IntPredicate

other)

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
IntPredicate
negate()
```

Returns a predicate that represents the logical negation of this
predicate.

**Returns:** a predicate that represents the logical negation of this
predicate

---

#### negate

default

IntPredicate

negate()

Returns a predicate that represents the logical negation of this
predicate.

or

```java
default
IntPredicate
or​(
IntPredicate
other)
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

IntPredicate

or​(

IntPredicate

other)

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

