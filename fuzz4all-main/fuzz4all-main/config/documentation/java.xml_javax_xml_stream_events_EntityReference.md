# Interface EntityReference

**Source:** `java.xml\javax\xml\stream\events\EntityReference.html`

### Class Description

```java
public interface
EntityReference

extends
XMLEvent
```

An interface for handling Entity events.

This event reports entities that have not been resolved
and reports their replacement text unprocessed (if
available). This event will be reported if javax.xml.stream.isReplacingEntityReferences
is set to false. If javax.xml.stream.isReplacingEntityReferences is set to true
entity references will be resolved transparently.

Entities are handled in two possible ways:

(1) If javax.xml.stream.isReplacingEntityReferences is set to true
all entity references are resolved and reported as markup transparently.
(2) If javax.xml.stream.isReplacingEntityReferences is set to false
Entity references are reported as an EntityReference Event.

**All Superinterfaces:** XMLEvent

,

XMLStreamConstants

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### EntityDeclaration
getDeclaration()

Return the declaration of this entity.

---

#### String
getName()

The name of the entity

**Returns:**
- the entity's name, may not be null

---

### Additional Sections

#### Interface EntityReference

**All Superinterfaces:** XMLEvent

,

XMLStreamConstants

```java
public interface
EntityReference

extends
XMLEvent
```

An interface for handling Entity events.

This event reports entities that have not been resolved
and reports their replacement text unprocessed (if
available). This event will be reported if javax.xml.stream.isReplacingEntityReferences
is set to false. If javax.xml.stream.isReplacingEntityReferences is set to true
entity references will be resolved transparently.

Entities are handled in two possible ways:

(1) If javax.xml.stream.isReplacingEntityReferences is set to true
all entity references are resolved and reported as markup transparently.
(2) If javax.xml.stream.isReplacingEntityReferences is set to false
Entity references are reported as an EntityReference Event.

**Since:** 1.6

public interface

EntityReference

extends

XMLEvent

An interface for handling Entity events.

This event reports entities that have not been resolved
and reports their replacement text unprocessed (if
available). This event will be reported if javax.xml.stream.isReplacingEntityReferences
is set to false. If javax.xml.stream.isReplacingEntityReferences is set to true
entity references will be resolved transparently.

Entities are handled in two possible ways:

(1) If javax.xml.stream.isReplacingEntityReferences is set to true
all entity references are resolved and reported as markup transparently.
(2) If javax.xml.stream.isReplacingEntityReferences is set to false
Entity references are reported as an EntityReference Event.

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

EntityDeclaration

getDeclaration

()

Return the declaration of this entity.

String

getName

()

The name of the entity

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

EntityDeclaration

getDeclaration

()

Return the declaration of this entity.

String

getName

()

The name of the entity

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

Return the declaration of this entity.

The name of the entity

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

- getDeclaration

```java
EntityDeclaration
getDeclaration()
```

Return the declaration of this entity.

- getName

```java
String
getName()
```

The name of the entity

**Returns:** the entity's name, may not be null

Method Detail

- getDeclaration

```java
EntityDeclaration
getDeclaration()
```

Return the declaration of this entity.

- getName

```java
String
getName()
```

The name of the entity

**Returns:** the entity's name, may not be null

---

#### Method Detail

getDeclaration

```java
EntityDeclaration
getDeclaration()
```

Return the declaration of this entity.

---

#### getDeclaration

EntityDeclaration

getDeclaration()

Return the declaration of this entity.

getName

```java
String
getName()
```

The name of the entity

**Returns:** the entity's name, may not be null

---

#### getName

String

getName()

The name of the entity

---

