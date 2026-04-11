# Interface StartDocument

**Source:** `java.xml\javax\xml\stream\events\StartDocument.html`

### Class Description

```java
public interface
StartDocument

extends
XMLEvent
```

An interface for the start document event

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
getSystemId()

Returns the system ID of the XML data

**Returns:**
- the system ID, defaults to ""

---

#### String
getCharacterEncodingScheme()

Returns the encoding style of the XML data

**Returns:**
- the character encoding, defaults to "UTF-8"

---

#### boolean encodingSet()

Returns true if CharacterEncodingScheme was set in
the encoding declaration of the document

---

#### boolean isStandalone()

Returns if this XML is standalone

**Returns:**
- the standalone state of XML, defaults to "no"

---

#### boolean standaloneSet()

Returns true if the standalone attribute was set in
the encoding declaration of the document.

---

#### String
getVersion()

Returns the version of XML of this XML stream

**Returns:**
- the version of XML, defaults to "1.0"

---

### Additional Sections

#### Interface StartDocument

**All Superinterfaces:** XMLEvent

,

XMLStreamConstants

```java
public interface
StartDocument

extends
XMLEvent
```

An interface for the start document event

**Since:** 1.6

public interface

StartDocument

extends

XMLEvent

An interface for the start document event

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

boolean

encodingSet

()

Returns true if CharacterEncodingScheme was set in
the encoding declaration of the document

String

getCharacterEncodingScheme

()

Returns the encoding style of the XML data

String

getSystemId

()

Returns the system ID of the XML data

String

getVersion

()

Returns the version of XML of this XML stream

boolean

isStandalone

()

Returns if this XML is standalone

boolean

standaloneSet

()

Returns true if the standalone attribute was set in
the encoding declaration of the document.

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

boolean

encodingSet

()

Returns true if CharacterEncodingScheme was set in
the encoding declaration of the document

String

getCharacterEncodingScheme

()

Returns the encoding style of the XML data

String

getSystemId

()

Returns the system ID of the XML data

String

getVersion

()

Returns the version of XML of this XML stream

boolean

isStandalone

()

Returns if this XML is standalone

boolean

standaloneSet

()

Returns true if the standalone attribute was set in
the encoding declaration of the document.

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

Returns true if CharacterEncodingScheme was set in
the encoding declaration of the document

Returns the encoding style of the XML data

Returns the system ID of the XML data

Returns the version of XML of this XML stream

Returns if this XML is standalone

Returns true if the standalone attribute was set in
the encoding declaration of the document.

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

- getSystemId

```java
String
getSystemId()
```

Returns the system ID of the XML data

**Returns:** the system ID, defaults to ""

- getCharacterEncodingScheme

```java
String
getCharacterEncodingScheme()
```

Returns the encoding style of the XML data

**Returns:** the character encoding, defaults to "UTF-8"

- encodingSet

```java
boolean encodingSet()
```

Returns true if CharacterEncodingScheme was set in
the encoding declaration of the document

- isStandalone

```java
boolean isStandalone()
```

Returns if this XML is standalone

**Returns:** the standalone state of XML, defaults to "no"

- standaloneSet

```java
boolean standaloneSet()
```

Returns true if the standalone attribute was set in
the encoding declaration of the document.

- getVersion

```java
String
getVersion()
```

Returns the version of XML of this XML stream

**Returns:** the version of XML, defaults to "1.0"

Method Detail

- getSystemId

```java
String
getSystemId()
```

Returns the system ID of the XML data

**Returns:** the system ID, defaults to ""

- getCharacterEncodingScheme

```java
String
getCharacterEncodingScheme()
```

Returns the encoding style of the XML data

**Returns:** the character encoding, defaults to "UTF-8"

- encodingSet

```java
boolean encodingSet()
```

Returns true if CharacterEncodingScheme was set in
the encoding declaration of the document

- isStandalone

```java
boolean isStandalone()
```

Returns if this XML is standalone

**Returns:** the standalone state of XML, defaults to "no"

- standaloneSet

```java
boolean standaloneSet()
```

Returns true if the standalone attribute was set in
the encoding declaration of the document.

- getVersion

```java
String
getVersion()
```

Returns the version of XML of this XML stream

**Returns:** the version of XML, defaults to "1.0"

---

#### Method Detail

getSystemId

```java
String
getSystemId()
```

Returns the system ID of the XML data

**Returns:** the system ID, defaults to ""

---

#### getSystemId

String

getSystemId()

Returns the system ID of the XML data

getCharacterEncodingScheme

```java
String
getCharacterEncodingScheme()
```

Returns the encoding style of the XML data

**Returns:** the character encoding, defaults to "UTF-8"

---

#### getCharacterEncodingScheme

String

getCharacterEncodingScheme()

Returns the encoding style of the XML data

encodingSet

```java
boolean encodingSet()
```

Returns true if CharacterEncodingScheme was set in
the encoding declaration of the document

---

#### encodingSet

boolean encodingSet()

Returns true if CharacterEncodingScheme was set in
the encoding declaration of the document

isStandalone

```java
boolean isStandalone()
```

Returns if this XML is standalone

**Returns:** the standalone state of XML, defaults to "no"

---

#### isStandalone

boolean isStandalone()

Returns if this XML is standalone

standaloneSet

```java
boolean standaloneSet()
```

Returns true if the standalone attribute was set in
the encoding declaration of the document.

---

#### standaloneSet

boolean standaloneSet()

Returns true if the standalone attribute was set in
the encoding declaration of the document.

getVersion

```java
String
getVersion()
```

Returns the version of XML of this XML stream

**Returns:** the version of XML, defaults to "1.0"

---

#### getVersion

String

getVersion()

Returns the version of XML of this XML stream

---

