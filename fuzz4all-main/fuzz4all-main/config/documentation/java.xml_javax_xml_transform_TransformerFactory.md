# Class TransformerFactory

**Source:** `java.xml\javax\xml\transform\TransformerFactory.html`

### Class Description

```java
public abstract class
TransformerFactory

extends
Object
```

A TransformerFactory instance can be used to create

Transformer

and

Templates

objects.

The system property that determines which Factory implementation
to create is named

"javax.xml.transform.TransformerFactory"

.
This property names a concrete subclass of the

TransformerFactory

abstract class. If the property is not
defined, a platform default is be used.

**Direct Known Subclasses:** SAXTransformerFactory

---

### Field Details

*No entries found.*

### Constructor Details

#### protected TransformerFactory()

Default constructor is protected on purpose.

---

### Method Details

#### public static
TransformerFactory
newDefaultInstance()

Creates a new instance of the

TransformerFactory

builtin
system-default implementation.

**Returns:**
- A new instance of the

TransformerFactory

builtin
system-default implementation.

**Since:**
- 9

---

#### public static
TransformerFactory
newInstance()
throws
TransformerFactoryConfigurationError

Obtain a new instance of a

TransformerFactory

.
This static method creates a new factory instance.

This method uses the following ordered lookup procedure to determine
the

TransformerFactory

implementation class to load:

- Use the

javax.xml.transform.TransformerFactory

system
property.
- Use the configuration file "jaxp.properties". The file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. It contains the fully qualified
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
- Otherwise, the

system-default

implementation is returned.

Once an application has obtained a reference to a

TransformerFactory

it can use the factory to configure
and obtain transformer instances.

**Returns:**
- new TransformerFactory instance, never null.

**Throws:**
- TransformerFactoryConfigurationError

- Thrown in case of

service configuration error

or if
the implementation is not available or cannot be instantiated.

---

#### public static
TransformerFactory
newInstance​(
String
factoryClassName,

ClassLoader
classLoader)
throws
TransformerFactoryConfigurationError

Obtain a new instance of a

TransformerFactory

from factory class name.
This function is useful when there are multiple providers in the classpath.
It gives more control to the application as it can specify which provider
should be loaded.

Once an application has obtained a reference to a

TransformerFactory

it can use the factory to configure
and obtain transformer instances.

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
- factoryClassName

- fully qualified factory class name that provides implementation of

javax.xml.transform.TransformerFactory

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
- new TransformerFactory instance, never null.

**Throws:**
- TransformerFactoryConfigurationError

- if

factoryClassName

is

null

, or
the factory class cannot be loaded, instantiated.

**See Also:**
- newInstance()

**Since:**
- 1.6

---

#### public abstract
Transformer
newTransformer​(
Source
source)
throws
TransformerConfigurationException

Process the

Source

into a

Transformer

Object

. The

Source

is an XSLT document that
conforms to

XSL Transformations (XSLT) Version 1.0

. Care must
be taken not to use this

Transformer

in multiple

Thread

s running concurrently.
Different

TransformerFactories

can be used concurrently by
different

Thread

s.

**Parameters:**
- source

-

Source

of XSLT document used to create

Transformer

.
Examples of XML

Source

s include

DOMSource

,

SAXSource

, and

StreamSource

.

**Returns:**
- A

Transformer

object that may be used to perform
a transformation in a single

Thread

, never

null

.

**Throws:**
- TransformerConfigurationException

- Thrown if there are errors when
parsing the

Source

or it is not possible to create a

Transformer

instance.

**See Also:**
- XSL Transformations (XSLT) Version 1.0

---

#### public abstract
Transformer
newTransformer()
throws
TransformerConfigurationException

Create a new

Transformer

that performs a copy
of the

Source

to the

Result

.
i.e. the "

identity transform

".

**Returns:**
- A Transformer object that may be used to perform a transformation
in a single thread, never null.

**Throws:**
- TransformerConfigurationException

- When it is not
possible to create a

Transformer

instance.

---

#### public abstract
Templates
newTemplates​(
Source
source)
throws
TransformerConfigurationException

Process the Source into a Templates object, which is a
a compiled representation of the source. This Templates object
may then be used concurrently across multiple threads. Creating
a Templates object allows the TransformerFactory to do detailed
performance optimization of transformation instructions, without
penalizing runtime transformation.

**Parameters:**
- source

- An object that holds a URL, input stream, etc.

**Returns:**
- A Templates object capable of being used for transformation
purposes, never

null

.

**Throws:**
- TransformerConfigurationException

- When parsing to
construct the Templates object fails.

---

#### public abstract
Source
getAssociatedStylesheet​(
Source
source,

String
media,

String
title,

String
charset)
throws
TransformerConfigurationException

Get the stylesheet specification(s) associated with the
XML

Source

document via the

xml-stylesheet processing instruction

that match the given criteria.
Note that it is possible to return several stylesheets, in which case
they are applied as if they were a list of imports or cascades in a
single stylesheet.

**Parameters:**
- source

- The XML source document.
- media

- The media attribute to be matched. May be null, in which
case the prefered templates will be used (i.e. alternate = no).
- title

- The value of the title attribute to match. May be null.
- charset

- The value of the charset attribute to match. May be null.

**Returns:**
- A

Source

Object

suitable for passing
to the

TransformerFactory

.

**Throws:**
- TransformerConfigurationException

- An

Exception

is thrown if an error occurings during parsing of the

source

.

**See Also:**
- Associating Style Sheets with XML documents Version 1.0

---

#### public abstract void setURIResolver​(
URIResolver
resolver)

Set an object that is used by default during the transformation
to resolve URIs used in document(), xsl:import, or xsl:include.

**Parameters:**
- resolver

- An object that implements the URIResolver interface,
or null.

---

#### public abstract
URIResolver
getURIResolver()

Get the object that is used by default during the transformation
to resolve URIs used in document(), xsl:import, or xsl:include.

**Returns:**
- The URIResolver that was set with setURIResolver.

---

#### public abstract void setFeature​(
String
name,
boolean value)
throws
TransformerConfigurationException

Set a feature for this

TransformerFactory

and

Transformer

s
or

Template

s created by this factory.

Feature names are fully qualified

URI

s.
Implementations may define their own features.
An

TransformerConfigurationException

is thrown if this

TransformerFactory

or the

Transformer

s or

Template

s it creates cannot support the feature.
It is possible for an

TransformerFactory

to expose a feature value but be unable to change its state.

All implementations are required to support the

XMLConstants.FEATURE_SECURE_PROCESSING

feature.
When the feature is:

- true

: the implementation will limit XML processing to conform to implementation limits
and behave in a secure fashion as defined by the implementation.
Examples include resolving user defined style sheets and functions.
If XML processing is limited for security reasons, it will be reported via a call to the registered

ErrorListener.fatalError(TransformerException exception)

.
See

setErrorListener(ErrorListener listener)

.
- false

: the implementation will processing XML according to the XML specifications without
regard to possible implementation limits.

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
- TransformerConfigurationException

- if this

TransformerFactory

or the

Transformer

s or

Template

s it creates cannot support this feature.
- NullPointerException

- If the

name

parameter is null.

---

#### public abstract boolean getFeature​(
String
name)

Look up the value of a feature.

Feature names are fully qualified

URI

s.
Implementations may define their own features.

false

is returned if this

TransformerFactory

or the

Transformer

s or

Template

s it creates cannot support the feature.
It is possible for an

TransformerFactory

to expose a feature value but be unable to change its state.

**Parameters:**
- name

- Feature name.

**Returns:**
- The current state of the feature,

true

or

false

.

**Throws:**
- NullPointerException

- If the

name

parameter is null.

---

