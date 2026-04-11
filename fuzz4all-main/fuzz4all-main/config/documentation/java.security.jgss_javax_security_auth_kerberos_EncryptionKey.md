# Class EncryptionKey

**Source:** `java.security.jgss\javax\security\auth\kerberos\EncryptionKey.html`

### Class Description

```java
public final class
EncryptionKey

extends
Object

implements
SecretKey
```

This class encapsulates an EncryptionKey used in Kerberos.

An EncryptionKey is defined in Section 4.2.9 of the Kerberos Protocol
Specification (

RFC 4120

) as:

```java
EncryptionKey ::= SEQUENCE {
keytype [0] Int32 -- actually encryption type --,
keyvalue [1] OCTET STRING
}
```

The key material of an

EncryptionKey

is defined as the value
of the

keyValue

above.

**All Implemented Interfaces:** Serializable

,

Key

,

SecretKey

,

Destroyable

---

### Field Details

*No entries found.*

### Constructor Details

#### public EncryptionKey​(byte[] keyBytes,
int keyType)

Constructs an

EncryptionKey

from the given bytes and
the key type.

The contents of the byte array are copied; subsequent modification of
the byte array does not affect the newly created key.

**Parameters:**
- keyBytes

- the key material for the key
- keyType

- the key type for the key as defined by the
Kerberos protocol specification.

**Throws:**
- NullPointerException

- if keyBytes is null

---

### Method Details

#### public int getKeyType()

Returns the key type for this key.

**Returns:**
- the key type.

**Throws:**
- IllegalStateException

- if the key is destroyed

---

#### public
String
getAlgorithm()

Returns the standard algorithm name for this key. The algorithm names
are the encryption type string defined on the IANA

Kerberos Encryption Type Numbers

page.

This method can return the following value not defined on the IANA page:

- none: for etype equal to 0
- unknown: for etype greater than 0 but unsupported by
the implementation
- private: for etype smaller than 0

**Specified by:**
- getAlgorithm

in interface

Key

**Returns:**
- the name of the algorithm associated with this key.

**Throws:**
- IllegalStateException

- if the key is destroyed

---

#### public
String
getFormat()

Returns the name of the encoding format for this key.

**Specified by:**
- getFormat

in interface

Key

**Returns:**
- the String "RAW"

**Throws:**
- IllegalStateException

- if the key is destroyed

---

#### public byte[] getEncoded()

Returns the key material of this key.

**Specified by:**
- getEncoded

in interface

Key

**Returns:**
- a newly allocated byte array that contains the key material

**Throws:**
- IllegalStateException

- if the key is destroyed

---

#### public void destroy()
throws
DestroyFailedException

Destroys this key by clearing out the key material of this key.

**Specified by:**
- destroy

in interface

Destroyable

**Throws:**
- DestroyFailedException

- if some error occurs while destorying
this key.

---

#### public
String
toString()

Returns an informative textual representation of this

EncryptionKey

.

**Overrides:**
- toString

in class

Object

**Returns:**
- an informative textual representation of this

EncryptionKey

.

---

#### public int hashCode()

Returns a hash code for this

EncryptionKey

.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code for this

EncryptionKey

.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public boolean equals​(
Object
other)

Compares the specified object with this key for equality.
Returns true if the given object is also an

EncryptionKey

and the two

EncryptionKey

instances are equivalent. More formally two

EncryptionKey

instances are equal if they have equal key types
and key material.
A destroyed

EncryptionKey

object is only equal to itself.

**Overrides:**
- equals

in class

Object

**Parameters:**
- other

- the object to compare to

**Returns:**
- true if the specified object is equal to this

EncryptionKey

, false otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

---

### Additional Sections

#### Class EncryptionKey

java.lang.Object

- javax.security.auth.kerberos.EncryptionKey

javax.security.auth.kerberos.EncryptionKey

**All Implemented Interfaces:** Serializable

,

Key

,

SecretKey

,

Destroyable

```java
public final class
EncryptionKey

extends
Object

implements
SecretKey
```

This class encapsulates an EncryptionKey used in Kerberos.

An EncryptionKey is defined in Section 4.2.9 of the Kerberos Protocol
Specification (

RFC 4120

) as:

```java
EncryptionKey ::= SEQUENCE {
keytype [0] Int32 -- actually encryption type --,
keyvalue [1] OCTET STRING
}
```

The key material of an

EncryptionKey

is defined as the value
of the

keyValue

above.

**Since:** 9
**See Also:** Serialized Form

