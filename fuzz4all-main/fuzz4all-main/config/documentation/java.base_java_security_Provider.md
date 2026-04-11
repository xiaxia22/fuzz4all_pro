# Class Provider

**Source:** `java.base\java\security\Provider.html`

### Class Description

```java
public abstract class
Provider

extends
Properties
```

This class represents a "provider" for the
Java Security API, where a provider implements some or all parts of
Java Security. Services that a provider may implement include:

- Algorithms (such as DSA, RSA, or SHA-256).

Key generation, conversion, and management facilities (such as for
algorithm-specific keys).

Some provider implementations may encounter unrecoverable internal
errors during their operation, for example a failure to communicate with a
security token. A

ProviderException

should be used to indicate
such errors.

Please note that a provider can be used to implement any security
service in Java that uses a pluggable architecture with a choice
of implementations that fit underneath.

The service type

Provider

is reserved for use by the
security framework. Services of this type cannot be added, removed,
or modified by applications.
The following attributes are automatically placed in each Provider object:

Attributes Automatically Placed in a Provider Object

Name

Value

Provider.id name

String.valueOf(provider.getName())

Provider.id version

String.valueOf(provider.getVersionStr())

Provider.id info

String.valueOf(provider.getInfo())

Provider.id className

provider.getClass().getName()

Each provider has a name and a version string. A provider normally
identifies itself with a file named

java.security.Provider

in the resource directory

META-INF/services

.
Security providers are looked up via the

ServiceLoader

mechanism
using the

application class loader

.

Providers may be configured such that they are automatically
installed and made available at runtime via the

Security.getProviders()

method.
The mechanism for configuring and installing security providers is
implementation-specific.

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Map

<

Object

,​

Object

>

---

### Field Details

*No entries found.*

### Constructor Details

#### @Deprecated
(
since
="9")
protected Provider​(
String
name,
double version,

String
info)

Constructs a provider with the specified name, version number,
and information. Calling this constructor is equivalent to call the

Provider(String, String, String)

with

name

name,

Double.toString(version)

, and

info

.

**Parameters:**
- name

- the provider name.
- version

- the provider version number.
- info

- a description of the provider and its services.

---

#### protected Provider​(
String
name,

String
versionStr,

String
info)

Constructs a provider with the specified name, version string,
and information.

The version string contains a version number optionally followed
by other information separated by one of the characters of '+', '-'.

The format for the version number is:

```java
^[0-9]+(\.[0-9]+)*
```

In order to return the version number in a double, when there are
more than two components (separated by '.' as defined above), only
the first two components are retained. The resulting string is then
passed to

Double.valueOf(String)

to generate version number,
i.e.

getVersion()

.

If the conversion failed, value 0 will be used.

**Parameters:**
- name

- the provider name.
- versionStr

- the provider version string.
- info

- a description of the provider and its services.

**Since:**
- 9

---

### Method Details

#### public
Provider
configure​(
String
configArg)

Apply the supplied configuration argument to this provider instance
and return the configured provider. Note that if this provider cannot
be configured in-place, a new provider will be created and returned.
Therefore, callers should always use the returned provider.

**Parameters:**
- configArg

- the configuration information for configuring this
provider.

**Returns:**
- a provider configured with the supplied configuration argument.

**Throws:**
- UnsupportedOperationException

- if a configuration argument is
not supported.
- NullPointerException

- if the supplied configuration argument is
null.
- InvalidParameterException

- if the supplied configuration argument
is invalid.

**Since:**
- 9

**Implementation Requirements:**
- The default implementation throws

UnsupportedOperationException

.
Subclasses should override this method only if a configuration argument
is supported.

---

#### public boolean isConfigured()

Check if this provider instance has been configured.

**Returns:**
- true if no further configuration is needed, false otherwise.

**Since:**
- 9

**Implementation Requirements:**
- The default implementation returns true.
Subclasses should override this method if the provider instance requires
an explicit

configure

call after being constructed.

---

#### public
String
getName()

Returns the name of this provider.

**Returns:**
- the name of this provider.

---

#### @Deprecated
(
since
="9")
public double getVersion()

Returns the version number for this provider.

**Returns:**
- the version number for this provider.

---

#### public
String
getVersionStr()

Returns the version string for this provider.

**Returns:**
- the version string for this provider.

**Since:**
- 9

---

#### public
String
getInfo()

Returns a human-readable description of the provider and its
services. This may return an HTML page, with relevant links.

**Returns:**
- a description of the provider and its services.

---

#### public
String
toString()

Returns a string with the name and the version string
of this provider.

**Overrides:**
- toString

in class

Hashtable

<

Object

,​

Object

>

**Returns:**
- the string with the name and the version string
for this provider.

---

#### public void clear()

Clears this provider so that it no longer contains the properties
used to look up facilities implemented by the provider.

If a security manager is enabled, its

checkSecurityAccess

method is called with the string

"clearProviderProperties."+name

(where

name

is the provider name) to see if it's ok to clear
this provider.

**Specified by:**
- clear

in interface

Map

<

Object

,​

Object

>

**Overrides:**
- clear

in class

Hashtable

<

Object

,​

Object

>

**Throws:**
- SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to clear this provider

**Since:**
- 1.2

---

#### public void load​(
InputStream
inStream)
throws
IOException

Reads a property list (key and element pairs) from the input stream.

**Overrides:**
- load

in class

Properties

**Parameters:**
- inStream

- the input stream.

**Throws:**
- IOException

- if an error occurred when reading from the
input stream.

**See Also:**
- Properties.load(java.io.Reader)

---

#### public void putAll​(
Map
<?,​?> t)

Copies all of the mappings from the specified Map to this provider.
These mappings will replace any properties that this provider had
for any of the keys currently in the specified Map.

**Specified by:**
- putAll

in interface

Map

<

Object

,​

Object

>

**Overrides:**
- putAll

in class

Hashtable

<

Object

,​

Object

>

**Parameters:**
- t

- mappings to be stored in this map

**Since:**
- 1.2

---

#### public
Set
<
Map.Entry
<
Object
,​
Object
>> entrySet()

Returns an unmodifiable Set view of the property entries contained
in this Provider.

**Specified by:**
- entrySet

in interface

Map

<

Object

,​

Object

>

**Overrides:**
- entrySet

in class

Hashtable

<

Object

,​

Object

>

**Returns:**
- a set view of the mappings contained in this map

**See Also:**
- Map.Entry

**Since:**
- 1.2

---

#### public
Set
<
Object
> keySet()

Returns an unmodifiable Set view of the property keys contained in
this provider.

**Specified by:**
- keySet

in interface

Map

<

Object

,​

Object

>

**Overrides:**
- keySet

in class

Hashtable

<

Object

,​

Object

>

**Returns:**
- a set view of the keys contained in this map

**Since:**
- 1.2

---

#### public
Collection
<
Object
> values()

Returns an unmodifiable Collection view of the property values
contained in this provider.

**Specified by:**
- values

in interface

Map

<

Object

,​

Object

>

**Overrides:**
- values

in class

Hashtable

<

Object

,​

Object

>

**Returns:**
- a collection view of the values contained in this map

**Since:**
- 1.2

---

#### public
Object
put​(
Object
key,

Object
value)

Sets the

key

property to have the specified

value

.

If a security manager is enabled, its

checkSecurityAccess

method is called with the string

"putProviderProperty."+name

,
where

name

is the provider name, to see if it's ok to set this
provider's property values.

**Specified by:**
- put

in interface

Map

<

Object

,​

Object

>

**Overrides:**
- put

in class

Hashtable

<

Object

,​

Object

>

**Parameters:**
- key

- the hashtable key
- value

- the value

**Returns:**
- the previous value of the specified key in this hashtable,
or

null

if it did not have one

**Throws:**
- SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to set property values.

**See Also:**
- Object.equals(Object)

,

Hashtable.get(Object)

**Since:**
- 1.2

---

#### public
Object
putIfAbsent​(
Object
key,

Object
value)

If the specified key is not already associated with a value (or is mapped
to

null

) associates it with the given value and returns

null

, else returns the current value.

If a security manager is enabled, its

checkSecurityAccess

method is called with the string

"putProviderProperty."+name

,
where

name

is the provider name, to see if it's ok to set this
provider's property values.

**Parameters:**
- key

- key with which the specified value is to be associated
- value

- value to be associated with the specified key

**Returns:**
- the previous value associated with the specified key, or

null

if there was no mapping for the key.
(A

null

return can also indicate that the map
previously associated

null

with the key,
if the implementation supports null values.)

**Throws:**
- SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to set property values.

**Since:**
- 1.8

---

#### public
Object
remove​(
Object
key)

Removes the

key

property (and its corresponding

value

).

If a security manager is enabled, its

checkSecurityAccess

method is called with the string

"removeProviderProperty."+name

,
where

name

is the provider name, to see if it's ok to remove this
provider's properties.

**Specified by:**
- remove

in interface

Map

<

Object

,​

Object

>

**Overrides:**
- remove

in class

Hashtable

<

Object

,​

Object

>

**Parameters:**
- key

- the key that needs to be removed

**Returns:**
- the value to which the key had been mapped in this hashtable,
or

null

if the key did not have a mapping

**Throws:**
- SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to remove this provider's properties.

**Since:**
- 1.2

---

#### public boolean remove​(
Object
key,

Object
value)

Removes the entry for the specified key only if it is currently
mapped to the specified value.

If a security manager is enabled, its

checkSecurityAccess

method is called with the string

"removeProviderProperty."+name

,
where

name

is the provider name, to see if it's ok to remove this
provider's properties.

**Parameters:**
- key

- key with which the specified value is associated
- value

- value expected to be associated with the specified key

**Returns:**
- true

if the value was removed

**Throws:**
- SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to remove this provider's properties.

**Since:**
- 1.8

---

#### public boolean replace​(
Object
key,

Object
oldValue,

Object
newValue)

Replaces the entry for the specified key only if currently
mapped to the specified value.

If a security manager is enabled, its

checkSecurityAccess

method is called with the string

"putProviderProperty."+name

,
where

name

is the provider name, to see if it's ok to set this
provider's property values.

**Parameters:**
- key

- key with which the specified value is associated
- oldValue

- value expected to be associated with the specified key
- newValue

- value to be associated with the specified key

**Returns:**
- true

if the value was replaced

**Throws:**
- SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to set property values.

**Since:**
- 1.8

---

#### public
Object
replace​(
Object
key,

Object
value)

Replaces the entry for the specified key only if it is
currently mapped to some value.

If a security manager is enabled, its

checkSecurityAccess

method is called with the string

"putProviderProperty."+name

,
where

name

is the provider name, to see if it's ok to set this
provider's property values.

**Parameters:**
- key

- key with which the specified value is associated
- value

- value to be associated with the specified key

**Returns:**
- the previous value associated with the specified key, or

null

if there was no mapping for the key.
(A

null

return can also indicate that the map
previously associated

null

with the key,
if the implementation supports null values.)

**Throws:**
- SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to set property values.

**Since:**
- 1.8

---

#### public void replaceAll​(
BiFunction
<? super
Object
,​? super
Object
,​? extends
Object
> function)

Replaces each entry's value with the result of invoking the given
function on that entry, in the order entries are returned by an entry
set iterator, until all entries have been processed or the function
throws an exception.

If a security manager is enabled, its

checkSecurityAccess

method is called with the string

"putProviderProperty."+name

,
where

name

is the provider name, to see if it's ok to set this
provider's property values.

**Parameters:**
- function

- the function to apply to each entry

**Throws:**
- SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to set property values.

**Since:**
- 1.8

---

#### public
Object
compute​(
Object
key,

BiFunction
<? super
Object
,​? super
Object
,​? extends
Object
> remappingFunction)

Attempts to compute a mapping for the specified key and its
current mapped value (or

null

if there is no current
mapping).

If a security manager is enabled, its

checkSecurityAccess

method is called with the strings

"putProviderProperty."+name

and

"removeProviderProperty."+name

, where

name

is the
provider name, to see if it's ok to set this provider's property values
and remove this provider's properties.

**Specified by:**
- compute

in interface

Map

<

Object

,​

Object

>

**Overrides:**
- compute

in class

Hashtable

<

Object

,​

Object

>

**Parameters:**
- key

- key with which the specified value is to be associated
- remappingFunction

- the remapping function to compute a value

**Returns:**
- the new value associated with the specified key, or null if none

**Throws:**
- SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to set property values or remove properties.

**Since:**
- 1.8

---

#### public
Object
computeIfAbsent​(
Object
key,

Function
<? super
Object
,​? extends
Object
> mappingFunction)

If the specified key is not already associated with a value (or
is mapped to

null

), attempts to compute its value using
the given mapping function and enters it into this map unless

null

.

If a security manager is enabled, its

checkSecurityAccess

method is called with the strings

"putProviderProperty."+name

and

"removeProviderProperty."+name

, where

name

is the
provider name, to see if it's ok to set this provider's property values
and remove this provider's properties.

