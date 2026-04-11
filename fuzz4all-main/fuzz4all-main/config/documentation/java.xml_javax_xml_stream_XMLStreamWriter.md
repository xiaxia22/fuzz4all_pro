# Interface XMLStreamWriter

**Source:** `java.xml\javax\xml\stream\XMLStreamWriter.html`

### Class Description

```java
public interface
XMLStreamWriter
```

The XMLStreamWriter interface specifies how to write XML. The XMLStreamWriter does
not perform well formedness checking on its input. However
the writeCharacters method is required to escape &, < and >
For attribute values the writeAttribute method will escape the
above characters plus " to ensure that all character content
and attribute values are well formed.

Each NAMESPACE
and ATTRIBUTE must be individually written.

XML Namespaces,

javax.xml.stream.isRepairingNamespaces

and write method behaviour

Method

method

isRepairingNamespaces

== true

isRepairingNamespaces

== false

method

namespaceURI bound

namespaceURI unbound

namespaceURI bound

namespaceURI unbound

writeAttribute(namespaceURI, localName, value)

isRepairingNamespaces == true

namespaceURI bound

prefix:localName="value"

[1]

namespaceURI unbound

xmlns:{generated}="namespaceURI" {generated}:localName="value"

isRepairingNamespaces == false

namespaceURI bound

prefix:localName="value"

[1]

namespaceURI unbound

XMLStreamException

writeAttribute(prefix, namespaceURI, localName, value)

isRepairingNamespaces == true

namespaceURI bound

bound to same prefix:

prefix:localName="value"

[1]

bound to different prefix:

xmlns:{generated}="namespaceURI" {generated}:localName="value"

namespaceURI unbound

xmlns:prefix="namespaceURI" prefix:localName="value"

[3]

isRepairingNamespaces == false

namespaceURI bound

bound to same prefix:

prefix:localName="value"

[1][2]

bound to different prefix:

XMLStreamException

[2]

namespaceURI unbound

xmlns:prefix="namespaceURI" prefix:localName="value"

[2][5]

writeStartElement(namespaceURI, localName)

writeEmptyElement(namespaceURI, localName)

isRepairingNamespaces == true

namespaceURI bound

<prefix:localName>

[1]

namespaceURI unbound

<{generated}:localName xmlns:{generated}="namespaceURI">

isRepairingNamespaces == false

namespaceURI bound

prefix:localName>

[1]

namespaceURI unbound

XMLStreamException

writeStartElement(prefix, localName, namespaceURI)

writeEmptyElement(prefix, localName, namespaceURI)

isRepairingNamespaces == true

namespaceURI bound

bound to same prefix:

<prefix:localName>

[1]

bound to different prefix:

<{generated}:localName xmlns:{generated}="namespaceURI">

namespaceURI unbound

<prefix:localName xmlns:prefix="namespaceURI">

[4]

isRepairingNamespaces == false

namespaceURI bound

bound to same prefix:

<prefix:localName>

[1]

bound to different prefix:

XMLStreamException

namespaceURI unbound

<prefix:localName>

Notes:

- [1] if namespaceURI == default Namespace URI, then no prefix is written
- [2] if prefix == "" || null && namespaceURI == "", then
no prefix or Namespace declaration is generated or written
- [3] if prefix == "" || null, then a prefix is randomly generated
- [4] if prefix == "" || null, then it is treated as the default Namespace and
no prefix is generated or written, an xmlns declaration is generated
and written if the namespaceURI is unbound
- [5] if prefix == "" || null, then it is treated as an invalid attempt to
define the default Namespace and an XMLStreamException is thrown

**Since:** 1.6
**See Also:** XMLOutputFactory

,

XMLStreamReader

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void writeStartElement​(
String
localName)
throws
XMLStreamException

Writes a start tag to the output. All writeStartElement methods
open a new scope in the internal namespace context. Writing the
corresponding EndElement causes the scope to be closed.

**Parameters:**
- localName

- local name of the tag, may not be null

**Throws:**
- XMLStreamException

---

#### void writeStartElement​(
String
namespaceURI,

String
localName)
throws
XMLStreamException

Writes a start tag to the output

**Parameters:**
- namespaceURI

- the namespaceURI of the prefix to use, may not be null
- localName

- local name of the tag, may not be null

**Throws:**
- XMLStreamException

- if the namespace URI has not been bound to a prefix and
javax.xml.stream.isRepairingNamespaces has not been set to true

---

#### void writeStartElement​(
String
prefix,

String
localName,

String
namespaceURI)
throws
XMLStreamException

Writes a start tag to the output

**Parameters:**
- localName

- local name of the tag, may not be null
- prefix

- the prefix of the tag, may not be null
- namespaceURI

- the uri to bind the prefix to, may not be null

**Throws:**
- XMLStreamException

---

#### void writeEmptyElement​(
String
namespaceURI,

String
localName)
throws
XMLStreamException

Writes an empty element tag to the output

**Parameters:**
- namespaceURI

- the uri to bind the tag to, may not be null
- localName

- local name of the tag, may not be null

**Throws:**
- XMLStreamException

- if the namespace URI has not been bound to a prefix and
javax.xml.stream.isRepairingNamespaces has not been set to true

---

#### void writeEmptyElement​(
String
prefix,

String
localName,

String
namespaceURI)
throws
XMLStreamException

Writes an empty element tag to the output

**Parameters:**
- prefix

- the prefix of the tag, may not be null
- localName

- local name of the tag, may not be null
- namespaceURI

- the uri to bind the tag to, may not be null

**Throws:**
- XMLStreamException

---

#### void writeEmptyElement​(
String
localName)
throws
XMLStreamException

Writes an empty element tag to the output

**Parameters:**
- localName

- local name of the tag, may not be null

**Throws:**
- XMLStreamException

---

#### void writeEndElement()
throws
XMLStreamException

Writes an end tag to the output relying on the internal
state of the writer to determine the prefix and local name
of the event.

**Throws:**
- XMLStreamException

---

#### void writeEndDocument()
throws
XMLStreamException

Closes any start tags and writes corresponding end tags.

**Throws:**
- XMLStreamException

---

#### void close()
throws
XMLStreamException

Close this writer and free any resources associated with the
writer. This must not close the underlying output stream.

**Throws:**
- XMLStreamException

---

#### void flush()
throws
XMLStreamException

Write any cached data to the underlying output mechanism.

**Throws:**
- XMLStreamException

---

#### void writeAttribute​(
String
localName,

String
value)
throws
XMLStreamException

Writes an attribute to the output stream without
a prefix.

**Parameters:**
- localName

- the local name of the attribute
- value

- the value of the attribute

**Throws:**
- IllegalStateException

- if the current state does not allow Attribute writing
- XMLStreamException

---

#### void writeAttribute​(
String
prefix,

String
namespaceURI,

String
localName,

String
value)
throws
XMLStreamException

Writes an attribute to the output stream

**Parameters:**
- prefix

- the prefix for this attribute
- namespaceURI

- the uri of the prefix for this attribute
- localName

- the local name of the attribute
- value

- the value of the attribute

**Throws:**
- IllegalStateException

- if the current state does not allow Attribute writing
- XMLStreamException

