# Class Signer

**Source:** `java.base\java\security\Signer.html`

### Class Description

```java
@Deprecated
(
since
="1.2",

forRemoval
=true)
public abstract class
Signer

extends
Identity
```

This class is used to represent an Identity that can also digitally
sign data.

The management of a signer's private keys is an important and
sensitive issue that should be handled by subclasses as appropriate
to their intended use.

**All Implemented Interfaces:** Serializable

,

Principal

---

### Field Details

*No entries found.*

### Constructor Details

#### protected Signer()

Creates a signer. This constructor should only be used for
serialization.

---

#### public Signer​(
String
name)

Creates a signer with the specified identity name.

**Parameters:**
- name

- the identity name.

---

#### public Signer​(
String
name,

IdentityScope
scope)
throws
KeyManagementException

Creates a signer with the specified identity name and scope.

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

### Method Details

#### public
PrivateKey
getPrivateKey()

Returns this signer's private key.

First, if there is a security manager, its

checkSecurityAccess

method is called with

"getSignerPrivateKey"

as its argument to see if it's ok to return the private key.

**Returns:**
- this signer's private key, or null if the private key has
not yet been set.

**Throws:**
- SecurityException

- if a security manager exists and its

checkSecurityAccess

method doesn't allow
returning the private key.

**See Also:**
- SecurityManager.checkSecurityAccess(java.lang.String)

---

#### public final void setKeyPair​(
KeyPair
pair)
throws
InvalidParameterException
,

KeyException

Sets the key pair (public key and private key) for this signer.

First, if there is a security manager, its

checkSecurityAccess

method is called with

"setSignerKeyPair"

as its argument to see if it's ok to set the key pair.

**Parameters:**
- pair

- an initialized key pair.

**Throws:**
- InvalidParameterException

- if the key pair is not
properly initialized.
- KeyException

- if the key pair cannot be set for any
other reason.
- SecurityException

- if a security manager exists and its

checkSecurityAccess

method doesn't allow
setting the key pair.

**See Also:**
- SecurityManager.checkSecurityAccess(java.lang.String)

---

#### public
String
toString()

Returns a string of information about the signer.

**Specified by:**
- toString

in interface

Principal

**Overrides:**
- toString

in class

Identity

**Returns:**
- a string of information about the signer.

**See Also:**
- SecurityManager.checkSecurityAccess(java.lang.String)

---

### Additional Sections

#### Class Signer

java.lang.Object

- java.security.Identity
- - java.security.Signer

java.security.Identity

- java.security.Signer

java.security.Signer

**All Implemented Interfaces:** Serializable

,

Principal

```java
@Deprecated
(
since
="1.2",

forRemoval
=true)
public abstract class
Signer

extends
Identity
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

This class is used to represent an Identity that can also digitally
sign data.

The management of a signer's private keys is an important and
sensitive issue that should be handled by subclasses as appropriate
to their intended use.

**Since:** 1.1
**See Also:** Identity

,

Serialized Form

@Deprecated

(

since

="1.2",

forRemoval

=true)
public abstract class

Signer

extends

Identity

This class is used to represent an Identity that can also digitally
sign data.

The management of a signer's private keys is an important and
sensitive issue that should be handled by subclasses as appropriate
to their intended use.

The management of a signer's private keys is an important and
sensitive issue that should be handled by subclasses as appropriate
to their intended use.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Signer

()

Deprecated, for removal: This API element is subject to removal in a future version.

Creates a signer.

Signer

​(

String

name)

Deprecated, for removal: This API element is subject to removal in a future version.

Creates a signer with the specified identity name.

Signer

​(

String

name,

IdentityScope

scope)

Deprecated, for removal: This API element is subject to removal in a future version.

Creates a signer with the specified identity name and scope.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

PrivateKey

getPrivateKey

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns this signer's private key.

void

setKeyPair

​(

KeyPair

pair)

Deprecated, for removal: This API element is subject to removal in a future version.

Sets the key pair (public key and private key) for this signer.

String

toString

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns a string of information about the signer.

- Methods declared in class java.security.

Identity

addCertificate

,

certificates

,

equals

,

getInfo

,

getName

,

getPublicKey

,

getScope

,

hashCode

,

identityEquals

,

removeCertificate

,

setInfo

,

setPublicKey

,

toString

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

Signer

()

Deprecated, for removal: This API element is subject to removal in a future version.

Creates a signer.

Signer

​(

String

name)

Deprecated, for removal: This API element is subject to removal in a future version.

Creates a signer with the specified identity name.

Signer

​(

String

name,

IdentityScope

scope)

Deprecated, for removal: This API element is subject to removal in a future version.

Creates a signer with the specified identity name and scope.

---

#### Constructor Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Creates a signer.

Creates a signer with the specified identity name.

Creates a signer with the specified identity name and scope.

Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

PrivateKey

getPrivateKey

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns this signer's private key.

void

setKeyPair

​(

KeyPair

pair)

Deprecated, for removal: This API element is subject to removal in a future version.

Sets the key pair (public key and private key) for this signer.

String

toString

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns a string of information about the signer.

- Methods declared in class java.security.

Identity

addCertificate

,

certificates

,

equals

,

getInfo

,

getName

,

getPublicKey

,

getScope

,

hashCode

,

identityEquals

,

removeCertificate

,

setInfo

,

setPublicKey

,

toString

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

Returns this signer's private key.

Sets the key pair (public key and private key) for this signer.

Returns a string of information about the signer.

Methods declared in class java.security.

Identity

addCertificate

,

certificates

,

equals

,

getInfo

,

getName

,

getPublicKey

,

getScope

,

hashCode

,

identityEquals

,

removeCertificate

,

setInfo

,

setPublicKey

,

toString

---

#### Methods declared in class java.security. Identity

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

- Signer

```java
protected Signer()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Creates a signer. This constructor should only be used for
serialization.

