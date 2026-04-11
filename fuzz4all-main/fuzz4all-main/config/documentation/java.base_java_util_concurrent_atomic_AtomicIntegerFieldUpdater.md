# Class AtomicIntegerFieldUpdater<T>

**Source:** `java.base\java\util\concurrent\atomic\AtomicIntegerFieldUpdater.html`

### Class Description

```java
public abstract class
AtomicIntegerFieldUpdater<T>

extends
Object
```

A reflection-based utility that enables atomic updates to
designated

volatile int

fields of designated classes.
This class is designed for use in atomic data structures in which
several fields of the same node are independently subject to atomic
updates.

Note that the guarantees of the

compareAndSet

method in this class are weaker than in other atomic classes.
Because this class cannot ensure that all uses of the field
are appropriate for purposes of atomic access, it can
guarantee atomicity only with respect to other invocations of

compareAndSet

and

set

on the same updater.

Object arguments for parameters of type

T

that are not
instances of the class passed to

newUpdater(java.lang.Class<U>, java.lang.String)

will result in
a

ClassCastException

being thrown.

**Type Parameters:** T

- The type of the object holding the updatable field

---

### Field Details

*No entries found.*

### Constructor Details

#### protected AtomicIntegerFieldUpdater()

Protected do-nothing constructor for use by subclasses.

---

### Method Details

#### public static <U>
AtomicIntegerFieldUpdater
<U> newUpdater​(
Class
<U> tclass,

String
fieldName)

Creates and returns an updater for objects with the given field.
The Class argument is needed to check that reflective types and
generic types match.

**Parameters:**
- tclass

- the class of the objects holding the field
- fieldName

- the name of the field to be updated

**Returns:**
- the updater

**Throws:**
- IllegalArgumentException

- if the field is not a
volatile integer type
- RuntimeException

- with a nested reflection-based
exception if the class does not hold field or is the wrong type,
or the field is inaccessible to the caller according to Java language
access control

**Type Parameters:**
- U

- the type of instances of tclass

---

#### public abstract boolean compareAndSet​(
T
obj,
int expect,
int update)

Atomically sets the field of the given object managed by this updater
to the given updated value if the current value

==

the
expected value. This method is guaranteed to be atomic with respect to
other calls to

compareAndSet

and

set

, but not
necessarily with respect to other changes in the field.

**Parameters:**
- obj

- An object whose field to conditionally set
- expect

- the expected value
- update

- the new value

**Returns:**
- true

if successful

---

#### public abstract boolean weakCompareAndSet​(
T
obj,
int expect,
int update)

Atomically sets the field of the given object managed by this updater
to the given updated value if the current value

==

the
expected value. This method is guaranteed to be atomic with respect to
other calls to

compareAndSet

and

set

, but not
necessarily with respect to other changes in the field.

May fail
spuriously and does not provide ordering guarantees

, so is
only rarely an appropriate alternative to

compareAndSet

.

**Parameters:**
- obj

- An object whose field to conditionally set
- expect

- the expected value
- update

- the new value

**Returns:**
- true

if successful

---

#### public abstract void set​(
T
obj,
int newValue)

Sets the field of the given object managed by this updater to the
given updated value. This operation is guaranteed to act as a volatile
store with respect to subsequent invocations of

compareAndSet

.

**Parameters:**
- obj

- An object whose field to set
- newValue

- the new value

---

#### public abstract void lazySet​(
T
obj,
int newValue)

Eventually sets the field of the given object managed by this
updater to the given updated value.

**Parameters:**
- obj

- An object whose field to set
- newValue

- the new value

**Since:**
- 1.6

---

#### public abstract int get​(
T
obj)

Returns the current value held in the field of the given object
managed by this updater.

**Parameters:**
- obj

- An object whose field to get

**Returns:**
- the current value

---

#### public int getAndSet​(
T
obj,
int newValue)

Atomically sets the field of the given object managed by this updater
to the given value and returns the old value.

**Parameters:**
- obj

- An object whose field to get and set
- newValue

- the new value

**Returns:**
- the previous value

---

#### public int getAndIncrement​(
T
obj)

Atomically increments by one the current value of the field of the
given object managed by this updater.

**Parameters:**
- obj

- An object whose field to get and set

**Returns:**
- the previous value

---

#### public int getAndDecrement​(
T
obj)

Atomically decrements by one the current value of the field of the
given object managed by this updater.

**Parameters:**
- obj

- An object whose field to get and set

**Returns:**
- the previous value

---

#### public int getAndAdd​(
T
obj,
int delta)

Atomically adds the given value to the current value of the field of
the given object managed by this updater.

**Parameters:**
- obj

- An object whose field to get and set
- delta

- the value to add

**Returns:**
- the previous value

---

#### public int incrementAndGet​(
T
obj)

Atomically increments by one the current value of the field of the
given object managed by this updater.

**Parameters:**
- obj

- An object whose field to get and set

**Returns:**
- the updated value

---

#### public int decrementAndGet​(
T
obj)

Atomically decrements by one the current value of the field of the
given object managed by this updater.

