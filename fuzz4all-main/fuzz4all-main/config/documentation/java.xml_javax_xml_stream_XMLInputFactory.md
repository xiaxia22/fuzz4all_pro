# Class XMLInputFactory

**Source:** `java.xml\javax\xml\stream\XMLInputFactory.html`

### Class Description

```java
public abstract class
XMLInputFactory

extends
Object
```

Defines an abstract implementation of a factory for getting streams.

The following table defines the standard properties of this specification.
Each property varies in the level of support required by each implementation.
The level of support required is described in the 'Required' column.

Configuration Parameters

Property Name

Behavior

Return type

Default Value

Required

javax.xml.stream.isValidating

Turns on/off implementation specific DTD validation

Boolean

False

No

javax.xml.stream.isNamespaceAware

Turns on/off namespace processing for XML 1.0 support

Boolean

True

True (required) / False (optional)

javax.xml.stream.isCoalescing

Requires the processor to coalesce adjacent character data

Boolean

False

Yes

javax.xml.stream.isReplacingEntityReferences

replace internal entity references with their replacement text and report them as characters

Boolean

True

Yes

javax.xml.stream.isSupportingExternalEntities

Resolve external parsed entities

Boolean

Unspecified

Yes

javax.xml.stream.supportDTD

Use this property to request processors that do not support DTDs

Boolean

True

Yes

javax.xml.stream.reporter

sets/gets the impl of the XMLReporter

javax.xml.stream.XMLReporter

Null

Yes

javax.xml.stream.resolver

sets/gets the impl of the XMLResolver interface

javax.xml.stream.XMLResolver

Null

Yes

javax.xml.stream.allocator

sets/gets the impl of the XMLEventAllocator interface

javax.xml.stream.util.XMLEventAllocator

Null

Yes

**Since:** 1.6
**See Also:** XMLOutputFactory

,

XMLEventReader

,

XMLStreamReader

,

EventFilter

,

XMLReporter

,

XMLResolver

,

XMLEventAllocator

---

### Field Details

#### public static final
String
IS_NAMESPACE_AWARE

The property used to turn on/off namespace support,
this is to support XML 1.0 documents,
only the true setting must be supported

**See Also:**
- Constant Field Values

---

#### public static final
String
IS_VALIDATING

The property used to turn on/off implementation specific validation

**See Also:**
- Constant Field Values

---

#### public static final
String
IS_COALESCING

The property that requires the parser to coalesce adjacent character data sections

**See Also:**
- Constant Field Values

---

#### public static final
String
IS_REPLACING_ENTITY_REFERENCES

Requires the parser to replace internal
entity references with their replacement
text and report them as characters

**See Also:**
- Constant Field Values

---

#### public static final
String
IS_SUPPORTING_EXTERNAL_ENTITIES

The property that requires the parser to resolve external parsed entities

**See Also:**
- Constant Field Values

---

#### public static final
String
SUPPORT_DTD

The property that requires the parser to support DTDs

**See Also:**
- Constant Field Values

---

#### public static final
String
REPORTER

The property used to
set/get the implementation of the XMLReporter interface

**See Also:**
- Constant Field Values

---

#### public static final
String
RESOLVER

The property used to set/get the implementation of the XMLResolver

**See Also:**
- Constant Field Values

---

#### public static final
String
ALLOCATOR

The property used to set/get the implementation of the allocator

**See Also:**
- Constant Field Values

---

### Constructor Details

#### protected XMLInputFactory()

*No description found.*

---

### Method Details

#### public static
XMLInputFactory
newDefaultFactory()

Creates a new instance of the

XMLInputFactory

builtin
system-default implementation.

**Returns:**
- A new instance of the

XMLInputFactory

builtin
system-default implementation.

**Since:**
- 9

---

#### public static
XMLInputFactory
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
XMLInputFactory
newFactory()
throws
FactoryConfigurationError

Create a new instance of the factory.

This static method creates a new factory instance.
This method uses the following ordered lookup procedure to determine
the XMLInputFactory implementation class to load:

- Use the javax.xml.stream.XMLInputFactory system property.
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

Once an application has obtained a reference to a XMLInputFactory it
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

Create a new instance of the factory

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
XMLInputFactory
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
the XMLInputFactory implementation class to load:

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

is "javax.xml.stream.XMLInputFactory",
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

Note that this is a new method that replaces the deprecated

newInstance(String factoryId, ClassLoader classLoader)

method.
No changes in behavior are defined by this replacement method relative
to the deprecated method.

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
- FactoryConfigurationError

- if an instance of this factory cannot be loaded

**API Note:**
- The parameter factoryId defined here is inconsistent with that
of other JAXP factories where the first parameter is fully qualified
factory class name that provides implementation of the factory.

---

#### public abstract
XMLStreamReader
createXMLStreamReader​(
Reader
reader)
throws
XMLStreamException

Create a new XMLStreamReader from a reader

**Parameters:**
- reader

- the XML data to read from

**Throws:**
- XMLStreamException

---

#### public abstract
XMLStreamReader
createXMLStreamReader​(
Source
source)
throws
XMLStreamException

Create a new XMLStreamReader from a JAXP source. This method is optional.

**Parameters:**
- source

- the source to read from

**Throws:**
- UnsupportedOperationException

- if this method is not
supported by this XMLInputFactory
- XMLStreamException

---

#### public abstract
XMLStreamReader
createXMLStreamReader​(
InputStream
stream)
throws
XMLStreamException

Create a new XMLStreamReader from a java.io.InputStream

**Parameters:**
- stream

- the InputStream to read from

**Throws:**
- XMLStreamException

---

#### public abstract
XMLStreamReader
createXMLStreamReader​(
InputStream
stream,

String
encoding)
throws
XMLStreamException

Create a new XMLStreamReader from a java.io.InputStream

**Parameters:**
- stream

- the InputStream to read from
- encoding

- the character encoding of the stream

**Throws:**
- XMLStreamException

---

#### public abstract
XMLStreamReader
createXMLStreamReader​(
String
systemId,

InputStream
stream)
throws
XMLStreamException

Create a new XMLStreamReader from a java.io.InputStream

**Parameters:**
- systemId

- the system ID of the stream
- stream

- the InputStream to read from

**Throws:**
- XMLStreamException

---

#### public abstract
XMLStreamReader
createXMLStreamReader​(
String
systemId,

Reader
reader)
throws
XMLStreamException

Create a new XMLStreamReader from a java.io.InputStream

**Parameters:**
- systemId

- the system ID of the stream
- reader

- the InputStream to read from

**Throws:**
- XMLStreamException

---

#### public abstract
XMLEventReader
createXMLEventReader​(
Reader
reader)
throws
XMLStreamException

Create a new XMLEventReader from a reader

**Parameters:**
- reader

- the XML data to read from

**Throws:**
- XMLStreamException

---

#### public abstract
XMLEventReader
createXMLEventReader​(
String
systemId,

Reader
reader)
throws
XMLStreamException

Create a new XMLEventReader from a reader

**Parameters:**
- systemId

- the system ID of the input
- reader

- the XML data to read from

**Throws:**
- XMLStreamException

---

#### public abstract
XMLEventReader
createXMLEventReader​(
XMLStreamReader
reader)
throws
XMLStreamException

Create a new XMLEventReader from an XMLStreamReader. After being used
to construct the XMLEventReader instance returned from this method
the XMLStreamReader must not be used.

**Parameters:**
- reader

- the XMLStreamReader to read from (may not be modified)

**Returns:**
- a new XMLEventReader

**Throws:**
- XMLStreamException

---

#### public abstract
XMLEventReader
createXMLEventReader​(
Source
source)
throws
XMLStreamException

Create a new XMLEventReader from a JAXP source.
Support of this method is optional.

**Parameters:**
- source

- the source to read from

**Throws:**
- UnsupportedOperationException

- if this method is not
supported by this XMLInputFactory
- XMLStreamException

---

#### public abstract
XMLEventReader
createXMLEventReader​(
InputStream
stream)
throws
XMLStreamException

Create a new XMLEventReader from a java.io.InputStream

**Parameters:**
- stream

- the InputStream to read from

**Throws:**
- XMLStreamException

---

#### public abstract
XMLEventReader
createXMLEventReader​(
InputStream
stream,

String
encoding)
throws
XMLStreamException

