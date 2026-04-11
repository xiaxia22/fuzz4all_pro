# Class KerberosKey

**Source:** `java.security.jgss\javax\security\auth\kerberos\KerberosKey.html`

### Class Description

```java
public class
KerberosKey

extends
Object

implements
SecretKey
```

This class encapsulates a long term secret key for a Kerberos
principal.

A

KerberosKey

object includes an EncryptionKey, a

KerberosPrincipal

as its owner, and the version number
of the key.

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

The key material of a

KerberosKey

is defined as the value
of the

keyValue

above.

All Kerberos JAAS login modules that obtain a principal's password and
generate the secret key from it should use this class.
Sometimes, such as when authenticating a server in
the absence of user-to-user authentication, the login module will store
an instance of this class in the private credential set of a

Subject

during the commit phase of the
authentication process.

A Kerberos service using a keytab to read secret keys should use
the

KeyTab

class, where latest keys can be read when needed.

It might be necessary for the application to be granted a

PrivateCredentialPermission

if it needs to access the

KerberosKey

instance from a Subject. This permission is not needed when the
application depends on the default JGSS Kerberos mechanism to access the

KerberosKey

. In that case, however, the application will need an
appropriate

ServicePermission

.

When creating a

KerberosKey

using the

KerberosKey(KerberosPrincipal, char[], String)

constructor,
an implementation may accept non-IANA algorithm names (For example,
"ArcFourMac" for "rc4-hmac"), but the

getAlgorithm()

method
must always return the IANA algorithm name.

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

#### public KerberosKey​(
KerberosPrincipal
principal,
byte[] keyBytes,
int keyType,
int versionNum)

Constructs a

KerberosKey

from the given bytes when the key type
and key version number are known. This can be used when reading the
secret key information from a Kerberos "keytab".

**Parameters:**
- principal

- the principal that this secret key belongs to
- keyBytes

- the key material for the secret key
- keyType

- the key type for the secret key as defined by the
Kerberos protocol specification.
- versionNum

- the version number of this secret key

---

#### public KerberosKey​(
KerberosPrincipal
principal,
char[] password,

String
algorithm)

Constructs a

KerberosKey

from a principal's password using the
specified algorithm name. The algorithm name (case insensitive) should
be provided as the encryption type string defined on the IANA

Kerberos Encryption Type Numbers

page. The version number of the key generated will be 0.

**Parameters:**
- principal

- the principal that this password belongs to
- password

- the password that should be used to compute the key
- algorithm

- the name for the algorithm that this key will be
used for

**Throws:**
- IllegalArgumentException

- if the name of the
algorithm passed is unsupported.

---

### Method Details

#### public final
KerberosPrincipal
getPrincipal()

Returns the principal that this key belongs to.

**Returns:**
- the principal this key belongs to.

**Throws:**
- IllegalStateException

- if the key is destroyed

---

#### public final int getVersionNumber()

Returns the key version number.

**Returns:**
- the key version number.

**Throws:**
- IllegalStateException

- if the key is destroyed

---

#### public final int getKeyType()

Returns the key type for this long-term key.

**Returns:**
- the key type.

**Throws:**
- IllegalStateException

- if the key is destroyed

---

#### public final
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

#### public final
String
getFormat()

Returns the name of the encoding format for this secret key.

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

#### public final byte[] getEncoded()

Returns the key material of this secret key.

**Specified by:**
- getEncoded

in interface

Key

**Returns:**
- the key material

**Throws:**
- IllegalStateException

- if the key is destroyed

---

#### public void destroy()
throws
DestroyFailedException

Destroys this key by clearing out the key material of this secret key.

**Specified by:**
- destroy

in interface

Destroyable

**Throws:**
- DestroyFailedException

- if some error occurs while destorying
this key.

---

#### public boolean isDestroyed()

Determines if this key has been destroyed.

**Specified by:**
- isDestroyed

in interface

Destroyable

**Returns:**
- true if this

Object

has been destroyed,
false otherwise.

---

#### public
String
toString()

Returns an informative textual representation of this

KerberosKey

