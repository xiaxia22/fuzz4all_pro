# Class Reference<T>

**Source:** `java.base\java\lang\ref\Reference.html`

### Class Description

```java
public abstract class
Reference<T>

extends
Object
```

Abstract base class for reference objects. This class defines the
operations common to all reference objects. Because reference objects are
implemented in close cooperation with the garbage collector, this class may
not be subclassed directly.

**Direct Known Subclasses:** PhantomReference

,

SoftReference

,

WeakReference

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public
T
get()

Returns this reference object's referent. If this reference object has
been cleared, either by the program or by the garbage collector, then
this method returns

null

.

**Returns:**
- The object to which this reference refers, or

null

if this reference object has been cleared

---

#### public void clear()

Clears this reference object. Invoking this method will not cause this
object to be enqueued.

This method is invoked only by Java code; when the garbage collector
clears references it does so directly, without invoking this method.

---

#### public boolean isEnqueued()

Tells whether or not this reference object has been enqueued, either by
the program or by the garbage collector. If this reference object was
not registered with a queue when it was created, then this method will
always return

false

.

**Returns:**
- true

if and only if this reference object has
been enqueued

---

#### public boolean enqueue()

Clears this reference object and adds it to the queue with which
it is registered, if any.

This method is invoked only by Java code; when the garbage collector
enqueues references it does so directly, without invoking this method.

**Returns:**
- true

if this reference object was successfully
enqueued;

false

if it was already enqueued or if
it was not registered with a queue when it was created

---

#### protected
Object
clone()
throws
CloneNotSupportedException

Throws

CloneNotSupportedException

. A

Reference

cannot be
meaningfully cloned. Construct a new

Reference

instead.

**Overrides:**
- clone

in class

Object

**Returns:**
- a clone of this instance.

**Throws:**
- CloneNotSupportedException

- always

**See Also:**
- Cloneable

**Since:**
- 11

---

#### public static void reachabilityFence​(
Object
ref)

Ensures that the object referenced by the given reference remains

strongly reachable

,
regardless of any prior actions of the program that might otherwise cause
the object to become unreachable; thus, the referenced object is not
reclaimable by garbage collection at least until after the invocation of
this method. Invocation of this method does not itself initiate garbage
collection or finalization.

This method establishes an ordering for

strong reachability

with respect to garbage collection. It controls relations that are
otherwise only implicit in a program -- the reachability conditions
triggering garbage collection. This method is designed for use in
uncommon situations of premature finalization where using

synchronized

blocks or methods, or using other synchronization
facilities are not possible or do not provide the desired control. This
method is applicable only when reclamation may have visible effects,
which is possible for objects with finalizers (See

Section 12.6 17 of

The Java™ Language Specification

)
that are implemented in ways that rely on ordering control for correctness.

**Parameters:**
- ref

- the reference. If

null

, this method has no effect.

**Since:**
- 9

**API Note:**
- Finalization may occur whenever the virtual machine detects that no
reference to an object will ever be stored in the heap: The garbage
collector may reclaim an object even if the fields of that object are
still in use, so long as the object has otherwise become unreachable.
This may have surprising and undesirable effects in cases such as the
following example in which the bookkeeping associated with a class is
managed through array indices. Here, method

action

uses a

reachabilityFence

to ensure that the

Resource

object is
not reclaimed before bookkeeping on an associated

ExternalResource

has been performed; in particular here, to
ensure that the array slot holding the

ExternalResource

is not
nulled out in method

Object.finalize()

, which may otherwise run
concurrently.

```java
class Resource {
private static ExternalResource[] externalResourceArray = ...

int myIndex;
Resource(...) {
myIndex = ...
externalResourceArray[myIndex] = ...;
...
}
protected void finalize() {
externalResourceArray[myIndex] = null;
...
}
public void action() {
try {
// ...
int i = myIndex;
Resource.update(externalResourceArray[i]);
} finally {
Reference.reachabilityFence(this);
}
}
private static void update(ExternalResource ext) {
ext.status = ...;
}
}
```

Here, the invocation of

reachabilityFence

