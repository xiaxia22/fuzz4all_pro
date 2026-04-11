# Interface PrimitiveIterator.OfDouble

**Source:** `java.base\java\util\PrimitiveIterator.OfDouble.html`

### Class Description

```java
public static interface
PrimitiveIterator.OfDouble

extends
PrimitiveIterator
<
Double
,​
DoubleConsumer
>
```

An Iterator specialized for

double

values.

**All Superinterfaces:** Iterator

<

Double

>

,

PrimitiveIterator

<

Double

,​

DoubleConsumer

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### double nextDouble()

Returns the next

double

element in the iteration.

**Returns:**
- the next

double

element in the iteration

**Throws:**
- NoSuchElementException

- if the iteration has no more elements

---

#### default void forEachRemaining​(
DoubleConsumer
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

Double

,​

DoubleConsumer

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
action.accept(nextDouble());
```

---

#### default
Double
next()

Returns the next element in the iteration.

**Specified by:**
- next

in interface

Iterator

<

Double

>

**Returns:**
- the next element in the iteration

**Implementation Requirements:**
- The default implementation boxes the result of calling

nextDouble()

, and returns that boxed result.

---

#### default void forEachRemaining​(
Consumer
<? super
Double
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

Double

>

**Parameters:**
- action

- The action to be performed for each element

**Implementation Requirements:**
- If the action is an instance of

DoubleConsumer

then it is
cast to

DoubleConsumer

and passed to

forEachRemaining(java.util.function.DoubleConsumer)

; otherwise the action is adapted to
an instance of

DoubleConsumer

, by boxing the argument of

DoubleConsumer

, and then passed to

forEachRemaining(java.util.function.DoubleConsumer)

.

---

### Additional Sections

#### Interface PrimitiveIterator.OfDouble

**All Superinterfaces:** Iterator

<

Double

>

,

PrimitiveIterator

<

Double

,​

DoubleConsumer

>

**Enclosing interface:** PrimitiveIterator

<

T

,​

T_CONS

>

```java
public static interface
PrimitiveIterator.OfDouble

