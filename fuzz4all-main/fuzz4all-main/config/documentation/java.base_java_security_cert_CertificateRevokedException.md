# Class CertificateRevokedException

**Source:** `java.base\java\security\cert\CertificateRevokedException.html`

### Class Description

```java
public class
CertificateRevokedException

extends
CertificateException
```

An exception that indicates an X.509 certificate is revoked. A

CertificateRevokedException

contains additional information
about the revoked certificate, such as the date on which the
certificate was revoked and the reason it was revoked.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public CertificateRevokedException​(
Date
revocationDate,

CRLReason
reason,

X500Principal
authority,

Map
<
String
,​
Extension
> extensions)

Constructs a

CertificateRevokedException

with
the specified revocation date, reason code, authority name, and map
of extensions.

**Parameters:**
- revocationDate

- the date on which the certificate was revoked. The
date is copied to protect against subsequent modification.
- reason

- the revocation reason
- extensions

- a map of X.509 Extensions. Each key is an OID String
that maps to the corresponding Extension. The map is copied to
prevent subsequent modification.
- authority

- the

X500Principal

that represents the name
of the authority that signed the certificate's revocation status
information

**Throws:**
- NullPointerException

- if

revocationDate

,

reason

,

authority

, or

extensions

is

null
- ClassCastException

- if

extensions

contains an incorrectly
typed key or value

---

### Method Details

#### public
Date
getRevocationDate()

Returns the date on which the certificate was revoked. A new copy is
returned each time the method is invoked to protect against subsequent
modification.

**Returns:**
- the revocation date

---

#### public
CRLReason
getRevocationReason()

Returns the reason the certificate was revoked.

**Returns:**
- the revocation reason

---

#### public
X500Principal
getAuthorityName()

Returns the name of the authority that signed the certificate's
revocation status information.

**Returns:**
- the

X500Principal

that represents the name of the
authority that signed the certificate's revocation status information

---

#### public
Date
getInvalidityDate()

Returns the invalidity date, as specified in the Invalidity Date
extension of this

CertificateRevokedException

. The
invalidity date is the date on which it is known or suspected that the
private key was compromised or that the certificate otherwise became
invalid. This implementation calls

getExtensions()

and
checks the returned map for an entry for the Invalidity Date extension
OID ("2.5.29.24"). If found, it returns the invalidity date in the
extension; otherwise null. A new Date object is returned each time the
method is invoked to protect against subsequent modification.

**Returns:**
- the invalidity date, or

null

if not specified

---

#### public
Map
<
String
,​
Extension
> getExtensions()

Returns a map of X.509 extensions containing additional information
about the revoked certificate, such as the Invalidity Date
Extension. Each key is an OID String that maps to the corresponding
Extension.

**Returns:**
- an unmodifiable map of X.509 extensions, or an empty map
if there are no extensions

---

### Additional Sections

#### Class CertificateRevokedException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.security.GeneralSecurityException
- - java.security.cert.CertificateException
- - java.security.cert.CertificateRevokedException

java.lang.Throwable

- java.lang.Exception
- - java.security.GeneralSecurityException
- - java.security.cert.CertificateException
- - java.security.cert.CertificateRevokedException

java.lang.Exception

- java.security.GeneralSecurityException
- - java.security.cert.CertificateException
- - java.security.cert.CertificateRevokedException

java.security.GeneralSecurityException

- java.security.cert.CertificateException
- - java.security.cert.CertificateRevokedException

java.security.cert.CertificateException

- java.security.cert.CertificateRevokedException

java.security.cert.CertificateRevokedException

**All Implemented Interfaces:** Serializable

```java
public class
CertificateRevokedException

extends
CertificateException
```

An exception that indicates an X.509 certificate is revoked. A

CertificateRevokedException

contains additional information
about the revoked certificate, such as the date on which the
certificate was revoked and the reason it was revoked.