**Specified by:**
- computeIfAbsent

in interface

Map

<

Object

,​

Object

>

**Overrides:**
- computeIfAbsent

in class

Hashtable

<

Object

,​

Object

>

**Parameters:**
- key

- key with which the specified value is to be associated
- mappingFunction

- the mapping function to compute a value

**Returns:**
- the current (existing or computed) value associated with
the specified key, or null if the computed value is null

**Throws:**
- SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to set property values and remove properties.

**Since:**
- 1.8

---

#### public
Object
computeIfPresent​(
Object
key,

BiFunction
<? super
Object
,​? super
Object
,​? extends
Object
> remappingFunction)

If the value for the specified key is present and non-null, attempts to
compute a new mapping given the key and its current mapped value.

If a security manager is enabled, its

checkSecurityAccess

method is called with the strings

"putProviderProperty."+name

and

"removeProviderProperty."+name

, where

name

is the
provider name, to see if it's ok to set this provider's property values
and remove this provider's properties.

**Specified by:**
- computeIfPresent

in interface

Map

<

Object

,​

Object

>

**Overrides:**
- computeIfPresent

in class

Hashtable

<

Object

,​

Object

>

**Parameters:**
- key

- key with which the specified value is to be associated
- remappingFunction

- the remapping function to compute a value

**Returns:**
- the new value associated with the specified key, or null if none

**Throws:**
- SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to set property values or remove properties.

**Since:**
- 1.8

---

#### public
Object
merge​(
Object
key,

Object
value,

BiFunction
<? super
Object
,​? super
Object
,​? extends
Object
> remappingFunction)

If the specified key is not already associated with a value or is
associated with null, associates it with the given value. Otherwise,
replaces the value with the results of the given remapping function,
or removes if the result is null. This method may be of use when
combining multiple mapped values for a key.

If a security manager is enabled, its

checkSecurityAccess

method is called with the strings

"putProviderProperty."+name

and

"removeProviderProperty."+name

, where

name

is the
provider name, to see if it's ok to set this provider's property values
and remove this provider's properties.

**Specified by:**
- merge

in interface

Map

<

Object

,​

Object

>

**Overrides:**
- merge

in class

Hashtable

<

Object

,​

Object

>

**Parameters:**
- key

- key with which the resulting value is to be associated
- value

- the non-null value to be merged with the existing value
associated with the key or, if no existing value or a null value
is associated with the key, to be associated with the key
- remappingFunction

- the remapping function to recompute a value if
present

**Returns:**
- the new value associated with the specified key, or null if no
value is associated with the key

**Throws:**
- SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to set property values or remove properties.

**Since:**
- 1.8

---

#### public
Object
getOrDefault​(
Object
key,

Object
defaultValue)

Description copied from interface:

Map

**Parameters:**
- key

- the key whose associated value is to be returned
- defaultValue

- the default mapping of the key

**Returns:**
- the value to which the specified key is mapped, or

defaultValue

if this map contains no mapping for the key

**Since:**
- 1.8

---

#### public void forEach​(
BiConsumer
<? super
Object
,​? super
Object
> action)

Description copied from interface:

Map

**Parameters:**
- action

- The action to be performed for each entry

**Since:**
- 1.8

---

#### public
Provider.Service
getService​(
String
type,

String
algorithm)

Get the service describing this Provider's implementation of the
specified type of this algorithm or alias. If no such
implementation exists, this method returns null. If there are two
matching services, one added to this provider using

putService()

and one added via

put()

,
the service added via

putService()

is returned.

**Parameters:**
- type

- the type of

service

requested
(for example,

MessageDigest

)
- algorithm

- the case insensitive algorithm name (or alternate
alias) of the service requested (for example,

SHA-1

)

**Returns:**
- the service describing this Provider's matching service
or null if no such service exists

**Throws:**
- NullPointerException

- if type or algorithm is null

**Since:**
- 1.5

---

#### public
Set
<
Provider.Service
> getServices()

Get an unmodifiable Set of all services supported by
this Provider.

**Returns:**
- an unmodifiable Set of all services supported by
this Provider

**Since:**
- 1.5

---

#### protected void putService​(
Provider.Service
s)

Add a service. If a service of the same type with the same algorithm
name exists and it was added using

putService()

,
it is replaced by the new service.
This method also places information about this service
in the provider's Hashtable values in the format described in the

Java Cryptography Architecture (JCA) Reference Guide

.

Also, if there is a security manager, its

checkSecurityAccess

method is called with the string

"putProviderProperty."+name

, where

name

is
the provider name, to see if it's ok to set this provider's property
values. If the default implementation of

checkSecurityAccess

is used (that is, that method is not overriden), then this results in
a call to the security manager's

checkPermission

method with
a

SecurityPermission("putProviderProperty."+name)

permission.

**Parameters:**
- s

- the Service to add

**Throws:**
- SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method denies
access to set property values.
- NullPointerException

- if s is null

**Since:**
- 1.5

---

#### protected void removeService​(
Provider.Service
s)

Remove a service previously added using

putService()

. The specified service is removed from
this provider. It will no longer be returned by

getService()

and its information will be removed
from this provider's Hashtable.

Also, if there is a security manager, its

checkSecurityAccess

method is called with the string

"removeProviderProperty."+name

, where

name

is
the provider name, to see if it's ok to remove this provider's
properties. If the default implementation of

checkSecurityAccess

is used (that is, that method is not
overriden), then this results in a call to the security manager's

checkPermission

method with a

SecurityPermission("removeProviderProperty."+name)

permission.

**Parameters:**
- s

- the Service to be removed

**Throws:**
- SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method denies
access to remove this provider's properties.
- NullPointerException

- if s is null

**Since:**
- 1.5

---

### Additional Sections

#### Class Provider

java.lang.Object

- java.util.Dictionary

<K,​V>
- - java.util.Hashtable

<

Object

,​

Object

>
- - java.util.Properties
- - java.security.Provider

java.util.Dictionary

<K,​V>

- java.util.Hashtable

<

Object

,​

Object

>
- - java.util.Properties
- - java.security.Provider

java.util.Hashtable

<

Object

,​

Object

>

- java.util.Properties
- - java.security.Provider

java.util.Properties

- java.security.Provider

java.security.Provider

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Map

<

Object

,​

Object

>

**Direct Known Subclasses:** AuthProvider

```java
public abstract class
Provider

extends
Properties
```

This class represents a "provider" for the
Java Security API, where a provider implements some or all parts of
Java Security. Services that a provider may implement include:

- Algorithms (such as DSA, RSA, or SHA-256).

Key generation, conversion, and management facilities (such as for
algorithm-specific keys).

Some provider implementations may encounter unrecoverable internal
errors during their operation, for example a failure to communicate with a
security token. A

ProviderException

should be used to indicate
such errors.

Please note that a provider can be used to implement any security
service in Java that uses a pluggable architecture with a choice
of implementations that fit underneath.

The service type

Provider

is reserved for use by the
security framework. Services of this type cannot be added, removed,
or modified by applications.
The following attributes are automatically placed in each Provider object:

Attributes Automatically Placed in a Provider Object

Name

Value

Provider.id name

String.valueOf(provider.getName())

Provider.id version

String.valueOf(provider.getVersionStr())

Provider.id info

String.valueOf(provider.getInfo())

Provider.id className

provider.getClass().getName()

Each provider has a name and a version string. A provider normally
identifies itself with a file named

java.security.Provider

in the resource directory

META-INF/services

.
Security providers are looked up via the

ServiceLoader

mechanism
using the

application class loader

.

Providers may be configured such that they are automatically
installed and made available at runtime via the

Security.getProviders()

method.
The mechanism for configuring and installing security providers is
implementation-specific.

**Implementation Note:** The JDK implementation supports static registration of the security
providers via the

conf/security/java.security

file in the Java
installation directory. These providers are automatically installed by
the JDK runtime, see

The Provider Class

in the Java Cryptography Architecture (JCA) Reference Guide
for information about how a particular type of provider, the cryptographic
service provider, works and is installed.
**Since:** 1.1
**See Also:** Serialized Form

public abstract class

Provider

extends

Properties

This class represents a "provider" for the
Java Security API, where a provider implements some or all parts of
Java Security. Services that a provider may implement include:

- Algorithms (such as DSA, RSA, or SHA-256).

Key generation, conversion, and management facilities (such as for
algorithm-specific keys).

Some provider implementations may encounter unrecoverable internal
errors during their operation, for example a failure to communicate with a
security token. A

ProviderException

should be used to indicate
such errors.

Please note that a provider can be used to implement any security
service in Java that uses a pluggable architecture with a choice
of implementations that fit underneath.

The service type

Provider

is reserved for use by the
security framework. Services of this type cannot be added, removed,
or modified by applications.
The following attributes are automatically placed in each Provider object:

Attributes Automatically Placed in a Provider Object

Name

Value

Provider.id name

String.valueOf(provider.getName())

Provider.id version

String.valueOf(provider.getVersionStr())

Provider.id info

String.valueOf(provider.getInfo())

Provider.id className

provider.getClass().getName()

Each provider has a name and a version string. A provider normally
identifies itself with a file named

java.security.Provider

in the resource directory

META-INF/services

.
Security providers are looked up via the

ServiceLoader

mechanism
using the

application class loader

.

Providers may be configured such that they are automatically
installed and made available at runtime via the

Security.getProviders()

method.
The mechanism for configuring and installing security providers is
implementation-specific.

Algorithms (such as DSA, RSA, or SHA-256).

Key generation, conversion, and management facilities (such as for
algorithm-specific keys).

Some provider implementations may encounter unrecoverable internal
errors during their operation, for example a failure to communicate with a
security token. A

ProviderException

should be used to indicate
such errors.

Please note that a provider can be used to implement any security
service in Java that uses a pluggable architecture with a choice
of implementations that fit underneath.

The service type

Provider

is reserved for use by the
security framework. Services of this type cannot be added, removed,
or modified by applications.
The following attributes are automatically placed in each Provider object:

Attributes Automatically Placed in a Provider Object

Name

Value

Provider.id name

String.valueOf(provider.getName())

Provider.id version

String.valueOf(provider.getVersionStr())

Provider.id info

String.valueOf(provider.getInfo())

Provider.id className

provider.getClass().getName()

Each provider has a name and a version string. A provider normally
identifies itself with a file named

java.security.Provider

in the resource directory

META-INF/services

.
Security providers are looked up via the

ServiceLoader

mechanism
using the

application class loader

.

Providers may be configured such that they are automatically
installed and made available at runtime via the

Security.getProviders()

method.
The mechanism for configuring and installing security providers is
implementation-specific.

Please note that a provider can be used to implement any security
service in Java that uses a pluggable architecture with a choice
of implementations that fit underneath.

The service type

Provider

is reserved for use by the
security framework. Services of this type cannot be added, removed,
or modified by applications.
The following attributes are automatically placed in each Provider object:

Attributes Automatically Placed in a Provider Object

Name

Value

Provider.id name

String.valueOf(provider.getName())

Provider.id version

String.valueOf(provider.getVersionStr())

Provider.id info

String.valueOf(provider.getInfo())

Provider.id className

provider.getClass().getName()

Each provider has a name and a version string. A provider normally
identifies itself with a file named

java.security.Provider

in the resource directory

META-INF/services

.
Security providers are looked up via the

ServiceLoader

mechanism
using the

application class loader

.

Providers may be configured such that they are automatically
installed and made available at runtime via the

Security.getProviders()

method.
The mechanism for configuring and installing security providers is
implementation-specific.

The service type

Provider

is reserved for use by the
security framework. Services of this type cannot be added, removed,
or modified by applications.
The following attributes are automatically placed in each Provider object:

Attributes Automatically Placed in a Provider Object

Name

Value

Provider.id name

String.valueOf(provider.getName())

Provider.id version

String.valueOf(provider.getVersionStr())

Provider.id info

String.valueOf(provider.getInfo())

Provider.id className

provider.getClass().getName()

Each provider has a name and a version string. A provider normally
identifies itself with a file named

java.security.Provider

in the resource directory

META-INF/services

.
Security providers are looked up via the

ServiceLoader

mechanism
using the

application class loader

.

Providers may be configured such that they are automatically
installed and made available at runtime via the

Security.getProviders()

method.
The mechanism for configuring and installing security providers is
implementation-specific.

Each provider has a name and a version string. A provider normally
identifies itself with a file named

java.security.Provider

in the resource directory

META-INF/services

.
Security providers are looked up via the

ServiceLoader

mechanism
using the

application class loader

.

Providers may be configured such that they are automatically
installed and made available at runtime via the

Security.getProviders()

method.
The mechanism for configuring and installing security providers is
implementation-specific.

Providers may be configured such that they are automatically
installed and made available at runtime via the

Security.getProviders()

method.
The mechanism for configuring and installing security providers is
implementation-specific.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

Provider.Service

The description of a security service.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.util.

