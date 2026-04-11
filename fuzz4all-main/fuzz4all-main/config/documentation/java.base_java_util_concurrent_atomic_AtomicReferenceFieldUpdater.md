# Class AtomicReferenceFieldUpdater<T,​V>

**Source:** `java.base\java\util\concurrent\atomic\AtomicReferenceFieldUpdater.html`

### Class Description

```java
public abstract class
AtomicReferenceFieldUpdater<T,​V>

extends
Object
```

A reflection-based utility that enables atomic updates to
designated

volatile

reference fields of designated
classes. This class is designed for use in atomic data structures
in which several reference fields of the same node are
independently subject to atomic updates. For example, a tree node
might be declared as

```java
class Node {
private volatile Node left, right;

private static final AtomicReferenceFieldUpdater<Node, Node> leftUpdater =
AtomicReferenceFieldUpdater.newUpdater(Node.class, Node.class, "left");
private static AtomicReferenceFieldUpdater<Node, Node> rightUpdater =
AtomicReferenceFieldUpdater.newUpdater(Node.class, Node.class, "right");

Node getLeft() { return left; }
boolean compareAndSetLeft(Node expect, Node update) {
return leftUpdater.compareAndSet(this, expect, update);
}
// ... and so on
}
```

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

newUpdater(java.lang.Class<U>, java.lang.Class<W>, java.lang.String)

will result in
a

ClassCastException

being thrown.

**Type Parameters:** T

- The type of the object holding the updatable field
**Type Parameters:** V

- The type of the field

---

### Field Details

*No entries found.*

### Constructor Details

#### protected AtomicReferenceFieldUpdater()

Protected do-nothing constructor for use by subclasses.

---

### Method Details

#### public static <U,​W>
AtomicReferenceFieldUpdater
<U,​W> newUpdater​(
Class
<U> tclass,

Class
<W> vclass,

String
fieldName)

Creates and returns an updater for objects with the given field.
The Class arguments are needed to check that reflective types and
generic types match.

**Parameters:**
- tclass

- the class of the objects holding the field
- vclass

- the class of the field
- fieldName

- the name of the field to be updated

**Returns:**
- the updater

**Throws:**
- ClassCastException

- if the field is of the wrong type
- IllegalArgumentException

- if the field is not volatile
- RuntimeException

- with a nested reflection-based
exception if the class does not hold field or is the wrong type,
or the field is inaccessible to the caller according to Java language
access control

**Type Parameters:**
- U

- the type of instances of tclass
- W

- the type of instances of vclass

---

#### public abstract boolean compareAndSet​(
T
obj,

V
expect,

V
update)

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

V
expect,

V
update)

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

V
newValue)

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

V
newValue)

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

