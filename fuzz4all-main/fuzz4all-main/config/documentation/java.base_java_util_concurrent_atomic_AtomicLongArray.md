# Class AtomicLongArray

**Source:** `java.base\java\util\concurrent\atomic\AtomicLongArray.html`

### Class Description

```java
public class
AtomicLongArray

extends
Object

implements
Serializable
```

A

long

array in which elements may be updated atomically.
See the

VarHandle

specification for descriptions of the
properties of atomic accesses.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public AtomicLongArray​(int length)

Creates a new AtomicLongArray of the given length, with all
elements initially zero.

**Parameters:**
- length

- the length of the array

---

#### public AtomicLongArray​(long[] array)

Creates a new AtomicLongArray with the same length as, and
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

#### public final long get​(int i)

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
long newValue)

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
long newValue)

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

#### public final long getAndSet​(int i,
long newValue)

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
long expectedValue,
long newValue)

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
long expectedValue,
long newValue)

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
- weakCompareAndSetPlain(int, long, long)

---

#### public final boolean weakCompareAndSetPlain​(int i,
long expectedValue,
long newValue)

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

#### public final long getAndIncrement​(int i)

Atomically increments the value of the element at index

i

,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

Equivalent to

getAndAdd(i, 1)

.

**Parameters:**
- i

- the index

**Returns:**
- the previous value

---

#### public final long getAndDecrement​(int i)

Atomically decrements the value of the element at index

i

,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

Equivalent to

getAndAdd(i, -1)

.

**Parameters:**
- i

- the index

**Returns:**
- the previous value

---

#### public final long getAndAdd​(int i,
long delta)

Atomically adds the given value to the element at index

i

,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

**Parameters:**
- i

- the index
- delta

- the value to add

**Returns:**
- the previous value

---

#### public final long incrementAndGet​(int i)

Atomically increments the value of the element at index

i

,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

Equivalent to

addAndGet(i, 1)

.

**Parameters:**
- i

- the index

**Returns:**
- the updated value

---

#### public final long decrementAndGet​(int i)

Atomically decrements the value of the element at index

i

,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

Equivalent to

addAndGet(i, -1)

.

**Parameters:**
- i

- the index

**Returns:**
- the updated value

---

#### public long addAndGet​(int i,
long delta)

Atomically adds the given value to the element at index

i

,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

**Parameters:**
- i

- the index
- delta

- the value to add

**Returns:**
- the updated value

---

#### public final long getAndUpdate​(int i,

LongUnaryOperator
updateFunction)

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

#### public final long updateAndGet​(int i,

LongUnaryOperator
updateFunction)

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

#### public final long getAndAccumulate​(int i,
long x,

LongBinaryOperator
accumulatorFunction)

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

#### public final long accumulateAndGet​(int i,
long x,

LongBinaryOperator
accumulatorFunction)

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

#### public final long getPlain​(int i)

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
long newValue)

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

#### public final long getOpaque​(int i)

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
long newValue)

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

#### public final long getAcquire​(int i)

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
long newValue)

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

#### public final long compareAndExchange​(int i,
long expectedValue,
long newValue)

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

#### public final long compareAndExchangeAcquire​(int i,
long expectedValue,
long newValue)

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

#### public final long compareAndExchangeRelease​(int i,
long expectedValue,
long newValue)

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
long expectedValue,
long newValue)

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
long expectedValue,
long newValue)

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
long expectedValue,
long newValue)

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

#### Class AtomicLongArray

java.lang.Object

- java.util.concurrent.atomic.AtomicLongArray

java.util.concurrent.atomic.AtomicLongArray

**All Implemented Interfaces:** Serializable

```java
public class
AtomicLongArray

extends
Object

implements
Serializable
```

A

long

array in which elements may be updated atomically.
See the

VarHandle

specification for descriptions of the
properties of atomic accesses.

**Since:** 1.5
**See Also:** Serialized Form

public class

AtomicLongArray

extends

Object

implements

Serializable

A

long

array in which elements may be updated atomically.
See the

VarHandle