Create a new XMLEventReader from a java.io.InputStream

**Parameters:**
- stream

- the InputStream to read from
- encoding

- the character encoding of the stream

**Throws:**
- XMLStreamException

---

#### public abstract
XMLEventReader
createXMLEventReader​(
String
systemId,

InputStream
stream)
throws
XMLStreamException

Create a new XMLEventReader from a java.io.InputStream

**Parameters:**
- systemId

- the system ID of the stream
- stream

- the InputStream to read from

**Throws:**
- XMLStreamException

---

#### public abstract
XMLStreamReader
createFilteredReader​(
XMLStreamReader
reader,

StreamFilter
filter)
throws
XMLStreamException

Create a filtered reader that wraps the filter around the reader

**Parameters:**
- reader

- the reader to filter
- filter

- the filter to apply to the reader

**Throws:**
- XMLStreamException

---

#### public abstract
XMLEventReader
createFilteredReader​(
XMLEventReader
reader,

EventFilter
filter)
throws
XMLStreamException

Create a filtered event reader that wraps the filter around the event reader

**Parameters:**
- reader

- the event reader to wrap
- filter

- the filter to apply to the event reader

**Throws:**
- XMLStreamException

---

#### public abstract
XMLResolver
getXMLResolver()

The resolver that will be set on any XMLStreamReader or XMLEventReader created
by this factory instance.

---

#### public abstract void setXMLResolver​(
XMLResolver
resolver)

The resolver that will be set on any XMLStreamReader or XMLEventReader created
by this factory instance.

**Parameters:**
- resolver

- the resolver to use to resolve references

---

#### public abstract
XMLReporter
getXMLReporter()

The reporter that will be set on any XMLStreamReader or XMLEventReader created
by this factory instance.

---

#### public abstract void setXMLReporter​(
XMLReporter
reporter)

The reporter that will be set on any XMLStreamReader or XMLEventReader created
by this factory instance.

**Parameters:**
- reporter

- the resolver to use to report non fatal errors

---

#### public abstract void setProperty​(
String
name,

Object
value)
throws
IllegalArgumentException

Allows the user to set specific feature/property on the underlying
implementation. The underlying implementation is not required to support
every setting of every property in the specification and may use
IllegalArgumentException to signal that an unsupported property may not be
set with the specified value.

All implementations that implement JAXP 1.5 or newer are required to
support the

XMLConstants.ACCESS_EXTERNAL_DTD

property.

- Access to external DTDs, external Entity References is restricted to the
protocols specified by the property. If access is denied during parsing
due to the restriction of this property,

XMLStreamException

will be thrown by the

XMLStreamReader.next()

or

XMLEventReader.nextEvent()

method.

**Parameters:**
- name

- The name of the property (may not be null)
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

Get the value of a feature/property from the underlying implementation

**Parameters:**
- name

- The name of the property (may not be null)

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

#### public abstract void setEventAllocator​(
XMLEventAllocator
allocator)

Set a user defined event allocator for events

**Parameters:**
- allocator

- the user defined allocator

---

#### public abstract
XMLEventAllocator
getEventAllocator()

Gets the allocator used by streams created with this factory

---

### Additional Sections

#### Class XMLInputFactory

java.lang.Object

- javax.xml.stream.XMLInputFactory

javax.xml.stream.XMLInputFactory

```java
public abstract class
XMLInputFactory

extends
Object
```

Defines an abstract implementation of a factory for getting streams.

The following table defines the standard properties of this specification.
Each property varies in the level of support required by each implementation.
The level of support required is described in the 'Required' column.

Configuration Parameters

Property Name

Behavior

Return type

Default Value

Required

javax.xml.stream.isValidating

Turns on/off implementation specific DTD validation

Boolean

False

No

javax.xml.stream.isNamespaceAware

Turns on/off namespace processing for XML 1.0 support

Boolean

True

True (required) / False (optional)

javax.xml.stream.isCoalescing

Requires the processor to coalesce adjacent character data

Boolean

False

Yes

javax.xml.stream.isReplacingEntityReferences

replace internal entity references with their replacement text and report them as characters

Boolean

True

Yes

javax.xml.stream.isSupportingExternalEntities

Resolve external parsed entities

Boolean

Unspecified

Yes

javax.xml.stream.supportDTD

Use this property to request processors that do not support DTDs

Boolean

True

Yes

javax.xml.stream.reporter

sets/gets the impl of the XMLReporter

javax.xml.stream.XMLReporter

Null

Yes

javax.xml.stream.resolver

sets/gets the impl of the XMLResolver interface

javax.xml.stream.XMLResolver

Null

Yes

javax.xml.stream.allocator

sets/gets the impl of the XMLEventAllocator interface

javax.xml.stream.util.XMLEventAllocator

Null

Yes

**Since:** 1.6
**See Also:** XMLOutputFactory

,

XMLEventReader

,

XMLStreamReader

,

EventFilter

,

XMLReporter

,

XMLResolver

,

XMLEventAllocator

public abstract class

XMLInputFactory

extends

Object

Defines an abstract implementation of a factory for getting streams.

The following table defines the standard properties of this specification.
Each property varies in the level of support required by each implementation.
The level of support required is described in the 'Required' column.

Configuration Parameters

Property Name

Behavior

Return type

Default Value

Required

javax.xml.stream.isValidating

Turns on/off implementation specific DTD validation

Boolean

False

No

javax.xml.stream.isNamespaceAware

Turns on/off namespace processing for XML 1.0 support

Boolean

True

True (required) / False (optional)

javax.xml.stream.isCoalescing

Requires the processor to coalesce adjacent character data

Boolean

False

Yes

javax.xml.stream.isReplacingEntityReferences

replace internal entity references with their replacement text and report them as characters

Boolean

True

Yes

javax.xml.stream.isSupportingExternalEntities

Resolve external parsed entities

Boolean

Unspecified

Yes

javax.xml.stream.supportDTD

Use this property to request processors that do not support DTDs

Boolean

True

Yes

javax.xml.stream.reporter

sets/gets the impl of the XMLReporter

javax.xml.stream.XMLReporter

Null

Yes

javax.xml.stream.resolver

sets/gets the impl of the XMLResolver interface

javax.xml.stream.XMLResolver

Null

Yes

javax.xml.stream.allocator

sets/gets the impl of the XMLEventAllocator interface

javax.xml.stream.util.XMLEventAllocator

Null

Yes

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

ALLOCATOR

The property used to set/get the implementation of the allocator

static

String

IS_COALESCING

The property that requires the parser to coalesce adjacent character data sections

static

String

IS_NAMESPACE_AWARE

The property used to turn on/off namespace support,
this is to support XML 1.0 documents,
only the true setting must be supported

static

String

IS_REPLACING_ENTITY_REFERENCES

Requires the parser to replace internal
entity references with their replacement
text and report them as characters

static

String

IS_SUPPORTING_EXTERNAL_ENTITIES

The property that requires the parser to resolve external parsed entities

static

String

IS_VALIDATING

The property used to turn on/off implementation specific validation

static

String

REPORTER

The property used to
set/get the implementation of the XMLReporter interface

static

String

RESOLVER

The property used to set/get the implementation of the XMLResolver

static

String

SUPPORT_DTD

The property that requires the parser to support DTDs

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

XMLInputFactory

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

XMLEventReader

createFilteredReader

​(

XMLEventReader

reader,

EventFilter

filter)

Create a filtered event reader that wraps the filter around the event reader

abstract

XMLStreamReader

createFilteredReader

​(

XMLStreamReader

reader,

StreamFilter

filter)

Create a filtered reader that wraps the filter around the reader

abstract

XMLEventReader

createXMLEventReader

​(

InputStream

stream)

Create a new XMLEventReader from a java.io.InputStream

abstract

XMLEventReader

createXMLEventReader

​(

InputStream

stream,

String

encoding)

Create a new XMLEventReader from a java.io.InputStream

abstract

XMLEventReader

createXMLEventReader

​(

Reader

reader)

Create a new XMLEventReader from a reader

abstract

XMLEventReader

createXMLEventReader

​(

String

systemId,

InputStream

stream)

Create a new XMLEventReader from a java.io.InputStream

abstract

XMLEventReader