is nonintuitively
placed

after

the call to

update

, to ensure that the
array slot is not nulled out by

Object.finalize()

before the
update, even if the call to

action

was the last use of this
object. This might be the case if, for example a usage in a user program
had the form

new Resource().action();

which retains no other
reference to this

Resource

. While probably overkill here,

reachabilityFence

is placed in a

finally

block to ensure
that it is invoked across all paths in the method. In a method with more
complex control paths, you might need further precautions to ensure that

reachabilityFence

is encountered along all of them.

It is sometimes possible to better encapsulate use of

reachabilityFence

. Continuing the above example, if it were
acceptable for the call to method

update

to proceed even if the
finalizer had already executed (nulling out slot), then you could
localize use of

reachabilityFence

:

```java
public void action2() {
// ...
Resource.update(getExternalResource());
}
private ExternalResource getExternalResource() {
ExternalResource ext = externalResourceArray[myIndex];
Reference.reachabilityFence(this);
return ext;
}
```

Method

reachabilityFence

is not required in constructions
that themselves ensure reachability. For example, because objects that
are locked cannot, in general, be reclaimed, it would suffice if all
accesses of the object, in all methods of class

Resource

(including

finalize

) were enclosed in

synchronized (this)

blocks. (Further, such blocks must not include infinite loops, or
themselves be unreachable, which fall into the corner case exceptions to
the "in general" disclaimer.) However, method

reachabilityFence

remains a better option in cases where this approach is not as efficient,
desirable, or possible; for example because it would encounter deadlock.

---

### Additional Sections

#### Class Reference<T>

java.lang.Object

- java.lang.ref.Reference<T>

java.lang.ref.Reference<T>

**Direct Known Subclasses:** PhantomReference

,

SoftReference

,

WeakReference

```java
public abstract class
Reference<T>

extends
Object
```

Abstract base class for reference objects. This class defines the
operations common to all reference objects. Because reference objects are
implemented in close cooperation with the garbage collector, this class may
not be subclassed directly.

**Since:** 1.2

public abstract class

Reference<T>

extends

Object

Abstract base class for reference objects. This class defines the
operations common to all reference objects. Because reference objects are
implemented in close cooperation with the garbage collector, this class may
not be subclassed directly.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

clear

()

Clears this reference object.

protected

Object

clone

()

Throws

CloneNotSupportedException

.

boolean

enqueue

()

Clears this reference object and adds it to the queue with which
it is registered, if any.

T

get

()

Returns this reference object's referent.

boolean

isEnqueued

()

Tells whether or not this reference object has been enqueued, either by
the program or by the garbage collector.

static void

reachabilityFence

​(

Object

ref)

Ensures that the object referenced by the given reference remains

strongly reachable

,
regardless of any prior actions of the program that might otherwise cause
the object to become unreachable; thus, the referenced object is not
reclaimable by garbage collection at least until after the invocation of
this method.

- Methods declared in class java.lang.

Object

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

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

clear

()

Clears this reference object.

protected

Object

clone

()

Throws

CloneNotSupportedException

.

boolean

enqueue

()

Clears this reference object and adds it to the queue with which
it is registered, if any.

T

get

()

Returns this reference object's referent.

boolean

isEnqueued

()

Tells whether or not this reference object has been enqueued, either by
the program or by the garbage collector.

static void

reachabilityFence

​(

Object

ref)

Ensures that the object referenced by the given reference remains

strongly reachable

,
regardless of any prior actions of the program that might otherwise cause
the object to become unreachable; thus, the referenced object is not
reclaimable by garbage collection at least until after the invocation of
this method.

- Methods declared in class java.lang.

Object

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

Clears this reference object.

Throws

CloneNotSupportedException

.

Clears this reference object and adds it to the queue with which
it is registered, if any.

Returns this reference object's referent.

Tells whether or not this reference object has been enqueued, either by
the program or by the garbage collector.

Ensures that the object referenced by the given reference remains

strongly reachable

,
regardless of any prior actions of the program that might otherwise cause
the object to become unreachable; thus, the referenced object is not
reclaimable by garbage collection at least until after the invocation of
this method.

