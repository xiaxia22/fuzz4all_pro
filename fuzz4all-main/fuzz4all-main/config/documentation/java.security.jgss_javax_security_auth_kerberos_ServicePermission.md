# Class ServicePermission

**Source:** `java.security.jgss\javax\security\auth\kerberos\ServicePermission.html`

### Class Description

```java
public final class
ServicePermission

extends
Permission

implements
Serializable
```

This class is used to protect Kerberos services and the
credentials necessary to access those services. There is a one to
one mapping of a service principal and the credentials necessary
to access the service. Therefore granting access to a service
principal implicitly grants access to the credential necessary to
establish a security context with the service principal. This
applies regardless of whether the credentials are in a cache
or acquired via an exchange with the KDC. The credential can
be either a ticket granting ticket, a service ticket or a secret
key from a key table.

A ServicePermission contains a service principal name and
a list of actions which specify the context the credential can be
used within.

The service principal name is the canonical name of the

KerberosPrincipal

supplying the service, that is
the KerberosPrincipal represents a Kerberos service
principal. This name is treated in a case sensitive manner.
An asterisk may appear by itself, to signify any service principal.

Granting this permission implies that the caller can use a cached
credential (TGT, service ticket or secret key) within the context
designated by the action. In the case of the TGT, granting this
permission also implies that the TGT can be obtained by an
Authentication Service exchange.

Granting this permission also implies creating

KerberosPrincipal

or

GSSName

without providing a Kerberos
realm, as long as the permission's service principal is in this realm.

The possible actions are:

```java
initiate - allow the caller to use the credential to
initiate a security context with a service
principal.

accept - allow the caller to use the credential to
accept security context as a particular
principal.
```

For example, to specify the permission to access to the TGT to
initiate a security context the permission is constructed as follows:

```java
ServicePermission("krbtgt/EXAMPLE.COM@EXAMPLE.COM", "initiate");
```

To obtain a service ticket to initiate a context with the "host"
service the permission is constructed as follows:

```java
ServicePermission("host/foo.example.com@EXAMPLE.COM", "initiate");
```

For a Kerberized server the action is "accept". For example, the permission
necessary to access and use the secret key of the Kerberized "host"
service (telnet and the likes) would be constructed as follows:

```java
ServicePermission("host/foo.example.com@EXAMPLE.COM", "accept");
```

**All Implemented Interfaces:** Serializable

,

Guard

---

### Field Details

*No entries found.*

### Constructor Details

#### public ServicePermission​(
String
servicePrincipal,

String
action)

Create a new

ServicePermission

with the specified

servicePrincipal

and

action

.

**Parameters:**
- servicePrincipal

- the name of the service principal.
An asterisk may appear by itself, to signify any service principal.
- action

- the action string

---

### Method Details

#### public boolean implies​(
Permission
p)

Checks if this Kerberos service permission object "implies" the
specified permission.

More specifically, this method returns true if all of the following
are true (and returns false if any of them are not):

- p

is an instanceof

ServicePermission

,

p

's actions are a proper subset of this

ServicePermission

's actions,

p

's name is equal to this

ServicePermission

's name
or this

ServicePermission

's name is "*".

**Specified by:**
- implies

in class

Permission

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

Checks two ServicePermission objects for equality.

**Specified by:**
- equals

in class

Permission

**Parameters:**
- obj

- the object to test for equality with this object.

**Returns:**
- true if

obj

is a ServicePermission, and has the
same service principal, and actions as this
ServicePermission object.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns the hash code value for this object.

**Specified by:**
- hashCode

in class

Permission

**Returns:**
- a hash code value for this object.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public
String
getActions()

Returns the canonical string representation of the actions.
Always returns present actions in the following order:
initiate, accept.

**Specified by:**
- getActions

in class

Permission

**Returns:**
- the actions of this Permission.

---

#### public
PermissionCollection
newPermissionCollection()

Returns a PermissionCollection object for storing
ServicePermission objects.

ServicePermission objects must be stored in a manner that
allows them to be inserted into the collection in any order, but
that also enables the PermissionCollection implies method to
be implemented in an efficient (and consistent) manner.

