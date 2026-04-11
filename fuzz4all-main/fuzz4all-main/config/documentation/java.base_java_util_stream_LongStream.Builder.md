# Interface LongStream.Builder

**Source:** `java.base\java\util\stream\LongStream.Builder.html`

### Class Description

```java
public static interface
LongStream.Builder

extends
LongConsumer
```

A mutable builder for a

LongStream

.

A stream builder has a lifecycle, which starts in a building
phase, during which elements can be added, and then transitions to a built
phase, after which elements may not be added. The built phase begins
begins when the

build()

method is called, which creates an
ordered stream whose elements are the elements that were added to the
stream builder, in the order they were added.

**All Superinterfaces:** LongConsumer

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void accept​(long t)

Adds an element to the stream being built.

**Specified by:**
- accept

in interface

LongConsumer

**Parameters:**
- t

- the input argument

**Throws:**
- IllegalStateException

- if the builder has already transitioned
to the built state

---

#### default
LongStream.Builder
add​(long t)

Adds an element to the stream being built.

**Parameters:**
- t

- the element to add

**Returns:**
- this

builder

**Throws:**
- IllegalStateException

- if the builder has already transitioned
to the built state

**Implementation Requirements:**
- The default implementation behaves as if:

```java
accept(t)
return this;
```

---

#### LongStream
build()

Builds the stream, transitioning this builder to the built state.
An

IllegalStateException

is thrown if there are further
attempts to operate on the builder after it has entered the built
state.

**Returns:**
- the built stream

**Throws:**
- IllegalStateException

- if the builder has already transitioned
to the built state

---

### Additional Sections

#### Interface LongStream.Builder

**All Superinterfaces:** LongConsumer

**Enclosing interface:** LongStream

```java
public static interface
LongStream.Builder

extends
LongConsumer
```

A mutable builder for a

LongStream

.

A stream builder has a lifecycle, which starts in a building
phase, during which elements can be added, and then transitions to a built
phase, after which elements may not be added. The built phase begins
begins when the

build()

method is called, which creates an
ordered stream whose elements are the elements that were added to the
stream builder, in the order they were added.

**Since:** 1.8
**See Also:** LongStream.builder()

public static interface

LongStream.Builder

extends

LongConsumer

A mutable builder for a

LongStream

.

A stream builder has a lifecycle, which starts in a building
phase, during which elements can be added, and then transitions to a built
phase, after which elements may not be added. The built phase begins
begins when the

build()

method is called, which creates an
ordered stream whose elements are the elements that were added to the
stream builder, in the order they were added.

A stream builder has a lifecycle, which starts in a building
phase, during which elements can be added, and then transitions to a built
phase, after which elements may not be added. The built phase begins
begins when the

build()

method is called, which creates an
ordered stream whose elements are the elements that were added to the
stream builder, in the order they were added.

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

​(long t)

Adds an element to the stream being built.

default

LongStream.Builder

add

​(long t)

Adds an element to the stream being built.

LongStream

build

()

Builds the stream, transitioning this builder to the built state.

- Methods declared in interface java.util.function.

LongConsumer

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

​(long t)

Adds an element to the stream being built.

default

LongStream.Builder

add

​(long t)

Adds an element to the stream being built.

LongStream

build

()

Builds the stream, transitioning this builder to the built state.

- Methods declared in interface java.util.function.

LongConsumer

andThen

---

#### Method Summary

Adds an element to the stream being built.

Builds the stream, transitioning this builder to the built state.

Methods declared in interface java.util.function.

LongConsumer

andThen

---

#### Methods declared in interface java.util.function. LongConsumer

============ METHOD DETAIL ==========

- Method Detail

- accept

```java
void accept​(long t)
```

Adds an element to the stream being built.

**Specified by:** accept

in interface

LongConsumer
**Parameters:** t

- the input argument
**Throws:** IllegalStateException

- if the builder has already transitioned
to the built state

- add

```java
default
LongStream.Builder
add​(long t)
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

- if the builder has already transitioned
to the built state

- build

```java
LongStream
build()
```

Builds the stream, transitioning this builder to the built state.
An

IllegalStateException

is thrown if there are further
attempts to operate on the builder after it has entered the built
state.

**Returns:** the built stream
**Throws:** IllegalStateException

- if the builder has already transitioned
to the built state

Method Detail

- accept

```java
void accept​(long t)
```

Adds an element to the stream being built.

**Specified by:** accept

in interface

LongConsumer
**Parameters:** t

- the input argument
**Throws:** IllegalStateException

- if the builder has already transitioned
to the built state

- add

```java
default
LongStream.Builder
add​(long t)
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

- if the builder has already transitioned
to the built state

- build

```java
LongStream
build()
```

Builds the stream, transitioning this builder to the built state.
An

IllegalStateException

is thrown if there are further
attempts to operate on the builder after it has entered the built
state.

**Returns:** the built stream
**Throws:** IllegalStateException

- if the builder has already transitioned
to the built state

---

#### Method Detail

accept

```java
void accept​(long t)
```

Adds an element to the stream being built.

**Specified by:** accept

in interface

LongConsumer
**Parameters:** t

- the input argument
**Throws:** IllegalStateException

- if the builder has already transitioned
to the built state

---

#### accept

void accept​(long t)

Adds an element to the stream being built.

add

```java
default
LongStream.Builder
add​(long t)
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

- if the builder has already transitioned
to the built state

---

#### add

default

LongStream.Builder

add​(long t)

Adds an element to the stream being built.

accept(t)
return this;

build

```java
LongStream
build()
```

Builds the stream, transitioning this builder to the built state.
An

IllegalStateException

is thrown if there are further
attempts to operate on the builder after it has entered the built
state.

**Returns:** the built stream
**Throws:** IllegalStateException

- if the builder has already transitioned
to the built state

---

#### build

LongStream

build()

Builds the stream, transitioning this builder to the built state.
An

IllegalStateException

is thrown if there are further
attempts to operate on the builder after it has entered the built
state.

---

