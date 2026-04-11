# Class VolatileCallSite

**Source:** `java.base\java\lang\invoke\VolatileCallSite.html`

### Class Description

```java
public class
VolatileCallSite

extends
CallSite
```

A

VolatileCallSite

is a

CallSite

whose target acts like a volatile variable.
An

invokedynamic

instruction linked to a

VolatileCallSite

sees updates
to its call site target immediately, even if the update occurs in another thread.
There may be a performance penalty for such tight coupling between threads.

Unlike

MutableCallSite

, there is no

syncAll operation

on volatile
call sites, since every write to a volatile variable is implicitly
synchronized with reader threads.

In other respects, a

VolatileCallSite

is interchangeable
with

MutableCallSite

.

**Since:** 1.7
**See Also:** MutableCallSite

---

### Field Details

*No entries found.*

### Constructor Details

#### public VolatileCallSite​(
MethodType
type)

Creates a call site with a volatile binding to its target.
The initial target is set to a method handle
of the given type which will throw an

IllegalStateException

if called.

**Parameters:**
- type

- the method type that this call site will have

**Throws:**
- NullPointerException

- if the proposed type is null

---

#### public VolatileCallSite​(
MethodHandle
target)

Creates a call site with a volatile binding to its target.
The target is set to the given value.

**Parameters:**
- target

- the method handle that will be the initial target of the call site

**Throws:**
- NullPointerException

- if the proposed target is null

---

### Method Details

#### public final
MethodHandle
getTarget()

Returns the target method of the call site, which behaves
like a

volatile

field of the

VolatileCallSite

.

The interactions of

getTarget

with memory are the same
as of a read from a

volatile

field.

In particular, the current thread is required to issue a fresh
read of the target from memory, and must not fail to see
a recent update to the target by another thread.

**Specified by:**
- getTarget

in class

CallSite

**Returns:**
- the linkage state of this call site, a method handle which can change over time

**See Also:**
- setTarget(java.lang.invoke.MethodHandle)

---

#### public void setTarget​(
MethodHandle
newTarget)

Updates the target method of this call site, as a volatile variable.
The type of the new target must agree with the type of the old target.

The interactions with memory are the same as of a write to a volatile field.
In particular, any threads is guaranteed to see the updated target
the next time it calls

getTarget

.

**Specified by:**
- setTarget

in class

CallSite

**Parameters:**
- newTarget

- the new target

**Throws:**
- NullPointerException

- if the proposed new target is null
- WrongMethodTypeException

- if the proposed new target
has a method type that differs from the previous target

**See Also:**
- getTarget()

---

### Additional Sections

#### Class VolatileCallSite

java.lang.Object

- java.lang.invoke.CallSite
- - java.lang.invoke.VolatileCallSite

java.lang.invoke.CallSite

- java.lang.invoke.VolatileCallSite

java.lang.invoke.VolatileCallSite

```java
public class
VolatileCallSite

extends
CallSite
```

A

VolatileCallSite

is a

CallSite

whose target acts like a volatile variable.
An

invokedynamic

instruction linked to a

VolatileCallSite

sees updates
to its call site target immediately, even if the update occurs in another thread.
There may be a performance penalty for such tight coupling between threads.

Unlike

MutableCallSite

, there is no

syncAll operation

on volatile
call sites, since every write to a volatile variable is implicitly
synchronized with reader threads.

In other respects, a

VolatileCallSite

is interchangeable
with

MutableCallSite

.

**Since:** 1.7
**See Also:** MutableCallSite

public class

VolatileCallSite

extends

CallSite

A

VolatileCallSite

is a

CallSite

whose target acts like a volatile variable.
An

invokedynamic

instruction linked to a

VolatileCallSite

sees updates
to its call site target immediately, even if the update occurs in another thread.
There may be a performance penalty for such tight coupling between threads.

Unlike

MutableCallSite

, there is no

syncAll operation

on volatile
call sites, since every write to a volatile variable is implicitly
synchronized with reader threads.

In other respects, a

VolatileCallSite

is interchangeable
with

MutableCallSite

.

Unlike

MutableCallSite

, there is no

syncAll operation

on volatile
call sites, since every write to a volatile variable is implicitly
synchronized with reader threads.

In other respects, a

VolatileCallSite

