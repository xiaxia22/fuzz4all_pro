# Class RemoteStub

**Source:** `java.rmi\java\rmi\server\RemoteStub.html`

### Class Description

```java
@Deprecated

public abstract class
RemoteStub

extends
RemoteObject
```

The

RemoteStub

class is the common superclass of
statically generated client
stubs and provides the framework to support a wide range of remote
reference semantics. Stub objects are surrogates that support
exactly the same set of remote interfaces defined by the actual
implementation of the remote object.

**All Implemented Interfaces:** Serializable

,

Remote

---

### Field Details

*No entries found.*

### Constructor Details

#### protected RemoteStub()

Constructs a

RemoteStub

.

---

#### protected RemoteStub​(
RemoteRef
ref)

Constructs a

RemoteStub

with the specified remote
reference.

**Parameters:**
- ref

- the remote reference

**Since:**
- 1.1

---

### Method Details

#### @Deprecated

protected static void setRef​(
RemoteStub
stub,

RemoteRef
ref)

Throws

UnsupportedOperationException

.

**Parameters:**
- stub

- the remote stub
- ref

- the remote reference

**Throws:**
- UnsupportedOperationException

- always

**Since:**
- 1.1

---

### Additional Sections

#### Class RemoteStub

java.lang.Object

- java.rmi.server.RemoteObject
- - java.rmi.server.RemoteStub

java.rmi.server.RemoteObject

- java.rmi.server.RemoteStub

java.rmi.server.RemoteStub

**All Implemented Interfaces:** Serializable

,

Remote

**Direct Known Subclasses:** ActivationGroup_Stub

,

RMIConnectionImpl_Stub

,

RMIServerImpl_Stub

```java
@Deprecated

public abstract class
RemoteStub

extends
RemoteObject
```

Deprecated.

Statically generated stubs are deprecated, since
stubs are generated dynamically. See

UnicastRemoteObject

for information about dynamic stub generation.

The

RemoteStub

class is the common superclass of
statically generated client
stubs and provides the framework to support a wide range of remote
reference semantics. Stub objects are surrogates that support
exactly the same set of remote interfaces defined by the actual
implementation of the remote object.

**Since:** 1.1
**See Also:** Serialized Form

@Deprecated

public abstract class

RemoteStub

extends

RemoteObject

The

RemoteStub

class is the common superclass of
statically generated client
stubs and provides the framework to support a wide range of remote
reference semantics. Stub objects are surrogates that support
exactly the same set of remote interfaces defined by the actual
implementation of the remote object.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.rmi.server.

RemoteObject

ref

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

RemoteStub

()

Deprecated.

Constructs a

RemoteStub

.

protected

RemoteStub

​(

RemoteRef

ref)

Deprecated.

Constructs a

RemoteStub

with the specified remote
reference.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

protected static void

setRef

​(

RemoteStub

stub,

RemoteRef

ref)

Deprecated.

No replacement.

- Methods declared in class java.rmi.server.

RemoteObject

equals

,

getRef

,

hashCode

,

toString

,

toStub

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

Field Summary

- Fields declared in class java.rmi.server.

RemoteObject

ref

---

#### Field Summary

Fields declared in class java.rmi.server.

RemoteObject

ref

---

#### Fields declared in class java.rmi.server. RemoteObject

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

RemoteStub

()

Deprecated.

Constructs a

RemoteStub

.

protected

RemoteStub

​(

RemoteRef

ref)

Deprecated.

Constructs a

RemoteStub

with the specified remote
reference.

---

#### Constructor Summary

Deprecated.

Constructs a

RemoteStub

.

Constructs a

RemoteStub

with the specified remote
reference.

Method Summary

All Methods

Static Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

protected static void

setRef

​(

RemoteStub

stub,

RemoteRef

ref)

Deprecated.

No replacement.

- Methods declared in class java.rmi.server.

RemoteObject

equals

,

getRef

,

hashCode

,

toString

,

toStub

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

Deprecated.

No replacement.

Methods declared in class java.rmi.server.

RemoteObject

equals

,

getRef

,

hashCode

,

toString

,

toStub

---

#### Methods declared in class java.rmi.server. RemoteObject

Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

- RemoteStub

```java
protected RemoteStub()
```

Deprecated.

Constructs a

RemoteStub

.

- RemoteStub

```java
protected RemoteStub​(
RemoteRef
ref)
```

Deprecated.

Constructs a

RemoteStub

with the specified remote
reference.

**Parameters:** ref

- the remote reference
**Since:** 1.1

============ METHOD DETAIL ==========

- Method Detail

- setRef

```java
@Deprecated

protected static void setRef​(
RemoteStub
stub,

RemoteRef
ref)
```

Deprecated.

No replacement. The

setRef

method
was intended for setting the remote reference of a remote
stub. This is unnecessary, since

RemoteStub

s can be created
and initialized with a remote reference through use of
the

RemoteStub(RemoteRef)

constructor.

Throws

UnsupportedOperationException

.

**Parameters:** stub

- the remote stub
**Parameters:** ref

- the remote reference
**Throws:** UnsupportedOperationException

- always
**Since:** 1.1

Constructor Detail

- RemoteStub

```java
protected RemoteStub()
```

Deprecated.

Constructs a

RemoteStub

.

- RemoteStub

```java
protected RemoteStub​(
RemoteRef
ref)
```

Deprecated.

Constructs a

RemoteStub

with the specified remote
reference.

**Parameters:** ref

- the remote reference
**Since:** 1.1

---

#### Constructor Detail

RemoteStub

```java
protected RemoteStub()
```

Deprecated.

Constructs a

RemoteStub

.

---

#### RemoteStub

protected RemoteStub()

Constructs a

RemoteStub

.

RemoteStub

```java
protected RemoteStub​(
RemoteRef
ref)
```

Deprecated.

Constructs a

RemoteStub

with the specified remote
reference.

**Parameters:** ref

- the remote reference
**Since:** 1.1

---

#### RemoteStub

protected RemoteStub​(

RemoteRef

ref)

Constructs a

RemoteStub

with the specified remote
reference.

Method Detail

- setRef

```java
@Deprecated

protected static void setRef​(
RemoteStub
stub,

RemoteRef
ref)
```

Deprecated.

No replacement. The

setRef

method
was intended for setting the remote reference of a remote
stub. This is unnecessary, since

RemoteStub

s can be created
and initialized with a remote reference through use of
the

RemoteStub(RemoteRef)

constructor.

Throws

UnsupportedOperationException

.

**Parameters:** stub

- the remote stub
**Parameters:** ref

- the remote reference
**Throws:** UnsupportedOperationException

- always
**Since:** 1.1

---

#### Method Detail

setRef

```java
@Deprecated

protected static void setRef​(
RemoteStub
stub,

RemoteRef
ref)
```

Deprecated.

No replacement. The

setRef

method
was intended for setting the remote reference of a remote
stub. This is unnecessary, since

RemoteStub

s can be created
and initialized with a remote reference through use of
the

RemoteStub(RemoteRef)

constructor.

Throws

UnsupportedOperationException

.

**Parameters:** stub

- the remote stub
**Parameters:** ref

- the remote reference
**Throws:** UnsupportedOperationException

- always
**Since:** 1.1

---

#### setRef

@Deprecated

protected static void setRef​(

RemoteStub

stub,

RemoteRef

ref)

Throws

UnsupportedOperationException

.

---