Properties

defaults

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Provider

​(

String

name,
double version,

String

info)

Deprecated.

use

Provider(String, String, String)

instead.

protected

Provider

​(

String

name,

String

versionStr,

String

info)

Constructs a provider with the specified name, version string,
and information.

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

clear

()

Clears this provider so that it no longer contains the properties
used to look up facilities implemented by the provider.

Object

compute

​(

Object

key,

BiFunction

<? super

Object

,​? super

Object

,​? extends

Object

> remappingFunction)

Attempts to compute a mapping for the specified key and its
current mapped value (or

null

if there is no current
mapping).

Object

computeIfAbsent

​(

Object

key,

Function

<? super

Object

,​? extends

Object

> mappingFunction)

If the specified key is not already associated with a value (or
is mapped to

null

), attempts to compute its value using
the given mapping function and enters it into this map unless

null

.

Object

computeIfPresent

​(

Object

key,

BiFunction

<? super

Object

,​? super

Object

,​? extends

Object

> remappingFunction)

If the value for the specified key is present and non-null, attempts to
compute a new mapping given the key and its current mapped value.

Provider

configure

​(

String

configArg)

Apply the supplied configuration argument to this provider instance
and return the configured provider.

Set

<

Map.Entry

<

Object

,​

Object

>>

entrySet

()

Returns an unmodifiable Set view of the property entries contained
in this Provider.

void

forEach

​(

BiConsumer

<? super

Object

,​? super

Object

> action)

Performs the given action for each entry in this map until all entries
have been processed or the action throws an exception.

String

getInfo

()

Returns a human-readable description of the provider and its
services.

String

getName

()

Returns the name of this provider.

Object

getOrDefault

​(

Object

key,

Object

defaultValue)

Returns the value to which the specified key is mapped, or

defaultValue

if this map contains no mapping for the key.

Provider.Service

getService

​(

String

type,

String

algorithm)

Get the service describing this Provider's implementation of the
specified type of this algorithm or alias.

Set

<

Provider.Service

>

getServices

()

Get an unmodifiable Set of all services supported by
this Provider.

double

getVersion

()

Deprecated.

use

getVersionStr()

instead.

String

getVersionStr

()

Returns the version string for this provider.

boolean

isConfigured

()

Check if this provider instance has been configured.

Set

<

Object

>

keySet

()

Returns an unmodifiable Set view of the property keys contained in
this provider.

void

load

​(

InputStream

inStream)

Reads a property list (key and element pairs) from the input stream.

Object

merge

​(

Object

key,

Object

value,

BiFunction

<? super

Object

,​? super

Object

,​? extends

Object

> remappingFunction)

If the specified key is not already associated with a value or is
associated with null, associates it with the given value.

Object

put

​(

Object

key,

Object

value)

Sets the

key

property to have the specified

value

.

void

putAll

​(

Map

<?,​?> t)

Copies all of the mappings from the specified Map to this provider.

Object

putIfAbsent

​(

Object

key,

Object

value)

If the specified key is not already associated with a value (or is mapped
to

null

) associates it with the given value and returns

null

, else returns the current value.

protected void

putService

​(

Provider.Service

s)

Add a service.

Object

remove

​(

Object

key)

Removes the

key

property (and its corresponding

value

).

boolean

remove

​(

Object

key,

Object

value)

Removes the entry for the specified key only if it is currently
mapped to the specified value.

protected void

removeService

​(

Provider.Service

s)

Remove a service previously added using

putService()

.

Object

replace

​(

Object

key,

Object

value)

Replaces the entry for the specified key only if it is
currently mapped to some value.

boolean

replace

​(

Object

key,

Object

oldValue,

Object

newValue)

Replaces the entry for the specified key only if currently
mapped to the specified value.

void

replaceAll

​(

BiFunction

<? super

Object

,​? super

Object

,​? extends

Object

> function)

Replaces each entry's value with the result of invoking the given
function on that entry, in the order entries are returned by an entry
set iterator, until all entries have been processed or the function
throws an exception.

String

toString

()

Returns a string with the name and the version string
of this provider.

Collection

<

Object

>

values

()

Returns an unmodifiable Collection view of the property values
contained in this provider.

- Methods declared in class java.util.

Properties

getProperty

,

getProperty

,

list

,

list

,

load

,

loadFromXML

,

propertyNames

,

save

,

setProperty

,

store

,

store

,

storeToXML

,

storeToXML

,

storeToXML

,

stringPropertyNames

- Methods declared in class java.util.

Hashtable

clone

,

contains

,

containsKey

,

containsValue

,

elements

,

equals

,

get

,

hashCode

,

isEmpty

,

keys

,

rehash

,

size

- Methods declared in class java.lang.

Object

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

Provider.Service

The description of a security service.

---

#### Nested Class Summary

The description of a security service.

Field Summary

- Fields declared in class java.util.

Properties

defaults

---

#### Field Summary

Fields declared in class java.util.

Properties

defaults

---

#### Fields declared in class java.util. Properties

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Provider

​(

String

name,
double version,

String

info)

Deprecated.

use

Provider(String, String, String)

instead.

protected

Provider

​(

String

name,

String

versionStr,

String

info)

Constructs a provider with the specified name, version string,
and information.

---

#### Constructor Summary

Deprecated.

use

Provider(String, String, String)

instead.

Constructs a provider with the specified name, version string,
and information.

Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

void

clear

()

Clears this provider so that it no longer contains the properties
used to look up facilities implemented by the provider.

Object

compute

​(

Object

key,

BiFunction

<? super

Object

,​? super

Object

,​? extends

Object

> remappingFunction)

Attempts to compute a mapping for the specified key and its
current mapped value (or

null

if there is no current
mapping).

Object

computeIfAbsent

​(

Object

key,

Function

<? super

Object

,​? extends

Object

> mappingFunction)

If the specified key is not already associated with a value (or
is mapped to

null

), attempts to compute its value using
the given mapping function and enters it into this map unless

null

.

Object

computeIfPresent

​(

Object

key,

BiFunction

<? super

Object

,​? super

Object

,​? extends

Object

> remappingFunction)

If the value for the specified key is present and non-null, attempts to
compute a new mapping given the key and its current mapped value.

Provider

configure

​(

String

configArg)

Apply the supplied configuration argument to this provider instance
and return the configured provider.

Set

<

Map.Entry

<

Object

,​

Object

>>

entrySet

()

Returns an unmodifiable Set view of the property entries contained
in this Provider.

void

forEach

​(

BiConsumer

<? super

Object

,​? super

Object

> action)

Performs the given action for each entry in this map until all entries
have been processed or the action throws an exception.

String

getInfo

()

Returns a human-readable description of the provider and its
services.

String

getName

()

Returns the name of this provider.

Object

getOrDefault

​(

Object

key,

Object

defaultValue)

Returns the value to which the specified key is mapped, or

defaultValue

if this map contains no mapping for the key.

Provider.Service

getService

​(

String

type,

String

algorithm)

Get the service describing this Provider's implementation of the
specified type of this algorithm or alias.

Set

<

Provider.Service

>

getServices

()

Get an unmodifiable Set of all services supported by
this Provider.

double

getVersion

()

Deprecated.

use

getVersionStr()

instead.

String

getVersionStr

()

Returns the version string for this provider.

boolean

isConfigured

()

Check if this provider instance has been configured.

Set

<

Object

>

keySet

()

Returns an unmodifiable Set view of the property keys contained in
this provider.

void

load

​(

InputStream

inStream)

Reads a property list (key and element pairs) from the input stream.

Object

merge

​(

Object

key,

Object

value,

BiFunction

<? super

Object

,​? super

Object

,​? extends

Object

> remappingFunction)

If the specified key is not already associated with a value or is
associated with null, associates it with the given value.

Object

put

​(

Object

key,

Object

value)

Sets the

key

property to have the specified

value

.

void

putAll

​(

Map

<?,​?> t)

Copies all of the mappings from the specified Map to this provider.

Object

putIfAbsent

​(

Object

key,

Object

value)

If the specified key is not already associated with a value (or is mapped
to

null

) associates it with the given value and returns

null

, else returns the current value.

protected void

putService

​(

Provider.Service

s)

Add a service.

Object

remove

​(

Object

key)

Removes the

key

property (and its corresponding

value

).

boolean

remove

​(

Object

key,

Object

value)

Removes the entry for the specified key only if it is currently
mapped to the specified value.

protected void

removeService

​(

Provider.Service

s)

Remove a service previously added using

putService()

.

Object

replace

​(

Object

key,

Object

value)

Replaces the entry for the specified key only if it is
currently mapped to some value.

boolean

replace

​(

Object

key,

Object

oldValue,

Object

newValue)

Replaces the entry for the specified key only if currently
mapped to the specified value.

void

replaceAll

​(

BiFunction

<? super

Object

,​? super

Object

,​? extends

Object

> function)

Replaces each entry's value with the result of invoking the given
function on that entry, in the order entries are returned by an entry
set iterator, until all entries have been processed or the function
throws an exception.

String

toString

()

Returns a string with the name and the version string
of this provider.

Collection

<

Object

>

values

()

Returns an unmodifiable Collection view of the property values
contained in this provider.

- Methods declared in class java.util.

Properties

getProperty

,

getProperty

,

list

,

list

,

load

,

loadFromXML

,

propertyNames

,

save

,

setProperty

,

store

,

store

,

storeToXML

,

storeToXML

,

storeToXML

,

stringPropertyNames

- Methods declared in class java.util.

Hashtable

clone

,

contains

,

containsKey

,

containsValue

,

elements

,

equals

,

get

,

hashCode

,

isEmpty

,

keys

,

rehash

,

size

- Methods declared in class java.lang.

Object

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

Clears this provider so that it no longer contains the properties
used to look up facilities implemented by the provider.

Attempts to compute a mapping for the specified key and its
current mapped value (or

null

if there is no current
mapping).

If the specified key is not already associated with a value (or
is mapped to

null

), attempts to compute its value using
the given mapping function and enters it into this map unless

null

.

If the value for the specified key is present and non-null, attempts to
compute a new mapping given the key and its current mapped value.

Apply the supplied configuration argument to this provider instance
and return the configured provider.

Returns an unmodifiable Set view of the property entries contained
in this Provider.

Performs the given action for each entry in this map until all entries
have been processed or the action throws an exception.

Returns a human-readable description of the provider and its
services.

Returns the name of this provider.

Returns the value to which the specified key is mapped, or

defaultValue

if this map contains no mapping for the key.

Get the service describing this Provider's implementation of the
specified type of this algorithm or alias.

Get an unmodifiable Set of all services supported by
this Provider.

Deprecated.

use

getVersionStr()

instead.

Returns the version string for this provider.

Check if this provider instance has been configured.

Returns an unmodifiable Set view of the property keys contained in
this provider.

Reads a property list (key and element pairs) from the input stream.

If the specified key is not already associated with a value or is
associated with null, associates it with the given value.

Sets the

key

property to have the specified

value

.

Copies all of the mappings from the specified Map to this provider.

If the specified key is not already associated with a value (or is mapped
to

null

) associates it with the given value and returns

null

, else returns the current value.

Add a service.

Removes the

key

property (and its corresponding

value

).

Removes the entry for the specified key only if it is currently
mapped to the specified value.

Remove a service previously added using

putService()

.

Replaces the entry for the specified key only if it is
currently mapped to some value.

Replaces the entry for the specified key only if currently
mapped to the specified value.

Replaces each entry's value with the result of invoking the given
function on that entry, in the order entries are returned by an entry
set iterator, until all entries have been processed or the function
throws an exception.

Returns a string with the name and the version string
of this provider.

Returns an unmodifiable Collection view of the property values
contained in this provider.

Methods declared in class java.util.

Properties

getProperty

,

getProperty

,

list

,

list

,

load

,

loadFromXML

,

propertyNames

,

save

,

setProperty

,

store

,

store

,

storeToXML

,

storeToXML

,

storeToXML

,

stringPropertyNames

---

#### Methods declared in class java.util. Properties

Methods declared in class java.util.

Hashtable

clone

,

contains

,

containsKey

,

containsValue

,

elements

,

equals

,

get

,

hashCode

,

isEmpty

,

keys

,

rehash

,

size

---

#### Methods declared in class java.util. Hashtable

Methods declared in class java.lang.

Object

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

- Provider

```java
@Deprecated
(
since
="9")
protected Provider​(
String
name,
double version,

String
info)
```

Deprecated.

use

Provider(String, String, String)

instead.

Constructs a provider with the specified name, version number,
and information. Calling this constructor is equivalent to call the

Provider(String, String, String)

with

name

name,

Double.toString(version)

, and

info

.

**Parameters:** name

- the provider name.
**Parameters:** version

- the provider version number.
**Parameters:** info

- a description of the provider and its services.

- Provider

```java
protected Provider​(
String
name,

String
versionStr,

String
info)
```

Constructs a provider with the specified name, version string,
and information.

