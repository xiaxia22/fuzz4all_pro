# Class URICertStoreParameters

**Source:** `java.base\java\security\cert\URICertStoreParameters.html`

### Class Description

```java
public final class
URICertStoreParameters

extends
Object

implements
CertStoreParameters
```

Parameters used as input for

CertStore

algorithms which use
information contained in a URI to retrieve certificates and CRLs.

This class is used to provide necessary configuration parameters
through a URI as defined in RFC 5280 to implementations of

CertStore

algorithms.

Concurrent Access

Unless otherwise specified, the methods defined in this class are not
thread-safe. Multiple threads that need to access a single
object concurrently should synchronize amongst themselves and
provide the necessary locking. Multiple threads each manipulating
separate objects need not synchronize.

**All Implemented Interfaces:** Cloneable

,

CertStoreParameters

---

### Field Details

*No entries found.*

### Constructor Details

#### public URICertStoreParameters​(
URI
uri)

Creates an instance of

URICertStoreParameters

with the
specified URI.

**Parameters:**
- uri

- the URI which contains configuration information.

**Throws:**
- NullPointerException

- if

uri

is null

---

### Method Details

#### public
URI
getURI()

Returns the URI used to construct this

URICertStoreParameters

object.

**Returns:**
- the URI.

---

#### public
URICertStoreParameters
clone()

Returns a copy of this object. Changes to the copy will not affect
the original and vice versa.

**Specified by:**
- clone

in interface

CertStoreParameters

**Overrides:**
- clone

in class

Object

**Returns:**
- the copy

**See Also:**
- Cloneable

---

#### public int hashCode()

Returns a hash code value for this parameters object.
The hash code is generated using the URI supplied at construction.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code value for this parameters.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public boolean equals​(
Object
p)

Compares the specified object with this parameters object for equality.
Two URICertStoreParameters are considered equal if the URIs used
to construct them are equal.

**Overrides:**
- equals

in class

Object

**Parameters:**
- p

- the object to test for equality with this parameters.

**Returns:**
- true if the specified object is equal to this parameters object.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public
String
toString()

Returns a formatted string describing the parameters
including the URI used to construct this object.

**Overrides:**
- toString

in class

Object

**Returns:**
- a formatted string describing the parameters

---

### Additional Sections

#### Class URICertStoreParameters

java.lang.Object

- java.security.cert.URICertStoreParameters

java.security.cert.URICertStoreParameters

**All Implemented Interfaces:** Cloneable

,

CertStoreParameters

```java
public final class
URICertStoreParameters

extends
Object

implements
CertStoreParameters
```

Parameters used as input for

CertStore

algorithms which use
information contained in a URI to retrieve certificates and CRLs.

This class is used to provide necessary configuration parameters
through a URI as defined in RFC 5280 to implementations of

CertStore

algorithms.

Concurrent Access

Unless otherwise specified, the methods defined in this class are not
thread-safe. Multiple threads that need to access a single
object concurrently should synchronize amongst themselves and
provide the necessary locking. Multiple threads each manipulating
separate objects need not synchronize.

**Since:** 9
**See Also:** CertStore

,

URI

public final class

URICertStoreParameters

extends

Object

implements

CertStoreParameters

Parameters used as input for

CertStore

algorithms which use
information contained in a URI to retrieve certificates and CRLs.

This class is used to provide necessary configuration parameters
through a URI as defined in RFC 5280 to implementations of

CertStore

algorithms.

Concurrent Access

Unless otherwise specified, the methods defined in this class are not
thread-safe. Multiple threads that need to access a single
object concurrently should synchronize amongst themselves and
provide the necessary locking. Multiple threads each manipulating
separate objects need not synchronize.

This class is used to provide necessary configuration parameters
through a URI as defined in RFC 5280 to implementations of

CertStore

algorithms.

Concurrent Access

Unless otherwise specified, the methods defined in this class are not
thread-safe. Multiple threads that need to access a single
object concurrently should synchronize amongst themselves and
provide the necessary locking. Multiple threads each manipulating
separate objects need not synchronize.

Concurrent Access

Unless otherwise specified, the methods defined in this class are not
thread-safe. Multiple threads that need to access a single
object concurrently should synchronize amongst themselves and
provide the necessary locking. Multiple threads each manipulating
separate objects need not synchronize.

Unless otherwise specified, the methods defined in this class are not
thread-safe. Multiple threads that need to access a single
object concurrently should synchronize amongst themselves and
provide the necessary locking. Multiple threads each manipulating
separate objects need not synchronize.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

URICertStoreParameters

​(

URI

uri)

Creates an instance of

URICertStoreParameters

with the
specified URI.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

URICertStoreParameters

clone

()

Returns a copy of this object.

boolean

equals

​(

Object

p)

Compares the specified object with this parameters object for equality.

URI

getURI

()

Returns the URI used to construct this

URICertStoreParameters

object.

int

hashCode

()

Returns a hash code value for this parameters object.

String

toString

()

Returns a formatted string describing the parameters
including the URI used to construct this object.

- Methods declared in class java.lang.

Object

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

URICertStoreParameters

​(

URI

uri)

Creates an instance of

URICertStoreParameters

with the
specified URI.

---

#### Constructor Summary

Creates an instance of

URICertStoreParameters

with the
specified URI.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

URICertStoreParameters

clone

()

Returns a copy of this object.

boolean

equals

​(

Object

p)

Compares the specified object with this parameters object for equality.

URI

getURI

()

Returns the URI used to construct this

URICertStoreParameters

object.

int

