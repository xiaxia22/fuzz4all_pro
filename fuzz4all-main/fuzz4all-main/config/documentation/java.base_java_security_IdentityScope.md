# Class IdentityScope

**Source:** `java.base\java\security\IdentityScope.html`

### Class Description

```java
@Deprecated
(
since
="1.2",

forRemoval
=true)
public abstract class
IdentityScope

extends
Identity
```

This class represents a scope for identities. It is an Identity
itself, and therefore has a name and can have a scope. It can also
optionally have a public key and associated certificates.

An IdentityScope can contain Identity objects of all kinds, including
Signers. All types of Identity objects can be retrieved, added, and
removed using the same methods. Note that it is possible, and in fact
expected, that different types of identity scopes will
apply different policies for their various operations on the
various types of Identities.

There is a one-to-one mapping between keys and identities, and
there can only be one copy of one key per scope. For example, suppose

Acme Software, Inc

is a software publisher known to a user.
Suppose it is an Identity, that is, it has a public key, and a set of
associated certificates. It is named in the scope using the name
"Acme Software". No other named Identity in the scope has the same
public key. Of course, none has the same name as well.

**All Implemented Interfaces:** Serializable

,

Principal

---

### Field Details

*No entries found.*

### Constructor Details

#### protected IdentityScope()

This constructor is used for serialization only and should not
be used by subclasses.

---

#### public IdentityScope​(
String
name)

Constructs a new identity scope with the specified name.

**Parameters:**
- name

- the scope name.

---

#### public IdentityScope​(
String
name,

IdentityScope
scope)
throws
KeyManagementException

Constructs a new identity scope with the specified name and scope.

**Parameters:**
- name

- the scope name.
- scope

- the scope for the new identity scope.

**Throws:**
- KeyManagementException

- if there is already an identity
with the same name in the scope.

---

### Method Details

#### public static
IdentityScope
getSystemScope()

Returns the system's identity scope.

**Returns:**
- the system's identity scope, or

null

if none has been
set.

**See Also:**
- setSystemScope(java.security.IdentityScope)

---

#### protected static void setSystemScope​(
IdentityScope
scope)

Sets the system's identity scope.

First, if there is a security manager, its

checkSecurityAccess

method is called with

"setSystemScope"

as its argument to see if it's ok to set the identity scope.

**Parameters:**
- scope

- the scope to set.

**Throws:**
- SecurityException

- if a security manager exists and its

checkSecurityAccess

method doesn't allow
setting the identity scope.

**See Also:**
- getSystemScope()

,

SecurityManager.checkSecurityAccess(java.lang.String)

---

#### public abstract int size()

Returns the number of identities within this identity scope.

**Returns:**
- the number of identities within this identity scope.

---

#### public abstract
Identity
getIdentity​(
String
name)

Returns the identity in this scope with the specified name (if any).

**Parameters:**
- name

- the name of the identity to be retrieved.

**Returns:**
- the identity named

name

, or null if there are
no identities named

name

in this scope.

---

#### public
Identity
getIdentity​(
Principal
principal)

Retrieves the identity whose name is the same as that of the
specified principal. (Note: Identity implements Principal.)

**Parameters:**
- principal

- the principal corresponding to the identity
to be retrieved.

**Returns:**
- the identity whose name is the same as that of the
principal, or null if there are no identities of the same name
in this scope.

---

#### public abstract
Identity
getIdentity​(
PublicKey
key)

Retrieves the identity with the specified public key.

**Parameters:**
- key

- the public key for the identity to be returned.

**Returns:**
- the identity with the given key, or null if there are
no identities in this scope with that key.

---

#### public abstract void addIdentity​(
Identity
identity)
throws
KeyManagementException

Adds an identity to this identity scope.

**Parameters:**
- identity

- the identity to be added.

**Throws:**
- KeyManagementException

- if the identity is not
valid, a name conflict occurs, another identity has the same
public key as the identity being added, or another exception
occurs.

---

#### public abstract void removeIdentity​(
Identity
identity)
throws
KeyManagementException

Removes an identity from this identity scope.

**Parameters:**
- identity

