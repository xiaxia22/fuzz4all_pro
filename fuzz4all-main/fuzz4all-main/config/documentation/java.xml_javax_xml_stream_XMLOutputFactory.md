# Class XMLOutputFactory

**Source:** `java.xml\javax\xml\stream\XMLOutputFactory.html`

### Class Description

```java
public abstract class
XMLOutputFactory

extends
Object
```

Defines an abstract implementation of a factory for
getting XMLEventWriters and XMLStreamWriters.

The following table defines the standard properties of this specification.
Each property varies in the level of support required by each implementation.
The level of support required is described in the 'Required' column.

Configuration Parameters

Property Name

Behavior

Return type

Default Value

Required

javax.xml.stream.isRepairingNamespaces

defaults prefixes
on the output side

Boolean

False

Yes

The following paragraphs describe the namespace and prefix repair algorithm:

The property can be set with the following code line:

setProperty("javax.xml.stream.isRepairingNamespaces", new Boolean(true|false));

This property specifies that the writer default namespace prefix declarations.
The default value is false.

If a writer isRepairingNamespaces it will create a namespace declaration
on the current StartElement for
any attribute that does not
currently have a namespace declaration in scope. If the StartElement
has a uri but no prefix specified a prefix will be assigned, if the prefix
has not been declared in a parent of the current StartElement it will be declared
on the current StartElement. If the defaultNamespace is bound and in scope
and the default namespace matches the URI of the attribute or StartElement
QName no prefix will be assigned.

If an element or attribute name has a prefix, but is not
bound to any namespace URI, then the prefix will be removed
during serialization.

If element and/or attribute names in the same start or
empty-element tag are bound to different namespace URIs and
are using the same prefix then the element or the first
occurring attribute retains the original prefix and the
following attributes have their prefixes replaced with a
new prefix that is bound to the namespace URIs of those
attributes.

If an element or attribute name uses a prefix that is
bound to a different URI than that inherited from the
namespace context of the parent of that element and there
is no namespace declaration in the context of the current
element then such a namespace declaration is added.

If an element or attribute name is bound to a prefix and
there is a namespace declaration that binds that prefix
to a different URI then that namespace declaration is
either removed if the correct mapping is inherited from
the parent context of that element, or changed to the
namespace URI of the element or attribute using that prefix.

**Since:** 1.6
**See Also:** XMLInputFactory

,

XMLEventWriter

,

XMLStreamWriter

---

### Field Details

#### public static final
String
IS_REPAIRING_NAMESPACES

Property used to set prefix defaulting on the output side

**See Also:**
- Constant Field Values

---

### Constructor Details

#### protected XMLOutputFactory()

*No description found.*

---

### Method Details

#### public static
XMLOutputFactory
newDefaultFactory()

Creates a new instance of the

XMLOutputFactory

builtin
system-default implementation.

**Returns:**
- A new instance of the

XMLOutputFactory

builtin
system-default implementation.

**Since:**
- 9

---

#### public static
XMLOutputFactory
newInstance()
throws
FactoryConfigurationError

Creates a new instance of the factory in exactly the same manner as the

newFactory()

method.

**Throws:**
- FactoryConfigurationError

- if an instance of this factory cannot be loaded

---

#### public static
XMLOutputFactory
newFactory()
throws
FactoryConfigurationError

Create a new instance of the factory.

This static method creates a new factory instance. This method uses the
following ordered lookup procedure to determine the XMLOutputFactory
implementation class to load:

- Use the javax.xml.stream.XMLOutputFactory system property.
- Use the configuration file "stax.properties". The file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. It contains the fully qualified
name of the implementation class with the key being the system property
defined above.

The stax.properties file is read only once by the implementation
and its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any property in stax.properties after it has been read for the first time.

Use the jaxp configuration file "jaxp.properties". The file is in the same
format as stax.properties and will only be read if stax.properties does
not exist.
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

Once an application has obtained a reference to a XMLOutputFactory it
can use the factory to configure and obtain stream instances.

**Throws:**
- FactoryConfigurationError

- in case of

service configuration error

or if
the implementation is not available or cannot be instantiated.

---

#### @Deprecated
(
since
="1.7")
public static
XMLInputFactory
newInstance​(
String
factoryId,

ClassLoader
classLoader)
throws
FactoryConfigurationError

Create a new instance of the factory.

**Parameters:**
- factoryId

- Name of the factory to find, same as
a property name
- classLoader

- classLoader to use

**Returns:**
- the factory implementation

**Throws:**
- FactoryConfigurationError

- if an instance of this factory cannot be loaded

---

#### public static
XMLOutputFactory
newFactory​(
String
factoryId,

ClassLoader
classLoader)
throws
FactoryConfigurationError

Create a new instance of the factory.
If the classLoader argument is null, then the ContextClassLoader is used.

This method uses the following ordered lookup procedure to determine
the XMLOutputFactory implementation class to load:

- Use the value of the system property identified by

factoryId

.
- Use the configuration file "stax.properties". The file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. It contains the fully qualified
name of the implementation class with the key being the system property
defined above.

The stax.properties file is read only once by the implementation
and its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any property in stax.properties after it has been read for the first time.

Use the jaxp configuration file "jaxp.properties". The file is in the same
format as stax.properties and will only be read if stax.properties does
not exist.
- If

factoryId

is "javax.xml.stream.XMLOutputFactory",
use the service-provider loading facility, defined by the

ServiceLoader

class, to attempt to

locate and load

an implementation of the service using the specified

ClassLoader

.
If

classLoader

is null, the

default loading mechanism

will apply:
That is, the service-provider loading facility will use the

current thread's context class loader

to attempt to load the service. If the context class
loader is null, the

system class loader

will be used.
- Otherwise, throws a

FactoryConfigurationError

.

**Parameters:**
- factoryId

- Name of the factory to find, same as
a property name
- classLoader

- classLoader to use

**Returns:**
- the factory implementation

**Throws:**
- FactoryConfigurationError

- in case of

service configuration error

or if
the implementation is not available or cannot be instantiated.

**API Note:**
- The parameter factoryId defined here is inconsistent with that
of other JAXP factories where the first parameter is fully qualified
factory class name that provides implementation of the factory.

Note that this is a new method that replaces the deprecated

newInstance(String factoryId, ClassLoader classLoader)

method.
The original method was incorrectly defined to return XMLInputFactory.

---

#### public abstract
XMLStreamWriter
createXMLStreamWriter​(
Writer
stream)
throws
XMLStreamException

Create a new XMLStreamWriter that writes to a writer

**Parameters:**
- stream

- the writer to write to

**Throws:**
- XMLStreamException

---

#### public abstract
XMLStreamWriter
createXMLStreamWriter​(
OutputStream
stream)
throws
XMLStreamException

Create a new XMLStreamWriter that writes to a stream

**Parameters:**
- stream

- the stream to write to

**Throws:**
- XMLStreamException

---

#### public abstract
XMLStreamWriter
createXMLStreamWriter​(
OutputStream
stream,

String
encoding)
throws
XMLStreamException

Create a new XMLStreamWriter that writes to a stream

**Parameters:**
- stream

- the stream to write to
- encoding

- the encoding to use

**Throws:**
- XMLStreamException

---

#### public abstract
XMLStreamWriter
createXMLStreamWriter​(
Result
result)
throws
XMLStreamException

Create a new XMLStreamWriter that writes to a JAXP result. This method is optional.

**Parameters:**
- result

- the result to write to

**Throws:**
- UnsupportedOperationException

