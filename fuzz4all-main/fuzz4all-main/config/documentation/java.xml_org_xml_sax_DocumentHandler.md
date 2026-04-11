# Interface DocumentHandler

**Source:** `java.xml\org\xml\sax\DocumentHandler.html`

### Class Description

```java
@Deprecated
(
since
="1.5")
public interface
DocumentHandler
```

Receive notification of general document events.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

This was the main event-handling interface for SAX1; in
SAX2, it has been replaced by

ContentHandler

, which provides Namespace support and reporting
of skipped entities. This interface is included in SAX2 only
to support legacy SAX1 applications.

The order of events in this interface is very important, and
mirrors the order of information in the document itself. For
example, all of an element's content (character data, processing
instructions, and/or subelements) will appear, in order, between
the startElement event and the corresponding endElement event.

Application writers who do not want to implement the entire
interface can derive a class from HandlerBase, which implements
the default functionality; parser writers can instantiate
HandlerBase to obtain a default handler. The application can find
the location of any document event using the Locator interface
supplied by the Parser through the setDocumentLocator method.

**All Known Implementing Classes:** HandlerBase

,

ParserAdapter

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void setDocumentLocator​(
Locator
locator)

Receive an object for locating the origin of SAX document events.

SAX parsers are strongly encouraged (though not absolutely
required) to supply a locator: if it does so, it must supply
the locator to the application by invoking this method before
invoking any of the other methods in the DocumentHandler
interface.

The locator allows the application to determine the end
position of any document-related event, even if the parser is
not reporting an error. Typically, the application will
use this information for reporting its own errors (such as
character content that does not match an application's
business rules). The information returned by the locator
is probably not sufficient for use with a search engine.

Note that the locator will return correct information only
during the invocation of the events in this interface. The
application should not attempt to use it at any other time.

**Parameters:**
- locator

- An object that can return the location of
any SAX document event.

**See Also:**
- Locator

---

#### void startDocument()
throws
SAXException

Receive notification of the beginning of a document.

The SAX parser will invoke this method only once, before any
other methods in this interface or in DTDHandler (except for
setDocumentLocator).

**Throws:**
- SAXException

- Any SAX exception, possibly
wrapping another exception.

---

#### void endDocument()
throws
SAXException

Receive notification of the end of a document.

The SAX parser will invoke this method only once, and it will
be the last method invoked during the parse. The parser shall
not invoke this method until it has either abandoned parsing
(because of an unrecoverable error) or reached the end of
input.

**Throws:**
- SAXException

- Any SAX exception, possibly
wrapping another exception.

---

#### void startElement​(
String
name,

AttributeList
atts)
throws
SAXException

Receive notification of the beginning of an element.

The Parser will invoke this method at the beginning of every
element in the XML document; there will be a corresponding
endElement() event for every startElement() event (even when the
element is empty). All of the element's content will be
reported, in order, before the corresponding endElement()
event.

If the element name has a namespace prefix, the prefix will
still be attached. Note that the attribute list provided will
contain only attributes with explicit values (specified or
defaulted): #IMPLIED attributes will be omitted.

**Parameters:**
- name

- The element type name.
- atts

- The attributes attached to the element, if any.

**Throws:**
- SAXException

- Any SAX exception, possibly
wrapping another exception.

**See Also:**
- endElement(java.lang.String)

,

AttributeList

---

#### void endElement​(
String
name)
throws
SAXException

Receive notification of the end of an element.

The SAX parser will invoke this method at the end of every
element in the XML document; there will be a corresponding
startElement() event for every endElement() event (even when the
element is empty).

If the element name has a namespace prefix, the prefix will
still be attached to the name.

**Parameters:**
- name

- The element type name

**Throws:**
- SAXException

- Any SAX exception, possibly
wrapping another exception.

---

#### void characters​(char[] ch,
int start,
int length)
throws
SAXException

Receive notification of character data.

The Parser will call this method to report each chunk of
character data. SAX parsers may return all contiguous character
data in a single chunk, or they may split it into several
chunks; however, all of the characters in any single event
must come from the same external entity, so that the Locator
provides useful information.