- the identity to be removed.

**Throws:**
- KeyManagementException

- if the identity is missing,
or another exception occurs.

---

#### public abstract
Enumeration
<
Identity
> identities()

Returns an enumeration of all identities in this identity scope.

**Returns:**
- an enumeration of all identities in this identity scope.

---

#### public
String
toString()

Returns a string representation of this identity scope, including
its name, its scope name, and the number of identities in this
identity scope.

**Specified by:**
- toString

in interface

Principal

**Overrides:**
- toString

in class

Identity

**Returns:**
- a string representation of this identity scope.

**See Also:**
- SecurityManager.checkSecurityAccess(java.lang.String)

---

### Additional Sections

#### Class IdentityScope

java.lang.Object

- java.security.Identity
- - java.security.IdentityScope

java.security.Identity

- java.security.IdentityScope

java.security.IdentityScope

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
IdentityScope

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

This class represents a scope for identities. It is an Identity
itself, and therefore has a name and can have a scope. It can also
optionally have a public key and associated certificates.

An IdentityScope can contain Identity objects of all kinds, including
Signers. All types of Identity objects can be retrieved, added, and
removed using the same methods. Note that it is possible, and in fact
expected, that different types of identity scopes will
apply different policies for their various operations on the
various types of Identities.

There is a one-to-one mapping between keys and identities, and
there can only be one copy of one key per scope. For example, suppose

Acme Software, Inc

is a software publisher known to a user.
Suppose it is an Identity, that is, it has a public key, and a set of
associated certificates. It is named in the scope using the name
"Acme Software". No other named Identity in the scope has the same
public key. Of course, none has the same name as well.

**Since:** 1.1
**See Also:** Identity

,

Signer

,

Principal

,

Key

,

Serialized Form

@Deprecated

(

since

="1.2",

forRemoval

=true)
public abstract class

IdentityScope

extends

Identity

This class represents a scope for identities. It is an Identity
itself, and therefore has a name and can have a scope. It can also
optionally have a public key and associated certificates.

An IdentityScope can contain Identity objects of all kinds, including
Signers. All types of Identity objects can be retrieved, added, and
removed using the same methods. Note that it is possible, and in fact
expected, that different types of identity scopes will
apply different policies for their various operations on the
various types of Identities.

There is a one-to-one mapping between keys and identities, and
there can only be one copy of one key per scope. For example, suppose

Acme Software, Inc

is a software publisher known to a user.
Suppose it is an Identity, that is, it has a public key, and a set of
associated certificates. It is named in the scope using the name
"Acme Software". No other named Identity in the scope has the same
public key. Of course, none has the same name as well.

An IdentityScope can contain Identity objects of all kinds, including
Signers. All types of Identity objects can be retrieved, added, and
removed using the same methods. Note that it is possible, and in fact
expected, that different types of identity scopes will
apply different policies for their various operations on the
various types of Identities.

There is a one-to-one mapping between keys and identities, and
there can only be one copy of one key per scope. For example, suppose

Acme Software, Inc

is a software publisher known to a user.
Suppose it is an Identity, that is, it has a public key, and a set of
associated certificates. It is named in the scope using the name
"Acme Software". No other named Identity in the scope has the same
public key. Of course, none has the same name as well.

There is a one-to-one mapping between keys and identities, and
there can only be one copy of one key per scope. For example, suppose

Acme Software, Inc

is a software publisher known to a user.
Suppose it is an Identity, that is, it has a public key, and a set of
associated certificates. It is named in the scope using the name
"Acme Software". No other named Identity in the scope has the same
public key. Of course, none has the same name as well.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

IdentityScope

()

Deprecated, for removal: This API element is subject to removal in a future version.

This constructor is used for serialization only and should not
be used by subclasses.

IdentityScope

​(

String

name)

Deprecated, for removal: This API element is subject to removal in a future version.

Constructs a new identity scope with the specified name.

IdentityScope

​(

String

name,

IdentityScope

scope)

Deprecated, for removal: This API element is subject to removal in a future version.

Constructs a new identity scope with the specified name and scope.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

abstract void

addIdentity