#### public abstract
V
get​(
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

#### public
V
getAndSet​(
T
obj,

V
newValue)

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

#### public final
V
getAndUpdate​(
T
obj,

UnaryOperator
<
V
> updateFunction)

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

#### public final
V
updateAndGet​(
T
obj,

UnaryOperator
<
V
> updateFunction)

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

#### public final
V
getAndAccumulate​(
T
obj,

V
x,

BinaryOperator
<
V
> accumulatorFunction)

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

#### public final
V
accumulateAndGet​(
T
obj,

V
x,

BinaryOperator
<
V
> accumulatorFunction)

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

#### Class AtomicReferenceFieldUpdater<T,​V>

java.lang.Object

- java.util.concurrent.atomic.AtomicReferenceFieldUpdater<T,​V>

java.util.concurrent.atomic.AtomicReferenceFieldUpdater<T,​V>

**Type Parameters:** T

- The type of the object holding the updatable field
**Type Parameters:** V

- The type of the field

```java
public abstract class
AtomicReferenceFieldUpdater<T,​V>

extends
Object
```

A reflection-based utility that enables atomic updates to
designated

volatile

reference fields of designated
classes. This class is designed for use in atomic data structures
in which several reference fields of the same node are
independently subject to atomic updates. For example, a tree node
might be declared as

```java
class Node {
private volatile Node left, right;

private static final AtomicReferenceFieldUpdater<Node, Node> leftUpdater =
AtomicReferenceFieldUpdater.newUpdater(Node.class, Node.class, "left");
private static AtomicReferenceFieldUpdater<Node, Node> rightUpdater =
AtomicReferenceFieldUpdater.newUpdater(Node.class, Node.class, "right");

Node getLeft() { return left; }
boolean compareAndSetLeft(Node expect, Node update) {
return leftUpdater.compareAndSet(this, expect, update);
}
// ... and so on
}
```

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

newUpdater(java.lang.Class<U>, java.lang.Class<W>, java.lang.String)

will result in
a

ClassCastException

being thrown.

**Since:** 1.5

public abstract class

AtomicReferenceFieldUpdater<T,​V>

extends

Object

A reflection-based utility that enables atomic updates to
designated

volatile

reference fields of designated
classes. This class is designed for use in atomic data structures
in which several reference fields of the same node are
independently subject to atomic updates. For example, a tree node
might be declared as

```java
class Node {
private volatile Node left, right;

private static final AtomicReferenceFieldUpdater<Node, Node> leftUpdater =
AtomicReferenceFieldUpdater.newUpdater(Node.class, Node.class, "left");
private static AtomicReferenceFieldUpdater<Node, Node> rightUpdater =
AtomicReferenceFieldUpdater.newUpdater(Node.class, Node.class, "right");

Node getLeft() { return left; }
boolean compareAndSetLeft(Node expect, Node update) {
return leftUpdater.compareAndSet(this, expect, update);
}
// ... and so on
}
```

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

newUpdater(java.lang.Class<U>, java.lang.Class<W>, java.lang.String)

will result in
a

ClassCastException

being thrown.

class Node {
private volatile Node left, right;

private static final AtomicReferenceFieldUpdater<Node, Node> leftUpdater =
AtomicReferenceFieldUpdater.newUpdater(Node.class, Node.class, "left");
private static AtomicReferenceFieldUpdater<Node, Node> rightUpdater =
AtomicReferenceFieldUpdater.newUpdater(Node.class, Node.class, "right");

Node getLeft() { return left; }
boolean compareAndSetLeft(Node expect, Node update) {
return leftUpdater.compareAndSet(this, expect, update);
}
// ... and so on
}

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

newUpdater(java.lang.Class<U>, java.lang.Class<W>, java.lang.String)

will result in
a

ClassCastException

being thrown.

Object arguments for parameters of type

T

that are not
instances of the class passed to

newUpdater(java.lang.Class<U>, java.lang.Class<W>, java.lang.String)

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

AtomicReferenceFieldUpdater

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

V

accumulateAndGet

​(

T

obj,

V

x,

BinaryOperator

<

V

> accumulatorFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the field of the given object managed
by this updater with the results of applying the given function
to the current and given values, returning the updated value.

abstract boolean

compareAndSet

​(

T

obj,

V

expect,

V

update)

Atomically sets the field of the given object managed by this updater
to the given updated value if the current value

==

the
expected value.

abstract

V

get

​(

T

obj)

Returns the current value held in the field of the given object
managed by this updater.

V

getAndAccumulate

​(

T

obj,

V

x,

BinaryOperator

<

V

> accumulatorFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the field of the given object managed
by this updater with the results of applying the given function
to the current and given values, returning the previous value.

V

getAndSet

​(

T

obj,

V

newValue)

Atomically sets the field of the given object managed by this updater
to the given value and returns the old value.

V

getAndUpdate

​(

T

obj,

UnaryOperator

<

V

> updateFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the field of the given object managed
by this updater with the results of applying the given
function, returning the previous value.

abstract void

lazySet

​(

T

obj,

V

newValue)

Eventually sets the field of the given object managed by this
updater to the given updated value.

static <U,​W>

AtomicReferenceFieldUpdater

<U,​W>

newUpdater

​(

Class

<U> tclass,

Class

<W> vclass,

String

fieldName)

Creates and returns an updater for objects with the given field.

abstract void

set

​(

T

obj,

V

newValue)

Sets the field of the given object managed by this updater to the
given updated value.

V

updateAndGet

​(

T

obj,

UnaryOperator

<

V

> updateFunction)

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

V

expect,

V

update)

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

AtomicReferenceFieldUpdater

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

V

accumulateAndGet

​(

T

obj,

V

x,

BinaryOperator

<

V

> accumulatorFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the field of the given object managed
by this updater with the results of applying the given function
to the current and given values, returning the updated value.

abstract boolean

compareAndSet

​(

T

obj,

V

expect,

V

update)

Atomically sets the field of the given object managed by this updater
to the given updated value if the current value

==

the
expected value.

abstract

V

get

​(

T

obj)

Returns the current value held in the field of the given object
managed by this updater.

V

getAndAccumulate

​(

T

obj,

V

x,

BinaryOperator

<

V

> accumulatorFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the field of the given object managed
by this updater with the results of applying the given function
to the current and given values, returning the previous value.

V

getAndSet

​(

T

obj,

V

newValue)

Atomically sets the field of the given object managed by this updater
to the given value and returns the old value.

V

getAndUpdate

​(

T

obj,

UnaryOperator

<

V

> updateFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the field of the given object managed
by this updater with the results of applying the given
function, returning the previous value.

abstract void

lazySet

​(

T

obj,

V

newValue)

Eventually sets the field of the given object managed by this
updater to the given updated value.

static <U,​W>

AtomicReferenceFieldUpdater

<U,​W>

newUpdater

​(

Class

<U> tclass,

Class

<W> vclass,

String

fieldName)

Creates and returns an updater for objects with the given field.

abstract void

set

​(

T

obj,

V

newValue)

Sets the field of the given object managed by this updater to the
given updated value.

V

updateAndGet

​(

T

obj,

UnaryOperator

<

V

> updateFunction)

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

V

expect,

V

update)

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

Atomically sets the field of the given object managed by this updater
to the given updated value if the current value

==

the
expected value.

Returns the current value held in the field of the given object
managed by this updater.

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the field of the given object managed
by this updater with the results of applying the given function
to the current and given values, returning the previous value.

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

- AtomicReferenceFieldUpdater

```java
protected AtomicReferenceFieldUpdater()
```

Protected do-nothing constructor for use by subclasses.

============ METHOD DETAIL ==========

- Method Detail

- newUpdater

```java
public static <U,​W>
AtomicReferenceFieldUpdater
<U,​W> newUpdater​(
Class
<U> tclass,

Class
<W> vclass,

String
fieldName)
```

Creates and returns an updater for objects with the given field.
The Class arguments are needed to check that reflective types and
generic types match.

**Type Parameters:** U

- the type of instances of tclass
**Type Parameters:** W

- the type of instances of vclass
**Parameters:** tclass

- the class of the objects holding the field
**Parameters:** vclass

- the class of the field
**Parameters:** fieldName

- the name of the field to be updated
**Returns:** the updater
**Throws:** ClassCastException

- if the field is of the wrong type
**Throws:** IllegalArgumentException

- if the field is not volatile
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

V
expect,

V
update)
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

V
expect,

V
update)
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

V
newValue)
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

V
newValue)
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
public abstract
V
get​(
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
public
V
getAndSet​(
T
obj,

V
newValue)
```

Atomically sets the field of the given object managed by this updater
to the given value and returns the old value.

**Parameters:** obj

- An object whose field to get and set
**Parameters:** newValue

- the new value
**Returns:** the previous value

- getAndUpdate

```java
public final
V
getAndUpdate​(
T
obj,

UnaryOperator
<
V
> updateFunction)
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
public final
V
updateAndGet​(
T
obj,

UnaryOperator
<
V
> updateFunction)
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
public final
V
getAndAccumulate​(
T
obj,

V
x,

BinaryOperator
<
V
> accumulatorFunction)
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
public final
V
accumulateAndGet​(
T
obj,

V
x,

BinaryOperator
<
V
> accumulatorFunction)
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

- AtomicReferenceFieldUpdater

```java
protected AtomicReferenceFieldUpdater()
```

Protected do-nothing constructor for use by subclasses.

---

#### Constructor Detail

AtomicReferenceFieldUpdater

```java
protected AtomicReferenceFieldUpdater()
```

Protected do-nothing constructor for use by subclasses.

---

#### AtomicReferenceFieldUpdater

protected AtomicReferenceFieldUpdater()

Protected do-nothing constructor for use by subclasses.

Method Detail

- newUpdater

```java
public static <U,​W>
AtomicReferenceFieldUpdater
<U,​W> newUpdater​(
Class
<U> tclass,

Class
<W> vclass,

String
fieldName)
```

Creates and returns an updater for objects with the given field.
The Class arguments are needed to check that reflective types and
generic types match.

**Type Parameters:** U

- the type of instances of tclass
**Type Parameters:** W

- the type of instances of vclass
**Parameters:** tclass

- the class of the objects holding the field
**Parameters:** vclass

- the class of the field
**Parameters:** fieldName

- the name of the field to be updated
**Returns:** the updater
**Throws:** ClassCastException

- if the field is of the wrong type
**Throws:** IllegalArgumentException

- if the field is not volatile
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

V
expect,

V
update)
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

V
expect,

V
update)
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