The application must not attempt to read from the array
outside of the specified range.

Note that some parsers will report whitespace using the
ignorableWhitespace() method rather than this one (validating
parsers must do so).

**Parameters:**
- ch

- The characters from the XML document.
- start

- The start position in the array.
- length

- The number of characters to read from the array.

**Throws:**
- SAXException

- Any SAX exception, possibly
wrapping another exception.

**See Also:**
- ignorableWhitespace(char[], int, int)

,

Locator

---

#### void ignorableWhitespace​(char[] ch,
int start,
int length)
throws
SAXException

Receive notification of ignorable whitespace in element content.

Validating Parsers must use this method to report each chunk
of ignorable whitespace (see the W3C XML 1.0 recommendation,
section 2.10): non-validating parsers may also use this method
if they are capable of parsing and using content models.

SAX parsers may return all contiguous whitespace in a single
chunk, or they may split it into several chunks; however, all of
the characters in any single event must come from the same
external entity, so that the Locator provides useful
information.

The application must not attempt to read from the array
outside of the specified range.

**Parameters:**
- ch

- The characters from the XML document.
- start

- The start position in the array.
- length

- The number of characters to read from the array.

**Throws:**
- SAXException

- Any SAX exception, possibly
wrapping another exception.

**See Also:**
- characters(char[], int, int)

---

#### void processingInstruction​(
String
target,

String
data)
throws
SAXException

Receive notification of a processing instruction.

The Parser will invoke this method once for each processing
instruction found: note that processing instructions may occur
before or after the main document element.

A SAX parser should never report an XML declaration (XML 1.0,
section 2.8) or a text declaration (XML 1.0, section 4.3.1)
using this method.

**Parameters:**
- target

- The processing instruction target.
- data

- The processing instruction data, or null if
none was supplied.

**Throws:**
- SAXException

- Any SAX exception, possibly
wrapping another exception.

---

### Additional Sections

#### Interface DocumentHandler

**All Known Implementing Classes:** HandlerBase

,

ParserAdapter

```java
@Deprecated
(
since
="1.5")
public interface
DocumentHandler
```

Deprecated.

This interface has been replaced by the SAX2

ContentHandler

interface, which includes Namespace support.

Receive notification of general document events.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

This was the main event-handling interface for SAX1; in
SAX2, it has been replaced by

ContentHandler

, which provides Namespace support and reporting
of skipped entities. This interface is included in SAX2 only
to support legacy SAX1 applications.

The order of events in this interface is very important, and
mirrors the order of information in the document itself. For
example, all of an element's content (character data, processing
instructions, and/or subelements) will appear, in order, between
the startElement event and the corresponding endElement event.

Application writers who do not want to implement the entire
interface can derive a class from HandlerBase, which implements
the default functionality; parser writers can instantiate
HandlerBase to obtain a default handler. The application can find
the location of any document event using the Locator interface
supplied by the Parser through the setDocumentLocator method.

**Since:** 1.4, SAX 1.0
**See Also:** Parser.setDocumentHandler(org.xml.sax.DocumentHandler)

,

Locator

,

HandlerBase

@Deprecated

(

since

="1.5")
public interface

DocumentHandler

Receive notification of general document events.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

This was the main event-handling interface for SAX1; in
SAX2, it has been replaced by

ContentHandler

, which provides Namespace support and reporting
of skipped entities. This interface is included in SAX2 only
to support legacy SAX1 applications.

The order of events in this interface is very important, and
mirrors the order of information in the document itself. For
example, all of an element's content (character data, processing
instructions, and/or subelements) will appear, in order, between
the startElement event and the corresponding endElement event.

Application writers who do not want to implement the entire
interface can derive a class from HandlerBase, which implements
the default functionality; parser writers can instantiate
HandlerBase to obtain a default handler. The application can find
the location of any document event using the Locator interface
supplied by the Parser through the setDocumentLocator method.

This was the main event-handling interface for SAX1; in
SAX2, it has been replaced by