- if this method is not
supported by this XMLOutputFactory
- XMLStreamException

---

#### public abstract
XMLEventWriter
createXMLEventWriter​(
Result
result)
throws
XMLStreamException

Create a new XMLEventWriter that writes to a JAXP result. This method is optional.

**Parameters:**
- result

- the result to write to

**Throws:**
- UnsupportedOperationException

- if this method is not
supported by this XMLOutputFactory
- XMLStreamException

---

#### public abstract
XMLEventWriter
createXMLEventWriter​(
OutputStream
stream)
throws
XMLStreamException

Create a new XMLEventWriter that writes to a stream

**Parameters:**
- stream

- the stream to write to

**Throws:**
- XMLStreamException

---

#### public abstract
XMLEventWriter
createXMLEventWriter​(
OutputStream
stream,

String
encoding)
throws
XMLStreamException

Create a new XMLEventWriter that writes to a stream

**Parameters:**
- stream

- the stream to write to
- encoding

- the encoding to use

**Throws:**
- XMLStreamException

---

#### public abstract
XMLEventWriter
createXMLEventWriter​(
Writer
stream)
throws
XMLStreamException

Create a new XMLEventWriter that writes to a writer

**Parameters:**
- stream

- the stream to write to

**Throws:**
- XMLStreamException

---

#### public abstract void setProperty​(
String
name,

Object
value)
throws
IllegalArgumentException

Allows the user to set specific features/properties on the underlying implementation.

**Parameters:**
- name

- The name of the property
- value

- The value of the property

**Throws:**
- IllegalArgumentException

- if the property is not supported

---

#### public abstract
Object
getProperty​(
String
name)
throws
IllegalArgumentException

Get a feature/property on the underlying implementation

**Parameters:**
- name

- The name of the property

**Returns:**
- The value of the property

**Throws:**
- IllegalArgumentException

- if the property is not supported

---

#### public abstract boolean isPropertySupported​(
String
name)

Query the set of properties that this factory supports.

**Parameters:**
- name

- The name of the property (may not be null)

**Returns:**
- true if the property is supported and false otherwise

---

### Additional Sections

#### Class XMLOutputFactory

java.lang.Object

- javax.xml.stream.XMLOutputFactory

javax.xml.stream.XMLOutputFactory

```java
public abstract class
XMLOutputFactory

extends
Object
```

Defines an abstract implementation of a factory for
getting XMLEventWriters and XMLStreamWriters.

The following table defines the standard properties of this specification.
Each property varies in the level of support required by each implementation.
The level of support required is described in the 'Required' column.

Configuration Parameters

Property Name

Behavior

Return type

Default Value

Required

javax.xml.stream.isRepairingNamespaces

defaults prefixes
on the output side

Boolean

False

Yes

The following paragraphs describe the namespace and prefix repair algorithm:

The property can be set with the following code line:

setProperty("javax.xml.stream.isRepairingNamespaces", new Boolean(true|false));

This property specifies that the writer default namespace prefix declarations.
The default value is false.

If a writer isRepairingNamespaces it will create a namespace declaration
on the current StartElement for
any attribute that does not
currently have a namespace declaration in scope. If the StartElement
has a uri but no prefix specified a prefix will be assigned, if the prefix
has not been declared in a parent of the current StartElement it will be declared
on the current StartElement. If the defaultNamespace is bound and in scope
and the default namespace matches the URI of the attribute or StartElement
QName no prefix will be assigned.

If an element or attribute name has a prefix, but is not
bound to any namespace URI, then the prefix will be removed
during serialization.

If element and/or attribute names in the same start or
empty-element tag are bound to different namespace URIs and
are using the same prefix then the element or the first
occurring attribute retains the original prefix and the
following attributes have their prefixes replaced with a
new prefix that is bound to the namespace URIs of those
attributes.

If an element or attribute name uses a prefix that is
bound to a different URI than that inherited from the
namespace context of the parent of that element and there
is no namespace declaration in the context of the current
element then such a namespace declaration is added.

If an element or attribute name is bound to a prefix and
there is a namespace declaration that binds that prefix
to a different URI then that namespace declaration is
either removed if the correct mapping is inherited from
the parent context of that element, or changed to the
namespace URI of the element or attribute using that prefix.

**Since:** 1.6
**See Also:** XMLInputFactory

,

XMLEventWriter

,

XMLStreamWriter

public abstract class

XMLOutputFactory

extends

Object

Defines an abstract implementation of a factory for
getting XMLEventWriters and XMLStreamWriters.

The following table defines the standard properties of this specification.
Each property varies in the level of support required by each implementation.
The level of support required is described in the 'Required' column.

Configuration Parameters

Property Name

Behavior

Return type

Default Value

Required

javax.xml.stream.isRepairingNamespaces

defaults prefixes
on the output side

Boolean

False

Yes

The following paragraphs describe the namespace and prefix repair algorithm:

The property can be set with the following code line:

setProperty("javax.xml.stream.isRepairingNamespaces", new Boolean(true|false));

This property specifies that the writer default namespace prefix declarations.
The default value is false.

If a writer isRepairingNamespaces it will create a namespace declaration
on the current StartElement for
any attribute that does not
currently have a namespace declaration in scope. If the StartElement
has a uri but no prefix specified a prefix will be assigned, if the prefix
has not been declared in a parent of the current StartElement it will be declared
on the current StartElement. If the defaultNamespace is bound and in scope
and the default namespace matches the URI of the attribute or StartElement
QName no prefix will be assigned.

If an element or attribute name has a prefix, but is not
bound to any namespace URI, then the prefix will be removed
during serialization.

If element and/or attribute names in the same start or
empty-element tag are bound to different namespace URIs and
are using the same prefix then the element or the first
occurring attribute retains the original prefix and the
following attributes have their prefixes replaced with a
new prefix that is bound to the namespace URIs of those
attributes.

If an element or attribute name uses a prefix that is
bound to a different URI than that inherited from the
namespace context of the parent of that element and there
is no namespace declaration in the context of the current
element then such a namespace declaration is added.

If an element or attribute name is bound to a prefix and
there is a namespace declaration that binds that prefix
to a different URI then that namespace declaration is
either removed if the correct mapping is inherited from
the parent context of that element, or changed to the
namespace URI of the element or attribute using that prefix.

The following paragraphs describe the namespace and prefix repair algorithm:

The property can be set with the following code line:

setProperty("javax.xml.stream.isRepairingNamespaces", new Boolean(true|false));

This property specifies that the writer default namespace prefix declarations.
The default value is false.

If a writer isRepairingNamespaces it will create a namespace declaration
on the current StartElement for
any attribute that does not
currently have a namespace declaration in scope. If the StartElement
has a uri but no prefix specified a prefix will be assigned, if the prefix
has not been declared in a parent of the current StartElement it will be declared
on the current StartElement. If the defaultNamespace is bound and in scope
and the default namespace matches the URI of the attribute or StartElement
QName no prefix will be assigned.

If an element or attribute name has a prefix, but is not
bound to any namespace URI, then the prefix will be removed
during serialization.

If element and/or attribute names in the same start or
empty-element tag are bound to different namespace URIs and
are using the same prefix then the element or the first
occurring attribute retains the original prefix and the
following attributes have their prefixes replaced with a
new prefix that is bound to the namespace URIs of those
attributes.

If an element or attribute name uses a prefix that is
bound to a different URI than that inherited from the
namespace context of the parent of that element and there
is no namespace declaration in the context of the current
element then such a namespace declaration is added.