specification for descriptions of the
properties of atomic accesses.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AtomicLongArray

​(int length)

Creates a new AtomicLongArray of the given length, with all
elements initially zero.

AtomicLongArray

​(long[] array)

Creates a new AtomicLongArray with the same length as, and
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

long

accumulateAndGet

​(int i,
long x,

LongBinaryOperator

accumulatorFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the element at index

i

with
the results of applying the given function to the current and
given values, returning the updated value.

long

addAndGet

​(int i,
long delta)

Atomically adds the given value to the element at index

i

,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

long

compareAndExchange

​(int i,
long expectedValue,
long newValue)

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

long

compareAndExchangeAcquire

​(int i,
long expectedValue,
long newValue)

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

long

compareAndExchangeRelease

​(int i,
long expectedValue,
long newValue)

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
long expectedValue,
long newValue)

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

long

decrementAndGet

​(int i)

Atomically decrements the value of the element at index

i

,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

long

get

​(int i)

Returns the current value of the element at index

i

,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

long

getAcquire

​(int i)

Returns the current value of the element at index

i

,
with memory effects as specified by

VarHandle.getAcquire(java.lang.Object...)

.

long

getAndAccumulate

​(int i,
long x,

LongBinaryOperator

accumulatorFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the element at index

i

with
the results of applying the given function to the current and
given values, returning the previous value.

long

getAndAdd

​(int i,
long delta)

Atomically adds the given value to the element at index

i

,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

long

getAndDecrement

​(int i)

Atomically decrements the value of the element at index

i

,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

long

getAndIncrement

​(int i)

Atomically increments the value of the element at index

i

,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

long

getAndSet

​(int i,
long newValue)

Atomically sets the element at index

i

to

newValue

and returns the old value,
with memory effects as specified by

VarHandle.getAndSet(java.lang.Object...)

.

long

getAndUpdate

​(int i,

LongUnaryOperator

updateFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the element at index

i

with
the results of applying the given function, returning the
previous value.

long

getOpaque

​(int i)

Returns the current value of the element at index

i

,
with memory effects as specified by

VarHandle.getOpaque(java.lang.Object...)

.

long

getPlain

​(int i)

Returns the current value of the element at index

i

,
with memory semantics of reading as if the variable was declared
non-

volatile

.

long

incrementAndGet

​(int i)

Atomically increments the value of the element at index

i

,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

void

lazySet

​(int i,
long newValue)

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
long newValue)

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
long newValue)

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
long newValue)

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
long newValue)

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

long

updateAndGet

​(int i,

LongUnaryOperator

updateFunction)

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
long expectedValue,
long newValue)

Deprecated.

This method has plain memory effects but the method
name implies volatile memory effects (see methods such as

compareAndExchange(int, long, long)

and

compareAndSet(int, long, long)

).

boolean

weakCompareAndSetAcquire

​(int i,
long expectedValue,
long newValue)

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
long expectedValue,
long newValue)

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
long expectedValue,
long newValue)

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
long expectedValue,
long newValue)

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

AtomicLongArray

​(int length)

Creates a new AtomicLongArray of the given length, with all
elements initially zero.

AtomicLongArray

​(long[] array)

Creates a new AtomicLongArray with the same length as, and
all elements copied from, the given array.

---

#### Constructor Summary

Creates a new AtomicLongArray of the given length, with all
elements initially zero.

Creates a new AtomicLongArray with the same length as, and
all elements copied from, the given array.

Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

long

accumulateAndGet

​(int i,
long x,

LongBinaryOperator

accumulatorFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the element at index

i

with
the results of applying the given function to the current and
given values, returning the updated value.

long

addAndGet

​(int i,
long delta)

Atomically adds the given value to the element at index

i

,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

long

compareAndExchange

​(int i,
long expectedValue,
long newValue)

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

long

compareAndExchangeAcquire

​(int i,
long expectedValue,
long newValue)

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

long

compareAndExchangeRelease

​(int i,
long expectedValue,
long newValue)

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
long expectedValue,
long newValue)

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

