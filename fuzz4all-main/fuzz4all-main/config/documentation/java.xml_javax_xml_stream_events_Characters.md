# Interface Characters

**Source:** `java.xml\javax\xml\stream\events\Characters.html`

### Class Description

```java
public interface
Characters

extends
XMLEvent
```

This describes the interface to Characters events.
All text events get reported as Characters events.
Content, CData and whitespace are all reported as
Characters events. IgnorableWhitespace, in most cases,
will be set to false unless an element declaration of element
content is present for the current element.

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
getData()

Get the character data of this event

---

#### boolean isWhiteSpace()

Returns true if this set of Characters
is all whitespace. Whitespace inside a document
is reported as CHARACTERS. This method allows
checking of CHARACTERS events to see if they
are composed of only whitespace characters

---

#### boolean isCData()

Returns true if this is a CData section. If this
event is CData its event type will be CDATA

If javax.xml.stream.isCoalescing is set to true CDATA Sections
that are surrounded by non CDATA characters will be reported
as a single Characters event. This method will return false
in this case.

---

#### boolean isIgnorableWhiteSpace()

Return true if this is ignorableWhiteSpace. If
this event is ignorableWhiteSpace its event type will
be SPACE.

---

### Additional Sections

#### Interface Characters

**All Superinterfaces:** XMLEvent

,

XMLStreamConstants

```java
public interface
Characters

extends
XMLEvent
```

This describes the interface to Characters events.
All text events get reported as Characters events.
Content, CData and whitespace are all reported as
Characters events. IgnorableWhitespace, in most cases,
will be set to false unless an element declaration of element
content is present for the current element.

**Since:** 1.6

public interface

Characters

extends

XMLEvent

This describes the interface to Characters events.
All text events get reported as Characters events.
Content, CData and whitespace are all reported as
Characters events. IgnorableWhitespace, in most cases,
will be set to false unless an element declaration of element
content is present for the current element.

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

Get the character data of this event

boolean

isCData

()

Returns true if this is a CData section.

boolean

isIgnorableWhiteSpace

()

Return true if this is ignorableWhiteSpace.

boolean

isWhiteSpace

()

Returns true if this set of Characters
is all whitespace.

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

Get the character data of this event

boolean

isCData

()

Returns true if this is a CData section.

boolean

isIgnorableWhiteSpace

()

Return true if this is ignorableWhiteSpace.

boolean

isWhiteSpace

()

Returns true if this set of Characters
is all whitespace.

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

Get the character data of this event

Returns true if this is a CData section.

Return true if this is ignorableWhiteSpace.

Returns true if this set of Characters
is all whitespace.

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

- getData

```java
String
getData()
```

Get the character data of this event

- isWhiteSpace

```java
boolean isWhiteSpace()
```

Returns true if this set of Characters
is all whitespace. Whitespace inside a document
is reported as CHARACTERS. This method allows
checking of CHARACTERS events to see if they
are composed of only whitespace characters

- isCData

```java
boolean isCData()
```

Returns true if this is a CData section. If this
event is CData its event type will be CDATA

If javax.xml.stream.isCoalescing is set to true CDATA Sections
that are surrounded by non CDATA characters will be reported
as a single Characters event. This method will return false
in this case.

- isIgnorableWhiteSpace

```java
boolean isIgnorableWhiteSpace()
```

Return true if this is ignorableWhiteSpace. If
this event is ignorableWhiteSpace its event type will
be SPACE.

Method Detail

- getData

```java
String
getData()
```

Get the character data of this event

- isWhiteSpace

```java
boolean isWhiteSpace()
```

Returns true if this set of Characters
is all whitespace. Whitespace inside a document
is reported as CHARACTERS. This method allows
checking of CHARACTERS events to see if they
are composed of only whitespace characters

- isCData

```java
boolean isCData()
```

Returns true if this is a CData section. If this
event is CData its event type will be CDATA

If javax.xml.stream.isCoalescing is set to true CDATA Sections
that are surrounded by non CDATA characters will be reported
as a single Characters event. This method will return false
in this case.

- isIgnorableWhiteSpace

```java
boolean isIgnorableWhiteSpace()
```

Return true if this is ignorableWhiteSpace. If
this event is ignorableWhiteSpace its event type will
be SPACE.

---

#### Method Detail

getData

```java
String
getData()
```

Get the character data of this event

---

#### getData

String

getData()

Get the character data of this event

isWhiteSpace

```java
boolean isWhiteSpace()
```

Returns true if this set of Characters
is all whitespace. Whitespace inside a document
is reported as CHARACTERS. This method allows
checking of CHARACTERS events to see if they
are composed of only whitespace characters

---

#### isWhiteSpace

boolean isWhiteSpace()

Returns true if this set of Characters
is all whitespace. Whitespace inside a document
is reported as CHARACTERS. This method allows
checking of CHARACTERS events to see if they
are composed of only whitespace characters

isCData

```java
boolean isCData()
```

Returns true if this is a CData section. If this
event is CData its event type will be CDATA

If javax.xml.stream.isCoalescing is set to true CDATA Sections
that are surrounded by non CDATA characters will be reported
as a single Characters event. This method will return false
in this case.

---

#### isCData

boolean isCData()

Returns true if this is a CData section. If this
event is CData its event type will be CDATA

If javax.xml.stream.isCoalescing is set to true CDATA Sections
that are surrounded by non CDATA characters will be reported
as a single Characters event. This method will return false
in this case.

isIgnorableWhiteSpace

```java
boolean isIgnorableWhiteSpace()
```

Return true if this is ignorableWhiteSpace. If
this event is ignorableWhiteSpace its event type will
be SPACE.

---

#### isIgnorableWhiteSpace

boolean isIgnorableWhiteSpace()

Return true if this is ignorableWhiteSpace. If
this event is ignorableWhiteSpace its event type will
be SPACE.

---

