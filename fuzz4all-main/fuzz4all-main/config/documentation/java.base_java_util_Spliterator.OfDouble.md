# Interface Spliterator.OfDouble

**Source:** `java.base\java\util\Spliterator.OfDouble.html`

### Class Description

```java
public static interface
Spliterator.OfDouble

extends
Spliterator.OfPrimitive
<
Double
,​
DoubleConsumer
,​
Spliterator.OfDouble
>
```

A Spliterator specialized for

double

values.

**All Superinterfaces:** Spliterator

<

Double

>

,

Spliterator.OfPrimitive

<

Double

,​

DoubleConsumer

,​

Spliterator.OfDouble

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### default boolean tryAdvance​(
Consumer
<? super
Double
> action)

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

**Specified by:**
- tryAdvance

in interface

Spliterator

<

Double

>

**Parameters:**
- action

- The action

**Returns:**
- false

if no remaining elements existed
upon entry to this method, else

true

.

**Implementation Requirements:**
- If the action is an instance of

DoubleConsumer

then it is
cast to

DoubleConsumer

and passed to

Spliterator.OfPrimitive.tryAdvance(java.util.function.DoubleConsumer)

; otherwise
the action is adapted to an instance of

DoubleConsumer

, by
boxing the argument of

DoubleConsumer

, and then passed to

Spliterator.OfPrimitive.tryAdvance(java.util.function.DoubleConsumer)

.

---

#### default void forEachRemaining​(
Consumer
<? super
Double
> action)

Performs the given action for each remaining element, sequentially in
the current thread, until all elements have been processed or the action
throws an exception. If this Spliterator is

Spliterator.ORDERED

, actions
are performed in encounter order. Exceptions thrown by the action
are relayed to the caller.

**Specified by:**
- forEachRemaining

in interface

Spliterator

<

Double

>

**Parameters:**
- action

- The action

**Implementation Requirements:**
- If the action is an instance of

DoubleConsumer

then it is
cast to

DoubleConsumer

and passed to

Spliterator.OfPrimitive.forEachRemaining(java.util.function.DoubleConsumer)

;
otherwise the action is adapted to an instance of

DoubleConsumer

, by boxing the argument of

DoubleConsumer

, and then passed to

Spliterator.OfPrimitive.forEachRemaining(java.util.function.DoubleConsumer)

.

---

### Additional Sections

#### Interface Spliterator.OfDouble

**All Superinterfaces:** Spliterator

<

Double

>

,

Spliterator.OfPrimitive

<

Double

,​

DoubleConsumer

,​

Spliterator.OfDouble

>

**All Known Implementing Classes:** Spliterators.AbstractDoubleSpliterator

**Enclosing interface:** Spliterator

<

T

>

```java
public static interface
Spliterator.OfDouble

extends
Spliterator.OfPrimitive
<
Double
,​
DoubleConsumer
,​
Spliterator.OfDouble
>
```

A Spliterator specialized for

double

values.

**Since:** 1.8

public static interface

Spliterator.OfDouble

extends

Spliterator.OfPrimitive

<

Double

,​

DoubleConsumer

,​

Spliterator.OfDouble

>

A Spliterator specialized for

double

values.

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

Default Methods

Modifier and Type

Method

Description

default void

forEachRemaining

​(

Consumer

<? super

Double

> action)

Performs the given action for each remaining element, sequentially in
the current thread, until all elements have been processed or the action
throws an exception.

default boolean

tryAdvance

​(

Consumer

<? super

Double

> action)

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

getComparator

,

getExactSizeIfKnown

,

hasCharacteristics

,

trySplit

- Methods declared in interface java.util.

Spliterator.OfPrimitive

forEachRemaining

,

tryAdvance

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

Default Methods

Modifier and Type

Method

Description

default void

forEachRemaining

​(

Consumer

<? super

Double

> action)

Performs the given action for each remaining element, sequentially in
the current thread, until all elements have been processed or the action
throws an exception.

default boolean

tryAdvance

​(

Consumer

<? super

Double

> action)

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

getComparator

,

getExactSizeIfKnown

,

hasCharacteristics

,

trySplit

- Methods declared in interface java.util.

Spliterator.OfPrimitive

forEachRemaining

,

tryAdvance

---

#### Method Summary

Performs the given action for each remaining element, sequentially in
the current thread, until all elements have been processed or the action
throws an exception.

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

getComparator

,

getExactSizeIfKnown

,

hasCharacteristics

,

trySplit

---

#### Methods declared in interface java.util. Spliterator

Methods declared in interface java.util.

Spliterator.OfPrimitive

forEachRemaining

,

tryAdvance

---

#### Methods declared in interface java.util. Spliterator.OfPrimitive

============ METHOD DETAIL ==========

- Method Detail

- tryAdvance