long

decrementAndGet

​(int i)

Atomically decrements the value of the element at index

i

,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

long

get

​(int i)

Returns the current value of the element at index

i

,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

long

getAcquire

​(int i)

Returns the current value of the element at index

i

,
with memory effects as specified by

VarHandle.getAcquire(java.lang.Object...)

.

long

getAndAccumulate

​(int i,
long x,

LongBinaryOperator

accumulatorFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the element at index

i

with
the results of applying the given function to the current and
given values, returning the previous value.

long

getAndAdd

​(int i,
long delta)

Atomically adds the given value to the element at index

i

,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

long

getAndDecrement

​(int i)

Atomically decrements the value of the element at index

i

,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

long

getAndIncrement

​(int i)

Atomically increments the value of the element at index

i

,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

long

getAndSet

​(int i,
long newValue)

Atomically sets the element at index

i

to

newValue

and returns the old value,
with memory effects as specified by

VarHandle.getAndSet(java.lang.Object...)

.

long

getAndUpdate

​(int i,

LongUnaryOperator

updateFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the element at index

i

with
the results of applying the given function, returning the
previous value.

long

getOpaque

​(int i)

Returns the current value of the element at index

i

,
with memory effects as specified by

VarHandle.getOpaque(java.lang.Object...)

.

long

getPlain

​(int i)

Returns the current value of the element at index

i

,
with memory semantics of reading as if the variable was declared
non-

volatile

.

long

incrementAndGet

​(int i)

Atomically increments the value of the element at index

i

,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

void

lazySet

​(int i,
long newValue)

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
long newValue)

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
long newValue)

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
long newValue)

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
long newValue)

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

long

updateAndGet

​(int i,

LongUnaryOperator

updateFunction)

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
long expectedValue,
long newValue)

Deprecated.

This method has plain memory effects but the method
name implies volatile memory effects (see methods such as

compareAndExchange(int, long, long)

and

compareAndSet(int, long, long)

).

boolean

weakCompareAndSetAcquire

​(int i,
long expectedValue,
long newValue)

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
long expectedValue,
long newValue)

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
long expectedValue,
long newValue)

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
long expectedValue,
long newValue)

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

Atomically adds the given value to the element at index

i

,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

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

Atomically decrements the value of the element at index

i

,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

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

Atomically increments the value of the element at index

i

,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

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

compareAndExchange(int, long, long)

and

compareAndSet(int, long, long)

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

- AtomicLongArray

```java
public AtomicLongArray​(int length)
```

Creates a new AtomicLongArray of the given length, with all
elements initially zero.

**Parameters:** length

- the length of the array

- AtomicLongArray

```java
public AtomicLongArray​(long[] array)
```

Creates a new AtomicLongArray with the same length as, and
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
public final long get​(int i)
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
long newValue)
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
long newValue)
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
public final long getAndSet​(int i,
long newValue)
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
long expectedValue,
long newValue)
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
long expectedValue,
long newValue)
```

Deprecated.

This method has plain memory effects but the method
name implies volatile memory effects (see methods such as

compareAndExchange(int, long, long)

and

compareAndSet(int, long, long)

). To avoid
confusion over plain or volatile memory effects it is recommended that
the method

weakCompareAndSetPlain(int, long, long)

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
**See Also:** weakCompareAndSetPlain(int, long, long)

- weakCompareAndSetPlain

```java
public final boolean weakCompareAndSetPlain​(int i,
long expectedValue,
long newValue)
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

- getAndIncrement

```java
public final long getAndIncrement​(int i)
```

Atomically increments the value of the element at index

i

,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

Equivalent to

getAndAdd(i, 1)

.

**Parameters:** i

- the index
**Returns:** the previous value

- getAndDecrement

```java
public final long getAndDecrement​(int i)
```

Atomically decrements the value of the element at index

i

,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

Equivalent to

getAndAdd(i, -1)

.

**Parameters:** i

- the index
**Returns:** the previous value

- getAndAdd

```java
public final long getAndAdd​(int i,
long delta)
```

