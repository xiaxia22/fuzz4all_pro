# Class TransformService

**Source:** `java.xml.crypto\javax\xml\crypto\dsig\TransformService.html`

### Class Description

```java
public abstract class
TransformService

extends
Object

implements
Transform
```

A Service Provider Interface for transform and canonicalization algorithms.

Each instance of

TransformService

supports a specific
transform or canonicalization algorithm and XML mechanism type. To create a

TransformService

, call one of the static

getInstance

methods, passing in the algorithm URI and
XML mechanism type desired, for example:

TransformService ts = TransformService.getInstance(Transform.XPATH2, "DOM");

TransformService

implementations are registered and loaded
using the

Provider

mechanism. Each

TransformService

service provider implementation should include
a

MechanismType

service attribute that identifies the XML
mechanism type that it supports. If the attribute is not specified,
"DOM" is assumed. For example, a service provider that supports the
XPath Filter 2 Transform and DOM mechanism would be specified in the

Provider

subclass as:

```java
put("TransformService." + Transform.XPATH2,
"org.example.XPath2TransformService");
put("TransformService." + Transform.XPATH2 + " MechanismType", "DOM");
```

TransformService

implementations that support the DOM
mechanism type must abide by the DOM interoperability requirements defined
in the

DOM Mechanism Requirements

section
of the API overview. See the

Service Providers

section of
the API overview for a list of standard mechanism types.

Once a

TransformService

has been created, it can be used
to process

Transform

or

CanonicalizationMethod

objects. If the

Transform

or

CanonicalizationMethod

exists in XML form (for example, when validating an existing

XMLSignature

), the

init(XMLStructure, XMLCryptoContext)

method must be first called to initialize the transform and provide document
context (even if there are no parameters). Alternatively, if the

Transform

or

CanonicalizationMethod

is being
created from scratch, the

init(TransformParameterSpec)

method
is called to initialize the transform with parameters and the

marshalParams

method is called to marshal the
parameters to XML and provide the transform with document context. Finally,
the

transform

method is called to perform the
transformation.

Concurrent Access

The static methods of this class are guaranteed to be thread-safe.
Multiple threads may concurrently invoke the static methods defined in this
class with no ill effects.

However, this is not true for the non-static methods defined by this
class. Unless otherwise documented by a specific provider, threads that
need to access a single

TransformService

instance
concurrently should synchronize amongst themselves and provide the
necessary locking. Multiple threads each manipulating a different

TransformService

instance need not synchronize.

**All Implemented Interfaces:** AlgorithmMethod

,

Transform

,

XMLStructure

---

### Field Details

*No entries found.*

### Constructor Details

#### protected TransformService()

Default constructor, for invocation by subclasses.

---

### Method Details

#### public static
TransformService
getInstance​(
String
algorithm,

String
mechanismType)
throws
NoSuchAlgorithmException

Returns a

TransformService

that supports the specified
algorithm URI (ex:

Transform.XPATH2

) and mechanism type
(ex: DOM).

This method uses the standard JCA provider lookup mechanism to
locate and instantiate a

TransformService

implementation
of the desired algorithm and

MechanismType

service
attribute. It traverses the list of registered security

Provider

s, starting with the most preferred

Provider

. A new

TransformService

object
from the first

Provider

that supports the specified
algorithm and mechanism type is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:**
- algorithm

- the URI of the algorithm
- mechanismType

- the type of the XML processing mechanism and
representation

**Returns:**
- a new

TransformService

**Throws:**
- NullPointerException

- if

algorithm

or

mechanismType

is

null
- NoSuchAlgorithmException

- if no

Provider

supports a

TransformService

implementation for the specified
algorithm and mechanism type

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
TransformService
getInstance​(
String
algorithm,

String
mechanismType,

Provider
provider)
throws
NoSuchAlgorithmException

Returns a

TransformService

that supports the specified
algorithm URI (ex:

Transform.XPATH2

) and mechanism type
(ex: DOM) as supplied by the specified provider. Note that the specified

Provider

object does not have to be registered in the
provider list.

**Parameters:**
- algorithm

- the URI of the algorithm
- mechanismType

- the type of the XML processing mechanism and
representation
- provider

- the

Provider

object

**Returns:**
- a new

TransformService

**Throws:**
- NullPointerException

- if

provider

,

algorithm

, or

mechanismType

is

null
- NoSuchAlgorithmException

- if a

TransformService

implementation for the specified algorithm and mechanism type is not
available from the specified

Provider

object

**See Also:**
- Provider

---

#### public static
TransformService
getInstance​(
String
algorithm,

String
mechanismType,

String
provider)
throws
NoSuchAlgorithmException
,

NoSuchProviderException

Returns a

TransformService

that supports the specified
algorithm URI (ex:

Transform.XPATH2

) and mechanism type
(ex: DOM) as supplied by the specified provider. The specified provider
must be registered in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:**
- algorithm

- the URI of the algorithm
- mechanismType

- the type of the XML processing mechanism and
representation
- provider

- the string name of the provider

**Returns:**
- a new

TransformService

**Throws:**
- NoSuchProviderException

- if the specified provider is not
registered in the security provider list
- NullPointerException

- if

provider

,

mechanismType

, or

algorithm

is

null
- NoSuchAlgorithmException

- if a

TransformService