- Signer

```java
public Signer​(
String
name)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Creates a signer with the specified identity name.

**Parameters:** name

- the identity name.

- Signer

```java
public Signer​(
String
name,

IdentityScope
scope)
throws
KeyManagementException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Creates a signer with the specified identity name and scope.

**Parameters:** name

- the identity name.
**Parameters:** scope

- the scope of the identity.
**Throws:** KeyManagementException

- if there is already an identity
with the same name in the scope.

============ METHOD DETAIL ==========

- Method Detail

- getPrivateKey

```java
public
PrivateKey
getPrivateKey()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns this signer's private key.

First, if there is a security manager, its

checkSecurityAccess

method is called with

"getSignerPrivateKey"

as its argument to see if it's ok to return the private key.

**Returns:** this signer's private key, or null if the private key has
not yet been set.
**Throws:** SecurityException

- if a security manager exists and its

checkSecurityAccess

method doesn't allow
returning the private key.
**See Also:** SecurityManager.checkSecurityAccess(java.lang.String)

- setKeyPair

```java
public final void setKeyPair​(
KeyPair
pair)
throws
InvalidParameterException
,

KeyException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Sets the key pair (public key and private key) for this signer.

First, if there is a security manager, its

checkSecurityAccess

method is called with

"setSignerKeyPair"

as its argument to see if it's ok to set the key pair.

**Parameters:** pair

- an initialized key pair.
**Throws:** InvalidParameterException

- if the key pair is not
properly initialized.
**Throws:** KeyException

- if the key pair cannot be set for any
other reason.
**Throws:** SecurityException

- if a security manager exists and its

checkSecurityAccess

method doesn't allow
setting the key pair.
**See Also:** SecurityManager.checkSecurityAccess(java.lang.String)

- toString

```java
public
String
toString()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns a string of information about the signer.

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

Identity
**Returns:** a string of information about the signer.
**See Also:** SecurityManager.checkSecurityAccess(java.lang.String)

Constructor Detail

- Signer

```java
protected Signer()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Creates a signer. This constructor should only be used for
serialization.

- Signer

```java
public Signer​(
String
name)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Creates a signer with the specified identity name.

**Parameters:** name

- the identity name.

- Signer

```java
public Signer​(
String
name,

IdentityScope
scope)
throws
KeyManagementException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Creates a signer with the specified identity name and scope.

**Parameters:** name

- the identity name.
**Parameters:** scope

- the scope of the identity.
**Throws:** KeyManagementException

- if there is already an identity
with the same name in the scope.

---

#### Constructor Detail

Signer

```java
protected Signer()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Creates a signer. This constructor should only be used for
serialization.

---

#### Signer

protected Signer()

Creates a signer. This constructor should only be used for
serialization.

Signer

```java
public Signer​(
String
name)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Creates a signer with the specified identity name.

**Parameters:** name

- the identity name.

---

#### Signer

public Signer​(

String

name)