**Since:** 1.7
**See Also:** CertPathValidatorException

,

Serialized Form

public class

CertificateRevokedException

extends

CertificateException

An exception that indicates an X.509 certificate is revoked. A

CertificateRevokedException

contains additional information
about the revoked certificate, such as the date on which the
certificate was revoked and the reason it was revoked.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

CertificateRevokedException

​(

Date

revocationDate,

CRLReason

reason,

X500Principal

authority,

Map

<

String

,​

Extension

> extensions)

Constructs a

CertificateRevokedException

with
the specified revocation date, reason code, authority name, and map
of extensions.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

X500Principal

getAuthorityName

()

Returns the name of the authority that signed the certificate's
revocation status information.

Map

<

String

,​

Extension

>

getExtensions

()

Returns a map of X.509 extensions containing additional information
about the revoked certificate, such as the Invalidity Date
Extension.

Date

getInvalidityDate

()

Returns the invalidity date, as specified in the Invalidity Date
extension of this

CertificateRevokedException

.

Date

getRevocationDate

()

Returns the date on which the certificate was revoked.

CRLReason

getRevocationReason

()

Returns the reason the certificate was revoked.

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

CertificateRevokedException

​(

Date

revocationDate,

CRLReason

reason,

X500Principal

authority,

Map

<

String

,​

Extension

> extensions)

Constructs a

CertificateRevokedException

with
the specified revocation date, reason code, authority name, and map
of extensions.

---

#### Constructor Summary

Constructs a

CertificateRevokedException

with
the specified revocation date, reason code, authority name, and map
of extensions.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

X500Principal

getAuthorityName

()

Returns the name of the authority that signed the certificate's
revocation status information.

Map

<

String

,​

Extension

>

getExtensions

()

Returns a map of X.509 extensions containing additional information
about the revoked certificate, such as the Invalidity Date
Extension.

Date

getInvalidityDate

()

Returns the invalidity date, as specified in the Invalidity Date
extension of this

CertificateRevokedException

.

Date

getRevocationDate

()

Returns the date on which the certificate was revoked.

CRLReason

getRevocationReason

()

Returns the reason the certificate was revoked.

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

Returns the name of the authority that signed the certificate's
revocation status information.

Returns a map of X.509 extensions containing additional information
about the revoked certificate, such as the Invalidity Date
Extension.

Returns the invalidity date, as specified in the Invalidity Date
extension of this

CertificateRevokedException

.

Returns the date on which the certificate was revoked.

Returns the reason the certificate was revoked.

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

- CertificateRevokedException

```java
public CertificateRevokedException​(
Date
revocationDate,

CRLReason
reason,

X500Principal
authority,

Map
<
String
,​
Extension
> extensions)
```

Constructs a

CertificateRevokedException

with
the specified revocation date, reason code, authority name, and map
of extensions.

**Parameters:** revocationDate

- the date on which the certificate was revoked. The
date is copied to protect against subsequent modification.
**Parameters:** reason

- the revocation reason
**Parameters:** extensions

- a map of X.509 Extensions. Each key is an OID String
that maps to the corresponding Extension. The map is copied to
prevent subsequent modification.
**Parameters:** authority

- the

X500Principal

that represents the name
of the authority that signed the certificate's revocation status
information
**Throws:** NullPointerException

- if

revocationDate

,

reason

,

authority

, or

extensions

is

null
**Throws:** ClassCastException

- if

extensions

contains an incorrectly
typed key or value

============ METHOD DETAIL ==========

- Method Detail

- getRevocationDate

```java
public
Date
getRevocationDate()
```

Returns the date on which the certificate was revoked. A new copy is
returned each time the method is invoked to protect against subsequent
modification.

**Returns:** the revocation date

- getRevocationReason

```java
public
CRLReason
getRevocationReason()
```

Returns the reason the certificate was revoked.

**Returns:** the revocation reason

- getAuthorityName

