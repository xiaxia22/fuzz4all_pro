# Interface Namespace

**Source:** `java.xml\javax\xml\stream\events\Namespace.html`

### Class Description

```java
public interface
Namespace

extends
Attribute
```

An interface that contains information about a namespace.
Namespaces are accessed from a StartElement.

**All Superinterfaces:** Attribute

,

XMLEvent

,

XMLStreamConstants

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
getPrefix()

Gets the prefix, returns "" if this is a default
namespace declaration.

---

#### String
getNamespaceURI()

Gets the uri bound to the prefix of this namespace

---

#### boolean isDefaultNamespaceDeclaration()

returns true if this attribute declares the default namespace

---

### Additional Sections

#### Interface Namespace

**All Superinterfaces:** Attribute

,

XMLEvent

,

XMLStreamConstants

```java
public interface
Namespace

extends
Attribute
```

An interface that contains information about a namespace.
Namespaces are accessed from a StartElement.

**Since:** 1.6
**See Also:** StartElement

public interface

Namespace

extends

Attribute

An interface that contains information about a namespace.
Namespaces are accessed from a StartElement.

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

getNamespaceURI

()

Gets the uri bound to the prefix of this namespace

String

getPrefix

()

Gets the prefix, returns "" if this is a default
namespace declaration.

boolean

isDefaultNamespaceDeclaration

()

returns true if this attribute declares the default namespace

- Methods declared in interface javax.xml.stream.events.

Attribute

getDTDType

,

getName

,

getValue

,

isSpecified

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

getNamespaceURI

()

Gets the uri bound to the prefix of this namespace

String

getPrefix

()

Gets the prefix, returns "" if this is a default
namespace declaration.

boolean

isDefaultNamespaceDeclaration

()

returns true if this attribute declares the default namespace

- Methods declared in interface javax.xml.stream.events.

Attribute

getDTDType

,

getName

,

getValue

,

isSpecified

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

Gets the uri bound to the prefix of this namespace

Gets the prefix, returns "" if this is a default
namespace declaration.

returns true if this attribute declares the default namespace

Methods declared in interface javax.xml.stream.events.

Attribute

getDTDType

,

getName

,

getValue

,

isSpecified

---

#### Methods declared in interface javax.xml.stream.events. Attribute

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

- getPrefix

```java
String
getPrefix()
```

Gets the prefix, returns "" if this is a default
namespace declaration.

- getNamespaceURI

```java
String
getNamespaceURI()
```

Gets the uri bound to the prefix of this namespace

- isDefaultNamespaceDeclaration

```java
boolean isDefaultNamespaceDeclaration()
```

returns true if this attribute declares the default namespace

Method Detail

- getPrefix

```java
String
getPrefix()
```

Gets the prefix, returns "" if this is a default
namespace declaration.

- getNamespaceURI

```java
String
getNamespaceURI()
```

Gets the uri bound to the prefix of this namespace

- isDefaultNamespaceDeclaration

```java
boolean isDefaultNamespaceDeclaration()
```

returns true if this attribute declares the default namespace

---

#### Method Detail

getPrefix

```java
String
getPrefix()
```

Gets the prefix, returns "" if this is a default
namespace declaration.

---

#### getPrefix

String

getPrefix()

Gets the prefix, returns "" if this is a default
namespace declaration.

getNamespaceURI

```java
String
getNamespaceURI()
```

Gets the uri bound to the prefix of this namespace

---

#### getNamespaceURI

String

getNamespaceURI()

Gets the uri bound to the prefix of this namespace

isDefaultNamespaceDeclaration

```java
boolean isDefaultNamespaceDeclaration()
```

returns true if this attribute declares the default namespace

---

#### isDefaultNamespaceDeclaration

boolean isDefaultNamespaceDeclaration()

returns true if this attribute declares the default namespace

---