​(

Identity

identity)

Deprecated, for removal: This API element is subject to removal in a future version.

Adds an identity to this identity scope.

abstract

Identity

getIdentity

​(

String

name)

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the identity in this scope with the specified name (if any).

Identity

getIdentity

​(

Principal

principal)

Deprecated, for removal: This API element is subject to removal in a future version.

Retrieves the identity whose name is the same as that of the
specified principal.

abstract

Identity

getIdentity

​(

PublicKey

key)

Deprecated, for removal: This API element is subject to removal in a future version.

Retrieves the identity with the specified public key.

static

IdentityScope

getSystemScope

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the system's identity scope.

abstract

Enumeration

<

Identity

>

identities

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns an enumeration of all identities in this identity scope.

abstract void

removeIdentity

​(

Identity

identity)

Deprecated, for removal: This API element is subject to removal in a future version.

Removes an identity from this identity scope.

protected static void

setSystemScope

​(

IdentityScope

scope)

Deprecated, for removal: This API element is subject to removal in a future version.

Sets the system's identity scope.

abstract int

size

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the number of identities within this identity scope.

String

toString

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns a string representation of this identity scope, including
its name, its scope name, and the number of identities in this
identity scope.

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

IdentityScope

()

Deprecated, for removal: This API element is subject to removal in a future version.

This constructor is used for serialization only and should not
be used by subclasses.

IdentityScope

​(

String

name)

Deprecated, for removal: This API element is subject to removal in a future version.

Constructs a new identity scope with the specified name.

IdentityScope

​(

String

name,

IdentityScope

scope)

Deprecated, for removal: This API element is subject to removal in a future version.

Constructs a new identity scope with the specified name and scope.

---

#### Constructor Summary

Deprecated, for removal: This API element is subject to removal in a future version.

This constructor is used for serialization only and should not
be used by subclasses.

Constructs a new identity scope with the specified name.

Constructs a new identity scope with the specified name and scope.

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

abstract void

addIdentity

​(

Identity

identity)

Deprecated, for removal: This API element is subject to removal in a future version.

Adds an identity to this identity scope.

abstract

Identity

getIdentity

​(

String

name)

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the identity in this scope with the specified name (if any).

Identity

getIdentity

​(

Principal

principal)

Deprecated, for removal: This API element is subject to removal in a future version.

Retrieves the identity whose name is the same as that of the
specified principal.

abstract

Identity

getIdentity

​(

PublicKey

key)

Deprecated, for removal: This API element is subject to removal in a future version.

Retrieves the identity with the specified public key.

static

IdentityScope

getSystemScope

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the system's identity scope.

abstract

Enumeration

<

Identity

>

identities

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns an enumeration of all identities in this identity scope.

abstract void

removeIdentity

​(

Identity

identity)

Deprecated, for removal: This API element is subject to removal in a future version.

Removes an identity from this identity scope.

protected static void

setSystemScope

​(

IdentityScope

scope)

Deprecated, for removal: This API element is subject to removal in a future version.

Sets the system's identity scope.

abstract int

size

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the number of identities within this identity scope.

String

toString

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns a string representation of this identity scope, including
its name, its scope name, and the number of identities in this
identity scope.

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

Adds an identity to this identity scope.

Returns the identity in this scope with the specified name (if any).

Retrieves the identity whose name is the same as that of the
specified principal.

Retrieves the identity with the specified public key.

Returns the system's identity scope.

Returns an enumeration of all identities in this identity scope.

Removes an identity from this identity scope.

Sets the system's identity scope.

Returns the number of identities within this identity scope.

Returns a string representation of this identity scope, including
its name, its scope name, and the number of identities in this
identity scope.

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

- IdentityScope

```java
protected IdentityScope()
```

Deprecated, for removal: This API element is subject to removal in a future version.

This constructor is used for serialization only and should not
be used by subclasses.

- IdentityScope

```java
public IdentityScope​(
String
name)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Constructs a new identity scope with the specified name.

**Parameters:** name

- the scope name.

- IdentityScope

```java
public IdentityScope​(
String
name,

IdentityScope
scope)
throws
KeyManagementException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Constructs a new identity scope with the specified name and scope.