- if the namespace URI has not been bound to a prefix and
javax.xml.stream.isRepairingNamespaces has not been set to true

---

#### void writeAttribute​(
String
namespaceURI,

String
localName,

String
value)
throws
XMLStreamException

Writes an attribute to the output stream

**Parameters:**
- namespaceURI

- the uri of the prefix for this attribute
- localName

- the local name of the attribute
- value

- the value of the attribute

**Throws:**
- IllegalStateException

- if the current state does not allow Attribute writing
- XMLStreamException

- if the namespace URI has not been bound to a prefix and
javax.xml.stream.isRepairingNamespaces has not been set to true

---

#### void writeNamespace​(
String
prefix,

String
namespaceURI)
throws
XMLStreamException

Writes a namespace to the output stream
If the prefix argument to this method is the empty string,
"xmlns", or null this method will delegate to writeDefaultNamespace

**Parameters:**
- prefix

- the prefix to bind this namespace to
- namespaceURI

- the uri to bind the prefix to

**Throws:**
- IllegalStateException

- if the current state does not allow Namespace writing
- XMLStreamException

---

#### void writeDefaultNamespace​(
String
namespaceURI)
throws
XMLStreamException

Writes the default namespace to the stream

**Parameters:**
- namespaceURI

- the uri to bind the default namespace to

**Throws:**
- IllegalStateException

- if the current state does not allow Namespace writing
- XMLStreamException

---

#### void writeComment​(
String
data)
throws
XMLStreamException

Writes an xml comment with the data enclosed

**Parameters:**
- data

- the data contained in the comment, may be null

**Throws:**
- XMLStreamException

---

#### void writeProcessingInstruction​(
String
target)
throws
XMLStreamException

Writes a processing instruction

**Parameters:**
- target

- the target of the processing instruction, may not be null

**Throws:**
- XMLStreamException

---

#### void writeProcessingInstruction​(
String
target,

String
data)
throws
XMLStreamException

Writes a processing instruction

**Parameters:**
- target

- the target of the processing instruction, may not be null
- data

- the data contained in the processing instruction, may not be null

**Throws:**
- XMLStreamException

---

#### void writeCData​(
String
data)
throws
XMLStreamException

Writes a CData section

**Parameters:**
- data

- the data contained in the CData Section, may not be null

**Throws:**
- XMLStreamException

---

#### void writeDTD​(
String
dtd)
throws
XMLStreamException

Write a DTD section. This string represents the entire doctypedecl production
from the XML 1.0 specification.

**Parameters:**
- dtd

- the DTD to be written

**Throws:**
- XMLStreamException

---

#### void writeEntityRef​(
String
name)
throws
XMLStreamException

Writes an entity reference

**Parameters:**
- name

- the name of the entity

**Throws:**
- XMLStreamException

---

#### void writeStartDocument()
throws
XMLStreamException

Write the XML Declaration. Defaults the XML version to 1.0, and the encoding to utf-8

**Throws:**
- XMLStreamException

---

#### void writeStartDocument​(
String
version)
throws
XMLStreamException

Write the XML Declaration. Defaults the XML version to 1.0

**Parameters:**
- version

- version of the xml document

**Throws:**
- XMLStreamException

---

#### void writeStartDocument​(
String
encoding,

String
version)
throws
XMLStreamException

Write the XML Declaration. Note that the encoding parameter does
not set the actual encoding of the underlying output. That must
be set when the instance of the XMLStreamWriter is created using the
XMLOutputFactory

**Parameters:**
- encoding

- encoding of the xml declaration
- version

- version of the xml document

**Throws:**
- XMLStreamException

- If given encoding does not match encoding
of the underlying stream

---

#### void writeCharacters​(
String
text)
throws
XMLStreamException

Write text to the output

**Parameters:**
- text

- the value to write

**Throws:**
- XMLStreamException

---

#### void writeCharacters​(char[] text,
int start,
int len)
throws
XMLStreamException

Write text to the output

**Parameters:**
- text

- the value to write
- start

- the starting position in the array
- len

- the number of characters to write

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

**Returns:**
- the prefix or null

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

- the prefix to bind to the uri, may not be null
- uri

- the uri to bind to the prefix, may be null

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

- the uri to bind to the default namespace, may be null

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
namespaces. This method may only be called once at the start of
the document. It does not cause the namespaces to be declared.
If a namespace URI to prefix mapping is found in the namespace
context it is treated as declared and the prefix may be used
by the StreamWriter.

**Parameters:**
- context

- the namespace context to use for this writer, may not be null

**Throws:**
- XMLStreamException

---

#### NamespaceContext
getNamespaceContext()

Returns the current namespace context.

**Returns:**
- the current NamespaceContext

---

#### Object
getProperty​(
String
name)
throws
IllegalArgumentException

Get the value of a feature/property from the underlying implementation

**Parameters:**
- name

- The name of the property, may not be null

**Returns:**
- The value of the property

**Throws:**
- IllegalArgumentException

- if the property is not supported
- NullPointerException

- if the name is null

---

### Additional Sections

#### Interface XMLStreamWriter

```java
public interface
XMLStreamWriter
```

The XMLStreamWriter interface specifies how to write XML. The XMLStreamWriter does
not perform well formedness checking on its input. However
the writeCharacters method is required to escape &, < and >
For attribute values the writeAttribute method will escape the
above characters plus " to ensure that all character content
and attribute values are well formed.

Each NAMESPACE
and ATTRIBUTE must be individually written.

XML Namespaces,

javax.xml.stream.isRepairingNamespaces

and write method behaviour

Method

method

isRepairingNamespaces

== true

isRepairingNamespaces

== false

method

namespaceURI bound

namespaceURI unbound

namespaceURI bound

namespaceURI unbound

writeAttribute(namespaceURI, localName, value)

isRepairingNamespaces == true

namespaceURI bound

prefix:localName="value"

[1]

namespaceURI unbound

xmlns:{generated}="namespaceURI" {generated}:localName="value"

isRepairingNamespaces == false

namespaceURI bound

prefix:localName="value"

[1]

namespaceURI unbound

XMLStreamException

writeAttribute(prefix, namespaceURI, localName, value)

isRepairingNamespaces == true

namespaceURI bound

bound to same prefix:

prefix:localName="value"

[1]

bound to different prefix:

xmlns:{generated}="namespaceURI" {generated}:localName="value"

namespaceURI unbound

xmlns:prefix="namespaceURI" prefix:localName="value"

[3]

isRepairingNamespaces == false

namespaceURI bound

bound to same prefix:

prefix:localName="value"

[1][2]

bound to different prefix:

XMLStreamException

[2]

namespaceURI unbound

xmlns:prefix="namespaceURI" prefix:localName="value"

[2][5]

writeStartElement(namespaceURI, localName)

writeEmptyElement(namespaceURI, localName)

isRepairingNamespaces == true

namespaceURI bound

<prefix:localName>

[1]

namespaceURI unbound

<{generated}:localName xmlns:{generated}="namespaceURI">

isRepairingNamespaces == false

namespaceURI bound

prefix:localName>

[1]

namespaceURI unbound

XMLStreamException

writeStartElement(prefix, localName, namespaceURI)

writeEmptyElement(prefix, localName, namespaceURI)

isRepairingNamespaces == true

