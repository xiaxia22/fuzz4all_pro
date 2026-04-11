# Interface StartElement

**Source:** `java.xml\javax\xml\stream\events\StartElement.html`

### Class Description

```java
public interface
StartElement

extends
XMLEvent
```

The StartElement interface provides access to information about
start elements. A StartElement is reported for each Start Tag
in the document.

**All Superinterfaces:** XMLEvent

,

XMLStreamConstants

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### QName
getName()

Get the name of this event

**Returns:**
- the qualified name of this event

---

#### Iterator
<
Attribute
> getAttributes()

Returns an Iterator of non-namespace declared attributes declared on
this START_ELEMENT,
returns an empty iterator if there are no attributes. The
iterator must contain only implementations of the javax.xml.stream.Attribute
interface. Attributes are fundamentally unordered and may not be reported
in any order.

**Returns:**
- a readonly Iterator over Attribute interfaces, or an
empty iterator

---

#### Iterator
<
Namespace
> getNamespaces()

Returns an Iterator of namespaces declared on this element.
This Iterator does not contain previously declared namespaces
unless they appear on the current START_ELEMENT.
Therefore this list may contain redeclared namespaces and duplicate namespace
declarations. Use the getNamespaceContext() method to get the
current context of namespace declarations.

The iterator must contain only implementations of the
javax.xml.stream.Namespace interface.

A Namespace isA Attribute. One
can iterate over a list of namespaces as a list of attributes.
However this method returns only the list of namespaces
declared on this START_ELEMENT and does not
include the attributes declared on this START_ELEMENT.

Returns an empty iterator if there are no namespaces.

**Returns:**
- a readonly Iterator over Namespace interfaces, or an
empty iterator

---

#### Attribute
getAttributeByName​(
QName
name)

Returns the attribute referred to by this name

**Parameters:**
- name

- the qname of the desired name

**Returns:**
- the attribute corresponding to the name value or null

---

#### NamespaceContext
getNamespaceContext()

Gets a read-only namespace context. If no context is
available this method will return an empty namespace context.
The NamespaceContext contains information about all namespaces
in scope for this StartElement.

**Returns:**
- the current namespace context

---

#### String
getNamespaceURI​(
String
prefix)

Gets the value that the prefix is bound to in the
context of this element. Returns null if
the prefix is not bound in this context

**Parameters:**
- prefix

- the prefix to lookup

**Returns:**
- the uri bound to the prefix or null

---

### Additional Sections

#### Interface StartElement

**All Superinterfaces:** XMLEvent

,

XMLStreamConstants

```java
public interface
StartElement

extends
XMLEvent
```

The StartElement interface provides access to information about
start elements. A StartElement is reported for each Start Tag
in the document.

**Since:** 1.6

public interface

StartElement

extends

XMLEvent

The StartElement interface provides access to information about
start elements. A StartElement is reported for each Start Tag
in the document.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in interface javax.xml.stream.

XMLStreamConstants

ATTRIBUTE

,

CDATA

,

CHARACTERS

,

COMMENT

,

DTD

,

END_DOCUMENT

,

END_ELEMENT

,

ENTITY_DECLARATION

,

ENTITY_REFERENCE

,

NAMESPACE

,

NOTATION_DECLARATION

,

PROCESSING_INSTRUCTION

,

SPACE

,

START_DOCUMENT

,

START_ELEMENT

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Attribute

getAttributeByName

​(

QName

name)

Returns the attribute referred to by this name

Iterator

<

Attribute

>

getAttributes

()

Returns an Iterator of non-namespace declared attributes declared on
this START_ELEMENT,
returns an empty iterator if there are no attributes.

QName

getName

()

Get the name of this event

NamespaceContext

getNamespaceContext

()

Gets a read-only namespace context.

Iterator

<

Namespace

>

getNamespaces

()

Returns an Iterator of namespaces declared on this element.

String

getNamespaceURI

​(

String

prefix)

Gets the value that the prefix is bound to in the
context of this element.

- Methods declared in interface javax.xml.stream.events.

