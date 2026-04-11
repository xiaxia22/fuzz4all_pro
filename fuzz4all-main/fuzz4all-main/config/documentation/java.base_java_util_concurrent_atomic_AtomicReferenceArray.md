# Class AtomicReferenceArray<E>

**Source:** `java.base\java\util\concurrent\atomic\AtomicReferenceArray.html`

### Class Description

```java
public class
AtomicReferenceArray<E>

extends
Object

implements
Serializable
```

An array of object references in which elements may be updated
atomically. See the

VarHandle

specification for
descriptions of the properties of atomic accesses.

**Type Parameters:** E

- The base class of elements held in this array

---

### Field Details

*No entries found.*

### Constructor Details

#### public AtomicReferenceArray​(int length)

Creates a new AtomicReferenceArray of the given length, with all
elements initially null.

**Parameters:**
- length

- the length of the array

---

#### public AtomicReferenceArray​(
E
[] array)

Creates a new AtomicReferenceArray with the same length as, and
all elements copied from, the given array.

**Parameters:**
- array

- the array to copy elements from

**Throws:**
- NullPointerException

- if array is null

---

### Method Details

#### public final int length()

Returns the length of the array.

**Returns:**
- the length of the array

---

#### public final
E
get​(int i)

Returns the current value of the element at index

i

,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

**Parameters:**
- i

- the index

**Returns:**
- the current value

---

#### public final void set​(int i,

E
newValue)

Sets the element at index

i

to

newValue

,
with memory effects as specified by

VarHandle.setVolatile(java.lang.Object...)

.

**Parameters:**
- i

- the index
- newValue

- the new value

---

#### public final void lazySet​(int i,

E
newValue)

Sets the element at index

i

to

newValue

,
with memory effects as specified by

VarHandle.setRelease(java.lang.Object...)

.

**Parameters:**
- i

- the index
- newValue

- the new value

**Since:**
- 1.6

---

#### public final
E
getAndSet​(int i,

E
newValue)

Atomically sets the element at index

i

to

newValue

and returns the old value,
with memory effects as specified by

VarHandle.getAndSet(java.lang.Object...)

.

**Parameters:**
- i

- the index
- newValue

- the new value

**Returns:**
- the previous value

---

#### public final boolean compareAndSet​(int i,

E
expectedValue,

E
newValue)

Atomically sets the element at index

i

to

newValue

if the element's current value

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

.

**Parameters:**
- i

- the index
- expectedValue

- the expected value
- newValue

- the new value

**Returns:**
- true

if successful. False return indicates that
the actual value was not equal to the expected value.

---

#### @Deprecated
(
since
="9")
public final boolean weakCompareAndSet​(int i,

E
expectedValue,

E
newValue)

Possibly atomically sets the element at index

i

to

newValue

if the element's current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetPlain(java.lang.Object...)

.

**Parameters:**
- i

- the index
- expectedValue

- the expected value
- newValue

- the new value

**Returns:**
- true

if successful

**See Also:**
- weakCompareAndSetPlain(int, E, E)

---

#### public final boolean weakCompareAndSetPlain​(int i,

E
expectedValue,

E
newValue)

Possibly atomically sets the element at index

i

to

newValue

if the element's current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetPlain(java.lang.Object...)

.

**Parameters:**
- i

- the index
- expectedValue

- the expected value
- newValue

- the new value

**Returns:**
- true

if successful

**Since:**
- 9

---

#### public final
E
getAndUpdate​(int i,

UnaryOperator
<
E
> updateFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the element at index

i

with
the results of applying the given function, returning the
previous value. The function should be side-effect-free, since
it may be re-applied when attempted updates fail due to
contention among threads.

**Parameters:**
- i

- the index
- updateFunction

- a side-effect-free function

**Returns:**
- the previous value

**Since:**
- 1.8

---

#### public final
E
updateAndGet​(int i,

UnaryOperator
<
E
> updateFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the element at index

i

with
the results of applying the given function, returning the
updated value. The function should be side-effect-free, since it
may be re-applied when attempted updates fail due to contention
among threads.

**Parameters:**
- i

- the index
- updateFunction

- a side-effect-free function

**Returns:**
- the updated value

**Since:**
- 1.8

---

#### public final
E
getAndAccumulate​(int i,

E
x,

BinaryOperator
<
E
> accumulatorFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the element at index

i

with
the results of applying the given function to the current and
given values, returning the previous value. The function should
be side-effect-free, since it may be re-applied when attempted
updates fail due to contention among threads. The function is
applied with the current value of the element at index

i

as its first argument, and the given update as the second
argument.

**Parameters:**
- i

- the index
- x

- the update value
- accumulatorFunction

- a side-effect-free function of two arguments

**Returns:**
- the previous value

**Since:**
- 1.8

---

#### public final
E
accumulateAndGet​(int i,

E
x,

BinaryOperator
<
E
> accumulatorFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the element at index

i

with
the results of applying the given function to the current and
given values, returning the updated value. The function should
be side-effect-free, since it may be re-applied when attempted
updates fail due to contention among threads. The function is
applied with the current value of the element at index

i

as its first argument, and the given update as the second
argument.

**Parameters:**
- i

- the index
- x

- the update value
- accumulatorFunction

- a side-effect-free function of two arguments

**Returns:**
- the updated value

**Since:**
- 1.8

---

#### public
String
toString()

Returns the String representation of the current values of array.

**Overrides:**
- toString

in class

Object

**Returns:**
- the String representation of the current values of array

---

#### public final
E
getPlain​(int i)

Returns the current value of the element at index

i

,
with memory semantics of reading as if the variable was declared
non-

volatile

.

**Parameters:**
- i

- the index

**Returns:**
- the value

**Since:**
- 9

---

#### public final void setPlain​(int i,

E
newValue)

Sets the element at index

i

to

newValue

,
with memory semantics of setting as if the variable was
declared non-

volatile

and non-

final

.

**Parameters:**
- i

- the index
- newValue

- the new value

**Since:**
- 9

---

#### public final
E
getOpaque​(int i)

Returns the current value of the element at index

i

,
with memory effects as specified by

VarHandle.getOpaque(java.lang.Object...)

.

**Parameters:**
- i

- the index

**Returns:**
- the value

**Since:**
- 9

---

#### public final void setOpaque​(int i,

E
newValue)

Sets the element at index

i

to

newValue

,
with memory effects as specified by

VarHandle.setOpaque(java.lang.Object...)

.

**Parameters:**
- i

- the index
- newValue

- the new value

**Since:**
- 9

---

#### public final
E
getAcquire​(int i)

Returns the current value of the element at index

i

,
with memory effects as specified by

VarHandle.getAcquire(java.lang.Object...)

.

**Parameters:**
- i

- the index

**Returns:**
- the value

**Since:**
- 9

---

#### public final void setRelease​(int i,

E
newValue)

Sets the element at index

i

to

newValue

,
with memory effects as specified by

VarHandle.setRelease(java.lang.Object...)

.

**Parameters:**
- i

- the index
- newValue

- the new value

**Since:**
- 9

---

#### public final
E
compareAndExchange​(int i,

E
expectedValue,

E
newValue)

Atomically sets the element at index

i

to

newValue

if the element's current value, referred to as the

witness
value

,

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndExchange(java.lang.Object...)

.

**Parameters:**
- i

- the index
- expectedValue

- the expected value
- newValue

- the new value

**Returns:**
- the witness value, which will be the same as the
expected value if successful

**Since:**
- 9

---

#### public final
E
compareAndExchangeAcquire​(int i,

E
expectedValue,

E
newValue)

Atomically sets the element at index

i

to

newValue

if the element's current value, referred to as the

witness
value

,

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndExchangeAcquire(java.lang.Object...)

.

**Parameters:**
- i

- the index
- expectedValue

- the expected value
- newValue

- the new value

**Returns:**
- the witness value, which will be the same as the
expected value if successful

**Since:**
- 9

---

#### public final
E
compareAndExchangeRelease​(int i,

E
expectedValue,

E
newValue)

Atomically sets the element at index

i

to

newValue

if the element's current value, referred to as the

witness
value

,

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndExchangeRelease(java.lang.Object...)

.

**Parameters:**
- i

- the index
- expectedValue

- the expected value
- newValue

- the new value

**Returns:**
- the witness value, which will be the same as the
expected value if successful

**Since:**
- 9

---

#### public final boolean weakCompareAndSetVolatile​(int i,

E
expectedValue,

E
newValue)

