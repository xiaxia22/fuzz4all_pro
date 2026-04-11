# Class Policy

**Source:** `java.base\java\security\Policy.html`

### Class Description

```java
public abstract class
Policy

extends
Object
```

A Policy object is responsible for determining whether code executing
in the Java runtime environment has permission to perform a
security-sensitive operation.

There is only one Policy object installed in the runtime at any
given time. A Policy object can be installed by calling the

setPolicy

method. The installed Policy object can be
obtained by calling the

getPolicy

method.

If no Policy object has been installed in the runtime, a call to

getPolicy

installs an instance of the default Policy
implementation (a default subclass implementation of this abstract class).
The default Policy implementation can be changed by setting the value
of the

policy.provider

security property to the fully qualified
name of the desired Policy subclass implementation. The system class loader
is used to load this class.

Application code can directly subclass Policy to provide a custom
implementation. In addition, an instance of a Policy object can be
constructed by invoking one of the

getInstance

factory methods
with a standard type. The default policy type is "JavaPolicy".

Once a Policy instance has been installed (either by default, or by
calling

setPolicy

), the Java runtime invokes its

implies

method when it needs to
determine whether executing code (encapsulated in a ProtectionDomain)
can perform SecurityManager-protected operations. How a Policy object
retrieves its policy data is up to the Policy implementation itself.
The policy data may be stored, for example, in a flat ASCII file,
in a serialized binary file of the Policy class, or in a database.

The

refresh

method causes the policy object to
refresh/reload its data. This operation is implementation-dependent.
For example, if the policy object stores its data in configuration files,
calling

refresh

will cause it to re-read the configuration
policy files. If a refresh operation is not supported, this method does
nothing. Note that refreshed policy may not have an effect on classes
in a particular ProtectionDomain. This is dependent on the Policy
provider's implementation of the

implies

method and its PermissionCollection caching strategy.

**Since:** 1.2
**See Also:** Provider

,

ProtectionDomain

,

Permission

,

security properties

---

### Field Details

#### public static final
PermissionCollection
UNSUPPORTED_EMPTY_COLLECTION

A read-only empty PermissionCollection instance.

**Since:**
- 1.6

---

### Constructor Details

#### public Policy()

*No description found.*

---

### Method Details

#### public static
Policy
getPolicy()

Returns the installed Policy object. This value should not be cached,
as it may be changed by a call to

setPolicy

.
This method first calls

SecurityManager.checkPermission

with a

SecurityPermission("getPolicy")

permission
to ensure it's ok to get the Policy object.

**Returns:**
- the installed Policy.

**Throws:**
- SecurityException

- if a security manager exists and its

checkPermission

method doesn't allow
getting the Policy object.

**See Also:**
- SecurityManager.checkPermission(Permission)

,

setPolicy(java.security.Policy)

---

#### public static void setPolicy​(
Policy
p)

Sets the system-wide Policy object. This method first calls

SecurityManager.checkPermission

with a

SecurityPermission("setPolicy")

permission to ensure it's ok to set the Policy.

**Parameters:**
- p

- the new system Policy object.

**Throws:**
- SecurityException

- if a security manager exists and its

checkPermission

method doesn't allow
setting the Policy.

**See Also:**
- SecurityManager.checkPermission(Permission)

,

getPolicy()

---

#### public static
Policy
getInstance​(
String
type,

Policy.Parameters
params)
throws
NoSuchAlgorithmException

Returns a Policy object of the specified type.

This method traverses the list of registered security providers,
starting with the most preferred Provider.
A new Policy object encapsulating the
PolicySpi implementation from the first
Provider that supports the specified type is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:**
- type

- the specified Policy type. See the Policy section in the

Java Security Standard Algorithm Names Specification

for a list of standard Policy types.
- params

- parameters for the Policy, which may be null.

**Returns:**
- the new

Policy

object

**Throws:**
- IllegalArgumentException

- if the specified parameters
are not understood by the

PolicySpi

implementation
from the selected

Provider
- NoSuchAlgorithmException

- if no

Provider

supports
a

PolicySpi

implementation for the specified type
- NullPointerException

- if

type

is

null
- SecurityException

- if the caller does not have permission
to get a

Policy

instance for the specified type.

**See Also:**
- Provider

**Since:**
- 1.6

**Implementation Note:**
- The JDK Reference Implementation additionally uses the

jdk.security.provider.preferred

Security

property to determine
the preferred provider order for the specified algorithm. This
may be different than the order of providers returned by

Security.getProviders()

.

---

#### public static
Policy
getInstance​(
String
type,

Policy.Parameters
params,

String
provider)
throws
NoSuchProviderException
,

NoSuchAlgorithmException

Returns a Policy object of the specified type.

A new Policy object encapsulating the
PolicySpi implementation from the specified provider
is returned. The specified provider must be registered
in the provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:**
- type

- the specified Policy type. See the Policy section in the

Java Security Standard Algorithm Names Specification

for a list of standard Policy types.
- params

- parameters for the Policy, which may be null.
- provider

- the provider.

**Returns:**
- the new

Policy

object

**Throws:**
- IllegalArgumentException

- if the specified provider
is

null

or empty, or if the specified parameters are
not understood by the

PolicySpi

implementation from
the specified provider
- NoSuchAlgorithmException

- if the specified provider does not
support a

PolicySpi

implementation for the specified
type
- NoSuchProviderException

- if the specified provider is not
registered in the security provider list
- NullPointerException

- if

type

is

null
- SecurityException

- if the caller does not have permission
to get a

Policy

instance for the specified type

**See Also:**
- Provider

**Since:**
- 1.6

---

#### public static
Policy
getInstance​(
String
type,

Policy.Parameters
params,

Provider
provider)
throws
NoSuchAlgorithmException

Returns a Policy object of the specified type.

A new Policy object encapsulating the
PolicySpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

**Parameters:**
- type

- the specified Policy type. See the Policy section in the

Java Security Standard Algorithm Names Specification

for a list of standard Policy types.
- params

- parameters for the Policy, which may be null.
- provider

- the Provider.

**Returns:**
- the new

Policy

object

**Throws:**
- IllegalArgumentException

- if the specified

Provider

is

null

, or if the specified parameters are not
understood by the

PolicySpi

implementation from the
specified

Provider
- NoSuchAlgorithmException

- if the specified

Provider

does not support a

PolicySpi

implementation for
the specified type
- NullPointerException

- if

type

is

null
- SecurityException

- if the caller does not have permission
to get a

Policy

instance for the specified type

**See Also:**
- Provider

**Since:**
- 1.6

---

#### public
Provider
getProvider()

Return the Provider of this Policy.

This Policy instance will only have a Provider if it
was obtained via a call to

Policy.getInstance

