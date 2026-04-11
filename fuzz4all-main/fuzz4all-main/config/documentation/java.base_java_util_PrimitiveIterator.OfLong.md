# Interface PrimitiveIterator.OfLong

**Source:** `java.base\java\util\PrimitiveIterator.OfLong.html`

### Class Description

```java
public static interface
PrimitiveIterator.OfLong

extends
PrimitiveIterator
<
Long
,​
LongConsumer
>
```

An Iterator specialized for

long

values.

**All Superinterfaces:** Iterator

<

Long

>

,

PrimitiveIterator

<

Long

,​

LongConsumer

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### long nextLong()

Returns the next

long

element in the iteration.

**Returns:**
- the next

long

element in the iteration

**Throws:**
- NoSuchElementException

- if the iteration has no more elements

---

#### default void forEachRemaining​(
LongConsumer
action)

Performs the given action for each remaining element until all elements
have been processed or the action throws an exception. Actions are
performed in the order of iteration, if that order is specified.
Exceptions thrown by the action are relayed to the caller.

**Specified by:**
- forEachRemaining

in interface

PrimitiveIterator

<

Long

,​

LongConsumer

>

**Parameters:**
- action

- The action to be performed for each element

**Throws:**
- NullPointerException

- if the specified action is null

**Implementation Requirements:**
- The default implementation behaves as if:

```java
while (hasNext())
action.accept(nextLong());
```

---

#### default
Long
next()

Returns the next element in the iteration.

**Specified by:**
- next

in interface

Iterator

<

Long

>

**Returns:**
- the next element in the iteration

**Implementation Requirements:**
- The default implementation boxes the result of calling

nextLong()

, and returns that boxed result.

---

#### default void forEachRemaining​(
Consumer
<? super
Long
> action)

Performs the given action for each remaining element until all elements
have been processed or the action throws an exception. Actions are
performed in the order of iteration, if that order is specified.
Exceptions thrown by the action are relayed to the caller.

The behavior of an iterator is unspecified if the action modifies the
collection in any way (even by calling the

remove

method
or other mutator methods of

Iterator

subtypes),
unless an overriding class has specified a concurrent modification policy.

Subsequent behavior of an iterator is unspecified if the action throws an
exception.

**Specified by:**
- forEachRemaining

in interface

Iterator

<

Long

>

**Parameters:**
- action

- The action to be performed for each element

**Implementation Requirements:**
- If the action is an instance of

LongConsumer

then it is cast
to

LongConsumer

and passed to

forEachRemaining(java.util.function.LongConsumer)

;
otherwise the action is adapted to an instance of

LongConsumer

, by boxing the argument of

LongConsumer

,
and then passed to

forEachRemaining(java.util.function.LongConsumer)

.

---

### Additional Sections

#### Interface PrimitiveIterator.OfLong

**All Superinterfaces:** Iterator

<

Long

>

,

PrimitiveIterator

<

Long

,​

LongConsumer

>

**Enclosing interface:** PrimitiveIterator

<

T

,​

T_CONS

>

```java
public static interface
PrimitiveIterator.OfLong

extends
PrimitiveIterator
<
Long
,​
LongConsumer
>
```

An Iterator specialized for

long

values.

**Since:** 1.8

public static interface

PrimitiveIterator.OfLong

extends

PrimitiveIterator

<

Long

,​

LongConsumer

>

An Iterator specialized for

long

values.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in interface java.util.

PrimitiveIterator

PrimitiveIterator.OfDouble

,

PrimitiveIterator.OfInt

,

PrimitiveIterator.OfLong

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

Consumer

<? super

Long

> action)

Performs the given action for each remaining element until all elements
have been processed or the action throws an exception.

default void

forEachRemaining

​(

LongConsumer

action)

Performs the given action for each remaining element until all elements
have been processed or the action throws an exception.

default

Long

next

()

Returns the next element in the iteration.

long

nextLong

()

Returns the next

long

element in the iteration.

- Methods declared in interface java.util.

Iterator

hasNext

,

remove

Nested Class Summary

- Nested classes/interfaces declared in interface java.util.

PrimitiveIterator

PrimitiveIterator.OfDouble

,

PrimitiveIterator.OfInt

,

PrimitiveIterator.OfLong

---

#### Nested Class Summary

Nested classes/interfaces declared in interface java.util.

PrimitiveIterator

PrimitiveIterator.OfDouble

,

PrimitiveIterator.OfInt

,

