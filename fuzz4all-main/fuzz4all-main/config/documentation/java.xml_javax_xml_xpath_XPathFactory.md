# Class XPathFactory

**Source:** `java.xml\javax\xml\xpath\XPathFactory.html`

### Class Description

```java
public abstract class
XPathFactory

extends
Object
```

An

XPathFactory

instance can be used to create

XPath

objects.

See

newInstance(String uri)

for lookup mechanism.

The

XPathFactory

class is not thread-safe. In other words,
it is the application's responsibility to ensure that at most
one thread is using a

XPathFactory

object at any
given moment. Implementations are encouraged to mark methods
as

synchronized

to protect themselves from broken clients.

XPathFactory

is not re-entrant. While one of the

newInstance

methods is being invoked, applications
may not attempt to recursively invoke a

newInstance

method,
even from the same thread.

**Since:** 1.5

---

### Field Details

#### public static final
String
DEFAULT_PROPERTY_NAME

The default property name according to the JAXP spec.

**See Also:**
- Constant Field Values

---

#### public static final
String
DEFAULT_OBJECT_MODEL_URI

Default Object Model URI.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### protected XPathFactory()

Protected constructor as

newInstance()

or

newInstance(String uri)

or

newInstance(String uri, String factoryClassName, ClassLoader classLoader)

should be used to create a new instance of an

XPathFactory

.

---

### Method Details

#### public static
XPathFactory
newDefaultInstance()

Creates a new instance of the

XPathFactory

builtin
system-default implementation.

**Returns:**
- A new instance of the

XPathFactory

builtin
system-default implementation.

**Since:**
- 9

**Implementation Requirements:**
- The

XPathFactory

builtin
system-default implementation is only required to support the

default object model

, the

W3C DOM

, but may support additional
object models.

---

#### public static
XPathFactory
newInstance()

Get a new

XPathFactory

instance using the default object model,

DEFAULT_OBJECT_MODEL_URI

,
the W3C DOM.

This method is functionally equivalent to:

```java
newInstance(DEFAULT_OBJECT_MODEL_URI)
```

Since the implementation for the W3C DOM is always available, this method will never fail.

**Returns:**
- Instance of an

XPathFactory

.

**Throws:**
- RuntimeException

- When there is a failure in creating an

XPathFactory

for the default object model.

---

#### public static
XPathFactory
newInstance​(
String
uri)
throws
XPathFactoryConfigurationException

Get a new

XPathFactory

instance using the specified object model.

To find a

XPathFactory

object,
this method looks the following places in the following order where "the class loader" refers to the context class loader:

- If the system property

DEFAULT_PROPERTY_NAME

+ ":uri" is present,
where uri is the parameter to this method, then its value is read as a class name.
The method will try to create a new instance of this class by using the class loader,
and returns it if it is successfully created.
- Use the configuration file "jaxp.properties". The file is in standard

Properties

format and typically located in the
conf directory of the Java installation. It contains the fully qualified
name of the implementation class with the key being the system property
defined above.

The jaxp.properties file is read only once by the JAXP implementation
and its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any property in jaxp.properties after it has been read for the first time.
- Use the service-provider loading facility, defined by the

ServiceLoader

class, to attempt to locate and load an
implementation of the service using the

default loading mechanism

:
the service-provider loading facility will use the

current thread's context class loader

to attempt to load the service. If the context class
loader is null, the

system class loader

will be used.

Each potential service provider is required to implement the method

isObjectModelSupported(String objectModel)

.
The first service provider found that supports the specified object
model is returned.

In case of

ServiceConfigurationError

an

XPathFactoryConfigurationException

will be thrown.
- Platform default

XPathFactory

is located in a platform
specific way.
There must be a

platform default

XPathFactory

for the W3C DOM, i.e.

DEFAULT_OBJECT_MODEL_URI

.

If everything fails, an

XPathFactoryConfigurationException

will be thrown.

Tip for Trouble-shooting:

See

Properties.load(java.io.InputStream)

for exactly how a property file is parsed.
In particular, colons ':' need to be escaped in a property file, so make sure the URIs are properly escaped in it.
For example:

```java
http\://java.sun.com/jaxp/xpath/dom=org.acme.DomXPathFactory
```

**Parameters:**
- uri

- Identifies the underlying object model.
The specification only defines the URI

DEFAULT_OBJECT_MODEL_URI

,

http://java.sun.com/jaxp/xpath/dom

for the W3C DOM,
the org.w3c.dom package, and implementations are free to introduce other URIs for other object models.

**Returns:**
- Instance of an

XPathFactory

.

**Throws:**
- XPathFactoryConfigurationException

- If the specified object model
is unavailable, or if there is a configuration error.
- NullPointerException

- If

uri

is

null

.
- IllegalArgumentException

- If

uri

is

null

or

uri.length() == 0

.

---

#### public static
XPathFactory
newInstance​(
String
uri,

String
factoryClassName,

ClassLoader
classLoader)
throws
XPathFactoryConfigurationException

Obtain a new instance of a

XPathFactory

from a factory class name.

XPathFactory

is returned if specified factory class supports the specified object model.
This function is useful when there are multiple providers in the classpath.
It gives more control to the application as it can specify which provider
should be loaded.

Tip for Trouble-shooting

Setting the

jaxp.debug

system property will cause
this method to print a lot of debug messages
to

System.err

about what it is doing and where it is looking at.

If you have problems try:

```java
java -Djaxp.debug=1 YourProgram ....
```

**Parameters:**
- uri

- Identifies the underlying object model. The specification only defines the URI

DEFAULT_OBJECT_MODEL_URI

,

http://java.sun.com/jaxp/xpath/dom

for the W3C DOM, the org.w3c.dom package, and implementations are free to introduce
other URIs for other object models.
- factoryClassName

- fully qualified factory class name that provides implementation of

javax.xml.xpath.XPathFactory

.
- classLoader

-

ClassLoader

used to load the factory class. If

null

current

Thread

's context classLoader is used to load the factory class.

**Returns:**
- New instance of a

XPathFactory

**Throws:**
- XPathFactoryConfigurationException

- if

factoryClassName

is

null

, or
the factory class cannot be loaded, instantiated
or the factory class does not support the object model specified
in the

uri

parameter.
- NullPointerException

- If

uri

is

null

.
- IllegalArgumentException

- If

uri

is

null

or

uri.length() == 0

.

**See Also:**
- newInstance()

,

newInstance(String uri)

**Since:**
- 1.6

---

#### public abstract boolean isObjectModelSupported​(
String
objectModel)

Is specified object model supported by this

XPathFactory

?

**Parameters:**
- objectModel

- Specifies the object model which the returned

XPathFactory

will understand.

**Returns:**
- true

if

XPathFactory

supports

objectModel

, else

false

.

**Throws:**
- NullPointerException

- If

objectModel

is

null

