# Interface Spliterator.OfPrimitive<T,​T_CONS,​T_SPLITR extends Spliterator.OfPrimitive<T,​T_CONS,​T_SPLITR>>

**Source:** `java.base\java\util\Spliterator.OfPrimitive.html`

### Class Description

```java
public static interface
Spliterator.OfPrimitive<T,​T_CONS,​T_SPLITR extends Spliterator.OfPrimitive<T,​T_CONS,​T_SPLITR>>

extends
Spliterator
<T>
```

A Spliterator specialized for primitive values.

**Type Parameters:** T

- the type of elements returned by this Spliterator. The
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
**Type Parameters:** T_SPLITR

- the type of primitive Spliterator. The type must be
a primitive specialization of Spliterator for

T

, such as

Spliterator.OfInt

for

Integer

.

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean tryAdvance​(
T_CONS
action)

If a remaining element exists, performs the given action on it,
returning

true

; else returns

false

. If this
Spliterator is

Spliterator.ORDERED

the action is performed on the
next element in encounter order. Exceptions thrown by the
action are relayed to the caller.

**Parameters:**
- action

- The action

**Returns:**
- false

if no remaining elements existed
upon entry to this method, else

true

.

**Throws:**
- NullPointerException

- if the specified action is null

---

#### default void forEachRemaining​(
T_CONS
action)

Performs the given action for each remaining element, sequentially in
the current thread, until all elements have been processed or the
action throws an exception. If this Spliterator is

Spliterator.ORDERED

,
actions are performed in encounter order. Exceptions thrown by the
action are relayed to the caller.

**Parameters:**
- action

- The action

**Throws:**
- NullPointerException

- if the specified action is null

**Implementation Requirements:**
- The default implementation repeatedly invokes

tryAdvance(T_CONS)

until it returns

false

. It should be overridden whenever
possible.

---

### Additional Sections

#### Interface Spliterator.OfPrimitive<T,​T_CONS,​T_SPLITR extends Spliterator.OfPrimitive<T,​T_CONS,​T_SPLITR>>

**Type Parameters:** T

- the type of elements returned by this Spliterator. The
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
**Type Parameters:** T_SPLITR

- the type of primitive Spliterator. The type must be
a primitive specialization of Spliterator for

T

, such as

Spliterator.OfInt

for

Integer

.

**All Superinterfaces:** Spliterator

<T>

**All Known Subinterfaces:** Spliterator.OfDouble

,

Spliterator.OfInt

,

Spliterator.OfLong

**All Known Implementing Classes:** Spliterators.AbstractDoubleSpliterator

,

Spliterators.AbstractIntSpliterator

,

Spliterators.AbstractLongSpliterator

**Enclosing interface:** Spliterator

<

T

>

```java
public static interface
Spliterator.OfPrimitive<T,​T_CONS,​T_SPLITR extends Spliterator.OfPrimitive<T,​T_CONS,​T_SPLITR>>

extends
Spliterator
<T>
```

A Spliterator specialized for primitive values.

**Since:** 1.8
**See Also:** Spliterator.OfInt

,

Spliterator.OfLong

,

Spliterator.OfDouble

public static interface

Spliterator.OfPrimitive<T,​T_CONS,​T_SPLITR extends Spliterator.OfPrimitive<T,​T_CONS,​T_SPLITR>>

extends

Spliterator

<T>

A Spliterator specialized for primitive values.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in interface java.util.

Spliterator

Spliterator.OfDouble

,

Spliterator.OfInt

,

Spliterator.OfLong

,

Spliterator.OfPrimitive

<

T

,​

T_CONS

,​

T_SPLITR

extends

Spliterator.OfPrimitive

<

T

,​

T_CONS

,​

T_SPLITR

>>

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in interface java.util.

Spliterator

CONCURRENT

,

DISTINCT

,

IMMUTABLE

,

NONNULL

,

ORDERED

,

SIZED

,

SORTED

,

SUBSIZED

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

default void

forEachRemaining

​(

T_CONS

action)

Performs the given action for each remaining element, sequentially in
the current thread, until all elements have been processed or the
action throws an exception.

boolean

tryAdvance

​(

T_CONS

action)

If a remaining element exists, performs the given action on it,
returning

true

; else returns

false

.

- Methods declared in interface java.util.

Spliterator

characteristics

,

estimateSize

,

forEachRemaining

,

getComparator

,

getExactSizeIfKnown

,

hasCharacteristics

,

tryAdvance

,

trySplit

Nested Class Summary

- Nested classes/interfaces declared in interface java.util.

Spliterator

Spliterator.OfDouble

,

Spliterator.OfInt

,

Spliterator.OfLong

,

Spliterator.OfPrimitive

<

T

,​

T_CONS

,​

T_SPLITR

extends

Spliterator.OfPrimitive

<

T

,​

T_CONS

,​

T_SPLITR

>>

---

#### Nested Class Summary

Nested classes/interfaces declared in interface java.util.

Spliterator

Spliterator.OfDouble

,

Spliterator.OfInt

,

Spliterator.OfLong

,

Spliterator.OfPrimitive

<

T

,​

T_CONS

,​

T_SPLITR

extends

Spliterator.OfPrimitive

<

T

,​

T_CONS

,​

T_SPLITR

>>

---

#### Nested classes/interfaces declared in interface java.util. Spliterator

Field Summary

- Fields declared in interface java.util.

Spliterator