namespaceURI bound

bound to same prefix:

<prefix:localName>

[1]

bound to different prefix:

<{generated}:localName xmlns:{generated}="namespaceURI">

namespaceURI unbound

<prefix:localName xmlns:prefix="namespaceURI">

[4]

isRepairingNamespaces == false

namespaceURI bound

bound to same prefix:

<prefix:localName>

[1]

bound to different prefix:

XMLStreamException

namespaceURI unbound

<prefix:localName>

Notes:

- [1] if namespaceURI == default Namespace URI, then no prefix is written
- [2] if prefix == "" || null && namespaceURI == "", then
no prefix or Namespace declaration is generated or written
- [3] if prefix == "" || null, then a prefix is randomly generated
- [4] if prefix == "" || null, then it is treated as the default Namespace and
no prefix is generated or written, an xmlns declaration is generated
and written if the namespaceURI is unbound
- [5] if prefix == "" || null, then it is treated as an invalid attempt to
define the default Namespace and an XMLStreamException is thrown

**Since:** 1.6
**See Also:** XMLOutputFactory

,

XMLStreamReader

public interface

XMLStreamWriter

The XMLStreamWriter interface specifies how to write XML. The XMLStreamWriter does
not perform well formedness checking on its input. However
the writeCharacters method is required to escape &, < and >
For attribute values the writeAttribute method will escape the
above characters plus " to ensure that all character content
and attribute values are well formed.

Each NAMESPACE
and ATTRIBUTE must be individually written.

XML Namespaces,

javax.xml.stream.isRepairingNamespaces

and write method behaviour

Method

method

isRepairingNamespaces

== true

isRepairingNamespaces

== false

method

namespaceURI bound

namespaceURI unbound

namespaceURI bound

namespaceURI unbound

writeAttribute(namespaceURI, localName, value)

isRepairingNamespaces == true

namespaceURI bound

prefix:localName="value"

[1]

namespaceURI unbound

xmlns:{generated}="namespaceURI" {generated}:localName="value"

isRepairingNamespaces == false

namespaceURI bound

prefix:localName="value"

[1]

namespaceURI unbound

XMLStreamException

writeAttribute(prefix, namespaceURI, localName, value)

isRepairingNamespaces == true

namespaceURI bound

bound to same prefix:

prefix:localName="value"

[1]

bound to different prefix:

xmlns:{generated}="namespaceURI" {generated}:localName="value"

namespaceURI unbound

xmlns:prefix="namespaceURI" prefix:localName="value"

[3]

isRepairingNamespaces == false

namespaceURI bound

bound to same prefix:

prefix:localName="value"

[1][2]

bound to different prefix:

XMLStreamException

[2]

namespaceURI unbound

xmlns:prefix="namespaceURI" prefix:localName="value"

[2][5]

writeStartElement(namespaceURI, localName)

writeEmptyElement(namespaceURI, localName)

isRepairingNamespaces == true

namespaceURI bound

<prefix:localName>

[1]

namespaceURI unbound

<{generated}:localName xmlns:{generated}="namespaceURI">

isRepairingNamespaces == false

namespaceURI bound

prefix:localName>

[1]

namespaceURI unbound

XMLStreamException

writeStartElement(prefix, localName, namespaceURI)

writeEmptyElement(prefix, localName, namespaceURI)

isRepairingNamespaces == true

namespaceURI bound

bound to same prefix:

<prefix:localName>

[1]

bound to different prefix:

<{generated}:localName xmlns:{generated}="namespaceURI">

namespaceURI unbound

<prefix:localName xmlns:prefix="namespaceURI">

[4]

isRepairingNamespaces == false

namespaceURI bound

bound to same prefix:

<prefix:localName>

[1]

bound to different prefix:

XMLStreamException

namespaceURI unbound

<prefix:localName>

Notes:

- [1] if namespaceURI == default Namespace URI, then no prefix is written
- [2] if prefix == "" || null && namespaceURI == "", then
no prefix or Namespace declaration is generated or written
- [3] if prefix == "" || null, then a prefix is randomly generated
- [4] if prefix == "" || null, then it is treated as the default Namespace and
no prefix is generated or written, an xmlns declaration is generated
and written if the namespaceURI is unbound
- [5] if prefix == "" || null, then it is treated as an invalid attempt to
define the default Namespace and an XMLStreamException is thrown

[1] if namespaceURI == default Namespace URI, then no prefix is written

[2] if prefix == "" || null && namespaceURI == "", then
no prefix or Namespace declaration is generated or written

[3] if prefix == "" || null, then a prefix is randomly generated

[4] if prefix == "" || null, then it is treated as the default Namespace and
no prefix is generated or written, an xmlns declaration is generated
and written if the namespaceURI is unbound

[5] if prefix == "" || null, then it is treated as an invalid attempt to
define the default Namespace and an XMLStreamException is thrown

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

close

()

Close this writer and free any resources associated with the
writer.

void

flush

()

Write any cached data to the underlying output mechanism.

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

Object

getProperty

​(

String

name)

Get the value of a feature/property from the underlying implementation

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

void

writeAttribute

​(

String

localName,

String

value)

Writes an attribute to the output stream without
a prefix.

void

writeAttribute

​(

String

namespaceURI,

String

localName,

String

value)

Writes an attribute to the output stream

void

writeAttribute

​(

String

prefix,

String

namespaceURI,

String

localName,

String

value)

Writes an attribute to the output stream

void

writeCData

​(

String

data)

Writes a CData section

void

writeCharacters

​(char[] text,
int start,
int len)

Write text to the output

void

writeCharacters

​(

String

text)

Write text to the output

void

writeComment

​(

String

data)

Writes an xml comment with the data enclosed

void

writeDefaultNamespace

​(

String

namespaceURI)

Writes the default namespace to the stream

void

writeDTD

​(

String

dtd)

Write a DTD section.

void

writeEmptyElement

​(

String

localName)

Writes an empty element tag to the output

void

writeEmptyElement

​(

String

namespaceURI,

String

localName)

Writes an empty element tag to the output

void

writeEmptyElement

​(

String

prefix,

String

localName,

String

namespaceURI)

Writes an empty element tag to the output

void

writeEndDocument

()

Closes any start tags and writes corresponding end tags.

void

writeEndElement

()

Writes an end tag to the output relying on the internal
state of the writer to determine the prefix and local name
of the event.

void

writeEntityRef

​(

String

name)

Writes an entity reference

void

writeNamespace

​(

String

prefix,

String

namespaceURI)

Writes a namespace to the output stream
If the prefix argument to this method is the empty string,
"xmlns", or null this method will delegate to writeDefaultNamespace

void

writeProcessingInstruction

​(

String

target)

Writes a processing instruction

void

writeProcessingInstruction

​(

String

target,

String

data)

Writes a processing instruction

void

writeStartDocument

()

Write the XML Declaration.

void

writeStartDocument

​(

String

version)

Write the XML Declaration.

void

writeStartDocument

​(

String

encoding,

String

version)

Write the XML Declaration.

void

writeStartElement

​(

String

localName)

Writes a start tag to the output.

void

writeStartElement

​(

String

namespaceURI,

String

localName)

Writes a start tag to the output

void

writeStartElement