implementation for the specified algorithm and mechanism type is not
available from the specified provider

**See Also:**
- Provider

---

#### public final
String
getMechanismType()

Returns the mechanism type supported by this

TransformService

.

**Returns:**
- the mechanism type

---

#### public final
String
getAlgorithm()

Returns the URI of the algorithm supported by this

TransformService

.

**Specified by:**
- getAlgorithm

in interface

AlgorithmMethod

**Returns:**
- the algorithm URI

---

#### public final
Provider
getProvider()

Returns the provider of this

TransformService

.

**Returns:**
- the provider

---

#### public abstract void init​(
TransformParameterSpec
params)
throws
InvalidAlgorithmParameterException

Initializes this

TransformService

with the specified
parameters.

If the parameters exist in XML form, the

init(XMLStructure, XMLCryptoContext)

method should be used to
initialize the

TransformService

.

**Parameters:**
- params

- the algorithm parameters (may be

null

if
not required or optional)

**Throws:**
- InvalidAlgorithmParameterException

- if the specified parameters
are invalid for this algorithm

---

#### public abstract void marshalParams​(
XMLStructure
parent,

XMLCryptoContext
context)
throws
MarshalException

Marshals the algorithm-specific parameters. If there are no parameters
to be marshalled, this method returns without throwing an exception.

**Parameters:**
- parent

- a mechanism-specific structure containing the parent
node that the marshalled parameters should be appended to
- context

- the

XMLCryptoContext

containing
additional context (may be

null

if not applicable)

**Throws:**
- ClassCastException

- if the type of

parent

or

context

is not compatible with this

TransformService
- NullPointerException

- if

parent

is

null
- MarshalException

- if the parameters cannot be marshalled

---

#### public abstract void init​(
XMLStructure
parent,

XMLCryptoContext
context)
throws
InvalidAlgorithmParameterException

Initializes this

TransformService

with the specified
parameters and document context.

**Parameters:**
- parent

- a mechanism-specific structure containing the parent
structure
- context

- the

XMLCryptoContext

containing
additional context (may be

null

if not applicable)

**Throws:**
- ClassCastException

- if the type of

parent

or

context

is not compatible with this

TransformService
- NullPointerException

- if

parent

is

null
- InvalidAlgorithmParameterException

- if the specified parameters
are invalid for this algorithm

---

### Additional Sections

#### Class TransformService

java.lang.Object

- javax.xml.crypto.dsig.TransformService

javax.xml.crypto.dsig.TransformService

**All Implemented Interfaces:** AlgorithmMethod

,

Transform

,

XMLStructure

```java
public abstract class
TransformService

extends
Object

implements
Transform
```

A Service Provider Interface for transform and canonicalization algorithms.

Each instance of

TransformService

supports a specific
transform or canonicalization algorithm and XML mechanism type. To create a

TransformService

, call one of the static

getInstance

methods, passing in the algorithm URI and
XML mechanism type desired, for example:

TransformService ts = TransformService.getInstance(Transform.XPATH2, "DOM");

TransformService

implementations are registered and loaded
using the

Provider

mechanism. Each

TransformService

service provider implementation should include
a

MechanismType

service attribute that identifies the XML
mechanism type that it supports. If the attribute is not specified,
"DOM" is assumed. For example, a service provider that supports the
XPath Filter 2 Transform and DOM mechanism would be specified in the

Provider

subclass as:

```java
put("TransformService." + Transform.XPATH2,
"org.example.XPath2TransformService");
put("TransformService." + Transform.XPATH2 + " MechanismType", "DOM");
```

TransformService

implementations that support the DOM
mechanism type must abide by the DOM interoperability requirements defined
in the

DOM Mechanism Requirements

section
of the API overview. See the

Service Providers

section of
the API overview for a list of standard mechanism types.

Once a

TransformService

has been created, it can be used
to process

Transform

or

CanonicalizationMethod

objects. If the

Transform

or

CanonicalizationMethod

exists in XML form (for example, when validating an existing

XMLSignature

), the

init(XMLStructure, XMLCryptoContext)

method must be first called to initialize the transform and provide document
context (even if there are no parameters). Alternatively, if the

Transform

or

CanonicalizationMethod

is being
created from scratch, the

init(TransformParameterSpec)

method
is called to initialize the transform with parameters and the

marshalParams

method is called to marshal the
parameters to XML and provide the transform with document context. Finally,
the

transform

method is called to perform the
transformation.

Concurrent Access

The static methods of this class are guaranteed to be thread-safe.
Multiple threads may concurrently invoke the static methods defined in this
class with no ill effects.

However, this is not true for the non-static methods defined by this
class. Unless otherwise documented by a specific provider, threads that
need to access a single

TransformService

instance
concurrently should synchronize amongst themselves and provide the
necessary locking. Multiple threads each manipulating a different

TransformService

instance need not synchronize.

**Since:** 1.6

public abstract class

TransformService

extends

Object

implements

Transform

A Service Provider Interface for transform and canonicalization algorithms.

Each instance of

TransformService

supports a specific
transform or canonicalization algorithm and XML mechanism type. To create a

TransformService

, call one of the static

getInstance

methods, passing in the algorithm URI and
XML mechanism type desired, for example:

TransformService ts = TransformService.getInstance(Transform.XPATH2, "DOM");

TransformService

implementations are registered and loaded
using the

Provider

