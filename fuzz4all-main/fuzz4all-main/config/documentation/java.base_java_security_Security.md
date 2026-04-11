# Class Security

**Source:** `java.base\java\security\Security.html`

### Class Description

```java
public final class
Security

extends
Object
```

This class centralizes all security properties and common security
methods. One of its primary uses is to manage providers.

The default values of security properties are read from an
implementation-specific location, which is typically the properties file

conf/security/java.security

in the Java installation directory.

**Implementation Note:** If the properties file fails to load, the JDK implementation will
throw an unspecified error when initializing the

Security

class.
**Since:** 1.1

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### @Deprecated

public static
String
getAlgorithmProperty​(
String
algName,

String
propName)

Gets a specified property for an algorithm. The algorithm name
should be a standard name. See the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.

One possible use is by specialized algorithm parsers, which may map
classes to algorithms which they understand (much like Key parsers
do).

**Parameters:**
- algName

- the algorithm name.
- propName

- the name of the property to get.

**Returns:**
- the value of the specified property.

---

#### public static int insertProviderAt​(
Provider
provider,
int position)

Adds a new provider, at a specified position. The position is
the preference order in which providers are searched for
requested algorithms. The position is 1-based, that is,
1 is most preferred, followed by 2, and so on.

If the given provider is installed at the requested position,
the provider that used to be at that position, and all providers
with a position greater than

position

, are shifted up
one position (towards the end of the list of installed providers).

A provider cannot be added if it is already installed.

If there is a security manager, the

SecurityManager.checkSecurityAccess(java.lang.String)

method is called
with the

"insertProvider"

permission target name to see if
it's ok to add a new provider. If this permission check is denied,

checkSecurityAccess

is called again with the

"insertProvider."+provider.getName()

permission target name. If
both checks are denied, a

SecurityException

is thrown.

**Parameters:**
- provider

- the provider to be added.
- position

- the preference position that the caller would
like for this provider.

**Returns:**
- the actual preference position in which the provider was
added, or -1 if the provider was not added because it is
already installed.

**Throws:**
- NullPointerException

- if provider is null
- SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to add a new provider

**See Also:**
- getProvider(java.lang.String)

,

removeProvider(java.lang.String)

,

SecurityPermission

---

#### public static int addProvider​(
Provider
provider)

Adds a provider to the next position available.

If there is a security manager, the

SecurityManager.checkSecurityAccess(java.lang.String)

method is called
with the

"insertProvider"

permission target name to see if
it's ok to add a new provider. If this permission check is denied,

checkSecurityAccess

is called again with the

"insertProvider."+provider.getName()

permission target name. If
both checks are denied, a

SecurityException

is thrown.

**Parameters:**
- provider

- the provider to be added.

**Returns:**
- the preference position in which the provider was
added, or -1 if the provider was not added because it is
already installed.

**Throws:**
- NullPointerException

- if provider is null
- SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to add a new provider

**See Also:**
- getProvider(java.lang.String)

,

removeProvider(java.lang.String)

,

SecurityPermission

---

#### public static void removeProvider​(
String
name)

Removes the provider with the specified name.

When the specified provider is removed, all providers located
at a position greater than where the specified provider was are shifted
down one position (towards the head of the list of installed
providers).

This method returns silently if the provider is not installed or
if name is null.

First, if there is a security manager, its

checkSecurityAccess

method is called with the string

"removeProvider."+name

to see if it's ok to remove the provider.
If the default implementation of

checkSecurityAccess

is used (i.e., that method is not overriden), then this will result in
a call to the security manager's

checkPermission

method
with a

SecurityPermission("removeProvider."+name)

permission.

**Parameters:**
- name

- the name of the provider to remove.

**Throws:**
- SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies
access to remove the provider

**See Also:**
- getProvider(java.lang.String)

,

addProvider(java.security.Provider)

---

#### public static
Provider
[] getProviders()

Returns an array containing all the installed providers. The order of
the providers in the array is their preference order.

**Returns:**
- an array of all the installed providers.

---

#### public static
Provider
getProvider​(
String
name)

Returns the provider installed with the specified name, if
any. Returns null if no provider with the specified name is
installed or if name is null.

**Parameters:**
- name

- the name of the provider to get.

**Returns:**
- the provider of the specified name.

**See Also:**
- removeProvider(java.lang.String)

,

addProvider(java.security.Provider)

---

#### public static
Provider
[] getProviders​(
String
filter)

Returns an array containing all installed providers that satisfy the
specified selection criterion, or null if no such providers have been
installed. The returned providers are ordered
according to their

preference order

.

A cryptographic service is always associated with a particular
algorithm or type. For example, a digital signature service is
always associated with a particular algorithm (e.g., DSA),
and a CertificateFactory service is always associated with
a particular certificate type (e.g., X.509).

The selection criterion must be specified in one of the following two
formats:

- <crypto_service>.<algorithm_or_type>

The cryptographic service name must not contain any dots.

A
provider satisfies the specified selection criterion iff the provider
implements the
specified algorithm or type for the specified cryptographic service.

For example, "CertificateFactory.X.509"
would be satisfied by any provider that supplied
a CertificateFactory implementation for X.509 certificates.

<crypto_service>.<algorithm_or_type>
<attribute_name>:<attribute_value>

The cryptographic service name must not contain any dots. There
must be one or more space characters between the

<algorithm_or_type>

and the

<attribute_name>

.

A provider satisfies this selection criterion iff the
provider implements the specified algorithm or type for the specified
cryptographic service and its implementation meets the
constraint expressed by the specified attribute name/value pair.

For example, "Signature.SHA1withDSA KeySize:1024" would be
satisfied by any provider that implemented
the SHA1withDSA signature algorithm with a keysize of 1024 (or larger).

See the

Java Security Standard Algorithm Names Specification

for information about standard cryptographic service names, standard
algorithm names and standard attribute names.

**Parameters:**
- filter

- the criterion for selecting
providers. The filter is case-insensitive.

**Returns:**
- all the installed providers that satisfy the selection
criterion, or null if no such providers have been installed.

**Throws:**
- InvalidParameterException

- if the filter is not in the required format
- NullPointerException

- if filter is null

**See Also:**
- getProviders(java.util.Map)

**Since:**
- 1.3

---

#### public static
Provider
[] getProviders​(
Map
<
String
,​
String
> filter)

Returns an array containing all installed providers that satisfy the
specified selection criteria, or null if no such providers have been
installed. The returned providers are ordered
according to their

preference order

.

The selection criteria are represented by a map.
Each map entry represents a selection criterion.
A provider is selected iff it satisfies all selection
criteria. The key for any entry in such a map must be in one of the
following two formats:

- <crypto_service>.<algorithm_or_type>

The cryptographic service name must not contain any dots.

The value associated with the key must be an empty string.

A provider
satisfies this selection criterion iff the provider implements the
specified algorithm or type for the specified cryptographic service.

<crypto_service>.
<algorithm_or_type> <attribute_name>

The cryptographic service name must not contain any dots. There
must be one or more space characters between the

<algorithm_or_type>

and the

<attribute_name>

.

The value associated with the key must be a non-empty string.
A provider satisfies this selection criterion iff the
provider implements the specified algorithm or type for the specified
cryptographic service and its implementation meets the
constraint expressed by the specified attribute name/value pair.

See the

Java Security Standard Algorithm Names Specification

for information about standard cryptographic service names, standard
algorithm names and standard attribute names.

**Parameters:**
- filter

- the criteria for selecting
providers. The filter is case-insensitive.

**Returns:**
- all the installed providers that satisfy the selection
criteria, or null if no such providers have been installed.

**Throws:**
- InvalidParameterException

- if the filter is not in the required format
- NullPointerException

- if filter is null

**See Also:**
- getProviders(java.lang.String)

**Since:**
- 1.3

---

#### public static
String
getProperty​(
String
key)

Gets a security property value.

First, if there is a security manager, its

checkPermission

method is called with a

