# Interface XMLStreamReader

**Source:** `java.xml\javax\xml\stream\XMLStreamReader.html`

### Class Description

```java
public interface
XMLStreamReader

extends
XMLStreamConstants
```

The XMLStreamReader interface allows forward, read-only access to XML.
It is designed to be the lowest level and most efficient way to
read XML data.

The XMLStreamReader is designed to iterate over XML using
next() and hasNext(). The data can be accessed using methods such as getEventType(),
getNamespaceURI(), getLocalName() and getText();

An XMLStreamReader instance is created with an initial event type START_DOCUMENT.
At any moment in time, it has a current event that the methods of the interface
access and may load the next event through the

next()

method.
The current event type can be determined by

getEventType()

, and
the next returned by the

next()

method.

Parsing events are defined as the XML Declaration, a DTD,
start tag, character data, white space, end tag, comment,
or processing instruction. An attribute or namespace event may be encountered
at the root level of a document as the result of a query operation.

For XML 1.0 compliance an XML processor must pass the
identifiers of declared unparsed entities, notation declarations and their
associated identifiers to the application. This information is
provided through the property API on this interface.
The following two properties allow access to this information:
javax.xml.stream.notations and javax.xml.stream.entities.
When the current event is a DTD the following call will return a
list of Notations

List l = (List) getProperty("javax.xml.stream.notations");

The following call will return a list of entity declarations:

List l = (List) getProperty("javax.xml.stream.entities");

These properties can only be accessed during a DTD event and
are defined to return null if the information is not available.

The following table describes which methods are valid in what state.
If a method is called in an invalid state the method will throw a
java.lang.IllegalStateException.

Valid methods for each state

Event Type

Valid Methods

All States

getProperty(), hasNext(), require(), close(),
getNamespaceURI(), isStartElement(),
isEndElement(), isCharacters(), isWhiteSpace(),
getNamespaceContext(), getEventType(),getLocation(),
hasText(), hasName()

START_ELEMENT

next(), getName(), getLocalName(), hasName(), getPrefix(),
getAttributeXXX(), isAttributeSpecified(),
getNamespaceXXX(),
getElementText(), nextTag()

ATTRIBUTE

next(), nextTag()
getAttributeXXX(), isAttributeSpecified(),

NAMESPACE

next(), nextTag()
getNamespaceXXX()

END_ELEMENT

next(), getName(), getLocalName(), hasName(), getPrefix(),
getNamespaceXXX(), nextTag()

CHARACTERS

next(), getTextXXX(), nextTag()

CDATA

next(), getTextXXX(), nextTag()

COMMENT

next(), getTextXXX(), nextTag()

SPACE

next(), getTextXXX(), nextTag()

START_DOCUMENT

next(), getEncoding(), getVersion(), isStandalone(), standaloneSet(),
getCharacterEncodingScheme(), nextTag()

END_DOCUMENT

close()

PROCESSING_INSTRUCTION

next(), getPITarget(), getPIData(), nextTag()

ENTITY_REFERENCE

next(), getLocalName(), getText(), nextTag()

DTD

next(), getText(), nextTag()

**All Superinterfaces:** XMLStreamConstants

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Object
getProperty​(
String
name)
throws
IllegalArgumentException

Get the value of a feature/property from the underlying implementation

**Parameters:**
- name

- The name of the property, may not be null

**Returns:**
- The value of the property

**Throws:**
- IllegalArgumentException

- if name is null

---

#### int next()
throws
XMLStreamException

Get next parsing event - a processor may return all contiguous
character data in a single chunk, or it may split it into several chunks.
If the property javax.xml.stream.isCoalescing is set to true
element content must be coalesced and only one CHARACTERS event
must be returned for contiguous element content or
CDATA Sections.

By default entity references must be
expanded and reported transparently to the application.
An exception will be thrown if an entity reference cannot be expanded.
If element content is empty (i.e. content is "") then no CHARACTERS event will be reported.

Given the following XML:

<foo><!--description-->content text<![CDATA[<greeting>Hello>/greeting>]]>other content>/foo>

The behavior of calling next() when being on foo will be:

1- the comment (COMMENT)

2- then the characters section (CHARACTERS)

3- then the CDATA section (another CHARACTERS)

4- then the next characters section (another CHARACTERS)

5- then the END_ELEMENT

NOTE:

empty element (such as

<tag/>

) will be reported
with two separate events: START_ELEMENT, END_ELEMENT - This preserves
parsing equivalency of empty element to

<tag></tag>

.

This method will throw an IllegalStateException if it is called after hasNext() returns false.

**Returns:**
- the integer code corresponding to the current parse event

**Throws:**
- NoSuchElementException

- if this is called when hasNext() returns false
- XMLStreamException

- if there is an error processing the underlying XML source

**See Also:**
- XMLEvent

---

#### void require​(int type,

String
namespaceURI,

String
localName)
throws
XMLStreamException

Test if the current event is of the given type and if the namespace and name match the current
namespace and name of the current event. If the namespaceURI is null it is not checked for equality,
if the localName is null it is not checked for equality.

**Parameters:**
- type

- the event type
- namespaceURI

- the uri of the event, may be null
- localName

- the localName of the event, may be null

**Throws:**
- XMLStreamException

- if the required values are not matched.

---

#### String
getElementText()
throws
XMLStreamException

Reads the content of a text-only element, an exception is thrown if this is
not a text-only element.
Regardless of value of javax.xml.stream.isCoalescing this method always returns coalesced content.

Precondition: the current event is START_ELEMENT.

Postcondition: the current event is the corresponding END_ELEMENT.

The method does the following (implementations are free to optimized
but must do equivalent processing):

```java
if(getEventType() != XMLStreamConstants.START_ELEMENT) {
throw new XMLStreamException(
"parser must be on START_ELEMENT to read next text", getLocation());
}

int eventType = next();
StringBuffer content = new StringBuffer();
while(eventType != XMLStreamConstants.END_ELEMENT) {
if(eventType == XMLStreamConstants.CHARACTERS
|| eventType == XMLStreamConstants.CDATA
|| eventType == XMLStreamConstants.SPACE
|| eventType == XMLStreamConstants.ENTITY_REFERENCE) {
buf.append(getText());
} else if(eventType == XMLStreamConstants.PROCESSING_INSTRUCTION
|| eventType == XMLStreamConstants.COMMENT) {
// skipping
} else if(eventType == XMLStreamConstants.END_DOCUMENT) {
throw new XMLStreamException(
"unexpected end of document when reading element text content", this);
} else if(eventType == XMLStreamConstants.START_ELEMENT) {
throw new XMLStreamException(
"element text content may not contain START_ELEMENT", getLocation());
} else {
throw new XMLStreamException(
"Unexpected event type "+eventType, getLocation());
}
eventType = next();
}
return buf.toString();
```

**Throws:**
- XMLStreamException

- if the current event is not a START_ELEMENT
or if a non text element is encountered

---

#### int nextTag()
throws
XMLStreamException

Skips any white space (isWhiteSpace() returns true), COMMENT,
or PROCESSING_INSTRUCTION,
until a START_ELEMENT or END_ELEMENT is reached.
If other than white space characters, COMMENT, PROCESSING_INSTRUCTION, START_ELEMENT, END_ELEMENT
are encountered, an exception is thrown. This method should
be used when processing element-only content seperated by white space.

Precondition: none

Postcondition: the current event is START_ELEMENT or END_ELEMENT
and cursor may have moved over any whitespace event.

Essentially it does the following (implementations are free to optimized
but must do equivalent processing):

```java
int eventType = next();
while((eventType == XMLStreamConstants.CHARACTERS && isWhiteSpace()) // skip whitespace
|| (eventType == XMLStreamConstants.CDATA && isWhiteSpace())
// skip whitespace
|| eventType == XMLStreamConstants.SPACE
|| eventType == XMLStreamConstants.PROCESSING_INSTRUCTION
|| eventType == XMLStreamConstants.COMMENT
) {
eventType = next();
}
if (eventType != XMLStreamConstants.START_ELEMENT && eventType != XMLStreamConstants.END_ELEMENT) {
throw new String XMLStreamException("expected start or end tag", getLocation());
}
return eventType;
```

**Returns:**
- the event type of the element read (START_ELEMENT or END_ELEMENT)

**Throws:**
- XMLStreamException

- if the current event is not white space, PROCESSING_INSTRUCTION,
START_ELEMENT or END_ELEMENT
- NoSuchElementException

- if this is called when hasNext() returns false

---

#### boolean hasNext()
throws
XMLStreamException

Returns true if there are more parsing events and false
if there are no more events. This method will return
false if the current state of the XMLStreamReader is
END_DOCUMENT

**Returns:**
- true if there are more events, false otherwise

**Throws:**
- XMLStreamException

- if there is a fatal error detecting the next state

---

#### void close()
throws
XMLStreamException

Frees any resources associated with this Reader. This method does not close the
underlying input source.

**Throws:**
- XMLStreamException

- if there are errors freeing associated resources

---

#### String
getNamespaceURI​(
String
prefix)

Return the uri for the given prefix.
The uri returned depends on the current state of the processor.

NOTE:

The 'xml' prefix is bound as defined in

Namespaces in XML

specification to "http://www.w3.org/XML/1998/namespace".

NOTE:

The 'xmlns' prefix must be resolved to following namespace

http://www.w3.org/2000/xmlns/

**Parameters:**
- prefix

- The prefix to lookup, may not be null

**Returns:**
- the uri bound to the given prefix or null if it is not bound

**Throws:**
- IllegalArgumentException

- if the prefix is null

---

#### boolean isStartElement()

Returns true if the cursor points to a start tag (otherwise false)

**Returns:**
- true if the cursor points to a start tag, false otherwise

---

#### boolean isEndElement()

Returns true if the cursor points to an end tag (otherwise false)

**Returns:**
- true if the cursor points to an end tag, false otherwise

---

#### boolean isCharacters()

Returns true if the cursor points to a character data event

**Returns:**
- true if the cursor points to character data, false otherwise

---

#### boolean isWhiteSpace()

Returns true if the cursor points to a character data event
that consists of all whitespace

**Returns:**
- true if the cursor points to all whitespace, false otherwise

---

#### String
getAttributeValue​(
String
namespaceURI,

String
localName)

Returns the normalized attribute value of the
attribute with the namespace and localName
If the namespaceURI is null the namespace
is not checked for equality

**Parameters:**
- namespaceURI

- the namespace of the attribute
- localName

- the local name of the attribute, cannot be null

**Returns:**
- returns the value of the attribute , returns null if not found

**Throws:**
- IllegalStateException

- if this is not a START_ELEMENT or ATTRIBUTE

---

#### int getAttributeCount()

Returns the count of attributes on this START_ELEMENT,
this method is only valid on a START_ELEMENT or ATTRIBUTE. This
count excludes namespace definitions. Attribute indices are
zero-based.

**Returns:**
- returns the number of attributes

**Throws:**
- IllegalStateException

- if this is not a START_ELEMENT or ATTRIBUTE

---

#### QName
getAttributeName​(int index)

Returns the qname of the attribute at the provided index

**Parameters:**
- index

- the position of the attribute

**Returns:**
- the QName of the attribute

**Throws:**
- IllegalStateException

- if this is not a START_ELEMENT or ATTRIBUTE

---

#### String
getAttributeNamespace​(int index)

Returns the namespace of the attribute at the provided
index

**Parameters:**
- index

- the position of the attribute

**Returns:**
- the namespace URI (can be null)

**Throws:**
- IllegalStateException

- if this is not a START_ELEMENT or ATTRIBUTE

---

#### String
getAttributeLocalName​(int index)

Returns the localName of the attribute at the provided
index

**Parameters:**
- index

- the position of the attribute

**Returns:**
- the localName of the attribute

**Throws:**
- IllegalStateException

- if this is not a START_ELEMENT or ATTRIBUTE

---

#### String
getAttributePrefix​(int index)

Returns the prefix of this attribute at the
provided index

**Parameters:**
- index

- the position of the attribute

**Returns:**
- the prefix of the attribute

**Throws:**
- IllegalStateException

- if this is not a START_ELEMENT or ATTRIBUTE

---

#### String
getAttributeType​(int index)

Returns the XML type of the attribute at the provided
index

**Parameters:**
- index

- the position of the attribute

**Returns:**
- the XML type of the attribute

**Throws:**
- IllegalStateException

- if this is not a START_ELEMENT or ATTRIBUTE

---

#### String
getAttributeValue​(int index)

Returns the value of the attribute at the
index

**Parameters:**
- index

- the position of the attribute

**Returns:**
- the attribute value

**Throws:**
- IllegalStateException

- if this is not a START_ELEMENT or ATTRIBUTE

---

#### boolean isAttributeSpecified​(int index)

Returns a boolean which indicates if this
attribute was created by default

**Parameters:**
- index

- the position of the attribute

**Returns:**
- true if this is a default attribute

**Throws:**
- IllegalStateException

- if this is not a START_ELEMENT or ATTRIBUTE

---

#### int getNamespaceCount()

Returns the count of namespaces declared on this START_ELEMENT or END_ELEMENT,
this method is only valid on a START_ELEMENT, END_ELEMENT or NAMESPACE. On
an END_ELEMENT the count is of the namespaces that are about to go
out of scope. This is the equivalent of the information reported
by SAX callback for an end element event.

**Returns:**
- returns the number of namespace declarations on this specific element

**Throws:**
- IllegalStateException

- if this is not a START_ELEMENT, END_ELEMENT or NAMESPACE

---

#### String
getNamespacePrefix​(int index)

Returns the prefix for the namespace declared at the
index. Returns null if this is the default namespace
declaration

**Parameters:**
- index

- the position of the namespace declaration

**Returns:**
- returns the namespace prefix

**Throws:**
- IllegalStateException

- if this is not a START_ELEMENT, END_ELEMENT or NAMESPACE

---

#### String
getNamespaceURI​(int index)

Returns the uri for the namespace declared at the
index.

**Parameters:**
- index

- the position of the namespace declaration

**Returns:**
- returns the namespace uri

**Throws:**
- IllegalStateException

- if this is not a START_ELEMENT, END_ELEMENT or NAMESPACE

---

#### NamespaceContext
getNamespaceContext()

Returns a read only namespace context for the current
position. The context is transient and only valid until
a call to next() changes the state of the reader.

**Returns:**
- return a namespace context

---

#### int getEventType()

Returns an integer code that indicates the type of the event the cursor is
pointing to. The initial event type is

XMLStreamConstants.START_DOCUMENT

.

**Returns:**
- the type of the current event

---

#### String
getText()

