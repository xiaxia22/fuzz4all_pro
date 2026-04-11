# Interface XMLEvent

**Source:** `java.xml\javax\xml\stream\events\XMLEvent.html`

### Class Description

```java
public interface
XMLEvent

extends
XMLStreamConstants
```

This is the base event interface for handling markup events.
Events are value objects that are used to communicate the
XML 1.0 InfoSet to the Application. Events may be cached
and referenced after the parse has completed.

**All Superinterfaces:** XMLStreamConstants

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### int getEventType()

Returns an integer code for this event.

**See Also:**
- XMLStreamConstants.START_ELEMENT

,

XMLStreamConstants.END_ELEMENT

,

XMLStreamConstants.CHARACTERS

,

XMLStreamConstants.ATTRIBUTE

,

XMLStreamConstants.NAMESPACE

,

XMLStreamConstants.PROCESSING_INSTRUCTION

,

XMLStreamConstants.COMMENT

,

XMLStreamConstants.START_DOCUMENT

,

XMLStreamConstants.END_DOCUMENT

,

XMLStreamConstants.DTD

---

#### Location
getLocation()

Return the location of this event. The Location
returned from this method is non-volatile and
will retain its information.

**See Also:**
- Location

---

#### boolean isStartElement()

A utility function to check if this event is a StartElement.

**See Also:**
- StartElement

---

#### boolean isAttribute()

A utility function to check if this event is an Attribute.

**See Also:**
- Attribute

---

#### boolean isNamespace()

A utility function to check if this event is a Namespace.

**See Also:**
- Namespace

---

#### boolean isEndElement()

A utility function to check if this event is a EndElement.

**See Also:**
- EndElement

---

#### boolean isEntityReference()

A utility function to check if this event is an EntityReference.

**See Also:**
- EntityReference

---

#### boolean isProcessingInstruction()

A utility function to check if this event is a ProcessingInstruction.

**See Also:**
- ProcessingInstruction

---

#### boolean isCharacters()

A utility function to check if this event is Characters.

**See Also:**
- Characters

---

#### boolean isStartDocument()

A utility function to check if this event is a StartDocument.

**See Also:**
- StartDocument

---

#### boolean isEndDocument()

A utility function to check if this event is an EndDocument.

**See Also:**
- EndDocument

---

#### StartElement
asStartElement()

Returns this event as a start element event, may result in
a class cast exception if this event is not a start element.

---

#### EndElement
asEndElement()

Returns this event as an end element event, may result in
a class cast exception if this event is not a end element.

---

#### Characters
asCharacters()

Returns this event as Characters, may result in
a class cast exception if this event is not Characters.

---

#### QName
getSchemaType()

This method is provided for implementations to provide
optional type information about the associated event.
It is optional and will return null if no information
is available.

---

#### void writeAsEncodedUnicode​(
Writer
writer)
throws
XMLStreamException

This method will write the XMLEvent as per the XML 1.0 specification as Unicode characters.
No indentation or whitespace should be outputted.

Any user defined event type SHALL have this method
called when being written to on an output stream.
Built in Event types MUST implement this method,
but implementations MAY choose not call these methods
for optimizations reasons when writing out built in
Events to an output stream.
The output generated MUST be equivalent in terms of the
infoset expressed.

**Parameters:**
- writer

- The writer that will output the data

**Throws:**
- XMLStreamException

- if there is a fatal error writing the event

---

### Additional Sections

#### Interface XMLEvent

**All Superinterfaces:** XMLStreamConstants

**All Known Subinterfaces:** Attribute

,

Characters

,

Comment

,

DTD

,

EndDocument

,

EndElement

,

EntityDeclaration

,

EntityReference

,

Namespace

,

NotationDeclaration

,

ProcessingInstruction

,

StartDocument

,

StartElement

```java
public interface
XMLEvent

extends
XMLStreamConstants
```

This is the base event interface for handling markup events.
Events are value objects that are used to communicate the
XML 1.0 InfoSet to the Application. Events may be cached
and referenced after the parse has completed.