createXMLEventReader

​(

String

systemId,

Reader

reader)

Create a new XMLEventReader from a reader

abstract

XMLEventReader

createXMLEventReader

​(

XMLStreamReader

reader)

Create a new XMLEventReader from an XMLStreamReader.

abstract

XMLEventReader

createXMLEventReader

​(

Source

source)

Create a new XMLEventReader from a JAXP source.

abstract

XMLStreamReader

createXMLStreamReader

​(

InputStream

stream)

Create a new XMLStreamReader from a java.io.InputStream

abstract

XMLStreamReader

createXMLStreamReader

​(

InputStream

stream,

String

encoding)

Create a new XMLStreamReader from a java.io.InputStream

abstract

XMLStreamReader

createXMLStreamReader

​(

Reader

reader)

Create a new XMLStreamReader from a reader

abstract

XMLStreamReader

createXMLStreamReader

​(

String

systemId,

InputStream

stream)

Create a new XMLStreamReader from a java.io.InputStream

abstract

XMLStreamReader

createXMLStreamReader

​(

String

systemId,

Reader

reader)

Create a new XMLStreamReader from a java.io.InputStream

abstract

XMLStreamReader

createXMLStreamReader

​(

Source

source)

Create a new XMLStreamReader from a JAXP source.

abstract

XMLEventAllocator

getEventAllocator

()

Gets the allocator used by streams created with this factory

abstract

Object

getProperty

​(

String

name)

Get the value of a feature/property from the underlying implementation

abstract

XMLReporter

getXMLReporter

()

The reporter that will be set on any XMLStreamReader or XMLEventReader created
by this factory instance.

abstract

XMLResolver

getXMLResolver

()

The resolver that will be set on any XMLStreamReader or XMLEventReader created
by this factory instance.

abstract boolean

isPropertySupported

​(

String

name)

Query the set of properties that this factory supports.

static

XMLInputFactory

newDefaultFactory

()

Creates a new instance of the

XMLInputFactory

builtin
system-default implementation.

static

XMLInputFactory

newFactory

()

Create a new instance of the factory.

static

XMLInputFactory

newFactory

​(

String

factoryId,

ClassLoader

classLoader)

Create a new instance of the factory.

static

XMLInputFactory

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

This method has been deprecated to maintain API consistency.

abstract void

setEventAllocator

​(

XMLEventAllocator

allocator)

Set a user defined event allocator for events

abstract void

setProperty

​(

String

name,

Object

value)

Allows the user to set specific feature/property on the underlying
implementation.

abstract void

setXMLReporter

​(

XMLReporter

reporter)

The reporter that will be set on any XMLStreamReader or XMLEventReader created
by this factory instance.

abstract void

setXMLResolver

​(

XMLResolver

resolver)

The resolver that will be set on any XMLStreamReader or XMLEventReader created
by this factory instance.

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

ALLOCATOR

The property used to set/get the implementation of the allocator

static

String

IS_COALESCING

The property that requires the parser to coalesce adjacent character data sections

static

String

IS_NAMESPACE_AWARE

The property used to turn on/off namespace support,
this is to support XML 1.0 documents,
only the true setting must be supported

static

String

IS_REPLACING_ENTITY_REFERENCES

Requires the parser to replace internal
entity references with their replacement
text and report them as characters

static

String

IS_SUPPORTING_EXTERNAL_ENTITIES

The property that requires the parser to resolve external parsed entities

static

String

IS_VALIDATING

The property used to turn on/off implementation specific validation

static

String

REPORTER

The property used to
set/get the implementation of the XMLReporter interface

static

String

RESOLVER

The property used to set/get the implementation of the XMLResolver

static

String

SUPPORT_DTD

The property that requires the parser to support DTDs

---

#### Field Summary

The property used to set/get the implementation of the allocator

The property that requires the parser to coalesce adjacent character data sections

The property used to turn on/off namespace support,
this is to support XML 1.0 documents,
only the true setting must be supported

Requires the parser to replace internal
entity references with their replacement
text and report them as characters

The property that requires the parser to resolve external parsed entities

The property used to turn on/off implementation specific validation

The property used to
set/get the implementation of the XMLReporter interface

The property used to set/get the implementation of the XMLResolver

The property that requires the parser to support DTDs

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

XMLInputFactory

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

XMLEventReader

createFilteredReader

​(

XMLEventReader

reader,

EventFilter

filter)

Create a filtered event reader that wraps the filter around the event reader

abstract

XMLStreamReader

createFilteredReader

​(

XMLStreamReader

reader,

StreamFilter

filter)

Create a filtered reader that wraps the filter around the reader

abstract

XMLEventReader

createXMLEventReader

​(

InputStream

stream)

Create a new XMLEventReader from a java.io.InputStream

abstract

XMLEventReader

createXMLEventReader

​(

InputStream

stream,

String

encoding)

Create a new XMLEventReader from a java.io.InputStream

abstract

XMLEventReader

createXMLEventReader

​(

Reader

reader)

Create a new XMLEventReader from a reader

abstract

XMLEventReader

createXMLEventReader

​(

String

systemId,

InputStream

stream)

Create a new XMLEventReader from a java.io.InputStream

abstract

XMLEventReader

createXMLEventReader

​(

String

systemId,

Reader

reader)

Create a new XMLEventReader from a reader

abstract

XMLEventReader

createXMLEventReader

​(

XMLStreamReader

reader)

Create a new XMLEventReader from an XMLStreamReader.

abstract

XMLEventReader

createXMLEventReader

​(

Source

source)

Create a new XMLEventReader from a JAXP source.

abstract

XMLStreamReader

createXMLStreamReader

​(

InputStream

stream)

Create a new XMLStreamReader from a java.io.InputStream

abstract

XMLStreamReader

createXMLStreamReader

​(

InputStream

stream,

String

encoding)

Create a new XMLStreamReader from a java.io.InputStream

abstract

XMLStreamReader

createXMLStreamReader

​(

Reader

reader)

Create a new XMLStreamReader from a reader

abstract

XMLStreamReader

createXMLStreamReader

​(

String

systemId,

InputStream

stream)

Create a new XMLStreamReader from a java.io.InputStream

abstract

XMLStreamReader

createXMLStreamReader

​(

String

systemId,

Reader

reader)

Create a new XMLStreamReader from a java.io.InputStream

abstract

XMLStreamReader

createXMLStreamReader

​(

Source

source)

Create a new XMLStreamReader from a JAXP source.

abstract

XMLEventAllocator

getEventAllocator

()

Gets the allocator used by streams created with this factory

abstract

Object

getProperty

​(

String

name)

Get the value of a feature/property from the underlying implementation

abstract

XMLReporter

getXMLReporter

()

The reporter that will be set on any XMLStreamReader or XMLEventReader created
by this factory instance.

abstract

XMLResolver

getXMLResolver

()

The resolver that will be set on any XMLStreamReader or XMLEventReader created
by this factory instance.

abstract boolean

isPropertySupported

​(

String

name)

Query the set of properties that this factory supports.

static

XMLInputFactory

newDefaultFactory

()

Creates a new instance of the

XMLInputFactory

builtin
system-default implementation.

static

XMLInputFactory

newFactory

()

Create a new instance of the factory.

static

XMLInputFactory

newFactory

​(

String

factoryId,

ClassLoader

classLoader)

Create a new instance of the factory.

static

XMLInputFactory

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

This method has been deprecated to maintain API consistency.

abstract void

setEventAllocator

​(

XMLEventAllocator

allocator)

Set a user defined event allocator for events

abstract void

setProperty

​(

String

name,

Object

value)

Allows the user to set specific feature/property on the underlying
implementation.

abstract void

setXMLReporter

​(

XMLReporter

reporter)

The reporter that will be set on any XMLStreamReader or XMLEventReader created
by this factory instance.

abstract void

setXMLResolver

​(

XMLResolver

resolver)

The resolver that will be set on any XMLStreamReader or XMLEventReader created
by this factory instance.

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

Create a filtered event reader that wraps the filter around the event reader

Create a filtered reader that wraps the filter around the reader

Create a new XMLEventReader from a java.io.InputStream

Create a new XMLEventReader from a reader

Create a new XMLEventReader from an XMLStreamReader.

