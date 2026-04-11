# Class KeyInfoFactory

**Source:** `java.xml.crypto\javax\xml\crypto\dsig\keyinfo\KeyInfoFactory.html`

### Class Description

```java
public abstract class
KeyInfoFactory

extends
Object
```

A factory for creating

KeyInfo

objects from scratch or for
unmarshalling a

KeyInfo

object from a corresponding XML
representation.

Each instance of

KeyInfoFactory

supports a specific
XML mechanism type. To create a

KeyInfoFactory

, call one of the
static

getInstance

methods, passing in the XML
mechanism type desired, for example:

KeyInfoFactory factory = KeyInfoFactory.getInstance("DOM");

The objects that this factory produces will be based
on DOM and abide by the DOM interoperability requirements as defined in the

DOM Mechanism Requirements

section
of the API overview. See the

Java Security Standard Algorithm Names

document
for more information.

KeyInfoFactory

implementations are registered and loaded
using the

Provider

mechanism.
For example, a service provider that supports the
DOM mechanism would be specified in the

Provider

subclass as:

```java
put("KeyInfoFactory.DOM", "org.example.DOMKeyInfoFactory");
```

Also, the

XMLStructure

s that are created by this factory
may contain state specific to the

KeyInfo

and are not
intended to be reusable.

An implementation MUST minimally support the default mechanism type: DOM.

Note that a caller must use the same

KeyInfoFactory

instance to create the

XMLStructure

s of a particular

KeyInfo

object. The behavior is undefined if

XMLStructure

s from different providers or different mechanism
types are used together.

Concurrent Access

The static methods of this class are guaranteed to be thread-safe.
Multiple threads may concurrently invoke the static methods defined in this
class with no ill effects.

However, this is not true for the non-static methods defined by this
class. Unless otherwise documented by a specific provider, threads that
need to access a single

KeyInfoFactory

instance concurrently
should synchronize amongst themselves and provide the necessary locking.
Multiple threads each manipulating a different

KeyInfoFactory

instance need not synchronize.

**Since:** 1.6

---

### Field Details

*No entries found.*

### Constructor Details

#### protected KeyInfoFactory()

Default constructor, for invocation by subclasses.

---

### Method Details

#### public static
KeyInfoFactory
getInstance​(
String
mechanismType)

Returns a

KeyInfoFactory

that supports the
specified XML processing mechanism and representation type (ex: "DOM").

This method uses the standard JCA provider lookup mechanism to
locate and instantiate a

KeyInfoFactory

implementation of
the desired mechanism type. It traverses the list of registered security

Provider

s, starting with the most preferred

Provider

. A new

KeyInfoFactory

object
from the first

Provider

that supports the specified
mechanism is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:**
- mechanismType

- the type of the XML processing mechanism and
representation. See the

Java Security Standard Algorithm Names

document
for more information.

**Returns:**
- a new

KeyInfoFactory

**Throws:**
- NullPointerException

- if

mechanismType

is

null
- NoSuchMechanismException

- if no

Provider

supports a

KeyInfoFactory

implementation for the specified mechanism

**See Also:**
- Provider

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
KeyInfoFactory
getInstance​(
String
mechanismType,

Provider
provider)

Returns a

KeyInfoFactory

that supports the
requested XML processing mechanism and representation type (ex: "DOM"),
as supplied by the specified provider. Note that the specified

Provider

object does not have to be registered in the
provider list.

**Parameters:**
- mechanismType

- the type of the XML processing mechanism and
representation. See the

Java Security Standard Algorithm Names

document
for more information.
- provider

- the

Provider

object

**Returns:**
- a new

KeyInfoFactory

**Throws:**
- NullPointerException

- if

mechanismType

or

provider

are

null
- NoSuchMechanismException

- if a

KeyInfoFactory

implementation for the specified mechanism is not available from the
specified

Provider

object

**See Also:**
- Provider

---

#### public static
KeyInfoFactory
getInstance​(
String
mechanismType,

String
provider)
throws
NoSuchProviderException

Returns a

KeyInfoFactory

that supports the
requested XML processing mechanism and representation type (ex: "DOM"),
as supplied by the specified provider. The specified provider must be
registered in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:**
- mechanismType

- the type of the XML processing mechanism and
representation. See the

Java Security Standard Algorithm Names

document
for more information.
- provider

- the string name of the provider

**Returns:**
- a new

KeyInfoFactory

**Throws:**
- NoSuchProviderException

- if the specified provider is not
registered in the security provider list
- NullPointerException

- if

mechanismType

or

provider

are

null
- NoSuchMechanismException

- if a

KeyInfoFactory

implementation for the specified mechanism is not available from the
specified provider

**See Also:**
- Provider

---

#### public static
KeyInfoFactory
getInstance()

Returns a

KeyInfoFactory

that supports the
default XML processing mechanism and representation type ("DOM").

This method uses the standard JCA provider lookup mechanism to
locate and instantiate a

KeyInfoFactory

implementation of
the default mechanism type. It traverses the list of registered security

Provider

s, starting with the most preferred

Provider

. A new

KeyInfoFactory

object
from the first

Provider

that supports the DOM mechanism is
returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Returns:**
- a new

KeyInfoFactory

**Throws:**
- NoSuchMechanismException

- if no

Provider

supports a

KeyInfoFactory

implementation for the DOM mechanism

**See Also:**
- Provider

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

#### public final
String
getMechanismType()

Returns the type of the XML processing mechanism and representation
supported by this

KeyInfoFactory

(ex: "DOM")

**Returns:**
- the XML processing mechanism type supported by this

KeyInfoFactory

---

#### public final
Provider
getProvider()

Returns the provider of this

KeyInfoFactory

.

**Returns:**
- the provider of this

KeyInfoFactory

---

#### public abstract
KeyInfo
newKeyInfo​(
List
<? extends
XMLStructure
> content)

Creates a

KeyInfo

containing the specified list of
key information types.

**Parameters:**
- content

- a list of one or more

XMLStructure

s representing
key information types. The list is defensively copied to protect
against subsequent modification.

**Returns:**
- a

KeyInfo

**Throws:**
- NullPointerException

- if

content

is

null
- IllegalArgumentException

- if

content

is empty
- ClassCastException

- if

content

contains any entries
that are not of type

XMLStructure

---

#### public abstract
KeyInfo
newKeyInfo​(
List
<? extends
XMLStructure
> content,

String
id)

Creates a

KeyInfo

containing the specified list of key
information types and optional id. The

id

parameter represents the value of an XML

ID

attribute and is useful for referencing
the

KeyInfo

from other XML structures.

**Parameters:**
- content

- a list of one or more

XMLStructure

s representing
key information types. The list is defensively copied to protect
against subsequent modification.
- id

- the value of an XML

ID

(may be

null

)

**Returns:**
- a

KeyInfo

**Throws:**
- NullPointerException

- if

content

is

null
- IllegalArgumentException

- if

content

is empty
- ClassCastException

- if

content

contains any entries
that are not of type

XMLStructure

---

#### public abstract
KeyName
newKeyName​(
String
name)

Creates a

KeyName

from the specified name.

**Parameters:**
- name

- the name that identifies the key

**Returns:**
- a

KeyName

**Throws:**
- NullPointerException

- if

name

is

null

---

#### public abstract
KeyValue
newKeyValue​(
PublicKey
key)
throws
KeyException

Creates a

KeyValue

from the specified public key.

**Parameters:**
- key

- the public key

**Returns:**
- a

KeyValue

**Throws:**
- KeyException

- if the

key

's algorithm is not
recognized or supported by this

KeyInfoFactory
- NullPointerException

- if

key

is

null

---

#### public abstract
PGPData
newPGPData​(byte[] keyId)

Creates a

PGPData

from the specified PGP public key
identifier.

**Parameters:**
- keyId

- a PGP public key identifier as defined in

RFC 2440

, section 11.2.
The array is cloned to protect against subsequent modification.

**Returns:**
- a

PGPData

**Throws:**
- NullPointerException

- if

keyId

is

null
- IllegalArgumentException

- if the key id is not in the correct
format

---

#### public abstract
PGPData
newPGPData​(byte[] keyId,
byte[] keyPacket,

List
<? extends
XMLStructure
> other)

Creates a

PGPData

from the specified PGP public key
identifier, and optional key material packet and list of external
elements.

**Parameters:**
- keyId

- a PGP public key identifier as defined in

RFC 2440

, section 11.2.
The array is cloned to protect against subsequent modification.
- keyPacket

- a PGP key material packet as defined in

RFC 2440

, section 5.5.
The array is cloned to protect against subsequent modification. May
be

null

.
- other

- a list of

XMLStructure

s representing elements from
an external namespace. The list is defensively copied to protect
against subsequent modification. May be

null

or empty.

**Returns:**
- a

PGPData

**Throws:**
- NullPointerException

- if

keyId

is

null
- IllegalArgumentException

- if the

keyId

or

keyPacket

is not in the correct format. For

keyPacket

, the format of the packet header is
checked and the tag is verified that it is of type key material. The
contents and format of the packet body are not checked.
- ClassCastException

- if

other

contains any
entries that are not of type

XMLStructure

---

#### public abstract
PGPData
newPGPData​(byte[] keyPacket,

List
<? extends
XMLStructure
> other)

Creates a

PGPData

from the specified PGP key material
packet and optional list of external elements.

**Parameters:**
- keyPacket

- a PGP key material packet as defined in

RFC 2440

, section 5.5.
The array is cloned to protect against subsequent modification.
- other

- a list of

XMLStructure

s representing elements from
an external namespace. The list is defensively copied to protect
against subsequent modification. May be

null

or empty.

**Returns:**
- a

PGPData

**Throws:**
- NullPointerException

