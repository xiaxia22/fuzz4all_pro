# Class AbstractRelinkableCallSite

**Source:** `jdk.dynalink\jdk\dynalink\support\AbstractRelinkableCallSite.html`

### Class Description

```java
public abstract class
AbstractRelinkableCallSite

extends
MutableCallSite

implements
RelinkableCallSite
```

A basic implementation of the

RelinkableCallSite

as a

MutableCallSite

. It carries a

CallSiteDescriptor

passed in
the constructor and provides the correct implementation of the

RelinkableCallSite.initialize(MethodHandle)

method. Subclasses must provide

RelinkableCallSite.relink(GuardedInvocation, MethodHandle)

and

RelinkableCallSite.resetAndRelink(GuardedInvocation, MethodHandle)

methods.

**All Implemented Interfaces:** RelinkableCallSite

---

### Field Details

*No entries found.*

### Constructor Details

#### protected AbstractRelinkableCallSite​(
CallSiteDescriptor
descriptor)

Creates a new abstract relinkable call site.

**Parameters:**
- descriptor

- the descriptor for this call site that will be returned
from

RelinkableCallSite.getDescriptor()

. The call site's

CallSite.type()

will be equal to descriptor's

CallSiteDescriptor.getMethodType()

.

**Throws:**
- NullPointerException

- if

descriptor

is null.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class AbstractRelinkableCallSite

java.lang.Object

- java.lang.invoke.CallSite
- - java.lang.invoke.MutableCallSite
- - jdk.dynalink.support.AbstractRelinkableCallSite

java.lang.invoke.CallSite

- java.lang.invoke.MutableCallSite
- - jdk.dynalink.support.AbstractRelinkableCallSite

java.lang.invoke.MutableCallSite

- jdk.dynalink.support.AbstractRelinkableCallSite

jdk.dynalink.support.AbstractRelinkableCallSite

**All Implemented Interfaces:** RelinkableCallSite

**Direct Known Subclasses:** ChainedCallSite

,

SimpleRelinkableCallSite

```java
public abstract class
AbstractRelinkableCallSite

extends
MutableCallSite

implements
RelinkableCallSite
```

A basic implementation of the

RelinkableCallSite

as a

MutableCallSite

. It carries a

CallSiteDescriptor

passed in
the constructor and provides the correct implementation of the

RelinkableCallSite.initialize(MethodHandle)

method. Subclasses must provide

RelinkableCallSite.relink(GuardedInvocation, MethodHandle)

and

RelinkableCallSite.resetAndRelink(GuardedInvocation, MethodHandle)

methods.

public abstract class

AbstractRelinkableCallSite

extends

MutableCallSite

implements

RelinkableCallSite

A basic implementation of the

RelinkableCallSite

as a

MutableCallSite

. It carries a

CallSiteDescriptor

passed in
the constructor and provides the correct implementation of the

RelinkableCallSite.initialize(MethodHandle)

method. Subclasses must provide

RelinkableCallSite.relink(GuardedInvocation, MethodHandle)

and

RelinkableCallSite.resetAndRelink(GuardedInvocation, MethodHandle)

methods.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

AbstractRelinkableCallSite

​(

CallSiteDescriptor

descriptor)

Creates a new abstract relinkable call site.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in class java.lang.invoke.

MutableCallSite

getTarget

,

setTarget

,

syncAll

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

- Methods declared in interface jdk.dynalink.

RelinkableCallSite

getDescriptor

,

initialize

,

relink

,

resetAndRelink

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

AbstractRelinkableCallSite

​(

CallSiteDescriptor

descriptor)

Creates a new abstract relinkable call site.

---

#### Constructor Summary

Creates a new abstract relinkable call site.

Method Summary

- Methods declared in class java.lang.invoke.

MutableCallSite

getTarget

,

setTarget

,

syncAll

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

- Methods declared in interface jdk.dynalink.

RelinkableCallSite

getDescriptor

,

initialize

,

relink

,

resetAndRelink

---

#### Method Summary

Methods declared in class java.lang.invoke.

MutableCallSite

getTarget

,

setTarget

,

syncAll

---

#### Methods declared in class java.lang.invoke. MutableCallSite

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

Methods declared in interface jdk.dynalink.

RelinkableCallSite

getDescriptor

,

initialize

,

relink

,

resetAndRelink

---

#### Methods declared in interface jdk.dynalink. RelinkableCallSite

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- AbstractRelinkableCallSite

```java
protected AbstractRelinkableCallSite​(
CallSiteDescriptor
descriptor)
```

Creates a new abstract relinkable call site.

**Parameters:** descriptor

- the descriptor for this call site that will be returned
from

RelinkableCallSite.getDescriptor()

. The call site's

CallSite.type()

will be equal to descriptor's

CallSiteDescriptor.getMethodType()

.
**Throws:** NullPointerException

- if

descriptor

is null.

Constructor Detail

- AbstractRelinkableCallSite

```java
protected AbstractRelinkableCallSite​(
CallSiteDescriptor
descriptor)
```

Creates a new abstract relinkable call site.

**Parameters:** descriptor

- the descriptor for this call site that will be returned
from

RelinkableCallSite.getDescriptor()

. The call site's

CallSite.type()

will be equal to descriptor's

CallSiteDescriptor.getMethodType()

.
**Throws:** NullPointerException

- if

descriptor

is null.

---

#### Constructor Detail

AbstractRelinkableCallSite

```java
protected AbstractRelinkableCallSite​(
CallSiteDescriptor
descriptor)
```

Creates a new abstract relinkable call site.

**Parameters:** descriptor

- the descriptor for this call site that will be returned
from

RelinkableCallSite.getDescriptor()

. The call site's

CallSite.type()

will be equal to descriptor's

CallSiteDescriptor.getMethodType()

.
**Throws:** NullPointerException

- if

descriptor

is null.

---

#### AbstractRelinkableCallSite

protected AbstractRelinkableCallSite​(

CallSiteDescriptor

descriptor)

Creates a new abstract relinkable call site.

---