The version string contains a version number optionally followed
by other information separated by one of the characters of '+', '-'.

The format for the version number is:

```java
^[0-9]+(\.[0-9]+)*
```

In order to return the version number in a double, when there are
more than two components (separated by '.' as defined above), only
the first two components are retained. The resulting string is then
passed to

Double.valueOf(String)

to generate version number,
i.e.

getVersion()

.

If the conversion failed, value 0 will be used.

**Parameters:** name

- the provider name.
**Parameters:** versionStr

- the provider version string.
**Parameters:** info

- a description of the provider and its services.
**Since:** 9

============ METHOD DETAIL ==========

- Method Detail

- configure

```java
public
Provider
configure​(
String
configArg)
```

Apply the supplied configuration argument to this provider instance
and return the configured provider. Note that if this provider cannot
be configured in-place, a new provider will be created and returned.
Therefore, callers should always use the returned provider.

**Implementation Requirements:** The default implementation throws

UnsupportedOperationException

.
Subclasses should override this method only if a configuration argument
is supported.
**Parameters:** configArg

- the configuration information for configuring this
provider.
**Returns:** a provider configured with the supplied configuration argument.
**Throws:** UnsupportedOperationException

- if a configuration argument is
not supported.
**Throws:** NullPointerException

- if the supplied configuration argument is
null.
**Throws:** InvalidParameterException

- if the supplied configuration argument
is invalid.
**Since:** 9

- isConfigured

```java
public boolean isConfigured()
```

Check if this provider instance has been configured.

**Implementation Requirements:** The default implementation returns true.
Subclasses should override this method if the provider instance requires
an explicit

configure

call after being constructed.
**Returns:** true if no further configuration is needed, false otherwise.
**Since:** 9

- getName

```java
public
String
getName()
```

Returns the name of this provider.

**Returns:** the name of this provider.

- getVersion

```java
@Deprecated
(
since
="9")
public double getVersion()
```

Deprecated.

use

getVersionStr()

instead.

Returns the version number for this provider.

**Returns:** the version number for this provider.

- getVersionStr

```java
public
String
getVersionStr()
```

Returns the version string for this provider.

**Returns:** the version string for this provider.
**Since:** 9

- getInfo

```java
public
String
getInfo()
```

Returns a human-readable description of the provider and its
services. This may return an HTML page, with relevant links.

**Returns:** a description of the provider and its services.

- toString

```java
public
String
toString()
```

Returns a string with the name and the version string
of this provider.

**Overrides:** toString

in class

Hashtable

<

Object

,​

Object

>
**Returns:** the string with the name and the version string
for this provider.

- clear

```java
public void clear()
```

Clears this provider so that it no longer contains the properties
used to look up facilities implemented by the provider.

If a security manager is enabled, its

checkSecurityAccess

method is called with the string

"clearProviderProperties."+name

(where

name

is the provider name) to see if it's ok to clear
this provider.

**Specified by:** clear

in interface

Map

<

Object

,​

Object

>
**Overrides:** clear

in class

Hashtable

<

Object

,​

Object

>
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to clear this provider
**Since:** 1.2

- load

```java
public void load​(
InputStream
inStream)
throws
IOException
```

Reads a property list (key and element pairs) from the input stream.

**Overrides:** load

in class

Properties
**Parameters:** inStream

- the input stream.
**Throws:** IOException

- if an error occurred when reading from the
input stream.
**See Also:** Properties.load(java.io.Reader)

- putAll

```java
public void putAll​(
Map
<?,​?> t)
```

Copies all of the mappings from the specified Map to this provider.
These mappings will replace any properties that this provider had
for any of the keys currently in the specified Map.

**Specified by:** putAll

in interface

Map

<

Object

,​

Object

>
**Overrides:** putAll

in class

Hashtable

<

Object

,​

Object

>
**Parameters:** t

- mappings to be stored in this map
**Since:** 1.2

- entrySet

```java
public
Set
<
Map.Entry
<
Object
,​
Object
>> entrySet()
```

Returns an unmodifiable Set view of the property entries contained
in this Provider.

**Specified by:** entrySet

in interface

Map

<

Object

,​

Object

>
**Overrides:** entrySet

in class

Hashtable

<

Object

,​

Object

>
**Returns:** a set view of the mappings contained in this map
**Since:** 1.2
**See Also:** Map.Entry

- keySet

```java
public
Set
<
Object
> keySet()
```

Returns an unmodifiable Set view of the property keys contained in
this provider.

**Specified by:** keySet

in interface

Map

<

Object

,​

Object

>
**Overrides:** keySet

in class

Hashtable

<

Object

,​

Object

>
**Returns:** a set view of the keys contained in this map
**Since:** 1.2

- values

```java
public
Collection
<
Object
> values()
```

Returns an unmodifiable Collection view of the property values
contained in this provider.

**Specified by:** values

in interface

Map

<

Object

,​

Object

>
**Overrides:** values

in class

Hashtable

<

Object

,​

Object

>
**Returns:** a collection view of the values contained in this map
**Since:** 1.2

- put

```java
public
Object
put​(
Object
key,

Object
value)
```

Sets the

key

property to have the specified

value

.

If a security manager is enabled, its

checkSecurityAccess

method is called with the string

"putProviderProperty."+name

,
where

name

is the provider name, to see if it's ok to set this
provider's property values.

**Specified by:** put

in interface

Map

<

Object

,​

Object

>
**Overrides:** put

in class

Hashtable

<

Object

,​

Object

>
**Parameters:** key

- the hashtable key
**Parameters:** value

- the value
**Returns:** the previous value of the specified key in this hashtable,
or

null

if it did not have one
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to set property values.
**Since:** 1.2
**See Also:** Object.equals(Object)

,

Hashtable.get(Object)

- putIfAbsent

```java
public
Object
putIfAbsent​(
Object
key,

Object
value)
```

If the specified key is not already associated with a value (or is mapped
to

null

) associates it with the given value and returns

null

, else returns the current value.

If a security manager is enabled, its

checkSecurityAccess

method is called with the string

"putProviderProperty."+name

,
where

name

is the provider name, to see if it's ok to set this
provider's property values.

**Parameters:** key

- key with which the specified value is to be associated
**Parameters:** value

- value to be associated with the specified key
**Returns:** the previous value associated with the specified key, or

null

if there was no mapping for the key.
(A

null

return can also indicate that the map
previously associated

null

with the key,
if the implementation supports null values.)
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to set property values.
**Since:** 1.8

- remove

```java
public
Object
remove​(
Object
key)
```

Removes the

key

property (and its corresponding

value

).

If a security manager is enabled, its

checkSecurityAccess

method is called with the string

"removeProviderProperty."+name

,
where

name

is the provider name, to see if it's ok to remove this
provider's properties.

**Specified by:** remove

in interface

Map

<

Object

,​

Object

>
**Overrides:** remove

in class

Hashtable

<

Object

,​

Object

>
**Parameters:** key

- the key that needs to be removed
**Returns:** the value to which the key had been mapped in this hashtable,
or

null

if the key did not have a mapping
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to remove this provider's properties.
**Since:** 1.2

- remove

```java
public boolean remove​(
Object
key,

Object
value)
```

Removes the entry for the specified key only if it is currently
mapped to the specified value.

If a security manager is enabled, its

checkSecurityAccess

method is called with the string

"removeProviderProperty."+name

,
where

name

is the provider name, to see if it's ok to remove this
provider's properties.

**Parameters:** key

- key with which the specified value is associated
**Parameters:** value

- value expected to be associated with the specified key
**Returns:** true

if the value was removed
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to remove this provider's properties.
**Since:** 1.8

- replace

```java
public boolean replace​(
Object
key,

Object
oldValue,

Object
newValue)
```

Replaces the entry for the specified key only if currently
mapped to the specified value.

If a security manager is enabled, its

checkSecurityAccess

method is called with the string

"putProviderProperty."+name

,
where

name

is the provider name, to see if it's ok to set this
provider's property values.

**Parameters:** key

- key with which the specified value is associated
**Parameters:** oldValue

- value expected to be associated with the specified key
**Parameters:** newValue

- value to be associated with the specified key
**Returns:** true

if the value was replaced
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to set property values.
**Since:** 1.8

- replace

```java
public
Object
replace​(
Object
key,

Object
value)
```

Replaces the entry for the specified key only if it is
currently mapped to some value.

If a security manager is enabled, its

checkSecurityAccess

method is called with the string

"putProviderProperty."+name

,
where

name

is the provider name, to see if it's ok to set this
provider's property values.

**Parameters:** key

- key with which the specified value is associated
**Parameters:** value

- value to be associated with the specified key
**Returns:** the previous value associated with the specified key, or

null

if there was no mapping for the key.
(A

null

return can also indicate that the map
previously associated

null

with the key,
if the implementation supports null values.)
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to set property values.
**Since:** 1.8

- replaceAll

```java
public void replaceAll​(
BiFunction
<? super
Object
,​? super
Object
,​? extends
Object
> function)
```

Replaces each entry's value with the result of invoking the given
function on that entry, in the order entries are returned by an entry
set iterator, until all entries have been processed or the function
throws an exception.

If a security manager is enabled, its

checkSecurityAccess

method is called with the string

"putProviderProperty."+name

,
where

name

is the provider name, to see if it's ok to set this
provider's property values.

**Parameters:** function

- the function to apply to each entry
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to set property values.
**Since:** 1.8

- compute

```java
public
Object
compute​(
Object
key,

BiFunction
<? super
Object
,​? super
Object
,​? extends
Object
> remappingFunction)
```

Attempts to compute a mapping for the specified key and its
current mapped value (or

null

if there is no current
mapping).

If a security manager is enabled, its

checkSecurityAccess

method is called with the strings

"putProviderProperty."+name

and

"removeProviderProperty."+name

, where

name

is the
provider name, to see if it's ok to set this provider's property values
and remove this provider's properties.

**Specified by:** compute

in interface

Map

<

Object

,​

Object

>
**Overrides:** compute

in class

Hashtable

<

Object

,​

Object

>
**Parameters:** key

- key with which the specified value is to be associated
**Parameters:** remappingFunction

- the remapping function to compute a value
**Returns:** the new value associated with the specified key, or null if none
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to set property values or remove properties.
**Since:** 1.8

- computeIfAbsent

```java
public
Object
computeIfAbsent​(
Object
key,

Function
<? super
Object
,​? extends
Object
> mappingFunction)
```

If the specified key is not already associated with a value (or
is mapped to

null

), attempts to compute its value using
the given mapping function and enters it into this map unless

null

.

If a security manager is enabled, its

checkSecurityAccess

method is called with the strings

"putProviderProperty."+name

and

"removeProviderProperty."+name

, where

name

is the
provider name, to see if it's ok to set this provider's property values
and remove this provider's properties.

**Specified by:** computeIfAbsent

in interface

Map

<

Object

,​

Object

>
**Overrides:** computeIfAbsent

in class

Hashtable

<

Object

,​

Object

>
**Parameters:** key

- key with which the specified value is to be associated
**Parameters:** mappingFunction

- the mapping function to compute a value
**Returns:** the current (existing or computed) value associated with
the specified key, or null if the computed value is null
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to set property values and remove properties.
**Since:** 1.8

- computeIfPresent

```java
public
Object
computeIfPresent​(
Object
key,

BiFunction
<? super
Object
,​? super
Object
,​? extends
Object
> remappingFunction)
```

If the value for the specified key is present and non-null, attempts to
compute a new mapping given the key and its current mapped value.

If a security manager is enabled, its

checkSecurityAccess

method is called with the strings

"putProviderProperty."+name

and

"removeProviderProperty."+name

, where

name

is the
provider name, to see if it's ok to set this provider's property values
and remove this provider's properties.

**Specified by:** computeIfPresent

in interface

Map

<

Object

,​

Object

>
**Overrides:** computeIfPresent

in class

Hashtable

<

Object

,​

Object

>
**Parameters:** key

- key with which the specified value is to be associated
**Parameters:** remappingFunction

- the remapping function to compute a value
**Returns:** the new value associated with the specified key, or null if none
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to set property values or remove properties.
**Since:** 1.8

- merge

```java
public
Object
merge​(
Object
key,

Object
value,

BiFunction
<? super
Object
,​? super
Object
,​? extends
Object
> remappingFunction)
```

If the specified key is not already associated with a value or is
associated with null, associates it with the given value. Otherwise,
replaces the value with the results of the given remapping function,
or removes if the result is null. This method may be of use when
combining multiple mapped values for a key.

If a security manager is enabled, its

checkSecurityAccess

method is called with the strings

"putProviderProperty."+name

and

"removeProviderProperty."+name

, where

name

is the
provider name, to see if it's ok to set this provider's property values
and remove this provider's properties.

**Specified by:** merge

in interface

Map

<

Object

,​

Object

>
**Overrides:** merge

in class

Hashtable

<

Object

,​

Object

>
**Parameters:** key

