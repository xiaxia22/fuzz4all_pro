# Interface PrimitiveIterator<T,​T_CONS>

**Source:** `java.base\java\util\PrimitiveIterator.html`

### Class Description

```java
public interface
PrimitiveIterator<T,​T_CONS>

extends
Iterator
<T>
```

A base type for primitive specializations of

Iterator

. Specialized
subtypes are provided for

int

,

long

, and

double

values.

The specialized subtype default implementations of

Iterator.next()

and

Iterator.forEachRemaining(java.util.function.Consumer)

box
primitive values to instances of their corresponding wrapper class. Such
boxing may offset any advantages gained when using the primitive
specializations. To avoid boxing, the corresponding primitive-based methods
should be used. For example,

PrimitiveIterator.OfInt.nextInt()

and

PrimitiveIterator.OfInt.forEachRemaining(java.util.function.IntConsumer)

should be used in preference to

PrimitiveIterator.OfInt.next()

and

PrimitiveIterator.OfInt.forEachRemaining(java.util.function.Consumer)

.

Iteration of primitive values using boxing-based methods

next()

and

forEachRemaining()

,
does not affect the order in which the values, transformed to boxed values,
are encountered.

**Type Parameters:** T

- the type of elements returned by this PrimitiveIterator. The
type must be a wrapper type for a primitive type, such as

Integer

for the primitive

int

type.
**Type Parameters:** T_CONS

- the type of primitive consumer. The type must be a
primitive specialization of

Consumer

for

T

, such as

IntConsumer

for

Integer

.

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void forEachRemaining​(
T_CONS
action)

Performs the given action for each remaining element, in the order
elements occur when iterating, until all elements have been processed
or the action throws an exception. Errors or runtime exceptions
thrown by the action are relayed to the caller.

**Parameters:**
- action

- The action to be performed for each element

**Throws:**
- NullPointerException

- if the specified action is null

---

### Additional Sections

#### Interface PrimitiveIterator<T,​T_CONS>

**Type Parameters:** T

- the type of elements returned by this PrimitiveIterator. The
type must be a wrapper type for a primitive type, such as

Integer

for the primitive

int

type.
**Type Parameters:** T_CONS

- the type of primitive consumer. The type must be a
primitive specialization of

Consumer

for

T

, such as

IntConsumer

for

Integer

.

**All Superinterfaces:** Iterator

<T>

**All Known Subinterfaces:** PrimitiveIterator.OfDouble

,

PrimitiveIterator.OfInt

,

PrimitiveIterator.OfLong

```java
public interface
PrimitiveIterator<T,​T_CONS>

extends
Iterator
<T>
```

A base type for primitive specializations of

Iterator

. Specialized
subtypes are provided for

int

,

long

, and

double

values.

The specialized subtype default implementations of

Iterator.next()

and

Iterator.forEachRemaining(java.util.function.Consumer)

box
primitive values to instances of their corresponding wrapper class. Such
boxing may offset any advantages gained when using the primitive
specializations. To avoid boxing, the corresponding primitive-based methods
should be used. For example,

PrimitiveIterator.OfInt.nextInt()

and

PrimitiveIterator.OfInt.forEachRemaining(java.util.function.IntConsumer)

should be used in preference to

PrimitiveIterator.OfInt.next()

and

PrimitiveIterator.OfInt.forEachRemaining(java.util.function.Consumer)

.

Iteration of primitive values using boxing-based methods

next()

and

forEachRemaining()

,
does not affect the order in which the values, transformed to boxed values,
are encountered.

**Implementation Note:** If the boolean system property

org.openjdk.java.util.stream.tripwire

is set to

true

then diagnostic warnings are reported if boxing of
primitive values occur when operating on primitive subtype specializations.
**Since:** 1.8

public interface

PrimitiveIterator<T,​T_CONS>

extends

Iterator

<T>

A base type for primitive specializations of

Iterator

. Specialized
subtypes are provided for

int

,

long

, and

double

values.

The specialized subtype default implementations of

Iterator.next()

and

Iterator.forEachRemaining(java.util.function.Consumer)

box
primitive values to instances of their corresponding wrapper class. Such
boxing may offset any advantages gained when using the primitive
specializations. To avoid boxing, the corresponding primitive-based methods
should be used. For example,

PrimitiveIterator.OfInt.nextInt()

and

