# Class PKIXCertPathBuilderResult

**Source:** `java.base\java\security\cert\PKIXCertPathBuilderResult.html`

### Class Description

```java
public class
PKIXCertPathBuilderResult

extends
PKIXCertPathValidatorResult

implements
CertPathBuilderResult
```

This class represents the successful result of the PKIX certification
path builder algorithm. All certification paths that are built and
returned using this algorithm are also validated according to the PKIX
certification path validation algorithm.

Instances of

PKIXCertPathBuilderResult

are returned by
the

build

method of

CertPathBuilder

objects implementing the PKIX algorithm.

All

PKIXCertPathBuilderResult

objects contain the
certification path constructed by the build algorithm, the
valid policy tree and subject public key resulting from the build
algorithm, and a

TrustAnchor

describing the certification
authority (CA) that served as a trust anchor for the certification path.

Concurrent Access

Unless otherwise specified, the methods defined in this class are not
thread-safe. Multiple threads that need to access a single
object concurrently should synchronize amongst themselves and
provide the necessary locking. Multiple threads each manipulating
separate objects need not synchronize.

**All Implemented Interfaces:** Cloneable

,

CertPathBuilderResult

,

CertPathValidatorResult

---

### Field Details

*No entries found.*

### Constructor Details

#### public PKIXCertPathBuilderResult​(
CertPath
certPath,

TrustAnchor
trustAnchor,

PolicyNode
policyTree,

PublicKey
subjectPublicKey)

Creates an instance of

PKIXCertPathBuilderResult

containing the specified parameters.

**Parameters:**
- certPath

- the validated

CertPath
- trustAnchor

- a

TrustAnchor

describing the CA that
served as a trust anchor for the certification path
- policyTree

- the immutable valid policy tree, or

null

if there are no valid policies
- subjectPublicKey

- the public key of the subject

**Throws:**
- NullPointerException

- if the

certPath

,

trustAnchor

or

subjectPublicKey

parameters
are

null

---

### Method Details

#### public
CertPath
getCertPath()

Returns the built and validated certification path. The

CertPath

object does not include the trust anchor.
Instead, use the

getTrustAnchor()

method to
obtain the

TrustAnchor

that served as the trust anchor
for the certification path.

**Specified by:**
- getCertPath

in interface

CertPathBuilderResult

**Returns:**
- the built and validated

CertPath

(never

null

)

---

#### public
String
toString()

Return a printable representation of this

PKIXCertPathBuilderResult

.

**Overrides:**
- toString

in class

PKIXCertPathValidatorResult

**Returns:**
- a

String

describing the contents of this

PKIXCertPathBuilderResult

---

### Additional Sections

#### Class PKIXCertPathBuilderResult

java.lang.Object

- java.security.cert.PKIXCertPathValidatorResult
- - java.security.cert.PKIXCertPathBuilderResult

java.security.cert.PKIXCertPathValidatorResult

- java.security.cert.PKIXCertPathBuilderResult

java.security.cert.PKIXCertPathBuilderResult

**All Implemented Interfaces:** Cloneable

,

CertPathBuilderResult

,

CertPathValidatorResult

```java
public class
PKIXCertPathBuilderResult

extends
PKIXCertPathValidatorResult

implements
CertPathBuilderResult
```

This class represents the successful result of the PKIX certification
path builder algorithm. All certification paths that are built and
returned using this algorithm are also validated according to the PKIX
certification path validation algorithm.

Instances of

PKIXCertPathBuilderResult

are returned by
the

build

method of

CertPathBuilder

objects implementing the PKIX algorithm.

All

PKIXCertPathBuilderResult

objects contain the
certification path constructed by the build algorithm, the
valid policy tree and subject public key resulting from the build
algorithm, and a

TrustAnchor

describing the certification
authority (CA) that served as a trust anchor for the certification path.

Concurrent Access

Unless otherwise specified, the methods defined in this class are not
thread-safe. Multiple threads that need to access a single
object concurrently should synchronize amongst themselves and
provide the necessary locking. Multiple threads each manipulating
separate objects need not synchronize.

**Since:** 1.4
**See Also:** CertPathBuilderResult

public class

PKIXCertPathBuilderResult

extends

PKIXCertPathValidatorResult

implements

CertPathBuilderResult

This class represents the successful result of the PKIX certification
path builder algorithm. All certification paths that are built and
returned using this algorithm are also validated according to the PKIX
certification path validation algorithm.

