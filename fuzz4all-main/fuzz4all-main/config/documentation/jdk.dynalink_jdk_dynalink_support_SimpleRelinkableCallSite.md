# Class SimpleRelinkableCallSite

**Source:** `jdk.dynalink\jdk\dynalink\support\SimpleRelinkableCallSite.html`

### Class Description

```java
public class
SimpleRelinkableCallSite

extends
AbstractRelinkableCallSite
```

A relinkable call site that implements monomorphic inline caching strategy,
only being linked to a single

GuardedInvocation

at any given time.
If the guard of that single invocation fails, or it has an invalidated
switch point, or its invalidating exception triggered, then the call site
will throw it away and ask its associated

DynamicLinker

to relink it.

**All Implemented Interfaces:** RelinkableCallSite

---

### Field Details

*No entries found.*

### Constructor Details

#### public SimpleRelinkableCallSite​(
CallSiteDescriptor
descriptor)

Creates a new call site with monomorphic inline caching strategy.

**Parameters:**
- descriptor

- the descriptor for this call site

---

### Method Details

*No entries found.*

### Additional Sections

#### Class SimpleRelinkableCallSite

java.lang.Object

- java.lang.invoke.CallSite
- - java.lang.invoke.MutableCallSite
- - jdk.dynalink.support.AbstractRelinkableCallSite
- - jdk.dynalink.support.SimpleRelinkableCallSite

java.lang.invoke.CallSite

- java.lang.invoke.MutableCallSite
- - jdk.dynalink.support.AbstractRelinkableCallSite
- - jdk.dynalink.support.SimpleRelinkableCallSite

java.lang.invoke.MutableCallSite

- jdk.dynalink.support.AbstractRelinkableCallSite
- - jdk.dynalink.support.SimpleRelinkableCallSite

jdk.dynalink.support.AbstractRelinkableCallSite

- jdk.dynalink.support.SimpleRelinkableCallSite

jdk.dynalink.support.SimpleRelinkableCallSite

**All Implemented Interfaces:** RelinkableCallSite

```java
public class
SimpleRelinkableCallSite

extends
AbstractRelinkableCallSite
```

A relinkable call site that implements monomorphic inline caching strategy,
only being linked to a single

GuardedInvocation

at any given time.
If the guard of that single invocation fails, or it has an invalidated
switch point, or its invalidating exception triggered, then the call site
will throw it away and ask its associated

DynamicLinker

to relink it.

public class

SimpleRelinkableCallSite

extends

AbstractRelinkableCallSite

A relinkable call site that implements monomorphic inline caching strategy,
only being linked to a single

GuardedInvocation

at any given time.
If the guard of that single invocation fails, or it has an invalidated
switch point, or its invalidating exception triggered, then the call site
will throw it away and ask its associated

DynamicLinker

to relink it.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SimpleRelinkableCallSite

​(

CallSiteDescriptor

descriptor)

Creates a new call site with monomorphic inline caching strategy.

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

Constructor

Description

SimpleRelinkableCallSite

​(

CallSiteDescriptor

descriptor)

Creates a new call site with monomorphic inline caching strategy.

---

#### Constructor Summary

Creates a new call site with monomorphic inline caching strategy.

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

- SimpleRelinkableCallSite

```java
public SimpleRelinkableCallSite​(
CallSiteDescriptor
descriptor)
```

Creates a new call site with monomorphic inline caching strategy.

**Parameters:** descriptor

- the descriptor for this call site

Constructor Detail

- SimpleRelinkableCallSite

```java
public SimpleRelinkableCallSite​(
CallSiteDescriptor
descriptor)
```

Creates a new call site with monomorphic inline caching strategy.

**Parameters:** descriptor

- the descriptor for this call site

---

#### Constructor Detail

SimpleRelinkableCallSite

```java
public SimpleRelinkableCallSite​(
CallSiteDescriptor
descriptor)
```

Creates a new call site with monomorphic inline caching strategy.

**Parameters:** descriptor

- the descriptor for this call site

---

#### SimpleRelinkableCallSite

public SimpleRelinkableCallSite​(

CallSiteDescriptor

descriptor)

Creates a new call site with monomorphic inline caching strategy.

---