.
Otherwise this method returns null.

**Returns:**
- the Provider of this Policy, or null.

**Since:**
- 1.6

---

#### public
String
getType()

Return the type of this Policy.

This Policy instance will only have a type if it
was obtained via a call to

Policy.getInstance

.
Otherwise this method returns null.

**Returns:**
- the type of this Policy, or null.

**Since:**
- 1.6

---

#### public
Policy.Parameters
getParameters()

Return Policy parameters.

This Policy instance will only have parameters if it
was obtained via a call to

Policy.getInstance

.
Otherwise this method returns null.

**Returns:**
- Policy parameters, or null.

**Since:**
- 1.6

---

#### public
PermissionCollection
getPermissions​(
CodeSource
codesource)

Return a PermissionCollection object containing the set of
permissions granted to the specified CodeSource.

Applications are discouraged from calling this method
since this operation may not be supported by all policy implementations.
Applications should solely rely on the

implies

method
to perform policy checks. If an application absolutely must call
a getPermissions method, it should call

getPermissions(ProtectionDomain)

.

The default implementation of this method returns
Policy.UNSUPPORTED_EMPTY_COLLECTION. This method can be
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

#### public
PermissionCollection
getPermissions​(
ProtectionDomain
domain)

Return a PermissionCollection object containing the set of
permissions granted to the specified ProtectionDomain.

Applications are discouraged from calling this method
since this operation may not be supported by all policy implementations.
Applications should rely on the

implies

method
to perform policy checks.

The default implementation of this method first retrieves
the permissions returned via

getPermissions(CodeSource)

(the CodeSource is taken from the specified ProtectionDomain),
as well as the permissions located inside the specified ProtectionDomain.
All of these permissions are then combined and returned in a new
PermissionCollection object. If

getPermissions(CodeSource)

returns Policy.UNSUPPORTED_EMPTY_COLLECTION, then this method
returns the permissions contained inside the specified ProtectionDomain
in a new PermissionCollection object.

This method can be overridden if the policy implementation
supports returning a set of permissions granted to a ProtectionDomain.

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

**Since:**
- 1.4

---

#### public boolean implies​(
ProtectionDomain
domain,

Permission
permission)

Evaluates the global policy for the permissions granted to
the ProtectionDomain and tests whether the permission is
granted.

**Parameters:**
- domain

- the ProtectionDomain to test
- permission

- the Permission object to be tested for implication.

**Returns:**
- true if "permission" is a proper subset of a permission
granted to this ProtectionDomain.

**See Also:**
- ProtectionDomain

**Since:**
- 1.4

---

#### public void refresh()

Refreshes/reloads the policy configuration. The behavior of this method
depends on the implementation. For example, calling

refresh

on a file-based policy will cause the file to be re-read.

The default implementation of this method does nothing.
This method should be overridden if a refresh operation is supported
by the policy implementation.

---

### Additional Sections

#### Class Policy

java.lang.Object

- java.security.Policy

java.security.Policy

```java
public abstract class
Policy

extends
Object
```

A Policy object is responsible for determining whether code executing
in the Java runtime environment has permission to perform a
security-sensitive operation.

There is only one Policy object installed in the runtime at any
given time. A Policy object can be installed by calling the

setPolicy

method. The installed Policy object can be
obtained by calling the

getPolicy

method.

If no Policy object has been installed in the runtime, a call to

getPolicy

installs an instance of the default Policy
implementation (a default subclass implementation of this abstract class).
The default Policy implementation can be changed by setting the value
of the

policy.provider

security property to the fully qualified
name of the desired Policy subclass implementation. The system class loader
is used to load this class.

Application code can directly subclass Policy to provide a custom
implementation. In addition, an instance of a Policy object can be
constructed by invoking one of the

getInstance

factory methods
with a standard type. The default policy type is "JavaPolicy".

Once a Policy instance has been installed (either by default, or by
calling

setPolicy

), the Java runtime invokes its

implies

method when it needs to
determine whether executing code (encapsulated in a ProtectionDomain)
can perform SecurityManager-protected operations. How a Policy object
retrieves its policy data is up to the Policy implementation itself.
The policy data may be stored, for example, in a flat ASCII file,
in a serialized binary file of the Policy class, or in a database.

The

refresh

method causes the policy object to
refresh/reload its data. This operation is implementation-dependent.
For example, if the policy object stores its data in configuration files,
calling

refresh

will cause it to re-read the configuration
policy files. If a refresh operation is not supported, this method does
nothing. Note that refreshed policy may not have an effect on classes
in a particular ProtectionDomain. This is dependent on the Policy
provider's implementation of the

implies

method and its PermissionCollection caching strategy.

**Since:** 1.2
**See Also:** Provider

,

ProtectionDomain

,

Permission

,

security properties

public abstract class

Policy

extends

Object

A Policy object is responsible for determining whether code executing
in the Java runtime environment has permission to perform a
security-sensitive operation.

There is only one Policy object installed in the runtime at any
given time. A Policy object can be installed by calling the

setPolicy

method. The installed Policy object can be
obtained by calling the

getPolicy

method.

If no Policy object has been installed in the runtime, a call to

getPolicy

installs an instance of the default Policy
implementation (a default subclass implementation of this abstract class).
The default Policy implementation can be changed by setting the value
of the

policy.provider

security property to the fully qualified
name of the desired Policy subclass implementation. The system class loader
is used to load this class.

Application code can directly subclass Policy to provide a custom
implementation. In addition, an instance of a Policy object can be
constructed by invoking one of the

getInstance

factory methods
with a standard type. The default policy type is "JavaPolicy".

Once a Policy instance has been installed (either by default, or by
calling

setPolicy

), the Java runtime invokes its

implies

method when it needs to
determine whether executing code (encapsulated in a ProtectionDomain)
can perform SecurityManager-protected operations. How a Policy object
retrieves its policy data is up to the Policy implementation itself.
The policy data may be stored, for example, in a flat ASCII file,
in a serialized binary file of the Policy class, or in a database.

The

refresh

method causes the policy object to
refresh/reload its data. This operation is implementation-dependent.
For example, if the policy object stores its data in configuration files,
calling

refresh

will cause it to re-read the configuration
policy files. If a refresh operation is not supported, this method does
nothing. Note that refreshed policy may not have an effect on classes
in a particular ProtectionDomain. This is dependent on the Policy
provider's implementation of the

implies

method and its PermissionCollection caching strategy.

There is only one Policy object installed in the runtime at any
given time. A Policy object can be installed by calling the

setPolicy

method. The installed Policy object can be
obtained by calling the

getPolicy

method.

If no Policy object has been installed in the runtime, a call to

getPolicy