​(

String

prefix,

String

localName,

String

namespaceURI)

Writes a start tag to the output

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

close

()

Close this writer and free any resources associated with the
writer.

void

flush

()

Write any cached data to the underlying output mechanism.

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

Object

getProperty

​(

String

name)

Get the value of a feature/property from the underlying implementation

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

void

writeAttribute

​(

String

localName,

String

value)

Writes an attribute to the output stream without
a prefix.

void

writeAttribute

​(

String

namespaceURI,

String

localName,

String

value)

Writes an attribute to the output stream

void

writeAttribute

​(

String

prefix,

String

namespaceURI,

String

localName,

String

value)

Writes an attribute to the output stream

void

writeCData

​(

String

data)

Writes a CData section

void

writeCharacters

​(char[] text,
int start,
int len)

Write text to the output

void

writeCharacters

​(

String

text)

Write text to the output

void

writeComment

​(

String

data)

Writes an xml comment with the data enclosed

void

writeDefaultNamespace

​(

String

namespaceURI)

Writes the default namespace to the stream

void

writeDTD

​(

String

dtd)

Write a DTD section.

void

writeEmptyElement

​(

String

localName)

Writes an empty element tag to the output

void

writeEmptyElement

​(

String

namespaceURI,

String

localName)

Writes an empty element tag to the output

void

writeEmptyElement

​(

String

prefix,

String

localName,

String

namespaceURI)

Writes an empty element tag to the output

void

writeEndDocument

()

Closes any start tags and writes corresponding end tags.

void

writeEndElement

()

Writes an end tag to the output relying on the internal
state of the writer to determine the prefix and local name
of the event.

void

writeEntityRef

​(

String

name)

Writes an entity reference

void

writeNamespace

​(

String

prefix,

String

namespaceURI)

Writes a namespace to the output stream
If the prefix argument to this method is the empty string,
"xmlns", or null this method will delegate to writeDefaultNamespace

void

writeProcessingInstruction

​(

String

target)

Writes a processing instruction

void

writeProcessingInstruction

​(

String

target,

String

data)

Writes a processing instruction

void

writeStartDocument

()

Write the XML Declaration.

void

writeStartDocument

​(

String

version)

Write the XML Declaration.

void

writeStartDocument

​(

String

encoding,

String

version)

Write the XML Declaration.

void

writeStartElement

​(

String

localName)

Writes a start tag to the output.

void

writeStartElement

​(

String

namespaceURI,

String

localName)

Writes a start tag to the output

void

writeStartElement

​(

String

prefix,

String

localName,

String

namespaceURI)

Writes a start tag to the output

---

#### Method Summary

Close this writer and free any resources associated with the
writer.

Write any cached data to the underlying output mechanism.

Returns the current namespace context.

Gets the prefix the uri is bound to

Get the value of a feature/property from the underlying implementation

Binds a URI to the default namespace
This URI is bound
in the scope of the current START_ELEMENT / END_ELEMENT pair.

Sets the current namespace context for prefix and uri bindings.

Sets the prefix the uri is bound to.

Writes an attribute to the output stream without
a prefix.

Writes an attribute to the output stream

Writes a CData section

Write text to the output

Writes an xml comment with the data enclosed

Writes the default namespace to the stream

Write a DTD section.

Writes an empty element tag to the output

Closes any start tags and writes corresponding end tags.

Writes an end tag to the output relying on the internal
state of the writer to determine the prefix and local name
of the event.

Writes an entity reference

Writes a namespace to the output stream
If the prefix argument to this method is the empty string,
"xmlns", or null this method will delegate to writeDefaultNamespace

Writes a processing instruction

Write the XML Declaration.

Writes a start tag to the output.

Writes a start tag to the output

============ METHOD DETAIL ==========

- Method Detail

- writeStartElement

```java
void writeStartElement​(
String
localName)
throws
XMLStreamException
```

Writes a start tag to the output. All writeStartElement methods
open a new scope in the internal namespace context. Writing the
corresponding EndElement causes the scope to be closed.

**Parameters:** localName

- local name of the tag, may not be null
**Throws:** XMLStreamException

- writeStartElement

```java
void writeStartElement​(
String
namespaceURI,

String
localName)
throws
XMLStreamException
```

Writes a start tag to the output

**Parameters:** namespaceURI

- the namespaceURI of the prefix to use, may not be null
**Parameters:** localName

- local name of the tag, may not be null
**Throws:** XMLStreamException

- if the namespace URI has not been bound to a prefix and
javax.xml.stream.isRepairingNamespaces has not been set to true

- writeStartElement

```java
void writeStartElement​(
String
prefix,

String
localName,

String
namespaceURI)
throws
XMLStreamException
```

Writes a start tag to the output

**Parameters:** localName

- local name of the tag, may not be null
**Parameters:** prefix

- the prefix of the tag, may not be null
**Parameters:** namespaceURI

- the uri to bind the prefix to, may not be null
**Throws:** XMLStreamException

- writeEmptyElement

```java
void writeEmptyElement​(
String
namespaceURI,

String
localName)
throws
XMLStreamException
```

Writes an empty element tag to the output

**Parameters:** namespaceURI

- the uri to bind the tag to, may not be null
**Parameters:** localName

- local name of the tag, may not be null
**Throws:** XMLStreamException

- if the namespace URI has not been bound to a prefix and
javax.xml.stream.isRepairingNamespaces has not been set to true

- writeEmptyElement

```java
void writeEmptyElement​(
String
prefix,

String
localName,

String
namespaceURI)
throws
XMLStreamException
```

Writes an empty element tag to the output

**Parameters:** prefix

- the prefix of the tag, may not be null
**Parameters:** localName

- local name of the tag, may not be null
**Parameters:** namespaceURI

- the uri to bind the tag to, may not be null
**Throws:** XMLStreamException

- writeEmptyElement

```java
void writeEmptyElement​(
String
localName)
throws
XMLStreamException
```

Writes an empty element tag to the output

**Parameters:** localName

- local name of the tag, may not be null
**Throws:** XMLStreamException

- writeEndElement

```java
void writeEndElement()
throws
XMLStreamException
```

Writes an end tag to the output relying on the internal
state of the writer to determine the prefix and local name
of the event.

**Throws:** XMLStreamException

- writeEndDocument

```java
void writeEndDocument()
throws
XMLStreamException
```

Closes any start tags and writes corresponding end tags.

**Throws:** XMLStreamException

- close

```java
void close()
throws
XMLStreamException
```

Close this writer and free any resources associated with the
writer. This must not close the underlying output stream.

**Throws:** XMLStreamException

- flush

```java
void flush()
throws
XMLStreamException
```

Write any cached data to the underlying output mechanism.

**Throws:** XMLStreamException

- writeAttribute

```java
void writeAttribute​(
String
localName,

String
value)
throws
XMLStreamException
```

Writes an attribute to the output stream without
a prefix.

**Parameters:** localName

- the local name of the attribute
**Parameters:** value

- the value of the attribute
**Throws:** IllegalStateException

- if the current state does not allow Attribute writing
**Throws:** XMLStreamException

- writeAttribute

```java
void writeAttribute​(
String
prefix,

String
namespaceURI,

String
localName,

String
value)
throws
XMLStreamException
```