Possibly atomically sets the element at index

i

to

newValue

if the element's current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSet(java.lang.Object...)

.

**Parameters:**
- i

- the index
- expectedValue

- the expected value
- newValue

- the new value

**Returns:**
- true

if successful

**Since:**
- 9

---

#### public final boolean weakCompareAndSetAcquire​(int i,

E
expectedValue,

E
newValue)

Possibly atomically sets the element at index

i

to

newValue

if the element's current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetAcquire(java.lang.Object...)

.

**Parameters:**
- i

- the index
- expectedValue

- the expected value
- newValue

- the new value

**Returns:**
- true

if successful

**Since:**
- 9

---

#### public final boolean weakCompareAndSetRelease​(int i,

E
expectedValue,

E
newValue)

Possibly atomically sets the element at index

i

to

newValue

if the element's current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetRelease(java.lang.Object...)

.

**Parameters:**
- i

- the index
- expectedValue

- the expected value
- newValue

- the new value

**Returns:**
- true

if successful

**Since:**
- 9

---

### Additional Sections

#### Class AtomicReferenceArray<E>

java.lang.Object

- java.util.concurrent.atomic.AtomicReferenceArray<E>

java.util.concurrent.atomic.AtomicReferenceArray<E>

**Type Parameters:** E

- The base class of elements held in this array

**All Implemented Interfaces:** Serializable

```java
public class
AtomicReferenceArray<E>

extends
Object

implements
Serializable
```

An array of object references in which elements may be updated
atomically. See the

VarHandle

specification for
descriptions of the properties of atomic accesses.

**Since:** 1.5
**See Also:** Serialized Form

public class

AtomicReferenceArray<E>

extends

Object

implements

Serializable

An array of object references in which elements may be updated
atomically. See the

VarHandle

specification for
descriptions of the properties of atomic accesses.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AtomicReferenceArray

​(int length)

Creates a new AtomicReferenceArray of the given length, with all
elements initially null.

AtomicReferenceArray

​(

E

[] array)

Creates a new AtomicReferenceArray with the same length as, and
all elements copied from, the given array.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

E

accumulateAndGet

