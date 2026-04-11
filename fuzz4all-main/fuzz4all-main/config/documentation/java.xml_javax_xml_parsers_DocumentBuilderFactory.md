# Class DocumentBuilderFactory

**Source:** `java.xml\javax\xml\parsers\DocumentBuilderFactory.html`

### Class Description

```java
public abstract class
DocumentBuilderFactory

extends
Object
```

Defines a factory API that enables applications to obtain a
parser that produces DOM object trees from XML documents.

**Since:** 1.4

---

### Field Details

*No entries found.*

### Constructor Details

#### protected DocumentBuilderFactory()

Protected constructor to prevent instantiation.
Use

newInstance()

.

---

### Method Details

#### public static
DocumentBuilderFactory
newDefaultInstance()

Creates a new instance of the

DocumentBuilderFactory

builtin
system-default implementation.

**Returns:**
- A new instance of the

DocumentBuilderFactory

builtin
system-default implementation.

**Since:**
- 9

---

#### public static
DocumentBuilderFactory
newInstance()

Obtain a new instance of a

DocumentBuilderFactory

. This static method creates
a new factory instance.
This method uses the following ordered lookup procedure to determine
the

DocumentBuilderFactory

implementation class to
load:

- Use the

javax.xml.parsers.DocumentBuilderFactory

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

DocumentBuilderFactory

it can use the factory to
configure and obtain parser instances.

Tip for Trouble-shooting

Setting the

jaxp.debug

system property will cause
this method to print a lot of debug messages
to

System.err

about what it is doing and where it is looking at.

If you have problems loading

DocumentBuilder

s, try:

```java
java -Djaxp.debug=1 YourProgram ....
```

**Returns:**
- New instance of a

DocumentBuilderFactory

**Throws:**
- FactoryConfigurationError

- in case of

service configuration error

or if
the implementation is not available or cannot be instantiated.

---

#### public static
DocumentBuilderFactory
newInstance​(
String
factoryClassName,

ClassLoader
classLoader)

Obtain a new instance of a

DocumentBuilderFactory

from class name.
This function is useful when there are multiple providers in the classpath.
It gives more control to the application as it can specify which provider
should be loaded.

Once an application has obtained a reference to a

DocumentBuilderFactory

it can use the factory to configure and obtain parser instances.

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

- fully qualified factory class name that provides
implementation of

javax.xml.parsers.DocumentBuilderFactory

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

DocumentBuilderFactory

**Throws:**
- FactoryConfigurationError

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
DocumentBuilder
newDocumentBuilder()
throws
ParserConfigurationException

Creates a new instance of a

DocumentBuilder

using the currently configured parameters.

**Returns:**
- A new instance of a DocumentBuilder.

**Throws:**
- ParserConfigurationException

- if a DocumentBuilder
cannot be created which satisfies the configuration requested.

---

#### public void setNamespaceAware​(boolean awareness)

Specifies that the parser produced by this code will
provide support for XML namespaces. By default the value of this is set
to

false

**Parameters:**
- awareness

- true if the parser produced will provide support
for XML namespaces; false otherwise.

---

#### public void setValidating​(boolean validating)

Specifies that the parser produced by this code will
validate documents as they are parsed. By default the value of this
is set to

false

.

Note that "the validation" here means

a validating
parser

as defined in the XML recommendation.
In other words, it essentially just controls the DTD validation.
(except the legacy two properties defined in JAXP 1.2.)

To use modern schema languages such as W3C XML Schema or
RELAX NG instead of DTD, you can configure your parser to be
a non-validating parser by leaving the

setValidating(boolean)

method

false

, then use the

setSchema(Schema)

method to associate a schema to a parser.

**Parameters:**
- validating

- true if the parser produced will validate documents
as they are parsed; false otherwise.

---

#### public void setIgnoringElementContentWhitespace​(boolean whitespace)

Specifies that the parsers created by this factory must eliminate
whitespace in element content (sometimes known loosely as
'ignorable whitespace') when parsing XML documents (see XML Rec
2.10). Note that only whitespace which is directly contained within
element content that has an element only content model (see XML
Rec 3.2.1) will be eliminated. Due to reliance on the content model
this setting requires the parser to be in validating mode. By default
the value of this is set to

false

.

**Parameters:**
- whitespace

- true if the parser created must eliminate whitespace
in the element content when parsing XML documents;
false otherwise.

---

#### public void setExpandEntityReferences​(boolean expandEntityRef)

Specifies that the parser produced by this code will
expand entity reference nodes. By default the value of this is set to

true

**Parameters:**
- expandEntityRef

- true if the parser produced will expand entity
reference nodes; false otherwise.

---

#### public void setIgnoringComments​(boolean ignoreComments)

Specifies that the parser produced by this code will
ignore comments. By default the value of this is set to

false

.

**Parameters:**
- ignoreComments

-

boolean

value to ignore comments during processing

---

#### public void setCoalescing​(boolean coalescing)

Specifies that the parser produced by this code will
convert CDATA nodes to Text nodes and append it to the
adjacent (if any) text node. By default the value of this is set to

false

**Parameters:**
- coalescing

- true if the parser produced will convert CDATA nodes
to Text nodes and append it to the adjacent (if any)
text node; false otherwise.

---

#### public boolean isNamespaceAware()

Indicates whether or not the factory is configured to produce
parsers which are namespace aware.

**Returns:**
- true if the factory is configured to produce parsers which
are namespace aware; false otherwise.

---

#### public boolean isValidating()

Indicates whether or not the factory is configured to produce
parsers which validate the XML content during parse.

**Returns:**
- true if the factory is configured to produce parsers
which validate the XML content during parse; false otherwise.

---

#### public boolean isIgnoringElementContentWhitespace()

Indicates whether or not the factory is configured to produce
parsers which ignore ignorable whitespace in element content.

**Returns:**
- true if the factory is configured to produce parsers
which ignore ignorable whitespace in element content;
false otherwise.

---

#### public boolean isExpandEntityReferences()

Indicates whether or not the factory is configured to produce
parsers which expand entity reference nodes.

**Returns:**
- true if the factory is configured to produce parsers
which expand entity reference nodes; false otherwise.

---

#### public boolean isIgnoringComments()

Indicates whether or not the factory is configured to produce
parsers which ignores comments.

**Returns:**
- true if the factory is configured to produce parsers
which ignores comments; false otherwise.

---

#### public boolean isCoalescing()

Indicates whether or not the factory is configured to produce
parsers which converts CDATA nodes to Text nodes and appends it to
the adjacent (if any) Text node.

**Returns:**
- true if the factory is configured to produce parsers
which converts CDATA nodes to Text nodes and appends it to
the adjacent (if any) Text node; false otherwise.

---

#### public abstract void setAttribute​(
String
name,

Object
value)
throws
IllegalArgumentException

Allows the user to set specific attributes on the underlying
implementation.

All implementations that implement JAXP 1.5 or newer are required to
support the

XMLConstants.ACCESS_EXTERNAL_DTD

and

XMLConstants.ACCESS_EXTERNAL_SCHEMA

properties.

- Setting the

XMLConstants.ACCESS_EXTERNAL_DTD

property
restricts the access to external DTDs, external Entity References to the
protocols specified by the property.
If access is denied during parsing due to the restriction of this property,

SAXException

will be thrown by the parse methods defined by

DocumentBuilder

.
- Setting the

XMLConstants.ACCESS_EXTERNAL_SCHEMA

property
restricts the access to external Schema set by the schemaLocation attribute to
the protocols specified by the property. If access is denied during parsing
due to the restriction of this property,

SAXException

will be thrown by the parse methods defined by

DocumentBuilder

.

**Parameters:**
- name

- The name of the attribute.
- value

- The value of the attribute.

**Throws:**
- IllegalArgumentException

- thrown if the underlying
implementation doesn't recognize the attribute.

---

#### public abstract
Object
getAttribute​(
String
name)
throws
IllegalArgumentException

Allows the user to retrieve specific attributes on the underlying
implementation.

**Parameters:**
- name

- The name of the attribute.

**Returns:**
- value The value of the attribute.

**Throws:**
- IllegalArgumentException

- thrown if the underlying
implementation doesn't recognize the attribute.

---

#### public abstract void setFeature​(
String
name,
boolean value)
throws
ParserConfigurationException

Set a feature for this

DocumentBuilderFactory

and

DocumentBuilder

s created by this factory.

Feature names are fully qualified

URI

s.
Implementations may define their own features.
A

ParserConfigurationException

is thrown if this

DocumentBuilderFactory

or the

DocumentBuilder

s it creates cannot support the feature.
It is possible for a

DocumentBuilderFactory

to expose a feature value but be unable to change its state.

All implementations are required to support the

XMLConstants.FEATURE_SECURE_PROCESSING

feature.
When the feature is:

- true

: the implementation will limit XML processing to conform to implementation limits.
Examples include entity expansion limits and XML Schema constructs that would consume large amounts of resources.
If XML processing is limited for security reasons, it will be reported via a call to the registered

ErrorHandler.fatalError(SAXParseException exception)

.
See

DocumentBuilder.setErrorHandler(org.xml.sax.ErrorHandler errorHandler)

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
- ParserConfigurationException

- if this

DocumentBuilderFactory

or the

DocumentBuilder

s
it creates cannot support this feature.
- NullPointerException

- If the

name

parameter is null.

**Since:**
- 1.5

---

#### public abstract boolean getFeature​(
String
name)
throws
ParserConfigurationException

Get the state of the named feature.

Feature names are fully qualified

URI

s.
Implementations may define their own features.
An

ParserConfigurationException

is thrown if this

DocumentBuilderFactory

or the

DocumentBuilder

s it creates cannot support the feature.
It is possible for an

DocumentBuilderFactory