.
- IllegalArgumentException

- If

objectModel.length() == 0

.

---

#### public abstract void setFeature​(
String
name,
boolean value)
throws
XPathFactoryConfigurationException

Set a feature for this

XPathFactory

and

XPath

s created by this factory.

Feature names are fully qualified

URI

s.
Implementations may define their own features.
An

XPathFactoryConfigurationException

is thrown if this

XPathFactory

or the

XPath

s
it creates cannot support the feature.
It is possible for an

XPathFactory

to expose a feature value
but be unable to change its state.

All implementations are required to support the

XMLConstants.FEATURE_SECURE_PROCESSING

feature.
When the feature is

true

, any reference to an external function is an error.
Under these conditions, the implementation must not call the

XPathFunctionResolver

and must throw an

XPathFunctionException

.

**Parameters:**
- name

- Feature name.
- value

- Is feature state

true

or

false

.

**Throws:**
- XPathFactoryConfigurationException

- if this

XPathFactory

or the

XPath

s
it creates cannot support this feature.
- NullPointerException

- if

name

is

null

.

---

#### public abstract boolean getFeature​(
String
name)
throws
XPathFactoryConfigurationException

Get the state of the named feature.

Feature names are fully qualified

URI

s.
Implementations may define their own features.
An

XPathFactoryConfigurationException

is thrown if this

XPathFactory

or the

XPath

s
it creates cannot support the feature.
It is possible for an

XPathFactory

to expose a feature value
but be unable to change its state.

**Parameters:**
- name

- Feature name.

**Returns:**
- State of the named feature.

**Throws:**
- XPathFactoryConfigurationException

- if this

XPathFactory

or the

XPath

s
it creates cannot support this feature.
- NullPointerException

- if

name

is

null

.

---

#### public abstract void setXPathVariableResolver​(
XPathVariableResolver
resolver)

Establish a default variable resolver.

Any

XPath

objects constructed from this factory will use
the specified resolver by default.

A

NullPointerException

is thrown if

resolver

is

null

.

**Parameters:**
- resolver

- Variable resolver.

**Throws:**
- NullPointerException

- If

resolver

is

null

.

---

#### public abstract void setXPathFunctionResolver​(
XPathFunctionResolver
resolver)

Establish a default function resolver.

Any

XPath

objects constructed from this factory will
use the specified resolver by default.

A

NullPointerException

is thrown if

resolver

is

null

.

**Parameters:**
- resolver

- XPath function resolver.

**Throws:**
- NullPointerException

- If

resolver

is

null

.

---

#### public abstract
XPath
newXPath()

Return a new

XPath

using the underlying object
model determined when the

XPathFactory

was instantiated.

**Returns:**
- New instance of an

XPath

.

---

### Additional Sections

#### Class XPathFactory

java.lang.Object

- javax.xml.xpath.XPathFactory

javax.xml.xpath.XPathFactory

```java
public abstract class
XPathFactory

extends
Object
```

An

XPathFactory

instance can be used to create

XPath

objects.

See

newInstance(String uri)

for lookup mechanism.

The

XPathFactory

class is not thread-safe. In other words,
it is the application's responsibility to ensure that at most
one thread is using a

XPathFactory

object at any
given moment. Implementations are encouraged to mark methods
as

synchronized

to protect themselves from broken clients.

XPathFactory

is not re-entrant. While one of the

newInstance

methods is being invoked, applications
may not attempt to recursively invoke a

newInstance

method,
even from the same thread.

**Since:** 1.5

public abstract class

XPathFactory

extends

Object

An

XPathFactory

instance can be used to create

XPath

objects.

See

newInstance(String uri)

for lookup mechanism.

The

XPathFactory

class is not thread-safe. In other words,
it is the application's responsibility to ensure that at most
one thread is using a

XPathFactory

object at any
given moment. Implementations are encouraged to mark methods
as

synchronized

to protect themselves from broken clients.

XPathFactory

is not re-entrant. While one of the

newInstance

methods is being invoked, applications
may not attempt to recursively invoke a

newInstance

method,
even from the same thread.

An

XPathFactory

instance can be used to create

XPath

objects.

See

newInstance(String uri)

for lookup mechanism.

The

XPathFactory

class is not thread-safe. In other words,
it is the application's responsibility to ensure that at most
one thread is using a

XPathFactory

object at any
given moment. Implementations are encouraged to mark methods
as

synchronized

to protect themselves from broken clients.

XPathFactory

is not re-entrant. While one of the

newInstance

methods is being invoked, applications
may not attempt to recursively invoke a

newInstance

method,
even from the same thread.

XPathFactory

is not re-entrant. While one of the

newInstance

methods is being invoked, applications
may not attempt to recursively invoke a

newInstance

method,
even from the same thread.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

DEFAULT_OBJECT_MODEL_URI

Default Object Model URI.

static

String

DEFAULT_PROPERTY_NAME

The default property name according to the JAXP spec.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

XPathFactory

()

Protected constructor as

newInstance()

or

newInstance(String uri)

or

newInstance(String uri, String factoryClassName, ClassLoader classLoader)

should be used to create a new instance of an

XPathFactory

.

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

abstract boolean

getFeature

​(

String

name)

Get the state of the named feature.

abstract boolean

isObjectModelSupported

​(

String

objectModel)

Is specified object model supported by this

XPathFactory

?

static

XPathFactory

newDefaultInstance

()

Creates a new instance of the

XPathFactory

builtin
system-default implementation.

static

XPathFactory

newInstance

()

Get a new

XPathFactory

instance using the default object model,

DEFAULT_OBJECT_MODEL_URI

,
the W3C DOM.

static

XPathFactory

newInstance

​(

String

uri)

Get a new

XPathFactory

instance using the specified object model.

static

XPathFactory

newInstance

​(

String

uri,

String

factoryClassName,

ClassLoader

classLoader)

Obtain a new instance of a

XPathFactory

from a factory class name.

abstract

XPath

newXPath

()

Return a new

XPath

using the underlying object
model determined when the

XPathFactory

was instantiated.

abstract void

setFeature

​(

String

name,
boolean value)

Set a feature for this

XPathFactory

and

XPath

s created by this factory.

abstract void

setXPathFunctionResolver

​(

XPathFunctionResolver

resolver)

Establish a default function resolver.

abstract void

setXPathVariableResolver

​(

XPathVariableResolver

resolver)

Establish a default variable resolver.

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

Field Summary

Fields

Modifier and Type

Field

Description

static

String

DEFAULT_OBJECT_MODEL_URI

Default Object Model URI.

static

String

DEFAULT_PROPERTY_NAME

The default property name according to the JAXP spec.

---

#### Field Summary

Default Object Model URI.

The default property name according to the JAXP spec.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

XPathFactory

()

Protected constructor as

newInstance()

or

newInstance(String uri)

or

