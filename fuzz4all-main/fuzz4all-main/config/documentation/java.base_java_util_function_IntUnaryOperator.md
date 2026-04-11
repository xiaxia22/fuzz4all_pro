# Interface IntUnaryOperator

**Source:** `java.base\java\util\function\IntUnaryOperator.html`

### Class Description

```java
@FunctionalInterface

public interface
IntUnaryOperator
```

Represents an operation on a single

int

-valued operand that produces
an

int

-valued result. This is the primitive type specialization of

UnaryOperator

for

int

.

This is a

functional interface

whose functional method is

applyAsInt(int)

.

**Functional Interface:** This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### int applyAsInt​(int operand)

Applies this operator to the given operand.

**Parameters:**
- operand

- the operand

**Returns:**
- the operator result

---

#### default
IntUnaryOperator
compose​(
IntUnaryOperator
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
- andThen(IntUnaryOperator)

---

#### default
IntUnaryOperator
andThen​(
IntUnaryOperator
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
- compose(IntUnaryOperator)

---

#### static
IntUnaryOperator
identity()

Returns a unary operator that always returns its input argument.

**Returns:**
- a unary operator that always returns its input argument

---

### Additional Sections

#### Interface IntUnaryOperator

**Functional Interface:** This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

```java
@FunctionalInterface

public interface
IntUnaryOperator
```

Represents an operation on a single

int

-valued operand that produces
an

int

-valued result. This is the primitive type specialization of

UnaryOperator

for

int

.

This is a

functional interface

whose functional method is

applyAsInt(int)

.

**Since:** 1.8
**See Also:** UnaryOperator

@FunctionalInterface

public interface

IntUnaryOperator

Represents an operation on a single

int

-valued operand that produces
an

int

-valued result. This is the primitive type specialization of

UnaryOperator

for

int

.

This is a

functional interface

whose functional method is

applyAsInt(int)

.

This is a

functional interface

whose functional method is

applyAsInt(int)

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

IntUnaryOperator

andThen

​(

IntUnaryOperator

after)

Returns a composed operator that first applies this operator to
its input, and then applies the

after

operator to the result.

int

applyAsInt

​(int operand)

Applies this operator to the given operand.

default

IntUnaryOperator

compose

​(

IntUnaryOperator

before)

Returns a composed operator that first applies the

before

operator to its input, and then applies this operator to the result.

static

IntUnaryOperator

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

IntUnaryOperator

andThen

​(

IntUnaryOperator

after)

Returns a composed operator that first applies this operator to
its input, and then applies the

after

operator to the result.

int

applyAsInt

​(int operand)

Applies this operator to the given operand.

default

IntUnaryOperator

compose

​(

IntUnaryOperator

before)

Returns a composed operator that first applies the

before

operator to its input, and then applies this operator to the result.

static

IntUnaryOperator

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

- applyAsInt

```java
int applyAsInt​(int operand)
```

Applies this operator to the given operand.

**Parameters:** operand

- the operand
**Returns:** the operator result

- compose

```java
default
IntUnaryOperator
compose​(
IntUnaryOperator
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
**See Also:** andThen(IntUnaryOperator)

- andThen

```java
default
IntUnaryOperator
andThen​(
IntUnaryOperator
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
**See Also:** compose(IntUnaryOperator)

- identity

```java
static
IntUnaryOperator
identity()
```

Returns a unary operator that always returns its input argument.

**Returns:** a unary operator that always returns its input argument

Method Detail

- applyAsInt

```java
int applyAsInt​(int operand)
```

Applies this operator to the given operand.

**Parameters:** operand

- the operand
**Returns:** the operator result

- compose

```java
default
IntUnaryOperator
compose​(
IntUnaryOperator
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
**See Also:** andThen(IntUnaryOperator)

- andThen

```java
default
IntUnaryOperator
andThen​(
IntUnaryOperator
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
**See Also:** compose(IntUnaryOperator)

- identity

```java
static
IntUnaryOperator
identity()
```

Returns a unary operator that always returns its input argument.

**Returns:** a unary operator that always returns its input argument

---

#### Method Detail

applyAsInt

```java
int applyAsInt​(int operand)
```

Applies this operator to the given operand.

**Parameters:** operand

- the operand
**Returns:** the operator result

---

#### applyAsInt

int applyAsInt​(int operand)

Applies this operator to the given operand.

compose

```java
default
IntUnaryOperator
compose​(
IntUnaryOperator
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
**See Also:** andThen(IntUnaryOperator)

---

#### compose

default

IntUnaryOperator

compose​(

IntUnaryOperator

before)

Returns a composed operator that first applies the

before

operator to its input, and then applies this operator to the result.
If evaluation of either operator throws an exception, it is relayed to
the caller of the composed operator.

andThen

```java
default
IntUnaryOperator
andThen​(
IntUnaryOperator
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
**See Also:** compose(IntUnaryOperator)

---

#### andThen

default

IntUnaryOperator

andThen​(

IntUnaryOperator

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
IntUnaryOperator
identity()
```

Returns a unary operator that always returns its input argument.

**Returns:** a unary operator that always returns its input argument

---

#### identity

static

IntUnaryOperator

identity()

Returns a unary operator that always returns its input argument.

---