- if

keyPacket

is

null
- IllegalArgumentException

- if

keyPacket

is not in the
correct format. For

keyPacket

, the format of the packet
header is checked and the tag is verified that it is of type key
material. The contents and format of the packet body are not checked.
- ClassCastException

- if

other

contains any
entries that are not of type

XMLStructure

---

#### public abstract
RetrievalMethod
newRetrievalMethod​(
String
uri)

Creates a

RetrievalMethod

from the specified URI.

**Parameters:**
- uri

- the URI that identifies the

KeyInfo

information
to be retrieved

**Returns:**
- a

RetrievalMethod

**Throws:**
- NullPointerException

- if

uri

is

null
- IllegalArgumentException

- if

uri

is not RFC 2396
compliant

---

#### public abstract
RetrievalMethod
newRetrievalMethod​(
String
uri,

String
type,

List
<? extends
Transform
> transforms)

Creates a

RetrievalMethod

from the specified parameters.

**Parameters:**
- uri

- the URI that identifies the

KeyInfo

information
to be retrieved
- type

- a URI that identifies the type of

KeyInfo

information to be retrieved (may be

null

)
- transforms

- a list of

Transform

s. The list is defensively
copied to protect against subsequent modification. May be

null

or empty.

**Returns:**
- a

RetrievalMethod

**Throws:**
- NullPointerException

- if

uri

is

null
- IllegalArgumentException

- if

uri

is not RFC 2396
compliant
- ClassCastException

- if

transforms

contains any
entries that are not of type

Transform

---

#### public abstract
X509Data
newX509Data​(
List
<?> content)

Creates a

X509Data

containing the specified list of
X.509 content.

**Parameters:**
- content

- a list of one or more X.509 content types. Valid types are

String

(subject names),

byte[]

(subject key ids),

X509Certificate

,

X509CRL

,
or

XMLStructure

(

X509IssuerSerial

objects or elements from an external namespace). Subject names are
distinguished names in RFC 2253 String format. Implementations MUST
support the attribute type keywords defined in RFC 2253 (CN, L, ST,
O, OU, C, STREET, DC and UID). Implementations MAY support additional
keywords. The list is defensively copied to protect against
subsequent modification.

**Returns:**
- a

X509Data

**Throws:**
- NullPointerException

- if

content

is

null
- IllegalArgumentException

- if

content

is empty, or
if a subject name is not RFC 2253 compliant or one of the attribute
type keywords is not recognized.
- ClassCastException

- if

content

contains any entries
that are not of one of the valid types mentioned above

---

#### public abstract
X509IssuerSerial
newX509IssuerSerial​(
String
issuerName,

BigInteger
serialNumber)

Creates an

X509IssuerSerial

from the specified X.500 issuer
distinguished name and serial number.

**Parameters:**
- issuerName

- the issuer's distinguished name in RFC 2253 String
format. Implementations MUST support the attribute type keywords
defined in RFC 2253 (CN, L, ST, O, OU, C, STREET, DC and UID).
Implementations MAY support additional keywords.
- serialNumber

- the serial number

**Returns:**
- an

X509IssuerSerial

**Throws:**
- NullPointerException

- if

issuerName

or

serialNumber

are

null
- IllegalArgumentException

- if the issuer name is not RFC 2253
compliant or one of the attribute type keywords is not recognized.

---

#### public abstract boolean isFeatureSupported​(
String
feature)

Indicates whether a specified feature is supported.

**Parameters:**
- feature

- the feature name (as an absolute URI)

**Returns:**
- true

if the specified feature is supported,

false

otherwise

**Throws:**
- NullPointerException

- if

feature

is

null

---

#### public abstract
URIDereferencer
getURIDereferencer()

Returns a reference to the

URIDereferencer

that is used by
default to dereference URIs in

RetrievalMethod

objects.

**Returns:**
- a reference to the default

URIDereferencer

---

#### public abstract
KeyInfo
unmarshalKeyInfo​(
XMLStructure
xmlStructure)
throws
MarshalException

Unmarshals a new

KeyInfo

instance from a
mechanism-specific

XMLStructure

(ex:

DOMStructure

)
instance.

**Parameters:**
- xmlStructure

- a mechanism-specific XML structure from which to
unmarshal the keyinfo from

**Returns:**
- the

KeyInfo

**Throws:**
- NullPointerException

- if

xmlStructure

is

null
- ClassCastException

- if the type of

xmlStructure

is
inappropriate for this factory
- MarshalException

- if an unrecoverable exception occurs during
unmarshalling

---

### Additional Sections

#### Class KeyInfoFactory

java.lang.Object

- javax.xml.crypto.dsig.keyinfo.KeyInfoFactory

javax.xml.crypto.dsig.keyinfo.KeyInfoFactory

```java
public abstract class
KeyInfoFactory

extends
Object
```

A factory for creating

KeyInfo

objects from scratch or for
unmarshalling a

KeyInfo

object from a corresponding XML
representation.

Each instance of

KeyInfoFactory

supports a specific
XML mechanism type. To create a

KeyInfoFactory

, call one of the
static

getInstance

methods, passing in the XML
mechanism type desired, for example:

KeyInfoFactory factory = KeyInfoFactory.getInstance("DOM");

The objects that this factory produces will be based
on DOM and abide by the DOM interoperability requirements as defined in the

DOM Mechanism Requirements

section
of the API overview. See the

Java Security Standard Algorithm Names

document
for more information.

KeyInfoFactory

implementations are registered and loaded
using the

Provider

mechanism.
For example, a service provider that supports the
DOM mechanism would be specified in the

Provider

subclass as:

```java
put("KeyInfoFactory.DOM", "org.example.DOMKeyInfoFactory");
```

Also, the

XMLStructure

s that are created by this factory
may contain state specific to the

KeyInfo

and are not
intended to be reusable.

An implementation MUST minimally support the default mechanism type: DOM.

Note that a caller must use the same

KeyInfoFactory

instance to create the

XMLStructure

s of a particular

KeyInfo

object. The behavior is undefined if

XMLStructure

s from different providers or different mechanism
types are used together.

Concurrent Access

The static methods of this class are guaranteed to be thread-safe.
Multiple threads may concurrently invoke the static methods defined in this
class with no ill effects.

However, this is not true for the non-static methods defined by this
class. Unless otherwise documented by a specific provider, threads that
need to access a single

KeyInfoFactory

instance concurrently
should synchronize amongst themselves and provide the necessary locking.
Multiple threads each manipulating a different

KeyInfoFactory

instance need not synchronize.

**Since:** 1.6

public abstract class

KeyInfoFactory

extends

Object

A factory for creating

KeyInfo

objects from scratch or for
unmarshalling a

KeyInfo

object from a corresponding XML
representation.

Each instance of

KeyInfoFactory

supports a specific
XML mechanism type. To create a

KeyInfoFactory

, call one of the
static

getInstance

methods, passing in the XML
mechanism type desired, for example:

KeyInfoFactory factory = KeyInfoFactory.getInstance("DOM");

The objects that this factory produces will be based
on DOM and abide by the DOM interoperability requirements as defined in the

DOM Mechanism Requirements

section
of the API overview. See the

Java Security Standard Algorithm Names

document
for more information.

KeyInfoFactory

implementations are registered and loaded
using the

Provider

mechanism.
For example, a service provider that supports the
DOM mechanism would be specified in the

Provider

subclass as:

```java
put("KeyInfoFactory.DOM", "org.example.DOMKeyInfoFactory");
```

Also, the

XMLStructure

s that are created by this factory
may contain state specific to the

KeyInfo

and are not
intended to be reusable.

An implementation MUST minimally support the default mechanism type: DOM.

Note that a caller must use the same

KeyInfoFactory

instance to create the

XMLStructure

s of a particular

KeyInfo

object. The behavior is undefined if

XMLStructure

s from different providers or different mechanism
types are used together.

Concurrent Access

The static methods of this class are guaranteed to be thread-safe.
Multiple threads may concurrently invoke the static methods defined in this
class with no ill effects.

However, this is not true for the non-static methods defined by this
class. Unless otherwise documented by a specific provider, threads that
need to access a single

KeyInfoFactory

instance concurrently
should synchronize amongst themselves and provide the necessary locking.
Multiple threads each manipulating a different

KeyInfoFactory

instance need not synchronize.

Each instance of

KeyInfoFactory

supports a specific
XML mechanism type. To create a

KeyInfoFactory

, call one of the
static

getInstance

methods, passing in the XML
mechanism type desired, for example:

KeyInfoFactory factory = KeyInfoFactory.getInstance("DOM");

The objects that this factory produces will be based
on DOM and abide by the DOM interoperability requirements as defined in the

DOM Mechanism Requirements

section
of the API overview. See the

Java Security Standard Algorithm Names

document
for more information.

KeyInfoFactory

implementations are registered and loaded
using the

Provider

mechanism.
For example, a service provider that supports the
DOM mechanism would be specified in the

Provider

subclass as:

```java
put("KeyInfoFactory.DOM", "org.example.DOMKeyInfoFactory");
```

Also, the

XMLStructure

s that are created by this factory
may contain state specific to the

KeyInfo

and are not
intended to be reusable.

An implementation MUST minimally support the default mechanism type: DOM.

Note that a caller must use the same

KeyInfoFactory

instance to create the

XMLStructure

s of a particular

KeyInfo

object. The behavior is undefined if

XMLStructure

s from different providers or different mechanism
types are used together.

Concurrent Access

The static methods of this class are guaranteed to be thread-safe.
Multiple threads may concurrently invoke the static methods defined in this
class with no ill effects.

However, this is not true for the non-static methods defined by this
class. Unless otherwise documented by a specific provider, threads that
need to access a single

KeyInfoFactory