V
newValue)
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

V
newValue)
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
public abstract
V
get​(
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
public
V
getAndSet​(
T
obj,

V
newValue)
```

Atomically sets the field of the given object managed by this updater
to the given value and returns the old value.

**Parameters:** obj

- An object whose field to get and set
**Parameters:** newValue

- the new value
**Returns:** the previous value

- getAndUpdate

```java
public final
V
getAndUpdate​(
T
obj,

UnaryOperator
<
V
> updateFunction)
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
public final
V
updateAndGet​(
T
obj,

UnaryOperator
<
V
> updateFunction)
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
public final
V
getAndAccumulate​(
T
obj,

V
x,

BinaryOperator
<
V
> accumulatorFunction)
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
public final
V
accumulateAndGet​(
T
obj,

V
x,

BinaryOperator
<
V
> accumulatorFunction)
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
public static <U,​W>
AtomicReferenceFieldUpdater
<U,​W> newUpdater​(
Class
<U> tclass,

Class
<W> vclass,

String
fieldName)
```

Creates and returns an updater for objects with the given field.
The Class arguments are needed to check that reflective types and
generic types match.

**Type Parameters:** U

- the type of instances of tclass
**Type Parameters:** W

- the type of instances of vclass
**Parameters:** tclass

- the class of the objects holding the field
**Parameters:** vclass

- the class of the field
**Parameters:** fieldName

- the name of the field to be updated
**Returns:** the updater
**Throws:** ClassCastException

- if the field is of the wrong type
**Throws:** IllegalArgumentException

- if the field is not volatile
**Throws:** RuntimeException

- with a nested reflection-based
exception if the class does not hold field or is the wrong type,
or the field is inaccessible to the caller according to Java language
access control

---

#### newUpdater

public static <U,​W>

AtomicReferenceFieldUpdater

<U,​W> newUpdater​(

Class

<U> tclass,

Class

<W> vclass,

String

fieldName)

Creates and returns an updater for objects with the given field.
The Class arguments are needed to check that reflective types and
generic types match.

compareAndSet

```java
public abstract boolean compareAndSet​(
T
obj,

V
expect,

V
update)
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

V

expect,

V

update)

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