Methods declared in class java.lang.

Object

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

============ METHOD DETAIL ==========

- Method Detail

- get

```java
public
T
get()
```

Returns this reference object's referent. If this reference object has
been cleared, either by the program or by the garbage collector, then
this method returns

null

.

**Returns:** The object to which this reference refers, or

null

if this reference object has been cleared

- clear

```java
public void clear()
```

Clears this reference object. Invoking this method will not cause this
object to be enqueued.

This method is invoked only by Java code; when the garbage collector
clears references it does so directly, without invoking this method.

- isEnqueued

```java
public boolean isEnqueued()
```

Tells whether or not this reference object has been enqueued, either by
the program or by the garbage collector. If this reference object was
not registered with a queue when it was created, then this method will
always return

false

.

**Returns:** true

if and only if this reference object has
been enqueued

- enqueue

```java
public boolean enqueue()
```

Clears this reference object and adds it to the queue with which
it is registered, if any.

This method is invoked only by Java code; when the garbage collector
enqueues references it does so directly, without invoking this method.

**Returns:** true

if this reference object was successfully
enqueued;

false

if it was already enqueued or if
it was not registered with a queue when it was created

- clone

```java
protected
Object
clone()
throws
CloneNotSupportedException
```

Throws

CloneNotSupportedException

. A

Reference

cannot be
meaningfully cloned. Construct a new

Reference

instead.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**Throws:** CloneNotSupportedException

- always
**Since:** 11
**See Also:** Cloneable

- reachabilityFence

```java
public static void reachabilityFence​(
Object
ref)
```

Ensures that the object referenced by the given reference remains

strongly reachable

,
regardless of any prior actions of the program that might otherwise cause
the object to become unreachable; thus, the referenced object is not
reclaimable by garbage collection at least until after the invocation of
this method. Invocation of this method does not itself initiate garbage
collection or finalization.

This method establishes an ordering for

strong reachability

with respect to garbage collection. It controls relations that are
otherwise only implicit in a program -- the reachability conditions
triggering garbage collection. This method is designed for use in
uncommon situations of premature finalization where using

synchronized

blocks or methods, or using other synchronization
facilities are not possible or do not provide the desired control. This
method is applicable only when reclamation may have visible effects,
which is possible for objects with finalizers (See

Section 12.6 17 of

The Java™ Language Specification

)
that are implemented in ways that rely on ordering control for correctness.

**API Note:** Finalization may occur whenever the virtual machine detects that no
reference to an object will ever be stored in the heap: The garbage
collector may reclaim an object even if the fields of that object are
still in use, so long as the object has otherwise become unreachable.
This may have surprising and undesirable effects in cases such as the
following example in which the bookkeeping associated with a class is
managed through array indices. Here, method

action

uses a

reachabilityFence

to ensure that the

Resource

object is
not reclaimed before bookkeeping on an associated

ExternalResource

has been performed; in particular here, to
ensure that the array slot holding the

ExternalResource

is not
nulled out in method

Object.finalize()

, which may otherwise run
concurrently.

```java
class Resource {
private static ExternalResource[] externalResourceArray = ...

int myIndex;
Resource(...) {
myIndex = ...
externalResourceArray[myIndex] = ...;
...
}
protected void finalize() {
externalResourceArray[myIndex] = null;
...
}
public void action() {
try {
// ...
int i = myIndex;
Resource.update(externalResourceArray[i]);
} finally {
Reference.reachabilityFence(this);
}
}
private static void update(ExternalResource ext) {
ext.status = ...;
}
}
```

Here, the invocation of

reachabilityFence

is nonintuitively
placed

after

the call to

update

, to ensure that the
array slot is not nulled out by

Object.finalize()

before the
update, even if the call to

action

was the last use of this
object. This might be the case if, for example a usage in a user program
had the form

new Resource().action();

which retains no other
reference to this

Resource

. While probably overkill here,

reachabilityFence

is placed in a

finally

block to ensure
that it is invoked across all paths in the method. In a method with more
complex control paths, you might need further precautions to ensure that