is interchangeable
with

MutableCallSite

.

In other respects, a

VolatileCallSite

is interchangeable
with

MutableCallSite

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

VolatileCallSite

​(

MethodHandle

target)

Creates a call site with a volatile binding to its target.

VolatileCallSite

​(

MethodType

type)

Creates a call site with a volatile binding to its target.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

MethodHandle

getTarget

()

Returns the target method of the call site, which behaves
like a

volatile

field of the

VolatileCallSite

.

void

setTarget

​(

MethodHandle

newTarget)

Updates the target method of this call site, as a volatile variable.

- Methods declared in class java.lang.invoke.

CallSite

dynamicInvoker

,

type

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

Constructor

Description

VolatileCallSite

​(

MethodHandle

target)

Creates a call site with a volatile binding to its target.

VolatileCallSite

​(

MethodType

type)

Creates a call site with a volatile binding to its target.

---

#### Constructor Summary

Creates a call site with a volatile binding to its target.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

MethodHandle

getTarget

()

Returns the target method of the call site, which behaves
like a

volatile

field of the

VolatileCallSite

.

void

setTarget

​(

MethodHandle

newTarget)

Updates the target method of this call site, as a volatile variable.

- Methods declared in class java.lang.invoke.

CallSite

dynamicInvoker

,

type

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

Returns the target method of the call site, which behaves
like a

volatile

field of the

VolatileCallSite

.

Updates the target method of this call site, as a volatile variable.

Methods declared in class java.lang.invoke.

CallSite

dynamicInvoker

,

type

---

#### Methods declared in class java.lang.invoke. CallSite

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

- VolatileCallSite

```java
public VolatileCallSite​(
MethodType
type)
```

Creates a call site with a volatile binding to its target.
The initial target is set to a method handle
of the given type which will throw an

IllegalStateException

if called.

**Parameters:** type

- the method type that this call site will have
**Throws:** NullPointerException

- if the proposed type is null

- VolatileCallSite

```java
public VolatileCallSite​(
MethodHandle
target)
```

Creates a call site with a volatile binding to its target.
The target is set to the given value.

**Parameters:** target

- the method handle that will be the initial target of the call site
**Throws:** NullPointerException

- if the proposed target is null

============ METHOD DETAIL ==========

- Method Detail

- getTarget

```java
public final
MethodHandle
getTarget()
```

Returns the target method of the call site, which behaves
like a

volatile

field of the

VolatileCallSite

.

The interactions of

getTarget

with memory are the same
as of a read from a

volatile

field.

In particular, the current thread is required to issue a fresh
read of the target from memory, and must not fail to see
a recent update to the target by another thread.

**Specified by:** getTarget

in class

CallSite
**Returns:** the linkage state of this call site, a method handle which can change over time
**See Also:** setTarget(java.lang.invoke.MethodHandle)

- setTarget

```java
public void setTarget​(
MethodHandle
newTarget)
```

Updates the target method of this call site, as a volatile variable.
The type of the new target must agree with the type of the old target.

The interactions with memory are the same as of a write to a volatile field.
In particular, any threads is guaranteed to see the updated target
the next time it calls

getTarget

.

**Specified by:** setTarget

in class

CallSite
**Parameters:** newTarget

- the new target
**Throws:** NullPointerException

- if the proposed new target is null
**Throws:** WrongMethodTypeException

- if the proposed new target
has a method type that differs from the previous target
**See Also:** getTarget()

Constructor Detail

- VolatileCallSite

```java
public VolatileCallSite​(
MethodType
type)
```

Creates a call site with a volatile binding to its target.
The initial target is set to a method handle
of the given type which will throw an

IllegalStateException

if called.

**Parameters:** type

- the method type that this call site will have
**Throws:** NullPointerException

- if the proposed type is null

- VolatileCallSite

```java
public VolatileCallSite​(
MethodHandle
target)
```

Creates a call site with a volatile binding to its target.
The target is set to the given value.

**Parameters:** target

- the method handle that will be the initial target of the call site
**Throws:** NullPointerException

- if the proposed target is null

---

#### Constructor Detail

VolatileCallSite

```java
public VolatileCallSite​(
MethodType
type)
```

Creates a call site with a volatile binding to its target.
The initial target is set to a method handle
of the given type which will throw an

