# Interface Iterator<E>

**Source:** `java.base\java\util\Iterator.html`

### Class Description

```java
public interface
Iterator<E>
```

An iterator over a collection.

Iterator

takes the place of

Enumeration

in the Java Collections Framework. Iterators
differ from enumerations in two ways:

- Iterators allow the caller to remove elements from the
underlying collection during the iteration with well-defined
semantics.

Method names have been improved.

This interface is a member of the

Java Collections Framework

.

**Type Parameters:** E

- the type of elements returned by this iterator

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean hasNext()

Returns

true

if the iteration has more elements.
(In other words, returns

true

if

next()

would
return an element rather than throwing an exception.)

**Returns:**
- true

if the iteration has more elements

---

#### E
next()

Returns the next element in the iteration.

**Returns:**
- the next element in the iteration

**Throws:**
- NoSuchElementException

- if the iteration has no more elements

---

#### default void remove()

Removes from the underlying collection the last element returned
by this iterator (optional operation). This method can be called
only once per call to

next()

.

The behavior of an iterator is unspecified if the underlying collection
is modified while the iteration is in progress in any way other than by
calling this method, unless an overriding class has specified a
concurrent modification policy.

The behavior of an iterator is unspecified if this method is called
after a call to the

forEachRemaining

method.

**Throws:**
- UnsupportedOperationException

- if the

remove

operation is not supported by this iterator
- IllegalStateException

- if the

next

method has not
yet been called, or the

remove

method has already
been called after the last call to the

next

method

**Implementation Requirements:**
- The default implementation throws an instance of

UnsupportedOperationException

and performs no other action.

---

#### default void forEachRemaining​(
Consumer
<? super
E
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

**Parameters:**
- action

- The action to be performed for each element

**Throws:**
- NullPointerException

- if the specified action is null

**Since:**
- 1.8

**Implementation Requirements:**
- The default implementation behaves as if:

```java
while (hasNext())
action.accept(next());
```

---

### Additional Sections

#### Interface Iterator<E>

**Type Parameters:** E

- the type of elements returned by this iterator

**All Known Subinterfaces:** EventIterator

,

ListIterator

<E>

,

PrimitiveIterator

<T,​T_CONS>

,

PrimitiveIterator.OfDouble

,

PrimitiveIterator.OfInt

,

PrimitiveIterator.OfLong

,

XMLEventReader

**All Known Implementing Classes:** BeanContextSupport.BCSIterator

,

EventReaderDelegate

,

Scanner

```java
public interface
Iterator<E>
```

An iterator over a collection.

Iterator

takes the place of

Enumeration

in the Java Collections Framework. Iterators
differ from enumerations in two ways:

- Iterators allow the caller to remove elements from the
underlying collection during the iteration with well-defined
semantics.

Method names have been improved.

This interface is a member of the

Java Collections Framework

.

**API Note:** An

Enumeration

can be converted into an

Iterator

by
using the

Enumeration.asIterator()

method.
**Since:** 1.2
**See Also:** Collection

,

ListIterator

,

Iterable

public interface

Iterator<E>

An iterator over a collection.

Iterator

takes the place of

Enumeration

in the Java Collections Framework. Iterators
differ from enumerations in two ways:

- Iterators allow the caller to remove elements from the
underlying collection during the iteration with well-defined
semantics.

Method names have been improved.

This interface is a member of the

Java Collections Framework

.

Iterators allow the caller to remove elements from the
underlying collection during the iteration with well-defined
semantics.

Method names have been improved.

This interface is a member of the

Java Collections Framework

.

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

E

> action)

Performs the given action for each remaining element until all elements
have been processed or the action throws an exception.

boolean

hasNext

()

Returns

true

if the iteration has more elements.

E

next

()

Returns the next element in the iteration.

default void

remove

()

Removes from the underlying collection the last element returned
by this iterator (optional operation).

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

E

> action)

Performs the given action for each remaining element until all elements
have been processed or the action throws an exception.

boolean

hasNext

()

Returns

true

if the iteration has more elements.

E

next

()

Returns the next element in the iteration.

default void

remove

()

Removes from the underlying collection the last element returned
by this iterator (optional operation).

---

#### Method Summary

Performs the given action for each remaining element until all elements
have been processed or the action throws an exception.

Returns

true

if the iteration has more elements.

Returns the next element in the iteration.

Removes from the underlying collection the last element returned
by this iterator (optional operation).

============ METHOD DETAIL ==========

- Method Detail

- hasNext

```java
boolean hasNext()
```

Returns

true

if the iteration has more elements.
(In other words, returns

true

if

next()

would
return an element rather than throwing an exception.)

**Returns:** true

if the iteration has more elements

- next

```java
E
next()
```

Returns the next element in the iteration.

**Returns:** the next element in the iteration
**Throws:** NoSuchElementException

- if the iteration has no more elements

- remove

```java
default void remove()
```

Removes from the underlying collection the last element returned
by this iterator (optional operation). This method can be called
only once per call to

next()

.

