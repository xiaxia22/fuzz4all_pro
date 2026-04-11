# Class AtomicBoolean

**Source:** `java.base\java\util\concurrent\atomic\AtomicBoolean.html`

### Class Description

```java
public class
AtomicBoolean

extends
Object

implements
Serializable
```

A

boolean

value that may be updated atomically. See the

VarHandle

specification for descriptions of the properties
of atomic accesses. An

AtomicBoolean

is used in
applications such as atomically updated flags, and cannot be used
as a replacement for a

Boolean

.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public AtomicBoolean​(boolean initialValue)

Creates a new

AtomicBoolean

with the given initial value.

**Parameters:**
- initialValue

- the initial value

---

#### public AtomicBoolean()

Creates a new

AtomicBoolean

with initial value

false

.

---

### Method Details

#### public final boolean get()

Returns the current value,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

**Returns:**
- the current value

---

#### public final boolean compareAndSet​(boolean expectedValue,
boolean newValue)

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
public boolean weakCompareAndSet​(boolean expectedValue,
boolean newValue)

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
- weakCompareAndSetPlain(boolean, boolean)

---

#### public boolean weakCompareAndSetPlain​(boolean expectedValue,
boolean newValue)

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

#### public final void set​(boolean newValue)

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

#### public final void lazySet​(boolean newValue)

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

#### public final boolean getAndSet​(boolean newValue)

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

#### public final boolean getPlain()

Returns the current value, with memory semantics of reading as
if the variable was declared non-

volatile

.

**Returns:**
- the value

**Since:**
- 9

---

#### public final void setPlain​(boolean newValue)

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

#### public final boolean getOpaque()

Returns the current value,
with memory effects as specified by

VarHandle.getOpaque(java.lang.Object...)

.

**Returns:**
- the value

**Since:**
- 9

---

#### public final void setOpaque​(boolean newValue)

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

#### public final boolean getAcquire()

Returns the current value,
with memory effects as specified by

VarHandle.getAcquire(java.lang.Object...)

.

**Returns:**
- the value

**Since:**
- 9

---

#### public final void setRelease​(boolean newValue)

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

#### public final boolean compareAndExchange​(boolean expectedValue,
boolean newValue)

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

#### public final boolean compareAndExchangeAcquire​(boolean expectedValue,
boolean newValue)

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

#### public final boolean compareAndExchangeRelease​(boolean expectedValue,
boolean newValue)

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

#### public final boolean weakCompareAndSetVolatile​(boolean expectedValue,
boolean newValue)

Possibly atomically sets the value to

newValue

if the current
value

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

#### public final boolean weakCompareAndSetAcquire​(boolean expectedValue,
boolean newValue)

Possibly atomically sets the value to

newValue

if the current
value

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

#### public final boolean weakCompareAndSetRelease​(boolean expectedValue,
boolean newValue)

Possibly atomically sets the value to

newValue

if the current
value

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

#### Class AtomicBoolean

java.lang.Object

- java.util.concurrent.atomic.AtomicBoolean

java.util.concurrent.atomic.AtomicBoolean

**All Implemented Interfaces:** Serializable

```java
public class
AtomicBoolean

extends
Object

implements
Serializable
```

A

boolean

value that may be updated atomically. See the

VarHandle

specification for descriptions of the properties
of atomic accesses. An

AtomicBoolean

is used in
applications such as atomically updated flags, and cannot be used
as a replacement for a

Boolean

.

**Since:** 1.5
**See Also:** Serialized Form

public class

AtomicBoolean

extends

Object

implements

Serializable

A

boolean

value that may be updated atomically. See the

VarHandle

specification for descriptions of the properties
of atomic accesses. An

AtomicBoolean

is used in
applications such as atomically updated flags, and cannot be used
as a replacement for a

Boolean

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AtomicBoolean

()

Creates a new

AtomicBoolean

with initial value

false

.

AtomicBoolean

​(boolean initialValue)

Creates a new

AtomicBoolean

with the given initial value.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

boolean

compareAndExchange

​(boolean expectedValue,
boolean newValue)

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

boolean

compareAndExchangeAcquire

​(boolean expectedValue,
boolean newValue)

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

boolean

compareAndExchangeRelease

​(boolean expectedValue,
boolean newValue)

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

​(boolean expectedValue,
boolean newValue)

