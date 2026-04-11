# Class DelegationPermission

**Source:** `java.security.jgss\javax\security\auth\kerberos\DelegationPermission.html`

### Class Description

```java
public final class
DelegationPermission

extends
BasicPermission

implements
Serializable
```

This class is used to restrict the usage of the Kerberos
delegation model, ie: forwardable and proxiable tickets.

The target name of this

Permission

specifies a pair of
kerberos service principals. The first is the subordinate service principal
being entrusted to use the TGT. The second service principal designates
the target service the subordinate service principal is to
interact with on behalf of the initiating KerberosPrincipal. This
latter service principal is specified to restrict the use of a
proxiable ticket.

For example, to specify the "host" service use of a forwardable TGT the
target permission is specified as follows:

```java
DelegationPermission("\"host/foo.example.com@EXAMPLE.COM\" \"krbtgt/EXAMPLE.COM@EXAMPLE.COM\"");
```

To give the "backup" service a proxiable nfs service ticket the target permission
might be specified:

```java
DelegationPermission("\"backup/bar.example.com@EXAMPLE.COM\" \"nfs/home.EXAMPLE.COM@EXAMPLE.COM\"");
```

**All Implemented Interfaces:** Serializable

,

Guard

---

### Field Details

*No entries found.*

### Constructor Details

#### public DelegationPermission​(
String
principals)

Create a new

DelegationPermission

with the specified subordinate and target principals.

**Parameters:**
- principals

- the name of the subordinate and target principals

**Throws:**
- NullPointerException

- if

principals

is

null

.
- IllegalArgumentException

- if

principals

is empty.

---

#### public DelegationPermission​(
String
principals,

String
actions)

Create a new

DelegationPermission

with the specified subordinate and target principals.

**Parameters:**
- principals

- the name of the subordinate and target principals
- actions

- should be null.

**Throws:**
- NullPointerException

- if

principals

is

null

.
- IllegalArgumentException

- if

principals

is empty.

---

### Method Details

#### public boolean implies​(
Permission
p)

Checks if this Kerberos delegation permission object "implies" the
specified permission.

This method returns true if this

DelegationPermission

is equal to

p

, and returns false otherwise.

**Overrides:**
- implies

in class

BasicPermission

**Parameters:**
- p

- the permission to check against.

**Returns:**
- true if the specified permission is implied by this object,
false if not.

---

#### public boolean equals​(
Object
obj)

Checks two DelegationPermission objects for equality.

**Overrides:**
- equals

in class

BasicPermission

**Parameters:**
- obj

- the object to test for equality with this object.

**Returns:**
- true if

obj

is a DelegationPermission, and
has the same subordinate and service principal as this
DelegationPermission object.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns the hash code value for this object.

**Overrides:**
- hashCode

in class

BasicPermission

**Returns:**
- a hash code value for this object.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public
PermissionCollection
newPermissionCollection()

Returns a PermissionCollection object for storing
DelegationPermission objects.

DelegationPermission objects must be stored in a manner that
allows them to be inserted into the collection in any order, but
that also enables the PermissionCollection implies method to
be implemented in an efficient (and consistent) manner.

**Overrides:**
- newPermissionCollection

in class

BasicPermission

**Returns:**
- a new PermissionCollection object suitable for storing
DelegationPermissions.

---

### Additional Sections

#### Class DelegationPermission

java.lang.Object

- java.security.Permission
- - java.security.BasicPermission
- - javax.security.auth.kerberos.DelegationPermission

java.security.Permission

- java.security.BasicPermission
- - javax.security.auth.kerberos.DelegationPermission

java.security.BasicPermission

- javax.security.auth.kerberos.DelegationPermission

javax.security.auth.kerberos.DelegationPermission

**All Implemented Interfaces:** Serializable

,

Guard

```java
public final class
DelegationPermission

extends
BasicPermission

implements
Serializable
```

This class is used to restrict the usage of the Kerberos
delegation model, ie: forwardable and proxiable tickets.

The target name of this

Permission

specifies a pair of
kerberos service principals. The first is the subordinate service principal
being entrusted to use the TGT. The second service principal designates
the target service the subordinate service principal is to
interact with on behalf of the initiating KerberosPrincipal. This
latter service principal is specified to restrict the use of a
proxiable ticket.

