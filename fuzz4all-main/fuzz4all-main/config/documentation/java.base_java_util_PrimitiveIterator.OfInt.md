# Interface PrimitiveIterator.OfInt

**Source:** `java.base\java\util\PrimitiveIterator.OfInt.html`

### Class Description

```java
public static interface
PrimitiveIterator.OfInt

extends
PrimitiveIterator
<
Integer
,​
IntConsumer
>
```

An Iterator specialized for

int

values.

**All Superinterfaces:** Iterator

<

Integer

>

,

PrimitiveIterator

<

Integer

,​

IntConsumer

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### int nextInt()

Returns the next

int

element in the iteration.

**Returns:**
- the next

int

element in the iteration

**Throws:**
- NoSuchElementException

- if the iteration has no more elements

---

#### default void forEachRemaining​(
IntConsumer
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

Integer

,​

IntConsumer

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
action.accept(nextInt());
```

---

#### default
Integer
next()

Returns the next element in the iteration.

**Specified by:**
- next

in interface

Iterator

<

Integer

>

**Returns:**
- the next element in the iteration

**Implementation Requirements:**
- The default implementation boxes the result of calling

nextInt()

, and returns that boxed result.

---

#### default void forEachRemaining​(
Consumer
<? super
Integer
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

Integer

>

**Parameters:**
- action

- The action to be performed for each element

**Implementation Requirements:**
- If the action is an instance of

IntConsumer

then it is cast
to

IntConsumer

and passed to

forEachRemaining(java.util.function.IntConsumer)

;
otherwise the action is adapted to an instance of

IntConsumer

, by boxing the argument of

IntConsumer

,
and then passed to

forEachRemaining(java.util.function.IntConsumer)

.

---

### Additional Sections

#### Interface PrimitiveIterator.OfInt

**All Superinterfaces:** Iterator

<

Integer

>

,

PrimitiveIterator

<

Integer

,​

IntConsumer

>

**Enclosing interface:** PrimitiveIterator

<

T

,​

T_CONS

>

```java
public static interface
PrimitiveIterator.OfInt