mechanism. Each

TransformService

service provider implementation should include
a

MechanismType

service attribute that identifies the XML
mechanism type that it supports. If the attribute is not specified,
"DOM" is assumed. For example, a service provider that supports the
XPath Filter 2 Transform and DOM mechanism would be specified in the

Provider

subclass as:

```java
put("TransformService." + Transform.XPATH2,
"org.example.XPath2TransformService");
put("TransformService." + Transform.XPATH2 + " MechanismType", "DOM");
```

TransformService

implementations that support the DOM
mechanism type must abide by the DOM interoperability requirements defined
in the

DOM Mechanism Requirements

section
of the API overview. See the

Service Providers

section of
the API overview for a list of standard mechanism types.

Once a

TransformService

has been created, it can be used
to process

Transform

or

CanonicalizationMethod

objects. If the

Transform

or

CanonicalizationMethod

exists in XML form (for example, when validating an existing

XMLSignature

), the

init(XMLStructure, XMLCryptoContext)

method must be first called to initialize the transform and provide document
context (even if there are no parameters). Alternatively, if the

Transform

or

CanonicalizationMethod

is being
created from scratch, the

init(TransformParameterSpec)

method
is called to initialize the transform with parameters and the

marshalParams

method is called to marshal the
parameters to XML and provide the transform with document context. Finally,
the

transform

method is called to perform the
transformation.

Concurrent Access

The static methods of this class are guaranteed to be thread-safe.
Multiple threads may concurrently invoke the static methods defined in this
class with no ill effects.

However, this is not true for the non-static methods defined by this
class. Unless otherwise documented by a specific provider, threads that
need to access a single

TransformService

instance
concurrently should synchronize amongst themselves and provide the
necessary locking. Multiple threads each manipulating a different

TransformService

instance need not synchronize.

Each instance of

TransformService

supports a specific
transform or canonicalization algorithm and XML mechanism type. To create a

TransformService

, call one of the static

getInstance

methods, passing in the algorithm URI and
XML mechanism type desired, for example:

TransformService ts = TransformService.getInstance(Transform.XPATH2, "DOM");

TransformService

implementations are registered and loaded
using the

Provider

mechanism. Each

TransformService

service provider implementation should include
a

MechanismType

service attribute that identifies the XML
mechanism type that it supports. If the attribute is not specified,
"DOM" is assumed. For example, a service provider that supports the
XPath Filter 2 Transform and DOM mechanism would be specified in the

Provider

subclass as:

```java
put("TransformService." + Transform.XPATH2,
"org.example.XPath2TransformService");
put("TransformService." + Transform.XPATH2 + " MechanismType", "DOM");
```

TransformService

implementations that support the DOM
mechanism type must abide by the DOM interoperability requirements defined
in the

DOM Mechanism Requirements

section
of the API overview. See the

Service Providers

section of
the API overview for a list of standard mechanism types.

Once a

TransformService

has been created, it can be used
to process

Transform

or

CanonicalizationMethod

objects. If the

Transform

or

CanonicalizationMethod

exists in XML form (for example, when validating an existing

XMLSignature

), the

init(XMLStructure, XMLCryptoContext)

method must be first called to initialize the transform and provide document
context (even if there are no parameters). Alternatively, if the

Transform

or

CanonicalizationMethod

is being
created from scratch, the

init(TransformParameterSpec)

method
is called to initialize the transform with parameters and the

marshalParams

method is called to marshal the
parameters to XML and provide the transform with document context. Finally,
the

transform

method is called to perform the
transformation.

Concurrent Access

The static methods of this class are guaranteed to be thread-safe.
Multiple threads may concurrently invoke the static methods defined in this
class with no ill effects.

However, this is not true for the non-static methods defined by this
class. Unless otherwise documented by a specific provider, threads that
need to access a single

TransformService

instance
concurrently should synchronize amongst themselves and provide the
necessary locking. Multiple threads each manipulating a different

TransformService

instance need not synchronize.

TransformService

implementations are registered and loaded
using the

Provider

mechanism. Each

TransformService

service provider implementation should include
a

MechanismType

service attribute that identifies the XML
mechanism type that it supports. If the attribute is not specified,
"DOM" is assumed. For example, a service provider that supports the
XPath Filter 2 Transform and DOM mechanism would be specified in the

Provider

subclass as:

```java
put("TransformService." + Transform.XPATH2,
"org.example.XPath2TransformService");
put("TransformService." + Transform.XPATH2 + " MechanismType", "DOM");
```

TransformService

implementations that support the DOM
mechanism type must abide by the DOM interoperability requirements defined
in the

DOM Mechanism Requirements

section
of the API overview. See the

Service Providers

section of
the API overview for a list of standard mechanism types.

Once a

TransformService

has been created, it can be used
to process

Transform

or

CanonicalizationMethod

objects. If the

Transform

or

CanonicalizationMethod

exists in XML form (for example, when validating an existing

XMLSignature

), the

init(XMLStructure, XMLCryptoContext)

method must be first called to initialize the transform and provide document
context (even if there are no parameters). Alternatively, if the

Transform

or

CanonicalizationMethod

is being
created from scratch, the

init(TransformParameterSpec)

method
is called to initialize the transform with parameters and the

marshalParams

method is called to marshal the
parameters to XML and provide the transform with document context. Finally,
the