to expose a feature value but be unable to change its state.

**Parameters:**
- name

- Feature name.

**Returns:**
- State of the named feature.

**Throws:**
- ParserConfigurationException

- if this

DocumentBuilderFactory

or the

DocumentBuilder

s it creates cannot support this feature.

**Since:**
- 1.5

---

#### public
Schema
getSchema()

Gets the

Schema

object specified through
the

setSchema(Schema schema)

method.

**Returns:**
- the

Schema

object that was last set through
the

setSchema(Schema)

method, or null
if the method was not invoked since a

DocumentBuilderFactory

is created.

**Throws:**
- UnsupportedOperationException

- When implementation does not
override this method.

**Since:**
- 1.5

---

#### public void setSchema​(
Schema
schema)

Set the

Schema

to be used by parsers created
from this factory.

When a

Schema

is non-null, a parser will use a validator
created from it to validate documents before it passes information
down to the application.

When errors are found by the validator, the parser is responsible
to report them to the user-specified

ErrorHandler

(or if the error handler is not set, ignore them or throw them), just
like any other errors found by the parser itself.
In other words, if the user-specified

ErrorHandler

is set, it must receive those errors, and if not, they must be
treated according to the implementation specific
default error handling rules.

A validator may modify the outcome of a parse (for example by
adding default values that were missing in documents), and a parser
is responsible to make sure that the application will receive
modified DOM trees.

Initially, null is set as the

Schema

.

This processing will take effect even if
the

isValidating()

method returns

false

.

It is an error to use
the

http://java.sun.com/xml/jaxp/properties/schemaSource

property and/or the

http://java.sun.com/xml/jaxp/properties/schemaLanguage

property in conjunction with a

Schema

object.
Such configuration will cause a

ParserConfigurationException

exception when the

newDocumentBuilder()

is invoked.

Note for implementors

A parser must be able to work with any

Schema

implementation. However, parsers and schemas are allowed
to use implementation-specific custom mechanisms
as long as they yield the result described in the specification.

**Parameters:**
- schema

-

Schema

to use or

null

to remove a schema.

**Throws:**
- UnsupportedOperationException

- When implementation does not
override this method.

**Since:**
- 1.5

---

#### public void setXIncludeAware​(boolean state)

Set state of XInclude processing.

If XInclude markup is found in the document instance, should it be
processed as specified in

XML Inclusions (XInclude) Version 1.0

.

XInclude processing defaults to

false

.

**Parameters:**
- state

- Set XInclude processing to

true

or

false

**Throws:**
- UnsupportedOperationException

- When implementation does not
override this method.

**Since:**
- 1.5

---

#### public boolean isXIncludeAware()

Get state of XInclude processing.

**Returns:**
- current state of XInclude processing

**Throws:**
- UnsupportedOperationException

- When implementation does not
override this method.

**Since:**
- 1.5

---

### Additional Sections

#### Class DocumentBuilderFactory

java.lang.Object

- javax.xml.parsers.DocumentBuilderFactory

javax.xml.parsers.DocumentBuilderFactory

```java
public abstract class
DocumentBuilderFactory

extends
Object
```

Defines a factory API that enables applications to obtain a
parser that produces DOM object trees from XML documents.

**Since:** 1.4

public abstract class

DocumentBuilderFactory

extends

Object

Defines a factory API that enables applications to obtain a
parser that produces DOM object trees from XML documents.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

DocumentBuilderFactory

()

Protected constructor to prevent instantiation.

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

Object

getAttribute

​(

String

name)

Allows the user to retrieve specific attributes on the underlying
implementation.

abstract boolean

getFeature

​(

String

name)

Get the state of the named feature.

Schema

getSchema

()

Gets the

Schema

object specified through
the

setSchema(Schema schema)

method.

boolean

isCoalescing

()

Indicates whether or not the factory is configured to produce
parsers which converts CDATA nodes to Text nodes and appends it to
the adjacent (if any) Text node.

boolean

isExpandEntityReferences

()

Indicates whether or not the factory is configured to produce
parsers which expand entity reference nodes.

boolean

isIgnoringComments

()

Indicates whether or not the factory is configured to produce
parsers which ignores comments.

boolean

isIgnoringElementContentWhitespace

()

Indicates whether or not the factory is configured to produce
parsers which ignore ignorable whitespace in element content.

boolean

isNamespaceAware

()

Indicates whether or not the factory is configured to produce
parsers which are namespace aware.

boolean

isValidating

()

Indicates whether or not the factory is configured to produce
parsers which validate the XML content during parse.

boolean

isXIncludeAware

()

Get state of XInclude processing.

static

DocumentBuilderFactory

newDefaultInstance

()

Creates a new instance of the

DocumentBuilderFactory

builtin
system-default implementation.

abstract

DocumentBuilder

newDocumentBuilder

()

Creates a new instance of a

DocumentBuilder

using the currently configured parameters.

static

DocumentBuilderFactory

newInstance

()

Obtain a new instance of a

DocumentBuilderFactory

.

static

DocumentBuilderFactory

newInstance

​(

String

factoryClassName,

ClassLoader

classLoader)

Obtain a new instance of a

DocumentBuilderFactory

from class name.

abstract void

setAttribute

​(

String

name,

Object

value)

Allows the user to set specific attributes on the underlying
implementation.

void

setCoalescing

​(boolean coalescing)

Specifies that the parser produced by this code will
convert CDATA nodes to Text nodes and append it to the
adjacent (if any) text node.

void

setExpandEntityReferences

​(boolean expandEntityRef)

Specifies that the parser produced by this code will
expand entity reference nodes.

abstract void

setFeature

​(

String

name,
boolean value)

Set a feature for this

DocumentBuilderFactory

and

DocumentBuilder

s created by this factory.

void

setIgnoringComments

​(boolean ignoreComments)

Specifies that the parser produced by this code will
ignore comments.

void

setIgnoringElementContentWhitespace

​(boolean whitespace)

Specifies that the parsers created by this factory must eliminate
whitespace in element content (sometimes known loosely as
'ignorable whitespace') when parsing XML documents (see XML Rec
2.10).

void

setNamespaceAware

​(boolean awareness)

Specifies that the parser produced by this code will
provide support for XML namespaces.

void

setSchema

​(

Schema

schema)

Set the

Schema

to be used by parsers created
from this factory.

void

setValidating

​(boolean validating)

Specifies that the parser produced by this code will
validate documents as they are parsed.

void

setXIncludeAware

​(boolean state)

Set state of XInclude processing.

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

DocumentBuilderFactory

()

Protected constructor to prevent instantiation.

---

#### Constructor Summary

Protected constructor to prevent instantiation.

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

Object

getAttribute

​(

String

name)

Allows the user to retrieve specific attributes on the underlying
implementation.

abstract boolean

getFeature

​(

String

name)

Get the state of the named feature.

Schema

getSchema

()

Gets the

Schema

object specified through
the

setSchema(Schema schema)

method.

boolean

isCoalescing

()

Indicates whether or not the factory is configured to produce
parsers which converts CDATA nodes to Text nodes and appends it to
the adjacent (if any) Text node.

boolean

isExpandEntityReferences

()

Indicates whether or not the factory is configured to produce
parsers which expand entity reference nodes.

boolean

isIgnoringComments

()

Indicates whether or not the factory is configured to produce
parsers which ignores comments.

boolean

isIgnoringElementContentWhitespace

()

Indicates whether or not the factory is configured to produce
parsers which ignore ignorable whitespace in element content.

boolean

isNamespaceAware

()

Indicates whether or not the factory is configured to produce
parsers which are namespace aware.

boolean

isValidating

()

Indicates whether or not the factory is configured to produce
parsers which validate the XML content during parse.

boolean

isXIncludeAware

()

Get state of XInclude processing.

static

DocumentBuilderFactory

newDefaultInstance

()

Creates a new instance of the

DocumentBuilderFactory

builtin
system-default implementation.

abstract

DocumentBuilder

newDocumentBuilder

()

Creates a new instance of a

DocumentBuilder

using the currently configured parameters.

static

DocumentBuilderFactory

newInstance

()

Obtain a new instance of a

DocumentBuilderFactory

.

static

DocumentBuilderFactory

newInstance

​(

String

factoryClassName,

ClassLoader

classLoader)

Obtain a new instance of a

DocumentBuilderFactory

from class name.

abstract void

setAttribute

​(

String

name,

Object

value)

Allows the user to set specific attributes on the underlying
implementation.

void

setCoalescing

​(boolean coalescing)

Specifies that the parser produced by this code will
convert CDATA nodes to Text nodes and append it to the
adjacent (if any) text node.

void

setExpandEntityReferences

​(boolean expandEntityRef)

Specifies that the parser produced by this code will
expand entity reference nodes.

abstract void

setFeature

​(

String

name,
boolean value)

Set a feature for this

DocumentBuilderFactory

and

DocumentBuilder

s created by this factory.

void

setIgnoringComments

​(boolean ignoreComments)

Specifies that the parser produced by this code will
ignore comments.

void

setIgnoringElementContentWhitespace

​(boolean whitespace)

Specifies that the parsers created by this factory must eliminate
whitespace in element content (sometimes known loosely as
'ignorable whitespace') when parsing XML documents (see XML Rec
2.10).

void

setNamespaceAware

​(boolean awareness)

Specifies that the parser produced by this code will
provide support for XML namespaces.

void

setSchema

​(

Schema

schema)

Set the

Schema

to be used by parsers created
from this factory.

void

setValidating

​(boolean validating)

Specifies that the parser produced by this code will
validate documents as they are parsed.

void

setXIncludeAware

​(boolean state)

Set state of XInclude processing.

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

Allows the user to retrieve specific attributes on the underlying
implementation.