.

**Overrides:**
- toString

in class

Object

**Returns:**
- an informative textual representation of this

KerberosKey

.

---

#### public int hashCode()

Returns a hash code for this

KerberosKey

.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code for this

KerberosKey

.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

**Since:**
- 1.6

---

#### public boolean equals​(
Object
other)

Compares the specified object with this

KerberosKey

for
equality. Returns true if the given object is also a

KerberosKey

and the two

KerberosKey

instances are equivalent.
A destroyed

KerberosKey

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

KerberosKey

,
false otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

**Since:**
- 1.6

---

### Additional Sections

#### Class KerberosKey

java.lang.Object

- javax.security.auth.kerberos.KerberosKey

javax.security.auth.kerberos.KerberosKey

**All Implemented Interfaces:** Serializable

,

Key

,

SecretKey

,

Destroyable

```java
public class
KerberosKey

extends
Object

implements
SecretKey
```

This class encapsulates a long term secret key for a Kerberos
principal.

A

KerberosKey

object includes an EncryptionKey, a

KerberosPrincipal

as its owner, and the version number
of the key.

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

The key material of a

KerberosKey

is defined as the value
of the

keyValue

above.

All Kerberos JAAS login modules that obtain a principal's password and
generate the secret key from it should use this class.
Sometimes, such as when authenticating a server in
the absence of user-to-user authentication, the login module will store
an instance of this class in the private credential set of a

Subject

during the commit phase of the
authentication process.

A Kerberos service using a keytab to read secret keys should use
the

KeyTab

class, where latest keys can be read when needed.

It might be necessary for the application to be granted a

PrivateCredentialPermission

if it needs to access the

KerberosKey

instance from a Subject. This permission is not needed when the
application depends on the default JGSS Kerberos mechanism to access the

KerberosKey

. In that case, however, the application will need an
appropriate

ServicePermission

.

When creating a

KerberosKey

using the

KerberosKey(KerberosPrincipal, char[], String)

constructor,
an implementation may accept non-IANA algorithm names (For example,
"ArcFourMac" for "rc4-hmac"), but the

getAlgorithm()

method
must always return the IANA algorithm name.

**Implementation Note:** Old algorithm names used before JDK 9 are supported in the

KerberosKey(KerberosPrincipal, char[], String)

constructor in this
implementation for compatibility reasons, which are "DES" (and null) for
"des-cbc-md5", "DESede" for "des3-cbc-sha1-kd", "ArcFourHmac" for "rc4-hmac",
"AES128" for "aes128-cts-hmac-sha1-96", and "AES256" for
"aes256-cts-hmac-sha1-96".
**Since:** 1.4
**See Also:** Serialized Form

public class

KerberosKey

extends

Object

implements

SecretKey

This class encapsulates a long term secret key for a Kerberos
principal.

A

KerberosKey

object includes an EncryptionKey, a

KerberosPrincipal

as its owner, and the version number
of the key.

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

The key material of a

KerberosKey

is defined as the value
of the

keyValue

above.

All Kerberos JAAS login modules that obtain a principal's password and
generate the secret key from it should use this class.
Sometimes, such as when authenticating a server in
the absence of user-to-user authentication, the login module will store
an instance of this class in the private credential set of a

Subject

during the commit phase of the
authentication process.

A Kerberos service using a keytab to read secret keys should use
the

KeyTab

class, where latest keys can be read when needed.

It might be necessary for the application to be granted a

PrivateCredentialPermission

if it needs to access the

KerberosKey

instance from a Subject. This permission is not needed when the
application depends on the default JGSS Kerberos mechanism to access the

KerberosKey

. In that case, however, the application will need an
appropriate

ServicePermission

.

When creating a

KerberosKey

using the

KerberosKey(KerberosPrincipal, char[], String)

constructor,
an implementation may accept non-IANA algorithm names (For example,
"ArcFourMac" for "rc4-hmac"), but the

getAlgorithm()

method
must always return the IANA algorithm name.

A

KerberosKey

object includes an EncryptionKey, a

KerberosPrincipal