#### public abstract void setAttribute​(
String
name,

Object
value)

Allows the user to set specific attributes on the underlying
implementation. An attribute in this context is defined to
be an option that the implementation provides.
An

IllegalArgumentException

is thrown if the underlying
implementation doesn't recognize the attribute.

All implementations that implement JAXP 1.5 or newer are required to
support the

XMLConstants.ACCESS_EXTERNAL_DTD

and

XMLConstants.ACCESS_EXTERNAL_STYLESHEET

properties.

- Access to external DTDs in the source file is restricted to the protocols
specified by the

XMLConstants.ACCESS_EXTERNAL_DTD

property.
If access is denied during transformation due to the restriction of this property,

TransformerException

will be thrown by

Transformer.transform(Source, Result)

.

Access to external DTDs in the stylesheet is restricted to the protocols
specified by the

XMLConstants.ACCESS_EXTERNAL_DTD

property.
If access is denied during the creation of a new transformer due to the
restriction of this property,

TransformerConfigurationException

will be thrown
by the

newTransformer(Source)

method.

Access to external reference set by the stylesheet processing instruction,
Import and Include element is restricted to the protocols specified by the

XMLConstants.ACCESS_EXTERNAL_STYLESHEET

property.
If access is denied during the creation of a new transformer due to the
restriction of this property,

TransformerConfigurationException

will be thrown
by the

newTransformer(Source)

method.

Access to external document through XSLT document function is restricted
to the protocols specified by the property. If access is denied during
the transformation due to the restriction of this property,

TransformerException

will be thrown by the

Transformer.transform(Source, Result)

method.

**Parameters:**
- name

- The name of the attribute.
- value

- The value of the attribute.

**Throws:**
- IllegalArgumentException

- When implementation does not
recognize the attribute.

---

#### public abstract
Object
getAttribute​(
String
name)

Allows the user to retrieve specific attributes on the underlying
implementation.
An

IllegalArgumentException

is thrown if the underlying
implementation doesn't recognize the attribute.

**Parameters:**
- name

- The name of the attribute.

**Returns:**
- value The value of the attribute.

**Throws:**
- IllegalArgumentException

- When implementation does not
recognize the attribute.

---

#### public abstract void setErrorListener​(
ErrorListener
listener)

Set the error event listener for the TransformerFactory, which
is used for the processing of transformation instructions,
and not for the transformation itself.
An

IllegalArgumentException

is thrown if the

ErrorListener

listener is

null

.

**Parameters:**
- listener

- The new error listener.

**Throws:**
- IllegalArgumentException

- When

listener

is

null

---

#### public abstract
ErrorListener
getErrorListener()

Get the error event handler for the TransformerFactory.

**Returns:**
- The current error handler, which should never be null.

---

### Additional Sections

#### Class TransformerFactory

java.lang.Object

- javax.xml.transform.TransformerFactory

javax.xml.transform.TransformerFactory

**Direct Known Subclasses:** SAXTransformerFactory

```java
public abstract class
TransformerFactory

extends
Object
```

A TransformerFactory instance can be used to create

Transformer

and

Templates

objects.

The system property that determines which Factory implementation
to create is named

"javax.xml.transform.TransformerFactory"

.
This property names a concrete subclass of the

TransformerFactory

abstract class. If the property is not
defined, a platform default is be used.

**Since:** 1.5

public abstract class

TransformerFactory

extends

Object

A TransformerFactory instance can be used to create

Transformer

and

Templates

objects.

The system property that determines which Factory implementation
to create is named

"javax.xml.transform.TransformerFactory"

.
This property names a concrete subclass of the

TransformerFactory

abstract class. If the property is not
defined, a platform default is be used.

The system property that determines which Factory implementation
to create is named

"javax.xml.transform.TransformerFactory"

.
This property names a concrete subclass of the

TransformerFactory

abstract class. If the property is not
defined, a platform default is be used.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

TransformerFactory

()

Default constructor is protected on purpose.

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

abstract

Source

getAssociatedStylesheet

​(

Source

source,

String

media,

String

title,

String

charset)

Get the stylesheet specification(s) associated with the
XML

Source

document via the

xml-stylesheet processing instruction

that match the given criteria.

abstract

Object

getAttribute

​(

String

name)

Allows the user to retrieve specific attributes on the underlying
implementation.

abstract

ErrorListener

getErrorListener

()

Get the error event handler for the TransformerFactory.

abstract boolean

getFeature

​(

String

name)

Look up the value of a feature.

abstract

URIResolver

getURIResolver

()

Get the object that is used by default during the transformation
to resolve URIs used in document(), xsl:import, or xsl:include.

static

TransformerFactory

newDefaultInstance

()

Creates a new instance of the

TransformerFactory

builtin
system-default implementation.

static

TransformerFactory

newInstance

()

Obtain a new instance of a

TransformerFactory

.

static

TransformerFactory

newInstance

​(

String

factoryClassName,

ClassLoader

classLoader)

Obtain a new instance of a

TransformerFactory

from factory class name.

abstract

Templates

newTemplates

​(

Source

source)

Process the Source into a Templates object, which is a
a compiled representation of the source.

abstract

Transformer

newTransformer

()

Create a new

Transformer

that performs a copy
of the

Source

to the

Result

.

abstract

Transformer

newTransformer

​(

Source

source)

Process the

Source

into a

Transformer

Object

.

abstract void

setAttribute

​(

String

name,

Object

value)

Allows the user to set specific attributes on the underlying
implementation.

abstract void

setErrorListener

​(

ErrorListener

listener)

Set the error event listener for the TransformerFactory, which
is used for the processing of transformation instructions,
and not for the transformation itself.

abstract void

setFeature

​(

String

name,
boolean value)

Set a feature for this

TransformerFactory

and

Transformer

s
or

Template

s created by this factory.

abstract void

setURIResolver

​(

URIResolver

resolver)

Set an object that is used by default during the transformation
to resolve URIs used in document(), xsl:import, or xsl:include.

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

TransformerFactory

()

Default constructor is protected on purpose.

---

#### Constructor Summary

Default constructor is protected on purpose.

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

Source

getAssociatedStylesheet

​(

Source

source,

String

media,

String

title,

String

charset)

Get the stylesheet specification(s) associated with the
XML

Source

document via the

xml-stylesheet processing instruction

that match the given criteria.

abstract

Object

getAttribute

​(

String

name)

Allows the user to retrieve specific attributes on the underlying
implementation.

abstract

ErrorListener

getErrorListener

()

Get the error event handler for the TransformerFactory.

abstract boolean

getFeature

​(

String

name)

Look up the value of a feature.

abstract

URIResolver

getURIResolver

()

Get the object that is used by default during the transformation
to resolve URIs used in document(), xsl:import, or xsl:include.

static

TransformerFactory

newDefaultInstance

()

Creates a new instance of the

TransformerFactory

builtin
system-default implementation.

static

TransformerFactory

newInstance

()

Obtain a new instance of a

TransformerFactory

.

static

TransformerFactory

newInstance

​(

String

factoryClassName,

ClassLoader

classLoader)

Obtain a new instance of a

TransformerFactory

from factory class name.

abstract

Templates

newTemplates

​(

Source

source)

Process the Source into a Templates object, which is a
a compiled representation of the source.

abstract

Transformer

newTransformer

()

Create a new

Transformer

that performs a copy
of the

Source

to the

Result

.

abstract

Transformer

newTransformer

​(

Source

source)

Process the

Source

into a

Transformer

Object

.

abstract void

setAttribute

​(

String

name,

Object

value)

Allows the user to set specific attributes on the underlying
implementation.

abstract void

setErrorListener

​(

ErrorListener

listener)

