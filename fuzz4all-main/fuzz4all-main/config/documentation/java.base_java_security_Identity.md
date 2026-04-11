# Class Identity

**Source:** `java.base\java\security\Identity.html`

### Class Description

```java
@Deprecated
(
since
="1.2",

forRemoval
=true)
public abstract class
Identity

extends
Object

implements
Principal
,
Serializable
```

This class represents identities: real-world objects such as people,
companies or organizations whose identities can be authenticated using
their public keys. Identities may also be more abstract (or concrete)
constructs, such as daemon threads or smart cards.

All Identity objects have a name and a public key. Names are
immutable. Identities may also be scoped. That is, if an Identity is
specified to have a particular scope, then the name and public
key of the Identity are unique within that scope.

An Identity also has a set of certificates (all certifying its own
public key). The Principal names specified in these certificates need
not be the same, only the key.

An Identity can be subclassed, to include postal and email addresses,
telephone numbers, images of faces and logos, and so on.

**All Implemented Interfaces:** Serializable

,

Principal

---

### Field Details

*No entries found.*

### Constructor Details

#### protected Identity()

Constructor for serialization only.

---

#### public Identity​(
String
name,

IdentityScope
scope)
throws
KeyManagementException

Constructs an identity with the specified name and scope.

**Parameters:**
- name

- the identity name.
- scope

- the scope of the identity.

**Throws:**
- KeyManagementException

- if there is already an identity
with the same name in the scope.

---

#### public Identity​(
String
name)

Constructs an identity with the specified name and no scope.

**Parameters:**
- name

- the identity name.

---

### Method Details

#### public final
String
getName()

Returns this identity's name.

**Specified by:**
- getName

in interface

Principal

**Returns:**
- the name of this identity.

---

#### public final
IdentityScope
getScope()

Returns this identity's scope.

**Returns:**
- the scope of this identity.

---

#### public
PublicKey
getPublicKey()

Returns this identity's public key.

**Returns:**
- the public key for this identity.

**See Also:**
- setPublicKey(java.security.PublicKey)

---

#### public void setPublicKey​(
PublicKey
key)
throws
KeyManagementException

Sets this identity's public key. The old key and all of this
identity's certificates are removed by this operation.

First, if there is a security manager, its

checkSecurityAccess

method is called with

"setIdentityPublicKey"

as its argument to see if it's ok to set the public key.

**Parameters:**
- key

- the public key for this identity.

**Throws:**
- KeyManagementException

- if another identity in the
identity's scope has the same public key, or if another exception occurs.
- SecurityException

- if a security manager exists and its

checkSecurityAccess

method doesn't allow
setting the public key.

**See Also:**
- getPublicKey()

,

SecurityManager.checkSecurityAccess(java.lang.String)

---

#### public void setInfo​(
String
info)

Specifies a general information string for this identity.

First, if there is a security manager, its

checkSecurityAccess

method is called with

"setIdentityInfo"

as its argument to see if it's ok to specify the information string.

**Parameters:**
- info

- the information string.

**Throws:**
- SecurityException

- if a security manager exists and its

checkSecurityAccess

method doesn't allow
setting the information string.

**See Also:**
- getInfo()

,

SecurityManager.checkSecurityAccess(java.lang.String)

---

#### public
String
getInfo()

Returns general information previously specified for this identity.

**Returns:**
- general information about this identity.

**See Also:**
- setInfo(java.lang.String)

---

#### public void addCertificate​(
Certificate
certificate)
throws
KeyManagementException

Adds a certificate for this identity. If the identity has a public
key, the public key in the certificate must be the same, and if
the identity does not have a public key, the identity's
public key is set to be that specified in the certificate.

First, if there is a security manager, its

checkSecurityAccess

method is called with

"addIdentityCertificate"

as its argument to see if it's ok to add a certificate.

**Parameters:**
- certificate

- the certificate to be added.

**Throws:**
- KeyManagementException

- if the certificate is not valid,
if the public key in the certificate being added conflicts with
this identity's public key, or if another exception occurs.
- SecurityException

- if a security manager exists and its

checkSecurityAccess

method doesn't allow
adding a certificate.

**See Also:**
- SecurityManager.checkSecurityAccess(java.lang.String)

---

#### public void removeCertificate​(
Certificate
certificate)
throws
KeyManagementException

Removes a certificate from this identity.

First, if there is a security manager, its

checkSecurityAccess

method is called with

"removeIdentityCertificate"

as its argument to see if it's ok to remove a certificate.

**Parameters:**
- certificate

- the certificate to be removed.

**Throws:**
- KeyManagementException

- if the certificate is
missing, or if another exception occurs.
- SecurityException

- if a security manager exists and its

checkSecurityAccess

method doesn't allow
removing a certificate.