reachabilityFence

is encountered along all of them.

It is sometimes possible to better encapsulate use of

reachabilityFence

. Continuing the above example, if it were
acceptable for the call to method

update

to proceed even if the
finalizer had already executed (nulling out slot), then you could
localize use of

reachabilityFence

:

```java
public void action2() {
// ...
Resource.update(getExternalResource());
}
private ExternalResource getExternalResource() {
ExternalResource ext = externalResourceArray[myIndex];
Reference.reachabilityFence(this);
return ext;
}
```

Method

reachabilityFence

is not required in constructions
that themselves ensure reachability. For example, because objects that
are locked cannot, in general, be reclaimed, it would suffice if all
accesses of the object, in all methods of class

Resource

(including

finalize

) were enclosed in

synchronized (this)

blocks. (Further, such blocks must not include infinite loops, or
themselves be unreachable, which fall into the corner case exceptions to
the "in general" disclaimer.) However, method

reachabilityFence

remains a better option in cases where this approach is not as efficient,
desirable, or possible; for example because it would encounter deadlock.
**Parameters:** ref

- the reference. If

null

, this method has no effect.
**Since:** 9

Method Detail

- get

```java
public
T
get()
```

Returns this reference object's referent. If this reference object has
been cleared, either by the program or by the garbage collector, then
this method returns

null

.

**Returns:** The object to which this reference refers, or

null

if this reference object has been cleared

- clear

```java
public void clear()
```

Clears this reference object. Invoking this method will not cause this
object to be enqueued.

This method is invoked only by Java code; when the garbage collector
clears references it does so directly, without invoking this method.

- isEnqueued

```java
public boolean isEnqueued()
```

Tells whether or not this reference object has been enqueued, either by
the program or by the garbage collector. If this reference object was
not registered with a queue when it was created, then this method will
always return

false

.

**Returns:** true

if and only if this reference object has
been enqueued

- enqueue

```java
public boolean enqueue()
```

Clears this reference object and adds it to the queue with which
it is registered, if any.

This method is invoked only by Java code; when the garbage collector
enqueues references it does so directly, without invoking this method.

**Returns:** true

if this reference object was successfully
enqueued;

false

if it was already enqueued or if
it was not registered with a queue when it was created

- clone

```java
protected
Object
clone()
throws
CloneNotSupportedException
```

Throws

CloneNotSupportedException

. A

Reference

cannot be
meaningfully cloned. Construct a new

Reference

instead.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**Throws:** CloneNotSupportedException

- always
**Since:** 11
**See Also:** Cloneable

- reachabilityFence

```java
public static void reachabilityFence​(
Object
ref)
```

Ensures that the object referenced by the given reference remains

strongly reachable

,
regardless of any prior actions of the program that might otherwise cause
the object to become unreachable; thus, the referenced object is not
reclaimable by garbage collection at least until after the invocation of
this method. Invocation of this method does not itself initiate garbage
collection or finalization.

This method establishes an ordering for

strong reachability

with respect to garbage collection. It controls relations that are
otherwise only implicit in a program -- the reachability conditions
triggering garbage collection. This method is designed for use in
uncommon situations of premature finalization where using

synchronized

blocks or methods, or using other synchronization
facilities are not possible or do not provide the desired control. This
method is applicable only when reclamation may have visible effects,
which is possible for objects with finalizers (See

Section 12.6 17 of

The Java™ Language Specification

)
that are implemented in ways that rely on ordering control for correctness.

**API Note:** Finalization may occur whenever the virtual machine detects that no
reference to an object will ever be stored in the heap: The garbage
collector may reclaim an object even if the fields of that object are
still in use, so long as the object has otherwise become unreachable.
This may have surprising and undesirable effects in cases such as the
following example in which the bookkeeping associated with a class is
managed through array indices. Here, method

action

uses a

reachabilityFence

to ensure that the

Resource

object is
not reclaimed before bookkeeping on an associated

ExternalResource

has been performed; in particular here, to
ensure that the array slot holding the

ExternalResource

is not
nulled out in method