Atomically adds the given value to the element at index

i

,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

**Parameters:** i

- the index
**Parameters:** delta

- the value to add
**Returns:** the previous value

- incrementAndGet

```java
public final long incrementAndGet​(int i)
```

Atomically increments the value of the element at index

i

,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

Equivalent to

addAndGet(i, 1)

.

**Parameters:** i

- the index
**Returns:** the updated value

- decrementAndGet

```java
public final long decrementAndGet​(int i)
```

Atomically decrements the value of the element at index

i

,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

Equivalent to

addAndGet(i, -1)

.

**Parameters:** i

- the index
**Returns:** the updated value

- addAndGet

```java
public long addAndGet​(int i,
long delta)
```

Atomically adds the given value to the element at index

i

,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

**Parameters:** i

- the index
**Parameters:** delta

- the value to add
**Returns:** the updated value

- getAndUpdate

```java
public final long getAndUpdate​(int i,

LongUnaryOperator
updateFunction)
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
public final long updateAndGet​(int i,

LongUnaryOperator
updateFunction)
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
public final long getAndAccumulate​(int i,
long x,

LongBinaryOperator
accumulatorFunction)
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
public final long accumulateAndGet​(int i,
long x,

LongBinaryOperator
accumulatorFunction)
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
public final long getPlain​(int i)
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
long newValue)
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
public final long getOpaque​(int i)
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
long newValue)
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
public final long getAcquire​(int i)
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
long newValue)
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
public final long compareAndExchange​(int i,
long expectedValue,
long newValue)
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
public final long compareAndExchangeAcquire​(int i,
long expectedValue,
long newValue)
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
public final long compareAndExchangeRelease​(int i,
long expectedValue,
long newValue)
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
long expectedValue,
long newValue)
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
long expectedValue,
long newValue)
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
long expectedValue,
long newValue)
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

- AtomicLongArray

```java
public AtomicLongArray​(int length)
```

Creates a new AtomicLongArray of the given length, with all
elements initially zero.

**Parameters:** length

- the length of the array

- AtomicLongArray

```java
public AtomicLongArray​(long[] array)
```

Creates a new AtomicLongArray with the same length as, and
all elements copied from, the given array.

**Parameters:** array

- the array to copy elements from
**Throws:** NullPointerException

- if array is null

---

#### Constructor Detail

AtomicLongArray

```java
public AtomicLongArray​(int length)
```

Creates a new AtomicLongArray of the given length, with all
elements initially zero.

**Parameters:** length

- the length of the array

---

#### AtomicLongArray

public AtomicLongArray​(int length)

Creates a new AtomicLongArray of the given length, with all
elements initially zero.

AtomicLongArray

```java
public AtomicLongArray​(long[] array)
```

Creates a new AtomicLongArray with the same length as, and
all elements copied from, the given array.

**Parameters:** array

- the array to copy elements from
**Throws:** NullPointerException

- if array is null

---

#### AtomicLongArray

public AtomicLongArray​(long[] array)

Creates a new AtomicLongArray with the same length as, and
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
public final long get​(int i)
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
long newValue)
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
long newValue)
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
public final long getAndSet​(int i,
long newValue)
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
long expectedValue,
long newValue)
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
long expectedValue,
long newValue)
```

Deprecated.

This method has plain memory effects but the method
name implies volatile memory effects (see methods such as

compareAndExchange(int, long, long)

and

compareAndSet(int, long, long)

). To avoid
confusion over plain or volatile memory effects it is recommended that
the method

weakCompareAndSetPlain(int, long, long)

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
**See Also:** weakCompareAndSetPlain(int, long, long)

- weakCompareAndSetPlain