as its owner, and the version number
of the key.

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

The key material of a

KerberosKey

is defined as the value
of the

keyValue

above.

All Kerberos JAAS login modules that obtain a principal's password and
generate the secret key from it should use this class.
Sometimes, such as when authenticating a server in
the absence of user-to-user authentication, the login module will store
an instance of this class in the private credential set of a

Subject

during the commit phase of the
authentication process.

A Kerberos service using a keytab to read secret keys should use
the

KeyTab

class, where latest keys can be read when needed.

It might be necessary for the application to be granted a

PrivateCredentialPermission

if it needs to access the

KerberosKey

instance from a Subject. This permission is not needed when the
application depends on the default JGSS Kerberos mechanism to access the

KerberosKey

. In that case, however, the application will need an
appropriate

ServicePermission

.

When creating a

KerberosKey

using the

KerberosKey(KerberosPrincipal, char[], String)

constructor,
an implementation may accept non-IANA algorithm names (For example,
"ArcFourMac" for "rc4-hmac"), but the

getAlgorithm()

method
must always return the IANA algorithm name.

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

The key material of a

KerberosKey

is defined as the value
of the

keyValue

above.

All Kerberos JAAS login modules that obtain a principal's password and
generate the secret key from it should use this class.
Sometimes, such as when authenticating a server in
the absence of user-to-user authentication, the login module will store
an instance of this class in the private credential set of a

Subject

during the commit phase of the
authentication process.

A Kerberos service using a keytab to read secret keys should use
the

KeyTab

class, where latest keys can be read when needed.

It might be necessary for the application to be granted a

PrivateCredentialPermission

if it needs to access the

KerberosKey

instance from a Subject. This permission is not needed when the
application depends on the default JGSS Kerberos mechanism to access the

KerberosKey

. In that case, however, the application will need an
appropriate

ServicePermission

.

When creating a

KerberosKey

using the

KerberosKey(KerberosPrincipal, char[], String)

constructor,
an implementation may accept non-IANA algorithm names (For example,
"ArcFourMac" for "rc4-hmac"), but the

getAlgorithm()

method
must always return the IANA algorithm name.

EncryptionKey ::= SEQUENCE {
keytype [0] Int32 -- actually encryption type --,
keyvalue [1] OCTET STRING
}

All Kerberos JAAS login modules that obtain a principal's password and
generate the secret key from it should use this class.
Sometimes, such as when authenticating a server in
the absence of user-to-user authentication, the login module will store
an instance of this class in the private credential set of a

Subject

during the commit phase of the
authentication process.

A Kerberos service using a keytab to read secret keys should use
the

KeyTab

class, where latest keys can be read when needed.

It might be necessary for the application to be granted a

PrivateCredentialPermission

if it needs to access the

KerberosKey

instance from a Subject. This permission is not needed when the
application depends on the default JGSS Kerberos mechanism to access the

KerberosKey

. In that case, however, the application will need an
appropriate

ServicePermission

.

When creating a

KerberosKey

using the

KerberosKey(KerberosPrincipal, char[], String)

constructor,
an implementation may accept non-IANA algorithm names (For example,
"ArcFourMac" for "rc4-hmac"), but the

getAlgorithm()

method
must always return the IANA algorithm name.

A Kerberos service using a keytab to read secret keys should use
the

KeyTab

class, where latest keys can be read when needed.

It might be necessary for the application to be granted a

PrivateCredentialPermission

if it needs to access the

KerberosKey

instance from a Subject. This permission is not needed when the
application depends on the default JGSS Kerberos mechanism to access the

KerberosKey

. In that case, however, the application will need an
appropriate

ServicePermission

.

When creating a

KerberosKey

using the

KerberosKey(KerberosPrincipal, char[], String)

constructor,
an implementation may accept non-IANA algorithm names (For example,
"ArcFourMac" for "rc4-hmac"), but the

getAlgorithm()

method
must always return the IANA algorithm name.

It might be necessary for the application to be granted a

PrivateCredentialPermission

if it needs to access the

KerberosKey