**See Also:**
- SecurityManager.checkSecurityAccess(java.lang.String)

---

#### public
Certificate
[] certificates()

Returns a copy of all the certificates for this identity.

**Returns:**
- a copy of all the certificates for this identity.

---

#### public final boolean equals​(
Object
identity)

Tests for equality between the specified object and this identity.
This first tests to see if the entities actually refer to the same
object, in which case it returns true. Next, it checks to see if
the entities have the same name and the same scope. If they do,
the method returns true. Otherwise, it calls

identityEquals

, which subclasses should
override.

**Specified by:**
- equals

in interface

Principal

**Overrides:**
- equals

in class

Object

**Parameters:**
- identity

- the object to test for equality with this identity.

**Returns:**
- true if the objects are considered equal, false otherwise.

**See Also:**
- identityEquals(java.security.Identity)

---

#### protected boolean identityEquals​(
Identity
identity)

Tests for equality between the specified identity and this identity.
This method should be overriden by subclasses to test for equality.
The default behavior is to return true if the names and public keys
are equal.

**Parameters:**
- identity

- the identity to test for equality with this identity.

**Returns:**
- true if the identities are considered equal, false
otherwise.

**See Also:**
- equals(java.lang.Object)

---

#### public
String
toString()

Returns a short string describing this identity, telling its
name and its scope (if any).

First, if there is a security manager, its

checkSecurityAccess

method is called with

"printIdentity"

as its argument to see if it's ok to return the string.

**Specified by:**
- toString

in interface

Principal

**Overrides:**
- toString

in class

Object

**Returns:**
- information about this identity, such as its name and the
name of its scope (if any).

**Throws:**
- SecurityException

- if a security manager exists and its

checkSecurityAccess

method doesn't allow
returning a string describing this identity.

**See Also:**
- SecurityManager.checkSecurityAccess(java.lang.String)

---

#### public
String
toString​(boolean detailed)

Returns a string representation of this identity, with
optionally more details than that provided by the

toString

method without any arguments.

First, if there is a security manager, its

checkSecurityAccess

method is called with

"printIdentity"

as its argument to see if it's ok to return the string.

**Parameters:**
- detailed

- whether or not to provide detailed information.

**Returns:**
- information about this identity. If

detailed

is true, then this method returns more information than that
provided by the

toString

method without any arguments.

**Throws:**
- SecurityException

- if a security manager exists and its

checkSecurityAccess

method doesn't allow
returning a string describing this identity.

**See Also:**
- toString()

,

SecurityManager.checkSecurityAccess(java.lang.String)

---

#### public int hashCode()

Returns a hashcode for this identity.

**Specified by:**
- hashCode

in interface

Principal

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hashcode for this identity.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

### Additional Sections

#### Class Identity

java.lang.Object

- java.security.Identity

java.security.Identity

**All Implemented Interfaces:** Serializable

,

Principal

**Direct Known Subclasses:** IdentityScope

,

Signer

```java
@Deprecated
(
since
="1.2",

forRemoval
=true)
public abstract class
Identity

extends
Object

implements
Principal
,
Serializable
```

Deprecated, for removal: This API element is subject to removal in a future version.

This class is deprecated and subject to removal in a future
version of Java SE. It has been replaced by

java.security.KeyStore

, the

java.security.cert

package,
and

java.security.Principal

.

This class represents identities: real-world objects such as people,
companies or organizations whose identities can be authenticated using
their public keys. Identities may also be more abstract (or concrete)
constructs, such as daemon threads or smart cards.

All Identity objects have a name and a public key. Names are
immutable. Identities may also be scoped. That is, if an Identity is
specified to have a particular scope, then the name and public
key of the Identity are unique within that scope.

An Identity also has a set of certificates (all certifying its own
public key). The Principal names specified in these certificates need
not be the same, only the key.

An Identity can be subclassed, to include postal and email addresses,
telephone numbers, images of faces and logos, and so on.

**Since:** 1.1
**See Also:** IdentityScope

,

Signer

,

Principal

,

Serialized Form

@Deprecated

(

since

="1.2",

forRemoval

=true)
public abstract class

Identity

extends

Object

implements

Principal

,

Serializable

This class represents identities: real-world objects such as people,
companies or organizations whose identities can be authenticated using
their public keys. Identities may also be more abstract (or concrete)
constructs, such as daemon threads or smart cards.

All Identity objects have a name and a public key. Names are
immutable. Identities may also be scoped. That is, if an Identity is
specified to have a particular scope, then the name and public
key of the Identity are unique within that scope.

An Identity also has a set of certificates (all certifying its own
public key). The Principal names specified in these certificates need
not be the same, only the key.

An Identity can be subclassed, to include postal and email addresses,
telephone numbers, images of faces and logos, and so on.

