# Class DomainLoadStoreParameter

**Source:** `java.base\java\security\DomainLoadStoreParameter.html`

### Class Description

```java
public final class
DomainLoadStoreParameter

extends
Object

implements
KeyStore.LoadStoreParameter
```

Configuration data that specifies the keystores in a keystore domain.
A keystore domain is a collection of keystores that are presented as a
single logical keystore. The configuration data is used during

KeyStore

load

and

store

operations.

The following syntax is supported for configuration data:

```java
domain <domainName> [<property> ...] {
keystore <keystoreName> [<property> ...] ;
...
};
...
```

where

domainName

and

keystoreName

are identifiers
and

property

is a key/value pairing. The key and value are
separated by an 'equals' symbol and the value is enclosed in double
quotes. A property value may be either a printable string or a binary
string of colon-separated pairs of hexadecimal digits. Multi-valued
properties are represented as a comma-separated list of values,
enclosed in square brackets.
See

Arrays.toString(java.lang.Object[])

.

To ensure that keystore entries are uniquely identified, each
entry's alias is prefixed by its

keystoreName

followed
by the entry name separator and each

keystoreName

must be
unique within its domain. Entry name prefixes are omitted when
storing a keystore.

Properties are context-sensitive: properties that apply to
all the keystores in a domain are located in the domain clause,
and properties that apply only to a specific keystore are located
in that keystore's clause.
Unless otherwise specified, a property in a keystore clause overrides
a property of the same name in the domain clause. All property names
are case-insensitive. The following properties are supported:

**keystoreType="<type>":** The keystore type.
**keystoreURI="<url>":** The keystore location.
**keystoreProviderName="<name>":** The name of the keystore's JCE provider.
**keystorePasswordEnv="<environment-variable>":** The environment variable that stores a keystore password.
Alternatively, passwords may be supplied to the constructor
method in a

Map<String, ProtectionParameter>

.
**entryNameSeparator="<separator>":** The separator between a keystore name prefix and an entry name.
When specified, it applies to all the entries in a domain.
Its default value is a space.

For example, configuration data for a simple keystore domain
comprising three keystores is shown below:

```java
domain app1 {
keystore app1-truststore
keystoreURI="file:///app1/etc/truststore.jks";

keystore system-truststore
keystoreURI="${java.home}/lib/security/cacerts";

keystore app1-keystore
keystoreType="PKCS12"
keystoreURI="file:///app1/etc/keystore.p12";
};
```

**All Implemented Interfaces:** KeyStore.LoadStoreParameter

---

### Field Details

*No entries found.*

### Constructor Details

#### public DomainLoadStoreParameter​(
URI
configuration,

Map
<
String
,​
KeyStore.ProtectionParameter
> protectionParams)

Constructs a DomainLoadStoreParameter for a keystore domain with
the parameters used to protect keystore data.

**Parameters:**
- configuration

- identifier for the domain configuration data.
The name of the target domain should be specified in the

java.net.URI

fragment component when it is necessary
to distinguish between several domain configurations at the
same location.
- protectionParams

- the map from keystore name to the parameter
used to protect keystore data.
A

java.util.Collections.EMPTY_MAP

should be used
when protection parameters are not required or when they have
been specified by properties in the domain configuration data.
It is cloned to prevent subsequent modification.

**Throws:**
- NullPointerException

- if

configuration

or

protectionParams

is

null

---

### Method Details

#### public
URI
getConfiguration()

Gets the identifier for the domain configuration data.

**Returns:**
- the identifier for the configuration data

---

#### public
Map
<
String
,​
KeyStore.ProtectionParameter
> getProtectionParams()

Gets the keystore protection parameters for keystores in this
domain.

**Returns:**
- an unmodifiable map of keystore names to protection
parameters

---

#### public
KeyStore.ProtectionParameter
getProtectionParameter()

Gets the keystore protection parameters for this domain.
Keystore domains do not support a protection parameter.

**Specified by:**
- getProtectionParameter

in interface

KeyStore.LoadStoreParameter

**Returns:**
- always returns

null

---

### Additional Sections

#### Class DomainLoadStoreParameter

java.lang.Object

- java.security.DomainLoadStoreParameter

java.security.DomainLoadStoreParameter

**All Implemented Interfaces:** KeyStore.LoadStoreParameter

