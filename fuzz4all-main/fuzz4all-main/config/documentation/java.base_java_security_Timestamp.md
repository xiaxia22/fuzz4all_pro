# Class Timestamp

**Source:** `java.base\java\security\Timestamp.html`

### Class Description

```java
public final class
Timestamp

extends
Object

implements
Serializable
```

This class encapsulates information about a signed timestamp.
It is immutable.
It includes the timestamp's date and time as well as information about the
Timestamping Authority (TSA) which generated and signed the timestamp.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public Timestamp​(
Date
timestamp,

CertPath
signerCertPath)

Constructs a Timestamp.

**Parameters:**
- timestamp

- is the timestamp's date and time. It must not be null.
- signerCertPath

- is the TSA's certificate path. It must not be null.

**Throws:**
- NullPointerException

- if timestamp or signerCertPath is null.

---

### Method Details

#### public
Date
getTimestamp()

Returns the date and time when the timestamp was generated.

**Returns:**
- The timestamp's date and time.

---

#### public
CertPath
getSignerCertPath()

Returns the certificate path for the Timestamping Authority.

**Returns:**
- The TSA's certificate path.

---

#### public int hashCode()

Returns the hash code value for this timestamp.
The hash code is generated using the date and time of the timestamp
and the TSA's certificate path.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code value for this timestamp.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public boolean equals​(
Object
obj)

Tests for equality between the specified object and this
timestamp. Two timestamps are considered equal if the date and time of
their timestamp's and their signer's certificate paths are equal.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the object to test for equality with this timestamp.

**Returns:**
- true if the timestamp are considered equal, false otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public
String
toString()

Returns a string describing this timestamp.

**Overrides:**
- toString

in class

Object

**Returns:**
- A string comprising the date and time of the timestamp and
its signer's certificate.

---

### Additional Sections

#### Class Timestamp

java.lang.Object

- java.security.Timestamp

java.security.Timestamp

**All Implemented Interfaces:** Serializable

```java
public final class
Timestamp

extends
Object

implements
Serializable
```

This class encapsulates information about a signed timestamp.
It is immutable.
It includes the timestamp's date and time as well as information about the
Timestamping Authority (TSA) which generated and signed the timestamp.

**Since:** 1.5
**See Also:** Serialized Form

public final class

Timestamp

extends

Object

implements

Serializable

This class encapsulates information about a signed timestamp.
It is immutable.
It includes the timestamp's date and time as well as information about the
Timestamping Authority (TSA) which generated and signed the timestamp.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Timestamp

​(

Date

timestamp,

CertPath

signerCertPath)

Constructs a Timestamp.

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
timestamp.

CertPath

getSignerCertPath

()

Returns the certificate path for the Timestamping Authority.

Date

getTimestamp

()

Returns the date and time when the timestamp was generated.

int

hashCode

()

Returns the hash code value for this timestamp.

String

toString

()

Returns a string describing this timestamp.

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

Timestamp

​(

Date

timestamp,

CertPath

signerCertPath)

Constructs a Timestamp.

---

#### Constructor Summary

Constructs a Timestamp.

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
timestamp.

CertPath

getSignerCertPath

()

Returns the certificate path for the Timestamping Authority.

Date

getTimestamp

()

Returns the date and time when the timestamp was generated.

int

hashCode

()

Returns the hash code value for this timestamp.

String

toString

()

Returns a string describing this timestamp.

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
timestamp.

Returns the certificate path for the Timestamping Authority.

Returns the date and time when the timestamp was generated.

Returns the hash code value for this timestamp.

Returns a string describing this timestamp.

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

- Timestamp

```java
public Timestamp​(
Date
timestamp,

CertPath
signerCertPath)
```

Constructs a Timestamp.

**Parameters:** timestamp

- is the timestamp's date and time. It must not be null.
**Parameters:** signerCertPath

- is the TSA's certificate path. It must not be null.
**Throws:** NullPointerException

- if timestamp or signerCertPath is null.

============ METHOD DETAIL ==========

- Method Detail

- getTimestamp

```java
public
Date
getTimestamp()
```

Returns the date and time when the timestamp was generated.

**Returns:** The timestamp's date and time.

- getSignerCertPath