Returns the current value of the parse event as a string,
this returns the string value of a CHARACTERS event,
returns the value of a COMMENT, the replacement value
for an ENTITY_REFERENCE, the string value of a CDATA section,
the string value for a SPACE event,
or the String value of the internal subset of the DTD.
If an ENTITY_REFERENCE has been resolved, any character data
will be reported as CHARACTERS events.

**Returns:**
- the current text or null

**Throws:**
- IllegalStateException

- if this state is not
a valid text state.

---

#### char[] getTextCharacters()

Returns an array which contains the characters from this event.
This array should be treated as read-only and transient. I.e. the array will
contain the text characters until the XMLStreamReader moves on to the next event.
Attempts to hold onto the character array beyond that time or modify the
contents of the array are breaches of the contract for this interface.

**Returns:**
- the current text or an empty array

**Throws:**
- IllegalStateException

- if this state is not
a valid text state.

---

#### int getTextCharacters​(int sourceStart,
char[] target,
int targetStart,
int length)
throws
XMLStreamException

Gets the the text associated with a CHARACTERS, SPACE or CDATA event.
Text starting a "sourceStart" is copied into "target" starting at "targetStart".
Up to "length" characters are copied. The number of characters actually copied is returned.

The "sourceStart" argument must be greater or equal to 0 and less than or equal to
the number of characters associated with the event. Usually, one requests text starting at a "sourceStart" of 0.
If the number of characters actually copied is less than the "length", then there is no more text.
Otherwise, subsequent calls need to be made until all text has been retrieved. For example:

```java
int length = 1024;
char[] myBuffer = new char[ length ];

for ( int sourceStart = 0 ; ; sourceStart += length )
{
int nCopied = stream.getTextCharacters( sourceStart, myBuffer, 0, length );

if (nCopied < length)
break;
}
```

XMLStreamException may be thrown if there are any XML errors in the underlying source.
The "targetStart" argument must be greater than or equal to 0 and less than the length of "target",
Length must be greater than 0 and "targetStart + length" must be less than or equal to length of "target".

**Parameters:**
- sourceStart

- the index of the first character in the source array to copy
- target

- the destination array
- targetStart

- the start offset in the target array
- length

- the number of characters to copy

**Returns:**
- the number of characters actually copied

**Throws:**
- XMLStreamException

- if the underlying XML source is not well-formed
- IndexOutOfBoundsException

- if targetStart < 0 or > than the length of target
- IndexOutOfBoundsException

- if length < 0 or targetStart + length > length of target
- UnsupportedOperationException

- if this method is not supported
- NullPointerException

- is if target is null

---

#### int getTextStart()

Returns the offset into the text character array where the first
character (of this text event) is stored.

**Returns:**
- the starting position of the text in the character array

**Throws:**
- IllegalStateException

- if this state is not
a valid text state.

---

#### int getTextLength()

Returns the length of the sequence of characters for this
Text event within the text character array.

**Returns:**
- the length of the text

**Throws:**
- IllegalStateException

- if this state is not
a valid text state.

---

#### String
getEncoding()

Return input encoding if known or null if unknown.

**Returns:**
- the encoding of this instance or null

---

#### boolean hasText()

Return a boolean indicating whether the current event has text.
The following events have text:
CHARACTERS,DTD ,ENTITY_REFERENCE, COMMENT, SPACE

**Returns:**
- true if the event has text, false otherwise

---

#### Location
getLocation()

Return the current location of the processor.
If the Location is unknown the processor should return
an implementation of Location that returns -1 for the
location and null for the publicId and systemId.
The location information is only valid until next() is
called.

**Returns:**
- the location of the cursor

---

#### QName
getName()

Returns a QName for the current START_ELEMENT or END_ELEMENT event

**Returns:**
- the QName for the current START_ELEMENT or END_ELEMENT event

**Throws:**
- IllegalStateException

- if this is not a START_ELEMENT or
END_ELEMENT

---

#### String
getLocalName()

Returns the (local) name of the current event.
For START_ELEMENT or END_ELEMENT returns the (local) name of the current element.
For ENTITY_REFERENCE it returns entity name.
The current event must be START_ELEMENT or END_ELEMENT,
or ENTITY_REFERENCE

**Returns:**
- the localName

**Throws:**
- IllegalStateException

- if this not a START_ELEMENT,
END_ELEMENT or ENTITY_REFERENCE

---

#### boolean hasName()

returns a boolean indicating whether the current event has a name
(is a START_ELEMENT or END_ELEMENT).

**Returns:**
- true if the event has a name, false otherwise

---

#### String
getNamespaceURI()

If the current event is a START_ELEMENT or END_ELEMENT this method
returns the URI of the prefix or the default namespace.
Returns null if the event does not have a prefix.

**Returns:**
- the URI bound to this elements prefix, the default namespace, or null

---

#### String
getPrefix()

Returns the prefix of the current event or null if the event does not have a prefix

**Returns:**
- the prefix or null

---

#### String
getVersion()

Get the xml version declared on the xml declaration
Returns null if none was declared

**Returns:**
- the XML version or null

---

#### boolean isStandalone()

Get the standalone declaration from the xml declaration

**Returns:**
- true if this is standalone, or false otherwise

---

#### boolean standaloneSet()

Checks if standalone was set in the document

**Returns:**
- true if standalone was set in the document, or false otherwise

---

#### String
getCharacterEncodingScheme()

Returns the character encoding declared on the xml declaration
Returns null if none was declared

**Returns:**
- the encoding declared in the document or null

---

#### String
getPITarget()

Get the target of a processing instruction

**Returns:**
- the target or null

---

#### String
getPIData()

Get the data section of a processing instruction

**Returns:**
- the data or null

---

### Additional Sections

#### Interface XMLStreamReader

**All Superinterfaces:** XMLStreamConstants

**All Known Implementing Classes:** StreamReaderDelegate

```java
public interface
XMLStreamReader

extends
XMLStreamConstants
```

The XMLStreamReader interface allows forward, read-only access to XML.
It is designed to be the lowest level and most efficient way to
read XML data.

The XMLStreamReader is designed to iterate over XML using
next() and hasNext(). The data can be accessed using methods such as getEventType(),
getNamespaceURI(), getLocalName() and getText();

An XMLStreamReader instance is created with an initial event type START_DOCUMENT.
At any moment in time, it has a current event that the methods of the interface
access and may load the next event through the

next()

method.
The current event type can be determined by

getEventType()

, and
the next returned by the

next()

method.

Parsing events are defined as the XML Declaration, a DTD,
start tag, character data, white space, end tag, comment,
or processing instruction. An attribute or namespace event may be encountered
at the root level of a document as the result of a query operation.

For XML 1.0 compliance an XML processor must pass the
identifiers of declared unparsed entities, notation declarations and their
associated identifiers to the application. This information is
provided through the property API on this interface.
The following two properties allow access to this information:
javax.xml.stream.notations and javax.xml.stream.entities.
When the current event is a DTD the following call will return a
list of Notations

List l = (List) getProperty("javax.xml.stream.notations");

The following call will return a list of entity declarations:

List l = (List) getProperty("javax.xml.stream.entities");

These properties can only be accessed during a DTD event and
are defined to return null if the information is not available.

The following table describes which methods are valid in what state.
If a method is called in an invalid state the method will throw a
java.lang.IllegalStateException.

Valid methods for each state

Event Type

Valid Methods

All States

getProperty(), hasNext(), require(), close(),
getNamespaceURI(), isStartElement(),
isEndElement(), isCharacters(), isWhiteSpace(),
getNamespaceContext(), getEventType(),getLocation(),
hasText(), hasName()

START_ELEMENT

next(), getName(), getLocalName(), hasName(), getPrefix(),
getAttributeXXX(), isAttributeSpecified(),
getNamespaceXXX(),
getElementText(), nextTag()

ATTRIBUTE

next(), nextTag()
getAttributeXXX(), isAttributeSpecified(),

NAMESPACE

next(), nextTag()
getNamespaceXXX()

END_ELEMENT

next(), getName(), getLocalName(), hasName(), getPrefix(),
getNamespaceXXX(), nextTag()

CHARACTERS

next(), getTextXXX(), nextTag()

CDATA

next(), getTextXXX(), nextTag()

COMMENT

next(), getTextXXX(), nextTag()

SPACE

next(), getTextXXX(), nextTag()

START_DOCUMENT

next(), getEncoding(), getVersion(), isStandalone(), standaloneSet(),
getCharacterEncodingScheme(), nextTag()

END_DOCUMENT

close()

PROCESSING_INSTRUCTION

next(), getPITarget(), getPIData(), nextTag()

ENTITY_REFERENCE

next(), getLocalName(), getText(), nextTag()

DTD

next(), getText(), nextTag()

**Since:** 1.6
**See Also:** XMLEvent

,

XMLInputFactory

,

XMLStreamWriter

public interface

XMLStreamReader

extends

XMLStreamConstants

The XMLStreamReader interface allows forward, read-only access to XML.
It is designed to be the lowest level and most efficient way to
read XML data.

The XMLStreamReader is designed to iterate over XML using
next() and hasNext(). The data can be accessed using methods such as getEventType(),
getNamespaceURI(), getLocalName() and getText();

An XMLStreamReader instance is created with an initial event type START_DOCUMENT.
At any moment in time, it has a current event that the methods of the interface
access and may load the next event through the

next()

method.
The current event type can be determined by

getEventType()

, and
the next returned by the

next()

method.

Parsing events are defined as the XML Declaration, a DTD,
start tag, character data, white space, end tag, comment,
or processing instruction. An attribute or namespace event may be encountered
at the root level of a document as the result of a query operation.

For XML 1.0 compliance an XML processor must pass the
identifiers of declared unparsed entities, notation declarations and their
associated identifiers to the application. This information is
provided through the property API on this interface.
The following two properties allow access to this information:
javax.xml.stream.notations and javax.xml.stream.entities.
When the current event is a DTD the following call will return a
list of Notations

List l = (List) getProperty("javax.xml.stream.notations");

The following call will return a list of entity declarations:

List l = (List) getProperty("javax.xml.stream.entities");

These properties can only be accessed during a DTD event and
are defined to return null if the information is not available.

The following table describes which methods are valid in what state.
If a method is called in an invalid state the method will throw a
java.lang.IllegalStateException.

Valid methods for each state

Event Type

Valid Methods

All States

getProperty(), hasNext(), require(), close(),
getNamespaceURI(), isStartElement(),
isEndElement(), isCharacters(), isWhiteSpace(),
getNamespaceContext(), getEventType(),getLocation(),
hasText(), hasName()

START_ELEMENT

next(), getName(), getLocalName(), hasName(), getPrefix(),
getAttributeXXX(), isAttributeSpecified(),
getNamespaceXXX(),
getElementText(), nextTag()

ATTRIBUTE

next(), nextTag()
getAttributeXXX(), isAttributeSpecified(),

NAMESPACE

next(), nextTag()
getNamespaceXXX()

END_ELEMENT

next(), getName(), getLocalName(), hasName(), getPrefix(),
getNamespaceXXX(), nextTag()

CHARACTERS

next(), getTextXXX(), nextTag()

CDATA

next(), getTextXXX(), nextTag()

COMMENT

next(), getTextXXX(), nextTag()

SPACE

next(), getTextXXX(), nextTag()

START_DOCUMENT

next(), getEncoding(), getVersion(), isStandalone(), standaloneSet(),
getCharacterEncodingScheme(), nextTag()

END_DOCUMENT

close()

PROCESSING_INSTRUCTION

next(), getPITarget(), getPIData(), nextTag()

ENTITY_REFERENCE

next(), getLocalName(), getText(), nextTag()

DTD

next(), getText(), nextTag()

The XMLStreamReader is designed to iterate over XML using
next() and hasNext(). The data can be accessed using methods such as getEventType(),
getNamespaceURI(), getLocalName() and getText();

An XMLStreamReader instance is created with an initial event type START_DOCUMENT.
At any moment in time, it has a current event that the methods of the interface
access and may load the next event through the

next()

method.
The current event type can be determined by

getEventType()

, and
the next returned by the

next()

method.

Parsing events are defined as the XML Declaration, a DTD,
start tag, character data, white space, end tag, comment,
or processing instruction. An attribute or namespace event may be encountered
at the root level of a document as the result of a query operation.

For XML 1.0 compliance an XML processor must pass the
identifiers of declared unparsed entities, notation declarations and their
associated identifiers to the application. This information is
provided through the property API on this interface.
The following two properties allow access to this information:
javax.xml.stream.notations and javax.xml.stream.entities.
When the current event is a DTD the following call will return a
list of Notations

List l = (List) getProperty("javax.xml.stream.notations");

The following call will return a list of entity declarations:

List l = (List) getProperty("javax.xml.stream.entities");

These properties can only be accessed during a DTD event and
are defined to return null if the information is not available.

The following table describes which methods are valid in what state.
If a method is called in an invalid state the method will throw a
java.lang.IllegalStateException.

Valid methods for each state

Event Type

Valid Methods

All States

getProperty(), hasNext(), require(), close(),
getNamespaceURI(), isStartElement(),
isEndElement(), isCharacters(), isWhiteSpace(),
getNamespaceContext(), getEventType(),getLocation(),
hasText(), hasName()

START_ELEMENT

next(), getName(), getLocalName(), hasName(), getPrefix(),
getAttributeXXX(), isAttributeSpecified(),
getNamespaceXXX(),
getElementText(), nextTag()

ATTRIBUTE

next(), nextTag()
getAttributeXXX(), isAttributeSpecified(),

NAMESPACE

next(), nextTag()
getNamespaceXXX()

END_ELEMENT

next(), getName(), getLocalName(), hasName(), getPrefix(),
getNamespaceXXX(), nextTag()

CHARACTERS

next(), getTextXXX(), nextTag()

CDATA

next(), getTextXXX(), nextTag()

COMMENT

next(), getTextXXX(), nextTag()

SPACE

next(), getTextXXX(), nextTag()

START_DOCUMENT

next(), getEncoding(), getVersion(), isStandalone(), standaloneSet(),
getCharacterEncodingScheme(), nextTag()

END_DOCUMENT

close()

PROCESSING_INSTRUCTION

next(), getPITarget(), getPIData(), nextTag()

ENTITY_REFERENCE

next(), getLocalName(), getText(), nextTag()

DTD

next(), getText(), nextTag()

An XMLStreamReader instance is created with an initial event type START_DOCUMENT.
At any moment in time, it has a current event that the methods of the interface
access and may load the next event through the

next()

method.
The current event type can be determined by

getEventType()

, and
the next returned by the

next()

method.

Parsing events are defined as the XML Declaration, a DTD,
start tag, character data, white space, end tag, comment,
or processing instruction. An attribute or namespace event may be encountered
at the root level of a document as the result of a query operation.