If an element or attribute name is bound to a prefix and
there is a namespace declaration that binds that prefix
to a different URI then that namespace declaration is
either removed if the correct mapping is inherited from
the parent context of that element, or changed to the
namespace URI of the element or attribute using that prefix.

The property can be set with the following code line:

setProperty("javax.xml.stream.isRepairingNamespaces", new Boolean(true|false));

This property specifies that the writer default namespace prefix declarations.
The default value is false.

If a writer isRepairingNamespaces it will create a namespace declaration
on the current StartElement for
any attribute that does not
currently have a namespace declaration in scope. If the StartElement
has a uri but no prefix specified a prefix will be assigned, if the prefix
has not been declared in a parent of the current StartElement it will be declared
on the current StartElement. If the defaultNamespace is bound and in scope
and the default namespace matches the URI of the attribute or StartElement
QName no prefix will be assigned.

If an element or attribute name has a prefix, but is not
bound to any namespace URI, then the prefix will be removed
during serialization.

If element and/or attribute names in the same start or
empty-element tag are bound to different namespace URIs and
are using the same prefix then the element or the first
occurring attribute retains the original prefix and the
following attributes have their prefixes replaced with a
new prefix that is bound to the namespace URIs of those
attributes.

If an element or attribute name uses a prefix that is
bound to a different URI than that inherited from the
namespace context of the parent of that element and there
is no namespace declaration in the context of the current
element then such a namespace declaration is added.

If an element or attribute name is bound to a prefix and
there is a namespace declaration that binds that prefix
to a different URI then that namespace declaration is
either removed if the correct mapping is inherited from
the parent context of that element, or changed to the
namespace URI of the element or attribute using that prefix.

This property specifies that the writer default namespace prefix declarations.
The default value is false.

If a writer isRepairingNamespaces it will create a namespace declaration
on the current StartElement for
any attribute that does not
currently have a namespace declaration in scope. If the StartElement
has a uri but no prefix specified a prefix will be assigned, if the prefix
has not been declared in a parent of the current StartElement it will be declared
on the current StartElement. If the defaultNamespace is bound and in scope
and the default namespace matches the URI of the attribute or StartElement
QName no prefix will be assigned.

If an element or attribute name has a prefix, but is not
bound to any namespace URI, then the prefix will be removed
during serialization.

If element and/or attribute names in the same start or
empty-element tag are bound to different namespace URIs and
are using the same prefix then the element or the first
occurring attribute retains the original prefix and the
following attributes have their prefixes replaced with a
new prefix that is bound to the namespace URIs of those
attributes.

If an element or attribute name uses a prefix that is
bound to a different URI than that inherited from the
namespace context of the parent of that element and there
is no namespace declaration in the context of the current
element then such a namespace declaration is added.

If an element or attribute name is bound to a prefix and
there is a namespace declaration that binds that prefix
to a different URI then that namespace declaration is
either removed if the correct mapping is inherited from
the parent context of that element, or changed to the
namespace URI of the element or attribute using that prefix.

If a writer isRepairingNamespaces it will create a namespace declaration
on the current StartElement for
any attribute that does not
currently have a namespace declaration in scope. If the StartElement
has a uri but no prefix specified a prefix will be assigned, if the prefix
has not been declared in a parent of the current StartElement it will be declared
on the current StartElement. If the defaultNamespace is bound and in scope
and the default namespace matches the URI of the attribute or StartElement
QName no prefix will be assigned.

If an element or attribute name has a prefix, but is not
bound to any namespace URI, then the prefix will be removed
during serialization.

If element and/or attribute names in the same start or
empty-element tag are bound to different namespace URIs and
are using the same prefix then the element or the first
occurring attribute retains the original prefix and the
following attributes have their prefixes replaced with a
new prefix that is bound to the namespace URIs of those
attributes.

If an element or attribute name uses a prefix that is
bound to a different URI than that inherited from the
namespace context of the parent of that element and there
is no namespace declaration in the context of the current
element then such a namespace declaration is added.

If an element or attribute name is bound to a prefix and
there is a namespace declaration that binds that prefix
to a different URI then that namespace declaration is
either removed if the correct mapping is inherited from
the parent context of that element, or changed to the
namespace URI of the element or attribute using that prefix.

If an element or attribute name has a prefix, but is not
bound to any namespace URI, then the prefix will be removed
during serialization.

If element and/or attribute names in the same start or
empty-element tag are bound to different namespace URIs and
are using the same prefix then the element or the first
occurring attribute retains the original prefix and the
following attributes have their prefixes replaced with a
new prefix that is bound to the namespace URIs of those
attributes.

If an element or attribute name uses a prefix that is
bound to a different URI than that inherited from the
namespace context of the parent of that element and there
is no namespace declaration in the context of the current
element then such a namespace declaration is added.

If an element or attribute name is bound to a prefix and
there is a namespace declaration that binds that prefix
to a different URI then that namespace declaration is
either removed if the correct mapping is inherited from
the parent context of that element, or changed to the
namespace URI of the element or attribute using that prefix.

If element and/or attribute names in the same start or
empty-element tag are bound to different namespace URIs and
are using the same prefix then the element or the first
occurring attribute retains the original prefix and the
following attributes have their prefixes replaced with a
new prefix that is bound to the namespace URIs of those
attributes.

If an element or attribute name uses a prefix that is
bound to a different URI than that inherited from the
namespace context of the parent of that element and there
is no namespace declaration in the context of the current
element then such a namespace declaration is added.

If an element or attribute name is bound to a prefix and
there is a namespace declaration that binds that prefix
to a different URI then that namespace declaration is
either removed if the correct mapping is inherited from
the parent context of that element, or changed to the
namespace URI of the element or attribute using that prefix.

If an element or attribute name uses a prefix that is
bound to a different URI than that inherited from the
namespace context of the parent of that element and there
is no namespace declaration in the context of the current
element then such a namespace declaration is added.

If an element or attribute name is bound to a prefix and
there is a namespace declaration that binds that prefix
to a different URI then that namespace declaration is
either removed if the correct mapping is inherited from
the parent context of that element, or changed to the
namespace URI of the element or attribute using that prefix.

If an element or attribute name is bound to a prefix and
there is a namespace declaration that binds that prefix
to a different URI then that namespace declaration is
either removed if the correct mapping is inherited from
the parent context of that element, or changed to the
namespace URI of the element or attribute using that prefix.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

IS_REPAIRING_NAMESPACES

Property used to set prefix defaulting on the output side

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

XMLOutputFactory

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

abstract

XMLEventWriter

createXMLEventWriter

​(

OutputStream

stream)

Create a new XMLEventWriter that writes to a stream

abstract

XMLEventWriter

createXMLEventWriter

​(

OutputStream

stream,

String

encoding)

Create a new XMLEventWriter that writes to a stream

abstract

XMLEventWriter

createXMLEventWriter

​(

Writer

stream)

Create a new XMLEventWriter that writes to a writer

abstract

XMLEventWriter

createXMLEventWriter

​(

Result

result)

Create a new XMLEventWriter that writes to a JAXP result.

abstract

XMLStreamWriter

createXMLStreamWriter

​(

OutputStream

stream)

Create a new XMLStreamWriter that writes to a stream

abstract

XMLStreamWriter

createXMLStreamWriter

​(

OutputStream

stream,

String

encoding)

Create a new XMLStreamWriter that writes to a stream

abstract

XMLStreamWriter

createXMLStreamWriter

​(

Writer

stream)

Create a new XMLStreamWriter that writes to a writer

abstract

XMLStreamWriter