Instances of

PKIXCertPathBuilderResult

are returned by
the

build

method of

CertPathBuilder

objects implementing the PKIX algorithm.

All

PKIXCertPathBuilderResult

objects contain the
certification path constructed by the build algorithm, the
valid policy tree and subject public key resulting from the build
algorithm, and a

TrustAnchor

describing the certification
authority (CA) that served as a trust anchor for the certification path.

Concurrent Access

Unless otherwise specified, the methods defined in this class are not
thread-safe. Multiple threads that need to access a single
object concurrently should synchronize amongst themselves and
provide the necessary locking. Multiple threads each manipulating
separate objects need not synchronize.

Instances of

PKIXCertPathBuilderResult

are returned by
the

build

method of

CertPathBuilder

objects implementing the PKIX algorithm.

All

PKIXCertPathBuilderResult

objects contain the
certification path constructed by the build algorithm, the
valid policy tree and subject public key resulting from the build
algorithm, and a

TrustAnchor

describing the certification
authority (CA) that served as a trust anchor for the certification path.

Concurrent Access

Unless otherwise specified, the methods defined in this class are not
thread-safe. Multiple threads that need to access a single
object concurrently should synchronize amongst themselves and
provide the necessary locking. Multiple threads each manipulating
separate objects need not synchronize.

All

PKIXCertPathBuilderResult

objects contain the
certification path constructed by the build algorithm, the
valid policy tree and subject public key resulting from the build
algorithm, and a

TrustAnchor

describing the certification
authority (CA) that served as a trust anchor for the certification path.

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

PKIXCertPathBuilderResult

​(

CertPath

certPath,

TrustAnchor

trustAnchor,

PolicyNode

policyTree,

PublicKey

subjectPublicKey)

Creates an instance of

PKIXCertPathBuilderResult

containing the specified parameters.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

CertPath

getCertPath

()

Returns the built and validated certification path.

String

toString

()

Return a printable representation of this

PKIXCertPathBuilderResult

.

- Methods declared in class java.security.cert.

PKIXCertPathValidatorResult

clone

,

getPolicyTree

,

getPublicKey

,

getTrustAnchor

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

wait

,

wait

,

wait

- Methods declared in interface java.security.cert.

CertPathBuilderResult

clone

Constructor Summary

Constructors

Constructor

Description

PKIXCertPathBuilderResult

​(

CertPath

certPath,

TrustAnchor

trustAnchor,

PolicyNode

policyTree,

PublicKey

subjectPublicKey)

Creates an instance of

PKIXCertPathBuilderResult

containing the specified parameters.

---

#### Constructor Summary

Creates an instance of

PKIXCertPathBuilderResult

containing the specified parameters.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

CertPath

getCertPath

()

Returns the built and validated certification path.

String

toString

()

Return a printable representation of this

PKIXCertPathBuilderResult

.

- Methods declared in class java.security.cert.

PKIXCertPathValidatorResult

clone

,

getPolicyTree

,

getPublicKey

,

getTrustAnchor

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

wait

,

wait

,

wait

- Methods declared in interface java.security.cert.

CertPathBuilderResult

clone

---

#### Method Summary

Returns the built and validated certification path.

Return a printable representation of this

PKIXCertPathBuilderResult

.

Methods declared in class java.security.cert.

PKIXCertPathValidatorResult

clone

,

getPolicyTree

,

getPublicKey

,

getTrustAnchor

---

#### Methods declared in class java.security.cert. PKIXCertPathValidatorResult

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

Methods declared in interface java.security.cert.

CertPathBuilderResult

clone

---

#### Methods declared in interface java.security.cert. CertPathBuilderResult

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- PKIXCertPathBuilderResult

```java
public PKIXCertPathBuilderResult​(
CertPath
certPath,

TrustAnchor
trustAnchor,

PolicyNode
policyTree,

PublicKey
subjectPublicKey)
```

Creates an instance of

PKIXCertPathBuilderResult

containing the specified parameters.

**Parameters:** certPath

- the validated

CertPath
**Parameters:** trustAnchor

- a

TrustAnchor

describing the CA that
served as a trust anchor for the certification path
**Parameters:** policyTree

- the immutable valid policy tree, or

null

if there are no valid policies
**Parameters:** subjectPublicKey

- the public key of the subject
**Throws:** NullPointerException

- if the

certPath

,

trustAnchor

or

