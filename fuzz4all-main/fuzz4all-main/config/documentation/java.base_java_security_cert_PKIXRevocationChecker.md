# Class PKIXRevocationChecker

**Source:** `java.base\java\security\cert\PKIXRevocationChecker.html`

### Class Description

```java
public abstract class
PKIXRevocationChecker

extends
PKIXCertPathChecker
```

A

PKIXCertPathChecker

for checking the revocation status of
certificates with the PKIX algorithm.

A

PKIXRevocationChecker

checks the revocation status of
certificates with the Online Certificate Status Protocol (OCSP) or
Certificate Revocation Lists (CRLs). OCSP is described in RFC 2560 and
is a network protocol for determining the status of a certificate. A CRL
is a time-stamped list identifying revoked certificates, and RFC 5280
describes an algorithm for determining the revocation status of certificates
using CRLs.

Each

PKIXRevocationChecker

must be able to check the revocation
status of certificates with OCSP and CRLs. By default, OCSP is the
preferred mechanism for checking revocation status, with CRLs as the
fallback mechanism. However, this preference can be switched to CRLs with
the

PREFER_CRLS

option. In addition, the fallback
mechanism can be disabled with the

NO_FALLBACK

option.

A

PKIXRevocationChecker

is obtained by calling the

getRevocationChecker

method
of a PKIX

CertPathValidator

. Additional parameters and options
specific to revocation can be set (by calling the

setOcspResponder

method for instance). The

PKIXRevocationChecker

is added to a

PKIXParameters

object
using the

addCertPathChecker

or

setCertPathCheckers

method,
and then the

PKIXParameters

is passed along with the

CertPath

to be validated to the

validate

method
of a PKIX

CertPathValidator

. When supplying a revocation checker in
this manner, it will be used to check revocation irrespective of the setting
of the

RevocationEnabled

flag.
Similarly, a

PKIXRevocationChecker

may be added to a

PKIXBuilderParameters

object for use with a PKIX

CertPathBuilder

.

Note that when a

PKIXRevocationChecker

is added to

PKIXParameters

, it clones the

PKIXRevocationChecker

;
thus any subsequent modifications to the

PKIXRevocationChecker

have no effect.

Any parameter that is not set (or is set to

null

) will be set to
the default value for that parameter.

Concurrent Access

Unless otherwise specified, the methods defined in this class are not
thread-safe. Multiple threads that need to access a single object
concurrently should synchronize amongst themselves and provide the
necessary locking. Multiple threads each manipulating separate objects
need not synchronize.

**All Implemented Interfaces:** Cloneable

,

CertPathChecker

---

### Field Details

*No entries found.*

### Constructor Details

#### protected PKIXRevocationChecker()

Default constructor.

---

### Method Details

#### public void setOcspResponder​(
URI
uri)

Sets the URI that identifies the location of the OCSP responder. This
overrides the

ocsp.responderURL

security property and any
responder specified in a certificate's Authority Information Access
Extension, as defined in RFC 5280.

**Parameters:**
- uri

- the responder URI

---

#### public
URI
getOcspResponder()

Gets the URI that identifies the location of the OCSP responder. This
overrides the

ocsp.responderURL

security property. If this
parameter or the

ocsp.responderURL

property is not set, the
location is determined from the certificate's Authority Information
Access Extension, as defined in RFC 5280.

**Returns:**
- the responder URI, or

null

if not set

---

#### public void setOcspResponderCert​(
X509Certificate
cert)

Sets the OCSP responder's certificate. This overrides the

ocsp.responderCertSubjectName

,

ocsp.responderCertIssuerName

,
and

ocsp.responderCertSerialNumber

security properties.

**Parameters:**
- cert

- the responder's certificate

---

#### public
X509Certificate
getOcspResponderCert()

Gets the OCSP responder's certificate. This overrides the

ocsp.responderCertSubjectName

,

ocsp.responderCertIssuerName

,
and

ocsp.responderCertSerialNumber

security properties. If this
parameter or the aforementioned properties are not set, then the
responder's certificate is determined as specified in RFC 2560.

**Returns:**
- the responder's certificate, or

null

if not set

---

#### public void setOcspExtensions​(
List
<
Extension
> extensions)

Sets the optional OCSP request extensions.

**Parameters:**
- extensions

- a list of extensions. The list is copied to protect
against subsequent modification.

---

#### public
List
<
Extension
> getOcspExtensions()

Gets the optional OCSP request extensions.

**Returns:**
- an unmodifiable list of extensions. The list is empty if no
extensions have been specified.

---

#### public void setOcspResponses​(
Map
<
X509Certificate
,​byte[]> responses)