hashCode

()

Returns a hash code value for this parameters object.

String

toString

()

Returns a formatted string describing the parameters
including the URI used to construct this object.

- Methods declared in class java.lang.

Object

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

Returns a copy of this object.

Compares the specified object with this parameters object for equality.

Returns the URI used to construct this

URICertStoreParameters

object.

Returns a hash code value for this parameters object.

Returns a formatted string describing the parameters
including the URI used to construct this object.

Methods declared in class java.lang.

Object

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

- URICertStoreParameters

```java
public URICertStoreParameters​(
URI
uri)
```

Creates an instance of

URICertStoreParameters

with the
specified URI.

**Parameters:** uri

- the URI which contains configuration information.
**Throws:** NullPointerException

- if

uri

is null

============ METHOD DETAIL ==========

- Method Detail

- getURI

```java
public
URI
getURI()
```

Returns the URI used to construct this

URICertStoreParameters

object.

**Returns:** the URI.

- clone

```java
public
URICertStoreParameters
clone()
```

Returns a copy of this object. Changes to the copy will not affect
the original and vice versa.

**Specified by:** clone

in interface

CertStoreParameters
**Overrides:** clone

in class

Object
**Returns:** the copy
**See Also:** Cloneable

- hashCode

```java
public int hashCode()
```

Returns a hash code value for this parameters object.
The hash code is generated using the URI supplied at construction.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this parameters.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
p)
```

Compares the specified object with this parameters object for equality.
Two URICertStoreParameters are considered equal if the URIs used
to construct them are equal.

**Overrides:** equals

in class

Object
**Parameters:** p

- the object to test for equality with this parameters.
**Returns:** true if the specified object is equal to this parameters object.
**See Also:** Object.hashCode()

,

HashMap

- toString

```java
public
String
toString()
```

Returns a formatted string describing the parameters
including the URI used to construct this object.

**Overrides:** toString

in class

Object
**Returns:** a formatted string describing the parameters

Constructor Detail

- URICertStoreParameters

```java
public URICertStoreParameters​(
URI
uri)
```

Creates an instance of

URICertStoreParameters

with the
specified URI.

**Parameters:** uri

- the URI which contains configuration information.
**Throws:** NullPointerException

- if

uri

is null

---

#### Constructor Detail

URICertStoreParameters

```java
public URICertStoreParameters​(
URI
uri)
```

Creates an instance of

URICertStoreParameters

with the
specified URI.

**Parameters:** uri

- the URI which contains configuration information.
**Throws:** NullPointerException

- if

uri

is null

---

#### URICertStoreParameters

public URICertStoreParameters​(

URI

uri)

Creates an instance of

URICertStoreParameters

with the
specified URI.

Method Detail

- getURI

```java
public
URI
getURI()
```

Returns the URI used to construct this

URICertStoreParameters

object.

**Returns:** the URI.

- clone

```java
public
URICertStoreParameters
clone()
```

Returns a copy of this object. Changes to the copy will not affect
the original and vice versa.

**Specified by:** clone

in interface

CertStoreParameters
**Overrides:** clone

in class

Object
**Returns:** the copy
**See Also:** Cloneable

- hashCode

```java
public int hashCode()
```

Returns a hash code value for this parameters object.
The hash code is generated using the URI supplied at construction.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this parameters.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
p)
```

Compares the specified object with this parameters object for equality.
Two URICertStoreParameters are considered equal if the URIs used
to construct them are equal.

**Overrides:** equals

in class

Object
**Parameters:** p

- the object to test for equality with this parameters.
**Returns:** true if the specified object is equal to this parameters object.
**See Also:** Object.hashCode()

,

HashMap

- toString

```java
public
String
toString()
```

Returns a formatted string describing the parameters
including the URI used to construct this object.

**Overrides:** toString

in class

Object
**Returns:** a formatted string describing the parameters

---

#### Method Detail

getURI

```java
public
URI
getURI()
```

Returns the URI used to construct this

URICertStoreParameters

object.

**Returns:** the URI.

---

#### getURI

public

URI

getURI()

Returns the URI used to construct this

URICertStoreParameters

object.

clone

```java
public
URICertStoreParameters
clone()
```

Returns a copy of this object. Changes to the copy will not affect
the original and vice versa.

**Specified by:** clone

in interface

CertStoreParameters
**Overrides:** clone

in class

Object
**Returns:** the copy
**See Also:** Cloneable

---

#### clone

public

URICertStoreParameters

clone()

Returns a copy of this object. Changes to the copy will not affect
the original and vice versa.

hashCode

```java
public int hashCode()
```

Returns a hash code value for this parameters object.
The hash code is generated using the URI supplied at construction.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this parameters.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns a hash code value for this parameters object.
The hash code is generated using the URI supplied at construction.

equals

```java
public boolean equals​(
Object
p)
```

Compares the specified object with this parameters object for equality.
Two URICertStoreParameters are considered equal if the URIs used
to construct them are equal.

**Overrides:** equals

in class

Object
**Parameters:** p

- the object to test for equality with this parameters.
**Returns:** true if the specified object is equal to this parameters object.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

p)

Compares the specified object with this parameters object for equality.
Two URICertStoreParameters are considered equal if the URIs used
to construct them are equal.

toString

```java
public
String
toString()
```

Returns a formatted string describing the parameters
including the URI used to construct this object.

**Overrides:** toString

in class

Object
**Returns:** a formatted string describing the parameters

---

#### toString

public

String

toString()

Returns a formatted string describing the parameters
including the URI used to construct this object.

---

