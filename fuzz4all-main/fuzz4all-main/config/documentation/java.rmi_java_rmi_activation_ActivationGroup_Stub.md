# Class ActivationGroup_Stub

**Source:** `java.rmi\java\rmi\activation\ActivationGroup_Stub.html`

### Class Description

```java
public final class
ActivationGroup_Stub

extends
RemoteStub

implements
ActivationInstantiator
,
Remote
```

ActivationGroup_Stub

is a stub class
for the subclasses of

java.rmi.activation.ActivationGroup

that are exported as a

java.rmi.server.UnicastRemoteObject

.

**All Implemented Interfaces:** Serializable

,

ActivationInstantiator

,

Remote

---

### Field Details

*No entries found.*

### Constructor Details

#### public ActivationGroup_Stub​(
RemoteRef
ref)

Constructs a stub for the

ActivationGroup

class. It
invokes the superclass

RemoteStub(RemoteRef)

constructor with its argument,

ref

.

**Parameters:**
- ref

- a remote ref

---

### Method Details

#### public
MarshalledObject
newInstance​(
ActivationID
id,

ActivationDesc
desc)
throws
RemoteException
,

ActivationException

Stub method for

ActivationGroup.newInstance

. Invokes
the

invoke

method on this instance's

RemoteObject.ref

field, with

this

as the
first argument, a two-element

Object[]

as the second
argument (with

id

as the first element and

desc

as the second element), and -5274445189091581345L
as the third argument, and returns the result. If that invocation
throws a

RuntimeException

,

RemoteException

,
or an

ActivationException

, then that exception is
thrown to the caller. If that invocation throws any other

java.lang.Exception

, then a

java.rmi.UnexpectedException

is thrown to the caller
with the original exception as the cause.

**Specified by:**
- newInstance

in interface

ActivationInstantiator

**Parameters:**
- id

- an activation identifier
- desc

- an activation descriptor

**Returns:**
- the result of the invocation

**Throws:**
- RemoteException

- if invocation results in
a

RemoteException
- ActivationException

- if invocation
results in an

ActivationException

---

### Additional Sections

#### Class ActivationGroup_Stub

java.lang.Object

- java.rmi.server.RemoteObject
- - java.rmi.server.RemoteStub
- - java.rmi.activation.ActivationGroup_Stub

java.rmi.server.RemoteObject

- java.rmi.server.RemoteStub
- - java.rmi.activation.ActivationGroup_Stub

java.rmi.server.RemoteStub

- java.rmi.activation.ActivationGroup_Stub

java.rmi.activation.ActivationGroup_Stub

**All Implemented Interfaces:** Serializable

,

ActivationInstantiator

,

Remote

```java
public final class
ActivationGroup_Stub

extends
RemoteStub

implements
ActivationInstantiator
,
Remote
```

ActivationGroup_Stub

is a stub class
for the subclasses of

java.rmi.activation.ActivationGroup

that are exported as a

java.rmi.server.UnicastRemoteObject

.

**Since:** 1.2
**See Also:** Serialized Form

public final class

ActivationGroup_Stub

extends

RemoteStub

implements

ActivationInstantiator

,

Remote

ActivationGroup_Stub

is a stub class
for the subclasses of

java.rmi.activation.ActivationGroup

that are exported as a

java.rmi.server.UnicastRemoteObject

.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.rmi.server.

RemoteObject

ref

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ActivationGroup_Stub

​(

RemoteRef

ref)

Constructs a stub for the

ActivationGroup

class.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

MarshalledObject

newInstance

​(

ActivationID

id,

ActivationDesc

desc)

Stub method for

ActivationGroup.newInstance

.

- Methods declared in class java.rmi.server.

RemoteStub

setRef

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

Constructor

Description

ActivationGroup_Stub

​(

RemoteRef

ref)

Constructs a stub for the

ActivationGroup

class.

---

#### Constructor Summary

Constructs a stub for the

ActivationGroup

class.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

MarshalledObject

newInstance

​(

ActivationID

id,

ActivationDesc

desc)

Stub method for

ActivationGroup.newInstance

.

- Methods declared in class java.rmi.server.

RemoteStub

setRef

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

Stub method for

ActivationGroup.newInstance

.

Methods declared in class java.rmi.server.

RemoteStub

setRef

---

#### Methods declared in class java.rmi.server. RemoteStub

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

- ActivationGroup_Stub

```java
public ActivationGroup_Stub​(
RemoteRef
ref)
```

Constructs a stub for the

ActivationGroup

class. It
invokes the superclass

RemoteStub(RemoteRef)

constructor with its argument,

ref

.

**Parameters:** ref

- a remote ref

============ METHOD DETAIL ==========

- Method Detail

- newInstance

```java
public
MarshalledObject
newInstance​(
ActivationID
id,

ActivationDesc
desc)
throws
RemoteException
,

ActivationException
```

