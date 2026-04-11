# Interface LongUnaryOperator

**Source:** `java.base\java\util\function\LongUnaryOperator.html`

### Class Description

```java
@FunctionalInterface

public interface
LongUnaryOperator
```

Represents an operation on a single

long

-valued operand that produces
a

long

-valued result. This is the primitive type specialization of

UnaryOperator

for

long

.

This is a

functional interface

whose functional method is

applyAsLong(long)

.

**Functional Interface:** This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### long applyAsLong​(long operand)

Applies this operator to the given operand.

**Parameters:**
- operand

- the operand

**Returns:**
- the operator result

---

#### default
LongUnaryOperator
compose​(
LongUnaryOperator
before)

Returns a composed operator that first applies the

before

operator to its input, and then applies this operator to the result.
If evaluation of either operator throws an exception, it is relayed to
the caller of the composed operator.

**Parameters:**
- before

- the operator to apply before this operator is applied

**Returns:**
- a composed operator that first applies the

before

operator and then applies this operator

**Throws:**
- NullPointerException

- if before is null

**See Also:**
- andThen(LongUnaryOperator)

---

#### default
LongUnaryOperator
andThen​(
LongUnaryOperator
after)

Returns a composed operator that first applies this operator to
its input, and then applies the

after

operator to the result.
If evaluation of either operator throws an exception, it is relayed to
the caller of the composed operator.

**Parameters:**
- after

- the operator to apply after this operator is applied

**Returns:**
- a composed operator that first applies this operator and then
applies the

after

operator

**Throws:**
- NullPointerException

- if after is null

**See Also:**
- compose(LongUnaryOperator)

---

#### static
LongUnaryOperator
identity()

Returns a unary operator that always returns its input argument.

**Returns:**
- a unary operator that always returns its input argument

---

### Additional Sections

#### Interface LongUnaryOperator

**Functional Interface:** This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

```java
@FunctionalInterface

public interface
LongUnaryOperator
```

Represents an operation on a single

long

-valued operand that produces
a

long

-valued result. This is the primitive type specialization of

UnaryOperator

for

long

.

This is a

functional interface

whose functional method is

applyAsLong(long)

.

**Since:** 1.8
**See Also:** UnaryOperator

@FunctionalInterface

public interface

LongUnaryOperator

Represents an operation on a single

long

-valued operand that produces
a

long

-valued result. This is the primitive type specialization of

UnaryOperator

for

long

.

This is a

functional interface

whose functional method is

applyAsLong(long)

.

This is a

functional interface

whose functional method is

applyAsLong(long)

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

default

LongUnaryOperator

andThen

​(

LongUnaryOperator

after)

Returns a composed operator that first applies this operator to
its input, and then applies the

after

operator to the result.

long

applyAsLong

​(long operand)

Applies this operator to the given operand.

default

LongUnaryOperator

compose

​(

LongUnaryOperator

before)

Returns a composed operator that first applies the

before

operator to its input, and then applies this operator to the result.

static

LongUnaryOperator

identity

()

Returns a unary operator that always returns its input argument.

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

default

LongUnaryOperator

andThen

​(

LongUnaryOperator

after)

Returns a composed operator that first applies this operator to
its input, and then applies the

after

operator to the result.

long

applyAsLong

​(long operand)

Applies this operator to the given operand.

default

LongUnaryOperator

compose

​(

LongUnaryOperator

before)

Returns a composed operator that first applies the

before

operator to its input, and then applies this operator to the result.

static

LongUnaryOperator

identity

()

Returns a unary operator that always returns its input argument.

---

#### Method Summary

Returns a composed operator that first applies this operator to
its input, and then applies the

after

operator to the result.

Applies this operator to the given operand.

Returns a composed operator that first applies the

before

operator to its input, and then applies this operator to the result.

Returns a unary operator that always returns its input argument.

============ METHOD DETAIL ==========

- Method Detail

- applyAsLong

```java
long applyAsLong​(long operand)
```

Applies this operator to the given operand.

**Parameters:** operand

- the operand
**Returns:** the operator result

- compose

```java
default
LongUnaryOperator
compose​(
LongUnaryOperator
before)
```

Returns a composed operator that first applies the

before

operator to its input, and then applies this operator to the result.
If evaluation of either operator throws an exception, it is relayed to
the caller of the composed operator.

