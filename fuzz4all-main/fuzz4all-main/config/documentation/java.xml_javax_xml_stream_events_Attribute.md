# Interface Attribute

**Source:** `java.xml\javax\xml\stream\events\Attribute.html`

### Class Description

```java
public interface
Attribute

extends
XMLEvent
```

An interface that contains information about an attribute. Attributes are reported
as a set of events accessible from a StartElement. Other applications may report
Attributes as first-order events, for example as the results of an XPath expression.

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

Returns the QName for this attribute

---

#### String
getValue()

Gets the normalized value of this attribute

---

#### String
getDTDType()

Gets the type of this attribute, default is
the String "CDATA"

**Returns:**
- the type as a String, default is "CDATA"

---

#### boolean isSpecified()

A flag indicating whether this attribute was actually
specified in the start-tag of its element, or was defaulted from the schema.

**Returns:**
- returns true if this was specified in the start element

---

### Additional Sections

#### Interface Attribute

**All Superinterfaces:** XMLEvent

,

XMLStreamConstants

**All Known Subinterfaces:** Namespace

```java
public interface
Attribute

extends
XMLEvent
```

An interface that contains information about an attribute. Attributes are reported
as a set of events accessible from a StartElement. Other applications may report
Attributes as first-order events, for example as the results of an XPath expression.

**Since:** 1.6
**See Also:** StartElement

public interface

Attribute

extends

XMLEvent

An interface that contains information about an attribute. Attributes are reported
as a set of events accessible from a StartElement. Other applications may report
Attributes as first-order events, for example as the results of an XPath expression.

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

getDTDType

()

Gets the type of this attribute, default is
the String "CDATA"

QName

getName

()

Returns the QName for this attribute

String

getValue

()

Gets the normalized value of this attribute

boolean

isSpecified

()

A flag indicating whether this attribute was actually
specified in the start-tag of its element, or was defaulted from the schema.

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

getDTDType

()

Gets the type of this attribute, default is
the String "CDATA"

QName

getName

()

Returns the QName for this attribute

String

getValue

()

Gets the normalized value of this attribute

boolean

isSpecified

()

A flag indicating whether this attribute was actually
specified in the start-tag of its element, or was defaulted from the schema.

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

Gets the type of this attribute, default is
the String "CDATA"

Returns the QName for this attribute

Gets the normalized value of this attribute

A flag indicating whether this attribute was actually
specified in the start-tag of its element, or was defaulted from the schema.

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

Returns the QName for this attribute

- getValue

```java
String
getValue()
```

Gets the normalized value of this attribute

- getDTDType

```java
String
getDTDType()
```

Gets the type of this attribute, default is
the String "CDATA"

**Returns:** the type as a String, default is "CDATA"

- isSpecified

```java
boolean isSpecified()
```

A flag indicating whether this attribute was actually
specified in the start-tag of its element, or was defaulted from the schema.

**Returns:** returns true if this was specified in the start element

Method Detail

- getName

```java
QName
getName()
```

Returns the QName for this attribute

- getValue

```java
String
getValue()
```

Gets the normalized value of this attribute

- getDTDType

```java
String
getDTDType()
```

Gets the type of this attribute, default is
the String "CDATA"

**Returns:** the type as a String, default is "CDATA"

- isSpecified

```java
boolean isSpecified()
```

A flag indicating whether this attribute was actually
specified in the start-tag of its element, or was defaulted from the schema.

**Returns:** returns true if this was specified in the start element

---

#### Method Detail

getName

```java
QName
getName()
```

Returns the QName for this attribute

---

#### getName

QName

getName()

Returns the QName for this attribute

getValue

```java
String
getValue()
```

Gets the normalized value of this attribute

---

#### getValue

String

getValue()

Gets the normalized value of this attribute

getDTDType

```java
String
getDTDType()
```

Gets the type of this attribute, default is
the String "CDATA"

**Returns:** the type as a String, default is "CDATA"

---

#### getDTDType

String

getDTDType()

Gets the type of this attribute, default is
the String "CDATA"

isSpecified

```java
boolean isSpecified()
```

A flag indicating whether this attribute was actually
specified in the start-tag of its element, or was defaulted from the schema.

**Returns:** returns true if this was specified in the start element

---

#### isSpecified

boolean isSpecified()

A flag indicating whether this attribute was actually
specified in the start-tag of its element, or was defaulted from the schema.

---