For XML 1.0 compliance an XML processor must pass the
identifiers of declared unparsed entities, notation declarations and their
associated identifiers to the application. This information is
provided through the property API on this interface.
The following two properties allow access to this information:
javax.xml.stream.notations and javax.xml.stream.entities.
When the current event is a DTD the following call will return a
list of Notations

List l = (List) getProperty("javax.xml.stream.notations");

The following call will return a list of entity declarations:

List l = (List) getProperty("javax.xml.stream.entities");

These properties can only be accessed during a DTD event and
are defined to return null if the information is not available.

The following table describes which methods are valid in what state.
If a method is called in an invalid state the method will throw a
java.lang.IllegalStateException.

Valid methods for each state

Event Type

Valid Methods

All States

getProperty(), hasNext(), require(), close(),
getNamespaceURI(), isStartElement(),
isEndElement(), isCharacters(), isWhiteSpace(),
getNamespaceContext(), getEventType(),getLocation(),
hasText(), hasName()

START_ELEMENT

next(), getName(), getLocalName(), hasName(), getPrefix(),
getAttributeXXX(), isAttributeSpecified(),
getNamespaceXXX(),
getElementText(), nextTag()

ATTRIBUTE

next(), nextTag()
getAttributeXXX(), isAttributeSpecified(),

NAMESPACE

next(), nextTag()
getNamespaceXXX()

END_ELEMENT

next(), getName(), getLocalName(), hasName(), getPrefix(),
getNamespaceXXX(), nextTag()

CHARACTERS

next(), getTextXXX(), nextTag()

CDATA

next(), getTextXXX(), nextTag()

COMMENT

next(), getTextXXX(), nextTag()

SPACE

next(), getTextXXX(), nextTag()

START_DOCUMENT

next(), getEncoding(), getVersion(), isStandalone(), standaloneSet(),
getCharacterEncodingScheme(), nextTag()

END_DOCUMENT

close()

PROCESSING_INSTRUCTION

next(), getPITarget(), getPIData(), nextTag()

ENTITY_REFERENCE

next(), getLocalName(), getText(), nextTag()

DTD

next(), getText(), nextTag()

Parsing events are defined as the XML Declaration, a DTD,
start tag, character data, white space, end tag, comment,
or processing instruction. An attribute or namespace event may be encountered
at the root level of a document as the result of a query operation.

For XML 1.0 compliance an XML processor must pass the
identifiers of declared unparsed entities, notation declarations and their
associated identifiers to the application. This information is
provided through the property API on this interface.
The following two properties allow access to this information:
javax.xml.stream.notations and javax.xml.stream.entities.
When the current event is a DTD the following call will return a
list of Notations

List l = (List) getProperty("javax.xml.stream.notations");

The following call will return a list of entity declarations:

List l = (List) getProperty("javax.xml.stream.entities");

These properties can only be accessed during a DTD event and
are defined to return null if the information is not available.

The following table describes which methods are valid in what state.
If a method is called in an invalid state the method will throw a
java.lang.IllegalStateException.

Valid methods for each state

Event Type

Valid Methods

All States

getProperty(), hasNext(), require(), close(),
getNamespaceURI(), isStartElement(),
isEndElement(), isCharacters(), isWhiteSpace(),
getNamespaceContext(), getEventType(),getLocation(),
hasText(), hasName()

START_ELEMENT

next(), getName(), getLocalName(), hasName(), getPrefix(),
getAttributeXXX(), isAttributeSpecified(),
getNamespaceXXX(),
getElementText(), nextTag()

ATTRIBUTE

next(), nextTag()
getAttributeXXX(), isAttributeSpecified(),

NAMESPACE

next(), nextTag()
getNamespaceXXX()

END_ELEMENT

next(), getName(), getLocalName(), hasName(), getPrefix(),
getNamespaceXXX(), nextTag()

CHARACTERS

next(), getTextXXX(), nextTag()

CDATA

next(), getTextXXX(), nextTag()

COMMENT

next(), getTextXXX(), nextTag()

SPACE

next(), getTextXXX(), nextTag()

START_DOCUMENT

next(), getEncoding(), getVersion(), isStandalone(), standaloneSet(),
getCharacterEncodingScheme(), nextTag()

END_DOCUMENT

close()

PROCESSING_INSTRUCTION

next(), getPITarget(), getPIData(), nextTag()

ENTITY_REFERENCE

next(), getLocalName(), getText(), nextTag()

DTD

next(), getText(), nextTag()

For XML 1.0 compliance an XML processor must pass the
identifiers of declared unparsed entities, notation declarations and their
associated identifiers to the application. This information is
provided through the property API on this interface.
The following two properties allow access to this information:
javax.xml.stream.notations and javax.xml.stream.entities.
When the current event is a DTD the following call will return a
list of Notations

List l = (List) getProperty("javax.xml.stream.notations");

The following call will return a list of entity declarations:

List l = (List) getProperty("javax.xml.stream.entities");

These properties can only be accessed during a DTD event and
are defined to return null if the information is not available.

The following table describes which methods are valid in what state.
If a method is called in an invalid state the method will throw a
java.lang.IllegalStateException.

Valid methods for each state

Event Type

Valid Methods

All States

getProperty(), hasNext(), require(), close(),
getNamespaceURI(), isStartElement(),
isEndElement(), isCharacters(), isWhiteSpace(),
getNamespaceContext(), getEventType(),getLocation(),
hasText(), hasName()

START_ELEMENT

next(), getName(), getLocalName(), hasName(), getPrefix(),
getAttributeXXX(), isAttributeSpecified(),
getNamespaceXXX(),
getElementText(), nextTag()

ATTRIBUTE

next(), nextTag()
getAttributeXXX(), isAttributeSpecified(),

NAMESPACE

next(), nextTag()
getNamespaceXXX()

END_ELEMENT

next(), getName(), getLocalName(), hasName(), getPrefix(),
getNamespaceXXX(), nextTag()

CHARACTERS

next(), getTextXXX(), nextTag()

CDATA

next(), getTextXXX(), nextTag()

COMMENT

next(), getTextXXX(), nextTag()

SPACE

next(), getTextXXX(), nextTag()

START_DOCUMENT

next(), getEncoding(), getVersion(), isStandalone(), standaloneSet(),
getCharacterEncodingScheme(), nextTag()

END_DOCUMENT

close()

PROCESSING_INSTRUCTION

next(), getPITarget(), getPIData(), nextTag()

ENTITY_REFERENCE

next(), getLocalName(), getText(), nextTag()

DTD

next(), getText(), nextTag()

The following table describes which methods are valid in what state.
If a method is called in an invalid state the method will throw a
java.lang.IllegalStateException.

Valid methods for each state

Event Type

Valid Methods

All States

getProperty(), hasNext(), require(), close(),
getNamespaceURI(), isStartElement(),
isEndElement(), isCharacters(), isWhiteSpace(),
getNamespaceContext(), getEventType(),getLocation(),
hasText(), hasName()

START_ELEMENT

next(), getName(), getLocalName(), hasName(), getPrefix(),
getAttributeXXX(), isAttributeSpecified(),
getNamespaceXXX(),
getElementText(), nextTag()

ATTRIBUTE

next(), nextTag()
getAttributeXXX(), isAttributeSpecified(),

NAMESPACE

next(), nextTag()
getNamespaceXXX()

END_ELEMENT

next(), getName(), getLocalName(), hasName(), getPrefix(),
getNamespaceXXX(), nextTag()

CHARACTERS

next(), getTextXXX(), nextTag()

CDATA

next(), getTextXXX(), nextTag()

COMMENT

next(), getTextXXX(), nextTag()

SPACE

next(), getTextXXX(), nextTag()

START_DOCUMENT

next(), getEncoding(), getVersion(), isStandalone(), standaloneSet(),
getCharacterEncodingScheme(), nextTag()

END_DOCUMENT

close()

PROCESSING_INSTRUCTION

next(), getPITarget(), getPIData(), nextTag()

ENTITY_REFERENCE

next(), getLocalName(), getText(), nextTag()

DTD

next(), getText(), nextTag()

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

void

close

()

Frees any resources associated with this Reader.

int

getAttributeCount

()

Returns the count of attributes on this START_ELEMENT,
this method is only valid on a START_ELEMENT or ATTRIBUTE.

String

getAttributeLocalName

​(int index)

Returns the localName of the attribute at the provided
index

QName

getAttributeName

​(int index)

Returns the qname of the attribute at the provided index

String

getAttributeNamespace

​(int index)

Returns the namespace of the attribute at the provided
index

String

getAttributePrefix

​(int index)

Returns the prefix of this attribute at the
provided index

String

getAttributeType

​(int index)

Returns the XML type of the attribute at the provided
index

String

getAttributeValue

​(int index)

Returns the value of the attribute at the
index

String

getAttributeValue

​(

String

namespaceURI,

String

localName)

Returns the normalized attribute value of the
attribute with the namespace and localName
If the namespaceURI is null the namespace
is not checked for equality

String

getCharacterEncodingScheme

()

Returns the character encoding declared on the xml declaration
Returns null if none was declared

String

getElementText

()

Reads the content of a text-only element, an exception is thrown if this is
not a text-only element.

String

getEncoding

()

Return input encoding if known or null if unknown.

int

getEventType

()

Returns an integer code that indicates the type of the event the cursor is
pointing to.

String

getLocalName

()

Returns the (local) name of the current event.

Location

getLocation

()

Return the current location of the processor.

QName

getName

()

Returns a QName for the current START_ELEMENT or END_ELEMENT event

NamespaceContext

getNamespaceContext

()

Returns a read only namespace context for the current
position.

int

getNamespaceCount

()

Returns the count of namespaces declared on this START_ELEMENT or END_ELEMENT,
this method is only valid on a START_ELEMENT, END_ELEMENT or NAMESPACE.

String

getNamespacePrefix

​(int index)

Returns the prefix for the namespace declared at the
index.

String

getNamespaceURI

()

If the current event is a START_ELEMENT or END_ELEMENT this method
returns the URI of the prefix or the default namespace.

String

getNamespaceURI

​(int index)

Returns the uri for the namespace declared at the
index.

String

getNamespaceURI

​(

String

prefix)

Return the uri for the given prefix.

String

getPIData

()

Get the data section of a processing instruction

String

getPITarget

()

Get the target of a processing instruction

String

getPrefix

()

Returns the prefix of the current event or null if the event does not have a prefix

Object

getProperty

​(

String

name)

Get the value of a feature/property from the underlying implementation

String

getText

()

Returns the current value of the parse event as a string,
this returns the string value of a CHARACTERS event,
returns the value of a COMMENT, the replacement value
for an ENTITY_REFERENCE, the string value of a CDATA section,
the string value for a SPACE event,
or the String value of the internal subset of the DTD.

char[]

getTextCharacters

()

Returns an array which contains the characters from this event.

int

getTextCharacters

​(int sourceStart,
char[] target,
int targetStart,
int length)

Gets the the text associated with a CHARACTERS, SPACE or CDATA event.

int

getTextLength

()

Returns the length of the sequence of characters for this
Text event within the text character array.

int

getTextStart

()

Returns the offset into the text character array where the first
character (of this text event) is stored.

String

getVersion

()

Get the xml version declared on the xml declaration
Returns null if none was declared

boolean

hasName

()

returns a boolean indicating whether the current event has a name
(is a START_ELEMENT or END_ELEMENT).

boolean

hasNext

()

Returns true if there are more parsing events and false
if there are no more events.

boolean

hasText

()

Return a boolean indicating whether the current event has text.

boolean

isAttributeSpecified

​(int index)

Returns a boolean which indicates if this
attribute was created by default

boolean

isCharacters

()

Returns true if the cursor points to a character data event

boolean

isEndElement

()

Returns true if the cursor points to an end tag (otherwise false)

boolean

isStandalone

()

Get the standalone declaration from the xml declaration

boolean

isStartElement

()

Returns true if the cursor points to a start tag (otherwise false)

boolean

isWhiteSpace

()

Returns true if the cursor points to a character data event
that consists of all whitespace

int

next

()

Get next parsing event - a processor may return all contiguous
character data in a single chunk, or it may split it into several chunks.

int

nextTag

()

Skips any white space (isWhiteSpace() returns true), COMMENT,
or PROCESSING_INSTRUCTION,
until a START_ELEMENT or END_ELEMENT is reached.

void

require

​(int type,

String

namespaceURI,

String

localName)

Test if the current event is of the given type and if the namespace and name match the current
namespace and name of the current event.

boolean

standaloneSet

()

Checks if standalone was set in the document

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

void

close

()

Frees any resources associated with this Reader.

int

getAttributeCount

()

Returns the count of attributes on this START_ELEMENT,
this method is only valid on a START_ELEMENT or ATTRIBUTE.

String

getAttributeLocalName

​(int index)

Returns the localName of the attribute at the provided
index

QName

getAttributeName

​(int index)

Returns the qname of the attribute at the provided index

String

getAttributeNamespace

​(int index)

Returns the namespace of the attribute at the provided
index

String

getAttributePrefix

​(int index)

Returns the prefix of this attribute at the
provided index

String

getAttributeType

​(int index)

Returns the XML type of the attribute at the provided
index

String

getAttributeValue

​(int index)

Returns the value of the attribute at the
index

String

getAttributeValue

​(

String

namespaceURI,

String

localName)

Returns the normalized attribute value of the
attribute with the namespace and localName
If the namespaceURI is null the namespace
is not checked for equality

String

getCharacterEncodingScheme

()

Returns the character encoding declared on the xml declaration
Returns null if none was declared

String

getElementText

()

Reads the content of a text-only element, an exception is thrown if this is
not a text-only element.

String

getEncoding

()

Return input encoding if known or null if unknown.

int

getEventType

()

Returns an integer code that indicates the type of the event the cursor is
pointing to.

String

getLocalName

()

Returns the (local) name of the current event.

Location

getLocation

()

Return the current location of the processor.

QName

getName

()

Returns a QName for the current START_ELEMENT or END_ELEMENT event

NamespaceContext

getNamespaceContext

()

Returns a read only namespace context for the current
position.

int

getNamespaceCount

()

Returns the count of namespaces declared on this START_ELEMENT or END_ELEMENT,
this method is only valid on a START_ELEMENT, END_ELEMENT or NAMESPACE.

String

getNamespacePrefix

​(int index)

Returns the prefix for the namespace declared at the
index.

String

getNamespaceURI

()

If the current event is a START_ELEMENT or END_ELEMENT this method
returns the URI of the prefix or the default namespace.

String

getNamespaceURI

​(int index)

Returns the uri for the namespace declared at the
index.

String

getNamespaceURI

​(

String

prefix)

Return the uri for the given prefix.

String

getPIData

()

Get the data section of a processing instruction

String

getPITarget

()

Get the target of a processing instruction

String

getPrefix

()

Returns the prefix of the current event or null if the event does not have a prefix