java.security.SecurityPermission("getProperty."+key)

permission to see if it's ok to retrieve the specified
security property value..

**Parameters:**
- key

- the key of the property being retrieved.

**Returns:**
- the value of the security property corresponding to key.

**Throws:**
- SecurityException

- if a security manager exists and its

SecurityManager.checkPermission(java.security.Permission)

method
denies
access to retrieve the specified security property value
- NullPointerException

- is key is null

**See Also:**
- setProperty(java.lang.String, java.lang.String)

,

SecurityPermission

---

#### public static void setProperty​(
String
key,

String
datum)

Sets a security property value.

First, if there is a security manager, its

checkPermission

method is called with a

java.security.SecurityPermission("setProperty."+key)

permission to see if it's ok to set the specified
security property value.

**Parameters:**
- key

- the name of the property to be set.
- datum

- the value of the property to be set.

**Throws:**
- SecurityException

- if a security manager exists and its

SecurityManager.checkPermission(java.security.Permission)

method
denies access to set the specified security property value
- NullPointerException

- if key or datum is null

**See Also:**
- getProperty(java.lang.String)

,

SecurityPermission

---

#### public static
Set
<
String
> getAlgorithms​(
String
serviceName)

Returns a Set of Strings containing the names of all available
algorithms or types for the specified Java cryptographic service
(e.g., Signature, MessageDigest, Cipher, Mac, KeyStore). Returns
an empty Set if there is no provider that supports the
specified service or if serviceName is null. For a complete list
of Java cryptographic services, please see the

Java Cryptography Architecture (JCA) Reference Guide

.
Note: the returned set is immutable.

**Parameters:**
- serviceName

- the name of the Java cryptographic
service (e.g., Signature, MessageDigest, Cipher, Mac, KeyStore).
Note: this parameter is case-insensitive.

**Returns:**
- a Set of Strings containing the names of all available
algorithms or types for the specified Java cryptographic service
or an empty set if no provider supports the specified service.

**Since:**
- 1.4

---

### Additional Sections

#### Class Security

java.lang.Object

- java.security.Security

java.security.Security

```java
public final class
Security

extends
Object
```

This class centralizes all security properties and common security
methods. One of its primary uses is to manage providers.

The default values of security properties are read from an
implementation-specific location, which is typically the properties file

conf/security/java.security

in the Java installation directory.

**Implementation Note:** If the properties file fails to load, the JDK implementation will
throw an unspecified error when initializing the

Security

class.
**Since:** 1.1

public final class

Security

extends

Object

This class centralizes all security properties and common security
methods. One of its primary uses is to manage providers.

The default values of security properties are read from an
implementation-specific location, which is typically the properties file

conf/security/java.security

in the Java installation directory.

The default values of security properties are read from an
implementation-specific location, which is typically the properties file

conf/security/java.security

in the Java installation directory.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

static int

addProvider

​(

Provider

provider)

Adds a provider to the next position available.

static

String

getAlgorithmProperty

​(

String

algName,

String

propName)

Deprecated.

This method used to return the value of a proprietary
property in the master file of the "SUN" Cryptographic Service
Provider in order to determine how to parse algorithm-specific
parameters.

static

Set

<

String

>

getAlgorithms

​(

String

serviceName)

Returns a Set of Strings containing the names of all available
algorithms or types for the specified Java cryptographic service
(e.g., Signature, MessageDigest, Cipher, Mac, KeyStore).

static

String

getProperty

​(

String

key)

Gets a security property value.

static

Provider

getProvider

​(

String

name)

Returns the provider installed with the specified name, if
any.

static

Provider

[]

getProviders

()

Returns an array containing all the installed providers.

static

Provider

[]

getProviders

​(

String

filter)

Returns an array containing all installed providers that satisfy the
specified selection criterion, or null if no such providers have been
installed.

static

Provider

[]

getProviders

​(

Map

<

String

,​

String

> filter)

Returns an array containing all installed providers that satisfy the
specified selection criteria, or null if no such providers have been
installed.

static int

insertProviderAt

​(

Provider

provider,
int position)

Adds a new provider, at a specified position.

static void

removeProvider

​(

String

name)

Removes the provider with the specified name.

static void

setProperty

​(

String

key,

String

datum)

Sets a security property value.

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

Method Summary

All Methods

Static Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

static int

addProvider

​(

Provider

provider)

Adds a provider to the next position available.

static

String

getAlgorithmProperty

​(

String

algName,

String

propName)

Deprecated.

This method used to return the value of a proprietary
property in the master file of the "SUN" Cryptographic Service
Provider in order to determine how to parse algorithm-specific
parameters.

static

Set

<

String

>

getAlgorithms

​(

String

serviceName)

Returns a Set of Strings containing the names of all available
algorithms or types for the specified Java cryptographic service
(e.g., Signature, MessageDigest, Cipher, Mac, KeyStore).

static

String

getProperty

​(

String

key)

Gets a security property value.

static

Provider

getProvider

​(

String

name)

Returns the provider installed with the specified name, if
any.

static

Provider

[]

getProviders

()

Returns an array containing all the installed providers.

static

Provider

[]

getProviders

​(

String

filter)

Returns an array containing all installed providers that satisfy the
specified selection criterion, or null if no such providers have been
installed.

static

Provider

[]

getProviders

​(

Map

<

String

,​

String

> filter)

Returns an array containing all installed providers that satisfy the
specified selection criteria, or null if no such providers have been
installed.

static int

insertProviderAt

​(

Provider

provider,
int position)

Adds a new provider, at a specified position.

static void

removeProvider

​(

String

name)

Removes the provider with the specified name.

static void

setProperty

​(

String

key,

String

datum)

Sets a security property value.

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

Adds a provider to the next position available.

Deprecated.

This method used to return the value of a proprietary
property in the master file of the "SUN" Cryptographic Service
Provider in order to determine how to parse algorithm-specific
parameters.

Returns a Set of Strings containing the names of all available
algorithms or types for the specified Java cryptographic service
(e.g., Signature, MessageDigest, Cipher, Mac, KeyStore).

Gets a security property value.

Returns the provider installed with the specified name, if
any.

Returns an array containing all the installed providers.

Returns an array containing all installed providers that satisfy the
specified selection criterion, or null if no such providers have been
installed.

Returns an array containing all installed providers that satisfy the
specified selection criteria, or null if no such providers have been
installed.

Adds a new provider, at a specified position.

Removes the provider with the specified name.

Sets a security property value.

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

============ METHOD DETAIL ==========

- Method Detail

- getAlgorithmProperty

```java
@Deprecated

public static
String
getAlgorithmProperty​(
String
algName,

String
propName)
```

Deprecated.

This method used to return the value of a proprietary
property in the master file of the "SUN" Cryptographic Service
Provider in order to determine how to parse algorithm-specific
parameters. Use the new provider-based and algorithm-independent

AlgorithmParameters

and

KeyFactory

engine
classes (introduced in the J2SE version 1.2 platform) instead.

Gets a specified property for an algorithm. The algorithm name
should be a standard name. See the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.

One possible use is by specialized algorithm parsers, which may map
classes to algorithms which they understand (much like Key parsers
do).

**Parameters:** algName

- the algorithm name.
**Parameters:** propName

- the name of the property to get.
**Returns:** the value of the specified property.

- insertProviderAt

```java
public static int insertProviderAt​(
Provider
provider,
int position)
```

Adds a new provider, at a specified position. The position is
the preference order in which providers are searched for
requested algorithms. The position is 1-based, that is,
1 is most preferred, followed by 2, and so on.

If the given provider is installed at the requested position,
the provider that used to be at that position, and all providers
with a position greater than

position

, are shifted up
one position (towards the end of the list of installed providers).

A provider cannot be added if it is already installed.

If there is a security manager, the

SecurityManager.checkSecurityAccess(java.lang.String)

method is called
with the

"insertProvider"

permission target name to see if
it's ok to add a new provider. If this permission check is denied,

