# Interface XMLEventWriter

**Source:** `java.xml\javax\xml\stream\XMLEventWriter.html`

### Class Description

```java
public interface
XMLEventWriter

extends
XMLEventConsumer
```

This is the top level interface for writing XML documents.

Instances of this interface are not required to validate the
form of the XML.

**All Superinterfaces:** XMLEventConsumer

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void flush()
throws
XMLStreamException

Writes any cached events to the underlying output mechanism

**Throws:**
- XMLStreamException

---

#### void close()
throws
XMLStreamException

Frees any resources associated with this stream

**Throws:**
- XMLStreamException

---

#### void add​(
XMLEvent
event)
throws
XMLStreamException

Add an event to the output stream
Adding a START_ELEMENT will open a new namespace scope that
will be closed when the corresponding END_ELEMENT is written.

Required and optional fields for events added to the writer

Event Type

Required Fields

Optional Fields

Required Behavior

START_ELEMENT

QName name

namespaces , attributes

A START_ELEMENT will be written by writing the name,
namespaces, and attributes of the event in XML 1.0 valid
syntax for START_ELEMENTs.
The name is written by looking up the prefix for
the namespace uri. The writer can be configured to
respect prefixes of QNames. If the writer is respecting
prefixes it must use the prefix set on the QName. The
default behavior is to lookup the value for the prefix
on the EventWriter's internal namespace context.
Each attribute (if any)
is written using the behavior specified in the attribute
section of this table. Each namespace (if any) is written
using the behavior specified in the namespace section of this
table.

END_ELEMENT

Qname name

None

A well formed END_ELEMENT tag is written.
The name is written by looking up the prefix for
the namespace uri. The writer can be configured to
respect prefixes of QNames. If the writer is respecting
prefixes it must use the prefix set on the QName. The
default behavior is to lookup the value for the prefix
on the EventWriter's internal namespace context.
If the END_ELEMENT name does not match the START_ELEMENT
name an XMLStreamException is thrown.

ATTRIBUTE

QName name , String value

QName type

An attribute is written using the same algorithm
to find the lexical form as used in START_ELEMENT.
The default is to use double quotes to wrap attribute
values and to escape any double quotes found in the
value. The type value is ignored.

NAMESPACE

String prefix, String namespaceURI,
boolean isDefaultNamespaceDeclaration

None

A namespace declaration is written. If the
namespace is a default namespace declaration
(isDefault is true) then xmlns="$namespaceURI"
is written and the prefix is optional. If
isDefault is false, the prefix must be declared
and the writer must prepend xmlns to the prefix
and write out a standard prefix declaration.

PROCESSING_INSTRUCTION

None

String target, String data

The data does not need to be present and may be
null. Target is required and many not be null.
The writer
will write data section
directly after the target,
enclosed in appropriate XML 1.0 syntax

COMMENT

None

String comment

If the comment is present (not null) it is written, otherwise an
an empty comment is written

START_DOCUMENT

None

String encoding , boolean standalone, String version

A START_DOCUMENT event is not required to be written to the
stream. If present the attributes are written inside
the appropriate XML declaration syntax

END_DOCUMENT

None

None

Nothing is written to the output

DTD

String DocumentTypeDefinition

None

The DocumentTypeDefinition is written to the output

**Specified by:**
- add

in interface

XMLEventConsumer

**Parameters:**
- event

- the event to be added

**Throws:**
- XMLStreamException

---

#### void add​(
XMLEventReader
reader)
throws
XMLStreamException

Adds an entire stream to an output stream,
calls next() on the inputStream argument until hasNext() returns false
This should be treated as a convenience method that will
perform the following loop over all the events in an
event reader and call add on each event.

**Parameters:**
- reader

- the event stream to add to the output

**Throws:**
- XMLStreamException

---

#### String
getPrefix​(
String
uri)
throws
XMLStreamException

Gets the prefix the uri is bound to

**Parameters:**
- uri

- the uri to look up

**Throws:**
- XMLStreamException

---

#### void setPrefix​(
String
prefix,

String
uri)
throws
XMLStreamException

