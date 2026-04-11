# Class AtomicLong

**Source:** `java.base\java\util\concurrent\atomic\AtomicLong.html`

### Class Description

```java
public class
AtomicLong

extends
Number

implements
Serializable
```

A

long

value that may be updated atomically. See the

VarHandle

specification for descriptions of the properties
of atomic accesses. An

AtomicLong

is used in applications
such as atomically incremented sequence numbers, and cannot be used
as a replacement for a

Long

. However, this class
does extend

Number

to allow uniform access by tools and
utilities that deal with numerically-based classes.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public AtomicLong​(long initialValue)

Creates a new AtomicLong with the given initial value.

**Parameters:**
- initialValue

- the initial value

---

#### public AtomicLong()

Creates a new AtomicLong with initial value

0

.

---

### Method Details

#### public final long get()

Returns the current value,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

**Returns:**
- the current value

---

#### public final void set​(long newValue)

Sets the value to

newValue

,
with memory effects as specified by

VarHandle.setVolatile(java.lang.Object...)

.

**Parameters:**
- newValue

- the new value

---

#### public final void lazySet​(long newValue)

Sets the value to

newValue

,
with memory effects as specified by

VarHandle.setRelease(java.lang.Object...)

.

**Parameters:**
- newValue

- the new value

**Since:**
- 1.6

---

#### public final long getAndSet​(long newValue)

Atomically sets the value to

newValue

and returns the old value,
with memory effects as specified by

VarHandle.getAndSet(java.lang.Object...)

.

**Parameters:**
- newValue

- the new value

**Returns:**
- the previous value

---

#### public final boolean compareAndSet​(long expectedValue,
long newValue)

Atomically sets the value to

newValue

if the current value

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

.

**Parameters:**
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
public final boolean weakCompareAndSet​(long expectedValue,
long newValue)

Possibly atomically sets the value to

newValue

if the current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetPlain(java.lang.Object...)

.

**Parameters:**
- expectedValue

- the expected value
- newValue

- the new value

**Returns:**
- true

if successful

**See Also:**
- weakCompareAndSetPlain(long, long)

---

#### public final boolean weakCompareAndSetPlain​(long expectedValue,
long newValue)

Possibly atomically sets the value to

newValue

if the current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetPlain(java.lang.Object...)

.

**Parameters:**
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

#### public final long getAndIncrement()

Atomically increments the current value,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

Equivalent to

getAndAdd(1)

.

**Returns:**
- the previous value

---

#### public final long getAndDecrement()

Atomically decrements the current value,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

Equivalent to

getAndAdd(-1)

.

**Returns:**
- the previous value

---

#### public final long getAndAdd​(long delta)

Atomically adds the given value to the current value,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

**Parameters:**
- delta

- the value to add

**Returns:**
- the previous value

---

#### public final long incrementAndGet()

Atomically increments the current value,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

Equivalent to

addAndGet(1)

.

**Returns:**
- the updated value

---

#### public final long decrementAndGet()

Atomically decrements the current value,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

Equivalent to

addAndGet(-1)

.

**Returns:**
- the updated value

---

#### public final long addAndGet​(long delta)

Atomically adds the given value to the current value,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

**Parameters:**
- delta

- the value to add

**Returns:**
- the updated value

---

#### public final long getAndUpdate​(
LongUnaryOperator
updateFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the current value with the results of
applying the given function, returning the previous value. The
function should be side-effect-free, since it may be re-applied
when attempted updates fail due to contention among threads.

**Parameters:**
- updateFunction

- a side-effect-free function

**Returns:**
- the previous value

**Since:**
- 1.8

---

#### public final long updateAndGet​(
LongUnaryOperator
updateFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the current value with the results of
applying the given function, returning the updated value. The
function should be side-effect-free, since it may be re-applied
when attempted updates fail due to contention among threads.

**Parameters:**
- updateFunction

- a side-effect-free function

**Returns:**
- the updated value

**Since:**
- 1.8

---

#### public final long getAndAccumulate​(long x,

LongBinaryOperator
accumulatorFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the current value with the results of
applying the given function to the current and given values,
returning the previous value. The function should be
side-effect-free, since it may be re-applied when attempted
updates fail due to contention among threads. The function is
applied with the current value as its first argument, and the
given update as the second argument.

**Parameters:**
- x

- the update value
- accumulatorFunction

- a side-effect-free function of two arguments

**Returns:**
- the previous value

**Since:**
- 1.8

---

#### public final long accumulateAndGet​(long x,

LongBinaryOperator
accumulatorFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the current value with the results of
applying the given function to the current and given values,
returning the updated value. The function should be
side-effect-free, since it may be re-applied when attempted
updates fail due to contention among threads. The function is
applied with the current value as its first argument, and the
given update as the second argument.

**Parameters:**
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

Returns the String representation of the current value.

**Overrides:**
- toString

in class

Object

**Returns:**
- the String representation of the current value

---

#### public int intValue()

Returns the current value of this

AtomicLong

as an

int

after a narrowing primitive conversion,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

**Specified by:**
- intValue

in class

Number

**Returns:**
- the numeric value represented by this object after conversion
to type

int

.

**See The Java™ Language Specification :**
- 5.1.3 Narrowing Primitive Conversions

---

#### public long longValue()

Returns the current value of this

AtomicLong

as a

long

,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.
Equivalent to

get()

.

**Specified by:**
- longValue

in class

Number

**Returns:**
- the numeric value represented by this object after conversion
to type

long

.

---

#### public float floatValue()

Returns the current value of this

AtomicLong

as a

float

after a widening primitive conversion,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

**Specified by:**
- floatValue

in class

Number

**Returns:**
- the numeric value represented by this object after conversion
to type

float

.

**See The Java™ Language Specification :**
- 5.1.2 Widening Primitive Conversions

---

#### public double doubleValue()

Returns the current value of this

AtomicLong

as a

double

after a widening primitive conversion,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

**Specified by:**
- doubleValue

in class

Number

**Returns:**
- the numeric value represented by this object after conversion
to type

double

.

**See The Java™ Language Specification :**
- 5.1.2 Widening Primitive Conversions

---

#### public final long getPlain()

Returns the current value, with memory semantics of reading as if the
variable was declared non-

volatile

.

**Returns:**
- the value

**Since:**
- 9

---

#### public final void setPlain​(long newValue)

Sets the value to

newValue

, with memory semantics
of setting as if the variable was declared non-

volatile

and non-

final

.

**Parameters:**
- newValue

- the new value

**Since:**
- 9

---

#### public final long getOpaque()

Returns the current value,
with memory effects as specified by

VarHandle.getOpaque(java.lang.Object...)

.

**Returns:**
- the value

**Since:**
- 9

---

#### public final void setOpaque​(long newValue)

Sets the value to

newValue

,
with memory effects as specified by

VarHandle.setOpaque(java.lang.Object...)

.

**Parameters:**
- newValue

- the new value

**Since:**
- 9

---

#### public final long getAcquire()

Returns the current value,
with memory effects as specified by

VarHandle.getAcquire(java.lang.Object...)

.

**Returns:**
- the value

**Since:**
- 9

---

#### public final void setRelease​(long newValue)

Sets the value to

newValue

,
with memory effects as specified by

VarHandle.setRelease(java.lang.Object...)

.

**Parameters:**
- newValue

- the new value

**Since:**
- 9