Creates a signer with the specified identity name.

Signer

```java
public Signer​(
String
name,

IdentityScope
scope)
throws
KeyManagementException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Creates a signer with the specified identity name and scope.

**Parameters:** name

- the identity name.
**Parameters:** scope

- the scope of the identity.
**Throws:** KeyManagementException

- if there is already an identity
with the same name in the scope.

---

#### Signer

public Signer​(

String

name,

IdentityScope

scope)
throws

KeyManagementException

Creates a signer with the specified identity name and scope.

Method Detail

- getPrivateKey

```java
public
PrivateKey
getPrivateKey()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns this signer's private key.

First, if there is a security manager, its

checkSecurityAccess

method is called with

"getSignerPrivateKey"

as its argument to see if it's ok to return the private key.

**Returns:** this signer's private key, or null if the private key has
not yet been set.
**Throws:** SecurityException

- if a security manager exists and its

checkSecurityAccess

method doesn't allow
returning the private key.
**See Also:** SecurityManager.checkSecurityAccess(java.lang.String)

- setKeyPair

```java
public final void setKeyPair​(
KeyPair
pair)
throws
InvalidParameterException
,

KeyException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Sets the key pair (public key and private key) for this signer.

First, if there is a security manager, its

checkSecurityAccess

method is called with

"setSignerKeyPair"

as its argument to see if it's ok to set the key pair.

**Parameters:** pair

- an initialized key pair.
**Throws:** InvalidParameterException

- if the key pair is not
properly initialized.
**Throws:** KeyException

- if the key pair cannot be set for any
other reason.
**Throws:** SecurityException

- if a security manager exists and its

checkSecurityAccess

method doesn't allow
setting the key pair.
**See Also:** SecurityManager.checkSecurityAccess(java.lang.String)

- toString

```java
public
String
toString()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns a string of information about the signer.

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

Identity
**Returns:** a string of information about the signer.
**See Also:** SecurityManager.checkSecurityAccess(java.lang.String)

---

#### Method Detail

getPrivateKey

```java
public
PrivateKey
getPrivateKey()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns this signer's private key.

First, if there is a security manager, its

checkSecurityAccess

method is called with

"getSignerPrivateKey"

as its argument to see if it's ok to return the private key.

**Returns:** this signer's private key, or null if the private key has
not yet been set.
**Throws:** SecurityException

- if a security manager exists and its

checkSecurityAccess

method doesn't allow
returning the private key.
**See Also:** SecurityManager.checkSecurityAccess(java.lang.String)

---

#### getPrivateKey

public

PrivateKey

getPrivateKey()

Returns this signer's private key.

First, if there is a security manager, its

checkSecurityAccess

method is called with

"getSignerPrivateKey"

as its argument to see if it's ok to return the private key.

First, if there is a security manager, its

checkSecurityAccess

method is called with

"getSignerPrivateKey"

as its argument to see if it's ok to return the private key.

setKeyPair

```java
public final void setKeyPair​(
KeyPair
pair)
throws
InvalidParameterException
,

KeyException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Sets the key pair (public key and private key) for this signer.

First, if there is a security manager, its

checkSecurityAccess

method is called with

"setSignerKeyPair"

as its argument to see if it's ok to set the key pair.

**Parameters:** pair

- an initialized key pair.
**Throws:** InvalidParameterException

- if the key pair is not
properly initialized.
**Throws:** KeyException

- if the key pair cannot be set for any
other reason.
**Throws:** SecurityException

- if a security manager exists and its

checkSecurityAccess

method doesn't allow
setting the key pair.
**See Also:** SecurityManager.checkSecurityAccess(java.lang.String)

---

#### setKeyPair

public final void setKeyPair​(

KeyPair

pair)
throws

InvalidParameterException

,

KeyException

Sets the key pair (public key and private key) for this signer.

First, if there is a security manager, its

checkSecurityAccess

method is called with

"setSignerKeyPair"

as its argument to see if it's ok to set the key pair.

First, if there is a security manager, its

checkSecurityAccess

method is called with

"setSignerKeyPair"

as its argument to see if it's ok to set the key pair.

toString

```java
public
String
toString()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns a string of information about the signer.

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

Identity
**Returns:** a string of information about the signer.
**See Also:** SecurityManager.checkSecurityAccess(java.lang.String)

---

#### toString

public

String

toString()

Returns a string of information about the signer.

---