PrimitiveIterator.OfLong

---

#### Nested classes/interfaces declared in interface java.util. PrimitiveIterator

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

Consumer

<? super

Long

> action)

Performs the given action for each remaining element until all elements
have been processed or the action throws an exception.

default void

forEachRemaining

​(

LongConsumer

action)

Performs the given action for each remaining element until all elements
have been processed or the action throws an exception.

default

Long

next

()

Returns the next element in the iteration.

long

nextLong

()

Returns the next

long

element in the iteration.

- Methods declared in interface java.util.

Iterator

hasNext

,

remove

---

#### Method Summary

Performs the given action for each remaining element until all elements
have been processed or the action throws an exception.

Returns the next element in the iteration.

Returns the next

long

element in the iteration.

Methods declared in interface java.util.

Iterator

hasNext

,

remove

---

#### Methods declared in interface java.util. Iterator

============ METHOD DETAIL ==========

- Method Detail

- nextLong

```java
long nextLong()
```

Returns the next

long

element in the iteration.

**Returns:** the next

long

element in the iteration
**Throws:** NoSuchElementException

- if the iteration has no more elements

- forEachRemaining

```java
default void forEachRemaining​(
LongConsumer
action)
```

Performs the given action for each remaining element until all elements
have been processed or the action throws an exception. Actions are
performed in the order of iteration, if that order is specified.
Exceptions thrown by the action are relayed to the caller.

**Specified by:** forEachRemaining

in interface

PrimitiveIterator

<

Long

,​

LongConsumer

>
**Implementation Requirements:** The default implementation behaves as if:

```java
while (hasNext())
action.accept(nextLong());
```
**Parameters:** action

- The action to be performed for each element
**Throws:** NullPointerException

- if the specified action is null

- next

```java
default
Long
next()
```

Returns the next element in the iteration.

**Specified by:** next

in interface

Iterator

<

Long

>
**Implementation Requirements:** The default implementation boxes the result of calling

nextLong()

, and returns that boxed result.
**Returns:** the next element in the iteration

- forEachRemaining

```java
default void forEachRemaining​(
Consumer
<? super
Long
> action)
```

Performs the given action for each remaining element until all elements
have been processed or the action throws an exception. Actions are
performed in the order of iteration, if that order is specified.
Exceptions thrown by the action are relayed to the caller.

The behavior of an iterator is unspecified if the action modifies the
collection in any way (even by calling the

remove

method
or other mutator methods of

Iterator

subtypes),
unless an overriding class has specified a concurrent modification policy.

Subsequent behavior of an iterator is unspecified if the action throws an
exception.

**Specified by:** forEachRemaining

in interface

Iterator

<

Long

>
**Implementation Requirements:** If the action is an instance of

LongConsumer

then it is cast
to

LongConsumer

and passed to

forEachRemaining(java.util.function.LongConsumer)

;
otherwise the action is adapted to an instance of

LongConsumer

, by boxing the argument of

LongConsumer

,
and then passed to

forEachRemaining(java.util.function.LongConsumer)

.
**Parameters:** action

- The action to be performed for each element

Method Detail

- nextLong

```java
long nextLong()
```

Returns the next

long

element in the iteration.

**Returns:** the next

long

element in the iteration
**Throws:** NoSuchElementException

- if the iteration has no more elements

- forEachRemaining

```java
default void forEachRemaining​(
LongConsumer
action)
```

Performs the given action for each remaining element until all elements
have been processed or the action throws an exception. Actions are
performed in the order of iteration, if that order is specified.
Exceptions thrown by the action are relayed to the caller.

**Specified by:** forEachRemaining

in interface

PrimitiveIterator

<

Long

,​

LongConsumer

>
**Implementation Requirements:** The default implementation behaves as if:

```java
while (hasNext())
action.accept(nextLong());
```
**Parameters:** action

- The action to be performed for each element
**Throws:** NullPointerException

- if the specified action is null

- next

```java
default
Long
next()
```

Returns the next element in the iteration.

**Specified by:** next

in interface

Iterator

<

Long

>
**Implementation Requirements:** The default implementation boxes the result of calling

nextLong()

, and returns that boxed result.
**Returns:** the next element in the iteration

- forEachRemaining

```java
default void forEachRemaining​(
Consumer
<? super
Long
> action)
```

Performs the given action for each remaining element until all elements
have been processed or the action throws an exception. Actions are
performed in the order of iteration, if that order is specified.
Exceptions thrown by the action are relayed to the caller.

