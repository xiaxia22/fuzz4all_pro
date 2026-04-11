# Interface EntityDeclaration

**Source:** `java.xml\javax\xml\stream\events\EntityDeclaration.html`

### Class Description

```java
public interface
EntityDeclaration

extends
XMLEvent
```

An interface for handling Entity Declarations

This interface is used to record and report unparsed entity declarations.

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
getPublicId()

The entity's public identifier, or null if none was given

**Returns:**
- the public ID for this declaration or null

---

#### String
getSystemId()

The entity's system identifier.

**Returns:**
- the system ID for this declaration or null

---

#### String
getName()

The entity's name

**Returns:**
- the name, may not be null

---

#### String
getNotationName()

The name of the associated notation.

**Returns:**
- the notation name

---

#### String
getReplacementText()

The replacement text of the entity.
This method will only return non-null
if this is an internal entity.

**Returns:**
- null or the replacment text

---

#### String
getBaseURI()

Get the base URI for this reference
or null if this information is not available

**Returns:**
- the base URI or null

---

### Additional Sections

#### Interface EntityDeclaration

**All Superinterfaces:** XMLEvent

,

XMLStreamConstants

```java
public interface
EntityDeclaration

extends
XMLEvent
```

An interface for handling Entity Declarations

This interface is used to record and report unparsed entity declarations.

**Since:** 1.6

public interface

EntityDeclaration

extends

XMLEvent

An interface for handling Entity Declarations

This interface is used to record and report unparsed entity declarations.

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

getBaseURI

()

Get the base URI for this reference
or null if this information is not available

String

getName

()

The entity's name

String

getNotationName

()

The name of the associated notation.

String

getPublicId

()

The entity's public identifier, or null if none was given

String

getReplacementText

()

The replacement text of the entity.

String

getSystemId

()

The entity's system identifier.

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

getBaseURI

()

Get the base URI for this reference
or null if this information is not available

String

getName

()

The entity's name

String

getNotationName

()

The name of the associated notation.

String

getPublicId

()

The entity's public identifier, or null if none was given

String

getReplacementText

()

The replacement text of the entity.

String

getSystemId

()

The entity's system identifier.

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

Get the base URI for this reference
or null if this information is not available

The entity's name

The name of the associated notation.

The entity's public identifier, or null if none was given

The replacement text of the entity.

The entity's system identifier.

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

- getPublicId

```java
String
getPublicId()
```

The entity's public identifier, or null if none was given

**Returns:** the public ID for this declaration or null

- getSystemId

```java
String
getSystemId()
```

The entity's system identifier.

**Returns:** the system ID for this declaration or null

- getName

```java
String
getName()
```

The entity's name

**Returns:** the name, may not be null

- getNotationName

```java
String
getNotationName()
```

The name of the associated notation.

**Returns:** the notation name

- getReplacementText

```java
String
getReplacementText()
```

The replacement text of the entity.
This method will only return non-null
if this is an internal entity.

**Returns:** null or the replacment text

- getBaseURI

```java
String
getBaseURI()
```

Get the base URI for this reference
or null if this information is not available

**Returns:** the base URI or null

Method Detail

- getPublicId

```java
String
getPublicId()
```

The entity's public identifier, or null if none was given

**Returns:** the public ID for this declaration or null

- getSystemId

```java
String
getSystemId()
```

The entity's system identifier.

**Returns:** the system ID for this declaration or null

- getName

```java
String
getName()
```

The entity's name

**Returns:** the name, may not be null

- getNotationName

```java
String
getNotationName()
```

The name of the associated notation.

**Returns:** the notation name

- getReplacementText

```java
String
getReplacementText()
```

The replacement text of the entity.
This method will only return non-null
if this is an internal entity.

**Returns:** null or the replacment text

- getBaseURI

```java
String
getBaseURI()
```

Get the base URI for this reference
or null if this information is not available

**Returns:** the base URI or null

---

#### Method Detail

getPublicId

```java
String
getPublicId()
```

The entity's public identifier, or null if none was given

**Returns:** the public ID for this declaration or null

---

#### getPublicId

String

getPublicId()

The entity's public identifier, or null if none was given

getSystemId

```java
String
getSystemId()
```

The entity's system identifier.

**Returns:** the system ID for this declaration or null

---

#### getSystemId

String

getSystemId()

The entity's system identifier.

getName

```java
String
getName()
```

The entity's name

**Returns:** the name, may not be null

---

#### getName

String

getName()

The entity's name

getNotationName

```java
String
getNotationName()
```

The name of the associated notation.

**Returns:** the notation name

---

#### getNotationName

String

getNotationName()

The name of the associated notation.

getReplacementText

```java
String
getReplacementText()
```

The replacement text of the entity.
This method will only return non-null
if this is an internal entity.

**Returns:** null or the replacment text

---

#### getReplacementText

String

getReplacementText()

The replacement text of the entity.
This method will only return non-null
if this is an internal entity.

getBaseURI

```java
String
getBaseURI()
```

Get the base URI for this reference
or null if this information is not available

**Returns:** the base URI or null

---

#### getBaseURI

String

getBaseURI()

Get the base URI for this reference
or null if this information is not available

---

