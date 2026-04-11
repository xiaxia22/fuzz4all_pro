# Class SimpleLinkRequest

**Source:** `jdk.dynalink\jdk\dynalink\linker\support\SimpleLinkRequest.html`

### Class Description

```java
public class
SimpleLinkRequest

extends
Object

implements
LinkRequest
```

Default simple implementation of

LinkRequest

.

**All Implemented Interfaces:** LinkRequest

---

### Field Details

*No entries found.*

### Constructor Details

#### public SimpleLinkRequest​(
CallSiteDescriptor
callSiteDescriptor,
boolean callSiteUnstable,

Object
... arguments)

Creates a new link request.

**Parameters:**
- callSiteDescriptor

- the descriptor for the call site being linked.
Must not be null.
- callSiteUnstable

- true if the call site being linked is considered
unstable.
- arguments

- the arguments for the invocation. Must not be null.

**Throws:**
- NullPointerException

- if either

callSiteDescriptor

or

arguments

is null.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class SimpleLinkRequest

java.lang.Object

- jdk.dynalink.linker.support.SimpleLinkRequest

jdk.dynalink.linker.support.SimpleLinkRequest

**All Implemented Interfaces:** LinkRequest

```java
public class
SimpleLinkRequest

extends
Object

implements
LinkRequest
```

Default simple implementation of

LinkRequest

.

public class

SimpleLinkRequest

extends

Object

implements

LinkRequest

Default simple implementation of

LinkRequest

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SimpleLinkRequest

​(

CallSiteDescriptor

callSiteDescriptor,
boolean callSiteUnstable,

Object

... arguments)

Creates a new link request.

========== METHOD SUMMARY ===========

- Method Summary

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

- Methods declared in interface jdk.dynalink.linker.

LinkRequest

getArguments

,

getCallSiteDescriptor

,

getReceiver

,

isCallSiteUnstable

,

replaceArguments

Constructor Summary

Constructors

Constructor

Description

SimpleLinkRequest

​(

CallSiteDescriptor

callSiteDescriptor,
boolean callSiteUnstable,

Object

... arguments)

Creates a new link request.

---

#### Constructor Summary

Creates a new link request.

Method Summary

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

- Methods declared in interface jdk.dynalink.linker.

LinkRequest

getArguments

,

getCallSiteDescriptor

,

getReceiver

,

isCallSiteUnstable

,

replaceArguments

---

#### Method Summary

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

Methods declared in interface jdk.dynalink.linker.

LinkRequest

getArguments

,

getCallSiteDescriptor

,

getReceiver

,

isCallSiteUnstable

,

replaceArguments

---

#### Methods declared in interface jdk.dynalink.linker. LinkRequest

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SimpleLinkRequest

```java
public SimpleLinkRequest​(
CallSiteDescriptor
callSiteDescriptor,
boolean callSiteUnstable,

Object
... arguments)
```

Creates a new link request.

**Parameters:** callSiteDescriptor

- the descriptor for the call site being linked.
Must not be null.
**Parameters:** callSiteUnstable

- true if the call site being linked is considered
unstable.
**Parameters:** arguments

- the arguments for the invocation. Must not be null.
**Throws:** NullPointerException

- if either

callSiteDescriptor

or

arguments

is null.

Constructor Detail

- SimpleLinkRequest

```java
public SimpleLinkRequest​(
CallSiteDescriptor
callSiteDescriptor,
boolean callSiteUnstable,

Object
... arguments)
```

Creates a new link request.

**Parameters:** callSiteDescriptor

- the descriptor for the call site being linked.
Must not be null.
**Parameters:** callSiteUnstable

- true if the call site being linked is considered
unstable.
**Parameters:** arguments

- the arguments for the invocation. Must not be null.
**Throws:** NullPointerException

- if either

callSiteDescriptor

or

arguments

is null.

---

#### Constructor Detail

SimpleLinkRequest

```java
public SimpleLinkRequest​(
CallSiteDescriptor
callSiteDescriptor,
boolean callSiteUnstable,

Object
... arguments)
```

Creates a new link request.

**Parameters:** callSiteDescriptor

- the descriptor for the call site being linked.
Must not be null.
**Parameters:** callSiteUnstable

- true if the call site being linked is considered
unstable.
**Parameters:** arguments

- the arguments for the invocation. Must not be null.
**Throws:** NullPointerException

- if either

callSiteDescriptor

or

arguments

is null.

---

#### SimpleLinkRequest

public SimpleLinkRequest​(

CallSiteDescriptor

callSiteDescriptor,
boolean callSiteUnstable,

Object

... arguments)

Creates a new link request.

---