For example, to specify the "host" service use of a forwardable TGT the
target permission is specified as follows:

```java
DelegationPermission("\"host/foo.example.com@EXAMPLE.COM\" \"krbtgt/EXAMPLE.COM@EXAMPLE.COM\"");
```

To give the "backup" service a proxiable nfs service ticket the target permission
might be specified:

```java
DelegationPermission("\"backup/bar.example.com@EXAMPLE.COM\" \"nfs/home.EXAMPLE.COM@EXAMPLE.COM\"");
```

**Since:** 1.4
**See Also:** Serialized Form

public final class

DelegationPermission

extends

BasicPermission

implements

Serializable

This class is used to restrict the usage of the Kerberos
delegation model, ie: forwardable and proxiable tickets.

The target name of this

Permission

specifies a pair of
kerberos service principals. The first is the subordinate service principal
being entrusted to use the TGT. The second service principal designates
the target service the subordinate service principal is to
interact with on behalf of the initiating KerberosPrincipal. This
latter service principal is specified to restrict the use of a
proxiable ticket.

For example, to specify the "host" service use of a forwardable TGT the
target permission is specified as follows:

```java
DelegationPermission("\"host/foo.example.com@EXAMPLE.COM\" \"krbtgt/EXAMPLE.COM@EXAMPLE.COM\"");
```

To give the "backup" service a proxiable nfs service ticket the target permission
might be specified:

```java
DelegationPermission("\"backup/bar.example.com@EXAMPLE.COM\" \"nfs/home.EXAMPLE.COM@EXAMPLE.COM\"");
```

The target name of this

Permission

specifies a pair of
kerberos service principals. The first is the subordinate service principal
being entrusted to use the TGT. The second service principal designates
the target service the subordinate service principal is to
interact with on behalf of the initiating KerberosPrincipal. This
latter service principal is specified to restrict the use of a
proxiable ticket.

For example, to specify the "host" service use of a forwardable TGT the
target permission is specified as follows:

```java
DelegationPermission("\"host/foo.example.com@EXAMPLE.COM\" \"krbtgt/EXAMPLE.COM@EXAMPLE.COM\"");
```

To give the "backup" service a proxiable nfs service ticket the target permission
might be specified:

```java
DelegationPermission("\"backup/bar.example.com@EXAMPLE.COM\" \"nfs/home.EXAMPLE.COM@EXAMPLE.COM\"");
```

For example, to specify the "host" service use of a forwardable TGT the
target permission is specified as follows:

```java
DelegationPermission("\"host/foo.example.com@EXAMPLE.COM\" \"krbtgt/EXAMPLE.COM@EXAMPLE.COM\"");
```

To give the "backup" service a proxiable nfs service ticket the target permission
might be specified:

```java
DelegationPermission("\"backup/bar.example.com@EXAMPLE.COM\" \"nfs/home.EXAMPLE.COM@EXAMPLE.COM\"");
```

DelegationPermission("\"host/foo.example.com@EXAMPLE.COM\" \"krbtgt/EXAMPLE.COM@EXAMPLE.COM\"");

To give the "backup" service a proxiable nfs service ticket the target permission
might be specified:

```java
DelegationPermission("\"backup/bar.example.com@EXAMPLE.COM\" \"nfs/home.EXAMPLE.COM@EXAMPLE.COM\"");
```

DelegationPermission("\"backup/bar.example.com@EXAMPLE.COM\" \"nfs/home.EXAMPLE.COM@EXAMPLE.COM\"");

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DelegationPermission

​(

String

principals)

Create a new

DelegationPermission

with the specified subordinate and target principals.

DelegationPermission

​(

String

principals,

String

actions)

Create a new

DelegationPermission

with the specified subordinate and target principals.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Checks two DelegationPermission objects for equality.

int

hashCode

()

Returns the hash code value for this object.

boolean

implies

​(

Permission

p)

Checks if this Kerberos delegation permission object "implies" the
specified permission.

PermissionCollection

newPermissionCollection

()

Returns a PermissionCollection object for storing
DelegationPermission objects.

- Methods declared in class java.security.

BasicPermission

getActions

- Methods declared in class java.security.

Permission

checkGuard

,

getName

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

Constructor Summary

Constructors

Constructor

Description

