# Class CRL

**Source:** `java.base\java\security\cert\CRL.html`

### Class Description

```java
public abstract class
CRL

extends
Object
```

This class is an abstraction of certificate revocation lists (CRLs) that
have different formats but important common uses. For example, all CRLs
share the functionality of listing revoked certificates, and can be queried
on whether or not they list a given certificate.

Specialized CRL types can be defined by subclassing off of this abstract
class.

**Direct Known Subclasses:** X509CRL

---

### Field Details

*No entries found.*

### Constructor Details

#### protected CRL​(
String
type)

Creates a CRL of the specified type.

**Parameters:**
- type

- the standard name of the CRL type.
See the

Java Security Standard Algorithm Names

document
for information about standard CRL types.

---

### Method Details

#### public final
String
getType()

Returns the type of this CRL.

**Returns:**
- the type of this CRL.

---

#### public abstract
String
toString()

Returns a string representation of this CRL.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this CRL.

---

#### public abstract boolean isRevoked​(
Certificate
cert)

Checks whether the given certificate is on this CRL.

**Parameters:**
- cert

- the certificate to check for.

**Returns:**
- true if the given certificate is on this CRL,
false otherwise.

---

### Additional Sections

#### Class CRL

java.lang.Object

- java.security.cert.CRL

java.security.cert.CRL

**Direct Known Subclasses:** X509CRL

```java
public abstract class
CRL

extends
Object
```

This class is an abstraction of certificate revocation lists (CRLs) that
have different formats but important common uses. For example, all CRLs
share the functionality of listing revoked certificates, and can be queried
on whether or not they list a given certificate.

Specialized CRL types can be defined by subclassing off of this abstract
class.

**Since:** 1.2
**See Also:** X509CRL

,

CertificateFactory

public abstract class

CRL

extends

Object

This class is an abstraction of certificate revocation lists (CRLs) that
have different formats but important common uses. For example, all CRLs
share the functionality of listing revoked certificates, and can be queried
on whether or not they list a given certificate.

Specialized CRL types can be defined by subclassing off of this abstract
class.

Specialized CRL types can be defined by subclassing off of this abstract
class.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

CRL

​(

String

type)

Creates a CRL of the specified type.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

String

getType

()

Returns the type of this CRL.

abstract boolean

isRevoked

​(

Certificate

cert)

Checks whether the given certificate is on this CRL.

abstract

String

toString

()

Returns a string representation of this CRL.

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

Modifier

Constructor

Description

protected

CRL

​(

String

type)

Creates a CRL of the specified type.

---

#### Constructor Summary

Creates a CRL of the specified type.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

String

getType

()

Returns the type of this CRL.

abstract boolean

isRevoked

​(

Certificate

cert)

Checks whether the given certificate is on this CRL.

abstract

String

toString

()

Returns a string representation of this CRL.

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

Returns the type of this CRL.

Checks whether the given certificate is on this CRL.

Returns a string representation of this CRL.

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

- CRL

```java
protected CRL​(
String
type)
```

Creates a CRL of the specified type.

**Parameters:** type

- the standard name of the CRL type.
See the

Java Security Standard Algorithm Names

document
for information about standard CRL types.

============ METHOD DETAIL ==========

- Method Detail

- getType

```java
public final
String
getType()
```

Returns the type of this CRL.

**Returns:** the type of this CRL.

- toString

```java
public abstract
String
toString()
```

Returns a string representation of this CRL.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this CRL.

- isRevoked

```java
public abstract boolean isRevoked​(
Certificate
cert)
```

Checks whether the given certificate is on this CRL.

**Parameters:** cert

- the certificate to check for.
**Returns:** true if the given certificate is on this CRL,
false otherwise.

Constructor Detail

- CRL

```java
protected CRL​(
String
type)
```

Creates a CRL of the specified type.

**Parameters:** type

- the standard name of the CRL type.
See the

Java Security Standard Algorithm Names

document
for information about standard CRL types.

---

#### Constructor Detail

CRL

```java
protected CRL​(
String
type)
```

Creates a CRL of the specified type.

**Parameters:** type

- the standard name of the CRL type.
See the

Java Security Standard Algorithm Names

document
for information about standard CRL types.

---

#### CRL

protected CRL​(

String

type)

Creates a CRL of the specified type.

Method Detail

- getType

```java
public final
String
getType()
```

Returns the type of this CRL.

**Returns:** the type of this CRL.

- toString

```java
public abstract
String
toString()
```

Returns a string representation of this CRL.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this CRL.

- isRevoked

```java
public abstract boolean isRevoked​(
Certificate
cert)
```

Checks whether the given certificate is on this CRL.

**Parameters:** cert

- the certificate to check for.
**Returns:** true if the given certificate is on this CRL,
false otherwise.

---

#### Method Detail

getType

```java
public final
String
getType()
```

Returns the type of this CRL.

**Returns:** the type of this CRL.

---

#### getType

public final

String

getType()

Returns the type of this CRL.

toString

```java
public abstract
String
toString()
```

Returns a string representation of this CRL.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this CRL.

---

#### toString

public abstract

String

toString()

Returns a string representation of this CRL.

isRevoked

```java
public abstract boolean isRevoked​(
Certificate
cert)
```

Checks whether the given certificate is on this CRL.

**Parameters:** cert

- the certificate to check for.
**Returns:** true if the given certificate is on this CRL,
false otherwise.

---

#### isRevoked

public abstract boolean isRevoked​(

Certificate

cert)

Checks whether the given certificate is on this CRL.

---