All Identity objects have a name and a public key. Names are
immutable. Identities may also be scoped. That is, if an Identity is
specified to have a particular scope, then the name and public
key of the Identity are unique within that scope.

An Identity also has a set of certificates (all certifying its own
public key). The Principal names specified in these certificates need
not be the same, only the key.

An Identity can be subclassed, to include postal and email addresses,
telephone numbers, images of faces and logos, and so on.

An Identity also has a set of certificates (all certifying its own
public key). The Principal names specified in these certificates need
not be the same, only the key.

An Identity can be subclassed, to include postal and email addresses,
telephone numbers, images of faces and logos, and so on.

An Identity can be subclassed, to include postal and email addresses,
telephone numbers, images of faces and logos, and so on.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Identity

()

Deprecated, for removal: This API element is subject to removal in a future version.

Constructor for serialization only.

Identity

​(

String

name)

Deprecated, for removal: This API element is subject to removal in a future version.

Constructs an identity with the specified name and no scope.

Identity

​(

String

name,

IdentityScope

scope)

Deprecated, for removal: This API element is subject to removal in a future version.

Constructs an identity with the specified name and scope.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

void

addCertificate

​(

Certificate

certificate)

Deprecated, for removal: This API element is subject to removal in a future version.

Adds a certificate for this identity.

Certificate

[]

certificates

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns a copy of all the certificates for this identity.

boolean

equals

​(

Object

identity)

Deprecated, for removal: This API element is subject to removal in a future version.

Tests for equality between the specified object and this identity.

String

getInfo

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns general information previously specified for this identity.

String

getName

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns this identity's name.

PublicKey

getPublicKey

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns this identity's public key.

IdentityScope

getScope

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns this identity's scope.

int

hashCode

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns a hashcode for this identity.

protected boolean

identityEquals

​(

Identity

identity)

Deprecated, for removal: This API element is subject to removal in a future version.

Tests for equality between the specified identity and this identity.

void

removeCertificate

​(

Certificate

certificate)

Deprecated, for removal: This API element is subject to removal in a future version.

Removes a certificate from this identity.

void

setInfo

​(

String

info)

Deprecated, for removal: This API element is subject to removal in a future version.

Specifies a general information string for this identity.

void

setPublicKey

​(

PublicKey

key)

Deprecated, for removal: This API element is subject to removal in a future version.

Sets this identity's public key.

String

toString

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns a short string describing this identity, telling its
name and its scope (if any).

String

toString

​(boolean detailed)

Deprecated, for removal: This API element is subject to removal in a future version.

Returns a string representation of this identity, with
optionally more details than that provided by the

toString

method without any arguments.

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

- Methods declared in interface java.security.

Principal

implies

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Identity

()

Deprecated, for removal: This API element is subject to removal in a future version.

Constructor for serialization only.

Identity

​(

String

name)

Deprecated, for removal: This API element is subject to removal in a future version.

Constructs an identity with the specified name and no scope.

Identity

​(

String

name,

IdentityScope

scope)

Deprecated, for removal: This API element is subject to removal in a future version.

Constructs an identity with the specified name and scope.

---

#### Constructor Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Constructor for serialization only.

Constructs an identity with the specified name and no scope.

Constructs an identity with the specified name and scope.

Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

void

addCertificate

​(

Certificate

certificate)

Deprecated, for removal: This API element is subject to removal in a future version.

Adds a certificate for this identity.

Certificate

[]

certificates

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns a copy of all the certificates for this identity.

boolean

equals

​(

Object

identity)

Deprecated, for removal: This API element is subject to removal in a future version.

Tests for equality between the specified object and this identity.

String

getInfo

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns general information previously specified for this identity.

String

getName

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns this identity's name.

PublicKey

getPublicKey

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns this identity's public key.

IdentityScope

getScope

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns this identity's scope.

int

hashCode

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns a hashcode for this identity.

protected boolean

identityEquals

​(

Identity

identity)

Deprecated, for removal: This API element is subject to removal in a future version.

Tests for equality between the specified identity and this identity.

void

removeCertificate

​(

Certificate

certificate)

Deprecated, for removal: This API element is subject to removal in a future version.

Removes a certificate from this identity.

void

setInfo

​(

String

info)

Deprecated, for removal: This API element is subject to removal in a future version.

Specifies a general information string for this identity.

void

setPublicKey

​(

PublicKey

key)

Deprecated, for removal: This API element is subject to removal in a future version.

Sets this identity's public key.

String

toString

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns a short string describing this identity, telling its
name and its scope (if any).

String

toString

​(boolean detailed)

Deprecated, for removal: This API element is subject to removal in a future version.

Returns a string representation of this identity, with
optionally more details than that provided by the

toString

method without any arguments.

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

- Methods declared in interface java.security.

Principal

implies

