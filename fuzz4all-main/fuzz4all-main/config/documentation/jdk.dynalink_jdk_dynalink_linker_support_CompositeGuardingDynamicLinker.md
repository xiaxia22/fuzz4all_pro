# Class CompositeGuardingDynamicLinker

**Source:** `jdk.dynalink\jdk\dynalink\linker\support\CompositeGuardingDynamicLinker.html`

### Class Description

```java
public class
CompositeGuardingDynamicLinker

extends
Object

implements
GuardingDynamicLinker
```

A

GuardingDynamicLinker

that delegates sequentially to a list of
other guarding dynamic linkers in its

getGuardedInvocation(LinkRequest, LinkerServices)

.

**All Implemented Interfaces:** GuardingDynamicLinker

---

### Field Details

*No entries found.*

### Constructor Details

#### public CompositeGuardingDynamicLinker​(
Iterable
<? extends
GuardingDynamicLinker
> linkers)

Creates a new composite linker.

**Parameters:**
- linkers

- a list of component linkers.

**Throws:**
- NullPointerException

- if

linkers

or any of its elements
are null.

---

### Method Details

#### public
GuardedInvocation
getGuardedInvocation​(
LinkRequest
linkRequest,

LinkerServices
linkerServices)
throws
Exception

Delegates the call to its component linkers. The first non-null value
returned from a component linker is returned. If no component linker
returns a non-null invocation, null is returned.

**Specified by:**
- getGuardedInvocation

in interface

GuardingDynamicLinker

**Parameters:**
- linkRequest

- the object describing the request for linking a
particular invocation
- linkerServices

- linker services

**Returns:**
- the first non-null return value from a component linker, or null
if none of the components returned a non-null.

**Throws:**
- Exception

- if the operation fails for whatever reason

---

### Additional Sections

#### Class CompositeGuardingDynamicLinker

java.lang.Object

- jdk.dynalink.linker.support.CompositeGuardingDynamicLinker

jdk.dynalink.linker.support.CompositeGuardingDynamicLinker

**All Implemented Interfaces:** GuardingDynamicLinker

```java
public class
CompositeGuardingDynamicLinker

extends
Object

implements
GuardingDynamicLinker
```

A

GuardingDynamicLinker

that delegates sequentially to a list of
other guarding dynamic linkers in its

getGuardedInvocation(LinkRequest, LinkerServices)

.

public class

CompositeGuardingDynamicLinker

extends

Object

implements

GuardingDynamicLinker

A

GuardingDynamicLinker

that delegates sequentially to a list of
other guarding dynamic linkers in its

getGuardedInvocation(LinkRequest, LinkerServices)

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

CompositeGuardingDynamicLinker

​(

Iterable

<? extends

GuardingDynamicLinker

> linkers)

Creates a new composite linker.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

GuardedInvocation

getGuardedInvocation

​(

LinkRequest

linkRequest,

LinkerServices

linkerServices)

Delegates the call to its component linkers.

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

CompositeGuardingDynamicLinker

​(

Iterable

<? extends

GuardingDynamicLinker

> linkers)

Creates a new composite linker.

---

#### Constructor Summary

Creates a new composite linker.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

GuardedInvocation

getGuardedInvocation

​(

LinkRequest

linkRequest,

LinkerServices

linkerServices)

Delegates the call to its component linkers.

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

Delegates the call to its component linkers.

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

- CompositeGuardingDynamicLinker

```java
public CompositeGuardingDynamicLinker​(
Iterable
<? extends
GuardingDynamicLinker
> linkers)
```

Creates a new composite linker.

**Parameters:** linkers

- a list of component linkers.
**Throws:** NullPointerException

- if

linkers

or any of its elements
are null.

============ METHOD DETAIL ==========

- Method Detail

- getGuardedInvocation

```java
public
GuardedInvocation
getGuardedInvocation​(
LinkRequest
linkRequest,

LinkerServices
linkerServices)
throws
Exception
```

Delegates the call to its component linkers. The first non-null value
returned from a component linker is returned. If no component linker
returns a non-null invocation, null is returned.

**Specified by:** getGuardedInvocation

in interface

GuardingDynamicLinker
**Parameters:** linkRequest

- the object describing the request for linking a
particular invocation
**Parameters:** linkerServices

- linker services
**Returns:** the first non-null return value from a component linker, or null
if none of the components returned a non-null.
**Throws:** Exception

- if the operation fails for whatever reason

Constructor Detail

- CompositeGuardingDynamicLinker

```java
public CompositeGuardingDynamicLinker​(
Iterable
<? extends
GuardingDynamicLinker
> linkers)
```

Creates a new composite linker.

**Parameters:** linkers

- a list of component linkers.
**Throws:** NullPointerException

- if

linkers

or any of its elements
are null.

---

#### Constructor Detail

CompositeGuardingDynamicLinker

```java
public CompositeGuardingDynamicLinker​(
Iterable
<? extends
GuardingDynamicLinker
> linkers)
```

Creates a new composite linker.

**Parameters:** linkers

- a list of component linkers.
**Throws:** NullPointerException

- if

linkers

or any of its elements
are null.

---

#### CompositeGuardingDynamicLinker

public CompositeGuardingDynamicLinker​(

Iterable

<? extends

GuardingDynamicLinker

> linkers)

Creates a new composite linker.

Method Detail

- getGuardedInvocation

```java
public
GuardedInvocation
getGuardedInvocation​(
LinkRequest
linkRequest,

LinkerServices
linkerServices)
throws
Exception
```

Delegates the call to its component linkers. The first non-null value
returned from a component linker is returned. If no component linker
returns a non-null invocation, null is returned.

**Specified by:** getGuardedInvocation

in interface

GuardingDynamicLinker
**Parameters:** linkRequest

- the object describing the request for linking a
particular invocation
**Parameters:** linkerServices

- linker services
**Returns:** the first non-null return value from a component linker, or null
if none of the components returned a non-null.
**Throws:** Exception

- if the operation fails for whatever reason

---

#### Method Detail

getGuardedInvocation

```java
public
GuardedInvocation
getGuardedInvocation​(
LinkRequest
linkRequest,

LinkerServices
linkerServices)
throws
Exception
```

Delegates the call to its component linkers. The first non-null value
returned from a component linker is returned. If no component linker
returns a non-null invocation, null is returned.

**Specified by:** getGuardedInvocation

in interface

GuardingDynamicLinker
**Parameters:** linkRequest

- the object describing the request for linking a
particular invocation
**Parameters:** linkerServices

- linker services
**Returns:** the first non-null return value from a component linker, or null
if none of the components returned a non-null.
**Throws:** Exception

- if the operation fails for whatever reason

---

#### getGuardedInvocation

public

GuardedInvocation

getGuardedInvocation​(

LinkRequest

linkRequest,

LinkerServices

linkerServices)
throws

Exception

Delegates the call to its component linkers. The first non-null value
returned from a component linker is returned. If no component linker
returns a non-null invocation, null is returned.

---