**Overrides:**
- newPermissionCollection

in class

Permission

**Returns:**
- a new PermissionCollection object suitable for storing
ServicePermissions.

---

### Additional Sections

#### Class ServicePermission

java.lang.Object

- java.security.Permission
- - javax.security.auth.kerberos.ServicePermission

java.security.Permission

- javax.security.auth.kerberos.ServicePermission

javax.security.auth.kerberos.ServicePermission

**All Implemented Interfaces:** Serializable

,

Guard

```java
public final class
ServicePermission

extends
Permission

implements
Serializable
```

This class is used to protect Kerberos services and the
credentials necessary to access those services. There is a one to
one mapping of a service principal and the credentials necessary
to access the service. Therefore granting access to a service
principal implicitly grants access to the credential necessary to
establish a security context with the service principal. This
applies regardless of whether the credentials are in a cache
or acquired via an exchange with the KDC. The credential can
be either a ticket granting ticket, a service ticket or a secret
key from a key table.

A ServicePermission contains a service principal name and
a list of actions which specify the context the credential can be
used within.

The service principal name is the canonical name of the

KerberosPrincipal

supplying the service, that is
the KerberosPrincipal represents a Kerberos service
principal. This name is treated in a case sensitive manner.
An asterisk may appear by itself, to signify any service principal.

Granting this permission implies that the caller can use a cached
credential (TGT, service ticket or secret key) within the context
designated by the action. In the case of the TGT, granting this
permission also implies that the TGT can be obtained by an
Authentication Service exchange.

Granting this permission also implies creating

KerberosPrincipal

or

GSSName

without providing a Kerberos
realm, as long as the permission's service principal is in this realm.

The possible actions are:

```java
initiate - allow the caller to use the credential to
initiate a security context with a service
principal.

accept - allow the caller to use the credential to
accept security context as a particular
principal.
```

For example, to specify the permission to access to the TGT to
initiate a security context the permission is constructed as follows:

```java
ServicePermission("krbtgt/EXAMPLE.COM@EXAMPLE.COM", "initiate");
```

To obtain a service ticket to initiate a context with the "host"
service the permission is constructed as follows:

```java
ServicePermission("host/foo.example.com@EXAMPLE.COM", "initiate");
```

For a Kerberized server the action is "accept". For example, the permission
necessary to access and use the secret key of the Kerberized "host"
service (telnet and the likes) would be constructed as follows:

```java
ServicePermission("host/foo.example.com@EXAMPLE.COM", "accept");
```

**Since:** 1.4
**See Also:** Serialized Form

public final class

ServicePermission

extends

Permission

implements

Serializable

This class is used to protect Kerberos services and the
credentials necessary to access those services. There is a one to
one mapping of a service principal and the credentials necessary
to access the service. Therefore granting access to a service
principal implicitly grants access to the credential necessary to
establish a security context with the service principal. This
applies regardless of whether the credentials are in a cache
or acquired via an exchange with the KDC. The credential can
be either a ticket granting ticket, a service ticket or a secret
key from a key table.

A ServicePermission contains a service principal name and
a list of actions which specify the context the credential can be
used within.

The service principal name is the canonical name of the

KerberosPrincipal

supplying the service, that is
the KerberosPrincipal represents a Kerberos service
principal. This name is treated in a case sensitive manner.
An asterisk may appear by itself, to signify any service principal.

Granting this permission implies that the caller can use a cached
credential (TGT, service ticket or secret key) within the context
designated by the action. In the case of the TGT, granting this
permission also implies that the TGT can be obtained by an
Authentication Service exchange.

Granting this permission also implies creating

KerberosPrincipal

or

GSSName

without providing a Kerberos
realm, as long as the permission's service principal is in this realm.

The possible actions are:

```java
initiate - allow the caller to use the credential to
initiate a security context with a service
principal.

accept - allow the caller to use the credential to
accept security context as a particular
principal.
```

For example, to specify the permission to access to the TGT to
initiate a security context the permission is constructed as follows:

```java
ServicePermission("krbtgt/EXAMPLE.COM@EXAMPLE.COM", "initiate");
```

To obtain a service ticket to initiate a context with the "host"
service the permission is constructed as follows:

```java
ServicePermission("host/foo.example.com@EXAMPLE.COM", "initiate");
```

For a Kerberized server the action is "accept". For example, the permission
necessary to access and use the secret key of the Kerberized "host"
service (telnet and the likes) would be constructed as follows:

```java
ServicePermission("host/foo.example.com@EXAMPLE.COM", "accept");
```

A ServicePermission contains a service principal name and
a list of actions which specify the context the credential can be
used within.

The service principal name is the canonical name of the

KerberosPrincipal

supplying the service, that is
the KerberosPrincipal represents a Kerberos service
principal. This name is treated in a case sensitive manner.
An asterisk may appear by itself, to signify any service principal.

Granting this permission implies that the caller can use a cached
credential (TGT, service ticket or secret key) within the context
designated by the action. In the case of the TGT, granting this
permission also implies that the TGT can be obtained by an
Authentication Service exchange.

Granting this permission also implies creating

KerberosPrincipal

or

GSSName

without providing a Kerberos
realm, as long as the permission's service principal is in this realm.

The possible actions are:

```java
initiate - allow the caller to use the credential to
initiate a security context with a service
principal.

accept - allow the caller to use the credential to
accept security context as a particular
principal.
```

For example, to specify the permission to access to the TGT to
initiate a security context the permission is constructed as follows:

```java
ServicePermission("krbtgt/EXAMPLE.COM@EXAMPLE.COM", "initiate");
```

To obtain a service ticket to initiate a context with the "host"
service the permission is constructed as follows:

```java
ServicePermission("host/foo.example.com@EXAMPLE.COM", "initiate");
```

For a Kerberized server the action is "accept". For example, the permission
necessary to access and use the secret key of the Kerberized "host"
service (telnet and the likes) would be constructed as follows:

```java
ServicePermission("host/foo.example.com@EXAMPLE.COM", "accept");
```

The service principal name is the canonical name of the

KerberosPrincipal

supplying the service, that is
the KerberosPrincipal represents a Kerberos service
principal. This name is treated in a case sensitive manner.
An asterisk may appear by itself, to signify any service principal.

Granting this permission implies that the caller can use a cached
credential (TGT, service ticket or secret key) within the context
designated by the action. In the case of the TGT, granting this
permission also implies that the TGT can be obtained by an
Authentication Service exchange.

Granting this permission also implies creating

KerberosPrincipal

or

GSSName

without providing a Kerberos
realm, as long as the permission's service principal is in this realm.

The possible actions are:

```java
initiate - allow the caller to use the credential to
initiate a security context with a service
principal.

accept - allow the caller to use the credential to
accept security context as a particular
principal.
```

For example, to specify the permission to access to the TGT to
initiate a security context the permission is constructed as follows:

```java
ServicePermission("krbtgt/EXAMPLE.COM@EXAMPLE.COM", "initiate");
```

To obtain a service ticket to initiate a context with the "host"
service the permission is constructed as follows:

```java
ServicePermission("host/foo.example.com@EXAMPLE.COM", "initiate");
```

For a Kerberized server the action is "accept". For example, the permission
necessary to access and use the secret key of the Kerberized "host"
service (telnet and the likes) would be constructed as follows:

```java
ServicePermission("host/foo.example.com@EXAMPLE.COM", "accept");
```

Granting this permission implies that the caller can use a cached
credential (TGT, service ticket or secret key) within the context
designated by the action. In the case of the TGT, granting this
permission also implies that the TGT can be obtained by an
Authentication Service exchange.

Granting this permission also implies creating

KerberosPrincipal

or

GSSName

without providing a Kerberos
realm, as long as the permission's service principal is in this realm.

The possible actions are:

```java
initiate - allow the caller to use the credential to
initiate a security context with a service
principal.

accept - allow the caller to use the credential to
accept security context as a particular
principal.
```

For example, to specify the permission to access to the TGT to
initiate a security context the permission is constructed as follows:

```java
ServicePermission("krbtgt/EXAMPLE.COM@EXAMPLE.COM", "initiate");
```

To obtain a service ticket to initiate a context with the "host"
service the permission is constructed as follows:

```java
ServicePermission("host/foo.example.com@EXAMPLE.COM", "initiate");
```

For a Kerberized server the action is "accept". For example, the permission
necessary to access and use the secret key of the Kerberized "host"
service (telnet and the likes) would be constructed as follows:

```java
ServicePermission("host/foo.example.com@EXAMPLE.COM", "accept");
```

Granting this permission also implies creating

KerberosPrincipal

or

GSSName

without providing a Kerberos
realm, as long as the permission's service principal is in this realm.

The possible actions are:

```java
initiate - allow the caller to use the credential to
initiate a security context with a service
principal.

accept - allow the caller to use the credential to
accept security context as a particular
principal.
```

For example, to specify the permission to access to the TGT to
initiate a security context the permission is constructed as follows:

```java
ServicePermission("krbtgt/EXAMPLE.COM@EXAMPLE.COM", "initiate");
```

To obtain a service ticket to initiate a context with the "host"
service the permission is constructed as follows:

```java
ServicePermission("host/foo.example.com@EXAMPLE.COM", "initiate");
```

For a Kerberized server the action is "accept". For example, the permission
necessary to access and use the secret key of the Kerberized "host"
service (telnet and the likes) would be constructed as follows:

```java
ServicePermission("host/foo.example.com@EXAMPLE.COM", "accept");
```

The possible actions are:

```java
initiate - allow the caller to use the credential to
initiate a security context with a service
principal.

accept - allow the caller to use the credential to
accept security context as a particular
principal.
```

For example, to specify the permission to access to the TGT to
initiate a security context the permission is constructed as follows:

```java
ServicePermission("krbtgt/EXAMPLE.COM@EXAMPLE.COM", "initiate");
```

To obtain a service ticket to initiate a context with the "host"
service the permission is constructed as follows:

```java
ServicePermission("host/foo.example.com@EXAMPLE.COM", "initiate");
```

For a Kerberized server the action is "accept". For example, the permission
necessary to access and use the secret key of the Kerberized "host"
service (telnet and the likes) would be constructed as follows:

```java
ServicePermission("host/foo.example.com@EXAMPLE.COM", "accept");
```

initiate - allow the caller to use the credential to
initiate a security context with a service
principal.

accept - allow the caller to use the credential to
accept security context as a particular
principal.

ServicePermission("krbtgt/EXAMPLE.COM@EXAMPLE.COM", "initiate");

To obtain a service ticket to initiate a context with the "host"
service the permission is constructed as follows:

```java
ServicePermission("host/foo.example.com@EXAMPLE.COM", "initiate");
```

For a Kerberized server the action is "accept". For example, the permission
necessary to access and use the secret key of the Kerberized "host"
service (telnet and the likes) would be constructed as follows:

```java
ServicePermission("host/foo.example.com@EXAMPLE.COM", "accept");
```

ServicePermission("host/foo.example.com@EXAMPLE.COM", "initiate");

For a Kerberized server the action is "accept". For example, the permission
necessary to access and use the secret key of the Kerberized "host"
service (telnet and the likes) would be constructed as follows:

```java
ServicePermission("host/foo.example.com@EXAMPLE.COM", "accept");
```

ServicePermission("host/foo.example.com@EXAMPLE.COM", "accept");

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ServicePermission

​(

String

servicePrincipal,

String

action)

Create a new

ServicePermission

with the specified

servicePrincipal

and

action

.

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

Checks two ServicePermission objects for equality.

String

getActions

()

Returns the canonical string representation of the actions.

int

hashCode

()

Returns the hash code value for this object.

boolean

implies

​(

Permission

p)

Checks if this Kerberos service permission object "implies" the
specified permission.

PermissionCollection

newPermissionCollection

()

Returns a PermissionCollection object for storing
ServicePermission objects.

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

ServicePermission

​(

String

servicePrincipal,

String

action)

Create a new

ServicePermission

with the specified

servicePrincipal