**Parameters:** name

- the scope name.
**Parameters:** scope

- the scope for the new identity scope.
**Throws:** KeyManagementException

- if there is already an identity
with the same name in the scope.

============ METHOD DETAIL ==========

- Method Detail

- getSystemScope

```java
public static
IdentityScope
getSystemScope()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the system's identity scope.

**Returns:** the system's identity scope, or

null

if none has been
set.
**See Also:** setSystemScope(java.security.IdentityScope)

- setSystemScope

```java
protected static void setSystemScope​(
IdentityScope
scope)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Sets the system's identity scope.

First, if there is a security manager, its

checkSecurityAccess

method is called with

"setSystemScope"

as its argument to see if it's ok to set the identity scope.

**Parameters:** scope

- the scope to set.
**Throws:** SecurityException

- if a security manager exists and its

checkSecurityAccess

method doesn't allow
setting the identity scope.
**See Also:** getSystemScope()

,

SecurityManager.checkSecurityAccess(java.lang.String)

- size

```java
public abstract int size()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the number of identities within this identity scope.

**Returns:** the number of identities within this identity scope.

- getIdentity

```java
public abstract
Identity
getIdentity​(
String
name)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the identity in this scope with the specified name (if any).

**Parameters:** name

- the name of the identity to be retrieved.
**Returns:** the identity named

name

, or null if there are
no identities named

name

in this scope.

- getIdentity

```java
public
Identity
getIdentity​(
Principal
principal)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Retrieves the identity whose name is the same as that of the
specified principal. (Note: Identity implements Principal.)

**Parameters:** principal

- the principal corresponding to the identity
to be retrieved.
**Returns:** the identity whose name is the same as that of the
principal, or null if there are no identities of the same name
in this scope.

- getIdentity

```java
public abstract
Identity
getIdentity​(
PublicKey
key)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Retrieves the identity with the specified public key.

**Parameters:** key

- the public key for the identity to be returned.
**Returns:** the identity with the given key, or null if there are
no identities in this scope with that key.

- addIdentity

```java
public abstract void addIdentity​(
Identity
identity)
throws
KeyManagementException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Adds an identity to this identity scope.

**Parameters:** identity

- the identity to be added.
**Throws:** KeyManagementException

- if the identity is not
valid, a name conflict occurs, another identity has the same
public key as the identity being added, or another exception
occurs.

- removeIdentity

```java
public abstract void removeIdentity​(
Identity
identity)
throws
KeyManagementException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Removes an identity from this identity scope.

**Parameters:** identity

- the identity to be removed.
**Throws:** KeyManagementException

- if the identity is missing,
or another exception occurs.

- identities

```java
public abstract
Enumeration
<
Identity
> identities()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns an enumeration of all identities in this identity scope.

**Returns:** an enumeration of all identities in this identity scope.

- toString

```java
public
String
toString()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns a string representation of this identity scope, including
its name, its scope name, and the number of identities in this
identity scope.

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

Identity
**Returns:** a string representation of this identity scope.
**See Also:** SecurityManager.checkSecurityAccess(java.lang.String)

Constructor Detail

- IdentityScope

```java
protected IdentityScope()
```

Deprecated, for removal: This API element is subject to removal in a future version.

This constructor is used for serialization only and should not
be used by subclasses.

- IdentityScope

```java
public IdentityScope​(
String
name)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Constructs a new identity scope with the specified name.

**Parameters:** name

- the scope name.

- IdentityScope

```java
public IdentityScope​(
String
name,

IdentityScope
scope)
throws
KeyManagementException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Constructs a new identity scope with the specified name and scope.

**Parameters:** name

- the scope name.
**Parameters:** scope

- the scope for the new identity scope.
**Throws:** KeyManagementException

- if there is already an identity
with the same name in the scope.

---

#### Constructor Detail

IdentityScope

```java
protected IdentityScope()
```

Deprecated, for removal: This API element is subject to removal in a future version.

This constructor is used for serialization only and should not
be used by subclasses.

---

#### IdentityScope