instance from a Subject. This permission is not needed when the
application depends on the default JGSS Kerberos mechanism to access the

KerberosKey

. In that case, however, the application will need an
appropriate

ServicePermission

.

When creating a

KerberosKey

using the

KerberosKey(KerberosPrincipal, char[], String)

constructor,
an implementation may accept non-IANA algorithm names (For example,
"ArcFourMac" for "rc4-hmac"), but the

getAlgorithm()

method
must always return the IANA algorithm name.

When creating a

KerberosKey

using the

KerberosKey(KerberosPrincipal, char[], String)

constructor,
an implementation may accept non-IANA algorithm names (For example,
"ArcFourMac" for "rc4-hmac"), but the

getAlgorithm()

method
must always return the IANA algorithm name.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

KerberosKey

​(

KerberosPrincipal

principal,
byte[] keyBytes,
int keyType,
int versionNum)

Constructs a

KerberosKey

from the given bytes when the key type
and key version number are known.

KerberosKey

​(

KerberosPrincipal

principal,
char[] password,

String

algorithm)

Constructs a

KerberosKey

from a principal's password using the
specified algorithm name.

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

Destroys this key by clearing out the key material of this secret key.

boolean

equals

​(

Object

other)

Compares the specified object with this

KerberosKey

for
equality.

String

getAlgorithm

()

Returns the standard algorithm name for this key.

byte[]

getEncoded

()

Returns the key material of this secret key.

String

getFormat

()

Returns the name of the encoding format for this secret key.

int

getKeyType

()

Returns the key type for this long-term key.

KerberosPrincipal

getPrincipal

()

Returns the principal that this key belongs to.

int

getVersionNumber

()

Returns the key version number.

int

hashCode

()

Returns a hash code for this

KerberosKey

.

boolean

isDestroyed

()

Determines if this key has been destroyed.

String

toString

()

Returns an informative textual representation of this

KerberosKey

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

Constructor Summary

Constructors

Constructor

Description

KerberosKey

​(

KerberosPrincipal

principal,
byte[] keyBytes,
int keyType,
int versionNum)

Constructs a

KerberosKey

from the given bytes when the key type
and key version number are known.

KerberosKey

​(

KerberosPrincipal

principal,
char[] password,

String

algorithm)

Constructs a

KerberosKey

from a principal's password using the
specified algorithm name.

---

#### Constructor Summary

Constructs a

KerberosKey

from the given bytes when the key type
and key version number are known.

Constructs a

KerberosKey

from a principal's password using the
specified algorithm name.

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

Destroys this key by clearing out the key material of this secret key.

boolean

equals

​(

Object

other)

Compares the specified object with this

KerberosKey

for
equality.

String

getAlgorithm

()

Returns the standard algorithm name for this key.

byte[]

getEncoded

()

Returns the key material of this secret key.

String

getFormat

()

Returns the name of the encoding format for this secret key.

int

getKeyType

()

Returns the key type for this long-term key.

KerberosPrincipal

getPrincipal

()

Returns the principal that this key belongs to.

int

getVersionNumber

()

Returns the key version number.

int

hashCode

()

Returns a hash code for this

KerberosKey

.

boolean

isDestroyed

()

Determines if this key has been destroyed.

String

toString

()

Returns an informative textual representation of this

KerberosKey

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

---

#### Method Summary

Destroys this key by clearing out the key material of this secret key.

Compares the specified object with this

KerberosKey

for
equality.

Returns the standard algorithm name for this key.

Returns the key material of this secret key.

Returns the name of the encoding format for this secret key.

Returns the key type for this long-term key.

Returns the principal that this key belongs to.

Returns the key version number.

Returns a hash code for this

KerberosKey

.

Determines if this key has been destroyed.

Returns an informative textual representation of this

KerberosKey

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- KerberosKey

```java
public KerberosKey​(
KerberosPrincipal
principal,
byte[] keyBytes,
int keyType,
int versionNum)
```

Constructs a

KerberosKey

from the given bytes when the key type
and key version number are known. This can be used when reading the
secret key information from a Kerberos "keytab".

