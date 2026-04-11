# Interface Consumer<T>

**Source:** `java.base\java\util\function\Consumer.html`

### Class Description

```java
@FunctionalInterface

public interface
Consumer<T>
```

Represents an operation that accepts a single input argument and returns no
result. Unlike most other functional interfaces,

Consumer

is expected
to operate via side-effects.

This is a

functional interface

whose functional method is

accept(Object)

.

**Type Parameters:** T

- the type of the input to the operation

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void accept​(
T
t)

Performs this operation on the given argument.

**Parameters:**
- t

- the input argument

---

#### default
Consumer
<
T
> andThen​(
Consumer
<? super
T
> after)

Returns a composed

Consumer

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

Consumer

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

#### Interface Consumer<T>

**Type Parameters:** T

- the type of the input to the operation

**All Known Subinterfaces:** Stream.Builder

<T>

**Functional Interface:** This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

```java
@FunctionalInterface

public interface
Consumer<T>
```

Represents an operation that accepts a single input argument and returns no
result. Unlike most other functional interfaces,

Consumer

is expected
to operate via side-effects.

This is a

functional interface

whose functional method is

accept(Object)

.

**Since:** 1.8

@FunctionalInterface

public interface

Consumer<T>

Represents an operation that accepts a single input argument and returns no
result. Unlike most other functional interfaces,

Consumer

is expected
to operate via side-effects.

This is a

functional interface

whose functional method is

accept(Object)

.

This is a

functional interface

whose functional method is

accept(Object)

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

​(

T

t)

Performs this operation on the given argument.

default

Consumer

<

T

>

andThen

​(

Consumer

<? super

T

> after)

Returns a composed

Consumer

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

​(

T

t)

Performs this operation on the given argument.

default

Consumer

<

T

>

andThen

​(

Consumer

<? super

T

> after)

Returns a composed

Consumer

that performs, in sequence, this
operation followed by the

after

operation.

---

#### Method Summary

Performs this operation on the given argument.

Returns a composed

Consumer

that performs, in sequence, this
operation followed by the

after

operation.

============ METHOD DETAIL ==========

- Method Detail

- accept

```java
void accept​(
T
t)
```

Performs this operation on the given argument.

**Parameters:** t

- the input argument

- andThen

```java
default
Consumer
<
T
> andThen​(
Consumer
<? super
T
> after)
```

Returns a composed

Consumer

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

Consumer

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
void accept​(
T
t)
```

Performs this operation on the given argument.

**Parameters:** t

- the input argument

- andThen

```java
default
Consumer
<
T
> andThen​(
Consumer
<? super
T
> after)
```

Returns a composed

Consumer

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

Consumer

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
void accept​(
T
t)
```

Performs this operation on the given argument.

**Parameters:** t

- the input argument

---

#### accept

void accept​(

T

t)

Performs this operation on the given argument.

andThen

```java
default
Consumer
<
T
> andThen​(
Consumer
<? super
T
> after)
```

Returns a composed

Consumer

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

Consumer

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

Consumer

<

T

> andThen​(

Consumer

<? super

T

> after)

Returns a composed

Consumer

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