```java
public final boolean weakCompareAndSetPlain​(int i,
long expectedValue,
long newValue)
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

- getAndIncrement

```java
public final long getAndIncrement​(int i)
```

Atomically increments the value of the element at index

i

,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

Equivalent to

getAndAdd(i, 1)

.

**Parameters:** i

- the index
**Returns:** the previous value

- getAndDecrement

```java
public final long getAndDecrement​(int i)
```

Atomically decrements the value of the element at index

i

,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

Equivalent to

getAndAdd(i, -1)

.

**Parameters:** i

- the index
**Returns:** the previous value

- getAndAdd

```java
public final long getAndAdd​(int i,
long delta)
```

Atomically adds the given value to the element at index

i

,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

**Parameters:** i

- the index
**Parameters:** delta

- the value to add
**Returns:** the previous value

- incrementAndGet

```java
public final long incrementAndGet​(int i)
```

Atomically increments the value of the element at index

i

,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

Equivalent to

addAndGet(i, 1)

.

**Parameters:** i

- the index
**Returns:** the updated value

- decrementAndGet

```java
public final long decrementAndGet​(int i)
```

Atomically decrements the value of the element at index

i

,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

Equivalent to

addAndGet(i, -1)

.

**Parameters:** i

- the index
**Returns:** the updated value

- addAndGet

```java
public long addAndGet​(int i,
long delta)
```

Atomically adds the given value to the element at index

i

,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

**Parameters:** i

- the index
**Parameters:** delta

- the value to add
**Returns:** the updated value

- getAndUpdate

```java
public final long getAndUpdate​(int i,

LongUnaryOperator
updateFunction)
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
public final long updateAndGet​(int i,

LongUnaryOperator
updateFunction)
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
public final long getAndAccumulate​(int i,
long x,

LongBinaryOperator
accumulatorFunction)
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
public final long accumulateAndGet​(int i,
long x,

LongBinaryOperator
accumulatorFunction)
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
public final long getPlain​(int i)
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
long newValue)
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
public final long getOpaque​(int i)
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
long newValue)
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
public final long getAcquire​(int i)
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
long newValue)
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
public final long compareAndExchange​(int i,
long expectedValue,
long newValue)
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
public final long compareAndExchangeAcquire​(int i,
long expectedValue,
long newValue)
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
public final long compareAndExchangeRelease​(int i,
long expectedValue,
long newValue)
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
long expectedValue,
long newValue)
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
long expectedValue,
long newValue)
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
long expectedValue,
long newValue)
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
public final long get​(int i)
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

public final long get​(int i)

Returns the current value of the element at index

i

,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

set

```java
public final void set​(int i,
long newValue)
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
long newValue)

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
long newValue)
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
long newValue)

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
public final long getAndSet​(int i,
long newValue)
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

public final long getAndSet​(int i,
long newValue)

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
long expectedValue,
long newValue)
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
long expectedValue,
long newValue)

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
long expectedValue,
long newValue)
```

Deprecated.

This method has plain memory effects but the method
name implies volatile memory effects (see methods such as

compareAndExchange(int, long, long)

and

compareAndSet(int, long, long)

). To avoid
confusion over plain or volatile memory effects it is recommended that
the method

weakCompareAndSetPlain(int, long, long)

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
**See Also:** weakCompareAndSetPlain(int, long, long)

---

#### weakCompareAndSet

@Deprecated

(

since

="9")
public final boolean weakCompareAndSet​(int i,
long expectedValue,
long newValue)

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
long expectedValue,
long newValue)
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
long expectedValue,
long newValue)

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

getAndIncrement

```java
public final long getAndIncrement​(int i)
```

Atomically increments the value of the element at index

i

,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

Equivalent to

getAndAdd(i, 1)

.

**Parameters:** i

- the index
**Returns:** the previous value

---

#### getAndIncrement

public final long getAndIncrement​(int i)

Atomically increments the value of the element at index

i

,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

Equivalent to

getAndAdd(i, 1)

.

Equivalent to

getAndAdd(i, 1)

.

getAndDecrement

```java
public final long getAndDecrement​(int i)
```

Atomically decrements the value of the element at index

i

,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

Equivalent to

getAndAdd(i, -1)

.

**Parameters:** i

- the index
**Returns:** the previous value

---

#### getAndDecrement

public final long getAndDecrement​(int i)

Atomically decrements the value of the element at index

i

,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