checkSecurityAccess

is called again with the

"insertProvider."+provider.getName()

permission target name. If
both checks are denied, a

SecurityException

is thrown.

**Parameters:** provider

- the provider to be added.
**Parameters:** position

- the preference position that the caller would
like for this provider.
**Returns:** the actual preference position in which the provider was
added, or -1 if the provider was not added because it is
already installed.
**Throws:** NullPointerException

- if provider is null
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to add a new provider
**See Also:** getProvider(java.lang.String)

,

removeProvider(java.lang.String)

,

SecurityPermission

- addProvider

```java
public static int addProvider​(
Provider
provider)
```

Adds a provider to the next position available.

If there is a security manager, the

SecurityManager.checkSecurityAccess(java.lang.String)

method is called
with the

"insertProvider"

permission target name to see if
it's ok to add a new provider. If this permission check is denied,

checkSecurityAccess

is called again with the

"insertProvider."+provider.getName()

permission target name. If
both checks are denied, a

SecurityException

is thrown.

**Parameters:** provider

- the provider to be added.
**Returns:** the preference position in which the provider was
added, or -1 if the provider was not added because it is
already installed.
**Throws:** NullPointerException

- if provider is null
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to add a new provider
**See Also:** getProvider(java.lang.String)

,

removeProvider(java.lang.String)

,

SecurityPermission

- removeProvider

```java
public static void removeProvider​(
String
name)
```

Removes the provider with the specified name.

When the specified provider is removed, all providers located
at a position greater than where the specified provider was are shifted
down one position (towards the head of the list of installed
providers).

This method returns silently if the provider is not installed or
if name is null.

First, if there is a security manager, its

checkSecurityAccess

method is called with the string

"removeProvider."+name

to see if it's ok to remove the provider.
If the default implementation of

checkSecurityAccess

is used (i.e., that method is not overriden), then this will result in
a call to the security manager's

checkPermission

method
with a

SecurityPermission("removeProvider."+name)

permission.

**Parameters:** name

- the name of the provider to remove.
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies
access to remove the provider
**See Also:** getProvider(java.lang.String)

,

addProvider(java.security.Provider)

- getProviders

```java
public static
Provider
[] getProviders()
```

Returns an array containing all the installed providers. The order of
the providers in the array is their preference order.

**Returns:** an array of all the installed providers.

- getProvider

```java
public static
Provider
getProvider​(
String
name)
```

Returns the provider installed with the specified name, if
any. Returns null if no provider with the specified name is
installed or if name is null.

**Parameters:** name

- the name of the provider to get.
**Returns:** the provider of the specified name.
**See Also:** removeProvider(java.lang.String)

,

addProvider(java.security.Provider)

- getProviders

```java
public static
Provider
[] getProviders​(
String
filter)
```

Returns an array containing all installed providers that satisfy the
specified selection criterion, or null if no such providers have been
installed. The returned providers are ordered
according to their

preference order

.

A cryptographic service is always associated with a particular
algorithm or type. For example, a digital signature service is
always associated with a particular algorithm (e.g., DSA),
and a CertificateFactory service is always associated with
a particular certificate type (e.g., X.509).

The selection criterion must be specified in one of the following two
formats:

- <crypto_service>.<algorithm_or_type>

The cryptographic service name must not contain any dots.

A
provider satisfies the specified selection criterion iff the provider
implements the
specified algorithm or type for the specified cryptographic service.

For example, "CertificateFactory.X.509"
would be satisfied by any provider that supplied
a CertificateFactory implementation for X.509 certificates.

<crypto_service>.<algorithm_or_type>
<attribute_name>:<attribute_value>

The cryptographic service name must not contain any dots. There
must be one or more space characters between the

<algorithm_or_type>

and the

<attribute_name>

.

A provider satisfies this selection criterion iff the
provider implements the specified algorithm or type for the specified
cryptographic service and its implementation meets the
constraint expressed by the specified attribute name/value pair.

For example, "Signature.SHA1withDSA KeySize:1024" would be
satisfied by any provider that implemented
the SHA1withDSA signature algorithm with a keysize of 1024 (or larger).

See the

Java Security Standard Algorithm Names Specification

for information about standard cryptographic service names, standard
algorithm names and standard attribute names.

**Parameters:** filter

- the criterion for selecting
providers. The filter is case-insensitive.
**Returns:** all the installed providers that satisfy the selection
criterion, or null if no such providers have been installed.
**Throws:** InvalidParameterException

- if the filter is not in the required format
**Throws:** NullPointerException

- if filter is null
**Since:** 1.3
**See Also:** getProviders(java.util.Map)

- getProviders

```java
public static
Provider
[] getProviders​(
Map
<
String
,​
String
> filter)
```

Returns an array containing all installed providers that satisfy the
specified selection criteria, or null if no such providers have been
installed. The returned providers are ordered
according to their

preference order

.

The selection criteria are represented by a map.
Each map entry represents a selection criterion.
A provider is selected iff it satisfies all selection
criteria. The key for any entry in such a map must be in one of the
following two formats:

- <crypto_service>.<algorithm_or_type>

The cryptographic service name must not contain any dots.

The value associated with the key must be an empty string.

A provider
satisfies this selection criterion iff the provider implements the
specified algorithm or type for the specified cryptographic service.

<crypto_service>.
<algorithm_or_type> <attribute_name>

The cryptographic service name must not contain any dots. There
must be one or more space characters between the

<algorithm_or_type>

and the

<attribute_name>

.

The value associated with the key must be a non-empty string.
A provider satisfies this selection criterion iff the
provider implements the specified algorithm or type for the specified
cryptographic service and its implementation meets the
constraint expressed by the specified attribute name/value pair.

See the

Java Security Standard Algorithm Names Specification

for information about standard cryptographic service names, standard
algorithm names and standard attribute names.

**Parameters:** filter

- the criteria for selecting
providers. The filter is case-insensitive.
**Returns:** all the installed providers that satisfy the selection
criteria, or null if no such providers have been installed.
**Throws:** InvalidParameterException

- if the filter is not in the required format
**Throws:** NullPointerException

- if filter is null
**Since:** 1.3
**See Also:** getProviders(java.lang.String)

- getProperty

```java
public static
String
getProperty​(
String
key)
```

Gets a security property value.

First, if there is a security manager, its

checkPermission

method is called with a

java.security.SecurityPermission("getProperty."+key)

permission to see if it's ok to retrieve the specified
security property value..

**Parameters:** key

- the key of the property being retrieved.
**Returns:** the value of the security property corresponding to key.
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkPermission(java.security.Permission)

method
denies
access to retrieve the specified security property value
**Throws:** NullPointerException

- is key is null
**See Also:** setProperty(java.lang.String, java.lang.String)

,

SecurityPermission

- setProperty

```java
public static void setProperty​(
String
key,

String
datum)
```

Sets a security property value.

First, if there is a security manager, its

checkPermission

method is called with a

java.security.SecurityPermission("setProperty."+key)

permission to see if it's ok to set the specified
security property value.

**Parameters:** key

- the name of the property to be set.
**Parameters:** datum

- the value of the property to be set.
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkPermission(java.security.Permission)

method
denies access to set the specified security property value
**Throws:** NullPointerException

- if key or datum is null
**See Also:** getProperty(java.lang.String)

,

SecurityPermission

- getAlgorithms

```java
public static
Set
<
String
> getAlgorithms​(
String
serviceName)
```

Returns a Set of Strings containing the names of all available
algorithms or types for the specified Java cryptographic service
(e.g., Signature, MessageDigest, Cipher, Mac, KeyStore). Returns
an empty Set if there is no provider that supports the
specified service or if serviceName is null. For a complete list
of Java cryptographic services, please see the

Java Cryptography Architecture (JCA) Reference Guide

.
Note: the returned set is immutable.

**Parameters:** serviceName