createXMLStreamWriter

​(

Result

result)

Create a new XMLStreamWriter that writes to a JAXP result.

abstract

Object

getProperty

​(

String

name)

Get a feature/property on the underlying implementation

abstract boolean

isPropertySupported

​(

String

name)

Query the set of properties that this factory supports.

static

XMLOutputFactory

newDefaultFactory

()

Creates a new instance of the

XMLOutputFactory

builtin
system-default implementation.

static

XMLOutputFactory

newFactory

()

Create a new instance of the factory.

static

XMLOutputFactory

newFactory

​(

String

factoryId,

ClassLoader

classLoader)

Create a new instance of the factory.

static

XMLOutputFactory

newInstance

()

Creates a new instance of the factory in exactly the same manner as the

newFactory()

method.

static

XMLInputFactory

newInstance

​(

String

factoryId,

ClassLoader

classLoader)

Deprecated.

This method has been deprecated because it returns an
instance of XMLInputFactory, which is of the wrong class.

abstract void

setProperty

​(

String

name,

Object

value)

Allows the user to set specific features/properties on the underlying implementation.

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

IS_REPAIRING_NAMESPACES

Property used to set prefix defaulting on the output side

---

#### Field Summary

Property used to set prefix defaulting on the output side

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

XMLOutputFactory

()

---

#### Constructor Summary

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

abstract

XMLEventWriter

createXMLEventWriter

​(

OutputStream

stream)

Create a new XMLEventWriter that writes to a stream

abstract

XMLEventWriter

createXMLEventWriter

​(

OutputStream

stream,

String

encoding)

Create a new XMLEventWriter that writes to a stream

abstract

XMLEventWriter

createXMLEventWriter

​(

Writer

stream)

Create a new XMLEventWriter that writes to a writer

abstract

XMLEventWriter

createXMLEventWriter

​(

Result

result)

Create a new XMLEventWriter that writes to a JAXP result.

abstract

XMLStreamWriter

createXMLStreamWriter

​(

OutputStream

stream)

Create a new XMLStreamWriter that writes to a stream

abstract

XMLStreamWriter

createXMLStreamWriter

​(

OutputStream

stream,

String

encoding)

Create a new XMLStreamWriter that writes to a stream

abstract

XMLStreamWriter

createXMLStreamWriter

​(

Writer

stream)

Create a new XMLStreamWriter that writes to a writer

abstract

XMLStreamWriter

createXMLStreamWriter

​(

Result

result)

Create a new XMLStreamWriter that writes to a JAXP result.

abstract

Object

getProperty

​(

String

name)

Get a feature/property on the underlying implementation

abstract boolean

isPropertySupported

​(

String

name)

Query the set of properties that this factory supports.

static

XMLOutputFactory

newDefaultFactory

()

Creates a new instance of the

XMLOutputFactory

builtin
system-default implementation.

static

XMLOutputFactory

newFactory

()

Create a new instance of the factory.

static

XMLOutputFactory

newFactory

​(

String

factoryId,

ClassLoader

classLoader)

Create a new instance of the factory.

static

XMLOutputFactory

newInstance

()

Creates a new instance of the factory in exactly the same manner as the

newFactory()

method.

static

XMLInputFactory

newInstance

​(

String

factoryId,

ClassLoader

classLoader)

Deprecated.

This method has been deprecated because it returns an
instance of XMLInputFactory, which is of the wrong class.

abstract void

setProperty

​(

String

name,

Object

value)

Allows the user to set specific features/properties on the underlying implementation.

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

Create a new XMLEventWriter that writes to a stream

Create a new XMLEventWriter that writes to a writer

Create a new XMLEventWriter that writes to a JAXP result.

Create a new XMLStreamWriter that writes to a stream

Create a new XMLStreamWriter that writes to a writer

Create a new XMLStreamWriter that writes to a JAXP result.

Get a feature/property on the underlying implementation

Query the set of properties that this factory supports.

Creates a new instance of the

XMLOutputFactory

builtin
system-default implementation.

Create a new instance of the factory.

Creates a new instance of the factory in exactly the same manner as the

newFactory()

method.

Deprecated.

This method has been deprecated because it returns an
instance of XMLInputFactory, which is of the wrong class.

Allows the user to set specific features/properties on the underlying implementation.

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

- IS_REPAIRING_NAMESPACES

```java
public static final
String
IS_REPAIRING_NAMESPACES
```

Property used to set prefix defaulting on the output side

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- XMLOutputFactory

```java
protected XMLOutputFactory()
```

============ METHOD DETAIL ==========

- Method Detail

- newDefaultFactory

```java
public static
XMLOutputFactory
newDefaultFactory()
```

Creates a new instance of the

XMLOutputFactory

builtin
system-default implementation.

**Returns:** A new instance of the

XMLOutputFactory

builtin
system-default implementation.
**Since:** 9

- newInstance

```java
public static
XMLOutputFactory
newInstance()
throws
FactoryConfigurationError
```

Creates a new instance of the factory in exactly the same manner as the

newFactory()

method.

**Throws:** FactoryConfigurationError

- if an instance of this factory cannot be loaded

- newFactory

```java
public static
XMLOutputFactory
newFactory()
throws
FactoryConfigurationError
```

Create a new instance of the factory.

This static method creates a new factory instance. This method uses the
following ordered lookup procedure to determine the XMLOutputFactory
implementation class to load:

- Use the javax.xml.stream.XMLOutputFactory system property.
- Use the configuration file "stax.properties". The file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. It contains the fully qualified
name of the implementation class with the key being the system property
defined above.

The stax.properties file is read only once by the implementation
and its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any property in stax.properties after it has been read for the first time.

Use the jaxp configuration file "jaxp.properties". The file is in the same
format as stax.properties and will only be read if stax.properties does
not exist.
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

Once an application has obtained a reference to a XMLOutputFactory it
can use the factory to configure and obtain stream instances.

**Throws:** FactoryConfigurationError

- in case of

service configuration error

or if
the implementation is not available or cannot be instantiated.

- newInstance

```java
@Deprecated
(
since
="1.7")
public static
XMLInputFactory
newInstance​(
String
factoryId,

ClassLoader
classLoader)
throws
FactoryConfigurationError
```

Deprecated.

This method has been deprecated because it returns an
instance of XMLInputFactory, which is of the wrong class.
Use the new method

newFactory(java.lang.String,
java.lang.ClassLoader)

instead.

Create a new instance of the factory.

**Parameters:** factoryId

- Name of the factory to find, same as
a property name
**Parameters:** classLoader

- classLoader to use
**Returns:** the factory implementation
**Throws:** FactoryConfigurationError

- if an instance of this factory cannot be loaded

- newFactory

```java
public static
XMLOutputFactory
newFactory​(
String
factoryId,

ClassLoader
classLoader)
throws
FactoryConfigurationError
```

Create a new instance of the factory.
If the classLoader argument is null, then the ContextClassLoader is used.

This method uses the following ordered lookup procedure to determine
the XMLOutputFactory implementation class to load:

- Use the value of the system property identified by

factoryId

.
- Use the configuration file "stax.properties". The file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. It contains the fully qualified
name of the implementation class with the key being the system property
defined above.

The stax.properties file is read only once by the implementation
and its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any property in stax.properties after it has been read for the first time.

Use the jaxp configuration file "jaxp.properties". The file is in the same
format as stax.properties and will only be read if stax.properties does
not exist.
- If

factoryId

is "javax.xml.stream.XMLOutputFactory",
use the service-provider loading facility, defined by the