Set the error event listener for the TransformerFactory, which
is used for the processing of transformation instructions,
and not for the transformation itself.

abstract void

setFeature

​(

String

name,
boolean value)

Set a feature for this

TransformerFactory

and

Transformer

s
or

Template

s created by this factory.

abstract void

setURIResolver

​(

URIResolver

resolver)

Set an object that is used by default during the transformation
to resolve URIs used in document(), xsl:import, or xsl:include.

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

Get the stylesheet specification(s) associated with the
XML

Source

document via the

xml-stylesheet processing instruction

that match the given criteria.

Allows the user to retrieve specific attributes on the underlying
implementation.

Get the error event handler for the TransformerFactory.

Look up the value of a feature.

Get the object that is used by default during the transformation
to resolve URIs used in document(), xsl:import, or xsl:include.

Creates a new instance of the

TransformerFactory

builtin
system-default implementation.

Obtain a new instance of a

TransformerFactory

.

Obtain a new instance of a

TransformerFactory

from factory class name.

Process the Source into a Templates object, which is a
a compiled representation of the source.

Create a new

Transformer

that performs a copy
of the

Source

to the

Result

.

Process the

Source

into a

Transformer

Object

.

Allows the user to set specific attributes on the underlying
implementation.

Set the error event listener for the TransformerFactory, which
is used for the processing of transformation instructions,
and not for the transformation itself.

Set a feature for this

TransformerFactory

and

Transformer

s
or

Template

s created by this factory.

Set an object that is used by default during the transformation
to resolve URIs used in document(), xsl:import, or xsl:include.

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

- TransformerFactory

```java
protected TransformerFactory()
```

Default constructor is protected on purpose.

============ METHOD DETAIL ==========

- Method Detail

- newDefaultInstance

```java
public static
TransformerFactory
newDefaultInstance()
```

Creates a new instance of the

TransformerFactory

builtin
system-default implementation.

**Returns:** A new instance of the

TransformerFactory

builtin
system-default implementation.
**Since:** 9

- newInstance

```java
public static
TransformerFactory
newInstance()
throws
TransformerFactoryConfigurationError
```

Obtain a new instance of a

TransformerFactory

.
This static method creates a new factory instance.

This method uses the following ordered lookup procedure to determine
the

TransformerFactory

implementation class to load:

- Use the

javax.xml.transform.TransformerFactory

system
property.
- Use the configuration file "jaxp.properties". The file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. It contains the fully qualified
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
- Otherwise, the

system-default

implementation is returned.

Once an application has obtained a reference to a

TransformerFactory

it can use the factory to configure
and obtain transformer instances.

**Returns:** new TransformerFactory instance, never null.
**Throws:** TransformerFactoryConfigurationError

- Thrown in case of

service configuration error

or if
the implementation is not available or cannot be instantiated.

- newInstance

```java
public static
TransformerFactory
newInstance​(
String
factoryClassName,

ClassLoader
classLoader)
throws
TransformerFactoryConfigurationError
```

Obtain a new instance of a

TransformerFactory

from factory class name.
This function is useful when there are multiple providers in the classpath.
It gives more control to the application as it can specify which provider
should be loaded.

Once an application has obtained a reference to a

TransformerFactory

it can use the factory to configure
and obtain transformer instances.

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

**Parameters:** factoryClassName

- fully qualified factory class name that provides implementation of

javax.xml.transform.TransformerFactory

.
**Parameters:** classLoader

-

ClassLoader

used to load the factory class. If

null

current

Thread

's context classLoader is used to load the factory class.
**Returns:** new TransformerFactory instance, never null.
**Throws:** TransformerFactoryConfigurationError

- if

factoryClassName

is

null

, or
the factory class cannot be loaded, instantiated.
**Since:** 1.6
**See Also:** newInstance()

- newTransformer

```java
public abstract
Transformer
newTransformer​(
Source
source)
throws
TransformerConfigurationException
```

Process the

Source

into a

Transformer

Object

. The

Source

is an XSLT document that
conforms to

XSL Transformations (XSLT) Version 1.0

. Care must
be taken not to use this

Transformer

in multiple

Thread

s running concurrently.
Different

TransformerFactories

can be used concurrently by
different

Thread

s.

**Parameters:** source

-

Source

of XSLT document used to create

Transformer

.
Examples of XML

Source

s include

DOMSource

,

SAXSource

, and

StreamSource

.
**Returns:** A

Transformer

object that may be used to perform
a transformation in a single

Thread

, never

null

.
**Throws:** TransformerConfigurationException

- Thrown if there are errors when
parsing the

Source

or it is not possible to create a

Transformer

instance.
**See Also:** XSL Transformations (XSLT) Version 1.0

- newTransformer

```java
public abstract
Transformer
newTransformer()
throws
TransformerConfigurationException
```

Create a new

Transformer

that performs a copy
of the

Source

to the

Result

.
i.e. the "

identity transform

".

**Returns:** A Transformer object that may be used to perform a transformation
in a single thread, never null.
**Throws:** TransformerConfigurationException

- When it is not
possible to create a

Transformer

instance.

- newTemplates

```java
public abstract
Templates
newTemplates​(
Source
source)
throws
TransformerConfigurationException
```

Process the Source into a Templates object, which is a
a compiled representation of the source. This Templates object
may then be used concurrently across multiple threads. Creating
a Templates object allows the TransformerFactory to do detailed
performance optimization of transformation instructions, without
penalizing runtime transformation.

**Parameters:** source

- An object that holds a URL, input stream, etc.
**Returns:** A Templates object capable of being used for transformation
purposes, never

null

.
**Throws:** TransformerConfigurationException

- When parsing to
construct the Templates object fails.

- getAssociatedStylesheet

```java
public abstract
Source
getAssociatedStylesheet​(
Source
source,

String
media,

String
title,

String
charset)
throws
TransformerConfigurationException
```

Get the stylesheet specification(s) associated with the
XML

Source

document via the

xml-stylesheet processing instruction

that match the given criteria.
Note that it is possible to return several stylesheets, in which case
they are applied as if they were a list of imports or cascades in a
single stylesheet.

**Parameters:** source

- The XML source document.
**Parameters:** media

- The media attribute to be matched. May be null, in which
case the prefered templates will be used (i.e. alternate = no).
**Parameters:** title

- The value of the title attribute to match. May be null.
**Parameters:** charset

- The value of the charset attribute to match. May be null.
**Returns:** A

Source

Object

suitable for passing
to the

TransformerFactory

.
**Throws:** TransformerConfigurationException

- An

Exception

is thrown if an error occurings during parsing of the

source

.
**See Also:** Associating Style Sheets with XML documents Version 1.0

- setURIResolver

```java
public abstract void setURIResolver​(
URIResolver
resolver)
```

Set an object that is used by default during the transformation
to resolve URIs used in document(), xsl:import, or xsl:include.

**Parameters:** resolver

- An object that implements the URIResolver interface,
or null.

- getURIResolver

```java
public abstract
URIResolver
getURIResolver()
```

Get the object that is used by default during the transformation
to resolve URIs used in document(), xsl:import, or xsl:include.

**Returns:** The URIResolver that was set with setURIResolver.

- setFeature

```java
public abstract void setFeature​(
String
name,
boolean value)
throws
TransformerConfigurationException
```

Set a feature for this

TransformerFactory

and

Transformer

s
or

Template

s created by this factory.

Feature names are fully qualified

URI

s.
Implementations may define their own features.
An

TransformerConfigurationException

is thrown if this

TransformerFactory

or the

Transformer

s or

Template

s it creates cannot support the feature.
It is possible for an

TransformerFactory

to expose a feature value but be unable to change its state.

All implementations are required to support the