ContentHandler

, which provides Namespace support and reporting
of skipped entities. This interface is included in SAX2 only
to support legacy SAX1 applications.

The order of events in this interface is very important, and
mirrors the order of information in the document itself. For
example, all of an element's content (character data, processing
instructions, and/or subelements) will appear, in order, between
the startElement event and the corresponding endElement event.

Application writers who do not want to implement the entire
interface can derive a class from HandlerBase, which implements
the default functionality; parser writers can instantiate
HandlerBase to obtain a default handler. The application can find
the location of any document event using the Locator interface
supplied by the Parser through the setDocumentLocator method.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

void

characters

​(char[] ch,
int start,
int length)

Deprecated.

Receive notification of character data.

void

endDocument

()

Deprecated.

Receive notification of the end of a document.

void

endElement

​(

String

name)

Deprecated.

Receive notification of the end of an element.

void

ignorableWhitespace

​(char[] ch,
int start,
int length)

Deprecated.

Receive notification of ignorable whitespace in element content.

void

processingInstruction

​(

String

target,

String

data)

Deprecated.

Receive notification of a processing instruction.

void

setDocumentLocator

​(

Locator

locator)

Deprecated.

Receive an object for locating the origin of SAX document events.

void

startDocument

()

Deprecated.

Receive notification of the beginning of a document.

void

startElement

​(

String

name,

AttributeList

atts)

Deprecated.

Receive notification of the beginning of an element.

Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

void

characters

​(char[] ch,
int start,
int length)

Deprecated.

Receive notification of character data.

void

endDocument

()

Deprecated.

Receive notification of the end of a document.

void

endElement

​(

String

name)

Deprecated.

Receive notification of the end of an element.

void

ignorableWhitespace

​(char[] ch,
int start,
int length)

Deprecated.

Receive notification of ignorable whitespace in element content.

void

processingInstruction

​(

String

target,

String

data)

Deprecated.

Receive notification of a processing instruction.

void

setDocumentLocator

​(

Locator

locator)

Deprecated.

Receive an object for locating the origin of SAX document events.

void

startDocument

()

Deprecated.

Receive notification of the beginning of a document.

void

startElement

​(

String

name,

AttributeList

atts)

Deprecated.

Receive notification of the beginning of an element.

---

#### Method Summary

Deprecated.

Receive notification of character data.

Receive notification of the end of a document.

Receive notification of the end of an element.

Receive notification of ignorable whitespace in element content.

Receive notification of a processing instruction.

Receive an object for locating the origin of SAX document events.

Receive notification of the beginning of a document.

Receive notification of the beginning of an element.

============ METHOD DETAIL ==========

- Method Detail

- setDocumentLocator

```java
void setDocumentLocator​(
Locator
locator)
```

Deprecated.

Receive an object for locating the origin of SAX document events.

SAX parsers are strongly encouraged (though not absolutely
required) to supply a locator: if it does so, it must supply
the locator to the application by invoking this method before
invoking any of the other methods in the DocumentHandler
interface.

The locator allows the application to determine the end
position of any document-related event, even if the parser is
not reporting an error. Typically, the application will
use this information for reporting its own errors (such as
character content that does not match an application's
business rules). The information returned by the locator
is probably not sufficient for use with a search engine.

Note that the locator will return correct information only
during the invocation of the events in this interface. The
application should not attempt to use it at any other time.

**Parameters:** locator

- An object that can return the location of
any SAX document event.
**See Also:** Locator

- startDocument

```java
void startDocument()
throws
SAXException
```

Deprecated.

Receive notification of the beginning of a document.

The SAX parser will invoke this method only once, before any
other methods in this interface or in DTDHandler (except for
setDocumentLocator).

**Throws:** SAXException

- Any SAX exception, possibly
wrapping another exception.

- endDocument

```java
void endDocument()
throws
SAXException
```

Deprecated.

Receive notification of the end of a document.

The SAX parser will invoke this method only once, and it will
be the last method invoked during the parse. The parser shall
not invoke this method until it has either abandoned parsing
(because of an unrecoverable error) or reached the end of
input.

