# Interface IntConsumer

**Source:** `java.base\java\util\function\IntConsumer.html`

### Class Description

```java
@FunctionalInterface

public interface
IntConsumer
```

Represents an operation that accepts a single

int

-valued argument and
returns no result. This is the primitive type specialization of

Consumer

for

int

. Unlike most other functional interfaces,

IntConsumer

is expected to operate via side-effects.

This is a

functional interface

whose functional method is

accept(int)

.

**All Known Subinterfaces:** IntStream.Builder

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void accept​(int value)

Performs this operation on the given argument.

**Parameters:**
- value

- the input argument

---

#### default
IntConsumer
andThen​(
IntConsumer
after)

Returns a composed

IntConsumer

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

IntConsumer

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

#### Interface IntConsumer

**All Known Subinterfaces:** IntStream.Builder

**All Known Implementing Classes:** IntSummaryStatistics

,

LongSummaryStatistics

**Functional Interface:** This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

```java
@FunctionalInterface

public interface
IntConsumer
```

Represents an operation that accepts a single

int

-valued argument and
returns no result. This is the primitive type specialization of

Consumer

for

int

. Unlike most other functional interfaces,

IntConsumer

is expected to operate via side-effects.

This is a

functional interface

whose functional method is

accept(int)

.

**Since:** 1.8
**See Also:** Consumer

@FunctionalInterface

public interface

IntConsumer

Represents an operation that accepts a single

int

-valued argument and
returns no result. This is the primitive type specialization of

Consumer

for

int

. Unlike most other functional interfaces,

IntConsumer

is expected to operate via side-effects.

This is a

functional interface

whose functional method is

accept(int)

.

This is a

functional interface

whose functional method is

accept(int)

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

​(int value)

Performs this operation on the given argument.

default

IntConsumer

andThen

​(

IntConsumer

after)

Returns a composed

IntConsumer

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

​(int value)

Performs this operation on the given argument.

default

IntConsumer

andThen

​(

IntConsumer

after)

Returns a composed

IntConsumer

that performs, in sequence, this
operation followed by the

after

operation.

---

#### Method Summary

Performs this operation on the given argument.

Returns a composed

IntConsumer

that performs, in sequence, this
operation followed by the

after

operation.

============ METHOD DETAIL ==========

- Method Detail

- accept

```java
void accept​(int value)
```

Performs this operation on the given argument.

**Parameters:** value

- the input argument

- andThen

```java
default
IntConsumer
andThen​(
IntConsumer
after)
```

Returns a composed

IntConsumer

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

IntConsumer

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
void accept​(int value)
```

Performs this operation on the given argument.

**Parameters:** value

- the input argument

- andThen

```java
default
IntConsumer
andThen​(
IntConsumer
after)
```

Returns a composed

IntConsumer

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

IntConsumer

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
void accept​(int value)
```

Performs this operation on the given argument.

**Parameters:** value

- the input argument

---

#### accept

void accept​(int value)

Performs this operation on the given argument.

andThen

```java
default
IntConsumer
andThen​(
IntConsumer
after)
```

Returns a composed

IntConsumer

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

IntConsumer

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

IntConsumer

andThen​(

IntConsumer

after)

Returns a composed

IntConsumer

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