Atomically sets the value to

newValue

if the current value

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

.

boolean

get

()

Returns the current value,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

boolean

getAcquire

()

Returns the current value,
with memory effects as specified by

VarHandle.getAcquire(java.lang.Object...)

.

boolean

getAndSet

​(boolean newValue)

Atomically sets the value to

newValue

and returns the old value,
with memory effects as specified by

VarHandle.getAndSet(java.lang.Object...)

.

boolean

getOpaque

()

Returns the current value,
with memory effects as specified by

VarHandle.getOpaque(java.lang.Object...)

.

boolean

getPlain

()

Returns the current value, with memory semantics of reading as
if the variable was declared non-

volatile

.

void

lazySet

​(boolean newValue)

Sets the value to

newValue

,
with memory effects as specified by

VarHandle.setRelease(java.lang.Object...)

.

void

set

​(boolean newValue)

Sets the value to

newValue

,
with memory effects as specified by

VarHandle.setVolatile(java.lang.Object...)

.

void

setOpaque

​(boolean newValue)

Sets the value to

newValue

,
with memory effects as specified by

VarHandle.setOpaque(java.lang.Object...)

.

void

setPlain

​(boolean newValue)

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

​(boolean newValue)

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

boolean

weakCompareAndSet

​(boolean expectedValue,
boolean newValue)

Deprecated.

This method has plain memory effects but the method
name implies volatile memory effects (see methods such as

compareAndExchange(boolean, boolean)

and

compareAndSet(boolean, boolean)

).

boolean

weakCompareAndSetAcquire

​(boolean expectedValue,
boolean newValue)

Possibly atomically sets the value to

newValue

if the current
value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetAcquire(java.lang.Object...)

.

boolean

weakCompareAndSetPlain

​(boolean expectedValue,
boolean newValue)

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

​(boolean expectedValue,
boolean newValue)

Possibly atomically sets the value to

newValue

if the current
value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetRelease(java.lang.Object...)

.

boolean

weakCompareAndSetVolatile

​(boolean expectedValue,
boolean newValue)

Possibly atomically sets the value to

newValue

if the current
value

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

AtomicBoolean

()

Creates a new

AtomicBoolean

with initial value

false

.

AtomicBoolean

​(boolean initialValue)

Creates a new

AtomicBoolean

with the given initial value.

---

#### Constructor Summary

Creates a new

AtomicBoolean

with initial value

false

.

Creates a new

AtomicBoolean

with the given initial value.

Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

boolean

compareAndExchange

​(boolean expectedValue,
boolean newValue)

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

boolean

compareAndExchangeAcquire

​(boolean expectedValue,
boolean newValue)

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

boolean

compareAndExchangeRelease

​(boolean expectedValue,
boolean newValue)

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

​(boolean expectedValue,
boolean newValue)

Atomically sets the value to

newValue

if the current value

== expectedValue

,
with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

.

boolean

get

()

Returns the current value,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

boolean

getAcquire

()

Returns the current value,
with memory effects as specified by

VarHandle.getAcquire(java.lang.Object...)

.

boolean

getAndSet

​(boolean newValue)

Atomically sets the value to

newValue

and returns the old value,
with memory effects as specified by

VarHandle.getAndSet(java.lang.Object...)

.

boolean

getOpaque

()

Returns the current value,
with memory effects as specified by

VarHandle.getOpaque(java.lang.Object...)

.

boolean

getPlain

()

Returns the current value, with memory semantics of reading as
if the variable was declared non-

volatile

.

void

lazySet

​(boolean newValue)

Sets the value to

newValue

,
with memory effects as specified by

VarHandle.setRelease(java.lang.Object...)

.

void

set

​(boolean newValue)

Sets the value to

newValue

,
with memory effects as specified by

VarHandle.setVolatile(java.lang.Object...)

.

void

setOpaque

​(boolean newValue)

Sets the value to

newValue

,
with memory effects as specified by

VarHandle.setOpaque(java.lang.Object...)

.

void

setPlain

​(boolean newValue)

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

​(boolean newValue)

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

boolean

weakCompareAndSet

​(boolean expectedValue,
boolean newValue)

Deprecated.

This method has plain memory effects but the method
name implies volatile memory effects (see methods such as

compareAndExchange(boolean, boolean)

and

compareAndSet(boolean, boolean)

).