**Parameters:**
- obj

- An object whose field to get and set

**Returns:**
- the updated value

---

#### public int addAndGet​(
T
obj,
int delta)

Atomically adds the given value to the current value of the field of
the given object managed by this updater.

**Parameters:**
- obj

- An object whose field to get and set
- delta

- the value to add

**Returns:**
- the updated value

---

#### public final int getAndUpdate​(
T
obj,

IntUnaryOperator
updateFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the field of the given object managed
by this updater with the results of applying the given
function, returning the previous value. The function should be
side-effect-free, since it may be re-applied when attempted
updates fail due to contention among threads.

**Parameters:**
- obj

- An object whose field to get and set
- updateFunction

- a side-effect-free function

**Returns:**
- the previous value

**Since:**
- 1.8

---

#### public final int updateAndGet​(
T
obj,

IntUnaryOperator
updateFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the field of the given object managed
by this updater with the results of applying the given
function, returning the updated value. The function should be
side-effect-free, since it may be re-applied when attempted
updates fail due to contention among threads.

**Parameters:**
- obj

- An object whose field to get and set
- updateFunction

- a side-effect-free function

**Returns:**
- the updated value

**Since:**
- 1.8

---

#### public final int getAndAccumulate​(
T
obj,
int x,

IntBinaryOperator
accumulatorFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the field of the given object managed
by this updater with the results of applying the given function
to the current and given values, returning the previous value.
The function should be side-effect-free, since it may be
re-applied when attempted updates fail due to contention among
threads. The function is applied with the current value as its
first argument, and the given update as the second argument.

**Parameters:**
- obj

- An object whose field to get and set
- x

- the update value
- accumulatorFunction

- a side-effect-free function of two arguments

**Returns:**
- the previous value

**Since:**
- 1.8

---

#### public final int accumulateAndGet​(
T
obj,
int x,

IntBinaryOperator
accumulatorFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the field of the given object managed
by this updater with the results of applying the given function
to the current and given values, returning the updated value.
The function should be side-effect-free, since it may be
re-applied when attempted updates fail due to contention among
threads. The function is applied with the current value as its
first argument, and the given update as the second argument.

**Parameters:**
- obj

- An object whose field to get and set
- x

- the update value
- accumulatorFunction

- a side-effect-free function of two arguments

**Returns:**
- the updated value

**Since:**
- 1.8

---

### Additional Sections

#### Class AtomicIntegerFieldUpdater<T>

java.lang.Object

- java.util.concurrent.atomic.AtomicIntegerFieldUpdater<T>

java.util.concurrent.atomic.AtomicIntegerFieldUpdater<T>

**Type Parameters:** T

- The type of the object holding the updatable field

```java
public abstract class
AtomicIntegerFieldUpdater<T>

extends
Object
```

A reflection-based utility that enables atomic updates to
designated

volatile int

fields of designated classes.
This class is designed for use in atomic data structures in which
several fields of the same node are independently subject to atomic
updates.

Note that the guarantees of the

compareAndSet

method in this class are weaker than in other atomic classes.
Because this class cannot ensure that all uses of the field
are appropriate for purposes of atomic access, it can
guarantee atomicity only with respect to other invocations of

compareAndSet

and

set

on the same updater.

Object arguments for parameters of type

T

that are not
instances of the class passed to

newUpdater(java.lang.Class<U>, java.lang.String)

will result in
a

ClassCastException

being thrown.

**Since:** 1.5

public abstract class

AtomicIntegerFieldUpdater<T>

extends

Object

A reflection-based utility that enables atomic updates to
designated

volatile int

fields of designated classes.
This class is designed for use in atomic data structures in which
several fields of the same node are independently subject to atomic
updates.

Note that the guarantees of the

compareAndSet

method in this class are weaker than in other atomic classes.
Because this class cannot ensure that all uses of the field
are appropriate for purposes of atomic access, it can
guarantee atomicity only with respect to other invocations of

compareAndSet

and

set

on the same updater.

Object arguments for parameters of type

T

that are not
instances of the class passed to

newUpdater(java.lang.Class<U>, java.lang.String)

will result in
a

ClassCastException

being thrown.

Note that the guarantees of the

compareAndSet

method in this class are weaker than in other atomic classes.
Because this class cannot ensure that all uses of the field
are appropriate for purposes of atomic access, it can
guarantee atomicity only with respect to other invocations of

compareAndSet

and

set

on the same updater.

Object arguments for parameters of type

T

that are not
instances of the class passed to

newUpdater(java.lang.Class<U>, java.lang.String)

will result in
a

ClassCastException

being thrown.

Object arguments for parameters of type

T

that are not
instances of the class passed to

newUpdater(java.lang.Class<U>, java.lang.String)

will result in
a

ClassCastException

being thrown.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

AtomicIntegerFieldUpdater

()

Protected do-nothing constructor for use by subclasses.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

int

accumulateAndGet