**Throws:** SAXException

- Any SAX exception, possibly
wrapping another exception.

- startElement

```java
void startElement​(
String
name,

AttributeList
atts)
throws
SAXException
```

Deprecated.

Receive notification of the beginning of an element.

The Parser will invoke this method at the beginning of every
element in the XML document; there will be a corresponding
endElement() event for every startElement() event (even when the
element is empty). All of the element's content will be
reported, in order, before the corresponding endElement()
event.

If the element name has a namespace prefix, the prefix will
still be attached. Note that the attribute list provided will
contain only attributes with explicit values (specified or
defaulted): #IMPLIED attributes will be omitted.

**Parameters:** name

- The element type name.
**Parameters:** atts

- The attributes attached to the element, if any.
**Throws:** SAXException

- Any SAX exception, possibly
wrapping another exception.
**See Also:** endElement(java.lang.String)

,

AttributeList

- endElement

```java
void endElement​(
String
name)
throws
SAXException
```

Deprecated.

Receive notification of the end of an element.

The SAX parser will invoke this method at the end of every
element in the XML document; there will be a corresponding
startElement() event for every endElement() event (even when the
element is empty).

If the element name has a namespace prefix, the prefix will
still be attached to the name.

**Parameters:** name

- The element type name
**Throws:** SAXException

- Any SAX exception, possibly
wrapping another exception.

- characters

```java
void characters​(char[] ch,
int start,
int length)
throws
SAXException
```

Deprecated.

Receive notification of character data.

The Parser will call this method to report each chunk of
character data. SAX parsers may return all contiguous character
data in a single chunk, or they may split it into several
chunks; however, all of the characters in any single event
must come from the same external entity, so that the Locator
provides useful information.

The application must not attempt to read from the array
outside of the specified range.

Note that some parsers will report whitespace using the
ignorableWhitespace() method rather than this one (validating
parsers must do so).

**Parameters:** ch

- The characters from the XML document.
**Parameters:** start

- The start position in the array.
**Parameters:** length

- The number of characters to read from the array.
**Throws:** SAXException

- Any SAX exception, possibly
wrapping another exception.
**See Also:** ignorableWhitespace(char[], int, int)

,

Locator

- ignorableWhitespace

```java
void ignorableWhitespace​(char[] ch,
int start,
int length)
throws
SAXException
```

Deprecated.

Receive notification of ignorable whitespace in element content.

Validating Parsers must use this method to report each chunk
of ignorable whitespace (see the W3C XML 1.0 recommendation,
section 2.10): non-validating parsers may also use this method
if they are capable of parsing and using content models.

SAX parsers may return all contiguous whitespace in a single
chunk, or they may split it into several chunks; however, all of
the characters in any single event must come from the same
external entity, so that the Locator provides useful
information.

The application must not attempt to read from the array
outside of the specified range.

**Parameters:** ch

- The characters from the XML document.
**Parameters:** start

- The start position in the array.
**Parameters:** length

- The number of characters to read from the array.
**Throws:** SAXException

- Any SAX exception, possibly
wrapping another exception.
**See Also:** characters(char[], int, int)

- processingInstruction

```java
void processingInstruction​(
String
target,

String
data)
throws
SAXException
```

Deprecated.

Receive notification of a processing instruction.

The Parser will invoke this method once for each processing
instruction found: note that processing instructions may occur
before or after the main document element.

A SAX parser should never report an XML declaration (XML 1.0,
section 2.8) or a text declaration (XML 1.0, section 4.3.1)
using this method.

**Parameters:** target

- The processing instruction target.
**Parameters:** data

- The processing instruction data, or null if
none was supplied.
**Throws:** SAXException

- Any SAX exception, possibly
wrapping another exception.

Method Detail

- setDocumentLocator

```java
void setDocumentLocator​(
Locator
locator)
```

Deprecated.

Receive an object for locating the origin of SAX document events.

SAX parsers are strongly encouraged (though not absolutely
required) to supply a locator: if it does so, it must supply
the locator to the application by invoking this method before
invoking any of the other methods in the DocumentHandler
interface.

