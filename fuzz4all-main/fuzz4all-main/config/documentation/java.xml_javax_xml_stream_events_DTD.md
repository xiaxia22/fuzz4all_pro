# Interface DTD

**Source:** `java.xml\javax\xml\stream\events\DTD.html`

### Class Description

```java
public interface
DTD

extends
XMLEvent
```

This is the top level interface for events dealing with DTDs

**All Superinterfaces:** XMLEvent

,

XMLStreamConstants

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
getDocumentTypeDeclaration()

Returns the entire Document Type Declaration as a string, including the
internal DTD subset. This may be null if there is not an internal subset.
If it is not null it must return the entire Document Type Declaration
which matches the doctypedecl production in the XML 1.0 specification

**Returns:**
- the Document Type Declaration

---

#### Object
getProcessedDTD()

Returns an implementation defined representation of the DTD. This method
may return null if no representation is available.

**Returns:**
- the representation of the DTD

---

#### List
<
NotationDeclaration
> getNotations()

Return a List containing the notations declared in the DTD. This list
must contain NotationDeclaration events.

**Returns:**
- an unordered list of NotationDeclaration events

**See Also:**
- NotationDeclaration

---

#### List
<
EntityDeclaration
> getEntities()

Return a List containing the general entities, both external and
internal, declared in the DTD. This list must contain EntityDeclaration
events.

**Returns:**
- an unordered list of EntityDeclaration events

**See Also:**
- EntityDeclaration

---

### Additional Sections

#### Interface DTD

**All Superinterfaces:** XMLEvent

,

XMLStreamConstants

```java
public interface
DTD

extends
XMLEvent
```

This is the top level interface for events dealing with DTDs

**Since:** 1.6

public interface

DTD

extends

XMLEvent

This is the top level interface for events dealing with DTDs

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

String

getDocumentTypeDeclaration

()

Returns the entire Document Type Declaration as a string, including the
internal DTD subset.

List

<

EntityDeclaration

>

getEntities

()

Return a List containing the general entities, both external and
internal, declared in the DTD.

List

<

NotationDeclaration

>

getNotations

()

Return a List containing the notations declared in the DTD.

Object

getProcessedDTD

()

Returns an implementation defined representation of the DTD.

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

String

getDocumentTypeDeclaration

()

Returns the entire Document Type Declaration as a string, including the
internal DTD subset.

List

<

EntityDeclaration

>

getEntities

()

Return a List containing the general entities, both external and
internal, declared in the DTD.

List

<

NotationDeclaration

>

getNotations

()

Return a List containing the notations declared in the DTD.

Object

getProcessedDTD

()

Returns an implementation defined representation of the DTD.

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

Returns the entire Document Type Declaration as a string, including the
internal DTD subset.

Return a List containing the general entities, both external and
internal, declared in the DTD.

Return a List containing the notations declared in the DTD.

Returns an implementation defined representation of the DTD.

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

- getDocumentTypeDeclaration

```java
String
getDocumentTypeDeclaration()
```

Returns the entire Document Type Declaration as a string, including the
internal DTD subset. This may be null if there is not an internal subset.
If it is not null it must return the entire Document Type Declaration
which matches the doctypedecl production in the XML 1.0 specification

**Returns:** the Document Type Declaration

- getProcessedDTD

```java
Object
getProcessedDTD()
```

Returns an implementation defined representation of the DTD. This method
may return null if no representation is available.

**Returns:** the representation of the DTD

- getNotations

```java
List
<
NotationDeclaration
> getNotations()
```

Return a List containing the notations declared in the DTD. This list
must contain NotationDeclaration events.

**Returns:** an unordered list of NotationDeclaration events
**See Also:** NotationDeclaration

- getEntities

```java
List
<
EntityDeclaration
> getEntities()
```

Return a List containing the general entities, both external and
internal, declared in the DTD. This list must contain EntityDeclaration
events.

**Returns:** an unordered list of EntityDeclaration events
**See Also:** EntityDeclaration

Method Detail

- getDocumentTypeDeclaration

```java
String
getDocumentTypeDeclaration()
```

Returns the entire Document Type Declaration as a string, including the
internal DTD subset. This may be null if there is not an internal subset.
If it is not null it must return the entire Document Type Declaration
which matches the doctypedecl production in the XML 1.0 specification

**Returns:** the Document Type Declaration

- getProcessedDTD

```java
Object
getProcessedDTD()
```

Returns an implementation defined representation of the DTD. This method
may return null if no representation is available.

**Returns:** the representation of the DTD

- getNotations

```java
List
<
NotationDeclaration
> getNotations()
```

Return a List containing the notations declared in the DTD. This list
must contain NotationDeclaration events.

**Returns:** an unordered list of NotationDeclaration events
**See Also:** NotationDeclaration

- getEntities

```java
List
<
EntityDeclaration
> getEntities()
```

Return a List containing the general entities, both external and
internal, declared in the DTD. This list must contain EntityDeclaration
events.

**Returns:** an unordered list of EntityDeclaration events
**See Also:** EntityDeclaration

---

#### Method Detail

getDocumentTypeDeclaration

```java
String
getDocumentTypeDeclaration()
```

Returns the entire Document Type Declaration as a string, including the
internal DTD subset. This may be null if there is not an internal subset.
If it is not null it must return the entire Document Type Declaration
which matches the doctypedecl production in the XML 1.0 specification

**Returns:** the Document Type Declaration

---

#### getDocumentTypeDeclaration

String

getDocumentTypeDeclaration()

Returns the entire Document Type Declaration as a string, including the
internal DTD subset. This may be null if there is not an internal subset.
If it is not null it must return the entire Document Type Declaration
which matches the doctypedecl production in the XML 1.0 specification

getProcessedDTD

```java
Object
getProcessedDTD()
```

Returns an implementation defined representation of the DTD. This method
may return null if no representation is available.

**Returns:** the representation of the DTD

---

#### getProcessedDTD

Object

getProcessedDTD()

Returns an implementation defined representation of the DTD. This method
may return null if no representation is available.

getNotations

```java
List
<
NotationDeclaration
> getNotations()
```

Return a List containing the notations declared in the DTD. This list
must contain NotationDeclaration events.

**Returns:** an unordered list of NotationDeclaration events
**See Also:** NotationDeclaration

---

#### getNotations

List

<

NotationDeclaration

> getNotations()

Return a List containing the notations declared in the DTD. This list
must contain NotationDeclaration events.

getEntities

```java
List
<
EntityDeclaration
> getEntities()
```

Return a List containing the general entities, both external and
internal, declared in the DTD. This list must contain EntityDeclaration
events.

**Returns:** an unordered list of EntityDeclaration events
**See Also:** EntityDeclaration

---

#### getEntities

List

<

EntityDeclaration

> getEntities()

Return a List containing the general entities, both external and
internal, declared in the DTD. This list must contain EntityDeclaration
events.

---