**Parameters:** principal

- the principal that this secret key belongs to
**Parameters:** keyBytes

- the key material for the secret key
**Parameters:** keyType

- the key type for the secret key as defined by the
Kerberos protocol specification.
**Parameters:** versionNum

- the version number of this secret key

- KerberosKey

```java
public KerberosKey​(
KerberosPrincipal
principal,
char[] password,

String
algorithm)
```

Constructs a

KerberosKey

from a principal's password using the
specified algorithm name. The algorithm name (case insensitive) should
be provided as the encryption type string defined on the IANA

Kerberos Encryption Type Numbers

page. The version number of the key generated will be 0.

**Parameters:** principal

- the principal that this password belongs to
**Parameters:** password

- the password that should be used to compute the key
**Parameters:** algorithm

- the name for the algorithm that this key will be
used for
**Throws:** IllegalArgumentException

- if the name of the
algorithm passed is unsupported.

============ METHOD DETAIL ==========

- Method Detail

- getPrincipal

```java
public final
KerberosPrincipal
getPrincipal()
```

Returns the principal that this key belongs to.

**Returns:** the principal this key belongs to.
**Throws:** IllegalStateException

- if the key is destroyed

- getVersionNumber

```java
public final int getVersionNumber()
```

Returns the key version number.

**Returns:** the key version number.
**Throws:** IllegalStateException

- if the key is destroyed

- getKeyType

```java
public final int getKeyType()
```

Returns the key type for this long-term key.

**Returns:** the key type.
**Throws:** IllegalStateException

- if the key is destroyed

- getAlgorithm

```java
public final
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
public final
String
getFormat()
```

Returns the name of the encoding format for this secret key.

**Specified by:** getFormat

in interface

Key
**Returns:** the String "RAW"
**Throws:** IllegalStateException

- if the key is destroyed

- getEncoded

```java
public final byte[] getEncoded()
```

Returns the key material of this secret key.

**Specified by:** getEncoded

in interface

Key
**Returns:** the key material
**Throws:** IllegalStateException

- if the key is destroyed

- destroy

```java
public void destroy()
throws
DestroyFailedException
```

Destroys this key by clearing out the key material of this secret key.

**Specified by:** destroy

in interface

Destroyable
**Throws:** DestroyFailedException

- if some error occurs while destorying
this key.

- isDestroyed

```java
public boolean isDestroyed()
```

Determines if this key has been destroyed.

**Specified by:** isDestroyed

in interface

Destroyable
**Returns:** true if this

Object

has been destroyed,
false otherwise.

- toString

```java
public
String
toString()
```

Returns an informative textual representation of this

KerberosKey

.

**Overrides:** toString

in class

Object
**Returns:** an informative textual representation of this

KerberosKey

.

- hashCode

```java
public int hashCode()
```

Returns a hash code for this

KerberosKey

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this

KerberosKey