```java
public
X500Principal
getAuthorityName()
```

Returns the name of the authority that signed the certificate's
revocation status information.

**Returns:** the

X500Principal

that represents the name of the
authority that signed the certificate's revocation status information

- getInvalidityDate

```java
public
Date
getInvalidityDate()
```

Returns the invalidity date, as specified in the Invalidity Date
extension of this

CertificateRevokedException

. The
invalidity date is the date on which it is known or suspected that the
private key was compromised or that the certificate otherwise became
invalid. This implementation calls

getExtensions()

and
checks the returned map for an entry for the Invalidity Date extension
OID ("2.5.29.24"). If found, it returns the invalidity date in the
extension; otherwise null. A new Date object is returned each time the
method is invoked to protect against subsequent modification.

**Returns:** the invalidity date, or

null

if not specified

- getExtensions

```java
public
Map
<
String
,​
Extension
> getExtensions()
```

Returns a map of X.509 extensions containing additional information
about the revoked certificate, such as the Invalidity Date
Extension. Each key is an OID String that maps to the corresponding
Extension.

**Returns:** an unmodifiable map of X.509 extensions, or an empty map
if there are no extensions

Constructor Detail

- CertificateRevokedException

```java
public CertificateRevokedException​(
Date
revocationDate,

CRLReason
reason,

X500Principal
authority,

Map
<
String
,​
Extension
> extensions)
```

Constructs a

CertificateRevokedException

with
the specified revocation date, reason code, authority name, and map
of extensions.

**Parameters:** revocationDate

- the date on which the certificate was revoked. The
date is copied to protect against subsequent modification.
**Parameters:** reason

- the revocation reason
**Parameters:** extensions

- a map of X.509 Extensions. Each key is an OID String
that maps to the corresponding Extension. The map is copied to
prevent subsequent modification.
**Parameters:** authority

- the

X500Principal

that represents the name
of the authority that signed the certificate's revocation status
information
**Throws:** NullPointerException

- if

revocationDate

,

reason

,

authority

, or

extensions

is

null
**Throws:** ClassCastException

- if

extensions

contains an incorrectly
typed key or value

---

#### Constructor Detail

CertificateRevokedException

```java
public CertificateRevokedException​(
Date
revocationDate,

CRLReason
reason,

X500Principal
authority,

Map
<
String
,​
Extension
> extensions)
```

Constructs a

CertificateRevokedException

with
the specified revocation date, reason code, authority name, and map
of extensions.

**Parameters:** revocationDate

- the date on which the certificate was revoked. The
date is copied to protect against subsequent modification.
**Parameters:** reason

- the revocation reason
**Parameters:** extensions

- a map of X.509 Extensions. Each key is an OID String
that maps to the corresponding Extension. The map is copied to
prevent subsequent modification.
**Parameters:** authority

- the

X500Principal

that represents the name
of the authority that signed the certificate's revocation status
information
**Throws:** NullPointerException

- if

revocationDate

,

reason

,

authority

, or

extensions

is

null
**Throws:** ClassCastException

- if

extensions

contains an incorrectly
typed key or value

---

#### CertificateRevokedException

public CertificateRevokedException​(

Date

revocationDate,

CRLReason

reason,

X500Principal

authority,

Map

<

String

,​

Extension

> extensions)

Constructs a

CertificateRevokedException

with
the specified revocation date, reason code, authority name, and map
of extensions.

Method Detail

- getRevocationDate

```java
public
Date
getRevocationDate()
```

Returns the date on which the certificate was revoked. A new copy is
returned each time the method is invoked to protect against subsequent
modification.

**Returns:** the revocation date

- getRevocationReason

```java
public
CRLReason
getRevocationReason()
```

Returns the reason the certificate was revoked.

**Returns:** the revocation reason

- getAuthorityName

```java
public
X500Principal
getAuthorityName()
```