- key with which the resulting value is to be associated
**Parameters:** value

- the non-null value to be merged with the existing value
associated with the key or, if no existing value or a null value
is associated with the key, to be associated with the key
**Parameters:** remappingFunction

- the remapping function to recompute a value if
present
**Returns:** the new value associated with the specified key, or null if no
value is associated with the key
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to set property values or remove properties.
**Since:** 1.8

- getOrDefault

```java
public
Object
getOrDefault​(
Object
key,

Object
defaultValue)
```

Description copied from interface:

Map

Returns the value to which the specified key is mapped, or

defaultValue

if this map contains no mapping for the key.

**Parameters:** key

- the key whose associated value is to be returned
**Parameters:** defaultValue

- the default mapping of the key
**Returns:** the value to which the specified key is mapped, or

defaultValue

if this map contains no mapping for the key
**Since:** 1.8

- forEach

```java
public void forEach​(
BiConsumer
<? super
Object
,​? super
Object
> action)
```

Description copied from interface:

Map

Performs the given action for each entry in this map until all entries
have been processed or the action throws an exception. Unless
otherwise specified by the implementing class, actions are performed in
the order of entry set iteration (if an iteration order is specified.)
Exceptions thrown by the action are relayed to the caller.

**Parameters:** action

- The action to be performed for each entry
**Since:** 1.8

- getService

```java
public
Provider.Service
getService​(
String
type,

String
algorithm)
```

Get the service describing this Provider's implementation of the
specified type of this algorithm or alias. If no such
implementation exists, this method returns null. If there are two
matching services, one added to this provider using

putService()

and one added via

put()

,
the service added via

putService()

is returned.

**Parameters:** type

- the type of

service

requested
(for example,

MessageDigest

)
**Parameters:** algorithm

- the case insensitive algorithm name (or alternate
alias) of the service requested (for example,

SHA-1

)
**Returns:** the service describing this Provider's matching service
or null if no such service exists
**Throws:** NullPointerException

- if type or algorithm is null
**Since:** 1.5

- getServices

```java
public
Set
<
Provider.Service
> getServices()
```

Get an unmodifiable Set of all services supported by
this Provider.

**Returns:** an unmodifiable Set of all services supported by
this Provider
**Since:** 1.5

- putService

```java
protected void putService​(
Provider.Service
s)
```

Add a service. If a service of the same type with the same algorithm
name exists and it was added using

putService()

,
it is replaced by the new service.
This method also places information about this service
in the provider's Hashtable values in the format described in the

Java Cryptography Architecture (JCA) Reference Guide

.

Also, if there is a security manager, its

checkSecurityAccess

method is called with the string

"putProviderProperty."+name

, where

name

is
the provider name, to see if it's ok to set this provider's property
values. If the default implementation of

checkSecurityAccess

is used (that is, that method is not overriden), then this results in
a call to the security manager's

checkPermission

method with
a

SecurityPermission("putProviderProperty."+name)

permission.

**Parameters:** s

- the Service to add
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method denies
access to set property values.
**Throws:** NullPointerException

- if s is null
**Since:** 1.5

- removeService

```java
protected void removeService​(
Provider.Service
s)
```

Remove a service previously added using

putService()

. The specified service is removed from
this provider. It will no longer be returned by

getService()

and its information will be removed
from this provider's Hashtable.

Also, if there is a security manager, its

checkSecurityAccess

method is called with the string

"removeProviderProperty."+name

, where

name

is
the provider name, to see if it's ok to remove this provider's
properties. If the default implementation of

checkSecurityAccess

is used (that is, that method is not
overriden), then this results in a call to the security manager's

checkPermission

method with a

SecurityPermission("removeProviderProperty."+name)

permission.

**Parameters:** s

- the Service to be removed
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method denies
access to remove this provider's properties.
**Throws:** NullPointerException

- if s is null
**Since:** 1.5

Constructor Detail

- Provider

```java
@Deprecated
(
since
="9")
protected Provider​(
String
name,
double version,

String
info)
```

Deprecated.

use

Provider(String, String, String)

instead.

Constructs a provider with the specified name, version number,
and information. Calling this constructor is equivalent to call the

Provider(String, String, String)

with

name

name,

Double.toString(version)

, and

info

.

**Parameters:** name

- the provider name.
**Parameters:** version

- the provider version number.
**Parameters:** info

- a description of the provider and its services.

- Provider

```java
protected Provider​(
String
name,

String
versionStr,

String
info)
```

Constructs a provider with the specified name, version string,
and information.

The version string contains a version number optionally followed
by other information separated by one of the characters of '+', '-'.

The format for the version number is:

```java
^[0-9]+(\.[0-9]+)*
```

In order to return the version number in a double, when there are
more than two components (separated by '.' as defined above), only
the first two components are retained. The resulting string is then
passed to

Double.valueOf(String)

to generate version number,
i.e.

getVersion()

.

If the conversion failed, value 0 will be used.

**Parameters:** name

- the provider name.
**Parameters:** versionStr

- the provider version string.
**Parameters:** info

- a description of the provider and its services.
**Since:** 9

---

#### Constructor Detail

Provider

```java
@Deprecated
(
since
="9")
protected Provider​(
String
name,
double version,

String
info)
```

Deprecated.

use

Provider(String, String, String)

instead.

Constructs a provider with the specified name, version number,
and information. Calling this constructor is equivalent to call the

Provider(String, String, String)

with

name

name,

Double.toString(version)

, and

info

.

**Parameters:** name

- the provider name.
**Parameters:** version

- the provider version number.
**Parameters:** info

- a description of the provider and its services.

---

#### Provider

@Deprecated

(

since

="9")
protected Provider​(

String

name,
double version,

String

info)

Constructs a provider with the specified name, version number,
and information. Calling this constructor is equivalent to call the

Provider(String, String, String)

with

name

name,

Double.toString(version)

, and

info

.

Provider

```java
protected Provider​(
String
name,

String
versionStr,

String
info)
```

Constructs a provider with the specified name, version string,
and information.

The version string contains a version number optionally followed
by other information separated by one of the characters of '+', '-'.

The format for the version number is:

```java
^[0-9]+(\.[0-9]+)*
```

In order to return the version number in a double, when there are
more than two components (separated by '.' as defined above), only
the first two components are retained. The resulting string is then
passed to

Double.valueOf(String)

to generate version number,
i.e.

getVersion()

.

If the conversion failed, value 0 will be used.

**Parameters:** name

- the provider name.
**Parameters:** versionStr

- the provider version string.
**Parameters:** info

- a description of the provider and its services.
**Since:** 9

---

#### Provider

protected Provider​(

String

name,

String

versionStr,

String

info)

Constructs a provider with the specified name, version string,
and information.

The version string contains a version number optionally followed
by other information separated by one of the characters of '+', '-'.

The format for the version number is:

```java
^[0-9]+(\.[0-9]+)*
```

In order to return the version number in a double, when there are
more than two components (separated by '.' as defined above), only
the first two components are retained. The resulting string is then
passed to

Double.valueOf(String)

to generate version number,
i.e.

getVersion()

.

If the conversion failed, value 0 will be used.

The version string contains a version number optionally followed
by other information separated by one of the characters of '+', '-'.

The format for the version number is:

```java
^[0-9]+(\.[0-9]+)*
```

In order to return the version number in a double, when there are
more than two components (separated by '.' as defined above), only
the first two components are retained. The resulting string is then
passed to

Double.valueOf(String)

to generate version number,
i.e.

getVersion()

.

If the conversion failed, value 0 will be used.

^[0-9]+(\.[0-9]+)*

In order to return the version number in a double, when there are
more than two components (separated by '.' as defined above), only
the first two components are retained. The resulting string is then
passed to

Double.valueOf(String)

to generate version number,
i.e.

getVersion()

.

If the conversion failed, value 0 will be used.

If the conversion failed, value 0 will be used.

Method Detail

- configure

```java
public
Provider
configure​(
String
configArg)
```

Apply the supplied configuration argument to this provider instance
and return the configured provider. Note that if this provider cannot
be configured in-place, a new provider will be created and returned.
Therefore, callers should always use the returned provider.

**Implementation Requirements:** The default implementation throws

UnsupportedOperationException

.
Subclasses should override this method only if a configuration argument
is supported.
**Parameters:** configArg

- the configuration information for configuring this
provider.
**Returns:** a provider configured with the supplied configuration argument.
**Throws:** UnsupportedOperationException

- if a configuration argument is
not supported.
**Throws:** NullPointerException

- if the supplied configuration argument is
null.
**Throws:** InvalidParameterException

- if the supplied configuration argument
is invalid.
**Since:** 9

- isConfigured

```java
public boolean isConfigured()
```

Check if this provider instance has been configured.

**Implementation Requirements:** The default implementation returns true.
Subclasses should override this method if the provider instance requires
an explicit

configure

call after being constructed.
**Returns:** true if no further configuration is needed, false otherwise.
**Since:** 9

- getName

```java
public
String
getName()
```

Returns the name of this provider.

**Returns:** the name of this provider.

- getVersion

```java
@Deprecated
(
since
="9")
public double getVersion()
```

Deprecated.

use

getVersionStr()

instead.

Returns the version number for this provider.

**Returns:** the version number for this provider.

- getVersionStr

```java
public
String
getVersionStr()
```

Returns the version string for this provider.

**Returns:** the version string for this provider.
**Since:** 9

- getInfo

```java
public
String
getInfo()
```

Returns a human-readable description of the provider and its
services. This may return an HTML page, with relevant links.

**Returns:** a description of the provider and its services.

- toString

```java
public
String
toString()
```

Returns a string with the name and the version string
of this provider.

**Overrides:** toString

in class

Hashtable

<

Object

,​

Object

>
**Returns:** the string with the name and the version string
for this provider.

- clear

```java
public void clear()
```

Clears this provider so that it no longer contains the properties
used to look up facilities implemented by the provider.

If a security manager is enabled, its

checkSecurityAccess

method is called with the string

"clearProviderProperties."+name

(where

name

is the provider name) to see if it's ok to clear
this provider.

**Specified by:** clear

in interface

Map

<

Object

,​

Object

>
**Overrides:** clear

in class

Hashtable

<

Object

,​

Object

>
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to clear this provider
**Since:** 1.2

- load

```java
public void load​(
InputStream
inStream)
throws
IOException
```

Reads a property list (key and element pairs) from the input stream.

**Overrides:** load

in class

Properties
**Parameters:** inStream

- the input stream.
**Throws:** IOException

- if an error occurred when reading from the
input stream.
**See Also:** Properties.load(java.io.Reader)

- putAll

```java
public void putAll​(
Map
<?,​?> t)
```

Copies all of the mappings from the specified Map to this provider.
These mappings will replace any properties that this provider had
for any of the keys currently in the specified Map.

**Specified by:** putAll

in interface

Map

<

Object

,​

Object

>
**Overrides:** putAll

in class

Hashtable

<

Object

,​

Object

>
**Parameters:** t

- mappings to be stored in this map
**Since:** 1.2

- entrySet

```java
public
Set
<
Map.Entry
<
Object
,​
Object
>> entrySet()
```

Returns an unmodifiable Set view of the property entries contained
in this Provider.

**Specified by:** entrySet

in interface

Map

<

Object

,​

Object

>
**Overrides:** entrySet

in class

Hashtable

<

Object

,​

Object

>
**Returns:** a set view of the mappings contained in this map
**Since:** 1.2
**See Also:** Map.Entry

- keySet

```java
public
Set
<
Object
> keySet()
```

Returns an unmodifiable Set view of the property keys contained in
this provider.

**Specified by:** keySet

in interface

Map

<

Object

,​

Object

>
**Overrides:** keySet

in class

Hashtable

<

Object

,​

Object

>
**Returns:** a set view of the keys contained in this map
**Since:** 1.2

- values

```java
public
Collection
<
Object
> values()
```

Returns an unmodifiable Collection view of the property values
contained in this provider.

**Specified by:** values

in interface

Map

<

Object

,​

Object

>
**Overrides:** values

in class

Hashtable

<

Object

,​

Object

>
**Returns:** a collection view of the values contained in this map
**Since:** 1.2

- put

```java
public
Object
put​(
Object
key,

Object
value)
```

Sets the

key

property to have the specified

value

.

If a security manager is enabled, its

checkSecurityAccess

method is called with the string

"putProviderProperty."+name

,
where

name

is the provider name, to see if it's ok to set this
provider's property values.

**Specified by:** put

in interface

Map

<

Object

,​

Object

>
**Overrides:** put

in class

Hashtable

<

Object

,​

Object

>
**Parameters:** key

- the hashtable key
**Parameters:** value

- the value
**Returns:** the previous value of the specified key in this hashtable,
or

null

if it did not have one
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to set property values.
**Since:** 1.2
**See Also:** Object.equals(Object)

,

Hashtable.get(Object)

- putIfAbsent

```java
public
Object
putIfAbsent​(
Object
key,

Object
value)
```