Sets the prefix the uri is bound to. This prefix is bound
in the scope of the current START_ELEMENT / END_ELEMENT pair.
If this method is called before a START_ELEMENT has been written
the prefix is bound in the root scope.

**Parameters:**
- prefix

- the prefix to bind to the uri
- uri

- the uri to bind to the prefix

**Throws:**
- XMLStreamException

---

#### void setDefaultNamespace​(
String
uri)
throws
XMLStreamException

Binds a URI to the default namespace
This URI is bound
in the scope of the current START_ELEMENT / END_ELEMENT pair.
If this method is called before a START_ELEMENT has been written
the uri is bound in the root scope.

**Parameters:**
- uri

- the uri to bind to the default namespace

**Throws:**
- XMLStreamException

---

#### void setNamespaceContext​(
NamespaceContext
context)
throws
XMLStreamException

Sets the current namespace context for prefix and uri bindings.
This context becomes the root namespace context for writing and
will replace the current root namespace context. Subsequent calls
to setPrefix and setDefaultNamespace will bind namespaces using
the context passed to the method as the root context for resolving
namespaces.

**Parameters:**
- context

- the namespace context to use for this writer

**Throws:**
- XMLStreamException

---

#### NamespaceContext
getNamespaceContext()

Returns the current namespace context.

**Returns:**
- the current namespace context

---

### Additional Sections

#### Interface XMLEventWriter

**All Superinterfaces:** XMLEventConsumer

```java
public interface
XMLEventWriter

extends
XMLEventConsumer
```

This is the top level interface for writing XML documents.

Instances of this interface are not required to validate the
form of the XML.

**Since:** 1.6
**See Also:** XMLEventReader

,

XMLEvent

,

Characters

,

ProcessingInstruction

,

StartElement

,

EndElement

public interface

XMLEventWriter

extends

XMLEventConsumer

This is the top level interface for writing XML documents.

Instances of this interface are not required to validate the
form of the XML.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

add

​(

XMLEvent

event)

Add an event to the output stream
Adding a START_ELEMENT will open a new namespace scope that
will be closed when the corresponding END_ELEMENT is written.

void

add

​(

XMLEventReader

reader)

Adds an entire stream to an output stream,
calls next() on the inputStream argument until hasNext() returns false
This should be treated as a convenience method that will
perform the following loop over all the events in an
event reader and call add on each event.

void

close

()

Frees any resources associated with this stream

void

flush

()

Writes any cached events to the underlying output mechanism

NamespaceContext

getNamespaceContext

()

Returns the current namespace context.

String

getPrefix

​(

String

uri)

Gets the prefix the uri is bound to

void

setDefaultNamespace

​(

String

uri)

Binds a URI to the default namespace
This URI is bound
in the scope of the current START_ELEMENT / END_ELEMENT pair.

void

setNamespaceContext

​(

NamespaceContext

context)

Sets the current namespace context for prefix and uri bindings.

void

setPrefix

​(

String

prefix,

String

uri)

Sets the prefix the uri is bound to.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

add

​(

XMLEvent

event)

Add an event to the output stream
Adding a START_ELEMENT will open a new namespace scope that
will be closed when the corresponding END_ELEMENT is written.

void

add

​(

XMLEventReader

reader)

Adds an entire stream to an output stream,
calls next() on the inputStream argument until hasNext() returns false
This should be treated as a convenience method that will
perform the following loop over all the events in an
event reader and call add on each event.

void

close

()

Frees any resources associated with this stream

void

flush

()

Writes any cached events to the underlying output mechanism

NamespaceContext

getNamespaceContext

()

Returns the current namespace context.

String

getPrefix

​(

String

uri)

Gets the prefix the uri is bound to

void

setDefaultNamespace

​(

String

uri)

Binds a URI to the default namespace
This URI is bound
in the scope of the current START_ELEMENT / END_ELEMENT pair.

void

setNamespaceContext

​(

NamespaceContext

context)

Sets the current namespace context for prefix and uri bindings.

void

setPrefix

​(

String

prefix,

String

uri)

Sets the prefix the uri is bound to.

---

#### Method Summary