transform

method is called to perform the
transformation.

Concurrent Access

The static methods of this class are guaranteed to be thread-safe.
Multiple threads may concurrently invoke the static methods defined in this
class with no ill effects.

However, this is not true for the non-static methods defined by this
class. Unless otherwise documented by a specific provider, threads that
need to access a single

TransformService

instance
concurrently should synchronize amongst themselves and provide the
necessary locking. Multiple threads each manipulating a different

TransformService

instance need not synchronize.

put("TransformService." + Transform.XPATH2,
"org.example.XPath2TransformService");
put("TransformService." + Transform.XPATH2 + " MechanismType", "DOM");

Once a

TransformService

has been created, it can be used
to process

Transform

or

CanonicalizationMethod

objects. If the

Transform

or

CanonicalizationMethod

exists in XML form (for example, when validating an existing

XMLSignature

), the

init(XMLStructure, XMLCryptoContext)

method must be first called to initialize the transform and provide document
context (even if there are no parameters). Alternatively, if the

Transform

or

CanonicalizationMethod

is being
created from scratch, the

init(TransformParameterSpec)

method
is called to initialize the transform with parameters and the

marshalParams

method is called to marshal the
parameters to XML and provide the transform with document context. Finally,
the

transform

method is called to perform the
transformation.

Concurrent Access

The static methods of this class are guaranteed to be thread-safe.
Multiple threads may concurrently invoke the static methods defined in this
class with no ill effects.

However, this is not true for the non-static methods defined by this
class. Unless otherwise documented by a specific provider, threads that
need to access a single

TransformService

instance
concurrently should synchronize amongst themselves and provide the
necessary locking. Multiple threads each manipulating a different

TransformService

instance need not synchronize.

Concurrent Access

The static methods of this class are guaranteed to be thread-safe.
Multiple threads may concurrently invoke the static methods defined in this
class with no ill effects.

However, this is not true for the non-static methods defined by this
class. Unless otherwise documented by a specific provider, threads that
need to access a single

TransformService

instance
concurrently should synchronize amongst themselves and provide the
necessary locking. Multiple threads each manipulating a different

TransformService

instance need not synchronize.

The static methods of this class are guaranteed to be thread-safe.
Multiple threads may concurrently invoke the static methods defined in this
class with no ill effects.

However, this is not true for the non-static methods defined by this
class. Unless otherwise documented by a specific provider, threads that
need to access a single

TransformService

instance
concurrently should synchronize amongst themselves and provide the
necessary locking. Multiple threads each manipulating a different

TransformService

instance need not synchronize.

However, this is not true for the non-static methods defined by this
class. Unless otherwise documented by a specific provider, threads that
need to access a single

TransformService

instance
concurrently should synchronize amongst themselves and provide the
necessary locking. Multiple threads each manipulating a different

TransformService

instance need not synchronize.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in interface javax.xml.crypto.dsig.

Transform

BASE64

,

ENVELOPED

,

XPATH

,

XPATH2

,

XSLT

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

TransformService

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

String

getAlgorithm

()

Returns the URI of the algorithm supported by this

TransformService

.

static

TransformService

getInstance

​(

String

algorithm,

String

mechanismType)

Returns a

TransformService

that supports the specified
algorithm URI (ex:

Transform.XPATH2

) and mechanism type
(ex: DOM).

static

TransformService

getInstance

​(

String

algorithm,

String

mechanismType,

String

provider)

Returns a

TransformService

that supports the specified
algorithm URI (ex:

Transform.XPATH2

) and mechanism type
(ex: DOM) as supplied by the specified provider.

static

TransformService

getInstance

​(

String

algorithm,

String

mechanismType,

Provider

provider)

Returns a

TransformService

that supports the specified
algorithm URI (ex:

Transform.XPATH2

) and mechanism type
(ex: DOM) as supplied by the specified provider.

String

getMechanismType

()

Returns the mechanism type supported by this

TransformService

.

Provider

getProvider

()

Returns the provider of this

TransformService

.

abstract void

init

​(

TransformParameterSpec

params)

Initializes this

TransformService

with the specified
parameters.

abstract void

init

​(

XMLStructure

parent,

XMLCryptoContext

context)

Initializes this

TransformService

with the specified
parameters and document context.

abstract void

marshalParams

​(

XMLStructure

parent,

XMLCryptoContext

context)

Marshals the algorithm-specific parameters.

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

- Methods declared in interface javax.xml.crypto.dsig.

Transform

getParameterSpec

,

transform

,

transform

- Methods declared in interface javax.xml.crypto.

XMLStructure

isFeatureSupported

Field Summary

- Fields declared in interface javax.xml.crypto.dsig.

Transform

BASE64

,

ENVELOPED

,

XPATH

,

XPATH2

,

XSLT

---

#### Field Summary

Fields declared in interface javax.xml.crypto.dsig.

Transform

BASE64

,

ENVELOPED

,

XPATH

,

XPATH2

,

XSLT

---

#### Fields declared in interface javax.xml.crypto.dsig. Transform

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

TransformService

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

String

getAlgorithm

()

Returns the URI of the algorithm supported by this

TransformService

.

static

TransformService

getInstance

​(

String

algorithm,

String

mechanismType)

Returns a

TransformService

that supports the specified
algorithm URI (ex:

Transform.XPATH2

) and mechanism type
(ex: DOM).

