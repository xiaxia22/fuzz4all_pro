# Interface EndElement

**Source:** `java.xml\javax\xml\stream\events\EndElement.html`

### Class Description

```java
public interface
EndElement

extends
XMLEvent
```

An interface for the end element event. An EndElement is reported
for each End Tag in the document.

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
Namespace
> getNamespaces()

Returns an Iterator of namespaces that have gone out
of scope. Returns an empty iterator if no namespaces have gone
out of scope.

**Returns:**
- an Iterator over Namespace interfaces, or an
empty iterator

---

### Additional Sections

#### Interface EndElement

**All Superinterfaces:** XMLEvent

,

XMLStreamConstants

```java
public interface
EndElement

extends
XMLEvent
```

An interface for the end element event. An EndElement is reported
for each End Tag in the document.

**Since:** 1.6
**See Also:** XMLEvent

public interface

EndElement

extends

XMLEvent

An interface for the end element event. An EndElement is reported
for each End Tag in the document.

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

QName

getName

()

Get the name of this event

Iterator

<

Namespace

>

getNamespaces

()

Returns an Iterator of namespaces that have gone out
of scope.

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

QName

getName

()

Get the name of this event

Iterator

<

Namespace

>

getNamespaces

()

Returns an Iterator of namespaces that have gone out
of scope.

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

Get the name of this event

Returns an Iterator of namespaces that have gone out
of scope.

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

- getNamespaces

```java
Iterator
<
Namespace
> getNamespaces()
```

Returns an Iterator of namespaces that have gone out
of scope. Returns an empty iterator if no namespaces have gone
out of scope.

**Returns:** an Iterator over Namespace interfaces, or an
empty iterator

Method Detail

- getName

```java
QName
getName()
```

Get the name of this event

**Returns:** the qualified name of this event

- getNamespaces

```java
Iterator
<
Namespace
> getNamespaces()
```

Returns an Iterator of namespaces that have gone out
of scope. Returns an empty iterator if no namespaces have gone
out of scope.

**Returns:** an Iterator over Namespace interfaces, or an
empty iterator

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

getNamespaces

```java
Iterator
<
Namespace
> getNamespaces()
```

Returns an Iterator of namespaces that have gone out
of scope. Returns an empty iterator if no namespaces have gone
out of scope.

**Returns:** an Iterator over Namespace interfaces, or an
empty iterator

---

#### getNamespaces

Iterator

<

Namespace

> getNamespaces()

Returns an Iterator of namespaces that have gone out
of scope. Returns an empty iterator if no namespaces have gone
out of scope.

---