newInstance(String uri, String factoryClassName, ClassLoader classLoader)

should be used to create a new instance of an

XPathFactory

.

---

#### Constructor Summary

Protected constructor as

newInstance()

or

newInstance(String uri)

or

newInstance(String uri, String factoryClassName, ClassLoader classLoader)

should be used to create a new instance of an

XPathFactory

.

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract boolean

getFeature

​(

String

name)

Get the state of the named feature.

abstract boolean

isObjectModelSupported

​(

String

objectModel)

Is specified object model supported by this

XPathFactory

?

static

XPathFactory

newDefaultInstance

()

Creates a new instance of the

XPathFactory

builtin
system-default implementation.

static

XPathFactory

newInstance

()

Get a new

XPathFactory

instance using the default object model,

DEFAULT_OBJECT_MODEL_URI

,
the W3C DOM.

static

XPathFactory

newInstance

​(

String

uri)

Get a new

XPathFactory

instance using the specified object model.

static

XPathFactory

newInstance

​(

String

uri,

String

factoryClassName,

ClassLoader

classLoader)

Obtain a new instance of a

XPathFactory

from a factory class name.

abstract

XPath

newXPath

()

Return a new

XPath

using the underlying object
model determined when the

XPathFactory

was instantiated.

abstract void

setFeature

​(

String

name,
boolean value)

Set a feature for this

XPathFactory

and

XPath

s created by this factory.

abstract void

setXPathFunctionResolver

​(

XPathFunctionResolver

resolver)

Establish a default function resolver.

abstract void

setXPathVariableResolver

​(

XPathVariableResolver

resolver)

Establish a default variable resolver.

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

Get the state of the named feature.

Is specified object model supported by this

XPathFactory

?

Creates a new instance of the

XPathFactory

builtin
system-default implementation.

Get a new

XPathFactory

instance using the default object model,

DEFAULT_OBJECT_MODEL_URI

,
the W3C DOM.

Get a new

XPathFactory

instance using the specified object model.

Obtain a new instance of a

XPathFactory

from a factory class name.

Return a new

XPath

using the underlying object
model determined when the

XPathFactory

was instantiated.

Set a feature for this

XPathFactory

and

XPath

s created by this factory.

Establish a default function resolver.

Establish a default variable resolver.

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

- DEFAULT_PROPERTY_NAME

```java
public static final
String
DEFAULT_PROPERTY_NAME
```

The default property name according to the JAXP spec.

**See Also:** Constant Field Values

- DEFAULT_OBJECT_MODEL_URI

```java
public static final
String
DEFAULT_OBJECT_MODEL_URI
```

Default Object Model URI.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- XPathFactory

```java
protected XPathFactory()
```

Protected constructor as

newInstance()

or

newInstance(String uri)

or

newInstance(String uri, String factoryClassName, ClassLoader classLoader)

should be used to create a new instance of an

XPathFactory

.

============ METHOD DETAIL ==========

- Method Detail

- newDefaultInstance

```java
public static
XPathFactory
newDefaultInstance()
```

Creates a new instance of the

XPathFactory

builtin
system-default implementation.

**Implementation Requirements:** The

XPathFactory

builtin
system-default implementation is only required to support the

default object model

, the

W3C DOM

, but may support additional
object models.
**Returns:** A new instance of the

XPathFactory

builtin
system-default implementation.
**Since:** 9

- newInstance

```java
public static
XPathFactory
newInstance()
```

Get a new

XPathFactory

instance using the default object model,

DEFAULT_OBJECT_MODEL_URI

,
the W3C DOM.

This method is functionally equivalent to:

```java
newInstance(DEFAULT_OBJECT_MODEL_URI)
```

Since the implementation for the W3C DOM is always available, this method will never fail.

**Returns:** Instance of an

XPathFactory

.
**Throws:** RuntimeException

- When there is a failure in creating an

XPathFactory

for the default object model.

- newInstance

```java
public static
XPathFactory
newInstance​(
String
uri)
throws
XPathFactoryConfigurationException
```

Get a new

XPathFactory

instance using the specified object model.

To find a

XPathFactory

object,
this method looks the following places in the following order where "the class loader" refers to the context class loader:

- If the system property

DEFAULT_PROPERTY_NAME

+ ":uri" is present,
where uri is the parameter to this method, then its value is read as a class name.
The method will try to create a new instance of this class by using the class loader,
and returns it if it is successfully created.
- Use the configuration file "jaxp.properties". The file is in standard

Properties

format and typically located in the
conf directory of the Java installation. It contains the fully qualified
name of the implementation class with the key being the system property
defined above.

The jaxp.properties file is read only once by the JAXP implementation
and its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any property in jaxp.properties after it has been read for the first time.
- Use the service-provider loading facility, defined by the

ServiceLoader

class, to attempt to locate and load an
implementation of the service using the

default loading mechanism

:
the service-provider loading facility will use the

current thread's context class loader

to attempt to load the service. If the context class
loader is null, the

system class loader

will be used.

Each potential service provider is required to implement the method

isObjectModelSupported(String objectModel)

.
The first service provider found that supports the specified object
model is returned.

In case of

ServiceConfigurationError

an

XPathFactoryConfigurationException

will be thrown.
- Platform default

XPathFactory

is located in a platform
specific way.
There must be a

platform default

XPathFactory

for the W3C DOM, i.e.

DEFAULT_OBJECT_MODEL_URI

.

If everything fails, an

XPathFactoryConfigurationException

will be thrown.

Tip for Trouble-shooting:

See

Properties.load(java.io.InputStream)

for exactly how a property file is parsed.
In particular, colons ':' need to be escaped in a property file, so make sure the URIs are properly escaped in it.
For example:

```java
http\://java.sun.com/jaxp/xpath/dom=org.acme.DomXPathFactory
```

**Parameters:** uri

- Identifies the underlying object model.
The specification only defines the URI

DEFAULT_OBJECT_MODEL_URI

,

http://java.sun.com/jaxp/xpath/dom

for the W3C DOM,
the org.w3c.dom package, and implementations are free to introduce other URIs for other object models.
**Returns:** Instance of an

XPathFactory

.
**Throws:** XPathFactoryConfigurationException

- If the specified object model
is unavailable, or if there is a configuration error.
**Throws:** NullPointerException

- If

uri

is

null

.
**Throws:** IllegalArgumentException

- If

uri

is

null

or

uri.length() == 0

.

- newInstance

```java
public static
XPathFactory
newInstance​(
String
uri,

String
factoryClassName,

ClassLoader
classLoader)
throws
XPathFactoryConfigurationException
```

Obtain a new instance of a

XPathFactory

from a factory class name.

XPathFactory

is returned if specified factory class supports the specified object model.
This function is useful when there are multiple providers in the classpath.
It gives more control to the application as it can specify which provider
should be loaded.

Tip for Trouble-shooting

Setting the