Add an event to the output stream
Adding a START_ELEMENT will open a new namespace scope that
will be closed when the corresponding END_ELEMENT is written.

Adds an entire stream to an output stream,
calls next() on the inputStream argument until hasNext() returns false
This should be treated as a convenience method that will
perform the following loop over all the events in an
event reader and call add on each event.

Frees any resources associated with this stream

Writes any cached events to the underlying output mechanism

Returns the current namespace context.

Gets the prefix the uri is bound to

Binds a URI to the default namespace
This URI is bound
in the scope of the current START_ELEMENT / END_ELEMENT pair.

Sets the current namespace context for prefix and uri bindings.

Sets the prefix the uri is bound to.

============ METHOD DETAIL ==========

- Method Detail

- flush

```java
void flush()
throws
XMLStreamException
```

Writes any cached events to the underlying output mechanism

**Throws:** XMLStreamException

- close

```java
void close()
throws
XMLStreamException
```

Frees any resources associated with this stream

**Throws:** XMLStreamException

- add

```java
void add​(
XMLEvent
event)
throws
XMLStreamException
```

Add an event to the output stream
Adding a START_ELEMENT will open a new namespace scope that
will be closed when the corresponding END_ELEMENT is written.

Required and optional fields for events added to the writer

Event Type

Required Fields

Optional Fields

Required Behavior

START_ELEMENT

QName name

namespaces , attributes

A START_ELEMENT will be written by writing the name,
namespaces, and attributes of the event in XML 1.0 valid
syntax for START_ELEMENTs.
The name is written by looking up the prefix for
the namespace uri. The writer can be configured to
respect prefixes of QNames. If the writer is respecting
prefixes it must use the prefix set on the QName. The
default behavior is to lookup the value for the prefix
on the EventWriter's internal namespace context.
Each attribute (if any)
is written using the behavior specified in the attribute
section of this table. Each namespace (if any) is written
using the behavior specified in the namespace section of this
table.

END_ELEMENT

Qname name

None

A well formed END_ELEMENT tag is written.
The name is written by looking up the prefix for
the namespace uri. The writer can be configured to
respect prefixes of QNames. If the writer is respecting
prefixes it must use the prefix set on the QName. The
default behavior is to lookup the value for the prefix
on the EventWriter's internal namespace context.
If the END_ELEMENT name does not match the START_ELEMENT
name an XMLStreamException is thrown.

ATTRIBUTE

QName name , String value

QName type

An attribute is written using the same algorithm
to find the lexical form as used in START_ELEMENT.
The default is to use double quotes to wrap attribute
values and to escape any double quotes found in the
value. The type value is ignored.

NAMESPACE

String prefix, String namespaceURI,
boolean isDefaultNamespaceDeclaration

None

A namespace declaration is written. If the
namespace is a default namespace declaration
(isDefault is true) then xmlns="$namespaceURI"
is written and the prefix is optional. If
isDefault is false, the prefix must be declared
and the writer must prepend xmlns to the prefix
and write out a standard prefix declaration.

PROCESSING_INSTRUCTION

None

String target, String data

The data does not need to be present and may be
null. Target is required and many not be null.
The writer
will write data section
directly after the target,
enclosed in appropriate XML 1.0 syntax

COMMENT

None

String comment

If the comment is present (not null) it is written, otherwise an
an empty comment is written

START_DOCUMENT

None

String encoding , boolean standalone, String version

A START_DOCUMENT event is not required to be written to the
stream. If present the attributes are written inside
the appropriate XML declaration syntax

END_DOCUMENT

None

None

Nothing is written to the output

DTD

String DocumentTypeDefinition

None

The DocumentTypeDefinition is written to the output

**Specified by:** add

in interface

XMLEventConsumer
**Parameters:** event

- the event to be added
**Throws:** XMLStreamException

- add

```java
void add​(
XMLEventReader
reader)
throws
XMLStreamException
```

Adds an entire stream to an output stream,
calls next() on the inputStream argument until hasNext() returns false
This should be treated as a convenience method that will
perform the following loop over all the events in an
event reader and call add on each event.

**Parameters:** reader

- the event stream to add to the output
**Throws:** XMLStreamException