installs an instance of the default Policy
implementation (a default subclass implementation of this abstract class).
The default Policy implementation can be changed by setting the value
of the

policy.provider

security property to the fully qualified
name of the desired Policy subclass implementation. The system class loader
is used to load this class.

Application code can directly subclass Policy to provide a custom
implementation. In addition, an instance of a Policy object can be
constructed by invoking one of the

getInstance

factory methods
with a standard type. The default policy type is "JavaPolicy".

Once a Policy instance has been installed (either by default, or by
calling

setPolicy

), the Java runtime invokes its

implies

method when it needs to
determine whether executing code (encapsulated in a ProtectionDomain)
can perform SecurityManager-protected operations. How a Policy object
retrieves its policy data is up to the Policy implementation itself.
The policy data may be stored, for example, in a flat ASCII file,
in a serialized binary file of the Policy class, or in a database.

The

refresh

method causes the policy object to
refresh/reload its data. This operation is implementation-dependent.
For example, if the policy object stores its data in configuration files,
calling

refresh

will cause it to re-read the configuration
policy files. If a refresh operation is not supported, this method does
nothing. Note that refreshed policy may not have an effect on classes
in a particular ProtectionDomain. This is dependent on the Policy
provider's implementation of the

implies

method and its PermissionCollection caching strategy.

If no Policy object has been installed in the runtime, a call to

getPolicy

installs an instance of the default Policy
implementation (a default subclass implementation of this abstract class).
The default Policy implementation can be changed by setting the value
of the

policy.provider

security property to the fully qualified
name of the desired Policy subclass implementation. The system class loader
is used to load this class.

Application code can directly subclass Policy to provide a custom
implementation. In addition, an instance of a Policy object can be
constructed by invoking one of the

getInstance

factory methods
with a standard type. The default policy type is "JavaPolicy".

Once a Policy instance has been installed (either by default, or by
calling

setPolicy

), the Java runtime invokes its

implies

method when it needs to
determine whether executing code (encapsulated in a ProtectionDomain)
can perform SecurityManager-protected operations. How a Policy object
retrieves its policy data is up to the Policy implementation itself.
The policy data may be stored, for example, in a flat ASCII file,
in a serialized binary file of the Policy class, or in a database.

The

refresh

method causes the policy object to
refresh/reload its data. This operation is implementation-dependent.
For example, if the policy object stores its data in configuration files,
calling

refresh

will cause it to re-read the configuration
policy files. If a refresh operation is not supported, this method does
nothing. Note that refreshed policy may not have an effect on classes
in a particular ProtectionDomain. This is dependent on the Policy
provider's implementation of the

implies

method and its PermissionCollection caching strategy.

Application code can directly subclass Policy to provide a custom
implementation. In addition, an instance of a Policy object can be
constructed by invoking one of the

getInstance

factory methods
with a standard type. The default policy type is "JavaPolicy".

Once a Policy instance has been installed (either by default, or by
calling

setPolicy

), the Java runtime invokes its

implies

method when it needs to
determine whether executing code (encapsulated in a ProtectionDomain)
can perform SecurityManager-protected operations. How a Policy object
retrieves its policy data is up to the Policy implementation itself.
The policy data may be stored, for example, in a flat ASCII file,
in a serialized binary file of the Policy class, or in a database.

The

refresh

method causes the policy object to
refresh/reload its data. This operation is implementation-dependent.
For example, if the policy object stores its data in configuration files,
calling

refresh

will cause it to re-read the configuration
policy files. If a refresh operation is not supported, this method does
nothing. Note that refreshed policy may not have an effect on classes
in a particular ProtectionDomain. This is dependent on the Policy
provider's implementation of the

implies

method and its PermissionCollection caching strategy.

Once a Policy instance has been installed (either by default, or by
calling

setPolicy

), the Java runtime invokes its

implies

method when it needs to
determine whether executing code (encapsulated in a ProtectionDomain)
can perform SecurityManager-protected operations. How a Policy object
retrieves its policy data is up to the Policy implementation itself.
The policy data may be stored, for example, in a flat ASCII file,
in a serialized binary file of the Policy class, or in a database.

The

refresh

method causes the policy object to
refresh/reload its data. This operation is implementation-dependent.
For example, if the policy object stores its data in configuration files,
calling

refresh

will cause it to re-read the configuration
policy files. If a refresh operation is not supported, this method does
nothing. Note that refreshed policy may not have an effect on classes
in a particular ProtectionDomain. This is dependent on the Policy
provider's implementation of the

implies

method and its PermissionCollection caching strategy.

The

refresh

method causes the policy object to
refresh/reload its data. This operation is implementation-dependent.
For example, if the policy object stores its data in configuration files,
calling

refresh

will cause it to re-read the configuration
policy files. If a refresh operation is not supported, this method does
nothing. Note that refreshed policy may not have an effect on classes
in a particular ProtectionDomain. This is dependent on the Policy
provider's implementation of the

implies

method and its PermissionCollection caching strategy.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static interface

Policy.Parameters

This represents a marker interface for Policy parameters.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

PermissionCollection

UNSUPPORTED_EMPTY_COLLECTION

A read-only empty PermissionCollection instance.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Policy

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

Policy

getInstance

​(

String

type,

Policy.Parameters

params)

Returns a Policy object of the specified type.

static

Policy

getInstance

​(

String

type,

Policy.Parameters

params,

String

provider)

Returns a Policy object of the specified type.

static

Policy

getInstance

​(

String

type,

Policy.Parameters

params,

Provider

provider)

Returns a Policy object of the specified type.

Policy.Parameters

getParameters

()

Return Policy parameters.

PermissionCollection

getPermissions

​(

CodeSource

codesource)

Return a PermissionCollection object containing the set of
permissions granted to the specified CodeSource.

PermissionCollection

getPermissions

​(

ProtectionDomain

domain)

Return a PermissionCollection object containing the set of
permissions granted to the specified ProtectionDomain.

static

Policy

getPolicy

()

Returns the installed Policy object.

Provider

getProvider

()

Return the Provider of this Policy.

String

getType

()

Return the type of this Policy.

boolean

implies

​(

ProtectionDomain

domain,

Permission

permission)

Evaluates the global policy for the permissions granted to
the ProtectionDomain and tests whether the permission is
granted.

void

refresh

()

Refreshes/reloads the policy configuration.

static void

setPolicy

​(

Policy

p)

Sets the system-wide Policy object.

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static interface

Policy.Parameters

This represents a marker interface for Policy parameters.

---

#### Nested Class Summary

This represents a marker interface for Policy parameters.

Field Summary

Fields

Modifier and Type

Field

Description

static

PermissionCollection

UNSUPPORTED_EMPTY_COLLECTION

A read-only empty PermissionCollection instance.

---