The behavior of an iterator is unspecified if the action modifies the
collection in any way (even by calling the

remove

method
or other mutator methods of

Iterator

subtypes),
unless an overriding class has specified a concurrent modification policy.

Subsequent behavior of an iterator is unspecified if the action throws an
exception.

**Specified by:** forEachRemaining

in interface

Iterator

<

Long

>
**Implementation Requirements:** If the action is an instance of

LongConsumer

then it is cast
to

LongConsumer

and passed to

forEachRemaining(java.util.function.LongConsumer)

;
otherwise the action is adapted to an instance of

LongConsumer

, by boxing the argument of

LongConsumer

,
and then passed to

forEachRemaining(java.util.function.LongConsumer)

.
**Parameters:** action

- The action to be performed for each element

---

#### Method Detail

nextLong

```java
long nextLong()
```

Returns the next

long

element in the iteration.

**Returns:** the next

long

element in the iteration
**Throws:** NoSuchElementException

- if the iteration has no more elements

---

#### nextLong

long nextLong()

Returns the next

long

element in the iteration.

forEachRemaining

```java
default void forEachRemaining​(
LongConsumer
action)
```

Performs the given action for each remaining element until all elements
have been processed or the action throws an exception. Actions are
performed in the order of iteration, if that order is specified.
Exceptions thrown by the action are relayed to the caller.

**Specified by:** forEachRemaining

in interface

PrimitiveIterator

<

Long

,​

LongConsumer

>
**Implementation Requirements:** The default implementation behaves as if:

```java
while (hasNext())
action.accept(nextLong());
```
**Parameters:** action

- The action to be performed for each element
**Throws:** NullPointerException

- if the specified action is null

---

#### forEachRemaining

default void forEachRemaining​(

LongConsumer

action)

Performs the given action for each remaining element until all elements
have been processed or the action throws an exception. Actions are
performed in the order of iteration, if that order is specified.
Exceptions thrown by the action are relayed to the caller.

The default implementation behaves as if:

```java
while (hasNext())
action.accept(nextLong());
```

while (hasNext())
action.accept(nextLong());

next

```java
default
Long
next()
```

Returns the next element in the iteration.

**Specified by:** next

in interface

Iterator

<

Long

>
**Implementation Requirements:** The default implementation boxes the result of calling

nextLong()

, and returns that boxed result.
**Returns:** the next element in the iteration

---

#### next

default

Long

next()

Returns the next element in the iteration.

forEachRemaining

```java
default void forEachRemaining​(
Consumer
<? super
Long
> action)
```

Performs the given action for each remaining element until all elements
have been processed or the action throws an exception. Actions are
performed in the order of iteration, if that order is specified.
Exceptions thrown by the action are relayed to the caller.

The behavior of an iterator is unspecified if the action modifies the
collection in any way (even by calling the

remove

method
or other mutator methods of

Iterator

subtypes),
unless an overriding class has specified a concurrent modification policy.

Subsequent behavior of an iterator is unspecified if the action throws an
exception.

**Specified by:** forEachRemaining

in interface

Iterator

<

Long

>
**Implementation Requirements:** If the action is an instance of

LongConsumer

then it is cast
to

LongConsumer

and passed to

forEachRemaining(java.util.function.LongConsumer)

;
otherwise the action is adapted to an instance of

LongConsumer

, by boxing the argument of

LongConsumer

,
and then passed to

forEachRemaining(java.util.function.LongConsumer)

.
**Parameters:** action

- The action to be performed for each element

---

#### forEachRemaining

default void forEachRemaining​(

Consumer

<? super

Long

> action)

Performs the given action for each remaining element until all elements
have been processed or the action throws an exception. Actions are
performed in the order of iteration, if that order is specified.
Exceptions thrown by the action are relayed to the caller.

The behavior of an iterator is unspecified if the action modifies the
collection in any way (even by calling the

remove

method
or other mutator methods of

Iterator

subtypes),
unless an overriding class has specified a concurrent modification policy.

Subsequent behavior of an iterator is unspecified if the action throws an
exception.

The behavior of an iterator is unspecified if the action modifies the
collection in any way (even by calling the

remove

method
or other mutator methods of

Iterator

subtypes),
unless an overriding class has specified a concurrent modification policy.

Subsequent behavior of an iterator is unspecified if the action throws an
exception.

Subsequent behavior of an iterator is unspecified if the action throws an
exception.

---