XMLConstants.FEATURE_SECURE_PROCESSING

feature.
When the feature is:

- true

: the implementation will limit XML processing to conform to implementation limits
and behave in a secure fashion as defined by the implementation.
Examples include resolving user defined style sheets and functions.
If XML processing is limited for security reasons, it will be reported via a call to the registered

ErrorListener.fatalError(TransformerException exception)

.
See

setErrorListener(ErrorListener listener)

.
- false

: the implementation will processing XML according to the XML specifications without
regard to possible implementation limits.

**Parameters:** name

- Feature name.
**Parameters:** value

- Is feature state

true

or

false

.
**Throws:** TransformerConfigurationException

- if this

TransformerFactory

or the

Transformer

s or

Template

s it creates cannot support this feature.
**Throws:** NullPointerException

- If the

name

parameter is null.

- getFeature

```java
public abstract boolean getFeature​(
String
name)
```

Look up the value of a feature.

Feature names are fully qualified

URI

s.
Implementations may define their own features.

false

is returned if this

TransformerFactory

or the

Transformer

s or

Template

s it creates cannot support the feature.
It is possible for an

TransformerFactory

to expose a feature value but be unable to change its state.

**Parameters:** name

- Feature name.
**Returns:** The current state of the feature,

true

or

false

.
**Throws:** NullPointerException

- If the

name

parameter is null.

- setAttribute

```java
public abstract void setAttribute​(
String
name,

Object
value)
```

Allows the user to set specific attributes on the underlying
implementation. An attribute in this context is defined to
be an option that the implementation provides.
An

IllegalArgumentException

is thrown if the underlying
implementation doesn't recognize the attribute.

All implementations that implement JAXP 1.5 or newer are required to
support the

XMLConstants.ACCESS_EXTERNAL_DTD

and

XMLConstants.ACCESS_EXTERNAL_STYLESHEET

properties.

- Access to external DTDs in the source file is restricted to the protocols
specified by the

XMLConstants.ACCESS_EXTERNAL_DTD

property.
If access is denied during transformation due to the restriction of this property,

TransformerException

will be thrown by

Transformer.transform(Source, Result)

.

Access to external DTDs in the stylesheet is restricted to the protocols
specified by the

XMLConstants.ACCESS_EXTERNAL_DTD

property.
If access is denied during the creation of a new transformer due to the
restriction of this property,

TransformerConfigurationException

will be thrown
by the

newTransformer(Source)

method.

Access to external reference set by the stylesheet processing instruction,
Import and Include element is restricted to the protocols specified by the

XMLConstants.ACCESS_EXTERNAL_STYLESHEET

property.
If access is denied during the creation of a new transformer due to the
restriction of this property,

TransformerConfigurationException

will be thrown
by the

newTransformer(Source)

method.

Access to external document through XSLT document function is restricted
to the protocols specified by the property. If access is denied during
the transformation due to the restriction of this property,

TransformerException

will be thrown by the

Transformer.transform(Source, Result)

method.

**Parameters:** name

- The name of the attribute.
**Parameters:** value

- The value of the attribute.
**Throws:** IllegalArgumentException

- When implementation does not
recognize the attribute.

- getAttribute

```java
public abstract
Object
getAttribute​(
String
name)
```

Allows the user to retrieve specific attributes on the underlying
implementation.
An

IllegalArgumentException

is thrown if the underlying
implementation doesn't recognize the attribute.

**Parameters:** name

- The name of the attribute.
**Returns:** value The value of the attribute.
**Throws:** IllegalArgumentException

- When implementation does not
recognize the attribute.

- setErrorListener

```java
public abstract void setErrorListener​(
ErrorListener
listener)
```

Set the error event listener for the TransformerFactory, which
is used for the processing of transformation instructions,
and not for the transformation itself.
An

IllegalArgumentException

is thrown if the

ErrorListener

listener is

null

.

**Parameters:** listener

- The new error listener.
**Throws:** IllegalArgumentException

- When

listener

is

null

- getErrorListener

```java
public abstract
ErrorListener
getErrorListener()
```

Get the error event handler for the TransformerFactory.

**Returns:** The current error handler, which should never be null.

Constructor Detail

- TransformerFactory

```java
protected TransformerFactory()
```

Default constructor is protected on purpose.

---

#### Constructor Detail

TransformerFactory

```java
protected TransformerFactory()
```

Default constructor is protected on purpose.

---

#### TransformerFactory

protected TransformerFactory()

Default constructor is protected on purpose.

Method Detail

- newDefaultInstance

```java
public static
TransformerFactory
newDefaultInstance()
```

Creates a new instance of the

TransformerFactory

builtin
system-default implementation.

**Returns:** A new instance of the

TransformerFactory

builtin
system-default implementation.
**Since:** 9

- newInstance

```java
public static
TransformerFactory
newInstance()
throws
TransformerFactoryConfigurationError
```

Obtain a new instance of a

TransformerFactory

.
This static method creates a new factory instance.

This method uses the following ordered lookup procedure to determine
the

TransformerFactory

implementation class to load:

- Use the

javax.xml.transform.TransformerFactory

system
property.
- Use the configuration file "jaxp.properties". The file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. It contains the fully qualified
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
- Otherwise, the

system-default

implementation is returned.

Once an application has obtained a reference to a

TransformerFactory

it can use the factory to configure
and obtain transformer instances.

**Returns:** new TransformerFactory instance, never null.
**Throws:** TransformerFactoryConfigurationError

- Thrown in case of

service configuration error

or if
the implementation is not available or cannot be instantiated.

- newInstance

```java
public static
TransformerFactory
newInstance​(
String
factoryClassName,

ClassLoader
classLoader)
throws
TransformerFactoryConfigurationError
```

Obtain a new instance of a

TransformerFactory

from factory class name.
This function is useful when there are multiple providers in the classpath.
It gives more control to the application as it can specify which provider
should be loaded.

Once an application has obtained a reference to a

TransformerFactory

it can use the factory to configure
and obtain transformer instances.

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

**Parameters:** factoryClassName

- fully qualified factory class name that provides implementation of

javax.xml.transform.TransformerFactory

.
**Parameters:** classLoader

-

ClassLoader

used to load the factory class. If

null

current

Thread

's context classLoader is used to load the factory class.
**Returns:** new TransformerFactory instance, never null.
**Throws:** TransformerFactoryConfigurationError

- if

factoryClassName

is

null

, or
the factory class cannot be loaded, instantiated.
**Since:** 1.6
**See Also:** newInstance()

- newTransformer

```java
public abstract
Transformer
newTransformer​(
Source
source)
throws
TransformerConfigurationException
```

Process the

Source

into a

Transformer

Object

. The

Source

is an XSLT document that
conforms to

XSL Transformations (XSLT) Version 1.0

. Care must
be taken not to use this

Transformer

in multiple

Thread

s running concurrently.
Different

TransformerFactories

can be used concurrently by
different

Thread

s.

**Parameters:** source

-

Source

of XSLT document used to create

Transformer

.
Examples of XML

Source

s include

DOMSource

,

SAXSource

, and

StreamSource

.
**Returns:** A

Transformer

object that may be used to perform
a transformation in a single

Thread

, never

null

.
**Throws:** TransformerConfigurationException

- Thrown if there are errors when
parsing the

Source

or it is not possible to create a

Transformer

instance.
**See Also:** XSL Transformations (XSLT) Version 1.0

- newTransformer

```java
public abstract
Transformer
newTransformer()
throws
TransformerConfigurationException
```

Create a new

Transformer

that performs a copy
of the

Source

to the

Result

.
i.e. the "

identity transform

".

**Returns:** A Transformer object that may be used to perform a transformation
in a single thread, never null.
**Throws:** TransformerConfigurationException