DelegationPermission

​(

String

principals)

Create a new

DelegationPermission

with the specified subordinate and target principals.

DelegationPermission

​(

String

principals,

String

actions)

Create a new

DelegationPermission

with the specified subordinate and target principals.

---

#### Constructor Summary

Create a new

DelegationPermission

with the specified subordinate and target principals.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Checks two DelegationPermission objects for equality.

int

hashCode

()

Returns the hash code value for this object.

boolean

implies

​(

Permission

p)

Checks if this Kerberos delegation permission object "implies" the
specified permission.

PermissionCollection

newPermissionCollection

()

Returns a PermissionCollection object for storing
DelegationPermission objects.

- Methods declared in class java.security.

BasicPermission

getActions

- Methods declared in class java.security.

Permission

checkGuard

,

getName

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

---

#### Method Summary

Checks two DelegationPermission objects for equality.

Returns the hash code value for this object.

Checks if this Kerberos delegation permission object "implies" the
specified permission.

Returns a PermissionCollection object for storing
DelegationPermission objects.

Methods declared in class java.security.

BasicPermission

getActions

---

#### Methods declared in class java.security. BasicPermission

Methods declared in class java.security.

Permission

checkGuard

,

getName

,

toString

---

#### Methods declared in class java.security. Permission

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

- DelegationPermission

```java
public DelegationPermission​(
String
principals)
```

Create a new

DelegationPermission

with the specified subordinate and target principals.

**Parameters:** principals

- the name of the subordinate and target principals
**Throws:** NullPointerException

- if

principals

is

null

.
**Throws:** IllegalArgumentException

- if

principals

is empty.

- DelegationPermission

```java
public DelegationPermission​(
String
principals,

String
actions)
```

Create a new

DelegationPermission

with the specified subordinate and target principals.

**Parameters:** principals

- the name of the subordinate and target principals
**Parameters:** actions

- should be null.
**Throws:** NullPointerException

- if

principals

is

null

.
**Throws:** IllegalArgumentException

- if

principals

is empty.

============ METHOD DETAIL ==========

- Method Detail

- implies

```java
public boolean implies​(
Permission
p)
```

Checks if this Kerberos delegation permission object "implies" the
specified permission.

This method returns true if this

DelegationPermission

is equal to

p

, and returns false otherwise.

**Overrides:** implies

in class

BasicPermission
**Parameters:** p

- the permission to check against.
**Returns:** true if the specified permission is implied by this object,
false if not.

- equals

```java
public boolean equals​(
Object
obj)
```

Checks two DelegationPermission objects for equality.

**Overrides:** equals

in class

BasicPermission
**Parameters:** obj

- the object to test for equality with this object.
**Returns:** true if

obj

is a DelegationPermission, and
has the same subordinate and service principal as this
DelegationPermission object.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this object.

**Overrides:** hashCode

in class

BasicPermission
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- newPermissionCollection

```java
public
PermissionCollection
newPermissionCollection()
```

Returns a PermissionCollection object for storing
DelegationPermission objects.

DelegationPermission objects must be stored in a manner that
allows them to be inserted into the collection in any order, but
that also enables the PermissionCollection implies method to
be implemented in an efficient (and consistent) manner.

**Overrides:** newPermissionCollection

in class

BasicPermission
**Returns:** a new PermissionCollection object suitable for storing
DelegationPermissions.

Constructor Detail

- DelegationPermission

```java
public DelegationPermission​(
String
principals)
```

Create a new

DelegationPermission

with the specified subordinate and target principals.

**Parameters:** principals

- the name of the subordinate and target principals
**Throws:** NullPointerException

- if

principals

is

null

.
**Throws:** IllegalArgumentException

- if

principals

is empty.

- DelegationPermission

```java
public DelegationPermission​(
String
principals,

String
actions)
```

Create a new

DelegationPermission

with the specified subordinate and target principals.

**Parameters:** principals

- the name of the subordinate and target principals
**Parameters:** actions

- should be null.
**Throws:** NullPointerException

- if

principals

is

null

.
**Throws:** IllegalArgumentException

- if

principals

is empty.

---

#### Constructor Detail

DelegationPermission

```java
public DelegationPermission​(
String
principals)
```

Create a new

DelegationPermission

with the specified subordinate and target principals.