Object

getProperty

​(

String

name)

Get the value of a feature/property from the underlying implementation

String

getText

()

Returns the current value of the parse event as a string,
this returns the string value of a CHARACTERS event,
returns the value of a COMMENT, the replacement value
for an ENTITY_REFERENCE, the string value of a CDATA section,
the string value for a SPACE event,
or the String value of the internal subset of the DTD.

char[]

getTextCharacters

()

Returns an array which contains the characters from this event.

int

getTextCharacters

​(int sourceStart,
char[] target,
int targetStart,
int length)

Gets the the text associated with a CHARACTERS, SPACE or CDATA event.

int

getTextLength

()

Returns the length of the sequence of characters for this
Text event within the text character array.

int

getTextStart

()

Returns the offset into the text character array where the first
character (of this text event) is stored.

String

getVersion

()

Get the xml version declared on the xml declaration
Returns null if none was declared

boolean

hasName

()

returns a boolean indicating whether the current event has a name
(is a START_ELEMENT or END_ELEMENT).

boolean

hasNext

()

Returns true if there are more parsing events and false
if there are no more events.

boolean

hasText

()

Return a boolean indicating whether the current event has text.

boolean

isAttributeSpecified

​(int index)

Returns a boolean which indicates if this
attribute was created by default

boolean

isCharacters

()

Returns true if the cursor points to a character data event

boolean

isEndElement

()

Returns true if the cursor points to an end tag (otherwise false)

boolean

isStandalone

()

Get the standalone declaration from the xml declaration

boolean

isStartElement

()

Returns true if the cursor points to a start tag (otherwise false)

boolean

isWhiteSpace

()

Returns true if the cursor points to a character data event
that consists of all whitespace

int

next

()

Get next parsing event - a processor may return all contiguous
character data in a single chunk, or it may split it into several chunks.

int

nextTag

()

Skips any white space (isWhiteSpace() returns true), COMMENT,
or PROCESSING_INSTRUCTION,
until a START_ELEMENT or END_ELEMENT is reached.

void

require

​(int type,

String

namespaceURI,

String

localName)

Test if the current event is of the given type and if the namespace and name match the current
namespace and name of the current event.

boolean

standaloneSet

()

Checks if standalone was set in the document

---

#### Method Summary

Frees any resources associated with this Reader.

Returns the count of attributes on this START_ELEMENT,
this method is only valid on a START_ELEMENT or ATTRIBUTE.

Returns the localName of the attribute at the provided
index

Returns the qname of the attribute at the provided index

Returns the namespace of the attribute at the provided
index

Returns the prefix of this attribute at the
provided index

Returns the XML type of the attribute at the provided
index

Returns the value of the attribute at the
index

Returns the normalized attribute value of the
attribute with the namespace and localName
If the namespaceURI is null the namespace
is not checked for equality

Returns the character encoding declared on the xml declaration
Returns null if none was declared

Reads the content of a text-only element, an exception is thrown if this is
not a text-only element.

Return input encoding if known or null if unknown.

Returns an integer code that indicates the type of the event the cursor is
pointing to.

Returns the (local) name of the current event.

Return the current location of the processor.

Returns a QName for the current START_ELEMENT or END_ELEMENT event

Returns a read only namespace context for the current
position.

Returns the count of namespaces declared on this START_ELEMENT or END_ELEMENT,
this method is only valid on a START_ELEMENT, END_ELEMENT or NAMESPACE.

Returns the prefix for the namespace declared at the
index.

If the current event is a START_ELEMENT or END_ELEMENT this method
returns the URI of the prefix or the default namespace.

Returns the uri for the namespace declared at the
index.

Return the uri for the given prefix.

Get the data section of a processing instruction

Get the target of a processing instruction

Returns the prefix of the current event or null if the event does not have a prefix

Get the value of a feature/property from the underlying implementation

Returns the current value of the parse event as a string,
this returns the string value of a CHARACTERS event,
returns the value of a COMMENT, the replacement value
for an ENTITY_REFERENCE, the string value of a CDATA section,
the string value for a SPACE event,
or the String value of the internal subset of the DTD.

Returns an array which contains the characters from this event.

Gets the the text associated with a CHARACTERS, SPACE or CDATA event.

Returns the length of the sequence of characters for this
Text event within the text character array.

Returns the offset into the text character array where the first
character (of this text event) is stored.

Get the xml version declared on the xml declaration
Returns null if none was declared

returns a boolean indicating whether the current event has a name
(is a START_ELEMENT or END_ELEMENT).

Returns true if there are more parsing events and false
if there are no more events.

Return a boolean indicating whether the current event has text.

Returns a boolean which indicates if this
attribute was created by default

Returns true if the cursor points to a character data event

Returns true if the cursor points to an end tag (otherwise false)

Get the standalone declaration from the xml declaration

Returns true if the cursor points to a start tag (otherwise false)

Returns true if the cursor points to a character data event
that consists of all whitespace

Get next parsing event - a processor may return all contiguous
character data in a single chunk, or it may split it into several chunks.

Skips any white space (isWhiteSpace() returns true), COMMENT,
or PROCESSING_INSTRUCTION,
until a START_ELEMENT or END_ELEMENT is reached.

Test if the current event is of the given type and if the namespace and name match the current
namespace and name of the current event.

Checks if standalone was set in the document

============ METHOD DETAIL ==========

- Method Detail

- getProperty

```java
Object
getProperty​(
String
name)
throws
IllegalArgumentException
```

Get the value of a feature/property from the underlying implementation

**Parameters:** name

- The name of the property, may not be null
**Returns:** The value of the property
**Throws:** IllegalArgumentException

- if name is null

- next

```java
int next()
throws
XMLStreamException
```

Get next parsing event - a processor may return all contiguous
character data in a single chunk, or it may split it into several chunks.
If the property javax.xml.stream.isCoalescing is set to true
element content must be coalesced and only one CHARACTERS event
must be returned for contiguous element content or
CDATA Sections.

By default entity references must be
expanded and reported transparently to the application.
An exception will be thrown if an entity reference cannot be expanded.
If element content is empty (i.e. content is "") then no CHARACTERS event will be reported.

Given the following XML:

<foo><!--description-->content text<![CDATA[<greeting>Hello>/greeting>]]>other content>/foo>

The behavior of calling next() when being on foo will be:

1- the comment (COMMENT)

2- then the characters section (CHARACTERS)

3- then the CDATA section (another CHARACTERS)

4- then the next characters section (another CHARACTERS)

5- then the END_ELEMENT

NOTE:

empty element (such as

<tag/>

) will be reported
with two separate events: START_ELEMENT, END_ELEMENT - This preserves
parsing equivalency of empty element to

<tag></tag>

.

This method will throw an IllegalStateException if it is called after hasNext() returns false.

**Returns:** the integer code corresponding to the current parse event
**Throws:** NoSuchElementException

- if this is called when hasNext() returns false
**Throws:** XMLStreamException

- if there is an error processing the underlying XML source
**See Also:** XMLEvent

- require

```java
void require​(int type,

String
namespaceURI,

String
localName)
throws
XMLStreamException
```

Test if the current event is of the given type and if the namespace and name match the current
namespace and name of the current event. If the namespaceURI is null it is not checked for equality,
if the localName is null it is not checked for equality.

**Parameters:** type

- the event type
**Parameters:** namespaceURI

- the uri of the event, may be null
**Parameters:** localName

- the localName of the event, may be null
**Throws:** XMLStreamException

- if the required values are not matched.

- getElementText

```java
String
getElementText()
throws
XMLStreamException
```

Reads the content of a text-only element, an exception is thrown if this is
not a text-only element.
Regardless of value of javax.xml.stream.isCoalescing this method always returns coalesced content.

Precondition: the current event is START_ELEMENT.

Postcondition: the current event is the corresponding END_ELEMENT.

The method does the following (implementations are free to optimized
but must do equivalent processing):

```java
if(getEventType() != XMLStreamConstants.START_ELEMENT) {
throw new XMLStreamException(
"parser must be on START_ELEMENT to read next text", getLocation());
}

int eventType = next();
StringBuffer content = new StringBuffer();
while(eventType != XMLStreamConstants.END_ELEMENT) {
if(eventType == XMLStreamConstants.CHARACTERS
|| eventType == XMLStreamConstants.CDATA
|| eventType == XMLStreamConstants.SPACE
|| eventType == XMLStreamConstants.ENTITY_REFERENCE) {
buf.append(getText());
} else if(eventType == XMLStreamConstants.PROCESSING_INSTRUCTION
|| eventType == XMLStreamConstants.COMMENT) {
// skipping
} else if(eventType == XMLStreamConstants.END_DOCUMENT) {
throw new XMLStreamException(
"unexpected end of document when reading element text content", this);
} else if(eventType == XMLStreamConstants.START_ELEMENT) {
throw new XMLStreamException(
"element text content may not contain START_ELEMENT", getLocation());
} else {
throw new XMLStreamException(
"Unexpected event type "+eventType, getLocation());
}
eventType = next();
}
return buf.toString();
```

**Throws:** XMLStreamException

- if the current event is not a START_ELEMENT
or if a non text element is encountered

- nextTag

```java
int nextTag()
throws
XMLStreamException
```

Skips any white space (isWhiteSpace() returns true), COMMENT,
or PROCESSING_INSTRUCTION,
until a START_ELEMENT or END_ELEMENT is reached.
If other than white space characters, COMMENT, PROCESSING_INSTRUCTION, START_ELEMENT, END_ELEMENT
are encountered, an exception is thrown. This method should
be used when processing element-only content seperated by white space.

Precondition: none

Postcondition: the current event is START_ELEMENT or END_ELEMENT
and cursor may have moved over any whitespace event.

Essentially it does the following (implementations are free to optimized
but must do equivalent processing):

```java
int eventType = next();
while((eventType == XMLStreamConstants.CHARACTERS && isWhiteSpace()) // skip whitespace
|| (eventType == XMLStreamConstants.CDATA && isWhiteSpace())
// skip whitespace
|| eventType == XMLStreamConstants.SPACE
|| eventType == XMLStreamConstants.PROCESSING_INSTRUCTION
|| eventType == XMLStreamConstants.COMMENT
) {
eventType = next();
}
if (eventType != XMLStreamConstants.START_ELEMENT && eventType != XMLStreamConstants.END_ELEMENT) {
throw new String XMLStreamException("expected start or end tag", getLocation());
}
return eventType;
```

**Returns:** the event type of the element read (START_ELEMENT or END_ELEMENT)
**Throws:** XMLStreamException

- if the current event is not white space, PROCESSING_INSTRUCTION,
START_ELEMENT or END_ELEMENT
**Throws:** NoSuchElementException

- if this is called when hasNext() returns false

- hasNext

```java
boolean hasNext()
throws
XMLStreamException
```

Returns true if there are more parsing events and false
if there are no more events. This method will return
false if the current state of the XMLStreamReader is
END_DOCUMENT

**Returns:** true if there are more events, false otherwise
**Throws:** XMLStreamException

- if there is a fatal error detecting the next state

- close

```java
void close()
throws
XMLStreamException
```

Frees any resources associated with this Reader. This method does not close the
underlying input source.

**Throws:** XMLStreamException

- if there are errors freeing associated resources

- getNamespaceURI

```java
String
getNamespaceURI​(
String
prefix)
```

Return the uri for the given prefix.
The uri returned depends on the current state of the processor.

NOTE:

The 'xml' prefix is bound as defined in

Namespaces in XML

specification to "http://www.w3.org/XML/1998/namespace".

NOTE:

The 'xmlns' prefix must be resolved to following namespace

http://www.w3.org/2000/xmlns/

**Parameters:** prefix

- The prefix to lookup, may not be null
**Returns:** the uri bound to the given prefix or null if it is not bound
**Throws:** IllegalArgumentException

- if the prefix is null

- isStartElement

```java
boolean isStartElement()
```

Returns true if the cursor points to a start tag (otherwise false)

**Returns:** true if the cursor points to a start tag, false otherwise

- isEndElement

```java
boolean isEndElement()
```

Returns true if the cursor points to an end tag (otherwise false)

**Returns:** true if the cursor points to an end tag, false otherwise

- isCharacters

```java
boolean isCharacters()
```

Returns true if the cursor points to a character data event

**Returns:** true if the cursor points to character data, false otherwise

- isWhiteSpace

```java
boolean isWhiteSpace()
```

Returns true if the cursor points to a character data event
that consists of all whitespace

**Returns:** true if the cursor points to all whitespace, false otherwise

- getAttributeValue

```java
String
getAttributeValue​(
String
namespaceURI,

String
localName)
```

Returns the normalized attribute value of the
attribute with the namespace and localName
If the namespaceURI is null the namespace
is not checked for equality

**Parameters:** namespaceURI

- the namespace of the attribute
**Parameters:** localName

- the local name of the attribute, cannot be null
**Returns:** returns the value of the attribute , returns null if not found
**Throws:** IllegalStateException

- if this is not a START_ELEMENT or ATTRIBUTE

- getAttributeCount

```java
int getAttributeCount()
```

Returns the count of attributes on this START_ELEMENT,
this method is only valid on a START_ELEMENT or ATTRIBUTE. This
count excludes namespace definitions. Attribute indices are
zero-based.

**Returns:** returns the number of attributes
**Throws:** IllegalStateException

- if this is not a START_ELEMENT or ATTRIBUTE

- getAttributeName

```java
QName
getAttributeName​(int index)
```

Returns the qname of the attribute at the provided index

**Parameters:** index

- the position of the attribute
**Returns:** the QName of the attribute
**Throws:** IllegalStateException

- if this is not a START_ELEMENT or ATTRIBUTE

- getAttributeNamespace

```java
String
getAttributeNamespace​(int index)
```

Returns the namespace of the attribute at the provided
index

**Parameters:** index

- the position of the attribute
**Returns:** the namespace URI (can be null)
**Throws:** IllegalStateException

- if this is not a START_ELEMENT or ATTRIBUTE

- getAttributeLocalName

```java
String
getAttributeLocalName​(int index)
```

Returns the localName of the attribute at the provided
index

**Parameters:** index

- the position of the attribute
**Returns:** the localName of the attribute
**Throws:** IllegalStateException

- if this is not a START_ELEMENT or ATTRIBUTE

- getAttributePrefix

```java
String
getAttributePrefix​(int index)
```

Returns the prefix of this attribute at the
provided index

**Parameters:** index

- the position of the attribute
**Returns:** the prefix of the attribute
**Throws:** IllegalStateException

- if this is not a START_ELEMENT or ATTRIBUTE

- getAttributeType

```java
String
getAttributeType​(int index)
```

Returns the XML type of the attribute at the provided
index

**Parameters:** index