XMLEvent

asCharacters

,

asEndElement

,

asStartElement

,

getEventType

,

getLocation

,

getSchemaType

,

isAttribute

,

isCharacters

,

isEndDocument

,

isEndElement

,

isEntityReference

,

isNamespace

,

isProcessingInstruction

,

isStartDocument

,

isStartElement

,

writeAsEncodedUnicode

Field Summary

- Fields declared in interface javax.xml.stream.

XMLStreamConstants

ATTRIBUTE

,

CDATA

,

CHARACTERS

,

COMMENT

,

DTD

,

END_DOCUMENT

,

END_ELEMENT

,

ENTITY_DECLARATION

,

ENTITY_REFERENCE

,

NAMESPACE

,

NOTATION_DECLARATION

,

PROCESSING_INSTRUCTION

,

SPACE

,

START_DOCUMENT

,

START_ELEMENT

---

#### Field Summary

Fields declared in interface javax.xml.stream.

XMLStreamConstants

ATTRIBUTE

,

CDATA

,

CHARACTERS

,

COMMENT

,

DTD

,

END_DOCUMENT

,

END_ELEMENT

,

ENTITY_DECLARATION

,

ENTITY_REFERENCE

,

NAMESPACE

,

NOTATION_DECLARATION

,

PROCESSING_INSTRUCTION

,

SPACE

,

START_DOCUMENT

,

START_ELEMENT

---

#### Fields declared in interface javax.xml.stream. XMLStreamConstants

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Attribute

getAttributeByName

​(

QName

name)

Returns the attribute referred to by this name

Iterator

<

Attribute

>

getAttributes

()

Returns an Iterator of non-namespace declared attributes declared on
this START_ELEMENT,
returns an empty iterator if there are no attributes.

QName

getName

()

Get the name of this event

NamespaceContext

getNamespaceContext

()

Gets a read-only namespace context.

Iterator

<

Namespace

>

getNamespaces

()

Returns an Iterator of namespaces declared on this element.

String

getNamespaceURI

​(

String

prefix)

Gets the value that the prefix is bound to in the
context of this element.

- Methods declared in interface javax.xml.stream.events.

XMLEvent

asCharacters

,

asEndElement

,

asStartElement

,

getEventType

,

getLocation

,

getSchemaType

,

isAttribute

,

isCharacters

,

isEndDocument

,

isEndElement

,

isEntityReference

,

isNamespace

,

isProcessingInstruction

,

isStartDocument

,

isStartElement

,

writeAsEncodedUnicode

---

#### Method Summary

Returns the attribute referred to by this name

Returns an Iterator of non-namespace declared attributes declared on
this START_ELEMENT,
returns an empty iterator if there are no attributes.

Get the name of this event

Gets a read-only namespace context.

Returns an Iterator of namespaces declared on this element.

Gets the value that the prefix is bound to in the
context of this element.

Methods declared in interface javax.xml.stream.events.

XMLEvent

asCharacters

,

asEndElement

,

asStartElement

,

getEventType

,

getLocation

,

getSchemaType

,

isAttribute

,

isCharacters

,

isEndDocument

,

isEndElement

,

isEntityReference

,

isNamespace

,

isProcessingInstruction

,

isStartDocument

,

isStartElement

,

writeAsEncodedUnicode

---

#### Methods declared in interface javax.xml.stream.events. XMLEvent

============ METHOD DETAIL ==========

- Method Detail

- getName

```java
QName
getName()
```

Get the name of this event

**Returns:** the qualified name of this event

- getAttributes

```java
Iterator
<
Attribute
> getAttributes()
```

Returns an Iterator of non-namespace declared attributes declared on
this START_ELEMENT,
returns an empty iterator if there are no attributes. The
iterator must contain only implementations of the javax.xml.stream.Attribute
interface. Attributes are fundamentally unordered and may not be reported
in any order.

**Returns:** a readonly Iterator over Attribute interfaces, or an
empty iterator

- getNamespaces

