# Class PKIXCertPathValidatorResult

**Source:** `java.base\java\security\cert\PKIXCertPathValidatorResult.html`

### Class Description

```java
public class
PKIXCertPathValidatorResult

extends
Object

implements
CertPathValidatorResult
```

This class represents the successful result of the PKIX certification
path validation algorithm.

Instances of

PKIXCertPathValidatorResult

are returned by the

validate

method of

CertPathValidator

objects implementing the PKIX algorithm.

All

PKIXCertPathValidatorResult

objects contain the
valid policy tree and subject public key resulting from the
validation algorithm, as well as a

TrustAnchor

describing
the certification authority (CA) that served as a trust anchor for the
certification path.

Concurrent Access

Unless otherwise specified, the methods defined in this class are not
thread-safe. Multiple threads that need to access a single
object concurrently should synchronize amongst themselves and
provide the necessary locking. Multiple threads each manipulating
separate objects need not synchronize.

**All Implemented Interfaces:** Cloneable

,

CertPathValidatorResult

---

### Field Details

*No entries found.*

### Constructor Details

#### public PKIXCertPathValidatorResult​(
TrustAnchor
trustAnchor,

PolicyNode
policyTree,

PublicKey
subjectPublicKey)

Creates an instance of

PKIXCertPathValidatorResult

containing the specified parameters.

**Parameters:**
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

subjectPublicKey

or

trustAnchor

parameters are

null

---

### Method Details

#### public
TrustAnchor
getTrustAnchor()

Returns the

TrustAnchor

describing the CA that served
as a trust anchor for the certification path.

**Returns:**
- the

TrustAnchor

(never

null

)

---

#### public
PolicyNode
getPolicyTree()

Returns the root node of the valid policy tree resulting from the
PKIX certification path validation algorithm. The

PolicyNode

object that is returned and any objects that
it returns through public methods are immutable.

Most applications will not need to examine the valid policy tree.
They can achieve their policy processing goals by setting the
policy-related parameters in

PKIXParameters

. However, more
sophisticated applications, especially those that process policy
qualifiers, may need to traverse the valid policy tree using the

PolicyNode.getParent

and

PolicyNode.getChildren

methods.

**Returns:**
- the root node of the valid policy tree, or

null

if there are no valid policies

---

#### public
PublicKey
getPublicKey()

Returns the public key of the subject (target) of the certification
path, including any inherited public key parameters if applicable.

**Returns:**
- the public key of the subject (never

null

)

---

#### public
Object
clone()

Returns a copy of this object.

**Specified by:**
- clone

in interface

CertPathValidatorResult

**Overrides:**
- clone

in class

Object

**Returns:**
- the copy

**See Also:**
- Cloneable

---

#### public
String
toString()

Return a printable representation of this

PKIXCertPathValidatorResult

.

**Overrides:**
- toString

in class

Object

**Returns:**
- a

String

describing the contents of this

PKIXCertPathValidatorResult

---

### Additional Sections

#### Class PKIXCertPathValidatorResult

java.lang.Object

- java.security.cert.PKIXCertPathValidatorResult

java.security.cert.PKIXCertPathValidatorResult

**All Implemented Interfaces:** Cloneable

,

CertPathValidatorResult

**Direct Known Subclasses:** PKIXCertPathBuilderResult

```java
public class
PKIXCertPathValidatorResult

extends
Object

implements
CertPathValidatorResult
```

This class represents the successful result of the PKIX certification
path validation algorithm.

Instances of

PKIXCertPathValidatorResult

are returned by the

validate

method of

CertPathValidator

objects implementing the PKIX algorithm.

All

PKIXCertPathValidatorResult

objects contain the
valid policy tree and subject public key resulting from the
validation algorithm, as well as a

TrustAnchor

describing
the certification authority (CA) that served as a trust anchor for the
certification path.

Concurrent Access

Unless otherwise specified, the methods defined in this class are not
thread-safe. Multiple threads that need to access a single
object concurrently should synchronize amongst themselves and
provide the necessary locking. Multiple threads each manipulating
separate objects need not synchronize.

**Since:** 1.4
**See Also:** CertPathValidatorResult

public class

PKIXCertPathValidatorResult

extends

Object

implements

CertPathValidatorResult

This class represents the successful result of the PKIX certification
path validation algorithm.

Instances of

PKIXCertPathValidatorResult

are returned by the

validate

method of

CertPathValidator

objects implementing the PKIX algorithm.

All

PKIXCertPathValidatorResult

objects contain the
valid policy tree and subject public key resulting from the
validation algorithm, as well as a

TrustAnchor

describing
the certification authority (CA) that served as a trust anchor for the
certification path.

Concurrent Access

Unless otherwise specified, the methods defined in this class are not
thread-safe. Multiple threads that need to access a single
object concurrently should synchronize amongst themselves and
provide the necessary locking. Multiple threads each manipulating
separate objects need not synchronize.

Instances of

PKIXCertPathValidatorResult

are returned by the

validate

method of

CertPathValidator

objects implementing the PKIX algorithm.

All

PKIXCertPathValidatorResult