---

#### Method Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Adds a certificate for this identity.

Returns a copy of all the certificates for this identity.

Tests for equality between the specified object and this identity.

Returns general information previously specified for this identity.

Returns this identity's name.

Returns this identity's public key.

Returns this identity's scope.

Returns a hashcode for this identity.

Tests for equality between the specified identity and this identity.

Removes a certificate from this identity.

Specifies a general information string for this identity.

Sets this identity's public key.

Returns a short string describing this identity, telling its
name and its scope (if any).

Returns a string representation of this identity, with
optionally more details than that provided by the

toString

method without any arguments.

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

Methods declared in interface java.security.

Principal

implies

---

#### Methods declared in interface java.security. Principal

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Identity

```java
protected Identity()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Constructor for serialization only.

- Identity

```java
public Identity​(
String
name,

IdentityScope
scope)
throws
KeyManagementException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Constructs an identity with the specified name and scope.

**Parameters:** name

- the identity name.
**Parameters:** scope

- the scope of the identity.
**Throws:** KeyManagementException

- if there is already an identity
with the same name in the scope.

- Identity

```java
public Identity​(
String
name)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Constructs an identity with the specified name and no scope.

**Parameters:** name

- the identity name.

============ METHOD DETAIL ==========

- Method Detail

- getName

```java
public final
String
getName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns this identity's name.

**Specified by:** getName

in interface

Principal
**Returns:** the name of this identity.

- getScope

```java
public final
IdentityScope
getScope()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns this identity's scope.

**Returns:** the scope of this identity.

- getPublicKey

```java
public
PublicKey
getPublicKey()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns this identity's public key.

**Returns:** the public key for this identity.
**See Also:** setPublicKey(java.security.PublicKey)

- setPublicKey

```java
public void setPublicKey​(
PublicKey
key)
throws
KeyManagementException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Sets this identity's public key. The old key and all of this
identity's certificates are removed by this operation.

First, if there is a security manager, its

checkSecurityAccess

method is called with

"setIdentityPublicKey"

as its argument to see if it's ok to set the public key.

**Parameters:** key

- the public key for this identity.
**Throws:** KeyManagementException

- if another identity in the
identity's scope has the same public key, or if another exception occurs.
**Throws:** SecurityException

- if a security manager exists and its

checkSecurityAccess

method doesn't allow
setting the public key.
**See Also:** getPublicKey()

,

SecurityManager.checkSecurityAccess(java.lang.String)

- setInfo

```java
public void setInfo​(
String
info)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Specifies a general information string for this identity.

First, if there is a security manager, its

checkSecurityAccess

method is called with

"setIdentityInfo"

as its argument to see if it's ok to specify the information string.

**Parameters:** info

- the information string.
**Throws:** SecurityException

- if a security manager exists and its

checkSecurityAccess

method doesn't allow
setting the information string.
**See Also:** getInfo()

,

SecurityManager.checkSecurityAccess(java.lang.String)

- getInfo

```java
public
String
getInfo()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns general information previously specified for this identity.

**Returns:** general information about this identity.
**See Also:** setInfo(java.lang.String)

- addCertificate

```java
public void addCertificate​(
Certificate
certificate)
throws
KeyManagementException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Adds a certificate for this identity. If the identity has a public
key, the public key in the certificate must be the same, and if
the identity does not have a public key, the identity's
public key is set to be that specified in the certificate.

First, if there is a security manager, its

checkSecurityAccess

method is called with

"addIdentityCertificate"

as its argument to see if it's ok to add a certificate.

**Parameters:** certificate

- the certificate to be added.
**Throws:** KeyManagementException

- if the certificate is not valid,
if the public key in the certificate being added conflicts with
this identity's public key, or if another exception occurs.
**Throws:** SecurityException

- if a security manager exists and its

checkSecurityAccess

method doesn't allow
adding a certificate.
**See Also:** SecurityManager.checkSecurityAccess(java.lang.String)

- removeCertificate

```java
public void removeCertificate​(
Certificate
certificate)
throws
KeyManagementException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Removes a certificate from this identity.

First, if there is a security manager, its

checkSecurityAccess

method is called with

"removeIdentityCertificate"

as its argument to see if it's ok to remove a certificate.

**Parameters:** certificate

- the certificate to be removed.
**Throws:** KeyManagementException

- if the certificate is
missing, or if another exception occurs.
**Throws:** SecurityException

- if a security manager exists and its

checkSecurityAccess

method doesn't allow
removing a certificate.
**See Also:** SecurityManager.checkSecurityAccess(java.lang.String)

- certificates

```java
public
Certificate
[] certificates()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns a copy of all the certificates for this identity.

**Returns:** a copy of all the certificates for this identity.

- equals