Create a new XMLEventReader from a JAXP source.

Create a new XMLStreamReader from a java.io.InputStream

Create a new XMLStreamReader from a reader

Create a new XMLStreamReader from a JAXP source.

Gets the allocator used by streams created with this factory

Get the value of a feature/property from the underlying implementation

The reporter that will be set on any XMLStreamReader or XMLEventReader created
by this factory instance.

The resolver that will be set on any XMLStreamReader or XMLEventReader created
by this factory instance.

Query the set of properties that this factory supports.

Creates a new instance of the

XMLInputFactory

builtin
system-default implementation.

Create a new instance of the factory.

Creates a new instance of the factory in exactly the same manner as the

newFactory()

method.

Deprecated.

This method has been deprecated to maintain API consistency.

Set a user defined event allocator for events

Allows the user to set specific feature/property on the underlying
implementation.

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

- IS_NAMESPACE_AWARE

```java
public static final
String
IS_NAMESPACE_AWARE
```

The property used to turn on/off namespace support,
this is to support XML 1.0 documents,
only the true setting must be supported

**See Also:** Constant Field Values

- IS_VALIDATING

```java
public static final
String
IS_VALIDATING
```

The property used to turn on/off implementation specific validation

**See Also:** Constant Field Values

- IS_COALESCING

```java
public static final
String
IS_COALESCING
```

The property that requires the parser to coalesce adjacent character data sections

**See Also:** Constant Field Values

- IS_REPLACING_ENTITY_REFERENCES

```java
public static final
String
IS_REPLACING_ENTITY_REFERENCES
```

Requires the parser to replace internal
entity references with their replacement
text and report them as characters

**See Also:** Constant Field Values

- IS_SUPPORTING_EXTERNAL_ENTITIES

```java
public static final
String
IS_SUPPORTING_EXTERNAL_ENTITIES
```

The property that requires the parser to resolve external parsed entities

**See Also:** Constant Field Values

- SUPPORT_DTD

```java
public static final
String
SUPPORT_DTD
```

The property that requires the parser to support DTDs

**See Also:** Constant Field Values

- REPORTER

```java
public static final
String
REPORTER
```

The property used to
set/get the implementation of the XMLReporter interface

**See Also:** Constant Field Values

- RESOLVER

```java
public static final
String
RESOLVER
```

The property used to set/get the implementation of the XMLResolver

**See Also:** Constant Field Values

- ALLOCATOR

```java
public static final
String
ALLOCATOR
```

The property used to set/get the implementation of the allocator

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- XMLInputFactory

```java
protected XMLInputFactory()
```

============ METHOD DETAIL ==========

- Method Detail

- newDefaultFactory

```java
public static
XMLInputFactory
newDefaultFactory()
```

Creates a new instance of the

XMLInputFactory

builtin
system-default implementation.

**Returns:** A new instance of the

XMLInputFactory

builtin
system-default implementation.
**Since:** 9

- newInstance

```java
public static
XMLInputFactory
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
XMLInputFactory
newFactory()
throws
FactoryConfigurationError
```

Create a new instance of the factory.

This static method creates a new factory instance.
This method uses the following ordered lookup procedure to determine
the XMLInputFactory implementation class to load:

- Use the javax.xml.stream.XMLInputFactory system property.
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

Once an application has obtained a reference to a XMLInputFactory it
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

This method has been deprecated to maintain API consistency.
All newInstance methods have been replaced with corresponding
newFactory methods. The replacement

newFactory(java.lang.String, java.lang.ClassLoader)

method
defines no changes in behavior.

Create a new instance of the factory

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
XMLInputFactory
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
the XMLInputFactory implementation class to load:

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

is "javax.xml.stream.XMLInputFactory",
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

Note that this is a new method that replaces the deprecated

newInstance(String factoryId, ClassLoader classLoader)

method.
No changes in behavior are defined by this replacement method relative
to the deprecated method.

**API Note:** The parameter factoryId defined here is inconsistent with that
of other JAXP factories where the first parameter is fully qualified
factory class name that provides implementation of the factory.
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
**Throws:** FactoryConfigurationError

- if an instance of this factory cannot be loaded

- createXMLStreamReader

```java
public abstract
XMLStreamReader
createXMLStreamReader​(
Reader
reader)
throws
XMLStreamException
```

Create a new XMLStreamReader from a reader

**Parameters:** reader

- the XML data to read from
**Throws:** XMLStreamException

- createXMLStreamReader

```java
public abstract
XMLStreamReader
createXMLStreamReader​(
Source
source)
throws
XMLStreamException
```

Create a new XMLStreamReader from a JAXP source. This method is optional.

**Parameters:** source

- the source to read from
**Throws:** UnsupportedOperationException

- if this method is not
supported by this XMLInputFactory
**Throws:** XMLStreamException

- createXMLStreamReader

```java
public abstract
XMLStreamReader
createXMLStreamReader​(
InputStream
stream)
throws
XMLStreamException
```

Create a new XMLStreamReader from a java.io.InputStream

**Parameters:** stream

- the InputStream to read from
**Throws:** XMLStreamException

- createXMLStreamReader

```java
public abstract
XMLStreamReader
createXMLStreamReader​(
InputStream
stream,

String
encoding)
throws
XMLStreamException
```

Create a new XMLStreamReader from a java.io.InputStream

**Parameters:** stream

- the InputStream to read from
**Parameters:** encoding

- the character encoding of the stream
**Throws:** XMLStreamException

- createXMLStreamReader

```java
public abstract
XMLStreamReader
createXMLStreamReader​(
String
systemId,

InputStream
stream)
throws
XMLStreamException
```

Create a new XMLStreamReader from a java.io.InputStream

**Parameters:** systemId

- the system ID of the stream
**Parameters:** stream

- the InputStream to read from
**Throws:** XMLStreamException

- createXMLStreamReader

```java
public abstract
XMLStreamReader
createXMLStreamReader​(
String
systemId,

Reader
reader)
throws
XMLStreamException
```

Create a new XMLStreamReader from a java.io.InputStream

**Parameters:** systemId

- the system ID of the stream
**Parameters:** reader

- the InputStream to read from
**Throws:** XMLStreamException

- createXMLEventReader

```java
public abstract
XMLEventReader
createXMLEventReader​(
Reader
reader)
throws
XMLStreamException
```

Create a new XMLEventReader from a reader

**Parameters:** reader

- the XML data to read from
**Throws:** XMLStreamException

- createXMLEventReader

```java
public abstract
XMLEventReader
createXMLEventReader​(
String
systemId,

Reader
reader)
throws
XMLStreamException
```

Create a new XMLEventReader from a reader

**Parameters:** systemId

- the system ID of the input
**Parameters:** reader

- the XML data to read from
**Throws:** XMLStreamException

- createXMLEventReader

```java
public abstract
XMLEventReader
createXMLEventReader​(
XMLStreamReader
reader)
throws
XMLStreamException
```

Create a new XMLEventReader from an XMLStreamReader. After being used
to construct the XMLEventReader instance returned from this method
the XMLStreamReader must not be used.

**Parameters:** reader

- the XMLStreamReader to read from (may not be modified)
**Returns:** a new XMLEventReader
**Throws:** XMLStreamException

- createXMLEventReader

```java
public abstract
XMLEventReader
createXMLEventReader​(
Source
source)
throws
XMLStreamException
```

Create a new XMLEventReader from a JAXP source.
Support of this method is optional.

**Parameters:** source

- the source to read from
**Throws:** UnsupportedOperationException

- if this method is not
supported by this XMLInputFactory
**Throws:** XMLStreamException

- createXMLEventReader

```java
public abstract
XMLEventReader
createXMLEventReader​(
InputStream
stream)
throws
XMLStreamException
```

Create a new XMLEventReader from a java.io.InputStream

**Parameters:** stream

- the InputStream to read from
**Throws:** XMLStreamException

- createXMLEventReader

```java
public abstract
XMLEventReader
createXMLEventReader​(
InputStream
stream,

String
encoding)
throws
XMLStreamException
```

Create a new XMLEventReader from a java.io.InputStream

**Parameters:** stream

- the InputStream to read from
**Parameters:** encoding

- the character encoding of the stream
**Throws:** XMLStreamException

- createXMLEventReader