---

#### public final long compareAndExchange​(long expectedValue,
long newValue)

Atomically sets the value to

newValue

if the current value,
referred to as the

witness value

,

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndExchange(java.lang.Object...)

.

**Parameters:**
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

#### public final long compareAndExchangeAcquire​(long expectedValue,
long newValue)

Atomically sets the value to

newValue

if the current value,
referred to as the

witness value

,

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndExchangeAcquire(java.lang.Object...)

.

**Parameters:**
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

#### public final long compareAndExchangeRelease​(long expectedValue,
long newValue)

Atomically sets the value to

newValue

if the current value,
referred to as the

witness value

,

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndExchangeRelease(java.lang.Object...)

.

**Parameters:**
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

#### public final boolean weakCompareAndSetVolatile​(long expectedValue,
long newValue)

Possibly atomically sets the value to

newValue

if the current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSet(java.lang.Object...)

.

**Parameters:**
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

#### public final boolean weakCompareAndSetAcquire​(long expectedValue,
long newValue)

Possibly atomically sets the value to

newValue

if the current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetAcquire(java.lang.Object...)

.

**Parameters:**
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

#### public final boolean weakCompareAndSetRelease​(long expectedValue,
long newValue)

Possibly atomically sets the value to

newValue

if the current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetRelease(java.lang.Object...)

.

**Parameters:**
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

#### Class AtomicLong

java.lang.Object

- java.lang.Number
- - java.util.concurrent.atomic.AtomicLong

java.lang.Number

- java.util.concurrent.atomic.AtomicLong

java.util.concurrent.atomic.AtomicLong

**All Implemented Interfaces:** Serializable

```java
public class
AtomicLong

extends
Number

implements
Serializable
```

A

long

value that may be updated atomically. See the

VarHandle

specification for descriptions of the properties
of atomic accesses. An

AtomicLong

is used in applications
such as atomically incremented sequence numbers, and cannot be used
as a replacement for a

Long

. However, this class
does extend

Number

to allow uniform access by tools and
utilities that deal with numerically-based classes.

**Since:** 1.5
**See Also:** Serialized Form

public class

AtomicLong

extends

Number

implements

Serializable

A

long

value that may be updated atomically. See the

VarHandle

specification for descriptions of the properties
of atomic accesses. An

AtomicLong

is used in applications
such as atomically incremented sequence numbers, and cannot be used
as a replacement for a

Long

. However, this class
does extend

Number

to allow uniform access by tools and
utilities that deal with numerically-based classes.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AtomicLong

()

Creates a new AtomicLong with initial value

0

.

AtomicLong

​(long initialValue)

Creates a new AtomicLong with the given initial value.

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