#### Field Summary

A read-only empty PermissionCollection instance.

Constructor Summary

Constructors

Constructor

Description

Policy

()

---

#### Constructor Summary

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

Policy

getInstance

​(

String

type,

Policy.Parameters

params)

Returns a Policy object of the specified type.

static

Policy

getInstance

​(

String

type,

Policy.Parameters

params,

String

provider)

Returns a Policy object of the specified type.

static

Policy

getInstance

​(

String

type,

Policy.Parameters

params,

Provider

provider)

Returns a Policy object of the specified type.

Policy.Parameters

getParameters

()

Return Policy parameters.

PermissionCollection

getPermissions

​(

CodeSource

codesource)

Return a PermissionCollection object containing the set of
permissions granted to the specified CodeSource.

PermissionCollection

getPermissions

​(

ProtectionDomain

domain)

Return a PermissionCollection object containing the set of
permissions granted to the specified ProtectionDomain.

static

Policy

getPolicy

()

Returns the installed Policy object.

Provider

getProvider

()

Return the Provider of this Policy.

String

getType

()

Return the type of this Policy.

boolean

implies

​(

ProtectionDomain

domain,

Permission

permission)

Evaluates the global policy for the permissions granted to
the ProtectionDomain and tests whether the permission is
granted.

void

refresh

()

Refreshes/reloads the policy configuration.

static void

setPolicy

​(

Policy

p)

Sets the system-wide Policy object.

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

Returns a Policy object of the specified type.

Return Policy parameters.

Return a PermissionCollection object containing the set of
permissions granted to the specified CodeSource.

Return a PermissionCollection object containing the set of
permissions granted to the specified ProtectionDomain.

Returns the installed Policy object.

Return the Provider of this Policy.

Return the type of this Policy.

Evaluates the global policy for the permissions granted to
the ProtectionDomain and tests whether the permission is
granted.

Refreshes/reloads the policy configuration.

Sets the system-wide Policy object.

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

============ FIELD DETAIL ===========

- Field Detail

- UNSUPPORTED_EMPTY_COLLECTION

```java
public static final
PermissionCollection
UNSUPPORTED_EMPTY_COLLECTION
```

A read-only empty PermissionCollection instance.

**Since:** 1.6

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Policy

```java
public Policy()
```

============ METHOD DETAIL ==========

- Method Detail

- getPolicy

```java
public static
Policy
getPolicy()
```

Returns the installed Policy object. This value should not be cached,
as it may be changed by a call to

setPolicy

.
This method first calls

SecurityManager.checkPermission

with a

SecurityPermission("getPolicy")

permission
to ensure it's ok to get the Policy object.

**Returns:** the installed Policy.
**Throws:** SecurityException

- if a security manager exists and its

checkPermission

method doesn't allow
getting the Policy object.
**See Also:** SecurityManager.checkPermission(Permission)

,

setPolicy(java.security.Policy)

- setPolicy

```java
public static void setPolicy​(
Policy
p)
```

Sets the system-wide Policy object. This method first calls

SecurityManager.checkPermission

with a

SecurityPermission("setPolicy")

permission to ensure it's ok to set the Policy.

**Parameters:** p

- the new system Policy object.
**Throws:** SecurityException

- if a security manager exists and its

checkPermission

method doesn't allow
setting the Policy.
**See Also:** SecurityManager.checkPermission(Permission)

,

getPolicy()

- getInstance

```java
public static
Policy
getInstance​(
String
type,

Policy.Parameters
params)
throws
NoSuchAlgorithmException
```

Returns a Policy object of the specified type.

This method traverses the list of registered security providers,
starting with the most preferred Provider.
A new Policy object encapsulating the
PolicySpi implementation from the first
Provider that supports the specified type is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Implementation Note:** The JDK Reference Implementation additionally uses the

jdk.security.provider.preferred

Security

property to determine
the preferred provider order for the specified algorithm. This
may be different than the order of providers returned by

Security.getProviders()

.
**Parameters:** type

- the specified Policy type. See the Policy section in the

Java Security Standard Algorithm Names Specification

for a list of standard Policy types.
**Parameters:** params

- parameters for the Policy, which may be null.
**Returns:** the new

Policy

object
**Throws:** IllegalArgumentException

- if the specified parameters
are not understood by the

PolicySpi

implementation
from the selected

Provider
**Throws:** NoSuchAlgorithmException

- if no

Provider

supports
a

PolicySpi

implementation for the specified type
**Throws:** NullPointerException

- if

type

is

null
**Throws:** SecurityException

- if the caller does not have permission
to get a

Policy

instance for the specified type.
**Since:** 1.6
**See Also:** Provider

- getInstance

```java
public static
Policy
getInstance​(
String
type,

Policy.Parameters
params,

String
provider)
throws
NoSuchProviderException
,

NoSuchAlgorithmException
```

Returns a Policy object of the specified type.

A new Policy object encapsulating the
PolicySpi implementation from the specified provider
is returned. The specified provider must be registered
in the provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:** type

- the specified Policy type. See the Policy section in the

Java Security Standard Algorithm Names Specification

for a list of standard Policy types.
**Parameters:** params

- parameters for the Policy, which may be null.
**Parameters:** provider

- the provider.
**Returns:** the new

Policy

object
**Throws:** IllegalArgumentException

- if the specified provider
is

null

or empty, or if the specified parameters are
not understood by the

PolicySpi

implementation from
the specified provider
**Throws:** NoSuchAlgorithmException

- if the specified provider does not
support a

PolicySpi

implementation for the specified
type
**Throws:** NoSuchProviderException

- if the specified provider is not
registered in the security provider list
**Throws:** NullPointerException

- if

type

is

null
**Throws:** SecurityException

- if the caller does not have permission
to get a

Policy

instance for the specified type
**Since:** 1.6
**See Also:** Provider

- getInstance

```java
public static
Policy
getInstance​(
String
type,

Policy.Parameters
params,

Provider
provider)
throws
NoSuchAlgorithmException
```

Returns a Policy object of the specified type.

A new Policy object encapsulating the
PolicySpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

**Parameters:** type

- the specified Policy type. See the Policy section in the

Java Security Standard Algorithm Names Specification

for a list of standard Policy types.
**Parameters:** params

- parameters for the Policy, which may be null.
**Parameters:** provider

- the Provider.
**Returns:** the new

Policy

object
**Throws:** IllegalArgumentException

- if the specified

Provider

is

null

, or if the specified parameters are not
understood by the

PolicySpi

implementation from the
specified

Provider
**Throws:** NoSuchAlgorithmException

- if the specified

Provider

does not support a

PolicySpi

implementation for
the specified type
**Throws:** NullPointerException

- if

type

is

null
**Throws:** SecurityException