instance concurrently
should synchronize amongst themselves and provide the necessary locking.
Multiple threads each manipulating a different

KeyInfoFactory

instance need not synchronize.

The objects that this factory produces will be based
on DOM and abide by the DOM interoperability requirements as defined in the

DOM Mechanism Requirements

section
of the API overview. See the

Java Security Standard Algorithm Names

document
for more information.

KeyInfoFactory

implementations are registered and loaded
using the

Provider

mechanism.
For example, a service provider that supports the
DOM mechanism would be specified in the

Provider

subclass as:

```java
put("KeyInfoFactory.DOM", "org.example.DOMKeyInfoFactory");
```

Also, the

XMLStructure

s that are created by this factory
may contain state specific to the

KeyInfo

and are not
intended to be reusable.

An implementation MUST minimally support the default mechanism type: DOM.

Note that a caller must use the same

KeyInfoFactory

instance to create the

XMLStructure

s of a particular

KeyInfo

object. The behavior is undefined if

XMLStructure

s from different providers or different mechanism
types are used together.

Concurrent Access

The static methods of this class are guaranteed to be thread-safe.
Multiple threads may concurrently invoke the static methods defined in this
class with no ill effects.

However, this is not true for the non-static methods defined by this
class. Unless otherwise documented by a specific provider, threads that
need to access a single

KeyInfoFactory

instance concurrently
should synchronize amongst themselves and provide the necessary locking.
Multiple threads each manipulating a different

KeyInfoFactory

instance need not synchronize.

KeyInfoFactory

implementations are registered and loaded
using the

Provider

mechanism.
For example, a service provider that supports the
DOM mechanism would be specified in the

Provider

subclass as:

```java
put("KeyInfoFactory.DOM", "org.example.DOMKeyInfoFactory");
```

Also, the

XMLStructure

s that are created by this factory
may contain state specific to the

KeyInfo

and are not
intended to be reusable.

An implementation MUST minimally support the default mechanism type: DOM.

Note that a caller must use the same

KeyInfoFactory

instance to create the

XMLStructure

s of a particular

KeyInfo

object. The behavior is undefined if

XMLStructure

s from different providers or different mechanism
types are used together.

Concurrent Access

The static methods of this class are guaranteed to be thread-safe.
Multiple threads may concurrently invoke the static methods defined in this
class with no ill effects.

However, this is not true for the non-static methods defined by this
class. Unless otherwise documented by a specific provider, threads that
need to access a single

KeyInfoFactory

instance concurrently
should synchronize amongst themselves and provide the necessary locking.
Multiple threads each manipulating a different

KeyInfoFactory

instance need not synchronize.

put("KeyInfoFactory.DOM", "org.example.DOMKeyInfoFactory");

Also, the

XMLStructure

s that are created by this factory
may contain state specific to the

KeyInfo

and are not
intended to be reusable.

An implementation MUST minimally support the default mechanism type: DOM.

Note that a caller must use the same

KeyInfoFactory

instance to create the

XMLStructure

s of a particular

KeyInfo

object. The behavior is undefined if

XMLStructure

s from different providers or different mechanism
types are used together.

Concurrent Access

The static methods of this class are guaranteed to be thread-safe.
Multiple threads may concurrently invoke the static methods defined in this
class with no ill effects.

However, this is not true for the non-static methods defined by this
class. Unless otherwise documented by a specific provider, threads that
need to access a single

KeyInfoFactory

instance concurrently
should synchronize amongst themselves and provide the necessary locking.
Multiple threads each manipulating a different

KeyInfoFactory

instance need not synchronize.

An implementation MUST minimally support the default mechanism type: DOM.

Note that a caller must use the same

KeyInfoFactory

instance to create the

XMLStructure

s of a particular

KeyInfo

object. The behavior is undefined if

XMLStructure

s from different providers or different mechanism
types are used together.

Concurrent Access

The static methods of this class are guaranteed to be thread-safe.
Multiple threads may concurrently invoke the static methods defined in this
class with no ill effects.

However, this is not true for the non-static methods defined by this
class. Unless otherwise documented by a specific provider, threads that
need to access a single

KeyInfoFactory

instance concurrently
should synchronize amongst themselves and provide the necessary locking.
Multiple threads each manipulating a different

KeyInfoFactory

instance need not synchronize.

Note that a caller must use the same

KeyInfoFactory

instance to create the

XMLStructure

s of a particular

KeyInfo

object. The behavior is undefined if

XMLStructure

s from different providers or different mechanism
types are used together.

Concurrent Access

The static methods of this class are guaranteed to be thread-safe.
Multiple threads may concurrently invoke the static methods defined in this
class with no ill effects.

However, this is not true for the non-static methods defined by this
class. Unless otherwise documented by a specific provider, threads that
need to access a single

KeyInfoFactory

instance concurrently
should synchronize amongst themselves and provide the necessary locking.
Multiple threads each manipulating a different

KeyInfoFactory

instance need not synchronize.

Concurrent Access

The static methods of this class are guaranteed to be thread-safe.
Multiple threads may concurrently invoke the static methods defined in this
class with no ill effects.

However, this is not true for the non-static methods defined by this
class. Unless otherwise documented by a specific provider, threads that
need to access a single

KeyInfoFactory

instance concurrently
should synchronize amongst themselves and provide the necessary locking.
Multiple threads each manipulating a different

KeyInfoFactory

instance need not synchronize.

The static methods of this class are guaranteed to be thread-safe.
Multiple threads may concurrently invoke the static methods defined in this
class with no ill effects.

However, this is not true for the non-static methods defined by this
class. Unless otherwise documented by a specific provider, threads that
need to access a single

KeyInfoFactory

instance concurrently
should synchronize amongst themselves and provide the necessary locking.
Multiple threads each manipulating a different

KeyInfoFactory

instance need not synchronize.

However, this is not true for the non-static methods defined by this
class. Unless otherwise documented by a specific provider, threads that
need to access a single

KeyInfoFactory

instance concurrently
should synchronize amongst themselves and provide the necessary locking.
Multiple threads each manipulating a different

KeyInfoFactory

instance need not synchronize.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

KeyInfoFactory

()

Default constructor, for invocation by subclasses.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

static

KeyInfoFactory

getInstance

()

Returns a

KeyInfoFactory

that supports the
default XML processing mechanism and representation type ("DOM").

static

KeyInfoFactory

getInstance

​(

String

mechanismType)

Returns a

KeyInfoFactory

that supports the
specified XML processing mechanism and representation type (ex: "DOM").

static

KeyInfoFactory

getInstance

​(

String

mechanismType,

String

provider)

Returns a

KeyInfoFactory

that supports the
requested XML processing mechanism and representation type (ex: "DOM"),
as supplied by the specified provider.

static

KeyInfoFactory

getInstance

​(

String

mechanismType,

Provider

provider)

Returns a

KeyInfoFactory

that supports the
requested XML processing mechanism and representation type (ex: "DOM"),
as supplied by the specified provider.

String

getMechanismType

()

Returns the type of the XML processing mechanism and representation
supported by this

KeyInfoFactory

(ex: "DOM")

Provider

getProvider

()

Returns the provider of this

KeyInfoFactory

.

abstract

URIDereferencer

getURIDereferencer

()

Returns a reference to the

URIDereferencer

that is used by
default to dereference URIs in

RetrievalMethod

objects.

abstract boolean

isFeatureSupported

​(

String

feature)

Indicates whether a specified feature is supported.

abstract

KeyInfo

newKeyInfo

​(

List

<? extends

XMLStructure

> content)

Creates a

KeyInfo

containing the specified list of
key information types.

abstract

KeyInfo

newKeyInfo

​(

List

<? extends

XMLStructure

> content,

String

id)

Creates a

KeyInfo

containing the specified list of key
information types and optional id.

abstract

KeyName

newKeyName

​(

String

name)

Creates a

KeyName

from the specified name.

abstract

KeyValue

newKeyValue

​(

PublicKey

key)

Creates a

KeyValue

from the specified public key.

abstract

PGPData

newPGPData

​(byte[] keyId)

Creates a

PGPData

from the specified PGP public key
identifier.

abstract

PGPData

newPGPData

​(byte[] keyId,
byte[] keyPacket,

List

<? extends

XMLStructure

> other)

Creates a

PGPData

from the specified PGP public key
identifier, and optional key material packet and list of external
elements.

abstract

PGPData

newPGPData

​(byte[] keyPacket,

List

<? extends

XMLStructure

> other)

Creates a

PGPData

from the specified PGP key material
packet and optional list of external elements.

abstract

RetrievalMethod

newRetrievalMethod

​(

String

uri)

Creates a

RetrievalMethod

from the specified URI.

abstract

RetrievalMethod

newRetrievalMethod

​(

String

uri,

String

type,

List

<? extends

Transform

> transforms)

Creates a

RetrievalMethod

from the specified parameters.

abstract

X509Data

newX509Data

​(

List

<?> content)

Creates a

X509Data

containing the specified list of
X.509 content.

abstract

X509IssuerSerial

newX509IssuerSerial

​(

String

issuerName,

BigInteger

serialNumber)

Creates an

X509IssuerSerial

from the specified X.500 issuer
distinguished name and serial number.

abstract

KeyInfo

unmarshalKeyInfo

​(

XMLStructure

xmlStructure)

Unmarshals a new

KeyInfo

instance from a
mechanism-specific

XMLStructure

(ex:

DOMStructure

)
instance.

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

Modifier

Constructor

Description

protected

KeyInfoFactory

()

Default constructor, for invocation by subclasses.

---

#### Constructor Summary

Default constructor, for invocation by subclasses.

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

static

KeyInfoFactory

getInstance

()

Returns a

KeyInfoFactory