Object.finalize()

, which may otherwise run
concurrently.

```java
class Resource {
private static ExternalResource[] externalResourceArray = ...

int myIndex;
Resource(...) {
myIndex = ...
externalResourceArray[myIndex] = ...;
...
}
protected void finalize() {
externalResourceArray[myIndex] = null;
...
}
public void action() {
try {
// ...
int i = myIndex;
Resource.update(externalResourceArray[i]);
} finally {
Reference.reachabilityFence(this);
}
}
private static void update(ExternalResource ext) {
ext.status = ...;
}
}
```

Here, the invocation of

reachabilityFence

is nonintuitively
placed

after

the call to

update

, to ensure that the
array slot is not nulled out by

Object.finalize()

before the
update, even if the call to

action

was the last use of this
object. This might be the case if, for example a usage in a user program
had the form

new Resource().action();

which retains no other
reference to this

Resource

. While probably overkill here,

reachabilityFence

is placed in a

finally

block to ensure
that it is invoked across all paths in the method. In a method with more
complex control paths, you might need further precautions to ensure that

reachabilityFence

is encountered along all of them.

It is sometimes possible to better encapsulate use of

reachabilityFence

. Continuing the above example, if it were
acceptable for the call to method

update

to proceed even if the
finalizer had already executed (nulling out slot), then you could
localize use of

reachabilityFence

:

```java
public void action2() {
// ...
Resource.update(getExternalResource());
}
private ExternalResource getExternalResource() {
ExternalResource ext = externalResourceArray[myIndex];
Reference.reachabilityFence(this);
return ext;
}
```

Method

reachabilityFence

is not required in constructions
that themselves ensure reachability. For example, because objects that
are locked cannot, in general, be reclaimed, it would suffice if all
accesses of the object, in all methods of class

Resource

(including

finalize

) were enclosed in

synchronized (this)

blocks. (Further, such blocks must not include infinite loops, or
themselves be unreachable, which fall into the corner case exceptions to
the "in general" disclaimer.) However, method

reachabilityFence

remains a better option in cases where this approach is not as efficient,
desirable, or possible; for example because it would encounter deadlock.
**Parameters:** ref

- the reference. If

null

, this method has no effect.
**Since:** 9

---

#### Method Detail

get

```java
public
T
get()
```

Returns this reference object's referent. If this reference object has
been cleared, either by the program or by the garbage collector, then
this method returns

null

.

**Returns:** The object to which this reference refers, or

null

if this reference object has been cleared

---

#### get

public

T

get()

Returns this reference object's referent. If this reference object has
been cleared, either by the program or by the garbage collector, then
this method returns

null

.

clear

```java
public void clear()
```

Clears this reference object. Invoking this method will not cause this
object to be enqueued.

This method is invoked only by Java code; when the garbage collector
clears references it does so directly, without invoking this method.

---

#### clear

public void clear()

Clears this reference object. Invoking this method will not cause this
object to be enqueued.

This method is invoked only by Java code; when the garbage collector
clears references it does so directly, without invoking this method.

This method is invoked only by Java code; when the garbage collector
clears references it does so directly, without invoking this method.

isEnqueued

```java
public boolean isEnqueued()
```

Tells whether or not this reference object has been enqueued, either by
the program or by the garbage collector. If this reference object was
not registered with a queue when it was created, then this method will
always return

false

.

**Returns:** true

if and only if this reference object has
been enqueued

---

#### isEnqueued

public boolean isEnqueued()

Tells whether or not this reference object has been enqueued, either by
the program or by the garbage collector. If this reference object was
not registered with a queue when it was created, then this method will
always return

false

.

enqueue

```java
public boolean enqueue()
```

Clears this reference object and adds it to the queue with which
it is registered, if any.

This method is invoked only by Java code; when the garbage collector
enqueues references it does so directly, without invoking this method.

**Returns:** true

if this reference object was successfully
enqueued;

false

if it was already enqueued or if
it was not registered with a queue when it was created

---

#### enqueue

public boolean enqueue()

Clears this reference object and adds it to the queue with which
it is registered, if any.