- if the caller does not have permission
to get a

Policy

instance for the specified type
**Since:** 1.6
**See Also:** Provider

- getProvider

```java
public
Provider
getProvider()
```

Return the Provider of this Policy.

This Policy instance will only have a Provider if it
was obtained via a call to

Policy.getInstance

.
Otherwise this method returns null.

**Returns:** the Provider of this Policy, or null.
**Since:** 1.6

- getType

```java
public
String
getType()
```

Return the type of this Policy.

This Policy instance will only have a type if it
was obtained via a call to

Policy.getInstance

.
Otherwise this method returns null.

**Returns:** the type of this Policy, or null.
**Since:** 1.6

- getParameters

```java
public
Policy.Parameters
getParameters()
```

Return Policy parameters.

This Policy instance will only have parameters if it
was obtained via a call to

Policy.getInstance

.
Otherwise this method returns null.

**Returns:** Policy parameters, or null.
**Since:** 1.6

- getPermissions

```java
public
PermissionCollection
getPermissions​(
CodeSource
codesource)
```

Return a PermissionCollection object containing the set of
permissions granted to the specified CodeSource.

Applications are discouraged from calling this method
since this operation may not be supported by all policy implementations.
Applications should solely rely on the

implies

method
to perform policy checks. If an application absolutely must call
a getPermissions method, it should call

getPermissions(ProtectionDomain)

.

The default implementation of this method returns
Policy.UNSUPPORTED_EMPTY_COLLECTION. This method can be
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

- getPermissions

```java
public
PermissionCollection
getPermissions​(
ProtectionDomain
domain)
```

Return a PermissionCollection object containing the set of
permissions granted to the specified ProtectionDomain.

Applications are discouraged from calling this method
since this operation may not be supported by all policy implementations.
Applications should rely on the

implies

method
to perform policy checks.

The default implementation of this method first retrieves
the permissions returned via

getPermissions(CodeSource)

(the CodeSource is taken from the specified ProtectionDomain),
as well as the permissions located inside the specified ProtectionDomain.
All of these permissions are then combined and returned in a new
PermissionCollection object. If

getPermissions(CodeSource)

returns Policy.UNSUPPORTED_EMPTY_COLLECTION, then this method
returns the permissions contained inside the specified ProtectionDomain
in a new PermissionCollection object.

This method can be overridden if the policy implementation
supports returning a set of permissions granted to a ProtectionDomain.

**Parameters:** domain

- the ProtectionDomain to which the returned
PermissionCollection has been granted.
**Returns:** a set of permissions granted to the specified ProtectionDomain.
If this operation is supported, the returned
set of permissions must be a new mutable instance
and it must support heterogeneous Permission types.
If this operation is not supported,
Policy.UNSUPPORTED_EMPTY_COLLECTION is returned.
**Since:** 1.4

- implies

```java
public boolean implies​(
ProtectionDomain
domain,

Permission
permission)
```

Evaluates the global policy for the permissions granted to
the ProtectionDomain and tests whether the permission is
granted.

**Parameters:** domain

- the ProtectionDomain to test
**Parameters:** permission

- the Permission object to be tested for implication.
**Returns:** true if "permission" is a proper subset of a permission
granted to this ProtectionDomain.
**Since:** 1.4
**See Also:** ProtectionDomain

- refresh

```java
public void refresh()
```

Refreshes/reloads the policy configuration. The behavior of this method
depends on the implementation. For example, calling

refresh

on a file-based policy will cause the file to be re-read.

The default implementation of this method does nothing.
This method should be overridden if a refresh operation is supported
by the policy implementation.

Field Detail

- UNSUPPORTED_EMPTY_COLLECTION

```java
public static final
PermissionCollection
UNSUPPORTED_EMPTY_COLLECTION
```

A read-only empty PermissionCollection instance.

**Since:** 1.6

---

#### Field Detail

UNSUPPORTED_EMPTY_COLLECTION

```java
public static final
PermissionCollection
UNSUPPORTED_EMPTY_COLLECTION
```

A read-only empty PermissionCollection instance.

**Since:** 1.6

---

#### UNSUPPORTED_EMPTY_COLLECTION

public static final

PermissionCollection

UNSUPPORTED_EMPTY_COLLECTION

A read-only empty PermissionCollection instance.

Constructor Detail

- Policy

```java
public Policy()
```

---

#### Constructor Detail

Policy

```java
public Policy()
```

---

#### Policy

public Policy()

Method Detail

- getPolicy

```java
public static
Policy
getPolicy()
```

Returns the installed Policy object. This value should not be cached,
as it may be changed by a call to

setPolicy

.
This method first calls

SecurityManager.checkPermission

with a

SecurityPermission("getPolicy")

permission
to ensure it's ok to get the Policy object.

**Returns:** the installed Policy.
**Throws:** SecurityException

- if a security manager exists and its

checkPermission

method doesn't allow
getting the Policy object.
**See Also:** SecurityManager.checkPermission(Permission)

,

setPolicy(java.security.Policy)

- setPolicy

```java
public static void setPolicy​(
Policy
p)
```

Sets the system-wide Policy object. This method first calls

SecurityManager.checkPermission

with a

SecurityPermission("setPolicy")

permission to ensure it's ok to set the Policy.

**Parameters:** p

- the new system Policy object.
**Throws:** SecurityException

- if a security manager exists and its

checkPermission

method doesn't allow
setting the Policy.
**See Also:** SecurityManager.checkPermission(Permission)

,

getPolicy()

- getInstance

```java
public static
Policy
getInstance​(
String
type,

Policy.Parameters
params)
throws
NoSuchAlgorithmException
```

Returns a Policy object of the specified type.

This method traverses the list of registered security providers,
starting with the most preferred Provider.
A new Policy object encapsulating the
PolicySpi implementation from the first
Provider that supports the specified type is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Implementation Note:** The JDK Reference Implementation additionally uses the

jdk.security.provider.preferred

Security

property to determine
the preferred provider order for the specified algorithm. This
may be different than the order of providers returned by

Security.getProviders()

.
**Parameters:** type

- the specified Policy type. See the Policy section in the

Java Security Standard Algorithm Names Specification

for a list of standard Policy types.
**Parameters:** params

- parameters for the Policy, which may be null.
**Returns:** the new

Policy

object
**Throws:** IllegalArgumentException

- if the specified parameters
are not understood by the

PolicySpi

implementation
from the selected

Provider
**Throws:** NoSuchAlgorithmException

- if no

Provider

supports
a

PolicySpi

implementation for the specified type
**Throws:** NullPointerException

- if

type

is

null
**Throws:** SecurityException

- if the caller does not have permission
to get a

Policy

instance for the specified type.
**Since:** 1.6
**See Also:** Provider