that supports the
default XML processing mechanism and representation type ("DOM").

static

KeyInfoFactory

getInstance

​(

String

mechanismType)

Returns a

KeyInfoFactory

that supports the
specified XML processing mechanism and representation type (ex: "DOM").

static

KeyInfoFactory

getInstance

​(

String

mechanismType,

String

provider)

Returns a

KeyInfoFactory

that supports the
requested XML processing mechanism and representation type (ex: "DOM"),
as supplied by the specified provider.

static

KeyInfoFactory

getInstance

​(

String

mechanismType,

Provider

provider)

Returns a

KeyInfoFactory

that supports the
requested XML processing mechanism and representation type (ex: "DOM"),
as supplied by the specified provider.

String

getMechanismType

()

Returns the type of the XML processing mechanism and representation
supported by this

KeyInfoFactory

(ex: "DOM")

Provider

getProvider

()

Returns the provider of this

KeyInfoFactory

.

abstract

URIDereferencer

getURIDereferencer

()

Returns a reference to the

URIDereferencer

that is used by
default to dereference URIs in

RetrievalMethod

objects.

abstract boolean

isFeatureSupported

​(

String

feature)

Indicates whether a specified feature is supported.

abstract

KeyInfo

newKeyInfo

​(

List

<? extends

XMLStructure

> content)

Creates a

KeyInfo

containing the specified list of
key information types.

abstract

KeyInfo

newKeyInfo

​(

List

<? extends

XMLStructure

> content,

String

id)

Creates a

KeyInfo

containing the specified list of key
information types and optional id.

abstract

KeyName

newKeyName

​(

String

name)

Creates a

KeyName

from the specified name.

abstract

KeyValue

newKeyValue

​(

PublicKey

key)

Creates a

KeyValue

from the specified public key.

abstract

PGPData

newPGPData

​(byte[] keyId)

Creates a

PGPData

from the specified PGP public key
identifier.

abstract

PGPData

newPGPData

​(byte[] keyId,
byte[] keyPacket,

List

<? extends

XMLStructure

> other)

Creates a

PGPData

from the specified PGP public key
identifier, and optional key material packet and list of external
elements.

abstract

PGPData

newPGPData

​(byte[] keyPacket,

List

<? extends

XMLStructure

> other)

Creates a

PGPData

from the specified PGP key material
packet and optional list of external elements.

abstract

RetrievalMethod

newRetrievalMethod

​(

String

uri)

Creates a

RetrievalMethod

from the specified URI.

abstract

RetrievalMethod

newRetrievalMethod

​(

String

uri,

String

type,

List

<? extends

Transform

> transforms)

Creates a

RetrievalMethod

from the specified parameters.

abstract

X509Data

newX509Data

​(

List

<?> content)

Creates a

X509Data

containing the specified list of
X.509 content.

abstract

X509IssuerSerial

newX509IssuerSerial

​(

String

issuerName,

BigInteger

serialNumber)

Creates an

X509IssuerSerial

from the specified X.500 issuer
distinguished name and serial number.

abstract

KeyInfo

unmarshalKeyInfo

​(

XMLStructure

xmlStructure)

Unmarshals a new

KeyInfo

instance from a
mechanism-specific

XMLStructure

(ex:

DOMStructure

)
instance.

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

Returns a

KeyInfoFactory

that supports the
default XML processing mechanism and representation type ("DOM").

Returns a

KeyInfoFactory

that supports the
specified XML processing mechanism and representation type (ex: "DOM").

Returns a

KeyInfoFactory

that supports the
requested XML processing mechanism and representation type (ex: "DOM"),
as supplied by the specified provider.

Returns the type of the XML processing mechanism and representation
supported by this

KeyInfoFactory

(ex: "DOM")

Returns the provider of this

KeyInfoFactory

.

Returns a reference to the

URIDereferencer

that is used by
default to dereference URIs in

RetrievalMethod

objects.

Indicates whether a specified feature is supported.

Creates a

KeyInfo

containing the specified list of
key information types.

Creates a

KeyInfo

containing the specified list of key
information types and optional id.

Creates a

KeyName

from the specified name.

Creates a

KeyValue

from the specified public key.

Creates a

PGPData

from the specified PGP public key
identifier.

Creates a

PGPData

from the specified PGP public key
identifier, and optional key material packet and list of external
elements.

Creates a

PGPData

from the specified PGP key material
packet and optional list of external elements.

Creates a

RetrievalMethod

from the specified URI.

Creates a

RetrievalMethod

from the specified parameters.

Creates a

X509Data

containing the specified list of
X.509 content.

Creates an

X509IssuerSerial

from the specified X.500 issuer
distinguished name and serial number.

Unmarshals a new

KeyInfo

instance from a
mechanism-specific

XMLStructure

(ex:

DOMStructure

)
instance.

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

- KeyInfoFactory

```java
protected KeyInfoFactory()
```

Default constructor, for invocation by subclasses.

============ METHOD DETAIL ==========

- Method Detail

- getInstance

```java
public static
KeyInfoFactory
getInstance​(
String
mechanismType)
```

Returns a

KeyInfoFactory

that supports the
specified XML processing mechanism and representation type (ex: "DOM").

This method uses the standard JCA provider lookup mechanism to
locate and instantiate a

KeyInfoFactory

implementation of
the desired mechanism type. It traverses the list of registered security

Provider

s, starting with the most preferred

Provider

. A new

KeyInfoFactory

object
from the first

Provider

that supports the specified
mechanism is returned.

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
**Parameters:** mechanismType

- the type of the XML processing mechanism and
representation. See the

Java Security Standard Algorithm Names

document
for more information.
**Returns:** a new

KeyInfoFactory
**Throws:** NullPointerException

- if

mechanismType

is

null
**Throws:** NoSuchMechanismException

- if no

Provider

supports a

KeyInfoFactory

implementation for the specified mechanism
**See Also:** Provider

- getInstance

```java
public static
KeyInfoFactory
getInstance​(
String
mechanismType,

Provider
provider)
```

Returns a

KeyInfoFactory

that supports the
requested XML processing mechanism and representation type (ex: "DOM"),
as supplied by the specified provider. Note that the specified

Provider

object does not have to be registered in the
provider list.

**Parameters:** mechanismType

- the type of the XML processing mechanism and
representation. See the

Java Security Standard Algorithm Names

document
for more information.
**Parameters:** provider

- the

Provider

object
**Returns:** a new

KeyInfoFactory
**Throws:** NullPointerException

- if

mechanismType

or

provider

are

null
**Throws:** NoSuchMechanismException

- if a

KeyInfoFactory

implementation for the specified mechanism is not available from the
specified

Provider

object
**See Also:** Provider

- getInstance

```java
public static
KeyInfoFactory
getInstance​(
String
mechanismType,

String
provider)
throws
NoSuchProviderException
```

Returns a

KeyInfoFactory

that supports the
requested XML processing mechanism and representation type (ex: "DOM"),
as supplied by the specified provider. The specified provider must be
registered in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:** mechanismType

- the type of the XML processing mechanism and
representation. See the

Java Security Standard Algorithm Names

document
for more information.
**Parameters:** provider

- the string name of the provider
**Returns:** a new

KeyInfoFactory
**Throws:** NoSuchProviderException

- if the specified provider is not
registered in the security provider list
**Throws:** NullPointerException

- if

mechanismType

or

provider

are

null
**Throws:** NoSuchMechanismException

- if a

KeyInfoFactory

implementation for the specified mechanism is not available from the
specified provider
**See Also:** Provider

- getInstance

```java
public static
KeyInfoFactory
getInstance()
```

Returns a

KeyInfoFactory

that supports the
default XML processing mechanism and representation type ("DOM").

This method uses the standard JCA provider lookup mechanism to
locate and instantiate a

KeyInfoFactory

implementation of
the default mechanism type. It traverses the list of registered security

Provider

s, starting with the most preferred

Provider

. A new

KeyInfoFactory

object
from the first

Provider

that supports the DOM mechanism is
returned.

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
**Returns:** a new

KeyInfoFactory
**Throws:** NoSuchMechanismException

- if no

Provider

supports a

KeyInfoFactory

implementation for the DOM mechanism
**See Also:** Provider

- getMechanismType

```java
public final
String
getMechanismType()
```

Returns the type of the XML processing mechanism and representation
supported by this

KeyInfoFactory

(ex: "DOM")

**Returns:** the XML processing mechanism type supported by this

KeyInfoFactory

- getProvider

```java
public final
Provider
getProvider()
```

Returns the provider of this

KeyInfoFactory

.

**Returns:** the provider of this

KeyInfoFactory

- newKeyInfo

```java
public abstract
KeyInfo
newKeyInfo​(
List
<? extends
XMLStructure
> content)
```

Creates a

KeyInfo

containing the specified list of
key information types.

**Parameters:** content

- a list of one or more

XMLStructure

s representing
key information types. The list is defensively copied to protect
against subsequent modification.
**Returns:** a

KeyInfo
**Throws:** NullPointerException

- if

content

is

null
**Throws:** IllegalArgumentException

- if

content

is empty
**Throws:** ClassCastException

- if

content

contains any entries
that are not of type

XMLStructure

- newKeyInfo

```java
public abstract
KeyInfo
newKeyInfo​(
List
<? extends
XMLStructure
> content,

String
id)
```

Creates a

KeyInfo

containing the specified list of key
information types and optional id. The

id

parameter represents the value of an XML

ID

attribute and is useful for referencing
the

KeyInfo

from other XML structures.

**Parameters:** content

- a list of one or more

XMLStructure

s representing
key information types. The list is defensively copied to protect
against subsequent modification.
**Parameters:** id

- the value of an XML

ID

(may be

null

)
**Returns:** a