ServiceLoader

class, to attempt to

locate and load

an implementation of the service using the specified

ClassLoader

.
If

classLoader

is null, the

default loading mechanism

will apply:
That is, the service-provider loading facility will use the

current thread's context class loader

to attempt to load the service. If the context class
loader is null, the

system class loader

will be used.
- Otherwise, throws a

FactoryConfigurationError

.

**API Note:** The parameter factoryId defined here is inconsistent with that
of other JAXP factories where the first parameter is fully qualified
factory class name that provides implementation of the factory.

Note that this is a new method that replaces the deprecated

newInstance(String factoryId, ClassLoader classLoader)

method.
The original method was incorrectly defined to return XMLInputFactory.
**Parameters:** factoryId

- Name of the factory to find, same as
a property name
**Parameters:** classLoader

- classLoader to use
**Returns:** the factory implementation
**Throws:** FactoryConfigurationError

- in case of

service configuration error

or if
the implementation is not available or cannot be instantiated.

- createXMLStreamWriter

```java
public abstract
XMLStreamWriter
createXMLStreamWriter​(
Writer
stream)
throws
XMLStreamException
```

Create a new XMLStreamWriter that writes to a writer

**Parameters:** stream

- the writer to write to
**Throws:** XMLStreamException

- createXMLStreamWriter

```java
public abstract
XMLStreamWriter
createXMLStreamWriter​(
OutputStream
stream)
throws
XMLStreamException
```

Create a new XMLStreamWriter that writes to a stream

**Parameters:** stream

- the stream to write to
**Throws:** XMLStreamException

- createXMLStreamWriter

```java
public abstract
XMLStreamWriter
createXMLStreamWriter​(
OutputStream
stream,

String
encoding)
throws
XMLStreamException
```

Create a new XMLStreamWriter that writes to a stream

**Parameters:** stream

- the stream to write to
**Parameters:** encoding

- the encoding to use
**Throws:** XMLStreamException

- createXMLStreamWriter

```java
public abstract
XMLStreamWriter
createXMLStreamWriter​(
Result
result)
throws
XMLStreamException
```

Create a new XMLStreamWriter that writes to a JAXP result. This method is optional.

**Parameters:** result

- the result to write to
**Throws:** UnsupportedOperationException

- if this method is not
supported by this XMLOutputFactory
**Throws:** XMLStreamException

- createXMLEventWriter

```java
public abstract
XMLEventWriter
createXMLEventWriter​(
Result
result)
throws
XMLStreamException
```

Create a new XMLEventWriter that writes to a JAXP result. This method is optional.

**Parameters:** result

- the result to write to
**Throws:** UnsupportedOperationException

- if this method is not
supported by this XMLOutputFactory
**Throws:** XMLStreamException

- createXMLEventWriter

```java
public abstract
XMLEventWriter
createXMLEventWriter​(
OutputStream
stream)
throws
XMLStreamException
```

Create a new XMLEventWriter that writes to a stream

**Parameters:** stream

- the stream to write to
**Throws:** XMLStreamException

- createXMLEventWriter

```java
public abstract
XMLEventWriter
createXMLEventWriter​(
OutputStream
stream,

String
encoding)
throws
XMLStreamException
```

Create a new XMLEventWriter that writes to a stream

**Parameters:** stream

- the stream to write to
**Parameters:** encoding

- the encoding to use
**Throws:** XMLStreamException

- createXMLEventWriter

```java
public abstract
XMLEventWriter
createXMLEventWriter​(
Writer
stream)
throws
XMLStreamException
```

Create a new XMLEventWriter that writes to a writer

**Parameters:** stream

- the stream to write to
**Throws:** XMLStreamException

- setProperty

```java
public abstract void setProperty​(
String
name,

Object
value)
throws
IllegalArgumentException
```

Allows the user to set specific features/properties on the underlying implementation.

**Parameters:** name

- The name of the property
**Parameters:** value

- The value of the property
**Throws:** IllegalArgumentException

- if the property is not supported

- getProperty

```java
public abstract
Object
getProperty​(
String
name)
throws
IllegalArgumentException
```

Get a feature/property on the underlying implementation

**Parameters:** name

- The name of the property
**Returns:** The value of the property
**Throws:** IllegalArgumentException

- if the property is not supported

- isPropertySupported

```java
public abstract boolean isPropertySupported​(
String
name)
```

Query the set of properties that this factory supports.

**Parameters:** name

- The name of the property (may not be null)
**Returns:** true if the property is supported and false otherwise

Field Detail

- IS_REPAIRING_NAMESPACES

```java
public static final
String
IS_REPAIRING_NAMESPACES
```

Property used to set prefix defaulting on the output side

**See Also:** Constant Field Values

---

#### Field Detail

IS_REPAIRING_NAMESPACES

```java
public static final
String
IS_REPAIRING_NAMESPACES
```

Property used to set prefix defaulting on the output side

**See Also:** Constant Field Values

---

#### IS_REPAIRING_NAMESPACES

public static final

String

IS_REPAIRING_NAMESPACES

Property used to set prefix defaulting on the output side

Constructor Detail

- XMLOutputFactory

```java
protected XMLOutputFactory()
```

---

#### Constructor Detail

XMLOutputFactory

```java
protected XMLOutputFactory()
```

---

#### XMLOutputFactory

protected XMLOutputFactory()

Method Detail

- newDefaultFactory

```java
public static
XMLOutputFactory
newDefaultFactory()
```

Creates a new instance of the

XMLOutputFactory

builtin
system-default implementation.

**Returns:** A new instance of the

XMLOutputFactory

builtin
system-default implementation.
**Since:** 9

- newInstance

```java
public static
XMLOutputFactory
newInstance()
throws
FactoryConfigurationError
```

Creates a new instance of the factory in exactly the same manner as the

newFactory()

method.

**Throws:** FactoryConfigurationError

- if an instance of this factory cannot be loaded

- newFactory

```java
public static
XMLOutputFactory
newFactory()
throws
FactoryConfigurationError
```

Create a new instance of the factory.

This static method creates a new factory instance. This method uses the
following ordered lookup procedure to determine the XMLOutputFactory
implementation class to load:

- Use the javax.xml.stream.XMLOutputFactory system property.
- Use the configuration file "stax.properties". The file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. It contains the fully qualified
name of the implementation class with the key being the system property
defined above.

The stax.properties file is read only once by the implementation
and its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any property in stax.properties after it has been read for the first time.

Use the jaxp configuration file "jaxp.properties". The file is in the same
format as stax.properties and will only be read if stax.properties does
not exist.
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

Once an application has obtained a reference to a XMLOutputFactory it
can use the factory to configure and obtain stream instances.

**Throws:** FactoryConfigurationError

- in case of

service configuration error

or if
the implementation is not available or cannot be instantiated.

- newInstance

```java
@Deprecated
(
since
="1.7")
public static
XMLInputFactory
newInstance​(
String
factoryId,

ClassLoader
classLoader)
throws
FactoryConfigurationError
```

Deprecated.

This method has been deprecated because it returns an
instance of XMLInputFactory, which is of the wrong class.
Use the new method

newFactory(java.lang.String,
java.lang.ClassLoader)

instead.

Create a new instance of the factory.

**Parameters:** factoryId

- Name of the factory to find, same as
a property name
**Parameters:** classLoader

- classLoader to use
**Returns:** the factory implementation
**Throws:** FactoryConfigurationError

- if an instance of this factory cannot be loaded

- newFactory