- getInstance

```java
public static
Policy
getInstance​(
String
type,

Policy.Parameters
params,

String
provider)
throws
NoSuchProviderException
,

NoSuchAlgorithmException
```

Returns a Policy object of the specified type.

A new Policy object encapsulating the
PolicySpi implementation from the specified provider
is returned. The specified provider must be registered
in the provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:** type

- the specified Policy type. See the Policy section in the

Java Security Standard Algorithm Names Specification

for a list of standard Policy types.
**Parameters:** params

- parameters for the Policy, which may be null.
**Parameters:** provider

- the provider.
**Returns:** the new

Policy

object
**Throws:** IllegalArgumentException

- if the specified provider
is

null

or empty, or if the specified parameters are
not understood by the

PolicySpi

implementation from
the specified provider
**Throws:** NoSuchAlgorithmException

- if the specified provider does not
support a

PolicySpi

implementation for the specified
type
**Throws:** NoSuchProviderException

- if the specified provider is not
registered in the security provider list
**Throws:** NullPointerException

- if

type

is

null
**Throws:** SecurityException

- if the caller does not have permission
to get a

Policy

instance for the specified type
**Since:** 1.6
**See Also:** Provider

- getInstance

```java
public static
Policy
getInstance​(
String
type,

Policy.Parameters
params,

Provider
provider)
throws
NoSuchAlgorithmException
```

Returns a Policy object of the specified type.

A new Policy object encapsulating the
PolicySpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

**Parameters:** type

- the specified Policy type. See the Policy section in the

Java Security Standard Algorithm Names Specification

for a list of standard Policy types.
**Parameters:** params

- parameters for the Policy, which may be null.
**Parameters:** provider

- the Provider.
**Returns:** the new

Policy

object
**Throws:** IllegalArgumentException

- if the specified

Provider

is

null

, or if the specified parameters are not
understood by the

PolicySpi

implementation from the
specified

Provider
**Throws:** NoSuchAlgorithmException

- if the specified

Provider

does not support a

PolicySpi

implementation for
the specified type
**Throws:** NullPointerException

- if

type

is

null
**Throws:** SecurityException

- if the caller does not have permission
to get a

Policy

instance for the specified type
**Since:** 1.6
**See Also:** Provider

- getProvider

```java
public
Provider
getProvider()
```

Return the Provider of this Policy.

This Policy instance will only have a Provider if it
was obtained via a call to

Policy.getInstance

.
Otherwise this method returns null.

**Returns:** the Provider of this Policy, or null.
**Since:** 1.6

- getType

```java
public
String
getType()
```

Return the type of this Policy.

This Policy instance will only have a type if it
was obtained via a call to

Policy.getInstance

.
Otherwise this method returns null.

**Returns:** the type of this Policy, or null.
**Since:** 1.6

- getParameters

```java
public
Policy.Parameters
getParameters()
```

Return Policy parameters.

This Policy instance will only have parameters if it
was obtained via a call to

Policy.getInstance

.
Otherwise this method returns null.

**Returns:** Policy parameters, or null.
**Since:** 1.6

- getPermissions

```java
public
PermissionCollection
getPermissions​(
CodeSource
codesource)
```

Return a PermissionCollection object containing the set of
permissions granted to the specified CodeSource.

Applications are discouraged from calling this method
since this operation may not be supported by all policy implementations.
Applications should solely rely on the

implies

method
to perform policy checks. If an application absolutely must call
a getPermissions method, it should call

getPermissions(ProtectionDomain)

.

The default implementation of this method returns
Policy.UNSUPPORTED_EMPTY_COLLECTION. This method can be
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

- getPermissions

```java
public
PermissionCollection
getPermissions​(
ProtectionDomain
domain)
```

Return a PermissionCollection object containing the set of
permissions granted to the specified ProtectionDomain.

Applications are discouraged from calling this method
since this operation may not be supported by all policy implementations.
Applications should rely on the

implies

method
to perform policy checks.

The default implementation of this method first retrieves
the permissions returned via

getPermissions(CodeSource)

(the CodeSource is taken from the specified ProtectionDomain),
as well as the permissions located inside the specified ProtectionDomain.
All of these permissions are then combined and returned in a new
PermissionCollection object. If

getPermissions(CodeSource)

returns Policy.UNSUPPORTED_EMPTY_COLLECTION, then this method
returns the permissions contained inside the specified ProtectionDomain
in a new PermissionCollection object.

This method can be overridden if the policy implementation
supports returning a set of permissions granted to a ProtectionDomain.

**Parameters:** domain

- the ProtectionDomain to which the returned
PermissionCollection has been granted.
**Returns:** a set of permissions granted to the specified ProtectionDomain.
If this operation is supported, the returned
set of permissions must be a new mutable instance
and it must support heterogeneous Permission types.
If this operation is not supported,
Policy.UNSUPPORTED_EMPTY_COLLECTION is returned.
**Since:** 1.4

- implies

```java
public boolean implies​(
ProtectionDomain
domain,

Permission
permission)
```

Evaluates the global policy for the permissions granted to
the ProtectionDomain and tests whether the permission is
granted.

**Parameters:** domain

- the ProtectionDomain to test
**Parameters:** permission

- the Permission object to be tested for implication.
**Returns:** true if "permission" is a proper subset of a permission
granted to this ProtectionDomain.
**Since:** 1.4
**See Also:** ProtectionDomain

- refresh

```java
public void refresh()
```

Refreshes/reloads the policy configuration. The behavior of this method
depends on the implementation. For example, calling

refresh

on a file-based policy will cause the file to be re-read.

The default implementation of this method does nothing.
This method should be overridden if a refresh operation is supported
by the policy implementation.

---

#### Method Detail

getPolicy

```java
public static
Policy
getPolicy()
```

Returns the installed Policy object. This value should not be cached,
as it may be changed by a call to

setPolicy

.
This method first calls

SecurityManager.checkPermission

with a

SecurityPermission("getPolicy")

permission
to ensure it's ok to get the Policy object.

**Returns:** the installed Policy.
**Throws:** SecurityException

- if a security manager exists and its

checkPermission

method doesn't allow
getting the Policy object.
**See Also:** SecurityManager.checkPermission(Permission)

,

setPolicy(java.security.Policy)

---

#### getPolicy

public static

Policy

getPolicy()

Returns the installed Policy object. This value should not be cached,
as it may be changed by a call to

setPolicy

.
This method first calls

SecurityManager.checkPermission

with a

SecurityPermission("getPolicy")

permission
to ensure it's ok to get the Policy object.

setPolicy

```java
public static void setPolicy​(
Policy
p)
```

Sets the system-wide Policy object. This method first calls

SecurityManager.checkPermission