```java
public final class
DomainLoadStoreParameter

extends
Object

implements
KeyStore.LoadStoreParameter
```

Configuration data that specifies the keystores in a keystore domain.
A keystore domain is a collection of keystores that are presented as a
single logical keystore. The configuration data is used during

KeyStore

load

and

store

operations.

The following syntax is supported for configuration data:

```java
domain <domainName> [<property> ...] {
keystore <keystoreName> [<property> ...] ;
...
};
...
```

where

domainName

and

keystoreName

are identifiers
and

property

is a key/value pairing. The key and value are
separated by an 'equals' symbol and the value is enclosed in double
quotes. A property value may be either a printable string or a binary
string of colon-separated pairs of hexadecimal digits. Multi-valued
properties are represented as a comma-separated list of values,
enclosed in square brackets.
See

Arrays.toString(java.lang.Object[])

.

To ensure that keystore entries are uniquely identified, each
entry's alias is prefixed by its

keystoreName

followed
by the entry name separator and each

keystoreName

must be
unique within its domain. Entry name prefixes are omitted when
storing a keystore.

Properties are context-sensitive: properties that apply to
all the keystores in a domain are located in the domain clause,
and properties that apply only to a specific keystore are located
in that keystore's clause.
Unless otherwise specified, a property in a keystore clause overrides
a property of the same name in the domain clause. All property names
are case-insensitive. The following properties are supported:

**keystoreType="<type>":** The keystore type.
**keystoreURI="<url>":** The keystore location.
**keystoreProviderName="<name>":** The name of the keystore's JCE provider.
**keystorePasswordEnv="<environment-variable>":** The environment variable that stores a keystore password.
Alternatively, passwords may be supplied to the constructor
method in a

Map<String, ProtectionParameter>

.
**entryNameSeparator="<separator>":** The separator between a keystore name prefix and an entry name.
When specified, it applies to all the entries in a domain.
Its default value is a space.

For example, configuration data for a simple keystore domain
comprising three keystores is shown below:

```java
domain app1 {
keystore app1-truststore
keystoreURI="file:///app1/etc/truststore.jks";

keystore system-truststore
keystoreURI="${java.home}/lib/security/cacerts";

keystore app1-keystore
keystoreType="PKCS12"
keystoreURI="file:///app1/etc/keystore.p12";
};
```

**Since:** 1.8

public final class

DomainLoadStoreParameter

extends

Object

implements

KeyStore.LoadStoreParameter

Configuration data that specifies the keystores in a keystore domain.
A keystore domain is a collection of keystores that are presented as a
single logical keystore. The configuration data is used during

KeyStore

load

and

store

operations.

The following syntax is supported for configuration data:

```java
domain <domainName> [<property> ...] {
keystore <keystoreName> [<property> ...] ;
...
};
...
```

where

domainName

and

keystoreName

are identifiers
and

property

is a key/value pairing. The key and value are
separated by an 'equals' symbol and the value is enclosed in double
quotes. A property value may be either a printable string or a binary
string of colon-separated pairs of hexadecimal digits. Multi-valued
properties are represented as a comma-separated list of values,
enclosed in square brackets.
See

Arrays.toString(java.lang.Object[])

.

To ensure that keystore entries are uniquely identified, each
entry's alias is prefixed by its

keystoreName

followed
by the entry name separator and each

keystoreName

must be
unique within its domain. Entry name prefixes are omitted when
storing a keystore.

Properties are context-sensitive: properties that apply to
all the keystores in a domain are located in the domain clause,
and properties that apply only to a specific keystore are located
in that keystore's clause.
Unless otherwise specified, a property in a keystore clause overrides
a property of the same name in the domain clause. All property names
are case-insensitive. The following properties are supported:

**keystoreType="<type>":** The keystore type.
**keystoreURI="<url>":** The keystore location.
**keystoreProviderName="<name>":** The name of the keystore's JCE provider.
**keystorePasswordEnv="<environment-variable>":** The environment variable that stores a keystore password.
Alternatively, passwords may be supplied to the constructor
method in a

Map<String, ProtectionParameter>

.
**entryNameSeparator="<separator>":** The separator between a keystore name prefix and an entry name.
When specified, it applies to all the entries in a domain.
Its default value is a space.

For example, configuration data for a simple keystore domain
comprising three keystores is shown below:

```java
domain app1 {
keystore app1-truststore
keystoreURI="file:///app1/etc/truststore.jks";

keystore system-truststore
keystoreURI="${java.home}/lib/security/cacerts";

keystore app1-keystore
keystoreType="PKCS12"
keystoreURI="file:///app1/etc/keystore.p12";
};
```

The following syntax is supported for configuration data:

```java
domain <domainName> [<property> ...] {
keystore <keystoreName> [<property> ...] ;
...
};
...
```

where

domainName

and

keystoreName

are identifiers
and

property

is a key/value pairing. The key and value are
separated by an 'equals' symbol and the value is enclosed in double
quotes. A property value may be either a printable string or a binary
string of colon-separated pairs of hexadecimal digits. Multi-valued
properties are represented as a comma-separated list of values,
enclosed in square brackets.
See

Arrays.toString(java.lang.Object[])

.

To ensure that keystore entries are uniquely identified, each
entry's alias is prefixed by its

keystoreName

followed
by the entry name separator and each

keystoreName

must be
unique within its domain. Entry name prefixes are omitted when
storing a keystore.

Properties are context-sensitive: properties that apply to
all the keystores in a domain are located in the domain clause,
and properties that apply only to a specific keystore are located
in that keystore's clause.
Unless otherwise specified, a property in a keystore clause overrides
a property of the same name in the domain clause. All property names
are case-insensitive. The following properties are supported:

**keystoreType="<type>":** The keystore type.
**keystoreURI="<url>":** The keystore location.
**keystoreProviderName="<name>":** The name of the keystore's JCE provider.
**keystorePasswordEnv="<environment-variable>":** The environment variable that stores a keystore password.
Alternatively, passwords may be supplied to the constructor
method in a

Map<String, ProtectionParameter>

.
**entryNameSeparator="<separator>":** The separator between a keystore name prefix and an entry name.
When specified, it applies to all the entries in a domain.
Its default value is a space.

For example, configuration data for a simple keystore domain
comprising three keystores is shown below:

```java
domain app1 {
keystore app1-truststore
keystoreURI="file:///app1/etc/truststore.jks";

keystore system-truststore
keystoreURI="${java.home}/lib/security/cacerts";

keystore app1-keystore
keystoreType="PKCS12"
keystoreURI="file:///app1/etc/keystore.p12";
};
```

domain <domainName> [<property> ...] {
keystore <keystoreName> [<property> ...] ;
...
};
...

To ensure that keystore entries are uniquely identified, each
entry's alias is prefixed by its

keystoreName

followed
by the entry name separator and each

keystoreName

must be
unique within its domain. Entry name prefixes are omitted when
storing a keystore.

Properties are context-sensitive: properties that apply to
all the keystores in a domain are located in the domain clause,
and properties that apply only to a specific keystore are located
in that keystore's clause.
Unless otherwise specified, a property in a keystore clause overrides
a property of the same name in the domain clause. All property names
are case-insensitive. The following properties are supported:

**keystoreType="<type>":** The keystore type.
**keystoreURI="<url>":** The keystore location.
**keystoreProviderName="<name>":** The name of the keystore's JCE provider.
**keystorePasswordEnv="<environment-variable>":** The environment variable that stores a keystore password.
Alternatively, passwords may be supplied to the constructor
method in a

Map<String, ProtectionParameter>

.
**entryNameSeparator="<separator>":** The separator between a keystore name prefix and an entry name.
When specified, it applies to all the entries in a domain.
Its default value is a space.

For example, configuration data for a simple keystore domain
comprising three keystores is shown below:

```java
domain app1 {
keystore app1-truststore
keystoreURI="file:///app1/etc/truststore.jks";

keystore system-truststore
keystoreURI="${java.home}/lib/security/cacerts";

keystore app1-keystore
keystoreType="PKCS12"
keystoreURI="file:///app1/etc/keystore.p12";
};
```

Properties are context-sensitive: properties that apply to
all the keystores in a domain are located in the domain clause,
and properties that apply only to a specific keystore are located
in that keystore's clause.
Unless otherwise specified, a property in a keystore clause overrides
a property of the same name in the domain clause. All property names
are case-insensitive. The following properties are supported:

**keystoreType="<type>":** The keystore type.
**keystoreURI="<url>":** The keystore location.
**keystoreProviderName="<name>":** The name of the keystore's JCE provider.
**keystorePasswordEnv="<environment-variable>":** The environment variable that stores a keystore password.
Alternatively, passwords may be supplied to the constructor
method in a

Map<String, ProtectionParameter>

.
**entryNameSeparator="<separator>":** The separator between a keystore name prefix and an entry name.
When specified, it applies to all the entries in a domain.
Its default value is a space.

For example, configuration data for a simple keystore domain
comprising three keystores is shown below:

```java
domain app1 {
keystore app1-truststore
keystoreURI="file:///app1/etc/truststore.jks";

keystore system-truststore
keystoreURI="${java.home}/lib/security/cacerts";

keystore app1-keystore
keystoreType="PKCS12"
keystoreURI="file:///app1/etc/keystore.p12";
};
```

For example, configuration data for a simple keystore domain
comprising three keystores is shown below:

```java
domain app1 {
keystore app1-truststore
keystoreURI="file:///app1/etc/truststore.jks";

keystore system-truststore
keystoreURI="${java.home}/lib/security/cacerts";

keystore app1-keystore
keystoreType="PKCS12"
keystoreURI="file:///app1/etc/keystore.p12";
};
```

domain app1 {
keystore app1-truststore
keystoreURI="file:///app1/etc/truststore.jks";

keystore system-truststore
keystoreURI="${java.home}/lib/security/cacerts";

keystore app1-keystore
keystoreType="PKCS12"
keystoreURI="file:///app1/etc/keystore.p12";
};

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DomainLoadStoreParameter

​(

URI

configuration,

Map

<

String

,​

KeyStore.ProtectionParameter

> protectionParams)

Constructs a DomainLoadStoreParameter for a keystore domain with
the parameters used to protect keystore data.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

URI

getConfiguration

()

Gets the identifier for the domain configuration data.

KeyStore.ProtectionParameter

getProtectionParameter

()

Gets the keystore protection parameters for this domain.

Map

<

String

,​

KeyStore.ProtectionParameter

>

getProtectionParams

()

Gets the keystore protection parameters for keystores in this
domain.

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

DomainLoadStoreParameter

​(

URI

configuration,

Map

<

String

,​

KeyStore.ProtectionParameter

> protectionParams)

Constructs a DomainLoadStoreParameter for a keystore domain with
the parameters used to protect keystore data.

---

#### Constructor Summary

Constructs a DomainLoadStoreParameter for a keystore domain with
the parameters used to protect keystore data.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

URI

getConfiguration

()

Gets the identifier for the domain configuration data.

KeyStore.ProtectionParameter

getProtectionParameter

()

Gets the keystore protection parameters for this domain.

Map

<

String

,​

KeyStore.ProtectionParameter

>

getProtectionParams

()

Gets the keystore protection parameters for keystores in this
domain.

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

Gets the identifier for the domain configuration data.

Gets the keystore protection parameters for this domain.

Gets the keystore protection parameters for keystores in this
domain.

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

- DomainLoadStoreParameter

```java
public DomainLoadStoreParameter​(
URI
configuration,

Map
<
String
,​
KeyStore.ProtectionParameter
> protectionParams)
```

Constructs a DomainLoadStoreParameter for a keystore domain with
the parameters used to protect keystore data.

**Parameters:** configuration

- identifier for the domain configuration data.
The name of the target domain should be specified in the

java.net.URI

fragment component when it is necessary
to distinguish between several domain configurations at the
same location.
**Parameters:** protectionParams

- the map from keystore name to the parameter
used to protect keystore data.
A

java.util.Collections.EMPTY_MAP

should be used
when protection parameters are not required or when they have
been specified by properties in the domain configuration data.
It is cloned to prevent subsequent modification.
**Throws:** NullPointerException

- if

configuration

or

protectionParams

is

null

============ METHOD DETAIL ==========

- Method Detail

- getConfiguration

```java
public
URI
getConfiguration()
```

Gets the identifier for the domain configuration data.

**Returns:** the identifier for the configuration data

- getProtectionParams

```java
public
Map
<
String
,​
KeyStore.ProtectionParameter
> getProtectionParams()
```

Gets the keystore protection parameters for keystores in this
domain.

**Returns:** an unmodifiable map of keystore names to protection
parameters