Sets the OCSP responses. These responses are used to determine
the revocation status of the specified certificates when OCSP is used.

**Parameters:**
- responses

- a map of OCSP responses. Each key is an

X509Certificate

that maps to the corresponding
DER-encoded OCSP response for that certificate. A deep copy of
the map is performed to protect against subsequent modification.

---

#### public
Map
<
X509Certificate
,​byte[]> getOcspResponses()

Gets the OCSP responses. These responses are used to determine
the revocation status of the specified certificates when OCSP is used.

**Returns:**
- a map of OCSP responses. Each key is an

X509Certificate

that maps to the corresponding
DER-encoded OCSP response for that certificate. A deep copy of
the map is returned to protect against subsequent modification.
Returns an empty map if no responses have been specified.

---

#### public void setOptions​(
Set
<
PKIXRevocationChecker.Option
> options)

Sets the revocation options.

**Parameters:**
- options

- a set of revocation options. The set is copied to protect
against subsequent modification.

---

#### public
Set
<
PKIXRevocationChecker.Option
> getOptions()

Gets the revocation options.

**Returns:**
- an unmodifiable set of revocation options. The set is empty if
no options have been specified.

---

#### public abstract
List
<
CertPathValidatorException
> getSoftFailExceptions()

Returns a list containing the exceptions that are ignored by the
revocation checker when the

SOFT_FAIL

option
is set. The list is cleared each time

init

is called.
The list is ordered in ascending order according to the certificate
index returned by

getIndex

method of each entry.

An implementation of

PKIXRevocationChecker

is responsible for
adding the ignored exceptions to the list.

**Returns:**
- an unmodifiable list containing the ignored exceptions. The list
is empty if no exceptions have been ignored.

---

### Additional Sections

#### Class PKIXRevocationChecker

java.lang.Object

- java.security.cert.PKIXCertPathChecker
- - java.security.cert.PKIXRevocationChecker

java.security.cert.PKIXCertPathChecker

- java.security.cert.PKIXRevocationChecker

java.security.cert.PKIXRevocationChecker

**All Implemented Interfaces:** Cloneable

,

CertPathChecker

```java
public abstract class
PKIXRevocationChecker

extends
PKIXCertPathChecker
```

A

PKIXCertPathChecker

for checking the revocation status of
certificates with the PKIX algorithm.

A

PKIXRevocationChecker

checks the revocation status of
certificates with the Online Certificate Status Protocol (OCSP) or
Certificate Revocation Lists (CRLs). OCSP is described in RFC 2560 and
is a network protocol for determining the status of a certificate. A CRL
is a time-stamped list identifying revoked certificates, and RFC 5280
describes an algorithm for determining the revocation status of certificates
using CRLs.

Each

PKIXRevocationChecker

must be able to check the revocation
status of certificates with OCSP and CRLs. By default, OCSP is the
preferred mechanism for checking revocation status, with CRLs as the
fallback mechanism. However, this preference can be switched to CRLs with
the

PREFER_CRLS

option. In addition, the fallback
mechanism can be disabled with the

NO_FALLBACK

option.

A

PKIXRevocationChecker

is obtained by calling the

getRevocationChecker

method
of a PKIX

CertPathValidator

. Additional parameters and options
specific to revocation can be set (by calling the

setOcspResponder

method for instance). The

PKIXRevocationChecker

is added to a

PKIXParameters

object
using the

addCertPathChecker

or

setCertPathCheckers

method,
and then the

PKIXParameters

is passed along with the

CertPath

to be validated to the

validate

method
of a PKIX

CertPathValidator

. When supplying a revocation checker in
this manner, it will be used to check revocation irrespective of the setting
of the

RevocationEnabled

flag.
Similarly, a

PKIXRevocationChecker

may be added to a

PKIXBuilderParameters

object for use with a PKIX

CertPathBuilder

.

Note that when a

PKIXRevocationChecker

is added to

PKIXParameters

, it clones the

PKIXRevocationChecker

;
thus any subsequent modifications to the

PKIXRevocationChecker

have no effect.

Any parameter that is not set (or is set to

null

) will be set to
the default value for that parameter.

Concurrent Access

Unless otherwise specified, the methods defined in this class are not
thread-safe. Multiple threads that need to access a single object
concurrently should synchronize amongst themselves and provide the
necessary locking. Multiple threads each manipulating separate objects
need not synchronize.

**Since:** 1.8
**See Also:** RFC 2560: X.509
Internet Public Key Infrastructure Online Certificate Status Protocol -
OCSP

,