PrimitiveIterator.OfInt.forEachRemaining(java.util.function.IntConsumer)

should be used in preference to

PrimitiveIterator.OfInt.next()

and

PrimitiveIterator.OfInt.forEachRemaining(java.util.function.Consumer)

.

Iteration of primitive values using boxing-based methods

next()

and

forEachRemaining()

,
does not affect the order in which the values, transformed to boxed values,
are encountered.

The specialized subtype default implementations of

Iterator.next()

and

Iterator.forEachRemaining(java.util.function.Consumer)

box
primitive values to instances of their corresponding wrapper class. Such
boxing may offset any advantages gained when using the primitive
specializations. To avoid boxing, the corresponding primitive-based methods
should be used. For example,

PrimitiveIterator.OfInt.nextInt()

and

PrimitiveIterator.OfInt.forEachRemaining(java.util.function.IntConsumer)

should be used in preference to

PrimitiveIterator.OfInt.next()

and

PrimitiveIterator.OfInt.forEachRemaining(java.util.function.Consumer)

.

Iteration of primitive values using boxing-based methods

next()

and

forEachRemaining()

,
does not affect the order in which the values, transformed to boxed values,
are encountered.

Iteration of primitive values using boxing-based methods

next()

and

forEachRemaining()

,
does not affect the order in which the values, transformed to boxed values,
are encountered.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static interface

PrimitiveIterator.OfDouble

An Iterator specialized for

double

values.

static interface

PrimitiveIterator.OfInt

An Iterator specialized for

int

values.

static interface

PrimitiveIterator.OfLong

An Iterator specialized for

long

values.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

forEachRemaining

​(

T_CONS

action)

Performs the given action for each remaining element, in the order
elements occur when iterating, until all elements have been processed
or the action throws an exception.

- Methods declared in interface java.util.

Iterator

forEachRemaining

,

hasNext

,

next

,

remove

Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static interface

PrimitiveIterator.OfDouble

An Iterator specialized for

double

values.

static interface

PrimitiveIterator.OfInt

An Iterator specialized for

int

values.

static interface

PrimitiveIterator.OfLong

An Iterator specialized for

long

values.

---

#### Nested Class Summary

An Iterator specialized for

double

values.

An Iterator specialized for

int

values.

An Iterator specialized for

long

values.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

forEachRemaining

​(

T_CONS

action)

Performs the given action for each remaining element, in the order
elements occur when iterating, until all elements have been processed
or the action throws an exception.

- Methods declared in interface java.util.

Iterator

forEachRemaining

,

hasNext

,

next

,

remove

---

#### Method Summary

Performs the given action for each remaining element, in the order
elements occur when iterating, until all elements have been processed
or the action throws an exception.

Methods declared in interface java.util.

Iterator

forEachRemaining

,

hasNext

,

next

,

remove

---

#### Methods declared in interface java.util. Iterator

============ METHOD DETAIL ==========

- Method Detail

- forEachRemaining

```java
void forEachRemaining​(
T_CONS
action)
```

Performs the given action for each remaining element, in the order
elements occur when iterating, until all elements have been processed
or the action throws an exception. Errors or runtime exceptions
thrown by the action are relayed to the caller.

**Parameters:** action

- The action to be performed for each element
**Throws:** NullPointerException

- if the specified action is null

Method Detail

- forEachRemaining

```java
void forEachRemaining​(
T_CONS
action)
```

Performs the given action for each remaining element, in the order
elements occur when iterating, until all elements have been processed
or the action throws an exception. Errors or runtime exceptions
thrown by the action are relayed to the caller.

**Parameters:** action

- The action to be performed for each element
**Throws:** NullPointerException

- if the specified action is null

---

#### Method Detail

forEachRemaining

```java
void forEachRemaining​(
T_CONS
action)
```

Performs the given action for each remaining element, in the order
elements occur when iterating, until all elements have been processed
or the action throws an exception. Errors or runtime exceptions
thrown by the action are relayed to the caller.

**Parameters:** action

- The action to be performed for each element
**Throws:** NullPointerException

- if the specified action is null

---

#### forEachRemaining

void forEachRemaining​(

T_CONS

action)

Performs the given action for each remaining element, in the order
elements occur when iterating, until all elements have been processed
or the action throws an exception. Errors or runtime exceptions
thrown by the action are relayed to the caller.

---