Writes an attribute to the output stream

**Parameters:** prefix

- the prefix for this attribute
**Parameters:** namespaceURI

- the uri of the prefix for this attribute
**Parameters:** localName

- the local name of the attribute
**Parameters:** value

- the value of the attribute
**Throws:** IllegalStateException

- if the current state does not allow Attribute writing
**Throws:** XMLStreamException

- if the namespace URI has not been bound to a prefix and
javax.xml.stream.isRepairingNamespaces has not been set to true

- writeAttribute

```java
void writeAttribute​(
String
namespaceURI,

String
localName,

String
value)
throws
XMLStreamException
```

Writes an attribute to the output stream

**Parameters:** namespaceURI

- the uri of the prefix for this attribute
**Parameters:** localName

- the local name of the attribute
**Parameters:** value

- the value of the attribute
**Throws:** IllegalStateException

- if the current state does not allow Attribute writing
**Throws:** XMLStreamException

- if the namespace URI has not been bound to a prefix and
javax.xml.stream.isRepairingNamespaces has not been set to true

- writeNamespace

```java
void writeNamespace​(
String
prefix,

String
namespaceURI)
throws
XMLStreamException
```

Writes a namespace to the output stream
If the prefix argument to this method is the empty string,
"xmlns", or null this method will delegate to writeDefaultNamespace

**Parameters:** prefix

- the prefix to bind this namespace to
**Parameters:** namespaceURI

- the uri to bind the prefix to
**Throws:** IllegalStateException

- if the current state does not allow Namespace writing
**Throws:** XMLStreamException

- writeDefaultNamespace

```java
void writeDefaultNamespace​(
String
namespaceURI)
throws
XMLStreamException
```

Writes the default namespace to the stream

**Parameters:** namespaceURI

- the uri to bind the default namespace to
**Throws:** IllegalStateException

- if the current state does not allow Namespace writing
**Throws:** XMLStreamException

- writeComment

```java
void writeComment​(
String
data)
throws
XMLStreamException
```

Writes an xml comment with the data enclosed

**Parameters:** data

- the data contained in the comment, may be null
**Throws:** XMLStreamException

- writeProcessingInstruction

```java
void writeProcessingInstruction​(
String
target)
throws
XMLStreamException
```

Writes a processing instruction

**Parameters:** target

- the target of the processing instruction, may not be null
**Throws:** XMLStreamException

- writeProcessingInstruction

```java
void writeProcessingInstruction​(
String
target,

String
data)
throws
XMLStreamException
```

Writes a processing instruction

**Parameters:** target

- the target of the processing instruction, may not be null
**Parameters:** data

- the data contained in the processing instruction, may not be null
**Throws:** XMLStreamException

- writeCData

```java
void writeCData​(
String
data)
throws
XMLStreamException
```

Writes a CData section

**Parameters:** data

- the data contained in the CData Section, may not be null
**Throws:** XMLStreamException

- writeDTD

```java
void writeDTD​(
String
dtd)
throws
XMLStreamException
```

Write a DTD section. This string represents the entire doctypedecl production
from the XML 1.0 specification.

**Parameters:** dtd

- the DTD to be written
**Throws:** XMLStreamException

- writeEntityRef

```java
void writeEntityRef​(
String
name)
throws
XMLStreamException
```

Writes an entity reference

**Parameters:** name

- the name of the entity
**Throws:** XMLStreamException

- writeStartDocument

```java
void writeStartDocument()
throws
XMLStreamException
```

Write the XML Declaration. Defaults the XML version to 1.0, and the encoding to utf-8

**Throws:** XMLStreamException

- writeStartDocument

```java
void writeStartDocument​(
String
version)
throws
XMLStreamException
```

Write the XML Declaration. Defaults the XML version to 1.0

**Parameters:** version

- version of the xml document
**Throws:** XMLStreamException

- writeStartDocument

```java
void writeStartDocument​(
String
encoding,

String
version)
throws
XMLStreamException
```

Write the XML Declaration. Note that the encoding parameter does
not set the actual encoding of the underlying output. That must
be set when the instance of the XMLStreamWriter is created using the
XMLOutputFactory

**Parameters:** encoding

- encoding of the xml declaration
**Parameters:** version

- version of the xml document
**Throws:** XMLStreamException

- If given encoding does not match encoding
of the underlying stream

- writeCharacters

```java
void writeCharacters​(
String
text)
throws
XMLStreamException
```

Write text to the output

**Parameters:** text

- the value to write
**Throws:** XMLStreamException

- writeCharacters

```java
void writeCharacters​(char[] text,
int start,
int len)
throws
XMLStreamException
```

Write text to the output

**Parameters:** text

- the value to write
**Parameters:** start

- the starting position in the array
**Parameters:** len

- the number of characters to write
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

**Returns:** the prefix or null
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

- the prefix to bind to the uri, may not be null
**Parameters:** uri

- the uri to bind to the prefix, may be null
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

- the uri to bind to the default namespace, may be null
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
namespaces. This method may only be called once at the start of
the document. It does not cause the namespaces to be declared.
If a namespace URI to prefix mapping is found in the namespace
context it is treated as declared and the prefix may be used
by the StreamWriter.

**Parameters:** context

- the namespace context to use for this writer, may not be null
**Throws:** XMLStreamException

- getNamespaceContext

```java
NamespaceContext
getNamespaceContext()
```

Returns the current namespace context.

**Returns:** the current NamespaceContext

- getProperty

```java
Object
getProperty​(
String
name)
throws
IllegalArgumentException
```

Get the value of a feature/property from the underlying implementation

**Parameters:** name

- The name of the property, may not be null
**Returns:** The value of the property
**Throws:** IllegalArgumentException

- if the property is not supported
**Throws:** NullPointerException

- if the name is null

Method Detail

- writeStartElement

```java
void writeStartElement​(
String
localName)
throws
XMLStreamException
```

Writes a start tag to the output. All writeStartElement methods
open a new scope in the internal namespace context. Writing the
corresponding EndElement causes the scope to be closed.

**Parameters:** localName

- local name of the tag, may not be null
**Throws:** XMLStreamException

- writeStartElement

```java
void writeStartElement​(
String
namespaceURI,

String
localName)
throws
XMLStreamException
```

Writes a start tag to the output

**Parameters:** namespaceURI

- the namespaceURI of the prefix to use, may not be null
**Parameters:** localName

- local name of the tag, may not be null
**Throws:** XMLStreamException

- if the namespace URI has not been bound to a prefix and
javax.xml.stream.isRepairingNamespaces has not been set to true

- writeStartElement

```java
void writeStartElement​(
String
prefix,

String
localName,

String
namespaceURI)
throws
XMLStreamException
```

Writes a start tag to the output

**Parameters:** localName

- local name of the tag, may not be null
**Parameters:** prefix

- the prefix of the tag, may not be null
**Parameters:** namespaceURI

- the uri to bind the prefix to, may not be null
**Throws:** XMLStreamException

- writeEmptyElement

```java
void writeEmptyElement​(
String
namespaceURI,

String
localName)
throws
XMLStreamException
```

Writes an empty element tag to the output

**Parameters:** namespaceURI

- the uri to bind the tag to, may not be null
**Parameters:** localName