**Parameters:** before

- the operator to apply before this operator is applied
**Returns:** a composed operator that first applies the

before

operator and then applies this operator
**Throws:** NullPointerException

- if before is null
**See Also:** andThen(LongUnaryOperator)

- andThen

```java
default
LongUnaryOperator
andThen​(
LongUnaryOperator
after)
```

Returns a composed operator that first applies this operator to
its input, and then applies the

after

operator to the result.
If evaluation of either operator throws an exception, it is relayed to
the caller of the composed operator.

**Parameters:** after

- the operator to apply after this operator is applied
**Returns:** a composed operator that first applies this operator and then
applies the

after

operator
**Throws:** NullPointerException

- if after is null
**See Also:** compose(LongUnaryOperator)

- identity

```java
static
LongUnaryOperator
identity()
```

Returns a unary operator that always returns its input argument.

**Returns:** a unary operator that always returns its input argument

Method Detail

- applyAsLong

```java
long applyAsLong​(long operand)
```

Applies this operator to the given operand.

**Parameters:** operand

- the operand
**Returns:** the operator result

- compose

```java
default
LongUnaryOperator
compose​(
LongUnaryOperator
before)
```

Returns a composed operator that first applies the

before

operator to its input, and then applies this operator to the result.
If evaluation of either operator throws an exception, it is relayed to
the caller of the composed operator.

**Parameters:** before

- the operator to apply before this operator is applied
**Returns:** a composed operator that first applies the

before

operator and then applies this operator
**Throws:** NullPointerException

- if before is null
**See Also:** andThen(LongUnaryOperator)

- andThen

```java
default
LongUnaryOperator
andThen​(
LongUnaryOperator
after)
```

Returns a composed operator that first applies this operator to
its input, and then applies the

after

operator to the result.
If evaluation of either operator throws an exception, it is relayed to
the caller of the composed operator.

**Parameters:** after

- the operator to apply after this operator is applied
**Returns:** a composed operator that first applies this operator and then
applies the

after

operator
**Throws:** NullPointerException

- if after is null
**See Also:** compose(LongUnaryOperator)

- identity

```java
static
LongUnaryOperator
identity()
```

Returns a unary operator that always returns its input argument.

**Returns:** a unary operator that always returns its input argument

---

#### Method Detail

applyAsLong

```java
long applyAsLong​(long operand)
```

Applies this operator to the given operand.

**Parameters:** operand

- the operand
**Returns:** the operator result

---

#### applyAsLong

long applyAsLong​(long operand)

Applies this operator to the given operand.

compose

```java
default
LongUnaryOperator
compose​(
LongUnaryOperator
before)
```

Returns a composed operator that first applies the

before

operator to its input, and then applies this operator to the result.
If evaluation of either operator throws an exception, it is relayed to
the caller of the composed operator.

**Parameters:** before

- the operator to apply before this operator is applied
**Returns:** a composed operator that first applies the

before

operator and then applies this operator
**Throws:** NullPointerException

- if before is null
**See Also:** andThen(LongUnaryOperator)

---

#### compose

default

LongUnaryOperator

compose​(

LongUnaryOperator

before)

Returns a composed operator that first applies the

before

operator to its input, and then applies this operator to the result.
If evaluation of either operator throws an exception, it is relayed to
the caller of the composed operator.

andThen

```java
default
LongUnaryOperator
andThen​(
LongUnaryOperator
after)
```

Returns a composed operator that first applies this operator to
its input, and then applies the

after

operator to the result.
If evaluation of either operator throws an exception, it is relayed to
the caller of the composed operator.

**Parameters:** after

- the operator to apply after this operator is applied
**Returns:** a composed operator that first applies this operator and then
applies the

after

operator
**Throws:** NullPointerException

- if after is null
**See Also:** compose(LongUnaryOperator)

---

#### andThen

default

LongUnaryOperator

andThen​(

LongUnaryOperator

after)

Returns a composed operator that first applies this operator to
its input, and then applies the

after

operator to the result.
If evaluation of either operator throws an exception, it is relayed to
the caller of the composed operator.

identity

```java
static
LongUnaryOperator
identity()
```

Returns a unary operator that always returns its input argument.

**Returns:** a unary operator that always returns its input argument

---

#### identity

static

LongUnaryOperator

identity()

Returns a unary operator that always returns its input argument.

---