- getProtectionParameter

```java
public
KeyStore.ProtectionParameter
getProtectionParameter()
```

Gets the keystore protection parameters for this domain.
Keystore domains do not support a protection parameter.

**Specified by:** getProtectionParameter

in interface

KeyStore.LoadStoreParameter
**Returns:** always returns

null

Constructor Detail

- DomainLoadStoreParameter

```java
public DomainLoadStoreParameter​(
URI
configuration,

Map
<
String
,​
KeyStore.ProtectionParameter
> protectionParams)
```

Constructs a DomainLoadStoreParameter for a keystore domain with
the parameters used to protect keystore data.

**Parameters:** configuration

- identifier for the domain configuration data.
The name of the target domain should be specified in the

java.net.URI

fragment component when it is necessary
to distinguish between several domain configurations at the
same location.
**Parameters:** protectionParams

- the map from keystore name to the parameter
used to protect keystore data.
A

java.util.Collections.EMPTY_MAP

should be used
when protection parameters are not required or when they have
been specified by properties in the domain configuration data.
It is cloned to prevent subsequent modification.
**Throws:** NullPointerException

- if

configuration

or

protectionParams

is

null

---

#### Constructor Detail

DomainLoadStoreParameter

```java
public DomainLoadStoreParameter​(
URI
configuration,

Map
<
String
,​
KeyStore.ProtectionParameter
> protectionParams)
```

Constructs a DomainLoadStoreParameter for a keystore domain with
the parameters used to protect keystore data.

**Parameters:** configuration

- identifier for the domain configuration data.
The name of the target domain should be specified in the

java.net.URI

fragment component when it is necessary
to distinguish between several domain configurations at the
same location.
**Parameters:** protectionParams

- the map from keystore name to the parameter
used to protect keystore data.
A

java.util.Collections.EMPTY_MAP

should be used
when protection parameters are not required or when they have
been specified by properties in the domain configuration data.
It is cloned to prevent subsequent modification.
**Throws:** NullPointerException

- if

configuration

or

protectionParams

is

null

---

#### DomainLoadStoreParameter

public DomainLoadStoreParameter​(

URI

configuration,

Map

<

String

,​

KeyStore.ProtectionParameter

> protectionParams)

Constructs a DomainLoadStoreParameter for a keystore domain with
the parameters used to protect keystore data.

Method Detail

- getConfiguration

```java
public
URI
getConfiguration()
```

Gets the identifier for the domain configuration data.

**Returns:** the identifier for the configuration data

- getProtectionParams

```java
public
Map
<
String
,​
KeyStore.ProtectionParameter
> getProtectionParams()
```

Gets the keystore protection parameters for keystores in this
domain.

**Returns:** an unmodifiable map of keystore names to protection
parameters

- getProtectionParameter

```java
public
KeyStore.ProtectionParameter
getProtectionParameter()
```

Gets the keystore protection parameters for this domain.
Keystore domains do not support a protection parameter.

**Specified by:** getProtectionParameter

in interface

KeyStore.LoadStoreParameter
**Returns:** always returns

null

---

#### Method Detail

getConfiguration

```java
public
URI
getConfiguration()
```

Gets the identifier for the domain configuration data.

**Returns:** the identifier for the configuration data

---

#### getConfiguration

public

URI

getConfiguration()

Gets the identifier for the domain configuration data.

getProtectionParams

```java
public
Map
<
String
,​
KeyStore.ProtectionParameter
> getProtectionParams()
```

Gets the keystore protection parameters for keystores in this
domain.

**Returns:** an unmodifiable map of keystore names to protection
parameters

---

#### getProtectionParams

public

Map

<

String

,​

KeyStore.ProtectionParameter

> getProtectionParams()

Gets the keystore protection parameters for keystores in this
domain.

getProtectionParameter

```java
public
KeyStore.ProtectionParameter
getProtectionParameter()
```

Gets the keystore protection parameters for this domain.
Keystore domains do not support a protection parameter.

**Specified by:** getProtectionParameter

in interface

KeyStore.LoadStoreParameter
**Returns:** always returns

null

---

#### getProtectionParameter

public

KeyStore.ProtectionParameter

getProtectionParameter()

Gets the keystore protection parameters for this domain.
Keystore domains do not support a protection parameter.

---