The locator allows the application to determine the end
position of any document-related event, even if the parser is
not reporting an error. Typically, the application will
use this information for reporting its own errors (such as
character content that does not match an application's
business rules). The information returned by the locator
is probably not sufficient for use with a search engine.

Note that the locator will return correct information only
during the invocation of the events in this interface. The
application should not attempt to use it at any other time.

**Parameters:** locator

- An object that can return the location of
any SAX document event.
**See Also:** Locator

- startDocument

```java
void startDocument()
throws
SAXException
```

Deprecated.

Receive notification of the beginning of a document.

The SAX parser will invoke this method only once, before any
other methods in this interface or in DTDHandler (except for
setDocumentLocator).

**Throws:** SAXException

- Any SAX exception, possibly
wrapping another exception.

- endDocument

```java
void endDocument()
throws
SAXException
```

Deprecated.

Receive notification of the end of a document.

The SAX parser will invoke this method only once, and it will
be the last method invoked during the parse. The parser shall
not invoke this method until it has either abandoned parsing
(because of an unrecoverable error) or reached the end of
input.

**Throws:** SAXException

- Any SAX exception, possibly
wrapping another exception.

- startElement

```java
void startElement​(
String
name,

AttributeList
atts)
throws
SAXException
```

Deprecated.

Receive notification of the beginning of an element.

The Parser will invoke this method at the beginning of every
element in the XML document; there will be a corresponding
endElement() event for every startElement() event (even when the
element is empty). All of the element's content will be
reported, in order, before the corresponding endElement()
event.

If the element name has a namespace prefix, the prefix will
still be attached. Note that the attribute list provided will
contain only attributes with explicit values (specified or
defaulted): #IMPLIED attributes will be omitted.

**Parameters:** name

- The element type name.
**Parameters:** atts

- The attributes attached to the element, if any.
**Throws:** SAXException

- Any SAX exception, possibly
wrapping another exception.
**See Also:** endElement(java.lang.String)

,

AttributeList

- endElement

```java
void endElement​(
String
name)
throws
SAXException
```

Deprecated.

Receive notification of the end of an element.

The SAX parser will invoke this method at the end of every
element in the XML document; there will be a corresponding
startElement() event for every endElement() event (even when the
element is empty).

If the element name has a namespace prefix, the prefix will
still be attached to the name.

**Parameters:** name

- The element type name
**Throws:** SAXException

- Any SAX exception, possibly
wrapping another exception.

- characters

```java
void characters​(char[] ch,
int start,
int length)
throws
SAXException
```

Deprecated.

Receive notification of character data.

The Parser will call this method to report each chunk of
character data. SAX parsers may return all contiguous character
data in a single chunk, or they may split it into several
chunks; however, all of the characters in any single event
must come from the same external entity, so that the Locator
provides useful information.

The application must not attempt to read from the array
outside of the specified range.

Note that some parsers will report whitespace using the
ignorableWhitespace() method rather than this one (validating
parsers must do so).

**Parameters:** ch

- The characters from the XML document.
**Parameters:** start

- The start position in the array.
**Parameters:** length

- The number of characters to read from the array.
**Throws:** SAXException

- Any SAX exception, possibly
wrapping another exception.
**See Also:** ignorableWhitespace(char[], int, int)

,

Locator

- ignorableWhitespace

```java
void ignorableWhitespace​(char[] ch,
int start,
int length)
throws
SAXException
```

Deprecated.

Receive notification of ignorable whitespace in element content.

Validating Parsers must use this method to report each chunk
of ignorable whitespace (see the W3C XML 1.0 recommendation,
section 2.10): non-validating parsers may also use this method
if they are capable of parsing and using content models.

SAX parsers may return all contiguous whitespace in a single
chunk, or they may split it into several chunks; however, all of
the characters in any single event must come from the same
external entity, so that the Locator provides useful
information.

The application must not attempt to read from the array
outside of the specified range.

**Parameters:** ch