- local name of the tag, may not be null
**Throws:** XMLStreamException

- if the namespace URI has not been bound to a prefix and
javax.xml.stream.isRepairingNamespaces has not been set to true

- writeEmptyElement

```java
void writeEmptyElement​(
String
prefix,

String
localName,

String
namespaceURI)
throws
XMLStreamException
```

Writes an empty element tag to the output

**Parameters:** prefix

- the prefix of the tag, may not be null
**Parameters:** localName

- local name of the tag, may not be null
**Parameters:** namespaceURI

- the uri to bind the tag to, may not be null
**Throws:** XMLStreamException

- writeEmptyElement

```java
void writeEmptyElement​(
String
localName)
throws
XMLStreamException
```

Writes an empty element tag to the output

**Parameters:** localName

- local name of the tag, may not be null
**Throws:** XMLStreamException

- writeEndElement

```java
void writeEndElement()
throws
XMLStreamException
```

Writes an end tag to the output relying on the internal
state of the writer to determine the prefix and local name
of the event.

**Throws:** XMLStreamException

- writeEndDocument

```java
void writeEndDocument()
throws
XMLStreamException
```

Closes any start tags and writes corresponding end tags.

**Throws:** XMLStreamException

- close

```java
void close()
throws
XMLStreamException
```

Close this writer and free any resources associated with the
writer. This must not close the underlying output stream.

**Throws:** XMLStreamException

- flush

```java
void flush()
throws
XMLStreamException
```

Write any cached data to the underlying output mechanism.

**Throws:** XMLStreamException

- writeAttribute

```java
void writeAttribute​(
String
localName,

String
value)
throws
XMLStreamException
```

Writes an attribute to the output stream without
a prefix.

**Parameters:** localName

- the local name of the attribute
**Parameters:** value

- the value of the attribute
**Throws:** IllegalStateException

- if the current state does not allow Attribute writing
**Throws:** XMLStreamException

- writeAttribute

```java
void writeAttribute​(
String
prefix,

String
namespaceURI,

String
localName,

String
value)
throws
XMLStreamException
```

Writes an attribute to the output stream

**Parameters:** prefix

- the prefix for this attribute
**Parameters:** namespaceURI

- the uri of the prefix for this attribute
**Parameters:** localName

- the local name of the attribute
**Parameters:** value

- the value of the attribute
**Throws:** IllegalStateException

- if the current state does not allow Attribute writing
**Throws:** XMLStreamException

- if the namespace URI has not been bound to a prefix and
javax.xml.stream.isRepairingNamespaces has not been set to true

- writeAttribute

```java
void writeAttribute​(
String
namespaceURI,

String
localName,

String
value)
throws
XMLStreamException
```

Writes an attribute to the output stream

**Parameters:** namespaceURI

- the uri of the prefix for this attribute
**Parameters:** localName

- the local name of the attribute
**Parameters:** value

- the value of the attribute
**Throws:** IllegalStateException

- if the current state does not allow Attribute writing
**Throws:** XMLStreamException

- if the namespace URI has not been bound to a prefix and
javax.xml.stream.isRepairingNamespaces has not been set to true

- writeNamespace

```java
void writeNamespace​(
String
prefix,

String
namespaceURI)
throws
XMLStreamException
```

Writes a namespace to the output stream
If the prefix argument to this method is the empty string,
"xmlns", or null this method will delegate to writeDefaultNamespace

**Parameters:** prefix

- the prefix to bind this namespace to
**Parameters:** namespaceURI

- the uri to bind the prefix to
**Throws:** IllegalStateException

- if the current state does not allow Namespace writing
**Throws:** XMLStreamException

- writeDefaultNamespace

```java
void writeDefaultNamespace​(
String
namespaceURI)
throws
XMLStreamException
```

Writes the default namespace to the stream

**Parameters:** namespaceURI

- the uri to bind the default namespace to
**Throws:** IllegalStateException

- if the current state does not allow Namespace writing
**Throws:** XMLStreamException

- writeComment

```java
void writeComment​(
String
data)
throws
XMLStreamException
```

Writes an xml comment with the data enclosed

**Parameters:** data

- the data contained in the comment, may be null
**Throws:** XMLStreamException

- writeProcessingInstruction

```java
void writeProcessingInstruction​(
String
target)
throws
XMLStreamException
```

Writes a processing instruction

**Parameters:** target

- the target of the processing instruction, may not be null
**Throws:** XMLStreamException

- writeProcessingInstruction

```java
void writeProcessingInstruction​(
String
target,

String
data)
throws
XMLStreamException
```

Writes a processing instruction

**Parameters:** target

- the target of the processing instruction, may not be null
**Parameters:** data

- the data contained in the processing instruction, may not be null
**Throws:** XMLStreamException

- writeCData

```java
void writeCData​(
String
data)
throws
XMLStreamException
```

Writes a CData section

**Parameters:** data

- the data contained in the CData Section, may not be null
**Throws:** XMLStreamException

- writeDTD

```java
void writeDTD​(
String
dtd)
throws
XMLStreamException
```

Write a DTD section. This string represents the entire doctypedecl production
from the XML 1.0 specification.

**Parameters:** dtd

- the DTD to be written
**Throws:** XMLStreamException

- writeEntityRef

```java
void writeEntityRef​(
String
name)
throws
XMLStreamException
```

Writes an entity reference

**Parameters:** name

- the name of the entity
**Throws:** XMLStreamException

- writeStartDocument

```java
void writeStartDocument()
throws
XMLStreamException
```

Write the XML Declaration. Defaults the XML version to 1.0, and the encoding to utf-8

**Throws:** XMLStreamException

- writeStartDocument

```java
void writeStartDocument​(
String
version)
throws
XMLStreamException
```

Write the XML Declaration. Defaults the XML version to 1.0

**Parameters:** version

- version of the xml document
**Throws:** XMLStreamException

- writeStartDocument

```java
void writeStartDocument​(
String
encoding,

String
version)
throws
XMLStreamException
```

Write the XML Declaration. Note that the encoding parameter does
not set the actual encoding of the underlying output. That must
be set when the instance of the XMLStreamWriter is created using the
XMLOutputFactory

**Parameters:** encoding

- encoding of the xml declaration
**Parameters:** version

- version of the xml document
**Throws:** XMLStreamException

- If given encoding does not match encoding
of the underlying stream

- writeCharacters

```java
void writeCharacters​(
String
text)
throws
XMLStreamException
```

Write text to the output

**Parameters:** text

- the value to write
**Throws:** XMLStreamException

- writeCharacters

```java
void writeCharacters​(char[] text,
int start,
int len)
throws
XMLStreamException
```

Write text to the output

**Parameters:** text

- the value to write
**Parameters:** start

- the starting position in the array
**Parameters:** len

- the number of characters to write
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

**Returns:** the prefix or null
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

- the prefix to bind to the uri, may not be null
**Parameters:** uri

- the uri to bind to the prefix, may be null
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

- the uri to bind to the default namespace, may be null
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
namespaces. This method may only be called once at the start of
the document. It does not cause the namespaces to be declared.
If a namespace URI to prefix mapping is found in the namespace
context it is treated as declared and the prefix may be used
by the StreamWriter.