If the specified key is not already associated with a value (or is mapped
to

null

) associates it with the given value and returns

null

, else returns the current value.

If a security manager is enabled, its

checkSecurityAccess

method is called with the string

"putProviderProperty."+name

,
where

name

is the provider name, to see if it's ok to set this
provider's property values.

**Parameters:** key

- key with which the specified value is to be associated
**Parameters:** value

- value to be associated with the specified key
**Returns:** the previous value associated with the specified key, or

null

if there was no mapping for the key.
(A

null

return can also indicate that the map
previously associated

null

with the key,
if the implementation supports null values.)
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to set property values.
**Since:** 1.8

- remove

```java
public
Object
remove​(
Object
key)
```

Removes the

key

property (and its corresponding

value

).

If a security manager is enabled, its

checkSecurityAccess

method is called with the string

"removeProviderProperty."+name

,
where

name

is the provider name, to see if it's ok to remove this
provider's properties.

**Specified by:** remove

in interface

Map

<

Object

,​

Object

>
**Overrides:** remove

in class

Hashtable

<

Object

,​

Object

>
**Parameters:** key

- the key that needs to be removed
**Returns:** the value to which the key had been mapped in this hashtable,
or

null

if the key did not have a mapping
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to remove this provider's properties.
**Since:** 1.2

- remove

```java
public boolean remove​(
Object
key,

Object
value)
```

Removes the entry for the specified key only if it is currently
mapped to the specified value.

If a security manager is enabled, its

checkSecurityAccess

method is called with the string

"removeProviderProperty."+name

,
where

name

is the provider name, to see if it's ok to remove this
provider's properties.

**Parameters:** key

- key with which the specified value is associated
**Parameters:** value

- value expected to be associated with the specified key
**Returns:** true

if the value was removed
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to remove this provider's properties.
**Since:** 1.8

- replace

```java
public boolean replace​(
Object
key,

Object
oldValue,

Object
newValue)
```

Replaces the entry for the specified key only if currently
mapped to the specified value.

If a security manager is enabled, its

checkSecurityAccess

method is called with the string

"putProviderProperty."+name

,
where

name

is the provider name, to see if it's ok to set this
provider's property values.

**Parameters:** key

- key with which the specified value is associated
**Parameters:** oldValue

- value expected to be associated with the specified key
**Parameters:** newValue

- value to be associated with the specified key
**Returns:** true

if the value was replaced
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to set property values.
**Since:** 1.8

- replace

```java
public
Object
replace​(
Object
key,

Object
value)
```

Replaces the entry for the specified key only if it is
currently mapped to some value.

If a security manager is enabled, its

checkSecurityAccess

method is called with the string

"putProviderProperty."+name

,
where

name

is the provider name, to see if it's ok to set this
provider's property values.

**Parameters:** key

- key with which the specified value is associated
**Parameters:** value

- value to be associated with the specified key
**Returns:** the previous value associated with the specified key, or

null

if there was no mapping for the key.
(A

null

return can also indicate that the map
previously associated

null

with the key,
if the implementation supports null values.)
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to set property values.
**Since:** 1.8

- replaceAll

```java
public void replaceAll​(
BiFunction
<? super
Object
,​? super
Object
,​? extends
Object
> function)
```

Replaces each entry's value with the result of invoking the given
function on that entry, in the order entries are returned by an entry
set iterator, until all entries have been processed or the function
throws an exception.

If a security manager is enabled, its

checkSecurityAccess

method is called with the string

"putProviderProperty."+name

,
where

name

is the provider name, to see if it's ok to set this
provider's property values.

**Parameters:** function

- the function to apply to each entry
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to set property values.
**Since:** 1.8

- compute

```java
public
Object
compute​(
Object
key,

BiFunction
<? super
Object
,​? super
Object
,​? extends
Object
> remappingFunction)
```

Attempts to compute a mapping for the specified key and its
current mapped value (or

null

if there is no current
mapping).

If a security manager is enabled, its

checkSecurityAccess

method is called with the strings

"putProviderProperty."+name

and

"removeProviderProperty."+name

, where

name

is the
provider name, to see if it's ok to set this provider's property values
and remove this provider's properties.

**Specified by:** compute

in interface

Map

<

Object

,​

Object

>
**Overrides:** compute

in class

Hashtable

<

Object

,​

Object

>
**Parameters:** key

- key with which the specified value is to be associated
**Parameters:** remappingFunction

- the remapping function to compute a value
**Returns:** the new value associated with the specified key, or null if none
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to set property values or remove properties.
**Since:** 1.8

- computeIfAbsent

```java
public
Object
computeIfAbsent​(
Object
key,

Function
<? super
Object
,​? extends
Object
> mappingFunction)
```

If the specified key is not already associated with a value (or
is mapped to

null

), attempts to compute its value using
the given mapping function and enters it into this map unless

null

.

If a security manager is enabled, its

checkSecurityAccess

method is called with the strings

"putProviderProperty."+name

and

"removeProviderProperty."+name

, where

name

is the
provider name, to see if it's ok to set this provider's property values
and remove this provider's properties.

**Specified by:** computeIfAbsent

in interface

Map

<

Object

,​

Object

>
**Overrides:** computeIfAbsent

in class

Hashtable

<

Object

,​

Object

>
**Parameters:** key

- key with which the specified value is to be associated
**Parameters:** mappingFunction

- the mapping function to compute a value
**Returns:** the current (existing or computed) value associated with
the specified key, or null if the computed value is null
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to set property values and remove properties.
**Since:** 1.8

- computeIfPresent

```java
public
Object
computeIfPresent​(
Object
key,

BiFunction
<? super
Object
,​? super
Object
,​? extends
Object
> remappingFunction)
```

If the value for the specified key is present and non-null, attempts to
compute a new mapping given the key and its current mapped value.

If a security manager is enabled, its

checkSecurityAccess

method is called with the strings

"putProviderProperty."+name

and

"removeProviderProperty."+name

, where

name

is the
provider name, to see if it's ok to set this provider's property values
and remove this provider's properties.

**Specified by:** computeIfPresent

in interface

Map

<

Object

,​

Object

>
**Overrides:** computeIfPresent

in class

Hashtable

<

Object

,​

Object

>
**Parameters:** key

- key with which the specified value is to be associated
**Parameters:** remappingFunction

- the remapping function to compute a value
**Returns:** the new value associated with the specified key, or null if none
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to set property values or remove properties.
**Since:** 1.8

- merge

```java
public
Object
merge​(
Object
key,

Object
value,

BiFunction
<? super
Object
,​? super
Object
,​? extends
Object
> remappingFunction)
```

If the specified key is not already associated with a value or is
associated with null, associates it with the given value. Otherwise,
replaces the value with the results of the given remapping function,
or removes if the result is null. This method may be of use when
combining multiple mapped values for a key.

If a security manager is enabled, its

checkSecurityAccess

method is called with the strings

"putProviderProperty."+name

and

"removeProviderProperty."+name

, where

name

is the
provider name, to see if it's ok to set this provider's property values
and remove this provider's properties.

**Specified by:** merge

in interface

Map

<

Object

,​

Object

>
**Overrides:** merge

in class

Hashtable

<

Object

,​

Object

>
**Parameters:** key

- key with which the resulting value is to be associated
**Parameters:** value

- the non-null value to be merged with the existing value
associated with the key or, if no existing value or a null value
is associated with the key, to be associated with the key
**Parameters:** remappingFunction

- the remapping function to recompute a value if
present
**Returns:** the new value associated with the specified key, or null if no
value is associated with the key
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to set property values or remove properties.
**Since:** 1.8

- getOrDefault

```java
public
Object
getOrDefault​(
Object
key,

Object
defaultValue)
```

Description copied from interface:

Map

Returns the value to which the specified key is mapped, or

defaultValue

if this map contains no mapping for the key.

**Parameters:** key

- the key whose associated value is to be returned
**Parameters:** defaultValue

- the default mapping of the key
**Returns:** the value to which the specified key is mapped, or

defaultValue

if this map contains no mapping for the key
**Since:** 1.8

- forEach

```java
public void forEach​(
BiConsumer
<? super
Object
,​? super
Object
> action)
```

Description copied from interface:

Map

Performs the given action for each entry in this map until all entries
have been processed or the action throws an exception. Unless
otherwise specified by the implementing class, actions are performed in
the order of entry set iteration (if an iteration order is specified.)
Exceptions thrown by the action are relayed to the caller.

**Parameters:** action

- The action to be performed for each entry
**Since:** 1.8

- getService

```java
public
Provider.Service
getService​(
String
type,

String
algorithm)
```

Get the service describing this Provider's implementation of the
specified type of this algorithm or alias. If no such
implementation exists, this method returns null. If there are two
matching services, one added to this provider using

putService()

and one added via

put()

,
the service added via

putService()

is returned.

**Parameters:** type

- the type of

service

requested
(for example,

MessageDigest

)
**Parameters:** algorithm

- the case insensitive algorithm name (or alternate
alias) of the service requested (for example,

SHA-1

)
**Returns:** the service describing this Provider's matching service
or null if no such service exists
**Throws:** NullPointerException

- if type or algorithm is null
**Since:** 1.5

- getServices

```java
public
Set
<
Provider.Service
> getServices()
```

Get an unmodifiable Set of all services supported by
this Provider.

**Returns:** an unmodifiable Set of all services supported by
this Provider
**Since:** 1.5

- putService

```java
protected void putService​(
Provider.Service
s)
```

Add a service. If a service of the same type with the same algorithm
name exists and it was added using

putService()

,
it is replaced by the new service.
This method also places information about this service
in the provider's Hashtable values in the format described in the

Java Cryptography Architecture (JCA) Reference Guide

.

Also, if there is a security manager, its

checkSecurityAccess

method is called with the string

"putProviderProperty."+name

, where

name

is
the provider name, to see if it's ok to set this provider's property
values. If the default implementation of

checkSecurityAccess

is used (that is, that method is not overriden), then this results in
a call to the security manager's

checkPermission

method with
a

SecurityPermission("putProviderProperty."+name)

permission.

**Parameters:** s

- the Service to add
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method denies
access to set property values.
**Throws:** NullPointerException

- if s is null
**Since:** 1.5

- removeService

```java
protected void removeService​(
Provider.Service
s)
```

Remove a service previously added using

putService()

. The specified service is removed from
this provider. It will no longer be returned by

getService()

and its information will be removed
from this provider's Hashtable.

Also, if there is a security manager, its

checkSecurityAccess

method is called with the string

"removeProviderProperty."+name

, where

name

is
the provider name, to see if it's ok to remove this provider's
properties. If the default implementation of

checkSecurityAccess

is used (that is, that method is not
overriden), then this results in a call to the security manager's

checkPermission

method with a

SecurityPermission("removeProviderProperty."+name)

permission.

**Parameters:** s

- the Service to be removed
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method denies
access to remove this provider's properties.
**Throws:** NullPointerException

- if s is null
**Since:** 1.5

---

#### Method Detail

configure

```java
public
Provider
configure​(
String
configArg)
```

Apply the supplied configuration argument to this provider instance
and return the configured provider. Note that if this provider cannot
be configured in-place, a new provider will be created and returned.
Therefore, callers should always use the returned provider.

**Implementation Requirements:** The default implementation throws

UnsupportedOperationException

.
Subclasses should override this method only if a configuration argument
is supported.
**Parameters:** configArg

- the configuration information for configuring this
provider.
**Returns:** a provider configured with the supplied configuration argument.
**Throws:** UnsupportedOperationException

- if a configuration argument is
not supported.
**Throws:** NullPointerException

- if the supplied configuration argument is
null.
**Throws:** InvalidParameterException

- if the supplied configuration argument
is invalid.
**Since:** 9

---

#### configure

public

Provider

configure​(

String

configArg)

Apply the supplied configuration argument to this provider instance
and return the configured provider. Note that if this provider cannot
be configured in-place, a new provider will be created and returned.
Therefore, callers should always use the returned provider.

isConfigured

```java
public boolean isConfigured()
```

Check if this provider instance has been configured.

**Implementation Requirements:** The default implementation returns true.
Subclasses should override this method if the provider instance requires
an explicit

configure

call after being constructed.
**Returns:** true if no further configuration is needed, false otherwise.
**Since:** 9

---

#### isConfigured

public boolean isConfigured()

Check if this provider instance has been configured.

getName

```java
public
String
getName()
```

Returns the name of this provider.

**Returns:** the name of this provider.

---

#### getName

public

String

getName()

Returns the name of this provider.

getVersion

```java
@Deprecated
(
since
="9")
public double getVersion()
```

Deprecated.

use

getVersionStr()

instead.

Returns the version number for this provider.

**Returns:** the version number for this provider.

---

#### getVersion

@Deprecated

(

since

="9")
public double getVersion()

Returns the version number for this provider.

getVersionStr

```java
public
String
getVersionStr()
```

Returns the version string for this provider.