- the name of the Java cryptographic
service (e.g., Signature, MessageDigest, Cipher, Mac, KeyStore).
Note: this parameter is case-insensitive.
**Returns:** a Set of Strings containing the names of all available
algorithms or types for the specified Java cryptographic service
or an empty set if no provider supports the specified service.
**Since:** 1.4

Method Detail

- getAlgorithmProperty

```java
@Deprecated

public static
String
getAlgorithmProperty​(
String
algName,

String
propName)
```

Deprecated.

This method used to return the value of a proprietary
property in the master file of the "SUN" Cryptographic Service
Provider in order to determine how to parse algorithm-specific
parameters. Use the new provider-based and algorithm-independent

AlgorithmParameters

and

KeyFactory

engine
classes (introduced in the J2SE version 1.2 platform) instead.

Gets a specified property for an algorithm. The algorithm name
should be a standard name. See the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.

One possible use is by specialized algorithm parsers, which may map
classes to algorithms which they understand (much like Key parsers
do).

**Parameters:** algName

- the algorithm name.
**Parameters:** propName

- the name of the property to get.
**Returns:** the value of the specified property.

- insertProviderAt

```java
public static int insertProviderAt​(
Provider
provider,
int position)
```

Adds a new provider, at a specified position. The position is
the preference order in which providers are searched for
requested algorithms. The position is 1-based, that is,
1 is most preferred, followed by 2, and so on.

If the given provider is installed at the requested position,
the provider that used to be at that position, and all providers
with a position greater than

position

, are shifted up
one position (towards the end of the list of installed providers).

A provider cannot be added if it is already installed.

If there is a security manager, the

SecurityManager.checkSecurityAccess(java.lang.String)

method is called
with the

"insertProvider"

permission target name to see if
it's ok to add a new provider. If this permission check is denied,

checkSecurityAccess

is called again with the

"insertProvider."+provider.getName()

permission target name. If
both checks are denied, a

SecurityException

is thrown.

**Parameters:** provider

- the provider to be added.
**Parameters:** position

- the preference position that the caller would
like for this provider.
**Returns:** the actual preference position in which the provider was
added, or -1 if the provider was not added because it is
already installed.
**Throws:** NullPointerException

- if provider is null
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to add a new provider
**See Also:** getProvider(java.lang.String)

,

removeProvider(java.lang.String)

,

SecurityPermission

- addProvider

```java
public static int addProvider​(
Provider
provider)
```

Adds a provider to the next position available.

If there is a security manager, the

SecurityManager.checkSecurityAccess(java.lang.String)

method is called
with the

"insertProvider"

permission target name to see if
it's ok to add a new provider. If this permission check is denied,

checkSecurityAccess

is called again with the

"insertProvider."+provider.getName()

permission target name. If
both checks are denied, a

SecurityException

is thrown.

**Parameters:** provider

- the provider to be added.
**Returns:** the preference position in which the provider was
added, or -1 if the provider was not added because it is
already installed.
**Throws:** NullPointerException

- if provider is null
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to add a new provider
**See Also:** getProvider(java.lang.String)

,

removeProvider(java.lang.String)

,

SecurityPermission

- removeProvider

```java
public static void removeProvider​(
String
name)
```

Removes the provider with the specified name.

When the specified provider is removed, all providers located
at a position greater than where the specified provider was are shifted
down one position (towards the head of the list of installed
providers).

This method returns silently if the provider is not installed or
if name is null.

First, if there is a security manager, its

checkSecurityAccess

method is called with the string

"removeProvider."+name

to see if it's ok to remove the provider.
If the default implementation of

checkSecurityAccess

is used (i.e., that method is not overriden), then this will result in
a call to the security manager's

checkPermission

method
with a

SecurityPermission("removeProvider."+name)

permission.

**Parameters:** name

- the name of the provider to remove.
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies
access to remove the provider
**See Also:** getProvider(java.lang.String)

,

addProvider(java.security.Provider)

- getProviders

```java
public static
Provider
[] getProviders()
```

Returns an array containing all the installed providers. The order of
the providers in the array is their preference order.

**Returns:** an array of all the installed providers.

- getProvider

```java
public static
Provider
getProvider​(
String
name)
```

Returns the provider installed with the specified name, if
any. Returns null if no provider with the specified name is
installed or if name is null.

**Parameters:** name

- the name of the provider to get.
**Returns:** the provider of the specified name.
**See Also:** removeProvider(java.lang.String)

,

addProvider(java.security.Provider)

- getProviders

```java
public static
Provider
[] getProviders​(
String
filter)
```

Returns an array containing all installed providers that satisfy the
specified selection criterion, or null if no such providers have been
installed. The returned providers are ordered
according to their

preference order

.

A cryptographic service is always associated with a particular
algorithm or type. For example, a digital signature service is
always associated with a particular algorithm (e.g., DSA),
and a CertificateFactory service is always associated with
a particular certificate type (e.g., X.509).

The selection criterion must be specified in one of the following two
formats:

- <crypto_service>.<algorithm_or_type>

The cryptographic service name must not contain any dots.

A
provider satisfies the specified selection criterion iff the provider
implements the
specified algorithm or type for the specified cryptographic service.

For example, "CertificateFactory.X.509"
would be satisfied by any provider that supplied
a CertificateFactory implementation for X.509 certificates.

<crypto_service>.<algorithm_or_type>
<attribute_name>:<attribute_value>

The cryptographic service name must not contain any dots. There
must be one or more space characters between the

<algorithm_or_type>

and the

<attribute_name>

.

A provider satisfies this selection criterion iff the
provider implements the specified algorithm or type for the specified
cryptographic service and its implementation meets the
constraint expressed by the specified attribute name/value pair.

For example, "Signature.SHA1withDSA KeySize:1024" would be
satisfied by any provider that implemented
the SHA1withDSA signature algorithm with a keysize of 1024 (or larger).

See the

Java Security Standard Algorithm Names Specification

for information about standard cryptographic service names, standard
algorithm names and standard attribute names.

**Parameters:** filter

- the criterion for selecting
providers. The filter is case-insensitive.
**Returns:** all the installed providers that satisfy the selection
criterion, or null if no such providers have been installed.
**Throws:** InvalidParameterException

- if the filter is not in the required format
**Throws:** NullPointerException

- if filter is null
**Since:** 1.3
**See Also:** getProviders(java.util.Map)

- getProviders

```java
public static
Provider
[] getProviders​(
Map
<
String
,​
String
> filter)
```

Returns an array containing all installed providers that satisfy the
specified selection criteria, or null if no such providers have been
installed. The returned providers are ordered
according to their

preference order

.

The selection criteria are represented by a map.
Each map entry represents a selection criterion.
A provider is selected iff it satisfies all selection
criteria. The key for any entry in such a map must be in one of the
following two formats:

- <crypto_service>.<algorithm_or_type>

The cryptographic service name must not contain any dots.

The value associated with the key must be an empty string.

A provider
satisfies this selection criterion iff the provider implements the
specified algorithm or type for the specified cryptographic service.

<crypto_service>.
<algorithm_or_type> <attribute_name>

The cryptographic service name must not contain any dots. There
must be one or more space characters between the

<algorithm_or_type>

and the

<attribute_name>

.

The value associated with the key must be a non-empty string.
A provider satisfies this selection criterion iff the
provider implements the specified algorithm or type for the specified
cryptographic service and its implementation meets the
constraint expressed by the specified attribute name/value pair.

See the

Java Security Standard Algorithm Names Specification

for information about standard cryptographic service names, standard
algorithm names and standard attribute names.

**Parameters:** filter

- the criteria for selecting
providers. The filter is case-insensitive.
**Returns:** all the installed providers that satisfy the selection
criteria, or null if no such providers have been installed.
**Throws:** InvalidParameterException

- if the filter is not in the required format
**Throws:** NullPointerException

- if filter is null
**Since:** 1.3
**See Also:** getProviders(java.lang.String)

- getProperty

```java
public static
String
getProperty​(
String
key)
```

Gets a security property value.