.
**Since:** 1.6
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
other)
```

Compares the specified object with this

KerberosKey

for
equality. Returns true if the given object is also a

KerberosKey

and the two

KerberosKey

instances are equivalent.
A destroyed

KerberosKey

object is only equal to itself.

**Overrides:** equals

in class

Object
**Parameters:** other

- the object to compare to
**Returns:** true if the specified object is equal to this

KerberosKey

,
false otherwise.
**Since:** 1.6
**See Also:** Object.hashCode()

,

HashMap

Constructor Detail

- KerberosKey

```java
public KerberosKey​(
KerberosPrincipal
principal,
byte[] keyBytes,
int keyType,
int versionNum)
```

Constructs a

KerberosKey

from the given bytes when the key type
and key version number are known. This can be used when reading the
secret key information from a Kerberos "keytab".

**Parameters:** principal

- the principal that this secret key belongs to
**Parameters:** keyBytes

- the key material for the secret key
**Parameters:** keyType

- the key type for the secret key as defined by the
Kerberos protocol specification.
**Parameters:** versionNum

- the version number of this secret key

- KerberosKey

```java
public KerberosKey​(
KerberosPrincipal
principal,
char[] password,

String
algorithm)
```

Constructs a

KerberosKey

from a principal's password using the
specified algorithm name. The algorithm name (case insensitive) should
be provided as the encryption type string defined on the IANA

Kerberos Encryption Type Numbers

page. The version number of the key generated will be 0.

**Parameters:** principal

- the principal that this password belongs to
**Parameters:** password

- the password that should be used to compute the key
**Parameters:** algorithm

- the name for the algorithm that this key will be
used for
**Throws:** IllegalArgumentException

- if the name of the
algorithm passed is unsupported.

---

#### Constructor Detail

KerberosKey

```java
public KerberosKey​(
KerberosPrincipal
principal,
byte[] keyBytes,
int keyType,
int versionNum)
```

Constructs a

KerberosKey

from the given bytes when the key type
and key version number are known. This can be used when reading the
secret key information from a Kerberos "keytab".

**Parameters:** principal

- the principal that this secret key belongs to
**Parameters:** keyBytes

- the key material for the secret key
**Parameters:** keyType

- the key type for the secret key as defined by the
Kerberos protocol specification.
**Parameters:** versionNum

- the version number of this secret key

---

#### KerberosKey

public KerberosKey​(

KerberosPrincipal

principal,
byte[] keyBytes,
int keyType,
int versionNum)

Constructs a

KerberosKey

from the given bytes when the key type
and key version number are known. This can be used when reading the
secret key information from a Kerberos "keytab".

KerberosKey

```java
public KerberosKey​(
KerberosPrincipal
principal,
char[] password,

String
algorithm)
```

Constructs a

KerberosKey

from a principal's password using the
specified algorithm name. The algorithm name (case insensitive) should
be provided as the encryption type string defined on the IANA

Kerberos Encryption Type Numbers

page. The version number of the key generated will be 0.

**Parameters:** principal

- the principal that this password belongs to
**Parameters:** password

- the password that should be used to compute the key
**Parameters:** algorithm

- the name for the algorithm that this key will be
used for
**Throws:** IllegalArgumentException

- if the name of the
algorithm passed is unsupported.

---

#### KerberosKey

public KerberosKey​(

KerberosPrincipal

principal,
char[] password,

String

algorithm)

Constructs a

KerberosKey

from a principal's password using the
specified algorithm name. The algorithm name (case insensitive) should
be provided as the encryption type string defined on the IANA

Kerberos Encryption Type Numbers

page. The version number of the key generated will be 0.

Method Detail

- getPrincipal

```java
public final
KerberosPrincipal
getPrincipal()
```

Returns the principal that this key belongs to.

**Returns:** the principal this key belongs to.
**Throws:** IllegalStateException

- if the key is destroyed

- getVersionNumber

```java
public final int getVersionNumber()
```

Returns the key version number.

**Returns:** the key version number.
**Throws:** IllegalStateException

- if the key is destroyed

- getKeyType

```java
public final int getKeyType()
```

Returns the key type for this long-term key.

**Returns:** the key type.
**Throws:** IllegalStateException

- if the key is destroyed

- getAlgorithm

```java
public final
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
public final
String
getFormat()
```

Returns the name of the encoding format for this secret key.

**Specified by:** getFormat

in interface

Key
**Returns:** the String "RAW"
**Throws:** IllegalStateException

- if the key is destroyed

- getEncoded

```java
public final byte[] getEncoded()
```

Returns the key material of this secret key.

**Specified by:** getEncoded

in interface

Key
**Returns:** the key material
**Throws:** IllegalStateException

- if the key is destroyed

- destroy

```java
public void destroy()
throws
DestroyFailedException
```

Destroys this key by clearing out the key material of this secret key.

**Specified by:** destroy

in interface

Destroyable
**Throws:** DestroyFailedException

- if some error occurs while destorying
this key.

- isDestroyed

```java
public boolean isDestroyed()
```

Determines if this key has been destroyed.

**Specified by:** isDestroyed

in interface

Destroyable
**Returns:** true if this

Object

has been destroyed,
false otherwise.

- toString

```java
public
String
toString()
```

Returns an informative textual representation of this

KerberosKey

.

**Overrides:** toString

in class

Object
**Returns:** an informative textual representation of this

KerberosKey

.

- hashCode

```java
public int hashCode()
```

Returns a hash code for this

KerberosKey

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this

KerberosKey

.
**Since:** 1.6
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
other)
```