jaxp.debug

system property will cause
this method to print a lot of debug messages
to

System.err

about what it is doing and where it is looking at.

If you have problems try:

```java
java -Djaxp.debug=1 YourProgram ....
```

**Parameters:** uri

- Identifies the underlying object model. The specification only defines the URI

DEFAULT_OBJECT_MODEL_URI

,

http://java.sun.com/jaxp/xpath/dom

for the W3C DOM, the org.w3c.dom package, and implementations are free to introduce
other URIs for other object models.
**Parameters:** factoryClassName

- fully qualified factory class name that provides implementation of

javax.xml.xpath.XPathFactory

.
**Parameters:** classLoader

-

ClassLoader

used to load the factory class. If

null

current

Thread

's context classLoader is used to load the factory class.
**Returns:** New instance of a

XPathFactory
**Throws:** XPathFactoryConfigurationException

- if

factoryClassName

is

null

, or
the factory class cannot be loaded, instantiated
or the factory class does not support the object model specified
in the

uri

parameter.
**Throws:** NullPointerException

- If

uri

is

null

.
**Throws:** IllegalArgumentException

- If

uri

is

null

or

uri.length() == 0

.
**Since:** 1.6
**See Also:** newInstance()

,

newInstance(String uri)

- isObjectModelSupported

```java
public abstract boolean isObjectModelSupported​(
String
objectModel)
```

Is specified object model supported by this

XPathFactory

?

**Parameters:** objectModel

- Specifies the object model which the returned

XPathFactory

will understand.
**Returns:** true

if

XPathFactory

supports

objectModel

, else

false

.
**Throws:** NullPointerException

- If

objectModel

is

null

.
**Throws:** IllegalArgumentException

- If

objectModel.length() == 0

.

- setFeature

```java
public abstract void setFeature​(
String
name,
boolean value)
throws
XPathFactoryConfigurationException
```

Set a feature for this

XPathFactory

and

XPath

s created by this factory.

Feature names are fully qualified

URI

s.
Implementations may define their own features.
An

XPathFactoryConfigurationException

is thrown if this

XPathFactory

or the

XPath

s
it creates cannot support the feature.
It is possible for an

XPathFactory

to expose a feature value
but be unable to change its state.

All implementations are required to support the

XMLConstants.FEATURE_SECURE_PROCESSING

feature.
When the feature is

true

, any reference to an external function is an error.
Under these conditions, the implementation must not call the

XPathFunctionResolver

and must throw an

XPathFunctionException

.

**Parameters:** name

- Feature name.
**Parameters:** value

- Is feature state

true

or

false

.
**Throws:** XPathFactoryConfigurationException

- if this

XPathFactory

or the

XPath

s
it creates cannot support this feature.
**Throws:** NullPointerException

- if

name

is

null

.

- getFeature

```java
public abstract boolean getFeature​(
String
name)
throws
XPathFactoryConfigurationException
```

Get the state of the named feature.

Feature names are fully qualified

URI

s.
Implementations may define their own features.
An

XPathFactoryConfigurationException

is thrown if this

XPathFactory

or the

XPath

s
it creates cannot support the feature.
It is possible for an

XPathFactory

to expose a feature value
but be unable to change its state.

**Parameters:** name

- Feature name.
**Returns:** State of the named feature.
**Throws:** XPathFactoryConfigurationException

- if this

XPathFactory

or the

XPath

s
it creates cannot support this feature.
**Throws:** NullPointerException

- if

name

is

null

.

- setXPathVariableResolver

```java
public abstract void setXPathVariableResolver​(
XPathVariableResolver
resolver)
```

Establish a default variable resolver.

Any

XPath

objects constructed from this factory will use
the specified resolver by default.

A

NullPointerException

is thrown if

resolver

is

null

.

**Parameters:** resolver

- Variable resolver.
**Throws:** NullPointerException

- If

resolver

is

null

.

- setXPathFunctionResolver

```java
public abstract void setXPathFunctionResolver​(
XPathFunctionResolver
resolver)
```

Establish a default function resolver.

Any

XPath

objects constructed from this factory will
use the specified resolver by default.

A

NullPointerException

is thrown if

resolver

is

null

.

**Parameters:** resolver

- XPath function resolver.
**Throws:** NullPointerException

- If

resolver

is

null

.

- newXPath

```java
public abstract
XPath
newXPath()
```

Return a new

XPath

using the underlying object
model determined when the

XPathFactory

was instantiated.

**Returns:** New instance of an

XPath

.

Field Detail

- DEFAULT_PROPERTY_NAME

```java
public static final
String
DEFAULT_PROPERTY_NAME
```

The default property name according to the JAXP spec.

**See Also:** Constant Field Values

- DEFAULT_OBJECT_MODEL_URI

```java
public static final
String
DEFAULT_OBJECT_MODEL_URI
```

Default Object Model URI.

**See Also:** Constant Field Values

---

#### Field Detail

DEFAULT_PROPERTY_NAME

```java
public static final
String
DEFAULT_PROPERTY_NAME
```

The default property name according to the JAXP spec.

**See Also:** Constant Field Values

---

#### DEFAULT_PROPERTY_NAME

public static final

String

DEFAULT_PROPERTY_NAME

The default property name according to the JAXP spec.

DEFAULT_OBJECT_MODEL_URI

```java
public static final
String
DEFAULT_OBJECT_MODEL_URI
```

Default Object Model URI.

**See Also:** Constant Field Values

---

#### DEFAULT_OBJECT_MODEL_URI

public static final

String

DEFAULT_OBJECT_MODEL_URI

Default Object Model URI.

Constructor Detail

- XPathFactory

```java
protected XPathFactory()
```

Protected constructor as

newInstance()

or

newInstance(String uri)

or

newInstance(String uri, String factoryClassName, ClassLoader classLoader)

should be used to create a new instance of an

XPathFactory

.

---

#### Constructor Detail

XPathFactory

```java
protected XPathFactory()
```

Protected constructor as

newInstance()

or

newInstance(String uri)

or

newInstance(String uri, String factoryClassName, ClassLoader classLoader)

should be used to create a new instance of an

XPathFactory

.

---

#### XPathFactory

protected XPathFactory()

Protected constructor as

newInstance()

or

newInstance(String uri)

or

newInstance(String uri, String factoryClassName, ClassLoader classLoader)

should be used to create a new instance of an

XPathFactory

.

Method Detail

- newDefaultInstance

```java
public static
XPathFactory
newDefaultInstance()
```

Creates a new instance of the

XPathFactory

builtin
system-default implementation.

**Implementation Requirements:** The

XPathFactory

builtin
system-default implementation is only required to support the

default object model

, the

W3C DOM

, but may support additional
object models.
**Returns:** A new instance of the

XPathFactory

builtin
system-default implementation.
**Since:** 9

- newInstance