Get the state of the named feature.

Gets the

Schema

object specified through
the

setSchema(Schema schema)

method.

Indicates whether or not the factory is configured to produce
parsers which converts CDATA nodes to Text nodes and appends it to
the adjacent (if any) Text node.

Indicates whether or not the factory is configured to produce
parsers which expand entity reference nodes.

Indicates whether or not the factory is configured to produce
parsers which ignores comments.

Indicates whether or not the factory is configured to produce
parsers which ignore ignorable whitespace in element content.

Indicates whether or not the factory is configured to produce
parsers which are namespace aware.

Indicates whether or not the factory is configured to produce
parsers which validate the XML content during parse.

Get state of XInclude processing.

Creates a new instance of the

DocumentBuilderFactory

builtin
system-default implementation.

Creates a new instance of a

DocumentBuilder

using the currently configured parameters.

Obtain a new instance of a

DocumentBuilderFactory

.

Obtain a new instance of a

DocumentBuilderFactory

from class name.

Allows the user to set specific attributes on the underlying
implementation.

Specifies that the parser produced by this code will
convert CDATA nodes to Text nodes and append it to the
adjacent (if any) text node.

Specifies that the parser produced by this code will
expand entity reference nodes.

Set a feature for this

DocumentBuilderFactory

and

DocumentBuilder

s created by this factory.

Specifies that the parser produced by this code will
ignore comments.

Specifies that the parsers created by this factory must eliminate
whitespace in element content (sometimes known loosely as
'ignorable whitespace') when parsing XML documents (see XML Rec
2.10).

Specifies that the parser produced by this code will
provide support for XML namespaces.

Set the

Schema

to be used by parsers created
from this factory.

Specifies that the parser produced by this code will
validate documents as they are parsed.

Set state of XInclude processing.

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

- DocumentBuilderFactory

```java
protected DocumentBuilderFactory()
```

Protected constructor to prevent instantiation.
Use

newInstance()

.

============ METHOD DETAIL ==========

- Method Detail

- newDefaultInstance

```java
public static
DocumentBuilderFactory
newDefaultInstance()
```

Creates a new instance of the

DocumentBuilderFactory

builtin
system-default implementation.

**Returns:** A new instance of the

DocumentBuilderFactory

builtin
system-default implementation.
**Since:** 9

- newInstance

```java
public static
DocumentBuilderFactory
newInstance()
```

Obtain a new instance of a

DocumentBuilderFactory

. This static method creates
a new factory instance.
This method uses the following ordered lookup procedure to determine
the

DocumentBuilderFactory

implementation class to
load:

- Use the

javax.xml.parsers.DocumentBuilderFactory

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

DocumentBuilderFactory

it can use the factory to
configure and obtain parser instances.

Tip for Trouble-shooting

Setting the

jaxp.debug

system property will cause
this method to print a lot of debug messages
to

System.err

about what it is doing and where it is looking at.

If you have problems loading

DocumentBuilder

s, try:

```java
java -Djaxp.debug=1 YourProgram ....
```

**Returns:** New instance of a

DocumentBuilderFactory
**Throws:** FactoryConfigurationError

- in case of

service configuration error

or if
the implementation is not available or cannot be instantiated.

- newInstance

```java
public static
DocumentBuilderFactory
newInstance​(
String
factoryClassName,

ClassLoader
classLoader)
```

Obtain a new instance of a

DocumentBuilderFactory

from class name.
This function is useful when there are multiple providers in the classpath.
It gives more control to the application as it can specify which provider
should be loaded.

Once an application has obtained a reference to a

DocumentBuilderFactory

it can use the factory to configure and obtain parser instances.

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

- fully qualified factory class name that provides
implementation of

javax.xml.parsers.DocumentBuilderFactory

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

DocumentBuilderFactory
**Throws:** FactoryConfigurationError

- if

factoryClassName

is

null

, or
the factory class cannot be loaded, instantiated.
**Since:** 1.6
**See Also:** newInstance()

- newDocumentBuilder

```java
public abstract
DocumentBuilder
newDocumentBuilder()
throws
ParserConfigurationException
```

Creates a new instance of a

DocumentBuilder

using the currently configured parameters.

**Returns:** A new instance of a DocumentBuilder.
**Throws:** ParserConfigurationException

- if a DocumentBuilder
cannot be created which satisfies the configuration requested.

- setNamespaceAware

```java
public void setNamespaceAware​(boolean awareness)
```

Specifies that the parser produced by this code will
provide support for XML namespaces. By default the value of this is set
to

false

**Parameters:** awareness

- true if the parser produced will provide support
for XML namespaces; false otherwise.

- setValidating

```java
public void setValidating​(boolean validating)
```

Specifies that the parser produced by this code will
validate documents as they are parsed. By default the value of this
is set to

false

.

Note that "the validation" here means

a validating
parser

as defined in the XML recommendation.
In other words, it essentially just controls the DTD validation.
(except the legacy two properties defined in JAXP 1.2.)

To use modern schema languages such as W3C XML Schema or
RELAX NG instead of DTD, you can configure your parser to be
a non-validating parser by leaving the

setValidating(boolean)

method

false

, then use the

setSchema(Schema)

method to associate a schema to a parser.

**Parameters:** validating

- true if the parser produced will validate documents
as they are parsed; false otherwise.

- setIgnoringElementContentWhitespace

```java
public void setIgnoringElementContentWhitespace​(boolean whitespace)
```

Specifies that the parsers created by this factory must eliminate
whitespace in element content (sometimes known loosely as
'ignorable whitespace') when parsing XML documents (see XML Rec
2.10). Note that only whitespace which is directly contained within
element content that has an element only content model (see XML
Rec 3.2.1) will be eliminated. Due to reliance on the content model
this setting requires the parser to be in validating mode. By default
the value of this is set to

false

.

**Parameters:** whitespace

- true if the parser created must eliminate whitespace
in the element content when parsing XML documents;
false otherwise.

- setExpandEntityReferences

```java
public void setExpandEntityReferences​(boolean expandEntityRef)
```

Specifies that the parser produced by this code will
expand entity reference nodes. By default the value of this is set to

true

**Parameters:** expandEntityRef

- true if the parser produced will expand entity
reference nodes; false otherwise.

- setIgnoringComments

```java
public void setIgnoringComments​(boolean ignoreComments)
```

Specifies that the parser produced by this code will
ignore comments. By default the value of this is set to

false

.

**Parameters:** ignoreComments

-

boolean

value to ignore comments during processing

- setCoalescing

```java
public void setCoalescing​(boolean coalescing)
```

Specifies that the parser produced by this code will
convert CDATA nodes to Text nodes and append it to the
adjacent (if any) text node. By default the value of this is set to

false

**Parameters:** coalescing

- true if the parser produced will convert CDATA nodes
to Text nodes and append it to the adjacent (if any)
text node; false otherwise.

- isNamespaceAware

```java
public boolean isNamespaceAware()
```

Indicates whether or not the factory is configured to produce
parsers which are namespace aware.

**Returns:** true if the factory is configured to produce parsers which
are namespace aware; false otherwise.

- isValidating

```java
public boolean isValidating()
```

Indicates whether or not the factory is configured to produce
parsers which validate the XML content during parse.

**Returns:** true if the factory is configured to produce parsers
which validate the XML content during parse; false otherwise.

- isIgnoringElementContentWhitespace

```java
public boolean isIgnoringElementContentWhitespace()
```

Indicates whether or not the factory is configured to produce
parsers which ignore ignorable whitespace in element content.

**Returns:** true if the factory is configured to produce parsers
which ignore ignorable whitespace in element content;
false otherwise.

- isExpandEntityReferences

```java
public boolean isExpandEntityReferences()
```

Indicates whether or not the factory is configured to produce
parsers which expand entity reference nodes.

**Returns:** true if the factory is configured to produce parsers
which expand entity reference nodes; false otherwise.

- isIgnoringComments

```java
public boolean isIgnoringComments()
```

Indicates whether or not the factory is configured to produce
parsers which ignores comments.

**Returns:** true if the factory is configured to produce parsers
which ignores comments; false otherwise.

- isCoalescing

```java
public boolean isCoalescing()
```

Indicates whether or not the factory is configured to produce
parsers which converts CDATA nodes to Text nodes and appends it to
the adjacent (if any) Text node.

**Returns:** true if the factory is configured to produce parsers
which converts CDATA nodes to Text nodes and appends it to
the adjacent (if any) Text node; false otherwise.

- setAttribute

```java
public abstract void setAttribute​(
String
name,

Object
value)
throws
IllegalArgumentException
```

Allows the user to set specific attributes on the underlying
implementation.

All implementations that implement JAXP 1.5 or newer are required to
support the

XMLConstants.ACCESS_EXTERNAL_DTD

and

XMLConstants.ACCESS_EXTERNAL_SCHEMA

properties.

- Setting the

XMLConstants.ACCESS_EXTERNAL_DTD

property
restricts the access to external DTDs, external Entity References to the
protocols specified by the property.
If access is denied during parsing due to the restriction of this property,

SAXException

will be thrown by the parse methods defined by

DocumentBuilder

.
- Setting the

XMLConstants.ACCESS_EXTERNAL_SCHEMA

property
restricts the access to external Schema set by the schemaLocation attribute to
the protocols specified by the property. If access is denied during parsing
due to the restriction of this property,

SAXException

will be thrown by the parse methods defined by

DocumentBuilder

.

**Parameters:** name

- The name of the attribute.
**Parameters:** value

- The value of the attribute.
**Throws:** IllegalArgumentException

- thrown if the underlying
implementation doesn't recognize the attribute.

- getAttribute

```java
public abstract
Object
getAttribute​(
String
name)
throws
IllegalArgumentException
```