**Since:** 1.6
**See Also:** XMLEventReader

,

Characters

,

ProcessingInstruction

,

StartElement

,

EndElement

,

StartDocument

,

EndDocument

,

EntityReference

,

EntityDeclaration

,

NotationDeclaration

public interface

XMLEvent

extends

XMLStreamConstants

This is the base event interface for handling markup events.
Events are value objects that are used to communicate the
XML 1.0 InfoSet to the Application. Events may be cached
and referenced after the parse has completed.

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

Characters

asCharacters

()

Returns this event as Characters, may result in
a class cast exception if this event is not Characters.

EndElement

asEndElement

()

Returns this event as an end element event, may result in
a class cast exception if this event is not a end element.

StartElement

asStartElement

()

Returns this event as a start element event, may result in
a class cast exception if this event is not a start element.

int

getEventType

()

Returns an integer code for this event.

Location

getLocation

()

Return the location of this event.

QName

getSchemaType

()

This method is provided for implementations to provide
optional type information about the associated event.

boolean

isAttribute

()

A utility function to check if this event is an Attribute.

boolean

isCharacters

()

A utility function to check if this event is Characters.

boolean

isEndDocument

()

A utility function to check if this event is an EndDocument.

boolean

isEndElement

()

A utility function to check if this event is a EndElement.

boolean

isEntityReference

()

A utility function to check if this event is an EntityReference.

boolean

isNamespace

()

A utility function to check if this event is a Namespace.

boolean

isProcessingInstruction

()

A utility function to check if this event is a ProcessingInstruction.

boolean

isStartDocument

()

A utility function to check if this event is a StartDocument.

boolean

isStartElement

()

A utility function to check if this event is a StartElement.

void

writeAsEncodedUnicode

​(

Writer

writer)

This method will write the XMLEvent as per the XML 1.0 specification as Unicode characters.

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

Characters

asCharacters

()

Returns this event as Characters, may result in
a class cast exception if this event is not Characters.

EndElement

asEndElement

()

Returns this event as an end element event, may result in
a class cast exception if this event is not a end element.

StartElement

asStartElement

()

Returns this event as a start element event, may result in
a class cast exception if this event is not a start element.

int

getEventType

()

Returns an integer code for this event.

Location

getLocation

()

Return the location of this event.

QName

getSchemaType

()

This method is provided for implementations to provide
optional type information about the associated event.

boolean

isAttribute

()

A utility function to check if this event is an Attribute.

boolean

isCharacters

()

A utility function to check if this event is Characters.

boolean

isEndDocument

()

A utility function to check if this event is an EndDocument.

boolean

isEndElement

()

A utility function to check if this event is a EndElement.

boolean

isEntityReference

()

A utility function to check if this event is an EntityReference.

boolean

isNamespace

()

A utility function to check if this event is a Namespace.

boolean

isProcessingInstruction

()

A utility function to check if this event is a ProcessingInstruction.

boolean

isStartDocument

()

A utility function to check if this event is a StartDocument.

boolean

isStartElement

()

A utility function to check if this event is a StartElement.

void

writeAsEncodedUnicode

​(

Writer

writer)

This method will write the XMLEvent as per the XML 1.0 specification as Unicode characters.

---

#### Method Summary

Returns this event as Characters, may result in
a class cast exception if this event is not Characters.

Returns this event as an end element event, may result in
a class cast exception if this event is not a end element.

Returns this event as a start element event, may result in
a class cast exception if this event is not a start element.

Returns an integer code for this event.

Return the location of this event.

This method is provided for implementations to provide
optional type information about the associated event.

A utility function to check if this event is an Attribute.

A utility function to check if this event is Characters.

A utility function to check if this event is an EndDocument.

A utility function to check if this event is a EndElement.

A utility function to check if this event is an EntityReference.

A utility function to check if this event is a Namespace.

A utility function to check if this event is a ProcessingInstruction.

A utility function to check if this event is a StartDocument.