RFC 5280: Internet X.509
Public Key Infrastructure Certificate and Certificate Revocation List (CRL)
Profile

public abstract class

PKIXRevocationChecker

extends

PKIXCertPathChecker

A

PKIXCertPathChecker

for checking the revocation status of
certificates with the PKIX algorithm.

A

PKIXRevocationChecker

checks the revocation status of
certificates with the Online Certificate Status Protocol (OCSP) or
Certificate Revocation Lists (CRLs). OCSP is described in RFC 2560 and
is a network protocol for determining the status of a certificate. A CRL
is a time-stamped list identifying revoked certificates, and RFC 5280
describes an algorithm for determining the revocation status of certificates
using CRLs.

Each

PKIXRevocationChecker

must be able to check the revocation
status of certificates with OCSP and CRLs. By default, OCSP is the
preferred mechanism for checking revocation status, with CRLs as the
fallback mechanism. However, this preference can be switched to CRLs with
the

PREFER_CRLS

option. In addition, the fallback
mechanism can be disabled with the

NO_FALLBACK

option.

A

PKIXRevocationChecker

is obtained by calling the

getRevocationChecker

method
of a PKIX

CertPathValidator

. Additional parameters and options
specific to revocation can be set (by calling the

setOcspResponder

method for instance). The

PKIXRevocationChecker

is added to a

PKIXParameters

object
using the

addCertPathChecker

or

setCertPathCheckers

method,
and then the

PKIXParameters

is passed along with the

CertPath

to be validated to the

validate

method
of a PKIX

CertPathValidator

. When supplying a revocation checker in
this manner, it will be used to check revocation irrespective of the setting
of the

RevocationEnabled

flag.
Similarly, a

PKIXRevocationChecker

may be added to a

PKIXBuilderParameters

object for use with a PKIX

CertPathBuilder

.

Note that when a

PKIXRevocationChecker

is added to

PKIXParameters

, it clones the

PKIXRevocationChecker

;
thus any subsequent modifications to the

PKIXRevocationChecker

have no effect.

Any parameter that is not set (or is set to

null

) will be set to
the default value for that parameter.

Concurrent Access

Unless otherwise specified, the methods defined in this class are not
thread-safe. Multiple threads that need to access a single object
concurrently should synchronize amongst themselves and provide the
necessary locking. Multiple threads each manipulating separate objects
need not synchronize.

A

PKIXRevocationChecker

checks the revocation status of
certificates with the Online Certificate Status Protocol (OCSP) or
Certificate Revocation Lists (CRLs). OCSP is described in RFC 2560 and
is a network protocol for determining the status of a certificate. A CRL
is a time-stamped list identifying revoked certificates, and RFC 5280
describes an algorithm for determining the revocation status of certificates
using CRLs.

Each

PKIXRevocationChecker

must be able to check the revocation
status of certificates with OCSP and CRLs. By default, OCSP is the
preferred mechanism for checking revocation status, with CRLs as the
fallback mechanism. However, this preference can be switched to CRLs with
the

PREFER_CRLS

option. In addition, the fallback
mechanism can be disabled with the

NO_FALLBACK

option.

A

PKIXRevocationChecker

is obtained by calling the

getRevocationChecker

method
of a PKIX

CertPathValidator

. Additional parameters and options
specific to revocation can be set (by calling the

setOcspResponder

method for instance). The

PKIXRevocationChecker

is added to a

PKIXParameters

object
using the

addCertPathChecker

or

setCertPathCheckers

method,
and then the

PKIXParameters

is passed along with the

CertPath

to be validated to the

validate

method
of a PKIX

CertPathValidator

. When supplying a revocation checker in
this manner, it will be used to check revocation irrespective of the setting
of the

RevocationEnabled

flag.
Similarly, a

PKIXRevocationChecker

may be added to a

PKIXBuilderParameters

object for use with a PKIX

CertPathBuilder

.

Note that when a

PKIXRevocationChecker

is added to

PKIXParameters

, it clones the

PKIXRevocationChecker

;
thus any subsequent modifications to the

PKIXRevocationChecker

have no effect.

Any parameter that is not set (or is set to

null

) will be set to
the default value for that parameter.

Concurrent Access

Unless otherwise specified, the methods defined in this class are not
thread-safe. Multiple threads that need to access a single object
concurrently should synchronize amongst themselves and provide the
necessary locking. Multiple threads each manipulating separate objects
need not synchronize.

Each

PKIXRevocationChecker

must be able to check the revocation
status of certificates with OCSP and CRLs. By default, OCSP is the
preferred mechanism for checking revocation status, with CRLs as the
fallback mechanism. However, this preference can be switched to CRLs with
the