**Returns:** the version string for this provider.
**Since:** 9

---

#### getVersionStr

public

String

getVersionStr()

Returns the version string for this provider.

getInfo

```java
public
String
getInfo()
```

Returns a human-readable description of the provider and its
services. This may return an HTML page, with relevant links.

**Returns:** a description of the provider and its services.

---

#### getInfo

public

String

getInfo()

Returns a human-readable description of the provider and its
services. This may return an HTML page, with relevant links.

toString

```java
public
String
toString()
```

Returns a string with the name and the version string
of this provider.

**Overrides:** toString

in class

Hashtable

<

Object

,​

Object

>
**Returns:** the string with the name and the version string
for this provider.

---

#### toString

public

String

toString()

Returns a string with the name and the version string
of this provider.

clear

```java
public void clear()
```

Clears this provider so that it no longer contains the properties
used to look up facilities implemented by the provider.

If a security manager is enabled, its

checkSecurityAccess

method is called with the string

"clearProviderProperties."+name

(where

name

is the provider name) to see if it's ok to clear
this provider.

**Specified by:** clear

in interface

Map

<

Object

,​

Object

>
**Overrides:** clear

in class

Hashtable

<

Object

,​

Object

>
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to clear this provider
**Since:** 1.2

---

#### clear

public void clear()

Clears this provider so that it no longer contains the properties
used to look up facilities implemented by the provider.

If a security manager is enabled, its

checkSecurityAccess

method is called with the string

"clearProviderProperties."+name

(where

name

is the provider name) to see if it's ok to clear
this provider.

If a security manager is enabled, its

checkSecurityAccess

method is called with the string

"clearProviderProperties."+name

(where

name

is the provider name) to see if it's ok to clear
this provider.

load

```java
public void load​(
InputStream
inStream)
throws
IOException
```

Reads a property list (key and element pairs) from the input stream.

**Overrides:** load

in class

Properties
**Parameters:** inStream

- the input stream.
**Throws:** IOException

- if an error occurred when reading from the
input stream.
**See Also:** Properties.load(java.io.Reader)

---

#### load

public void load​(

InputStream

inStream)
throws

IOException

Reads a property list (key and element pairs) from the input stream.

putAll

```java
public void putAll​(
Map
<?,​?> t)
```

Copies all of the mappings from the specified Map to this provider.
These mappings will replace any properties that this provider had
for any of the keys currently in the specified Map.

**Specified by:** putAll

in interface

Map

<

Object

,​

Object

>
**Overrides:** putAll

in class

Hashtable

<

Object

,​

Object

>
**Parameters:** t

- mappings to be stored in this map
**Since:** 1.2

---

#### putAll

public void putAll​(

Map

<?,​?> t)

Copies all of the mappings from the specified Map to this provider.
These mappings will replace any properties that this provider had
for any of the keys currently in the specified Map.

entrySet

```java
public
Set
<
Map.Entry
<
Object
,​
Object
>> entrySet()
```

Returns an unmodifiable Set view of the property entries contained
in this Provider.

**Specified by:** entrySet

in interface

Map

<

Object

,​

Object

>
**Overrides:** entrySet

in class

Hashtable

<

Object

,​

Object

>
**Returns:** a set view of the mappings contained in this map
**Since:** 1.2
**See Also:** Map.Entry

---

#### entrySet

public

Set

<

Map.Entry

<

Object

,​

Object

>> entrySet()

Returns an unmodifiable Set view of the property entries contained
in this Provider.

keySet

```java
public
Set
<
Object
> keySet()
```

Returns an unmodifiable Set view of the property keys contained in
this provider.

**Specified by:** keySet

in interface

Map

<

Object

,​

Object

>
**Overrides:** keySet

in class

Hashtable

<

Object

,​

Object

>
**Returns:** a set view of the keys contained in this map
**Since:** 1.2

---

#### keySet

public

Set

<

Object

> keySet()

Returns an unmodifiable Set view of the property keys contained in
this provider.

values

```java
public
Collection
<
Object
> values()
```

Returns an unmodifiable Collection view of the property values
contained in this provider.

**Specified by:** values

in interface

Map

<

Object

,​

Object

>
**Overrides:** values

in class

Hashtable

<

Object

,​

Object

>
**Returns:** a collection view of the values contained in this map
**Since:** 1.2

---

#### values

public

Collection

<

Object

> values()

Returns an unmodifiable Collection view of the property values
contained in this provider.

put

```java
public
Object
put​(
Object
key,

Object
value)
```

Sets the

key

property to have the specified

value

.

If a security manager is enabled, its

checkSecurityAccess

method is called with the string

"putProviderProperty."+name

,
where

name

is the provider name, to see if it's ok to set this
provider's property values.

**Specified by:** put

in interface

Map

<

Object

,​

Object

>
**Overrides:** put

in class

Hashtable

<

Object

,​

Object

>
**Parameters:** key

- the hashtable key
**Parameters:** value

- the value
**Returns:** the previous value of the specified key in this hashtable,
or

null

if it did not have one
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to set property values.
**Since:** 1.2
**See Also:** Object.equals(Object)

,

Hashtable.get(Object)

---

#### put

public

Object

put​(

Object

key,

Object

value)

Sets the

key

property to have the specified

value

.

If a security manager is enabled, its

checkSecurityAccess

method is called with the string

"putProviderProperty."+name

,
where

name

is the provider name, to see if it's ok to set this
provider's property values.

If a security manager is enabled, its

checkSecurityAccess

method is called with the string

"putProviderProperty."+name

,
where

name

is the provider name, to see if it's ok to set this
provider's property values.

putIfAbsent

```java
public
Object
putIfAbsent​(
Object
key,

Object
value)
```

If the specified key is not already associated with a value (or is mapped
to

null

) associates it with the given value and returns

null

, else returns the current value.

If a security manager is enabled, its

checkSecurityAccess

method is called with the string

"putProviderProperty."+name

,
where

name

is the provider name, to see if it's ok to set this
provider's property values.

**Parameters:** key

- key with which the specified value is to be associated
**Parameters:** value

- value to be associated with the specified key
**Returns:** the previous value associated with the specified key, or

null

if there was no mapping for the key.
(A

null

return can also indicate that the map
previously associated

null

with the key,
if the implementation supports null values.)
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to set property values.
**Since:** 1.8

---

#### putIfAbsent

public

Object

putIfAbsent​(

Object

key,

Object

value)

If the specified key is not already associated with a value (or is mapped
to

null

) associates it with the given value and returns

null

, else returns the current value.

If a security manager is enabled, its

checkSecurityAccess

method is called with the string

"putProviderProperty."+name

,
where

name

is the provider name, to see if it's ok to set this
provider's property values.

If a security manager is enabled, its

checkSecurityAccess

method is called with the string

"putProviderProperty."+name

,
where

name

is the provider name, to see if it's ok to set this
provider's property values.

remove

```java
public
Object
remove​(
Object
key)
```

Removes the

key

property (and its corresponding

value

).

If a security manager is enabled, its

checkSecurityAccess

method is called with the string

"removeProviderProperty."+name

,
where

name

is the provider name, to see if it's ok to remove this
provider's properties.

**Specified by:** remove

in interface

Map

<

Object

,​

Object

>
**Overrides:** remove

in class

Hashtable

<

Object

,​

Object

>
**Parameters:** key

- the key that needs to be removed
**Returns:** the value to which the key had been mapped in this hashtable,
or

null

if the key did not have a mapping
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to remove this provider's properties.
**Since:** 1.2

---

#### remove

public

Object

remove​(

Object

key)

Removes the

key

property (and its corresponding

value

).

If a security manager is enabled, its

checkSecurityAccess

method is called with the string

"removeProviderProperty."+name

,
where

name

is the provider name, to see if it's ok to remove this
provider's properties.

If a security manager is enabled, its

checkSecurityAccess

method is called with the string

"removeProviderProperty."+name

,
where

name

is the provider name, to see if it's ok to remove this
provider's properties.

remove

```java
public boolean remove​(
Object
key,

Object
value)
```

Removes the entry for the specified key only if it is currently
mapped to the specified value.

If a security manager is enabled, its

checkSecurityAccess

method is called with the string

"removeProviderProperty."+name

,
where

name

is the provider name, to see if it's ok to remove this
provider's properties.

**Parameters:** key

- key with which the specified value is associated
**Parameters:** value

- value expected to be associated with the specified key
**Returns:** true

if the value was removed
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to remove this provider's properties.
**Since:** 1.8

---

#### remove

public boolean remove​(

Object

key,

Object

value)

Removes the entry for the specified key only if it is currently
mapped to the specified value.

If a security manager is enabled, its

checkSecurityAccess

method is called with the string

"removeProviderProperty."+name

,
where

name

is the provider name, to see if it's ok to remove this
provider's properties.

If a security manager is enabled, its

checkSecurityAccess

method is called with the string

"removeProviderProperty."+name

,
where

name

is the provider name, to see if it's ok to remove this
provider's properties.

replace

```java
public boolean replace​(
Object
key,

Object
oldValue,

Object
newValue)
```

Replaces the entry for the specified key only if currently
mapped to the specified value.

If a security manager is enabled, its

checkSecurityAccess

method is called with the string

"putProviderProperty."+name

,
where

name

is the provider name, to see if it's ok to set this
provider's property values.

**Parameters:** key

- key with which the specified value is associated
**Parameters:** oldValue

- value expected to be associated with the specified key
**Parameters:** newValue

- value to be associated with the specified key
**Returns:** true

if the value was replaced
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to set property values.
**Since:** 1.8

---

#### replace

public boolean replace​(

Object

key,

Object

oldValue,

Object

newValue)

Replaces the entry for the specified key only if currently
mapped to the specified value.

If a security manager is enabled, its

checkSecurityAccess

method is called with the string

"putProviderProperty."+name

,
where

name

is the provider name, to see if it's ok to set this
provider's property values.

If a security manager is enabled, its

checkSecurityAccess

method is called with the string

"putProviderProperty."+name

,
where

name

is the provider name, to see if it's ok to set this
provider's property values.

replace

```java
public
Object
replace​(
Object
key,

Object
value)
```

Replaces the entry for the specified key only if it is
currently mapped to some value.

If a security manager is enabled, its

checkSecurityAccess

method is called with the string

"putProviderProperty."+name

,
where

name

is the provider name, to see if it's ok to set this
provider's property values.

**Parameters:** key

- key with which the specified value is associated
**Parameters:** value

- value to be associated with the specified key
**Returns:** the previous value associated with the specified key, or

null

if there was no mapping for the key.
(A

null

return can also indicate that the map
previously associated

null

with the key,
if the implementation supports null values.)
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to set property values.
**Since:** 1.8

---

#### replace

public

Object

replace​(

Object

key,

Object

value)

Replaces the entry for the specified key only if it is
currently mapped to some value.

If a security manager is enabled, its

checkSecurityAccess

method is called with the string

"putProviderProperty."+name

,
where

name

is the provider name, to see if it's ok to set this
provider's property values.

If a security manager is enabled, its

checkSecurityAccess

method is called with the string

"putProviderProperty."+name

,
where

name

is the provider name, to see if it's ok to set this
provider's property values.

replaceAll

```java
public void replaceAll​(
BiFunction
<? super
Object
,​? super
Object
,​? extends
Object
> function)
```

Replaces each entry's value with the result of invoking the given
function on that entry, in the order entries are returned by an entry
set iterator, until all entries have been processed or the function
throws an exception.

If a security manager is enabled, its

checkSecurityAccess

method is called with the string

"putProviderProperty."+name

,
where

name

is the provider name, to see if it's ok to set this
provider's property values.

**Parameters:** function

- the function to apply to each entry
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to set property values.
**Since:** 1.8

---

#### replaceAll

public void replaceAll​(

BiFunction

<? super

Object

,​? super

Object

,​? extends

Object

> function)

Replaces each entry's value with the result of invoking the given
function on that entry, in the order entries are returned by an entry
set iterator, until all entries have been processed or the function
throws an exception.

If a security manager is enabled, its

checkSecurityAccess

method is called with the string

"putProviderProperty."+name

,
where

name

is the provider name, to see if it's ok to set this
provider's property values.

If a security manager is enabled, its

checkSecurityAccess

method is called with the string

"putProviderProperty."+name

,
where

name

is the provider name, to see if it's ok to set this
provider's property values.

compute

```java
public
Object
compute​(
Object
key,

BiFunction
<? super
Object
,​? super
Object
,​? extends
Object
> remappingFunction)
```

Attempts to compute a mapping for the specified key and its
current mapped value (or

null

if there is no current
mapping).

If a security manager is enabled, its

checkSecurityAccess

method is called with the strings

"putProviderProperty."+name

and

"removeProviderProperty."+name

, where

name

is the
provider name, to see if it's ok to set this provider's property values
and remove this provider's properties.

**Specified by:** compute

in interface

Map

<

Object

,​

Object

>
**Overrides:** compute

in class