objects contain the
valid policy tree and subject public key resulting from the
validation algorithm, as well as a

TrustAnchor

describing
the certification authority (CA) that served as a trust anchor for the
certification path.

Concurrent Access

Unless otherwise specified, the methods defined in this class are not
thread-safe. Multiple threads that need to access a single
object concurrently should synchronize amongst themselves and
provide the necessary locking. Multiple threads each manipulating
separate objects need not synchronize.

All

PKIXCertPathValidatorResult

objects contain the
valid policy tree and subject public key resulting from the
validation algorithm, as well as a

TrustAnchor

describing
the certification authority (CA) that served as a trust anchor for the
certification path.

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

PKIXCertPathValidatorResult

​(

TrustAnchor

trustAnchor,

PolicyNode

policyTree,

PublicKey

subjectPublicKey)

Creates an instance of

PKIXCertPathValidatorResult

containing the specified parameters.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Returns a copy of this object.

PolicyNode

getPolicyTree

()

Returns the root node of the valid policy tree resulting from the
PKIX certification path validation algorithm.

PublicKey

getPublicKey

()

Returns the public key of the subject (target) of the certification
path, including any inherited public key parameters if applicable.

TrustAnchor

getTrustAnchor

()

Returns the

TrustAnchor

describing the CA that served
as a trust anchor for the certification path.

String

toString

()

Return a printable representation of this

PKIXCertPathValidatorResult

.

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

Constructor Summary

Constructors

Constructor

Description

PKIXCertPathValidatorResult

​(

TrustAnchor

trustAnchor,

PolicyNode

policyTree,

PublicKey

subjectPublicKey)

Creates an instance of

PKIXCertPathValidatorResult

containing the specified parameters.

---

#### Constructor Summary

Creates an instance of

PKIXCertPathValidatorResult

containing the specified parameters.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Returns a copy of this object.

PolicyNode

getPolicyTree

()

Returns the root node of the valid policy tree resulting from the
PKIX certification path validation algorithm.

PublicKey

getPublicKey

()

Returns the public key of the subject (target) of the certification
path, including any inherited public key parameters if applicable.

TrustAnchor

getTrustAnchor

()

Returns the

TrustAnchor

describing the CA that served
as a trust anchor for the certification path.

String

toString

()

Return a printable representation of this

PKIXCertPathValidatorResult

.

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

---

#### Method Summary

Returns a copy of this object.

Returns the root node of the valid policy tree resulting from the
PKIX certification path validation algorithm.

Returns the public key of the subject (target) of the certification
path, including any inherited public key parameters if applicable.

Returns the

TrustAnchor

describing the CA that served
as a trust anchor for the certification path.

Return a printable representation of this

PKIXCertPathValidatorResult

.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- PKIXCertPathValidatorResult

```java
public PKIXCertPathValidatorResult​(
TrustAnchor
trustAnchor,

PolicyNode
policyTree,

PublicKey
subjectPublicKey)
```

Creates an instance of

PKIXCertPathValidatorResult

containing the specified parameters.

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

subjectPublicKey

or

trustAnchor

parameters are

null

============ METHOD DETAIL ==========

- Method Detail

- getTrustAnchor

```java
public
TrustAnchor
getTrustAnchor()
```

Returns the

TrustAnchor

describing the CA that served
as a trust anchor for the certification path.

**Returns:** the

TrustAnchor

(never

null

)

- getPolicyTree

```java
public
PolicyNode
getPolicyTree()
```

Returns the root node of the valid policy tree resulting from the
PKIX certification path validation algorithm. The

PolicyNode

object that is returned and any objects that
it returns through public methods are immutable.

Most applications will not need to examine the valid policy tree.
They can achieve their policy processing goals by setting the
policy-related parameters in

PKIXParameters

. However, more
sophisticated applications, especially those that process policy
qualifiers, may need to traverse the valid policy tree using the

PolicyNode.getParent

and

PolicyNode.getChildren

methods.

**Returns:** the root node of the valid policy tree, or

null

if there are no valid policies

- getPublicKey

```java
public
PublicKey
getPublicKey()
```

Returns the public key of the subject (target) of the certification
path, including any inherited public key parameters if applicable.

**Returns:** the public key of the subject (never

null

)

- clone

```java
public
Object
clone()
```

Returns a copy of this object.

**Specified by:** clone

in interface

CertPathValidatorResult
**Overrides:** clone

in class

Object
**Returns:** the copy
**See Also:** Cloneable

- toString

```java
public
String
toString()
```

Return a printable representation of this

PKIXCertPathValidatorResult

.

**Overrides:** toString

in class

Object
**Returns:** a

String

describing the contents of this

PKIXCertPathValidatorResult

Constructor Detail

- PKIXCertPathValidatorResult

```java
public PKIXCertPathValidatorResult​(
TrustAnchor
trustAnchor,

PolicyNode
policyTree,

PublicKey
subjectPublicKey)
```

Creates an instance of

PKIXCertPathValidatorResult

containing the specified parameters.

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

subjectPublicKey

or

trustAnchor

parameters are

null

---

#### Constructor Detail

PKIXCertPathValidatorResult