- getPrefix

```java
String
getPrefix​(
String
uri)
throws
XMLStreamException
```

Gets the prefix the uri is bound to

**Parameters:** uri

- the uri to look up
**Throws:** XMLStreamException

- setPrefix

```java
void setPrefix​(
String
prefix,

String
uri)
throws
XMLStreamException
```

Sets the prefix the uri is bound to. This prefix is bound
in the scope of the current START_ELEMENT / END_ELEMENT pair.
If this method is called before a START_ELEMENT has been written
the prefix is bound in the root scope.

**Parameters:** prefix

- the prefix to bind to the uri
**Parameters:** uri

- the uri to bind to the prefix
**Throws:** XMLStreamException

- setDefaultNamespace

```java
void setDefaultNamespace​(
String
uri)
throws
XMLStreamException
```

Binds a URI to the default namespace
This URI is bound
in the scope of the current START_ELEMENT / END_ELEMENT pair.
If this method is called before a START_ELEMENT has been written
the uri is bound in the root scope.

**Parameters:** uri

- the uri to bind to the default namespace
**Throws:** XMLStreamException

- setNamespaceContext

```java
void setNamespaceContext​(
NamespaceContext
context)
throws
XMLStreamException
```

Sets the current namespace context for prefix and uri bindings.
This context becomes the root namespace context for writing and
will replace the current root namespace context. Subsequent calls
to setPrefix and setDefaultNamespace will bind namespaces using
the context passed to the method as the root context for resolving
namespaces.

**Parameters:** context

- the namespace context to use for this writer
**Throws:** XMLStreamException

- getNamespaceContext

```java
NamespaceContext
getNamespaceContext()
```

Returns the current namespace context.

**Returns:** the current namespace context

Method Detail

- flush

```java
void flush()
throws
XMLStreamException
```

Writes any cached events to the underlying output mechanism

**Throws:** XMLStreamException

- close

```java
void close()
throws
XMLStreamException
```

Frees any resources associated with this stream

**Throws:** XMLStreamException

- add

```java
void add​(
XMLEvent
event)
throws
XMLStreamException
```

Add an event to the output stream
Adding a START_ELEMENT will open a new namespace scope that
will be closed when the corresponding END_ELEMENT is written.

Required and optional fields for events added to the writer

Event Type

Required Fields

Optional Fields

Required Behavior

START_ELEMENT

QName name

namespaces , attributes

A START_ELEMENT will be written by writing the name,
namespaces, and attributes of the event in XML 1.0 valid
syntax for START_ELEMENTs.
The name is written by looking up the prefix for
the namespace uri. The writer can be configured to
respect prefixes of QNames. If the writer is respecting
prefixes it must use the prefix set on the QName. The
default behavior is to lookup the value for the prefix
on the EventWriter's internal namespace context.
Each attribute (if any)
is written using the behavior specified in the attribute
section of this table. Each namespace (if any) is written
using the behavior specified in the namespace section of this
table.

END_ELEMENT

Qname name

None

A well formed END_ELEMENT tag is written.
The name is written by looking up the prefix for
the namespace uri. The writer can be configured to
respect prefixes of QNames. If the writer is respecting
prefixes it must use the prefix set on the QName. The
default behavior is to lookup the value for the prefix
on the EventWriter's internal namespace context.
If the END_ELEMENT name does not match the START_ELEMENT
name an XMLStreamException is thrown.

ATTRIBUTE

QName name , String value

QName type

An attribute is written using the same algorithm
to find the lexical form as used in START_ELEMENT.
The default is to use double quotes to wrap attribute
values and to escape any double quotes found in the
value. The type value is ignored.

NAMESPACE

String prefix, String namespaceURI,
boolean isDefaultNamespaceDeclaration

None

A namespace declaration is written. If the
namespace is a default namespace declaration
(isDefault is true) then xmlns="$namespaceURI"
is written and the prefix is optional. If
isDefault is false, the prefix must be declared
and the writer must prepend xmlns to the prefix
and write out a standard prefix declaration.

PROCESSING_INSTRUCTION

None

String target, String data

