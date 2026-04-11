# Class PolicySpi

**Source:** `java.base\java\security\PolicySpi.html`

### Class Description

```java
public abstract class
PolicySpi

extends
Object
```

This class defines the

Service Provider Interface

(

SPI

)
for the

Policy

class.
All the abstract methods in this class must be implemented by each
service provider who wishes to supply a Policy implementation.

Subclass implementations of this abstract class must provide
a public constructor that takes a

Policy.Parameters

object as an input parameter. This constructor also must throw
an IllegalArgumentException if it does not understand the

Policy.Parameters

input.

**Since:** 1.6

---

### Field Details

*No entries found.*

### Constructor Details

#### public PolicySpi()

*No description found.*

---

### Method Details

#### protected abstract boolean engineImplies​(
ProtectionDomain
domain,

Permission
permission)

Check whether the policy has granted a Permission to a ProtectionDomain.

**Parameters:**
- domain

- the ProtectionDomain to check.
- permission

- check whether this permission is granted to the
specified domain.

**Returns:**
- boolean true if the permission is granted to the domain.

---

#### protected void engineRefresh()

Refreshes/reloads the policy configuration. The behavior of this method
depends on the implementation. For example, calling

refresh

on a file-based policy will cause the file to be re-read.

The default implementation of this method does nothing.
This method should be overridden if a refresh operation is supported
by the policy implementation.

---

#### protected
PermissionCollection
engineGetPermissions​(
CodeSource
codesource)

Return a PermissionCollection object containing the set of
permissions granted to the specified CodeSource.

The default implementation of this method returns
Policy.UNSUPPORTED_EMPTY_COLLECTION object. This method can be
overridden if the policy implementation can return a set of
permissions granted to a CodeSource.

**Parameters:**
- codesource

- the CodeSource to which the returned
PermissionCollection has been granted.

**Returns:**
- a set of permissions granted to the specified CodeSource.
If this operation is supported, the returned
set of permissions must be a new mutable instance
and it must support heterogeneous Permission types.
If this operation is not supported,
Policy.UNSUPPORTED_EMPTY_COLLECTION is returned.

---

#### protected
PermissionCollection
engineGetPermissions​(
ProtectionDomain
domain)

Return a PermissionCollection object containing the set of
permissions granted to the specified ProtectionDomain.

The default implementation of this method returns
Policy.UNSUPPORTED_EMPTY_COLLECTION object. This method can be
overridden if the policy implementation can return a set of
permissions granted to a ProtectionDomain.

**Parameters:**
- domain

- the ProtectionDomain to which the returned
PermissionCollection has been granted.

**Returns:**
- a set of permissions granted to the specified ProtectionDomain.
If this operation is supported, the returned
set of permissions must be a new mutable instance
and it must support heterogeneous Permission types.
If this operation is not supported,
Policy.UNSUPPORTED_EMPTY_COLLECTION is returned.

---

### Additional Sections

#### Class PolicySpi

java.lang.Object

- java.security.PolicySpi

java.security.PolicySpi

```java
public abstract class
PolicySpi

extends
Object
```

This class defines the

Service Provider Interface

(

SPI

)
for the

Policy

class.
All the abstract methods in this class must be implemented by each
service provider who wishes to supply a Policy implementation.

Subclass implementations of this abstract class must provide
a public constructor that takes a

Policy.Parameters

object as an input parameter. This constructor also must throw
an IllegalArgumentException if it does not understand the

Policy.Parameters

input.

**Since:** 1.6

public abstract class

PolicySpi

extends

Object

This class defines the

Service Provider Interface

(

SPI

)
for the

Policy

class.
All the abstract methods in this class must be implemented by each
service provider who wishes to supply a Policy implementation.

Subclass implementations of this abstract class must provide
a public constructor that takes a

Policy.Parameters

object as an input parameter. This constructor also must throw
an IllegalArgumentException if it does not understand the

Policy.Parameters

input.

Subclass implementations of this abstract class must provide
a public constructor that takes a

Policy.Parameters

object as an input parameter. This constructor also must throw
an IllegalArgumentException if it does not understand the

Policy.Parameters

input.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

PolicySpi

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

protected

PermissionCollection

engineGetPermissions

​(

CodeSource

codesource)

Return a PermissionCollection object containing the set of
permissions granted to the specified CodeSource.

protected

PermissionCollection

engineGetPermissions

​(

ProtectionDomain

domain)

Return a PermissionCollection object containing the set of
permissions granted to the specified ProtectionDomain.

protected abstract boolean

engineImplies

​(

ProtectionDomain

domain,

Permission

permission)

Check whether the policy has granted a Permission to a ProtectionDomain.

protected void

engineRefresh

()

Refreshes/reloads the policy configuration.

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

toString

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

PolicySpi

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

protected

PermissionCollection

engineGetPermissions

