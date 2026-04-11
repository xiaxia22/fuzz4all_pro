# Class CodeSigner

**Source:** `java.base\java\security\CodeSigner.html`

### Class Description

```java
public final class
CodeSigner

extends
Object

implements
Serializable
```

This class encapsulates information about a code signer.
It is immutable.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public CodeSigner​(
CertPath
signerCertPath,

Timestamp
timestamp)

Constructs a CodeSigner object.

**Parameters:**
- signerCertPath

- The signer's certificate path.
It must not be

null

.
- timestamp

- A signature timestamp.
If

null

then no timestamp was generated
for the signature.

**Throws:**
- NullPointerException

- if

signerCertPath

is

null

.

---

### Method Details

#### public
CertPath
getSignerCertPath()

Returns the signer's certificate path.

**Returns:**
- A certificate path.

---

#### public
Timestamp
getTimestamp()

Returns the signature timestamp.

**Returns:**
- The timestamp or

null

if none is present.

---

#### public int hashCode()

Returns the hash code value for this code signer.
The hash code is generated using the signer's certificate path and the
timestamp, if present.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code value for this code signer.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public boolean equals​(
Object
obj)

Tests for equality between the specified object and this
code signer. Two code signers are considered equal if their
signer certificate paths are equal and if their timestamps are equal,
if present in both.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the object to test for equality with this object.

**Returns:**
- true if the objects are considered equal, false otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public
String
toString()

Returns a string describing this code signer.

**Overrides:**
- toString

in class

Object

**Returns:**
- A string comprising the signer's certificate and a timestamp,
if present.

---

### Additional Sections

#### Class CodeSigner

java.lang.Object

- java.security.CodeSigner

java.security.CodeSigner

**All Implemented Interfaces:** Serializable

```java
public final class
CodeSigner

extends
Object

implements
Serializable
```

This class encapsulates information about a code signer.
It is immutable.

**Since:** 1.5
**See Also:** Serialized Form

public final class

CodeSigner

extends

Object

implements

Serializable

This class encapsulates information about a code signer.
It is immutable.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

CodeSigner

​(

CertPath

signerCertPath,

Timestamp

timestamp)

Constructs a CodeSigner object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Tests for equality between the specified object and this
code signer.

CertPath

getSignerCertPath

()

Returns the signer's certificate path.

Timestamp

getTimestamp

()

Returns the signature timestamp.

int

hashCode

()

Returns the hash code value for this code signer.

String

toString

()

Returns a string describing this code signer.

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

Constructor Summary

Constructors

Constructor

Description

CodeSigner

​(

CertPath

signerCertPath,

Timestamp

timestamp)

Constructs a CodeSigner object.

---

#### Constructor Summary

Constructs a CodeSigner object.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Tests for equality between the specified object and this
code signer.

CertPath

getSignerCertPath

()

Returns the signer's certificate path.

Timestamp

getTimestamp

()

Returns the signature timestamp.

int

hashCode

()

Returns the hash code value for this code signer.

String

toString

()

Returns a string describing this code signer.

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

Tests for equality between the specified object and this
code signer.

Returns the signer's certificate path.

Returns the signature timestamp.

Returns the hash code value for this code signer.

Returns a string describing this code signer.

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

- CodeSigner

```java
public CodeSigner​(
CertPath
signerCertPath,

Timestamp
timestamp)
```

Constructs a CodeSigner object.

**Parameters:** signerCertPath

- The signer's certificate path.
It must not be

null

.
**Parameters:** timestamp

- A signature timestamp.
If

null

then no timestamp was generated
for the signature.
**Throws:** NullPointerException

- if

signerCertPath

is

null

.

============ METHOD DETAIL ==========

- Method Detail

- getSignerCertPath

```java
public
CertPath
getSignerCertPath()
```

Returns the signer's certificate path.

**Returns:** A certificate path.

- getTimestamp

```java
public
Timestamp
getTimestamp()
```

Returns the signature timestamp.

**Returns:** The timestamp or

null