```java
public static
XMLOutputFactory
newFactory​(
String
factoryId,

ClassLoader
classLoader)
throws
FactoryConfigurationError
```

Create a new instance of the factory.
If the classLoader argument is null, then the ContextClassLoader is used.

This method uses the following ordered lookup procedure to determine
the XMLOutputFactory implementation class to load:

- Use the value of the system property identified by

factoryId

.
- Use the configuration file "stax.properties". The file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. It contains the fully qualified
name of the implementation class with the key being the system property
defined above.

The stax.properties file is read only once by the implementation
and its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any property in stax.properties after it has been read for the first time.

Use the jaxp configuration file "jaxp.properties". The file is in the same
format as stax.properties and will only be read if stax.properties does
not exist.
- If

factoryId

is "javax.xml.stream.XMLOutputFactory",
use the service-provider loading facility, defined by the

ServiceLoader

class, to attempt to

locate and load

an implementation of the service using the specified

ClassLoader

.
If

classLoader

is null, the

default loading mechanism

will apply:
That is, the service-provider loading facility will use the

current thread's context class loader

to attempt to load the service. If the context class
loader is null, the

system class loader

will be used.
- Otherwise, throws a

FactoryConfigurationError

.

**API Note:** The parameter factoryId defined here is inconsistent with that
of other JAXP factories where the first parameter is fully qualified
factory class name that provides implementation of the factory.

Note that this is a new method that replaces the deprecated

newInstance(String factoryId, ClassLoader classLoader)

method.
The original method was incorrectly defined to return XMLInputFactory.
**Parameters:** factoryId

- Name of the factory to find, same as
a property name
**Parameters:** classLoader

- classLoader to use
**Returns:** the factory implementation
**Throws:** FactoryConfigurationError

- in case of

service configuration error

or if
the implementation is not available or cannot be instantiated.

- createXMLStreamWriter

```java
public abstract
XMLStreamWriter
createXMLStreamWriter​(
Writer
stream)
throws
XMLStreamException
```

Create a new XMLStreamWriter that writes to a writer

**Parameters:** stream

- the writer to write to
**Throws:** XMLStreamException

- createXMLStreamWriter

```java
public abstract
XMLStreamWriter
createXMLStreamWriter​(
OutputStream
stream)
throws
XMLStreamException
```

Create a new XMLStreamWriter that writes to a stream

**Parameters:** stream

- the stream to write to
**Throws:** XMLStreamException

- createXMLStreamWriter

```java
public abstract
XMLStreamWriter
createXMLStreamWriter​(
OutputStream
stream,

String
encoding)
throws
XMLStreamException
```

Create a new XMLStreamWriter that writes to a stream

**Parameters:** stream

- the stream to write to
**Parameters:** encoding

- the encoding to use
**Throws:** XMLStreamException

- createXMLStreamWriter

```java
public abstract
XMLStreamWriter
createXMLStreamWriter​(
Result
result)
throws
XMLStreamException
```

Create a new XMLStreamWriter that writes to a JAXP result. This method is optional.

**Parameters:** result

- the result to write to
**Throws:** UnsupportedOperationException

- if this method is not
supported by this XMLOutputFactory
**Throws:** XMLStreamException

- createXMLEventWriter

```java
public abstract
XMLEventWriter
createXMLEventWriter​(
Result
result)
throws
XMLStreamException
```

Create a new XMLEventWriter that writes to a JAXP result. This method is optional.

**Parameters:** result

- the result to write to
**Throws:** UnsupportedOperationException

- if this method is not
supported by this XMLOutputFactory
**Throws:** XMLStreamException

- createXMLEventWriter

```java
public abstract
XMLEventWriter
createXMLEventWriter​(
OutputStream
stream)
throws
XMLStreamException
```

Create a new XMLEventWriter that writes to a stream

**Parameters:** stream

- the stream to write to
**Throws:** XMLStreamException

- createXMLEventWriter

```java
public abstract
XMLEventWriter
createXMLEventWriter​(
OutputStream
stream,

String
encoding)
throws
XMLStreamException
```

Create a new XMLEventWriter that writes to a stream

**Parameters:** stream

- the stream to write to
**Parameters:** encoding

- the encoding to use
**Throws:** XMLStreamException

- createXMLEventWriter

```java
public abstract
XMLEventWriter
createXMLEventWriter​(
Writer
stream)
throws
XMLStreamException
```

Create a new XMLEventWriter that writes to a writer

**Parameters:** stream

- the stream to write to
**Throws:** XMLStreamException

- setProperty

```java
public abstract void setProperty​(
String
name,

Object
value)
throws
IllegalArgumentException
```

Allows the user to set specific features/properties on the underlying implementation.

**Parameters:** name

- The name of the property
**Parameters:** value

- The value of the property
**Throws:** IllegalArgumentException

- if the property is not supported

- getProperty

```java
public abstract
Object
getProperty​(
String
name)
throws
IllegalArgumentException
```

Get a feature/property on the underlying implementation

**Parameters:** name

- The name of the property
**Returns:** The value of the property
**Throws:** IllegalArgumentException

- if the property is not supported

- isPropertySupported

```java
public abstract boolean isPropertySupported​(
String
name)
```

Query the set of properties that this factory supports.

**Parameters:** name

- The name of the property (may not be null)
**Returns:** true if the property is supported and false otherwise

---

#### Method Detail

newDefaultFactory

```java
public static
XMLOutputFactory
newDefaultFactory()
```

Creates a new instance of the

XMLOutputFactory

builtin
system-default implementation.

**Returns:** A new instance of the

XMLOutputFactory

builtin
system-default implementation.
**Since:** 9

---

#### newDefaultFactory

public static

XMLOutputFactory

newDefaultFactory()

Creates a new instance of the

XMLOutputFactory

builtin
system-default implementation.

newInstance

```java
public static
XMLOutputFactory
newInstance()
throws
FactoryConfigurationError
```

Creates a new instance of the factory in exactly the same manner as the

newFactory()

method.

**Throws:** FactoryConfigurationError

- if an instance of this factory cannot be loaded

---

#### newInstance

public static

XMLOutputFactory

newInstance()
throws

FactoryConfigurationError

Creates a new instance of the factory in exactly the same manner as the

newFactory()

method.

newFactory

```java
public static
XMLOutputFactory
newFactory()
throws
FactoryConfigurationError
```

Create a new instance of the factory.

This static method creates a new factory instance. This method uses the
following ordered lookup procedure to determine the XMLOutputFactory
implementation class to load:

- Use the javax.xml.stream.XMLOutputFactory system property.
- Use the configuration file "stax.properties". The file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. It contains the fully qualified
name of the implementation class with the key being the system property
defined above.

The stax.properties file is read only once by the implementation
and its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any property in stax.properties after it has been read for the first time.

Use the jaxp configuration file "jaxp.properties". The file is in the same
format as stax.properties and will only be read if stax.properties does
not exist.
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

Once an application has obtained a reference to a XMLOutputFactory it
can use the factory to configure and obtain stream instances.

**Throws:** FactoryConfigurationError

- in case of

service configuration error

or if
the implementation is not available or cannot be instantiated.

---

#### newFactory

public static

XMLOutputFactory

newFactory()
throws

FactoryConfigurationError

Create a new instance of the factory.

This static method creates a new factory instance. This method uses the
following ordered lookup procedure to determine the XMLOutputFactory
implementation class to load:

- Use the javax.xml.stream.XMLOutputFactory system property.
- Use the configuration file "stax.properties". The file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. It contains the fully qualified
name of the implementation class with the key being the system property
defined above.

