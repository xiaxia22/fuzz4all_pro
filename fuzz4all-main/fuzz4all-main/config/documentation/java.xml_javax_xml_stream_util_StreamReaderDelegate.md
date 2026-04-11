# Class StreamReaderDelegate

**Source:** `java.xml\javax\xml\stream\util\StreamReaderDelegate.html`

### Class Description

```java
public class
StreamReaderDelegate

extends
Object

implements
XMLStreamReader
```

This is the base class for deriving an XMLStreamReader filter

This class is designed to sit between an XMLStreamReader and an
application's XMLStreamReader. By default each method
does nothing but call the corresponding method on the
parent interface.

**All Implemented Interfaces:** XMLStreamConstants

,

XMLStreamReader

---

### Field Details

*No entries found.*

### Constructor Details

#### public StreamReaderDelegate()

Construct an empty filter with no parent.

---

#### public StreamReaderDelegate​(
XMLStreamReader
reader)

Construct an filter with the specified parent.

**Parameters:**
- reader

- the parent

---

### Method Details

#### public void setParent​(
XMLStreamReader
reader)

Set the parent of this instance.

**Parameters:**
- reader

- the new parent

---

#### public
XMLStreamReader
getParent()

Get the parent of this instance.

**Returns:**
- the parent or null if none is set

---

### Additional Sections

#### Class StreamReaderDelegate

java.lang.Object

- javax.xml.stream.util.StreamReaderDelegate

javax.xml.stream.util.StreamReaderDelegate

**All Implemented Interfaces:** XMLStreamConstants

,

XMLStreamReader

```java
public class
StreamReaderDelegate

extends
Object

implements
XMLStreamReader
```

This is the base class for deriving an XMLStreamReader filter

This class is designed to sit between an XMLStreamReader and an
application's XMLStreamReader. By default each method
does nothing but call the corresponding method on the
parent interface.

**Since:** 1.6
**See Also:** XMLStreamReader

,

EventReaderDelegate

public class

StreamReaderDelegate

extends

Object

implements

XMLStreamReader

This is the base class for deriving an XMLStreamReader filter

This class is designed to sit between an XMLStreamReader and an
application's XMLStreamReader. By default each method
does nothing but call the corresponding method on the
parent interface.

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

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

StreamReaderDelegate

()

Construct an empty filter with no parent.

StreamReaderDelegate

​(

XMLStreamReader

reader)

Construct an filter with the specified parent.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

XMLStreamReader

getParent

()

Get the parent of this instance.

void

setParent

​(

XMLStreamReader

reader)

Set the parent of this instance.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

- Methods declared in interface javax.xml.stream.

XMLStreamReader

close

,

getAttributeCount

,

getAttributeLocalName

,

getAttributeName

,

getAttributeNamespace

,

getAttributePrefix

,

getAttributeType

,

getAttributeValue

,

getAttributeValue

,

getCharacterEncodingScheme

,

getElementText

,

getEncoding

,

getEventType

,

getLocalName

,

getLocation

,

getName

,

getNamespaceContext

,

getNamespaceCount

,

getNamespacePrefix

,

getNamespaceURI

,

getNamespaceURI

,

getNamespaceURI

,

getPIData

,

getPITarget

,

getPrefix

,

getProperty

,

getText

,

getTextCharacters

,

getTextCharacters

,

getTextLength

,

getTextStart

,

getVersion

,

hasName

,

hasNext

,

hasText

,

isAttributeSpecified

,

isCharacters

,

isEndElement

,

isStandalone

,

isStartElement

,

isWhiteSpace

,

next

,

nextTag

,

require

,

standaloneSet

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

Constructor Summary

Constructors

Constructor

Description

StreamReaderDelegate

()

Construct an empty filter with no parent.

StreamReaderDelegate

​(

XMLStreamReader

reader)

Construct an filter with the specified parent.

---

#### Constructor Summary

Construct an empty filter with no parent.

Construct an filter with the specified parent.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

XMLStreamReader

getParent

()

Get the parent of this instance.

void

setParent

​(

XMLStreamReader

reader)

Set the parent of this instance.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

- Methods declared in interface javax.xml.stream.

XMLStreamReader

close

,

getAttributeCount

,

getAttributeLocalName

,

getAttributeName

,

getAttributeNamespace

,

getAttributePrefix

,