KeyInfo
**Throws:** NullPointerException

- if

content

is

null
**Throws:** IllegalArgumentException

- if

content

is empty
**Throws:** ClassCastException

- if

content

contains any entries
that are not of type

XMLStructure

- newKeyName

```java
public abstract
KeyName
newKeyName​(
String
name)
```

Creates a

KeyName

from the specified name.

**Parameters:** name

- the name that identifies the key
**Returns:** a

KeyName
**Throws:** NullPointerException

- if

name

is

null

- newKeyValue

```java
public abstract
KeyValue
newKeyValue​(
PublicKey
key)
throws
KeyException
```

Creates a

KeyValue

from the specified public key.

**Parameters:** key

- the public key
**Returns:** a

KeyValue
**Throws:** KeyException

- if the

key

's algorithm is not
recognized or supported by this

KeyInfoFactory
**Throws:** NullPointerException

- if

key

is

null

- newPGPData

```java
public abstract
PGPData
newPGPData​(byte[] keyId)
```

Creates a

PGPData

from the specified PGP public key
identifier.

**Parameters:** keyId

- a PGP public key identifier as defined in

RFC 2440

, section 11.2.
The array is cloned to protect against subsequent modification.
**Returns:** a

PGPData
**Throws:** NullPointerException

- if

keyId

is

null
**Throws:** IllegalArgumentException

- if the key id is not in the correct
format

- newPGPData

```java
public abstract
PGPData
newPGPData​(byte[] keyId,
byte[] keyPacket,

List
<? extends
XMLStructure
> other)
```

Creates a

PGPData

from the specified PGP public key
identifier, and optional key material packet and list of external
elements.

**Parameters:** keyId

- a PGP public key identifier as defined in

RFC 2440

, section 11.2.
The array is cloned to protect against subsequent modification.
**Parameters:** keyPacket

- a PGP key material packet as defined in

RFC 2440

, section 5.5.
The array is cloned to protect against subsequent modification. May
be

null

.
**Parameters:** other

- a list of

XMLStructure

s representing elements from
an external namespace. The list is defensively copied to protect
against subsequent modification. May be

null

or empty.
**Returns:** a

PGPData
**Throws:** NullPointerException

- if

keyId

is

null
**Throws:** IllegalArgumentException

- if the

keyId

or

keyPacket

is not in the correct format. For

keyPacket

, the format of the packet header is
checked and the tag is verified that it is of type key material. The
contents and format of the packet body are not checked.
**Throws:** ClassCastException

- if

other

contains any
entries that are not of type

XMLStructure

- newPGPData

```java
public abstract
PGPData
newPGPData​(byte[] keyPacket,

List
<? extends
XMLStructure
> other)
```

Creates a

PGPData

from the specified PGP key material
packet and optional list of external elements.

**Parameters:** keyPacket

- a PGP key material packet as defined in

RFC 2440

, section 5.5.
The array is cloned to protect against subsequent modification.
**Parameters:** other

- a list of

XMLStructure

s representing elements from
an external namespace. The list is defensively copied to protect
against subsequent modification. May be

null

or empty.
**Returns:** a

PGPData
**Throws:** NullPointerException

- if

keyPacket

is

null
**Throws:** IllegalArgumentException

- if

keyPacket

is not in the
correct format. For

keyPacket

, the format of the packet
header is checked and the tag is verified that it is of type key
material. The contents and format of the packet body are not checked.
**Throws:** ClassCastException

- if

other

contains any
entries that are not of type

XMLStructure

- newRetrievalMethod

```java
public abstract
RetrievalMethod
newRetrievalMethod​(
String
uri)
```

Creates a

RetrievalMethod

from the specified URI.

**Parameters:** uri

- the URI that identifies the

KeyInfo

information
to be retrieved
**Returns:** a

RetrievalMethod
**Throws:** NullPointerException

- if

uri

is

null
**Throws:** IllegalArgumentException

- if

uri

is not RFC 2396
compliant

- newRetrievalMethod

```java
public abstract
RetrievalMethod
newRetrievalMethod​(
String
uri,

String
type,

List
<? extends
Transform
> transforms)
```

Creates a

RetrievalMethod

from the specified parameters.

**Parameters:** uri

- the URI that identifies the

KeyInfo

information
to be retrieved
**Parameters:** type

- a URI that identifies the type of

KeyInfo

information to be retrieved (may be

null

)
**Parameters:** transforms

- a list of

Transform

s. The list is defensively
copied to protect against subsequent modification. May be

null

or empty.
**Returns:** a

RetrievalMethod
**Throws:** NullPointerException

- if

uri

is

null
**Throws:** IllegalArgumentException

- if

uri

is not RFC 2396
compliant
**Throws:** ClassCastException

- if

transforms

contains any
entries that are not of type

Transform

- newX509Data

```java
public abstract
X509Data
newX509Data​(
List
<?> content)
```

Creates a

X509Data

containing the specified list of
X.509 content.

**Parameters:** content

- a list of one or more X.509 content types. Valid types are

String

(subject names),

byte[]

(subject key ids),

X509Certificate

,

X509CRL

,
or

XMLStructure

(

X509IssuerSerial

objects or elements from an external namespace). Subject names are
distinguished names in RFC 2253 String format. Implementations MUST
support the attribute type keywords defined in RFC 2253 (CN, L, ST,
O, OU, C, STREET, DC and UID). Implementations MAY support additional
keywords. The list is defensively copied to protect against
subsequent modification.
**Returns:** a

X509Data
**Throws:** NullPointerException

- if

content

is

null
**Throws:** IllegalArgumentException

- if

content

is empty, or
if a subject name is not RFC 2253 compliant or one of the attribute
type keywords is not recognized.
**Throws:** ClassCastException

- if

content

contains any entries
that are not of one of the valid types mentioned above

- newX509IssuerSerial

```java
public abstract
X509IssuerSerial
newX509IssuerSerial​(
String
issuerName,

BigInteger
serialNumber)
```

Creates an

X509IssuerSerial

from the specified X.500 issuer
distinguished name and serial number.

**Parameters:** issuerName

- the issuer's distinguished name in RFC 2253 String
format. Implementations MUST support the attribute type keywords
defined in RFC 2253 (CN, L, ST, O, OU, C, STREET, DC and UID).
Implementations MAY support additional keywords.
**Parameters:** serialNumber

- the serial number
**Returns:** an

X509IssuerSerial
**Throws:** NullPointerException

- if

issuerName

or

serialNumber

are

null
**Throws:** IllegalArgumentException

- if the issuer name is not RFC 2253
compliant or one of the attribute type keywords is not recognized.

- isFeatureSupported

```java
public abstract boolean isFeatureSupported​(
String
feature)
```

Indicates whether a specified feature is supported.

**Parameters:** feature

- the feature name (as an absolute URI)
**Returns:** true

if the specified feature is supported,

false

otherwise
**Throws:** NullPointerException

- if

feature

is

null

- getURIDereferencer

```java
public abstract
URIDereferencer
getURIDereferencer()
```

Returns a reference to the

URIDereferencer

that is used by
default to dereference URIs in

RetrievalMethod

objects.

**Returns:** a reference to the default

URIDereferencer

- unmarshalKeyInfo

```java
public abstract
KeyInfo
unmarshalKeyInfo​(
XMLStructure
xmlStructure)
throws
MarshalException
```

Unmarshals a new

KeyInfo

instance from a
mechanism-specific

XMLStructure

(ex:

DOMStructure

)
instance.

**Parameters:** xmlStructure

- a mechanism-specific XML structure from which to
unmarshal the keyinfo from
**Returns:** the

KeyInfo
**Throws:** NullPointerException

- if

xmlStructure

is

null
**Throws:** ClassCastException

- if the type of

xmlStructure

is
inappropriate for this factory
**Throws:** MarshalException

- if an unrecoverable exception occurs during
unmarshalling

Constructor Detail

- KeyInfoFactory

```java
protected KeyInfoFactory()
```

Default constructor, for invocation by subclasses.

---

#### Constructor Detail

KeyInfoFactory

```java
protected KeyInfoFactory()
```

Default constructor, for invocation by subclasses.

---

#### KeyInfoFactory

protected KeyInfoFactory()

Default constructor, for invocation by subclasses.

Method Detail

- getInstance

```java
public static
KeyInfoFactory
getInstance​(
String
mechanismType)
```

Returns a

KeyInfoFactory

that supports the
specified XML processing mechanism and representation type (ex: "DOM").

This method uses the standard JCA provider lookup mechanism to
locate and instantiate a

KeyInfoFactory

implementation of
the desired mechanism type. It traverses the list of registered security

Provider

s, starting with the most preferred

Provider

. A new

KeyInfoFactory

object
from the first

Provider

that supports the specified
mechanism is returned.

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
**Parameters:** mechanismType

- the type of the XML processing mechanism and
representation. See the

Java Security Standard Algorithm Names

document
for more information.
**Returns:** a new

KeyInfoFactory
**Throws:** NullPointerException

- if

mechanismType

is

null
**Throws:** NoSuchMechanismException

- if no

Provider

supports a

KeyInfoFactory

implementation for the specified mechanism
**See Also:** Provider

- getInstance

```java
public static
KeyInfoFactory
getInstance​(
String
mechanismType,

Provider
provider)
```

Returns a

KeyInfoFactory

that supports the
requested XML processing mechanism and representation type (ex: "DOM"),
as supplied by the specified provider. Note that the specified

Provider

object does not have to be registered in the
provider list.

**Parameters:** mechanismType

- the type of the XML processing mechanism and
representation. See the

Java Security Standard Algorithm Names

document
for more information.
**Parameters:** provider

- the

Provider

object
**Returns:** a new