and

action

.

---

#### Constructor Summary

Create a new

ServicePermission

with the specified

servicePrincipal

and

action

.

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

Checks two ServicePermission objects for equality.

String

getActions

()

Returns the canonical string representation of the actions.

int

hashCode

()

Returns the hash code value for this object.

boolean

implies

​(

Permission

p)

Checks if this Kerberos service permission object "implies" the
specified permission.

PermissionCollection

newPermissionCollection

()

Returns a PermissionCollection object for storing
ServicePermission objects.

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

Checks two ServicePermission objects for equality.

Returns the canonical string representation of the actions.

Returns the hash code value for this object.

Checks if this Kerberos service permission object "implies" the
specified permission.

Returns a PermissionCollection object for storing
ServicePermission objects.

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

- ServicePermission

```java
public ServicePermission​(
String
servicePrincipal,

String
action)
```

Create a new

ServicePermission

with the specified

servicePrincipal

and

action

.

**Parameters:** servicePrincipal

- the name of the service principal.
An asterisk may appear by itself, to signify any service principal.
**Parameters:** action

- the action string

============ METHOD DETAIL ==========

- Method Detail

- implies

```java
public boolean implies​(
Permission
p)
```

Checks if this Kerberos service permission object "implies" the
specified permission.

More specifically, this method returns true if all of the following
are true (and returns false if any of them are not):

- p

is an instanceof

ServicePermission

,

p

's actions are a proper subset of this

ServicePermission

's actions,

p

's name is equal to this

ServicePermission

's name
or this

ServicePermission

's name is "*".

**Specified by:** implies

in class

Permission
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

Checks two ServicePermission objects for equality.

**Specified by:** equals

in class

Permission
**Parameters:** obj

- the object to test for equality with this object.
**Returns:** true if

obj

is a ServicePermission, and has the
same service principal, and actions as this
ServicePermission object.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this object.

**Specified by:** hashCode

in class

Permission
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- getActions

```java
public
String
getActions()
```

Returns the canonical string representation of the actions.
Always returns present actions in the following order:
initiate, accept.

**Specified by:** getActions

in class

Permission
**Returns:** the actions of this Permission.

- newPermissionCollection

```java
public
PermissionCollection
newPermissionCollection()
```

Returns a PermissionCollection object for storing
ServicePermission objects.

ServicePermission objects must be stored in a manner that
allows them to be inserted into the collection in any order, but
that also enables the PermissionCollection implies method to
be implemented in an efficient (and consistent) manner.

**Overrides:** newPermissionCollection

in class

Permission
**Returns:** a new PermissionCollection object suitable for storing
ServicePermissions.

Constructor Detail

- ServicePermission

```java
public ServicePermission​(
String
servicePrincipal,

String
action)
```

Create a new

ServicePermission

with the specified

servicePrincipal

and

action

.

**Parameters:** servicePrincipal

- the name of the service principal.
An asterisk may appear by itself, to signify any service principal.
**Parameters:** action

- the action string

---

#### Constructor Detail

ServicePermission

```java
public ServicePermission​(
String
servicePrincipal,

String
action)
```

Create a new

ServicePermission

with the specified

servicePrincipal

and

action

.

**Parameters:** servicePrincipal

- the name of the service principal.
An asterisk may appear by itself, to signify any service principal.
**Parameters:** action

- the action string

---

#### ServicePermission

public ServicePermission​(

String

servicePrincipal,

String

action)

Create a new

ServicePermission

with the specified

servicePrincipal

and

action

.

Method Detail

- implies

```java
public boolean implies​(
Permission
p)
```

Checks if this Kerberos service permission object "implies" the
specified permission.

More specifically, this method returns true if all of the following
are true (and returns false if any of them are not):

- p

is an instanceof

ServicePermission

,

p

's actions are a proper subset of this

ServicePermission

's actions,

p

's name is equal to this

ServicePermission

's name
or this

ServicePermission

's name is "*".

**Specified by:** implies

in class

Permission
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

Checks two ServicePermission objects for equality.

**Specified by:** equals

in class

Permission
**Parameters:** obj