getAttributeType

,

getAttributeValue

,

getAttributeValue

,

getCharacterEncodingScheme

,

getElementText

,

getEncoding

,

getEventType

,

getLocalName

,

getLocation

,

getName

,

getNamespaceContext

,

getNamespaceCount

,

getNamespacePrefix

,

getNamespaceURI

,

getNamespaceURI

,

getNamespaceURI

,

getPIData

,

getPITarget

,

getPrefix

,

getProperty

,

getText

,

getTextCharacters

,

getTextCharacters

,

getTextLength

,

getTextStart

,

getVersion

,

hasName

,

hasNext

,

hasText

,

isAttributeSpecified

,

isCharacters

,

isEndElement

,

isStandalone

,

isStartElement

,

isWhiteSpace

,

next

,

nextTag

,

require

,

standaloneSet

---

#### Method Summary

Get the parent of this instance.

Set the parent of this instance.

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

Methods declared in interface javax.xml.stream.

XMLStreamReader

close

,

getAttributeCount

,

getAttributeLocalName

,

getAttributeName

,

getAttributeNamespace

,

getAttributePrefix

,

getAttributeType

,

getAttributeValue

,

getAttributeValue

,

getCharacterEncodingScheme

,

getElementText

,

getEncoding

,

getEventType

,

getLocalName

,

getLocation

,

getName

,

getNamespaceContext

,

getNamespaceCount

,

getNamespacePrefix

,

getNamespaceURI

,

getNamespaceURI

,

getNamespaceURI

,

getPIData

,

getPITarget

,

getPrefix

,

getProperty

,

getText

,

getTextCharacters

,

getTextCharacters

,

getTextLength

,

getTextStart

,

getVersion

,

hasName

,

hasNext

,

hasText

,

isAttributeSpecified

,

isCharacters

,

isEndElement

,

isStandalone

,

isStartElement

,

isWhiteSpace

,

next

,

nextTag

,

require

,

standaloneSet

---

#### Methods declared in interface javax.xml.stream. XMLStreamReader

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- StreamReaderDelegate

```java
public StreamReaderDelegate()
```

Construct an empty filter with no parent.

- StreamReaderDelegate

```java
public StreamReaderDelegate​(
XMLStreamReader
reader)
```

Construct an filter with the specified parent.

**Parameters:** reader

- the parent

============ METHOD DETAIL ==========

- Method Detail

- setParent

```java
public void setParent​(
XMLStreamReader
reader)
```

Set the parent of this instance.

**Parameters:** reader

- the new parent

- getParent

```java
public
XMLStreamReader
getParent()
```

Get the parent of this instance.

**Returns:** the parent or null if none is set

Constructor Detail

- StreamReaderDelegate

```java
public StreamReaderDelegate()
```

Construct an empty filter with no parent.

- StreamReaderDelegate

```java
public StreamReaderDelegate​(
XMLStreamReader
reader)
```

Construct an filter with the specified parent.

**Parameters:** reader

- the parent

---

#### Constructor Detail

StreamReaderDelegate

```java
public StreamReaderDelegate()
```

Construct an empty filter with no parent.

---

#### StreamReaderDelegate

public StreamReaderDelegate()

Construct an empty filter with no parent.

StreamReaderDelegate

```java
public StreamReaderDelegate​(
XMLStreamReader
reader)
```

Construct an filter with the specified parent.

**Parameters:** reader

- the parent

---

#### StreamReaderDelegate

public StreamReaderDelegate​(

XMLStreamReader

reader)

Construct an filter with the specified parent.

Method Detail

- setParent

```java
public void setParent​(
XMLStreamReader
reader)
```

Set the parent of this instance.

**Parameters:** reader

- the new parent

- getParent

```java
public
XMLStreamReader
getParent()
```

Get the parent of this instance.

**Returns:** the parent or null if none is set

---

#### Method Detail

setParent

```java
public void setParent​(
XMLStreamReader
reader)
```

Set the parent of this instance.

**Parameters:** reader

- the new parent

---

#### setParent

public void setParent​(

XMLStreamReader

reader)

Set the parent of this instance.

getParent

```java
public
XMLStreamReader
getParent()
```

Get the parent of this instance.

**Returns:** the parent or null if none is set

---

#### getParent

public

XMLStreamReader

getParent()

Get the parent of this instance.

---