KeyInfoFactory
**Throws:** NullPointerException

- if

mechanismType

or

provider

are

null
**Throws:** NoSuchMechanismException

- if a

KeyInfoFactory

implementation for the specified mechanism is not available from the
specified

Provider

object
**See Also:** Provider

- getInstance

```java
public static
KeyInfoFactory
getInstance​(
String
mechanismType,

String
provider)
throws
NoSuchProviderException
```

Returns a

KeyInfoFactory

that supports the
requested XML processing mechanism and representation type (ex: "DOM"),
as supplied by the specified provider. The specified provider must be
registered in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:** mechanismType

- the type of the XML processing mechanism and
representation. See the

Java Security Standard Algorithm Names

document
for more information.
**Parameters:** provider

- the string name of the provider
**Returns:** a new

KeyInfoFactory
**Throws:** NoSuchProviderException

- if the specified provider is not
registered in the security provider list
**Throws:** NullPointerException

- if

mechanismType

or

provider

are

null
**Throws:** NoSuchMechanismException

- if a

KeyInfoFactory

implementation for the specified mechanism is not available from the
specified provider
**See Also:** Provider

- getInstance

```java
public static
KeyInfoFactory
getInstance()
```

Returns a

KeyInfoFactory

that supports the
default XML processing mechanism and representation type ("DOM").

This method uses the standard JCA provider lookup mechanism to
locate and instantiate a

KeyInfoFactory

implementation of
the default mechanism type. It traverses the list of registered security

Provider

s, starting with the most preferred

Provider

. A new

KeyInfoFactory

object
from the first

Provider

that supports the DOM mechanism is
returned.

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
**Returns:** a new

KeyInfoFactory
**Throws:** NoSuchMechanismException

- if no

Provider

supports a

KeyInfoFactory

implementation for the DOM mechanism
**See Also:** Provider

- getMechanismType

```java
public final
String
getMechanismType()
```

Returns the type of the XML processing mechanism and representation
supported by this

KeyInfoFactory

(ex: "DOM")

**Returns:** the XML processing mechanism type supported by this

KeyInfoFactory

- getProvider

```java
public final
Provider
getProvider()
```

Returns the provider of this

KeyInfoFactory

.

**Returns:** the provider of this

KeyInfoFactory

- newKeyInfo

```java
public abstract
KeyInfo
newKeyInfo​(
List
<? extends
XMLStructure
> content)
```

Creates a

KeyInfo

containing the specified list of
key information types.

**Parameters:** content

- a list of one or more

XMLStructure

s representing
key information types. The list is defensively copied to protect
against subsequent modification.
**Returns:** a

KeyInfo
**Throws:** NullPointerException

- if

content

is

null
**Throws:** IllegalArgumentException

- if

content

is empty
**Throws:** ClassCastException

- if

content

contains any entries
that are not of type

XMLStructure

- newKeyInfo

```java
public abstract
KeyInfo
newKeyInfo​(
List
<? extends
XMLStructure
> content,

String
id)
```

Creates a

KeyInfo

containing the specified list of key
information types and optional id. The

id

parameter represents the value of an XML

ID

attribute and is useful for referencing
the

KeyInfo

from other XML structures.

**Parameters:** content

- a list of one or more

XMLStructure

s representing
key information types. The list is defensively copied to protect
against subsequent modification.
**Parameters:** id

- the value of an XML

ID

(may be

null

)
**Returns:** a

KeyInfo
**Throws:** NullPointerException

- if

content

is

null
**Throws:** IllegalArgumentException

- if

content

is empty
**Throws:** ClassCastException

- if

content

contains any entries
that are not of type

XMLStructure

- newKeyName

```java
public abstract
KeyName
newKeyName​(
String
name)
```

Creates a

KeyName

from the specified name.

**Parameters:** name

- the name that identifies the key
**Returns:** a

KeyName
**Throws:** NullPointerException

- if

name

is

null

- newKeyValue

```java
public abstract
KeyValue
newKeyValue​(
PublicKey
key)
throws
KeyException
```

Creates a

KeyValue

from the specified public key.

**Parameters:** key

- the public key
**Returns:** a

KeyValue
**Throws:** KeyException

- if the

key

's algorithm is not
recognized or supported by this

KeyInfoFactory
**Throws:** NullPointerException

- if

key

is

null

- newPGPData

```java
public abstract
PGPData
newPGPData​(byte[] keyId)
```

Creates a

PGPData

from the specified PGP public key
identifier.

**Parameters:** keyId

- a PGP public key identifier as defined in

RFC 2440

, section 11.2.
The array is cloned to protect against subsequent modification.
**Returns:** a

PGPData
**Throws:** NullPointerException

- if

keyId

is

null
**Throws:** IllegalArgumentException

- if the key id is not in the correct
format

- newPGPData

```java
public abstract
PGPData
newPGPData​(byte[] keyId,
byte[] keyPacket,

List
<? extends
XMLStructure
> other)
```

Creates a

PGPData

from the specified PGP public key
identifier, and optional key material packet and list of external
elements.

**Parameters:** keyId

- a PGP public key identifier as defined in

RFC 2440

, section 11.2.
The array is cloned to protect against subsequent modification.
**Parameters:** keyPacket

- a PGP key material packet as defined in

RFC 2440

, section 5.5.
The array is cloned to protect against subsequent modification. May
be

null

.
**Parameters:** other

- a list of

XMLStructure

s representing elements from
an external namespace. The list is defensively copied to protect
against subsequent modification. May be

null

or empty.
**Returns:** a

PGPData
**Throws:** NullPointerException

- if

keyId

is

null
**Throws:** IllegalArgumentException

- if the

keyId

or

keyPacket

is not in the correct format. For

keyPacket

, the format of the packet header is
checked and the tag is verified that it is of type key material. The
contents and format of the packet body are not checked.
**Throws:** ClassCastException

- if

other

contains any
entries that are not of type

XMLStructure

- newPGPData

```java
public abstract
PGPData
newPGPData​(byte[] keyPacket,

List
<? extends
XMLStructure
> other)
```

Creates a

PGPData

from the specified PGP key material
packet and optional list of external elements.

**Parameters:** keyPacket

- a PGP key material packet as defined in

RFC 2440

, section 5.5.
The array is cloned to protect against subsequent modification.
**Parameters:** other

- a list of

XMLStructure

s representing elements from
an external namespace. The list is defensively copied to protect
against subsequent modification. May be

null

or empty.
**Returns:** a

PGPData
**Throws:** NullPointerException

- if

keyPacket

is

null
**Throws:** IllegalArgumentException

- if

keyPacket

is not in the
correct format. For

keyPacket

, the format of the packet
header is checked and the tag is verified that it is of type key
material. The contents and format of the packet body are not checked.
**Throws:** ClassCastException

- if

other

contains any
entries that are not of type

XMLStructure

- newRetrievalMethod

```java
public abstract
RetrievalMethod
newRetrievalMethod​(
String
uri)
```

Creates a

RetrievalMethod

from the specified URI.

**Parameters:** uri

- the URI that identifies the

KeyInfo

information
to be retrieved
**Returns:** a

RetrievalMethod
**Throws:** NullPointerException

- if

uri

is

null
**Throws:** IllegalArgumentException

- if

uri

is not RFC 2396
compliant

- newRetrievalMethod

```java
public abstract
RetrievalMethod
newRetrievalMethod​(
String
uri,

String
type,

List
<? extends
Transform
> transforms)
```

Creates a

RetrievalMethod

from the specified parameters.

**Parameters:** uri

- the URI that identifies the

KeyInfo

information
to be retrieved
**Parameters:** type

- a URI that identifies the type of

KeyInfo

information to be retrieved (may be

null

)
**Parameters:** transforms

- a list of

Transform

s. The list is defensively
copied to protect against subsequent modification. May be

null

or empty.
**Returns:** a

RetrievalMethod
**Throws:** NullPointerException

- if

uri

is

null
**Throws:** IllegalArgumentException

- if

uri

is not RFC 2396
compliant
**Throws:** ClassCastException

- if

transforms

contains any
entries that are not of type

Transform

- newX509Data

```java
public abstract
X509Data
newX509Data​(
List
<?> content)
```

Creates a

X509Data

containing the specified list of
X.509 content.

**Parameters:** content

- a list of one or more X.509 content types. Valid types are

String

(subject names),

byte[]

(subject key ids),

X509Certificate

,

X509CRL

,
or

XMLStructure

(

X509IssuerSerial

objects or elements from an external namespace). Subject names are
distinguished names in RFC 2253 String format. Implementations MUST
support the attribute type keywords defined in RFC 2253 (CN, L, ST,
O, OU, C, STREET, DC and UID). Implementations MAY support additional
keywords. The list is defensively copied to protect against
subsequent modification.
**Returns:** a

X509Data
**Throws:** NullPointerException

- if

content

is

null
**Throws:** IllegalArgumentException

- if

content

is empty, or
if a subject name is not RFC 2253 compliant or one of the attribute
type keywords is not recognized.
**Throws:** ClassCastException

- if

content

contains any entries
that are not of one of the valid types mentioned above

- newX509IssuerSerial

```java
public abstract
X509IssuerSerial
newX509IssuerSerial​(
String
issuerName,

BigInteger
serialNumber)
```

Creates an

X509IssuerSerial

from the specified X.500 issuer
distinguished name and serial number.

**Parameters:** issuerName

- the issuer's distinguished name in RFC 2253 String
format. Implementations MUST support the attribute type keywords
defined in RFC 2253 (CN, L, ST, O, OU, C, STREET, DC and UID).
Implementations MAY support additional keywords.
**Parameters:** serialNumber

- the serial number
**Returns:** an

X509IssuerSerial
**Throws:** NullPointerException

