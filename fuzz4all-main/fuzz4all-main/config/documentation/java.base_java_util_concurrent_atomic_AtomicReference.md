# Class AtomicReference<V>

**Source:** `java.base\java\util\concurrent\atomic\AtomicReference.html`

### Class Description

```java
public class
AtomicReference<V>

extends
Object

implements
Serializable
```

An object reference that may be updated atomically. See the

VarHandle

specification for descriptions of the properties of
atomic accesses.

**Type Parameters:** V

- The type of object referred to by this reference

---

### Field Details

*No entries found.*

### Constructor Details

#### public AtomicReference​(
V
initialValue)

Creates a new AtomicReference with the given initial value.

**Parameters:**
- initialValue

- the initial value

---

#### public AtomicReference()

Creates a new AtomicReference with null initial value.

---

### Method Details

#### public final
V
get()

Returns the current value,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

**Returns:**
- the current value

---

#### public final void set​(
V
newValue)

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

#### public final void lazySet​(
V
newValue)

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

#### public final boolean compareAndSet​(
V
expectedValue,

V
newValue)

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
public final boolean weakCompareAndSet​(
V
expectedValue,

V
newValue)

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
- weakCompareAndSetPlain(V, V)

---

#### public final boolean weakCompareAndSetPlain​(
V
expectedValue,

V
newValue)

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

#### public final
V
getAndSet​(
V
newValue)

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

#### public final
V
getAndUpdate​(
UnaryOperator
<
V
> updateFunction)

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

#### public final
V
updateAndGet​(
UnaryOperator
<
V
> updateFunction)

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

#### public final
V
getAndAccumulate​(
V
x,

BinaryOperator
<
V
> accumulatorFunction)

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

#### public final
V
accumulateAndGet​(
V
x,

BinaryOperator
<
V
> accumulatorFunction)

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

#### public final
V
getPlain()

Returns the current value, with memory semantics of reading as
if the variable was declared non-

volatile

.

**Returns:**
- the value

**Since:**
- 9

---

#### public final void setPlain​(
V
newValue)

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

#### public final
V
getOpaque()

Returns the current value,
with memory effects as specified by

VarHandle.getOpaque(java.lang.Object...)

.

**Returns:**
- the value

**Since:**
- 9

---

#### public final void setOpaque​(
V
newValue)

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

#### public final
V
getAcquire()

Returns the current value,
with memory effects as specified by

VarHandle.getAcquire(java.lang.Object...)

.

**Returns:**
- the value

**Since:**
- 9

---

#### public final void setRelease​(
V
newValue)

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

#### public final
V
compareAndExchange​(
V
expectedValue,

V
newValue)

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

#### public final
V
compareAndExchangeAcquire​(
V
expectedValue,

V
newValue)

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

#### public final
V
compareAndExchangeRelease​(
V
expectedValue,

V
newValue)

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

#### public final boolean weakCompareAndSetVolatile​(
V
expectedValue,

V
newValue)

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

#### public final boolean weakCompareAndSetAcquire​(
V
expectedValue,

V
newValue)

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

#### public final boolean weakCompareAndSetRelease​(
V
expectedValue,

V
newValue)

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

#### Class AtomicReference<V>

java.lang.Object

- java.util.concurrent.atomic.AtomicReference<V>

java.util.concurrent.atomic.AtomicReference<V>

**Type Parameters:** V

- The type of object referred to by this reference

**All Implemented Interfaces:** Serializable

```java
public class
AtomicReference<V>

extends
Object

implements
Serializable
```

An object reference that may be updated atomically. See the

VarHandle

specification for descriptions of the properties of
atomic accesses.

**Since:** 1.5
**See Also:** Serialized Form

public class

AtomicReference<V>

extends

Object

implements

Serializable

An object reference that may be updated atomically. See the

VarHandle

specification for descriptions of the properties of
atomic accesses.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AtomicReference

()

Creates a new AtomicReference with null initial value.

AtomicReference

​(

V

initialValue)

Creates a new AtomicReference with the given initial value.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

V

accumulateAndGet