```java
public PKIXCertPathValidatorResult​(
TrustAnchor
trustAnchor,

PolicyNode
policyTree,

PublicKey
subjectPublicKey)
```

Creates an instance of

PKIXCertPathValidatorResult

containing the specified parameters.

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

subjectPublicKey

or

trustAnchor

parameters are

null

---

#### PKIXCertPathValidatorResult

public PKIXCertPathValidatorResult​(

TrustAnchor

trustAnchor,

PolicyNode

policyTree,

PublicKey

subjectPublicKey)

Creates an instance of

PKIXCertPathValidatorResult

containing the specified parameters.

Method Detail

- getTrustAnchor

```java
public
TrustAnchor
getTrustAnchor()
```

Returns the

TrustAnchor

describing the CA that served
as a trust anchor for the certification path.

**Returns:** the

TrustAnchor

(never

null

)

- getPolicyTree

```java
public
PolicyNode
getPolicyTree()
```

Returns the root node of the valid policy tree resulting from the
PKIX certification path validation algorithm. The

PolicyNode

object that is returned and any objects that
it returns through public methods are immutable.

Most applications will not need to examine the valid policy tree.
They can achieve their policy processing goals by setting the
policy-related parameters in

PKIXParameters

. However, more
sophisticated applications, especially those that process policy
qualifiers, may need to traverse the valid policy tree using the

PolicyNode.getParent

and

PolicyNode.getChildren

methods.

**Returns:** the root node of the valid policy tree, or

null

if there are no valid policies

- getPublicKey

```java
public
PublicKey
getPublicKey()
```

Returns the public key of the subject (target) of the certification
path, including any inherited public key parameters if applicable.

**Returns:** the public key of the subject (never

null

)

- clone

```java
public
Object
clone()
```

Returns a copy of this object.

**Specified by:** clone

in interface

CertPathValidatorResult
**Overrides:** clone

in class

Object
**Returns:** the copy
**See Also:** Cloneable

- toString

```java
public
String
toString()
```

Return a printable representation of this

PKIXCertPathValidatorResult

.

**Overrides:** toString

in class

Object
**Returns:** a

String

describing the contents of this

PKIXCertPathValidatorResult

---

#### Method Detail

getTrustAnchor

```java
public
TrustAnchor
getTrustAnchor()
```

Returns the

TrustAnchor

describing the CA that served
as a trust anchor for the certification path.

**Returns:** the

TrustAnchor

(never

null

)

---

#### getTrustAnchor

public

TrustAnchor

getTrustAnchor()

Returns the

TrustAnchor

describing the CA that served
as a trust anchor for the certification path.

getPolicyTree

```java
public
PolicyNode
getPolicyTree()
```

Returns the root node of the valid policy tree resulting from the
PKIX certification path validation algorithm. The

PolicyNode

object that is returned and any objects that
it returns through public methods are immutable.

Most applications will not need to examine the valid policy tree.
They can achieve their policy processing goals by setting the
policy-related parameters in

PKIXParameters

. However, more
sophisticated applications, especially those that process policy
qualifiers, may need to traverse the valid policy tree using the

PolicyNode.getParent

and

PolicyNode.getChildren

methods.

**Returns:** the root node of the valid policy tree, or

null

if there are no valid policies

---

#### getPolicyTree

public

PolicyNode

getPolicyTree()

Returns the root node of the valid policy tree resulting from the
PKIX certification path validation algorithm. The

PolicyNode

object that is returned and any objects that
it returns through public methods are immutable.

Most applications will not need to examine the valid policy tree.
They can achieve their policy processing goals by setting the
policy-related parameters in

PKIXParameters

. However, more
sophisticated applications, especially those that process policy
qualifiers, may need to traverse the valid policy tree using the

PolicyNode.getParent

and

PolicyNode.getChildren

methods.

Most applications will not need to examine the valid policy tree.
They can achieve their policy processing goals by setting the
policy-related parameters in

PKIXParameters

. However, more
sophisticated applications, especially those that process policy
qualifiers, may need to traverse the valid policy tree using the

PolicyNode.getParent

and

PolicyNode.getChildren

methods.

getPublicKey

```java
public
PublicKey
getPublicKey()
```

Returns the public key of the subject (target) of the certification
path, including any inherited public key parameters if applicable.

**Returns:** the public key of the subject (never

null

)

---

#### getPublicKey

public

PublicKey

getPublicKey()

Returns the public key of the subject (target) of the certification
path, including any inherited public key parameters if applicable.

clone

```java
public
Object
clone()
```

Returns a copy of this object.

**Specified by:** clone

in interface

CertPathValidatorResult
**Overrides:** clone

in class

Object
**Returns:** the copy
**See Also:** Cloneable

---

#### clone

public

Object

clone()

Returns a copy of this object.

toString

```java
public
String
toString()
```

Return a printable representation of this

PKIXCertPathValidatorResult

.

**Overrides:** toString

in class

Object
**Returns:** a

String

describing the contents of this

PKIXCertPathValidatorResult

---

#### toString

public

String

toString()

Return a printable representation of this

PKIXCertPathValidatorResult

.

---