​(int i,

E

x,

BinaryOperator

<

E

> accumulatorFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the element at index

i

with
the results of applying the given function to the current and
given values, returning the updated value.

E

compareAndExchange

​(int i,

E

expectedValue,

E

newValue)

Atomically sets the element at index

i

to

newValue

if the element's current value, referred to as the

witness
value

,

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndExchange(java.lang.Object...)

.

E

compareAndExchangeAcquire

​(int i,

E

expectedValue,

E

newValue)

Atomically sets the element at index

i

to

newValue

if the element's current value, referred to as the

witness
value

,

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndExchangeAcquire(java.lang.Object...)

.

E

compareAndExchangeRelease

​(int i,

E

expectedValue,

E

newValue)

Atomically sets the element at index

i

to

newValue

if the element's current value, referred to as the

witness
value

,

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndExchangeRelease(java.lang.Object...)

.

boolean

compareAndSet

​(int i,

E

expectedValue,

E

newValue)

Atomically sets the element at index

i

to

newValue

if the element's current value

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

.

E

get

​(int i)

Returns the current value of the element at index

i

,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

E

getAcquire

​(int i)

Returns the current value of the element at index

i

,
with memory effects as specified by

VarHandle.getAcquire(java.lang.Object...)

.

E

getAndAccumulate

​(int i,

E

x,

BinaryOperator

<

E

> accumulatorFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the element at index

i

with
the results of applying the given function to the current and
given values, returning the previous value.

E

getAndSet

​(int i,

E

newValue)

Atomically sets the element at index

i

to

newValue

and returns the old value,
with memory effects as specified by

VarHandle.getAndSet(java.lang.Object...)

.

E

getAndUpdate

​(int i,

UnaryOperator

<

E

> updateFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the element at index

i

with
the results of applying the given function, returning the
previous value.

E

getOpaque

​(int i)

Returns the current value of the element at index

i

,
with memory effects as specified by

VarHandle.getOpaque(java.lang.Object...)

.

E

getPlain

​(int i)

Returns the current value of the element at index

i

,
with memory semantics of reading as if the variable was declared
non-

volatile

.

void

lazySet

​(int i,

E

newValue)

Sets the element at index

i

to

newValue

,
with memory effects as specified by

VarHandle.setRelease(java.lang.Object...)

.

int

length

()

Returns the length of the array.

void

set

​(int i,

E

newValue)

Sets the element at index

i

to

newValue

,
with memory effects as specified by

VarHandle.setVolatile(java.lang.Object...)

.

void

setOpaque

​(int i,

E

newValue)

Sets the element at index

i

to

newValue

,
with memory effects as specified by

VarHandle.setOpaque(java.lang.Object...)

.

void

setPlain

​(int i,

E

newValue)

Sets the element at index

i

to

newValue

,
with memory semantics of setting as if the variable was
declared non-

volatile

and non-

final

.

void

setRelease

​(int i,

E

newValue)

Sets the element at index

i

to

newValue

,
with memory effects as specified by

VarHandle.setRelease(java.lang.Object...)

.

String

toString

()

Returns the String representation of the current values of array.

E

updateAndGet

​(int i,

UnaryOperator

<

E

> updateFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the element at index

i

with
the results of applying the given function, returning the
updated value.

boolean

weakCompareAndSet

​(int i,

E

expectedValue,

E

newValue)

Deprecated.

This method has plain memory effects but the method
name implies volatile memory effects (see methods such as

compareAndExchange(int, E, E)

and

compareAndSet(int, E, E)

).

boolean

weakCompareAndSetAcquire

​(int i,

E

expectedValue,

E

newValue)

Possibly atomically sets the element at index

i

to

newValue

if the element's current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetAcquire(java.lang.Object...)

.

boolean

weakCompareAndSetPlain

​(int i,

E

expectedValue,

E

newValue)

Possibly atomically sets the element at index

i

to

newValue

if the element's current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetPlain(java.lang.Object...)

.

boolean

weakCompareAndSetRelease

​(int i,

E

expectedValue,

E

newValue)

Possibly atomically sets the element at index

i

to

newValue

if the element's current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetRelease(java.lang.Object...)

.

boolean

weakCompareAndSetVolatile

​(int i,

E

expectedValue,

E

newValue)

Possibly atomically sets the element at index

i

to

newValue

if the element's current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSet(java.lang.Object...)

.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

wait

,

wait

,

wait

Constructor Summary

Constructors

Constructor

Description

AtomicReferenceArray

​(int length)

Creates a new AtomicReferenceArray of the given length, with all
elements initially null.

AtomicReferenceArray

​(

E

[] array)

Creates a new AtomicReferenceArray with the same length as, and
all elements copied from, the given array.

---

#### Constructor Summary

Creates a new AtomicReferenceArray of the given length, with all
elements initially null.

Creates a new AtomicReferenceArray with the same length as, and
all elements copied from, the given array.

Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

E

accumulateAndGet

​(int i,

E

x,

BinaryOperator

<

E

> accumulatorFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the element at index

i

with
the results of applying the given function to the current and
given values, returning the updated value.

E

compareAndExchange

​(int i,

E

expectedValue,

E

newValue)

Atomically sets the element at index

i

to

newValue

if the element's current value, referred to as the

witness
value

,

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndExchange(java.lang.Object...)

.

E

compareAndExchangeAcquire

​(int i,

E

expectedValue,

E

newValue)

Atomically sets the element at index

i

to

newValue

if the element's current value, referred to as the

witness
value

,

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndExchangeAcquire(java.lang.Object...)

.

E

compareAndExchangeRelease

​(int i,

E

expectedValue,

E

newValue)

Atomically sets the element at index

i

to

newValue

if the element's current value, referred to as the

witness
value

,

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndExchangeRelease(java.lang.Object...)

.

boolean

compareAndSet

​(int i,

E

expectedValue,

E

newValue)

Atomically sets the element at index

i

to

newValue

if the element's current value

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

.

E

get

​(int i)

Returns the current value of the element at index

i

,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

E

getAcquire

​(int i)

Returns the current value of the element at index

i

,
with memory effects as specified by

VarHandle.getAcquire(java.lang.Object...)

.

E

getAndAccumulate

​(int i,

E

x,

BinaryOperator

<

E

> accumulatorFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the element at index

i

with
the results of applying the given function to the current and
given values, returning the previous value.

E

getAndSet

​(int i,

E

newValue)

Atomically sets the element at index

i

to

newValue

and returns the old value,
with memory effects as specified by

VarHandle.getAndSet(java.lang.Object...)

.

E

getAndUpdate

​(int i,

UnaryOperator

<

E

> updateFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the element at index

i

with
the results of applying the given function, returning the
previous value.

E

getOpaque

​(int i)

Returns the current value of the element at index

i

,
with memory effects as specified by

VarHandle.getOpaque(java.lang.Object...)

.

E

getPlain

​(int i)

Returns the current value of the element at index

i

,
with memory semantics of reading as if the variable was declared
non-

volatile

.

void

lazySet

​(int i,

E

newValue)

Sets the element at index

i

to

newValue

,
with memory effects as specified by

VarHandle.setRelease(java.lang.Object...)

.

int

length

()

Returns the length of the array.

void

set

​(int i,

E

newValue)

Sets the element at index

i

to

newValue

,
with memory effects as specified by

VarHandle.setVolatile(java.lang.Object...)

.

void

setOpaque

​(int i,

E

newValue)

Sets the element at index

i

to

newValue

,
with memory effects as specified by

VarHandle.setOpaque(java.lang.Object...)

.

void

setPlain

​(int i,

E

newValue)

Sets the element at index

i

to

newValue

,
with memory semantics of setting as if the variable was
declared non-

volatile

and non-

final

.

void

setRelease

​(int i,

E

newValue)

Sets the element at index

i

to

newValue

,
with memory effects as specified by

VarHandle.setRelease(java.lang.Object...)

.

String

toString

()

Returns the String representation of the current values of array.

E

updateAndGet

​(int i,

UnaryOperator

<

E

> updateFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the element at index

i

with
the results of applying the given function, returning the
updated value.

boolean

weakCompareAndSet

​(int i,

E

expectedValue,

E

newValue)

Deprecated.

This method has plain memory effects but the method
name implies volatile memory effects (see methods such as

compareAndExchange(int, E, E)

and

compareAndSet(int, E, E)

).

boolean

weakCompareAndSetAcquire

​(int i,

E

expectedValue,

E

newValue)

Possibly atomically sets the element at index

i

to

newValue

if the element's current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetAcquire(java.lang.Object...)

.

boolean

weakCompareAndSetPlain

​(int i,

E

expectedValue,

E

newValue)

Possibly atomically sets the element at index

i

to

newValue

if the element's current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetPlain(java.lang.Object...)

.

boolean

weakCompareAndSetRelease

​(int i,

E

expectedValue,

E

newValue)

Possibly atomically sets the element at index

i

to

newValue

if the element's current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetRelease(java.lang.Object...)

.

boolean

weakCompareAndSetVolatile

​(int i,

E

expectedValue,

E

newValue)

Possibly atomically sets the element at index

i

to

newValue

if the element's current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSet(java.lang.Object...)

.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Method Summary

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the element at index

i

with
the results of applying the given function to the current and
given values, returning the updated value.

Atomically sets the element at index

i

to

newValue

if the element's current value, referred to as the

witness
value

,

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndExchange(java.lang.Object...)

.

Atomically sets the element at index

i

to

newValue

if the element's current value, referred to as the

witness
value

,

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndExchangeAcquire(java.lang.Object...)

.

Atomically sets the element at index

i

to

newValue

if the element's current value, referred to as the

witness
value

,

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndExchangeRelease(java.lang.Object...)

.

Atomically sets the element at index

i

to

newValue

if the element's current value

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

.

Returns the current value of the element at index

i

,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

Returns the current value of the element at index

i

,
with memory effects as specified by

VarHandle.getAcquire(java.lang.Object...)

.

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the element at index

i

with
the results of applying the given function to the current and
given values, returning the previous value.

Atomically sets the element at index

i

to

newValue

and returns the old value,
with memory effects as specified by

VarHandle.getAndSet(java.lang.Object...)

.

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the element at index

i

with
the results of applying the given function, returning the
previous value.

Returns the current value of the element at index

i

,
with memory effects as specified by

VarHandle.getOpaque(java.lang.Object...)

.

Returns the current value of the element at index

i

,
with memory semantics of reading as if the variable was declared
non-

volatile

.

Sets the element at index

i

to

newValue

,
with memory effects as specified by

VarHandle.setRelease(java.lang.Object...)

.

Returns the length of the array.

Sets the element at index

i

to

newValue

,
with memory effects as specified by

VarHandle.setVolatile(java.lang.Object...)

.

Sets the element at index

i

to

newValue

,
with memory effects as specified by

VarHandle.setOpaque(java.lang.Object...)

.

Sets the element at index

i

to

newValue

,
with memory semantics of setting as if the variable was
declared non-

volatile

and non-

final

.

Returns the String representation of the current values of array.

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the element at index

i

with
the results of applying the given function, returning the
updated value.

Deprecated.

This method has plain memory effects but the method
name implies volatile memory effects (see methods such as

compareAndExchange(int, E, E)

and

compareAndSet(int, E, E)

).

Possibly atomically sets the element at index

i

to

newValue

if the element's current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetAcquire(java.lang.Object...)

.

Possibly atomically sets the element at index

i

to

newValue

if the element's current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetPlain(java.lang.Object...)

.

Possibly atomically sets the element at index

i

to

newValue

if the element's current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetRelease(java.lang.Object...)

.

Possibly atomically sets the element at index

i

to

newValue

if the element's current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSet(java.lang.Object...)

.

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- AtomicReferenceArray

```java
public AtomicReferenceArray​(int length)
```

Creates a new AtomicReferenceArray of the given length, with all
elements initially null.

**Parameters:** length

- the length of the array

- AtomicReferenceArray

```java
public AtomicReferenceArray​(
E
[] array)
```

Creates a new AtomicReferenceArray with the same length as, and
all elements copied from, the given array.

**Parameters:** array

- the array to copy elements from
**Throws:** NullPointerException

- if array is null

============ METHOD DETAIL ==========

- Method Detail

- length

```java
public final int length()
```

Returns the length of the array.

**Returns:** the length of the array

- get

```java
public final
E
get​(int i)
```

Returns the current value of the element at index

i

,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

**Parameters:** i

- the index
**Returns:** the current value

- set

```java
public final void set​(int i,

E
newValue)
```

Sets the element at index

i

to

newValue

,
with memory effects as specified by

VarHandle.setVolatile(java.lang.Object...)

.

**Parameters:** i

- the index
**Parameters:** newValue

- the new value

- lazySet

```java
public final void lazySet​(int i,

E
newValue)
```

Sets the element at index

i

to

newValue

,
with memory effects as specified by

VarHandle.setRelease(java.lang.Object...)

.

**Parameters:** i

- the index
**Parameters:** newValue

- the new value
**Since:** 1.6

- getAndSet

```java
public final
E
getAndSet​(int i,

E
newValue)
```

Atomically sets the element at index

i

to

newValue

and returns the old value,
with memory effects as specified by

VarHandle.getAndSet(java.lang.Object...)

.

**Parameters:** i

- the index
**Parameters:** newValue

- the new value
**Returns:** the previous value

- compareAndSet

```java
public final boolean compareAndSet​(int i,

E
expectedValue,

E
newValue)
```

Atomically sets the element at index

i

to

newValue

if the element's current value

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

.

**Parameters:** i

- the index
**Parameters:** expectedValue

- the expected value
**Parameters:** newValue

- the new value
**Returns:** true

if successful. False return indicates that
the actual value was not equal to the expected value.

- weakCompareAndSet

```java
@Deprecated
(
since
="9")
public final boolean weakCompareAndSet​(int i,

E
expectedValue,

E
newValue)
```

Deprecated.

This method has plain memory effects but the method
name implies volatile memory effects (see methods such as

compareAndExchange(int, E, E)

and

compareAndSet(int, E, E)

). To avoid
confusion over plain or volatile memory effects it is recommended that
the method

weakCompareAndSetPlain(int, E, E)

be used instead.

Possibly atomically sets the element at index

i

to

newValue

if the element's current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetPlain(java.lang.Object...)

.

**Parameters:** i

- the index
**Parameters:** expectedValue

- the expected value
**Parameters:** newValue

- the new value
**Returns:** true

if successful
**See Also:** weakCompareAndSetPlain(int, E, E)

- weakCompareAndSetPlain

```java
public final boolean weakCompareAndSetPlain​(int i,

E
expectedValue,

E
newValue)
```

Possibly atomically sets the element at index

i

to

newValue

if the element's current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetPlain(java.lang.Object...)

.

**Parameters:** i

- the index
**Parameters:** expectedValue

- the expected value
**Parameters:** newValue

- the new value
**Returns:** true

if successful
**Since:** 9

- getAndUpdate

```java
public final
E
getAndUpdate​(int i,

UnaryOperator
<
E
> updateFunction)
```

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the element at index

i

with
the results of applying the given function, returning the
previous value. The function should be side-effect-free, since
it may be re-applied when attempted updates fail due to
contention among threads.

**Parameters:** i

- the index
**Parameters:** updateFunction

- a side-effect-free function
**Returns:** the previous value
**Since:** 1.8

- updateAndGet

```java
public final
E
updateAndGet​(int i,

UnaryOperator
<
E
> updateFunction)
```

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the element at index

i

with
the results of applying the given function, returning the
updated value. The function should be side-effect-free, since it
may be re-applied when attempted updates fail due to contention
among threads.

**Parameters:** i

- the index
**Parameters:** updateFunction

- a side-effect-free function
**Returns:** the updated value
**Since:** 1.8

- getAndAccumulate

```java
public final
E
getAndAccumulate​(int i,

E
x,

BinaryOperator
<
E
> accumulatorFunction)
```

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the element at index

i

with
the results of applying the given function to the current and
given values, returning the previous value. The function should
be side-effect-free, since it may be re-applied when attempted
updates fail due to contention among threads. The function is
applied with the current value of the element at index

i

as its first argument, and the given update as the second
argument.

**Parameters:** i

- the index
**Parameters:** x

- the update value
**Parameters:** accumulatorFunction

- a side-effect-free function of two arguments
**Returns:** the previous value
**Since:** 1.8

- accumulateAndGet

```java
public final
E
accumulateAndGet​(int i,

E
x,

BinaryOperator
<
E
> accumulatorFunction)
```

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the element at index

i

with
the results of applying the given function to the current and
given values, returning the updated value. The function should
be side-effect-free, since it may be re-applied when attempted
updates fail due to contention among threads. The function is
applied with the current value of the element at index

i

as its first argument, and the given update as the second
argument.

**Parameters:** i

- the index
**Parameters:** x

- the update value
**Parameters:** accumulatorFunction

- a side-effect-free function of two arguments
**Returns:** the updated value
**Since:** 1.8

- toString

```java
public
String
toString()
```

Returns the String representation of the current values of array.

**Overrides:** toString

in class

Object
**Returns:** the String representation of the current values of array

- getPlain

```java
public final
E
getPlain​(int i)
```

Returns the current value of the element at index

i

,
with memory semantics of reading as if the variable was declared
non-

volatile

.

**Parameters:** i

- the index
**Returns:** the value
**Since:** 9

- setPlain

```java
public final void setPlain​(int i,

E
newValue)
```

Sets the element at index

i

to

newValue

,
with memory semantics of setting as if the variable was
declared non-

volatile

and non-

final

.

**Parameters:** i

- the index
**Parameters:** newValue

- the new value
**Since:** 9

- getOpaque

```java
public final
E
getOpaque​(int i)
```

Returns the current value of the element at index

i

,
with memory effects as specified by

VarHandle.getOpaque(java.lang.Object...)

.

**Parameters:** i

- the index
**Returns:** the value
**Since:** 9

- setOpaque

```java
public final void setOpaque​(int i,

E
newValue)
```

Sets the element at index

i

to

newValue

,
with memory effects as specified by

VarHandle.setOpaque(java.lang.Object...)

.

**Parameters:** i

- the index
**Parameters:** newValue

- the new value
**Since:** 9

- getAcquire

```java
public final
E
getAcquire​(int i)
```

Returns the current value of the element at index

i

,
with memory effects as specified by

VarHandle.getAcquire(java.lang.Object...)

.

**Parameters:** i

- the index
**Returns:** the value
**Since:** 9

- setRelease

```java
public final void setRelease​(int i,

E
newValue)
```

Sets the element at index

i

to

newValue

,
with memory effects as specified by

VarHandle.setRelease(java.lang.Object...)

.

**Parameters:** i

- the index
**Parameters:** newValue

- the new value
**Since:** 9

- compareAndExchange

```java
public final
E
compareAndExchange​(int i,

E
expectedValue,

E
newValue)
```

Atomically sets the element at index

i

to

newValue

if the element's current value, referred to as the

witness
value

,

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndExchange(java.lang.Object...)

.

**Parameters:** i

- the index
**Parameters:** expectedValue

- the expected value
**Parameters:** newValue

- the new value
**Returns:** the witness value, which will be the same as the
expected value if successful
**Since:** 9

- compareAndExchangeAcquire

```java
public final
E
compareAndExchangeAcquire​(int i,

E
expectedValue,

E
newValue)
```

Atomically sets the element at index

i

to

newValue

if the element's current value, referred to as the

witness
value

,

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndExchangeAcquire(java.lang.Object...)

.

**Parameters:** i

- the index
**Parameters:** expectedValue

- the expected value
**Parameters:** newValue

- the new value
**Returns:** the witness value, which will be the same as the
expected value if successful
**Since:** 9

- compareAndExchangeRelease

```java
public final
E
compareAndExchangeRelease​(int i,

E
expectedValue,

E
newValue)
```

Atomically sets the element at index

i

to

newValue

if the element's current value, referred to as the

witness
value

,

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndExchangeRelease(java.lang.Object...)

.

**Parameters:** i

- the index
**Parameters:** expectedValue

- the expected value
**Parameters:** newValue

- the new value
**Returns:** the witness value, which will be the same as the
expected value if successful
**Since:** 9

- weakCompareAndSetVolatile

```java
public final boolean weakCompareAndSetVolatile​(int i,

E
expectedValue,

E
newValue)
```

Possibly atomically sets the element at index

i

to

newValue

if the element's current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSet(java.lang.Object...)

.

**Parameters:** i

- the index
**Parameters:** expectedValue

- the expected value
**Parameters:** newValue

- the new value
**Returns:** true

if successful
**Since:** 9

- weakCompareAndSetAcquire

```java
public final boolean weakCompareAndSetAcquire​(int i,

E
expectedValue,

E
newValue)
```

Possibly atomically sets the element at index

i

to

newValue

if the element's current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetAcquire(java.lang.Object...)

.

**Parameters:** i

- the index
**Parameters:** expectedValue

- the expected value
**Parameters:** newValue

- the new value
**Returns:** true

if successful
**Since:** 9

- weakCompareAndSetRelease

```java
public final boolean weakCompareAndSetRelease​(int i,

E
expectedValue,

E
newValue)
```

Possibly atomically sets the element at index

i

to

newValue

if the element's current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetRelease(java.lang.Object...)

.

**Parameters:** i

- the index
**Parameters:** expectedValue

- the expected value
**Parameters:** newValue

- the new value
**Returns:** true

if successful
**Since:** 9

Constructor Detail

- AtomicReferenceArray

```java
public AtomicReferenceArray​(int length)
```

Creates a new AtomicReferenceArray of the given length, with all
elements initially null.

**Parameters:** length

- the length of the array

- AtomicReferenceArray

```java
public AtomicReferenceArray​(
E
[] array)
```

Creates a new AtomicReferenceArray with the same length as, and
all elements copied from, the given array.

**Parameters:** array

- the array to copy elements from
**Throws:** NullPointerException

- if array is null

---

#### Constructor Detail

AtomicReferenceArray

```java
public AtomicReferenceArray​(int length)
```

Creates a new AtomicReferenceArray of the given length, with all
elements initially null.

**Parameters:** length

- the length of the array

---

#### AtomicReferenceArray

public AtomicReferenceArray​(int length)

Creates a new AtomicReferenceArray of the given length, with all
elements initially null.

AtomicReferenceArray

```java
public AtomicReferenceArray​(
E
[] array)
```

Creates a new AtomicReferenceArray with the same length as, and
all elements copied from, the given array.

**Parameters:** array

- the array to copy elements from
**Throws:** NullPointerException

- if array is null

---

#### AtomicReferenceArray

public AtomicReferenceArray​(

E

[] array)

Creates a new AtomicReferenceArray with the same length as, and
all elements copied from, the given array.

Method Detail

- length

```java
public final int length()
```

Returns the length of the array.

**Returns:** the length of the array

- get

```java
public final
E
get​(int i)
```

Returns the current value of the element at index

i

,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

**Parameters:** i

- the index
**Returns:** the current value

- set

```java
public final void set​(int i,

E
newValue)
```

Sets the element at index

i

to

newValue

,
with memory effects as specified by

VarHandle.setVolatile(java.lang.Object...)

.

**Parameters:** i

- the index
**Parameters:** newValue

- the new value

- lazySet

```java
public final void lazySet​(int i,

E
newValue)
```

Sets the element at index

i

to

newValue

,
with memory effects as specified by

VarHandle.setRelease(java.lang.Object...)

.

**Parameters:** i

- the index
**Parameters:** newValue

- the new value
**Since:** 1.6

- getAndSet

```java
public final
E
getAndSet​(int i,

E
newValue)
```

Atomically sets the element at index

i

to

newValue

and returns the old value,
with memory effects as specified by

VarHandle.getAndSet(java.lang.Object...)

.

**Parameters:** i

- the index
**Parameters:** newValue

- the new value
**Returns:** the previous value

- compareAndSet

```java
public final boolean compareAndSet​(int i,

E
expectedValue,

E
newValue)
```

Atomically sets the element at index

i

to

newValue

if the element's current value

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

.

**Parameters:** i

- the index
**Parameters:** expectedValue

- the expected value
**Parameters:** newValue

- the new value
**Returns:** true

if successful. False return indicates that
the actual value was not equal to the expected value.

- weakCompareAndSet

```java
@Deprecated
(
since
="9")
public final boolean weakCompareAndSet​(int i,

E
expectedValue,

E
newValue)
```

Deprecated.

This method has plain memory effects but the method
name implies volatile memory effects (see methods such as

compareAndExchange(int, E, E)

and

compareAndSet(int, E, E)

). To avoid
confusion over plain or volatile memory effects it is recommended that
the method

weakCompareAndSetPlain(int, E, E)

be used instead.

Possibly atomically sets the element at index

i

to

newValue

if the element's current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetPlain(java.lang.Object...)

.

**Parameters:** i

- the index
**Parameters:** expectedValue

- the expected value
**Parameters:** newValue

- the new value
**Returns:** true

if successful
**See Also:** weakCompareAndSetPlain(int, E, E)

- weakCompareAndSetPlain

```java
public final boolean weakCompareAndSetPlain​(int i,

E
expectedValue,

E
newValue)
```

Possibly atomically sets the element at index

i

to

newValue

if the element's current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetPlain(java.lang.Object...)

.

**Parameters:** i

- the index
**Parameters:** expectedValue

- the expected value
**Parameters:** newValue

- the new value
**Returns:** true

if successful
**Since:** 9

- getAndUpdate

```java
public final
E
getAndUpdate​(int i,

UnaryOperator
<
E
> updateFunction)
```

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the element at index

i

with
the results of applying the given function, returning the
previous value. The function should be side-effect-free, since
it may be re-applied when attempted updates fail due to
contention among threads.

**Parameters:** i

- the index
**Parameters:** updateFunction

- a side-effect-free function
**Returns:** the previous value
**Since:** 1.8

- updateAndGet

```java
public final
E
updateAndGet​(int i,

UnaryOperator
<
E
> updateFunction)
```

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the element at index

i

with
the results of applying the given function, returning the
updated value. The function should be side-effect-free, since it
may be re-applied when attempted updates fail due to contention
among threads.

**Parameters:** i

- the index
**Parameters:** updateFunction

- a side-effect-free function
**Returns:** the updated value
**Since:** 1.8

- getAndAccumulate

```java
public final
E
getAndAccumulate​(int i,

E
x,

BinaryOperator
<
E
> accumulatorFunction)
```

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the element at index

i

with
the results of applying the given function to the current and
given values, returning the previous value. The function should
be side-effect-free, since it may be re-applied when attempted
updates fail due to contention among threads. The function is
applied with the current value of the element at index

i

as its first argument, and the given update as the second
argument.

**Parameters:** i

- the index
**Parameters:** x

- the update value
**Parameters:** accumulatorFunction

- a side-effect-free function of two arguments
**Returns:** the previous value
**Since:** 1.8

- accumulateAndGet

```java
public final
E
accumulateAndGet​(int i,

E
x,

BinaryOperator
<
E
> accumulatorFunction)
```

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the element at index

i

with
the results of applying the given function to the current and
given values, returning the updated value. The function should
be side-effect-free, since it may be re-applied when attempted
updates fail due to contention among threads. The function is
applied with the current value of the element at index

i

as its first argument, and the given update as the second
argument.

**Parameters:** i

- the index
**Parameters:** x

- the update value
**Parameters:** accumulatorFunction

- a side-effect-free function of two arguments
**Returns:** the updated value
**Since:** 1.8

- toString

```java
public
String
toString()
```

Returns the String representation of the current values of array.

**Overrides:** toString

in class

Object
**Returns:** the String representation of the current values of array

- getPlain

```java
public final
E
getPlain​(int i)
```

Returns the current value of the element at index

i

,
with memory semantics of reading as if the variable was declared
non-

volatile

.

**Parameters:** i

- the index
**Returns:** the value
**Since:** 9

- setPlain

```java
public final void setPlain​(int i,

E
newValue)
```

Sets the element at index

i

to

newValue

,
with memory semantics of setting as if the variable was
declared non-

volatile

and non-

final

.

**Parameters:** i

- the index
**Parameters:** newValue

- the new value
**Since:** 9

- getOpaque

```java
public final
E
getOpaque​(int i)
```

Returns the current value of the element at index

i

,
with memory effects as specified by

VarHandle.getOpaque(java.lang.Object...)

.

**Parameters:** i

- the index
**Returns:** the value
**Since:** 9

- setOpaque

```java
public final void setOpaque​(int i,

E
newValue)
```

Sets the element at index

i

to

newValue

,
with memory effects as specified by

VarHandle.setOpaque(java.lang.Object...)

.

**Parameters:** i

- the index
**Parameters:** newValue

- the new value
**Since:** 9

- getAcquire

```java
public final
E
getAcquire​(int i)
```

Returns the current value of the element at index

i

,
with memory effects as specified by

VarHandle.getAcquire(java.lang.Object...)

.

**Parameters:** i

- the index
**Returns:** the value
**Since:** 9

- setRelease

```java
public final void setRelease​(int i,

E
newValue)
```

Sets the element at index

i

to

newValue

,
with memory effects as specified by

VarHandle.setRelease(java.lang.Object...)

.

**Parameters:** i

- the index
**Parameters:** newValue

- the new value
**Since:** 9

- compareAndExchange

```java
public final
E
compareAndExchange​(int i,

E
expectedValue,

E
newValue)
```

Atomically sets the element at index

i

to

newValue

if the element's current value, referred to as the

witness
value

,

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndExchange(java.lang.Object...)

.

**Parameters:** i

- the index
**Parameters:** expectedValue

- the expected value
**Parameters:** newValue

- the new value
**Returns:** the witness value, which will be the same as the
expected value if successful
**Since:** 9

- compareAndExchangeAcquire

```java
public final
E
compareAndExchangeAcquire​(int i,

E
expectedValue,

E
newValue)
```

Atomically sets the element at index

i

to

newValue

if the element's current value, referred to as the

witness
value

,

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndExchangeAcquire(java.lang.Object...)

.

**Parameters:** i

- the index
**Parameters:** expectedValue

- the expected value
**Parameters:** newValue

- the new value
**Returns:** the witness value, which will be the same as the
expected value if successful
**Since:** 9

- compareAndExchangeRelease

```java
public final
E
compareAndExchangeRelease​(int i,

E
expectedValue,

E
newValue)
```

Atomically sets the element at index

i

to

newValue

if the element's current value, referred to as the

witness
value

,

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndExchangeRelease(java.lang.Object...)

.

**Parameters:** i

- the index
**Parameters:** expectedValue

- the expected value
**Parameters:** newValue

- the new value
**Returns:** the witness value, which will be the same as the
expected value if successful
**Since:** 9

- weakCompareAndSetVolatile

```java
public final boolean weakCompareAndSetVolatile​(int i,

E
expectedValue,

E
newValue)
```

Possibly atomically sets the element at index

i

to

newValue

if the element's current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSet(java.lang.Object...)

.

**Parameters:** i

- the index
**Parameters:** expectedValue

- the expected value
**Parameters:** newValue

- the new value
**Returns:** true

if successful
**Since:** 9

- weakCompareAndSetAcquire

```java
public final boolean weakCompareAndSetAcquire​(int i,

E
expectedValue,

E
newValue)
```

Possibly atomically sets the element at index

i

to

newValue

if the element's current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetAcquire(java.lang.Object...)

.

**Parameters:** i

- the index
**Parameters:** expectedValue

- the expected value
**Parameters:** newValue

- the new value
**Returns:** true

if successful
**Since:** 9

- weakCompareAndSetRelease

```java
public final boolean weakCompareAndSetRelease​(int i,

E
expectedValue,

E
newValue)
```

Possibly atomically sets the element at index

i

to

newValue

if the element's current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetRelease(java.lang.Object...)

.

**Parameters:** i

- the index
**Parameters:** expectedValue

- the expected value
**Parameters:** newValue

- the new value
**Returns:** true

if successful
**Since:** 9

---

#### Method Detail

length

```java
public final int length()
```

Returns the length of the array.

**Returns:** the length of the array

---

#### length

public final int length()

Returns the length of the array.

get

```java
public final
E
get​(int i)
```

Returns the current value of the element at index

i

,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

**Parameters:** i

- the index
**Returns:** the current value

---

#### get

public final

E

get​(int i)

Returns the current value of the element at index

i

,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

set

```java
public final void set​(int i,

E
newValue)
```

Sets the element at index

i

to

newValue

,
with memory effects as specified by

VarHandle.setVolatile(java.lang.Object...)

.

**Parameters:** i

- the index
**Parameters:** newValue

- the new value

---

#### set

public final void set​(int i,

E

newValue)

Sets the element at index

i

to

newValue

,
with memory effects as specified by

VarHandle.setVolatile(java.lang.Object...)

.

lazySet

```java
public final void lazySet​(int i,

E
newValue)
```

Sets the element at index

i

to

newValue

,
with memory effects as specified by

VarHandle.setRelease(java.lang.Object...)

.

**Parameters:** i

- the index
**Parameters:** newValue

- the new value
**Since:** 1.6

---

#### lazySet

public final void lazySet​(int i,

E

newValue)

Sets the element at index

i

to

newValue

,
with memory effects as specified by

VarHandle.setRelease(java.lang.Object...)

.

getAndSet

```java
public final
E
getAndSet​(int i,

E
newValue)
```

Atomically sets the element at index

i

to

newValue

and returns the old value,
with memory effects as specified by

VarHandle.getAndSet(java.lang.Object...)

.

**Parameters:** i

- the index
**Parameters:** newValue

- the new value
**Returns:** the previous value

---

#### getAndSet

public final

E

getAndSet​(int i,

E

newValue)

Atomically sets the element at index

i

to

newValue

and returns the old value,
with memory effects as specified by

VarHandle.getAndSet(java.lang.Object...)

.

compareAndSet

```java
public final boolean compareAndSet​(int i,

E
expectedValue,

E
newValue)
```

Atomically sets the element at index

i

to

newValue

if the element's current value

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

.

**Parameters:** i

- the index
**Parameters:** expectedValue

- the expected value
**Parameters:** newValue

- the new value
**Returns:** true

if successful. False return indicates that
the actual value was not equal to the expected value.

---

#### compareAndSet

public final boolean compareAndSet​(int i,

E

expectedValue,

E

newValue)

Atomically sets the element at index

i

to

newValue

if the element's current value

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

.

weakCompareAndSet

```java
@Deprecated
(
since
="9")
public final boolean weakCompareAndSet​(int i,

E
expectedValue,

E
newValue)
```

Deprecated.

This method has plain memory effects but the method
name implies volatile memory effects (see methods such as

compareAndExchange(int, E, E)

and

compareAndSet(int, E, E)

). To avoid
confusion over plain or volatile memory effects it is recommended that
the method

weakCompareAndSetPlain(int, E, E)

be used instead.

Possibly atomically sets the element at index

i

to

newValue

if the element's current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetPlain(java.lang.Object...)

.

**Parameters:** i

- the index
**Parameters:** expectedValue

- the expected value
**Parameters:** newValue

- the new value
**Returns:** true

if successful
**See Also:** weakCompareAndSetPlain(int, E, E)

---

#### weakCompareAndSet

@Deprecated

(

since

="9")
public final boolean weakCompareAndSet​(int i,

E

expectedValue,

E

newValue)

Possibly atomically sets the element at index

i

to

newValue

if the element's current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetPlain(java.lang.Object...)

.

weakCompareAndSetPlain

```java
public final boolean weakCompareAndSetPlain​(int i,

E
expectedValue,

E
newValue)
```

Possibly atomically sets the element at index

i

to

newValue

if the element's current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetPlain(java.lang.Object...)

.

**Parameters:** i

- the index
**Parameters:** expectedValue

- the expected value
**Parameters:** newValue

- the new value
**Returns:** true

if successful
**Since:** 9

---

#### weakCompareAndSetPlain

public final boolean weakCompareAndSetPlain​(int i,

E

expectedValue,

E

newValue)

Possibly atomically sets the element at index

i

to

newValue

if the element's current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetPlain(java.lang.Object...)

.

getAndUpdate

```java
public final
E
getAndUpdate​(int i,

UnaryOperator
<
E
> updateFunction)
```

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the element at index

i

with
the results of applying the given function, returning the
previous value. The function should be side-effect-free, since
it may be re-applied when attempted updates fail due to
contention among threads.

**Parameters:** i

- the index
**Parameters:** updateFunction

- a side-effect-free function
**Returns:** the previous value
**Since:** 1.8

---

#### getAndUpdate

public final

E

getAndUpdate​(int i,

UnaryOperator

<

E

> updateFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the element at index

i

with
the results of applying the given function, returning the
previous value. The function should be side-effect-free, since
it may be re-applied when attempted updates fail due to
contention among threads.

updateAndGet

```java
public final
E
updateAndGet​(int i,

UnaryOperator
<
E
> updateFunction)
```

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the element at index

i

with
the results of applying the given function, returning the
updated value. The function should be side-effect-free, since it
may be re-applied when attempted updates fail due to contention
among threads.

**Parameters:** i

- the index
**Parameters:** updateFunction

- a side-effect-free function
**Returns:** the updated value
**Since:** 1.8

---

#### updateAndGet

public final

E

updateAndGet​(int i,

UnaryOperator

<

E

> updateFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the element at index

i

with
the results of applying the given function, returning the
updated value. The function should be side-effect-free, since it
may be re-applied when attempted updates fail due to contention
among threads.

getAndAccumulate

```java
public final
E
getAndAccumulate​(int i,

E
x,

BinaryOperator
<
E
> accumulatorFunction)
```

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the element at index

i

with
the results of applying the given function to the current and
given values, returning the previous value. The function should
be side-effect-free, since it may be re-applied when attempted
updates fail due to contention among threads. The function is
applied with the current value of the element at index

i

as its first argument, and the given update as the second
argument.

**Parameters:** i

- the index
**Parameters:** x

- the update value
**Parameters:** accumulatorFunction

- a side-effect-free function of two arguments
**Returns:** the previous value
**Since:** 1.8

---

#### getAndAccumulate

public final

E

getAndAccumulate​(int i,

E

x,

BinaryOperator

<

E

> accumulatorFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the element at index

i

with
the results of applying the given function to the current and
given values, returning the previous value. The function should
be side-effect-free, since it may be re-applied when attempted
updates fail due to contention among threads. The function is
applied with the current value of the element at index

i

as its first argument, and the given update as the second
argument.

accumulateAndGet

```java
public final
E
accumulateAndGet​(int i,

E
x,

BinaryOperator
<
E
> accumulatorFunction)
```

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the element at index

i

with
the results of applying the given function to the current and
given values, returning the updated value. The function should
be side-effect-free, since it may be re-applied when attempted
updates fail due to contention among threads. The function is
applied with the current value of the element at index

i

as its first argument, and the given update as the second
argument.

**Parameters:** i

- the index
**Parameters:** x

- the update value
**Parameters:** accumulatorFunction

- a side-effect-free function of two arguments
**Returns:** the updated value
**Since:** 1.8

---

#### accumulateAndGet

public final

E

accumulateAndGet​(int i,

E

x,

BinaryOperator

<

E

> accumulatorFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the element at index

i

with
the results of applying the given function to the current and
given values, returning the updated value. The function should
be side-effect-free, since it may be re-applied when attempted
updates fail due to contention among threads. The function is
applied with the current value of the element at index

i

as its first argument, and the given update as the second
argument.

toString

```java
public
String
toString()
```

Returns the String representation of the current values of array.

**Overrides:** toString

in class

Object
**Returns:** the String representation of the current values of array

---

#### toString

public

String

toString()

Returns the String representation of the current values of array.

getPlain

```java
public final
E
getPlain​(int i)
```

Returns the current value of the element at index

i

,
with memory semantics of reading as if the variable was declared
non-

volatile

.

**Parameters:** i

- the index
**Returns:** the value
**Since:** 9

---

#### getPlain

public final

E

getPlain​(int i)

Returns the current value of the element at index

i

,
with memory semantics of reading as if the variable was declared
non-

volatile

.

setPlain

```java
public final void setPlain​(int i,

E
newValue)
```

Sets the element at index

i

to

newValue

,
with memory semantics of setting as if the variable was
declared non-

volatile

and non-

final

.

**Parameters:** i

- the index
**Parameters:** newValue

- the new value
**Since:** 9

---

#### setPlain

public final void setPlain​(int i,

E

newValue)

Sets the element at index

i

to

newValue

,
with memory semantics of setting as if the variable was
declared non-

volatile

and non-

final

.

getOpaque

```java
public final
E
getOpaque​(int i)
```

Returns the current value of the element at index

i

,
with memory effects as specified by

VarHandle.getOpaque(java.lang.Object...)

.

**Parameters:** i

- the index
**Returns:** the value
**Since:** 9

---

#### getOpaque

public final

E

getOpaque​(int i)

Returns the current value of the element at index

i

,
with memory effects as specified by

VarHandle.getOpaque(java.lang.Object...)

.

setOpaque

```java
public final void setOpaque​(int i,

E
newValue)
```

Sets the element at index

i

to

newValue

,
with memory effects as specified by

VarHandle.setOpaque(java.lang.Object...)

.

**Parameters:** i

- the index
**Parameters:** newValue

- the new value
**Since:** 9

---

#### setOpaque

public final void setOpaque​(int i,

E

newValue)

Sets the element at index

i

to

newValue

,
with memory effects as specified by

VarHandle.setOpaque(java.lang.Object...)

.

getAcquire

```java
public final
E
getAcquire​(int i)
```

Returns the current value of the element at index

i

,
with memory effects as specified by

VarHandle.getAcquire(java.lang.Object...)

.

**Parameters:** i

- the index
**Returns:** the value
**Since:** 9

---

#### getAcquire

public final

E

getAcquire​(int i)

Returns the current value of the element at index

i

,
with memory effects as specified by

VarHandle.getAcquire(java.lang.Object...)

.

setRelease

```java
public final void setRelease​(int i,

E
newValue)
```

Sets the element at index

i

to

newValue

,
with memory effects as specified by

VarHandle.setRelease(java.lang.Object...)

.

**Parameters:** i

- the index
**Parameters:** newValue

- the new value
**Since:** 9

---

#### setRelease

public final void setRelease​(int i,

E

newValue)

Sets the element at index

i

to

newValue

,
with memory effects as specified by

VarHandle.setRelease(java.lang.Object...)

.

compareAndExchange

```java
public final
E
compareAndExchange​(int i,

E
expectedValue,

E
newValue)
```

Atomically sets the element at index

i

to

newValue

if the element's current value, referred to as the

witness
value

,

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndExchange(java.lang.Object...)

.

**Parameters:** i

- the index
**Parameters:** expectedValue

- the expected value
**Parameters:** newValue

- the new value
**Returns:** the witness value, which will be the same as the
expected value if successful
**Since:** 9

---

#### compareAndExchange

public final

E

compareAndExchange​(int i,

E

expectedValue,

E

newValue)

Atomically sets the element at index

i

to

newValue

if the element's current value, referred to as the

witness
value

,

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndExchange(java.lang.Object...)

.

compareAndExchangeAcquire

```java
public final
E
compareAndExchangeAcquire​(int i,

E
expectedValue,

E
newValue)
```

Atomically sets the element at index

i

to

newValue

if the element's current value, referred to as the

witness
value

,

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndExchangeAcquire(java.lang.Object...)

.

**Parameters:** i

- the index
**Parameters:** expectedValue

- the expected value
**Parameters:** newValue

- the new value
**Returns:** the witness value, which will be the same as the
expected value if successful
**Since:** 9

---

#### compareAndExchangeAcquire

public final

E

compareAndExchangeAcquire​(int i,

E

expectedValue,

E

newValue)

Atomically sets the element at index

i

to

newValue

if the element's current value, referred to as the

witness
value

,

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndExchangeAcquire(java.lang.Object...)

.

compareAndExchangeRelease

```java
public final
E
compareAndExchangeRelease​(int i,

E
expectedValue,

E
newValue)
```

Atomically sets the element at index

i

to

newValue

if the element's current value, referred to as the

witness
value

,

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndExchangeRelease(java.lang.Object...)

.

**Parameters:** i

- the index
**Parameters:** expectedValue

- the expected value
**Parameters:** newValue

- the new value
**Returns:** the witness value, which will be the same as the
expected value if successful
**Since:** 9

---

#### compareAndExchangeRelease

public final

E

compareAndExchangeRelease​(int i,

E

expectedValue,

E

newValue)

Atomically sets the element at index

i

to

newValue

if the element's current value, referred to as the

witness
value

,

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndExchangeRelease(java.lang.Object...)

.

weakCompareAndSetVolatile

```java
public final boolean weakCompareAndSetVolatile​(int i,

E
expectedValue,

E
newValue)
```

Possibly atomically sets the element at index

i

to

newValue

if the element's current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSet(java.lang.Object...)

.

**Parameters:** i

- the index
**Parameters:** expectedValue

- the expected value
**Parameters:** newValue

- the new value
**Returns:** true

if successful
**Since:** 9

---

#### weakCompareAndSetVolatile

public final boolean weakCompareAndSetVolatile​(int i,

E

expectedValue,

E

newValue)

Possibly atomically sets the element at index

i

to

newValue

if the element's current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSet(java.lang.Object...)

.

weakCompareAndSetAcquire

```java
public final boolean weakCompareAndSetAcquire​(int i,

E
expectedValue,

E
newValue)
```

Possibly atomically sets the element at index

i

to

newValue

if the element's current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetAcquire(java.lang.Object...)

.

**Parameters:** i

- the index
**Parameters:** expectedValue

- the expected value
**Parameters:** newValue

- the new value
**Returns:** true

if successful
**Since:** 9

---

#### weakCompareAndSetAcquire

public final boolean weakCompareAndSetAcquire​(int i,

E

expectedValue,

E

newValue)

Possibly atomically sets the element at index

i

to

newValue

if the element's current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetAcquire(java.lang.Object...)

.

weakCompareAndSetRelease

```java
public final boolean weakCompareAndSetRelease​(int i,

E
expectedValue,

E
newValue)
```

Possibly atomically sets the element at index

i

to

newValue

if the element's current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetRelease(java.lang.Object...)

.

**Parameters:** i

- the index
**Parameters:** expectedValue

- the expected value
**Parameters:** newValue

- the new value
**Returns:** true

if successful
**Since:** 9

---

#### weakCompareAndSetRelease

public final boolean weakCompareAndSetRelease​(int i,

E

expectedValue,

E

newValue)

Possibly atomically sets the element at index

i

to

newValue

if the element's current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetRelease(java.lang.Object...)

.

---