```java
public abstract
XMLEventReader
createXMLEventReader​(
String
systemId,

InputStream
stream)
throws
XMLStreamException
```

Create a new XMLEventReader from a java.io.InputStream

**Parameters:** systemId

- the system ID of the stream
**Parameters:** stream

- the InputStream to read from
**Throws:** XMLStreamException

- createFilteredReader

```java
public abstract
XMLStreamReader
createFilteredReader​(
XMLStreamReader
reader,

StreamFilter
filter)
throws
XMLStreamException
```

Create a filtered reader that wraps the filter around the reader

**Parameters:** reader

- the reader to filter
**Parameters:** filter

- the filter to apply to the reader
**Throws:** XMLStreamException

- createFilteredReader

```java
public abstract
XMLEventReader
createFilteredReader​(
XMLEventReader
reader,

EventFilter
filter)
throws
XMLStreamException
```

Create a filtered event reader that wraps the filter around the event reader

**Parameters:** reader

- the event reader to wrap
**Parameters:** filter

- the filter to apply to the event reader
**Throws:** XMLStreamException

- getXMLResolver

```java
public abstract
XMLResolver
getXMLResolver()
```

The resolver that will be set on any XMLStreamReader or XMLEventReader created
by this factory instance.

- setXMLResolver

```java
public abstract void setXMLResolver​(
XMLResolver
resolver)
```

The resolver that will be set on any XMLStreamReader or XMLEventReader created
by this factory instance.

**Parameters:** resolver

- the resolver to use to resolve references

- getXMLReporter

```java
public abstract
XMLReporter
getXMLReporter()
```

The reporter that will be set on any XMLStreamReader or XMLEventReader created
by this factory instance.

- setXMLReporter

```java
public abstract void setXMLReporter​(
XMLReporter
reporter)
```

The reporter that will be set on any XMLStreamReader or XMLEventReader created
by this factory instance.

**Parameters:** reporter

- the resolver to use to report non fatal errors

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

Allows the user to set specific feature/property on the underlying
implementation. The underlying implementation is not required to support
every setting of every property in the specification and may use
IllegalArgumentException to signal that an unsupported property may not be
set with the specified value.

All implementations that implement JAXP 1.5 or newer are required to
support the

XMLConstants.ACCESS_EXTERNAL_DTD

property.

- Access to external DTDs, external Entity References is restricted to the
protocols specified by the property. If access is denied during parsing
due to the restriction of this property,

XMLStreamException

will be thrown by the

XMLStreamReader.next()

or

XMLEventReader.nextEvent()

method.

**Parameters:** name

- The name of the property (may not be null)
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

Get the value of a feature/property from the underlying implementation

**Parameters:** name

- The name of the property (may not be null)
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

- setEventAllocator

```java
public abstract void setEventAllocator​(
XMLEventAllocator
allocator)
```

Set a user defined event allocator for events

**Parameters:** allocator

- the user defined allocator

- getEventAllocator

```java
public abstract
XMLEventAllocator
getEventAllocator()
```

Gets the allocator used by streams created with this factory

Field Detail

- IS_NAMESPACE_AWARE

```java
public static final
String
IS_NAMESPACE_AWARE
```

The property used to turn on/off namespace support,
this is to support XML 1.0 documents,
only the true setting must be supported

**See Also:** Constant Field Values

- IS_VALIDATING

```java
public static final
String
IS_VALIDATING
```

The property used to turn on/off implementation specific validation

**See Also:** Constant Field Values

- IS_COALESCING

```java
public static final
String
IS_COALESCING
```

The property that requires the parser to coalesce adjacent character data sections

**See Also:** Constant Field Values

- IS_REPLACING_ENTITY_REFERENCES

```java
public static final
String
IS_REPLACING_ENTITY_REFERENCES
```

Requires the parser to replace internal
entity references with their replacement
text and report them as characters

**See Also:** Constant Field Values

- IS_SUPPORTING_EXTERNAL_ENTITIES

```java
public static final
String
IS_SUPPORTING_EXTERNAL_ENTITIES
```

The property that requires the parser to resolve external parsed entities

**See Also:** Constant Field Values

- SUPPORT_DTD

```java
public static final
String
SUPPORT_DTD
```

The property that requires the parser to support DTDs

**See Also:** Constant Field Values

- REPORTER

```java
public static final
String
REPORTER
```

The property used to
set/get the implementation of the XMLReporter interface

**See Also:** Constant Field Values

- RESOLVER

```java
public static final
String
RESOLVER
```

The property used to set/get the implementation of the XMLResolver

**See Also:** Constant Field Values

- ALLOCATOR

```java
public static final
String
ALLOCATOR
```

The property used to set/get the implementation of the allocator

**See Also:** Constant Field Values

---

#### Field Detail

IS_NAMESPACE_AWARE

```java
public static final
String
IS_NAMESPACE_AWARE
```

The property used to turn on/off namespace support,
this is to support XML 1.0 documents,
only the true setting must be supported

**See Also:** Constant Field Values

---

#### IS_NAMESPACE_AWARE

public static final

String

IS_NAMESPACE_AWARE

The property used to turn on/off namespace support,
this is to support XML 1.0 documents,
only the true setting must be supported

IS_VALIDATING

```java
public static final
String
IS_VALIDATING
```

The property used to turn on/off implementation specific validation

**See Also:** Constant Field Values

---

#### IS_VALIDATING

public static final

String

IS_VALIDATING

The property used to turn on/off implementation specific validation

IS_COALESCING

```java
public static final
String
IS_COALESCING
```

The property that requires the parser to coalesce adjacent character data sections

**See Also:** Constant Field Values

---

#### IS_COALESCING

public static final

String

IS_COALESCING

The property that requires the parser to coalesce adjacent character data sections

IS_REPLACING_ENTITY_REFERENCES

```java
public static final
String
IS_REPLACING_ENTITY_REFERENCES
```

Requires the parser to replace internal
entity references with their replacement
text and report them as characters

**See Also:** Constant Field Values

---

#### IS_REPLACING_ENTITY_REFERENCES

public static final

String

IS_REPLACING_ENTITY_REFERENCES

Requires the parser to replace internal
entity references with their replacement
text and report them as characters

IS_SUPPORTING_EXTERNAL_ENTITIES

```java
public static final
String
IS_SUPPORTING_EXTERNAL_ENTITIES
```

The property that requires the parser to resolve external parsed entities

**See Also:** Constant Field Values

---

#### IS_SUPPORTING_EXTERNAL_ENTITIES

public static final

String

IS_SUPPORTING_EXTERNAL_ENTITIES

The property that requires the parser to resolve external parsed entities

SUPPORT_DTD

```java
public static final
String
SUPPORT_DTD
```

The property that requires the parser to support DTDs

**See Also:** Constant Field Values

---

#### SUPPORT_DTD

public static final

String

SUPPORT_DTD

The property that requires the parser to support DTDs

REPORTER

```java
public static final
String
REPORTER
```

The property used to
set/get the implementation of the XMLReporter interface

**See Also:** Constant Field Values

---

#### REPORTER

public static final

String

REPORTER

The property used to
set/get the implementation of the XMLReporter interface

RESOLVER

```java
public static final
String
RESOLVER
```

The property used to set/get the implementation of the XMLResolver

**See Also:** Constant Field Values

---

#### RESOLVER

public static final

String

RESOLVER

The property used to set/get the implementation of the XMLResolver

ALLOCATOR

```java
public static final
String
ALLOCATOR
```

The property used to set/get the implementation of the allocator

**See Also:** Constant Field Values

---

#### ALLOCATOR

public static final

String

ALLOCATOR

The property used to set/get the implementation of the allocator

Constructor Detail

- XMLInputFactory

```java
protected XMLInputFactory()
```

---

#### Constructor Detail

XMLInputFactory

```java
protected XMLInputFactory()
```

---

#### XMLInputFactory

protected XMLInputFactory()

Method Detail

- newDefaultFactory

```java
public static
XMLInputFactory
newDefaultFactory()
```

Creates a new instance of the

XMLInputFactory

builtin
system-default implementation.

**Returns:** A new instance of the

XMLInputFactory

builtin
system-default implementation.
**Since:** 9

- newInstance

```java
public static
XMLInputFactory
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
XMLInputFactory
newFactory()
throws
FactoryConfigurationError
```