This method is invoked only by Java code; when the garbage collector
enqueues references it does so directly, without invoking this method.

This method is invoked only by Java code; when the garbage collector
enqueues references it does so directly, without invoking this method.

clone

```java
protected
Object
clone()
throws
CloneNotSupportedException
```

Throws

CloneNotSupportedException

. A

Reference

cannot be
meaningfully cloned. Construct a new

Reference

instead.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**Throws:** CloneNotSupportedException

- always
**Since:** 11
**See Also:** Cloneable

---

#### clone

protected

Object

clone()
throws

CloneNotSupportedException

Throws

CloneNotSupportedException

. A

Reference

cannot be
meaningfully cloned. Construct a new

Reference

instead.

reachabilityFence

```java
public static void reachabilityFence​(
Object
ref)
```

Ensures that the object referenced by the given reference remains

strongly reachable

,
regardless of any prior actions of the program that might otherwise cause
the object to become unreachable; thus, the referenced object is not
reclaimable by garbage collection at least until after the invocation of
this method. Invocation of this method does not itself initiate garbage
collection or finalization.

This method establishes an ordering for

strong reachability

with respect to garbage collection. It controls relations that are
otherwise only implicit in a program -- the reachability conditions
triggering garbage collection. This method is designed for use in
uncommon situations of premature finalization where using

synchronized

blocks or methods, or using other synchronization
facilities are not possible or do not provide the desired control. This
method is applicable only when reclamation may have visible effects,
which is possible for objects with finalizers (See

Section 12.6 17 of

The Java™ Language Specification

)
that are implemented in ways that rely on ordering control for correctness.

**API Note:** Finalization may occur whenever the virtual machine detects that no
reference to an object will ever be stored in the heap: The garbage
collector may reclaim an object even if the fields of that object are
still in use, so long as the object has otherwise become unreachable.
This may have surprising and undesirable effects in cases such as the
following example in which the bookkeeping associated with a class is
managed through array indices. Here, method

action

uses a

reachabilityFence

to ensure that the

Resource

object is
not reclaimed before bookkeeping on an associated

ExternalResource

has been performed; in particular here, to
ensure that the array slot holding the

ExternalResource

is not
nulled out in method

Object.finalize()

, which may otherwise run
concurrently.

```java
class Resource {
private static ExternalResource[] externalResourceArray = ...

int myIndex;
Resource(...) {
myIndex = ...
externalResourceArray[myIndex] = ...;
...
}
protected void finalize() {
externalResourceArray[myIndex] = null;
...
}
public void action() {
try {
// ...
int i = myIndex;
Resource.update(externalResourceArray[i]);
} finally {
Reference.reachabilityFence(this);
}
}
private static void update(ExternalResource ext) {
ext.status = ...;
}
}
```

Here, the invocation of

reachabilityFence

is nonintuitively
placed

after

the call to

update

, to ensure that the
array slot is not nulled out by

Object.finalize()

before the
update, even if the call to

action

was the last use of this
object. This might be the case if, for example a usage in a user program
had the form

new Resource().action();

which retains no other
reference to this

Resource

. While probably overkill here,

reachabilityFence

is placed in a

finally

block to ensure
that it is invoked across all paths in the method. In a method with more
complex control paths, you might need further precautions to ensure that

reachabilityFence

is encountered along all of them.

It is sometimes possible to better encapsulate use of

reachabilityFence

. Continuing the above example, if it were
acceptable for the call to method

update

to proceed even if the
finalizer had already executed (nulling out slot), then you could
localize use of

reachabilityFence

:

```java
public void action2() {
// ...
Resource.update(getExternalResource());
}
private ExternalResource getExternalResource() {
ExternalResource ext = externalResourceArray[myIndex];
Reference.reachabilityFence(this);
return ext;
}
```

Method

reachabilityFence

is not required in constructions
that themselves ensure reachability. For example, because objects that
are locked cannot, in general, be reclaimed, it would suffice if all
accesses of the object, in all methods of class

Resource

(including

finalize

) were enclosed in

synchronized (this)