​(

CodeSource

codesource)

Return a PermissionCollection object containing the set of
permissions granted to the specified CodeSource.

protected

PermissionCollection

engineGetPermissions

​(

ProtectionDomain

domain)

Return a PermissionCollection object containing the set of
permissions granted to the specified ProtectionDomain.

protected abstract boolean

engineImplies

​(

ProtectionDomain

domain,

Permission

permission)

Check whether the policy has granted a Permission to a ProtectionDomain.

protected void

engineRefresh

()

Refreshes/reloads the policy configuration.

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

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Return a PermissionCollection object containing the set of
permissions granted to the specified CodeSource.

Return a PermissionCollection object containing the set of
permissions granted to the specified ProtectionDomain.

Check whether the policy has granted a Permission to a ProtectionDomain.

Refreshes/reloads the policy configuration.

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

- PolicySpi

```java
public PolicySpi()
```

============ METHOD DETAIL ==========

- Method Detail

- engineImplies

```java
protected abstract boolean engineImplies​(
ProtectionDomain
domain,

Permission
permission)
```

Check whether the policy has granted a Permission to a ProtectionDomain.

**Parameters:** domain

- the ProtectionDomain to check.
**Parameters:** permission

- check whether this permission is granted to the
specified domain.
**Returns:** boolean true if the permission is granted to the domain.

- engineRefresh

```java
protected void engineRefresh()
```

Refreshes/reloads the policy configuration. The behavior of this method
depends on the implementation. For example, calling

refresh

on a file-based policy will cause the file to be re-read.

The default implementation of this method does nothing.
This method should be overridden if a refresh operation is supported
by the policy implementation.

- engineGetPermissions

```java
protected
PermissionCollection
engineGetPermissions​(
CodeSource
codesource)
```

Return a PermissionCollection object containing the set of
permissions granted to the specified CodeSource.

The default implementation of this method returns
Policy.UNSUPPORTED_EMPTY_COLLECTION object. This method can be
overridden if the policy implementation can return a set of
permissions granted to a CodeSource.

**Parameters:** codesource

- the CodeSource to which the returned
PermissionCollection has been granted.
**Returns:** a set of permissions granted to the specified CodeSource.
If this operation is supported, the returned
set of permissions must be a new mutable instance
and it must support heterogeneous Permission types.
If this operation is not supported,
Policy.UNSUPPORTED_EMPTY_COLLECTION is returned.

- engineGetPermissions

```java
protected
PermissionCollection
engineGetPermissions​(
ProtectionDomain
domain)
```

Return a PermissionCollection object containing the set of
permissions granted to the specified ProtectionDomain.

The default implementation of this method returns
Policy.UNSUPPORTED_EMPTY_COLLECTION object. This method can be
overridden if the policy implementation can return a set of
permissions granted to a ProtectionDomain.

**Parameters:** domain

- the ProtectionDomain to which the returned
PermissionCollection has been granted.
**Returns:** a set of permissions granted to the specified ProtectionDomain.
If this operation is supported, the returned
set of permissions must be a new mutable instance
and it must support heterogeneous Permission types.
If this operation is not supported,
Policy.UNSUPPORTED_EMPTY_COLLECTION is returned.

Constructor Detail

- PolicySpi

```java
public PolicySpi()
```

---

#### Constructor Detail

PolicySpi

```java
public PolicySpi()
```

---

#### PolicySpi

public PolicySpi()

Method Detail

- engineImplies

```java
protected abstract boolean engineImplies​(
ProtectionDomain
domain,

Permission
permission)
```

Check whether the policy has granted a Permission to a ProtectionDomain.

**Parameters:** domain

- the ProtectionDomain to check.
**Parameters:** permission

- check whether this permission is granted to the
specified domain.
**Returns:** boolean true if the permission is granted to the domain.

- engineRefresh

```java
protected void engineRefresh()
```

Refreshes/reloads the policy configuration. The behavior of this method
depends on the implementation. For example, calling

refresh

on a file-based policy will cause the file to be re-read.

The default implementation of this method does nothing.
This method should be overridden if a refresh operation is supported
by the policy implementation.

- engineGetPermissions

```java
protected
PermissionCollection
engineGetPermissions​(
CodeSource
codesource)
```

Return a PermissionCollection object containing the set of
permissions granted to the specified CodeSource.

The default implementation of this method returns
Policy.UNSUPPORTED_EMPTY_COLLECTION object. This method can be
overridden if the policy implementation can return a set of
permissions granted to a CodeSource.

**Parameters:** codesource

- the CodeSource to which the returned
PermissionCollection has been granted.
**Returns:** a set of permissions granted to the specified CodeSource.
If this operation is supported, the returned
set of permissions must be a new mutable instance
and it must support heterogeneous Permission types.
If this operation is not supported,
Policy.UNSUPPORTED_EMPTY_COLLECTION is returned.