- the object to test for equality with this object.
**Returns:** true if

obj

is a ServicePermission, and has the
same service principal, and actions as this
ServicePermission object.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this object.

**Specified by:** hashCode

in class

Permission
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- getActions

```java
public
String
getActions()
```

Returns the canonical string representation of the actions.
Always returns present actions in the following order:
initiate, accept.

**Specified by:** getActions

in class

Permission
**Returns:** the actions of this Permission.

- newPermissionCollection

```java
public
PermissionCollection
newPermissionCollection()
```

Returns a PermissionCollection object for storing
ServicePermission objects.

ServicePermission objects must be stored in a manner that
allows them to be inserted into the collection in any order, but
that also enables the PermissionCollection implies method to
be implemented in an efficient (and consistent) manner.

**Overrides:** newPermissionCollection

in class

Permission
**Returns:** a new PermissionCollection object suitable for storing
ServicePermissions.

---

#### Method Detail

implies

```java
public boolean implies​(
Permission
p)
```

Checks if this Kerberos service permission object "implies" the
specified permission.

More specifically, this method returns true if all of the following
are true (and returns false if any of them are not):

- p

is an instanceof

ServicePermission

,

p

's actions are a proper subset of this

ServicePermission

's actions,

p

's name is equal to this

ServicePermission

's name
or this

ServicePermission

's name is "*".

**Specified by:** implies

in class

Permission
**Parameters:** p

- the permission to check against.
**Returns:** true if the specified permission is implied by this object,
false if not.

---

#### implies

public boolean implies​(

Permission

p)

Checks if this Kerberos service permission object "implies" the
specified permission.

More specifically, this method returns true if all of the following
are true (and returns false if any of them are not):

- p

is an instanceof

ServicePermission

,

p

's actions are a proper subset of this

ServicePermission

's actions,

p

's name is equal to this

ServicePermission

's name
or this

ServicePermission

's name is "*".

More specifically, this method returns true if all of the following
are true (and returns false if any of them are not):

- p

is an instanceof

ServicePermission

,

p

's actions are a proper subset of this

ServicePermission

's actions,

p

's name is equal to this

ServicePermission

's name
or this

ServicePermission

's name is "*".

p

is an instanceof

ServicePermission

,

p

's actions are a proper subset of this

ServicePermission

's actions,

p

's name is equal to this

ServicePermission

's name
or this

ServicePermission

's name is "*".

equals

```java
public boolean equals​(
Object
obj)
```

Checks two ServicePermission objects for equality.

**Specified by:** equals

in class

Permission
**Parameters:** obj

- the object to test for equality with this object.
**Returns:** true if

obj

is a ServicePermission, and has the
same service principal, and actions as this
ServicePermission object.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Checks two ServicePermission objects for equality.

hashCode

```java
public int hashCode()
```

Returns the hash code value for this object.

**Specified by:** hashCode

in class

Permission
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns the hash code value for this object.

getActions

```java
public
String
getActions()
```

Returns the canonical string representation of the actions.
Always returns present actions in the following order:
initiate, accept.

**Specified by:** getActions

in class

Permission
**Returns:** the actions of this Permission.

---

#### getActions

public

String

getActions()

Returns the canonical string representation of the actions.
Always returns present actions in the following order:
initiate, accept.

newPermissionCollection

```java
public
PermissionCollection
newPermissionCollection()
```

Returns a PermissionCollection object for storing
ServicePermission objects.

ServicePermission objects must be stored in a manner that
allows them to be inserted into the collection in any order, but
that also enables the PermissionCollection implies method to
be implemented in an efficient (and consistent) manner.

**Overrides:** newPermissionCollection

in class

Permission
**Returns:** a new PermissionCollection object suitable for storing
ServicePermissions.

---

#### newPermissionCollection

public

PermissionCollection

newPermissionCollection()

Returns a PermissionCollection object for storing
ServicePermission objects.

ServicePermission objects must be stored in a manner that
allows them to be inserted into the collection in any order, but
that also enables the PermissionCollection implies method to
be implemented in an efficient (and consistent) manner.

---