First, if there is a security manager, its

checkPermission

method is called with a

java.security.SecurityPermission("getProperty."+key)

permission to see if it's ok to retrieve the specified
security property value..

**Parameters:** key

- the key of the property being retrieved.
**Returns:** the value of the security property corresponding to key.
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkPermission(java.security.Permission)

method
denies
access to retrieve the specified security property value
**Throws:** NullPointerException

- is key is null
**See Also:** setProperty(java.lang.String, java.lang.String)

,

SecurityPermission

- setProperty

```java
public static void setProperty​(
String
key,

String
datum)
```

Sets a security property value.

First, if there is a security manager, its

checkPermission

method is called with a

java.security.SecurityPermission("setProperty."+key)

permission to see if it's ok to set the specified
security property value.

**Parameters:** key

- the name of the property to be set.
**Parameters:** datum

- the value of the property to be set.
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkPermission(java.security.Permission)

method
denies access to set the specified security property value
**Throws:** NullPointerException

- if key or datum is null
**See Also:** getProperty(java.lang.String)

,

SecurityPermission

- getAlgorithms

```java
public static
Set
<
String
> getAlgorithms​(
String
serviceName)
```

Returns a Set of Strings containing the names of all available
algorithms or types for the specified Java cryptographic service
(e.g., Signature, MessageDigest, Cipher, Mac, KeyStore). Returns
an empty Set if there is no provider that supports the
specified service or if serviceName is null. For a complete list
of Java cryptographic services, please see the

Java Cryptography Architecture (JCA) Reference Guide

.
Note: the returned set is immutable.

**Parameters:** serviceName

- the name of the Java cryptographic
service (e.g., Signature, MessageDigest, Cipher, Mac, KeyStore).
Note: this parameter is case-insensitive.
**Returns:** a Set of Strings containing the names of all available
algorithms or types for the specified Java cryptographic service
or an empty set if no provider supports the specified service.
**Since:** 1.4

---

#### Method Detail

getAlgorithmProperty

```java
@Deprecated

public static
String
getAlgorithmProperty​(
String
algName,

String
propName)
```

Deprecated.

This method used to return the value of a proprietary
property in the master file of the "SUN" Cryptographic Service
Provider in order to determine how to parse algorithm-specific
parameters. Use the new provider-based and algorithm-independent

AlgorithmParameters

and

KeyFactory

engine
classes (introduced in the J2SE version 1.2 platform) instead.

Gets a specified property for an algorithm. The algorithm name
should be a standard name. See the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.

One possible use is by specialized algorithm parsers, which may map
classes to algorithms which they understand (much like Key parsers
do).

**Parameters:** algName

- the algorithm name.
**Parameters:** propName

- the name of the property to get.
**Returns:** the value of the specified property.

---

#### getAlgorithmProperty

@Deprecated

public static

String

getAlgorithmProperty​(

String

algName,

String

propName)

Gets a specified property for an algorithm. The algorithm name
should be a standard name. See the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.

One possible use is by specialized algorithm parsers, which may map
classes to algorithms which they understand (much like Key parsers
do).

insertProviderAt

```java
public static int insertProviderAt​(
Provider
provider,
int position)
```

Adds a new provider, at a specified position. The position is
the preference order in which providers are searched for
requested algorithms. The position is 1-based, that is,
1 is most preferred, followed by 2, and so on.

If the given provider is installed at the requested position,
the provider that used to be at that position, and all providers
with a position greater than

position

, are shifted up
one position (towards the end of the list of installed providers).

A provider cannot be added if it is already installed.

If there is a security manager, the

SecurityManager.checkSecurityAccess(java.lang.String)

method is called
with the

"insertProvider"

permission target name to see if
it's ok to add a new provider. If this permission check is denied,

checkSecurityAccess

is called again with the

"insertProvider."+provider.getName()

permission target name. If
both checks are denied, a

SecurityException

is thrown.

**Parameters:** provider

- the provider to be added.
**Parameters:** position

- the preference position that the caller would
like for this provider.
**Returns:** the actual preference position in which the provider was
added, or -1 if the provider was not added because it is
already installed.
**Throws:** NullPointerException

- if provider is null
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to add a new provider
**See Also:** getProvider(java.lang.String)

,

removeProvider(java.lang.String)

,

SecurityPermission

---

#### insertProviderAt

public static int insertProviderAt​(

Provider

provider,
int position)

Adds a new provider, at a specified position. The position is
the preference order in which providers are searched for
requested algorithms. The position is 1-based, that is,
1 is most preferred, followed by 2, and so on.

If the given provider is installed at the requested position,
the provider that used to be at that position, and all providers
with a position greater than

position

, are shifted up
one position (towards the end of the list of installed providers).

A provider cannot be added if it is already installed.

If there is a security manager, the

SecurityManager.checkSecurityAccess(java.lang.String)

method is called
with the

"insertProvider"

permission target name to see if
it's ok to add a new provider. If this permission check is denied,

checkSecurityAccess

is called again with the

"insertProvider."+provider.getName()

permission target name. If
both checks are denied, a

SecurityException

is thrown.

If the given provider is installed at the requested position,
the provider that used to be at that position, and all providers
with a position greater than

position

, are shifted up
one position (towards the end of the list of installed providers).

A provider cannot be added if it is already installed.

If there is a security manager, the

SecurityManager.checkSecurityAccess(java.lang.String)

method is called
with the

"insertProvider"

permission target name to see if
it's ok to add a new provider. If this permission check is denied,

checkSecurityAccess

is called again with the

"insertProvider."+provider.getName()

permission target name. If
both checks are denied, a

SecurityException

is thrown.

A provider cannot be added if it is already installed.

If there is a security manager, the

SecurityManager.checkSecurityAccess(java.lang.String)

method is called
with the

"insertProvider"

permission target name to see if
it's ok to add a new provider. If this permission check is denied,

checkSecurityAccess

is called again with the

"insertProvider."+provider.getName()

permission target name. If
both checks are denied, a

SecurityException

is thrown.

If there is a security manager, the

SecurityManager.checkSecurityAccess(java.lang.String)

method is called
with the

"insertProvider"

permission target name to see if
it's ok to add a new provider. If this permission check is denied,

checkSecurityAccess

is called again with the

"insertProvider."+provider.getName()

permission target name. If
both checks are denied, a

SecurityException

is thrown.

addProvider

```java
public static int addProvider​(
Provider
provider)
```

Adds a provider to the next position available.

If there is a security manager, the

SecurityManager.checkSecurityAccess(java.lang.String)

method is called
with the

"insertProvider"

permission target name to see if
it's ok to add a new provider. If this permission check is denied,

checkSecurityAccess

is called again with the

"insertProvider."+provider.getName()

permission target name. If
both checks are denied, a

SecurityException

is thrown.

**Parameters:** provider

- the provider to be added.
**Returns:** the preference position in which the provider was
added, or -1 if the provider was not added because it is
already installed.
**Throws:** NullPointerException

- if provider is null
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to add a new provider
**See Also:** getProvider(java.lang.String)

,

removeProvider(java.lang.String)

,

SecurityPermission

---

#### addProvider

public static int addProvider​(

Provider

provider)

Adds a provider to the next position available.

If there is a security manager, the

SecurityManager.checkSecurityAccess(java.lang.String)

method is called
with the

"insertProvider"

permission target name to see if
it's ok to add a new provider. If this permission check is denied,

checkSecurityAccess

is called again with the

"insertProvider."+provider.getName()

permission target name. If
both checks are denied, a

SecurityException

is thrown.

If there is a security manager, the

SecurityManager.checkSecurityAccess(java.lang.String)

method is called
with the

"insertProvider"

permission target name to see if
it's ok to add a new provider. If this permission check is denied,

checkSecurityAccess

is called again with the

"insertProvider."+provider.getName()

permission target name. If
both checks are denied, a

SecurityException

is thrown.

removeProvider

```java
public static void removeProvider​(
String
name)
```