- The characters from the XML document.
**Parameters:** start

- The start position in the array.
**Parameters:** length

- The number of characters to read from the array.
**Throws:** SAXException

- Any SAX exception, possibly
wrapping another exception.
**See Also:** characters(char[], int, int)

- processingInstruction

```java
void processingInstruction​(
String
target,

String
data)
throws
SAXException
```

Deprecated.

Receive notification of a processing instruction.

The Parser will invoke this method once for each processing
instruction found: note that processing instructions may occur
before or after the main document element.

A SAX parser should never report an XML declaration (XML 1.0,
section 2.8) or a text declaration (XML 1.0, section 4.3.1)
using this method.

**Parameters:** target

- The processing instruction target.
**Parameters:** data

- The processing instruction data, or null if
none was supplied.
**Throws:** SAXException

- Any SAX exception, possibly
wrapping another exception.

---

#### Method Detail

setDocumentLocator

```java
void setDocumentLocator​(
Locator
locator)
```

Deprecated.

Receive an object for locating the origin of SAX document events.

SAX parsers are strongly encouraged (though not absolutely
required) to supply a locator: if it does so, it must supply
the locator to the application by invoking this method before
invoking any of the other methods in the DocumentHandler
interface.

The locator allows the application to determine the end
position of any document-related event, even if the parser is
not reporting an error. Typically, the application will
use this information for reporting its own errors (such as
character content that does not match an application's
business rules). The information returned by the locator
is probably not sufficient for use with a search engine.

Note that the locator will return correct information only
during the invocation of the events in this interface. The
application should not attempt to use it at any other time.

**Parameters:** locator

- An object that can return the location of
any SAX document event.
**See Also:** Locator

---

#### setDocumentLocator

void setDocumentLocator​(

Locator

locator)

Receive an object for locating the origin of SAX document events.

SAX parsers are strongly encouraged (though not absolutely
required) to supply a locator: if it does so, it must supply
the locator to the application by invoking this method before
invoking any of the other methods in the DocumentHandler
interface.

The locator allows the application to determine the end
position of any document-related event, even if the parser is
not reporting an error. Typically, the application will
use this information for reporting its own errors (such as
character content that does not match an application's
business rules). The information returned by the locator
is probably not sufficient for use with a search engine.

Note that the locator will return correct information only
during the invocation of the events in this interface. The
application should not attempt to use it at any other time.

SAX parsers are strongly encouraged (though not absolutely
required) to supply a locator: if it does so, it must supply
the locator to the application by invoking this method before
invoking any of the other methods in the DocumentHandler
interface.

The locator allows the application to determine the end
position of any document-related event, even if the parser is
not reporting an error. Typically, the application will
use this information for reporting its own errors (such as
character content that does not match an application's
business rules). The information returned by the locator
is probably not sufficient for use with a search engine.

Note that the locator will return correct information only
during the invocation of the events in this interface. The
application should not attempt to use it at any other time.

startDocument

```java
void startDocument()
throws
SAXException
```

Deprecated.

Receive notification of the beginning of a document.

The SAX parser will invoke this method only once, before any
other methods in this interface or in DTDHandler (except for
setDocumentLocator).

**Throws:** SAXException

- Any SAX exception, possibly
wrapping another exception.

---

#### startDocument

void startDocument()
throws

SAXException

Receive notification of the beginning of a document.

The SAX parser will invoke this method only once, before any
other methods in this interface or in DTDHandler (except for
setDocumentLocator).

The SAX parser will invoke this method only once, before any
other methods in this interface or in DTDHandler (except for
setDocumentLocator).

endDocument

```java
void endDocument()
throws
SAXException
```

Deprecated.

Receive notification of the end of a document.

The SAX parser will invoke this method only once, and it will
be the last method invoked during the parse. The parser shall
not invoke this method until it has either abandoned parsing
(because of an unrecoverable error) or reached the end of
input.

**Throws:** SAXException

- Any SAX exception, possibly
wrapping another exception.

---

#### endDocument

void endDocument()
throws

SAXException