boolean

weakCompareAndSetAcquire

​(boolean expectedValue,
boolean newValue)

Possibly atomically sets the value to

newValue

if the current
value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetAcquire(java.lang.Object...)

.

boolean

weakCompareAndSetPlain

​(boolean expectedValue,
boolean newValue)

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

​(boolean expectedValue,
boolean newValue)

Possibly atomically sets the value to

newValue

if the current
value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetRelease(java.lang.Object...)

.

boolean

weakCompareAndSetVolatile

​(boolean expectedValue,
boolean newValue)

Possibly atomically sets the value to

newValue

if the current
value

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

Atomically sets the value to

newValue

and returns the old value,
with memory effects as specified by

VarHandle.getAndSet(java.lang.Object...)

.

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

Deprecated.

This method has plain memory effects but the method
name implies volatile memory effects (see methods such as

compareAndExchange(boolean, boolean)

and

compareAndSet(boolean, boolean)

).

Possibly atomically sets the value to

newValue

if the current
value

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

if the current
value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetRelease(java.lang.Object...)

.

Possibly atomically sets the value to

newValue

if the current
value

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

- AtomicBoolean

```java
public AtomicBoolean​(boolean initialValue)
```

Creates a new

AtomicBoolean

with the given initial value.

**Parameters:** initialValue

- the initial value

- AtomicBoolean

```java
public AtomicBoolean()
```

Creates a new

AtomicBoolean

with initial value

false

.

============ METHOD DETAIL ==========

- Method Detail

- get

```java
public final boolean get()
```

Returns the current value,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

**Returns:** the current value

- compareAndSet

```java
public final boolean compareAndSet​(boolean expectedValue,
boolean newValue)
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
public boolean weakCompareAndSet​(boolean expectedValue,
boolean newValue)
```

Deprecated.

This method has plain memory effects but the method
name implies volatile memory effects (see methods such as

compareAndExchange(boolean, boolean)

and

compareAndSet(boolean, boolean)

). To avoid
confusion over plain or volatile memory effects it is recommended that
the method

weakCompareAndSetPlain(boolean, boolean)

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
**See Also:** weakCompareAndSetPlain(boolean, boolean)

- weakCompareAndSetPlain

```java
public boolean weakCompareAndSetPlain​(boolean expectedValue,
boolean newValue)
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

- set

```java
public final void set​(boolean newValue)
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
public final void lazySet​(boolean newValue)
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
public final boolean getAndSet​(boolean newValue)
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
public final boolean getPlain()
```

Returns the current value, with memory semantics of reading as
if the variable was declared non-

volatile

.

**Returns:** the value
**Since:** 9

- setPlain

```java
public final void setPlain​(boolean newValue)
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
public final boolean getOpaque()
```

Returns the current value,
with memory effects as specified by

VarHandle.getOpaque(java.lang.Object...)

.

**Returns:** the value
**Since:** 9

- setOpaque

```java
public final void setOpaque​(boolean newValue)
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
public final boolean getAcquire()
```

Returns the current value,
with memory effects as specified by

VarHandle.getAcquire(java.lang.Object...)

.

**Returns:** the value
**Since:** 9

- setRelease

```java
public final void setRelease​(boolean newValue)
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
public final boolean compareAndExchange​(boolean expectedValue,
boolean newValue)
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
public final boolean compareAndExchangeAcquire​(boolean expectedValue,
boolean newValue)
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
public final boolean compareAndExchangeRelease​(boolean expectedValue,
boolean newValue)
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
public final boolean weakCompareAndSetVolatile​(boolean expectedValue,
boolean newValue)
```

Possibly atomically sets the value to

newValue

if the current
value

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
public final boolean weakCompareAndSetAcquire​(boolean expectedValue,
boolean newValue)
```

Possibly atomically sets the value to

newValue