Allows the user to retrieve specific attributes on the underlying
implementation.

**Parameters:** name

- The name of the attribute.
**Returns:** value The value of the attribute.
**Throws:** IllegalArgumentException

- thrown if the underlying
implementation doesn't recognize the attribute.

- setFeature

```java
public abstract void setFeature​(
String
name,
boolean value)
throws
ParserConfigurationException
```

Set a feature for this

DocumentBuilderFactory

and

DocumentBuilder

s created by this factory.

Feature names are fully qualified

URI

s.
Implementations may define their own features.
A

ParserConfigurationException

is thrown if this

DocumentBuilderFactory

or the

DocumentBuilder

s it creates cannot support the feature.
It is possible for a

DocumentBuilderFactory

to expose a feature value but be unable to change its state.

All implementations are required to support the

XMLConstants.FEATURE_SECURE_PROCESSING

feature.
When the feature is:

- true

: the implementation will limit XML processing to conform to implementation limits.
Examples include entity expansion limits and XML Schema constructs that would consume large amounts of resources.
If XML processing is limited for security reasons, it will be reported via a call to the registered

ErrorHandler.fatalError(SAXParseException exception)

.
See

DocumentBuilder.setErrorHandler(org.xml.sax.ErrorHandler errorHandler)

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
**Throws:** ParserConfigurationException

- if this

DocumentBuilderFactory

or the

DocumentBuilder

s
it creates cannot support this feature.
**Throws:** NullPointerException

- If the

name

parameter is null.
**Since:** 1.5

- getFeature

```java
public abstract boolean getFeature​(
String
name)
throws
ParserConfigurationException
```

Get the state of the named feature.

Feature names are fully qualified

URI

s.
Implementations may define their own features.
An

ParserConfigurationException

is thrown if this

DocumentBuilderFactory

or the

DocumentBuilder

s it creates cannot support the feature.
It is possible for an

DocumentBuilderFactory

to expose a feature value but be unable to change its state.

**Parameters:** name

- Feature name.
**Returns:** State of the named feature.
**Throws:** ParserConfigurationException

- if this

DocumentBuilderFactory

or the

DocumentBuilder

s it creates cannot support this feature.
**Since:** 1.5

- getSchema

```java
public
Schema
getSchema()
```

Gets the

Schema

object specified through
the

setSchema(Schema schema)

method.

**Returns:** the

Schema

object that was last set through
the

setSchema(Schema)

method, or null
if the method was not invoked since a

DocumentBuilderFactory

is created.
**Throws:** UnsupportedOperationException

- When implementation does not
override this method.
**Since:** 1.5

- setSchema

```java
public void setSchema​(
Schema
schema)
```

Set the

Schema

to be used by parsers created
from this factory.

When a

Schema

is non-null, a parser will use a validator
created from it to validate documents before it passes information
down to the application.

When errors are found by the validator, the parser is responsible
to report them to the user-specified

ErrorHandler

(or if the error handler is not set, ignore them or throw them), just
like any other errors found by the parser itself.
In other words, if the user-specified

ErrorHandler

is set, it must receive those errors, and if not, they must be
treated according to the implementation specific
default error handling rules.

A validator may modify the outcome of a parse (for example by
adding default values that were missing in documents), and a parser
is responsible to make sure that the application will receive
modified DOM trees.

Initially, null is set as the

Schema

.

This processing will take effect even if
the

isValidating()

method returns

false

.

It is an error to use
the

http://java.sun.com/xml/jaxp/properties/schemaSource

property and/or the

http://java.sun.com/xml/jaxp/properties/schemaLanguage

property in conjunction with a

Schema

object.
Such configuration will cause a

ParserConfigurationException

exception when the

newDocumentBuilder()

is invoked.

Note for implementors

A parser must be able to work with any

Schema

implementation. However, parsers and schemas are allowed
to use implementation-specific custom mechanisms
as long as they yield the result described in the specification.

**Parameters:** schema

-

Schema

to use or

null

to remove a schema.
**Throws:** UnsupportedOperationException

- When implementation does not
override this method.
**Since:** 1.5

- setXIncludeAware

```java
public void setXIncludeAware​(boolean state)
```

Set state of XInclude processing.

If XInclude markup is found in the document instance, should it be
processed as specified in

XML Inclusions (XInclude) Version 1.0

.

XInclude processing defaults to

false

.

**Parameters:** state

- Set XInclude processing to

true

or

false
**Throws:** UnsupportedOperationException

- When implementation does not
override this method.
**Since:** 1.5

- isXIncludeAware

```java
public boolean isXIncludeAware()
```

Get state of XInclude processing.

**Returns:** current state of XInclude processing
**Throws:** UnsupportedOperationException

- When implementation does not
override this method.
**Since:** 1.5

Constructor Detail

- DocumentBuilderFactory

```java
protected DocumentBuilderFactory()
```

Protected constructor to prevent instantiation.
Use

newInstance()

.

---

#### Constructor Detail

DocumentBuilderFactory

```java
protected DocumentBuilderFactory()
```

Protected constructor to prevent instantiation.
Use

newInstance()

.

---

#### DocumentBuilderFactory

protected DocumentBuilderFactory()

Protected constructor to prevent instantiation.
Use

newInstance()

.

Method Detail

- newDefaultInstance

```java
public static
DocumentBuilderFactory
newDefaultInstance()
```

Creates a new instance of the

DocumentBuilderFactory

builtin
system-default implementation.

**Returns:** A new instance of the

DocumentBuilderFactory

builtin
system-default implementation.
**Since:** 9

- newInstance

```java
public static
DocumentBuilderFactory
newInstance()
```

Obtain a new instance of a

DocumentBuilderFactory

. This static method creates
a new factory instance.
This method uses the following ordered lookup procedure to determine
the

DocumentBuilderFactory

implementation class to
load:

- Use the

javax.xml.parsers.DocumentBuilderFactory

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

DocumentBuilderFactory

it can use the factory to
configure and obtain parser instances.

Tip for Trouble-shooting

Setting the

jaxp.debug

system property will cause
this method to print a lot of debug messages
to

System.err

about what it is doing and where it is looking at.

If you have problems loading

DocumentBuilder

s, try:

```java
java -Djaxp.debug=1 YourProgram ....
```

**Returns:** New instance of a

DocumentBuilderFactory
**Throws:** FactoryConfigurationError

- in case of

service configuration error

or if
the implementation is not available or cannot be instantiated.

- newInstance

```java
public static
DocumentBuilderFactory
newInstance​(
String
factoryClassName,

ClassLoader
classLoader)
```

Obtain a new instance of a

DocumentBuilderFactory

from class name.
This function is useful when there are multiple providers in the classpath.
It gives more control to the application as it can specify which provider
should be loaded.

Once an application has obtained a reference to a

DocumentBuilderFactory

it can use the factory to configure and obtain parser instances.

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

- fully qualified factory class name that provides
implementation of

javax.xml.parsers.DocumentBuilderFactory

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

DocumentBuilderFactory
**Throws:** FactoryConfigurationError

- if

factoryClassName

is

null

, or
the factory class cannot be loaded, instantiated.
**Since:** 1.6
**See Also:** newInstance()

- newDocumentBuilder

```java
public abstract
DocumentBuilder
newDocumentBuilder()
throws
ParserConfigurationException
```

Creates a new instance of a

DocumentBuilder

using the currently configured parameters.

**Returns:** A new instance of a DocumentBuilder.
**Throws:** ParserConfigurationException

- if a DocumentBuilder
cannot be created which satisfies the configuration requested.

- setNamespaceAware

```java
public void setNamespaceAware​(boolean awareness)
```

Specifies that the parser produced by this code will
provide support for XML namespaces. By default the value of this is set
to

false

**Parameters:** awareness

- true if the parser produced will provide support
for XML namespaces; false otherwise.

- setValidating

```java
public void setValidating​(boolean validating)
```

Specifies that the parser produced by this code will
validate documents as they are parsed. By default the value of this
is set to

false

.

Note that "the validation" here means

a validating
parser

as defined in the XML recommendation.
In other words, it essentially just controls the DTD validation.
(except the legacy two properties defined in JAXP 1.2.)

To use modern schema languages such as W3C XML Schema or
RELAX NG instead of DTD, you can configure your parser to be
a non-validating parser by leaving the

setValidating(boolean)

method

false

, then use the

setSchema(Schema)

method to associate a schema to a parser.

**Parameters:** validating

- true if the parser produced will validate documents
as they are parsed; false otherwise.

- setIgnoringElementContentWhitespace

```java
public void setIgnoringElementContentWhitespace​(boolean whitespace)
```

Specifies that the parsers created by this factory must eliminate
whitespace in element content (sometimes known loosely as
'ignorable whitespace') when parsing XML documents (see XML Rec
2.10). Note that only whitespace which is directly contained within
element content that has an element only content model (see XML
Rec 3.2.1) will be eliminated. Due to reliance on the content model
this setting requires the parser to be in validating mode. By default
the value of this is set to

false

.

**Parameters:** whitespace

- true if the parser created must eliminate whitespace
in the element content when parsing XML documents;
false otherwise.

- setExpandEntityReferences

```java
public void setExpandEntityReferences​(boolean expandEntityRef)
```

Specifies that the parser produced by this code will
expand entity reference nodes. By default the value of this is set to

true

**Parameters:** expandEntityRef

- true if the parser produced will expand entity
reference nodes; false otherwise.

- setIgnoringComments

```java
public void setIgnoringComments​(boolean ignoreComments)
```

Specifies that the parser produced by this code will
ignore comments. By default the value of this is set to

false

.

**Parameters:** ignoreComments

-

boolean

value to ignore comments during processing

- setCoalescing

```java
public void setCoalescing​(boolean coalescing)
```