The data does not need to be present and may be
null. Target is required and many not be null.
The writer
will write data section
directly after the target,
enclosed in appropriate XML 1.0 syntax

COMMENT

None

String comment

If the comment is present (not null) it is written, otherwise an
an empty comment is written

START_DOCUMENT

None

String encoding , boolean standalone, String version

A START_DOCUMENT event is not required to be written to the
stream. If present the attributes are written inside
the appropriate XML declaration syntax

END_DOCUMENT

None

None

Nothing is written to the output

DTD

String DocumentTypeDefinition

None

The DocumentTypeDefinition is written to the output

**Specified by:** add

in interface

XMLEventConsumer
**Parameters:** event

- the event to be added
**Throws:** XMLStreamException

- add

```java
void add​(
XMLEventReader
reader)
throws
XMLStreamException
```

Adds an entire stream to an output stream,
calls next() on the inputStream argument until hasNext() returns false
This should be treated as a convenience method that will
perform the following loop over all the events in an
event reader and call add on each event.

**Parameters:** reader

- the event stream to add to the output
**Throws:** XMLStreamException

- getPrefix

```java
String
getPrefix​(
String
uri)
throws
XMLStreamException
```

Gets the prefix the uri is bound to

**Parameters:** uri

- the uri to look up
**Throws:** XMLStreamException

- setPrefix

```java
void setPrefix​(
String
prefix,

String
uri)
throws
XMLStreamException
```

Sets the prefix the uri is bound to. This prefix is bound
in the scope of the current START_ELEMENT / END_ELEMENT pair.
If this method is called before a START_ELEMENT has been written
the prefix is bound in the root scope.

**Parameters:** prefix

- the prefix to bind to the uri
**Parameters:** uri

- the uri to bind to the prefix
**Throws:** XMLStreamException

- setDefaultNamespace

```java
void setDefaultNamespace​(
String
uri)
throws
XMLStreamException
```

Binds a URI to the default namespace
This URI is bound
in the scope of the current START_ELEMENT / END_ELEMENT pair.
If this method is called before a START_ELEMENT has been written
the uri is bound in the root scope.

**Parameters:** uri

- the uri to bind to the default namespace
**Throws:** XMLStreamException

- setNamespaceContext

```java
void setNamespaceContext​(
NamespaceContext
context)
throws
XMLStreamException
```

Sets the current namespace context for prefix and uri bindings.
This context becomes the root namespace context for writing and
will replace the current root namespace context. Subsequent calls
to setPrefix and setDefaultNamespace will bind namespaces using
the context passed to the method as the root context for resolving
namespaces.

**Parameters:** context

- the namespace context to use for this writer
**Throws:** XMLStreamException

- getNamespaceContext

```java
NamespaceContext
getNamespaceContext()
```

Returns the current namespace context.

**Returns:** the current namespace context

---

#### Method Detail

flush

```java
void flush()
throws
XMLStreamException
```

Writes any cached events to the underlying output mechanism

**Throws:** XMLStreamException

---

#### flush

void flush()
throws

XMLStreamException

Writes any cached events to the underlying output mechanism

close

```java
void close()
throws
XMLStreamException
```

Frees any resources associated with this stream

**Throws:** XMLStreamException

---

#### close

void close()
throws

XMLStreamException

Frees any resources associated with this stream

add

```java
void add​(
XMLEvent
event)
throws
XMLStreamException
```

Add an event to the output stream
Adding a START_ELEMENT will open a new namespace scope that
will be closed when the corresponding END_ELEMENT is written.

Required and optional fields for events added to the writer

Event Type

Required Fields

Optional Fields

Required Behavior

START_ELEMENT

QName name

namespaces , attributes

A START_ELEMENT will be written by writing the name,
namespaces, and attributes of the event in XML 1.0 valid
syntax for START_ELEMENTs.
The name is written by looking up the prefix for
the namespace uri. The writer can be configured to
respect prefixes of QNames. If the writer is respecting
prefixes it must use the prefix set on the QName. The
default behavior is to lookup the value for the prefix
on the EventWriter's internal namespace context.
Each attribute (if any)
is written using the behavior specified in the attribute
section of this table. Each namespace (if any) is written
using the behavior specified in the namespace section of this
table.