PREFER_CRLS

option. In addition, the fallback
mechanism can be disabled with the

NO_FALLBACK

option.

A

PKIXRevocationChecker

is obtained by calling the

getRevocationChecker

method
of a PKIX

CertPathValidator

. Additional parameters and options
specific to revocation can be set (by calling the

setOcspResponder

method for instance). The

PKIXRevocationChecker

is added to a

PKIXParameters

object
using the

addCertPathChecker

or

setCertPathCheckers

method,
and then the

PKIXParameters

is passed along with the

CertPath

to be validated to the

validate

method
of a PKIX

CertPathValidator

. When supplying a revocation checker in
this manner, it will be used to check revocation irrespective of the setting
of the

RevocationEnabled

flag.
Similarly, a

PKIXRevocationChecker

may be added to a

PKIXBuilderParameters

object for use with a PKIX

CertPathBuilder

.

Note that when a

PKIXRevocationChecker

is added to

PKIXParameters

, it clones the

PKIXRevocationChecker

;
thus any subsequent modifications to the

PKIXRevocationChecker

have no effect.

Any parameter that is not set (or is set to

null

) will be set to
the default value for that parameter.

Concurrent Access

Unless otherwise specified, the methods defined in this class are not
thread-safe. Multiple threads that need to access a single object
concurrently should synchronize amongst themselves and provide the
necessary locking. Multiple threads each manipulating separate objects
need not synchronize.

A

PKIXRevocationChecker

is obtained by calling the

getRevocationChecker

method
of a PKIX

CertPathValidator

. Additional parameters and options
specific to revocation can be set (by calling the

setOcspResponder

method for instance). The

PKIXRevocationChecker

is added to a

PKIXParameters

object
using the

addCertPathChecker

or

setCertPathCheckers

method,
and then the

PKIXParameters

is passed along with the

CertPath

to be validated to the

validate

method
of a PKIX

CertPathValidator

. When supplying a revocation checker in
this manner, it will be used to check revocation irrespective of the setting
of the

RevocationEnabled

flag.
Similarly, a

PKIXRevocationChecker

may be added to a

PKIXBuilderParameters

object for use with a PKIX

CertPathBuilder

.

Note that when a

PKIXRevocationChecker

is added to

PKIXParameters

, it clones the

PKIXRevocationChecker

;
thus any subsequent modifications to the

PKIXRevocationChecker

have no effect.

Any parameter that is not set (or is set to

null

) will be set to
the default value for that parameter.

Concurrent Access

Unless otherwise specified, the methods defined in this class are not
thread-safe. Multiple threads that need to access a single object
concurrently should synchronize amongst themselves and provide the
necessary locking. Multiple threads each manipulating separate objects
need not synchronize.

Note that when a

PKIXRevocationChecker

is added to

PKIXParameters

, it clones the

PKIXRevocationChecker

;
thus any subsequent modifications to the

PKIXRevocationChecker

have no effect.

Any parameter that is not set (or is set to

null

) will be set to
the default value for that parameter.

Concurrent Access

Unless otherwise specified, the methods defined in this class are not
thread-safe. Multiple threads that need to access a single object
concurrently should synchronize amongst themselves and provide the
necessary locking. Multiple threads each manipulating separate objects
need not synchronize.

Any parameter that is not set (or is set to

null

) will be set to
the default value for that parameter.

Concurrent Access

Unless otherwise specified, the methods defined in this class are not
thread-safe. Multiple threads that need to access a single object
concurrently should synchronize amongst themselves and provide the
necessary locking. Multiple threads each manipulating separate objects
need not synchronize.

Concurrent Access

Unless otherwise specified, the methods defined in this class are not
thread-safe. Multiple threads that need to access a single object
concurrently should synchronize amongst themselves and provide the
necessary locking. Multiple threads each manipulating separate objects
need not synchronize.

Unless otherwise specified, the methods defined in this class are not
thread-safe. Multiple threads that need to access a single object
concurrently should synchronize amongst themselves and provide the
necessary locking. Multiple threads each manipulating separate objects
need not synchronize.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

PKIXRevocationChecker.Option

Various revocation options that can be specified for the revocation
checking mechanism.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

PKIXRevocationChecker

()

Default constructor.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

List

<

Extension

>

getOcspExtensions

()

Gets the optional OCSP request extensions.

URI

getOcspResponder

()

Gets the URI that identifies the location of the OCSP responder.

X509Certificate

getOcspResponderCert

()

Gets the OCSP responder's certificate.

Map

<

X509Certificate

,​byte[]>

getOcspResponses

()

Gets the OCSP responses.

Set

