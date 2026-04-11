# Interface DoubleConsumer

**Source:** `java.base\java\util\function\DoubleConsumer.html`

### Class Description

```java
@FunctionalInterface

public interface
DoubleConsumer
```

Represents an operation that accepts a single

double

-valued argument and
returns no result. This is the primitive type specialization of

Consumer

for

double

. Unlike most other functional interfaces,

DoubleConsumer

is expected to operate via side-effects.

This is a

functional interface

whose functional method is

accept(double)

.

**All Known Subinterfaces:** DoubleStream.Builder

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void accept​(double value)

Performs this operation on the given argument.

**Parameters:**
- value

- the input argument

---

#### default
DoubleConsumer
andThen​(
DoubleConsumer
after)

Returns a composed

DoubleConsumer

that performs, in sequence, this
operation followed by the

after

operation. If performing either
operation throws an exception, it is relayed to the caller of the
composed operation. If performing this operation throws an exception,
the

after

operation will not be performed.

**Parameters:**
- after

- the operation to perform after this operation

**Returns:**
- a composed

DoubleConsumer

that performs in sequence this
operation followed by the

after

operation

**Throws:**
- NullPointerException

- if

after

is null

---

### Additional Sections

#### Interface DoubleConsumer

**All Known Subinterfaces:** DoubleStream.Builder

**All Known Implementing Classes:** DoubleSummaryStatistics

**Functional Interface:** This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

```java
@FunctionalInterface

public interface
DoubleConsumer
```

Represents an operation that accepts a single

double

-valued argument and
returns no result. This is the primitive type specialization of

Consumer

for

double

. Unlike most other functional interfaces,

DoubleConsumer

is expected to operate via side-effects.

This is a

functional interface

whose functional method is

accept(double)

.

**Since:** 1.8
**See Also:** Consumer

@FunctionalInterface

public interface

DoubleConsumer

Represents an operation that accepts a single

double

-valued argument and
returns no result. This is the primitive type specialization of

Consumer

for

double

. Unlike most other functional interfaces,

DoubleConsumer

is expected to operate via side-effects.

This is a

functional interface

whose functional method is

accept(double)

.

This is a

functional interface

whose functional method is

accept(double)

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

void

accept

​(double value)

Performs this operation on the given argument.

default

DoubleConsumer

andThen

​(

DoubleConsumer

after)

Returns a composed

DoubleConsumer

that performs, in sequence, this
operation followed by the

after

operation.

Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

void

accept

​(double value)

Performs this operation on the given argument.

default

DoubleConsumer

andThen

​(

DoubleConsumer

after)

Returns a composed

DoubleConsumer

that performs, in sequence, this
operation followed by the

after

operation.

---

#### Method Summary

Performs this operation on the given argument.

Returns a composed

DoubleConsumer

that performs, in sequence, this
operation followed by the

after

operation.

============ METHOD DETAIL ==========

- Method Detail

- accept

```java
void accept​(double value)
```

Performs this operation on the given argument.

**Parameters:** value

- the input argument

- andThen

```java
default
DoubleConsumer
andThen​(
DoubleConsumer
after)
```

Returns a composed

DoubleConsumer

that performs, in sequence, this
operation followed by the

after

operation. If performing either
operation throws an exception, it is relayed to the caller of the
composed operation. If performing this operation throws an exception,
the

after

operation will not be performed.

**Parameters:** after

- the operation to perform after this operation
**Returns:** a composed

DoubleConsumer

that performs in sequence this
operation followed by the

after

operation
**Throws:** NullPointerException

- if

after

is null

Method Detail

- accept

```java
void accept​(double value)
```

Performs this operation on the given argument.

**Parameters:** value

- the input argument

- andThen

```java
default
DoubleConsumer
andThen​(
DoubleConsumer
after)
```

Returns a composed

DoubleConsumer

that performs, in sequence, this
operation followed by the

after

operation. If performing either
operation throws an exception, it is relayed to the caller of the
composed operation. If performing this operation throws an exception,
the

after

operation will not be performed.

**Parameters:** after

- the operation to perform after this operation
**Returns:** a composed

DoubleConsumer

that performs in sequence this
operation followed by the

after

operation
**Throws:** NullPointerException

- if

after

is null

---

#### Method Detail

accept

```java
void accept​(double value)
```

Performs this operation on the given argument.

**Parameters:** value

- the input argument

---

#### accept

void accept​(double value)

Performs this operation on the given argument.

andThen

```java
default
DoubleConsumer
andThen​(
DoubleConsumer
after)
```

Returns a composed

DoubleConsumer

that performs, in sequence, this
operation followed by the

after

operation. If performing either
operation throws an exception, it is relayed to the caller of the
composed operation. If performing this operation throws an exception,
the

after

operation will not be performed.

**Parameters:** after

- the operation to perform after this operation
**Returns:** a composed

DoubleConsumer

that performs in sequence this
operation followed by the

after

operation
**Throws:** NullPointerException

- if

after

is null

---

#### andThen

default

DoubleConsumer

andThen​(

DoubleConsumer

after)

Returns a composed

DoubleConsumer

that performs, in sequence, this
operation followed by the

after

operation. If performing either
operation throws an exception, it is relayed to the caller of the
composed operation. If performing this operation throws an exception,
the

after

operation will not be performed.

---