END_ELEMENT

Qname name

None

A well formed END_ELEMENT tag is written.
The name is written by looking up the prefix for
the namespace uri. The writer can be configured to
respect prefixes of QNames. If the writer is respecting
prefixes it must use the prefix set on the QName. The
default behavior is to lookup the value for the prefix
on the EventWriter's internal namespace context.
If the END_ELEMENT name does not match the START_ELEMENT
name an XMLStreamException is thrown.

ATTRIBUTE

QName name , String value

QName type

An attribute is written using the same algorithm
to find the lexical form as used in START_ELEMENT.
The default is to use double quotes to wrap attribute
values and to escape any double quotes found in the
value. The type value is ignored.

NAMESPACE

String prefix, String namespaceURI,
boolean isDefaultNamespaceDeclaration

None

A namespace declaration is written. If the
namespace is a default namespace declaration
(isDefault is true) then xmlns="$namespaceURI"
is written and the prefix is optional. If
isDefault is false, the prefix must be declared
and the writer must prepend xmlns to the prefix
and write out a standard prefix declaration.

PROCESSING_INSTRUCTION

None

String target, String data

The data does not need to be present and may be
null. Target is required and many not be null.
The writer
will write data section
directly after the target,
enclosed in appropriate XML 1.0 syntax

COMMENT

None

String comment

If the comment is present (not null) it is written, otherwise an
an empty comment is written

START_DOCUMENT

None

String encoding , boolean standalone, String version

A START_DOCUMENT event is not required to be written to the
stream. If present the attributes are written inside
the appropriate XML declaration syntax

END_DOCUMENT

None

None

Nothing is written to the output

DTD

String DocumentTypeDefinition

None

The DocumentTypeDefinition is written to the output

**Specified by:** add

in interface

XMLEventConsumer
**Parameters:** event

- the event to be added
**Throws:** XMLStreamException

---

#### add

void add​(

XMLEvent

event)
throws

XMLStreamException

Add an event to the output stream
Adding a START_ELEMENT will open a new namespace scope that
will be closed when the corresponding END_ELEMENT is written.

Required and optional fields for events added to the writer

Event Type

Required Fields

Optional Fields

Required Behavior

START_ELEMENT

QName name

namespaces , attributes

A START_ELEMENT will be written by writing the name,
namespaces, and attributes of the event in XML 1.0 valid
syntax for START_ELEMENTs.
The name is written by looking up the prefix for
the namespace uri. The writer can be configured to
respect prefixes of QNames. If the writer is respecting
prefixes it must use the prefix set on the QName. The
default behavior is to lookup the value for the prefix
on the EventWriter's internal namespace context.
Each attribute (if any)
is written using the behavior specified in the attribute
section of this table. Each namespace (if any) is written
using the behavior specified in the namespace section of this
table.

END_ELEMENT

Qname name

None

A well formed END_ELEMENT tag is written.
The name is written by looking up the prefix for
the namespace uri. The writer can be configured to
respect prefixes of QNames. If the writer is respecting
prefixes it must use the prefix set on the QName. The
default behavior is to lookup the value for the prefix
on the EventWriter's internal namespace context.
If the END_ELEMENT name does not match the START_ELEMENT
name an XMLStreamException is thrown.

ATTRIBUTE

QName name , String value

QName type

An attribute is written using the same algorithm
to find the lexical form as used in START_ELEMENT.
The default is to use double quotes to wrap attribute
values and to escape any double quotes found in the
value. The type value is ignored.

NAMESPACE

String prefix, String namespaceURI,
boolean isDefaultNamespaceDeclaration

None

A namespace declaration is written. If the
namespace is a default namespace declaration
(isDefault is true) then xmlns="$namespaceURI"
is written and the prefix is optional. If
isDefault is false, the prefix must be declared
and the writer must prepend xmlns to the prefix
and write out a standard prefix declaration.

PROCESSING_INSTRUCTION

None

String target, String data

The data does not need to be present and may be
null. Target is required and many not be null.
The writer
will write data section
directly after the target,
enclosed in appropriate XML 1.0 syntax