Create a new instance of the factory.

This static method creates a new factory instance.
This method uses the following ordered lookup procedure to determine
the XMLInputFactory implementation class to load:

- Use the javax.xml.stream.XMLInputFactory system property.
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

Once an application has obtained a reference to a XMLInputFactory it
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

This method has been deprecated to maintain API consistency.
All newInstance methods have been replaced with corresponding
newFactory methods. The replacement

newFactory(java.lang.String, java.lang.ClassLoader)

method
defines no changes in behavior.

Create a new instance of the factory

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
XMLInputFactory
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
the XMLInputFactory implementation class to load:

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

is "javax.xml.stream.XMLInputFactory",
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

Note that this is a new method that replaces the deprecated

newInstance(String factoryId, ClassLoader classLoader)

method.
No changes in behavior are defined by this replacement method relative
to the deprecated method.

**API Note:** The parameter factoryId defined here is inconsistent with that
of other JAXP factories where the first parameter is fully qualified
factory class name that provides implementation of the factory.
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
**Throws:** FactoryConfigurationError

- if an instance of this factory cannot be loaded

- createXMLStreamReader

```java
public abstract
XMLStreamReader
createXMLStreamReader​(
Reader
reader)
throws
XMLStreamException
```

Create a new XMLStreamReader from a reader

**Parameters:** reader

- the XML data to read from
**Throws:** XMLStreamException

- createXMLStreamReader

```java
public abstract
XMLStreamReader
createXMLStreamReader​(
Source
source)
throws
XMLStreamException
```

Create a new XMLStreamReader from a JAXP source. This method is optional.

**Parameters:** source

- the source to read from
**Throws:** UnsupportedOperationException

- if this method is not
supported by this XMLInputFactory
**Throws:** XMLStreamException

- createXMLStreamReader

```java
public abstract
XMLStreamReader
createXMLStreamReader​(
InputStream
stream)
throws
XMLStreamException
```

Create a new XMLStreamReader from a java.io.InputStream

**Parameters:** stream

- the InputStream to read from
**Throws:** XMLStreamException

- createXMLStreamReader

```java
public abstract
XMLStreamReader
createXMLStreamReader​(
InputStream
stream,

String
encoding)
throws
XMLStreamException
```

Create a new XMLStreamReader from a java.io.InputStream

**Parameters:** stream

- the InputStream to read from
**Parameters:** encoding

- the character encoding of the stream
**Throws:** XMLStreamException

- createXMLStreamReader

```java
public abstract
XMLStreamReader
createXMLStreamReader​(
String
systemId,

InputStream
stream)
throws
XMLStreamException
```

Create a new XMLStreamReader from a java.io.InputStream

**Parameters:** systemId

- the system ID of the stream
**Parameters:** stream

- the InputStream to read from
**Throws:** XMLStreamException

- createXMLStreamReader

```java
public abstract
XMLStreamReader
createXMLStreamReader​(
String
systemId,

Reader
reader)
throws
XMLStreamException
```

Create a new XMLStreamReader from a java.io.InputStream

**Parameters:** systemId

- the system ID of the stream
**Parameters:** reader

- the InputStream to read from
**Throws:** XMLStreamException

- createXMLEventReader

```java
public abstract
XMLEventReader
createXMLEventReader​(
Reader
reader)
throws
XMLStreamException
```

Create a new XMLEventReader from a reader

**Parameters:** reader

- the XML data to read from
**Throws:** XMLStreamException

- createXMLEventReader

```java
public abstract
XMLEventReader
createXMLEventReader​(
String
systemId,

Reader
reader)
throws
XMLStreamException
```

Create a new XMLEventReader from a reader

**Parameters:** systemId

- the system ID of the input
**Parameters:** reader

- the XML data to read from
**Throws:** XMLStreamException

- createXMLEventReader

```java
public abstract
XMLEventReader
createXMLEventReader​(
XMLStreamReader
reader)
throws
XMLStreamException
```

Create a new XMLEventReader from an XMLStreamReader. After being used
to construct the XMLEventReader instance returned from this method
the XMLStreamReader must not be used.

**Parameters:** reader

- the XMLStreamReader to read from (may not be modified)
**Returns:** a new XMLEventReader
**Throws:** XMLStreamException

- createXMLEventReader

```java
public abstract
XMLEventReader
createXMLEventReader​(
Source
source)
throws
XMLStreamException
```

Create a new XMLEventReader from a JAXP source.
Support of this method is optional.

**Parameters:** source

- the source to read from
**Throws:** UnsupportedOperationException

- if this method is not
supported by this XMLInputFactory
**Throws:** XMLStreamException

- createXMLEventReader

```java
public abstract
XMLEventReader
createXMLEventReader​(
InputStream
stream)
throws
XMLStreamException
```

Create a new XMLEventReader from a java.io.InputStream

**Parameters:** stream

- the InputStream to read from
**Throws:** XMLStreamException

- createXMLEventReader

```java
public abstract
XMLEventReader
createXMLEventReader​(
InputStream
stream,

String
encoding)
throws
XMLStreamException
```

Create a new XMLEventReader from a java.io.InputStream

**Parameters:** stream

- the InputStream to read from
**Parameters:** encoding

- the character encoding of the stream
**Throws:** XMLStreamException

- createXMLEventReader

```java
public abstract
XMLEventReader
createXMLEventReader​(
String
systemId,

InputStream
stream)
throws
XMLStreamException
```

Create a new XMLEventReader from a java.io.InputStream

**Parameters:** systemId

- the system ID of the stream
**Parameters:** stream

- the InputStream to read from
**Throws:** XMLStreamException

- createFilteredReader

```java
public abstract
XMLStreamReader
createFilteredReader​(
XMLStreamReader
reader,

StreamFilter
filter)
throws
XMLStreamException
```

Create a filtered reader that wraps the filter around the reader

**Parameters:** reader

- the reader to filter
**Parameters:** filter

- the filter to apply to the reader
**Throws:** XMLStreamException

- createFilteredReader

```java
public abstract
XMLEventReader
createFilteredReader​(
XMLEventReader
reader,

EventFilter
filter)
throws
XMLStreamException
```

Create a filtered event reader that wraps the filter around the event reader

**Parameters:** reader

- the event reader to wrap
**Parameters:** filter

- the filter to apply to the event reader
**Throws:** XMLStreamException

- getXMLResolver

```java
public abstract
XMLResolver
getXMLResolver()
```

The resolver that will be set on any XMLStreamReader or XMLEventReader created
by this factory instance.

- setXMLResolver

```java
public abstract void setXMLResolver​(
XMLResolver
resolver)
```

The resolver that will be set on any XMLStreamReader or XMLEventReader created
by this factory instance.

**Parameters:** resolver

- the resolver to use to resolve references

- getXMLReporter

```java
public abstract
XMLReporter
getXMLReporter()
```

The reporter that will be set on any XMLStreamReader or XMLEventReader created
by this factory instance.

- setXMLReporter

```java
public abstract void setXMLReporter​(
XMLReporter
reporter)
```

The reporter that will be set on any XMLStreamReader or XMLEventReader created
by this factory instance.

**Parameters:** reporter

- the resolver to use to report non fatal errors

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

Allows the user to set specific feature/property on the underlying
implementation. The underlying implementation is not required to support
every setting of every property in the specification and may use
IllegalArgumentException to signal that an unsupported property may not be
set with the specified value.

All implementations that implement JAXP 1.5 or newer are required to
support the

XMLConstants.ACCESS_EXTERNAL_DTD

property.

- Access to external DTDs, external Entity References is restricted to the
protocols specified by the property. If access is denied during parsing
due to the restriction of this property,

XMLStreamException

will be thrown by the

XMLStreamReader.next()

or

XMLEventReader.nextEvent()

method.

**Parameters:** name

- The name of the property (may not be null)
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

Get the value of a feature/property from the underlying implementation

**Parameters:** name

- The name of the property (may not be null)
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

- setEventAllocator

```java
public abstract void setEventAllocator​(
XMLEventAllocator
allocator)
```

Set a user defined event allocator for events

**Parameters:** allocator

- the user defined allocator

- getEventAllocator

```java
public abstract
XMLEventAllocator
getEventAllocator()
```