- the position of the attribute
**Returns:** the XML type of the attribute
**Throws:** IllegalStateException

- if this is not a START_ELEMENT or ATTRIBUTE

- getAttributeValue

```java
String
getAttributeValue​(int index)
```

Returns the value of the attribute at the
index

**Parameters:** index

- the position of the attribute
**Returns:** the attribute value
**Throws:** IllegalStateException

- if this is not a START_ELEMENT or ATTRIBUTE

- isAttributeSpecified

```java
boolean isAttributeSpecified​(int index)
```

Returns a boolean which indicates if this
attribute was created by default

**Parameters:** index

- the position of the attribute
**Returns:** true if this is a default attribute
**Throws:** IllegalStateException

- if this is not a START_ELEMENT or ATTRIBUTE

- getNamespaceCount

```java
int getNamespaceCount()
```

Returns the count of namespaces declared on this START_ELEMENT or END_ELEMENT,
this method is only valid on a START_ELEMENT, END_ELEMENT or NAMESPACE. On
an END_ELEMENT the count is of the namespaces that are about to go
out of scope. This is the equivalent of the information reported
by SAX callback for an end element event.

**Returns:** returns the number of namespace declarations on this specific element
**Throws:** IllegalStateException

- if this is not a START_ELEMENT, END_ELEMENT or NAMESPACE

- getNamespacePrefix

```java
String
getNamespacePrefix​(int index)
```

Returns the prefix for the namespace declared at the
index. Returns null if this is the default namespace
declaration

**Parameters:** index

- the position of the namespace declaration
**Returns:** returns the namespace prefix
**Throws:** IllegalStateException

- if this is not a START_ELEMENT, END_ELEMENT or NAMESPACE

- getNamespaceURI

```java
String
getNamespaceURI​(int index)
```

Returns the uri for the namespace declared at the
index.

**Parameters:** index

- the position of the namespace declaration
**Returns:** returns the namespace uri
**Throws:** IllegalStateException

- if this is not a START_ELEMENT, END_ELEMENT or NAMESPACE

- getNamespaceContext

```java
NamespaceContext
getNamespaceContext()
```

Returns a read only namespace context for the current
position. The context is transient and only valid until
a call to next() changes the state of the reader.

**Returns:** return a namespace context

- getEventType

```java
int getEventType()
```

Returns an integer code that indicates the type of the event the cursor is
pointing to. The initial event type is

XMLStreamConstants.START_DOCUMENT

.

**Returns:** the type of the current event

- getText

```java
String
getText()
```

Returns the current value of the parse event as a string,
this returns the string value of a CHARACTERS event,
returns the value of a COMMENT, the replacement value
for an ENTITY_REFERENCE, the string value of a CDATA section,
the string value for a SPACE event,
or the String value of the internal subset of the DTD.
If an ENTITY_REFERENCE has been resolved, any character data
will be reported as CHARACTERS events.

**Returns:** the current text or null
**Throws:** IllegalStateException

- if this state is not
a valid text state.

- getTextCharacters

```java
char[] getTextCharacters()
```

Returns an array which contains the characters from this event.
This array should be treated as read-only and transient. I.e. the array will
contain the text characters until the XMLStreamReader moves on to the next event.
Attempts to hold onto the character array beyond that time or modify the
contents of the array are breaches of the contract for this interface.

**Returns:** the current text or an empty array
**Throws:** IllegalStateException

- if this state is not
a valid text state.

- getTextCharacters

```java
int getTextCharacters​(int sourceStart,
char[] target,
int targetStart,
int length)
throws
XMLStreamException
```

Gets the the text associated with a CHARACTERS, SPACE or CDATA event.
Text starting a "sourceStart" is copied into "target" starting at "targetStart".
Up to "length" characters are copied. The number of characters actually copied is returned.

The "sourceStart" argument must be greater or equal to 0 and less than or equal to
the number of characters associated with the event. Usually, one requests text starting at a "sourceStart" of 0.
If the number of characters actually copied is less than the "length", then there is no more text.
Otherwise, subsequent calls need to be made until all text has been retrieved. For example:

```java
int length = 1024;
char[] myBuffer = new char[ length ];

for ( int sourceStart = 0 ; ; sourceStart += length )
{
int nCopied = stream.getTextCharacters( sourceStart, myBuffer, 0, length );

if (nCopied < length)
break;
}
```

XMLStreamException may be thrown if there are any XML errors in the underlying source.
The "targetStart" argument must be greater than or equal to 0 and less than the length of "target",
Length must be greater than 0 and "targetStart + length" must be less than or equal to length of "target".

**Parameters:** sourceStart

- the index of the first character in the source array to copy
**Parameters:** target

- the destination array
**Parameters:** targetStart

- the start offset in the target array
**Parameters:** length

- the number of characters to copy
**Returns:** the number of characters actually copied
**Throws:** XMLStreamException

- if the underlying XML source is not well-formed
**Throws:** IndexOutOfBoundsException

- if targetStart < 0 or > than the length of target
**Throws:** IndexOutOfBoundsException

- if length < 0 or targetStart + length > length of target
**Throws:** UnsupportedOperationException

- if this method is not supported
**Throws:** NullPointerException

- is if target is null

- getTextStart

```java
int getTextStart()
```

Returns the offset into the text character array where the first
character (of this text event) is stored.

**Returns:** the starting position of the text in the character array
**Throws:** IllegalStateException

- if this state is not
a valid text state.

- getTextLength

```java
int getTextLength()
```

Returns the length of the sequence of characters for this
Text event within the text character array.

**Returns:** the length of the text
**Throws:** IllegalStateException

- if this state is not
a valid text state.

- getEncoding

```java
String
getEncoding()
```

Return input encoding if known or null if unknown.

**Returns:** the encoding of this instance or null

- hasText

```java
boolean hasText()
```

Return a boolean indicating whether the current event has text.
The following events have text:
CHARACTERS,DTD ,ENTITY_REFERENCE, COMMENT, SPACE

**Returns:** true if the event has text, false otherwise

- getLocation

```java
Location
getLocation()
```

Return the current location of the processor.
If the Location is unknown the processor should return
an implementation of Location that returns -1 for the
location and null for the publicId and systemId.
The location information is only valid until next() is
called.

**Returns:** the location of the cursor

- getName

```java
QName
getName()
```

Returns a QName for the current START_ELEMENT or END_ELEMENT event

**Returns:** the QName for the current START_ELEMENT or END_ELEMENT event
**Throws:** IllegalStateException

- if this is not a START_ELEMENT or
END_ELEMENT

- getLocalName

```java
String
getLocalName()
```

Returns the (local) name of the current event.
For START_ELEMENT or END_ELEMENT returns the (local) name of the current element.
For ENTITY_REFERENCE it returns entity name.
The current event must be START_ELEMENT or END_ELEMENT,
or ENTITY_REFERENCE

**Returns:** the localName
**Throws:** IllegalStateException

- if this not a START_ELEMENT,
END_ELEMENT or ENTITY_REFERENCE

- hasName

```java
boolean hasName()
```

returns a boolean indicating whether the current event has a name
(is a START_ELEMENT or END_ELEMENT).

**Returns:** true if the event has a name, false otherwise

- getNamespaceURI

```java
String
getNamespaceURI()
```

If the current event is a START_ELEMENT or END_ELEMENT this method
returns the URI of the prefix or the default namespace.
Returns null if the event does not have a prefix.

**Returns:** the URI bound to this elements prefix, the default namespace, or null

- getPrefix

```java
String
getPrefix()
```

Returns the prefix of the current event or null if the event does not have a prefix

**Returns:** the prefix or null

- getVersion

```java
String
getVersion()
```

Get the xml version declared on the xml declaration
Returns null if none was declared

**Returns:** the XML version or null

- isStandalone

```java
boolean isStandalone()
```

Get the standalone declaration from the xml declaration

**Returns:** true if this is standalone, or false otherwise

- standaloneSet

```java
boolean standaloneSet()
```

Checks if standalone was set in the document

**Returns:** true if standalone was set in the document, or false otherwise

- getCharacterEncodingScheme

```java
String
getCharacterEncodingScheme()
```

Returns the character encoding declared on the xml declaration
Returns null if none was declared

**Returns:** the encoding declared in the document or null

- getPITarget

```java
String
getPITarget()
```

Get the target of a processing instruction

**Returns:** the target or null

- getPIData

```java
String
getPIData()
```

Get the data section of a processing instruction

**Returns:** the data or null

Method Detail

- getProperty

```java
Object
getProperty​(
String
name)
throws
IllegalArgumentException
```

Get the value of a feature/property from the underlying implementation

**Parameters:** name

- The name of the property, may not be null
**Returns:** The value of the property
**Throws:** IllegalArgumentException

- if name is null

- next

```java
int next()
throws
XMLStreamException
```

Get next parsing event - a processor may return all contiguous
character data in a single chunk, or it may split it into several chunks.
If the property javax.xml.stream.isCoalescing is set to true
element content must be coalesced and only one CHARACTERS event
must be returned for contiguous element content or
CDATA Sections.

By default entity references must be
expanded and reported transparently to the application.
An exception will be thrown if an entity reference cannot be expanded.
If element content is empty (i.e. content is "") then no CHARACTERS event will be reported.

Given the following XML:

<foo><!--description-->content text<![CDATA[<greeting>Hello>/greeting>]]>other content>/foo>

The behavior of calling next() when being on foo will be:

1- the comment (COMMENT)

2- then the characters section (CHARACTERS)

3- then the CDATA section (another CHARACTERS)

4- then the next characters section (another CHARACTERS)

5- then the END_ELEMENT

NOTE:

empty element (such as

<tag/>

) will be reported
with two separate events: START_ELEMENT, END_ELEMENT - This preserves
parsing equivalency of empty element to

<tag></tag>

.

This method will throw an IllegalStateException if it is called after hasNext() returns false.

**Returns:** the integer code corresponding to the current parse event
**Throws:** NoSuchElementException

- if this is called when hasNext() returns false
**Throws:** XMLStreamException

- if there is an error processing the underlying XML source
**See Also:** XMLEvent

- require

```java
void require​(int type,

String
namespaceURI,

String
localName)
throws
XMLStreamException
```

Test if the current event is of the given type and if the namespace and name match the current
namespace and name of the current event. If the namespaceURI is null it is not checked for equality,
if the localName is null it is not checked for equality.

**Parameters:** type

- the event type
**Parameters:** namespaceURI

- the uri of the event, may be null
**Parameters:** localName

- the localName of the event, may be null
**Throws:** XMLStreamException

- if the required values are not matched.

- getElementText

```java
String
getElementText()
throws
XMLStreamException
```

Reads the content of a text-only element, an exception is thrown if this is
not a text-only element.
Regardless of value of javax.xml.stream.isCoalescing this method always returns coalesced content.

Precondition: the current event is START_ELEMENT.

Postcondition: the current event is the corresponding END_ELEMENT.

The method does the following (implementations are free to optimized
but must do equivalent processing):

```java
if(getEventType() != XMLStreamConstants.START_ELEMENT) {
throw new XMLStreamException(
"parser must be on START_ELEMENT to read next text", getLocation());
}

int eventType = next();
StringBuffer content = new StringBuffer();
while(eventType != XMLStreamConstants.END_ELEMENT) {
if(eventType == XMLStreamConstants.CHARACTERS
|| eventType == XMLStreamConstants.CDATA
|| eventType == XMLStreamConstants.SPACE
|| eventType == XMLStreamConstants.ENTITY_REFERENCE) {
buf.append(getText());
} else if(eventType == XMLStreamConstants.PROCESSING_INSTRUCTION
|| eventType == XMLStreamConstants.COMMENT) {
// skipping
} else if(eventType == XMLStreamConstants.END_DOCUMENT) {
throw new XMLStreamException(
"unexpected end of document when reading element text content", this);
} else if(eventType == XMLStreamConstants.START_ELEMENT) {
throw new XMLStreamException(
"element text content may not contain START_ELEMENT", getLocation());
} else {
throw new XMLStreamException(
"Unexpected event type "+eventType, getLocation());
}
eventType = next();
}
return buf.toString();
```

**Throws:** XMLStreamException

- if the current event is not a START_ELEMENT
or if a non text element is encountered

- nextTag

```java
int nextTag()
throws
XMLStreamException
```

Skips any white space (isWhiteSpace() returns true), COMMENT,
or PROCESSING_INSTRUCTION,
until a START_ELEMENT or END_ELEMENT is reached.
If other than white space characters, COMMENT, PROCESSING_INSTRUCTION, START_ELEMENT, END_ELEMENT
are encountered, an exception is thrown. This method should
be used when processing element-only content seperated by white space.

Precondition: none

Postcondition: the current event is START_ELEMENT or END_ELEMENT
and cursor may have moved over any whitespace event.

Essentially it does the following (implementations are free to optimized
but must do equivalent processing):

```java
int eventType = next();
while((eventType == XMLStreamConstants.CHARACTERS && isWhiteSpace()) // skip whitespace
|| (eventType == XMLStreamConstants.CDATA && isWhiteSpace())
// skip whitespace
|| eventType == XMLStreamConstants.SPACE
|| eventType == XMLStreamConstants.PROCESSING_INSTRUCTION
|| eventType == XMLStreamConstants.COMMENT
) {
eventType = next();
}
if (eventType != XMLStreamConstants.START_ELEMENT && eventType != XMLStreamConstants.END_ELEMENT) {
throw new String XMLStreamException("expected start or end tag", getLocation());
}
return eventType;
```

**Returns:** the event type of the element read (START_ELEMENT or END_ELEMENT)
**Throws:** XMLStreamException

- if the current event is not white space, PROCESSING_INSTRUCTION,
START_ELEMENT or END_ELEMENT
**Throws:** NoSuchElementException

- if this is called when hasNext() returns false

- hasNext

```java
boolean hasNext()
throws
XMLStreamException
```

Returns true if there are more parsing events and false
if there are no more events. This method will return
false if the current state of the XMLStreamReader is
END_DOCUMENT

**Returns:** true if there are more events, false otherwise
**Throws:** XMLStreamException

- if there is a fatal error detecting the next state

- close

```java
void close()
throws
XMLStreamException
```

Frees any resources associated with this Reader. This method does not close the
underlying input source.

**Throws:** XMLStreamException

- if there are errors freeing associated resources

- getNamespaceURI

```java
String
getNamespaceURI​(
String
prefix)
```

Return the uri for the given prefix.
The uri returned depends on the current state of the processor.

NOTE:

The 'xml' prefix is bound as defined in

Namespaces in XML

specification to "http://www.w3.org/XML/1998/namespace".

NOTE:

The 'xmlns' prefix must be resolved to following namespace

http://www.w3.org/2000/xmlns/

**Parameters:** prefix