A utility function to check if this event is a StartElement.

This method will write the XMLEvent as per the XML 1.0 specification as Unicode characters.

============ METHOD DETAIL ==========

- Method Detail

- getEventType

```java
int getEventType()
```

Returns an integer code for this event.

**See Also:** XMLStreamConstants.START_ELEMENT

,

XMLStreamConstants.END_ELEMENT

,

XMLStreamConstants.CHARACTERS

,

XMLStreamConstants.ATTRIBUTE

,

XMLStreamConstants.NAMESPACE

,

XMLStreamConstants.PROCESSING_INSTRUCTION

,

XMLStreamConstants.COMMENT

,

XMLStreamConstants.START_DOCUMENT

,

XMLStreamConstants.END_DOCUMENT

,

XMLStreamConstants.DTD

- getLocation

```java
Location
getLocation()
```

Return the location of this event. The Location
returned from this method is non-volatile and
will retain its information.

**See Also:** Location

- isStartElement

```java
boolean isStartElement()
```

A utility function to check if this event is a StartElement.

**See Also:** StartElement

- isAttribute

```java
boolean isAttribute()
```

A utility function to check if this event is an Attribute.

**See Also:** Attribute

- isNamespace

```java
boolean isNamespace()
```

A utility function to check if this event is a Namespace.

**See Also:** Namespace

- isEndElement

```java
boolean isEndElement()
```

A utility function to check if this event is a EndElement.

**See Also:** EndElement

- isEntityReference

```java
boolean isEntityReference()
```

A utility function to check if this event is an EntityReference.

**See Also:** EntityReference

- isProcessingInstruction

```java
boolean isProcessingInstruction()
```

A utility function to check if this event is a ProcessingInstruction.

**See Also:** ProcessingInstruction

- isCharacters

```java
boolean isCharacters()
```

A utility function to check if this event is Characters.

**See Also:** Characters

- isStartDocument

```java
boolean isStartDocument()
```

A utility function to check if this event is a StartDocument.

**See Also:** StartDocument

- isEndDocument

```java
boolean isEndDocument()
```

A utility function to check if this event is an EndDocument.

**See Also:** EndDocument

- asStartElement

```java
StartElement
asStartElement()
```

Returns this event as a start element event, may result in
a class cast exception if this event is not a start element.

- asEndElement

```java
EndElement
asEndElement()
```

Returns this event as an end element event, may result in
a class cast exception if this event is not a end element.

- asCharacters

```java
Characters
asCharacters()
```

Returns this event as Characters, may result in
a class cast exception if this event is not Characters.

- getSchemaType

```java
QName
getSchemaType()
```

This method is provided for implementations to provide
optional type information about the associated event.
It is optional and will return null if no information
is available.

- writeAsEncodedUnicode

```java
void writeAsEncodedUnicode​(
Writer
writer)
throws
XMLStreamException
```

This method will write the XMLEvent as per the XML 1.0 specification as Unicode characters.
No indentation or whitespace should be outputted.

Any user defined event type SHALL have this method
called when being written to on an output stream.
Built in Event types MUST implement this method,
but implementations MAY choose not call these methods
for optimizations reasons when writing out built in
Events to an output stream.
The output generated MUST be equivalent in terms of the
infoset expressed.

**Parameters:** writer

- The writer that will output the data
**Throws:** XMLStreamException

- if there is a fatal error writing the event

Method Detail

- getEventType

```java
int getEventType()
```

Returns an integer code for this event.

**See Also:** XMLStreamConstants.START_ELEMENT

,

XMLStreamConstants.END_ELEMENT

,

XMLStreamConstants.CHARACTERS

,

XMLStreamConstants.ATTRIBUTE

,

XMLStreamConstants.NAMESPACE

,

XMLStreamConstants.PROCESSING_INSTRUCTION

,

XMLStreamConstants.COMMENT

,

XMLStreamConstants.START_DOCUMENT

,

XMLStreamConstants.END_DOCUMENT

,