<

PKIXRevocationChecker.Option

>

getOptions

()

Gets the revocation options.

abstract

List

<

CertPathValidatorException

>

getSoftFailExceptions

()

Returns a list containing the exceptions that are ignored by the
revocation checker when the

SOFT_FAIL

option
is set.

void

setOcspExtensions

​(

List

<

Extension

> extensions)

Sets the optional OCSP request extensions.

void

setOcspResponder

​(

URI

uri)

Sets the URI that identifies the location of the OCSP responder.

void

setOcspResponderCert

​(

X509Certificate

cert)

Sets the OCSP responder's certificate.

void

setOcspResponses

​(

Map

<

X509Certificate

,​byte[]> responses)

Sets the OCSP responses.

void

setOptions

​(

Set

<

PKIXRevocationChecker.Option

> options)

Sets the revocation options.

- Methods declared in class java.security.cert.

PKIXCertPathChecker

check

,

check

,

clone

,

getSupportedExtensions

,

init

,

isForwardCheckingSupported

- Methods declared in class java.lang.

Object

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

PKIXRevocationChecker.Option

Various revocation options that can be specified for the revocation
checking mechanism.

---

#### Nested Class Summary

Various revocation options that can be specified for the revocation
checking mechanism.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

PKIXRevocationChecker

()

Default constructor.

---

#### Constructor Summary

Default constructor.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

List

<

Extension

>

getOcspExtensions

()

Gets the optional OCSP request extensions.

URI

getOcspResponder

()

Gets the URI that identifies the location of the OCSP responder.

X509Certificate

getOcspResponderCert

()

Gets the OCSP responder's certificate.

Map

<

X509Certificate

,​byte[]>

getOcspResponses

()

Gets the OCSP responses.

Set

<

PKIXRevocationChecker.Option

>

getOptions

()

Gets the revocation options.

abstract

List

<

CertPathValidatorException

>

getSoftFailExceptions

()

Returns a list containing the exceptions that are ignored by the
revocation checker when the

SOFT_FAIL

option
is set.

void

setOcspExtensions

​(

List

<

Extension

> extensions)

Sets the optional OCSP request extensions.

void

setOcspResponder

​(

URI

uri)

Sets the URI that identifies the location of the OCSP responder.

void

setOcspResponderCert

​(

X509Certificate

cert)

Sets the OCSP responder's certificate.

void

setOcspResponses

​(

Map

<

X509Certificate

,​byte[]> responses)

Sets the OCSP responses.

void

setOptions

​(

Set

<

PKIXRevocationChecker.Option

> options)

Sets the revocation options.

- Methods declared in class java.security.cert.

PKIXCertPathChecker

check

,

check

,

clone

,

getSupportedExtensions

,

init

,

isForwardCheckingSupported

- Methods declared in class java.lang.

Object

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

Gets the optional OCSP request extensions.

Gets the URI that identifies the location of the OCSP responder.

Gets the OCSP responder's certificate.

Gets the OCSP responses.

Gets the revocation options.

Returns a list containing the exceptions that are ignored by the
revocation checker when the

SOFT_FAIL

option
is set.

Sets the optional OCSP request extensions.

Sets the URI that identifies the location of the OCSP responder.

Sets the OCSP responder's certificate.

Sets the OCSP responses.

Sets the revocation options.

Methods declared in class java.security.cert.

PKIXCertPathChecker

check

,

check

,

clone

,

getSupportedExtensions

,

init

,

isForwardCheckingSupported

---

#### Methods declared in class java.security.cert. PKIXCertPathChecker

Methods declared in class java.lang.

Object

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

- PKIXRevocationChecker

```java
protected PKIXRevocationChecker()
```

Default constructor.

============ METHOD DETAIL ==========

- Method Detail

- setOcspResponder

```java
public void setOcspResponder​(
URI
uri)
```

Sets the URI that identifies the location of the OCSP responder. This
overrides the

ocsp.responderURL

security property and any
responder specified in a certificate's Authority Information Access
Extension, as defined in RFC 5280.

**Parameters:** uri

- the responder URI

- getOcspResponder

```java
public
URI
getOcspResponder()
```

Gets the URI that identifies the location of the OCSP responder. This
overrides the

ocsp.responderURL

security property. If this
parameter or the

ocsp.responderURL

property is not set, the
location is determined from the certificate's Authority Information
Access Extension, as defined in RFC 5280.

**Returns:** the responder URI, or

null

if not set

- setOcspResponderCert

```java
public void setOcspResponderCert​(
X509Certificate
cert)
```

Sets the OCSP responder's certificate. This overrides the