- The prefix to lookup, may not be null
**Returns:** the uri bound to the given prefix or null if it is not bound
**Throws:** IllegalArgumentException

- if the prefix is null

- isStartElement

```java
boolean isStartElement()
```

Returns true if the cursor points to a start tag (otherwise false)

**Returns:** true if the cursor points to a start tag, false otherwise

- isEndElement

```java
boolean isEndElement()
```

Returns true if the cursor points to an end tag (otherwise false)

**Returns:** true if the cursor points to an end tag, false otherwise

- isCharacters

```java
boolean isCharacters()
```

Returns true if the cursor points to a character data event

**Returns:** true if the cursor points to character data, false otherwise

- isWhiteSpace

```java
boolean isWhiteSpace()
```

Returns true if the cursor points to a character data event
that consists of all whitespace

**Returns:** true if the cursor points to all whitespace, false otherwise

- getAttributeValue

```java
String
getAttributeValue​(
String
namespaceURI,

String
localName)
```

Returns the normalized attribute value of the
attribute with the namespace and localName
If the namespaceURI is null the namespace
is not checked for equality

**Parameters:** namespaceURI

- the namespace of the attribute
**Parameters:** localName

- the local name of the attribute, cannot be null
**Returns:** returns the value of the attribute , returns null if not found
**Throws:** IllegalStateException

- if this is not a START_ELEMENT or ATTRIBUTE

- getAttributeCount

```java
int getAttributeCount()
```

Returns the count of attributes on this START_ELEMENT,
this method is only valid on a START_ELEMENT or ATTRIBUTE. This
count excludes namespace definitions. Attribute indices are
zero-based.

**Returns:** returns the number of attributes
**Throws:** IllegalStateException

- if this is not a START_ELEMENT or ATTRIBUTE

- getAttributeName

```java
QName
getAttributeName​(int index)
```

Returns the qname of the attribute at the provided index

**Parameters:** index

- the position of the attribute
**Returns:** the QName of the attribute
**Throws:** IllegalStateException

- if this is not a START_ELEMENT or ATTRIBUTE

- getAttributeNamespace

```java
String
getAttributeNamespace​(int index)
```

Returns the namespace of the attribute at the provided
index

**Parameters:** index

- the position of the attribute
**Returns:** the namespace URI (can be null)
**Throws:** IllegalStateException

- if this is not a START_ELEMENT or ATTRIBUTE

- getAttributeLocalName

```java
String
getAttributeLocalName​(int index)
```

Returns the localName of the attribute at the provided
index

**Parameters:** index

- the position of the attribute
**Returns:** the localName of the attribute
**Throws:** IllegalStateException

- if this is not a START_ELEMENT or ATTRIBUTE

- getAttributePrefix

```java
String
getAttributePrefix​(int index)
```

Returns the prefix of this attribute at the
provided index

**Parameters:** index

- the position of the attribute
**Returns:** the prefix of the attribute
**Throws:** IllegalStateException

- if this is not a START_ELEMENT or ATTRIBUTE

- getAttributeType

```java
String
getAttributeType​(int index)
```

Returns the XML type of the attribute at the provided
index

**Parameters:** index

- the position of the attribute
**Returns:** the XML type of the attribute
**Throws:** IllegalStateException

- if this is not a START_ELEMENT or ATTRIBUTE

- getAttributeValue

```java
String
getAttributeValue​(int index)
```

Returns the value of the attribute at the
index

**Parameters:** index

- the position of the attribute
**Returns:** the attribute value
**Throws:** IllegalStateException

- if this is not a START_ELEMENT or ATTRIBUTE

- isAttributeSpecified

```java
boolean isAttributeSpecified​(int index)
```

Returns a boolean which indicates if this
attribute was created by default

**Parameters:** index

- the position of the attribute
**Returns:** true if this is a default attribute
**Throws:** IllegalStateException

- if this is not a START_ELEMENT or ATTRIBUTE

- getNamespaceCount

```java
int getNamespaceCount()
```

Returns the count of namespaces declared on this START_ELEMENT or END_ELEMENT,
this method is only valid on a START_ELEMENT, END_ELEMENT or NAMESPACE. On
an END_ELEMENT the count is of the namespaces that are about to go
out of scope. This is the equivalent of the information reported
by SAX callback for an end element event.

**Returns:** returns the number of namespace declarations on this specific element
**Throws:** IllegalStateException

- if this is not a START_ELEMENT, END_ELEMENT or NAMESPACE

- getNamespacePrefix

```java
String
getNamespacePrefix​(int index)
```

Returns the prefix for the namespace declared at the
index. Returns null if this is the default namespace
declaration

**Parameters:** index

- the position of the namespace declaration
**Returns:** returns the namespace prefix
**Throws:** IllegalStateException

- if this is not a START_ELEMENT, END_ELEMENT or NAMESPACE

- getNamespaceURI

```java
String
getNamespaceURI​(int index)
```

Returns the uri for the namespace declared at the
index.

**Parameters:** index

- the position of the namespace declaration
**Returns:** returns the namespace uri
**Throws:** IllegalStateException

- if this is not a START_ELEMENT, END_ELEMENT or NAMESPACE

- getNamespaceContext

```java
NamespaceContext
getNamespaceContext()
```

Returns a read only namespace context for the current
position. The context is transient and only valid until
a call to next() changes the state of the reader.

**Returns:** return a namespace context

- getEventType

```java
int getEventType()
```

Returns an integer code that indicates the type of the event the cursor is
pointing to. The initial event type is

XMLStreamConstants.START_DOCUMENT

.

**Returns:** the type of the current event

- getText

```java
String
getText()
```

Returns the current value of the parse event as a string,
this returns the string value of a CHARACTERS event,
returns the value of a COMMENT, the replacement value
for an ENTITY_REFERENCE, the string value of a CDATA section,
the string value for a SPACE event,
or the String value of the internal subset of the DTD.
If an ENTITY_REFERENCE has been resolved, any character data
will be reported as CHARACTERS events.

**Returns:** the current text or null
**Throws:** IllegalStateException

- if this state is not
a valid text state.

- getTextCharacters

```java
char[] getTextCharacters()
```

Returns an array which contains the characters from this event.
This array should be treated as read-only and transient. I.e. the array will
contain the text characters until the XMLStreamReader moves on to the next event.
Attempts to hold onto the character array beyond that time or modify the
contents of the array are breaches of the contract for this interface.

**Returns:** the current text or an empty array
**Throws:** IllegalStateException

- if this state is not
a valid text state.

- getTextCharacters

```java
int getTextCharacters​(int sourceStart,
char[] target,
int targetStart,
int length)
throws
XMLStreamException
```

Gets the the text associated with a CHARACTERS, SPACE or CDATA event.
Text starting a "sourceStart" is copied into "target" starting at "targetStart".
Up to "length" characters are copied. The number of characters actually copied is returned.

The "sourceStart" argument must be greater or equal to 0 and less than or equal to
the number of characters associated with the event. Usually, one requests text starting at a "sourceStart" of 0.
If the number of characters actually copied is less than the "length", then there is no more text.
Otherwise, subsequent calls need to be made until all text has been retrieved. For example:

```java
int length = 1024;
char[] myBuffer = new char[ length ];

for ( int sourceStart = 0 ; ; sourceStart += length )
{
int nCopied = stream.getTextCharacters( sourceStart, myBuffer, 0, length );

if (nCopied < length)
break;
}
```

XMLStreamException may be thrown if there are any XML errors in the underlying source.
The "targetStart" argument must be greater than or equal to 0 and less than the length of "target",
Length must be greater than 0 and "targetStart + length" must be less than or equal to length of "target".

**Parameters:** sourceStart

- the index of the first character in the source array to copy
**Parameters:** target

- the destination array
**Parameters:** targetStart

- the start offset in the target array
**Parameters:** length

- the number of characters to copy
**Returns:** the number of characters actually copied
**Throws:** XMLStreamException

- if the underlying XML source is not well-formed
**Throws:** IndexOutOfBoundsException

- if targetStart < 0 or > than the length of target
**Throws:** IndexOutOfBoundsException

- if length < 0 or targetStart + length > length of target
**Throws:** UnsupportedOperationException

- if this method is not supported
**Throws:** NullPointerException

- is if target is null

- getTextStart

```java
int getTextStart()
```

Returns the offset into the text character array where the first
character (of this text event) is stored.

**Returns:** the starting position of the text in the character array
**Throws:** IllegalStateException

- if this state is not
a valid text state.

- getTextLength

```java
int getTextLength()
```

Returns the length of the sequence of characters for this
Text event within the text character array.

**Returns:** the length of the text
**Throws:** IllegalStateException

- if this state is not
a valid text state.

- getEncoding

```java
String
getEncoding()
```

Return input encoding if known or null if unknown.

**Returns:** the encoding of this instance or null

- hasText

```java
boolean hasText()
```

Return a boolean indicating whether the current event has text.
The following events have text:
CHARACTERS,DTD ,ENTITY_REFERENCE, COMMENT, SPACE

**Returns:** true if the event has text, false otherwise

- getLocation

```java
Location
getLocation()
```

Return the current location of the processor.
If the Location is unknown the processor should return
an implementation of Location that returns -1 for the
location and null for the publicId and systemId.
The location information is only valid until next() is
called.

**Returns:** the location of the cursor

- getName

```java
QName
getName()
```

Returns a QName for the current START_ELEMENT or END_ELEMENT event

**Returns:** the QName for the current START_ELEMENT or END_ELEMENT event
**Throws:** IllegalStateException

- if this is not a START_ELEMENT or
END_ELEMENT

- getLocalName

```java
String
getLocalName()
```

Returns the (local) name of the current event.
For START_ELEMENT or END_ELEMENT returns the (local) name of the current element.
For ENTITY_REFERENCE it returns entity name.
The current event must be START_ELEMENT or END_ELEMENT,
or ENTITY_REFERENCE

**Returns:** the localName
**Throws:** IllegalStateException

- if this not a START_ELEMENT,
END_ELEMENT or ENTITY_REFERENCE

- hasName

```java
boolean hasName()
```

returns a boolean indicating whether the current event has a name
(is a START_ELEMENT or END_ELEMENT).

**Returns:** true if the event has a name, false otherwise

- getNamespaceURI

```java
String
getNamespaceURI()
```

If the current event is a START_ELEMENT or END_ELEMENT this method
returns the URI of the prefix or the default namespace.
Returns null if the event does not have a prefix.

**Returns:** the URI bound to this elements prefix, the default namespace, or null

- getPrefix

```java
String
getPrefix()
```

Returns the prefix of the current event or null if the event does not have a prefix

**Returns:** the prefix or null

- getVersion

```java
String
getVersion()
```

Get the xml version declared on the xml declaration
Returns null if none was declared

**Returns:** the XML version or null

- isStandalone

```java
boolean isStandalone()
```

Get the standalone declaration from the xml declaration

**Returns:** true if this is standalone, or false otherwise

- standaloneSet

```java
boolean standaloneSet()
```

Checks if standalone was set in the document

**Returns:** true if standalone was set in the document, or false otherwise

- getCharacterEncodingScheme

```java
String
getCharacterEncodingScheme()
```

Returns the character encoding declared on the xml declaration
Returns null if none was declared

**Returns:** the encoding declared in the document or null

- getPITarget

```java
String
getPITarget()
```

Get the target of a processing instruction

**Returns:** the target or null

- getPIData

```java
String
getPIData()
```

Get the data section of a processing instruction

**Returns:** the data or null

---

#### Method Detail

getProperty

```java
Object
getProperty​(
String
name)
throws
IllegalArgumentException
```

Get the value of a feature/property from the underlying implementation

**Parameters:** name

- The name of the property, may not be null
**Returns:** The value of the property
**Throws:** IllegalArgumentException

- if name is null

---

#### getProperty

Object

getProperty​(

String

name)
throws

IllegalArgumentException

Get the value of a feature/property from the underlying implementation

next

```java
int next()
throws
XMLStreamException
```

Get next parsing event - a processor may return all contiguous
character data in a single chunk, or it may split it into several chunks.
If the property javax.xml.stream.isCoalescing is set to true
element content must be coalesced and only one CHARACTERS event
must be returned for contiguous element content or
CDATA Sections.

By default entity references must be
expanded and reported transparently to the application.
An exception will be thrown if an entity reference cannot be expanded.
If element content is empty (i.e. content is "") then no CHARACTERS event will be reported.

Given the following XML:

<foo><!--description-->content text<![CDATA[<greeting>Hello>/greeting>]]>other content>/foo>

The behavior of calling next() when being on foo will be:

1- the comment (COMMENT)

2- then the characters section (CHARACTERS)

3- then the CDATA section (another CHARACTERS)

4- then the next characters section (another CHARACTERS)

5- then the END_ELEMENT

NOTE:

empty element (such as

<tag/>

) will be reported
with two separate events: START_ELEMENT, END_ELEMENT - This preserves
parsing equivalency of empty element to

<tag></tag>

.

This method will throw an IllegalStateException if it is called after hasNext() returns false.

**Returns:** the integer code corresponding to the current parse event
**Throws:** NoSuchElementException

- if this is called when hasNext() returns false
**Throws:** XMLStreamException

- if there is an error processing the underlying XML source
**See Also:** XMLEvent

---

#### next

int next()
throws

XMLStreamException

Get next parsing event - a processor may return all contiguous
character data in a single chunk, or it may split it into several chunks.
If the property javax.xml.stream.isCoalescing is set to true
element content must be coalesced and only one CHARACTERS event
must be returned for contiguous element content or
CDATA Sections.

By default entity references must be
expanded and reported transparently to the application.
An exception will be thrown if an entity reference cannot be expanded.
If element content is empty (i.e. content is "") then no CHARACTERS event will be reported.

Given the following XML:

<foo><!--description-->content text<![CDATA[<greeting>Hello>/greeting>]]>other content>/foo>

The behavior of calling next() when being on foo will be:

1- the comment (COMMENT)

2- then the characters section (CHARACTERS)

3- then the CDATA section (another CHARACTERS)

4- then the next characters section (another CHARACTERS)

5- then the END_ELEMENT

NOTE:

empty element (such as

<tag/>

) will be reported
with two separate events: START_ELEMENT, END_ELEMENT - This preserves
parsing equivalency of empty element to

<tag></tag>

.

This method will throw an IllegalStateException if it is called after hasNext() returns false.

Given the following XML:

<foo><!--description-->content text<![CDATA[<greeting>Hello>/greeting>]]>other content>/foo>

The behavior of calling next() when being on foo will be:

1- the comment (COMMENT)

2- then the characters section (CHARACTERS)

3- then the CDATA section (another CHARACTERS)

4- then the next characters section (another CHARACTERS)

5- then the END_ELEMENT

NOTE:

empty element (such as

<tag/>

) will be reported
with two separate events: START_ELEMENT, END_ELEMENT - This preserves
parsing equivalency of empty element to

<tag></tag>

.

This method will throw an IllegalStateException if it is called after hasNext() returns false.

NOTE:

empty element (such as

<tag/>

) will be reported
with two separate events: START_ELEMENT, END_ELEMENT - This preserves
parsing equivalency of empty element to

<tag></tag>

.

This method will throw an IllegalStateException if it is called after hasNext() returns false.

require

```java
void require​(int type,

String
namespaceURI,

String
localName)
throws
XMLStreamException
```

Test if the current event is of the given type and if the namespace and name match the current
namespace and name of the current event. If the namespaceURI is null it is not checked for equality,
if the localName is null it is not checked for equality.

**Parameters:** type

- the event type
**Parameters:** namespaceURI

- the uri of the event, may be null
**Parameters:** localName

- the localName of the event, may be null
**Throws:** XMLStreamException

- if the required values are not matched.

---

#### require

void require​(int type,

String

namespaceURI,

String

localName)
throws

XMLStreamException

Test if the current event is of the given type and if the namespace and name match the current
namespace and name of the current event. If the namespaceURI is null it is not checked for equality,
if the localName is null it is not checked for equality.

getElementText

```java
String
getElementText()
throws
XMLStreamException
```

Reads the content of a text-only element, an exception is thrown if this is
not a text-only element.
Regardless of value of javax.xml.stream.isCoalescing this method always returns coalesced content.

Precondition: the current event is START_ELEMENT.

Postcondition: the current event is the corresponding END_ELEMENT.

The method does the following (implementations are free to optimized
but must do equivalent processing):

```java
if(getEventType() != XMLStreamConstants.START_ELEMENT) {
throw new XMLStreamException(
"parser must be on START_ELEMENT to read next text", getLocation());
}

int eventType = next();
StringBuffer content = new StringBuffer();
while(eventType != XMLStreamConstants.END_ELEMENT) {
if(eventType == XMLStreamConstants.CHARACTERS
|| eventType == XMLStreamConstants.CDATA
|| eventType == XMLStreamConstants.SPACE
|| eventType == XMLStreamConstants.ENTITY_REFERENCE) {
buf.append(getText());
} else if(eventType == XMLStreamConstants.PROCESSING_INSTRUCTION
|| eventType == XMLStreamConstants.COMMENT) {
// skipping
} else if(eventType == XMLStreamConstants.END_DOCUMENT) {
throw new XMLStreamException(
"unexpected end of document when reading element text content", this);
} else if(eventType == XMLStreamConstants.START_ELEMENT) {
throw new XMLStreamException(
"element text content may not contain START_ELEMENT", getLocation());
} else {
throw new XMLStreamException(
"Unexpected event type "+eventType, getLocation());
}
eventType = next();
}
return buf.toString();
```

**Throws:** XMLStreamException

- if the current event is not a START_ELEMENT
or if a non text element is encountered

---

#### getElementText

String

getElementText()
throws

XMLStreamException

Reads the content of a text-only element, an exception is thrown if this is
not a text-only element.
Regardless of value of javax.xml.stream.isCoalescing this method always returns coalesced content.

Precondition: the current event is START_ELEMENT.

Postcondition: the current event is the corresponding END_ELEMENT.

The method does the following (implementations are free to optimized
but must do equivalent processing):

```java
if(getEventType() != XMLStreamConstants.START_ELEMENT) {
throw new XMLStreamException(
"parser must be on START_ELEMENT to read next text", getLocation());
}

int eventType = next();
StringBuffer content = new StringBuffer();
while(eventType != XMLStreamConstants.END_ELEMENT) {
if(eventType == XMLStreamConstants.CHARACTERS
|| eventType == XMLStreamConstants.CDATA
|| eventType == XMLStreamConstants.SPACE
|| eventType == XMLStreamConstants.ENTITY_REFERENCE) {
buf.append(getText());
} else if(eventType == XMLStreamConstants.PROCESSING_INSTRUCTION
|| eventType == XMLStreamConstants.COMMENT) {
// skipping
} else if(eventType == XMLStreamConstants.END_DOCUMENT) {
throw new XMLStreamException(
"unexpected end of document when reading element text content", this);
} else if(eventType == XMLStreamConstants.START_ELEMENT) {
throw new XMLStreamException(
"element text content may not contain START_ELEMENT", getLocation());
} else {
throw new XMLStreamException(
"Unexpected event type "+eventType, getLocation());
}
eventType = next();
}
return buf.toString();
```

if(getEventType() != XMLStreamConstants.START_ELEMENT) {
throw new XMLStreamException(
"parser must be on START_ELEMENT to read next text", getLocation());
}

int eventType = next();
StringBuffer content = new StringBuffer();
while(eventType != XMLStreamConstants.END_ELEMENT) {
if(eventType == XMLStreamConstants.CHARACTERS
|| eventType == XMLStreamConstants.CDATA
|| eventType == XMLStreamConstants.SPACE
|| eventType == XMLStreamConstants.ENTITY_REFERENCE) {
buf.append(getText());
} else if(eventType == XMLStreamConstants.PROCESSING_INSTRUCTION
|| eventType == XMLStreamConstants.COMMENT) {
// skipping
} else if(eventType == XMLStreamConstants.END_DOCUMENT) {
throw new XMLStreamException(
"unexpected end of document when reading element text content", this);
} else if(eventType == XMLStreamConstants.START_ELEMENT) {
throw new XMLStreamException(
"element text content may not contain START_ELEMENT", getLocation());
} else {
throw new XMLStreamException(
"Unexpected event type "+eventType, getLocation());
}
eventType = next();
}
return buf.toString();

nextTag

```java
int nextTag()
throws
XMLStreamException
```

Skips any white space (isWhiteSpace() returns true), COMMENT,
or PROCESSING_INSTRUCTION,
until a START_ELEMENT or END_ELEMENT is reached.
If other than white space characters, COMMENT, PROCESSING_INSTRUCTION, START_ELEMENT, END_ELEMENT
are encountered, an exception is thrown. This method should
be used when processing element-only content seperated by white space.

Precondition: none

Postcondition: the current event is START_ELEMENT or END_ELEMENT
and cursor may have moved over any whitespace event.

Essentially it does the following (implementations are free to optimized
but must do equivalent processing):

```java
int eventType = next();
while((eventType == XMLStreamConstants.CHARACTERS && isWhiteSpace()) // skip whitespace
|| (eventType == XMLStreamConstants.CDATA && isWhiteSpace())
// skip whitespace
|| eventType == XMLStreamConstants.SPACE
|| eventType == XMLStreamConstants.PROCESSING_INSTRUCTION
|| eventType == XMLStreamConstants.COMMENT
) {
eventType = next();
}
if (eventType != XMLStreamConstants.START_ELEMENT && eventType != XMLStreamConstants.END_ELEMENT) {
throw new String XMLStreamException("expected start or end tag", getLocation());
}
return eventType;
```

**Returns:** the event type of the element read (START_ELEMENT or END_ELEMENT)
**Throws:** XMLStreamException

- if the current event is not white space, PROCESSING_INSTRUCTION,
START_ELEMENT or END_ELEMENT
**Throws:** NoSuchElementException

- if this is called when hasNext() returns false

---

#### nextTag

int nextTag()
throws

XMLStreamException

Skips any white space (isWhiteSpace() returns true), COMMENT,
or PROCESSING_INSTRUCTION,
until a START_ELEMENT or END_ELEMENT is reached.
If other than white space characters, COMMENT, PROCESSING_INSTRUCTION, START_ELEMENT, END_ELEMENT
are encountered, an exception is thrown. This method should
be used when processing element-only content seperated by white space.

Precondition: none

Postcondition: the current event is START_ELEMENT or END_ELEMENT
and cursor may have moved over any whitespace event.

Essentially it does the following (implementations are free to optimized
but must do equivalent processing):

```java
int eventType = next();
while((eventType == XMLStreamConstants.CHARACTERS && isWhiteSpace()) // skip whitespace
|| (eventType == XMLStreamConstants.CDATA && isWhiteSpace())
// skip whitespace
|| eventType == XMLStreamConstants.SPACE
|| eventType == XMLStreamConstants.PROCESSING_INSTRUCTION
|| eventType == XMLStreamConstants.COMMENT
) {
eventType = next();
}
if (eventType != XMLStreamConstants.START_ELEMENT && eventType != XMLStreamConstants.END_ELEMENT) {
throw new String XMLStreamException("expected start or end tag", getLocation());
}
return eventType;
```

int eventType = next();
while((eventType == XMLStreamConstants.CHARACTERS && isWhiteSpace()) // skip whitespace
|| (eventType == XMLStreamConstants.CDATA && isWhiteSpace())
// skip whitespace
|| eventType == XMLStreamConstants.SPACE
|| eventType == XMLStreamConstants.PROCESSING_INSTRUCTION
|| eventType == XMLStreamConstants.COMMENT
) {
eventType = next();
}
if (eventType != XMLStreamConstants.START_ELEMENT && eventType != XMLStreamConstants.END_ELEMENT) {
throw new String XMLStreamException("expected start or end tag", getLocation());
}
return eventType;

hasNext

```java
boolean hasNext()
throws
XMLStreamException
```

Returns true if there are more parsing events and false
if there are no more events. This method will return
false if the current state of the XMLStreamReader is
END_DOCUMENT

**Returns:** true if there are more events, false otherwise
**Throws:** XMLStreamException

- if there is a fatal error detecting the next state

---

#### hasNext

boolean hasNext()
throws

XMLStreamException

Returns true if there are more parsing events and false
if there are no more events. This method will return
false if the current state of the XMLStreamReader is
END_DOCUMENT

close

```java
void close()
throws
XMLStreamException
```

Frees any resources associated with this Reader. This method does not close the
underlying input source.

**Throws:** XMLStreamException

- if there are errors freeing associated resources

---

#### close

void close()
throws

XMLStreamException

Frees any resources associated with this Reader. This method does not close the
underlying input source.

getNamespaceURI

```java
String
getNamespaceURI​(
String
prefix)
```

Return the uri for the given prefix.
The uri returned depends on the current state of the processor.

NOTE:

The 'xml' prefix is bound as defined in

Namespaces in XML

specification to "http://www.w3.org/XML/1998/namespace".

NOTE:

The 'xmlns' prefix must be resolved to following namespace

http://www.w3.org/2000/xmlns/

**Parameters:** prefix

- The prefix to lookup, may not be null
**Returns:** the uri bound to the given prefix or null if it is not bound
**Throws:** IllegalArgumentException

- if the prefix is null

---

#### getNamespaceURI

String

getNamespaceURI​(

String

prefix)

Return the uri for the given prefix.
The uri returned depends on the current state of the processor.

NOTE:

The 'xml' prefix is bound as defined in

Namespaces in XML

specification to "http://www.w3.org/XML/1998/namespace".

NOTE:

The 'xmlns' prefix must be resolved to following namespace

http://www.w3.org/2000/xmlns/

NOTE:

The 'xml' prefix is bound as defined in

Namespaces in XML

specification to "http://www.w3.org/XML/1998/namespace".

NOTE:

The 'xmlns' prefix must be resolved to following namespace

http://www.w3.org/2000/xmlns/

NOTE:

The 'xmlns' prefix must be resolved to following namespace

http://www.w3.org/2000/xmlns/

isStartElement

```java
boolean isStartElement()
```

Returns true if the cursor points to a start tag (otherwise false)

**Returns:** true if the cursor points to a start tag, false otherwise

---

#### isStartElement

boolean isStartElement()

Returns true if the cursor points to a start tag (otherwise false)

isEndElement

```java
boolean isEndElement()
```

Returns true if the cursor points to an end tag (otherwise false)

**Returns:** true if the cursor points to an end tag, false otherwise

---

#### isEndElement

boolean isEndElement()

Returns true if the cursor points to an end tag (otherwise false)

isCharacters

```java
boolean isCharacters()
```

Returns true if the cursor points to a character data event

**Returns:** true if the cursor points to character data, false otherwise

---

#### isCharacters

boolean isCharacters()

Returns true if the cursor points to a character data event

isWhiteSpace

```java
boolean isWhiteSpace()
```

Returns true if the cursor points to a character data event
that consists of all whitespace

**Returns:** true if the cursor points to all whitespace, false otherwise

---

#### isWhiteSpace

boolean isWhiteSpace()

Returns true if the cursor points to a character data event
that consists of all whitespace

getAttributeValue

```java
String
getAttributeValue​(
String
namespaceURI,

String
localName)
```

Returns the normalized attribute value of the
attribute with the namespace and localName
If the namespaceURI is null the namespace
is not checked for equality

**Parameters:** namespaceURI

- the namespace of the attribute
**Parameters:** localName

- the local name of the attribute, cannot be null
**Returns:** returns the value of the attribute , returns null if not found
**Throws:** IllegalStateException

- if this is not a START_ELEMENT or ATTRIBUTE

---

#### getAttributeValue

String

getAttributeValue​(

String

namespaceURI,

String

localName)

Returns the normalized attribute value of the
attribute with the namespace and localName
If the namespaceURI is null the namespace
is not checked for equality

getAttributeCount

```java
int getAttributeCount()
```

Returns the count of attributes on this START_ELEMENT,
this method is only valid on a START_ELEMENT or ATTRIBUTE. This
count excludes namespace definitions. Attribute indices are
zero-based.

**Returns:** returns the number of attributes
**Throws:** IllegalStateException

- if this is not a START_ELEMENT or ATTRIBUTE

---

#### getAttributeCount

int getAttributeCount()

Returns the count of attributes on this START_ELEMENT,
this method is only valid on a START_ELEMENT or ATTRIBUTE. This
count excludes namespace definitions. Attribute indices are
zero-based.

getAttributeName

```java
QName
getAttributeName​(int index)
```

Returns the qname of the attribute at the provided index

**Parameters:** index

- the position of the attribute
**Returns:** the QName of the attribute
**Throws:** IllegalStateException

- if this is not a START_ELEMENT or ATTRIBUTE

---

#### getAttributeName

QName

getAttributeName​(int index)

Returns the qname of the attribute at the provided index

getAttributeNamespace

```java
String
getAttributeNamespace​(int index)
```

Returns the namespace of the attribute at the provided
index

**Parameters:** index

- the position of the attribute
**Returns:** the namespace URI (can be null)
**Throws:** IllegalStateException

- if this is not a START_ELEMENT or ATTRIBUTE

---

#### getAttributeNamespace

String

getAttributeNamespace​(int index)

Returns the namespace of the attribute at the provided
index

getAttributeLocalName

```java
String
getAttributeLocalName​(int index)
```

Returns the localName of the attribute at the provided
index

**Parameters:** index