Compares the specified object with this

KerberosKey

for
equality. Returns true if the given object is also a

KerberosKey

and the two

KerberosKey

instances are equivalent.
A destroyed

KerberosKey

object is only equal to itself.

**Overrides:** equals

in class

Object
**Parameters:** other

- the object to compare to
**Returns:** true if the specified object is equal to this

KerberosKey

,
false otherwise.
**Since:** 1.6
**See Also:** Object.hashCode()

,

HashMap

---

#### Method Detail

getPrincipal

```java
public final
KerberosPrincipal
getPrincipal()
```

Returns the principal that this key belongs to.

**Returns:** the principal this key belongs to.
**Throws:** IllegalStateException

- if the key is destroyed

---

#### getPrincipal

public final

KerberosPrincipal

getPrincipal()

Returns the principal that this key belongs to.

getVersionNumber

```java
public final int getVersionNumber()
```

Returns the key version number.

**Returns:** the key version number.
**Throws:** IllegalStateException

- if the key is destroyed

---

#### getVersionNumber

public final int getVersionNumber()

Returns the key version number.

getKeyType

```java
public final int getKeyType()
```

Returns the key type for this long-term key.

**Returns:** the key type.
**Throws:** IllegalStateException

- if the key is destroyed

---

#### getKeyType

public final int getKeyType()

Returns the key type for this long-term key.

getAlgorithm

```java
public final
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

public final

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
public final
String
getFormat()
```

Returns the name of the encoding format for this secret key.

**Specified by:** getFormat

in interface

Key
**Returns:** the String "RAW"
**Throws:** IllegalStateException

- if the key is destroyed

---

#### getFormat

public final

String

getFormat()

Returns the name of the encoding format for this secret key.

getEncoded

```java
public final byte[] getEncoded()
```

Returns the key material of this secret key.

**Specified by:** getEncoded

in interface

Key
**Returns:** the key material
**Throws:** IllegalStateException

- if the key is destroyed

---

#### getEncoded

public final byte[] getEncoded()

Returns the key material of this secret key.

destroy

```java
public void destroy()
throws
DestroyFailedException
```

Destroys this key by clearing out the key material of this secret key.

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

Destroys this key by clearing out the key material of this secret key.

isDestroyed

```java
public boolean isDestroyed()
```

Determines if this key has been destroyed.

**Specified by:** isDestroyed

in interface

Destroyable
**Returns:** true if this

Object

has been destroyed,
false otherwise.

---

#### isDestroyed

public boolean isDestroyed()

Determines if this key has been destroyed.

toString

```java
public
String
toString()
```

Returns an informative textual representation of this

KerberosKey

.

**Overrides:** toString

in class

Object
**Returns:** an informative textual representation of this

KerberosKey

.

---

#### toString

public

String

toString()

Returns an informative textual representation of this

KerberosKey

.

hashCode

```java
public int hashCode()
```

Returns a hash code for this

KerberosKey

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this

KerberosKey

.
**Since:** 1.6
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns a hash code for this

KerberosKey

.

equals

```java
public boolean equals​(
Object
other)
```

Compares the specified object with this

KerberosKey

for
equality. Returns true if the given object is also a

KerberosKey

and the two

KerberosKey

instances are equivalent.
A destroyed

KerberosKey

object is only equal to itself.

**Overrides:** equals

in class

Object
**Parameters:** other

- the object to compare to
**Returns:** true if the specified object is equal to this

KerberosKey

,
false otherwise.
**Since:** 1.6
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

other)

Compares the specified object with this

KerberosKey

for
equality. Returns true if the given object is also a

KerberosKey

and the two

KerberosKey

instances are equivalent.
A destroyed

KerberosKey

object is only equal to itself.

---