**Parameters:** context

- the namespace context to use for this writer, may not be null
**Throws:** XMLStreamException

- getNamespaceContext

```java
NamespaceContext
getNamespaceContext()
```

Returns the current namespace context.

**Returns:** the current NamespaceContext

- getProperty

```java
Object
getProperty​(
String
name)
throws
IllegalArgumentException
```

Get the value of a feature/property from the underlying implementation

**Parameters:** name

- The name of the property, may not be null
**Returns:** The value of the property
**Throws:** IllegalArgumentException

- if the property is not supported
**Throws:** NullPointerException

- if the name is null

---

#### Method Detail

writeStartElement

```java
void writeStartElement​(
String
localName)
throws
XMLStreamException
```

Writes a start tag to the output. All writeStartElement methods
open a new scope in the internal namespace context. Writing the
corresponding EndElement causes the scope to be closed.

**Parameters:** localName

- local name of the tag, may not be null
**Throws:** XMLStreamException

---

#### writeStartElement

void writeStartElement​(

String

localName)
throws

XMLStreamException

Writes a start tag to the output. All writeStartElement methods
open a new scope in the internal namespace context. Writing the
corresponding EndElement causes the scope to be closed.

writeStartElement

```java
void writeStartElement​(
String
namespaceURI,

String
localName)
throws
XMLStreamException
```

Writes a start tag to the output

**Parameters:** namespaceURI

- the namespaceURI of the prefix to use, may not be null
**Parameters:** localName

- local name of the tag, may not be null
**Throws:** XMLStreamException

- if the namespace URI has not been bound to a prefix and
javax.xml.stream.isRepairingNamespaces has not been set to true

---

#### writeStartElement

void writeStartElement​(

String

namespaceURI,

String

localName)
throws

XMLStreamException

Writes a start tag to the output

writeStartElement

```java
void writeStartElement​(
String
prefix,

String
localName,

String
namespaceURI)
throws
XMLStreamException
```

Writes a start tag to the output

**Parameters:** localName

- local name of the tag, may not be null
**Parameters:** prefix

- the prefix of the tag, may not be null
**Parameters:** namespaceURI

- the uri to bind the prefix to, may not be null
**Throws:** XMLStreamException

---

#### writeStartElement

void writeStartElement​(

String

prefix,

String

localName,

String

namespaceURI)
throws

XMLStreamException

Writes a start tag to the output

writeEmptyElement

```java
void writeEmptyElement​(
String
namespaceURI,

String
localName)
throws
XMLStreamException
```

Writes an empty element tag to the output

**Parameters:** namespaceURI

- the uri to bind the tag to, may not be null
**Parameters:** localName

- local name of the tag, may not be null
**Throws:** XMLStreamException

- if the namespace URI has not been bound to a prefix and
javax.xml.stream.isRepairingNamespaces has not been set to true

---

#### writeEmptyElement

void writeEmptyElement​(

String

namespaceURI,

String

localName)
throws

XMLStreamException

Writes an empty element tag to the output

writeEmptyElement

```java
void writeEmptyElement​(
String
prefix,

String
localName,

String
namespaceURI)
throws
XMLStreamException
```

Writes an empty element tag to the output

**Parameters:** prefix

- the prefix of the tag, may not be null
**Parameters:** localName

- local name of the tag, may not be null
**Parameters:** namespaceURI

- the uri to bind the tag to, may not be null
**Throws:** XMLStreamException

---

#### writeEmptyElement

void writeEmptyElement​(

String

prefix,

String

localName,

String

namespaceURI)
throws

XMLStreamException

Writes an empty element tag to the output

writeEmptyElement

```java
void writeEmptyElement​(
String
localName)
throws
XMLStreamException
```

Writes an empty element tag to the output

**Parameters:** localName

- local name of the tag, may not be null
**Throws:** XMLStreamException

---

#### writeEmptyElement

void writeEmptyElement​(

String

localName)
throws

XMLStreamException

Writes an empty element tag to the output

writeEndElement

```java
void writeEndElement()
throws
XMLStreamException
```

Writes an end tag to the output relying on the internal
state of the writer to determine the prefix and local name
of the event.

**Throws:** XMLStreamException

---

#### writeEndElement

void writeEndElement()
throws

XMLStreamException

Writes an end tag to the output relying on the internal
state of the writer to determine the prefix and local name
of the event.

writeEndDocument

```java
void writeEndDocument()
throws
XMLStreamException
```

Closes any start tags and writes corresponding end tags.

**Throws:** XMLStreamException

---

#### writeEndDocument

void writeEndDocument()
throws

XMLStreamException

Closes any start tags and writes corresponding end tags.

close

```java
void close()
throws
XMLStreamException
```

Close this writer and free any resources associated with the
writer. This must not close the underlying output stream.

**Throws:** XMLStreamException

---

#### close

void close()
throws

XMLStreamException

Close this writer and free any resources associated with the
writer. This must not close the underlying output stream.

flush

```java
void flush()
throws
XMLStreamException
```

Write any cached data to the underlying output mechanism.

**Throws:** XMLStreamException

---

#### flush

void flush()
throws

XMLStreamException

Write any cached data to the underlying output mechanism.

writeAttribute

```java
void writeAttribute​(
String
localName,

String
value)
throws
XMLStreamException
```

Writes an attribute to the output stream without
a prefix.

**Parameters:** localName

- the local name of the attribute
**Parameters:** value

- the value of the attribute
**Throws:** IllegalStateException

- if the current state does not allow Attribute writing
**Throws:** XMLStreamException

---

#### writeAttribute

void writeAttribute​(

String

localName,

String

value)
throws

XMLStreamException

Writes an attribute to the output stream without
a prefix.

writeAttribute

```java
void writeAttribute​(
String
prefix,

String
namespaceURI,

String
localName,

String
value)
throws
XMLStreamException
```

Writes an attribute to the output stream

**Parameters:** prefix

- the prefix for this attribute
**Parameters:** namespaceURI

- the uri of the prefix for this attribute
**Parameters:** localName

- the local name of the attribute
**Parameters:** value

- the value of the attribute
**Throws:** IllegalStateException

- if the current state does not allow Attribute writing
**Throws:** XMLStreamException

- if the namespace URI has not been bound to a prefix and
javax.xml.stream.isRepairingNamespaces has not been set to true

---

#### writeAttribute

void writeAttribute​(

String

prefix,

String

namespaceURI,

String

localName,

String

value)
throws

XMLStreamException

Writes an attribute to the output stream

writeAttribute

```java
void writeAttribute​(
String
namespaceURI,

String
localName,

String
value)
throws
XMLStreamException
```

Writes an attribute to the output stream

**Parameters:** namespaceURI

- the uri of the prefix for this attribute
**Parameters:** localName

- the local name of the attribute
**Parameters:** value

- the value of the attribute
**Throws:** IllegalStateException

- if the current state does not allow Attribute writing
**Throws:** XMLStreamException

- if the namespace URI has not been bound to a prefix and
javax.xml.stream.isRepairingNamespaces has not been set to true

---

#### writeAttribute

void writeAttribute​(

String

namespaceURI,

String

localName,

String

value)
throws

XMLStreamException

Writes an attribute to the output stream