protected IdentityScope()

This constructor is used for serialization only and should not
be used by subclasses.

IdentityScope

```java
public IdentityScope​(
String
name)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Constructs a new identity scope with the specified name.

**Parameters:** name

- the scope name.

---

#### IdentityScope

public IdentityScope​(

String

name)

Constructs a new identity scope with the specified name.

IdentityScope

```java
public IdentityScope​(
String
name,

IdentityScope
scope)
throws
KeyManagementException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Constructs a new identity scope with the specified name and scope.

**Parameters:** name

- the scope name.
**Parameters:** scope

- the scope for the new identity scope.
**Throws:** KeyManagementException

- if there is already an identity
with the same name in the scope.

---

#### IdentityScope

public IdentityScope​(

String

name,

IdentityScope

scope)
throws

KeyManagementException

Constructs a new identity scope with the specified name and scope.

Method Detail

- getSystemScope

```java
public static
IdentityScope
getSystemScope()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the system's identity scope.

**Returns:** the system's identity scope, or

null

if none has been
set.
**See Also:** setSystemScope(java.security.IdentityScope)

- setSystemScope

```java
protected static void setSystemScope​(
IdentityScope
scope)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Sets the system's identity scope.

First, if there is a security manager, its

checkSecurityAccess

method is called with

"setSystemScope"

as its argument to see if it's ok to set the identity scope.

**Parameters:** scope

- the scope to set.
**Throws:** SecurityException

- if a security manager exists and its

checkSecurityAccess

method doesn't allow
setting the identity scope.
**See Also:** getSystemScope()

,

SecurityManager.checkSecurityAccess(java.lang.String)

- size

```java
public abstract int size()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the number of identities within this identity scope.

**Returns:** the number of identities within this identity scope.

- getIdentity

```java
public abstract
Identity
getIdentity​(
String
name)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the identity in this scope with the specified name (if any).

**Parameters:** name

- the name of the identity to be retrieved.
**Returns:** the identity named

name

, or null if there are
no identities named

name

in this scope.

- getIdentity

```java
public
Identity
getIdentity​(
Principal
principal)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Retrieves the identity whose name is the same as that of the
specified principal. (Note: Identity implements Principal.)

**Parameters:** principal

- the principal corresponding to the identity
to be retrieved.
**Returns:** the identity whose name is the same as that of the
principal, or null if there are no identities of the same name
in this scope.

- getIdentity

```java
public abstract
Identity
getIdentity​(
PublicKey
key)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Retrieves the identity with the specified public key.

**Parameters:** key

- the public key for the identity to be returned.
**Returns:** the identity with the given key, or null if there are
no identities in this scope with that key.

- addIdentity

```java
public abstract void addIdentity​(
Identity
identity)
throws
KeyManagementException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Adds an identity to this identity scope.

**Parameters:** identity

- the identity to be added.
**Throws:** KeyManagementException

- if the identity is not
valid, a name conflict occurs, another identity has the same
public key as the identity being added, or another exception
occurs.

- removeIdentity

```java
public abstract void removeIdentity​(
Identity
identity)
throws
KeyManagementException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Removes an identity from this identity scope.

**Parameters:** identity

- the identity to be removed.
**Throws:** KeyManagementException

- if the identity is missing,
or another exception occurs.

- identities

```java
public abstract
Enumeration
<
Identity
> identities()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns an enumeration of all identities in this identity scope.

**Returns:** an enumeration of all identities in this identity scope.

- toString

```java
public
String
toString()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns a string representation of this identity scope, including
its name, its scope name, and the number of identities in this
identity scope.

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

Identity
**Returns:** a string representation of this identity scope.
**See Also:** SecurityManager.checkSecurityAccess(java.lang.String)

---

#### Method Detail

getSystemScope

```java
public static
IdentityScope
getSystemScope()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the system's identity scope.

**Returns:** the system's identity scope, or

null

if none has been
set.
**See Also:** setSystemScope(java.security.IdentityScope)

---

#### getSystemScope

public static

IdentityScope

getSystemScope()

Returns the system's identity scope.

setSystemScope

```java
protected static void setSystemScope​(
IdentityScope
scope)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Sets the system's identity scope.