```java
public final boolean equals​(
Object
identity)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Tests for equality between the specified object and this identity.
This first tests to see if the entities actually refer to the same
object, in which case it returns true. Next, it checks to see if
the entities have the same name and the same scope. If they do,
the method returns true. Otherwise, it calls

identityEquals

, which subclasses should
override.

**Specified by:** equals

in interface

Principal
**Overrides:** equals

in class

Object
**Parameters:** identity

- the object to test for equality with this identity.
**Returns:** true if the objects are considered equal, false otherwise.
**See Also:** identityEquals(java.security.Identity)

- identityEquals

```java
protected boolean identityEquals​(
Identity
identity)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Tests for equality between the specified identity and this identity.
This method should be overriden by subclasses to test for equality.
The default behavior is to return true if the names and public keys
are equal.

**Parameters:** identity

- the identity to test for equality with this identity.
**Returns:** true if the identities are considered equal, false
otherwise.
**See Also:** equals(java.lang.Object)

- toString

```java
public
String
toString()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns a short string describing this identity, telling its
name and its scope (if any).

First, if there is a security manager, its

checkSecurityAccess

method is called with

"printIdentity"

as its argument to see if it's ok to return the string.

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

Object
**Returns:** information about this identity, such as its name and the
name of its scope (if any).
**Throws:** SecurityException

- if a security manager exists and its

checkSecurityAccess

method doesn't allow
returning a string describing this identity.
**See Also:** SecurityManager.checkSecurityAccess(java.lang.String)

- toString

```java
public
String
toString​(boolean detailed)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns a string representation of this identity, with
optionally more details than that provided by the

toString

method without any arguments.

First, if there is a security manager, its

checkSecurityAccess

method is called with

"printIdentity"

as its argument to see if it's ok to return the string.

**Parameters:** detailed

- whether or not to provide detailed information.
**Returns:** information about this identity. If

detailed

is true, then this method returns more information than that
provided by the

toString

method without any arguments.
**Throws:** SecurityException

- if a security manager exists and its

checkSecurityAccess

method doesn't allow
returning a string describing this identity.
**See Also:** toString()

,

SecurityManager.checkSecurityAccess(java.lang.String)

- hashCode

```java
public int hashCode()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns a hashcode for this identity.

**Specified by:** hashCode

in interface

Principal
**Overrides:** hashCode

in class

Object
**Returns:** a hashcode for this identity.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

Constructor Detail

- Identity

```java
protected Identity()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Constructor for serialization only.

- Identity

```java
public Identity​(
String
name,

IdentityScope
scope)
throws
KeyManagementException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Constructs an identity with the specified name and scope.

**Parameters:** name

- the identity name.
**Parameters:** scope

- the scope of the identity.
**Throws:** KeyManagementException

- if there is already an identity
with the same name in the scope.

- Identity

```java
public Identity​(
String
name)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Constructs an identity with the specified name and no scope.

**Parameters:** name

- the identity name.

---

#### Constructor Detail

Identity

```java
protected Identity()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Constructor for serialization only.

---

#### Identity

protected Identity()

Constructor for serialization only.

Identity

```java
public Identity​(
String
name,

IdentityScope
scope)
throws
KeyManagementException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Constructs an identity with the specified name and scope.

**Parameters:** name

- the identity name.
**Parameters:** scope

- the scope of the identity.
**Throws:** KeyManagementException

- if there is already an identity
with the same name in the scope.

---

#### Identity

public Identity​(

String

name,

IdentityScope

scope)
throws

KeyManagementException

Constructs an identity with the specified name and scope.

Identity

```java
public Identity​(
String
name)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Constructs an identity with the specified name and no scope.

**Parameters:** name

- the identity name.

---

#### Identity

public Identity​(

String

name)

Constructs an identity with the specified name and no scope.

Method Detail

- getName

```java
public final
String
getName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns this identity's name.

**Specified by:** getName

in interface

Principal
**Returns:** the name of this identity.

- getScope

```java
public final
IdentityScope
getScope()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns this identity's scope.

**Returns:** the scope of this identity.

- getPublicKey

```java
public
PublicKey
getPublicKey()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns this identity's public key.

**Returns:** the public key for this identity.
**See Also:** setPublicKey(java.security.PublicKey)

- setPublicKey

```java
public void setPublicKey​(
PublicKey
key)
throws
KeyManagementException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Sets this identity's public key. The old key and all of this
identity's certificates are removed by this operation.

First, if there is a security manager, its

checkSecurityAccess

method is called with

"setIdentityPublicKey"

as its argument to see if it's ok to set the public key.

**Parameters:** key

- the public key for this identity.
**Throws:** KeyManagementException

- if another identity in the
identity's scope has the same public key, or if another exception occurs.
**Throws:** SecurityException

- if a security manager exists and its

checkSecurityAccess

method doesn't allow
setting the public key.
**See Also:** getPublicKey()

,

SecurityManager.checkSecurityAccess(java.lang.String)

- setInfo

```java
public void setInfo​(
String
info)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Specifies a general information string for this identity.