extends
PrimitiveIterator
<
Integer
,​
IntConsumer
>
```

An Iterator specialized for

int

values.

**Since:** 1.8

public static interface

PrimitiveIterator.OfInt

extends

PrimitiveIterator

<

Integer

,​

IntConsumer

>

An Iterator specialized for

int

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

Integer

> action)

Performs the given action for each remaining element until all elements
have been processed or the action throws an exception.

default void

forEachRemaining

​(

IntConsumer

action)

Performs the given action for each remaining element until all elements
have been processed or the action throws an exception.

default

Integer

next

()

Returns the next element in the iteration.

int

nextInt

()

Returns the next

int

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

Integer

> action)

Performs the given action for each remaining element until all elements
have been processed or the action throws an exception.

default void

forEachRemaining

​(

IntConsumer

action)

Performs the given action for each remaining element until all elements
have been processed or the action throws an exception.

default

Integer

next

()

Returns the next element in the iteration.

int

nextInt

()

Returns the next

int

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

int

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

- nextInt

```java
int nextInt()
```

Returns the next

int

element in the iteration.

**Returns:** the next

int

element in the iteration
**Throws:** NoSuchElementException

- if the iteration has no more elements

- forEachRemaining

```java
default void forEachRemaining​(
IntConsumer
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

Integer

,​

IntConsumer

>
**Implementation Requirements:** The default implementation behaves as if:

```java
while (hasNext())
action.accept(nextInt());
```
**Parameters:** action

- The action to be performed for each element
**Throws:** NullPointerException

- if the specified action is null

- next

```java
default
Integer
next()
```

Returns the next element in the iteration.

**Specified by:** next

in interface

Iterator

<

Integer

>
**Implementation Requirements:** The default implementation boxes the result of calling

nextInt()

, and returns that boxed result.
**Returns:** the next element in the iteration

- forEachRemaining

```java
default void forEachRemaining​(
Consumer
<? super
Integer
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

Integer

>
**Implementation Requirements:** If the action is an instance of

IntConsumer

then it is cast
to

IntConsumer

and passed to

forEachRemaining(java.util.function.IntConsumer)

;
otherwise the action is adapted to an instance of

IntConsumer

, by boxing the argument of

IntConsumer

,
and then passed to

forEachRemaining(java.util.function.IntConsumer)

.
**Parameters:** action

- The action to be performed for each element

Method Detail

- nextInt

```java
int nextInt()
```

Returns the next

int

element in the iteration.

**Returns:** the next

int

element in the iteration
**Throws:** NoSuchElementException

- if the iteration has no more elements

- forEachRemaining

```java
default void forEachRemaining​(
IntConsumer
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

Integer

,​

IntConsumer

>
**Implementation Requirements:** The default implementation behaves as if:

```java
while (hasNext())
action.accept(nextInt());
```
**Parameters:** action

- The action to be performed for each element
**Throws:** NullPointerException

- if the specified action is null

- next

```java
default
Integer
next()
```

Returns the next element in the iteration.

**Specified by:** next

in interface

Iterator

<

Integer

>
**Implementation Requirements:** The default implementation boxes the result of calling

nextInt()

, and returns that boxed result.
**Returns:** the next element in the iteration

- forEachRemaining

```java
default void forEachRemaining​(
Consumer
<? super
Integer
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

Integer

>
**Implementation Requirements:** If the action is an instance of

IntConsumer

then it is cast
to

IntConsumer

and passed to

forEachRemaining(java.util.function.IntConsumer)

;
otherwise the action is adapted to an instance of

IntConsumer

, by boxing the argument of

IntConsumer

,
and then passed to

forEachRemaining(java.util.function.IntConsumer)

.
**Parameters:** action

- The action to be performed for each element

---

#### Method Detail

nextInt

```java
int nextInt()
```

Returns the next

int

element in the iteration.

**Returns:** the next

int

element in the iteration
**Throws:** NoSuchElementException

- if the iteration has no more elements

---

#### nextInt

int nextInt()

Returns the next

int

element in the iteration.

forEachRemaining

```java
default void forEachRemaining​(
IntConsumer
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

Integer

,​

IntConsumer

>
**Implementation Requirements:** The default implementation behaves as if:

```java
while (hasNext())
action.accept(nextInt());
```
**Parameters:** action

- The action to be performed for each element
**Throws:** NullPointerException

- if the specified action is null

---

#### forEachRemaining

default void forEachRemaining​(

IntConsumer

action)

Performs the given action for each remaining element until all elements
have been processed or the action throws an exception. Actions are
performed in the order of iteration, if that order is specified.
Exceptions thrown by the action are relayed to the caller.

The default implementation behaves as if:

```java
while (hasNext())
action.accept(nextInt());
```

while (hasNext())
action.accept(nextInt());

next

```java
default
Integer
next()
```

Returns the next element in the iteration.

**Specified by:** next

in interface

Iterator

<

Integer

>
**Implementation Requirements:** The default implementation boxes the result of calling

nextInt()

, and returns that boxed result.
**Returns:** the next element in the iteration

---

#### next

default

Integer

next()

Returns the next element in the iteration.

forEachRemaining

```java
default void forEachRemaining​(
Consumer
<? super
Integer
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

Integer

>
**Implementation Requirements:** If the action is an instance of

IntConsumer

then it is cast
to

IntConsumer

and passed to

forEachRemaining(java.util.function.IntConsumer)

;
otherwise the action is adapted to an instance of

IntConsumer

, by boxing the argument of

IntConsumer

,
and then passed to

forEachRemaining(java.util.function.IntConsumer)

.
**Parameters:** action

- The action to be performed for each element

---

#### forEachRemaining

default void forEachRemaining​(

Consumer

<? super

Integer

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