The stax.properties file is read only once by the implementation
and its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any property in stax.properties after it has been read for the first time.

Use the jaxp configuration file "jaxp.properties". The file is in the same
format as stax.properties and will only be read if stax.properties does
not exist.
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

Once an application has obtained a reference to a XMLOutputFactory it
can use the factory to configure and obtain stream instances.

This static method creates a new factory instance. This method uses the
following ordered lookup procedure to determine the XMLOutputFactory
implementation class to load:

- Use the javax.xml.stream.XMLOutputFactory system property.
- Use the configuration file "stax.properties". The file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. It contains the fully qualified
name of the implementation class with the key being the system property
defined above.

The stax.properties file is read only once by the implementation
and its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any property in stax.properties after it has been read for the first time.

Use the jaxp configuration file "jaxp.properties". The file is in the same
format as stax.properties and will only be read if stax.properties does
not exist.
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

Once an application has obtained a reference to a XMLOutputFactory it
can use the factory to configure and obtain stream instances.

Use the javax.xml.stream.XMLOutputFactory system property.

Use the configuration file "stax.properties". The file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. It contains the fully qualified
name of the implementation class with the key being the system property
defined above.

The stax.properties file is read only once by the implementation
and its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any property in stax.properties after it has been read for the first time.

Use the jaxp configuration file "jaxp.properties". The file is in the same
format as stax.properties and will only be read if stax.properties does
not exist.

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

Use the configuration file "stax.properties". The file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. It contains the fully qualified
name of the implementation class with the key being the system property
defined above.

The stax.properties file is read only once by the implementation
and its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any property in stax.properties after it has been read for the first time.

Use the jaxp configuration file "jaxp.properties". The file is in the same
format as stax.properties and will only be read if stax.properties does
not exist.

The stax.properties file is read only once by the implementation
and its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any property in stax.properties after it has been read for the first time.

Use the jaxp configuration file "jaxp.properties". The file is in the same
format as stax.properties and will only be read if stax.properties does
not exist.

Use the jaxp configuration file "jaxp.properties". The file is in the same
format as stax.properties and will only be read if stax.properties does
not exist.

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

Once an application has obtained a reference to a XMLOutputFactory it
can use the factory to configure and obtain stream instances.

newInstance

```java
@Deprecated
(
since
="1.7")
public static
XMLInputFactory
newInstance​(
String
factoryId,

ClassLoader
classLoader)
throws
FactoryConfigurationError
```

Deprecated.

This method has been deprecated because it returns an
instance of XMLInputFactory, which is of the wrong class.
Use the new method

newFactory(java.lang.String,
java.lang.ClassLoader)

instead.

Create a new instance of the factory.

**Parameters:** factoryId

- Name of the factory to find, same as
a property name
**Parameters:** classLoader

- classLoader to use
**Returns:** the factory implementation
**Throws:** FactoryConfigurationError

- if an instance of this factory cannot be loaded

---

#### newInstance

@Deprecated

(

since

="1.7")
public static

XMLInputFactory

newInstance​(

String

factoryId,

ClassLoader

classLoader)
throws

FactoryConfigurationError

Create a new instance of the factory.

newFactory

```java
public static
XMLOutputFactory
newFactory​(
String
factoryId,

ClassLoader
classLoader)
throws
FactoryConfigurationError
```

Create a new instance of the factory.
If the classLoader argument is null, then the ContextClassLoader is used.

This method uses the following ordered lookup procedure to determine
the XMLOutputFactory implementation class to load:

- Use the value of the system property identified by

factoryId

.
- Use the configuration file "stax.properties". The file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. It contains the fully qualified
name of the implementation class with the key being the system property
defined above.

The stax.properties file is read only once by the implementation
and its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any property in stax.properties after it has been read for the first time.

Use the jaxp configuration file "jaxp.properties". The file is in the same
format as stax.properties and will only be read if stax.properties does
not exist.
- If

factoryId

is "javax.xml.stream.XMLOutputFactory",
use the service-provider loading facility, defined by the

ServiceLoader

class, to attempt to

locate and load

an implementation of the service using the specified

ClassLoader

.
If

classLoader

is null, the

default loading mechanism

will apply:
That is, the service-provider loading facility will use the

current thread's context class loader

to attempt to load the service. If the context class
loader is null, the

system class loader

will be used.
- Otherwise, throws a

FactoryConfigurationError

.

**API Note:** The parameter factoryId defined here is inconsistent with that
of other JAXP factories where the first parameter is fully qualified
factory class name that provides implementation of the factory.

Note that this is a new method that replaces the deprecated

newInstance(String factoryId, ClassLoader classLoader)

method.
The original method was incorrectly defined to return XMLInputFactory.
**Parameters:** factoryId

- Name of the factory to find, same as
a property name
**Parameters:** classLoader

- classLoader to use
**Returns:** the factory implementation
**Throws:** FactoryConfigurationError

- in case of

service configuration error

or if
the implementation is not available or cannot be instantiated.

---

#### newFactory

public static

XMLOutputFactory

newFactory​(

String

factoryId,

ClassLoader

classLoader)
throws

FactoryConfigurationError

Create a new instance of the factory.
If the classLoader argument is null, then the ContextClassLoader is used.

This method uses the following ordered lookup procedure to determine
the XMLOutputFactory implementation class to load:

- Use the value of the system property identified by

factoryId

.
- Use the configuration file "stax.properties". The file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. It contains the fully qualified
name of the implementation class with the key being the system property
defined above.

The stax.properties file is read only once by the implementation
and its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any property in stax.properties after it has been read for the first time.

Use the jaxp configuration file "jaxp.properties". The file is in the same
format as stax.properties and will only be read if stax.properties does
not exist.
- If

factoryId

is "javax.xml.stream.XMLOutputFactory",
use the service-provider loading facility, defined by the

ServiceLoader

class, to attempt to

locate and load

an implementation of the service using the specified

ClassLoader

.
If

classLoader

is null, the

default loading mechanism

will apply:
That is, the service-provider loading facility will use the

current thread's context class loader

to attempt to load the service. If the context class
loader is null, the

system class loader

will be used.
- Otherwise, throws a

FactoryConfigurationError

.

This method uses the following ordered lookup procedure to determine
the XMLOutputFactory implementation class to load:

- Use the value of the system property identified by

factoryId

.
- Use the configuration file "stax.properties". The file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. It contains the fully qualified
name of the implementation class with the key being the system property
defined above.

The stax.properties file is read only once by the implementation
and its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any property in stax.properties after it has been read for the first time.

Use the jaxp configuration file "jaxp.properties". The file is in the same
format as stax.properties and will only be read if stax.properties does
not exist.
- If

factoryId

is "javax.xml.stream.XMLOutputFactory",
use the service-provider loading facility, defined by the

ServiceLoader

class, to attempt to

locate and load

an implementation of the service using the specified

ClassLoader

.
If

classLoader

is null, the

default loading mechanism

will apply:
That is, the service-provider loading facility will use the

current thread's context class loader

to attempt to load the service. If the context class
loader is null, the

system class loader

will be used.
- Otherwise, throws a

FactoryConfigurationError

.

Use the value of the system property identified by

factoryId

.

Use the configuration file "stax.properties". The file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. It contains the fully qualified
name of the implementation class with the key being the system property
defined above.

The stax.properties file is read only once by the implementation
and its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any property in stax.properties after it has been read for the first time.

Use the jaxp configuration file "jaxp.properties". The file is in the same
format as stax.properties and will only be read if stax.properties does
not exist.

