# Class Certificate.CertificateRep

**Source:** `java.base\java\security\cert\Certificate.CertificateRep.html`

### Class Description

```java
protected static class
Certificate.CertificateRep

extends
Object

implements
Serializable
```

Alternate Certificate class for serialization.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### protected CertificateRep​(
String
type,
byte[] data)

Construct the alternate Certificate class with the Certificate
type and Certificate encoding bytes.

**Parameters:**
- type

- the standard name of the Certificate type.
- data

- the Certificate data.

---

### Method Details

#### protected
Object
readResolve()
throws
ObjectStreamException

Resolve the Certificate Object.

**Returns:**
- the resolved Certificate Object

**Throws:**
- ObjectStreamException

- if the Certificate
could not be resolved

---

### Additional Sections

#### Class Certificate.CertificateRep

java.lang.Object

- java.security.cert.Certificate.CertificateRep

java.security.cert.Certificate.CertificateRep

**All Implemented Interfaces:** Serializable

**Enclosing class:** Certificate

```java
protected static class
Certificate.CertificateRep

extends
Object

implements
Serializable
```

Alternate Certificate class for serialization.

**Since:** 1.3
**See Also:** Serialized Form

protected static class

Certificate.CertificateRep

extends

Object

implements

Serializable

Alternate Certificate class for serialization.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

CertificateRep

​(

String

type,
byte[] data)

Construct the alternate Certificate class with the Certificate
type and Certificate encoding bytes.

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

Resolve the Certificate Object.

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

CertificateRep

​(

String

type,
byte[] data)

Construct the alternate Certificate class with the Certificate
type and Certificate encoding bytes.

---

#### Constructor Summary

Construct the alternate Certificate class with the Certificate
type and Certificate encoding bytes.

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

Resolve the Certificate Object.

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

Resolve the Certificate Object.

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

- CertificateRep

```java
protected CertificateRep​(
String
type,
byte[] data)
```

Construct the alternate Certificate class with the Certificate
type and Certificate encoding bytes.

**Parameters:** type

- the standard name of the Certificate type.
**Parameters:** data

- the Certificate data.

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

Resolve the Certificate Object.

**Returns:** the resolved Certificate Object
**Throws:** ObjectStreamException

- if the Certificate
could not be resolved

Constructor Detail

- CertificateRep

```java
protected CertificateRep​(
String
type,
byte[] data)
```

Construct the alternate Certificate class with the Certificate
type and Certificate encoding bytes.

**Parameters:** type

- the standard name of the Certificate type.
**Parameters:** data

- the Certificate data.

---

#### Constructor Detail

CertificateRep

```java
protected CertificateRep​(
String
type,
byte[] data)
```

Construct the alternate Certificate class with the Certificate
type and Certificate encoding bytes.

**Parameters:** type

- the standard name of the Certificate type.
**Parameters:** data

- the Certificate data.

---

#### CertificateRep

protected CertificateRep​(

String

type,
byte[] data)

Construct the alternate Certificate class with the Certificate
type and Certificate encoding bytes.

Method Detail

- readResolve

```java
protected
Object
readResolve()
throws
ObjectStreamException
```

Resolve the Certificate Object.

**Returns:** the resolved Certificate Object
**Throws:** ObjectStreamException

- if the Certificate
could not be resolved

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

Resolve the Certificate Object.

**Returns:** the resolved Certificate Object
**Throws:** ObjectStreamException

- if the Certificate
could not be resolved

---

#### readResolve

protected

Object

readResolve()
throws

ObjectStreamException

Resolve the Certificate Object.

---

