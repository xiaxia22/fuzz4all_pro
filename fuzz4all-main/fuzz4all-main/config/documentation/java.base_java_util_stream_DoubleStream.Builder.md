# Interface DoubleStream.Builder

**Source:** `java.base\java\util\stream\DoubleStream.Builder.html`

### Class Description

```java
public static interface
DoubleStream.Builder

extends
DoubleConsumer
```

A mutable builder for a

DoubleStream

.

A stream builder has a lifecycle, which starts in a building
phase, during which elements can be added, and then transitions to a built
phase, after which elements may not be added. The built phase
begins when the

build()

method is called, which creates an
ordered stream whose elements are the elements that were added to the
stream builder, in the order they were added.

**All Superinterfaces:** DoubleConsumer

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void accept​(double t)

Adds an element to the stream being built.

**Specified by:**
- accept

in interface

DoubleConsumer

**Parameters:**
- t

- the input argument

**Throws:**
- IllegalStateException

- if the builder has already transitioned
to the built state

---

#### default
DoubleStream.Builder
add​(double t)

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

#### DoubleStream
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

#### Interface DoubleStream.Builder

**All Superinterfaces:** DoubleConsumer

**Enclosing interface:** DoubleStream

```java
public static interface
DoubleStream.Builder

extends
DoubleConsumer
```

A mutable builder for a

DoubleStream

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
**See Also:** DoubleStream.builder()

public static interface

DoubleStream.Builder

extends

DoubleConsumer

A mutable builder for a

DoubleStream

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

​(double t)

Adds an element to the stream being built.

default

DoubleStream.Builder

add

​(double t)

Adds an element to the stream being built.

DoubleStream

build

()

Builds the stream, transitioning this builder to the built state.

- Methods declared in interface java.util.function.

DoubleConsumer

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

​(double t)

Adds an element to the stream being built.

default

DoubleStream.Builder

add

​(double t)

Adds an element to the stream being built.

DoubleStream

build

()

Builds the stream, transitioning this builder to the built state.

- Methods declared in interface java.util.function.

DoubleConsumer

andThen

---

#### Method Summary

Adds an element to the stream being built.

Builds the stream, transitioning this builder to the built state.

Methods declared in interface java.util.function.

DoubleConsumer

andThen

---

#### Methods declared in interface java.util.function. DoubleConsumer

============ METHOD DETAIL ==========

- Method Detail

- accept

```java
void accept​(double t)
```

Adds an element to the stream being built.

**Specified by:** accept

in interface

DoubleConsumer
**Parameters:** t

- the input argument
**Throws:** IllegalStateException

- if the builder has already transitioned
to the built state

- add

```java
default
DoubleStream.Builder
add​(double t)
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
DoubleStream
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
void accept​(double t)
```

Adds an element to the stream being built.

**Specified by:** accept

in interface

DoubleConsumer
**Parameters:** t

- the input argument
**Throws:** IllegalStateException

- if the builder has already transitioned
to the built state

- add

```java
default
DoubleStream.Builder
add​(double t)
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
DoubleStream
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
void accept​(double t)
```

Adds an element to the stream being built.

**Specified by:** accept

in interface

DoubleConsumer
**Parameters:** t

- the input argument
**Throws:** IllegalStateException

- if the builder has already transitioned
to the built state

---

#### accept

void accept​(double t)

Adds an element to the stream being built.

add

```java
default
DoubleStream.Builder
add​(double t)
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

DoubleStream.Builder

add​(double t)

Adds an element to the stream being built.

accept(t)
return this;

build

```java
DoubleStream
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

DoubleStream

build()

Builds the stream, transitioning this builder to the built state.
An

IllegalStateException

is thrown if there are further
attempts to operate on the builder after it has entered the built
state.

---