- When it is not
possible to create a

Transformer

instance.

- newTemplates

```java
public abstract
Templates
newTemplates​(
Source
source)
throws
TransformerConfigurationException
```

Process the Source into a Templates object, which is a
a compiled representation of the source. This Templates object
may then be used concurrently across multiple threads. Creating
a Templates object allows the TransformerFactory to do detailed
performance optimization of transformation instructions, without
penalizing runtime transformation.

**Parameters:** source

- An object that holds a URL, input stream, etc.
**Returns:** A Templates object capable of being used for transformation
purposes, never

null

.
**Throws:** TransformerConfigurationException

- When parsing to
construct the Templates object fails.

- getAssociatedStylesheet

```java
public abstract
Source
getAssociatedStylesheet​(
Source
source,

String
media,

String
title,

String
charset)
throws
TransformerConfigurationException
```

Get the stylesheet specification(s) associated with the
XML

Source

document via the

xml-stylesheet processing instruction

that match the given criteria.
Note that it is possible to return several stylesheets, in which case
they are applied as if they were a list of imports or cascades in a
single stylesheet.

**Parameters:** source

- The XML source document.
**Parameters:** media

- The media attribute to be matched. May be null, in which
case the prefered templates will be used (i.e. alternate = no).
**Parameters:** title

- The value of the title attribute to match. May be null.
**Parameters:** charset

- The value of the charset attribute to match. May be null.
**Returns:** A

Source

Object

suitable for passing
to the

TransformerFactory

.
**Throws:** TransformerConfigurationException

- An

Exception

is thrown if an error occurings during parsing of the

source

.
**See Also:** Associating Style Sheets with XML documents Version 1.0

- setURIResolver

```java
public abstract void setURIResolver​(
URIResolver
resolver)
```

Set an object that is used by default during the transformation
to resolve URIs used in document(), xsl:import, or xsl:include.

**Parameters:** resolver

- An object that implements the URIResolver interface,
or null.

- getURIResolver

```java
public abstract
URIResolver
getURIResolver()
```

Get the object that is used by default during the transformation
to resolve URIs used in document(), xsl:import, or xsl:include.

**Returns:** The URIResolver that was set with setURIResolver.

- setFeature

```java
public abstract void setFeature​(
String
name,
boolean value)
throws
TransformerConfigurationException
```

Set a feature for this

TransformerFactory

and

Transformer

s
or

Template

s created by this factory.

Feature names are fully qualified

URI

s.
Implementations may define their own features.
An

TransformerConfigurationException

is thrown if this

TransformerFactory

or the

Transformer

s or

Template

s it creates cannot support the feature.
It is possible for an

TransformerFactory

to expose a feature value but be unable to change its state.

All implementations are required to support the

XMLConstants.FEATURE_SECURE_PROCESSING

feature.
When the feature is:

- true

: the implementation will limit XML processing to conform to implementation limits
and behave in a secure fashion as defined by the implementation.
Examples include resolving user defined style sheets and functions.
If XML processing is limited for security reasons, it will be reported via a call to the registered

ErrorListener.fatalError(TransformerException exception)

.
See

setErrorListener(ErrorListener listener)

.
- false

: the implementation will processing XML according to the XML specifications without
regard to possible implementation limits.

**Parameters:** name

- Feature name.
**Parameters:** value

- Is feature state

true

or

false

.
**Throws:** TransformerConfigurationException

- if this

TransformerFactory

or the

Transformer

s or

Template

s it creates cannot support this feature.
**Throws:** NullPointerException

- If the

name

parameter is null.

- getFeature

```java
public abstract boolean getFeature​(
String
name)
```

Look up the value of a feature.

Feature names are fully qualified

URI

s.
Implementations may define their own features.

false

is returned if this

TransformerFactory

or the

Transformer

s or

Template

s it creates cannot support the feature.
It is possible for an

TransformerFactory

to expose a feature value but be unable to change its state.

**Parameters:** name

- Feature name.
**Returns:** The current state of the feature,

true

or

false

.
**Throws:** NullPointerException

- If the

name

parameter is null.

- setAttribute

```java
public abstract void setAttribute​(
String
name,

Object
value)
```

Allows the user to set specific attributes on the underlying
implementation. An attribute in this context is defined to
be an option that the implementation provides.
An

IllegalArgumentException

is thrown if the underlying
implementation doesn't recognize the attribute.

All implementations that implement JAXP 1.5 or newer are required to
support the

XMLConstants.ACCESS_EXTERNAL_DTD

and

XMLConstants.ACCESS_EXTERNAL_STYLESHEET

properties.

- Access to external DTDs in the source file is restricted to the protocols
specified by the

XMLConstants.ACCESS_EXTERNAL_DTD

property.
If access is denied during transformation due to the restriction of this property,

TransformerException

will be thrown by

Transformer.transform(Source, Result)

.

Access to external DTDs in the stylesheet is restricted to the protocols
specified by the

XMLConstants.ACCESS_EXTERNAL_DTD

property.
If access is denied during the creation of a new transformer due to the
restriction of this property,

TransformerConfigurationException

will be thrown
by the

newTransformer(Source)

method.

Access to external reference set by the stylesheet processing instruction,
Import and Include element is restricted to the protocols specified by the

XMLConstants.ACCESS_EXTERNAL_STYLESHEET

property.
If access is denied during the creation of a new transformer due to the
restriction of this property,

TransformerConfigurationException

will be thrown
by the

newTransformer(Source)

method.

Access to external document through XSLT document function is restricted
to the protocols specified by the property. If access is denied during
the transformation due to the restriction of this property,

TransformerException

will be thrown by the

Transformer.transform(Source, Result)

method.

**Parameters:** name

- The name of the attribute.
**Parameters:** value

- The value of the attribute.
**Throws:** IllegalArgumentException

- When implementation does not
recognize the attribute.

- getAttribute

```java
public abstract
Object
getAttribute​(
String
name)
```

Allows the user to retrieve specific attributes on the underlying
implementation.
An

IllegalArgumentException

is thrown if the underlying
implementation doesn't recognize the attribute.

**Parameters:** name

- The name of the attribute.
**Returns:** value The value of the attribute.
**Throws:** IllegalArgumentException

- When implementation does not
recognize the attribute.

- setErrorListener

```java
public abstract void setErrorListener​(
ErrorListener
listener)
```

Set the error event listener for the TransformerFactory, which
is used for the processing of transformation instructions,
and not for the transformation itself.
An

IllegalArgumentException

is thrown if the

ErrorListener

listener is

null

.

**Parameters:** listener

- The new error listener.
**Throws:** IllegalArgumentException

- When

listener

is

null

- getErrorListener

```java
public abstract
ErrorListener
getErrorListener()
```

Get the error event handler for the TransformerFactory.

**Returns:** The current error handler, which should never be null.

---

#### Method Detail

newDefaultInstance

```java
public static
TransformerFactory
newDefaultInstance()
```

Creates a new instance of the

TransformerFactory

builtin
system-default implementation.

**Returns:** A new instance of the

TransformerFactory

builtin
system-default implementation.
**Since:** 9

---

#### newDefaultInstance

public static

TransformerFactory

newDefaultInstance()

Creates a new instance of the

TransformerFactory

builtin
system-default implementation.

newInstance

```java
public static
TransformerFactory
newInstance()
throws
TransformerFactoryConfigurationError
```

Obtain a new instance of a

TransformerFactory

.
This static method creates a new factory instance.

This method uses the following ordered lookup procedure to determine
the

TransformerFactory

implementation class to load:

- Use the

javax.xml.transform.TransformerFactory