```java
public
CertPath
getSignerCertPath()
```

Returns the certificate path for the Timestamping Authority.

**Returns:** The TSA's certificate path.

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this timestamp.
The hash code is generated using the date and time of the timestamp
and the TSA's certificate path.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this timestamp.
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
timestamp. Two timestamps are considered equal if the date and time of
their timestamp's and their signer's certificate paths are equal.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to test for equality with this timestamp.
**Returns:** true if the timestamp are considered equal, false otherwise.
**See Also:** Object.hashCode()

,

HashMap

- toString

```java
public
String
toString()
```

Returns a string describing this timestamp.

**Overrides:** toString

in class

Object
**Returns:** A string comprising the date and time of the timestamp and
its signer's certificate.

Constructor Detail

- Timestamp

```java
public Timestamp​(
Date
timestamp,

CertPath
signerCertPath)
```

Constructs a Timestamp.

**Parameters:** timestamp

- is the timestamp's date and time. It must not be null.
**Parameters:** signerCertPath

- is the TSA's certificate path. It must not be null.
**Throws:** NullPointerException

- if timestamp or signerCertPath is null.

---

#### Constructor Detail

Timestamp

```java
public Timestamp​(
Date
timestamp,

CertPath
signerCertPath)
```

Constructs a Timestamp.

**Parameters:** timestamp

- is the timestamp's date and time. It must not be null.
**Parameters:** signerCertPath

- is the TSA's certificate path. It must not be null.
**Throws:** NullPointerException

- if timestamp or signerCertPath is null.

---

#### Timestamp

public Timestamp​(

Date

timestamp,

CertPath

signerCertPath)

Constructs a Timestamp.

Method Detail

- getTimestamp

```java
public
Date
getTimestamp()
```

Returns the date and time when the timestamp was generated.

**Returns:** The timestamp's date and time.

- getSignerCertPath

```java
public
CertPath
getSignerCertPath()
```

Returns the certificate path for the Timestamping Authority.

**Returns:** The TSA's certificate path.

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this timestamp.
The hash code is generated using the date and time of the timestamp
and the TSA's certificate path.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this timestamp.
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
timestamp. Two timestamps are considered equal if the date and time of
their timestamp's and their signer's certificate paths are equal.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to test for equality with this timestamp.
**Returns:** true if the timestamp are considered equal, false otherwise.
**See Also:** Object.hashCode()

,

HashMap

- toString

```java
public
String
toString()
```

Returns a string describing this timestamp.

**Overrides:** toString

in class

Object
**Returns:** A string comprising the date and time of the timestamp and
its signer's certificate.

---

#### Method Detail

getTimestamp

```java
public
Date
getTimestamp()
```

Returns the date and time when the timestamp was generated.

**Returns:** The timestamp's date and time.

---

#### getTimestamp

public

Date

getTimestamp()

Returns the date and time when the timestamp was generated.

getSignerCertPath

```java
public
CertPath
getSignerCertPath()
```

Returns the certificate path for the Timestamping Authority.

**Returns:** The TSA's certificate path.

---

#### getSignerCertPath

public

CertPath

getSignerCertPath()

Returns the certificate path for the Timestamping Authority.

hashCode

```java
public int hashCode()
```

Returns the hash code value for this timestamp.
The hash code is generated using the date and time of the timestamp
and the TSA's certificate path.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this timestamp.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns the hash code value for this timestamp.
The hash code is generated using the date and time of the timestamp
and the TSA's certificate path.

equals

```java
public boolean equals​(
Object
obj)
```

Tests for equality between the specified object and this
timestamp. Two timestamps are considered equal if the date and time of
their timestamp's and their signer's certificate paths are equal.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to test for equality with this timestamp.
**Returns:** true if the timestamp are considered equal, false otherwise.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Tests for equality between the specified object and this
timestamp. Two timestamps are considered equal if the date and time of
their timestamp's and their signer's certificate paths are equal.

toString

```java
public
String
toString()
```

Returns a string describing this timestamp.

**Overrides:** toString

in class

Object
**Returns:** A string comprising the date and time of the timestamp and
its signer's certificate.

---

#### toString

public

String

toString()

Returns a string describing this timestamp.

---