​(long x,

LongBinaryOperator

accumulatorFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the current value with the results of
applying the given function to the current and given values,
returning the updated value.

long

addAndGet

​(long delta)

Atomically adds the given value to the current value,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

long

compareAndExchange

​(long expectedValue,
long newValue)

Atomically sets the value to

newValue

if the current value,
referred to as the

witness value

,

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndExchange(java.lang.Object...)

.

long

compareAndExchangeAcquire

​(long expectedValue,
long newValue)

Atomically sets the value to

newValue

if the current value,
referred to as the

witness value

,

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndExchangeAcquire(java.lang.Object...)

.

long

compareAndExchangeRelease

​(long expectedValue,
long newValue)

Atomically sets the value to

newValue

if the current value,
referred to as the

witness value

,

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndExchangeRelease(java.lang.Object...)

.

boolean

compareAndSet

​(long expectedValue,
long newValue)

Atomically sets the value to

newValue

if the current value

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

.

long

decrementAndGet

()

Atomically decrements the current value,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

double

doubleValue

()

Returns the current value of this

AtomicLong

as a

double

after a widening primitive conversion,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

float

floatValue

()

Returns the current value of this

AtomicLong

as a

float

after a widening primitive conversion,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

long

get

()

Returns the current value,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

long

getAcquire

()

Returns the current value,
with memory effects as specified by

VarHandle.getAcquire(java.lang.Object...)

.

long

getAndAccumulate

​(long x,

LongBinaryOperator

accumulatorFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the current value with the results of
applying the given function to the current and given values,
returning the previous value.

long

getAndAdd

​(long delta)

Atomically adds the given value to the current value,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

long

getAndDecrement

()

Atomically decrements the current value,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

long

getAndIncrement

()

Atomically increments the current value,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

long

getAndSet

​(long newValue)

Atomically sets the value to

newValue

and returns the old value,
with memory effects as specified by

VarHandle.getAndSet(java.lang.Object...)

.

long

getAndUpdate

​(

LongUnaryOperator

updateFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the current value with the results of
applying the given function, returning the previous value.

long

getOpaque

()

Returns the current value,
with memory effects as specified by

VarHandle.getOpaque(java.lang.Object...)

.

long

getPlain

()

Returns the current value, with memory semantics of reading as if the
variable was declared non-

volatile

.

long

incrementAndGet

()

Atomically increments the current value,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

int

intValue

()

Returns the current value of this

AtomicLong

as an

int

after a narrowing primitive conversion,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

void

lazySet

​(long newValue)

Sets the value to

newValue

,
with memory effects as specified by

VarHandle.setRelease(java.lang.Object...)

.

long

longValue

()

Returns the current value of this

AtomicLong

as a

long

,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

void

set

​(long newValue)

Sets the value to

newValue

,
with memory effects as specified by

VarHandle.setVolatile(java.lang.Object...)

.

void

setOpaque

​(long newValue)

Sets the value to

newValue

,
with memory effects as specified by

VarHandle.setOpaque(java.lang.Object...)

.

void

setPlain

​(long newValue)

Sets the value to

newValue

, with memory semantics
of setting as if the variable was declared non-

volatile

and non-

final

.

void

setRelease

​(long newValue)

Sets the value to

newValue

,
with memory effects as specified by

VarHandle.setRelease(java.lang.Object...)

.

String

toString

()

Returns the String representation of the current value.

long

updateAndGet

​(

LongUnaryOperator

updateFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the current value with the results of
applying the given function, returning the updated value.

boolean

weakCompareAndSet

​(long expectedValue,
long newValue)

Deprecated.

This method has plain memory effects but the method
name implies volatile memory effects (see methods such as

compareAndExchange(long, long)

and

compareAndSet(long, long)

).

boolean

weakCompareAndSetAcquire

​(long expectedValue,
long newValue)

Possibly atomically sets the value to

newValue

if the current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetAcquire(java.lang.Object...)

.

boolean

weakCompareAndSetPlain

​(long expectedValue,
long newValue)

Possibly atomically sets the value to

newValue

if the current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetPlain(java.lang.Object...)

.

boolean

weakCompareAndSetRelease

​(long expectedValue,
long newValue)

Possibly atomically sets the value to

newValue

if the current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetRelease(java.lang.Object...)

.

boolean

weakCompareAndSetVolatile

​(long expectedValue,
long newValue)

Possibly atomically sets the value to

newValue

if the current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSet(java.lang.Object...)

.

- Methods declared in class java.lang.

Number

byteValue

,

shortValue

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

AtomicLong

()

Creates a new AtomicLong with initial value

0

.

AtomicLong

​(long initialValue)

Creates a new AtomicLong with the given initial value.

---

#### Constructor Summary

Creates a new AtomicLong with initial value

0

.

Creates a new AtomicLong with the given initial value.

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

​(long x,

LongBinaryOperator

accumulatorFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the current value with the results of
applying the given function to the current and given values,
returning the updated value.

long

addAndGet

​(long delta)

Atomically adds the given value to the current value,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

long

compareAndExchange

​(long expectedValue,
long newValue)

Atomically sets the value to

newValue

if the current value,
referred to as the

witness value

,

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndExchange(java.lang.Object...)

.

long

compareAndExchangeAcquire

​(long expectedValue,
long newValue)

Atomically sets the value to

newValue

if the current value,
referred to as the

witness value

,

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndExchangeAcquire(java.lang.Object...)

.

long

compareAndExchangeRelease

​(long expectedValue,
long newValue)

Atomically sets the value to

newValue

if the current value,
referred to as the

witness value

,

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndExchangeRelease(java.lang.Object...)

.

boolean

compareAndSet

​(long expectedValue,
long newValue)

Atomically sets the value to

newValue

if the current value

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

.

long

decrementAndGet

()

Atomically decrements the current value,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

double

doubleValue

()

Returns the current value of this

AtomicLong

as a

double

after a widening primitive conversion,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

float

floatValue

()

Returns the current value of this

AtomicLong

as a

float

after a widening primitive conversion,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

long

get

()

Returns the current value,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

long

getAcquire

()

Returns the current value,
with memory effects as specified by

VarHandle.getAcquire(java.lang.Object...)

.

long

getAndAccumulate

​(long x,

LongBinaryOperator

accumulatorFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the current value with the results of
applying the given function to the current and given values,
returning the previous value.

long

getAndAdd

​(long delta)

Atomically adds the given value to the current value,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

long

getAndDecrement

()

Atomically decrements the current value,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

long

getAndIncrement

()

Atomically increments the current value,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

long

getAndSet

​(long newValue)

Atomically sets the value to

newValue

and returns the old value,
with memory effects as specified by

VarHandle.getAndSet(java.lang.Object...)

.

long

getAndUpdate

​(

LongUnaryOperator

updateFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the current value with the results of
applying the given function, returning the previous value.

long

getOpaque

()

Returns the current value,
with memory effects as specified by

VarHandle.getOpaque(java.lang.Object...)

.

long

getPlain

()

Returns the current value, with memory semantics of reading as if the
variable was declared non-

volatile

.

long

incrementAndGet

()

Atomically increments the current value,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

int

intValue

()

Returns the current value of this

AtomicLong

as an

int

after a narrowing primitive conversion,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

void

lazySet

​(long newValue)

Sets the value to

newValue

,
with memory effects as specified by

VarHandle.setRelease(java.lang.Object...)

.

long

longValue

()

Returns the current value of this

AtomicLong

as a

long

,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

void

set

​(long newValue)

Sets the value to

newValue

,
with memory effects as specified by

VarHandle.setVolatile(java.lang.Object...)

.

void

setOpaque

​(long newValue)

Sets the value to

newValue

,
with memory effects as specified by

VarHandle.setOpaque(java.lang.Object...)

.

void

setPlain

​(long newValue)

Sets the value to

newValue

, with memory semantics
of setting as if the variable was declared non-

volatile

and non-

final

.

void

setRelease

​(long newValue)

Sets the value to

newValue

,
with memory effects as specified by

VarHandle.setRelease(java.lang.Object...)

.

String

toString

()

Returns the String representation of the current value.

long

updateAndGet

​(

LongUnaryOperator

updateFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the current value with the results of
applying the given function, returning the updated value.

boolean

weakCompareAndSet

​(long expectedValue,
long newValue)

Deprecated.

This method has plain memory effects but the method
name implies volatile memory effects (see methods such as

compareAndExchange(long, long)

and

compareAndSet(long, long)

).

boolean

weakCompareAndSetAcquire

​(long expectedValue,
long newValue)

Possibly atomically sets the value to

newValue

if the current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetAcquire(java.lang.Object...)

.

boolean

weakCompareAndSetPlain

​(long expectedValue,
long newValue)

Possibly atomically sets the value to

newValue

if the current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetPlain(java.lang.Object...)

.

boolean

weakCompareAndSetRelease

​(long expectedValue,
long newValue)

Possibly atomically sets the value to

newValue

if the current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetRelease(java.lang.Object...)

.

boolean

weakCompareAndSetVolatile

​(long expectedValue,
long newValue)

Possibly atomically sets the value to

newValue

if the current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSet(java.lang.Object...)

.

- Methods declared in class java.lang.

Number

byteValue

,

shortValue

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

) the current value with the results of
applying the given function to the current and given values,
returning the updated value.

Atomically adds the given value to the current value,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

Atomically sets the value to

newValue

if the current value,
referred to as the

witness value

,

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndExchange(java.lang.Object...)

.

Atomically sets the value to

newValue

if the current value,
referred to as the

witness value

,

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndExchangeAcquire(java.lang.Object...)

.

Atomically sets the value to

newValue

if the current value,
referred to as the

witness value

,

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndExchangeRelease(java.lang.Object...)

.

Atomically sets the value to

newValue

if the current value

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

.

Atomically decrements the current value,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

Returns the current value of this

AtomicLong

as a

double

after a widening primitive conversion,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

Returns the current value of this

AtomicLong

as a

float

after a widening primitive conversion,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

Returns the current value,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

Returns the current value,
with memory effects as specified by

VarHandle.getAcquire(java.lang.Object...)

.

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the current value with the results of
applying the given function to the current and given values,
returning the previous value.

Atomically increments the current value,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

Atomically sets the value to

newValue

and returns the old value,
with memory effects as specified by

VarHandle.getAndSet(java.lang.Object...)

.

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the current value with the results of
applying the given function, returning the previous value.

Returns the current value,
with memory effects as specified by

VarHandle.getOpaque(java.lang.Object...)

.

Returns the current value, with memory semantics of reading as if the
variable was declared non-

volatile

.

Returns the current value of this

AtomicLong

as an

int

after a narrowing primitive conversion,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

Sets the value to

newValue

,
with memory effects as specified by

VarHandle.setRelease(java.lang.Object...)

.

Returns the current value of this

AtomicLong

as a

long

,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

Sets the value to

newValue

,
with memory effects as specified by

VarHandle.setVolatile(java.lang.Object...)

.

Sets the value to

newValue

,
with memory effects as specified by

VarHandle.setOpaque(java.lang.Object...)

.

Sets the value to

newValue

, with memory semantics
of setting as if the variable was declared non-

volatile

and non-

final

.

Returns the String representation of the current value.

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the current value with the results of
applying the given function, returning the updated value.

Deprecated.

This method has plain memory effects but the method
name implies volatile memory effects (see methods such as

compareAndExchange(long, long)

and

compareAndSet(long, long)

).

Possibly atomically sets the value to

newValue

if the current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetAcquire(java.lang.Object...)

.

Possibly atomically sets the value to

newValue

if the current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetPlain(java.lang.Object...)

.

Possibly atomically sets the value to

newValue

if the current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetRelease(java.lang.Object...)

.

Possibly atomically sets the value to

newValue

if the current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSet(java.lang.Object...)

.

Methods declared in class java.lang.

Number

byteValue

,

shortValue

---

#### Methods declared in class java.lang. Number

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

- AtomicLong

```java
public AtomicLong​(long initialValue)
```

Creates a new AtomicLong with the given initial value.

**Parameters:** initialValue

- the initial value

- AtomicLong

```java
public AtomicLong()
```

Creates a new AtomicLong with initial value

0

.

============ METHOD DETAIL ==========

- Method Detail

- get

```java
public final long get()
```

Returns the current value,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

**Returns:** the current value

- set

```java
public final void set​(long newValue)
```

Sets the value to

newValue

,
with memory effects as specified by

VarHandle.setVolatile(java.lang.Object...)

.

**Parameters:** newValue

- the new value

- lazySet

```java
public final void lazySet​(long newValue)
```

Sets the value to

newValue

,
with memory effects as specified by

VarHandle.setRelease(java.lang.Object...)

.

**Parameters:** newValue

- the new value
**Since:** 1.6

- getAndSet

```java
public final long getAndSet​(long newValue)
```

Atomically sets the value to

newValue

and returns the old value,
with memory effects as specified by

VarHandle.getAndSet(java.lang.Object...)

.

**Parameters:** newValue

- the new value
**Returns:** the previous value

- compareAndSet

```java
public final boolean compareAndSet​(long expectedValue,
long newValue)
```

Atomically sets the value to

newValue

if the current value

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

.

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
public final boolean weakCompareAndSet​(long expectedValue,
long newValue)
```

Deprecated.

This method has plain memory effects but the method
name implies volatile memory effects (see methods such as

compareAndExchange(long, long)

and

compareAndSet(long, long)

). To avoid
confusion over plain or volatile memory effects it is recommended that
the method

weakCompareAndSetPlain(long, long)

be used instead.

Possibly atomically sets the value to

newValue

if the current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetPlain(java.lang.Object...)

.

**Parameters:** expectedValue

- the expected value
**Parameters:** newValue

- the new value
**Returns:** true

if successful
**See Also:** weakCompareAndSetPlain(long, long)

- weakCompareAndSetPlain

```java
public final boolean weakCompareAndSetPlain​(long expectedValue,
long newValue)
```

Possibly atomically sets the value to

newValue

if the current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetPlain(java.lang.Object...)

.

**Parameters:** expectedValue

- the expected value
**Parameters:** newValue

- the new value
**Returns:** true

if successful
**Since:** 9

- getAndIncrement

```java
public final long getAndIncrement()
```

Atomically increments the current value,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

Equivalent to

getAndAdd(1)

.

**Returns:** the previous value

- getAndDecrement

```java
public final long getAndDecrement()
```

Atomically decrements the current value,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

Equivalent to

getAndAdd(-1)

.

**Returns:** the previous value

- getAndAdd

```java
public final long getAndAdd​(long delta)
```

Atomically adds the given value to the current value,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

**Parameters:** delta

- the value to add
**Returns:** the previous value

- incrementAndGet

```java
public final long incrementAndGet()
```

Atomically increments the current value,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

Equivalent to

addAndGet(1)

.

**Returns:** the updated value

- decrementAndGet

```java
public final long decrementAndGet()
```

Atomically decrements the current value,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

Equivalent to

addAndGet(-1)

.

**Returns:** the updated value

- addAndGet

```java
public final long addAndGet​(long delta)
```

Atomically adds the given value to the current value,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

**Parameters:** delta

- the value to add
**Returns:** the updated value

- getAndUpdate

```java
public final long getAndUpdate​(
LongUnaryOperator
updateFunction)
```

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the current value with the results of
applying the given function, returning the previous value. The
function should be side-effect-free, since it may be re-applied
when attempted updates fail due to contention among threads.

**Parameters:** updateFunction

- a side-effect-free function
**Returns:** the previous value
**Since:** 1.8

- updateAndGet

```java
public final long updateAndGet​(
LongUnaryOperator
updateFunction)
```

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the current value with the results of
applying the given function, returning the updated value. The
function should be side-effect-free, since it may be re-applied
when attempted updates fail due to contention among threads.

**Parameters:** updateFunction

- a side-effect-free function
**Returns:** the updated value
**Since:** 1.8

- getAndAccumulate

```java
public final long getAndAccumulate​(long x,

LongBinaryOperator
accumulatorFunction)
```

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the current value with the results of
applying the given function to the current and given values,
returning the previous value. The function should be
side-effect-free, since it may be re-applied when attempted
updates fail due to contention among threads. The function is
applied with the current value as its first argument, and the
given update as the second argument.

**Parameters:** x

- the update value
**Parameters:** accumulatorFunction

- a side-effect-free function of two arguments
**Returns:** the previous value
**Since:** 1.8

- accumulateAndGet

```java
public final long accumulateAndGet​(long x,

LongBinaryOperator
accumulatorFunction)
```

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the current value with the results of
applying the given function to the current and given values,
returning the updated value. The function should be
side-effect-free, since it may be re-applied when attempted
updates fail due to contention among threads. The function is
applied with the current value as its first argument, and the
given update as the second argument.

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

Returns the String representation of the current value.

**Overrides:** toString

in class

Object
**Returns:** the String representation of the current value

- intValue

```java
public int intValue()
```

Returns the current value of this

AtomicLong

as an

int

after a narrowing primitive conversion,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

**Specified by:** intValue

in class

Number
**Returns:** the numeric value represented by this object after conversion
to type

int

.
**See The Java™ Language Specification :** 5.1.3 Narrowing Primitive Conversions

- longValue

```java
public long longValue()
```

Returns the current value of this

AtomicLong

as a

long

,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.
Equivalent to

get()

.

**Specified by:** longValue

in class

Number
**Returns:** the numeric value represented by this object after conversion
to type

long

.

- floatValue

```java
public float floatValue()
```

Returns the current value of this

AtomicLong

as a

float

after a widening primitive conversion,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

**Specified by:** floatValue

in class

Number
**Returns:** the numeric value represented by this object after conversion
to type

float

.
**See The Java™ Language Specification :** 5.1.2 Widening Primitive Conversions

- doubleValue

```java
public double doubleValue()
```

Returns the current value of this

AtomicLong

as a

double

after a widening primitive conversion,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

**Specified by:** doubleValue

in class

Number
**Returns:** the numeric value represented by this object after conversion
to type

double

.
**See The Java™ Language Specification :** 5.1.2 Widening Primitive Conversions

- getPlain

```java
public final long getPlain()
```

Returns the current value, with memory semantics of reading as if the
variable was declared non-

volatile

.

**Returns:** the value
**Since:** 9

- setPlain

```java
public final void setPlain​(long newValue)
```

Sets the value to

newValue

, with memory semantics
of setting as if the variable was declared non-

volatile

and non-

final

.

**Parameters:** newValue

- the new value
**Since:** 9

- getOpaque

```java
public final long getOpaque()
```

Returns the current value,
with memory effects as specified by

VarHandle.getOpaque(java.lang.Object...)

.

**Returns:** the value
**Since:** 9

- setOpaque

```java
public final void setOpaque​(long newValue)
```

Sets the value to

newValue

,
with memory effects as specified by

VarHandle.setOpaque(java.lang.Object...)

.

**Parameters:** newValue

- the new value
**Since:** 9

- getAcquire

```java
public final long getAcquire()
```

Returns the current value,
with memory effects as specified by

VarHandle.getAcquire(java.lang.Object...)

.

**Returns:** the value
**Since:** 9

- setRelease

```java
public final void setRelease​(long newValue)
```

Sets the value to

newValue

,
with memory effects as specified by

VarHandle.setRelease(java.lang.Object...)

.

**Parameters:** newValue

- the new value
**Since:** 9

- compareAndExchange

```java
public final long compareAndExchange​(long expectedValue,
long newValue)
```

Atomically sets the value to

newValue

if the current value,
referred to as the

witness value

,

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndExchange(java.lang.Object...)

.

**Parameters:** expectedValue

- the expected value
**Parameters:** newValue

- the new value
**Returns:** the witness value, which will be the same as the
expected value if successful
**Since:** 9

- compareAndExchangeAcquire

```java
public final long compareAndExchangeAcquire​(long expectedValue,
long newValue)
```

Atomically sets the value to

newValue

if the current value,
referred to as the

witness value

,

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndExchangeAcquire(java.lang.Object...)

.

**Parameters:** expectedValue

- the expected value
**Parameters:** newValue

- the new value
**Returns:** the witness value, which will be the same as the
expected value if successful
**Since:** 9

- compareAndExchangeRelease

```java
public final long compareAndExchangeRelease​(long expectedValue,
long newValue)
```

Atomically sets the value to

newValue

if the current value,
referred to as the

witness value

,

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndExchangeRelease(java.lang.Object...)

.

**Parameters:** expectedValue

- the expected value
**Parameters:** newValue

- the new value
**Returns:** the witness value, which will be the same as the
expected value if successful
**Since:** 9

- weakCompareAndSetVolatile

```java
public final boolean weakCompareAndSetVolatile​(long expectedValue,
long newValue)
```

Possibly atomically sets the value to

newValue

if the current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSet(java.lang.Object...)

.

**Parameters:** expectedValue

- the expected value
**Parameters:** newValue

- the new value
**Returns:** true

if successful
**Since:** 9

- weakCompareAndSetAcquire

```java
public final boolean weakCompareAndSetAcquire​(long expectedValue,
long newValue)
```

Possibly atomically sets the value to

newValue

if the current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetAcquire(java.lang.Object...)

.

**Parameters:** expectedValue

- the expected value
**Parameters:** newValue

- the new value
**Returns:** true

if successful
**Since:** 9

- weakCompareAndSetRelease

```java
public final boolean weakCompareAndSetRelease​(long expectedValue,
long newValue)
```

Possibly atomically sets the value to

newValue

if the current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetRelease(java.lang.Object...)

.

**Parameters:** expectedValue

- the expected value
**Parameters:** newValue

- the new value
**Returns:** true

if successful
**Since:** 9

Constructor Detail

- AtomicLong

```java
public AtomicLong​(long initialValue)
```

Creates a new AtomicLong with the given initial value.

**Parameters:** initialValue

- the initial value

- AtomicLong

```java
public AtomicLong()
```

Creates a new AtomicLong with initial value

0

.

---

#### Constructor Detail

AtomicLong

```java
public AtomicLong​(long initialValue)
```

Creates a new AtomicLong with the given initial value.

**Parameters:** initialValue

- the initial value

---

#### AtomicLong

public AtomicLong​(long initialValue)

Creates a new AtomicLong with the given initial value.

AtomicLong

```java
public AtomicLong()
```

Creates a new AtomicLong with initial value

0

.

---

#### AtomicLong

public AtomicLong()

Creates a new AtomicLong with initial value

0

.

Method Detail

- get

```java
public final long get()
```

Returns the current value,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

**Returns:** the current value

- set

```java
public final void set​(long newValue)
```

Sets the value to

newValue

,
with memory effects as specified by

VarHandle.setVolatile(java.lang.Object...)

.

**Parameters:** newValue

- the new value

- lazySet

```java
public final void lazySet​(long newValue)
```

Sets the value to

newValue

,
with memory effects as specified by

VarHandle.setRelease(java.lang.Object...)

.

**Parameters:** newValue

- the new value
**Since:** 1.6

- getAndSet

```java
public final long getAndSet​(long newValue)
```

Atomically sets the value to

newValue

and returns the old value,
with memory effects as specified by

VarHandle.getAndSet(java.lang.Object...)

.

**Parameters:** newValue

- the new value
**Returns:** the previous value

- compareAndSet

```java
public final boolean compareAndSet​(long expectedValue,
long newValue)
```

Atomically sets the value to

newValue

if the current value

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

.

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
public final boolean weakCompareAndSet​(long expectedValue,
long newValue)
```

Deprecated.

This method has plain memory effects but the method
name implies volatile memory effects (see methods such as

compareAndExchange(long, long)

and

compareAndSet(long, long)

). To avoid
confusion over plain or volatile memory effects it is recommended that
the method

weakCompareAndSetPlain(long, long)

be used instead.

Possibly atomically sets the value to

newValue

if the current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetPlain(java.lang.Object...)

.

**Parameters:** expectedValue

- the expected value
**Parameters:** newValue

- the new value
**Returns:** true

if successful
**See Also:** weakCompareAndSetPlain(long, long)

- weakCompareAndSetPlain

```java
public final boolean weakCompareAndSetPlain​(long expectedValue,
long newValue)
```

Possibly atomically sets the value to

newValue

if the current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetPlain(java.lang.Object...)

.

**Parameters:** expectedValue

- the expected value
**Parameters:** newValue

- the new value
**Returns:** true

if successful
**Since:** 9

- getAndIncrement

```java
public final long getAndIncrement()
```

Atomically increments the current value,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

Equivalent to

getAndAdd(1)

.

**Returns:** the previous value

- getAndDecrement

```java
public final long getAndDecrement()
```

Atomically decrements the current value,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

Equivalent to

getAndAdd(-1)

.

**Returns:** the previous value

- getAndAdd

```java
public final long getAndAdd​(long delta)
```

Atomically adds the given value to the current value,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

**Parameters:** delta

- the value to add
**Returns:** the previous value

- incrementAndGet

```java
public final long incrementAndGet()
```

Atomically increments the current value,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

Equivalent to

addAndGet(1)

.

**Returns:** the updated value

- decrementAndGet

```java
public final long decrementAndGet()
```

Atomically decrements the current value,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

Equivalent to

addAndGet(-1)

.

**Returns:** the updated value

- addAndGet

```java
public final long addAndGet​(long delta)
```

Atomically adds the given value to the current value,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

**Parameters:** delta

- the value to add
**Returns:** the updated value

- getAndUpdate

```java
public final long getAndUpdate​(
LongUnaryOperator
updateFunction)
```

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the current value with the results of
applying the given function, returning the previous value. The
function should be side-effect-free, since it may be re-applied
when attempted updates fail due to contention among threads.

**Parameters:** updateFunction

- a side-effect-free function
**Returns:** the previous value
**Since:** 1.8

- updateAndGet

```java
public final long updateAndGet​(
LongUnaryOperator
updateFunction)
```

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the current value with the results of
applying the given function, returning the updated value. The
function should be side-effect-free, since it may be re-applied
when attempted updates fail due to contention among threads.

**Parameters:** updateFunction

- a side-effect-free function
**Returns:** the updated value
**Since:** 1.8

- getAndAccumulate

```java
public final long getAndAccumulate​(long x,

LongBinaryOperator
accumulatorFunction)
```

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the current value with the results of
applying the given function to the current and given values,
returning the previous value. The function should be
side-effect-free, since it may be re-applied when attempted
updates fail due to contention among threads. The function is
applied with the current value as its first argument, and the
given update as the second argument.

**Parameters:** x

- the update value
**Parameters:** accumulatorFunction

- a side-effect-free function of two arguments
**Returns:** the previous value
**Since:** 1.8

- accumulateAndGet

```java
public final long accumulateAndGet​(long x,

LongBinaryOperator
accumulatorFunction)
```

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the current value with the results of
applying the given function to the current and given values,
returning the updated value. The function should be
side-effect-free, since it may be re-applied when attempted
updates fail due to contention among threads. The function is
applied with the current value as its first argument, and the
given update as the second argument.

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

Returns the String representation of the current value.

**Overrides:** toString

in class

Object
**Returns:** the String representation of the current value

- intValue

```java
public int intValue()
```

Returns the current value of this

AtomicLong

as an

int

after a narrowing primitive conversion,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

**Specified by:** intValue

in class

Number
**Returns:** the numeric value represented by this object after conversion
to type

int

.
**See The Java™ Language Specification :** 5.1.3 Narrowing Primitive Conversions

- longValue

```java
public long longValue()
```

Returns the current value of this

AtomicLong

as a

long

,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.
Equivalent to

get()

.

**Specified by:** longValue

in class

Number
**Returns:** the numeric value represented by this object after conversion
to type

long

.

- floatValue

```java
public float floatValue()
```

Returns the current value of this

AtomicLong

as a

float

after a widening primitive conversion,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

**Specified by:** floatValue

in class

Number
**Returns:** the numeric value represented by this object after conversion
to type

float

.
**See The Java™ Language Specification :** 5.1.2 Widening Primitive Conversions

- doubleValue

```java
public double doubleValue()
```

Returns the current value of this

AtomicLong

as a

double

after a widening primitive conversion,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

**Specified by:** doubleValue

in class

Number
**Returns:** the numeric value represented by this object after conversion
to type

double

.
**See The Java™ Language Specification :** 5.1.2 Widening Primitive Conversions

- getPlain

```java
public final long getPlain()
```

Returns the current value, with memory semantics of reading as if the
variable was declared non-

volatile

.

**Returns:** the value
**Since:** 9

- setPlain

```java
public final void setPlain​(long newValue)
```

Sets the value to

newValue

, with memory semantics
of setting as if the variable was declared non-

volatile

and non-

final

.

**Parameters:** newValue

- the new value
**Since:** 9

- getOpaque

```java
public final long getOpaque()
```

Returns the current value,
with memory effects as specified by

VarHandle.getOpaque(java.lang.Object...)

.

**Returns:** the value
**Since:** 9

- setOpaque

```java
public final void setOpaque​(long newValue)
```

Sets the value to

newValue

,
with memory effects as specified by

VarHandle.setOpaque(java.lang.Object...)

.

**Parameters:** newValue

- the new value
**Since:** 9

- getAcquire

```java
public final long getAcquire()
```

Returns the current value,
with memory effects as specified by

VarHandle.getAcquire(java.lang.Object...)

.

**Returns:** the value
**Since:** 9

- setRelease

```java
public final void setRelease​(long newValue)
```

Sets the value to

newValue

,
with memory effects as specified by

VarHandle.setRelease(java.lang.Object...)

.

**Parameters:** newValue

- the new value
**Since:** 9

- compareAndExchange

```java
public final long compareAndExchange​(long expectedValue,
long newValue)
```

Atomically sets the value to

newValue

if the current value,
referred to as the

witness value

,

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndExchange(java.lang.Object...)

.

**Parameters:** expectedValue

- the expected value
**Parameters:** newValue

- the new value
**Returns:** the witness value, which will be the same as the
expected value if successful
**Since:** 9

- compareAndExchangeAcquire

```java
public final long compareAndExchangeAcquire​(long expectedValue,
long newValue)
```

Atomically sets the value to

newValue

if the current value,
referred to as the

witness value

,

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndExchangeAcquire(java.lang.Object...)

.

**Parameters:** expectedValue

- the expected value
**Parameters:** newValue

- the new value
**Returns:** the witness value, which will be the same as the
expected value if successful
**Since:** 9

- compareAndExchangeRelease

```java
public final long compareAndExchangeRelease​(long expectedValue,
long newValue)
```

Atomically sets the value to

newValue

if the current value,
referred to as the

witness value

,

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndExchangeRelease(java.lang.Object...)

.

**Parameters:** expectedValue

- the expected value
**Parameters:** newValue

- the new value
**Returns:** the witness value, which will be the same as the
expected value if successful
**Since:** 9

- weakCompareAndSetVolatile

```java
public final boolean weakCompareAndSetVolatile​(long expectedValue,
long newValue)
```

Possibly atomically sets the value to

newValue

if the current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSet(java.lang.Object...)

.

**Parameters:** expectedValue

- the expected value
**Parameters:** newValue

- the new value
**Returns:** true

if successful
**Since:** 9

- weakCompareAndSetAcquire

```java
public final boolean weakCompareAndSetAcquire​(long expectedValue,
long newValue)
```

Possibly atomically sets the value to

newValue

if the current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetAcquire(java.lang.Object...)

.

**Parameters:** expectedValue

- the expected value
**Parameters:** newValue

- the new value
**Returns:** true

if successful
**Since:** 9

- weakCompareAndSetRelease

```java
public final boolean weakCompareAndSetRelease​(long expectedValue,
long newValue)
```

Possibly atomically sets the value to

newValue

if the current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetRelease(java.lang.Object...)

.

**Parameters:** expectedValue

- the expected value
**Parameters:** newValue

- the new value
**Returns:** true

if successful
**Since:** 9

---

#### Method Detail

get

```java
public final long get()
```

Returns the current value,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

**Returns:** the current value

---

#### get

public final long get()

Returns the current value,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

set

```java
public final void set​(long newValue)
```

Sets the value to

newValue

,
with memory effects as specified by

VarHandle.setVolatile(java.lang.Object...)

.

**Parameters:** newValue

- the new value

---

#### set

public final void set​(long newValue)

Sets the value to

newValue

,
with memory effects as specified by

VarHandle.setVolatile(java.lang.Object...)

.

lazySet

```java
public final void lazySet​(long newValue)
```

Sets the value to

newValue

,
with memory effects as specified by

VarHandle.setRelease(java.lang.Object...)

.

**Parameters:** newValue

- the new value
**Since:** 1.6

---

#### lazySet

public final void lazySet​(long newValue)

Sets the value to

newValue

,
with memory effects as specified by

VarHandle.setRelease(java.lang.Object...)

.

getAndSet

```java
public final long getAndSet​(long newValue)
```

Atomically sets the value to

newValue

and returns the old value,
with memory effects as specified by

VarHandle.getAndSet(java.lang.Object...)

.

**Parameters:** newValue

- the new value
**Returns:** the previous value

---

#### getAndSet

public final long getAndSet​(long newValue)

Atomically sets the value to

newValue

and returns the old value,
with memory effects as specified by

VarHandle.getAndSet(java.lang.Object...)

.

compareAndSet

```java
public final boolean compareAndSet​(long expectedValue,
long newValue)
```

Atomically sets the value to

newValue

if the current value

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

.

**Parameters:** expectedValue

- the expected value
**Parameters:** newValue

- the new value
**Returns:** true

if successful. False return indicates that
the actual value was not equal to the expected value.

---

#### compareAndSet

public final boolean compareAndSet​(long expectedValue,
long newValue)

Atomically sets the value to

newValue

if the current value

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
public final boolean weakCompareAndSet​(long expectedValue,
long newValue)
```

Deprecated.

This method has plain memory effects but the method
name implies volatile memory effects (see methods such as

compareAndExchange(long, long)

and

compareAndSet(long, long)

). To avoid
confusion over plain or volatile memory effects it is recommended that
the method

weakCompareAndSetPlain(long, long)

be used instead.

Possibly atomically sets the value to

newValue

if the current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetPlain(java.lang.Object...)

.

**Parameters:** expectedValue

- the expected value
**Parameters:** newValue

- the new value
**Returns:** true

if successful
**See Also:** weakCompareAndSetPlain(long, long)

---

#### weakCompareAndSet

@Deprecated

(

since

="9")
public final boolean weakCompareAndSet​(long expectedValue,
long newValue)

Possibly atomically sets the value to

newValue

if the current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetPlain(java.lang.Object...)

.

weakCompareAndSetPlain

```java
public final boolean weakCompareAndSetPlain​(long expectedValue,
long newValue)
```

Possibly atomically sets the value to

newValue

if the current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetPlain(java.lang.Object...)

.

**Parameters:** expectedValue

- the expected value
**Parameters:** newValue

- the new value
**Returns:** true

if successful
**Since:** 9

---

#### weakCompareAndSetPlain

public final boolean weakCompareAndSetPlain​(long expectedValue,
long newValue)

Possibly atomically sets the value to

newValue

if the current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetPlain(java.lang.Object...)

.

getAndIncrement

```java
public final long getAndIncrement()
```

Atomically increments the current value,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

Equivalent to

getAndAdd(1)

.

**Returns:** the previous value

---

#### getAndIncrement

public final long getAndIncrement()

Atomically increments the current value,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

Equivalent to

getAndAdd(1)

.

Equivalent to

getAndAdd(1)

.

getAndDecrement

```java
public final long getAndDecrement()
```

Atomically decrements the current value,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

Equivalent to

getAndAdd(-1)

.

**Returns:** the previous value

---

#### getAndDecrement

public final long getAndDecrement()

Atomically decrements the current value,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

Equivalent to

getAndAdd(-1)

.

Equivalent to

getAndAdd(-1)

.

getAndAdd

```java
public final long getAndAdd​(long delta)
```

Atomically adds the given value to the current value,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

**Parameters:** delta

- the value to add
**Returns:** the previous value

---

#### getAndAdd

public final long getAndAdd​(long delta)

Atomically adds the given value to the current value,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

incrementAndGet

```java
public final long incrementAndGet()
```

Atomically increments the current value,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

Equivalent to

addAndGet(1)

.

**Returns:** the updated value

---

#### incrementAndGet

public final long incrementAndGet()

Atomically increments the current value,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

Equivalent to

addAndGet(1)

.

Equivalent to

addAndGet(1)

.

decrementAndGet

```java
public final long decrementAndGet()
```

Atomically decrements the current value,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

Equivalent to

addAndGet(-1)

.

**Returns:** the updated value

---

#### decrementAndGet

public final long decrementAndGet()

Atomically decrements the current value,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

Equivalent to

addAndGet(-1)

.

Equivalent to

addAndGet(-1)

.

addAndGet

```java
public final long addAndGet​(long delta)
```

Atomically adds the given value to the current value,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

**Parameters:** delta

- the value to add
**Returns:** the updated value

---

#### addAndGet

public final long addAndGet​(long delta)

Atomically adds the given value to the current value,
with memory effects as specified by

VarHandle.getAndAdd(java.lang.Object...)

.

getAndUpdate

```java
public final long getAndUpdate​(
LongUnaryOperator
updateFunction)
```

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the current value with the results of
applying the given function, returning the previous value. The
function should be side-effect-free, since it may be re-applied
when attempted updates fail due to contention among threads.

**Parameters:** updateFunction

- a side-effect-free function
**Returns:** the previous value
**Since:** 1.8

---

#### getAndUpdate

public final long getAndUpdate​(

LongUnaryOperator

updateFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the current value with the results of
applying the given function, returning the previous value. The
function should be side-effect-free, since it may be re-applied
when attempted updates fail due to contention among threads.

updateAndGet

```java
public final long updateAndGet​(
LongUnaryOperator
updateFunction)
```

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the current value with the results of
applying the given function, returning the updated value. The
function should be side-effect-free, since it may be re-applied
when attempted updates fail due to contention among threads.

**Parameters:** updateFunction

- a side-effect-free function
**Returns:** the updated value
**Since:** 1.8

---

#### updateAndGet

public final long updateAndGet​(

LongUnaryOperator

updateFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the current value with the results of
applying the given function, returning the updated value. The
function should be side-effect-free, since it may be re-applied
when attempted updates fail due to contention among threads.

getAndAccumulate

```java
public final long getAndAccumulate​(long x,

LongBinaryOperator
accumulatorFunction)
```

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the current value with the results of
applying the given function to the current and given values,
returning the previous value. The function should be
side-effect-free, since it may be re-applied when attempted
updates fail due to contention among threads. The function is
applied with the current value as its first argument, and the
given update as the second argument.

**Parameters:** x

- the update value
**Parameters:** accumulatorFunction

- a side-effect-free function of two arguments
**Returns:** the previous value
**Since:** 1.8

---

#### getAndAccumulate

public final long getAndAccumulate​(long x,

LongBinaryOperator

accumulatorFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the current value with the results of
applying the given function to the current and given values,
returning the previous value. The function should be
side-effect-free, since it may be re-applied when attempted
updates fail due to contention among threads. The function is
applied with the current value as its first argument, and the
given update as the second argument.

accumulateAndGet

```java
public final long accumulateAndGet​(long x,

LongBinaryOperator
accumulatorFunction)
```

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the current value with the results of
applying the given function to the current and given values,
returning the updated value. The function should be
side-effect-free, since it may be re-applied when attempted
updates fail due to contention among threads. The function is
applied with the current value as its first argument, and the
given update as the second argument.

**Parameters:** x

- the update value
**Parameters:** accumulatorFunction

- a side-effect-free function of two arguments
**Returns:** the updated value
**Since:** 1.8

---

#### accumulateAndGet

public final long accumulateAndGet​(long x,

LongBinaryOperator

accumulatorFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the current value with the results of
applying the given function to the current and given values,
returning the updated value. The function should be
side-effect-free, since it may be re-applied when attempted
updates fail due to contention among threads. The function is
applied with the current value as its first argument, and the
given update as the second argument.

toString

```java
public
String
toString()
```

Returns the String representation of the current value.

**Overrides:** toString

in class

Object
**Returns:** the String representation of the current value

---

#### toString

public

String

toString()

Returns the String representation of the current value.

intValue

```java
public int intValue()
```

Returns the current value of this

AtomicLong

as an

int

after a narrowing primitive conversion,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

**Specified by:** intValue

in class

Number
**Returns:** the numeric value represented by this object after conversion
to type

int

.
**See The Java™ Language Specification :** 5.1.3 Narrowing Primitive Conversions

---

#### intValue

public int intValue()

Returns the current value of this

AtomicLong

as an

int

after a narrowing primitive conversion,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

longValue

```java
public long longValue()
```

Returns the current value of this

AtomicLong

as a

long

,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.
Equivalent to

get()

.

**Specified by:** longValue

in class

Number
**Returns:** the numeric value represented by this object after conversion
to type

long

.

---

#### longValue

public long longValue()

Returns the current value of this

AtomicLong

as a

long

,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.
Equivalent to

get()

.

floatValue

```java
public float floatValue()
```

Returns the current value of this

AtomicLong

as a

float

after a widening primitive conversion,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

**Specified by:** floatValue

in class

Number
**Returns:** the numeric value represented by this object after conversion
to type

float

.
**See The Java™ Language Specification :** 5.1.2 Widening Primitive Conversions

---

#### floatValue

public float floatValue()

Returns the current value of this

AtomicLong

as a

float

after a widening primitive conversion,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

doubleValue

```java
public double doubleValue()
```

Returns the current value of this

AtomicLong

as a

double

after a widening primitive conversion,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

**Specified by:** doubleValue

in class

Number
**Returns:** the numeric value represented by this object after conversion
to type

double

.
**See The Java™ Language Specification :** 5.1.2 Widening Primitive Conversions

---

#### doubleValue

public double doubleValue()

Returns the current value of this

AtomicLong

as a

double

after a widening primitive conversion,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

getPlain

```java
public final long getPlain()
```

Returns the current value, with memory semantics of reading as if the
variable was declared non-

volatile

.

**Returns:** the value
**Since:** 9

---

#### getPlain

public final long getPlain()

Returns the current value, with memory semantics of reading as if the
variable was declared non-

volatile

.

setPlain

```java
public final void setPlain​(long newValue)
```

Sets the value to

newValue

, with memory semantics
of setting as if the variable was declared non-

volatile

and non-

final

.

**Parameters:** newValue

- the new value
**Since:** 9

---

#### setPlain

public final void setPlain​(long newValue)

Sets the value to

newValue

, with memory semantics
of setting as if the variable was declared non-

volatile

and non-

final

.

getOpaque

```java
public final long getOpaque()
```

Returns the current value,
with memory effects as specified by

VarHandle.getOpaque(java.lang.Object...)

.

**Returns:** the value
**Since:** 9

---

#### getOpaque

public final long getOpaque()

Returns the current value,
with memory effects as specified by

VarHandle.getOpaque(java.lang.Object...)

.

setOpaque

```java
public final void setOpaque​(long newValue)
```

Sets the value to

newValue

,
with memory effects as specified by

VarHandle.setOpaque(java.lang.Object...)

.

**Parameters:** newValue

- the new value
**Since:** 9

---

#### setOpaque

public final void setOpaque​(long newValue)

Sets the value to

newValue

,
with memory effects as specified by

VarHandle.setOpaque(java.lang.Object...)

.

getAcquire

```java
public final long getAcquire()
```

Returns the current value,
with memory effects as specified by

VarHandle.getAcquire(java.lang.Object...)

.

**Returns:** the value
**Since:** 9

---

#### getAcquire

public final long getAcquire()

Returns the current value,
with memory effects as specified by

VarHandle.getAcquire(java.lang.Object...)

.

setRelease

```java
public final void setRelease​(long newValue)
```

Sets the value to

newValue

,
with memory effects as specified by

VarHandle.setRelease(java.lang.Object...)

.

**Parameters:** newValue

- the new value
**Since:** 9

---

#### setRelease

public final void setRelease​(long newValue)

Sets the value to

newValue

,
with memory effects as specified by

VarHandle.setRelease(java.lang.Object...)

.

compareAndExchange

```java
public final long compareAndExchange​(long expectedValue,
long newValue)
```

Atomically sets the value to

newValue

if the current value,
referred to as the

witness value

,

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndExchange(java.lang.Object...)

.

**Parameters:** expectedValue

- the expected value
**Parameters:** newValue

- the new value
**Returns:** the witness value, which will be the same as the
expected value if successful
**Since:** 9

---

#### compareAndExchange

public final long compareAndExchange​(long expectedValue,
long newValue)

Atomically sets the value to

newValue

if the current value,
referred to as the

witness value

,

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndExchange(java.lang.Object...)

.

compareAndExchangeAcquire

```java
public final long compareAndExchangeAcquire​(long expectedValue,
long newValue)
```

Atomically sets the value to

newValue

if the current value,
referred to as the

witness value

,

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndExchangeAcquire(java.lang.Object...)

.

**Parameters:** expectedValue

- the expected value
**Parameters:** newValue

- the new value
**Returns:** the witness value, which will be the same as the
expected value if successful
**Since:** 9

---

#### compareAndExchangeAcquire

public final long compareAndExchangeAcquire​(long expectedValue,
long newValue)

Atomically sets the value to

newValue

if the current value,
referred to as the

witness value

,

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndExchangeAcquire(java.lang.Object...)

.

compareAndExchangeRelease

```java
public final long compareAndExchangeRelease​(long expectedValue,
long newValue)
```

Atomically sets the value to

newValue

if the current value,
referred to as the

witness value

,

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndExchangeRelease(java.lang.Object...)

.

**Parameters:** expectedValue

- the expected value
**Parameters:** newValue

- the new value
**Returns:** the witness value, which will be the same as the
expected value if successful
**Since:** 9

---

#### compareAndExchangeRelease

public final long compareAndExchangeRelease​(long expectedValue,
long newValue)

Atomically sets the value to

newValue

if the current value,
referred to as the

witness value

,

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndExchangeRelease(java.lang.Object...)

.

weakCompareAndSetVolatile

```java
public final boolean weakCompareAndSetVolatile​(long expectedValue,
long newValue)
```

Possibly atomically sets the value to

newValue

if the current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSet(java.lang.Object...)

.

**Parameters:** expectedValue

- the expected value
**Parameters:** newValue

- the new value
**Returns:** true

if successful
**Since:** 9

---

#### weakCompareAndSetVolatile

public final boolean weakCompareAndSetVolatile​(long expectedValue,
long newValue)

Possibly atomically sets the value to

newValue

if the current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSet(java.lang.Object...)

.

weakCompareAndSetAcquire

```java
public final boolean weakCompareAndSetAcquire​(long expectedValue,
long newValue)
```

Possibly atomically sets the value to

newValue

if the current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetAcquire(java.lang.Object...)

.

**Parameters:** expectedValue

- the expected value
**Parameters:** newValue

- the new value
**Returns:** true

if successful
**Since:** 9

---

#### weakCompareAndSetAcquire

public final boolean weakCompareAndSetAcquire​(long expectedValue,
long newValue)

Possibly atomically sets the value to

newValue

if the current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetAcquire(java.lang.Object...)

.

weakCompareAndSetRelease

```java
public final boolean weakCompareAndSetRelease​(long expectedValue,
long newValue)
```

Possibly atomically sets the value to

newValue

if the current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetRelease(java.lang.Object...)

.

**Parameters:** expectedValue

- the expected value
**Parameters:** newValue

- the new value
**Returns:** true

if successful
**Since:** 9

---

#### weakCompareAndSetRelease

public final boolean weakCompareAndSetRelease​(long expectedValue,
long newValue)

Possibly atomically sets the value to

newValue

if the current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetRelease(java.lang.Object...)

.

---