Receive notification of the end of a document.

The SAX parser will invoke this method only once, and it will
be the last method invoked during the parse. The parser shall
not invoke this method until it has either abandoned parsing
(because of an unrecoverable error) or reached the end of
input.

The SAX parser will invoke this method only once, and it will
be the last method invoked during the parse. The parser shall
not invoke this method until it has either abandoned parsing
(because of an unrecoverable error) or reached the end of
input.

startElement

```java
void startElement​(
String
name,

AttributeList
atts)
throws
SAXException
```

Deprecated.

Receive notification of the beginning of an element.

The Parser will invoke this method at the beginning of every
element in the XML document; there will be a corresponding
endElement() event for every startElement() event (even when the
element is empty). All of the element's content will be
reported, in order, before the corresponding endElement()
event.

If the element name has a namespace prefix, the prefix will
still be attached. Note that the attribute list provided will
contain only attributes with explicit values (specified or
defaulted): #IMPLIED attributes will be omitted.

**Parameters:** name

- The element type name.
**Parameters:** atts

- The attributes attached to the element, if any.
**Throws:** SAXException

- Any SAX exception, possibly
wrapping another exception.
**See Also:** endElement(java.lang.String)

,

AttributeList

---

#### startElement

void startElement​(

String

name,

AttributeList

atts)
throws

SAXException

Receive notification of the beginning of an element.

The Parser will invoke this method at the beginning of every
element in the XML document; there will be a corresponding
endElement() event for every startElement() event (even when the
element is empty). All of the element's content will be
reported, in order, before the corresponding endElement()
event.

If the element name has a namespace prefix, the prefix will
still be attached. Note that the attribute list provided will
contain only attributes with explicit values (specified or
defaulted): #IMPLIED attributes will be omitted.

The Parser will invoke this method at the beginning of every
element in the XML document; there will be a corresponding
endElement() event for every startElement() event (even when the
element is empty). All of the element's content will be
reported, in order, before the corresponding endElement()
event.

If the element name has a namespace prefix, the prefix will
still be attached. Note that the attribute list provided will
contain only attributes with explicit values (specified or
defaulted): #IMPLIED attributes will be omitted.

endElement

```java
void endElement​(
String
name)
throws
SAXException
```

Deprecated.

Receive notification of the end of an element.

The SAX parser will invoke this method at the end of every
element in the XML document; there will be a corresponding
startElement() event for every endElement() event (even when the
element is empty).

If the element name has a namespace prefix, the prefix will
still be attached to the name.

**Parameters:** name

- The element type name
**Throws:** SAXException

- Any SAX exception, possibly
wrapping another exception.

---

#### endElement

void endElement​(

String

name)
throws

SAXException

Receive notification of the end of an element.

The SAX parser will invoke this method at the end of every
element in the XML document; there will be a corresponding
startElement() event for every endElement() event (even when the
element is empty).

If the element name has a namespace prefix, the prefix will
still be attached to the name.

The SAX parser will invoke this method at the end of every
element in the XML document; there will be a corresponding
startElement() event for every endElement() event (even when the
element is empty).

If the element name has a namespace prefix, the prefix will
still be attached to the name.

characters

```java
void characters​(char[] ch,
int start,
int length)
throws
SAXException
```

Deprecated.

Receive notification of character data.

The Parser will call this method to report each chunk of
character data. SAX parsers may return all contiguous character
data in a single chunk, or they may split it into several
chunks; however, all of the characters in any single event
must come from the same external entity, so that the Locator
provides useful information.

The application must not attempt to read from the array
outside of the specified range.

Note that some parsers will report whitespace using the
ignorableWhitespace() method rather than this one (validating
parsers must do so).

**Parameters:** ch

- The characters from the XML document.
**Parameters:** start

- The start position in the array.
**Parameters:** length

- The number of characters to read from the array.
**Throws:** SAXException

- Any SAX exception, possibly
wrapping another exception.
**See Also:** ignorableWhitespace(char[], int, int)

,

Locator

---

#### characters

void characters​(char[] ch,
int start,
int length)
throws