ocsp.responderCertSubjectName

,

ocsp.responderCertIssuerName

,
and

ocsp.responderCertSerialNumber

security properties.

**Parameters:** cert

- the responder's certificate

- getOcspResponderCert

```java
public
X509Certificate
getOcspResponderCert()
```

Gets the OCSP responder's certificate. This overrides the

ocsp.responderCertSubjectName

,

ocsp.responderCertIssuerName

,
and

ocsp.responderCertSerialNumber

security properties. If this
parameter or the aforementioned properties are not set, then the
responder's certificate is determined as specified in RFC 2560.

**Returns:** the responder's certificate, or

null

if not set

- setOcspExtensions

```java
public void setOcspExtensions​(
List
<
Extension
> extensions)
```

Sets the optional OCSP request extensions.

**Parameters:** extensions

- a list of extensions. The list is copied to protect
against subsequent modification.

- getOcspExtensions

```java
public
List
<
Extension
> getOcspExtensions()
```

Gets the optional OCSP request extensions.

**Returns:** an unmodifiable list of extensions. The list is empty if no
extensions have been specified.

- setOcspResponses

```java
public void setOcspResponses​(
Map
<
X509Certificate
,​byte[]> responses)
```

Sets the OCSP responses. These responses are used to determine
the revocation status of the specified certificates when OCSP is used.

**Parameters:** responses

- a map of OCSP responses. Each key is an

X509Certificate

that maps to the corresponding
DER-encoded OCSP response for that certificate. A deep copy of
the map is performed to protect against subsequent modification.

- getOcspResponses

```java
public
Map
<
X509Certificate
,​byte[]> getOcspResponses()
```

Gets the OCSP responses. These responses are used to determine
the revocation status of the specified certificates when OCSP is used.

**Returns:** a map of OCSP responses. Each key is an

X509Certificate

that maps to the corresponding
DER-encoded OCSP response for that certificate. A deep copy of
the map is returned to protect against subsequent modification.
Returns an empty map if no responses have been specified.

- setOptions

```java
public void setOptions​(
Set
<
PKIXRevocationChecker.Option
> options)
```

Sets the revocation options.

**Parameters:** options

- a set of revocation options. The set is copied to protect
against subsequent modification.

- getOptions

```java
public
Set
<
PKIXRevocationChecker.Option
> getOptions()
```

Gets the revocation options.

**Returns:** an unmodifiable set of revocation options. The set is empty if
no options have been specified.

- getSoftFailExceptions

```java
public abstract
List
<
CertPathValidatorException
> getSoftFailExceptions()
```

Returns a list containing the exceptions that are ignored by the
revocation checker when the

SOFT_FAIL

option
is set. The list is cleared each time

init

is called.
The list is ordered in ascending order according to the certificate
index returned by

getIndex

method of each entry.

An implementation of

PKIXRevocationChecker

is responsible for
adding the ignored exceptions to the list.

**Returns:** an unmodifiable list containing the ignored exceptions. The list
is empty if no exceptions have been ignored.

Constructor Detail

- PKIXRevocationChecker

```java
protected PKIXRevocationChecker()
```

Default constructor.

---

#### Constructor Detail

PKIXRevocationChecker

```java
protected PKIXRevocationChecker()
```

Default constructor.

---

#### PKIXRevocationChecker

protected PKIXRevocationChecker()

Default constructor.

Method Detail

- setOcspResponder

```java
public void setOcspResponder​(
URI
uri)
```

Sets the URI that identifies the location of the OCSP responder. This
overrides the

ocsp.responderURL

security property and any
responder specified in a certificate's Authority Information Access
Extension, as defined in RFC 5280.

**Parameters:** uri

- the responder URI

- getOcspResponder

```java
public
URI
getOcspResponder()
```

Gets the URI that identifies the location of the OCSP responder. This
overrides the

ocsp.responderURL

security property. If this
parameter or the

ocsp.responderURL

property is not set, the
location is determined from the certificate's Authority Information
Access Extension, as defined in RFC 5280.

**Returns:** the responder URI, or

null

if not set

- setOcspResponderCert

```java
public void setOcspResponderCert​(
X509Certificate
cert)
```

Sets the OCSP responder's certificate. This overrides the

ocsp.responderCertSubjectName

,

ocsp.responderCertIssuerName

,
and

ocsp.responderCertSerialNumber

security properties.

**Parameters:** cert

- the responder's certificate

- getOcspResponderCert

```java
public
X509Certificate
getOcspResponderCert()
```

Gets the OCSP responder's certificate. This overrides the

ocsp.responderCertSubjectName

,

ocsp.responderCertIssuerName