if none is present.

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this code signer.
The hash code is generated using the signer's certificate path and the
timestamp, if present.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this code signer.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
obj)
```

Tests for equality between the specified object and this
code signer. Two code signers are considered equal if their
signer certificate paths are equal and if their timestamps are equal,
if present in both.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to test for equality with this object.
**Returns:** true if the objects are considered equal, false otherwise.
**See Also:** Object.hashCode()

,

HashMap

- toString

```java
public
String
toString()
```

Returns a string describing this code signer.

**Overrides:** toString

in class

Object
**Returns:** A string comprising the signer's certificate and a timestamp,
if present.

Constructor Detail

- CodeSigner

```java
public CodeSigner​(
CertPath
signerCertPath,

Timestamp
timestamp)
```

Constructs a CodeSigner object.

**Parameters:** signerCertPath

- The signer's certificate path.
It must not be

null

.
**Parameters:** timestamp

- A signature timestamp.
If

null

then no timestamp was generated
for the signature.
**Throws:** NullPointerException

- if

signerCertPath

is

null

.

---

#### Constructor Detail

CodeSigner

```java
public CodeSigner​(
CertPath
signerCertPath,

Timestamp
timestamp)
```

Constructs a CodeSigner object.

**Parameters:** signerCertPath

- The signer's certificate path.
It must not be

null

.
**Parameters:** timestamp

- A signature timestamp.
If

null

then no timestamp was generated
for the signature.
**Throws:** NullPointerException

- if

signerCertPath

is

null

.

---

#### CodeSigner

public CodeSigner​(

CertPath

signerCertPath,

Timestamp

timestamp)

Constructs a CodeSigner object.

Method Detail

- getSignerCertPath

```java
public
CertPath
getSignerCertPath()
```

Returns the signer's certificate path.

**Returns:** A certificate path.

- getTimestamp

```java
public
Timestamp
getTimestamp()
```

Returns the signature timestamp.

**Returns:** The timestamp or

null

if none is present.

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this code signer.
The hash code is generated using the signer's certificate path and the
timestamp, if present.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this code signer.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
obj)
```

Tests for equality between the specified object and this
code signer. Two code signers are considered equal if their
signer certificate paths are equal and if their timestamps are equal,
if present in both.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to test for equality with this object.
**Returns:** true if the objects are considered equal, false otherwise.
**See Also:** Object.hashCode()

,

HashMap

- toString

```java
public
String
toString()
```

Returns a string describing this code signer.

**Overrides:** toString

in class

Object
**Returns:** A string comprising the signer's certificate and a timestamp,
if present.

---

#### Method Detail

getSignerCertPath

```java
public
CertPath
getSignerCertPath()
```

Returns the signer's certificate path.

**Returns:** A certificate path.

---

#### getSignerCertPath

public

CertPath

getSignerCertPath()

Returns the signer's certificate path.

getTimestamp

```java
public
Timestamp
getTimestamp()
```

Returns the signature timestamp.

**Returns:** The timestamp or

null

if none is present.

---

#### getTimestamp

public

Timestamp

getTimestamp()

Returns the signature timestamp.

hashCode

```java
public int hashCode()
```

Returns the hash code value for this code signer.
The hash code is generated using the signer's certificate path and the
timestamp, if present.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this code signer.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns the hash code value for this code signer.
The hash code is generated using the signer's certificate path and the
timestamp, if present.

equals

```java
public boolean equals​(
Object
obj)
```

Tests for equality between the specified object and this
code signer. Two code signers are considered equal if their
signer certificate paths are equal and if their timestamps are equal,
if present in both.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to test for equality with this object.
**Returns:** true if the objects are considered equal, false otherwise.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Tests for equality between the specified object and this
code signer. Two code signers are considered equal if their
signer certificate paths are equal and if their timestamps are equal,
if present in both.

toString

```java
public
String
toString()
```

Returns a string describing this code signer.

**Overrides:** toString

in class

Object
**Returns:** A string comprising the signer's certificate and a timestamp,
if present.

---

#### toString

public

String

toString()

Returns a string describing this code signer.

---