- if

issuerName

or

serialNumber

are

null
**Throws:** IllegalArgumentException

- if the issuer name is not RFC 2253
compliant or one of the attribute type keywords is not recognized.

- isFeatureSupported

```java
public abstract boolean isFeatureSupported​(
String
feature)
```

Indicates whether a specified feature is supported.

**Parameters:** feature

- the feature name (as an absolute URI)
**Returns:** true

if the specified feature is supported,

false

otherwise
**Throws:** NullPointerException

- if

feature

is

null

- getURIDereferencer

```java
public abstract
URIDereferencer
getURIDereferencer()
```

Returns a reference to the

URIDereferencer

that is used by
default to dereference URIs in

RetrievalMethod

objects.

**Returns:** a reference to the default

URIDereferencer

- unmarshalKeyInfo

```java
public abstract
KeyInfo
unmarshalKeyInfo​(
XMLStructure
xmlStructure)
throws
MarshalException
```

Unmarshals a new

KeyInfo

instance from a
mechanism-specific

XMLStructure

(ex:

DOMStructure

)
instance.

**Parameters:** xmlStructure

- a mechanism-specific XML structure from which to
unmarshal the keyinfo from
**Returns:** the

KeyInfo
**Throws:** NullPointerException

- if

xmlStructure

is

null
**Throws:** ClassCastException

- if the type of

xmlStructure

is
inappropriate for this factory
**Throws:** MarshalException

- if an unrecoverable exception occurs during
unmarshalling

---

#### Method Detail

getInstance

```java
public static
KeyInfoFactory
getInstance​(
String
mechanismType)
```

Returns a

KeyInfoFactory

that supports the
specified XML processing mechanism and representation type (ex: "DOM").

This method uses the standard JCA provider lookup mechanism to
locate and instantiate a

KeyInfoFactory

implementation of
the desired mechanism type. It traverses the list of registered security

Provider

s, starting with the most preferred

Provider

. A new

KeyInfoFactory

object
from the first

Provider

that supports the specified
mechanism is returned.

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
**Parameters:** mechanismType

- the type of the XML processing mechanism and
representation. See the

Java Security Standard Algorithm Names

document
for more information.
**Returns:** a new

KeyInfoFactory
**Throws:** NullPointerException

- if

mechanismType

is

null
**Throws:** NoSuchMechanismException

- if no

Provider

supports a

KeyInfoFactory

implementation for the specified mechanism
**See Also:** Provider

---

#### getInstance

public static

KeyInfoFactory

getInstance​(

String

mechanismType)

Returns a

KeyInfoFactory

that supports the
specified XML processing mechanism and representation type (ex: "DOM").

This method uses the standard JCA provider lookup mechanism to
locate and instantiate a

KeyInfoFactory

implementation of
the desired mechanism type. It traverses the list of registered security

Provider

s, starting with the most preferred

Provider

. A new

KeyInfoFactory

object
from the first

Provider

that supports the specified
mechanism is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

This method uses the standard JCA provider lookup mechanism to
locate and instantiate a

KeyInfoFactory

implementation of
the desired mechanism type. It traverses the list of registered security

Provider

s, starting with the most preferred

Provider

. A new

KeyInfoFactory

object
from the first

Provider

that supports the specified
mechanism is returned.

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
KeyInfoFactory
getInstance​(
String
mechanismType,

Provider
provider)
```

Returns a

KeyInfoFactory

that supports the
requested XML processing mechanism and representation type (ex: "DOM"),
as supplied by the specified provider. Note that the specified

Provider

object does not have to be registered in the
provider list.

**Parameters:** mechanismType

- the type of the XML processing mechanism and
representation. See the

Java Security Standard Algorithm Names

document
for more information.
**Parameters:** provider

- the

Provider

object
**Returns:** a new

KeyInfoFactory
**Throws:** NullPointerException

- if

mechanismType

or

provider

are

null
**Throws:** NoSuchMechanismException

- if a

KeyInfoFactory

implementation for the specified mechanism is not available from the
specified

Provider

object
**See Also:** Provider

---

#### getInstance

public static

KeyInfoFactory

getInstance​(

String

mechanismType,

Provider

provider)

Returns a

KeyInfoFactory

that supports the
requested XML processing mechanism and representation type (ex: "DOM"),
as supplied by the specified provider. Note that the specified

Provider

object does not have to be registered in the
provider list.

getInstance

```java
public static
KeyInfoFactory
getInstance​(
String
mechanismType,

String
provider)
throws
NoSuchProviderException
```

Returns a

KeyInfoFactory

that supports the
requested XML processing mechanism and representation type (ex: "DOM"),
as supplied by the specified provider. The specified provider must be
registered in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:** mechanismType

- the type of the XML processing mechanism and
representation. See the

Java Security Standard Algorithm Names

document
for more information.
**Parameters:** provider

- the string name of the provider
**Returns:** a new

KeyInfoFactory
**Throws:** NoSuchProviderException

- if the specified provider is not
registered in the security provider list
**Throws:** NullPointerException

- if

mechanismType

or

provider

are

null
**Throws:** NoSuchMechanismException

- if a

KeyInfoFactory

implementation for the specified mechanism is not available from the
specified provider
**See Also:** Provider

---

#### getInstance

public static

KeyInfoFactory

getInstance​(

String

mechanismType,

String

provider)
throws

NoSuchProviderException

Returns a

KeyInfoFactory

that supports the
requested XML processing mechanism and representation type (ex: "DOM"),
as supplied by the specified provider. The specified provider must be
registered in the security provider list.

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
KeyInfoFactory
getInstance()
```

Returns a

KeyInfoFactory

that supports the
default XML processing mechanism and representation type ("DOM").

This method uses the standard JCA provider lookup mechanism to
locate and instantiate a

KeyInfoFactory

implementation of
the default mechanism type. It traverses the list of registered security

Provider

s, starting with the most preferred

Provider

. A new

KeyInfoFactory

object
from the first

Provider

that supports the DOM mechanism is
returned.

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
**Returns:** a new

KeyInfoFactory
**Throws:** NoSuchMechanismException

- if no

Provider

supports a

KeyInfoFactory

implementation for the DOM mechanism
**See Also:** Provider

---

#### getInstance

public static

KeyInfoFactory

getInstance()

Returns a

KeyInfoFactory

that supports the
default XML processing mechanism and representation type ("DOM").

This method uses the standard JCA provider lookup mechanism to
locate and instantiate a

KeyInfoFactory

implementation of
the default mechanism type. It traverses the list of registered security

Provider

s, starting with the most preferred

Provider

. A new

KeyInfoFactory

object
from the first

Provider

that supports the DOM mechanism is
returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

This method uses the standard JCA provider lookup mechanism to
locate and instantiate a

KeyInfoFactory

implementation of
the default mechanism type. It traverses the list of registered security

Provider

s, starting with the most preferred

Provider

. A new

KeyInfoFactory

object
from the first

Provider

that supports the DOM mechanism is
returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

getMechanismType

```java
public final
String
getMechanismType()
```

Returns the type of the XML processing mechanism and representation
supported by this

KeyInfoFactory

(ex: "DOM")

**Returns:** the XML processing mechanism type supported by this

KeyInfoFactory

---

#### getMechanismType

public final

String

getMechanismType()

Returns the type of the XML processing mechanism and representation
supported by this

KeyInfoFactory

(ex: "DOM")

getProvider

```java
public final
Provider
getProvider()
```

Returns the provider of this

KeyInfoFactory

.

**Returns:** the provider of this

KeyInfoFactory

---

#### getProvider

public final

Provider

getProvider()

Returns the provider of this

KeyInfoFactory

.

newKeyInfo

```java
public abstract
KeyInfo
newKeyInfo​(
List
<? extends
XMLStructure
> content)
```

Creates a

KeyInfo

containing the specified list of
key information types.

**Parameters:** content

- a list of one or more

XMLStructure

s representing
key information types. The list is defensively copied to protect
against subsequent modification.
**Returns:** a

KeyInfo
**Throws:** NullPointerException

- if

content

is

null
**Throws:** IllegalArgumentException

- if

content

is empty
**Throws:** ClassCastException

- if

content

contains any entries
that are not of type

XMLStructure

---

#### newKeyInfo

public abstract

KeyInfo

newKeyInfo​(

List

<? extends

XMLStructure

> content)

Creates a

KeyInfo

containing the specified list of
key information types.

newKeyInfo

```java
public abstract
KeyInfo
newKeyInfo​(
List
<? extends
XMLStructure
> content,

String
id)
```

Creates a

KeyInfo

containing the specified list of key
information types and optional id. The

id

parameter represents the value of an XML

ID

attribute and is useful for referencing
the

KeyInfo

from other XML structures.

**Parameters:** content

- a list of one or more

XMLStructure

s representing
key information types. The list is defensively copied to protect
against subsequent modification.
**Parameters:** id

- the value of an XML

ID

(may be

null

)
**Returns:** a

KeyInfo
**Throws:** NullPointerException

- if

content

is

null
**Throws:** IllegalArgumentException

- if

content

is empty
**Throws:** ClassCastException

- if

content

contains any entries
that are not of type

XMLStructure

---

#### newKeyInfo

public abstract

KeyInfo

newKeyInfo​(

List

<? extends

XMLStructure

> content,

String

id)

Creates a

KeyInfo

containing the specified list of key
information types and optional id. The

id

parameter represents the value of an XML

ID

attribute and is useful for referencing
the

KeyInfo

from other XML structures.

newKeyName

```java
public abstract
KeyName
newKeyName​(
String
name)
```

Creates a

KeyName

from the specified name.

**Parameters:** name

- the name that identifies the key
**Returns:** a

KeyName
**Throws:** NullPointerException