Equivalent to

getAndAdd(i, -1)

.

Equivalent to

getAndAdd(i, -1)

.

getAndAdd

```java
public final long getAndAdd​(int i,
long delta)
```

Atomically adds the given value to the element at index

i

,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

**Parameters:** i

- the index
**Parameters:** delta

- the value to add
**Returns:** the previous value

---

#### getAndAdd

public final long getAndAdd​(int i,
long delta)

Atomically adds the given value to the element at index

i

,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

incrementAndGet

```java
public final long incrementAndGet​(int i)
```

Atomically increments the value of the element at index

i

,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

Equivalent to

addAndGet(i, 1)

.

**Parameters:** i

- the index
**Returns:** the updated value

---

#### incrementAndGet

public final long incrementAndGet​(int i)

Atomically increments the value of the element at index

i

,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

Equivalent to

addAndGet(i, 1)

.

Equivalent to

addAndGet(i, 1)

.

decrementAndGet

```java
public final long decrementAndGet​(int i)
```

Atomically decrements the value of the element at index

i

,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

Equivalent to

addAndGet(i, -1)

.

**Parameters:** i

- the index
**Returns:** the updated value

---

#### decrementAndGet

public final long decrementAndGet​(int i)

Atomically decrements the value of the element at index

i

,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

Equivalent to

addAndGet(i, -1)

.

Equivalent to

addAndGet(i, -1)

.

addAndGet

```java
public long addAndGet​(int i,
long delta)
```

Atomically adds the given value to the element at index

i

,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

**Parameters:** i

- the index
**Parameters:** delta

- the value to add
**Returns:** the updated value

---

#### addAndGet

public long addAndGet​(int i,
long delta)

Atomically adds the given value to the element at index

i

,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

getAndUpdate

```java
public final long getAndUpdate​(int i,

LongUnaryOperator
updateFunction)
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

public final long getAndUpdate​(int i,

LongUnaryOperator

updateFunction)

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
public final long updateAndGet​(int i,

LongUnaryOperator
updateFunction)
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

public final long updateAndGet​(int i,

LongUnaryOperator

updateFunction)

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
public final long getAndAccumulate​(int i,
long x,

LongBinaryOperator
accumulatorFunction)
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

public final long getAndAccumulate​(int i,
long x,

LongBinaryOperator

accumulatorFunction)

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
public final long accumulateAndGet​(int i,
long x,

LongBinaryOperator
accumulatorFunction)
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

public final long accumulateAndGet​(int i,
long x,

LongBinaryOperator

accumulatorFunction)

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
public final long getPlain​(int i)
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

public final long getPlain​(int i)

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
long newValue)
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
long newValue)

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
public final long getOpaque​(int i)
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

public final long getOpaque​(int i)

Returns the current value of the element at index

i

,
with memory effects as specified by

VarHandle.getOpaque(java.lang.Object...)

.

setOpaque

```java
public final void setOpaque​(int i,
long newValue)
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
long newValue)

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
public final long getAcquire​(int i)
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

public final long getAcquire​(int i)

Returns the current value of the element at index

i

,
with memory effects as specified by

VarHandle.getAcquire(java.lang.Object...)

.

setRelease

```java
public final void setRelease​(int i,
long newValue)
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
long newValue)

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
public final long compareAndExchange​(int i,
long expectedValue,
long newValue)
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

public final long compareAndExchange​(int i,
long expectedValue,
long newValue)

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
public final long compareAndExchangeAcquire​(int i,
long expectedValue,
long newValue)
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

public final long compareAndExchangeAcquire​(int i,
long expectedValue,
long newValue)

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
public final long compareAndExchangeRelease​(int i,
long expectedValue,
long newValue)
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

public final long compareAndExchangeRelease​(int i,
long expectedValue,
long newValue)

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
long expectedValue,
long newValue)
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
long expectedValue,
long newValue)

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
long expectedValue,
long newValue)
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
long expectedValue,
long newValue)

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
long expectedValue,
long newValue)
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
long expectedValue,
long newValue)

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