**Parameters:** principals

- the name of the subordinate and target principals
**Throws:** NullPointerException

- if

principals

is

null

.
**Throws:** IllegalArgumentException

- if

principals

is empty.

---

#### DelegationPermission

public DelegationPermission​(

String

principals)

Create a new

DelegationPermission

with the specified subordinate and target principals.

DelegationPermission

```java
public DelegationPermission​(
String
principals,

String
actions)
```

Create a new

DelegationPermission

with the specified subordinate and target principals.

**Parameters:** principals

- the name of the subordinate and target principals
**Parameters:** actions

- should be null.
**Throws:** NullPointerException

- if

principals

is

null

.
**Throws:** IllegalArgumentException

- if

principals

is empty.

---

#### DelegationPermission

public DelegationPermission​(

String

principals,

String

actions)

Create a new

DelegationPermission

with the specified subordinate and target principals.

Method Detail

- implies

```java
public boolean implies​(
Permission
p)
```

Checks if this Kerberos delegation permission object "implies" the
specified permission.

This method returns true if this

DelegationPermission

is equal to

p

, and returns false otherwise.

**Overrides:** implies

in class

BasicPermission
**Parameters:** p

- the permission to check against.
**Returns:** true if the specified permission is implied by this object,
false if not.

- equals

```java
public boolean equals​(
Object
obj)
```

Checks two DelegationPermission objects for equality.

**Overrides:** equals

in class

BasicPermission
**Parameters:** obj

- the object to test for equality with this object.
**Returns:** true if

obj

is a DelegationPermission, and
has the same subordinate and service principal as this
DelegationPermission object.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this object.

**Overrides:** hashCode

in class

BasicPermission
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- newPermissionCollection

```java
public
PermissionCollection
newPermissionCollection()
```

Returns a PermissionCollection object for storing
DelegationPermission objects.

DelegationPermission objects must be stored in a manner that
allows them to be inserted into the collection in any order, but
that also enables the PermissionCollection implies method to
be implemented in an efficient (and consistent) manner.

**Overrides:** newPermissionCollection

in class

BasicPermission
**Returns:** a new PermissionCollection object suitable for storing
DelegationPermissions.

---

#### Method Detail

implies

```java
public boolean implies​(
Permission
p)
```

Checks if this Kerberos delegation permission object "implies" the
specified permission.

This method returns true if this

DelegationPermission

is equal to

p

, and returns false otherwise.

**Overrides:** implies

in class

BasicPermission
**Parameters:** p

- the permission to check against.
**Returns:** true if the specified permission is implied by this object,
false if not.

---

#### implies

public boolean implies​(

Permission

p)

Checks if this Kerberos delegation permission object "implies" the
specified permission.

This method returns true if this

DelegationPermission

is equal to

p

, and returns false otherwise.

This method returns true if this

DelegationPermission

is equal to

p

, and returns false otherwise.

equals

```java
public boolean equals​(
Object
obj)
```

Checks two DelegationPermission objects for equality.

**Overrides:** equals

in class

BasicPermission
**Parameters:** obj

- the object to test for equality with this object.
**Returns:** true if

obj

is a DelegationPermission, and
has the same subordinate and service principal as this
DelegationPermission object.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Checks two DelegationPermission objects for equality.

hashCode

```java
public int hashCode()
```

Returns the hash code value for this object.

**Overrides:** hashCode

in class

BasicPermission
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns the hash code value for this object.

newPermissionCollection

```java
public
PermissionCollection
newPermissionCollection()
```

Returns a PermissionCollection object for storing
DelegationPermission objects.

DelegationPermission objects must be stored in a manner that
allows them to be inserted into the collection in any order, but
that also enables the PermissionCollection implies method to
be implemented in an efficient (and consistent) manner.

**Overrides:** newPermissionCollection

in class

BasicPermission
**Returns:** a new PermissionCollection object suitable for storing
DelegationPermissions.

---

#### newPermissionCollection

public

PermissionCollection

newPermissionCollection()

Returns a PermissionCollection object for storing
DelegationPermission objects.

DelegationPermission objects must be stored in a manner that
allows them to be inserted into the collection in any order, but
that also enables the PermissionCollection implies method to
be implemented in an efficient (and consistent) manner.

---