COMMENT

None

String comment

If the comment is present (not null) it is written, otherwise an
an empty comment is written

START_DOCUMENT

None

String encoding , boolean standalone, String version

A START_DOCUMENT event is not required to be written to the
stream. If present the attributes are written inside
the appropriate XML declaration syntax

END_DOCUMENT

None

None

Nothing is written to the output

DTD

String DocumentTypeDefinition

None

The DocumentTypeDefinition is written to the output

add

```java
void add​(
XMLEventReader
reader)
throws
XMLStreamException
```

Adds an entire stream to an output stream,
calls next() on the inputStream argument until hasNext() returns false
This should be treated as a convenience method that will
perform the following loop over all the events in an
event reader and call add on each event.

**Parameters:** reader

- the event stream to add to the output
**Throws:** XMLStreamException

---

#### add

void add​(

XMLEventReader

reader)
throws

XMLStreamException

Adds an entire stream to an output stream,
calls next() on the inputStream argument until hasNext() returns false
This should be treated as a convenience method that will
perform the following loop over all the events in an
event reader and call add on each event.

getPrefix

```java
String
getPrefix​(
String
uri)
throws
XMLStreamException
```

Gets the prefix the uri is bound to

**Parameters:** uri

- the uri to look up
**Throws:** XMLStreamException

---

#### getPrefix

String

getPrefix​(

String

uri)
throws

XMLStreamException

Gets the prefix the uri is bound to

setPrefix

```java
void setPrefix​(
String
prefix,

String
uri)
throws
XMLStreamException
```

Sets the prefix the uri is bound to. This prefix is bound
in the scope of the current START_ELEMENT / END_ELEMENT pair.
If this method is called before a START_ELEMENT has been written
the prefix is bound in the root scope.

**Parameters:** prefix

- the prefix to bind to the uri
**Parameters:** uri

- the uri to bind to the prefix
**Throws:** XMLStreamException

---

#### setPrefix

void setPrefix​(

String

prefix,

String

uri)
throws

XMLStreamException

Sets the prefix the uri is bound to. This prefix is bound
in the scope of the current START_ELEMENT / END_ELEMENT pair.
If this method is called before a START_ELEMENT has been written
the prefix is bound in the root scope.

setDefaultNamespace

```java
void setDefaultNamespace​(
String
uri)
throws
XMLStreamException
```

Binds a URI to the default namespace
This URI is bound
in the scope of the current START_ELEMENT / END_ELEMENT pair.
If this method is called before a START_ELEMENT has been written
the uri is bound in the root scope.

**Parameters:** uri

- the uri to bind to the default namespace
**Throws:** XMLStreamException

---

#### setDefaultNamespace

void setDefaultNamespace​(

String

uri)
throws

XMLStreamException

Binds a URI to the default namespace
This URI is bound
in the scope of the current START_ELEMENT / END_ELEMENT pair.
If this method is called before a START_ELEMENT has been written
the uri is bound in the root scope.

setNamespaceContext

```java
void setNamespaceContext​(
NamespaceContext
context)
throws
XMLStreamException
```

Sets the current namespace context for prefix and uri bindings.
This context becomes the root namespace context for writing and
will replace the current root namespace context. Subsequent calls
to setPrefix and setDefaultNamespace will bind namespaces using
the context passed to the method as the root context for resolving
namespaces.

**Parameters:** context

- the namespace context to use for this writer
**Throws:** XMLStreamException

---

#### setNamespaceContext

void setNamespaceContext​(

NamespaceContext

context)
throws

XMLStreamException

Sets the current namespace context for prefix and uri bindings.
This context becomes the root namespace context for writing and
will replace the current root namespace context. Subsequent calls
to setPrefix and setDefaultNamespace will bind namespaces using
the context passed to the method as the root context for resolving
namespaces.

getNamespaceContext

```java
NamespaceContext
getNamespaceContext()
```

Returns the current namespace context.

**Returns:** the current namespace context

---

#### getNamespaceContext

NamespaceContext

getNamespaceContext()

Returns the current namespace context.

---