Specifies that the parser produced by this code will
convert CDATA nodes to Text nodes and append it to the
adjacent (if any) text node. By default the value of this is set to

false

**Parameters:** coalescing

- true if the parser produced will convert CDATA nodes
to Text nodes and append it to the adjacent (if any)
text node; false otherwise.

- isNamespaceAware

```java
public boolean isNamespaceAware()
```

Indicates whether or not the factory is configured to produce
parsers which are namespace aware.

**Returns:** true if the factory is configured to produce parsers which
are namespace aware; false otherwise.

- isValidating

```java
public boolean isValidating()
```

Indicates whether or not the factory is configured to produce
parsers which validate the XML content during parse.

**Returns:** true if the factory is configured to produce parsers
which validate the XML content during parse; false otherwise.

- isIgnoringElementContentWhitespace

```java
public boolean isIgnoringElementContentWhitespace()
```

Indicates whether or not the factory is configured to produce
parsers which ignore ignorable whitespace in element content.

**Returns:** true if the factory is configured to produce parsers
which ignore ignorable whitespace in element content;
false otherwise.

- isExpandEntityReferences

```java
public boolean isExpandEntityReferences()
```

Indicates whether or not the factory is configured to produce
parsers which expand entity reference nodes.

**Returns:** true if the factory is configured to produce parsers
which expand entity reference nodes; false otherwise.

- isIgnoringComments

```java
public boolean isIgnoringComments()
```

Indicates whether or not the factory is configured to produce
parsers which ignores comments.

**Returns:** true if the factory is configured to produce parsers
which ignores comments; false otherwise.

- isCoalescing

```java
public boolean isCoalescing()
```

Indicates whether or not the factory is configured to produce
parsers which converts CDATA nodes to Text nodes and appends it to
the adjacent (if any) Text node.

**Returns:** true if the factory is configured to produce parsers
which converts CDATA nodes to Text nodes and appends it to
the adjacent (if any) Text node; false otherwise.

- setAttribute

```java
public abstract void setAttribute​(
String
name,

Object
value)
throws
IllegalArgumentException
```

Allows the user to set specific attributes on the underlying
implementation.

All implementations that implement JAXP 1.5 or newer are required to
support the

XMLConstants.ACCESS_EXTERNAL_DTD

and

XMLConstants.ACCESS_EXTERNAL_SCHEMA

properties.

- Setting the

XMLConstants.ACCESS_EXTERNAL_DTD

property
restricts the access to external DTDs, external Entity References to the
protocols specified by the property.
If access is denied during parsing due to the restriction of this property,

SAXException

will be thrown by the parse methods defined by

DocumentBuilder

.
- Setting the

XMLConstants.ACCESS_EXTERNAL_SCHEMA

property
restricts the access to external Schema set by the schemaLocation attribute to
the protocols specified by the property. If access is denied during parsing
due to the restriction of this property,

SAXException

will be thrown by the parse methods defined by

DocumentBuilder

.

**Parameters:** name

- The name of the attribute.
**Parameters:** value

- The value of the attribute.
**Throws:** IllegalArgumentException

- thrown if the underlying
implementation doesn't recognize the attribute.

- getAttribute

```java
public abstract
Object
getAttribute​(
String
name)
throws
IllegalArgumentException
```

Allows the user to retrieve specific attributes on the underlying
implementation.

**Parameters:** name

- The name of the attribute.
**Returns:** value The value of the attribute.
**Throws:** IllegalArgumentException

- thrown if the underlying
implementation doesn't recognize the attribute.

- setFeature

```java
public abstract void setFeature​(
String
name,
boolean value)
throws
ParserConfigurationException
```

Set a feature for this

DocumentBuilderFactory

and

DocumentBuilder

s created by this factory.

Feature names are fully qualified

URI

s.
Implementations may define their own features.
A

ParserConfigurationException

is thrown if this

DocumentBuilderFactory

or the

DocumentBuilder

s it creates cannot support the feature.
It is possible for a

DocumentBuilderFactory

to expose a feature value but be unable to change its state.

All implementations are required to support the

XMLConstants.FEATURE_SECURE_PROCESSING

feature.
When the feature is:

- true

: the implementation will limit XML processing to conform to implementation limits.
Examples include entity expansion limits and XML Schema constructs that would consume large amounts of resources.
If XML processing is limited for security reasons, it will be reported via a call to the registered

ErrorHandler.fatalError(SAXParseException exception)

.
See

DocumentBuilder.setErrorHandler(org.xml.sax.ErrorHandler errorHandler)

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
**Throws:** ParserConfigurationException

- if this

DocumentBuilderFactory

or the

DocumentBuilder

s
it creates cannot support this feature.
**Throws:** NullPointerException

- If the

name

parameter is null.
**Since:** 1.5

- getFeature

```java
public abstract boolean getFeature​(
String
name)
throws
ParserConfigurationException
```

Get the state of the named feature.

Feature names are fully qualified

URI

s.
Implementations may define their own features.
An

ParserConfigurationException

is thrown if this

DocumentBuilderFactory

or the

DocumentBuilder

s it creates cannot support the feature.
It is possible for an

DocumentBuilderFactory

to expose a feature value but be unable to change its state.

**Parameters:** name

- Feature name.
**Returns:** State of the named feature.
**Throws:** ParserConfigurationException

- if this

DocumentBuilderFactory

or the

DocumentBuilder

s it creates cannot support this feature.
**Since:** 1.5

- getSchema

```java
public
Schema
getSchema()
```

Gets the

Schema

object specified through
the

setSchema(Schema schema)

method.

**Returns:** the

Schema

object that was last set through
the

setSchema(Schema)

method, or null
if the method was not invoked since a

DocumentBuilderFactory

is created.
**Throws:** UnsupportedOperationException

- When implementation does not
override this method.
**Since:** 1.5

- setSchema

```java
public void setSchema​(
Schema
schema)
```

Set the

Schema

to be used by parsers created
from this factory.

When a

Schema

is non-null, a parser will use a validator
created from it to validate documents before it passes information
down to the application.

When errors are found by the validator, the parser is responsible
to report them to the user-specified

ErrorHandler

(or if the error handler is not set, ignore them or throw them), just
like any other errors found by the parser itself.
In other words, if the user-specified

ErrorHandler

is set, it must receive those errors, and if not, they must be
treated according to the implementation specific
default error handling rules.

A validator may modify the outcome of a parse (for example by
adding default values that were missing in documents), and a parser
is responsible to make sure that the application will receive
modified DOM trees.

Initially, null is set as the

Schema

.

This processing will take effect even if
the

isValidating()

method returns

false

.

It is an error to use
the

http://java.sun.com/xml/jaxp/properties/schemaSource

property and/or the

http://java.sun.com/xml/jaxp/properties/schemaLanguage

property in conjunction with a

Schema

object.
Such configuration will cause a

ParserConfigurationException

exception when the

newDocumentBuilder()

is invoked.

Note for implementors

A parser must be able to work with any

Schema

implementation. However, parsers and schemas are allowed
to use implementation-specific custom mechanisms
as long as they yield the result described in the specification.

**Parameters:** schema

-

Schema

to use or

null

to remove a schema.
**Throws:** UnsupportedOperationException

- When implementation does not
override this method.
**Since:** 1.5

- setXIncludeAware

```java
public void setXIncludeAware​(boolean state)
```

Set state of XInclude processing.

If XInclude markup is found in the document instance, should it be
processed as specified in

XML Inclusions (XInclude) Version 1.0

.

XInclude processing defaults to

false

.

**Parameters:** state

- Set XInclude processing to

true

or

false
**Throws:** UnsupportedOperationException

- When implementation does not
override this method.
**Since:** 1.5

- isXIncludeAware

```java
public boolean isXIncludeAware()
```

Get state of XInclude processing.

**Returns:** current state of XInclude processing
**Throws:** UnsupportedOperationException

- When implementation does not
override this method.
**Since:** 1.5

---

#### Method Detail

newDefaultInstance

```java
public static
DocumentBuilderFactory
newDefaultInstance()
```

Creates a new instance of the

DocumentBuilderFactory

builtin
system-default implementation.

**Returns:** A new instance of the

DocumentBuilderFactory

builtin
system-default implementation.
**Since:** 9

---

#### newDefaultInstance

public static

DocumentBuilderFactory

newDefaultInstance()

Creates a new instance of the

DocumentBuilderFactory

builtin
system-default implementation.

newInstance

```java
public static
DocumentBuilderFactory
newInstance()
```

Obtain a new instance of a

DocumentBuilderFactory

. This static method creates
a new factory instance.
This method uses the following ordered lookup procedure to determine
the

DocumentBuilderFactory

implementation class to
load:

- Use the

javax.xml.parsers.DocumentBuilderFactory

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

DocumentBuilderFactory

it can use the factory to
configure and obtain parser instances.

Tip for Trouble-shooting

Setting the

jaxp.debug

system property will cause
this method to print a lot of debug messages
to

System.err

about what it is doing and where it is looking at.

If you have problems loading

DocumentBuilder

s, try:

```java
java -Djaxp.debug=1 YourProgram ....
```

**Returns:** New instance of a

DocumentBuilderFactory
**Throws:** FactoryConfigurationError

- in case of

service configuration error

or if
the implementation is not available or cannot be instantiated.

---

#### newInstance

public static

DocumentBuilderFactory

newInstance()

Obtain a new instance of a

DocumentBuilderFactory

. This static method creates
a new factory instance.
This method uses the following ordered lookup procedure to determine
the

DocumentBuilderFactory

implementation class to
load:

- Use the

javax.xml.parsers.DocumentBuilderFactory

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

DocumentBuilderFactory

it can use the factory to
configure and obtain parser instances.

Tip for Trouble-shooting