CONCURRENT

,

DISTINCT

,

IMMUTABLE

,

NONNULL

,

ORDERED

,

SIZED

,

SORTED

,

SUBSIZED

---

#### Field Summary

Fields declared in interface java.util.

Spliterator

CONCURRENT

,

DISTINCT

,

IMMUTABLE

,

NONNULL

,

ORDERED

,

SIZED

,

SORTED

,

SUBSIZED

---

#### Fields declared in interface java.util. Spliterator

Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

default void

forEachRemaining

​(

T_CONS

action)

Performs the given action for each remaining element, sequentially in
the current thread, until all elements have been processed or the
action throws an exception.

boolean

tryAdvance

​(

T_CONS

action)

If a remaining element exists, performs the given action on it,
returning

true

; else returns

false

.

- Methods declared in interface java.util.

Spliterator

characteristics

,

estimateSize

,

forEachRemaining

,

getComparator

,

getExactSizeIfKnown

,

hasCharacteristics

,

tryAdvance

,

trySplit

---

#### Method Summary

Performs the given action for each remaining element, sequentially in
the current thread, until all elements have been processed or the
action throws an exception.

If a remaining element exists, performs the given action on it,
returning

true

; else returns

false

.

Methods declared in interface java.util.

Spliterator

characteristics

,

estimateSize

,

forEachRemaining

,

getComparator

,

getExactSizeIfKnown

,

hasCharacteristics

,

tryAdvance

,

trySplit

---

#### Methods declared in interface java.util. Spliterator

============ METHOD DETAIL ==========

- Method Detail

- tryAdvance

```java
boolean tryAdvance​(
T_CONS
action)
```

If a remaining element exists, performs the given action on it,
returning

true

; else returns

false

. If this
Spliterator is

Spliterator.ORDERED

the action is performed on the
next element in encounter order. Exceptions thrown by the
action are relayed to the caller.

**Parameters:** action

- The action
**Returns:** false

if no remaining elements existed
upon entry to this method, else

true

.
**Throws:** NullPointerException

- if the specified action is null

- forEachRemaining

```java
default void forEachRemaining​(
T_CONS
action)
```

Performs the given action for each remaining element, sequentially in
the current thread, until all elements have been processed or the
action throws an exception. If this Spliterator is

Spliterator.ORDERED

,
actions are performed in encounter order. Exceptions thrown by the
action are relayed to the caller.

**Implementation Requirements:** The default implementation repeatedly invokes

tryAdvance(T_CONS)

until it returns

false

. It should be overridden whenever
possible.
**Parameters:** action

- The action
**Throws:** NullPointerException

- if the specified action is null

Method Detail

- tryAdvance

```java
boolean tryAdvance​(
T_CONS
action)
```

If a remaining element exists, performs the given action on it,
returning

true

; else returns

false

. If this
Spliterator is

Spliterator.ORDERED

the action is performed on the
next element in encounter order. Exceptions thrown by the
action are relayed to the caller.

**Parameters:** action

- The action
**Returns:** false

if no remaining elements existed
upon entry to this method, else

true

.
**Throws:** NullPointerException

- if the specified action is null

- forEachRemaining

```java
default void forEachRemaining​(
T_CONS
action)
```

Performs the given action for each remaining element, sequentially in
the current thread, until all elements have been processed or the
action throws an exception. If this Spliterator is

Spliterator.ORDERED

,
actions are performed in encounter order. Exceptions thrown by the
action are relayed to the caller.

**Implementation Requirements:** The default implementation repeatedly invokes

tryAdvance(T_CONS)

until it returns

false

. It should be overridden whenever
possible.
**Parameters:** action

- The action
**Throws:** NullPointerException

- if the specified action is null

---

#### Method Detail

tryAdvance

```java
boolean tryAdvance​(
T_CONS
action)
```

If a remaining element exists, performs the given action on it,
returning

true

; else returns

false

. If this
Spliterator is

Spliterator.ORDERED

the action is performed on the
next element in encounter order. Exceptions thrown by the
action are relayed to the caller.

**Parameters:** action

- The action
**Returns:** false

if no remaining elements existed
upon entry to this method, else

true

.
**Throws:** NullPointerException

- if the specified action is null

---

#### tryAdvance

boolean tryAdvance​(

T_CONS

action)

If a remaining element exists, performs the given action on it,
returning

true

; else returns

false

. If this
Spliterator is

Spliterator.ORDERED

the action is performed on the
next element in encounter order. Exceptions thrown by the
action are relayed to the caller.

forEachRemaining

```java
default void forEachRemaining​(
T_CONS
action)
```

Performs the given action for each remaining element, sequentially in
the current thread, until all elements have been processed or the
action throws an exception. If this Spliterator is

Spliterator.ORDERED

,
actions are performed in encounter order. Exceptions thrown by the
action are relayed to the caller.

**Implementation Requirements:** The default implementation repeatedly invokes

tryAdvance(T_CONS)

until it returns

false

. It should be overridden whenever
possible.
**Parameters:** action

- The action
**Throws:** NullPointerException

- if the specified action is null

---

#### forEachRemaining

default void forEachRemaining​(

T_CONS

action)

Performs the given action for each remaining element, sequentially in
the current thread, until all elements have been processed or the
action throws an exception. If this Spliterator is

Spliterator.ORDERED

,
actions are performed in encounter order. Exceptions thrown by the
action are relayed to the caller.

---