extends
PrimitiveIterator
<
Double
,​
DoubleConsumer
>
```

An Iterator specialized for

double

values.

**Since:** 1.8

public static interface

PrimitiveIterator.OfDouble

extends

PrimitiveIterator

<

Double

,​

DoubleConsumer

>

An Iterator specialized for

double

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

Double

> action)

Performs the given action for each remaining element until all elements
have been processed or the action throws an exception.

default void

forEachRemaining

​(

DoubleConsumer

action)

Performs the given action for each remaining element until all elements
have been processed or the action throws an exception.

default

Double

next

()

Returns the next element in the iteration.

double

nextDouble

()

Returns the next

double

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

Double

> action)

Performs the given action for each remaining element until all elements
have been processed or the action throws an exception.

default void

forEachRemaining

​(

DoubleConsumer

action)

Performs the given action for each remaining element until all elements
have been processed or the action throws an exception.

default

Double

next

()

Returns the next element in the iteration.

double

nextDouble

()

Returns the next

double

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

double

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

- nextDouble

```java
double nextDouble()
```

Returns the next

double

element in the iteration.

**Returns:** the next

double

element in the iteration
**Throws:** NoSuchElementException

- if the iteration has no more elements

- forEachRemaining

```java
default void forEachRemaining​(
DoubleConsumer
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

Double

,​

DoubleConsumer

>
**Implementation Requirements:** The default implementation behaves as if:

```java
while (hasNext())
action.accept(nextDouble());
```
**Parameters:** action

- The action to be performed for each element
**Throws:** NullPointerException

- if the specified action is null

- next

```java
default
Double
next()
```

Returns the next element in the iteration.

**Specified by:** next

in interface

Iterator

<

Double

>
**Implementation Requirements:** The default implementation boxes the result of calling

nextDouble()

, and returns that boxed result.
**Returns:** the next element in the iteration

- forEachRemaining

```java
default void forEachRemaining​(
Consumer
<? super
Double
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

Double

>
**Implementation Requirements:** If the action is an instance of

DoubleConsumer

then it is
cast to

DoubleConsumer

and passed to

forEachRemaining(java.util.function.DoubleConsumer)

; otherwise the action is adapted to
an instance of

DoubleConsumer

, by boxing the argument of

DoubleConsumer

, and then passed to

forEachRemaining(java.util.function.DoubleConsumer)

.
**Parameters:** action

- The action to be performed for each element

Method Detail

- nextDouble

```java
double nextDouble()
```

Returns the next

double

element in the iteration.

**Returns:** the next

double

element in the iteration
**Throws:** NoSuchElementException

- if the iteration has no more elements

- forEachRemaining

```java
default void forEachRemaining​(
DoubleConsumer
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

Double

,​

DoubleConsumer

>
**Implementation Requirements:** The default implementation behaves as if:

```java
while (hasNext())
action.accept(nextDouble());
```
**Parameters:** action

- The action to be performed for each element
**Throws:** NullPointerException

- if the specified action is null

- next

```java
default
Double
next()
```

Returns the next element in the iteration.

**Specified by:** next

in interface

Iterator

<

Double

>
**Implementation Requirements:** The default implementation boxes the result of calling

nextDouble()

, and returns that boxed result.
**Returns:** the next element in the iteration

- forEachRemaining

```java
default void forEachRemaining​(
Consumer
<? super
Double
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

Double

>
**Implementation Requirements:** If the action is an instance of

DoubleConsumer

then it is
cast to

DoubleConsumer

and passed to

forEachRemaining(java.util.function.DoubleConsumer)

; otherwise the action is adapted to
an instance of

DoubleConsumer

, by boxing the argument of

DoubleConsumer

, and then passed to

forEachRemaining(java.util.function.DoubleConsumer)

.
**Parameters:** action

- The action to be performed for each element

---

#### Method Detail

nextDouble

```java
double nextDouble()
```

Returns the next

double

element in the iteration.

**Returns:** the next

double

element in the iteration
**Throws:** NoSuchElementException

- if the iteration has no more elements

---

#### nextDouble

double nextDouble()

Returns the next

double

element in the iteration.

forEachRemaining

```java
default void forEachRemaining​(
DoubleConsumer
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

Double

,​

DoubleConsumer

>
**Implementation Requirements:** The default implementation behaves as if:

```java
while (hasNext())
action.accept(nextDouble());
```
**Parameters:** action

- The action to be performed for each element
**Throws:** NullPointerException

- if the specified action is null

---

#### forEachRemaining

default void forEachRemaining​(

DoubleConsumer

action)

Performs the given action for each remaining element until all elements
have been processed or the action throws an exception. Actions are
performed in the order of iteration, if that order is specified.
Exceptions thrown by the action are relayed to the caller.

The default implementation behaves as if:

```java
while (hasNext())
action.accept(nextDouble());
```

while (hasNext())
action.accept(nextDouble());

next

```java
default
Double
next()
```

Returns the next element in the iteration.

**Specified by:** next

in interface

Iterator

<

Double

>
**Implementation Requirements:** The default implementation boxes the result of calling

nextDouble()

, and returns that boxed result.
**Returns:** the next element in the iteration

---

#### next

default

Double

next()

Returns the next element in the iteration.

forEachRemaining

```java
default void forEachRemaining​(
Consumer
<? super
Double
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

Double

>
**Implementation Requirements:** If the action is an instance of

DoubleConsumer

then it is
cast to

DoubleConsumer

and passed to

forEachRemaining(java.util.function.DoubleConsumer)

; otherwise the action is adapted to
an instance of

DoubleConsumer

, by boxing the argument of

DoubleConsumer

, and then passed to

forEachRemaining(java.util.function.DoubleConsumer)

.
**Parameters:** action

- The action to be performed for each element

---

#### forEachRemaining

default void forEachRemaining​(

Consumer

<? super

Double

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