Returns the name of the authority that signed the certificate's
revocation status information.

**Returns:** the

X500Principal

that represents the name of the
authority that signed the certificate's revocation status information

- getInvalidityDate

```java
public
Date
getInvalidityDate()
```

Returns the invalidity date, as specified in the Invalidity Date
extension of this

CertificateRevokedException

. The
invalidity date is the date on which it is known or suspected that the
private key was compromised or that the certificate otherwise became
invalid. This implementation calls

getExtensions()

and
checks the returned map for an entry for the Invalidity Date extension
OID ("2.5.29.24"). If found, it returns the invalidity date in the
extension; otherwise null. A new Date object is returned each time the
method is invoked to protect against subsequent modification.

**Returns:** the invalidity date, or

null

if not specified

- getExtensions

```java
public
Map
<
String
,​
Extension
> getExtensions()
```

Returns a map of X.509 extensions containing additional information
about the revoked certificate, such as the Invalidity Date
Extension. Each key is an OID String that maps to the corresponding
Extension.

**Returns:** an unmodifiable map of X.509 extensions, or an empty map
if there are no extensions

---

#### Method Detail

getRevocationDate

```java
public
Date
getRevocationDate()
```

Returns the date on which the certificate was revoked. A new copy is
returned each time the method is invoked to protect against subsequent
modification.

**Returns:** the revocation date

---

#### getRevocationDate

public

Date

getRevocationDate()

Returns the date on which the certificate was revoked. A new copy is
returned each time the method is invoked to protect against subsequent
modification.

getRevocationReason

```java
public
CRLReason
getRevocationReason()
```

Returns the reason the certificate was revoked.

**Returns:** the revocation reason

---

#### getRevocationReason

public

CRLReason

getRevocationReason()

Returns the reason the certificate was revoked.

getAuthorityName

```java
public
X500Principal
getAuthorityName()
```

Returns the name of the authority that signed the certificate's
revocation status information.

**Returns:** the

X500Principal

that represents the name of the
authority that signed the certificate's revocation status information

---

#### getAuthorityName

public

X500Principal

getAuthorityName()

Returns the name of the authority that signed the certificate's
revocation status information.

getInvalidityDate

```java
public
Date
getInvalidityDate()
```

Returns the invalidity date, as specified in the Invalidity Date
extension of this

CertificateRevokedException

. The
invalidity date is the date on which it is known or suspected that the
private key was compromised or that the certificate otherwise became
invalid. This implementation calls

getExtensions()

and
checks the returned map for an entry for the Invalidity Date extension
OID ("2.5.29.24"). If found, it returns the invalidity date in the
extension; otherwise null. A new Date object is returned each time the
method is invoked to protect against subsequent modification.

**Returns:** the invalidity date, or

null

if not specified

---

#### getInvalidityDate

public

Date

getInvalidityDate()

Returns the invalidity date, as specified in the Invalidity Date
extension of this

CertificateRevokedException

. The
invalidity date is the date on which it is known or suspected that the
private key was compromised or that the certificate otherwise became
invalid. This implementation calls

getExtensions()

and
checks the returned map for an entry for the Invalidity Date extension
OID ("2.5.29.24"). If found, it returns the invalidity date in the
extension; otherwise null. A new Date object is returned each time the
method is invoked to protect against subsequent modification.

getExtensions

```java
public
Map
<
String
,​
Extension
> getExtensions()
```

Returns a map of X.509 extensions containing additional information
about the revoked certificate, such as the Invalidity Date
Extension. Each key is an OID String that maps to the corresponding
Extension.

**Returns:** an unmodifiable map of X.509 extensions, or an empty map
if there are no extensions

---

#### getExtensions

public

Map

<

String

,​

Extension

> getExtensions()

Returns a map of X.509 extensions containing additional information
about the revoked certificate, such as the Invalidity Date
Extension. Each key is an OID String that maps to the corresponding
Extension.

---