,
and

ocsp.responderCertSerialNumber

security properties. If this
parameter or the aforementioned properties are not set, then the
responder's certificate is determined as specified in RFC 2560.

**Returns:** the responder's certificate, or

null

if not set

- setOcspExtensions

```java
public void setOcspExtensions​(
List
<
Extension
> extensions)
```

Sets the optional OCSP request extensions.

**Parameters:** extensions

- a list of extensions. The list is copied to protect
against subsequent modification.

- getOcspExtensions

```java
public
List
<
Extension
> getOcspExtensions()
```

Gets the optional OCSP request extensions.

**Returns:** an unmodifiable list of extensions. The list is empty if no
extensions have been specified.

- setOcspResponses

```java
public void setOcspResponses​(
Map
<
X509Certificate
,​byte[]> responses)
```

Sets the OCSP responses. These responses are used to determine
the revocation status of the specified certificates when OCSP is used.

**Parameters:** responses

- a map of OCSP responses. Each key is an

X509Certificate

that maps to the corresponding
DER-encoded OCSP response for that certificate. A deep copy of
the map is performed to protect against subsequent modification.

- getOcspResponses

```java
public
Map
<
X509Certificate
,​byte[]> getOcspResponses()
```

Gets the OCSP responses. These responses are used to determine
the revocation status of the specified certificates when OCSP is used.

**Returns:** a map of OCSP responses. Each key is an

X509Certificate

that maps to the corresponding
DER-encoded OCSP response for that certificate. A deep copy of
the map is returned to protect against subsequent modification.
Returns an empty map if no responses have been specified.

- setOptions

```java
public void setOptions​(
Set
<
PKIXRevocationChecker.Option
> options)
```

Sets the revocation options.

**Parameters:** options

- a set of revocation options. The set is copied to protect
against subsequent modification.

- getOptions

```java
public
Set
<
PKIXRevocationChecker.Option
> getOptions()
```

Gets the revocation options.

**Returns:** an unmodifiable set of revocation options. The set is empty if
no options have been specified.

- getSoftFailExceptions

```java
public abstract
List
<
CertPathValidatorException
> getSoftFailExceptions()
```

Returns a list containing the exceptions that are ignored by the
revocation checker when the

SOFT_FAIL

option
is set. The list is cleared each time

init

is called.
The list is ordered in ascending order according to the certificate
index returned by

getIndex

method of each entry.

An implementation of

PKIXRevocationChecker

is responsible for
adding the ignored exceptions to the list.

**Returns:** an unmodifiable list containing the ignored exceptions. The list
is empty if no exceptions have been ignored.

---

#### Method Detail

setOcspResponder

```java
public void setOcspResponder​(
URI
uri)
```

Sets the URI that identifies the location of the OCSP responder. This
overrides the

ocsp.responderURL

security property and any
responder specified in a certificate's Authority Information Access
Extension, as defined in RFC 5280.

**Parameters:** uri

- the responder URI

---

#### setOcspResponder

public void setOcspResponder​(

URI

uri)

Sets the URI that identifies the location of the OCSP responder. This
overrides the

ocsp.responderURL

security property and any
responder specified in a certificate's Authority Information Access
Extension, as defined in RFC 5280.

getOcspResponder

```java
public
URI
getOcspResponder()
```

Gets the URI that identifies the location of the OCSP responder. This
overrides the

ocsp.responderURL

security property. If this
parameter or the

ocsp.responderURL

property is not set, the
location is determined from the certificate's Authority Information
Access Extension, as defined in RFC 5280.

**Returns:** the responder URI, or

null

if not set

---

#### getOcspResponder

public

URI

getOcspResponder()

Gets the URI that identifies the location of the OCSP responder. This
overrides the

ocsp.responderURL

security property. If this
parameter or the

ocsp.responderURL

property is not set, the
location is determined from the certificate's Authority Information
Access Extension, as defined in RFC 5280.

setOcspResponderCert

```java
public void setOcspResponderCert​(
X509Certificate
cert)
```

Sets the OCSP responder's certificate. This overrides the

ocsp.responderCertSubjectName

,

ocsp.responderCertIssuerName

,
and

ocsp.responderCertSerialNumber

security properties.

**Parameters:** cert

- the responder's certificate

---

#### setOcspResponderCert

public void setOcspResponderCert​(

X509Certificate

cert)

Sets the OCSP responder's certificate. This overrides the

ocsp.responderCertSubjectName

,

ocsp.responderCertIssuerName

,
and

ocsp.responderCertSerialNumber

security properties.

getOcspResponderCert

```java
public
X509Certificate
getOcspResponderCert()
```