static

TransformService

getInstance

​(

String

algorithm,

String

mechanismType,

String

provider)

Returns a

TransformService

that supports the specified
algorithm URI (ex:

Transform.XPATH2

) and mechanism type
(ex: DOM) as supplied by the specified provider.

static

TransformService

getInstance

​(

String

algorithm,

String

mechanismType,

Provider

provider)

Returns a

TransformService

that supports the specified
algorithm URI (ex:

Transform.XPATH2

) and mechanism type
(ex: DOM) as supplied by the specified provider.

String

getMechanismType

()

Returns the mechanism type supported by this

TransformService

.

Provider

getProvider

()

Returns the provider of this

TransformService

.

abstract void

init

​(

TransformParameterSpec

params)

Initializes this

TransformService

with the specified
parameters.

abstract void

init

​(

XMLStructure

parent,

XMLCryptoContext

context)

Initializes this

TransformService

with the specified
parameters and document context.

abstract void

marshalParams

​(

XMLStructure

parent,

XMLCryptoContext

context)

Marshals the algorithm-specific parameters.

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

- Methods declared in interface javax.xml.crypto.dsig.

Transform

getParameterSpec

,

transform

,

transform

- Methods declared in interface javax.xml.crypto.

XMLStructure

isFeatureSupported

---

#### Method Summary

Returns the URI of the algorithm supported by this

TransformService

.

Returns a

TransformService

that supports the specified
algorithm URI (ex:

Transform.XPATH2

) and mechanism type
(ex: DOM).

Returns a

TransformService

that supports the specified
algorithm URI (ex:

Transform.XPATH2

) and mechanism type
(ex: DOM) as supplied by the specified provider.

Returns the mechanism type supported by this

TransformService

.

Returns the provider of this

TransformService

.

Initializes this

TransformService

with the specified
parameters.

Initializes this

TransformService

with the specified
parameters and document context.

Marshals the algorithm-specific parameters.

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

Methods declared in interface javax.xml.crypto.dsig.

Transform

getParameterSpec

,

transform

,

transform

---

#### Methods declared in interface javax.xml.crypto.dsig. Transform

Methods declared in interface javax.xml.crypto.

XMLStructure

isFeatureSupported

---

#### Methods declared in interface javax.xml.crypto. XMLStructure

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- TransformService

```java
protected TransformService()
```

Default constructor, for invocation by subclasses.

============ METHOD DETAIL ==========

- Method Detail

- getInstance

```java
public static
TransformService
getInstance​(
String
algorithm,

String
mechanismType)
throws
NoSuchAlgorithmException
```

Returns a

TransformService

that supports the specified
algorithm URI (ex:

Transform.XPATH2

) and mechanism type
(ex: DOM).

This method uses the standard JCA provider lookup mechanism to
locate and instantiate a

TransformService

implementation
of the desired algorithm and

MechanismType

service
attribute. It traverses the list of registered security

Provider

s, starting with the most preferred

Provider

. A new

TransformService

object
from the first

Provider

that supports the specified
algorithm and mechanism type is returned.

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
**Parameters:** algorithm

- the URI of the algorithm
**Parameters:** mechanismType

- the type of the XML processing mechanism and
representation
**Returns:** a new

TransformService
**Throws:** NullPointerException

- if

algorithm

or

mechanismType

is

null
**Throws:** NoSuchAlgorithmException

- if no

Provider

supports a

TransformService

implementation for the specified
algorithm and mechanism type
**See Also:** Provider

- getInstance

```java
public static
TransformService
getInstance​(
String
algorithm,

String
mechanismType,

Provider
provider)
throws
NoSuchAlgorithmException
```

Returns a

TransformService

that supports the specified
algorithm URI (ex:

Transform.XPATH2

) and mechanism type
(ex: DOM) as supplied by the specified provider. Note that the specified

Provider

object does not have to be registered in the
provider list.

**Parameters:** algorithm

- the URI of the algorithm
**Parameters:** mechanismType

- the type of the XML processing mechanism and
representation
**Parameters:** provider

- the

Provider

object
**Returns:** a new

TransformService
**Throws:** NullPointerException

- if

provider

,

algorithm

, or

mechanismType

is

null
**Throws:** NoSuchAlgorithmException

- if a

TransformService

implementation for the specified algorithm and mechanism type is not
available from the specified

Provider

object
**See Also:** Provider

- getInstance

```java
public static
TransformService
getInstance​(
String
algorithm,

String
mechanismType,

String
provider)
throws
NoSuchAlgorithmException
,

NoSuchProviderException
```

Returns a

TransformService

that supports the specified
algorithm URI (ex:

Transform.XPATH2

) and mechanism type
(ex: DOM) as supplied by the specified provider. The specified provider
must be registered in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:** algorithm

- the URI of the algorithm
**Parameters:** mechanismType

- the type of the XML processing mechanism and
representation
**Parameters:** provider

- the string name of the provider
**Returns:** a new

TransformService
**Throws:** NoSuchProviderException

- if the specified provider is not
registered in the security provider list
**Throws:** NullPointerException

- if

provider

,

mechanismType

, or

algorithm

is

null
**Throws:** NoSuchAlgorithmException

- if a

TransformService

implementation for the specified algorithm and mechanism type is not
available from the specified provider
**See Also:** Provider