Setting the

jaxp.debug

system property will cause
this method to print a lot of debug messages
to

System.err

about what it is doing and where it is looking at.

If you have problems loading

DocumentBuilder

s, try:

```java
java -Djaxp.debug=1 YourProgram ....
```

Use the

javax.xml.parsers.DocumentBuilderFactory

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

DocumentBuilderFactory

it can use the factory to
configure and obtain parser instances.

Tip for Trouble-shooting

Setting the

jaxp.debug

system property will cause
this method to print a lot of debug messages
to

System.err

about what it is doing and where it is looking at.

If you have problems loading

DocumentBuilder

s, try:

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

If you have problems loading

DocumentBuilder

s, try:

```java
java -Djaxp.debug=1 YourProgram ....
```

If you have problems loading

DocumentBuilder

s, try:

```java
java -Djaxp.debug=1 YourProgram ....
```

java -Djaxp.debug=1 YourProgram ....

newInstance

```java
public static
DocumentBuilderFactory
newInstance​(
String
factoryClassName,

ClassLoader
classLoader)
```

Obtain a new instance of a

DocumentBuilderFactory

from class name.
This function is useful when there are multiple providers in the classpath.
It gives more control to the application as it can specify which provider
should be loaded.

Once an application has obtained a reference to a

DocumentBuilderFactory

it can use the factory to configure and obtain parser instances.

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

- fully qualified factory class name that provides
implementation of

javax.xml.parsers.DocumentBuilderFactory

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

DocumentBuilderFactory
**Throws:** FactoryConfigurationError

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

DocumentBuilderFactory

newInstance​(

String

factoryClassName,

ClassLoader

classLoader)

Obtain a new instance of a

DocumentBuilderFactory

from class name.
This function is useful when there are multiple providers in the classpath.
It gives more control to the application as it can specify which provider
should be loaded.

Once an application has obtained a reference to a

DocumentBuilderFactory

it can use the factory to configure and obtain parser instances.

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

DocumentBuilderFactory

it can use the factory to configure and obtain parser instances.

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

newDocumentBuilder

```java
public abstract
DocumentBuilder
newDocumentBuilder()
throws
ParserConfigurationException
```

Creates a new instance of a

DocumentBuilder

using the currently configured parameters.

**Returns:** A new instance of a DocumentBuilder.
**Throws:** ParserConfigurationException

- if a DocumentBuilder
cannot be created which satisfies the configuration requested.

---

#### newDocumentBuilder

public abstract

DocumentBuilder

newDocumentBuilder()
throws

ParserConfigurationException

Creates a new instance of a

DocumentBuilder

using the currently configured parameters.

setNamespaceAware

```java
public void setNamespaceAware​(boolean awareness)
```

Specifies that the parser produced by this code will
provide support for XML namespaces. By default the value of this is set
to

false

**Parameters:** awareness

- true if the parser produced will provide support
for XML namespaces; false otherwise.

---

#### setNamespaceAware

public void setNamespaceAware​(boolean awareness)

Specifies that the parser produced by this code will
provide support for XML namespaces. By default the value of this is set
to

false

setValidating

```java
public void setValidating​(boolean validating)
```

Specifies that the parser produced by this code will
validate documents as they are parsed. By default the value of this
is set to

false

.

Note that "the validation" here means

a validating
parser

as defined in the XML recommendation.
In other words, it essentially just controls the DTD validation.
(except the legacy two properties defined in JAXP 1.2.)

To use modern schema languages such as W3C XML Schema or
RELAX NG instead of DTD, you can configure your parser to be
a non-validating parser by leaving the

setValidating(boolean)

method

false

, then use the

setSchema(Schema)

method to associate a schema to a parser.

**Parameters:** validating

- true if the parser produced will validate documents
as they are parsed; false otherwise.

---

#### setValidating

public void setValidating​(boolean validating)

Specifies that the parser produced by this code will
validate documents as they are parsed. By default the value of this
is set to

false

.

Note that "the validation" here means

a validating
parser

as defined in the XML recommendation.
In other words, it essentially just controls the DTD validation.
(except the legacy two properties defined in JAXP 1.2.)

To use modern schema languages such as W3C XML Schema or
RELAX NG instead of DTD, you can configure your parser to be
a non-validating parser by leaving the

setValidating(boolean)

method

false

, then use the

setSchema(Schema)

method to associate a schema to a parser.

Note that "the validation" here means

a validating
parser

as defined in the XML recommendation.
In other words, it essentially just controls the DTD validation.
(except the legacy two properties defined in JAXP 1.2.)

To use modern schema languages such as W3C XML Schema or
RELAX NG instead of DTD, you can configure your parser to be
a non-validating parser by leaving the

setValidating(boolean)

method

false

, then use the

setSchema(Schema)

method to associate a schema to a parser.

To use modern schema languages such as W3C XML Schema or
RELAX NG instead of DTD, you can configure your parser to be
a non-validating parser by leaving the

setValidating(boolean)

method

false

, then use the

setSchema(Schema)

method to associate a schema to a parser.

setIgnoringElementContentWhitespace

```java
public void setIgnoringElementContentWhitespace​(boolean whitespace)
```

Specifies that the parsers created by this factory must eliminate
whitespace in element content (sometimes known loosely as
'ignorable whitespace') when parsing XML documents (see XML Rec
2.10). Note that only whitespace which is directly contained within
element content that has an element only content model (see XML
Rec 3.2.1) will be eliminated. Due to reliance on the content model
this setting requires the parser to be in validating mode. By default
the value of this is set to

false

.

**Parameters:** whitespace

- true if the parser created must eliminate whitespace
in the element content when parsing XML documents;
false otherwise.

---

#### setIgnoringElementContentWhitespace

public void setIgnoringElementContentWhitespace​(boolean whitespace)

Specifies that the parsers created by this factory must eliminate
whitespace in element content (sometimes known loosely as
'ignorable whitespace') when parsing XML documents (see XML Rec
2.10). Note that only whitespace which is directly contained within
element content that has an element only content model (see XML
Rec 3.2.1) will be eliminated. Due to reliance on the content model
this setting requires the parser to be in validating mode. By default
the value of this is set to

false

.

setExpandEntityReferences

```java
public void setExpandEntityReferences​(boolean expandEntityRef)
```

Specifies that the parser produced by this code will
expand entity reference nodes. By default the value of this is set to

true

**Parameters:** expandEntityRef

- true if the parser produced will expand entity
reference nodes; false otherwise.

---

#### setExpandEntityReferences

public void setExpandEntityReferences​(boolean expandEntityRef)

Specifies that the parser produced by this code will
expand entity reference nodes. By default the value of this is set to

true

setIgnoringComments

```java
public void setIgnoringComments​(boolean ignoreComments)
```

Specifies that the parser produced by this code will
ignore comments. By default the value of this is set to

false

.

**Parameters:** ignoreComments

-

boolean

value to ignore comments during processing

---

#### setIgnoringComments

public void setIgnoringComments​(boolean ignoreComments)

Specifies that the parser produced by this code will
ignore comments. By default the value of this is set to

false

.

setCoalescing

```java
public void setCoalescing​(boolean coalescing)
```

Specifies that the parser produced by this code will
convert CDATA nodes to Text nodes and append it to the
adjacent (if any) text node. By default the value of this is set to

false

**Parameters:** coalescing

- true if the parser produced will convert CDATA nodes
to Text nodes and append it to the adjacent (if any)
text node; false otherwise.

---

#### setCoalescing

public void setCoalescing​(boolean coalescing)

Specifies that the parser produced by this code will
convert CDATA nodes to Text nodes and append it to the
adjacent (if any) text node. By default the value of this is set to

false

isNamespaceAware

```java
public boolean isNamespaceAware()
```

Indicates whether or not the factory is configured to produce
parsers which are namespace aware.

**Returns:** true if the factory is configured to produce parsers which
are namespace aware; false otherwise.

---

#### isNamespaceAware

public boolean isNamespaceAware()

Indicates whether or not the factory is configured to produce
parsers which are namespace aware.

isValidating

```java
public boolean isValidating()
```

Indicates whether or not the factory is configured to produce
parsers which validate the XML content during parse.

**Returns:** true if the factory is configured to produce parsers
which validate the XML content during parse; false otherwise.

---

#### isValidating

public boolean isValidating()

Indicates whether or not the factory is configured to produce
parsers which validate the XML content during parse.

isIgnoringElementContentWhitespace

```java
public boolean isIgnoringElementContentWhitespace()
```

Indicates whether or not the factory is configured to produce
parsers which ignore ignorable whitespace in element content.

**Returns:** true if the factory is configured to produce parsers
which ignore ignorable whitespace in element content;
false otherwise.

---

#### isIgnoringElementContentWhitespace

public boolean isIgnoringElementContentWhitespace()

Indicates whether or not the factory is configured to produce
parsers which ignore ignorable whitespace in element content.

isExpandEntityReferences

```java
public boolean isExpandEntityReferences()
```

Indicates whether or not the factory is configured to produce
parsers which expand entity reference nodes.

**Returns:** true if the factory is configured to produce parsers
which expand entity reference nodes; false otherwise.

---

#### isExpandEntityReferences

public boolean isExpandEntityReferences()

Indicates whether or not the factory is configured to produce
parsers which expand entity reference nodes.

isIgnoringComments

```java
public boolean isIgnoringComments()
```

Indicates whether or not the factory is configured to produce
parsers which ignores comments.

**Returns:** true if the factory is configured to produce parsers
which ignores comments; false otherwise.

---

#### isIgnoringComments

public boolean isIgnoringComments()

Indicates whether or not the factory is configured to produce
parsers which ignores comments.

isCoalescing

```java
public boolean isCoalescing()
```