```java
public static
XPathFactory
newInstance()
```

Get a new

XPathFactory

instance using the default object model,

DEFAULT_OBJECT_MODEL_URI

,
the W3C DOM.

This method is functionally equivalent to:

```java
newInstance(DEFAULT_OBJECT_MODEL_URI)
```

Since the implementation for the W3C DOM is always available, this method will never fail.

**Returns:** Instance of an

XPathFactory

.
**Throws:** RuntimeException

- When there is a failure in creating an

XPathFactory

for the default object model.

- newInstance

```java
public static
XPathFactory
newInstance​(
String
uri)
throws
XPathFactoryConfigurationException
```

Get a new

XPathFactory

instance using the specified object model.

To find a

XPathFactory

object,
this method looks the following places in the following order where "the class loader" refers to the context class loader:

- If the system property

DEFAULT_PROPERTY_NAME

+ ":uri" is present,
where uri is the parameter to this method, then its value is read as a class name.
The method will try to create a new instance of this class by using the class loader,
and returns it if it is successfully created.
- Use the configuration file "jaxp.properties". The file is in standard

Properties

format and typically located in the
conf directory of the Java installation. It contains the fully qualified
name of the implementation class with the key being the system property
defined above.

The jaxp.properties file is read only once by the JAXP implementation
and its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any property in jaxp.properties after it has been read for the first time.
- Use the service-provider loading facility, defined by the

ServiceLoader

class, to attempt to locate and load an
implementation of the service using the

default loading mechanism

:
the service-provider loading facility will use the

current thread's context class loader

to attempt to load the service. If the context class
loader is null, the

system class loader

will be used.

Each potential service provider is required to implement the method

isObjectModelSupported(String objectModel)

.
The first service provider found that supports the specified object
model is returned.

In case of

ServiceConfigurationError

an

XPathFactoryConfigurationException

will be thrown.
- Platform default

XPathFactory

is located in a platform
specific way.
There must be a

platform default

XPathFactory

for the W3C DOM, i.e.

DEFAULT_OBJECT_MODEL_URI

.

If everything fails, an

XPathFactoryConfigurationException

will be thrown.

Tip for Trouble-shooting:

See

Properties.load(java.io.InputStream)

for exactly how a property file is parsed.
In particular, colons ':' need to be escaped in a property file, so make sure the URIs are properly escaped in it.
For example:

```java
http\://java.sun.com/jaxp/xpath/dom=org.acme.DomXPathFactory
```

**Parameters:** uri

- Identifies the underlying object model.
The specification only defines the URI

DEFAULT_OBJECT_MODEL_URI

,

http://java.sun.com/jaxp/xpath/dom

for the W3C DOM,
the org.w3c.dom package, and implementations are free to introduce other URIs for other object models.
**Returns:** Instance of an

XPathFactory

.
**Throws:** XPathFactoryConfigurationException

- If the specified object model
is unavailable, or if there is a configuration error.
**Throws:** NullPointerException

- If

uri

is

null

.
**Throws:** IllegalArgumentException

- If

uri

is

null

or

uri.length() == 0

.

- newInstance

```java
public static
XPathFactory
newInstance​(
String
uri,

String
factoryClassName,

ClassLoader
classLoader)
throws
XPathFactoryConfigurationException
```

Obtain a new instance of a

XPathFactory

from a factory class name.

XPathFactory

is returned if specified factory class supports the specified object model.
This function is useful when there are multiple providers in the classpath.
It gives more control to the application as it can specify which provider
should be loaded.

Tip for Trouble-shooting

Setting the

jaxp.debug

system property will cause
this method to print a lot of debug messages
to

System.err

about what it is doing and where it is looking at.

If you have problems try:

```java
java -Djaxp.debug=1 YourProgram ....
```

**Parameters:** uri

- Identifies the underlying object model. The specification only defines the URI

DEFAULT_OBJECT_MODEL_URI

,

http://java.sun.com/jaxp/xpath/dom

for the W3C DOM, the org.w3c.dom package, and implementations are free to introduce
other URIs for other object models.
**Parameters:** factoryClassName

- fully qualified factory class name that provides implementation of

javax.xml.xpath.XPathFactory

.
**Parameters:** classLoader

-

ClassLoader

used to load the factory class. If

null

current

Thread

's context classLoader is used to load the factory class.
**Returns:** New instance of a

XPathFactory
**Throws:** XPathFactoryConfigurationException

- if

factoryClassName

is

null

, or
the factory class cannot be loaded, instantiated
or the factory class does not support the object model specified
in the

uri

parameter.
**Throws:** NullPointerException

- If

uri

is

null

.
**Throws:** IllegalArgumentException

- If

uri

is

null

or

uri.length() == 0

.
**Since:** 1.6
**See Also:** newInstance()

,

newInstance(String uri)

- isObjectModelSupported

```java
public abstract boolean isObjectModelSupported​(
String
objectModel)
```

Is specified object model supported by this

XPathFactory

?

**Parameters:** objectModel

- Specifies the object model which the returned

XPathFactory

will understand.
**Returns:** true

if

XPathFactory

supports

objectModel

, else

false

.
**Throws:** NullPointerException

- If

objectModel

is

null

.
**Throws:** IllegalArgumentException

- If

objectModel.length() == 0

.

- setFeature

```java
public abstract void setFeature​(
String
name,
boolean value)
throws
XPathFactoryConfigurationException
```

Set a feature for this

XPathFactory

and

XPath

s created by this factory.

Feature names are fully qualified

URI

s.
Implementations may define their own features.
An

XPathFactoryConfigurationException

is thrown if this

XPathFactory

or the

XPath

s
it creates cannot support the feature.
It is possible for an

XPathFactory

to expose a feature value
but be unable to change its state.

All implementations are required to support the

XMLConstants.FEATURE_SECURE_PROCESSING

feature.
When the feature is

true

, any reference to an external function is an error.
Under these conditions, the implementation must not call the

XPathFunctionResolver

and must throw an

XPathFunctionException

.

**Parameters:** name

- Feature name.
**Parameters:** value

- Is feature state

true

or

false

.
**Throws:** XPathFactoryConfigurationException

- if this

XPathFactory

or the

XPath

s
it creates cannot support this feature.
**Throws:** NullPointerException

- if

name

is

null

.

- getFeature

```java
public abstract boolean getFeature​(
String
name)
throws
XPathFactoryConfigurationException
```

Get the state of the named feature.

Feature names are fully qualified

URI

s.
Implementations may define their own features.
An

XPathFactoryConfigurationException

is thrown if this

XPathFactory

or the

XPath

s
it creates cannot support the feature.
It is possible for an

XPathFactory

to expose a feature value
but be unable to change its state.

**Parameters:** name

- Feature name.
**Returns:** State of the named feature.
**Throws:** XPathFactoryConfigurationException

- if this

XPathFactory

or the