public final class

EncryptionKey

extends

Object

implements

SecretKey

This class encapsulates an EncryptionKey used in Kerberos.

An EncryptionKey is defined in Section 4.2.9 of the Kerberos Protocol
Specification (

RFC 4120

) as:

```java
EncryptionKey ::= SEQUENCE {
keytype [0] Int32 -- actually encryption type --,
keyvalue [1] OCTET STRING
}
```

The key material of an

EncryptionKey

is defined as the value
of the

keyValue

above.

An EncryptionKey is defined in Section 4.2.9 of the Kerberos Protocol
Specification (

RFC 4120

) as:

```java
EncryptionKey ::= SEQUENCE {
keytype [0] Int32 -- actually encryption type --,
keyvalue [1] OCTET STRING
}
```

The key material of an

EncryptionKey

is defined as the value
of the

keyValue

above.

EncryptionKey ::= SEQUENCE {
keytype [0] Int32 -- actually encryption type --,
keyvalue [1] OCTET STRING
}

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

EncryptionKey

​(byte[] keyBytes,
int keyType)

Constructs an

EncryptionKey

from the given bytes and
the key type.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

destroy

()

Destroys this key by clearing out the key material of this key.

boolean

equals

​(

Object

other)

Compares the specified object with this key for equality.

String

getAlgorithm

()

Returns the standard algorithm name for this key.

byte[]

getEncoded

()

Returns the key material of this key.

String

getFormat

()

Returns the name of the encoding format for this key.

int

getKeyType

()

Returns the key type for this key.

int

hashCode

()

Returns a hash code for this

EncryptionKey

.

String

toString

()

Returns an informative textual representation of this

EncryptionKey

.

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

- Methods declared in interface javax.security.auth.

Destroyable

isDestroyed

Constructor Summary

Constructors

Constructor

Description

EncryptionKey

​(byte[] keyBytes,
int keyType)

Constructs an

EncryptionKey

from the given bytes and
the key type.

---

#### Constructor Summary

Constructs an

EncryptionKey

from the given bytes and
the key type.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

destroy

()

Destroys this key by clearing out the key material of this key.

boolean

equals

​(

Object

other)

Compares the specified object with this key for equality.

String

getAlgorithm

()

Returns the standard algorithm name for this key.

byte[]

getEncoded

()

Returns the key material of this key.

String

getFormat

()

Returns the name of the encoding format for this key.

int

getKeyType

()

Returns the key type for this key.

int

hashCode

()

Returns a hash code for this

EncryptionKey

.

String

toString

()

Returns an informative textual representation of this

EncryptionKey

.

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

- Methods declared in interface javax.security.auth.

Destroyable

isDestroyed

---

#### Method Summary

Destroys this key by clearing out the key material of this key.

Compares the specified object with this key for equality.

Returns the standard algorithm name for this key.

Returns the key material of this key.

Returns the name of the encoding format for this key.

Returns the key type for this key.

Returns a hash code for this

EncryptionKey

.

Returns an informative textual representation of this

EncryptionKey

.

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

Methods declared in interface javax.security.auth.

Destroyable

isDestroyed

---

#### Methods declared in interface javax.security.auth. Destroyable

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- EncryptionKey

```java
public EncryptionKey​(byte[] keyBytes,
int keyType)
```

Constructs an

EncryptionKey

from the given bytes and
the key type.

The contents of the byte array are copied; subsequent modification of
the byte array does not affect the newly created key.

**Parameters:** keyBytes

- the key material for the key
**Parameters:** keyType

- the key type for the key as defined by the
Kerberos protocol specification.
**Throws:** NullPointerException

- if keyBytes is null

============ METHOD DETAIL ==========

- Method Detail

- getKeyType

```java
public int getKeyType()
```

Returns the key type for this key.

**Returns:** the key type.
**Throws:** IllegalStateException

- if the key is destroyed

- getAlgorithm

```java
public
String
getAlgorithm()
```

Returns the standard algorithm name for this key. The algorithm names
are the encryption type string defined on the IANA

Kerberos Encryption Type Numbers

page.

This method can return the following value not defined on the IANA page:

- none: for etype equal to 0
- unknown: for etype greater than 0 but unsupported by
the implementation
- private: for etype smaller than 0

**Specified by:** getAlgorithm

in interface

Key
**Returns:** the name of the algorithm associated with this key.
**Throws:** IllegalStateException

- if the key is destroyed

- getFormat

```java
public
String
getFormat()
```