Removes the provider with the specified name.

When the specified provider is removed, all providers located
at a position greater than where the specified provider was are shifted
down one position (towards the head of the list of installed
providers).

This method returns silently if the provider is not installed or
if name is null.

First, if there is a security manager, its

checkSecurityAccess

method is called with the string

"removeProvider."+name

to see if it's ok to remove the provider.
If the default implementation of

checkSecurityAccess

is used (i.e., that method is not overriden), then this will result in
a call to the security manager's

checkPermission

method
with a

SecurityPermission("removeProvider."+name)

permission.

**Parameters:** name

- the name of the provider to remove.
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies
access to remove the provider
**See Also:** getProvider(java.lang.String)

,

addProvider(java.security.Provider)

---

#### removeProvider

public static void removeProvider​(

String

name)

Removes the provider with the specified name.

When the specified provider is removed, all providers located
at a position greater than where the specified provider was are shifted
down one position (towards the head of the list of installed
providers).

This method returns silently if the provider is not installed or
if name is null.

First, if there is a security manager, its

checkSecurityAccess

method is called with the string

"removeProvider."+name

to see if it's ok to remove the provider.
If the default implementation of

checkSecurityAccess

is used (i.e., that method is not overriden), then this will result in
a call to the security manager's

checkPermission

method
with a

SecurityPermission("removeProvider."+name)

permission.

When the specified provider is removed, all providers located
at a position greater than where the specified provider was are shifted
down one position (towards the head of the list of installed
providers).

This method returns silently if the provider is not installed or
if name is null.

First, if there is a security manager, its

checkSecurityAccess

method is called with the string

"removeProvider."+name

to see if it's ok to remove the provider.
If the default implementation of

checkSecurityAccess

is used (i.e., that method is not overriden), then this will result in
a call to the security manager's

checkPermission

method
with a

SecurityPermission("removeProvider."+name)

permission.

This method returns silently if the provider is not installed or
if name is null.

First, if there is a security manager, its

checkSecurityAccess

method is called with the string

"removeProvider."+name

to see if it's ok to remove the provider.
If the default implementation of

checkSecurityAccess

is used (i.e., that method is not overriden), then this will result in
a call to the security manager's

checkPermission

method
with a

SecurityPermission("removeProvider."+name)

permission.

First, if there is a security manager, its

checkSecurityAccess

method is called with the string

"removeProvider."+name

to see if it's ok to remove the provider.
If the default implementation of

checkSecurityAccess

is used (i.e., that method is not overriden), then this will result in
a call to the security manager's

checkPermission

method
with a

SecurityPermission("removeProvider."+name)

permission.

getProviders

```java
public static
Provider
[] getProviders()
```

Returns an array containing all the installed providers. The order of
the providers in the array is their preference order.

**Returns:** an array of all the installed providers.

---

#### getProviders

public static

Provider

[] getProviders()

Returns an array containing all the installed providers. The order of
the providers in the array is their preference order.

getProvider

```java
public static
Provider
getProvider​(
String
name)
```

Returns the provider installed with the specified name, if
any. Returns null if no provider with the specified name is
installed or if name is null.

**Parameters:** name

- the name of the provider to get.
**Returns:** the provider of the specified name.
**See Also:** removeProvider(java.lang.String)

,

addProvider(java.security.Provider)

---

#### getProvider

public static

Provider

getProvider​(

String

name)

Returns the provider installed with the specified name, if
any. Returns null if no provider with the specified name is
installed or if name is null.

getProviders

```java
public static
Provider
[] getProviders​(
String
filter)
```

Returns an array containing all installed providers that satisfy the
specified selection criterion, or null if no such providers have been
installed. The returned providers are ordered
according to their

preference order

.

A cryptographic service is always associated with a particular
algorithm or type. For example, a digital signature service is
always associated with a particular algorithm (e.g., DSA),
and a CertificateFactory service is always associated with
a particular certificate type (e.g., X.509).

The selection criterion must be specified in one of the following two
formats:

- <crypto_service>.<algorithm_or_type>

The cryptographic service name must not contain any dots.

A
provider satisfies the specified selection criterion iff the provider
implements the
specified algorithm or type for the specified cryptographic service.

For example, "CertificateFactory.X.509"
would be satisfied by any provider that supplied
a CertificateFactory implementation for X.509 certificates.

<crypto_service>.<algorithm_or_type>
<attribute_name>:<attribute_value>

The cryptographic service name must not contain any dots. There
must be one or more space characters between the

<algorithm_or_type>

and the

<attribute_name>

.

A provider satisfies this selection criterion iff the
provider implements the specified algorithm or type for the specified
cryptographic service and its implementation meets the
constraint expressed by the specified attribute name/value pair.

For example, "Signature.SHA1withDSA KeySize:1024" would be
satisfied by any provider that implemented
the SHA1withDSA signature algorithm with a keysize of 1024 (or larger).

See the

Java Security Standard Algorithm Names Specification

for information about standard cryptographic service names, standard
algorithm names and standard attribute names.

**Parameters:** filter

- the criterion for selecting
providers. The filter is case-insensitive.
**Returns:** all the installed providers that satisfy the selection
criterion, or null if no such providers have been installed.
**Throws:** InvalidParameterException

- if the filter is not in the required format
**Throws:** NullPointerException

- if filter is null
**Since:** 1.3
**See Also:** getProviders(java.util.Map)

---

#### getProviders

public static

Provider

[] getProviders​(

String

filter)

Returns an array containing all installed providers that satisfy the
specified selection criterion, or null if no such providers have been
installed. The returned providers are ordered
according to their

preference order

.

A cryptographic service is always associated with a particular
algorithm or type. For example, a digital signature service is
always associated with a particular algorithm (e.g., DSA),
and a CertificateFactory service is always associated with
a particular certificate type (e.g., X.509).

The selection criterion must be specified in one of the following two
formats:

- <crypto_service>.<algorithm_or_type>

The cryptographic service name must not contain any dots.

A
provider satisfies the specified selection criterion iff the provider
implements the
specified algorithm or type for the specified cryptographic service.

For example, "CertificateFactory.X.509"
would be satisfied by any provider that supplied
a CertificateFactory implementation for X.509 certificates.

<crypto_service>.<algorithm_or_type>
<attribute_name>:<attribute_value>

The cryptographic service name must not contain any dots. There
must be one or more space characters between the

<algorithm_or_type>

and the

<attribute_name>

.

A provider satisfies this selection criterion iff the
provider implements the specified algorithm or type for the specified
cryptographic service and its implementation meets the
constraint expressed by the specified attribute name/value pair.

For example, "Signature.SHA1withDSA KeySize:1024" would be
satisfied by any provider that implemented
the SHA1withDSA signature algorithm with a keysize of 1024 (or larger).

See the

Java Security Standard Algorithm Names Specification

for information about standard cryptographic service names, standard
algorithm names and standard attribute names.

A cryptographic service is always associated with a particular
algorithm or type. For example, a digital signature service is
always associated with a particular algorithm (e.g., DSA),
and a CertificateFactory service is always associated with
a particular certificate type (e.g., X.509).

The selection criterion must be specified in one of the following two
formats:

- <crypto_service>.<algorithm_or_type>

The cryptographic service name must not contain any dots.

A
provider satisfies the specified selection criterion iff the provider
implements the
specified algorithm or type for the specified cryptographic service.

For example, "CertificateFactory.X.509"
would be satisfied by any provider that supplied
a CertificateFactory implementation for X.509 certificates.

<crypto_service>.<algorithm_or_type>
<attribute_name>:<attribute_value>

The cryptographic service name must not contain any dots. There
must be one or more space characters between the

<algorithm_or_type>

and the

<attribute_name>

.

A provider satisfies this selection criterion iff the
provider implements the specified algorithm or type for the specified
cryptographic service and its implementation meets the
constraint expressed by the specified attribute name/value pair.