with a

SecurityPermission("setPolicy")

permission to ensure it's ok to set the Policy.

**Parameters:** p

- the new system Policy object.
**Throws:** SecurityException

- if a security manager exists and its

checkPermission

method doesn't allow
setting the Policy.
**See Also:** SecurityManager.checkPermission(Permission)

,

getPolicy()

---

#### setPolicy

public static void setPolicy​(

Policy

p)

Sets the system-wide Policy object. This method first calls

SecurityManager.checkPermission

with a

SecurityPermission("setPolicy")

permission to ensure it's ok to set the Policy.

getInstance

```java
public static
Policy
getInstance​(
String
type,

Policy.Parameters
params)
throws
NoSuchAlgorithmException
```

Returns a Policy object of the specified type.

This method traverses the list of registered security providers,
starting with the most preferred Provider.
A new Policy object encapsulating the
PolicySpi implementation from the first
Provider that supports the specified type is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Implementation Note:** The JDK Reference Implementation additionally uses the

jdk.security.provider.preferred

Security

property to determine
the preferred provider order for the specified algorithm. This
may be different than the order of providers returned by

Security.getProviders()

.
**Parameters:** type

- the specified Policy type. See the Policy section in the

Java Security Standard Algorithm Names Specification

for a list of standard Policy types.
**Parameters:** params

- parameters for the Policy, which may be null.
**Returns:** the new

Policy

object
**Throws:** IllegalArgumentException

- if the specified parameters
are not understood by the

PolicySpi

implementation
from the selected

Provider
**Throws:** NoSuchAlgorithmException

- if no

Provider

supports
a

PolicySpi

implementation for the specified type
**Throws:** NullPointerException

- if

type

is

null
**Throws:** SecurityException

- if the caller does not have permission
to get a

Policy

instance for the specified type.
**Since:** 1.6
**See Also:** Provider

---

#### getInstance

public static

Policy

getInstance​(

String

type,

Policy.Parameters

params)
throws

NoSuchAlgorithmException

Returns a Policy object of the specified type.

This method traverses the list of registered security providers,
starting with the most preferred Provider.
A new Policy object encapsulating the
PolicySpi implementation from the first
Provider that supports the specified type is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

This method traverses the list of registered security providers,
starting with the most preferred Provider.
A new Policy object encapsulating the
PolicySpi implementation from the first
Provider that supports the specified type is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

getInstance

```java
public static
Policy
getInstance​(
String
type,

Policy.Parameters
params,

String
provider)
throws
NoSuchProviderException
,

NoSuchAlgorithmException
```

Returns a Policy object of the specified type.

A new Policy object encapsulating the
PolicySpi implementation from the specified provider
is returned. The specified provider must be registered
in the provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:** type

- the specified Policy type. See the Policy section in the

Java Security Standard Algorithm Names Specification

for a list of standard Policy types.
**Parameters:** params

- parameters for the Policy, which may be null.
**Parameters:** provider

- the provider.
**Returns:** the new

Policy

object
**Throws:** IllegalArgumentException

- if the specified provider
is

null

or empty, or if the specified parameters are
not understood by the

PolicySpi

implementation from
the specified provider
**Throws:** NoSuchAlgorithmException

- if the specified provider does not
support a

PolicySpi

implementation for the specified
type
**Throws:** NoSuchProviderException

- if the specified provider is not
registered in the security provider list
**Throws:** NullPointerException

- if

type

is

null
**Throws:** SecurityException

- if the caller does not have permission
to get a

Policy

instance for the specified type
**Since:** 1.6
**See Also:** Provider

---

#### getInstance

public static

Policy

getInstance​(

String

type,

Policy.Parameters

params,

String

provider)
throws

NoSuchProviderException

,

NoSuchAlgorithmException

Returns a Policy object of the specified type.

A new Policy object encapsulating the
PolicySpi implementation from the specified provider
is returned. The specified provider must be registered
in the provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

A new Policy object encapsulating the
PolicySpi implementation from the specified provider
is returned. The specified provider must be registered
in the provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

getInstance

```java
public static
Policy
getInstance​(
String
type,

Policy.Parameters
params,

Provider
provider)
throws
NoSuchAlgorithmException
```

Returns a Policy object of the specified type.

A new Policy object encapsulating the
PolicySpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

**Parameters:** type

- the specified Policy type. See the Policy section in the

Java Security Standard Algorithm Names Specification

for a list of standard Policy types.
**Parameters:** params

- parameters for the Policy, which may be null.
**Parameters:** provider

- the Provider.
**Returns:** the new

Policy

object
**Throws:** IllegalArgumentException

- if the specified

Provider

is

null

, or if the specified parameters are not
understood by the

PolicySpi

implementation from the
specified

Provider
**Throws:** NoSuchAlgorithmException

- if the specified

Provider

does not support a

PolicySpi

implementation for
the specified type
**Throws:** NullPointerException

- if

type

is

null
**Throws:** SecurityException

- if the caller does not have permission
to get a

Policy

instance for the specified type
**Since:** 1.6
**See Also:** Provider

---

#### getInstance

public static

Policy

getInstance​(

String

type,

Policy.Parameters

params,

Provider

provider)
throws

NoSuchAlgorithmException

Returns a Policy object of the specified type.

A new Policy object encapsulating the
PolicySpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

A new Policy object encapsulating the
PolicySpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

getProvider

```java
public
Provider
getProvider()
```

Return the Provider of this Policy.

This Policy instance will only have a Provider if it
was obtained via a call to

Policy.getInstance

.
Otherwise this method returns null.

**Returns:** the Provider of this Policy, or null.
**Since:** 1.6

---

#### getProvider

public

Provider

getProvider()

Return the Provider of this Policy.

This Policy instance will only have a Provider if it
was obtained via a call to

Policy.getInstance

.
Otherwise this method returns null.

This Policy instance will only have a Provider if it
was obtained via a call to

Policy.getInstance

.
Otherwise this method returns null.

getType

```java
public
String
getType()
```

Return the type of this Policy.

This Policy instance will only have a type if it
was obtained via a call to

Policy.getInstance

.
Otherwise this method returns null.

**Returns:** the type of this Policy, or null.
**Since:** 1.6

---

#### getType

public

String

getType()

Return the type of this Policy.

This Policy instance will only have a type if it
was obtained via a call to

Policy.getInstance

.
Otherwise this method returns null.

This Policy instance will only have a type if it
was obtained via a call to

Policy.getInstance

.
Otherwise this method returns null.

getParameters

```java
public
Policy.Parameters
getParameters()
```

Return Policy parameters.

This Policy instance will only have parameters if it
was obtained via a call to

Policy.getInstance

.
Otherwise this method returns null.