Returns the name of the encoding format for this key.

**Specified by:** getFormat

in interface

Key
**Returns:** the String "RAW"
**Throws:** IllegalStateException

- if the key is destroyed

- getEncoded

```java
public byte[] getEncoded()
```

Returns the key material of this key.

**Specified by:** getEncoded

in interface

Key
**Returns:** a newly allocated byte array that contains the key material
**Throws:** IllegalStateException

- if the key is destroyed

- destroy

```java
public void destroy()
throws
DestroyFailedException
```

Destroys this key by clearing out the key material of this key.

**Specified by:** destroy

in interface

Destroyable
**Throws:** DestroyFailedException

- if some error occurs while destorying
this key.

- toString

```java
public
String
toString()
```

Returns an informative textual representation of this

EncryptionKey

.

**Overrides:** toString

in class

Object
**Returns:** an informative textual representation of this

EncryptionKey

.

- hashCode

```java
public int hashCode()
```

Returns a hash code for this

EncryptionKey

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this

EncryptionKey

.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
other)
```

Compares the specified object with this key for equality.
Returns true if the given object is also an

EncryptionKey

and the two

EncryptionKey

instances are equivalent. More formally two

EncryptionKey

instances are equal if they have equal key types
and key material.
A destroyed

EncryptionKey

object is only equal to itself.

**Overrides:** equals

in class

Object
**Parameters:** other

- the object to compare to
**Returns:** true if the specified object is equal to this

EncryptionKey

, false otherwise.
**See Also:** Object.hashCode()

,

HashMap

Constructor Detail

- EncryptionKey

```java
public EncryptionKey​(byte[] keyBytes,
int keyType)
```

Constructs an

EncryptionKey

from the given bytes and
the key type.

The contents of the byte array are copied; subsequent modification of
the byte array does not affect the newly created key.

**Parameters:** keyBytes

- the key material for the key
**Parameters:** keyType

- the key type for the key as defined by the
Kerberos protocol specification.
**Throws:** NullPointerException

- if keyBytes is null

---

#### Constructor Detail

EncryptionKey

```java
public EncryptionKey​(byte[] keyBytes,
int keyType)
```

Constructs an

EncryptionKey

from the given bytes and
the key type.

The contents of the byte array are copied; subsequent modification of
the byte array does not affect the newly created key.

**Parameters:** keyBytes

- the key material for the key
**Parameters:** keyType

- the key type for the key as defined by the
Kerberos protocol specification.
**Throws:** NullPointerException

- if keyBytes is null

---

#### EncryptionKey

public EncryptionKey​(byte[] keyBytes,
int keyType)

Constructs an

EncryptionKey

from the given bytes and
the key type.

The contents of the byte array are copied; subsequent modification of
the byte array does not affect the newly created key.

The contents of the byte array are copied; subsequent modification of
the byte array does not affect the newly created key.

Method Detail

- getKeyType

```java
public int getKeyType()
```

Returns the key type for this key.

**Returns:** the key type.
**Throws:** IllegalStateException

- if the key is destroyed

- getAlgorithm

```java
public
String
getAlgorithm()
```

Returns the standard algorithm name for this key. The algorithm names
are the encryption type string defined on the IANA

Kerberos Encryption Type Numbers

page.

This method can return the following value not defined on the IANA page:

- none: for etype equal to 0
- unknown: for etype greater than 0 but unsupported by
the implementation
- private: for etype smaller than 0

**Specified by:** getAlgorithm

in interface

Key
**Returns:** the name of the algorithm associated with this key.
**Throws:** IllegalStateException

- if the key is destroyed

- getFormat

```java
public
String
getFormat()
```

Returns the name of the encoding format for this key.

**Specified by:** getFormat

in interface

Key
**Returns:** the String "RAW"
**Throws:** IllegalStateException

- if the key is destroyed

- getEncoded

```java
public byte[] getEncoded()
```

Returns the key material of this key.

**Specified by:** getEncoded

in interface

Key
**Returns:** a newly allocated byte array that contains the key material
**Throws:** IllegalStateException

- if the key is destroyed

- destroy

```java
public void destroy()
throws
DestroyFailedException
```

Destroys this key by clearing out the key material of this key.

**Specified by:** destroy

in interface

Destroyable
**Throws:** DestroyFailedException

- if some error occurs while destorying
this key.

- toString

```java
public
String
toString()
```

Returns an informative textual representation of this

EncryptionKey

.

**Overrides:** toString

in class

Object
**Returns:** an informative textual representation of this

EncryptionKey

.

- hashCode

```java
public int hashCode()
```

Returns a hash code for this

EncryptionKey

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this

EncryptionKey

.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
other)
```