system
property.
- Use the configuration file "jaxp.properties". The file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. It contains the fully qualified
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
- Otherwise, the

system-default

implementation is returned.

Once an application has obtained a reference to a

TransformerFactory

it can use the factory to configure
and obtain transformer instances.

**Returns:** new TransformerFactory instance, never null.
**Throws:** TransformerFactoryConfigurationError

- Thrown in case of

service configuration error

or if
the implementation is not available or cannot be instantiated.

---

#### newInstance

public static

TransformerFactory

newInstance()
throws

TransformerFactoryConfigurationError

Obtain a new instance of a

TransformerFactory

.
This static method creates a new factory instance.

This method uses the following ordered lookup procedure to determine
the

TransformerFactory

implementation class to load:

- Use the

javax.xml.transform.TransformerFactory

system
property.
- Use the configuration file "jaxp.properties". The file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. It contains the fully qualified
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
- Otherwise, the

system-default

implementation is returned.

Once an application has obtained a reference to a

TransformerFactory

it can use the factory to configure
and obtain transformer instances.

This method uses the following ordered lookup procedure to determine
the

TransformerFactory

implementation class to load:

- Use the

javax.xml.transform.TransformerFactory

system
property.
- Use the configuration file "jaxp.properties". The file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. It contains the fully qualified
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
- Otherwise, the

system-default

implementation is returned.

Once an application has obtained a reference to a

TransformerFactory

it can use the factory to configure
and obtain transformer instances.

Use the

javax.xml.transform.TransformerFactory

system
property.

Use the configuration file "jaxp.properties". The file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. It contains the fully qualified
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

Otherwise, the

system-default

implementation is returned.

Use the configuration file "jaxp.properties". The file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. It contains the fully qualified
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

Otherwise, the

system-default

implementation is returned.

Once an application has obtained a reference to a

TransformerFactory

it can use the factory to configure
and obtain transformer instances.

newInstance

```java
public static
TransformerFactory
newInstance​(
String
factoryClassName,

ClassLoader
classLoader)
throws
TransformerFactoryConfigurationError
```

Obtain a new instance of a

TransformerFactory

from factory class name.
This function is useful when there are multiple providers in the classpath.
It gives more control to the application as it can specify which provider
should be loaded.

Once an application has obtained a reference to a

TransformerFactory

it can use the factory to configure
and obtain transformer instances.

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

**Parameters:** factoryClassName

- fully qualified factory class name that provides implementation of

javax.xml.transform.TransformerFactory

.
**Parameters:** classLoader

-

ClassLoader

used to load the factory class. If

null

current

Thread

's context classLoader is used to load the factory class.
**Returns:** new TransformerFactory instance, never null.
**Throws:** TransformerFactoryConfigurationError

- if

factoryClassName

is

null

, or
the factory class cannot be loaded, instantiated.
**Since:** 1.6
**See Also:** newInstance()

---

#### newInstance

public static

TransformerFactory

newInstance​(

String

factoryClassName,

ClassLoader

classLoader)
throws

TransformerFactoryConfigurationError

Obtain a new instance of a

TransformerFactory

from factory class name.
This function is useful when there are multiple providers in the classpath.
It gives more control to the application as it can specify which provider
should be loaded.

Once an application has obtained a reference to a

TransformerFactory

it can use the factory to configure
and obtain transformer instances.

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

Once an application has obtained a reference to a

TransformerFactory

it can use the factory to configure
and obtain transformer instances.

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

```java
java -Djaxp.debug=1 YourProgram ....
```

If you have problems try:

```java
java -Djaxp.debug=1 YourProgram ....
```

java -Djaxp.debug=1 YourProgram ....

newTransformer

```java
public abstract
Transformer
newTransformer​(
Source
source)
throws
TransformerConfigurationException
```

Process the

Source

into a

Transformer

Object

. The

Source

is an XSLT document that
conforms to

XSL Transformations (XSLT) Version 1.0

. Care must
be taken not to use this

Transformer

in multiple

Thread

s running concurrently.
Different

TransformerFactories

can be used concurrently by
different

Thread

s.

**Parameters:** source

-

Source

of XSLT document used to create

Transformer

.
Examples of XML

Source

s include

DOMSource

,

SAXSource

, and

StreamSource

.
**Returns:** A

Transformer

object that may be used to perform
a transformation in a single

Thread

, never

null

.
**Throws:** TransformerConfigurationException

- Thrown if there are errors when
parsing the

Source

or it is not possible to create a

Transformer

instance.
**See Also:** XSL Transformations (XSLT) Version 1.0

---

#### newTransformer

public abstract

Transformer

newTransformer​(

Source

source)
throws

TransformerConfigurationException

Process the

Source

into a

Transformer

Object

. The

Source

is an XSLT document that
conforms to

XSL Transformations (XSLT) Version 1.0

. Care must
be taken not to use this

Transformer

in multiple

Thread

s running concurrently.
Different

TransformerFactories

can be used concurrently by
different

Thread

s.

newTransformer

```java
public abstract
Transformer
newTransformer()
throws
TransformerConfigurationException
```

Create a new

Transformer

that performs a copy
of the

Source

to the

Result

.
i.e. the "

identity transform

".

**Returns:** A Transformer object that may be used to perform a transformation
in a single thread, never null.
**Throws:** TransformerConfigurationException

- When it is not
possible to create a

Transformer

instance.

---

#### newTransformer

public abstract

Transformer

newTransformer()
throws

TransformerConfigurationException

Create a new

Transformer

that performs a copy
of the

Source

to the

Result

.
i.e. the "

identity transform

".

newTemplates

```java
public abstract
Templates
newTemplates​(
Source
source)
throws
TransformerConfigurationException
```

Process the Source into a Templates object, which is a
a compiled representation of the source. This Templates object
may then be used concurrently across multiple threads. Creating
a Templates object allows the TransformerFactory to do detailed
performance optimization of transformation instructions, without
penalizing runtime transformation.

**Parameters:** source

- An object that holds a URL, input stream, etc.
**Returns:** A Templates object capable of being used for transformation
purposes, never

null

.
**Throws:** TransformerConfigurationException

- When parsing to
construct the Templates object fails.

---

#### newTemplates

public abstract

Templates

newTemplates​(

Source

source)
throws

TransformerConfigurationException

Process the Source into a Templates object, which is a
a compiled representation of the source. This Templates object
may then be used concurrently across multiple threads. Creating
a Templates object allows the TransformerFactory to do detailed
performance optimization of transformation instructions, without
penalizing runtime transformation.

getAssociatedStylesheet

```java
public abstract
Source
getAssociatedStylesheet​(
Source
source,

String
media,

String
title,

String
charset)
throws
TransformerConfigurationException
```

Get the stylesheet specification(s) associated with the
XML

Source

document via the

xml-stylesheet processing instruction

that match the given criteria.
Note that it is possible to return several stylesheets, in which case
they are applied as if they were a list of imports or cascades in a
single stylesheet.

**Parameters:** source

- The XML source document.
**Parameters:** media

- The media attribute to be matched. May be null, in which
case the prefered templates will be used (i.e. alternate = no).
**Parameters:** title

- The value of the title attribute to match. May be null.
**Parameters:** charset

- The value of the charset attribute to match. May be null.
**Returns:** A

Source

Object

suitable for passing
to the

TransformerFactory

.
**Throws:** TransformerConfigurationException

- An

Exception

is thrown if an error occurings during parsing of the

source

.
**See Also:** Associating Style Sheets with XML documents Version 1.0

---

#### getAssociatedStylesheet

public abstract

Source

getAssociatedStylesheet​(

Source

source,

String

media,

String

title,

String

charset)
throws

TransformerConfigurationException