**Returns:** Policy parameters, or null.
**Since:** 1.6

---

#### getParameters

public

Policy.Parameters

getParameters()

Return Policy parameters.

This Policy instance will only have parameters if it
was obtained via a call to

Policy.getInstance

.
Otherwise this method returns null.

This Policy instance will only have parameters if it
was obtained via a call to

Policy.getInstance

.
Otherwise this method returns null.

getPermissions

```java
public
PermissionCollection
getPermissions​(
CodeSource
codesource)
```

Return a PermissionCollection object containing the set of
permissions granted to the specified CodeSource.

Applications are discouraged from calling this method
since this operation may not be supported by all policy implementations.
Applications should solely rely on the

implies

method
to perform policy checks. If an application absolutely must call
a getPermissions method, it should call

getPermissions(ProtectionDomain)

.

The default implementation of this method returns
Policy.UNSUPPORTED_EMPTY_COLLECTION. This method can be
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

#### getPermissions

public

PermissionCollection

getPermissions​(

CodeSource

codesource)

Return a PermissionCollection object containing the set of
permissions granted to the specified CodeSource.

Applications are discouraged from calling this method
since this operation may not be supported by all policy implementations.
Applications should solely rely on the

implies

method
to perform policy checks. If an application absolutely must call
a getPermissions method, it should call

getPermissions(ProtectionDomain)

.

The default implementation of this method returns
Policy.UNSUPPORTED_EMPTY_COLLECTION. This method can be
overridden if the policy implementation can return a set of
permissions granted to a CodeSource.

Applications are discouraged from calling this method
since this operation may not be supported by all policy implementations.
Applications should solely rely on the

implies

method
to perform policy checks. If an application absolutely must call
a getPermissions method, it should call

getPermissions(ProtectionDomain)

.

The default implementation of this method returns
Policy.UNSUPPORTED_EMPTY_COLLECTION. This method can be
overridden if the policy implementation can return a set of
permissions granted to a CodeSource.

The default implementation of this method returns
Policy.UNSUPPORTED_EMPTY_COLLECTION. This method can be
overridden if the policy implementation can return a set of
permissions granted to a CodeSource.

getPermissions

```java
public
PermissionCollection
getPermissions​(
ProtectionDomain
domain)
```

Return a PermissionCollection object containing the set of
permissions granted to the specified ProtectionDomain.

Applications are discouraged from calling this method
since this operation may not be supported by all policy implementations.
Applications should rely on the

implies

method
to perform policy checks.

The default implementation of this method first retrieves
the permissions returned via

getPermissions(CodeSource)

(the CodeSource is taken from the specified ProtectionDomain),
as well as the permissions located inside the specified ProtectionDomain.
All of these permissions are then combined and returned in a new
PermissionCollection object. If

getPermissions(CodeSource)

returns Policy.UNSUPPORTED_EMPTY_COLLECTION, then this method
returns the permissions contained inside the specified ProtectionDomain
in a new PermissionCollection object.

This method can be overridden if the policy implementation
supports returning a set of permissions granted to a ProtectionDomain.

**Parameters:** domain

- the ProtectionDomain to which the returned
PermissionCollection has been granted.
**Returns:** a set of permissions granted to the specified ProtectionDomain.
If this operation is supported, the returned
set of permissions must be a new mutable instance
and it must support heterogeneous Permission types.
If this operation is not supported,
Policy.UNSUPPORTED_EMPTY_COLLECTION is returned.
**Since:** 1.4

---

#### getPermissions

public

PermissionCollection

getPermissions​(

ProtectionDomain

domain)

Return a PermissionCollection object containing the set of
permissions granted to the specified ProtectionDomain.

Applications are discouraged from calling this method
since this operation may not be supported by all policy implementations.
Applications should rely on the

implies

method
to perform policy checks.

The default implementation of this method first retrieves
the permissions returned via

getPermissions(CodeSource)

(the CodeSource is taken from the specified ProtectionDomain),
as well as the permissions located inside the specified ProtectionDomain.
All of these permissions are then combined and returned in a new
PermissionCollection object. If

getPermissions(CodeSource)

returns Policy.UNSUPPORTED_EMPTY_COLLECTION, then this method
returns the permissions contained inside the specified ProtectionDomain
in a new PermissionCollection object.

This method can be overridden if the policy implementation
supports returning a set of permissions granted to a ProtectionDomain.

Applications are discouraged from calling this method
since this operation may not be supported by all policy implementations.
Applications should rely on the

implies

method
to perform policy checks.

The default implementation of this method first retrieves
the permissions returned via

getPermissions(CodeSource)

(the CodeSource is taken from the specified ProtectionDomain),
as well as the permissions located inside the specified ProtectionDomain.
All of these permissions are then combined and returned in a new
PermissionCollection object. If

getPermissions(CodeSource)

returns Policy.UNSUPPORTED_EMPTY_COLLECTION, then this method
returns the permissions contained inside the specified ProtectionDomain
in a new PermissionCollection object.

This method can be overridden if the policy implementation
supports returning a set of permissions granted to a ProtectionDomain.

The default implementation of this method first retrieves
the permissions returned via

getPermissions(CodeSource)

(the CodeSource is taken from the specified ProtectionDomain),
as well as the permissions located inside the specified ProtectionDomain.
All of these permissions are then combined and returned in a new
PermissionCollection object. If

getPermissions(CodeSource)

returns Policy.UNSUPPORTED_EMPTY_COLLECTION, then this method
returns the permissions contained inside the specified ProtectionDomain
in a new PermissionCollection object.

This method can be overridden if the policy implementation
supports returning a set of permissions granted to a ProtectionDomain.

This method can be overridden if the policy implementation
supports returning a set of permissions granted to a ProtectionDomain.

implies

```java
public boolean implies​(
ProtectionDomain
domain,

Permission
permission)
```

Evaluates the global policy for the permissions granted to
the ProtectionDomain and tests whether the permission is
granted.

**Parameters:** domain

- the ProtectionDomain to test
**Parameters:** permission

- the Permission object to be tested for implication.
**Returns:** true if "permission" is a proper subset of a permission
granted to this ProtectionDomain.
**Since:** 1.4
**See Also:** ProtectionDomain

---

#### implies

public boolean implies​(

ProtectionDomain

domain,

Permission

permission)

Evaluates the global policy for the permissions granted to
the ProtectionDomain and tests whether the permission is
granted.

refresh

```java
public void refresh()
```

Refreshes/reloads the policy configuration. The behavior of this method
depends on the implementation. For example, calling

refresh

on a file-based policy will cause the file to be re-read.

The default implementation of this method does nothing.
This method should be overridden if a refresh operation is supported
by the policy implementation.

---

#### refresh

public void refresh()

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

---