Compares the specified object with this key for equality.
Returns true if the given object is also an

EncryptionKey

and the two

EncryptionKey

instances are equivalent. More formally two

EncryptionKey

instances are equal if they have equal key types
and key material.
A destroyed

EncryptionKey

object is only equal to itself.

**Overrides:** equals

in class

Object
**Parameters:** other

- the object to compare to
**Returns:** true if the specified object is equal to this

EncryptionKey

, false otherwise.
**See Also:** Object.hashCode()

,

HashMap

---

#### Method Detail

getKeyType

```java
public int getKeyType()
```

Returns the key type for this key.

**Returns:** the key type.
**Throws:** IllegalStateException

- if the key is destroyed

---

#### getKeyType

public int getKeyType()

Returns the key type for this key.

getAlgorithm

```java
public
String
getAlgorithm()
```

Returns the standard algorithm name for this key. The algorithm names
are the encryption type string defined on the IANA

Kerberos Encryption Type Numbers

page.

This method can return the following value not defined on the IANA page:

- none: for etype equal to 0
- unknown: for etype greater than 0 but unsupported by
the implementation
- private: for etype smaller than 0

**Specified by:** getAlgorithm

in interface

Key
**Returns:** the name of the algorithm associated with this key.
**Throws:** IllegalStateException

- if the key is destroyed

---

#### getAlgorithm

public

String

getAlgorithm()

Returns the standard algorithm name for this key. The algorithm names
are the encryption type string defined on the IANA

Kerberos Encryption Type Numbers

page.

This method can return the following value not defined on the IANA page:

- none: for etype equal to 0
- unknown: for etype greater than 0 but unsupported by
the implementation
- private: for etype smaller than 0

This method can return the following value not defined on the IANA page:

- none: for etype equal to 0
- unknown: for etype greater than 0 but unsupported by
the implementation
- private: for etype smaller than 0

none: for etype equal to 0

unknown: for etype greater than 0 but unsupported by
the implementation

private: for etype smaller than 0

getFormat

```java
public
String
getFormat()
```

Returns the name of the encoding format for this key.

**Specified by:** getFormat

in interface

Key
**Returns:** the String "RAW"
**Throws:** IllegalStateException

- if the key is destroyed

---

#### getFormat

public

String

getFormat()

Returns the name of the encoding format for this key.

getEncoded

```java
public byte[] getEncoded()
```

Returns the key material of this key.

**Specified by:** getEncoded

in interface

Key
**Returns:** a newly allocated byte array that contains the key material
**Throws:** IllegalStateException

- if the key is destroyed

---

#### getEncoded

public byte[] getEncoded()

Returns the key material of this key.

destroy

```java
public void destroy()
throws
DestroyFailedException
```

Destroys this key by clearing out the key material of this key.

**Specified by:** destroy

in interface

Destroyable
**Throws:** DestroyFailedException

- if some error occurs while destorying
this key.

---

#### destroy

public void destroy()
throws

DestroyFailedException

Destroys this key by clearing out the key material of this key.

toString

```java
public
String
toString()
```

Returns an informative textual representation of this

EncryptionKey

.

**Overrides:** toString

in class

Object
**Returns:** an informative textual representation of this

EncryptionKey

.

---

#### toString

public

String

toString()

Returns an informative textual representation of this

EncryptionKey

.

hashCode

```java
public int hashCode()
```

Returns a hash code for this

EncryptionKey

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this

EncryptionKey

.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns a hash code for this

EncryptionKey

.

equals

```java
public boolean equals​(
Object
other)
```

Compares the specified object with this key for equality.
Returns true if the given object is also an

EncryptionKey

and the two

EncryptionKey

instances are equivalent. More formally two

EncryptionKey

instances are equal if they have equal key types
and key material.
A destroyed

EncryptionKey

object is only equal to itself.

**Overrides:** equals

in class

Object
**Parameters:** other

- the object to compare to
**Returns:** true if the specified object is equal to this

EncryptionKey

, false otherwise.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

other)

Compares the specified object with this key for equality.
Returns true if the given object is also an

EncryptionKey

and the two

EncryptionKey

instances are equivalent. More formally two

EncryptionKey

instances are equal if they have equal key types
and key material.
A destroyed

EncryptionKey

object is only equal to itself.

---