subjectPublicKey

parameters
are

null

============ METHOD DETAIL ==========

- Method Detail

- getCertPath

```java
public
CertPath
getCertPath()
```

Returns the built and validated certification path. The

CertPath

object does not include the trust anchor.
Instead, use the

getTrustAnchor()

method to
obtain the

TrustAnchor

that served as the trust anchor
for the certification path.

**Specified by:** getCertPath

in interface

CertPathBuilderResult
**Returns:** the built and validated

CertPath

(never

null

)

- toString

```java
public
String
toString()
```

Return a printable representation of this

PKIXCertPathBuilderResult

.

**Overrides:** toString

in class

PKIXCertPathValidatorResult
**Returns:** a

String

describing the contents of this

PKIXCertPathBuilderResult

Constructor Detail

- PKIXCertPathBuilderResult

```java
public PKIXCertPathBuilderResult​(
CertPath
certPath,

TrustAnchor
trustAnchor,

PolicyNode
policyTree,

PublicKey
subjectPublicKey)
```

Creates an instance of

PKIXCertPathBuilderResult

containing the specified parameters.

**Parameters:** certPath

- the validated

CertPath
**Parameters:** trustAnchor

- a

TrustAnchor

describing the CA that
served as a trust anchor for the certification path
**Parameters:** policyTree

- the immutable valid policy tree, or

null

if there are no valid policies
**Parameters:** subjectPublicKey

- the public key of the subject
**Throws:** NullPointerException

- if the

certPath

,

trustAnchor

or

subjectPublicKey

parameters
are

null

---

#### Constructor Detail

PKIXCertPathBuilderResult

```java
public PKIXCertPathBuilderResult​(
CertPath
certPath,

TrustAnchor
trustAnchor,

PolicyNode
policyTree,

PublicKey
subjectPublicKey)
```

Creates an instance of

PKIXCertPathBuilderResult

containing the specified parameters.

**Parameters:** certPath

- the validated

CertPath
**Parameters:** trustAnchor

- a

TrustAnchor

describing the CA that
served as a trust anchor for the certification path
**Parameters:** policyTree

- the immutable valid policy tree, or

null

if there are no valid policies
**Parameters:** subjectPublicKey

- the public key of the subject
**Throws:** NullPointerException

- if the

certPath

,

trustAnchor

or

subjectPublicKey

parameters
are

null

---

#### PKIXCertPathBuilderResult

public PKIXCertPathBuilderResult​(

CertPath

certPath,

TrustAnchor

trustAnchor,

PolicyNode

policyTree,

PublicKey

subjectPublicKey)

Creates an instance of

PKIXCertPathBuilderResult

containing the specified parameters.

Method Detail

- getCertPath

```java
public
CertPath
getCertPath()
```

Returns the built and validated certification path. The

CertPath

object does not include the trust anchor.
Instead, use the

getTrustAnchor()

method to
obtain the

TrustAnchor

that served as the trust anchor
for the certification path.

**Specified by:** getCertPath

in interface

CertPathBuilderResult
**Returns:** the built and validated

CertPath

(never

null

)

- toString

```java
public
String
toString()
```

Return a printable representation of this

PKIXCertPathBuilderResult

.

**Overrides:** toString

in class

PKIXCertPathValidatorResult
**Returns:** a

String

describing the contents of this

PKIXCertPathBuilderResult

---

#### Method Detail

getCertPath

```java
public
CertPath
getCertPath()
```

Returns the built and validated certification path. The

CertPath

object does not include the trust anchor.
Instead, use the

getTrustAnchor()

method to
obtain the

TrustAnchor

that served as the trust anchor
for the certification path.

**Specified by:** getCertPath

in interface

CertPathBuilderResult
**Returns:** the built and validated

CertPath

(never

null

)

---

#### getCertPath

public

CertPath

getCertPath()

Returns the built and validated certification path. The

CertPath

object does not include the trust anchor.
Instead, use the

getTrustAnchor()

method to
obtain the

TrustAnchor

that served as the trust anchor
for the certification path.

toString

```java
public
String
toString()
```

Return a printable representation of this

PKIXCertPathBuilderResult

.

**Overrides:** toString

in class

PKIXCertPathValidatorResult
**Returns:** a

String

describing the contents of this

PKIXCertPathBuilderResult

---

#### toString

public

String

toString()

Return a printable representation of this

PKIXCertPathBuilderResult

.

---