Indicates whether or not the factory is configured to produce
parsers which converts CDATA nodes to Text nodes and appends it to
the adjacent (if any) Text node.

**Returns:** true if the factory is configured to produce parsers
which converts CDATA nodes to Text nodes and appends it to
the adjacent (if any) Text node; false otherwise.

---

#### isCoalescing

public boolean isCoalescing()

Indicates whether or not the factory is configured to produce
parsers which converts CDATA nodes to Text nodes and appends it to
the adjacent (if any) Text node.

setAttribute

```java
public abstract void setAttribute​(
String
name,

Object
value)
throws
IllegalArgumentException
```

Allows the user to set specific attributes on the underlying
implementation.

All implementations that implement JAXP 1.5 or newer are required to
support the

XMLConstants.ACCESS_EXTERNAL_DTD

and

XMLConstants.ACCESS_EXTERNAL_SCHEMA

properties.

- Setting the

XMLConstants.ACCESS_EXTERNAL_DTD

property
restricts the access to external DTDs, external Entity References to the
protocols specified by the property.
If access is denied during parsing due to the restriction of this property,

SAXException

will be thrown by the parse methods defined by

DocumentBuilder

.
- Setting the

XMLConstants.ACCESS_EXTERNAL_SCHEMA

property
restricts the access to external Schema set by the schemaLocation attribute to
the protocols specified by the property. If access is denied during parsing
due to the restriction of this property,

SAXException

will be thrown by the parse methods defined by

DocumentBuilder

.

**Parameters:** name

- The name of the attribute.
**Parameters:** value

- The value of the attribute.
**Throws:** IllegalArgumentException

- thrown if the underlying
implementation doesn't recognize the attribute.

---

#### setAttribute

public abstract void setAttribute​(

String

name,

Object

value)
throws

IllegalArgumentException

Allows the user to set specific attributes on the underlying
implementation.

All implementations that implement JAXP 1.5 or newer are required to
support the

XMLConstants.ACCESS_EXTERNAL_DTD

and

XMLConstants.ACCESS_EXTERNAL_SCHEMA

properties.

- Setting the

XMLConstants.ACCESS_EXTERNAL_DTD

property
restricts the access to external DTDs, external Entity References to the
protocols specified by the property.
If access is denied during parsing due to the restriction of this property,

SAXException

will be thrown by the parse methods defined by

DocumentBuilder

.
- Setting the

XMLConstants.ACCESS_EXTERNAL_SCHEMA

property
restricts the access to external Schema set by the schemaLocation attribute to
the protocols specified by the property. If access is denied during parsing
due to the restriction of this property,

SAXException

will be thrown by the parse methods defined by

DocumentBuilder

.

All implementations that implement JAXP 1.5 or newer are required to
support the

XMLConstants.ACCESS_EXTERNAL_DTD

and

XMLConstants.ACCESS_EXTERNAL_SCHEMA

properties.

- Setting the

XMLConstants.ACCESS_EXTERNAL_DTD

property
restricts the access to external DTDs, external Entity References to the
protocols specified by the property.
If access is denied during parsing due to the restriction of this property,

SAXException

will be thrown by the parse methods defined by

DocumentBuilder

.
- Setting the

XMLConstants.ACCESS_EXTERNAL_SCHEMA

property
restricts the access to external Schema set by the schemaLocation attribute to
the protocols specified by the property. If access is denied during parsing
due to the restriction of this property,

SAXException

will be thrown by the parse methods defined by

DocumentBuilder

.

Setting the

XMLConstants.ACCESS_EXTERNAL_DTD

property
restricts the access to external DTDs, external Entity References to the
protocols specified by the property.
If access is denied during parsing due to the restriction of this property,

SAXException

will be thrown by the parse methods defined by

DocumentBuilder

.

Setting the

XMLConstants.ACCESS_EXTERNAL_SCHEMA

property
restricts the access to external Schema set by the schemaLocation attribute to
the protocols specified by the property. If access is denied during parsing
due to the restriction of this property,

SAXException

will be thrown by the parse methods defined by

DocumentBuilder

.

getAttribute

```java
public abstract
Object
getAttribute​(
String
name)
throws
IllegalArgumentException
```

Allows the user to retrieve specific attributes on the underlying
implementation.

**Parameters:** name

- The name of the attribute.
**Returns:** value The value of the attribute.
**Throws:** IllegalArgumentException

- thrown if the underlying
implementation doesn't recognize the attribute.

---

#### getAttribute

public abstract

Object

getAttribute​(

String

name)
throws

IllegalArgumentException

Allows the user to retrieve specific attributes on the underlying
implementation.

setFeature

```java
public abstract void setFeature​(
String
name,
boolean value)
throws
ParserConfigurationException
```

Set a feature for this

DocumentBuilderFactory

and

DocumentBuilder

s created by this factory.

Feature names are fully qualified

URI

s.
Implementations may define their own features.
A

ParserConfigurationException

is thrown if this

DocumentBuilderFactory

or the

DocumentBuilder

s it creates cannot support the feature.
It is possible for a

DocumentBuilderFactory

to expose a feature value but be unable to change its state.

All implementations are required to support the

XMLConstants.FEATURE_SECURE_PROCESSING

feature.
When the feature is:

- true

: the implementation will limit XML processing to conform to implementation limits.
Examples include entity expansion limits and XML Schema constructs that would consume large amounts of resources.
If XML processing is limited for security reasons, it will be reported via a call to the registered

ErrorHandler.fatalError(SAXParseException exception)

.
See

DocumentBuilder.setErrorHandler(org.xml.sax.ErrorHandler errorHandler)

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
**Throws:** ParserConfigurationException

- if this

DocumentBuilderFactory

or the

DocumentBuilder

s
it creates cannot support this feature.
**Throws:** NullPointerException

- If the

name

parameter is null.
**Since:** 1.5

---

#### setFeature

public abstract void setFeature​(

String

name,
boolean value)
throws

ParserConfigurationException

Set a feature for this

DocumentBuilderFactory

and

DocumentBuilder

s created by this factory.

Feature names are fully qualified

URI

s.
Implementations may define their own features.
A

ParserConfigurationException

is thrown if this

DocumentBuilderFactory

or the

DocumentBuilder

s it creates cannot support the feature.
It is possible for a

DocumentBuilderFactory

to expose a feature value but be unable to change its state.

All implementations are required to support the

XMLConstants.FEATURE_SECURE_PROCESSING

feature.
When the feature is:

- true

: the implementation will limit XML processing to conform to implementation limits.
Examples include entity expansion limits and XML Schema constructs that would consume large amounts of resources.
If XML processing is limited for security reasons, it will be reported via a call to the registered

ErrorHandler.fatalError(SAXParseException exception)

.
See

DocumentBuilder.setErrorHandler(org.xml.sax.ErrorHandler errorHandler)

.
- false

: the implementation will processing XML according to the XML specifications without
regard to possible implementation limits.

Feature names are fully qualified

URI

s.
Implementations may define their own features.
A

ParserConfigurationException

is thrown if this

DocumentBuilderFactory

or the

DocumentBuilder

s it creates cannot support the feature.
It is possible for a

DocumentBuilderFactory

to expose a feature value but be unable to change its state.

All implementations are required to support the

XMLConstants.FEATURE_SECURE_PROCESSING

feature.
When the feature is:

- true

: the implementation will limit XML processing to conform to implementation limits.
Examples include entity expansion limits and XML Schema constructs that would consume large amounts of resources.
If XML processing is limited for security reasons, it will be reported via a call to the registered

ErrorHandler.fatalError(SAXParseException exception)

.
See

DocumentBuilder.setErrorHandler(org.xml.sax.ErrorHandler errorHandler)

.
- false

: the implementation will processing XML according to the XML specifications without
regard to possible implementation limits.

All implementations are required to support the

XMLConstants.FEATURE_SECURE_PROCESSING

feature.
When the feature is:

- true

: the implementation will limit XML processing to conform to implementation limits.
Examples include entity expansion limits and XML Schema constructs that would consume large amounts of resources.
If XML processing is limited for security reasons, it will be reported via a call to the registered

ErrorHandler.fatalError(SAXParseException exception)

.
See

DocumentBuilder.setErrorHandler(org.xml.sax.ErrorHandler errorHandler)

.
- false

: the implementation will processing XML according to the XML specifications without
regard to possible implementation limits.

true

: the implementation will limit XML processing to conform to implementation limits.
Examples include entity expansion limits and XML Schema constructs that would consume large amounts of resources.
If XML processing is limited for security reasons, it will be reported via a call to the registered

ErrorHandler.fatalError(SAXParseException exception)

.
See

DocumentBuilder.setErrorHandler(org.xml.sax.ErrorHandler errorHandler)

.

false

: the implementation will processing XML according to the XML specifications without
regard to possible implementation limits.

getFeature

```java
public abstract boolean getFeature​(
String
name)
throws
ParserConfigurationException
```

Get the state of the named feature.

Feature names are fully qualified

URI

s.
Implementations may define their own features.
An

ParserConfigurationException

is thrown if this

DocumentBuilderFactory

or the

DocumentBuilder

s it creates cannot support the feature.
It is possible for an

DocumentBuilderFactory

to expose a feature value but be unable to change its state.

**Parameters:** name

- Feature name.
**Returns:** State of the named feature.
**Throws:** ParserConfigurationException

- if this

DocumentBuilderFactory

or the

DocumentBuilder

s it creates cannot support this feature.
**Since:** 1.5

---

#### getFeature

public abstract boolean getFeature​(

String

name)
throws

ParserConfigurationException

Get the state of the named feature.

Feature names are fully qualified

URI

s.
Implementations may define their own features.
An

ParserConfigurationException

is thrown if this

DocumentBuilderFactory