```java
default boolean tryAdvance​(
Consumer
<? super
Double
> action)
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

**Specified by:** tryAdvance

in interface

Spliterator

<

Double

>
**Implementation Requirements:** If the action is an instance of

DoubleConsumer

then it is
cast to

DoubleConsumer

and passed to

Spliterator.OfPrimitive.tryAdvance(java.util.function.DoubleConsumer)

; otherwise
the action is adapted to an instance of

DoubleConsumer

, by
boxing the argument of

DoubleConsumer

, and then passed to

Spliterator.OfPrimitive.tryAdvance(java.util.function.DoubleConsumer)

.
**Parameters:** action

- The action
**Returns:** false

if no remaining elements existed
upon entry to this method, else

true

.

- forEachRemaining

```java
default void forEachRemaining​(
Consumer
<? super
Double
> action)
```

Performs the given action for each remaining element, sequentially in
the current thread, until all elements have been processed or the action
throws an exception. If this Spliterator is

Spliterator.ORDERED

, actions
are performed in encounter order. Exceptions thrown by the action
are relayed to the caller.

**Specified by:** forEachRemaining

in interface

Spliterator

<

Double

>
**Implementation Requirements:** If the action is an instance of

DoubleConsumer

then it is
cast to

DoubleConsumer

and passed to

Spliterator.OfPrimitive.forEachRemaining(java.util.function.DoubleConsumer)

;
otherwise the action is adapted to an instance of

DoubleConsumer

, by boxing the argument of

DoubleConsumer

, and then passed to

Spliterator.OfPrimitive.forEachRemaining(java.util.function.DoubleConsumer)

.
**Parameters:** action

- The action

Method Detail

- tryAdvance

```java
default boolean tryAdvance​(
Consumer
<? super
Double
> action)
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

**Specified by:** tryAdvance

in interface

Spliterator

<

Double

>
**Implementation Requirements:** If the action is an instance of

DoubleConsumer

then it is
cast to

DoubleConsumer

and passed to

Spliterator.OfPrimitive.tryAdvance(java.util.function.DoubleConsumer)

; otherwise
the action is adapted to an instance of

DoubleConsumer

, by
boxing the argument of

DoubleConsumer

, and then passed to

Spliterator.OfPrimitive.tryAdvance(java.util.function.DoubleConsumer)

.
**Parameters:** action

- The action
**Returns:** false

if no remaining elements existed
upon entry to this method, else

true

.

- forEachRemaining

```java
default void forEachRemaining​(
Consumer
<? super
Double
> action)
```

Performs the given action for each remaining element, sequentially in
the current thread, until all elements have been processed or the action
throws an exception. If this Spliterator is

Spliterator.ORDERED

, actions
are performed in encounter order. Exceptions thrown by the action
are relayed to the caller.

**Specified by:** forEachRemaining

in interface

Spliterator

<

Double

>
**Implementation Requirements:** If the action is an instance of

DoubleConsumer

then it is
cast to

DoubleConsumer

and passed to

Spliterator.OfPrimitive.forEachRemaining(java.util.function.DoubleConsumer)

;
otherwise the action is adapted to an instance of

DoubleConsumer

, by boxing the argument of

DoubleConsumer

, and then passed to

Spliterator.OfPrimitive.forEachRemaining(java.util.function.DoubleConsumer)

.
**Parameters:** action

- The action

---

#### Method Detail

tryAdvance

```java
default boolean tryAdvance​(
Consumer
<? super
Double
> action)
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

**Specified by:** tryAdvance

in interface

Spliterator

<

Double

>
**Implementation Requirements:** If the action is an instance of

DoubleConsumer

then it is
cast to

DoubleConsumer

and passed to

Spliterator.OfPrimitive.tryAdvance(java.util.function.DoubleConsumer)

; otherwise
the action is adapted to an instance of

DoubleConsumer

, by
boxing the argument of

DoubleConsumer

, and then passed to

Spliterator.OfPrimitive.tryAdvance(java.util.function.DoubleConsumer)

.
**Parameters:** action

- The action
**Returns:** false

if no remaining elements existed
upon entry to this method, else

true

.

---

#### tryAdvance

default boolean tryAdvance​(

Consumer

<? super

Double

> action)

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
Consumer
<? super
Double
> action)
```

Performs the given action for each remaining element, sequentially in
the current thread, until all elements have been processed or the action
throws an exception. If this Spliterator is

Spliterator.ORDERED

, actions
are performed in encounter order. Exceptions thrown by the action
are relayed to the caller.

**Specified by:** forEachRemaining

in interface

Spliterator

<

Double

>
**Implementation Requirements:** If the action is an instance of

DoubleConsumer

then it is
cast to

DoubleConsumer

and passed to

Spliterator.OfPrimitive.forEachRemaining(java.util.function.DoubleConsumer)

;
otherwise the action is adapted to an instance of

DoubleConsumer

, by boxing the argument of

DoubleConsumer

, and then passed to

Spliterator.OfPrimitive.forEachRemaining(java.util.function.DoubleConsumer)

.
**Parameters:** action

- The action

---

#### forEachRemaining

default void forEachRemaining​(

Consumer

<? super

Double

> action)

Performs the given action for each remaining element, sequentially in
the current thread, until all elements have been processed or the action
throws an exception. If this Spliterator is

Spliterator.ORDERED

, actions
are performed in encounter order. Exceptions thrown by the action
are relayed to the caller.

---

