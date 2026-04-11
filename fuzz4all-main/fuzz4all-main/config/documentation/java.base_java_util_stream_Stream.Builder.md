# Interface Stream.Builder<T>

**Source:** `java.base\java\util\stream\Stream.Builder.html`

### Class Description

```java
public static interface
Stream.Builder<T>

extends
Consumer
<T>
```

A mutable builder for a

Stream

. This allows the creation of a

Stream

by generating elements individually and adding them to the

Builder

(without the copying overhead that comes from using
an

ArrayList

as a temporary buffer.)

A stream builder has a lifecycle, which starts in a building
phase, during which elements can be added, and then transitions to a built
phase, after which elements may not be added. The built phase begins
when the

build()

method is called, which creates an ordered

Stream

whose elements are the elements that were added to the stream
builder, in the order they were added.

**Type Parameters:** T

- the type of stream elements

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void accept​(
T
t)

Adds an element to the stream being built.

**Specified by:**
- accept

in interface

Consumer

<

T

>

**Parameters:**
- t

- the input argument

**Throws:**
- IllegalStateException

- if the builder has already transitioned to
the built state

---

#### default
Stream.Builder
<
T
> add​(
T
t)

Adds an element to the stream being built.

**Parameters:**
- t

- the element to add

**Returns:**
- this

builder

**Throws:**
- IllegalStateException

- if the builder has already transitioned to
the built state

**Implementation Requirements:**
- The default implementation behaves as if:

```java
accept(t)
return this;
```

---

#### Stream
<
T
> build()

Builds the stream, transitioning this builder to the built state.
An

IllegalStateException

is thrown if there are further attempts
to operate on the builder after it has entered the built state.

**Returns:**
- the built stream

**Throws:**
- IllegalStateException

- if the builder has already transitioned to
the built state

---

### Additional Sections

#### Interface Stream.Builder<T>

**Type Parameters:** T

- the type of stream elements

**All Superinterfaces:** Consumer

<T>

**Enclosing interface:** Stream

<

T

>

```java
public static interface
Stream.Builder<T>

extends
Consumer
<T>
```

A mutable builder for a

Stream

. This allows the creation of a

Stream

by generating elements individually and adding them to the

Builder

(without the copying overhead that comes from using
an

ArrayList

as a temporary buffer.)

A stream builder has a lifecycle, which starts in a building
phase, during which elements can be added, and then transitions to a built
phase, after which elements may not be added. The built phase begins
when the

build()

method is called, which creates an ordered

Stream

whose elements are the elements that were added to the stream
builder, in the order they were added.

**Since:** 1.8
**See Also:** Stream.builder()

public static interface

Stream.Builder<T>

extends

Consumer

<T>

A mutable builder for a

Stream

. This allows the creation of a

Stream

by generating elements individually and adding them to the

Builder

(without the copying overhead that comes from using
an

ArrayList

as a temporary buffer.)

A stream builder has a lifecycle, which starts in a building
phase, during which elements can be added, and then transitions to a built
phase, after which elements may not be added. The built phase begins
when the

build()

method is called, which creates an ordered

Stream

whose elements are the elements that were added to the stream
builder, in the order they were added.

A stream builder has a lifecycle, which starts in a building
phase, during which elements can be added, and then transitions to a built
phase, after which elements may not be added. The built phase begins
when the

build()

method is called, which creates an ordered

Stream

whose elements are the elements that were added to the stream
builder, in the order they were added.

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

Adds an element to the stream being built.

default

Stream.Builder

<

T

>

add

​(

T

t)

Adds an element to the stream being built.

Stream

<

T

>

build

()

Builds the stream, transitioning this builder to the built state.

- Methods declared in interface java.util.function.

Consumer

andThen

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

Adds an element to the stream being built.

default

Stream.Builder

<

T

>

add

​(

T

t)

Adds an element to the stream being built.

Stream

<

T

>

build

()

Builds the stream, transitioning this builder to the built state.

- Methods declared in interface java.util.function.

Consumer

andThen

---

#### Method Summary

Adds an element to the stream being built.

Builds the stream, transitioning this builder to the built state.

Methods declared in interface java.util.function.

Consumer

andThen

---

#### Methods declared in interface java.util.function. Consumer

============ METHOD DETAIL ==========

- Method Detail

- accept

```java
void accept​(
T
t)
```

Adds an element to the stream being built.

**Specified by:** accept

in interface

Consumer

<

T

>
**Parameters:** t

- the input argument
**Throws:** IllegalStateException

- if the builder has already transitioned to
the built state

- add

```java
default
Stream.Builder
<
T
> add​(
T
t)
```

Adds an element to the stream being built.

**Implementation Requirements:** The default implementation behaves as if:

```java
accept(t)
return this;
```
**Parameters:** t

- the element to add
**Returns:** this

builder
**Throws:** IllegalStateException

- if the builder has already transitioned to
the built state

- build

```java
Stream
<
T
> build()
```

Builds the stream, transitioning this builder to the built state.
An

IllegalStateException

is thrown if there are further attempts
to operate on the builder after it has entered the built state.

**Returns:** the built stream
**Throws:** IllegalStateException

- if the builder has already transitioned to
the built state

Method Detail

- accept

```java
void accept​(
T
t)
```

Adds an element to the stream being built.

**Specified by:** accept

in interface

Consumer

<

T

>
**Parameters:** t

- the input argument
**Throws:** IllegalStateException

- if the builder has already transitioned to
the built state

- add

```java
default
Stream.Builder
<
T
> add​(
T
t)
```

Adds an element to the stream being built.

**Implementation Requirements:** The default implementation behaves as if:

```java
accept(t)
return this;
```
**Parameters:** t

- the element to add
**Returns:** this

builder
**Throws:** IllegalStateException

- if the builder has already transitioned to
the built state

- build

```java
Stream
<
T
> build()
```

Builds the stream, transitioning this builder to the built state.
An

IllegalStateException

is thrown if there are further attempts
to operate on the builder after it has entered the built state.

**Returns:** the built stream
**Throws:** IllegalStateException

- if the builder has already transitioned to
the built state

---

#### Method Detail

accept

```java
void accept​(
T
t)
```

Adds an element to the stream being built.

**Specified by:** accept

in interface

Consumer

<

T

>
**Parameters:** t

- the input argument
**Throws:** IllegalStateException

- if the builder has already transitioned to
the built state

---

#### accept

void accept​(

T

t)

Adds an element to the stream being built.

add

```java
default
Stream.Builder
<
T
> add​(
T
t)
```

Adds an element to the stream being built.

**Implementation Requirements:** The default implementation behaves as if:

```java
accept(t)
return this;
```
**Parameters:** t

- the element to add
**Returns:** this

builder
**Throws:** IllegalStateException

- if the builder has already transitioned to
the built state

---

#### add

default

Stream.Builder

<

T

> add​(

T

t)

Adds an element to the stream being built.

accept(t)
return this;

build

```java
Stream
<
T
> build()
```

Builds the stream, transitioning this builder to the built state.
An

IllegalStateException

is thrown if there are further attempts
to operate on the builder after it has entered the built state.

**Returns:** the built stream
**Throws:** IllegalStateException

- if the builder has already transitioned to
the built state

---

#### build

Stream

<

T

> build()

Builds the stream, transitioning this builder to the built state.
An

IllegalStateException

is thrown if there are further attempts
to operate on the builder after it has entered the built state.

---