or the

DocumentBuilder

s it creates cannot support the feature.
It is possible for an

DocumentBuilderFactory

to expose a feature value but be unable to change its state.

Feature names are fully qualified

URI

s.
Implementations may define their own features.
An

ParserConfigurationException

is thrown if this

DocumentBuilderFactory

or the

DocumentBuilder

s it creates cannot support the feature.
It is possible for an

DocumentBuilderFactory

to expose a feature value but be unable to change its state.

getSchema

```java
public
Schema
getSchema()
```

Gets the

Schema

object specified through
the

setSchema(Schema schema)

method.

**Returns:** the

Schema

object that was last set through
the

setSchema(Schema)

method, or null
if the method was not invoked since a

DocumentBuilderFactory

is created.
**Throws:** UnsupportedOperationException

- When implementation does not
override this method.
**Since:** 1.5

---

#### getSchema

public

Schema

getSchema()

Gets the

Schema

object specified through
the

setSchema(Schema schema)

method.

setSchema

```java
public void setSchema​(
Schema
schema)
```

Set the

Schema

to be used by parsers created
from this factory.

When a

Schema

is non-null, a parser will use a validator
created from it to validate documents before it passes information
down to the application.

When errors are found by the validator, the parser is responsible
to report them to the user-specified

ErrorHandler

(or if the error handler is not set, ignore them or throw them), just
like any other errors found by the parser itself.
In other words, if the user-specified

ErrorHandler

is set, it must receive those errors, and if not, they must be
treated according to the implementation specific
default error handling rules.

A validator may modify the outcome of a parse (for example by
adding default values that were missing in documents), and a parser
is responsible to make sure that the application will receive
modified DOM trees.

Initially, null is set as the

Schema

.

This processing will take effect even if
the

isValidating()

method returns

false

.

It is an error to use
the

http://java.sun.com/xml/jaxp/properties/schemaSource

property and/or the

http://java.sun.com/xml/jaxp/properties/schemaLanguage

property in conjunction with a

Schema

object.
Such configuration will cause a

ParserConfigurationException

exception when the

newDocumentBuilder()

is invoked.

Note for implementors

A parser must be able to work with any

Schema

implementation. However, parsers and schemas are allowed
to use implementation-specific custom mechanisms
as long as they yield the result described in the specification.

**Parameters:** schema

-

Schema

to use or

null

to remove a schema.
**Throws:** UnsupportedOperationException

- When implementation does not
override this method.
**Since:** 1.5

---

#### setSchema

public void setSchema​(

Schema

schema)

Set the

Schema

to be used by parsers created
from this factory.

When a

Schema

is non-null, a parser will use a validator
created from it to validate documents before it passes information
down to the application.

When errors are found by the validator, the parser is responsible
to report them to the user-specified

ErrorHandler

(or if the error handler is not set, ignore them or throw them), just
like any other errors found by the parser itself.
In other words, if the user-specified

ErrorHandler

is set, it must receive those errors, and if not, they must be
treated according to the implementation specific
default error handling rules.

A validator may modify the outcome of a parse (for example by
adding default values that were missing in documents), and a parser
is responsible to make sure that the application will receive
modified DOM trees.

Initially, null is set as the

Schema

.

This processing will take effect even if
the

isValidating()

method returns

false

.

It is an error to use
the

http://java.sun.com/xml/jaxp/properties/schemaSource

property and/or the

http://java.sun.com/xml/jaxp/properties/schemaLanguage

property in conjunction with a

Schema

object.
Such configuration will cause a

ParserConfigurationException

exception when the

newDocumentBuilder()

is invoked.

Note for implementors

A parser must be able to work with any

Schema

implementation. However, parsers and schemas are allowed
to use implementation-specific custom mechanisms
as long as they yield the result described in the specification.

When a

Schema

is non-null, a parser will use a validator
created from it to validate documents before it passes information
down to the application.

When errors are found by the validator, the parser is responsible
to report them to the user-specified

ErrorHandler

(or if the error handler is not set, ignore them or throw them), just
like any other errors found by the parser itself.
In other words, if the user-specified

ErrorHandler

is set, it must receive those errors, and if not, they must be
treated according to the implementation specific
default error handling rules.

A validator may modify the outcome of a parse (for example by
adding default values that were missing in documents), and a parser
is responsible to make sure that the application will receive
modified DOM trees.

Initially, null is set as the

Schema

.

This processing will take effect even if
the

isValidating()

method returns

false

.

It is an error to use
the

http://java.sun.com/xml/jaxp/properties/schemaSource

property and/or the

http://java.sun.com/xml/jaxp/properties/schemaLanguage

property in conjunction with a

Schema

object.
Such configuration will cause a

ParserConfigurationException

exception when the

newDocumentBuilder()

is invoked.

Note for implementors

A parser must be able to work with any

Schema

implementation. However, parsers and schemas are allowed
to use implementation-specific custom mechanisms
as long as they yield the result described in the specification.

When errors are found by the validator, the parser is responsible
to report them to the user-specified

ErrorHandler

(or if the error handler is not set, ignore them or throw them), just
like any other errors found by the parser itself.
In other words, if the user-specified

ErrorHandler

is set, it must receive those errors, and if not, they must be
treated according to the implementation specific
default error handling rules.

A validator may modify the outcome of a parse (for example by
adding default values that were missing in documents), and a parser
is responsible to make sure that the application will receive
modified DOM trees.

Initially, null is set as the

Schema

.

This processing will take effect even if
the

isValidating()

method returns

false

.

It is an error to use
the

http://java.sun.com/xml/jaxp/properties/schemaSource

property and/or the

http://java.sun.com/xml/jaxp/properties/schemaLanguage

property in conjunction with a

Schema

object.
Such configuration will cause a

ParserConfigurationException

exception when the

newDocumentBuilder()

is invoked.

Note for implementors

A parser must be able to work with any

Schema

implementation. However, parsers and schemas are allowed
to use implementation-specific custom mechanisms
as long as they yield the result described in the specification.

A validator may modify the outcome of a parse (for example by
adding default values that were missing in documents), and a parser
is responsible to make sure that the application will receive
modified DOM trees.

Initially, null is set as the

Schema

.

This processing will take effect even if
the

isValidating()

method returns

false

.

It is an error to use
the

http://java.sun.com/xml/jaxp/properties/schemaSource

property and/or the

http://java.sun.com/xml/jaxp/properties/schemaLanguage

property in conjunction with a

Schema

object.
Such configuration will cause a

ParserConfigurationException

exception when the

newDocumentBuilder()

is invoked.

Note for implementors

A parser must be able to work with any

Schema

implementation. However, parsers and schemas are allowed
to use implementation-specific custom mechanisms
as long as they yield the result described in the specification.

Initially, null is set as the

Schema

.

This processing will take effect even if
the

isValidating()

method returns

false

.

It is an error to use
the

http://java.sun.com/xml/jaxp/properties/schemaSource

property and/or the

http://java.sun.com/xml/jaxp/properties/schemaLanguage

property in conjunction with a

Schema

object.
Such configuration will cause a

ParserConfigurationException

exception when the

newDocumentBuilder()

is invoked.

Note for implementors

A parser must be able to work with any

Schema

implementation. However, parsers and schemas are allowed
to use implementation-specific custom mechanisms
as long as they yield the result described in the specification.

This processing will take effect even if
the

isValidating()

method returns

false

.

It is an error to use
the

http://java.sun.com/xml/jaxp/properties/schemaSource

property and/or the

http://java.sun.com/xml/jaxp/properties/schemaLanguage

property in conjunction with a

Schema

object.
Such configuration will cause a

ParserConfigurationException

exception when the

newDocumentBuilder()

is invoked.

Note for implementors

A parser must be able to work with any

Schema

implementation. However, parsers and schemas are allowed
to use implementation-specific custom mechanisms
as long as they yield the result described in the specification.

It is an error to use
the

http://java.sun.com/xml/jaxp/properties/schemaSource

property and/or the

http://java.sun.com/xml/jaxp/properties/schemaLanguage

property in conjunction with a

Schema

object.
Such configuration will cause a

ParserConfigurationException

exception when the

newDocumentBuilder()

is invoked.

Note for implementors

A parser must be able to work with any

Schema

implementation. However, parsers and schemas are allowed
to use implementation-specific custom mechanisms
as long as they yield the result described in the specification.

---

#### Note for implementors

A parser must be able to work with any

Schema

implementation. However, parsers and schemas are allowed
to use implementation-specific custom mechanisms
as long as they yield the result described in the specification.

setXIncludeAware

```java
public void setXIncludeAware​(boolean state)
```

Set state of XInclude processing.

If XInclude markup is found in the document instance, should it be
processed as specified in

XML Inclusions (XInclude) Version 1.0

.

XInclude processing defaults to

false

.

**Parameters:** state

- Set XInclude processing to

true

or

false
**Throws:** UnsupportedOperationException

- When implementation does not
override this method.
**Since:** 1.5

---

#### setXIncludeAware

public void setXIncludeAware​(boolean state)

Set state of XInclude processing.

If XInclude markup is found in the document instance, should it be
processed as specified in

XML Inclusions (XInclude) Version 1.0

.

XInclude processing defaults to

false

.

If XInclude markup is found in the document instance, should it be
processed as specified in

XML Inclusions (XInclude) Version 1.0

.

XInclude processing defaults to

false

.

XInclude processing defaults to

false

.

isXIncludeAware

```java
public boolean isXIncludeAware()
```

Get state of XInclude processing.

**Returns:** current state of XInclude processing
**Throws:** UnsupportedOperationException

- When implementation does not
override this method.
**Since:** 1.5

---

#### isXIncludeAware

public boolean isXIncludeAware()

Get state of XInclude processing.

---