First, if there is a security manager, its

checkSecurityAccess

method is called with

"setIdentityInfo"

as its argument to see if it's ok to specify the information string.

**Parameters:** info

- the information string.
**Throws:** SecurityException

- if a security manager exists and its

checkSecurityAccess

method doesn't allow
setting the information string.
**See Also:** getInfo()

,

SecurityManager.checkSecurityAccess(java.lang.String)

- getInfo

```java
public
String
getInfo()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns general information previously specified for this identity.

**Returns:** general information about this identity.
**See Also:** setInfo(java.lang.String)

- addCertificate

```java
public void addCertificate​(
Certificate
certificate)
throws
KeyManagementException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Adds a certificate for this identity. If the identity has a public
key, the public key in the certificate must be the same, and if
the identity does not have a public key, the identity's
public key is set to be that specified in the certificate.

First, if there is a security manager, its

checkSecurityAccess

method is called with

"addIdentityCertificate"

as its argument to see if it's ok to add a certificate.

**Parameters:** certificate

- the certificate to be added.
**Throws:** KeyManagementException

- if the certificate is not valid,
if the public key in the certificate being added conflicts with
this identity's public key, or if another exception occurs.
**Throws:** SecurityException

- if a security manager exists and its

checkSecurityAccess

method doesn't allow
adding a certificate.
**See Also:** SecurityManager.checkSecurityAccess(java.lang.String)

- removeCertificate

```java
public void removeCertificate​(
Certificate
certificate)
throws
KeyManagementException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Removes a certificate from this identity.

First, if there is a security manager, its

checkSecurityAccess

method is called with

"removeIdentityCertificate"

as its argument to see if it's ok to remove a certificate.

**Parameters:** certificate

- the certificate to be removed.
**Throws:** KeyManagementException

- if the certificate is
missing, or if another exception occurs.
**Throws:** SecurityException

- if a security manager exists and its

checkSecurityAccess

method doesn't allow
removing a certificate.
**See Also:** SecurityManager.checkSecurityAccess(java.lang.String)

- certificates

```java
public
Certificate
[] certificates()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns a copy of all the certificates for this identity.

**Returns:** a copy of all the certificates for this identity.

- equals

```java
public final boolean equals​(
Object
identity)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Tests for equality between the specified object and this identity.
This first tests to see if the entities actually refer to the same
object, in which case it returns true. Next, it checks to see if
the entities have the same name and the same scope. If they do,
the method returns true. Otherwise, it calls

identityEquals

, which subclasses should
override.

**Specified by:** equals

in interface

Principal
**Overrides:** equals

in class

Object
**Parameters:** identity

- the object to test for equality with this identity.
**Returns:** true if the objects are considered equal, false otherwise.
**See Also:** identityEquals(java.security.Identity)

- identityEquals

```java
protected boolean identityEquals​(
Identity
identity)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Tests for equality between the specified identity and this identity.
This method should be overriden by subclasses to test for equality.
The default behavior is to return true if the names and public keys
are equal.

**Parameters:** identity

- the identity to test for equality with this identity.
**Returns:** true if the identities are considered equal, false
otherwise.
**See Also:** equals(java.lang.Object)

- toString

```java
public
String
toString()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns a short string describing this identity, telling its
name and its scope (if any).

First, if there is a security manager, its

checkSecurityAccess

method is called with

"printIdentity"

as its argument to see if it's ok to return the string.

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

Object
**Returns:** information about this identity, such as its name and the
name of its scope (if any).
**Throws:** SecurityException

- if a security manager exists and its

checkSecurityAccess

method doesn't allow
returning a string describing this identity.
**See Also:** SecurityManager.checkSecurityAccess(java.lang.String)

- toString

```java
public
String
toString​(boolean detailed)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns a string representation of this identity, with
optionally more details than that provided by the

toString

method without any arguments.

First, if there is a security manager, its

checkSecurityAccess

method is called with

"printIdentity"

as its argument to see if it's ok to return the string.

**Parameters:** detailed

- whether or not to provide detailed information.
**Returns:** information about this identity. If

detailed

is true, then this method returns more information than that
provided by the

toString

method without any arguments.
**Throws:** SecurityException

- if a security manager exists and its

checkSecurityAccess

method doesn't allow
returning a string describing this identity.
**See Also:** toString()

,

SecurityManager.checkSecurityAccess(java.lang.String)

- hashCode

```java
public int hashCode()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns a hashcode for this identity.

**Specified by:** hashCode

in interface

Principal
**Overrides:** hashCode

in class

Object
**Returns:** a hashcode for this identity.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### Method Detail

getName

```java
public final
String
getName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns this identity's name.