if the current
value

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
public final boolean weakCompareAndSetRelease​(boolean expectedValue,
boolean newValue)
```

Possibly atomically sets the value to

newValue

if the current
value

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

- AtomicBoolean

```java
public AtomicBoolean​(boolean initialValue)
```

Creates a new

AtomicBoolean

with the given initial value.

**Parameters:** initialValue

- the initial value

- AtomicBoolean

```java
public AtomicBoolean()
```

Creates a new

AtomicBoolean

with initial value

false

.

---

#### Constructor Detail

AtomicBoolean

```java
public AtomicBoolean​(boolean initialValue)
```

Creates a new

AtomicBoolean

with the given initial value.

**Parameters:** initialValue

- the initial value

---

#### AtomicBoolean

public AtomicBoolean​(boolean initialValue)

Creates a new

AtomicBoolean

with the given initial value.

AtomicBoolean

```java
public AtomicBoolean()
```

Creates a new

AtomicBoolean

with initial value

false

.

---

#### AtomicBoolean

public AtomicBoolean()

Creates a new

AtomicBoolean

with initial value

false

.

Method Detail

- get

```java
public final boolean get()
```

Returns the current value,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

**Returns:** the current value

- compareAndSet

```java
public final boolean compareAndSet​(boolean expectedValue,
boolean newValue)
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
public boolean weakCompareAndSet​(boolean expectedValue,
boolean newValue)
```

Deprecated.

This method has plain memory effects but the method
name implies volatile memory effects (see methods such as

compareAndExchange(boolean, boolean)

and

compareAndSet(boolean, boolean)

). To avoid
confusion over plain or volatile memory effects it is recommended that
the method

weakCompareAndSetPlain(boolean, boolean)

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
**See Also:** weakCompareAndSetPlain(boolean, boolean)

- weakCompareAndSetPlain

```java
public boolean weakCompareAndSetPlain​(boolean expectedValue,
boolean newValue)
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

- set

```java
public final void set​(boolean newValue)
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
public final void lazySet​(boolean newValue)
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
public final boolean getAndSet​(boolean newValue)
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
public final boolean getPlain()
```

Returns the current value, with memory semantics of reading as
if the variable was declared non-

volatile

.

**Returns:** the value
**Since:** 9

- setPlain

```java
public final void setPlain​(boolean newValue)
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
public final boolean getOpaque()
```

Returns the current value,
with memory effects as specified by

VarHandle.getOpaque(java.lang.Object...)

.

**Returns:** the value
**Since:** 9

- setOpaque

```java
public final void setOpaque​(boolean newValue)
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
public final boolean getAcquire()
```

Returns the current value,
with memory effects as specified by

VarHandle.getAcquire(java.lang.Object...)

.

**Returns:** the value
**Since:** 9

- setRelease

```java
public final void setRelease​(boolean newValue)
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
public final boolean compareAndExchange​(boolean expectedValue,
boolean newValue)
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
public final boolean compareAndExchangeAcquire​(boolean expectedValue,
boolean newValue)
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
public final boolean compareAndExchangeRelease​(boolean expectedValue,
boolean newValue)
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
public final boolean weakCompareAndSetVolatile​(boolean expectedValue,
boolean newValue)
```

Possibly atomically sets the value to

newValue

if the current
value

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
public final boolean weakCompareAndSetAcquire​(boolean expectedValue,
boolean newValue)
```

Possibly atomically sets the value to

newValue

if the current
value

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
public final boolean weakCompareAndSetRelease​(boolean expectedValue,
boolean newValue)
```

Possibly atomically sets the value to

newValue

if the current
value

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
public final boolean get()
```

Returns the current value,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

**Returns:** the current value

---

#### get

public final boolean get()

Returns the current value,
with memory effects as specified by

VarHandle.getVolatile(java.lang.Object...)

.

compareAndSet

```java
public final boolean compareAndSet​(boolean expectedValue,
boolean newValue)
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

public final boolean compareAndSet​(boolean expectedValue,
boolean newValue)

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
public boolean weakCompareAndSet​(boolean expectedValue,
boolean newValue)
```

Deprecated.

This method has plain memory effects but the method
name implies volatile memory effects (see methods such as

compareAndExchange(boolean, boolean)

and

compareAndSet(boolean, boolean)

). To avoid
confusion over plain or volatile memory effects it is recommended that
the method

weakCompareAndSetPlain(boolean, boolean)

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
**See Also:** weakCompareAndSetPlain(boolean, boolean)

---

#### weakCompareAndSet

@Deprecated

(

since

="9")
public boolean weakCompareAndSet​(boolean expectedValue,
boolean newValue)

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
public boolean weakCompareAndSetPlain​(boolean expectedValue,
boolean newValue)
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

public boolean weakCompareAndSetPlain​(boolean expectedValue,
boolean newValue)

Possibly atomically sets the value to

newValue

if the current value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetPlain(java.lang.Object...)

.

set

```java
public final void set​(boolean newValue)
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