- getMechanismType

```java
public final
String
getMechanismType()
```

Returns the mechanism type supported by this

TransformService

.

**Returns:** the mechanism type

- getAlgorithm

```java
public final
String
getAlgorithm()
```

Returns the URI of the algorithm supported by this

TransformService

.

**Specified by:** getAlgorithm

in interface

AlgorithmMethod
**Returns:** the algorithm URI

- getProvider

```java
public final
Provider
getProvider()
```

Returns the provider of this

TransformService

.

**Returns:** the provider

- init

```java
public abstract void init​(
TransformParameterSpec
params)
throws
InvalidAlgorithmParameterException
```

Initializes this

TransformService

with the specified
parameters.

If the parameters exist in XML form, the

init(XMLStructure, XMLCryptoContext)

method should be used to
initialize the

TransformService

.

**Parameters:** params

- the algorithm parameters (may be

null

if
not required or optional)
**Throws:** InvalidAlgorithmParameterException

- if the specified parameters
are invalid for this algorithm

- marshalParams

```java
public abstract void marshalParams​(
XMLStructure
parent,

XMLCryptoContext
context)
throws
MarshalException
```

Marshals the algorithm-specific parameters. If there are no parameters
to be marshalled, this method returns without throwing an exception.

**Parameters:** parent

- a mechanism-specific structure containing the parent
node that the marshalled parameters should be appended to
**Parameters:** context

- the

XMLCryptoContext

containing
additional context (may be

null

if not applicable)
**Throws:** ClassCastException

- if the type of

parent

or

context

is not compatible with this

TransformService
**Throws:** NullPointerException

- if

parent

is

null
**Throws:** MarshalException

- if the parameters cannot be marshalled

- init

```java
public abstract void init​(
XMLStructure
parent,

XMLCryptoContext
context)
throws
InvalidAlgorithmParameterException
```

Initializes this

TransformService

with the specified
parameters and document context.

**Parameters:** parent

- a mechanism-specific structure containing the parent
structure
**Parameters:** context

- the

XMLCryptoContext

containing
additional context (may be

null

if not applicable)
**Throws:** ClassCastException

- if the type of

parent

or

context

is not compatible with this

TransformService
**Throws:** NullPointerException

- if

parent

is

null
**Throws:** InvalidAlgorithmParameterException

- if the specified parameters
are invalid for this algorithm

Constructor Detail

- TransformService

```java
protected TransformService()
```

Default constructor, for invocation by subclasses.

---

#### Constructor Detail

TransformService

```java
protected TransformService()
```

Default constructor, for invocation by subclasses.

---

#### TransformService

protected TransformService()

Default constructor, for invocation by subclasses.

Method Detail

- getInstance

```java
public static
TransformService
getInstance​(
String
algorithm,

String
mechanismType)
throws
NoSuchAlgorithmException
```

Returns a

TransformService

that supports the specified
algorithm URI (ex:

Transform.XPATH2

) and mechanism type
(ex: DOM).

This method uses the standard JCA provider lookup mechanism to
locate and instantiate a

TransformService

implementation
of the desired algorithm and

MechanismType

service
attribute. It traverses the list of registered security

Provider

s, starting with the most preferred

Provider

. A new

TransformService

object
from the first

Provider

that supports the specified
algorithm and mechanism type is returned.

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
**Parameters:** algorithm

- the URI of the algorithm
**Parameters:** mechanismType

- the type of the XML processing mechanism and
representation
**Returns:** a new

TransformService
**Throws:** NullPointerException

- if

algorithm

or

mechanismType

is

null
**Throws:** NoSuchAlgorithmException

- if no

Provider

supports a

TransformService

implementation for the specified
algorithm and mechanism type
**See Also:** Provider

- getInstance

```java
public static
TransformService
getInstance​(
String
algorithm,

String
mechanismType,

Provider
provider)
throws
NoSuchAlgorithmException
```

Returns a

TransformService

that supports the specified
algorithm URI (ex:

Transform.XPATH2

) and mechanism type
(ex: DOM) as supplied by the specified provider. Note that the specified

Provider

object does not have to be registered in the
provider list.

**Parameters:** algorithm

- the URI of the algorithm
**Parameters:** mechanismType

- the type of the XML processing mechanism and
representation
**Parameters:** provider

- the

Provider

object
**Returns:** a new

TransformService
**Throws:** NullPointerException

- if

provider

,

algorithm

, or

mechanismType

is

null
**Throws:** NoSuchAlgorithmException

- if a

TransformService

implementation for the specified algorithm and mechanism type is not
available from the specified

Provider

object
**See Also:** Provider

- getInstance

```java
public static
TransformService
getInstance​(
String
algorithm,

String
mechanismType,

String
provider)
throws
NoSuchAlgorithmException
,

NoSuchProviderException
```

Returns a

TransformService

that supports the specified
algorithm URI (ex:

Transform.XPATH2

) and mechanism type
(ex: DOM) as supplied by the specified provider. The specified provider
must be registered in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:** algorithm

- the URI of the algorithm
**Parameters:** mechanismType

- the type of the XML processing mechanism and
representation
**Parameters:** provider

- the string name of the provider
**Returns:** a new

TransformService
**Throws:** NoSuchProviderException

- if the specified provider is not
registered in the security provider list
**Throws:** NullPointerException

- if

provider