- engineGetPermissions

```java
protected
PermissionCollection
engineGetPermissions​(
ProtectionDomain
domain)
```

Return a PermissionCollection object containing the set of
permissions granted to the specified ProtectionDomain.

The default implementation of this method returns
Policy.UNSUPPORTED_EMPTY_COLLECTION object. This method can be
overridden if the policy implementation can return a set of
permissions granted to a ProtectionDomain.

**Parameters:** domain

- the ProtectionDomain to which the returned
PermissionCollection has been granted.
**Returns:** a set of permissions granted to the specified ProtectionDomain.
If this operation is supported, the returned
set of permissions must be a new mutable instance
and it must support heterogeneous Permission types.
If this operation is not supported,
Policy.UNSUPPORTED_EMPTY_COLLECTION is returned.

---

#### Method Detail

engineImplies

```java
protected abstract boolean engineImplies​(
ProtectionDomain
domain,

Permission
permission)
```

Check whether the policy has granted a Permission to a ProtectionDomain.

**Parameters:** domain

- the ProtectionDomain to check.
**Parameters:** permission

- check whether this permission is granted to the
specified domain.
**Returns:** boolean true if the permission is granted to the domain.

---

#### engineImplies

protected abstract boolean engineImplies​(

ProtectionDomain

domain,

Permission

permission)

Check whether the policy has granted a Permission to a ProtectionDomain.

engineRefresh

```java
protected void engineRefresh()
```

Refreshes/reloads the policy configuration. The behavior of this method
depends on the implementation. For example, calling

refresh

on a file-based policy will cause the file to be re-read.

The default implementation of this method does nothing.
This method should be overridden if a refresh operation is supported
by the policy implementation.

---

#### engineRefresh

protected void engineRefresh()

Refreshes/reloads the policy configuration. The behavior of this method
depends on the implementation. For example, calling

refresh

on a file-based policy will cause the file to be re-read.

The default implementation of this method does nothing.
This method should be overridden if a refresh operation is supported
by the policy implementation.

The default implementation of this method does nothing.
This method should be overridden if a refresh operation is supported
by the policy implementation.

engineGetPermissions

```java
protected
PermissionCollection
engineGetPermissions​(
CodeSource
codesource)
```

Return a PermissionCollection object containing the set of
permissions granted to the specified CodeSource.

The default implementation of this method returns
Policy.UNSUPPORTED_EMPTY_COLLECTION object. This method can be
overridden if the policy implementation can return a set of
permissions granted to a CodeSource.

**Parameters:** codesource

- the CodeSource to which the returned
PermissionCollection has been granted.
**Returns:** a set of permissions granted to the specified CodeSource.
If this operation is supported, the returned
set of permissions must be a new mutable instance
and it must support heterogeneous Permission types.
If this operation is not supported,
Policy.UNSUPPORTED_EMPTY_COLLECTION is returned.

---

#### engineGetPermissions

protected

PermissionCollection

engineGetPermissions​(

CodeSource

codesource)

Return a PermissionCollection object containing the set of
permissions granted to the specified CodeSource.

The default implementation of this method returns
Policy.UNSUPPORTED_EMPTY_COLLECTION object. This method can be
overridden if the policy implementation can return a set of
permissions granted to a CodeSource.

The default implementation of this method returns
Policy.UNSUPPORTED_EMPTY_COLLECTION object. This method can be
overridden if the policy implementation can return a set of
permissions granted to a CodeSource.

engineGetPermissions

```java
protected
PermissionCollection
engineGetPermissions​(
ProtectionDomain
domain)
```

Return a PermissionCollection object containing the set of
permissions granted to the specified ProtectionDomain.

The default implementation of this method returns
Policy.UNSUPPORTED_EMPTY_COLLECTION object. This method can be
overridden if the policy implementation can return a set of
permissions granted to a ProtectionDomain.

**Parameters:** domain

- the ProtectionDomain to which the returned
PermissionCollection has been granted.
**Returns:** a set of permissions granted to the specified ProtectionDomain.
If this operation is supported, the returned
set of permissions must be a new mutable instance
and it must support heterogeneous Permission types.
If this operation is not supported,
Policy.UNSUPPORTED_EMPTY_COLLECTION is returned.

---

#### engineGetPermissions

protected

PermissionCollection

engineGetPermissions​(

ProtectionDomain

domain)

Return a PermissionCollection object containing the set of
permissions granted to the specified ProtectionDomain.

The default implementation of this method returns
Policy.UNSUPPORTED_EMPTY_COLLECTION object. This method can be
overridden if the policy implementation can return a set of
permissions granted to a ProtectionDomain.

The default implementation of this method returns
Policy.UNSUPPORTED_EMPTY_COLLECTION object. This method can be
overridden if the policy implementation can return a set of
permissions granted to a ProtectionDomain.

---

