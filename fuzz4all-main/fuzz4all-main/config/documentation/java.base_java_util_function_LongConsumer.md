# Interface LongConsumer

**Source:** `java.base\java\util\function\LongConsumer.html`

### Class Description

```java
@FunctionalInterface

public interface
LongConsumer
```

Represents an operation that accepts a single

long

-valued argument and
returns no result. This is the primitive type specialization of

Consumer

for

long

. Unlike most other functional interfaces,

LongConsumer

is expected to operate via side-effects.

This is a

functional interface

whose functional method is

accept(long)

.

**All Known Subinterfaces:** LongStream.Builder

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void accept​(long value)

Performs this operation on the given argument.

**Parameters:**
- value

- the input argument

---

#### default
LongConsumer
andThen​(
LongConsumer
after)

Returns a composed

LongConsumer

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

LongConsumer

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

#### Interface LongConsumer

**All Known Subinterfaces:** LongStream.Builder

**All Known Implementing Classes:** LongSummaryStatistics

**Functional Interface:** This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

```java
@FunctionalInterface

public interface
LongConsumer
```

Represents an operation that accepts a single

long

-valued argument and
returns no result. This is the primitive type specialization of

Consumer

for

long

. Unlike most other functional interfaces,

LongConsumer

is expected to operate via side-effects.

This is a

functional interface

whose functional method is

accept(long)

.

**Since:** 1.8
**See Also:** Consumer

@FunctionalInterface

public interface

LongConsumer

Represents an operation that accepts a single

long

-valued argument and
returns no result. This is the primitive type specialization of

Consumer

for

long

. Unlike most other functional interfaces,

LongConsumer

is expected to operate via side-effects.

This is a

functional interface

whose functional method is

accept(long)

.

This is a

functional interface

whose functional method is

accept(long)

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

​(long value)

Performs this operation on the given argument.

default

LongConsumer

andThen

​(

LongConsumer

after)

Returns a composed

LongConsumer

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

​(long value)

Performs this operation on the given argument.

default

LongConsumer

andThen

​(

LongConsumer

after)

Returns a composed

LongConsumer

that performs, in sequence, this
operation followed by the

after

operation.

---

#### Method Summary

Performs this operation on the given argument.

Returns a composed

LongConsumer

that performs, in sequence, this
operation followed by the

after

operation.

============ METHOD DETAIL ==========

- Method Detail

- accept

```java
void accept​(long value)
```

Performs this operation on the given argument.

**Parameters:** value

- the input argument

- andThen

```java
default
LongConsumer
andThen​(
LongConsumer
after)
```

Returns a composed

LongConsumer

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

LongConsumer

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
void accept​(long value)
```

Performs this operation on the given argument.

**Parameters:** value

- the input argument

- andThen

```java
default
LongConsumer
andThen​(
LongConsumer
after)
```

Returns a composed

LongConsumer

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

LongConsumer

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
void accept​(long value)
```

Performs this operation on the given argument.

**Parameters:** value

- the input argument

---

#### accept

void accept​(long value)

Performs this operation on the given argument.

andThen

```java
default
LongConsumer
andThen​(
LongConsumer
after)
```

Returns a composed

LongConsumer

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

LongConsumer

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

LongConsumer

andThen​(

LongConsumer

after)

Returns a composed

LongConsumer

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