If

factoryId

is "javax.xml.stream.XMLOutputFactory",
use the service-provider loading facility, defined by the

ServiceLoader

class, to attempt to

locate and load

an implementation of the service using the specified

ClassLoader

.
If

classLoader

is null, the

default loading mechanism

will apply:
That is, the service-provider loading facility will use the

current thread's context class loader

to attempt to load the service. If the context class
loader is null, the

system class loader

will be used.

Otherwise, throws a

FactoryConfigurationError

.

Use the configuration file "stax.properties". The file is in standard

Properties

format and typically located in the

conf

directory of the Java installation. It contains the fully qualified
name of the implementation class with the key being the system property
defined above.

The stax.properties file is read only once by the implementation
and its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any property in stax.properties after it has been read for the first time.

Use the jaxp configuration file "jaxp.properties". The file is in the same
format as stax.properties and will only be read if stax.properties does
not exist.

The stax.properties file is read only once by the implementation
and its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any property in stax.properties after it has been read for the first time.

Use the jaxp configuration file "jaxp.properties". The file is in the same
format as stax.properties and will only be read if stax.properties does
not exist.

Use the jaxp configuration file "jaxp.properties". The file is in the same
format as stax.properties and will only be read if stax.properties does
not exist.

If

factoryId

is "javax.xml.stream.XMLOutputFactory",
use the service-provider loading facility, defined by the

ServiceLoader

class, to attempt to

locate and load

an implementation of the service using the specified

ClassLoader

.
If

classLoader

is null, the

default loading mechanism

will apply:
That is, the service-provider loading facility will use the

current thread's context class loader

to attempt to load the service. If the context class
loader is null, the

system class loader

will be used.

Otherwise, throws a

FactoryConfigurationError

.

Note that this is a new method that replaces the deprecated

newInstance(String factoryId, ClassLoader classLoader)

method.
The original method was incorrectly defined to return XMLInputFactory.

createXMLStreamWriter

```java
public abstract
XMLStreamWriter
createXMLStreamWriter​(
Writer
stream)
throws
XMLStreamException
```

Create a new XMLStreamWriter that writes to a writer

**Parameters:** stream

- the writer to write to
**Throws:** XMLStreamException

---

#### createXMLStreamWriter

public abstract

XMLStreamWriter

createXMLStreamWriter​(

Writer

stream)
throws

XMLStreamException

Create a new XMLStreamWriter that writes to a writer

createXMLStreamWriter

```java
public abstract
XMLStreamWriter
createXMLStreamWriter​(
OutputStream
stream)
throws
XMLStreamException
```

Create a new XMLStreamWriter that writes to a stream

**Parameters:** stream

- the stream to write to
**Throws:** XMLStreamException

---

#### createXMLStreamWriter

public abstract

XMLStreamWriter

createXMLStreamWriter​(

OutputStream

stream)
throws

XMLStreamException

Create a new XMLStreamWriter that writes to a stream

createXMLStreamWriter

```java
public abstract
XMLStreamWriter
createXMLStreamWriter​(
OutputStream
stream,

String
encoding)
throws
XMLStreamException
```

Create a new XMLStreamWriter that writes to a stream

**Parameters:** stream

- the stream to write to
**Parameters:** encoding

- the encoding to use
**Throws:** XMLStreamException

---

#### createXMLStreamWriter

public abstract

XMLStreamWriter

createXMLStreamWriter​(

OutputStream

stream,

String

encoding)
throws

XMLStreamException

Create a new XMLStreamWriter that writes to a stream

createXMLStreamWriter

```java
public abstract
XMLStreamWriter
createXMLStreamWriter​(
Result
result)
throws
XMLStreamException
```

Create a new XMLStreamWriter that writes to a JAXP result. This method is optional.

**Parameters:** result

- the result to write to
**Throws:** UnsupportedOperationException

- if this method is not
supported by this XMLOutputFactory
**Throws:** XMLStreamException

---

#### createXMLStreamWriter

public abstract

XMLStreamWriter

createXMLStreamWriter​(

Result

result)
throws

XMLStreamException

Create a new XMLStreamWriter that writes to a JAXP result. This method is optional.

createXMLEventWriter

```java
public abstract
XMLEventWriter
createXMLEventWriter​(
Result
result)
throws
XMLStreamException
```

Create a new XMLEventWriter that writes to a JAXP result. This method is optional.

**Parameters:** result

- the result to write to
**Throws:** UnsupportedOperationException

- if this method is not
supported by this XMLOutputFactory
**Throws:** XMLStreamException

---

#### createXMLEventWriter

public abstract

XMLEventWriter

createXMLEventWriter​(

Result

result)
throws

XMLStreamException

Create a new XMLEventWriter that writes to a JAXP result. This method is optional.

createXMLEventWriter

```java
public abstract
XMLEventWriter
createXMLEventWriter​(
OutputStream
stream)
throws
XMLStreamException
```

Create a new XMLEventWriter that writes to a stream

**Parameters:** stream

- the stream to write to
**Throws:** XMLStreamException

---

#### createXMLEventWriter

public abstract

XMLEventWriter

createXMLEventWriter​(

OutputStream

stream)
throws

XMLStreamException

Create a new XMLEventWriter that writes to a stream

createXMLEventWriter

```java
public abstract
XMLEventWriter
createXMLEventWriter​(
OutputStream
stream,

String
encoding)
throws
XMLStreamException
```

Create a new XMLEventWriter that writes to a stream

**Parameters:** stream

- the stream to write to
**Parameters:** encoding

- the encoding to use
**Throws:** XMLStreamException

---

#### createXMLEventWriter

public abstract

XMLEventWriter

createXMLEventWriter​(

OutputStream

stream,

String

encoding)
throws

XMLStreamException

Create a new XMLEventWriter that writes to a stream

createXMLEventWriter

```java
public abstract
XMLEventWriter
createXMLEventWriter​(
Writer
stream)
throws
XMLStreamException
```

Create a new XMLEventWriter that writes to a writer

**Parameters:** stream

- the stream to write to
**Throws:** XMLStreamException

---

#### createXMLEventWriter

public abstract

XMLEventWriter

createXMLEventWriter​(

Writer

stream)
throws

XMLStreamException

Create a new XMLEventWriter that writes to a writer

setProperty

```java
public abstract void setProperty​(
String
name,

Object
value)
throws
IllegalArgumentException
```

Allows the user to set specific features/properties on the underlying implementation.

**Parameters:** name

- The name of the property
**Parameters:** value

- The value of the property
**Throws:** IllegalArgumentException

- if the property is not supported

---

#### setProperty

public abstract void setProperty​(

String

name,

Object

value)
throws

IllegalArgumentException

Allows the user to set specific features/properties on the underlying implementation.

getProperty

```java
public abstract
Object
getProperty​(
String
name)
throws
IllegalArgumentException
```

Get a feature/property on the underlying implementation

**Parameters:** name

- The name of the property
**Returns:** The value of the property
**Throws:** IllegalArgumentException

- if the property is not supported

---

#### getProperty

public abstract

Object

getProperty​(

String

name)
throws

IllegalArgumentException

Get a feature/property on the underlying implementation

isPropertySupported

```java
public abstract boolean isPropertySupported​(
String
name)
```

Query the set of properties that this factory supports.

**Parameters:** name

- The name of the property (may not be null)
**Returns:** true if the property is supported and false otherwise

---

#### isPropertySupported

public abstract boolean isPropertySupported​(

String

name)

Query the set of properties that this factory supports.

---