- the position of the attribute
**Returns:** the localName of the attribute
**Throws:** IllegalStateException

- if this is not a START_ELEMENT or ATTRIBUTE

---

#### getAttributeLocalName

String

getAttributeLocalName​(int index)

Returns the localName of the attribute at the provided
index

getAttributePrefix

```java
String
getAttributePrefix​(int index)
```

Returns the prefix of this attribute at the
provided index

**Parameters:** index

- the position of the attribute
**Returns:** the prefix of the attribute
**Throws:** IllegalStateException

- if this is not a START_ELEMENT or ATTRIBUTE

---

#### getAttributePrefix

String

getAttributePrefix​(int index)

Returns the prefix of this attribute at the
provided index

getAttributeType

```java
String
getAttributeType​(int index)
```

Returns the XML type of the attribute at the provided
index

**Parameters:** index

- the position of the attribute
**Returns:** the XML type of the attribute
**Throws:** IllegalStateException

- if this is not a START_ELEMENT or ATTRIBUTE

---

#### getAttributeType

String

getAttributeType​(int index)

Returns the XML type of the attribute at the provided
index

getAttributeValue

```java
String
getAttributeValue​(int index)
```

Returns the value of the attribute at the
index

**Parameters:** index

- the position of the attribute
**Returns:** the attribute value
**Throws:** IllegalStateException

- if this is not a START_ELEMENT or ATTRIBUTE

---

#### getAttributeValue

String

getAttributeValue​(int index)

Returns the value of the attribute at the
index

isAttributeSpecified

```java
boolean isAttributeSpecified​(int index)
```

Returns a boolean which indicates if this
attribute was created by default

**Parameters:** index

- the position of the attribute
**Returns:** true if this is a default attribute
**Throws:** IllegalStateException

- if this is not a START_ELEMENT or ATTRIBUTE

---

#### isAttributeSpecified

boolean isAttributeSpecified​(int index)

Returns a boolean which indicates if this
attribute was created by default

getNamespaceCount

```java
int getNamespaceCount()
```

Returns the count of namespaces declared on this START_ELEMENT or END_ELEMENT,
this method is only valid on a START_ELEMENT, END_ELEMENT or NAMESPACE. On
an END_ELEMENT the count is of the namespaces that are about to go
out of scope. This is the equivalent of the information reported
by SAX callback for an end element event.

**Returns:** returns the number of namespace declarations on this specific element
**Throws:** IllegalStateException

- if this is not a START_ELEMENT, END_ELEMENT or NAMESPACE

---

#### getNamespaceCount

int getNamespaceCount()

Returns the count of namespaces declared on this START_ELEMENT or END_ELEMENT,
this method is only valid on a START_ELEMENT, END_ELEMENT or NAMESPACE. On
an END_ELEMENT the count is of the namespaces that are about to go
out of scope. This is the equivalent of the information reported
by SAX callback for an end element event.

getNamespacePrefix

```java
String
getNamespacePrefix​(int index)
```

Returns the prefix for the namespace declared at the
index. Returns null if this is the default namespace
declaration

**Parameters:** index

- the position of the namespace declaration
**Returns:** returns the namespace prefix
**Throws:** IllegalStateException

- if this is not a START_ELEMENT, END_ELEMENT or NAMESPACE

---

#### getNamespacePrefix

String

getNamespacePrefix​(int index)

Returns the prefix for the namespace declared at the
index. Returns null if this is the default namespace
declaration

getNamespaceURI

```java
String
getNamespaceURI​(int index)
```

Returns the uri for the namespace declared at the
index.

**Parameters:** index

- the position of the namespace declaration
**Returns:** returns the namespace uri
**Throws:** IllegalStateException

- if this is not a START_ELEMENT, END_ELEMENT or NAMESPACE

---

#### getNamespaceURI

String

getNamespaceURI​(int index)

Returns the uri for the namespace declared at the
index.

getNamespaceContext

```java
NamespaceContext
getNamespaceContext()
```

Returns a read only namespace context for the current
position. The context is transient and only valid until
a call to next() changes the state of the reader.

**Returns:** return a namespace context

---

#### getNamespaceContext

NamespaceContext

getNamespaceContext()

Returns a read only namespace context for the current
position. The context is transient and only valid until
a call to next() changes the state of the reader.

getEventType

```java
int getEventType()
```

Returns an integer code that indicates the type of the event the cursor is
pointing to. The initial event type is

XMLStreamConstants.START_DOCUMENT

.

**Returns:** the type of the current event

---

#### getEventType

int getEventType()

Returns an integer code that indicates the type of the event the cursor is
pointing to. The initial event type is

XMLStreamConstants.START_DOCUMENT

.

getText

```java
String
getText()
```

Returns the current value of the parse event as a string,
this returns the string value of a CHARACTERS event,
returns the value of a COMMENT, the replacement value
for an ENTITY_REFERENCE, the string value of a CDATA section,
the string value for a SPACE event,
or the String value of the internal subset of the DTD.
If an ENTITY_REFERENCE has been resolved, any character data
will be reported as CHARACTERS events.

**Returns:** the current text or null
**Throws:** IllegalStateException

- if this state is not
a valid text state.

---

#### getText

String

getText()

Returns the current value of the parse event as a string,
this returns the string value of a CHARACTERS event,
returns the value of a COMMENT, the replacement value
for an ENTITY_REFERENCE, the string value of a CDATA section,
the string value for a SPACE event,
or the String value of the internal subset of the DTD.
If an ENTITY_REFERENCE has been resolved, any character data
will be reported as CHARACTERS events.

getTextCharacters

```java
char[] getTextCharacters()
```

Returns an array which contains the characters from this event.
This array should be treated as read-only and transient. I.e. the array will
contain the text characters until the XMLStreamReader moves on to the next event.
Attempts to hold onto the character array beyond that time or modify the
contents of the array are breaches of the contract for this interface.

**Returns:** the current text or an empty array
**Throws:** IllegalStateException

- if this state is not
a valid text state.

---

#### getTextCharacters

char[] getTextCharacters()

Returns an array which contains the characters from this event.
This array should be treated as read-only and transient. I.e. the array will
contain the text characters until the XMLStreamReader moves on to the next event.
Attempts to hold onto the character array beyond that time or modify the
contents of the array are breaches of the contract for this interface.

getTextCharacters

```java
int getTextCharacters​(int sourceStart,
char[] target,
int targetStart,
int length)
throws
XMLStreamException
```

Gets the the text associated with a CHARACTERS, SPACE or CDATA event.
Text starting a "sourceStart" is copied into "target" starting at "targetStart".
Up to "length" characters are copied. The number of characters actually copied is returned.

The "sourceStart" argument must be greater or equal to 0 and less than or equal to
the number of characters associated with the event. Usually, one requests text starting at a "sourceStart" of 0.
If the number of characters actually copied is less than the "length", then there is no more text.
Otherwise, subsequent calls need to be made until all text has been retrieved. For example:

```java
int length = 1024;
char[] myBuffer = new char[ length ];

for ( int sourceStart = 0 ; ; sourceStart += length )
{
int nCopied = stream.getTextCharacters( sourceStart, myBuffer, 0, length );

if (nCopied < length)
break;
}
```

XMLStreamException may be thrown if there are any XML errors in the underlying source.
The "targetStart" argument must be greater than or equal to 0 and less than the length of "target",
Length must be greater than 0 and "targetStart + length" must be less than or equal to length of "target".

**Parameters:** sourceStart

- the index of the first character in the source array to copy
**Parameters:** target

- the destination array
**Parameters:** targetStart

- the start offset in the target array
**Parameters:** length

- the number of characters to copy
**Returns:** the number of characters actually copied
**Throws:** XMLStreamException

- if the underlying XML source is not well-formed
**Throws:** IndexOutOfBoundsException

- if targetStart < 0 or > than the length of target
**Throws:** IndexOutOfBoundsException

- if length < 0 or targetStart + length > length of target
**Throws:** UnsupportedOperationException

- if this method is not supported
**Throws:** NullPointerException

- is if target is null

---

#### getTextCharacters

int getTextCharacters​(int sourceStart,
char[] target,
int targetStart,
int length)
throws

XMLStreamException

Gets the the text associated with a CHARACTERS, SPACE or CDATA event.
Text starting a "sourceStart" is copied into "target" starting at "targetStart".
Up to "length" characters are copied. The number of characters actually copied is returned.

The "sourceStart" argument must be greater or equal to 0 and less than or equal to
the number of characters associated with the event. Usually, one requests text starting at a "sourceStart" of 0.
If the number of characters actually copied is less than the "length", then there is no more text.
Otherwise, subsequent calls need to be made until all text has been retrieved. For example:

```java
int length = 1024;
char[] myBuffer = new char[ length ];

for ( int sourceStart = 0 ; ; sourceStart += length )
{
int nCopied = stream.getTextCharacters( sourceStart, myBuffer, 0, length );

if (nCopied < length)
break;
}
```

XMLStreamException may be thrown if there are any XML errors in the underlying source.
The "targetStart" argument must be greater than or equal to 0 and less than the length of "target",
Length must be greater than 0 and "targetStart + length" must be less than or equal to length of "target".

int length = 1024;
char[] myBuffer = new char[ length ];

for ( int sourceStart = 0 ; ; sourceStart += length )
{
int nCopied = stream.getTextCharacters( sourceStart, myBuffer, 0, length );

if (nCopied < length)
break;
}

getTextStart

```java
int getTextStart()
```

Returns the offset into the text character array where the first
character (of this text event) is stored.

**Returns:** the starting position of the text in the character array
**Throws:** IllegalStateException

- if this state is not
a valid text state.

---

#### getTextStart

int getTextStart()

Returns the offset into the text character array where the first
character (of this text event) is stored.

getTextLength

```java
int getTextLength()
```

Returns the length of the sequence of characters for this
Text event within the text character array.

**Returns:** the length of the text
**Throws:** IllegalStateException

- if this state is not
a valid text state.

---

#### getTextLength

int getTextLength()

Returns the length of the sequence of characters for this
Text event within the text character array.

getEncoding

```java
String
getEncoding()
```

Return input encoding if known or null if unknown.

**Returns:** the encoding of this instance or null

---

#### getEncoding

String

getEncoding()

Return input encoding if known or null if unknown.

hasText

```java
boolean hasText()
```

Return a boolean indicating whether the current event has text.
The following events have text:
CHARACTERS,DTD ,ENTITY_REFERENCE, COMMENT, SPACE

**Returns:** true if the event has text, false otherwise

---

#### hasText

boolean hasText()

Return a boolean indicating whether the current event has text.
The following events have text:
CHARACTERS,DTD ,ENTITY_REFERENCE, COMMENT, SPACE

getLocation

```java
Location
getLocation()
```

Return the current location of the processor.
If the Location is unknown the processor should return
an implementation of Location that returns -1 for the
location and null for the publicId and systemId.
The location information is only valid until next() is
called.

**Returns:** the location of the cursor

---

#### getLocation

Location

getLocation()

Return the current location of the processor.
If the Location is unknown the processor should return
an implementation of Location that returns -1 for the
location and null for the publicId and systemId.
The location information is only valid until next() is
called.

getName

```java
QName
getName()
```

Returns a QName for the current START_ELEMENT or END_ELEMENT event

**Returns:** the QName for the current START_ELEMENT or END_ELEMENT event
**Throws:** IllegalStateException

- if this is not a START_ELEMENT or
END_ELEMENT

---

#### getName

QName

getName()

Returns a QName for the current START_ELEMENT or END_ELEMENT event

getLocalName

```java
String
getLocalName()
```

Returns the (local) name of the current event.
For START_ELEMENT or END_ELEMENT returns the (local) name of the current element.
For ENTITY_REFERENCE it returns entity name.
The current event must be START_ELEMENT or END_ELEMENT,
or ENTITY_REFERENCE

**Returns:** the localName
**Throws:** IllegalStateException

- if this not a START_ELEMENT,
END_ELEMENT or ENTITY_REFERENCE

---

#### getLocalName

String

getLocalName()

Returns the (local) name of the current event.
For START_ELEMENT or END_ELEMENT returns the (local) name of the current element.
For ENTITY_REFERENCE it returns entity name.
The current event must be START_ELEMENT or END_ELEMENT,
or ENTITY_REFERENCE

hasName

```java
boolean hasName()
```

returns a boolean indicating whether the current event has a name
(is a START_ELEMENT or END_ELEMENT).

**Returns:** true if the event has a name, false otherwise

---

#### hasName

boolean hasName()

returns a boolean indicating whether the current event has a name
(is a START_ELEMENT or END_ELEMENT).

getNamespaceURI

```java
String
getNamespaceURI()
```

If the current event is a START_ELEMENT or END_ELEMENT this method
returns the URI of the prefix or the default namespace.
Returns null if the event does not have a prefix.

**Returns:** the URI bound to this elements prefix, the default namespace, or null

---

#### getNamespaceURI

String

getNamespaceURI()

If the current event is a START_ELEMENT or END_ELEMENT this method
returns the URI of the prefix or the default namespace.
Returns null if the event does not have a prefix.

getPrefix

```java
String
getPrefix()
```

Returns the prefix of the current event or null if the event does not have a prefix

**Returns:** the prefix or null

---

#### getPrefix

String

getPrefix()

Returns the prefix of the current event or null if the event does not have a prefix

getVersion

```java
String
getVersion()
```

Get the xml version declared on the xml declaration
Returns null if none was declared

**Returns:** the XML version or null

---

#### getVersion

String

getVersion()

Get the xml version declared on the xml declaration
Returns null if none was declared

isStandalone

```java
boolean isStandalone()
```

Get the standalone declaration from the xml declaration

**Returns:** true if this is standalone, or false otherwise

---

#### isStandalone

boolean isStandalone()

Get the standalone declaration from the xml declaration

standaloneSet

```java
boolean standaloneSet()
```

Checks if standalone was set in the document

**Returns:** true if standalone was set in the document, or false otherwise

---

#### standaloneSet

boolean standaloneSet()

Checks if standalone was set in the document

getCharacterEncodingScheme

```java
String
getCharacterEncodingScheme()
```

Returns the character encoding declared on the xml declaration
Returns null if none was declared

**Returns:** the encoding declared in the document or null

---

#### getCharacterEncodingScheme

String

getCharacterEncodingScheme()

Returns the character encoding declared on the xml declaration
Returns null if none was declared

getPITarget

```java
String
getPITarget()
```

Get the target of a processing instruction

**Returns:** the target or null

---

#### getPITarget

String

getPITarget()

Get the target of a processing instruction

getPIData

```java
String
getPIData()
```

Get the data section of a processing instruction

**Returns:** the data or null

---

#### getPIData

String

getPIData()

Get the data section of a processing instruction

---

