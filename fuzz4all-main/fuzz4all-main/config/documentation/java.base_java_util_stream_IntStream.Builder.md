# Interface IntStream.Builder

**Source:** `java.base\java\util\stream\IntStream.Builder.html`

### Class Description

```java
public static interface
IntStream.Builder

extends
IntConsumer
```

A mutable builder for an

IntStream

.

A stream builder has a lifecycle, which starts in a building
phase, during which elements can be added, and then transitions to a built
phase, after which elements may not be added. The built phase
begins when the

build()

method is called, which creates an
ordered stream whose elements are the elements that were added to the
stream builder, in the order they were added.

**All Superinterfaces:** IntConsumer

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void accept​(int t)

Adds an element to the stream being built.

**Specified by:**
- accept

in interface

IntConsumer

**Parameters:**
- t

- the input argument

**Throws:**
- IllegalStateException

- if the builder has already transitioned
to the built state

---

#### default
IntStream.Builder
add​(int t)

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

#### IntStream
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

- if the builder has already transitioned to
the built state

---

### Additional Sections

#### Interface IntStream.Builder

**All Superinterfaces:** IntConsumer

**Enclosing interface:** IntStream

```java
public static interface
IntStream.Builder

extends
IntConsumer
```

A mutable builder for an

IntStream

.

A stream builder has a lifecycle, which starts in a building
phase, during which elements can be added, and then transitions to a built
phase, after which elements may not be added. The built phase
begins when the

build()

method is called, which creates an
ordered stream whose elements are the elements that were added to the
stream builder, in the order they were added.

**Since:** 1.8
**See Also:** IntStream.builder()

public static interface

IntStream.Builder

extends

IntConsumer

A mutable builder for an

IntStream

.

A stream builder has a lifecycle, which starts in a building
phase, during which elements can be added, and then transitions to a built
phase, after which elements may not be added. The built phase
begins when the

build()

method is called, which creates an
ordered stream whose elements are the elements that were added to the
stream builder, in the order they were added.

A stream builder has a lifecycle, which starts in a building
phase, during which elements can be added, and then transitions to a built
phase, after which elements may not be added. The built phase
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

​(int t)

Adds an element to the stream being built.

default

IntStream.Builder

add

​(int t)

Adds an element to the stream being built.

IntStream

build

()

Builds the stream, transitioning this builder to the built state.

- Methods declared in interface java.util.function.

IntConsumer

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

​(int t)

Adds an element to the stream being built.

default

IntStream.Builder

add

​(int t)

Adds an element to the stream being built.

IntStream

build

()

Builds the stream, transitioning this builder to the built state.

- Methods declared in interface java.util.function.

IntConsumer

andThen

---

#### Method Summary

Adds an element to the stream being built.

Builds the stream, transitioning this builder to the built state.

Methods declared in interface java.util.function.

IntConsumer

andThen

---

#### Methods declared in interface java.util.function. IntConsumer

============ METHOD DETAIL ==========

- Method Detail

- accept

```java
void accept​(int t)
```

Adds an element to the stream being built.

**Specified by:** accept

in interface

IntConsumer
**Parameters:** t

- the input argument
**Throws:** IllegalStateException

- if the builder has already transitioned
to the built state

- add

```java
default
IntStream.Builder
add​(int t)
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
IntStream
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

- if the builder has already transitioned to
the built state

Method Detail

- accept

```java
void accept​(int t)
```

Adds an element to the stream being built.

**Specified by:** accept

in interface

IntConsumer
**Parameters:** t

- the input argument
**Throws:** IllegalStateException

- if the builder has already transitioned
to the built state

- add

```java
default
IntStream.Builder
add​(int t)
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
IntStream
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

- if the builder has already transitioned to
the built state

---

#### Method Detail

accept

```java
void accept​(int t)
```

Adds an element to the stream being built.

**Specified by:** accept

in interface

IntConsumer
**Parameters:** t

- the input argument
**Throws:** IllegalStateException

- if the builder has already transitioned
to the built state

---

#### accept

void accept​(int t)

Adds an element to the stream being built.

add

```java
default
IntStream.Builder
add​(int t)
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

IntStream.Builder

add​(int t)

Adds an element to the stream being built.

accept(t)
return this;

build

```java
IntStream
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

- if the builder has already transitioned to
the built state

---

#### build

IntStream

build()

Builds the stream, transitioning this builder to the built state.
An

IllegalStateException

is thrown if there are further
attempts to operate on the builder after it has entered the built
state.

---