Gets the allocator used by streams created with this factory

---

#### Method Detail

newDefaultFactory

```java
public static
XMLInputFactory
newDefaultFactory()
```

Creates a new instance of the

XMLInputFactory

builtin
system-default implementation.

**Returns:** A new instance of the

XMLInputFactory

builtin
system-default implementation.
**Since:** 9

---

#### newDefaultFactory

public static

XMLInputFactory

newDefaultFactory()

Creates a new instance of the

XMLInputFactory

builtin
system-default implementation.

newInstance

```java
public static
XMLInputFactory
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

XMLInputFactory

newInstance()
throws

FactoryConfigurationError

Creates a new instance of the factory in exactly the same manner as the

newFactory()

method.

newFactory

```java
public static
XMLInputFactory
newFactory()
throws
FactoryConfigurationError
```

Create a new instance of the factory.

This static method creates a new factory instance.
This method uses the following ordered lookup procedure to determine
the XMLInputFactory implementation class to load:

- Use the javax.xml.stream.XMLInputFactory system property.
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

Once an application has obtained a reference to a XMLInputFactory it
can use the factory to configure and obtain stream instances.

**Throws:** FactoryConfigurationError

- in case of

service configuration error

or if
the implementation is not available or cannot be instantiated.

---

#### newFactory

public static

XMLInputFactory

newFactory()
throws

FactoryConfigurationError

Create a new instance of the factory.

This static method creates a new factory instance.
This method uses the following ordered lookup procedure to determine
the XMLInputFactory implementation class to load:

- Use the javax.xml.stream.XMLInputFactory system property.
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

Once an application has obtained a reference to a XMLInputFactory it
can use the factory to configure and obtain stream instances.

This static method creates a new factory instance.
This method uses the following ordered lookup procedure to determine
the XMLInputFactory implementation class to load:

- Use the javax.xml.stream.XMLInputFactory system property.
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

Once an application has obtained a reference to a XMLInputFactory it
can use the factory to configure and obtain stream instances.

Use the javax.xml.stream.XMLInputFactory system property.

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

Use the javax.xml.stream.XMLInputFactory system property.

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

Once an application has obtained a reference to a XMLInputFactory it
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

This method has been deprecated to maintain API consistency.
All newInstance methods have been replaced with corresponding
newFactory methods. The replacement

newFactory(java.lang.String, java.lang.ClassLoader)

method
defines no changes in behavior.

Create a new instance of the factory

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

Create a new instance of the factory

newFactory

```java
public static
XMLInputFactory
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
the XMLInputFactory implementation class to load:

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

is "javax.xml.stream.XMLInputFactory",
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

Note that this is a new method that replaces the deprecated

newInstance(String factoryId, ClassLoader classLoader)

method.
No changes in behavior are defined by this replacement method relative
to the deprecated method.

**API Note:** The parameter factoryId defined here is inconsistent with that
of other JAXP factories where the first parameter is fully qualified
factory class name that provides implementation of the factory.
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
**Throws:** FactoryConfigurationError

- if an instance of this factory cannot be loaded

---

#### newFactory

public static

XMLInputFactory

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
the XMLInputFactory implementation class to load:

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

is "javax.xml.stream.XMLInputFactory",
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

Note that this is a new method that replaces the deprecated

newInstance(String factoryId, ClassLoader classLoader)

method.
No changes in behavior are defined by this replacement method relative
to the deprecated method.

This method uses the following ordered lookup procedure to determine
the XMLInputFactory implementation class to load:

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

is "javax.xml.stream.XMLInputFactory",
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

Note that this is a new method that replaces the deprecated

newInstance(String factoryId, ClassLoader classLoader)

method.
No changes in behavior are defined by this replacement method relative
to the deprecated method.

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

is "javax.xml.stream.XMLInputFactory",
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

is "javax.xml.stream.XMLInputFactory",
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
No changes in behavior are defined by this replacement method relative
to the deprecated method.

createXMLStreamReader

```java
public abstract
XMLStreamReader
createXMLStreamReader​(
Reader
reader)
throws
XMLStreamException
```

Create a new XMLStreamReader from a reader

**Parameters:** reader

- the XML data to read from
**Throws:** XMLStreamException

---

#### createXMLStreamReader

public abstract

XMLStreamReader

createXMLStreamReader​(

Reader

reader)
throws

XMLStreamException

Create a new XMLStreamReader from a reader

createXMLStreamReader

```java
public abstract
XMLStreamReader
createXMLStreamReader​(
Source
source)
throws
XMLStreamException
```

Create a new XMLStreamReader from a JAXP source. This method is optional.

**Parameters:** source

- the source to read from
**Throws:** UnsupportedOperationException

- if this method is not
supported by this XMLInputFactory
**Throws:** XMLStreamException

---

#### createXMLStreamReader

public abstract

XMLStreamReader

createXMLStreamReader​(

Source

source)
throws

XMLStreamException

Create a new XMLStreamReader from a JAXP source. This method is optional.

createXMLStreamReader

```java
public abstract
XMLStreamReader
createXMLStreamReader​(
InputStream
stream)
throws
XMLStreamException
```

Create a new XMLStreamReader from a java.io.InputStream

**Parameters:** stream

- the InputStream to read from
**Throws:** XMLStreamException

---

#### createXMLStreamReader

public abstract

XMLStreamReader

createXMLStreamReader​(

InputStream

stream)
throws

XMLStreamException

Create a new XMLStreamReader from a java.io.InputStream

createXMLStreamReader

```java
public abstract
XMLStreamReader
createXMLStreamReader​(
InputStream
stream,

String
encoding)
throws
XMLStreamException
```

Create a new XMLStreamReader from a java.io.InputStream

**Parameters:** stream

- the InputStream to read from
**Parameters:** encoding

- the character encoding of the stream
**Throws:** XMLStreamException

---

#### createXMLStreamReader

public abstract

XMLStreamReader

createXMLStreamReader​(

InputStream

stream,

String

encoding)
throws

XMLStreamException

Create a new XMLStreamReader from a java.io.InputStream

createXMLStreamReader

```java
public abstract
XMLStreamReader
createXMLStreamReader​(
String
systemId,

InputStream
stream)
throws
XMLStreamException
```

Create a new XMLStreamReader from a java.io.InputStream

**Parameters:** systemId

- the system ID of the stream
**Parameters:** stream

- the InputStream to read from
**Throws:** XMLStreamException

---

#### createXMLStreamReader

public abstract

XMLStreamReader

createXMLStreamReader​(

String

systemId,

InputStream

stream)
throws

XMLStreamException

Create a new XMLStreamReader from a java.io.InputStream

createXMLStreamReader

```java
public abstract
XMLStreamReader
createXMLStreamReader​(
String
systemId,

Reader
reader)
throws
XMLStreamException
```

Create a new XMLStreamReader from a java.io.InputStream

**Parameters:** systemId

- the system ID of the stream
**Parameters:** reader

- the InputStream to read from
**Throws:** XMLStreamException

---

#### createXMLStreamReader

public abstract

XMLStreamReader

createXMLStreamReader​(

String

systemId,

Reader

reader)
throws

XMLStreamException

Create a new XMLStreamReader from a java.io.InputStream

createXMLEventReader

```java
public abstract
XMLEventReader
createXMLEventReader​(
Reader
reader)
throws
XMLStreamException
```

Create a new XMLEventReader from a reader

**Parameters:** reader

- the XML data to read from
**Throws:** XMLStreamException

---

#### createXMLEventReader

public abstract

XMLEventReader

createXMLEventReader​(

Reader

reader)
throws

XMLStreamException

Create a new XMLEventReader from a reader

createXMLEventReader

```java
public abstract
XMLEventReader
createXMLEventReader​(
String
systemId,

Reader
reader)
throws
XMLStreamException
```

Create a new XMLEventReader from a reader

**Parameters:** systemId

- the system ID of the input
**Parameters:** reader

- the XML data to read from
**Throws:** XMLStreamException

---

#### createXMLEventReader

public abstract

XMLEventReader

createXMLEventReader​(

String

systemId,

Reader

reader)
throws

XMLStreamException

Create a new XMLEventReader from a reader

createXMLEventReader