Stub method for

ActivationGroup.newInstance

. Invokes
the

invoke

method on this instance's

RemoteObject.ref

field, with

this

as the
first argument, a two-element

Object[]

as the second
argument (with

id

as the first element and

desc

as the second element), and -5274445189091581345L
as the third argument, and returns the result. If that invocation
throws a

RuntimeException

,

RemoteException

,
or an

ActivationException

, then that exception is
thrown to the caller. If that invocation throws any other

java.lang.Exception

, then a

java.rmi.UnexpectedException

is thrown to the caller
with the original exception as the cause.

**Specified by:** newInstance

in interface

ActivationInstantiator
**Parameters:** id

- an activation identifier
**Parameters:** desc

- an activation descriptor
**Returns:** the result of the invocation
**Throws:** RemoteException

- if invocation results in
a

RemoteException
**Throws:** ActivationException

- if invocation
results in an

ActivationException

Constructor Detail

- ActivationGroup_Stub

```java
public ActivationGroup_Stub​(
RemoteRef
ref)
```

Constructs a stub for the

ActivationGroup

class. It
invokes the superclass

RemoteStub(RemoteRef)

constructor with its argument,

ref

.

**Parameters:** ref

- a remote ref

---

#### Constructor Detail

ActivationGroup_Stub

```java
public ActivationGroup_Stub​(
RemoteRef
ref)
```

Constructs a stub for the

ActivationGroup

class. It
invokes the superclass

RemoteStub(RemoteRef)

constructor with its argument,

ref

.

**Parameters:** ref

- a remote ref

---

#### ActivationGroup_Stub

public ActivationGroup_Stub​(

RemoteRef

ref)

Constructs a stub for the

ActivationGroup

class. It
invokes the superclass

RemoteStub(RemoteRef)

constructor with its argument,

ref

.

Method Detail

- newInstance

```java
public
MarshalledObject
newInstance​(
ActivationID
id,

ActivationDesc
desc)
throws
RemoteException
,

ActivationException
```

Stub method for

ActivationGroup.newInstance

. Invokes
the

invoke

method on this instance's

RemoteObject.ref

field, with

this

as the
first argument, a two-element

Object[]

as the second
argument (with

id

as the first element and

desc

as the second element), and -5274445189091581345L
as the third argument, and returns the result. If that invocation
throws a

RuntimeException

,

RemoteException

,
or an

ActivationException

, then that exception is
thrown to the caller. If that invocation throws any other

java.lang.Exception

, then a

java.rmi.UnexpectedException

is thrown to the caller
with the original exception as the cause.

**Specified by:** newInstance

in interface

ActivationInstantiator
**Parameters:** id

- an activation identifier
**Parameters:** desc

- an activation descriptor
**Returns:** the result of the invocation
**Throws:** RemoteException

- if invocation results in
a

RemoteException
**Throws:** ActivationException

- if invocation
results in an

ActivationException

---

#### Method Detail

newInstance

```java
public
MarshalledObject
newInstance​(
ActivationID
id,

ActivationDesc
desc)
throws
RemoteException
,

ActivationException
```

Stub method for

ActivationGroup.newInstance

. Invokes
the

invoke

method on this instance's

RemoteObject.ref

field, with

this

as the
first argument, a two-element

Object[]

as the second
argument (with

id

as the first element and

desc

as the second element), and -5274445189091581345L
as the third argument, and returns the result. If that invocation
throws a

RuntimeException

,

RemoteException

,
or an

ActivationException

, then that exception is
thrown to the caller. If that invocation throws any other

java.lang.Exception

, then a

java.rmi.UnexpectedException

is thrown to the caller
with the original exception as the cause.

**Specified by:** newInstance

in interface

ActivationInstantiator
**Parameters:** id

- an activation identifier
**Parameters:** desc

- an activation descriptor
**Returns:** the result of the invocation
**Throws:** RemoteException

- if invocation results in
a

RemoteException
**Throws:** ActivationException

- if invocation
results in an

ActivationException

---

#### newInstance

public

MarshalledObject

newInstance​(

ActivationID

id,

ActivationDesc

desc)
throws

RemoteException

,

ActivationException

Stub method for

ActivationGroup.newInstance

. Invokes
the

invoke

method on this instance's

RemoteObject.ref

field, with

this

as the
first argument, a two-element

Object[]

as the second
argument (with

id

as the first element and

desc

as the second element), and -5274445189091581345L
as the third argument, and returns the result. If that invocation
throws a

RuntimeException

,

RemoteException

,
or an

ActivationException

, then that exception is
thrown to the caller. If that invocation throws any other

java.lang.Exception

, then a

java.rmi.UnexpectedException

is thrown to the caller
with the original exception as the cause.

---