IllegalStateException

if called.

**Parameters:** type

- the method type that this call site will have
**Throws:** NullPointerException

- if the proposed type is null

---

#### VolatileCallSite

public VolatileCallSite​(

MethodType

type)

Creates a call site with a volatile binding to its target.
The initial target is set to a method handle
of the given type which will throw an

IllegalStateException

if called.

VolatileCallSite

```java
public VolatileCallSite​(
MethodHandle
target)
```

Creates a call site with a volatile binding to its target.
The target is set to the given value.

**Parameters:** target

- the method handle that will be the initial target of the call site
**Throws:** NullPointerException

- if the proposed target is null

---

#### VolatileCallSite

public VolatileCallSite​(

MethodHandle

target)

Creates a call site with a volatile binding to its target.
The target is set to the given value.

Method Detail

- getTarget

```java
public final
MethodHandle
getTarget()
```

Returns the target method of the call site, which behaves
like a

volatile

field of the

VolatileCallSite

.

The interactions of

getTarget

with memory are the same
as of a read from a

volatile

field.

In particular, the current thread is required to issue a fresh
read of the target from memory, and must not fail to see
a recent update to the target by another thread.

**Specified by:** getTarget

in class

CallSite
**Returns:** the linkage state of this call site, a method handle which can change over time
**See Also:** setTarget(java.lang.invoke.MethodHandle)

- setTarget

```java
public void setTarget​(
MethodHandle
newTarget)
```

Updates the target method of this call site, as a volatile variable.
The type of the new target must agree with the type of the old target.

The interactions with memory are the same as of a write to a volatile field.
In particular, any threads is guaranteed to see the updated target
the next time it calls

getTarget

.

**Specified by:** setTarget

in class

CallSite
**Parameters:** newTarget

- the new target
**Throws:** NullPointerException

- if the proposed new target is null
**Throws:** WrongMethodTypeException

- if the proposed new target
has a method type that differs from the previous target
**See Also:** getTarget()

---

#### Method Detail

getTarget

```java
public final
MethodHandle
getTarget()
```

Returns the target method of the call site, which behaves
like a

volatile

field of the

VolatileCallSite

.

The interactions of

getTarget

with memory are the same
as of a read from a

volatile

field.

In particular, the current thread is required to issue a fresh
read of the target from memory, and must not fail to see
a recent update to the target by another thread.

**Specified by:** getTarget

in class

CallSite
**Returns:** the linkage state of this call site, a method handle which can change over time
**See Also:** setTarget(java.lang.invoke.MethodHandle)

---

#### getTarget

public final

MethodHandle

getTarget()

Returns the target method of the call site, which behaves
like a

volatile

field of the

VolatileCallSite

.

The interactions of

getTarget

with memory are the same
as of a read from a

volatile

field.

In particular, the current thread is required to issue a fresh
read of the target from memory, and must not fail to see
a recent update to the target by another thread.

The interactions of

getTarget

with memory are the same
as of a read from a

volatile

field.

In particular, the current thread is required to issue a fresh
read of the target from memory, and must not fail to see
a recent update to the target by another thread.

In particular, the current thread is required to issue a fresh
read of the target from memory, and must not fail to see
a recent update to the target by another thread.

setTarget

```java
public void setTarget​(
MethodHandle
newTarget)
```

Updates the target method of this call site, as a volatile variable.
The type of the new target must agree with the type of the old target.

The interactions with memory are the same as of a write to a volatile field.
In particular, any threads is guaranteed to see the updated target
the next time it calls

getTarget

.

**Specified by:** setTarget

in class

CallSite
**Parameters:** newTarget

- the new target
**Throws:** NullPointerException

- if the proposed new target is null
**Throws:** WrongMethodTypeException

- if the proposed new target
has a method type that differs from the previous target
**See Also:** getTarget()

---

#### setTarget

public void setTarget​(

MethodHandle

newTarget)

Updates the target method of this call site, as a volatile variable.
The type of the new target must agree with the type of the old target.

The interactions with memory are the same as of a write to a volatile field.
In particular, any threads is guaranteed to see the updated target
the next time it calls

getTarget

.

The interactions with memory are the same as of a write to a volatile field.
In particular, any threads is guaranteed to see the updated target
the next time it calls

getTarget

.

---