​(

V

x,

BinaryOperator

<

V

> accumulatorFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the current value with the results of
applying the given function to the current and given values,
returning the updated value.

V

compareAndExchange

​(

V

expectedValue,

V

newValue)

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

V

compareAndExchangeAcquire

​(

V

expectedValue,

V

newValue)

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

V

compareAndExchangeRelease

​(

V

expectedValue,

V

newValue)

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

​(

V

expectedValue,

V

newValue)

Atomically sets the value to

newValue

if the current value

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

.

V

get

()

Returns the current value,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

V

getAcquire

()

Returns the current value,
with memory effects as specified by

VarHandle.getAcquire(java.lang.Object...)

.

V

getAndAccumulate

​(

V

x,

BinaryOperator

<

V

> accumulatorFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the current value with the results of
applying the given function to the current and given values,
returning the previous value.

V

getAndSet

​(

V

newValue)

Atomically sets the value to

newValue

and returns the old value,
with memory effects as specified by

VarHandle.getAndSet(java.lang.Object...)

.

V

getAndUpdate

​(

UnaryOperator

<

V

> updateFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the current value with the results of
applying the given function, returning the previous value.

V

getOpaque

()

Returns the current value,
with memory effects as specified by

VarHandle.getOpaque(java.lang.Object...)

.

V

getPlain

()

Returns the current value, with memory semantics of reading as
if the variable was declared non-

volatile

.

void

lazySet

​(

V

newValue)

Sets the value to

newValue

,
with memory effects as specified by

VarHandle.setRelease(java.lang.Object...)

.

void

set

​(

V

newValue)

Sets the value to

newValue

,
with memory effects as specified by

VarHandle.setVolatile(java.lang.Object...)

.

void

setOpaque

​(

V

newValue)

Sets the value to

newValue

,
with memory effects as specified by

VarHandle.setOpaque(java.lang.Object...)

.

void

setPlain

​(

V

newValue)

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

​(

V

newValue)

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

V

updateAndGet

​(

UnaryOperator

<

V

> updateFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the current value with the results of
applying the given function, returning the updated value.

boolean

weakCompareAndSet

​(

V

expectedValue,

V

newValue)

Deprecated.

This method has plain memory effects but the method
name implies volatile memory effects (see methods such as

compareAndExchange(V, V)

and

compareAndSet(V, V)

).

boolean

weakCompareAndSetAcquire

​(

V

expectedValue,

V

newValue)

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

​(

V

expectedValue,

V

newValue)

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

​(

V

expectedValue,

V

newValue)

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

​(

V

expectedValue,

V

newValue)

Possibly atomically sets the value to

newValue

if the current value

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

AtomicReference

()

Creates a new AtomicReference with null initial value.

AtomicReference

​(

V

initialValue)

Creates a new AtomicReference with the given initial value.

---

#### Constructor Summary

Creates a new AtomicReference with null initial value.

Creates a new AtomicReference with the given initial value.

Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

V

accumulateAndGet

​(

V

x,

BinaryOperator

<

V

> accumulatorFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the current value with the results of
applying the given function to the current and given values,
returning the updated value.

V

compareAndExchange

​(

V

expectedValue,

V

newValue)

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

V

compareAndExchangeAcquire

​(

V

expectedValue,

V

newValue)

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

V

compareAndExchangeRelease

​(

V

expectedValue,

V

newValue)

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

​(

V

expectedValue,

V

newValue)

Atomically sets the value to

newValue

if the current value

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

.

V

get

()

Returns the current value,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

V

getAcquire

()

Returns the current value,
with memory effects as specified by

VarHandle.getAcquire(java.lang.Object...)

.

V

getAndAccumulate

​(

V

x,

BinaryOperator

<

V

> accumulatorFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the current value with the results of
applying the given function to the current and given values,
returning the previous value.

V

getAndSet

​(

V

newValue)

Atomically sets the value to

newValue

and returns the old value,
with memory effects as specified by

VarHandle.getAndSet(java.lang.Object...)

.

V

getAndUpdate

​(

UnaryOperator

<

V

> updateFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the current value with the results of
applying the given function, returning the previous value.

V

getOpaque

()

Returns the current value,
with memory effects as specified by

VarHandle.getOpaque(java.lang.Object...)

.

V

getPlain

()

Returns the current value, with memory semantics of reading as
if the variable was declared non-

volatile

.

void

lazySet

​(

V

newValue)

Sets the value to

newValue

,
with memory effects as specified by

VarHandle.setRelease(java.lang.Object...)

.

void

set

​(

V

newValue)

Sets the value to

newValue

,
with memory effects as specified by

VarHandle.setVolatile(java.lang.Object...)

.

void

setOpaque

​(

V

newValue)

Sets the value to

newValue

,
with memory effects as specified by

VarHandle.setOpaque(java.lang.Object...)

.

void

setPlain

​(

V

newValue)

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

​(

V

newValue)

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

V

updateAndGet

​(

UnaryOperator

<

V

> updateFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the current value with the results of
applying the given function, returning the updated value.

boolean

weakCompareAndSet

​(

V

expectedValue,

V

newValue)

Deprecated.

This method has plain memory effects but the method
name implies volatile memory effects (see methods such as

compareAndExchange(V, V)

and

compareAndSet(V, V)

).

boolean

weakCompareAndSetAcquire

​(

V

expectedValue,

V

newValue)

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

​(

V

expectedValue,

V

newValue)

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

​(

V

expectedValue,

V

newValue)

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

​(

V

expectedValue,

V

newValue)

Possibly atomically sets the value to

newValue

if the current value

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

) the current value with the results of
applying the given function to the current and given values,
returning the updated value.

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

Returns the current value, with memory semantics of reading as
if the variable was declared non-

volatile

.

Sets the value to

newValue

,
with memory effects as specified by

VarHandle.setRelease(java.lang.Object...)

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

compareAndExchange(V, V)

and

compareAndSet(V, V)

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

- AtomicReference

```java
public AtomicReference​(
V
initialValue)
```

Creates a new AtomicReference with the given initial value.

**Parameters:** initialValue

- the initial value

- AtomicReference

```java
public AtomicReference()
```

Creates a new AtomicReference with null initial value.

============ METHOD DETAIL ==========

- Method Detail

- get

```java
public final
V
get()
```

Returns the current value,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

**Returns:** the current value

- set

```java
public final void set​(
V
newValue)
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
public final void lazySet​(
V
newValue)
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

- compareAndSet

```java
public final boolean compareAndSet​(
V
expectedValue,

V
newValue)
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
public final boolean weakCompareAndSet​(
V
expectedValue,

V
newValue)
```

Deprecated.

This method has plain memory effects but the method
name implies volatile memory effects (see methods such as

compareAndExchange(V, V)

and

compareAndSet(V, V)

). To avoid
confusion over plain or volatile memory effects it is recommended that
the method

weakCompareAndSetPlain(V, V)

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
**See Also:** weakCompareAndSetPlain(V, V)

- weakCompareAndSetPlain

```java
public final boolean weakCompareAndSetPlain​(
V
expectedValue,

V
newValue)
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

- getAndSet

```java
public final
V
getAndSet​(
V
newValue)
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

- getAndUpdate

```java
public final
V
getAndUpdate​(
UnaryOperator
<
V
> updateFunction)
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
public final
V
updateAndGet​(
UnaryOperator
<
V
> updateFunction)
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
public final
V
getAndAccumulate​(
V
x,

BinaryOperator
<
V
> accumulatorFunction)
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
public final
V
accumulateAndGet​(
V
x,

BinaryOperator
<
V
> accumulatorFunction)
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

- getPlain

```java
public final
V
getPlain()
```

Returns the current value, with memory semantics of reading as
if the variable was declared non-

volatile

.

**Returns:** the value
**Since:** 9

- setPlain

```java
public final void setPlain​(
V
newValue)
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
public final
V
getOpaque()
```

Returns the current value,
with memory effects as specified by

VarHandle.getOpaque(java.lang.Object...)

.

**Returns:** the value
**Since:** 9

- setOpaque

```java
public final void setOpaque​(
V
newValue)
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
public final
V
getAcquire()
```

Returns the current value,
with memory effects as specified by

VarHandle.getAcquire(java.lang.Object...)

.

**Returns:** the value
**Since:** 9

- setRelease

```java
public final void setRelease​(
V
newValue)
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
public final
V
compareAndExchange​(
V
expectedValue,

V
newValue)
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
public final
V
compareAndExchangeAcquire​(
V
expectedValue,

V
newValue)
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
public final
V
compareAndExchangeRelease​(
V
expectedValue,

V
newValue)
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
public final boolean weakCompareAndSetVolatile​(
V
expectedValue,

V
newValue)
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
public final boolean weakCompareAndSetAcquire​(
V
expectedValue,

V
newValue)
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
public final boolean weakCompareAndSetRelease​(
V
expectedValue,

V
newValue)
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

- AtomicReference

```java
public AtomicReference​(
V
initialValue)
```

Creates a new AtomicReference with the given initial value.

**Parameters:** initialValue

- the initial value

- AtomicReference

```java
public AtomicReference()
```

Creates a new AtomicReference with null initial value.

---

#### Constructor Detail

AtomicReference

```java
public AtomicReference​(
V
initialValue)
```

Creates a new AtomicReference with the given initial value.

**Parameters:** initialValue

- the initial value

---

#### AtomicReference

public AtomicReference​(

V

initialValue)

Creates a new AtomicReference with the given initial value.

AtomicReference

```java
public AtomicReference()
```

Creates a new AtomicReference with null initial value.

---

#### AtomicReference

public AtomicReference()

Creates a new AtomicReference with null initial value.

Method Detail

- get

```java
public final
V
get()
```

Returns the current value,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

**Returns:** the current value

- set

```java
public final void set​(
V
newValue)
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
public final void lazySet​(
V
newValue)
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

- compareAndSet

```java
public final boolean compareAndSet​(
V
expectedValue,

V
newValue)
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
public final boolean weakCompareAndSet​(
V
expectedValue,

V
newValue)
```

Deprecated.

This method has plain memory effects but the method
name implies volatile memory effects (see methods such as

compareAndExchange(V, V)

and

compareAndSet(V, V)

). To avoid
confusion over plain or volatile memory effects it is recommended that
the method

weakCompareAndSetPlain(V, V)

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
**See Also:** weakCompareAndSetPlain(V, V)

- weakCompareAndSetPlain

```java
public final boolean weakCompareAndSetPlain​(
V
expectedValue,

V
newValue)
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

- getAndSet

```java
public final
V
getAndSet​(
V
newValue)
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

- getAndUpdate

```java
public final
V
getAndUpdate​(
UnaryOperator
<
V
> updateFunction)
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
public final
V
updateAndGet​(
UnaryOperator
<
V
> updateFunction)
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
public final
V
getAndAccumulate​(
V
x,

BinaryOperator
<
V
> accumulatorFunction)
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
public final
V
accumulateAndGet​(
V
x,

BinaryOperator
<
V
> accumulatorFunction)
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

- getPlain

```java
public final
V
getPlain()
```

Returns the current value, with memory semantics of reading as
if the variable was declared non-

volatile

.

**Returns:** the value
**Since:** 9

- setPlain

```java
public final void setPlain​(
V
newValue)
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
public final
V
getOpaque()
```

Returns the current value,
with memory effects as specified by

VarHandle.getOpaque(java.lang.Object...)

.

**Returns:** the value
**Since:** 9

- setOpaque

```java
public final void setOpaque​(
V
newValue)
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
public final
V
getAcquire()
```

Returns the current value,
with memory effects as specified by

VarHandle.getAcquire(java.lang.Object...)

.

**Returns:** the value
**Since:** 9

- setRelease

```java
public final void setRelease​(
V
newValue)
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
public final
V
compareAndExchange​(
V
expectedValue,

V
newValue)
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
public final
V
compareAndExchangeAcquire​(
V
expectedValue,

V
newValue)
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
public final
V
compareAndExchangeRelease​(
V
expectedValue,

V
newValue)
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
public final boolean weakCompareAndSetVolatile​(
V
expectedValue,

V
newValue)
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
public final boolean weakCompareAndSetAcquire​(
V
expectedValue,

V
newValue)
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
public final boolean weakCompareAndSetRelease​(
V
expectedValue,

V
newValue)
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
public final
V
get()
```

Returns the current value,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

**Returns:** the current value

---

#### get

public final

V

get()

Returns the current value,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

set

```java
public final void set​(
V
newValue)
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

public final void set​(

V

newValue)

Sets the value to

newValue

,
with memory effects as specified by

VarHandle.setVolatile(java.lang.Object...)

.

lazySet

```java
public final void lazySet​(
V
newValue)
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

public final void lazySet​(

V

newValue)

Sets the value to

newValue

,
with memory effects as specified by

VarHandle.setRelease(java.lang.Object...)

.

compareAndSet

```java
public final boolean compareAndSet​(
V
expectedValue,

V
newValue)
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

public final boolean compareAndSet​(

V

expectedValue,

V

newValue)

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
public final boolean weakCompareAndSet​(
V
expectedValue,

V
newValue)
```

Deprecated.

This method has plain memory effects but the method
name implies volatile memory effects (see methods such as

compareAndExchange(V, V)

and

compareAndSet(V, V)

). To avoid
confusion over plain or volatile memory effects it is recommended that
the method

weakCompareAndSetPlain(V, V)

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
**See Also:** weakCompareAndSetPlain(V, V)

---

#### weakCompareAndSet

@Deprecated

(

since

="9")
public final boolean weakCompareAndSet​(

V

expectedValue,

V

newValue)

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
public final boolean weakCompareAndSetPlain​(
V
expectedValue,

V
newValue)
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

public final boolean weakCompareAndSetPlain​(

V

expectedValue,

V

newValue)

Possibly atomically sets the value to

newValue

if the current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetPlain(java.lang.Object...)

.

getAndSet

```java
public final
V
getAndSet​(
V
newValue)
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

public final

V

getAndSet​(

V

newValue)

Atomically sets the value to

newValue

and returns the old value,
with memory effects as specified by

VarHandle.getAndSet(java.lang.Object...)

.

getAndUpdate

```java
public final
V
getAndUpdate​(
UnaryOperator
<
V
> updateFunction)
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

public final

V

getAndUpdate​(

UnaryOperator

<

V

> updateFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the current value with the results of
applying the given function, returning the previous value. The
function should be side-effect-free, since it may be re-applied
when attempted updates fail due to contention among threads.

updateAndGet

```java
public final
V
updateAndGet​(
UnaryOperator
<
V
> updateFunction)
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

public final

V

updateAndGet​(

UnaryOperator

<

V

> updateFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the current value with the results of
applying the given function, returning the updated value. The
function should be side-effect-free, since it may be re-applied
when attempted updates fail due to contention among threads.

getAndAccumulate

```java
public final
V
getAndAccumulate​(
V
x,

BinaryOperator
<
V
> accumulatorFunction)
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

public final

V

getAndAccumulate​(

V

x,

BinaryOperator

<

V

> accumulatorFunction)

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
public final
V
accumulateAndGet​(
V
x,

BinaryOperator
<
V
> accumulatorFunction)
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

public final

V

accumulateAndGet​(

V

x,

BinaryOperator

<

V

> accumulatorFunction)

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

getPlain

```java
public final
V
getPlain()
```

Returns the current value, with memory semantics of reading as
if the variable was declared non-

volatile

.

**Returns:** the value
**Since:** 9

---

#### getPlain

public final

V

getPlain()

Returns the current value, with memory semantics of reading as
if the variable was declared non-

volatile

.

setPlain

```java
public final void setPlain​(
V
newValue)
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

public final void setPlain​(

V

newValue)

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
public final
V
getOpaque()
```

Returns the current value,
with memory effects as specified by

VarHandle.getOpaque(java.lang.Object...)

.

**Returns:** the value
**Since:** 9

---

#### getOpaque

public final

V

getOpaque()

Returns the current value,
with memory effects as specified by

VarHandle.getOpaque(java.lang.Object...)

.

setOpaque

```java
public final void setOpaque​(
V
newValue)
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

public final void setOpaque​(

V

newValue)

Sets the value to

newValue

,
with memory effects as specified by

VarHandle.setOpaque(java.lang.Object...)

.

getAcquire

```java
public final
V
getAcquire()
```

Returns the current value,
with memory effects as specified by

VarHandle.getAcquire(java.lang.Object...)

.

**Returns:** the value
**Since:** 9

---

#### getAcquire

public final

V

getAcquire()

Returns the current value,
with memory effects as specified by

VarHandle.getAcquire(java.lang.Object...)

.

setRelease

```java
public final void setRelease​(
V
newValue)
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

public final void setRelease​(

V

newValue)

Sets the value to

newValue

,
with memory effects as specified by

VarHandle.setRelease(java.lang.Object...)

.

compareAndExchange

```java
public final
V
compareAndExchange​(
V
expectedValue,

V
newValue)
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

public final

V

compareAndExchange​(

V

expectedValue,

V

newValue)

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
public final
V
compareAndExchangeAcquire​(
V
expectedValue,

V
newValue)
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

public final

V

compareAndExchangeAcquire​(

V

expectedValue,

V

newValue)

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
public final
V
compareAndExchangeRelease​(
V
expectedValue,

V
newValue)
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

public final

V

compareAndExchangeRelease​(

V

expectedValue,

V

newValue)

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
public final boolean weakCompareAndSetVolatile​(
V
expectedValue,

V
newValue)
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

public final boolean weakCompareAndSetVolatile​(

V

expectedValue,

V

newValue)

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
public final boolean weakCompareAndSetAcquire​(
V
expectedValue,

V
newValue)
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

public final boolean weakCompareAndSetAcquire​(

V

expectedValue,

V

newValue)

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
public final boolean weakCompareAndSetRelease​(
V
expectedValue,

V
newValue)
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

public final boolean weakCompareAndSetRelease​(

V

expectedValue,

V

newValue)

Possibly atomically sets the value to

newValue

if the current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetRelease(java.lang.Object...)

.

---