Get the stylesheet specification(s) associated with the
XML

Source

document via the

xml-stylesheet processing instruction

that match the given criteria.
Note that it is possible to return several stylesheets, in which case
they are applied as if they were a list of imports or cascades in a
single stylesheet.

setURIResolver

```java
public abstract void setURIResolver​(
URIResolver
resolver)
```

Set an object that is used by default during the transformation
to resolve URIs used in document(), xsl:import, or xsl:include.

**Parameters:** resolver

- An object that implements the URIResolver interface,
or null.

---

#### setURIResolver

public abstract void setURIResolver​(

URIResolver

resolver)

Set an object that is used by default during the transformation
to resolve URIs used in document(), xsl:import, or xsl:include.

getURIResolver

```java
public abstract
URIResolver
getURIResolver()
```

Get the object that is used by default during the transformation
to resolve URIs used in document(), xsl:import, or xsl:include.

**Returns:** The URIResolver that was set with setURIResolver.

---

#### getURIResolver

public abstract

URIResolver

getURIResolver()

Get the object that is used by default during the transformation
to resolve URIs used in document(), xsl:import, or xsl:include.

setFeature

```java
public abstract void setFeature​(
String
name,
boolean value)
throws
TransformerConfigurationException
```

Set a feature for this

TransformerFactory

and

Transformer

s
or

Template

s created by this factory.

Feature names are fully qualified

URI

s.
Implementations may define their own features.
An

TransformerConfigurationException

is thrown if this

TransformerFactory

or the

Transformer

s or

Template

s it creates cannot support the feature.
It is possible for an

TransformerFactory

to expose a feature value but be unable to change its state.

All implementations are required to support the

XMLConstants.FEATURE_SECURE_PROCESSING

feature.
When the feature is:

- true

: the implementation will limit XML processing to conform to implementation limits
and behave in a secure fashion as defined by the implementation.
Examples include resolving user defined style sheets and functions.
If XML processing is limited for security reasons, it will be reported via a call to the registered

ErrorListener.fatalError(TransformerException exception)

.
See

setErrorListener(ErrorListener listener)

.
- false

: the implementation will processing XML according to the XML specifications without
regard to possible implementation limits.

**Parameters:** name

- Feature name.
**Parameters:** value

- Is feature state

true

or

false

.
**Throws:** TransformerConfigurationException

- if this

TransformerFactory

or the

Transformer

s or

Template

s it creates cannot support this feature.
**Throws:** NullPointerException

- If the

name

parameter is null.

---

#### setFeature

public abstract void setFeature​(

String

name,
boolean value)
throws

TransformerConfigurationException

Set a feature for this

TransformerFactory

and

Transformer

s
or

Template

s created by this factory.

Feature names are fully qualified

URI

s.
Implementations may define their own features.
An

TransformerConfigurationException

is thrown if this

TransformerFactory

or the

Transformer

s or

Template

s it creates cannot support the feature.
It is possible for an

TransformerFactory

to expose a feature value but be unable to change its state.

All implementations are required to support the

XMLConstants.FEATURE_SECURE_PROCESSING

feature.
When the feature is:

- true

: the implementation will limit XML processing to conform to implementation limits
and behave in a secure fashion as defined by the implementation.
Examples include resolving user defined style sheets and functions.
If XML processing is limited for security reasons, it will be reported via a call to the registered

ErrorListener.fatalError(TransformerException exception)

.
See

setErrorListener(ErrorListener listener)

.
- false

: the implementation will processing XML according to the XML specifications without
regard to possible implementation limits.

Feature names are fully qualified

URI

s.
Implementations may define their own features.
An

TransformerConfigurationException

is thrown if this

TransformerFactory

or the

Transformer

s or

Template

s it creates cannot support the feature.
It is possible for an

TransformerFactory

to expose a feature value but be unable to change its state.

All implementations are required to support the

XMLConstants.FEATURE_SECURE_PROCESSING

feature.
When the feature is:

- true

: the implementation will limit XML processing to conform to implementation limits
and behave in a secure fashion as defined by the implementation.
Examples include resolving user defined style sheets and functions.
If XML processing is limited for security reasons, it will be reported via a call to the registered

ErrorListener.fatalError(TransformerException exception)

.
See

setErrorListener(ErrorListener listener)

.
- false

: the implementation will processing XML according to the XML specifications without
regard to possible implementation limits.

All implementations are required to support the

XMLConstants.FEATURE_SECURE_PROCESSING

feature.
When the feature is:

- true

: the implementation will limit XML processing to conform to implementation limits
and behave in a secure fashion as defined by the implementation.
Examples include resolving user defined style sheets and functions.
If XML processing is limited for security reasons, it will be reported via a call to the registered

ErrorListener.fatalError(TransformerException exception)

.
See

setErrorListener(ErrorListener listener)

.
- false

: the implementation will processing XML according to the XML specifications without
regard to possible implementation limits.

true

: the implementation will limit XML processing to conform to implementation limits
and behave in a secure fashion as defined by the implementation.
Examples include resolving user defined style sheets and functions.
If XML processing is limited for security reasons, it will be reported via a call to the registered

ErrorListener.fatalError(TransformerException exception)

.
See

setErrorListener(ErrorListener listener)

.

false

: the implementation will processing XML according to the XML specifications without
regard to possible implementation limits.

getFeature

```java
public abstract boolean getFeature​(
String
name)
```

Look up the value of a feature.

Feature names are fully qualified

URI

s.
Implementations may define their own features.

false

is returned if this

TransformerFactory

or the

Transformer

s or

Template

s it creates cannot support the feature.
It is possible for an

TransformerFactory

to expose a feature value but be unable to change its state.

**Parameters:** name

- Feature name.
**Returns:** The current state of the feature,

true

or

false

.
**Throws:** NullPointerException

- If the

name

parameter is null.

---

#### getFeature

public abstract boolean getFeature​(

String

name)

Look up the value of a feature.

Feature names are fully qualified

URI

s.
Implementations may define their own features.

false

is returned if this

TransformerFactory

or the

Transformer

s or

Template

s it creates cannot support the feature.
It is possible for an

TransformerFactory

to expose a feature value but be unable to change its state.

Feature names are fully qualified

URI

s.
Implementations may define their own features.

false

is returned if this

TransformerFactory

or the

Transformer

s or

Template

s it creates cannot support the feature.
It is possible for an

TransformerFactory

to expose a feature value but be unable to change its state.

setAttribute

```java
public abstract void setAttribute​(
String
name,

Object
value)
```

Allows the user to set specific attributes on the underlying
implementation. An attribute in this context is defined to
be an option that the implementation provides.
An

IllegalArgumentException

is thrown if the underlying
implementation doesn't recognize the attribute.

All implementations that implement JAXP 1.5 or newer are required to
support the

XMLConstants.ACCESS_EXTERNAL_DTD

and

XMLConstants.ACCESS_EXTERNAL_STYLESHEET

properties.

- Access to external DTDs in the source file is restricted to the protocols
specified by the

XMLConstants.ACCESS_EXTERNAL_DTD

property.
If access is denied during transformation due to the restriction of this property,

TransformerException

will be thrown by

Transformer.transform(Source, Result)

.

Access to external DTDs in the stylesheet is restricted to the protocols
specified by the

XMLConstants.ACCESS_EXTERNAL_DTD

property.
If access is denied during the creation of a new transformer due to the
restriction of this property,

TransformerConfigurationException

will be thrown
by the

newTransformer(Source)

method.

Access to external reference set by the stylesheet processing instruction,
Import and Include element is restricted to the protocols specified by the

XMLConstants.ACCESS_EXTERNAL_STYLESHEET

property.
If access is denied during the creation of a new transformer due to the
restriction of this property,

