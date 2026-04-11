# Interface NotationDeclaration

**Source:** `java.xml\javax\xml\stream\events\NotationDeclaration.html`

### Class Description

```java
public interface
NotationDeclaration

extends
XMLEvent
```

An interface for handling Notation Declarations

Receive notification of a notation declaration event.
It is up to the application to record the notation for later reference,
At least one of publicId and systemId must be non-null.
There is no guarantee that the notation declaration
will be reported before any unparsed entities that use it.

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
getName()

The notation name.

---

#### String
getPublicId()

The notation's public identifier, or null if none was given.

---

#### String
getSystemId()

The notation's system identifier, or null if none was given.

---

### Additional Sections

#### Interface NotationDeclaration

**All Superinterfaces:** XMLEvent

,

XMLStreamConstants

```java
public interface
NotationDeclaration

extends
XMLEvent
```

An interface for handling Notation Declarations

Receive notification of a notation declaration event.
It is up to the application to record the notation for later reference,
At least one of publicId and systemId must be non-null.
There is no guarantee that the notation declaration
will be reported before any unparsed entities that use it.

**Since:** 1.6

public interface

NotationDeclaration

extends

XMLEvent

An interface for handling Notation Declarations

Receive notification of a notation declaration event.
It is up to the application to record the notation for later reference,
At least one of publicId and systemId must be non-null.
There is no guarantee that the notation declaration
will be reported before any unparsed entities that use it.

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

getName

()

The notation name.

String

getPublicId

()

The notation's public identifier, or null if none was given.

String

getSystemId

()

The notation's system identifier, or null if none was given.

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

getName

()

The notation name.

String

getPublicId

()

The notation's public identifier, or null if none was given.

String

getSystemId

()

The notation's system identifier, or null if none was given.

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

The notation name.

The notation's public identifier, or null if none was given.

The notation's system identifier, or null if none was given.

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
String
getName()
```

The notation name.

- getPublicId

```java
String
getPublicId()
```

The notation's public identifier, or null if none was given.

- getSystemId

```java
String
getSystemId()
```

The notation's system identifier, or null if none was given.

Method Detail

- getName

```java
String
getName()
```

The notation name.

- getPublicId

```java
String
getPublicId()
```

The notation's public identifier, or null if none was given.

- getSystemId

```java
String
getSystemId()
```

The notation's system identifier, or null if none was given.

---

#### Method Detail

getName

```java
String
getName()
```

The notation name.

---

#### getName

String

getName()

The notation name.

getPublicId

```java
String
getPublicId()
```

The notation's public identifier, or null if none was given.

---

#### getPublicId

String

getPublicId()

The notation's public identifier, or null if none was given.

getSystemId

```java
String
getSystemId()
```

The notation's system identifier, or null if none was given.

---

#### getSystemId

String

getSystemId()

The notation's system identifier, or null if none was given.

---