```java
public abstract
XMLEventReader
createXMLEventReader​(
XMLStreamReader
reader)
throws
XMLStreamException
```

Create a new XMLEventReader from an XMLStreamReader. After being used
to construct the XMLEventReader instance returned from this method
the XMLStreamReader must not be used.

**Parameters:** reader

- the XMLStreamReader to read from (may not be modified)
**Returns:** a new XMLEventReader
**Throws:** XMLStreamException

---

#### createXMLEventReader

public abstract

XMLEventReader

createXMLEventReader​(

XMLStreamReader

reader)
throws

XMLStreamException

Create a new XMLEventReader from an XMLStreamReader. After being used
to construct the XMLEventReader instance returned from this method
the XMLStreamReader must not be used.

createXMLEventReader

```java
public abstract
XMLEventReader
createXMLEventReader​(
Source
source)
throws
XMLStreamException
```

Create a new XMLEventReader from a JAXP source.
Support of this method is optional.

**Parameters:** source

- the source to read from
**Throws:** UnsupportedOperationException

- if this method is not
supported by this XMLInputFactory
**Throws:** XMLStreamException

---

#### createXMLEventReader

public abstract

XMLEventReader

createXMLEventReader​(

Source

source)
throws

XMLStreamException

Create a new XMLEventReader from a JAXP source.
Support of this method is optional.

createXMLEventReader

```java
public abstract
XMLEventReader
createXMLEventReader​(
InputStream
stream)
throws
XMLStreamException
```

Create a new XMLEventReader from a java.io.InputStream

**Parameters:** stream

- the InputStream to read from
**Throws:** XMLStreamException

---

#### createXMLEventReader

public abstract

XMLEventReader

createXMLEventReader​(

InputStream

stream)
throws

XMLStreamException

Create a new XMLEventReader from a java.io.InputStream

createXMLEventReader

```java
public abstract
XMLEventReader
createXMLEventReader​(
InputStream
stream,

String
encoding)
throws
XMLStreamException
```

Create a new XMLEventReader from a java.io.InputStream

**Parameters:** stream

- the InputStream to read from
**Parameters:** encoding

- the character encoding of the stream
**Throws:** XMLStreamException

---

#### createXMLEventReader

public abstract

XMLEventReader

createXMLEventReader​(

InputStream

stream,

String

encoding)
throws

XMLStreamException

Create a new XMLEventReader from a java.io.InputStream

createXMLEventReader

```java
public abstract
XMLEventReader
createXMLEventReader​(
String
systemId,

InputStream
stream)
throws
XMLStreamException
```

Create a new XMLEventReader from a java.io.InputStream

**Parameters:** systemId

- the system ID of the stream
**Parameters:** stream

- the InputStream to read from
**Throws:** XMLStreamException

---

#### createXMLEventReader

public abstract

XMLEventReader

createXMLEventReader​(

String

systemId,

InputStream

stream)
throws

XMLStreamException

Create a new XMLEventReader from a java.io.InputStream

createFilteredReader

```java
public abstract
XMLStreamReader
createFilteredReader​(
XMLStreamReader
reader,

StreamFilter
filter)
throws
XMLStreamException
```

Create a filtered reader that wraps the filter around the reader

**Parameters:** reader

- the reader to filter
**Parameters:** filter

- the filter to apply to the reader
**Throws:** XMLStreamException

---

#### createFilteredReader

public abstract

XMLStreamReader

createFilteredReader​(

XMLStreamReader

reader,

StreamFilter

filter)
throws

XMLStreamException

Create a filtered reader that wraps the filter around the reader

createFilteredReader

```java
public abstract
XMLEventReader
createFilteredReader​(
XMLEventReader
reader,

EventFilter
filter)
throws
XMLStreamException
```

Create a filtered event reader that wraps the filter around the event reader

**Parameters:** reader

- the event reader to wrap
**Parameters:** filter

- the filter to apply to the event reader
**Throws:** XMLStreamException

---

#### createFilteredReader

public abstract

XMLEventReader

createFilteredReader​(

XMLEventReader

reader,

EventFilter

filter)
throws

XMLStreamException

Create a filtered event reader that wraps the filter around the event reader

getXMLResolver

```java
public abstract
XMLResolver
getXMLResolver()
```

The resolver that will be set on any XMLStreamReader or XMLEventReader created
by this factory instance.

---

#### getXMLResolver

public abstract

XMLResolver

getXMLResolver()

The resolver that will be set on any XMLStreamReader or XMLEventReader created
by this factory instance.

setXMLResolver

```java
public abstract void setXMLResolver​(
XMLResolver
resolver)
```

The resolver that will be set on any XMLStreamReader or XMLEventReader created
by this factory instance.

**Parameters:** resolver

- the resolver to use to resolve references

---

#### setXMLResolver

public abstract void setXMLResolver​(

XMLResolver

resolver)

The resolver that will be set on any XMLStreamReader or XMLEventReader created
by this factory instance.

getXMLReporter

```java
public abstract
XMLReporter
getXMLReporter()
```

The reporter that will be set on any XMLStreamReader or XMLEventReader created
by this factory instance.

---

#### getXMLReporter

public abstract

XMLReporter

getXMLReporter()

The reporter that will be set on any XMLStreamReader or XMLEventReader created
by this factory instance.

setXMLReporter

```java
public abstract void setXMLReporter​(
XMLReporter
reporter)
```

The reporter that will be set on any XMLStreamReader or XMLEventReader created
by this factory instance.

**Parameters:** reporter

- the resolver to use to report non fatal errors

---

#### setXMLReporter

public abstract void setXMLReporter​(

XMLReporter

reporter)

The reporter that will be set on any XMLStreamReader or XMLEventReader created
by this factory instance.

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

Allows the user to set specific feature/property on the underlying
implementation. The underlying implementation is not required to support
every setting of every property in the specification and may use
IllegalArgumentException to signal that an unsupported property may not be
set with the specified value.

All implementations that implement JAXP 1.5 or newer are required to
support the

XMLConstants.ACCESS_EXTERNAL_DTD

property.

- Access to external DTDs, external Entity References is restricted to the
protocols specified by the property. If access is denied during parsing
due to the restriction of this property,

XMLStreamException

will be thrown by the

XMLStreamReader.next()

or

XMLEventReader.nextEvent()

method.

**Parameters:** name

- The name of the property (may not be null)
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

Allows the user to set specific feature/property on the underlying
implementation. The underlying implementation is not required to support
every setting of every property in the specification and may use
IllegalArgumentException to signal that an unsupported property may not be
set with the specified value.

All implementations that implement JAXP 1.5 or newer are required to
support the

XMLConstants.ACCESS_EXTERNAL_DTD

property.

- Access to external DTDs, external Entity References is restricted to the
protocols specified by the property. If access is denied during parsing
due to the restriction of this property,

XMLStreamException

will be thrown by the

XMLStreamReader.next()

or

XMLEventReader.nextEvent()

method.

All implementations that implement JAXP 1.5 or newer are required to
support the

XMLConstants.ACCESS_EXTERNAL_DTD

property.

- Access to external DTDs, external Entity References is restricted to the
protocols specified by the property. If access is denied during parsing
due to the restriction of this property,

XMLStreamException

will be thrown by the

XMLStreamReader.next()

or

XMLEventReader.nextEvent()

method.

Access to external DTDs, external Entity References is restricted to the
protocols specified by the property. If access is denied during parsing
due to the restriction of this property,

XMLStreamException

will be thrown by the

XMLStreamReader.next()

or

XMLEventReader.nextEvent()

method.

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

Get the value of a feature/property from the underlying implementation

**Parameters:** name

- The name of the property (may not be null)
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

Get the value of a feature/property from the underlying implementation

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

setEventAllocator

```java
public abstract void setEventAllocator​(
XMLEventAllocator
allocator)
```

Set a user defined event allocator for events

**Parameters:** allocator

- the user defined allocator

---

#### setEventAllocator

public abstract void setEventAllocator​(

XMLEventAllocator

allocator)

Set a user defined event allocator for events

getEventAllocator

```java
public abstract
XMLEventAllocator
getEventAllocator()
```

Gets the allocator used by streams created with this factory

---

#### getEventAllocator

public abstract

XMLEventAllocator

getEventAllocator()

Gets the allocator used by streams created with this factory

---