V
expect,

V
update)
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

V

expect,

V

update)

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

V
newValue)
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

V

newValue)

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

V
newValue)
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

V

newValue)

Eventually sets the field of the given object managed by this
updater to the given updated value.

get

```java
public abstract
V
get​(
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

public abstract

V

get​(

T

obj)

Returns the current value held in the field of the given object
managed by this updater.

getAndSet

```java
public
V
getAndSet​(
T
obj,

V
newValue)
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

public

V

getAndSet​(

T

obj,

V

newValue)

Atomically sets the field of the given object managed by this updater
to the given value and returns the old value.

getAndUpdate

```java
public final
V
getAndUpdate​(
T
obj,

UnaryOperator
<
V
> updateFunction)
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

public final

V

getAndUpdate​(

T

obj,

UnaryOperator

<

V

> updateFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the field of the given object managed
by this updater with the results of applying the given
function, returning the previous value. The function should be
side-effect-free, since it may be re-applied when attempted
updates fail due to contention among threads.

updateAndGet

```java
public final
V
updateAndGet​(
T
obj,

UnaryOperator
<
V
> updateFunction)
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

public final

V

updateAndGet​(

T

obj,

UnaryOperator

<

V

> updateFunction)

Atomically updates (with memory effects as specified by

VarHandle.compareAndSet(java.lang.Object...)

) the field of the given object managed
by this updater with the results of applying the given
function, returning the updated value. The function should be
side-effect-free, since it may be re-applied when attempted
updates fail due to contention among threads.

getAndAccumulate

```java
public final
V
getAndAccumulate​(
T
obj,

V
x,

BinaryOperator
<
V
> accumulatorFunction)
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

public final

V

getAndAccumulate​(

T

obj,

V

x,

BinaryOperator

<

V

> accumulatorFunction)

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
public final
V
accumulateAndGet​(
T
obj,

V
x,

BinaryOperator
<
V
> accumulatorFunction)
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

public final

V

accumulateAndGet​(

T

obj,

V

x,

BinaryOperator

<

V

> accumulatorFunction)

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