**Specified by:** getName

in interface

Principal
**Returns:** the name of this identity.

---

#### getName

public final

String

getName()

Returns this identity's name.

getScope

```java
public final
IdentityScope
getScope()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns this identity's scope.

**Returns:** the scope of this identity.

---

#### getScope

public final

IdentityScope

getScope()

Returns this identity's scope.

getPublicKey

```java
public
PublicKey
getPublicKey()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns this identity's public key.

**Returns:** the public key for this identity.
**See Also:** setPublicKey(java.security.PublicKey)

---

#### getPublicKey

public

PublicKey

getPublicKey()

Returns this identity's public key.

setPublicKey

```java
public void setPublicKey​(
PublicKey
key)
throws
KeyManagementException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Sets this identity's public key. The old key and all of this
identity's certificates are removed by this operation.

First, if there is a security manager, its

checkSecurityAccess

method is called with

"setIdentityPublicKey"

as its argument to see if it's ok to set the public key.

**Parameters:** key

- the public key for this identity.
**Throws:** KeyManagementException

- if another identity in the
identity's scope has the same public key, or if another exception occurs.
**Throws:** SecurityException

- if a security manager exists and its

checkSecurityAccess

method doesn't allow
setting the public key.
**See Also:** getPublicKey()

,

SecurityManager.checkSecurityAccess(java.lang.String)

---

#### setPublicKey

public void setPublicKey​(

PublicKey

key)
throws

KeyManagementException

Sets this identity's public key. The old key and all of this
identity's certificates are removed by this operation.

First, if there is a security manager, its

checkSecurityAccess

method is called with

"setIdentityPublicKey"

as its argument to see if it's ok to set the public key.

First, if there is a security manager, its

checkSecurityAccess

method is called with

"setIdentityPublicKey"

as its argument to see if it's ok to set the public key.

setInfo

```java
public void setInfo​(
String
info)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Specifies a general information string for this identity.

First, if there is a security manager, its

checkSecurityAccess

method is called with

"setIdentityInfo"

as its argument to see if it's ok to specify the information string.

**Parameters:** info

- the information string.
**Throws:** SecurityException

- if a security manager exists and its

checkSecurityAccess

method doesn't allow
setting the information string.
**See Also:** getInfo()

,

SecurityManager.checkSecurityAccess(java.lang.String)

---

#### setInfo

public void setInfo​(

String

info)

Specifies a general information string for this identity.

First, if there is a security manager, its

checkSecurityAccess

method is called with

"setIdentityInfo"

as its argument to see if it's ok to specify the information string.

First, if there is a security manager, its

checkSecurityAccess

method is called with

"setIdentityInfo"

as its argument to see if it's ok to specify the information string.

getInfo

```java
public
String
getInfo()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns general information previously specified for this identity.

**Returns:** general information about this identity.
**See Also:** setInfo(java.lang.String)

---

#### getInfo

public

String

getInfo()

Returns general information previously specified for this identity.

addCertificate

```java
public void addCertificate​(
Certificate
certificate)
throws
KeyManagementException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Adds a certificate for this identity. If the identity has a public
key, the public key in the certificate must be the same, and if
the identity does not have a public key, the identity's
public key is set to be that specified in the certificate.

First, if there is a security manager, its

checkSecurityAccess

method is called with

"addIdentityCertificate"

as its argument to see if it's ok to add a certificate.

**Parameters:** certificate

- the certificate to be added.
**Throws:** KeyManagementException

- if the certificate is not valid,
if the public key in the certificate being added conflicts with
this identity's public key, or if another exception occurs.
**Throws:** SecurityException

- if a security manager exists and its

checkSecurityAccess

method doesn't allow
adding a certificate.
**See Also:** SecurityManager.checkSecurityAccess(java.lang.String)

---

#### addCertificate

public void addCertificate​(

Certificate

certificate)
throws

KeyManagementException

Adds a certificate for this identity. If the identity has a public
key, the public key in the certificate must be the same, and if
the identity does not have a public key, the identity's
public key is set to be that specified in the certificate.

First, if there is a security manager, its

checkSecurityAccess

method is called with

"addIdentityCertificate"

as its argument to see if it's ok to add a certificate.

First, if there is a security manager, its

checkSecurityAccess

method is called with

"addIdentityCertificate"

as its argument to see if it's ok to add a certificate.

removeCertificate