,

mechanismType

, or

algorithm

is

null
**Throws:** NoSuchAlgorithmException

- if a

TransformService

implementation for the specified algorithm and mechanism type is not
available from the specified provider
**See Also:** Provider

- getMechanismType

```java
public final
String
getMechanismType()
```

Returns the mechanism type supported by this

TransformService

.

**Returns:** the mechanism type

- getAlgorithm

```java
public final
String
getAlgorithm()
```

Returns the URI of the algorithm supported by this

TransformService

.

**Specified by:** getAlgorithm

in interface

AlgorithmMethod
**Returns:** the algorithm URI

- getProvider

```java
public final
Provider
getProvider()
```

Returns the provider of this

TransformService

.

**Returns:** the provider

- init

```java
public abstract void init​(
TransformParameterSpec
params)
throws
InvalidAlgorithmParameterException
```

Initializes this

TransformService

with the specified
parameters.

If the parameters exist in XML form, the

init(XMLStructure, XMLCryptoContext)

method should be used to
initialize the

TransformService

.

**Parameters:** params

- the algorithm parameters (may be

null

if
not required or optional)
**Throws:** InvalidAlgorithmParameterException

- if the specified parameters
are invalid for this algorithm

- marshalParams

```java
public abstract void marshalParams​(
XMLStructure
parent,

XMLCryptoContext
context)
throws
MarshalException
```

Marshals the algorithm-specific parameters. If there are no parameters
to be marshalled, this method returns without throwing an exception.

**Parameters:** parent

- a mechanism-specific structure containing the parent
node that the marshalled parameters should be appended to
**Parameters:** context

- the

XMLCryptoContext

containing
additional context (may be

null

if not applicable)
**Throws:** ClassCastException

- if the type of

parent

or

context

is not compatible with this

TransformService
**Throws:** NullPointerException

- if

parent

is

null
**Throws:** MarshalException

- if the parameters cannot be marshalled

- init

```java
public abstract void init​(
XMLStructure
parent,

XMLCryptoContext
context)
throws
InvalidAlgorithmParameterException
```

Initializes this

TransformService

with the specified
parameters and document context.

**Parameters:** parent

- a mechanism-specific structure containing the parent
structure
**Parameters:** context

- the

XMLCryptoContext

containing
additional context (may be

null

if not applicable)
**Throws:** ClassCastException

- if the type of

parent

or

context

is not compatible with this

TransformService
**Throws:** NullPointerException

- if

parent

is

null
**Throws:** InvalidAlgorithmParameterException

- if the specified parameters
are invalid for this algorithm

---

#### Method Detail

getInstance

```java
public static
TransformService
getInstance​(
String
algorithm,

String
mechanismType)
throws
NoSuchAlgorithmException
```

Returns a

TransformService

that supports the specified
algorithm URI (ex:

Transform.XPATH2

) and mechanism type
(ex: DOM).

This method uses the standard JCA provider lookup mechanism to
locate and instantiate a

TransformService

implementation
of the desired algorithm and

MechanismType

service
attribute. It traverses the list of registered security

Provider

s, starting with the most preferred

Provider

. A new

TransformService

object
from the first

Provider

that supports the specified
algorithm and mechanism type is returned.

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
**Parameters:** algorithm

- the URI of the algorithm
**Parameters:** mechanismType

- the type of the XML processing mechanism and
representation
**Returns:** a new

TransformService
**Throws:** NullPointerException

- if

algorithm

or

mechanismType

is

null
**Throws:** NoSuchAlgorithmException

- if no

Provider

supports a

TransformService

implementation for the specified
algorithm and mechanism type
**See Also:** Provider

---

#### getInstance

public static

TransformService

getInstance​(

String

algorithm,

String

mechanismType)
throws

NoSuchAlgorithmException

Returns a

TransformService

that supports the specified
algorithm URI (ex:

Transform.XPATH2

) and mechanism type
(ex: DOM).

This method uses the standard JCA provider lookup mechanism to
locate and instantiate a

TransformService

implementation
of the desired algorithm and

MechanismType

service
attribute. It traverses the list of registered security

Provider

s, starting with the most preferred

Provider

. A new

TransformService

object
from the first

Provider

that supports the specified
algorithm and mechanism type is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

This method uses the standard JCA provider lookup mechanism to
locate and instantiate a

TransformService

implementation
of the desired algorithm and

MechanismType

service
attribute. It traverses the list of registered security

Provider

s, starting with the most preferred

Provider

. A new

TransformService

object
from the first

Provider

that supports the specified
algorithm and mechanism type is returned.

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
TransformService
getInstance​(
String
algorithm,

String
mechanismType,

Provider
provider)
throws
NoSuchAlgorithmException
```

Returns a

TransformService

that supports the specified
algorithm URI (ex:

Transform.XPATH2

) and mechanism type
(ex: DOM) as supplied by the specified provider. Note that the specified

Provider

object does not have to be registered in the
provider list.

**Parameters:** algorithm

- the URI of the algorithm
**Parameters:** mechanismType

- the type of the XML processing mechanism and
representation
**Parameters:** provider

- the

Provider

object
**Returns:** a new

TransformService
**Throws:** NullPointerException

- if

provider

,

algorithm

, or

mechanismType

is

null
**Throws:** NoSuchAlgorithmException

- if a

TransformService

implementation for the specified algorithm and mechanism type is not
available from the specified

Provider

object
**See Also:** Provider

---

#### getInstance

public static

TransformService

getInstance​(

String

algorithm,

String

mechanismType,

Provider

provider)
throws

NoSuchAlgorithmException

Returns a

TransformService

that supports the specified
algorithm URI (ex:

Transform.XPATH2

) and mechanism type
(ex: DOM) as supplied by the specified provider. Note that the specified

Provider

object does not have to be registered in the
provider list.

getInstance

```java
public static
TransformService
getInstance​(
String
algorithm,

String
mechanismType,

String
provider)
throws
NoSuchAlgorithmException
,

