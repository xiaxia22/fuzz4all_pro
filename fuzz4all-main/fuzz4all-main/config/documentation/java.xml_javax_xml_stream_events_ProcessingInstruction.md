# Interface ProcessingInstruction

**Source:** `java.xml\javax\xml\stream\events\ProcessingInstruction.html`

### Class Description

```java
public interface
ProcessingInstruction

extends
XMLEvent
```

An interface that describes the data found in processing instructions

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
getTarget()

The target section of the processing instruction

**Returns:**
- the String value of the PI or null

---

#### String
getData()

The data section of the processing instruction

**Returns:**
- the String value of the PI's data or null

---

### Additional Sections

#### Interface ProcessingInstruction

**All Superinterfaces:** XMLEvent

,

XMLStreamConstants

```java
public interface
ProcessingInstruction

extends
XMLEvent
```

An interface that describes the data found in processing instructions

**Since:** 1.6

public interface

ProcessingInstruction

extends

XMLEvent

An interface that describes the data found in processing instructions

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

getData

()

The data section of the processing instruction

String

getTarget

()

The target section of the processing instruction

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

getData

()

The data section of the processing instruction

String

getTarget

()

The target section of the processing instruction

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

The data section of the processing instruction

The target section of the processing instruction

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

- getTarget

```java
String
getTarget()
```

The target section of the processing instruction

**Returns:** the String value of the PI or null

- getData

```java
String
getData()
```

The data section of the processing instruction

**Returns:** the String value of the PI's data or null

Method Detail

- getTarget

```java
String
getTarget()
```

The target section of the processing instruction

**Returns:** the String value of the PI or null

- getData

```java
String
getData()
```

The data section of the processing instruction

**Returns:** the String value of the PI's data or null

---

#### Method Detail

getTarget

```java
String
getTarget()
```

The target section of the processing instruction

**Returns:** the String value of the PI or null

---

#### getTarget

String

getTarget()

The target section of the processing instruction

getData

```java
String
getData()
```

The data section of the processing instruction

**Returns:** the String value of the PI's data or null

---

#### getData

String

getData()

The data section of the processing instruction

---