XMLStreamConstants.DTD

- getLocation

```java
Location
getLocation()
```

Return the location of this event. The Location
returned from this method is non-volatile and
will retain its information.

**See Also:** Location

- isStartElement

```java
boolean isStartElement()
```

A utility function to check if this event is a StartElement.

**See Also:** StartElement

- isAttribute

```java
boolean isAttribute()
```

A utility function to check if this event is an Attribute.

**See Also:** Attribute

- isNamespace

```java
boolean isNamespace()
```

A utility function to check if this event is a Namespace.

**See Also:** Namespace

- isEndElement

```java
boolean isEndElement()
```

A utility function to check if this event is a EndElement.

**See Also:** EndElement

- isEntityReference

```java
boolean isEntityReference()
```

A utility function to check if this event is an EntityReference.

**See Also:** EntityReference

- isProcessingInstruction

```java
boolean isProcessingInstruction()
```

A utility function to check if this event is a ProcessingInstruction.

**See Also:** ProcessingInstruction

- isCharacters

```java
boolean isCharacters()
```

A utility function to check if this event is Characters.

**See Also:** Characters

- isStartDocument

```java
boolean isStartDocument()
```

A utility function to check if this event is a StartDocument.

**See Also:** StartDocument

- isEndDocument

```java
boolean isEndDocument()
```

A utility function to check if this event is an EndDocument.

**See Also:** EndDocument

- asStartElement

```java
StartElement
asStartElement()
```

Returns this event as a start element event, may result in
a class cast exception if this event is not a start element.

- asEndElement

```java
EndElement
asEndElement()
```

Returns this event as an end element event, may result in
a class cast exception if this event is not a end element.

- asCharacters

```java
Characters
asCharacters()
```

Returns this event as Characters, may result in
a class cast exception if this event is not Characters.

- getSchemaType

```java
QName
getSchemaType()
```

This method is provided for implementations to provide
optional type information about the associated event.
It is optional and will return null if no information
is available.

- writeAsEncodedUnicode

```java
void writeAsEncodedUnicode​(
Writer
writer)
throws
XMLStreamException
```

This method will write the XMLEvent as per the XML 1.0 specification as Unicode characters.
No indentation or whitespace should be outputted.

Any user defined event type SHALL have this method
called when being written to on an output stream.
Built in Event types MUST implement this method,
but implementations MAY choose not call these methods
for optimizations reasons when writing out built in
Events to an output stream.
The output generated MUST be equivalent in terms of the
infoset expressed.

**Parameters:** writer

- The writer that will output the data
**Throws:** XMLStreamException

- if there is a fatal error writing the event

---

#### Method Detail

getEventType

```java
int getEventType()
```

Returns an integer code for this event.

**See Also:** XMLStreamConstants.START_ELEMENT

,

XMLStreamConstants.END_ELEMENT

,

XMLStreamConstants.CHARACTERS

,

XMLStreamConstants.ATTRIBUTE

,

XMLStreamConstants.NAMESPACE

,

XMLStreamConstants.PROCESSING_INSTRUCTION

,

XMLStreamConstants.COMMENT

,

XMLStreamConstants.START_DOCUMENT

,

XMLStreamConstants.END_DOCUMENT

,

XMLStreamConstants.DTD

---

#### getEventType

int getEventType()

Returns an integer code for this event.

getLocation

```java
Location
getLocation()
```

Return the location of this event. The Location
returned from this method is non-volatile and
will retain its information.

**See Also:** Location

---

#### getLocation

Location

getLocation()

Return the location of this event. The Location
returned from this method is non-volatile and
will retain its information.

isStartElement

```java
boolean isStartElement()
```

A utility function to check if this event is a StartElement.

**See Also:** StartElement

---

#### isStartElement

boolean isStartElement()

A utility function to check if this event is a StartElement.

isAttribute

```java
boolean isAttribute()
```

A utility function to check if this event is an Attribute.

**See Also:** Attribute

---

#### isAttribute

boolean isAttribute()