For example, "Signature.SHA1withDSA KeySize:1024" would be
satisfied by any provider that implemented
the SHA1withDSA signature algorithm with a keysize of 1024 (or larger).

See the

Java Security Standard Algorithm Names Specification

for information about standard cryptographic service names, standard
algorithm names and standard attribute names.

The selection criterion must be specified in one of the following two
formats:

- <crypto_service>.<algorithm_or_type>

The cryptographic service name must not contain any dots.

A
provider satisfies the specified selection criterion iff the provider
implements the
specified algorithm or type for the specified cryptographic service.

For example, "CertificateFactory.X.509"
would be satisfied by any provider that supplied
a CertificateFactory implementation for X.509 certificates.

<crypto_service>.<algorithm_or_type>
<attribute_name>:<attribute_value>

The cryptographic service name must not contain any dots. There
must be one or more space characters between the

<algorithm_or_type>

and the

<attribute_name>

.

A provider satisfies this selection criterion iff the
provider implements the specified algorithm or type for the specified
cryptographic service and its implementation meets the
constraint expressed by the specified attribute name/value pair.

For example, "Signature.SHA1withDSA KeySize:1024" would be
satisfied by any provider that implemented
the SHA1withDSA signature algorithm with a keysize of 1024 (or larger).

See the

Java Security Standard Algorithm Names Specification

for information about standard cryptographic service names, standard
algorithm names and standard attribute names.

<crypto_service>.<algorithm_or_type>

The cryptographic service name must not contain any dots.

A
provider satisfies the specified selection criterion iff the provider
implements the
specified algorithm or type for the specified cryptographic service.

For example, "CertificateFactory.X.509"
would be satisfied by any provider that supplied
a CertificateFactory implementation for X.509 certificates.

<crypto_service>.<algorithm_or_type>
<attribute_name>:<attribute_value>

The cryptographic service name must not contain any dots. There
must be one or more space characters between the

<algorithm_or_type>

and the

<attribute_name>

.

A provider satisfies this selection criterion iff the
provider implements the specified algorithm or type for the specified
cryptographic service and its implementation meets the
constraint expressed by the specified attribute name/value pair.

For example, "Signature.SHA1withDSA KeySize:1024" would be
satisfied by any provider that implemented
the SHA1withDSA signature algorithm with a keysize of 1024 (or larger).

The cryptographic service name must not contain any dots.

A
provider satisfies the specified selection criterion iff the provider
implements the
specified algorithm or type for the specified cryptographic service.

For example, "CertificateFactory.X.509"
would be satisfied by any provider that supplied
a CertificateFactory implementation for X.509 certificates.

<crypto_service>.<algorithm_or_type>
<attribute_name>:<attribute_value>

The cryptographic service name must not contain any dots. There
must be one or more space characters between the

<algorithm_or_type>

and the

<attribute_name>

.

A provider satisfies this selection criterion iff the
provider implements the specified algorithm or type for the specified
cryptographic service and its implementation meets the
constraint expressed by the specified attribute name/value pair.

For example, "Signature.SHA1withDSA KeySize:1024" would be
satisfied by any provider that implemented
the SHA1withDSA signature algorithm with a keysize of 1024 (or larger).

A
provider satisfies the specified selection criterion iff the provider
implements the
specified algorithm or type for the specified cryptographic service.

For example, "CertificateFactory.X.509"
would be satisfied by any provider that supplied
a CertificateFactory implementation for X.509 certificates.

<crypto_service>.<algorithm_or_type>
<attribute_name>:<attribute_value>

The cryptographic service name must not contain any dots. There
must be one or more space characters between the

<algorithm_or_type>

and the

<attribute_name>

.

A provider satisfies this selection criterion iff the
provider implements the specified algorithm or type for the specified
cryptographic service and its implementation meets the
constraint expressed by the specified attribute name/value pair.

For example, "Signature.SHA1withDSA KeySize:1024" would be
satisfied by any provider that implemented
the SHA1withDSA signature algorithm with a keysize of 1024 (or larger).

For example, "CertificateFactory.X.509"
would be satisfied by any provider that supplied
a CertificateFactory implementation for X.509 certificates.

<crypto_service>.<algorithm_or_type>
<attribute_name>:<attribute_value>

The cryptographic service name must not contain any dots. There
must be one or more space characters between the

<algorithm_or_type>

and the

<attribute_name>

.

A provider satisfies this selection criterion iff the
provider implements the specified algorithm or type for the specified
cryptographic service and its implementation meets the
constraint expressed by the specified attribute name/value pair.

For example, "Signature.SHA1withDSA KeySize:1024" would be
satisfied by any provider that implemented
the SHA1withDSA signature algorithm with a keysize of 1024 (or larger).

The cryptographic service name must not contain any dots. There
must be one or more space characters between the

<algorithm_or_type>

and the

<attribute_name>

.

A provider satisfies this selection criterion iff the
provider implements the specified algorithm or type for the specified
cryptographic service and its implementation meets the
constraint expressed by the specified attribute name/value pair.

For example, "Signature.SHA1withDSA KeySize:1024" would be
satisfied by any provider that implemented
the SHA1withDSA signature algorithm with a keysize of 1024 (or larger).

A provider satisfies this selection criterion iff the
provider implements the specified algorithm or type for the specified
cryptographic service and its implementation meets the
constraint expressed by the specified attribute name/value pair.

For example, "Signature.SHA1withDSA KeySize:1024" would be
satisfied by any provider that implemented
the SHA1withDSA signature algorithm with a keysize of 1024 (or larger).

For example, "Signature.SHA1withDSA KeySize:1024" would be
satisfied by any provider that implemented
the SHA1withDSA signature algorithm with a keysize of 1024 (or larger).

See the

Java Security Standard Algorithm Names Specification

for information about standard cryptographic service names, standard
algorithm names and standard attribute names.

getProviders

```java
public static
Provider
[] getProviders​(
Map
<
String
,​
String
> filter)
```

Returns an array containing all installed providers that satisfy the
specified selection criteria, or null if no such providers have been
installed. The returned providers are ordered
according to their

preference order

.

The selection criteria are represented by a map.
Each map entry represents a selection criterion.
A provider is selected iff it satisfies all selection
criteria. The key for any entry in such a map must be in one of the
following two formats:

- <crypto_service>.<algorithm_or_type>

The cryptographic service name must not contain any dots.

The value associated with the key must be an empty string.

A provider
satisfies this selection criterion iff the provider implements the
specified algorithm or type for the specified cryptographic service.

<crypto_service>.
<algorithm_or_type> <attribute_name>

The cryptographic service name must not contain any dots. There
must be one or more space characters between the

<algorithm_or_type>

and the

<attribute_name>

.

The value associated with the key must be a non-empty string.
A provider satisfies this selection criterion iff the
provider implements the specified algorithm or type for the specified
cryptographic service and its implementation meets the
constraint expressed by the specified attribute name/value pair.

See the

Java Security Standard Algorithm Names Specification

for information about standard cryptographic service names, standard
algorithm names and standard attribute names.

**Parameters:** filter

- the criteria for selecting
providers. The filter is case-insensitive.
**Returns:** all the installed providers that satisfy the selection
criteria, or null if no such providers have been installed.
**Throws:** InvalidParameterException

- if the filter is not in the required format
**Throws:** NullPointerException

- if filter is null
**Since:** 1.3
**See Also:** getProviders(java.lang.String)

---

#### getProviders

public static

Provider

[] getProviders​(

Map

<

String

,​

String

> filter)

Returns an array containing all installed providers that satisfy the
specified selection criteria, or null if no such providers have been
installed. The returned providers are ordered
according to their

preference order

.

The selection criteria are represented by a map.
Each map entry represents a selection criterion.
A provider is selected iff it satisfies all selection
criteria. The key for any entry in such a map must be in one of the
following two formats:

- <crypto_service>.<algorithm_or_type>

The cryptographic service name must not contain any dots.

The value associated with the key must be an empty string.