Hashtable

<

Object

,​

Object

>
**Parameters:** key

- key with which the specified value is to be associated
**Parameters:** remappingFunction

- the remapping function to compute a value
**Returns:** the new value associated with the specified key, or null if none
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to set property values or remove properties.
**Since:** 1.8

---

#### compute

public

Object

compute​(

Object

key,

BiFunction

<? super

Object

,​? super

Object

,​? extends

Object

> remappingFunction)

Attempts to compute a mapping for the specified key and its
current mapped value (or

null

if there is no current
mapping).

If a security manager is enabled, its

checkSecurityAccess

method is called with the strings

"putProviderProperty."+name

and

"removeProviderProperty."+name

, where

name

is the
provider name, to see if it's ok to set this provider's property values
and remove this provider's properties.

If a security manager is enabled, its

checkSecurityAccess

method is called with the strings

"putProviderProperty."+name

and

"removeProviderProperty."+name

, where

name

is the
provider name, to see if it's ok to set this provider's property values
and remove this provider's properties.

computeIfAbsent

```java
public
Object
computeIfAbsent​(
Object
key,

Function
<? super
Object
,​? extends
Object
> mappingFunction)
```

If the specified key is not already associated with a value (or
is mapped to

null

), attempts to compute its value using
the given mapping function and enters it into this map unless

null

.

If a security manager is enabled, its

checkSecurityAccess

method is called with the strings

"putProviderProperty."+name

and

"removeProviderProperty."+name

, where

name

is the
provider name, to see if it's ok to set this provider's property values
and remove this provider's properties.

**Specified by:** computeIfAbsent

in interface

Map

<

Object

,​

Object

>
**Overrides:** computeIfAbsent

in class

Hashtable

<

Object

,​

Object

>
**Parameters:** key

- key with which the specified value is to be associated
**Parameters:** mappingFunction

- the mapping function to compute a value
**Returns:** the current (existing or computed) value associated with
the specified key, or null if the computed value is null
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to set property values and remove properties.
**Since:** 1.8

---

#### computeIfAbsent

public

Object

computeIfAbsent​(

Object

key,

Function

<? super

Object

,​? extends

Object

> mappingFunction)

If the specified key is not already associated with a value (or
is mapped to

null

), attempts to compute its value using
the given mapping function and enters it into this map unless

null

.

If a security manager is enabled, its

checkSecurityAccess

method is called with the strings

"putProviderProperty."+name

and

"removeProviderProperty."+name

, where

name

is the
provider name, to see if it's ok to set this provider's property values
and remove this provider's properties.

If a security manager is enabled, its

checkSecurityAccess

method is called with the strings

"putProviderProperty."+name

and

"removeProviderProperty."+name

, where

name

is the
provider name, to see if it's ok to set this provider's property values
and remove this provider's properties.

computeIfPresent

```java
public
Object
computeIfPresent​(
Object
key,

BiFunction
<? super
Object
,​? super
Object
,​? extends
Object
> remappingFunction)
```

If the value for the specified key is present and non-null, attempts to
compute a new mapping given the key and its current mapped value.

If a security manager is enabled, its

checkSecurityAccess

method is called with the strings

"putProviderProperty."+name

and

"removeProviderProperty."+name

, where

name

is the
provider name, to see if it's ok to set this provider's property values
and remove this provider's properties.

**Specified by:** computeIfPresent

in interface

Map

<

Object

,​

Object

>
**Overrides:** computeIfPresent

in class

Hashtable

<

Object

,​

Object

>
**Parameters:** key

- key with which the specified value is to be associated
**Parameters:** remappingFunction

- the remapping function to compute a value
**Returns:** the new value associated with the specified key, or null if none
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to set property values or remove properties.
**Since:** 1.8

---

#### computeIfPresent

public

Object

computeIfPresent​(

Object

key,

BiFunction

<? super

Object

,​? super

Object

,​? extends

Object

> remappingFunction)

If the value for the specified key is present and non-null, attempts to
compute a new mapping given the key and its current mapped value.

If a security manager is enabled, its

checkSecurityAccess

method is called with the strings

"putProviderProperty."+name

and

"removeProviderProperty."+name

, where

name

is the
provider name, to see if it's ok to set this provider's property values
and remove this provider's properties.

If a security manager is enabled, its

checkSecurityAccess

method is called with the strings

"putProviderProperty."+name

and

"removeProviderProperty."+name

, where

name

is the
provider name, to see if it's ok to set this provider's property values
and remove this provider's properties.

merge

```java
public
Object
merge​(
Object
key,

Object
value,

BiFunction
<? super
Object
,​? super
Object
,​? extends
Object
> remappingFunction)
```

If the specified key is not already associated with a value or is
associated with null, associates it with the given value. Otherwise,
replaces the value with the results of the given remapping function,
or removes if the result is null. This method may be of use when
combining multiple mapped values for a key.

If a security manager is enabled, its

checkSecurityAccess

method is called with the strings

"putProviderProperty."+name

and

"removeProviderProperty."+name

, where

name

is the
provider name, to see if it's ok to set this provider's property values
and remove this provider's properties.

**Specified by:** merge

in interface

Map

<

Object

,​

Object

>
**Overrides:** merge

in class

Hashtable

<

Object

,​

Object

>
**Parameters:** key

- key with which the resulting value is to be associated
**Parameters:** value

- the non-null value to be merged with the existing value
associated with the key or, if no existing value or a null value
is associated with the key, to be associated with the key
**Parameters:** remappingFunction

- the remapping function to recompute a value if
present
**Returns:** the new value associated with the specified key, or null if no
value is associated with the key
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method
denies access to set property values or remove properties.
**Since:** 1.8

---

#### merge

public

Object

merge​(

Object

key,

Object

value,

BiFunction

<? super

Object

,​? super

Object

,​? extends

Object

> remappingFunction)

If the specified key is not already associated with a value or is
associated with null, associates it with the given value. Otherwise,
replaces the value with the results of the given remapping function,
or removes if the result is null. This method may be of use when
combining multiple mapped values for a key.

If a security manager is enabled, its

checkSecurityAccess

method is called with the strings

"putProviderProperty."+name

and

"removeProviderProperty."+name

, where

name

is the
provider name, to see if it's ok to set this provider's property values
and remove this provider's properties.

If a security manager is enabled, its

checkSecurityAccess

method is called with the strings

"putProviderProperty."+name

and

"removeProviderProperty."+name

, where

name

is the
provider name, to see if it's ok to set this provider's property values
and remove this provider's properties.

getOrDefault

```java
public
Object
getOrDefault​(
Object
key,

Object
defaultValue)
```

Description copied from interface:

Map

Returns the value to which the specified key is mapped, or

defaultValue

if this map contains no mapping for the key.

**Parameters:** key

- the key whose associated value is to be returned
**Parameters:** defaultValue

- the default mapping of the key
**Returns:** the value to which the specified key is mapped, or

defaultValue

if this map contains no mapping for the key
**Since:** 1.8

---

#### getOrDefault

public

Object

getOrDefault​(

Object

key,

Object

defaultValue)

Description copied from interface:

Map

Returns the value to which the specified key is mapped, or

defaultValue

if this map contains no mapping for the key.

forEach

```java
public void forEach​(
BiConsumer
<? super
Object
,​? super
Object
> action)
```

Description copied from interface:

Map

Performs the given action for each entry in this map until all entries
have been processed or the action throws an exception. Unless
otherwise specified by the implementing class, actions are performed in
the order of entry set iteration (if an iteration order is specified.)
Exceptions thrown by the action are relayed to the caller.

**Parameters:** action

- The action to be performed for each entry
**Since:** 1.8

---

#### forEach

public void forEach​(

BiConsumer

<? super

Object

,​? super

Object

> action)

Description copied from interface:

Map

Performs the given action for each entry in this map until all entries
have been processed or the action throws an exception. Unless
otherwise specified by the implementing class, actions are performed in
the order of entry set iteration (if an iteration order is specified.)
Exceptions thrown by the action are relayed to the caller.

getService

```java
public
Provider.Service
getService​(
String
type,

String
algorithm)
```

Get the service describing this Provider's implementation of the
specified type of this algorithm or alias. If no such
implementation exists, this method returns null. If there are two
matching services, one added to this provider using

putService()

and one added via

put()

,
the service added via

putService()

is returned.

**Parameters:** type

- the type of

service

requested
(for example,

MessageDigest

)
**Parameters:** algorithm

- the case insensitive algorithm name (or alternate
alias) of the service requested (for example,

SHA-1

)
**Returns:** the service describing this Provider's matching service
or null if no such service exists
**Throws:** NullPointerException

- if type or algorithm is null
**Since:** 1.5

---

#### getService

public

Provider.Service

getService​(

String

type,

String

algorithm)

Get the service describing this Provider's implementation of the
specified type of this algorithm or alias. If no such
implementation exists, this method returns null. If there are two
matching services, one added to this provider using

putService()

and one added via

put()

,
the service added via

putService()

is returned.

getServices

```java
public
Set
<
Provider.Service
> getServices()
```

Get an unmodifiable Set of all services supported by
this Provider.

**Returns:** an unmodifiable Set of all services supported by
this Provider
**Since:** 1.5

---

#### getServices

public

Set

<

Provider.Service

> getServices()

Get an unmodifiable Set of all services supported by
this Provider.

putService

```java
protected void putService​(
Provider.Service
s)
```

Add a service. If a service of the same type with the same algorithm
name exists and it was added using

putService()

,
it is replaced by the new service.
This method also places information about this service
in the provider's Hashtable values in the format described in the

Java Cryptography Architecture (JCA) Reference Guide

.

Also, if there is a security manager, its

checkSecurityAccess

method is called with the string

"putProviderProperty."+name

, where

name

is
the provider name, to see if it's ok to set this provider's property
values. If the default implementation of

checkSecurityAccess

is used (that is, that method is not overriden), then this results in
a call to the security manager's

checkPermission

method with
a

SecurityPermission("putProviderProperty."+name)

permission.

**Parameters:** s

- the Service to add
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method denies
access to set property values.
**Throws:** NullPointerException

- if s is null
**Since:** 1.5

---

#### putService

protected void putService​(

Provider.Service

s)

Add a service. If a service of the same type with the same algorithm
name exists and it was added using

putService()

,
it is replaced by the new service.
This method also places information about this service
in the provider's Hashtable values in the format described in the

Java Cryptography Architecture (JCA) Reference Guide

.

Also, if there is a security manager, its

checkSecurityAccess

method is called with the string

"putProviderProperty."+name

, where

name

is
the provider name, to see if it's ok to set this provider's property
values. If the default implementation of

checkSecurityAccess

is used (that is, that method is not overriden), then this results in
a call to the security manager's

checkPermission

method with
a

SecurityPermission("putProviderProperty."+name)

permission.

Also, if there is a security manager, its

checkSecurityAccess

method is called with the string

"putProviderProperty."+name

, where

name

is
the provider name, to see if it's ok to set this provider's property
values. If the default implementation of

checkSecurityAccess

is used (that is, that method is not overriden), then this results in
a call to the security manager's

checkPermission

method with
a

SecurityPermission("putProviderProperty."+name)

permission.

removeService

```java
protected void removeService​(
Provider.Service
s)
```

Remove a service previously added using

putService()

. The specified service is removed from
this provider. It will no longer be returned by

getService()

and its information will be removed
from this provider's Hashtable.

Also, if there is a security manager, its

checkSecurityAccess

method is called with the string

"removeProviderProperty."+name

, where

name

is
the provider name, to see if it's ok to remove this provider's
properties. If the default implementation of

checkSecurityAccess

is used (that is, that method is not
overriden), then this results in a call to the security manager's

checkPermission

method with a

SecurityPermission("removeProviderProperty."+name)

permission.

**Parameters:** s

- the Service to be removed
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkSecurityAccess(java.lang.String)

method denies
access to remove this provider's properties.
**Throws:** NullPointerException

- if s is null
**Since:** 1.5

---

#### removeService

protected void removeService​(

Provider.Service

s)

Remove a service previously added using

putService()

. The specified service is removed from
this provider. It will no longer be returned by

getService()

and its information will be removed
from this provider's Hashtable.

Also, if there is a security manager, its

checkSecurityAccess

method is called with the string

"removeProviderProperty."+name

, where

name

is
the provider name, to see if it's ok to remove this provider's
properties. If the default implementation of

checkSecurityAccess

is used (that is, that method is not
overriden), then this results in a call to the security manager's

checkPermission

method with a

SecurityPermission("removeProviderProperty."+name)

permission.

Also, if there is a security manager, its

checkSecurityAccess

method is called with the string

"removeProviderProperty."+name

, where

name

is
the provider name, to see if it's ok to remove this provider's
properties. If the default implementation of

checkSecurityAccess

is used (that is, that method is not
overriden), then this results in a call to the security manager's

checkPermission

method with a

SecurityPermission("removeProviderProperty."+name)

permission.

---