XPath

s
it creates cannot support this feature.
**Throws:** NullPointerException

- if

name

is

null

.

- setXPathVariableResolver

```java
public abstract void setXPathVariableResolver​(
XPathVariableResolver
resolver)
```

Establish a default variable resolver.

Any

XPath

objects constructed from this factory will use
the specified resolver by default.

A

NullPointerException

is thrown if

resolver

is

null

.

**Parameters:** resolver

- Variable resolver.
**Throws:** NullPointerException

- If

resolver

is

null

.

- setXPathFunctionResolver

```java
public abstract void setXPathFunctionResolver​(
XPathFunctionResolver
resolver)
```

Establish a default function resolver.

Any

XPath

objects constructed from this factory will
use the specified resolver by default.

A

NullPointerException

is thrown if

resolver

is

null

.

**Parameters:** resolver

- XPath function resolver.
**Throws:** NullPointerException

- If

resolver

is

null

.

- newXPath

```java
public abstract
XPath
newXPath()
```

Return a new

XPath

using the underlying object
model determined when the

XPathFactory

was instantiated.

**Returns:** New instance of an

XPath

.

---

#### Method Detail

newDefaultInstance

```java
public static
XPathFactory
newDefaultInstance()
```

Creates a new instance of the

XPathFactory

builtin
system-default implementation.

**Implementation Requirements:** The

XPathFactory

builtin
system-default implementation is only required to support the

default object model

, the

W3C DOM

, but may support additional
object models.
**Returns:** A new instance of the

XPathFactory

builtin
system-default implementation.
**Since:** 9

---

#### newDefaultInstance

public static

XPathFactory

newDefaultInstance()

Creates a new instance of the

XPathFactory

builtin
system-default implementation.

newInstance

```java
public static
XPathFactory
newInstance()
```

Get a new

XPathFactory

instance using the default object model,

DEFAULT_OBJECT_MODEL_URI

,
the W3C DOM.

This method is functionally equivalent to:

```java
newInstance(DEFAULT_OBJECT_MODEL_URI)
```

Since the implementation for the W3C DOM is always available, this method will never fail.

**Returns:** Instance of an

XPathFactory

.
**Throws:** RuntimeException

- When there is a failure in creating an

XPathFactory

for the default object model.

---

#### newInstance

public static

XPathFactory

newInstance()

Get a new

XPathFactory

instance using the default object model,

DEFAULT_OBJECT_MODEL_URI

,
the W3C DOM.

This method is functionally equivalent to:

```java
newInstance(DEFAULT_OBJECT_MODEL_URI)
```

Since the implementation for the W3C DOM is always available, this method will never fail.

Get a new

XPathFactory

instance using the default object model,

DEFAULT_OBJECT_MODEL_URI

,
the W3C DOM.

This method is functionally equivalent to:

newInstance(DEFAULT_OBJECT_MODEL_URI)

Since the implementation for the W3C DOM is always available, this method will never fail.

newInstance

```java
public static
XPathFactory
newInstance​(
String
uri)
throws
XPathFactoryConfigurationException
```

Get a new

XPathFactory

instance using the specified object model.

To find a

XPathFactory

object,
this method looks the following places in the following order where "the class loader" refers to the context class loader:

- If the system property

DEFAULT_PROPERTY_NAME

+ ":uri" is present,
where uri is the parameter to this method, then its value is read as a class name.
The method will try to create a new instance of this class by using the class loader,
and returns it if it is successfully created.
- Use the configuration file "jaxp.properties". The file is in standard

Properties

format and typically located in the
conf directory of the Java installation. It contains the fully qualified
name of the implementation class with the key being the system property
defined above.

The jaxp.properties file is read only once by the JAXP implementation
and its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any property in jaxp.properties after it has been read for the first time.
- Use the service-provider loading facility, defined by the

ServiceLoader

class, to attempt to locate and load an
implementation of the service using the

default loading mechanism

:
the service-provider loading facility will use the

current thread's context class loader

to attempt to load the service. If the context class
loader is null, the

system class loader

will be used.

Each potential service provider is required to implement the method

isObjectModelSupported(String objectModel)

.
The first service provider found that supports the specified object
model is returned.

In case of

ServiceConfigurationError

an

XPathFactoryConfigurationException

will be thrown.
- Platform default

XPathFactory

is located in a platform
specific way.
There must be a

platform default

XPathFactory

for the W3C DOM, i.e.

DEFAULT_OBJECT_MODEL_URI

.

If everything fails, an

XPathFactoryConfigurationException

will be thrown.

Tip for Trouble-shooting:

See

Properties.load(java.io.InputStream)

for exactly how a property file is parsed.
In particular, colons ':' need to be escaped in a property file, so make sure the URIs are properly escaped in it.
For example:

```java
http\://java.sun.com/jaxp/xpath/dom=org.acme.DomXPathFactory
```

**Parameters:** uri

- Identifies the underlying object model.
The specification only defines the URI

DEFAULT_OBJECT_MODEL_URI

,

http://java.sun.com/jaxp/xpath/dom

for the W3C DOM,
the org.w3c.dom package, and implementations are free to introduce other URIs for other object models.
**Returns:** Instance of an

XPathFactory

.
**Throws:** XPathFactoryConfigurationException

- If the specified object model
is unavailable, or if there is a configuration error.
**Throws:** NullPointerException

- If

uri

is

null

.
**Throws:** IllegalArgumentException

- If

uri

is

null

or

uri.length() == 0

.

---

#### newInstance

public static

XPathFactory

newInstance​(

String

uri)
throws

XPathFactoryConfigurationException

Get a new

XPathFactory

instance using the specified object model.

To find a

XPathFactory

object,
this method looks the following places in the following order where "the class loader" refers to the context class loader:

- If the system property

DEFAULT_PROPERTY_NAME

+ ":uri" is present,
where uri is the parameter to this method, then its value is read as a class name.
The method will try to create a new instance of this class by using the class loader,
and returns it if it is successfully created.
- Use the configuration file "jaxp.properties". The file is in standard

Properties

format and typically located in the
conf directory of the Java installation. It contains the fully qualified
name of the implementation class with the key being the system property
defined above.

The jaxp.properties file is read only once by the JAXP implementation
and its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any property in jaxp.properties after it has been read for the first time.
- Use the service-provider loading facility, defined by the

ServiceLoader

class, to attempt to locate and load an
implementation of the service using the

default loading mechanism

:
the service-provider loading facility will use the

current thread's context class loader

to attempt to load the service. If the context class
loader is null, the

system class loader

will be used.

Each potential service provider is required to implement the method

isObjectModelSupported(String objectModel)

.
The first service provider found that supports the specified object
model is returned.

In case of

ServiceConfigurationError

an

XPathFactoryConfigurationException

will be thrown.
- Platform default

XPathFactory

is located in a platform
specific way.
There must be a