​(

T

obj,
int x,

IntBinaryOperator

accumulatorFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the field of the given object managed
by this updater with the results of applying the given function
to the current and given values, returning the updated value.

int

addAndGet

​(

T

obj,
int delta)

Atomically adds the given value to the current value of the field of
the given object managed by this updater.

abstract boolean

compareAndSet

​(

T

obj,
int expect,
int update)

Atomically sets the field of the given object managed by this updater
to the given updated value if the current value

==

the
expected value.

int

decrementAndGet

​(

T

obj)

Atomically decrements by one the current value of the field of the
given object managed by this updater.

abstract int

get

​(

T

obj)

Returns the current value held in the field of the given object
managed by this updater.

int

getAndAccumulate

​(

T

obj,
int x,

IntBinaryOperator

accumulatorFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the field of the given object managed
by this updater with the results of applying the given function
to the current and given values, returning the previous value.

int

getAndAdd

​(

T

obj,
int delta)

Atomically adds the given value to the current value of the field of
the given object managed by this updater.

int

getAndDecrement

​(

T

obj)

Atomically decrements by one the current value of the field of the
given object managed by this updater.

int

getAndIncrement

​(

T

obj)

Atomically increments by one the current value of the field of the
given object managed by this updater.

int

getAndSet

​(

T

obj,
int newValue)

Atomically sets the field of the given object managed by this updater
to the given value and returns the old value.

int

getAndUpdate

​(

T

obj,

IntUnaryOperator

updateFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the field of the given object managed
by this updater with the results of applying the given
function, returning the previous value.

int

incrementAndGet

​(

T

obj)

Atomically increments by one the current value of the field of the
given object managed by this updater.

abstract void

lazySet

​(

T

obj,
int newValue)

Eventually sets the field of the given object managed by this
updater to the given updated value.

static <U>

AtomicIntegerFieldUpdater

<U>

newUpdater

​(

Class

<U> tclass,

String

fieldName)

Creates and returns an updater for objects with the given field.

abstract void

set

​(

T

obj,
int newValue)

Sets the field of the given object managed by this updater to the
given updated value.

int

updateAndGet

​(

T

obj,

IntUnaryOperator

updateFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the field of the given object managed
by this updater with the results of applying the given
function, returning the updated value.

abstract boolean

weakCompareAndSet

​(

T

obj,
int expect,
int update)

Atomically sets the field of the given object managed by this updater
to the given updated value if the current value

==

the
expected value.

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

toString

,

wait

,

wait

,

wait

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

AtomicIntegerFieldUpdater

()

Protected do-nothing constructor for use by subclasses.

---

#### Constructor Summary

Protected do-nothing constructor for use by subclasses.

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

int

accumulateAndGet

​(

T

obj,
int x,

IntBinaryOperator

accumulatorFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the field of the given object managed
by this updater with the results of applying the given function
to the current and given values, returning the updated value.

int

addAndGet

​(

T

obj,
int delta)

Atomically adds the given value to the current value of the field of
the given object managed by this updater.

abstract boolean

compareAndSet

​(

T

obj,
int expect,
int update)

Atomically sets the field of the given object managed by this updater
to the given updated value if the current value

==

the
expected value.

int

decrementAndGet

​(

T

obj)

Atomically decrements by one the current value of the field of the
given object managed by this updater.

abstract int

get

​(

T

obj)

Returns the current value held in the field of the given object
managed by this updater.

int

getAndAccumulate

​(

T

obj,
int x,

IntBinaryOperator

accumulatorFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the field of the given object managed
by this updater with the results of applying the given function
to the current and given values, returning the previous value.

int

getAndAdd

​(

T

obj,
int delta)

Atomically adds the given value to the current value of the field of
the given object managed by this updater.

int

getAndDecrement

​(

T

obj)

Atomically decrements by one the current value of the field of the
given object managed by this updater.

int

getAndIncrement

​(

T

obj)

Atomically increments by one the current value of the field of the
given object managed by this updater.

int

getAndSet

​(

T

obj,
int newValue)

Atomically sets the field of the given object managed by this updater
to the given value and returns the old value.

int

getAndUpdate

​(

T

obj,

IntUnaryOperator

updateFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the field of the given object managed
by this updater with the results of applying the given
function, returning the previous value.

int

incrementAndGet

​(

T

obj)

Atomically increments by one the current value of the field of the
given object managed by this updater.

abstract void

lazySet

​(

T

obj,
int newValue)

Eventually sets the field of the given object managed by this
updater to the given updated value.

static <U>

AtomicIntegerFieldUpdater

<U>

newUpdater

​(

Class

<U> tclass,

String

fieldName)

Creates and returns an updater for objects with the given field.

abstract void

set

​(

T

obj,
int newValue)

Sets the field of the given object managed by this updater to the
given updated value.

int

updateAndGet

​(

T

obj,

IntUnaryOperator

updateFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the field of the given object managed
by this updater with the results of applying the given
function, returning the updated value.

abstract boolean

weakCompareAndSet

​(

T

obj,
int expect,
int update)

Atomically sets the field of the given object managed by this updater
to the given updated value if the current value

==

the
expected value.

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

toString

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

) the field of the given object managed
by this updater with the results of applying the given function
to the current and given values, returning the updated value.

Atomically adds the given value to the current value of the field of
the given object managed by this updater.

Atomically sets the field of the given object managed by this updater
to the given updated value if the current value

==

the
expected value.

Atomically decrements by one the current value of the field of the
given object managed by this updater.

Returns the current value held in the field of the given object
managed by this updater.

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the field of the given object managed
by this updater with the results of applying the given function
to the current and given values, returning the previous value.

Atomically increments by one the current value of the field of the
given object managed by this updater.

Atomically sets the field of the given object managed by this updater
to the given value and returns the old value.

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the field of the given object managed
by this updater with the results of applying the given
function, returning the previous value.

Eventually sets the field of the given object managed by this
updater to the given updated value.

Creates and returns an updater for objects with the given field.

Sets the field of the given object managed by this updater to the
given updated value.

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the field of the given object managed
by this updater with the results of applying the given
function, returning the updated value.

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

toString

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

- AtomicIntegerFieldUpdater

```java
protected AtomicIntegerFieldUpdater()
```

Protected do-nothing constructor for use by subclasses.

============ METHOD DETAIL ==========

- Method Detail

- newUpdater

```java
public static <U>
AtomicIntegerFieldUpdater
<U> newUpdater​(
Class
<U> tclass,

String
fieldName)
```

Creates and returns an updater for objects with the given field.
The Class argument is needed to check that reflective types and
generic types match.

**Type Parameters:** U

- the type of instances of tclass
**Parameters:** tclass

- the class of the objects holding the field
**Parameters:** fieldName

- the name of the field to be updated
**Returns:** the updater
**Throws:** IllegalArgumentException

- if the field is not a
volatile integer type
**Throws:** RuntimeException

- with a nested reflection-based
exception if the class does not hold field or is the wrong type,
or the field is inaccessible to the caller according to Java language
access control

- compareAndSet

```java
public abstract boolean compareAndSet​(
T
obj,
int expect,
int update)
```

Atomically sets the field of the given object managed by this updater
to the given updated value if the current value

==

the
expected value. This method is guaranteed to be atomic with respect to
other calls to

compareAndSet

and

set

, but not
necessarily with respect to other changes in the field.

**Parameters:** obj

- An object whose field to conditionally set
**Parameters:** expect

- the expected value
**Parameters:** update

- the new value
**Returns:** true

if successful

- weakCompareAndSet

```java
public abstract boolean weakCompareAndSet​(
T
obj,
int expect,
int update)
```

Atomically sets the field of the given object managed by this updater
to the given updated value if the current value

==

the
expected value. This method is guaranteed to be atomic with respect to
other calls to

compareAndSet

and

set

, but not
necessarily with respect to other changes in the field.

May fail
spuriously and does not provide ordering guarantees

, so is
only rarely an appropriate alternative to

compareAndSet

.

**Parameters:** obj

- An object whose field to conditionally set
**Parameters:** expect

- the expected value
**Parameters:** update

- the new value
**Returns:** true

if successful

- set

```java
public abstract void set​(
T
obj,
int newValue)
```

Sets the field of the given object managed by this updater to the
given updated value. This operation is guaranteed to act as a volatile
store with respect to subsequent invocations of

compareAndSet

.

**Parameters:** obj

- An object whose field to set
**Parameters:** newValue

- the new value

- lazySet

```java
public abstract void lazySet​(
T
obj,
int newValue)
```

Eventually sets the field of the given object managed by this
updater to the given updated value.

**Parameters:** obj

- An object whose field to set
**Parameters:** newValue

- the new value
**Since:** 1.6

- get

```java
public abstract int get​(
T
obj)
```

Returns the current value held in the field of the given object
managed by this updater.

**Parameters:** obj

- An object whose field to get
**Returns:** the current value

- getAndSet

```java
public int getAndSet​(
T
obj,
int newValue)
```

Atomically sets the field of the given object managed by this updater
to the given value and returns the old value.

**Parameters:** obj

- An object whose field to get and set
**Parameters:** newValue

- the new value
**Returns:** the previous value

- getAndIncrement

```java
public int getAndIncrement​(
T
obj)
```

Atomically increments by one the current value of the field of the
given object managed by this updater.

**Parameters:** obj

- An object whose field to get and set
**Returns:** the previous value

- getAndDecrement

```java
public int getAndDecrement​(
T
obj)
```

Atomically decrements by one the current value of the field of the
given object managed by this updater.

**Parameters:** obj

- An object whose field to get and set
**Returns:** the previous value

- getAndAdd

```java
public int getAndAdd​(
T
obj,
int delta)
```

Atomically adds the given value to the current value of the field of
the given object managed by this updater.

**Parameters:** obj

- An object whose field to get and set
**Parameters:** delta

- the value to add
**Returns:** the previous value

- incrementAndGet

```java
public int incrementAndGet​(
T
obj)
```

Atomically increments by one the current value of the field of the
given object managed by this updater.

**Parameters:** obj

- An object whose field to get and set
**Returns:** the updated value

- decrementAndGet

```java
public int decrementAndGet​(
T
obj)
```

Atomically decrements by one the current value of the field of the
given object managed by this updater.

**Parameters:** obj

- An object whose field to get and set
**Returns:** the updated value

- addAndGet

```java
public int addAndGet​(
T
obj,
int delta)
```

Atomically adds the given value to the current value of the field of
the given object managed by this updater.

**Parameters:** obj

- An object whose field to get and set
**Parameters:** delta

- the value to add
**Returns:** the updated value

- getAndUpdate

```java
public final int getAndUpdate​(
T
obj,

IntUnaryOperator
updateFunction)
```

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the field of the given object managed
by this updater with the results of applying the given
function, returning the previous value. The function should be
side-effect-free, since it may be re-applied when attempted
updates fail due to contention among threads.

**Parameters:** obj

- An object whose field to get and set
**Parameters:** updateFunction

- a side-effect-free function
**Returns:** the previous value
**Since:** 1.8

- updateAndGet

```java
public final int updateAndGet​(
T
obj,

IntUnaryOperator
updateFunction)
```

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the field of the given object managed
by this updater with the results of applying the given
function, returning the updated value. The function should be
side-effect-free, since it may be re-applied when attempted
updates fail due to contention among threads.

**Parameters:** obj

- An object whose field to get and set
**Parameters:** updateFunction

- a side-effect-free function
**Returns:** the updated value
**Since:** 1.8

- getAndAccumulate

```java
public final int getAndAccumulate​(
T
obj,
int x,

IntBinaryOperator
accumulatorFunction)
```

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the field of the given object managed
by this updater with the results of applying the given function
to the current and given values, returning the previous value.
The function should be side-effect-free, since it may be
re-applied when attempted updates fail due to contention among
threads. The function is applied with the current value as its
first argument, and the given update as the second argument.

**Parameters:** obj

- An object whose field to get and set
**Parameters:** x

- the update value
**Parameters:** accumulatorFunction

- a side-effect-free function of two arguments
**Returns:** the previous value
**Since:** 1.8

- accumulateAndGet

```java
public final int accumulateAndGet​(
T
obj,
int x,

IntBinaryOperator
accumulatorFunction)
```

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the field of the given object managed
by this updater with the results of applying the given function
to the current and given values, returning the updated value.
The function should be side-effect-free, since it may be
re-applied when attempted updates fail due to contention among
threads. The function is applied with the current value as its
first argument, and the given update as the second argument.

**Parameters:** obj

- An object whose field to get and set
**Parameters:** x

- the update value
**Parameters:** accumulatorFunction

- a side-effect-free function of two arguments
**Returns:** the updated value
**Since:** 1.8

Constructor Detail

- AtomicIntegerFieldUpdater

```java
protected AtomicIntegerFieldUpdater()
```

Protected do-nothing constructor for use by subclasses.

---

#### Constructor Detail

AtomicIntegerFieldUpdater

```java
protected AtomicIntegerFieldUpdater()
```

Protected do-nothing constructor for use by subclasses.

---

#### AtomicIntegerFieldUpdater

protected AtomicIntegerFieldUpdater()

Protected do-nothing constructor for use by subclasses.

Method Detail

- newUpdater

```java
public static <U>
AtomicIntegerFieldUpdater
<U> newUpdater​(
Class
<U> tclass,

String
fieldName)
```

Creates and returns an updater for objects with the given field.
The Class argument is needed to check that reflective types and
generic types match.

**Type Parameters:** U

- the type of instances of tclass
**Parameters:** tclass

- the class of the objects holding the field
**Parameters:** fieldName

- the name of the field to be updated
**Returns:** the updater
**Throws:** IllegalArgumentException

- if the field is not a
volatile integer type
**Throws:** RuntimeException

- with a nested reflection-based
exception if the class does not hold field or is the wrong type,
or the field is inaccessible to the caller according to Java language
access control

- compareAndSet

```java
public abstract boolean compareAndSet​(
T
obj,
int expect,
int update)
```

Atomically sets the field of the given object managed by this updater
to the given updated value if the current value

==

the
expected value. This method is guaranteed to be atomic with respect to
other calls to

compareAndSet

and

set

, but not
necessarily with respect to other changes in the field.

**Parameters:** obj

- An object whose field to conditionally set
**Parameters:** expect

- the expected value
**Parameters:** update

- the new value
**Returns:** true

if successful

- weakCompareAndSet

```java
public abstract boolean weakCompareAndSet​(
T
obj,
int expect,
int update)
```

Atomically sets the field of the given object managed by this updater
to the given updated value if the current value

==

the
expected value. This method is guaranteed to be atomic with respect to
other calls to

compareAndSet

and

set

, but not
necessarily with respect to other changes in the field.

May fail
spuriously and does not provide ordering guarantees

, so is
only rarely an appropriate alternative to

compareAndSet

.

**Parameters:** obj

- An object whose field to conditionally set
**Parameters:** expect

- the expected value
**Parameters:** update

- the new value
**Returns:** true

if successful

- set

```java
public abstract void set​(
T
obj,
int newValue)
```

Sets the field of the given object managed by this updater to the
given updated value. This operation is guaranteed to act as a volatile
store with respect to subsequent invocations of

compareAndSet

.

**Parameters:** obj

- An object whose field to set
**Parameters:** newValue

- the new value

- lazySet

```java
public abstract void lazySet​(
T
obj,
int newValue)
```

Eventually sets the field of the given object managed by this
updater to the given updated value.

**Parameters:** obj

- An object whose field to set
**Parameters:** newValue

- the new value
**Since:** 1.6

- get

```java
public abstract int get​(
T
obj)
```

Returns the current value held in the field of the given object
managed by this updater.

**Parameters:** obj

- An object whose field to get
**Returns:** the current value

- getAndSet

```java
public int getAndSet​(
T
obj,
int newValue)
```

Atomically sets the field of the given object managed by this updater
to the given value and returns the old value.

**Parameters:** obj

- An object whose field to get and set
**Parameters:** newValue

- the new value
**Returns:** the previous value

- getAndIncrement

```java
public int getAndIncrement​(
T
obj)
```

Atomically increments by one the current value of the field of the
given object managed by this updater.

**Parameters:** obj

- An object whose field to get and set
**Returns:** the previous value

- getAndDecrement

```java
public int getAndDecrement​(
T
obj)
```

Atomically decrements by one the current value of the field of the
given object managed by this updater.

**Parameters:** obj

- An object whose field to get and set
**Returns:** the previous value

- getAndAdd

```java
public int getAndAdd​(
T
obj,
int delta)
```

Atomically adds the given value to the current value of the field of
the given object managed by this updater.

**Parameters:** obj

- An object whose field to get and set
**Parameters:** delta

- the value to add
**Returns:** the previous value

- incrementAndGet

```java
public int incrementAndGet​(
T
obj)
```

Atomically increments by one the current value of the field of the
given object managed by this updater.

**Parameters:** obj

- An object whose field to get and set
**Returns:** the updated value

- decrementAndGet

```java
public int decrementAndGet​(
T
obj)
```

Atomically decrements by one the current value of the field of the
given object managed by this updater.

**Parameters:** obj

- An object whose field to get and set
**Returns:** the updated value

- addAndGet

```java
public int addAndGet​(
T
obj,
int delta)
```

Atomically adds the given value to the current value of the field of
the given object managed by this updater.

**Parameters:** obj

- An object whose field to get and set
**Parameters:** delta

- the value to add
**Returns:** the updated value

- getAndUpdate

```java
public final int getAndUpdate​(
T
obj,

IntUnaryOperator
updateFunction)
```

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the field of the given object managed
by this updater with the results of applying the given
function, returning the previous value. The function should be
side-effect-free, since it may be re-applied when attempted
updates fail due to contention among threads.

**Parameters:** obj

- An object whose field to get and set
**Parameters:** updateFunction

- a side-effect-free function
**Returns:** the previous value
**Since:** 1.8

- updateAndGet

```java
public final int updateAndGet​(
T
obj,

IntUnaryOperator
updateFunction)
```

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the field of the given object managed
by this updater with the results of applying the given
function, returning the updated value. The function should be
side-effect-free, since it may be re-applied when attempted
updates fail due to contention among threads.

**Parameters:** obj

- An object whose field to get and set
**Parameters:** updateFunction

- a side-effect-free function
**Returns:** the updated value
**Since:** 1.8

- getAndAccumulate

```java
public final int getAndAccumulate​(
T
obj,
int x,

IntBinaryOperator
accumulatorFunction)
```

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the field of the given object managed
by this updater with the results of applying the given function
to the current and given values, returning the previous value.
The function should be side-effect-free, since it may be
re-applied when attempted updates fail due to contention among
threads. The function is applied with the current value as its
first argument, and the given update as the second argument.

**Parameters:** obj

- An object whose field to get and set
**Parameters:** x

- the update value
**Parameters:** accumulatorFunction

- a side-effect-free function of two arguments
**Returns:** the previous value
**Since:** 1.8

- accumulateAndGet

```java
public final int accumulateAndGet​(
T
obj,
int x,

IntBinaryOperator
accumulatorFunction)
```

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the field of the given object managed
by this updater with the results of applying the given function
to the current and given values, returning the updated value.
The function should be side-effect-free, since it may be
re-applied when attempted updates fail due to contention among
threads. The function is applied with the current value as its
first argument, and the given update as the second argument.

**Parameters:** obj

- An object whose field to get and set
**Parameters:** x

- the update value
**Parameters:** accumulatorFunction

- a side-effect-free function of two arguments
**Returns:** the updated value
**Since:** 1.8

---

#### Method Detail

newUpdater

```java
public static <U>
AtomicIntegerFieldUpdater
<U> newUpdater​(
Class
<U> tclass,

String
fieldName)
```

Creates and returns an updater for objects with the given field.
The Class argument is needed to check that reflective types and
generic types match.

**Type Parameters:** U

- the type of instances of tclass
**Parameters:** tclass

- the class of the objects holding the field
**Parameters:** fieldName

- the name of the field to be updated
**Returns:** the updater
**Throws:** IllegalArgumentException

- if the field is not a
volatile integer type
**Throws:** RuntimeException

- with a nested reflection-based
exception if the class does not hold field or is the wrong type,
or the field is inaccessible to the caller according to Java language
access control

---

#### newUpdater

public static <U>

AtomicIntegerFieldUpdater

<U> newUpdater​(

Class

<U> tclass,

String

fieldName)

Creates and returns an updater for objects with the given field.
The Class argument is needed to check that reflective types and
generic types match.

compareAndSet

```java
public abstract boolean compareAndSet​(
T
obj,
int expect,
int update)
```

Atomically sets the field of the given object managed by this updater
to the given updated value if the current value

==

the
expected value. This method is guaranteed to be atomic with respect to
other calls to

compareAndSet

and

set

, but not
necessarily with respect to other changes in the field.

**Parameters:** obj

- An object whose field to conditionally set
**Parameters:** expect

- the expected value
**Parameters:** update

- the new value
**Returns:** true

if successful

---

#### compareAndSet

public abstract boolean compareAndSet​(

T

obj,
int expect,
int update)

Atomically sets the field of the given object managed by this updater
to the given updated value if the current value

==

the
expected value. This method is guaranteed to be atomic with respect to
other calls to

compareAndSet

and

set

, but not
necessarily with respect to other changes in the field.

weakCompareAndSet

```java
public abstract boolean weakCompareAndSet​(
T
obj,
int expect,
int update)
```

Atomically sets the field of the given object managed by this updater
to the given updated value if the current value

==

the
expected value. This method is guaranteed to be atomic with respect to
other calls to

compareAndSet

and

set

, but not
necessarily with respect to other changes in the field.

May fail
spuriously and does not provide ordering guarantees

, so is
only rarely an appropriate alternative to

compareAndSet

.

**Parameters:** obj

- An object whose field to conditionally set
**Parameters:** expect

- the expected value
**Parameters:** update

- the new value
**Returns:** true

if successful

---

#### weakCompareAndSet

public abstract boolean weakCompareAndSet​(

T

obj,
int expect,
int update)

Atomically sets the field of the given object managed by this updater
to the given updated value if the current value

==

the
expected value. This method is guaranteed to be atomic with respect to
other calls to

compareAndSet

and

set

, but not
necessarily with respect to other changes in the field.

May fail
spuriously and does not provide ordering guarantees

, so is
only rarely an appropriate alternative to

compareAndSet

.

May fail
spuriously and does not provide ordering guarantees

, so is
only rarely an appropriate alternative to

compareAndSet

.

set

```java
public abstract void set​(
T
obj,
int newValue)
```

Sets the field of the given object managed by this updater to the
given updated value. This operation is guaranteed to act as a volatile
store with respect to subsequent invocations of

compareAndSet

.

**Parameters:** obj

- An object whose field to set
**Parameters:** newValue

- the new value

---

#### set

public abstract void set​(

T

obj,
int newValue)

Sets the field of the given object managed by this updater to the
given updated value. This operation is guaranteed to act as a volatile
store with respect to subsequent invocations of

compareAndSet

.

lazySet

```java
public abstract void lazySet​(
T
obj,
int newValue)
```

Eventually sets the field of the given object managed by this
updater to the given updated value.

**Parameters:** obj

- An object whose field to set
**Parameters:** newValue

- the new value
**Since:** 1.6

---

#### lazySet

public abstract void lazySet​(

T

obj,
int newValue)

Eventually sets the field of the given object managed by this
updater to the given updated value.

get

```java
public abstract int get​(
T
obj)
```

Returns the current value held in the field of the given object
managed by this updater.

**Parameters:** obj

- An object whose field to get
**Returns:** the current value

---

#### get

public abstract int get​(

T

obj)

Returns the current value held in the field of the given object
managed by this updater.

getAndSet

```java
public int getAndSet​(
T
obj,
int newValue)
```

Atomically sets the field of the given object managed by this updater
to the given value and returns the old value.

**Parameters:** obj

- An object whose field to get and set
**Parameters:** newValue

- the new value
**Returns:** the previous value

---

#### getAndSet

public int getAndSet​(

T

obj,
int newValue)

Atomically sets the field of the given object managed by this updater
to the given value and returns the old value.

getAndIncrement

```java
public int getAndIncrement​(
T
obj)
```

Atomically increments by one the current value of the field of the
given object managed by this updater.

**Parameters:** obj

- An object whose field to get and set
**Returns:** the previous value

---

#### getAndIncrement

public int getAndIncrement​(

T

obj)

Atomically increments by one the current value of the field of the
given object managed by this updater.

getAndDecrement

```java
public int getAndDecrement​(
T
obj)
```

Atomically decrements by one the current value of the field of the
given object managed by this updater.

**Parameters:** obj

- An object whose field to get and set
**Returns:** the previous value

---

#### getAndDecrement

public int getAndDecrement​(

T

obj)

Atomically decrements by one the current value of the field of the
given object managed by this updater.

getAndAdd

```java
public int getAndAdd​(
T
obj,
int delta)
```

Atomically adds the given value to the current value of the field of
the given object managed by this updater.

**Parameters:** obj

- An object whose field to get and set
**Parameters:** delta

- the value to add
**Returns:** the previous value

---

#### getAndAdd

public int getAndAdd​(

T

obj,
int delta)

Atomically adds the given value to the current value of the field of
the given object managed by this updater.

incrementAndGet

```java
public int incrementAndGet​(
T
obj)
```

Atomically increments by one the current value of the field of the
given object managed by this updater.

**Parameters:** obj

- An object whose field to get and set
**Returns:** the updated value

---

#### incrementAndGet

public int incrementAndGet​(

T

obj)

Atomically increments by one the current value of the field of the
given object managed by this updater.

decrementAndGet

```java
public int decrementAndGet​(
T
obj)
```

Atomically decrements by one the current value of the field of the
given object managed by this updater.

**Parameters:** obj

- An object whose field to get and set
**Returns:** the updated value

---

#### decrementAndGet

public int decrementAndGet​(

T

obj)

Atomically decrements by one the current value of the field of the
given object managed by this updater.

addAndGet

```java
public int addAndGet​(
T
obj,
int delta)
```

Atomically adds the given value to the current value of the field of
the given object managed by this updater.

**Parameters:** obj

- An object whose field to get and set
**Parameters:** delta

- the value to add
**Returns:** the updated value

---

#### addAndGet

public int addAndGet​(

T

obj,
int delta)

Atomically adds the given value to the current value of the field of
the given object managed by this updater.

getAndUpdate

```java
public final int getAndUpdate​(
T
obj,

IntUnaryOperator
updateFunction)
```

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the field of the given object managed
by this updater with the results of applying the given
function, returning the previous value. The function should be
side-effect-free, since it may be re-applied when attempted
updates fail due to contention among threads.

**Parameters:** obj

- An object whose field to get and set
**Parameters:** updateFunction

- a side-effect-free function
**Returns:** the previous value
**Since:** 1.8

---

#### getAndUpdate

public final int getAndUpdate​(

T

obj,

IntUnaryOperator

updateFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the field of the given object managed
by this updater with the results of applying the given
function, returning the previous value. The function should be
side-effect-free, since it may be re-applied when attempted
updates fail due to contention among threads.

updateAndGet

```java
public final int updateAndGet​(
T
obj,

IntUnaryOperator
updateFunction)
```

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the field of the given object managed
by this updater with the results of applying the given
function, returning the updated value. The function should be
side-effect-free, since it may be re-applied when attempted
updates fail due to contention among threads.

**Parameters:** obj

- An object whose field to get and set
**Parameters:** updateFunction

- a side-effect-free function
**Returns:** the updated value
**Since:** 1.8

---

#### updateAndGet

public final int updateAndGet​(

T

obj,

IntUnaryOperator

updateFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the field of the given object managed
by this updater with the results of applying the given
function, returning the updated value. The function should be
side-effect-free, since it may be re-applied when attempted
updates fail due to contention among threads.

getAndAccumulate

```java
public final int getAndAccumulate​(
T
obj,
int x,

IntBinaryOperator
accumulatorFunction)
```

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the field of the given object managed
by this updater with the results of applying the given function
to the current and given values, returning the previous value.
The function should be side-effect-free, since it may be
re-applied when attempted updates fail due to contention among
threads. The function is applied with the current value as its
first argument, and the given update as the second argument.

**Parameters:** obj

- An object whose field to get and set
**Parameters:** x

- the update value
**Parameters:** accumulatorFunction

- a side-effect-free function of two arguments
**Returns:** the previous value
**Since:** 1.8

---

#### getAndAccumulate

public final int getAndAccumulate​(

T

obj,
int x,

IntBinaryOperator

accumulatorFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the field of the given object managed
by this updater with the results of applying the given function
to the current and given values, returning the previous value.
The function should be side-effect-free, since it may be
re-applied when attempted updates fail due to contention among
threads. The function is applied with the current value as its
first argument, and the given update as the second argument.

accumulateAndGet

```java
public final int accumulateAndGet​(
T
obj,
int x,

IntBinaryOperator
accumulatorFunction)
```

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the field of the given object managed
by this updater with the results of applying the given function
to the current and given values, returning the updated value.
The function should be side-effect-free, since it may be
re-applied when attempted updates fail due to contention among
threads. The function is applied with the current value as its
first argument, and the given update as the second argument.

**Parameters:** obj

- An object whose field to get and set
**Parameters:** x

- the update value
**Parameters:** accumulatorFunction

- a side-effect-free function of two arguments
**Returns:** the updated value
**Since:** 1.8

---

#### accumulateAndGet

public final int accumulateAndGet​(

T

obj,
int x,

IntBinaryOperator

accumulatorFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the field of the given object managed
by this updater with the results of applying the given function
to the current and given values, returning the updated value.
The function should be side-effect-free, since it may be
re-applied when attempted updates fail due to contention among
threads. The function is applied with the current value as its
first argument, and the given update as the second argument.

---