The behavior of an iterator is unspecified if the underlying collection
is modified while the iteration is in progress in any way other than by
calling this method, unless an overriding class has specified a
concurrent modification policy.

The behavior of an iterator is unspecified if this method is called
after a call to the

forEachRemaining

method.

**Implementation Requirements:** The default implementation throws an instance of

UnsupportedOperationException

and performs no other action.
**Throws:** UnsupportedOperationException

- if the

remove

operation is not supported by this iterator
**Throws:** IllegalStateException

- if the

next

method has not
yet been called, or the

remove

method has already
been called after the last call to the

next

method

- forEachRemaining

```java
default void forEachRemaining​(
Consumer
<? super
E
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

**Implementation Requirements:** The default implementation behaves as if:

```java
while (hasNext())
action.accept(next());
```
**Parameters:** action

- The action to be performed for each element
**Throws:** NullPointerException

- if the specified action is null
**Since:** 1.8

Method Detail

- hasNext

```java
boolean hasNext()
```

Returns

true

if the iteration has more elements.
(In other words, returns

true

if

next()

would
return an element rather than throwing an exception.)

**Returns:** true

if the iteration has more elements

- next

```java
E
next()
```

Returns the next element in the iteration.

**Returns:** the next element in the iteration
**Throws:** NoSuchElementException

- if the iteration has no more elements

- remove

```java
default void remove()
```

Removes from the underlying collection the last element returned
by this iterator (optional operation). This method can be called
only once per call to

next()

.

The behavior of an iterator is unspecified if the underlying collection
is modified while the iteration is in progress in any way other than by
calling this method, unless an overriding class has specified a
concurrent modification policy.

The behavior of an iterator is unspecified if this method is called
after a call to the

forEachRemaining

method.

**Implementation Requirements:** The default implementation throws an instance of

UnsupportedOperationException

and performs no other action.
**Throws:** UnsupportedOperationException

- if the

remove

operation is not supported by this iterator
**Throws:** IllegalStateException

- if the

next

method has not
yet been called, or the

remove

method has already
been called after the last call to the

next

method

- forEachRemaining

```java
default void forEachRemaining​(
Consumer
<? super
E
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

**Implementation Requirements:** The default implementation behaves as if:

```java
while (hasNext())
action.accept(next());
```
**Parameters:** action

- The action to be performed for each element
**Throws:** NullPointerException

- if the specified action is null
**Since:** 1.8

---

#### Method Detail

hasNext

```java
boolean hasNext()
```

Returns

true

if the iteration has more elements.
(In other words, returns

true

if

next()

would
return an element rather than throwing an exception.)

**Returns:** true

if the iteration has more elements

---

#### hasNext

boolean hasNext()

Returns

true

if the iteration has more elements.
(In other words, returns

true

if

next()

would
return an element rather than throwing an exception.)

next

```java
E
next()
```

Returns the next element in the iteration.

**Returns:** the next element in the iteration
**Throws:** NoSuchElementException

- if the iteration has no more elements

---

#### next

E

next()

Returns the next element in the iteration.

remove

```java
default void remove()
```

Removes from the underlying collection the last element returned
by this iterator (optional operation). This method can be called
only once per call to

next()

.

The behavior of an iterator is unspecified if the underlying collection
is modified while the iteration is in progress in any way other than by
calling this method, unless an overriding class has specified a
concurrent modification policy.

The behavior of an iterator is unspecified if this method is called
after a call to the

forEachRemaining

method.

**Implementation Requirements:** The default implementation throws an instance of

UnsupportedOperationException

and performs no other action.
**Throws:** UnsupportedOperationException

- if the

remove

operation is not supported by this iterator
**Throws:** IllegalStateException

- if the

next

method has not
yet been called, or the

remove

method has already
been called after the last call to the

next

method

---

#### remove

default void remove()

Removes from the underlying collection the last element returned
by this iterator (optional operation). This method can be called
only once per call to

next()

.

The behavior of an iterator is unspecified if the underlying collection
is modified while the iteration is in progress in any way other than by
calling this method, unless an overriding class has specified a
concurrent modification policy.

The behavior of an iterator is unspecified if this method is called
after a call to the

forEachRemaining

method.

The behavior of an iterator is unspecified if the underlying collection
is modified while the iteration is in progress in any way other than by
calling this method, unless an overriding class has specified a
concurrent modification policy.

The behavior of an iterator is unspecified if this method is called
after a call to the

forEachRemaining

method.

The behavior of an iterator is unspecified if this method is called
after a call to the

forEachRemaining

method.

forEachRemaining

```java
default void forEachRemaining​(
Consumer
<? super
E
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

**Implementation Requirements:** The default implementation behaves as if:

```java
while (hasNext())
action.accept(next());
```
**Parameters:** action

- The action to be performed for each element
**Throws:** NullPointerException

- if the specified action is null
**Since:** 1.8

---

#### forEachRemaining

default void forEachRemaining​(

Consumer

<? super

E

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

The default implementation behaves as if:

```java
while (hasNext())
action.accept(next());
```

while (hasNext())
action.accept(next());

---