platform default

XPathFactory

for the W3C DOM, i.e.

DEFAULT_OBJECT_MODEL_URI

.

If everything fails, an

XPathFactoryConfigurationException

will be thrown.

Tip for Trouble-shooting:

See

Properties.load(java.io.InputStream)

for exactly how a property file is parsed.
In particular, colons ':' need to be escaped in a property file, so make sure the URIs are properly escaped in it.
For example:

```java
http\://java.sun.com/jaxp/xpath/dom=org.acme.DomXPathFactory
```

Get a new

XPathFactory

instance using the specified object model.

To find a

XPathFactory

object,
this method looks the following places in the following order where "the class loader" refers to the context class loader:

If the system property

DEFAULT_PROPERTY_NAME

+ ":uri" is present,
where uri is the parameter to this method, then its value is read as a class name.
The method will try to create a new instance of this class by using the class loader,
and returns it if it is successfully created.

Use the configuration file "jaxp.properties". The file is in standard

Properties

format and typically located in the
conf directory of the Java installation. It contains the fully qualified
name of the implementation class with the key being the system property
defined above.

The jaxp.properties file is read only once by the JAXP implementation
and its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any property in jaxp.properties after it has been read for the first time.

Use the service-provider loading facility, defined by the

ServiceLoader

class, to attempt to locate and load an
implementation of the service using the

default loading mechanism

:
the service-provider loading facility will use the

current thread's context class loader

to attempt to load the service. If the context class
loader is null, the

system class loader

will be used.

Each potential service provider is required to implement the method

isObjectModelSupported(String objectModel)

.
The first service provider found that supports the specified object
model is returned.

In case of

ServiceConfigurationError

an

XPathFactoryConfigurationException

will be thrown.

Platform default

XPathFactory

is located in a platform
specific way.
There must be a

platform default

XPathFactory

for the W3C DOM, i.e.

DEFAULT_OBJECT_MODEL_URI

.

If the system property

DEFAULT_PROPERTY_NAME

+ ":uri" is present,
where uri is the parameter to this method, then its value is read as a class name.
The method will try to create a new instance of this class by using the class loader,
and returns it if it is successfully created.

Use the configuration file "jaxp.properties". The file is in standard

Properties

format and typically located in the
conf directory of the Java installation. It contains the fully qualified
name of the implementation class with the key being the system property
defined above.

The jaxp.properties file is read only once by the JAXP implementation
and its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any property in jaxp.properties after it has been read for the first time.

The jaxp.properties file is read only once by the JAXP implementation
and its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any property in jaxp.properties after it has been read for the first time.

Use the service-provider loading facility, defined by the

ServiceLoader

class, to attempt to locate and load an
implementation of the service using the

default loading mechanism

:
the service-provider loading facility will use the

current thread's context class loader

to attempt to load the service. If the context class
loader is null, the

system class loader

will be used.

Each potential service provider is required to implement the method

isObjectModelSupported(String objectModel)

.
The first service provider found that supports the specified object
model is returned.

In case of

ServiceConfigurationError

an

XPathFactoryConfigurationException

will be thrown.

Platform default

XPathFactory

is located in a platform
specific way.
There must be a

platform default

XPathFactory

for the W3C DOM, i.e.

DEFAULT_OBJECT_MODEL_URI

.

If everything fails, an

XPathFactoryConfigurationException

will be thrown.

Tip for Trouble-shooting:

See

Properties.load(java.io.InputStream)

for exactly how a property file is parsed.
In particular, colons ':' need to be escaped in a property file, so make sure the URIs are properly escaped in it.
For example:

```java
http\://java.sun.com/jaxp/xpath/dom=org.acme.DomXPathFactory
```

Tip for Trouble-shooting:

See

Properties.load(java.io.InputStream)

for exactly how a property file is parsed.
In particular, colons ':' need to be escaped in a property file, so make sure the URIs are properly escaped in it.
For example:

```java
http\://java.sun.com/jaxp/xpath/dom=org.acme.DomXPathFactory
```

See

Properties.load(java.io.InputStream)

for exactly how a property file is parsed.
In particular, colons ':' need to be escaped in a property file, so make sure the URIs are properly escaped in it.
For example:

```java
http\://java.sun.com/jaxp/xpath/dom=org.acme.DomXPathFactory
```

http\://java.sun.com/jaxp/xpath/dom=org.acme.DomXPathFactory

newInstance

```java
public static
XPathFactory
newInstance​(
String
uri,

String
factoryClassName,

ClassLoader
classLoader)
throws
XPathFactoryConfigurationException
```

Obtain a new instance of a

XPathFactory

from a factory class name.

XPathFactory

is returned if specified factory class supports the specified object model.
This function is useful when there are multiple providers in the classpath.
It gives more control to the application as it can specify which provider
should be loaded.

Tip for Trouble-shooting

Setting the

jaxp.debug

system property will cause
this method to print a lot of debug messages
to

System.err

about what it is doing and where it is looking at.

If you have problems try:

```java
java -Djaxp.debug=1 YourProgram ....
```

**Parameters:** uri

- Identifies the underlying object model. The specification only defines the URI

DEFAULT_OBJECT_MODEL_URI

,

http://java.sun.com/jaxp/xpath/dom

for the W3C DOM, the org.w3c.dom package, and implementations are free to introduce
other URIs for other object models.
**Parameters:** factoryClassName

- fully qualified factory class name that provides implementation of

javax.xml.xpath.XPathFactory

.
**Parameters:** classLoader

-

ClassLoader

used to load the factory class. If

null

current

Thread

's context classLoader is used to load the factory class.
**Returns:** New instance of a

XPathFactory
**Throws:** XPathFactoryConfigurationException

- if

factoryClassName

is

null

, or
the factory class cannot be loaded, instantiated
or the factory class does not support the object model specified
in the

uri

parameter.
**Throws:** NullPointerException

- If

uri

is

null

.
**Throws:** IllegalArgumentException

- If

uri

is

null

or

uri.length() == 0

.
**Since:** 1.6
**See Also:** newInstance()

,

newInstance(String uri)

---

#### newInstance

public static

XPathFactory

newInstance​(

String

uri,

String

factoryClassName,

ClassLoader

classLoader)
throws

XPathFactoryConfigurationException

Obtain a new instance of a

XPathFactory

from a factory class name.

XPathFactory

is returned if specified factory class supports the specified object model.
This function is useful when there are multiple providers in the classpath.
It gives more control to the application as it can specify which provider
should be loaded.

Tip for Trouble-shooting

Setting the

jaxp.debug

system property will cause
this method to print a lot of debug messages
to

System.err

about what it is doing and where it is looking at.

If you have problems try:

```java
java -Djaxp.debug=1 YourProgram ....
```

Obtain a new instance of a

XPathFactory

from a factory class name.

XPathFactory