public final void set​(boolean newValue)

Sets the value to

newValue

,
with memory effects as specified by

VarHandle.setVolatile(java.lang.Object...)

.

lazySet

```java
public final void lazySet​(boolean newValue)
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

public final void lazySet​(boolean newValue)

Sets the value to

newValue

,
with memory effects as specified by

VarHandle.setRelease(java.lang.Object...)

.

getAndSet

```java
public final boolean getAndSet​(boolean newValue)
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

public final boolean getAndSet​(boolean newValue)

Atomically sets the value to

newValue

and returns the old value,
with memory effects as specified by

VarHandle.getAndSet(java.lang.Object...)

.

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
public final boolean getPlain()
```

Returns the current value, with memory semantics of reading as
if the variable was declared non-

volatile

.

**Returns:** the value
**Since:** 9

---

#### getPlain

public final boolean getPlain()

Returns the current value, with memory semantics of reading as
if the variable was declared non-

volatile

.

setPlain

```java
public final void setPlain​(boolean newValue)
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

public final void setPlain​(boolean newValue)

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
public final boolean getOpaque()
```

Returns the current value,
with memory effects as specified by

VarHandle.getOpaque(java.lang.Object...)

.

**Returns:** the value
**Since:** 9

---

#### getOpaque

public final boolean getOpaque()

Returns the current value,
with memory effects as specified by

VarHandle.getOpaque(java.lang.Object...)

.

setOpaque

```java
public final void setOpaque​(boolean newValue)
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

public final void setOpaque​(boolean newValue)

Sets the value to

newValue

,
with memory effects as specified by

VarHandle.setOpaque(java.lang.Object...)

.

getAcquire

```java
public final boolean getAcquire()
```

Returns the current value,
with memory effects as specified by

VarHandle.getAcquire(java.lang.Object...)

.

**Returns:** the value
**Since:** 9

---

#### getAcquire

public final boolean getAcquire()

Returns the current value,
with memory effects as specified by

VarHandle.getAcquire(java.lang.Object...)

.

setRelease

```java
public final void setRelease​(boolean newValue)
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

public final void setRelease​(boolean newValue)

Sets the value to

newValue

,
with memory effects as specified by

VarHandle.setRelease(java.lang.Object...)

.

compareAndExchange

```java
public final boolean compareAndExchange​(boolean expectedValue,
boolean newValue)
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

public final boolean compareAndExchange​(boolean expectedValue,
boolean newValue)

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
public final boolean compareAndExchangeAcquire​(boolean expectedValue,
boolean newValue)
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

public final boolean compareAndExchangeAcquire​(boolean expectedValue,
boolean newValue)

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
public final boolean compareAndExchangeRelease​(boolean expectedValue,
boolean newValue)
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

public final boolean compareAndExchangeRelease​(boolean expectedValue,
boolean newValue)

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
public final boolean weakCompareAndSetVolatile​(boolean expectedValue,
boolean newValue)
```

Possibly atomically sets the value to

newValue

if the current
value

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

public final boolean weakCompareAndSetVolatile​(boolean expectedValue,
boolean newValue)

Possibly atomically sets the value to

newValue

if the current
value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSet(java.lang.Object...)

.

weakCompareAndSetAcquire

```java
public final boolean weakCompareAndSetAcquire​(boolean expectedValue,
boolean newValue)
```

Possibly atomically sets the value to

newValue

if the current
value

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

public final boolean weakCompareAndSetAcquire​(boolean expectedValue,
boolean newValue)

Possibly atomically sets the value to

newValue

if the current
value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetAcquire(java.lang.Object...)

.

weakCompareAndSetRelease

```java
public final boolean weakCompareAndSetRelease​(boolean expectedValue,
boolean newValue)
```

Possibly atomically sets the value to

newValue

if the current
value

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

public final boolean weakCompareAndSetRelease​(boolean expectedValue,
boolean newValue)

Possibly atomically sets the value to

newValue

if the current
value

== expectedValue

,
with memory effects as specified by

VarHandle.weakCompareAndSetRelease(java.lang.Object...)

.

---