Gets the OCSP responder's certificate. This overrides the

ocsp.responderCertSubjectName

,

ocsp.responderCertIssuerName

,
and

ocsp.responderCertSerialNumber

security properties. If this
parameter or the aforementioned properties are not set, then the
responder's certificate is determined as specified in RFC 2560.

**Returns:** the responder's certificate, or

null

if not set

---

#### getOcspResponderCert

public

X509Certificate

getOcspResponderCert()

Gets the OCSP responder's certificate. This overrides the

ocsp.responderCertSubjectName

,

ocsp.responderCertIssuerName

,
and

ocsp.responderCertSerialNumber

security properties. If this
parameter or the aforementioned properties are not set, then the
responder's certificate is determined as specified in RFC 2560.

setOcspExtensions

```java
public void setOcspExtensions​(
List
<
Extension
> extensions)
```

Sets the optional OCSP request extensions.

**Parameters:** extensions

- a list of extensions. The list is copied to protect
against subsequent modification.

---

#### setOcspExtensions

public void setOcspExtensions​(

List

<

Extension

> extensions)

Sets the optional OCSP request extensions.

getOcspExtensions

```java
public
List
<
Extension
> getOcspExtensions()
```

Gets the optional OCSP request extensions.

**Returns:** an unmodifiable list of extensions. The list is empty if no
extensions have been specified.

---

#### getOcspExtensions

public

List

<

Extension

> getOcspExtensions()

Gets the optional OCSP request extensions.

setOcspResponses

```java
public void setOcspResponses​(
Map
<
X509Certificate
,​byte[]> responses)
```

Sets the OCSP responses. These responses are used to determine
the revocation status of the specified certificates when OCSP is used.

**Parameters:** responses

- a map of OCSP responses. Each key is an

X509Certificate

that maps to the corresponding
DER-encoded OCSP response for that certificate. A deep copy of
the map is performed to protect against subsequent modification.

---

#### setOcspResponses

public void setOcspResponses​(

Map

<

X509Certificate

,​byte[]> responses)

Sets the OCSP responses. These responses are used to determine
the revocation status of the specified certificates when OCSP is used.

getOcspResponses

```java
public
Map
<
X509Certificate
,​byte[]> getOcspResponses()
```

Gets the OCSP responses. These responses are used to determine
the revocation status of the specified certificates when OCSP is used.

**Returns:** a map of OCSP responses. Each key is an

X509Certificate

that maps to the corresponding
DER-encoded OCSP response for that certificate. A deep copy of
the map is returned to protect against subsequent modification.
Returns an empty map if no responses have been specified.

---

#### getOcspResponses

public

Map

<

X509Certificate

,​byte[]> getOcspResponses()

Gets the OCSP responses. These responses are used to determine
the revocation status of the specified certificates when OCSP is used.

setOptions

```java
public void setOptions​(
Set
<
PKIXRevocationChecker.Option
> options)
```

Sets the revocation options.

**Parameters:** options

- a set of revocation options. The set is copied to protect
against subsequent modification.

---

#### setOptions

public void setOptions​(

Set

<

PKIXRevocationChecker.Option

> options)

Sets the revocation options.

getOptions

```java
public
Set
<
PKIXRevocationChecker.Option
> getOptions()
```

Gets the revocation options.

**Returns:** an unmodifiable set of revocation options. The set is empty if
no options have been specified.

---

#### getOptions

public

Set

<

PKIXRevocationChecker.Option

> getOptions()

Gets the revocation options.

getSoftFailExceptions

```java
public abstract
List
<
CertPathValidatorException
> getSoftFailExceptions()
```

Returns a list containing the exceptions that are ignored by the
revocation checker when the

SOFT_FAIL

option
is set. The list is cleared each time

init

is called.
The list is ordered in ascending order according to the certificate
index returned by

getIndex

method of each entry.

An implementation of

PKIXRevocationChecker

is responsible for
adding the ignored exceptions to the list.

**Returns:** an unmodifiable list containing the ignored exceptions. The list
is empty if no exceptions have been ignored.

---

#### getSoftFailExceptions

public abstract

List

<

CertPathValidatorException

> getSoftFailExceptions()

Returns a list containing the exceptions that are ignored by the
revocation checker when the

SOFT_FAIL

option
is set. The list is cleared each time

init

is called.
The list is ordered in ascending order according to the certificate
index returned by

getIndex

method of each entry.

An implementation of

PKIXRevocationChecker

is responsible for
adding the ignored exceptions to the list.

An implementation of

PKIXRevocationChecker

is responsible for
adding the ignored exceptions to the list.

---