is returned if specified factory class supports the specified object model.
This function is useful when there are multiple providers in the classpath.
It gives more control to the application as it can specify which provider
should be loaded.

---

#### Tip for Trouble-shooting

Setting the

jaxp.debug

system property will cause
this method to print a lot of debug messages
to

System.err

about what it is doing and where it is looking at.

If you have problems try:

java -Djaxp.debug=1 YourProgram ....

isObjectModelSupported

```java
public abstract boolean isObjectModelSupported​(
String
objectModel)
```

Is specified object model supported by this

XPathFactory

?

**Parameters:** objectModel

- Specifies the object model which the returned

XPathFactory

will understand.
**Returns:** true

if

XPathFactory

supports

objectModel

, else

false

.
**Throws:** NullPointerException

- If

objectModel

is

null

.
**Throws:** IllegalArgumentException

- If

objectModel.length() == 0

.

---

#### isObjectModelSupported

public abstract boolean isObjectModelSupported​(

String

objectModel)

Is specified object model supported by this

XPathFactory

?

setFeature

```java
public abstract void setFeature​(
String
name,
boolean value)
throws
XPathFactoryConfigurationException
```

Set a feature for this

XPathFactory

and

XPath

s created by this factory.

Feature names are fully qualified

URI

s.
Implementations may define their own features.
An

XPathFactoryConfigurationException

is thrown if this

XPathFactory

or the

XPath

s
it creates cannot support the feature.
It is possible for an

XPathFactory

to expose a feature value
but be unable to change its state.

All implementations are required to support the

XMLConstants.FEATURE_SECURE_PROCESSING

feature.
When the feature is

true

, any reference to an external function is an error.
Under these conditions, the implementation must not call the

XPathFunctionResolver

and must throw an

XPathFunctionException

.

**Parameters:** name

- Feature name.
**Parameters:** value

- Is feature state

true

or

false

.
**Throws:** XPathFactoryConfigurationException

- if this

XPathFactory

or the

XPath

s
it creates cannot support this feature.
**Throws:** NullPointerException

- if

name

is

null

.

---

#### setFeature

public abstract void setFeature​(

String

name,
boolean value)
throws

XPathFactoryConfigurationException

Set a feature for this

XPathFactory

and

XPath

s created by this factory.

Feature names are fully qualified

URI

s.
Implementations may define their own features.
An

XPathFactoryConfigurationException

is thrown if this

XPathFactory

or the

XPath

s
it creates cannot support the feature.
It is possible for an

XPathFactory

to expose a feature value
but be unable to change its state.

All implementations are required to support the

XMLConstants.FEATURE_SECURE_PROCESSING

feature.
When the feature is

true

, any reference to an external function is an error.
Under these conditions, the implementation must not call the

XPathFunctionResolver

and must throw an

XPathFunctionException

.

Set a feature for this

XPathFactory

and

XPath

s created by this factory.

Feature names are fully qualified

URI

s.
Implementations may define their own features.
An

XPathFactoryConfigurationException

is thrown if this

XPathFactory

or the

XPath

s
it creates cannot support the feature.
It is possible for an

XPathFactory

to expose a feature value
but be unable to change its state.

All implementations are required to support the

XMLConstants.FEATURE_SECURE_PROCESSING

feature.
When the feature is

true

, any reference to an external function is an error.
Under these conditions, the implementation must not call the

XPathFunctionResolver

and must throw an

XPathFunctionException

.

getFeature

```java
public abstract boolean getFeature​(
String
name)
throws
XPathFactoryConfigurationException
```

Get the state of the named feature.

Feature names are fully qualified

URI

s.
Implementations may define their own features.
An

XPathFactoryConfigurationException

is thrown if this

XPathFactory

or the

XPath

s
it creates cannot support the feature.
It is possible for an

XPathFactory

to expose a feature value
but be unable to change its state.

**Parameters:** name

- Feature name.
**Returns:** State of the named feature.
**Throws:** XPathFactoryConfigurationException

- if this

XPathFactory

or the

XPath

s
it creates cannot support this feature.
**Throws:** NullPointerException

- if

name

is

null

.

---

#### getFeature

public abstract boolean getFeature​(

String

name)
throws

XPathFactoryConfigurationException

Get the state of the named feature.

Feature names are fully qualified

URI

s.
Implementations may define their own features.
An

XPathFactoryConfigurationException

is thrown if this

XPathFactory

or the

XPath

s
it creates cannot support the feature.
It is possible for an

XPathFactory

to expose a feature value
but be unable to change its state.

Get the state of the named feature.

Feature names are fully qualified

URI

s.
Implementations may define their own features.
An

XPathFactoryConfigurationException

is thrown if this

XPathFactory

or the

XPath

s
it creates cannot support the feature.
It is possible for an

XPathFactory

to expose a feature value
but be unable to change its state.

setXPathVariableResolver

```java
public abstract void setXPathVariableResolver​(
XPathVariableResolver
resolver)
```

Establish a default variable resolver.

Any

XPath

objects constructed from this factory will use
the specified resolver by default.

A

NullPointerException

is thrown if

resolver

is

null

.

**Parameters:** resolver

- Variable resolver.
**Throws:** NullPointerException

- If

resolver

is

null

.

---

#### setXPathVariableResolver

public abstract void setXPathVariableResolver​(

XPathVariableResolver

resolver)

Establish a default variable resolver.

Any

XPath

objects constructed from this factory will use
the specified resolver by default.

A

NullPointerException

is thrown if

resolver

is

null

.

Establish a default variable resolver.

Any

XPath

objects constructed from this factory will use
the specified resolver by default.

A

NullPointerException

is thrown if

resolver

is

null

.

setXPathFunctionResolver

```java
public abstract void setXPathFunctionResolver​(
XPathFunctionResolver
resolver)
```

Establish a default function resolver.

Any

XPath

objects constructed from this factory will
use the specified resolver by default.

A

NullPointerException

is thrown if

resolver

is

null

.

**Parameters:** resolver

- XPath function resolver.
**Throws:** NullPointerException

- If

resolver

is

null

.

---

#### setXPathFunctionResolver

public abstract void setXPathFunctionResolver​(

XPathFunctionResolver

resolver)

Establish a default function resolver.

Any

XPath

objects constructed from this factory will
use the specified resolver by default.

A

NullPointerException

is thrown if

resolver

is

null

.

Establish a default function resolver.

Any

XPath

objects constructed from this factory will
use the specified resolver by default.

A

NullPointerException

is thrown if

resolver

is

null

.

newXPath

```java
public abstract
XPath
newXPath()
```

Return a new

XPath

using the underlying object
model determined when the

XPathFactory

was instantiated.

**Returns:** New instance of an

XPath

.

---

#### newXPath

public abstract

XPath

newXPath()

Return a new

XPath

using the underlying object
model determined when the

XPathFactory

was instantiated.

---