First, if there is a security manager, its

checkSecurityAccess

method is called with

"setSystemScope"

as its argument to see if it's ok to set the identity scope.

**Parameters:** scope

- the scope to set.
**Throws:** SecurityException

- if a security manager exists and its

checkSecurityAccess

method doesn't allow
setting the identity scope.
**See Also:** getSystemScope()

,

SecurityManager.checkSecurityAccess(java.lang.String)

---

#### setSystemScope

protected static void setSystemScope​(

IdentityScope

scope)

Sets the system's identity scope.

First, if there is a security manager, its

checkSecurityAccess

method is called with

"setSystemScope"

as its argument to see if it's ok to set the identity scope.

First, if there is a security manager, its

checkSecurityAccess

method is called with

"setSystemScope"

as its argument to see if it's ok to set the identity scope.

size

```java
public abstract int size()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the number of identities within this identity scope.

**Returns:** the number of identities within this identity scope.

---

#### size

public abstract int size()

Returns the number of identities within this identity scope.

getIdentity

```java
public abstract
Identity
getIdentity​(
String
name)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the identity in this scope with the specified name (if any).

**Parameters:** name

- the name of the identity to be retrieved.
**Returns:** the identity named

name

, or null if there are
no identities named

name

in this scope.

---

#### getIdentity

public abstract

Identity

getIdentity​(

String

name)

Returns the identity in this scope with the specified name (if any).

getIdentity

```java
public
Identity
getIdentity​(
Principal
principal)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Retrieves the identity whose name is the same as that of the
specified principal. (Note: Identity implements Principal.)

**Parameters:** principal

- the principal corresponding to the identity
to be retrieved.
**Returns:** the identity whose name is the same as that of the
principal, or null if there are no identities of the same name
in this scope.

---

#### getIdentity

public

Identity

getIdentity​(

Principal

principal)

Retrieves the identity whose name is the same as that of the
specified principal. (Note: Identity implements Principal.)

getIdentity

```java
public abstract
Identity
getIdentity​(
PublicKey
key)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Retrieves the identity with the specified public key.

**Parameters:** key

- the public key for the identity to be returned.
**Returns:** the identity with the given key, or null if there are
no identities in this scope with that key.

---

#### getIdentity

public abstract

Identity

getIdentity​(

PublicKey

key)

Retrieves the identity with the specified public key.

addIdentity

```java
public abstract void addIdentity​(
Identity
identity)
throws
KeyManagementException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Adds an identity to this identity scope.

**Parameters:** identity

- the identity to be added.
**Throws:** KeyManagementException

- if the identity is not
valid, a name conflict occurs, another identity has the same
public key as the identity being added, or another exception
occurs.

---

#### addIdentity

public abstract void addIdentity​(

Identity

identity)
throws

KeyManagementException

Adds an identity to this identity scope.

removeIdentity

```java
public abstract void removeIdentity​(
Identity
identity)
throws
KeyManagementException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Removes an identity from this identity scope.

**Parameters:** identity

- the identity to be removed.
**Throws:** KeyManagementException

- if the identity is missing,
or another exception occurs.

---

#### removeIdentity

public abstract void removeIdentity​(

Identity

identity)
throws

KeyManagementException

Removes an identity from this identity scope.

identities

```java
public abstract
Enumeration
<
Identity
> identities()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns an enumeration of all identities in this identity scope.

**Returns:** an enumeration of all identities in this identity scope.

---

#### identities

public abstract

Enumeration

<

Identity

> identities()

Returns an enumeration of all identities in this identity scope.

toString

```java
public
String
toString()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns a string representation of this identity scope, including
its name, its scope name, and the number of identities in this
identity scope.

**Specified by:** toString

in interface

Principal
**Overrides:** toString

in class

Identity
**Returns:** a string representation of this identity scope.
**See Also:** SecurityManager.checkSecurityAccess(java.lang.String)

---

#### toString

public

String

toString()

Returns a string representation of this identity scope, including
its name, its scope name, and the number of identities in this
identity scope.

---

