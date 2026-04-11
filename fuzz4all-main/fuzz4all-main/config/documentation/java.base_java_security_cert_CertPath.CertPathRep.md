# Class CertPath.CertPathRep

**Source:** `java.base\java\security\cert\CertPath.CertPathRep.html`

### Class Description

```java
protected static class
CertPath.CertPathRep

extends
Object

implements
Serializable
```

Alternate

CertPath

class for serialization.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### protected CertPathRep​(
String
type,
byte[] data)

Creates a

CertPathRep

with the specified
type and encoded form of a certification path.

**Parameters:**
- type

- the standard name of a

CertPath

type
- data

- the encoded form of the certification path

---

### Method Details

#### protected
Object
readResolve()
throws
ObjectStreamException

Returns a

CertPath

constructed from the type and data.

**Returns:**
- the resolved

CertPath

object

**Throws:**
- ObjectStreamException

- if a

CertPath

could not
be constructed

---

### Additional Sections

#### Class CertPath.CertPathRep

java.lang.Object

- java.security.cert.CertPath.CertPathRep

java.security.cert.CertPath.CertPathRep

**All Implemented Interfaces:** Serializable

**Enclosing class:** CertPath

```java
protected static class
CertPath.CertPathRep

extends
Object

implements
Serializable
```

Alternate

CertPath

class for serialization.

**Since:** 1.4
**See Also:** Serialized Form

protected static class

CertPath.CertPathRep

extends

Object

implements

Serializable

Alternate

CertPath

class for serialization.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

CertPathRep

​(

String

type,
byte[] data)

Creates a

CertPathRep

with the specified
type and encoded form of a certification path.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

Object

readResolve

()

Returns a

CertPath

constructed from the type and data.

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

Modifier

Constructor

Description

protected

CertPathRep

​(

String

type,
byte[] data)

Creates a

CertPathRep

with the specified
type and encoded form of a certification path.

---

#### Constructor Summary

Creates a

CertPathRep

with the specified
type and encoded form of a certification path.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

Object

readResolve

()

Returns a

CertPath

constructed from the type and data.

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

Returns a

CertPath

constructed from the type and data.

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

- CertPathRep

```java
protected CertPathRep​(
String
type,
byte[] data)
```

Creates a

CertPathRep

with the specified
type and encoded form of a certification path.

**Parameters:** type

- the standard name of a

CertPath

type
**Parameters:** data

- the encoded form of the certification path

============ METHOD DETAIL ==========

- Method Detail

- readResolve

```java
protected
Object
readResolve()
throws
ObjectStreamException
```

Returns a

CertPath

constructed from the type and data.

**Returns:** the resolved

CertPath

object
**Throws:** ObjectStreamException

- if a

CertPath

could not
be constructed

Constructor Detail

- CertPathRep

```java
protected CertPathRep​(
String
type,
byte[] data)
```

Creates a

CertPathRep

with the specified
type and encoded form of a certification path.

**Parameters:** type

- the standard name of a

CertPath

type
**Parameters:** data

- the encoded form of the certification path

---

#### Constructor Detail

CertPathRep

```java
protected CertPathRep​(
String
type,
byte[] data)
```

Creates a

CertPathRep

with the specified
type and encoded form of a certification path.

**Parameters:** type

- the standard name of a

CertPath

type
**Parameters:** data

- the encoded form of the certification path

---

#### CertPathRep

protected CertPathRep​(

String

type,
byte[] data)

Creates a

CertPathRep

with the specified
type and encoded form of a certification path.

Method Detail

- readResolve

```java
protected
Object
readResolve()
throws
ObjectStreamException
```

Returns a

CertPath

constructed from the type and data.

**Returns:** the resolved

CertPath

object
**Throws:** ObjectStreamException

- if a

CertPath

could not
be constructed

---

#### Method Detail

readResolve

```java
protected
Object
readResolve()
throws
ObjectStreamException
```

Returns a

CertPath

constructed from the type and data.

**Returns:** the resolved

CertPath

object
**Throws:** ObjectStreamException

- if a

CertPath

could not
be constructed

---

#### readResolve

protected

Object

readResolve()
throws

ObjectStreamException

Returns a

CertPath

constructed from the type and data.

---

