# Interface DoubleUnaryOperator

**Source:** `java.base\java\util\function\DoubleUnaryOperator.html`

### Class Description

```java
@FunctionalInterface

public interface
DoubleUnaryOperator
```

Represents an operation on a single

double

-valued operand that produces
a

double

-valued result. This is the primitive type specialization of

UnaryOperator

for

double

.

This is a

functional interface

whose functional method is

applyAsDouble(double)

.

**Functional Interface:** This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### double applyAsDouble​(double operand)

Applies this operator to the given operand.

**Parameters:**
- operand

- the operand

**Returns:**
- the operator result

---

#### default
DoubleUnaryOperator
compose​(
DoubleUnaryOperator
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
- andThen(DoubleUnaryOperator)

---

#### default
DoubleUnaryOperator
andThen​(
DoubleUnaryOperator
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
- compose(DoubleUnaryOperator)

---

#### static
DoubleUnaryOperator
identity()

Returns a unary operator that always returns its input argument.

**Returns:**
- a unary operator that always returns its input argument

---

### Additional Sections

#### Interface DoubleUnaryOperator

**Functional Interface:** This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

```java
@FunctionalInterface

public interface
DoubleUnaryOperator
```

Represents an operation on a single

double

-valued operand that produces
a

double

-valued result. This is the primitive type specialization of

UnaryOperator

for

double

.

This is a

functional interface

whose functional method is

applyAsDouble(double)

.

**Since:** 1.8
**See Also:** UnaryOperator

@FunctionalInterface

public interface

DoubleUnaryOperator

Represents an operation on a single

double

-valued operand that produces
a

double

-valued result. This is the primitive type specialization of

UnaryOperator

for

double

.

This is a

functional interface

whose functional method is

applyAsDouble(double)

.

This is a

functional interface

whose functional method is

applyAsDouble(double)

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

DoubleUnaryOperator

andThen

​(

DoubleUnaryOperator

after)

Returns a composed operator that first applies this operator to
its input, and then applies the

after

operator to the result.

double

applyAsDouble

​(double operand)

Applies this operator to the given operand.

default

DoubleUnaryOperator

compose

​(

DoubleUnaryOperator

before)

Returns a composed operator that first applies the

before

operator to its input, and then applies this operator to the result.

static

DoubleUnaryOperator

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

DoubleUnaryOperator

andThen

​(

DoubleUnaryOperator

after)

Returns a composed operator that first applies this operator to
its input, and then applies the

after

operator to the result.

double

applyAsDouble

​(double operand)

Applies this operator to the given operand.

default

DoubleUnaryOperator

compose

​(

DoubleUnaryOperator

before)

Returns a composed operator that first applies the

before

operator to its input, and then applies this operator to the result.

static

DoubleUnaryOperator

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

- applyAsDouble

```java
double applyAsDouble​(double operand)
```

Applies this operator to the given operand.

**Parameters:** operand

- the operand
**Returns:** the operator result

- compose

```java
default
DoubleUnaryOperator
compose​(
DoubleUnaryOperator
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
**See Also:** andThen(DoubleUnaryOperator)

- andThen

```java
default
DoubleUnaryOperator
andThen​(
DoubleUnaryOperator
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
**See Also:** compose(DoubleUnaryOperator)

- identity

```java
static
DoubleUnaryOperator
identity()
```

Returns a unary operator that always returns its input argument.

**Returns:** a unary operator that always returns its input argument

Method Detail

- applyAsDouble

```java
double applyAsDouble​(double operand)
```

Applies this operator to the given operand.

**Parameters:** operand

- the operand
**Returns:** the operator result

- compose

```java
default
DoubleUnaryOperator
compose​(
DoubleUnaryOperator
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
**See Also:** andThen(DoubleUnaryOperator)

- andThen

```java
default
DoubleUnaryOperator
andThen​(
DoubleUnaryOperator
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
**See Also:** compose(DoubleUnaryOperator)

- identity

```java
static
DoubleUnaryOperator
identity()
```

Returns a unary operator that always returns its input argument.

**Returns:** a unary operator that always returns its input argument

---

#### Method Detail

applyAsDouble

```java
double applyAsDouble​(double operand)
```

Applies this operator to the given operand.

**Parameters:** operand

- the operand
**Returns:** the operator result

---

#### applyAsDouble

double applyAsDouble​(double operand)

Applies this operator to the given operand.

compose

```java
default
DoubleUnaryOperator
compose​(
DoubleUnaryOperator
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
**See Also:** andThen(DoubleUnaryOperator)

---

#### compose

default

DoubleUnaryOperator

compose​(

DoubleUnaryOperator

before)

Returns a composed operator that first applies the

before

operator to its input, and then applies this operator to the result.
If evaluation of either operator throws an exception, it is relayed to
the caller of the composed operator.

andThen

```java
default
DoubleUnaryOperator
andThen​(
DoubleUnaryOperator
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
**See Also:** compose(DoubleUnaryOperator)

---

#### andThen

default

DoubleUnaryOperator

andThen​(

DoubleUnaryOperator

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
DoubleUnaryOperator
identity()
```

Returns a unary operator that always returns its input argument.

**Returns:** a unary operator that always returns its input argument

---

#### identity

static

DoubleUnaryOperator

identity()

Returns a unary operator that always returns its input argument.

---