SAXException

Receive notification of character data.

The Parser will call this method to report each chunk of
character data. SAX parsers may return all contiguous character
data in a single chunk, or they may split it into several
chunks; however, all of the characters in any single event
must come from the same external entity, so that the Locator
provides useful information.

The application must not attempt to read from the array
outside of the specified range.

Note that some parsers will report whitespace using the
ignorableWhitespace() method rather than this one (validating
parsers must do so).

The Parser will call this method to report each chunk of
character data. SAX parsers may return all contiguous character
data in a single chunk, or they may split it into several
chunks; however, all of the characters in any single event
must come from the same external entity, so that the Locator
provides useful information.

The application must not attempt to read from the array
outside of the specified range.

Note that some parsers will report whitespace using the
ignorableWhitespace() method rather than this one (validating
parsers must do so).

ignorableWhitespace

```java
void ignorableWhitespace​(char[] ch,
int start,
int length)
throws
SAXException
```

Deprecated.

Receive notification of ignorable whitespace in element content.

Validating Parsers must use this method to report each chunk
of ignorable whitespace (see the W3C XML 1.0 recommendation,
section 2.10): non-validating parsers may also use this method
if they are capable of parsing and using content models.

SAX parsers may return all contiguous whitespace in a single
chunk, or they may split it into several chunks; however, all of
the characters in any single event must come from the same
external entity, so that the Locator provides useful
information.

The application must not attempt to read from the array
outside of the specified range.

**Parameters:** ch

- The characters from the XML document.
**Parameters:** start

- The start position in the array.
**Parameters:** length

- The number of characters to read from the array.
**Throws:** SAXException

- Any SAX exception, possibly
wrapping another exception.
**See Also:** characters(char[], int, int)

---

#### ignorableWhitespace

void ignorableWhitespace​(char[] ch,
int start,
int length)
throws

SAXException

Receive notification of ignorable whitespace in element content.

Validating Parsers must use this method to report each chunk
of ignorable whitespace (see the W3C XML 1.0 recommendation,
section 2.10): non-validating parsers may also use this method
if they are capable of parsing and using content models.

SAX parsers may return all contiguous whitespace in a single
chunk, or they may split it into several chunks; however, all of
the characters in any single event must come from the same
external entity, so that the Locator provides useful
information.

The application must not attempt to read from the array
outside of the specified range.

Validating Parsers must use this method to report each chunk
of ignorable whitespace (see the W3C XML 1.0 recommendation,
section 2.10): non-validating parsers may also use this method
if they are capable of parsing and using content models.

SAX parsers may return all contiguous whitespace in a single
chunk, or they may split it into several chunks; however, all of
the characters in any single event must come from the same
external entity, so that the Locator provides useful
information.

The application must not attempt to read from the array
outside of the specified range.

processingInstruction

```java
void processingInstruction​(
String
target,

String
data)
throws
SAXException
```

Deprecated.

Receive notification of a processing instruction.

The Parser will invoke this method once for each processing
instruction found: note that processing instructions may occur
before or after the main document element.

A SAX parser should never report an XML declaration (XML 1.0,
section 2.8) or a text declaration (XML 1.0, section 4.3.1)
using this method.

**Parameters:** target

- The processing instruction target.
**Parameters:** data

- The processing instruction data, or null if
none was supplied.
**Throws:** SAXException

- Any SAX exception, possibly
wrapping another exception.

---

#### processingInstruction

void processingInstruction​(

String

target,

String

data)
throws

SAXException

Receive notification of a processing instruction.

The Parser will invoke this method once for each processing
instruction found: note that processing instructions may occur
before or after the main document element.

A SAX parser should never report an XML declaration (XML 1.0,
section 2.8) or a text declaration (XML 1.0, section 4.3.1)
using this method.

The Parser will invoke this method once for each processing
instruction found: note that processing instructions may occur
before or after the main document element.

A SAX parser should never report an XML declaration (XML 1.0,
section 2.8) or a text declaration (XML 1.0, section 4.3.1)
using this method.

---