writeNamespace

```java
void writeNamespace​(
String
prefix,

String
namespaceURI)
throws
XMLStreamException
```

Writes a namespace to the output stream
If the prefix argument to this method is the empty string,
"xmlns", or null this method will delegate to writeDefaultNamespace

**Parameters:** prefix

- the prefix to bind this namespace to
**Parameters:** namespaceURI

- the uri to bind the prefix to
**Throws:** IllegalStateException

- if the current state does not allow Namespace writing
**Throws:** XMLStreamException

---

#### writeNamespace

void writeNamespace​(

String

prefix,

String

namespaceURI)
throws

XMLStreamException

Writes a namespace to the output stream
If the prefix argument to this method is the empty string,
"xmlns", or null this method will delegate to writeDefaultNamespace

writeDefaultNamespace

```java
void writeDefaultNamespace​(
String
namespaceURI)
throws
XMLStreamException
```

Writes the default namespace to the stream

**Parameters:** namespaceURI

- the uri to bind the default namespace to
**Throws:** IllegalStateException

- if the current state does not allow Namespace writing
**Throws:** XMLStreamException

---

#### writeDefaultNamespace

void writeDefaultNamespace​(

String

namespaceURI)
throws

XMLStreamException

Writes the default namespace to the stream

writeComment

```java
void writeComment​(
String
data)
throws
XMLStreamException
```

Writes an xml comment with the data enclosed

**Parameters:** data

- the data contained in the comment, may be null
**Throws:** XMLStreamException

---

#### writeComment

void writeComment​(

String

data)
throws

XMLStreamException

Writes an xml comment with the data enclosed

writeProcessingInstruction

```java
void writeProcessingInstruction​(
String
target)
throws
XMLStreamException
```

Writes a processing instruction

**Parameters:** target

- the target of the processing instruction, may not be null
**Throws:** XMLStreamException

---

#### writeProcessingInstruction

void writeProcessingInstruction​(

String

target)
throws

XMLStreamException

Writes a processing instruction

writeProcessingInstruction

```java
void writeProcessingInstruction​(
String
target,

String
data)
throws
XMLStreamException
```

Writes a processing instruction

**Parameters:** target

- the target of the processing instruction, may not be null
**Parameters:** data

- the data contained in the processing instruction, may not be null
**Throws:** XMLStreamException

---

#### writeProcessingInstruction

void writeProcessingInstruction​(

String

target,

String

data)
throws

XMLStreamException

Writes a processing instruction

writeCData

```java
void writeCData​(
String
data)
throws
XMLStreamException
```

Writes a CData section

**Parameters:** data

- the data contained in the CData Section, may not be null
**Throws:** XMLStreamException

---

#### writeCData

void writeCData​(

String

data)
throws

XMLStreamException

Writes a CData section

writeDTD

```java
void writeDTD​(
String
dtd)
throws
XMLStreamException
```

Write a DTD section. This string represents the entire doctypedecl production
from the XML 1.0 specification.

**Parameters:** dtd

- the DTD to be written
**Throws:** XMLStreamException

---

#### writeDTD

void writeDTD​(

String

dtd)
throws

XMLStreamException

Write a DTD section. This string represents the entire doctypedecl production
from the XML 1.0 specification.

writeEntityRef

```java
void writeEntityRef​(
String
name)
throws
XMLStreamException
```

Writes an entity reference

**Parameters:** name

- the name of the entity
**Throws:** XMLStreamException

---

#### writeEntityRef

void writeEntityRef​(

String

name)
throws

XMLStreamException

Writes an entity reference

writeStartDocument

```java
void writeStartDocument()
throws
XMLStreamException
```

Write the XML Declaration. Defaults the XML version to 1.0, and the encoding to utf-8

**Throws:** XMLStreamException

---

#### writeStartDocument

void writeStartDocument()
throws

XMLStreamException

Write the XML Declaration. Defaults the XML version to 1.0, and the encoding to utf-8

writeStartDocument

```java
void writeStartDocument​(
String
version)
throws
XMLStreamException
```

Write the XML Declaration. Defaults the XML version to 1.0

**Parameters:** version

- version of the xml document
**Throws:** XMLStreamException

---

#### writeStartDocument

void writeStartDocument​(

String

version)
throws

XMLStreamException

Write the XML Declaration. Defaults the XML version to 1.0

writeStartDocument

```java
void writeStartDocument​(
String
encoding,

String
version)
throws
XMLStreamException
```

Write the XML Declaration. Note that the encoding parameter does
not set the actual encoding of the underlying output. That must
be set when the instance of the XMLStreamWriter is created using the
XMLOutputFactory

**Parameters:** encoding

- encoding of the xml declaration
**Parameters:** version

- version of the xml document
**Throws:** XMLStreamException

- If given encoding does not match encoding
of the underlying stream

---

#### writeStartDocument

void writeStartDocument​(

String

encoding,

String

version)
throws

XMLStreamException

Write the XML Declaration. Note that the encoding parameter does
not set the actual encoding of the underlying output. That must
be set when the instance of the XMLStreamWriter is created using the
XMLOutputFactory

writeCharacters

```java
void writeCharacters​(
String
text)
throws
XMLStreamException
```

Write text to the output

**Parameters:** text

- the value to write
**Throws:** XMLStreamException

---

#### writeCharacters

void writeCharacters​(

String

text)
throws

XMLStreamException

Write text to the output

writeCharacters

```java
void writeCharacters​(char[] text,
int start,
int len)
throws
XMLStreamException
```

Write text to the output

**Parameters:** text

- the value to write
**Parameters:** start

- the starting position in the array
**Parameters:** len

- the number of characters to write
**Throws:** XMLStreamException

---

#### writeCharacters

void writeCharacters​(char[] text,
int start,
int len)
throws

XMLStreamException

Write text to the output

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

**Returns:** the prefix or null
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

- the prefix to bind to the uri, may not be null
**Parameters:** uri

- the uri to bind to the prefix, may be null
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

- the uri to bind to the default namespace, may be null
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
namespaces. This method may only be called once at the start of
the document. It does not cause the namespaces to be declared.
If a namespace URI to prefix mapping is found in the namespace
context it is treated as declared and the prefix may be used
by the StreamWriter.

**Parameters:** context

- the namespace context to use for this writer, may not be null
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
namespaces. This method may only be called once at the start of
the document. It does not cause the namespaces to be declared.
If a namespace URI to prefix mapping is found in the namespace
context it is treated as declared and the prefix may be used
by the StreamWriter.

getNamespaceContext

```java
NamespaceContext
getNamespaceContext()
```

Returns the current namespace context.

**Returns:** the current NamespaceContext

---

#### getNamespaceContext

NamespaceContext

getNamespaceContext()

Returns the current namespace context.

getProperty

```java
Object
getProperty​(
String
name)
throws
IllegalArgumentException
```

Get the value of a feature/property from the underlying implementation

**Parameters:** name

- The name of the property, may not be null
**Returns:** The value of the property
**Throws:** IllegalArgumentException

- if the property is not supported
**Throws:** NullPointerException

- if the name is null

---

#### getProperty

Object

getProperty​(

String

name)
throws

IllegalArgumentException

Get the value of a feature/property from the underlying implementation

---