- if

name

is

null

---

#### newKeyName

public abstract

KeyName

newKeyName​(

String

name)

Creates a

KeyName

from the specified name.

newKeyValue

```java
public abstract
KeyValue
newKeyValue​(
PublicKey
key)
throws
KeyException
```

Creates a

KeyValue

from the specified public key.

**Parameters:** key

- the public key
**Returns:** a

KeyValue
**Throws:** KeyException

- if the

key

's algorithm is not
recognized or supported by this

KeyInfoFactory
**Throws:** NullPointerException

- if

key

is

null

---

#### newKeyValue

public abstract

KeyValue

newKeyValue​(

PublicKey

key)
throws

KeyException

Creates a

KeyValue

from the specified public key.

newPGPData

```java
public abstract
PGPData
newPGPData​(byte[] keyId)
```

Creates a

PGPData

from the specified PGP public key
identifier.

**Parameters:** keyId

- a PGP public key identifier as defined in

RFC 2440

, section 11.2.
The array is cloned to protect against subsequent modification.
**Returns:** a

PGPData
**Throws:** NullPointerException

- if

keyId

is

null
**Throws:** IllegalArgumentException

- if the key id is not in the correct
format

---

#### newPGPData

public abstract

PGPData

newPGPData​(byte[] keyId)

Creates a

PGPData

from the specified PGP public key
identifier.

newPGPData

```java
public abstract
PGPData
newPGPData​(byte[] keyId,
byte[] keyPacket,

List
<? extends
XMLStructure
> other)
```

Creates a

PGPData

from the specified PGP public key
identifier, and optional key material packet and list of external
elements.

**Parameters:** keyId

- a PGP public key identifier as defined in

RFC 2440

, section 11.2.
The array is cloned to protect against subsequent modification.
**Parameters:** keyPacket

- a PGP key material packet as defined in

RFC 2440

, section 5.5.
The array is cloned to protect against subsequent modification. May
be

null

.
**Parameters:** other

- a list of

XMLStructure

s representing elements from
an external namespace. The list is defensively copied to protect
against subsequent modification. May be

null

or empty.
**Returns:** a

PGPData
**Throws:** NullPointerException

- if

keyId

is

null
**Throws:** IllegalArgumentException

- if the

keyId

or

keyPacket

is not in the correct format. For

keyPacket

, the format of the packet header is
checked and the tag is verified that it is of type key material. The
contents and format of the packet body are not checked.
**Throws:** ClassCastException

- if

other

contains any
entries that are not of type

XMLStructure

---

#### newPGPData

public abstract

PGPData

newPGPData​(byte[] keyId,
byte[] keyPacket,

List

<? extends

XMLStructure

> other)

Creates a

PGPData

from the specified PGP public key
identifier, and optional key material packet and list of external
elements.

newPGPData

```java
public abstract
PGPData
newPGPData​(byte[] keyPacket,

List
<? extends
XMLStructure
> other)
```

Creates a

PGPData

from the specified PGP key material
packet and optional list of external elements.

**Parameters:** keyPacket

- a PGP key material packet as defined in

RFC 2440

, section 5.5.
The array is cloned to protect against subsequent modification.
**Parameters:** other

- a list of

XMLStructure

s representing elements from
an external namespace. The list is defensively copied to protect
against subsequent modification. May be

null

or empty.
**Returns:** a

PGPData
**Throws:** NullPointerException

- if

keyPacket

is

null
**Throws:** IllegalArgumentException

- if

keyPacket

is not in the
correct format. For

keyPacket

, the format of the packet
header is checked and the tag is verified that it is of type key
material. The contents and format of the packet body are not checked.
**Throws:** ClassCastException

- if

other

contains any
entries that are not of type

XMLStructure

---

#### newPGPData

public abstract

PGPData

newPGPData​(byte[] keyPacket,

List

<? extends

XMLStructure

> other)

Creates a

PGPData

from the specified PGP key material
packet and optional list of external elements.

newRetrievalMethod

```java
public abstract
RetrievalMethod
newRetrievalMethod​(
String
uri)
```

Creates a

RetrievalMethod

from the specified URI.

**Parameters:** uri

- the URI that identifies the

KeyInfo

information
to be retrieved
**Returns:** a

RetrievalMethod
**Throws:** NullPointerException

- if

uri

is

null
**Throws:** IllegalArgumentException

- if

uri

is not RFC 2396
compliant

---

#### newRetrievalMethod

public abstract

RetrievalMethod

newRetrievalMethod​(

String

uri)

Creates a

RetrievalMethod

from the specified URI.

newRetrievalMethod

```java
public abstract
RetrievalMethod
newRetrievalMethod​(
String
uri,

String
type,

List
<? extends
Transform
> transforms)
```

Creates a

RetrievalMethod

from the specified parameters.

**Parameters:** uri

- the URI that identifies the

KeyInfo

information
to be retrieved
**Parameters:** type

- a URI that identifies the type of

KeyInfo

information to be retrieved (may be

null

)
**Parameters:** transforms

- a list of

Transform

s. The list is defensively
copied to protect against subsequent modification. May be

null

or empty.
**Returns:** a

RetrievalMethod
**Throws:** NullPointerException

- if

uri

is

null
**Throws:** IllegalArgumentException

- if

uri

is not RFC 2396
compliant
**Throws:** ClassCastException

- if

transforms

contains any
entries that are not of type

Transform

---

#### newRetrievalMethod

public abstract

RetrievalMethod

newRetrievalMethod​(

String

uri,

String

type,

List

<? extends

Transform

> transforms)

Creates a

RetrievalMethod

from the specified parameters.

newX509Data

```java
public abstract
X509Data
newX509Data​(
List
<?> content)
```

Creates a

X509Data

containing the specified list of
X.509 content.

**Parameters:** content

- a list of one or more X.509 content types. Valid types are

String

(subject names),

byte[]

(subject key ids),

X509Certificate

,

X509CRL

,
or

XMLStructure

(

X509IssuerSerial

objects or elements from an external namespace). Subject names are
distinguished names in RFC 2253 String format. Implementations MUST
support the attribute type keywords defined in RFC 2253 (CN, L, ST,
O, OU, C, STREET, DC and UID). Implementations MAY support additional
keywords. The list is defensively copied to protect against
subsequent modification.
**Returns:** a

X509Data
**Throws:** NullPointerException

- if

content

is

null
**Throws:** IllegalArgumentException

- if

content

is empty, or
if a subject name is not RFC 2253 compliant or one of the attribute
type keywords is not recognized.
**Throws:** ClassCastException

- if

content

contains any entries
that are not of one of the valid types mentioned above

---

#### newX509Data

public abstract

X509Data

newX509Data​(

List

<?> content)

Creates a

X509Data

containing the specified list of
X.509 content.

newX509IssuerSerial

```java
public abstract
X509IssuerSerial
newX509IssuerSerial​(
String
issuerName,

BigInteger
serialNumber)
```

Creates an

X509IssuerSerial

from the specified X.500 issuer
distinguished name and serial number.

**Parameters:** issuerName

- the issuer's distinguished name in RFC 2253 String
format. Implementations MUST support the attribute type keywords
defined in RFC 2253 (CN, L, ST, O, OU, C, STREET, DC and UID).
Implementations MAY support additional keywords.
**Parameters:** serialNumber

- the serial number
**Returns:** an

X509IssuerSerial
**Throws:** NullPointerException

- if

issuerName

or

serialNumber

are

null
**Throws:** IllegalArgumentException

- if the issuer name is not RFC 2253
compliant or one of the attribute type keywords is not recognized.

---

#### newX509IssuerSerial

public abstract

X509IssuerSerial

newX509IssuerSerial​(

String

issuerName,

BigInteger

serialNumber)

Creates an

X509IssuerSerial

from the specified X.500 issuer
distinguished name and serial number.

isFeatureSupported

```java
public abstract boolean isFeatureSupported​(
String
feature)
```

Indicates whether a specified feature is supported.

**Parameters:** feature

- the feature name (as an absolute URI)
**Returns:** true

if the specified feature is supported,

false

otherwise
**Throws:** NullPointerException

- if

feature

is

null

---

#### isFeatureSupported

public abstract boolean isFeatureSupported​(

String

feature)

Indicates whether a specified feature is supported.

getURIDereferencer

```java
public abstract
URIDereferencer
getURIDereferencer()
```

Returns a reference to the

URIDereferencer

that is used by
default to dereference URIs in

RetrievalMethod

objects.

**Returns:** a reference to the default

URIDereferencer

---

#### getURIDereferencer

public abstract

URIDereferencer

getURIDereferencer()

Returns a reference to the

URIDereferencer

that is used by
default to dereference URIs in

RetrievalMethod

objects.

unmarshalKeyInfo

```java
public abstract
KeyInfo
unmarshalKeyInfo​(
XMLStructure
xmlStructure)
throws
MarshalException
```

Unmarshals a new

KeyInfo

instance from a
mechanism-specific

XMLStructure

(ex:

DOMStructure

)
instance.

**Parameters:** xmlStructure

- a mechanism-specific XML structure from which to
unmarshal the keyinfo from
**Returns:** the

KeyInfo
**Throws:** NullPointerException

- if

xmlStructure

is

null
**Throws:** ClassCastException

- if the type of

xmlStructure

is
inappropriate for this factory
**Throws:** MarshalException

- if an unrecoverable exception occurs during
unmarshalling

---

#### unmarshalKeyInfo

public abstract

KeyInfo

unmarshalKeyInfo​(

XMLStructure

xmlStructure)
throws

MarshalException

Unmarshals a new

KeyInfo

instance from a
mechanism-specific

XMLStructure

(ex:

DOMStructure

)
instance.

---