NoSuchProviderException
```

Returns a

TransformService

that supports the specified
algorithm URI (ex:

Transform.XPATH2

) and mechanism type
(ex: DOM) as supplied by the specified provider. The specified provider
must be registered in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:** algorithm

- the URI of the algorithm
**Parameters:** mechanismType

- the type of the XML processing mechanism and
representation
**Parameters:** provider

- the string name of the provider
**Returns:** a new

TransformService
**Throws:** NoSuchProviderException

- if the specified provider is not
registered in the security provider list
**Throws:** NullPointerException

- if

provider

,

mechanismType

, or

algorithm

is

null
**Throws:** NoSuchAlgorithmException

- if a

TransformService

implementation for the specified algorithm and mechanism type is not
available from the specified provider
**See Also:** Provider

---

#### getInstance

public static

TransformService

getInstance​(

String

algorithm,

String

mechanismType,

String

provider)
throws

NoSuchAlgorithmException

,

NoSuchProviderException

Returns a

TransformService

that supports the specified
algorithm URI (ex:

Transform.XPATH2

) and mechanism type
(ex: DOM) as supplied by the specified provider. The specified provider
must be registered in the security provider list.

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

Returns the mechanism type supported by this

TransformService

.

**Returns:** the mechanism type

---

#### getMechanismType

public final

String

getMechanismType()

Returns the mechanism type supported by this

TransformService

.

getAlgorithm

```java
public final
String
getAlgorithm()
```

Returns the URI of the algorithm supported by this

TransformService

.

**Specified by:** getAlgorithm

in interface

AlgorithmMethod
**Returns:** the algorithm URI

---

#### getAlgorithm

public final

String

getAlgorithm()

Returns the URI of the algorithm supported by this

TransformService

.

getProvider

```java
public final
Provider
getProvider()
```

Returns the provider of this

TransformService

.

**Returns:** the provider

---

#### getProvider

public final

Provider

getProvider()

Returns the provider of this

TransformService

.

init

```java
public abstract void init​(
TransformParameterSpec
params)
throws
InvalidAlgorithmParameterException
```

Initializes this

TransformService

with the specified
parameters.

If the parameters exist in XML form, the

init(XMLStructure, XMLCryptoContext)

method should be used to
initialize the

TransformService

.

**Parameters:** params

- the algorithm parameters (may be

null

if
not required or optional)
**Throws:** InvalidAlgorithmParameterException

- if the specified parameters
are invalid for this algorithm

---

#### init

public abstract void init​(

TransformParameterSpec

params)
throws

InvalidAlgorithmParameterException

Initializes this

TransformService

with the specified
parameters.

If the parameters exist in XML form, the

init(XMLStructure, XMLCryptoContext)

method should be used to
initialize the

TransformService

.

If the parameters exist in XML form, the

init(XMLStructure, XMLCryptoContext)

method should be used to
initialize the

TransformService

.

marshalParams

```java
public abstract void marshalParams​(
XMLStructure
parent,

XMLCryptoContext
context)
throws
MarshalException
```

Marshals the algorithm-specific parameters. If there are no parameters
to be marshalled, this method returns without throwing an exception.

**Parameters:** parent

- a mechanism-specific structure containing the parent
node that the marshalled parameters should be appended to
**Parameters:** context

- the

XMLCryptoContext

containing
additional context (may be

null

if not applicable)
**Throws:** ClassCastException

- if the type of

parent

or

context

is not compatible with this

TransformService
**Throws:** NullPointerException

- if

parent

is

null
**Throws:** MarshalException

- if the parameters cannot be marshalled

---

#### marshalParams

public abstract void marshalParams​(

XMLStructure

parent,

XMLCryptoContext

context)
throws

MarshalException

Marshals the algorithm-specific parameters. If there are no parameters
to be marshalled, this method returns without throwing an exception.

init

```java
public abstract void init​(
XMLStructure
parent,

XMLCryptoContext
context)
throws
InvalidAlgorithmParameterException
```

Initializes this

TransformService

with the specified
parameters and document context.

**Parameters:** parent

- a mechanism-specific structure containing the parent
structure
**Parameters:** context

- the

XMLCryptoContext

containing
additional context (may be

null

if not applicable)
**Throws:** ClassCastException

- if the type of

parent

or

context

is not compatible with this

TransformService
**Throws:** NullPointerException

- if

parent

is

null
**Throws:** InvalidAlgorithmParameterException

- if the specified parameters
are invalid for this algorithm

---

#### init

public abstract void init​(

XMLStructure

parent,

XMLCryptoContext

context)
throws

InvalidAlgorithmParameterException

Initializes this

TransformService

with the specified
parameters and document context.

---