```java
Iterator
<
Namespace
> getNamespaces()
```

Returns an Iterator of namespaces declared on this element.
This Iterator does not contain previously declared namespaces
unless they appear on the current START_ELEMENT.
Therefore this list may contain redeclared namespaces and duplicate namespace
declarations. Use the getNamespaceContext() method to get the
current context of namespace declarations.

The iterator must contain only implementations of the
javax.xml.stream.Namespace interface.

A Namespace isA Attribute. One
can iterate over a list of namespaces as a list of attributes.
However this method returns only the list of namespaces
declared on this START_ELEMENT and does not
include the attributes declared on this START_ELEMENT.

Returns an empty iterator if there are no namespaces.

**Returns:** a readonly Iterator over Namespace interfaces, or an
empty iterator

- getAttributeByName

```java
Attribute
getAttributeByName​(
QName
name)
```

Returns the attribute referred to by this name

**Parameters:** name

- the qname of the desired name
**Returns:** the attribute corresponding to the name value or null

- getNamespaceContext

```java
NamespaceContext
getNamespaceContext()
```

Gets a read-only namespace context. If no context is
available this method will return an empty namespace context.
The NamespaceContext contains information about all namespaces
in scope for this StartElement.

**Returns:** the current namespace context

- getNamespaceURI

```java
String
getNamespaceURI​(
String
prefix)
```

Gets the value that the prefix is bound to in the
context of this element. Returns null if
the prefix is not bound in this context

**Parameters:** prefix

- the prefix to lookup
**Returns:** the uri bound to the prefix or null

Method Detail

- getName

```java
QName
getName()
```

Get the name of this event

**Returns:** the qualified name of this event

- getAttributes

```java
Iterator
<
Attribute
> getAttributes()
```

Returns an Iterator of non-namespace declared attributes declared on
this START_ELEMENT,
returns an empty iterator if there are no attributes. The
iterator must contain only implementations of the javax.xml.stream.Attribute
interface. Attributes are fundamentally unordered and may not be reported
in any order.

**Returns:** a readonly Iterator over Attribute interfaces, or an
empty iterator

- getNamespaces

```java
Iterator
<
Namespace
> getNamespaces()
```

Returns an Iterator of namespaces declared on this element.
This Iterator does not contain previously declared namespaces
unless they appear on the current START_ELEMENT.
Therefore this list may contain redeclared namespaces and duplicate namespace
declarations. Use the getNamespaceContext() method to get the
current context of namespace declarations.

The iterator must contain only implementations of the
javax.xml.stream.Namespace interface.

A Namespace isA Attribute. One
can iterate over a list of namespaces as a list of attributes.
However this method returns only the list of namespaces
declared on this START_ELEMENT and does not
include the attributes declared on this START_ELEMENT.

Returns an empty iterator if there are no namespaces.

**Returns:** a readonly Iterator over Namespace interfaces, or an
empty iterator

- getAttributeByName

```java
Attribute
getAttributeByName​(
QName
name)
```

Returns the attribute referred to by this name

**Parameters:** name

- the qname of the desired name
**Returns:** the attribute corresponding to the name value or null

- getNamespaceContext

```java
NamespaceContext
getNamespaceContext()
```

Gets a read-only namespace context. If no context is
available this method will return an empty namespace context.
The NamespaceContext contains information about all namespaces
in scope for this StartElement.

**Returns:** the current namespace context

- getNamespaceURI

```java
String
getNamespaceURI​(
String
prefix)
```

Gets the value that the prefix is bound to in the
context of this element. Returns null if
the prefix is not bound in this context

**Parameters:** prefix

- the prefix to lookup
**Returns:** the uri bound to the prefix or null

---

#### Method Detail

getName

```java
QName
getName()
```

Get the name of this event

**Returns:** the qualified name of this event

---

#### getName

QName

getName()

Get the name of this event

getAttributes

```java
Iterator
<
Attribute
> getAttributes()
```