```java
public void removeCertificate​(
Certificate
certificate)
throws
KeyManagementException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Removes a certificate from this identity.

First, if there is a security manager, its

checkSecurityAccess

method is called with

"removeIdentityCertificate"

as its argument to see if it's ok to remove a certificate.

**Parameters:** certificate

- the certificate to be removed.
**Throws:** KeyManagementException

- if the certificate is
missing, or if another exception occurs.
**Throws:** SecurityException

- if a security manager exists and its

checkSecurityAccess

method doesn't allow
removing a certificate.
**See Also:** SecurityManager.checkSecurityAccess(java.lang.String)

---

#### removeCertificate

public void removeCertificate​(

Certificate

certificate)
throws

KeyManagementException

Removes a certificate from this identity.

First, if there is a security manager, its

checkSecurityAccess

method is called with

"removeIdentityCertificate"

as its argument to see if it's ok to remove a certificate.

First, if there is a security manager, its

checkSecurityAccess

method is called with

"removeIdentityCertificate"

as its argument to see if it's ok to remove a certificate.

certificates

```java
public
Certificate
[] certificates()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns a copy of all the certificates for this identity.

**Returns:** a copy of all the certificates for this identity.

---

#### certificates

public

Certificate

[] certificates()

Returns a copy of all the certificates for this identity.

equals

```java
public final boolean equals​(
Object
identity)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Tests for equality between the specified object and this identity.
This first tests to see if the entities actually refer to the same
object, in which case it returns true. Next, it checks to see if
the entities have the same name and the same scope. If they do,
the method returns true. Otherwise, it calls

identityEquals

, which subclasses should
override.

**Specified by:** equals

in interface

Principal
**Overrides:** equals

in class

Object
**Parameters:** identity

- the object to test for equality with this identity.
**Returns:** true if the objects are considered equal, false otherwise.
**See Also:** identityEquals(java.security.Identity)

---

#### equals

public final boolean equals​(

Object

identity)

Tests for equality between the specified object and this identity.
This first tests to see if the entities actually refer to the same
object, in which case it returns true. Next, it checks to see if
the entities have the same name and the same scope. If they do,
the method returns true. Otherwise, it calls

identityEquals

, which subclasses should
override.

identityEquals

```java
protected boolean identityEquals​(
Identity
identity)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Tests for equality between the specified identity and this identity.
This method should be overriden by subclasses to test for equality.
The default behavior is to return true if the names and public keys
are equal.

**Parameters:** identity

- the identity to test for equality with this identity.
**Returns:** true if the identities are considered equal, false
otherwise.
**See Also:** equals(java.lang.Object)

---

#### identityEquals

protected boolean identityEquals​(

Identity

identity)

Tests for equality between the specified identity and this identity.
This method should be overriden by subclasses to test for equality.
The default behavior is to return true if the names and public keys
are equal.

toString

```java
public
String
toString()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns a short string describing this identity, telling its
name and its scope (if any).

First, if there is a security manager, its

checkSecurityAccess

method is called with

"printIdentity"

as its argument to see if it's ok to return the string.

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

Object
**Returns:** information about this identity, such as its name and the
name of its scope (if any).
**Throws:** SecurityException

- if a security manager exists and its

checkSecurityAccess

method doesn't allow
returning a string describing this identity.
**See Also:** SecurityManager.checkSecurityAccess(java.lang.String)

---

#### toString

public

String

toString()

Returns a short string describing this identity, telling its
name and its scope (if any).

First, if there is a security manager, its

checkSecurityAccess

method is called with

"printIdentity"

as its argument to see if it's ok to return the string.

First, if there is a security manager, its

checkSecurityAccess

method is called with

"printIdentity"

as its argument to see if it's ok to return the string.

toString

```java
public
String
toString​(boolean detailed)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns a string representation of this identity, with
optionally more details than that provided by the

toString

method without any arguments.

First, if there is a security manager, its

checkSecurityAccess

method is called with

"printIdentity"

as its argument to see if it's ok to return the string.

**Parameters:** detailed

- whether or not to provide detailed information.
**Returns:** information about this identity. If

detailed

is true, then this method returns more information than that
provided by the

toString

method without any arguments.
**Throws:** SecurityException

- if a security manager exists and its

checkSecurityAccess

method doesn't allow
returning a string describing this identity.
**See Also:** toString()

,

SecurityManager.checkSecurityAccess(java.lang.String)

---

#### toString

public

String

toString​(boolean detailed)

Returns a string representation of this identity, with
optionally more details than that provided by the

toString

method without any arguments.

First, if there is a security manager, its

checkSecurityAccess

method is called with

"printIdentity"

as its argument to see if it's ok to return the string.

First, if there is a security manager, its

checkSecurityAccess

method is called with

"printIdentity"

as its argument to see if it's ok to return the string.

hashCode

```java
public int hashCode()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns a hashcode for this identity.

**Specified by:** hashCode

in interface

Principal
**Overrides:** hashCode

in class

Object
**Returns:** a hashcode for this identity.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns a hashcode for this identity.

---

