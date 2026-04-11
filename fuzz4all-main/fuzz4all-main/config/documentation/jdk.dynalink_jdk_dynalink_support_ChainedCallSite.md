# Class ChainedCallSite

**Source:** `jdk.dynalink\jdk\dynalink\support\ChainedCallSite.html`

### Class Description

```java
public class
ChainedCallSite

extends
AbstractRelinkableCallSite
```

A relinkable call site that implements a polymorphic inline caching strategy.
It remembers up to 8

GuardedInvocation

s it was linked with, and on
each relink request builds a cascading chain of method handles of one
invocation falling back to the next one. The number of remembered invocations
can be customized by overriding

getMaxChainLength()

in a subclass.
When this call site is relinked with a new invocation and the length of the
chain is already at the maximum, it will throw away the oldest invocation.
Invocations with invalidated switch points and ones for which their
invalidating exception triggered are removed eagerly from the chain. The
invocations are never reordered; the most recently linked method handle is
always at the start of the chain and the least recently linked at its end.
The call site can be safely relinked on more than one thread concurrently.
Race conditions in linking are resolved by throwing away the

GuardedInvocation

produced on the losing thread without incorporating
it into the chain, so it can lead to repeated linking for the same arguments.

**All Implemented Interfaces:** RelinkableCallSite

---

### Field Details

*No entries found.*

### Constructor Details

#### public ChainedCallSite​(
CallSiteDescriptor
descriptor)

Creates a new chained call site.

**Parameters:**
- descriptor

- the descriptor for the call site.

---

### Method Details

#### protected int getMaxChainLength()

The maximum number of method handles in the chain. Defaults to 8. You can
override it in a subclass if you need to change the value.

**Returns:**
- the maximum number of method handles in the chain. The return
value is checked, and if your override returns a value less than 1, a

RuntimeException

will be thrown.

---

### Additional Sections

#### Class ChainedCallSite

java.lang.Object

- java.lang.invoke.CallSite
- - java.lang.invoke.MutableCallSite
- - jdk.dynalink.support.AbstractRelinkableCallSite
- - jdk.dynalink.support.ChainedCallSite

java.lang.invoke.CallSite

- java.lang.invoke.MutableCallSite
- - jdk.dynalink.support.AbstractRelinkableCallSite
- - jdk.dynalink.support.ChainedCallSite

java.lang.invoke.MutableCallSite

- jdk.dynalink.support.AbstractRelinkableCallSite
- - jdk.dynalink.support.ChainedCallSite

jdk.dynalink.support.AbstractRelinkableCallSite

- jdk.dynalink.support.ChainedCallSite

jdk.dynalink.support.ChainedCallSite

**All Implemented Interfaces:** RelinkableCallSite

```java
public class
ChainedCallSite

extends
AbstractRelinkableCallSite
```

A relinkable call site that implements a polymorphic inline caching strategy.
It remembers up to 8

GuardedInvocation

s it was linked with, and on
each relink request builds a cascading chain of method handles of one
invocation falling back to the next one. The number of remembered invocations
can be customized by overriding

getMaxChainLength()

in a subclass.
When this call site is relinked with a new invocation and the length of the
chain is already at the maximum, it will throw away the oldest invocation.
Invocations with invalidated switch points and ones for which their
invalidating exception triggered are removed eagerly from the chain. The
invocations are never reordered; the most recently linked method handle is
always at the start of the chain and the least recently linked at its end.
The call site can be safely relinked on more than one thread concurrently.
Race conditions in linking are resolved by throwing away the

GuardedInvocation

produced on the losing thread without incorporating
it into the chain, so it can lead to repeated linking for the same arguments.

public class

ChainedCallSite

extends

AbstractRelinkableCallSite

A relinkable call site that implements a polymorphic inline caching strategy.
It remembers up to 8

GuardedInvocation

s it was linked with, and on
each relink request builds a cascading chain of method handles of one
invocation falling back to the next one. The number of remembered invocations
can be customized by overriding

getMaxChainLength()

in a subclass.
When this call site is relinked with a new invocation and the length of the
chain is already at the maximum, it will throw away the oldest invocation.
Invocations with invalidated switch points and ones for which their
invalidating exception triggered are removed eagerly from the chain. The
invocations are never reordered; the most recently linked method handle is
always at the start of the chain and the least recently linked at its end.
The call site can be safely relinked on more than one thread concurrently.
Race conditions in linking are resolved by throwing away the

GuardedInvocation

produced on the losing thread without incorporating
it into the chain, so it can lead to repeated linking for the same arguments.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ChainedCallSite

​(

CallSiteDescriptor

descriptor)

Creates a new chained call site.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected int

getMaxChainLength

()

The maximum number of method handles in the chain.

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

Constructor

Description

ChainedCallSite

​(

CallSiteDescriptor

descriptor)

Creates a new chained call site.

---

#### Constructor Summary

Creates a new chained call site.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected int

getMaxChainLength

()

The maximum number of method handles in the chain.

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

The maximum number of method handles in the chain.

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

- ChainedCallSite

```java
public ChainedCallSite​(
CallSiteDescriptor
descriptor)
```

Creates a new chained call site.

**Parameters:** descriptor

- the descriptor for the call site.

============ METHOD DETAIL ==========

- Method Detail

- getMaxChainLength

```java
protected int getMaxChainLength()
```

The maximum number of method handles in the chain. Defaults to 8. You can
override it in a subclass if you need to change the value.

**Returns:** the maximum number of method handles in the chain. The return
value is checked, and if your override returns a value less than 1, a

RuntimeException

will be thrown.

Constructor Detail

- ChainedCallSite

```java
public ChainedCallSite​(
CallSiteDescriptor
descriptor)
```

Creates a new chained call site.

**Parameters:** descriptor

- the descriptor for the call site.

---

#### Constructor Detail

ChainedCallSite

```java
public ChainedCallSite​(
CallSiteDescriptor
descriptor)
```

Creates a new chained call site.

**Parameters:** descriptor

- the descriptor for the call site.

---

#### ChainedCallSite

public ChainedCallSite​(

CallSiteDescriptor

descriptor)

Creates a new chained call site.

Method Detail

- getMaxChainLength

```java
protected int getMaxChainLength()
```

The maximum number of method handles in the chain. Defaults to 8. You can
override it in a subclass if you need to change the value.

**Returns:** the maximum number of method handles in the chain. The return
value is checked, and if your override returns a value less than 1, a

RuntimeException

will be thrown.

---

#### Method Detail

getMaxChainLength

```java
protected int getMaxChainLength()
```

The maximum number of method handles in the chain. Defaults to 8. You can
override it in a subclass if you need to change the value.

**Returns:** the maximum number of method handles in the chain. The return
value is checked, and if your override returns a value less than 1, a

RuntimeException

will be thrown.

---

#### getMaxChainLength

protected int getMaxChainLength()

The maximum number of method handles in the chain. Defaults to 8. You can
override it in a subclass if you need to change the value.

---