A utility function to check if this event is an Attribute.

isNamespace

```java
boolean isNamespace()
```

A utility function to check if this event is a Namespace.

**See Also:** Namespace

---

#### isNamespace

boolean isNamespace()

A utility function to check if this event is a Namespace.

isEndElement

```java
boolean isEndElement()
```

A utility function to check if this event is a EndElement.

**See Also:** EndElement

---

#### isEndElement

boolean isEndElement()

A utility function to check if this event is a EndElement.

isEntityReference

```java
boolean isEntityReference()
```

A utility function to check if this event is an EntityReference.

**See Also:** EntityReference

---

#### isEntityReference

boolean isEntityReference()

A utility function to check if this event is an EntityReference.

isProcessingInstruction

```java
boolean isProcessingInstruction()
```

A utility function to check if this event is a ProcessingInstruction.

**See Also:** ProcessingInstruction

---

#### isProcessingInstruction

boolean isProcessingInstruction()

A utility function to check if this event is a ProcessingInstruction.

isCharacters

```java
boolean isCharacters()
```

A utility function to check if this event is Characters.

**See Also:** Characters

---

#### isCharacters

boolean isCharacters()

A utility function to check if this event is Characters.

isStartDocument

```java
boolean isStartDocument()
```

A utility function to check if this event is a StartDocument.

**See Also:** StartDocument

---

#### isStartDocument

boolean isStartDocument()

A utility function to check if this event is a StartDocument.

isEndDocument

```java
boolean isEndDocument()
```

A utility function to check if this event is an EndDocument.

**See Also:** EndDocument

---

#### isEndDocument

boolean isEndDocument()

A utility function to check if this event is an EndDocument.

asStartElement

```java
StartElement
asStartElement()
```

Returns this event as a start element event, may result in
a class cast exception if this event is not a start element.

---

#### asStartElement

StartElement

asStartElement()

Returns this event as a start element event, may result in
a class cast exception if this event is not a start element.

asEndElement

```java
EndElement
asEndElement()
```

Returns this event as an end element event, may result in
a class cast exception if this event is not a end element.

---

#### asEndElement

EndElement

asEndElement()

Returns this event as an end element event, may result in
a class cast exception if this event is not a end element.

asCharacters

```java
Characters
asCharacters()
```

Returns this event as Characters, may result in
a class cast exception if this event is not Characters.

---

#### asCharacters

Characters

asCharacters()

Returns this event as Characters, may result in
a class cast exception if this event is not Characters.

getSchemaType

```java
QName
getSchemaType()
```

This method is provided for implementations to provide
optional type information about the associated event.
It is optional and will return null if no information
is available.

---

#### getSchemaType

QName

getSchemaType()

This method is provided for implementations to provide
optional type information about the associated event.
It is optional and will return null if no information
is available.

writeAsEncodedUnicode

```java
void writeAsEncodedUnicode​(
Writer
writer)
throws
XMLStreamException
```

This method will write the XMLEvent as per the XML 1.0 specification as Unicode characters.
No indentation or whitespace should be outputted.

Any user defined event type SHALL have this method
called when being written to on an output stream.
Built in Event types MUST implement this method,
but implementations MAY choose not call these methods
for optimizations reasons when writing out built in
Events to an output stream.
The output generated MUST be equivalent in terms of the
infoset expressed.

**Parameters:** writer

- The writer that will output the data
**Throws:** XMLStreamException

- if there is a fatal error writing the event

---

#### writeAsEncodedUnicode

void writeAsEncodedUnicode​(

Writer

writer)
throws

XMLStreamException

This method will write the XMLEvent as per the XML 1.0 specification as Unicode characters.
No indentation or whitespace should be outputted.

Any user defined event type SHALL have this method
called when being written to on an output stream.
Built in Event types MUST implement this method,
but implementations MAY choose not call these methods
for optimizations reasons when writing out built in
Events to an output stream.
The output generated MUST be equivalent in terms of the
infoset expressed.

---