TransformerConfigurationException

will be thrown
by the

newTransformer(Source)

method.

Access to external document through XSLT document function is restricted
to the protocols specified by the property. If access is denied during
the transformation due to the restriction of this property,

TransformerException

will be thrown by the

Transformer.transform(Source, Result)

method.

**Parameters:** name

- The name of the attribute.
**Parameters:** value

- The value of the attribute.
**Throws:** IllegalArgumentException

- When implementation does not
recognize the attribute.

---

#### setAttribute

public abstract void setAttribute​(

String

name,

Object

value)

Allows the user to set specific attributes on the underlying
implementation. An attribute in this context is defined to
be an option that the implementation provides.
An

IllegalArgumentException

is thrown if the underlying
implementation doesn't recognize the attribute.

All implementations that implement JAXP 1.5 or newer are required to
support the

XMLConstants.ACCESS_EXTERNAL_DTD

and

XMLConstants.ACCESS_EXTERNAL_STYLESHEET

properties.

- Access to external DTDs in the source file is restricted to the protocols
specified by the

XMLConstants.ACCESS_EXTERNAL_DTD

property.
If access is denied during transformation due to the restriction of this property,

TransformerException

will be thrown by

Transformer.transform(Source, Result)

.

Access to external DTDs in the stylesheet is restricted to the protocols
specified by the

XMLConstants.ACCESS_EXTERNAL_DTD

property.
If access is denied during the creation of a new transformer due to the
restriction of this property,

TransformerConfigurationException

will be thrown
by the

newTransformer(Source)

method.

Access to external reference set by the stylesheet processing instruction,
Import and Include element is restricted to the protocols specified by the

XMLConstants.ACCESS_EXTERNAL_STYLESHEET

property.
If access is denied during the creation of a new transformer due to the
restriction of this property,

TransformerConfigurationException

will be thrown
by the

newTransformer(Source)

method.

Access to external document through XSLT document function is restricted
to the protocols specified by the property. If access is denied during
the transformation due to the restriction of this property,

TransformerException

will be thrown by the

Transformer.transform(Source, Result)

method.

All implementations that implement JAXP 1.5 or newer are required to
support the

XMLConstants.ACCESS_EXTERNAL_DTD

and

XMLConstants.ACCESS_EXTERNAL_STYLESHEET

properties.

- Access to external DTDs in the source file is restricted to the protocols
specified by the

XMLConstants.ACCESS_EXTERNAL_DTD

property.
If access is denied during transformation due to the restriction of this property,

TransformerException

will be thrown by

Transformer.transform(Source, Result)

.

Access to external DTDs in the stylesheet is restricted to the protocols
specified by the

XMLConstants.ACCESS_EXTERNAL_DTD

property.
If access is denied during the creation of a new transformer due to the
restriction of this property,

TransformerConfigurationException

will be thrown
by the

newTransformer(Source)

method.

Access to external reference set by the stylesheet processing instruction,
Import and Include element is restricted to the protocols specified by the

XMLConstants.ACCESS_EXTERNAL_STYLESHEET

property.
If access is denied during the creation of a new transformer due to the
restriction of this property,

TransformerConfigurationException

will be thrown
by the

newTransformer(Source)

method.

Access to external document through XSLT document function is restricted
to the protocols specified by the property. If access is denied during
the transformation due to the restriction of this property,

TransformerException

will be thrown by the

Transformer.transform(Source, Result)

method.

Access to external DTDs in the source file is restricted to the protocols
specified by the

XMLConstants.ACCESS_EXTERNAL_DTD

property.
If access is denied during transformation due to the restriction of this property,

TransformerException

will be thrown by

Transformer.transform(Source, Result)

.

Access to external DTDs in the stylesheet is restricted to the protocols
specified by the

XMLConstants.ACCESS_EXTERNAL_DTD

property.
If access is denied during the creation of a new transformer due to the
restriction of this property,

TransformerConfigurationException

will be thrown
by the

newTransformer(Source)

method.

Access to external reference set by the stylesheet processing instruction,
Import and Include element is restricted to the protocols specified by the

XMLConstants.ACCESS_EXTERNAL_STYLESHEET

property.
If access is denied during the creation of a new transformer due to the
restriction of this property,

TransformerConfigurationException

will be thrown
by the

newTransformer(Source)

method.

Access to external document through XSLT document function is restricted
to the protocols specified by the property. If access is denied during
the transformation due to the restriction of this property,

TransformerException

will be thrown by the

Transformer.transform(Source, Result)

method.

Access to external DTDs in the stylesheet is restricted to the protocols
specified by the

XMLConstants.ACCESS_EXTERNAL_DTD

property.
If access is denied during the creation of a new transformer due to the
restriction of this property,

TransformerConfigurationException

will be thrown
by the

newTransformer(Source)

method.

Access to external reference set by the stylesheet processing instruction,
Import and Include element is restricted to the protocols specified by the

XMLConstants.ACCESS_EXTERNAL_STYLESHEET

property.
If access is denied during the creation of a new transformer due to the
restriction of this property,

TransformerConfigurationException

will be thrown
by the

newTransformer(Source)

method.

Access to external document through XSLT document function is restricted
to the protocols specified by the property. If access is denied during
the transformation due to the restriction of this property,

TransformerException

will be thrown by the

Transformer.transform(Source, Result)

method.

Access to external reference set by the stylesheet processing instruction,
Import and Include element is restricted to the protocols specified by the

XMLConstants.ACCESS_EXTERNAL_STYLESHEET

property.
If access is denied during the creation of a new transformer due to the
restriction of this property,

TransformerConfigurationException

will be thrown
by the

newTransformer(Source)

method.

Access to external document through XSLT document function is restricted
to the protocols specified by the property. If access is denied during
the transformation due to the restriction of this property,

TransformerException

will be thrown by the

Transformer.transform(Source, Result)

method.

Access to external document through XSLT document function is restricted
to the protocols specified by the property. If access is denied during
the transformation due to the restriction of this property,

TransformerException

will be thrown by the

Transformer.transform(Source, Result)

method.

getAttribute

```java
public abstract
Object
getAttribute​(
String
name)
```

Allows the user to retrieve specific attributes on the underlying
implementation.
An

IllegalArgumentException

is thrown if the underlying
implementation doesn't recognize the attribute.

**Parameters:** name

- The name of the attribute.
**Returns:** value The value of the attribute.
**Throws:** IllegalArgumentException

- When implementation does not
recognize the attribute.

---

#### getAttribute

public abstract

Object

getAttribute​(

String

name)

Allows the user to retrieve specific attributes on the underlying
implementation.
An

IllegalArgumentException

is thrown if the underlying
implementation doesn't recognize the attribute.

setErrorListener

```java
public abstract void setErrorListener​(
ErrorListener
listener)
```

Set the error event listener for the TransformerFactory, which
is used for the processing of transformation instructions,
and not for the transformation itself.
An

IllegalArgumentException

is thrown if the

ErrorListener

listener is

null

.

**Parameters:** listener

- The new error listener.
**Throws:** IllegalArgumentException

- When

listener

is

null

---

#### setErrorListener

public abstract void setErrorListener​(

ErrorListener

listener)

Set the error event listener for the TransformerFactory, which
is used for the processing of transformation instructions,
and not for the transformation itself.
An

IllegalArgumentException

is thrown if the

ErrorListener

listener is

null

.

getErrorListener

```java
public abstract
ErrorListener
getErrorListener()
```

Get the error event handler for the TransformerFactory.

**Returns:** The current error handler, which should never be null.

---

#### getErrorListener

public abstract

ErrorListener

getErrorListener()

Get the error event handler for the TransformerFactory.

---

