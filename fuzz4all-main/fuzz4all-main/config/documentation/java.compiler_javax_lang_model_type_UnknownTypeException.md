# Class UnknownTypeException

**Source:** `java.compiler\javax\lang\model\type\UnknownTypeException.html`

### Class Description

```java
public class
UnknownTypeException

extends
UnknownEntityException
```

Indicates that an unknown kind of type was encountered. This can
occur if the language evolves and new kinds of types are added to
the

TypeMirror

hierarchy. May be thrown by a

type visitor

to indicate that the visitor was created
for a prior version of the language.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public UnknownTypeException​(
TypeMirror
t,

Object
p)

Creates a new

UnknownTypeException

.The

p

parameter may be used to pass in an additional argument with
information about the context in which the unknown type was
encountered; for example, the visit methods of

TypeVisitor

may pass in their additional parameter.

**Parameters:**
- t

- the unknown type, may be

null
- p

- an additional parameter, may be

null

---

### Method Details

#### public
TypeMirror
getUnknownType()

Returns the unknown type.
The value may be unavailable if this exception has been
serialized and then read back in.

**Returns:**
- the unknown type, or

null

if unavailable

---

#### public
Object
getArgument()

Returns the additional argument.

**Returns:**
- the additional argument, or

null

if unavailable

---

### Additional Sections

#### Class UnknownTypeException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.lang.RuntimeException
- - javax.lang.model.UnknownEntityException
- - javax.lang.model.type.UnknownTypeException

java.lang.Throwable

- java.lang.Exception
- - java.lang.RuntimeException
- - javax.lang.model.UnknownEntityException
- - javax.lang.model.type.UnknownTypeException

java.lang.Exception

- java.lang.RuntimeException
- - javax.lang.model.UnknownEntityException
- - javax.lang.model.type.UnknownTypeException

java.lang.RuntimeException

- javax.lang.model.UnknownEntityException
- - javax.lang.model.type.UnknownTypeException

javax.lang.model.UnknownEntityException

- javax.lang.model.type.UnknownTypeException

javax.lang.model.type.UnknownTypeException

**All Implemented Interfaces:** Serializable

```java
public class
UnknownTypeException

extends
UnknownEntityException
```

Indicates that an unknown kind of type was encountered. This can
occur if the language evolves and new kinds of types are added to
the

TypeMirror

hierarchy. May be thrown by a

type visitor

to indicate that the visitor was created
for a prior version of the language.

**Since:** 1.6
**See Also:** TypeVisitor.visitUnknown(javax.lang.model.type.TypeMirror, P)

,

Serialized Form

public class

UnknownTypeException

extends

UnknownEntityException

Indicates that an unknown kind of type was encountered. This can
occur if the language evolves and new kinds of types are added to
the

TypeMirror

hierarchy. May be thrown by a

type visitor

to indicate that the visitor was created
for a prior version of the language.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

UnknownTypeException

​(

TypeMirror

t,

Object

p)

Creates a new

UnknownTypeException

.The

p

parameter may be used to pass in an additional argument with
information about the context in which the unknown type was
encountered; for example, the visit methods of

TypeVisitor

may pass in their additional parameter.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

getArgument

()

Returns the additional argument.

TypeMirror

getUnknownType

()

Returns the unknown type.

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

,

toString

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

wait

,

wait

,

wait

Constructor Summary

Constructors

Constructor

Description

UnknownTypeException

​(

TypeMirror

t,

Object

p)

Creates a new

UnknownTypeException

.The

p

parameter may be used to pass in an additional argument with
information about the context in which the unknown type was
encountered; for example, the visit methods of

TypeVisitor

may pass in their additional parameter.

---

#### Constructor Summary

Creates a new

UnknownTypeException

.The

p

parameter may be used to pass in an additional argument with
information about the context in which the unknown type was
encountered; for example, the visit methods of

TypeVisitor

may pass in their additional parameter.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

getArgument

()

Returns the additional argument.

TypeMirror

getUnknownType

()

Returns the unknown type.

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

,

toString

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

wait

,

wait

,

wait

---

#### Method Summary

Returns the additional argument.

Returns the unknown type.

Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

,

toString

---

#### Methods declared in class java.lang. Throwable

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- UnknownTypeException

```java
public UnknownTypeException​(
TypeMirror
t,

Object
p)
```

Creates a new

UnknownTypeException

.The

p

parameter may be used to pass in an additional argument with
information about the context in which the unknown type was
encountered; for example, the visit methods of

TypeVisitor

may pass in their additional parameter.

**Parameters:** t

- the unknown type, may be

null
**Parameters:** p

- an additional parameter, may be

null

============ METHOD DETAIL ==========

- Method Detail

- getUnknownType

```java
public
TypeMirror
getUnknownType()
```

Returns the unknown type.
The value may be unavailable if this exception has been
serialized and then read back in.

**Returns:** the unknown type, or

null

if unavailable

- getArgument

```java
public
Object
getArgument()
```

Returns the additional argument.

**Returns:** the additional argument, or

null

if unavailable

Constructor Detail

- UnknownTypeException

```java
public UnknownTypeException​(
TypeMirror
t,

Object
p)
```

Creates a new

UnknownTypeException

.The

p

parameter may be used to pass in an additional argument with
information about the context in which the unknown type was
encountered; for example, the visit methods of

TypeVisitor

may pass in their additional parameter.

**Parameters:** t

- the unknown type, may be

null
**Parameters:** p

- an additional parameter, may be

null

---

#### Constructor Detail

UnknownTypeException

```java
public UnknownTypeException​(
TypeMirror
t,

Object
p)
```

Creates a new

UnknownTypeException

.The

p

parameter may be used to pass in an additional argument with
information about the context in which the unknown type was
encountered; for example, the visit methods of

TypeVisitor

may pass in their additional parameter.

**Parameters:** t

- the unknown type, may be

null
**Parameters:** p

- an additional parameter, may be

null

---

#### UnknownTypeException

public UnknownTypeException​(

TypeMirror

t,

Object

p)

Creates a new

UnknownTypeException

.The

p

parameter may be used to pass in an additional argument with
information about the context in which the unknown type was
encountered; for example, the visit methods of

TypeVisitor

may pass in their additional parameter.

Method Detail

- getUnknownType

```java
public
TypeMirror
getUnknownType()
```

Returns the unknown type.
The value may be unavailable if this exception has been
serialized and then read back in.

**Returns:** the unknown type, or

null

if unavailable

- getArgument

```java
public
Object
getArgument()
```

Returns the additional argument.

**Returns:** the additional argument, or

null

if unavailable

---

#### Method Detail

getUnknownType

```java
public
TypeMirror
getUnknownType()
```

Returns the unknown type.
The value may be unavailable if this exception has been
serialized and then read back in.

**Returns:** the unknown type, or

null

if unavailable

---

#### getUnknownType

public

TypeMirror

getUnknownType()

Returns the unknown type.
The value may be unavailable if this exception has been
serialized and then read back in.

getArgument

```java
public
Object
getArgument()
```

Returns the additional argument.

**Returns:** the additional argument, or

null

if unavailable

---

#### getArgument

public

Object

getArgument()

Returns the additional argument.

---