blocks. (Further, such blocks must not include infinite loops, or
themselves be unreachable, which fall into the corner case exceptions to
the "in general" disclaimer.) However, method

reachabilityFence

remains a better option in cases where this approach is not as efficient,
desirable, or possible; for example because it would encounter deadlock.
**Parameters:** ref

- the reference. If

null

, this method has no effect.
**Since:** 9

---

#### reachabilityFence

public static void reachabilityFence​(

Object

ref)

Ensures that the object referenced by the given reference remains

strongly reachable

,
regardless of any prior actions of the program that might otherwise cause
the object to become unreachable; thus, the referenced object is not
reclaimable by garbage collection at least until after the invocation of
this method. Invocation of this method does not itself initiate garbage
collection or finalization.

This method establishes an ordering for

strong reachability

with respect to garbage collection. It controls relations that are
otherwise only implicit in a program -- the reachability conditions
triggering garbage collection. This method is designed for use in
uncommon situations of premature finalization where using

synchronized

blocks or methods, or using other synchronization
facilities are not possible or do not provide the desired control. This
method is applicable only when reclamation may have visible effects,
which is possible for objects with finalizers (See

Section 12.6 17 of

The Java™ Language Specification

)
that are implemented in ways that rely on ordering control for correctness.

This method establishes an ordering for

strong reachability

with respect to garbage collection. It controls relations that are
otherwise only implicit in a program -- the reachability conditions
triggering garbage collection. This method is designed for use in
uncommon situations of premature finalization where using

synchronized

blocks or methods, or using other synchronization
facilities are not possible or do not provide the desired control. This
method is applicable only when reclamation may have visible effects,
which is possible for objects with finalizers (See

Section 12.6 17 of

The Java™ Language Specification

)
that are implemented in ways that rely on ordering control for correctness.

class Resource {
private static ExternalResource[] externalResourceArray = ...

int myIndex;
Resource(...) {
myIndex = ...
externalResourceArray[myIndex] = ...;
...
}
protected void finalize() {
externalResourceArray[myIndex] = null;
...
}
public void action() {
try {
// ...
int i = myIndex;
Resource.update(externalResourceArray[i]);
} finally {
Reference.reachabilityFence(this);
}
}
private static void update(ExternalResource ext) {
ext.status = ...;
}
}

It is sometimes possible to better encapsulate use of

reachabilityFence

. Continuing the above example, if it were
acceptable for the call to method

update

to proceed even if the
finalizer had already executed (nulling out slot), then you could
localize use of

reachabilityFence

:

```java
public void action2() {
// ...
Resource.update(getExternalResource());
}
private ExternalResource getExternalResource() {
ExternalResource ext = externalResourceArray[myIndex];
Reference.reachabilityFence(this);
return ext;
}
```

Method

reachabilityFence

is not required in constructions
that themselves ensure reachability. For example, because objects that
are locked cannot, in general, be reclaimed, it would suffice if all
accesses of the object, in all methods of class

Resource

(including

finalize

) were enclosed in

synchronized (this)

blocks. (Further, such blocks must not include infinite loops, or
themselves be unreachable, which fall into the corner case exceptions to
the "in general" disclaimer.) However, method

reachabilityFence

remains a better option in cases where this approach is not as efficient,
desirable, or possible; for example because it would encounter deadlock.

public void action2() {
// ...
Resource.update(getExternalResource());
}
private ExternalResource getExternalResource() {
ExternalResource ext = externalResourceArray[myIndex];
Reference.reachabilityFence(this);
return ext;
}

Method

reachabilityFence

is not required in constructions
that themselves ensure reachability. For example, because objects that
are locked cannot, in general, be reclaimed, it would suffice if all
accesses of the object, in all methods of class

Resource

(including

finalize

) were enclosed in

synchronized (this)

blocks. (Further, such blocks must not include infinite loops, or
themselves be unreachable, which fall into the corner case exceptions to
the "in general" disclaimer.) However, method

reachabilityFence

remains a better option in cases where this approach is not as efficient,
desirable, or possible; for example because it would encounter deadlock.

---