A provider
satisfies this selection criterion iff the provider implements the
specified algorithm or type for the specified cryptographic service.

<crypto_service>.
<algorithm_or_type> <attribute_name>

The cryptographic service name must not contain any dots. There
must be one or more space characters between the

<algorithm_or_type>

and the

<attribute_name>

.

The value associated with the key must be a non-empty string.
A provider satisfies this selection criterion iff the
provider implements the specified algorithm or type for the specified
cryptographic service and its implementation meets the
constraint expressed by the specified attribute name/value pair.

See the

Java Security Standard Algorithm Names Specification

for information about standard cryptographic service names, standard
algorithm names and standard attribute names.

The selection criteria are represented by a map.
Each map entry represents a selection criterion.
A provider is selected iff it satisfies all selection
criteria. The key for any entry in such a map must be in one of the
following two formats:

- <crypto_service>.<algorithm_or_type>

The cryptographic service name must not contain any dots.

The value associated with the key must be an empty string.

A provider
satisfies this selection criterion iff the provider implements the
specified algorithm or type for the specified cryptographic service.

<crypto_service>.
<algorithm_or_type> <attribute_name>

The cryptographic service name must not contain any dots. There
must be one or more space characters between the

<algorithm_or_type>

and the

<attribute_name>

.

The value associated with the key must be a non-empty string.
A provider satisfies this selection criterion iff the
provider implements the specified algorithm or type for the specified
cryptographic service and its implementation meets the
constraint expressed by the specified attribute name/value pair.

See the

Java Security Standard Algorithm Names Specification

for information about standard cryptographic service names, standard
algorithm names and standard attribute names.

<crypto_service>.<algorithm_or_type>

The cryptographic service name must not contain any dots.

The value associated with the key must be an empty string.

A provider
satisfies this selection criterion iff the provider implements the
specified algorithm or type for the specified cryptographic service.

<crypto_service>.
<algorithm_or_type> <attribute_name>

The cryptographic service name must not contain any dots. There
must be one or more space characters between the

<algorithm_or_type>

and the

<attribute_name>

.

The value associated with the key must be a non-empty string.
A provider satisfies this selection criterion iff the
provider implements the specified algorithm or type for the specified
cryptographic service and its implementation meets the
constraint expressed by the specified attribute name/value pair.

The cryptographic service name must not contain any dots.

The value associated with the key must be an empty string.

A provider
satisfies this selection criterion iff the provider implements the
specified algorithm or type for the specified cryptographic service.

<crypto_service>.
<algorithm_or_type> <attribute_name>

The cryptographic service name must not contain any dots. There
must be one or more space characters between the

<algorithm_or_type>

and the

<attribute_name>

.

The value associated with the key must be a non-empty string.
A provider satisfies this selection criterion iff the
provider implements the specified algorithm or type for the specified
cryptographic service and its implementation meets the
constraint expressed by the specified attribute name/value pair.

The value associated with the key must be an empty string.

A provider
satisfies this selection criterion iff the provider implements the
specified algorithm or type for the specified cryptographic service.

<crypto_service>.
<algorithm_or_type> <attribute_name>

The cryptographic service name must not contain any dots. There
must be one or more space characters between the

<algorithm_or_type>

and the

<attribute_name>

.

The value associated with the key must be a non-empty string.
A provider satisfies this selection criterion iff the
provider implements the specified algorithm or type for the specified
cryptographic service and its implementation meets the
constraint expressed by the specified attribute name/value pair.

A provider
satisfies this selection criterion iff the provider implements the
specified algorithm or type for the specified cryptographic service.

<crypto_service>.
<algorithm_or_type> <attribute_name>

The cryptographic service name must not contain any dots. There
must be one or more space characters between the

<algorithm_or_type>

and the

<attribute_name>

.

The value associated with the key must be a non-empty string.
A provider satisfies this selection criterion iff the
provider implements the specified algorithm or type for the specified
cryptographic service and its implementation meets the
constraint expressed by the specified attribute name/value pair.

The cryptographic service name must not contain any dots. There
must be one or more space characters between the

<algorithm_or_type>

and the

<attribute_name>

.

The value associated with the key must be a non-empty string.
A provider satisfies this selection criterion iff the
provider implements the specified algorithm or type for the specified
cryptographic service and its implementation meets the
constraint expressed by the specified attribute name/value pair.

The value associated with the key must be a non-empty string.
A provider satisfies this selection criterion iff the
provider implements the specified algorithm or type for the specified
cryptographic service and its implementation meets the
constraint expressed by the specified attribute name/value pair.

See the

Java Security Standard Algorithm Names Specification

for information about standard cryptographic service names, standard
algorithm names and standard attribute names.

getProperty

```java
public static
String
getProperty​(
String
key)
```

Gets a security property value.

First, if there is a security manager, its

checkPermission

method is called with a

java.security.SecurityPermission("getProperty."+key)

permission to see if it's ok to retrieve the specified
security property value..

**Parameters:** key

- the key of the property being retrieved.
**Returns:** the value of the security property corresponding to key.
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkPermission(java.security.Permission)

method
denies
access to retrieve the specified security property value
**Throws:** NullPointerException

- is key is null
**See Also:** setProperty(java.lang.String, java.lang.String)

,

SecurityPermission

---

#### getProperty

public static

String

getProperty​(

String

key)

Gets a security property value.

First, if there is a security manager, its

checkPermission

method is called with a

java.security.SecurityPermission("getProperty."+key)

permission to see if it's ok to retrieve the specified
security property value..

First, if there is a security manager, its

checkPermission

method is called with a

java.security.SecurityPermission("getProperty."+key)

permission to see if it's ok to retrieve the specified
security property value..

setProperty

```java
public static void setProperty​(
String
key,

String
datum)
```

Sets a security property value.

First, if there is a security manager, its

checkPermission

method is called with a

java.security.SecurityPermission("setProperty."+key)

permission to see if it's ok to set the specified
security property value.

**Parameters:** key

- the name of the property to be set.
**Parameters:** datum

- the value of the property to be set.
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkPermission(java.security.Permission)

method
denies access to set the specified security property value
**Throws:** NullPointerException

- if key or datum is null
**See Also:** getProperty(java.lang.String)

,

SecurityPermission

---

#### setProperty

public static void setProperty​(

String

key,

String

datum)

Sets a security property value.

First, if there is a security manager, its

checkPermission

method is called with a

java.security.SecurityPermission("setProperty."+key)

permission to see if it's ok to set the specified
security property value.

First, if there is a security manager, its

checkPermission

method is called with a

java.security.SecurityPermission("setProperty."+key)

permission to see if it's ok to set the specified
security property value.

getAlgorithms

```java
public static
Set
<
String
> getAlgorithms​(
String
serviceName)
```

Returns a Set of Strings containing the names of all available
algorithms or types for the specified Java cryptographic service
(e.g., Signature, MessageDigest, Cipher, Mac, KeyStore). Returns
an empty Set if there is no provider that supports the
specified service or if serviceName is null. For a complete list
of Java cryptographic services, please see the

Java Cryptography Architecture (JCA) Reference Guide

.
Note: the returned set is immutable.

**Parameters:** serviceName

- the name of the Java cryptographic
service (e.g., Signature, MessageDigest, Cipher, Mac, KeyStore).
Note: this parameter is case-insensitive.
**Returns:** a Set of Strings containing the names of all available
algorithms or types for the specified Java cryptographic service
or an empty set if no provider supports the specified service.
**Since:** 1.4

---

#### getAlgorithms

public static

Set

<

String

> getAlgorithms​(

String

serviceName)

Returns a Set of Strings containing the names of all available
algorithms or types for the specified Java cryptographic service
(e.g., Signature, MessageDigest, Cipher, Mac, KeyStore). Returns
an empty Set if there is no provider that supports the
specified service or if serviceName is null. For a complete list
of Java cryptographic services, please see the

Java Cryptography Architecture (JCA) Reference Guide

.
Note: the returned set is immutable.

---