Returns an Iterator of non-namespace declared attributes declared on
this START_ELEMENT,
returns an empty iterator if there are no attributes. The
iterator must contain only implementations of the javax.xml.stream.Attribute
interface. Attributes are fundamentally unordered and may not be reported
in any order.

**Returns:** a readonly Iterator over Attribute interfaces, or an
empty iterator

---

#### getAttributes

Iterator

<

Attribute

> getAttributes()

Returns an Iterator of non-namespace declared attributes declared on
this START_ELEMENT,
returns an empty iterator if there are no attributes. The
iterator must contain only implementations of the javax.xml.stream.Attribute
interface. Attributes are fundamentally unordered and may not be reported
in any order.

getNamespaces

```java
Iterator
<
Namespace
> getNamespaces()
```

Returns an Iterator of namespaces declared on this element.
This Iterator does not contain previously declared namespaces
unless they appear on the current START_ELEMENT.
Therefore this list may contain redeclared namespaces and duplicate namespace
declarations. Use the getNamespaceContext() method to get the
current context of namespace declarations.

The iterator must contain only implementations of the
javax.xml.stream.Namespace interface.

A Namespace isA Attribute. One
can iterate over a list of namespaces as a list of attributes.
However this method returns only the list of namespaces
declared on this START_ELEMENT and does not
include the attributes declared on this START_ELEMENT.

Returns an empty iterator if there are no namespaces.

**Returns:** a readonly Iterator over Namespace interfaces, or an
empty iterator

---

#### getNamespaces

Iterator

<

Namespace

> getNamespaces()

Returns an Iterator of namespaces declared on this element.
This Iterator does not contain previously declared namespaces
unless they appear on the current START_ELEMENT.
Therefore this list may contain redeclared namespaces and duplicate namespace
declarations. Use the getNamespaceContext() method to get the
current context of namespace declarations.

The iterator must contain only implementations of the
javax.xml.stream.Namespace interface.

A Namespace isA Attribute. One
can iterate over a list of namespaces as a list of attributes.
However this method returns only the list of namespaces
declared on this START_ELEMENT and does not
include the attributes declared on this START_ELEMENT.

Returns an empty iterator if there are no namespaces.

The iterator must contain only implementations of the
javax.xml.stream.Namespace interface.

A Namespace isA Attribute. One
can iterate over a list of namespaces as a list of attributes.
However this method returns only the list of namespaces
declared on this START_ELEMENT and does not
include the attributes declared on this START_ELEMENT.

Returns an empty iterator if there are no namespaces.

A Namespace isA Attribute. One
can iterate over a list of namespaces as a list of attributes.
However this method returns only the list of namespaces
declared on this START_ELEMENT and does not
include the attributes declared on this START_ELEMENT.

Returns an empty iterator if there are no namespaces.

getAttributeByName

```java
Attribute
getAttributeByName​(
QName
name)
```

Returns the attribute referred to by this name

**Parameters:** name

- the qname of the desired name
**Returns:** the attribute corresponding to the name value or null

---

#### getAttributeByName

Attribute

getAttributeByName​(

QName

name)

Returns the attribute referred to by this name

getNamespaceContext

```java
NamespaceContext
getNamespaceContext()
```

Gets a read-only namespace context. If no context is
available this method will return an empty namespace context.
The NamespaceContext contains information about all namespaces
in scope for this StartElement.

**Returns:** the current namespace context

---

#### getNamespaceContext

NamespaceContext

getNamespaceContext()

Gets a read-only namespace context. If no context is
available this method will return an empty namespace context.
The NamespaceContext contains information about all namespaces
in scope for this StartElement.

getNamespaceURI

```java
String
getNamespaceURI​(
String
prefix)
```

Gets the value that the prefix is bound to in the
context of this element. Returns null if
the prefix is not bound in this context

**Parameters:** prefix

- the prefix to lookup
**Returns:** the uri bound to the prefix or null

---

#### getNamespaceURI

String

getNamespaceURI​(

String

prefix)

Gets the value that the prefix is bound to in the
context of this element. Returns null if
the prefix is not bound in this context

---

