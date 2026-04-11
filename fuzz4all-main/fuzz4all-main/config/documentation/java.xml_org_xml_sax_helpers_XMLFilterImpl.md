# Class XMLFilterImpl

**Source:** `java.xml\org\xml\sax\helpers\XMLFilterImpl.html`

### Class Description

```java
public class
XMLFilterImpl

extends
Object

implements
XMLFilter
,
EntityResolver
,
DTDHandler
,
ContentHandler
,
ErrorHandler
```

Base class for deriving an XML filter.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

This class is designed to sit between an

XMLReader

and the client application's event handlers. By default, it
does nothing but pass requests up to the reader and events
on to the handlers unmodified, but subclasses can override
specific methods to modify the event stream or the configuration
requests as they pass through.

**All Implemented Interfaces:** ContentHandler

,

DTDHandler

,

EntityResolver

,

ErrorHandler

,

XMLFilter

,

XMLReader

---

### Field Details

*No entries found.*

### Constructor Details

#### public XMLFilterImpl()

Construct an empty XML filter, with no parent.

This filter will have no parent: you must assign a parent
before you start a parse or do any configuration with
setFeature or setProperty, unless you use this as a pure event
consumer rather than as an

XMLReader

.

**See Also:**
- XMLReader.setFeature(java.lang.String, boolean)

,

XMLReader.setProperty(java.lang.String, java.lang.Object)

,

setParent(org.xml.sax.XMLReader)

---

#### public XMLFilterImpl​(
XMLReader
parent)

Construct an XML filter with the specified parent.

**See Also:**
- setParent(org.xml.sax.XMLReader)

,

getParent()

---

### Method Details

#### public void setParent​(
XMLReader
parent)

Set the parent reader.

This is the

XMLReader

from which
this filter will obtain its events and to which it will pass its
configuration requests. The parent may itself be another filter.

If there is no parent reader set, any attempt to parse
or to set or get a feature or property will fail.

**Specified by:**
- setParent

in interface

XMLFilter

**Parameters:**
- parent

- The parent XML reader.

**See Also:**
- getParent()

---

#### public
XMLReader
getParent()

Get the parent reader.

**Specified by:**
- getParent

in interface

XMLFilter

**Returns:**
- The parent XML reader, or null if none is set.

**See Also:**
- setParent(org.xml.sax.XMLReader)

---

#### public void setFeature​(
String
name,
boolean value)
throws
SAXNotRecognizedException
,

SAXNotSupportedException

Set the value of a feature.

This will always fail if the parent is null.

**Specified by:**
- setFeature

in interface

XMLReader

**Parameters:**
- name

- The feature name.
- value

- The requested feature value.

**Throws:**
- SAXNotRecognizedException

- If the feature
value can't be assigned or retrieved from the parent.
- SAXNotSupportedException

- When the
parent recognizes the feature name but
cannot set the requested value.

**See Also:**
- XMLReader.getFeature(java.lang.String)

---

#### public boolean getFeature​(
String
name)
throws
SAXNotRecognizedException
,

SAXNotSupportedException

Look up the value of a feature.

This will always fail if the parent is null.

**Specified by:**
- getFeature

in interface

XMLReader

**Parameters:**
- name

- The feature name.

**Returns:**
- The current value of the feature.

**Throws:**
- SAXNotRecognizedException

- If the feature
value can't be assigned or retrieved from the parent.
- SAXNotSupportedException

- When the
parent recognizes the feature name but
cannot determine its value at this time.

**See Also:**
- XMLReader.setFeature(java.lang.String, boolean)

---

#### public void setProperty​(
String
name,

Object
value)
throws
SAXNotRecognizedException
,

SAXNotSupportedException

Set the value of a property.

This will always fail if the parent is null.

**Specified by:**
- setProperty

in interface

XMLReader

**Parameters:**
- name

- The property name.
- value

- The requested property value.

**Throws:**
- SAXNotRecognizedException

- If the property
value can't be assigned or retrieved from the parent.
- SAXNotSupportedException

- When the
parent recognizes the property name but
cannot set the requested value.

---

#### public
Object
getProperty​(
String
name)
throws
SAXNotRecognizedException
,

SAXNotSupportedException

Look up the value of a property.

**Specified by:**
- getProperty

in interface

XMLReader

**Parameters:**
- name

- The property name.

**Returns:**
- The current value of the property.

**Throws:**
- SAXNotRecognizedException

- If the property
value can't be assigned or retrieved from the parent.
- SAXNotSupportedException

- When the
parent recognizes the property name but
cannot determine its value at this time.

**See Also:**
- XMLReader.setProperty(java.lang.String, java.lang.Object)

---

#### public void setEntityResolver​(
EntityResolver
resolver)

Set the entity resolver.

**Specified by:**
- setEntityResolver

in interface

XMLReader

**Parameters:**
- resolver

- The new entity resolver.

**See Also:**
- XMLReader.getEntityResolver()

---

#### public
EntityResolver
getEntityResolver()

Get the current entity resolver.

**Specified by:**
- getEntityResolver

in interface

XMLReader

**Returns:**
- The current entity resolver, or null if none was set.

**See Also:**
- XMLReader.setEntityResolver(org.xml.sax.EntityResolver)

---

#### public void setDTDHandler​(
DTDHandler
handler)

Set the DTD event handler.

**Specified by:**
- setDTDHandler

in interface

XMLReader

**Parameters:**
- handler

- the new DTD handler

**See Also:**
- XMLReader.getDTDHandler()

---

#### public
DTDHandler
getDTDHandler()

Get the current DTD event handler.

**Specified by:**
- getDTDHandler

in interface

XMLReader

**Returns:**
- The current DTD handler, or null if none was set.

**See Also:**
- XMLReader.setDTDHandler(org.xml.sax.DTDHandler)

---

#### public void setContentHandler​(
ContentHandler
handler)

Set the content event handler.

**Specified by:**
- setContentHandler

in interface

XMLReader

**Parameters:**
- handler

- the new content handler

**See Also:**
- XMLReader.getContentHandler()

---

#### public
ContentHandler
getContentHandler()

Get the content event handler.

**Specified by:**
- getContentHandler

in interface

XMLReader

**Returns:**
- The current content handler, or null if none was set.

**See Also:**
- XMLReader.setContentHandler(org.xml.sax.ContentHandler)

---

#### public void setErrorHandler​(
ErrorHandler
handler)

Set the error event handler.

**Specified by:**
- setErrorHandler

in interface

XMLReader

**Parameters:**
- handler

- the new error handler

**See Also:**
- XMLReader.getErrorHandler()

---

#### public
ErrorHandler
getErrorHandler()

Get the current error event handler.

**Specified by:**
- getErrorHandler

in interface

XMLReader

**Returns:**
- The current error handler, or null if none was set.

**See Also:**
- XMLReader.setErrorHandler(org.xml.sax.ErrorHandler)

---

#### public void parse​(
InputSource
input)
throws
SAXException
,

IOException

Parse a document.

**Specified by:**
- parse

in interface

XMLReader

**Parameters:**
- input

- The input source for the document entity.

**Throws:**
- SAXException

- Any SAX exception, possibly
wrapping another exception.
- IOException

- An IO exception from the parser,
possibly from a byte stream or character stream
supplied by the application.

**See Also:**
- InputSource

,

XMLReader.parse(java.lang.String)

,

XMLReader.setEntityResolver(org.xml.sax.EntityResolver)

,

XMLReader.setDTDHandler(org.xml.sax.DTDHandler)

,

XMLReader.setContentHandler(org.xml.sax.ContentHandler)

,

XMLReader.setErrorHandler(org.xml.sax.ErrorHandler)

---

#### public void parse​(
String
systemId)
throws
SAXException
,

IOException

Parse a document.

**Specified by:**
- parse

in interface

XMLReader

**Parameters:**
- systemId

- The system identifier as a fully-qualified URI.

**Throws:**
- SAXException

- Any SAX exception, possibly
wrapping another exception.
- IOException

- An IO exception from the parser,
possibly from a byte stream or character stream
supplied by the application.

**See Also:**
- XMLReader.parse(org.xml.sax.InputSource)

---

#### public
InputSource
resolveEntity​(
String
publicId,

String
systemId)
throws
SAXException
,

IOException

Filter an external entity resolution.

**Specified by:**
- resolveEntity

in interface

EntityResolver

**Parameters:**
- publicId

- The entity's public identifier, or null.
- systemId

- The entity's system identifier.

**Returns:**
- A new InputSource or null for the default.

**Throws:**
- SAXException

- The client may throw
an exception during processing.
- IOException

- The client may throw an
I/O-related exception while obtaining the
new InputSource.

**See Also:**
- InputSource

---

#### public void notationDecl​(
String
name,

String
publicId,

String
systemId)
throws
SAXException

Filter a notation declaration event.

**Specified by:**
- notationDecl

in interface

DTDHandler

**Parameters:**
- name

- The notation name.
- publicId

- The notation's public identifier, or null.
- systemId

- The notation's system identifier, or null.

**Throws:**
- SAXException

- The client may throw
an exception during processing.

**See Also:**
- DTDHandler.unparsedEntityDecl(java.lang.String, java.lang.String, java.lang.String, java.lang.String)

,

Attributes

---

#### public void unparsedEntityDecl​(
String
name,

String
publicId,

String
systemId,

String
notationName)
throws
SAXException

Filter an unparsed entity declaration event.

**Specified by:**
- unparsedEntityDecl

in interface

DTDHandler

**Parameters:**
- name

- The entity name.
- publicId

- The entity's public identifier, or null.
- systemId

- The entity's system identifier, or null.
- notationName

- The name of the associated notation.

**Throws:**
- SAXException

- The client may throw
an exception during processing.

**See Also:**
- DTDHandler.notationDecl(java.lang.String, java.lang.String, java.lang.String)

,

Attributes

---

#### public void setDocumentLocator​(
Locator
locator)

Filter a new document locator event.

**Specified by:**
- setDocumentLocator

in interface

ContentHandler

**Parameters:**
- locator

- The document locator.

**See Also:**
- Locator

---

#### public void startDocument()
throws
SAXException

Filter a start document event.

**Specified by:**
- startDocument

in interface

ContentHandler

**Throws:**
- SAXException

- The client may throw
an exception during processing.

**See Also:**
- ContentHandler.endDocument()

---

#### public void endDocument()
throws
SAXException

Filter an end document event.

**Specified by:**
- endDocument

in interface

ContentHandler

**Throws:**
- SAXException

- The client may throw
an exception during processing.

**See Also:**
- ContentHandler.startDocument()

---

#### public void startPrefixMapping​(
String
prefix,

String
uri)
throws
SAXException

Filter a start Namespace prefix mapping event.

**Specified by:**
- startPrefixMapping

in interface

ContentHandler

**Parameters:**
- prefix

- The Namespace prefix.
- uri

- The Namespace URI.

**Throws:**
- SAXException

- The client may throw
an exception during processing.

**See Also:**
- ContentHandler.endPrefixMapping(java.lang.String)

,

ContentHandler.startElement(java.lang.String, java.lang.String, java.lang.String, org.xml.sax.Attributes)

---

#### public void endPrefixMapping​(
String
prefix)
throws
SAXException

Filter an end Namespace prefix mapping event.

**Specified by:**
- endPrefixMapping

in interface

ContentHandler

**Parameters:**
- prefix

- The Namespace prefix.

**Throws:**
- SAXException

- The client may throw
an exception during processing.

**See Also:**
- ContentHandler.startPrefixMapping(java.lang.String, java.lang.String)

,

ContentHandler.endElement(java.lang.String, java.lang.String, java.lang.String)

---

#### public void startElement​(
String
uri,

String
localName,

String
qName,

Attributes
atts)
throws
SAXException

Filter a start element event.

**Specified by:**
- startElement

in interface

ContentHandler

**Parameters:**
- uri

- The element's Namespace URI, or the empty string.
- localName

- The element's local name, or the empty string.
- qName

- The element's qualified (prefixed) name, or the empty
string.
- atts

- The element's attributes.

**Throws:**
- SAXException

- The client may throw
an exception during processing.

**See Also:**
- ContentHandler.endElement(java.lang.String, java.lang.String, java.lang.String)

,

Attributes

,

AttributesImpl

---

#### public void endElement​(
String
uri,

String
localName,

String
qName)
throws
SAXException

Filter an end element event.

**Specified by:**
- endElement

in interface

ContentHandler

**Parameters:**
- uri

- The element's Namespace URI, or the empty string.
- localName

- The element's local name, or the empty string.
- qName

- The element's qualified (prefixed) name, or the empty
string.

**Throws:**
- SAXException

- The client may throw
an exception during processing.

---

#### public void characters​(char[] ch,
int start,
int length)
throws
SAXException

Filter a character data event.

**Specified by:**
- characters

in interface

ContentHandler

**Parameters:**
- ch

- An array of characters.
- start

- The starting position in the array.
- length

- The number of characters to use from the array.

**Throws:**
- SAXException

- The client may throw
an exception during processing.

**See Also:**
- ContentHandler.ignorableWhitespace(char[], int, int)

,

Locator

---

#### public void ignorableWhitespace​(char[] ch,
int start,
int length)
throws
SAXException

Filter an ignorable whitespace event.

**Specified by:**
- ignorableWhitespace

in interface

ContentHandler

**Parameters:**
- ch

- An array of characters.
- start

- The starting position in the array.
- length

- The number of characters to use from the array.

**Throws:**
- SAXException

- The client may throw
an exception during processing.

**See Also:**
- ContentHandler.characters(char[], int, int)

---

#### public void processingInstruction​(
String
target,

String
data)
throws
SAXException

Filter a processing instruction event.

**Specified by:**
- processingInstruction

in interface

ContentHandler

**Parameters:**
- target

- The processing instruction target.
- data

- The text following the target.

**Throws:**
- SAXException

- The client may throw
an exception during processing.

---

#### public void skippedEntity​(
String
name)
throws
SAXException

Filter a skipped entity event.

**Specified by:**
- skippedEntity

in interface

ContentHandler

**Parameters:**
- name

- The name of the skipped entity.

**Throws:**
- SAXException

- The client may throw
an exception during processing.

---

#### public void warning​(
SAXParseException
e)
throws
SAXException

Filter a warning event.

**Specified by:**
- warning

in interface

ErrorHandler

**Parameters:**
- e

- The warning as an exception.

**Throws:**
- SAXException

- The client may throw
an exception during processing.

**See Also:**
- SAXParseException

---

#### public void error​(
SAXParseException
e)
throws
SAXException

Filter an error event.

**Specified by:**
- error

in interface

ErrorHandler

**Parameters:**
- e

- The error as an exception.

**Throws:**
- SAXException

- The client may throw
an exception during processing.

**See Also:**
- SAXParseException

---

#### public void fatalError​(
SAXParseException
e)
throws
SAXException

Filter a fatal error event.

**Specified by:**
- fatalError

in interface

ErrorHandler

**Parameters:**
- e

- The error as an exception.

**Throws:**
- SAXException

- The client may throw
an exception during processing.

**See Also:**
- SAXParseException

---

### Additional Sections

#### Class XMLFilterImpl

java.lang.Object

- org.xml.sax.helpers.XMLFilterImpl

org.xml.sax.helpers.XMLFilterImpl

**All Implemented Interfaces:** ContentHandler

,

DTDHandler

,

EntityResolver

,

ErrorHandler

,

XMLFilter

,

XMLReader

```java
public class
XMLFilterImpl

extends
Object

implements
XMLFilter
,
EntityResolver
,
DTDHandler
,
ContentHandler
,
ErrorHandler
```

Base class for deriving an XML filter.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

This class is designed to sit between an

XMLReader

and the client application's event handlers. By default, it
does nothing but pass requests up to the reader and events
on to the handlers unmodified, but subclasses can override
specific methods to modify the event stream or the configuration
requests as they pass through.

**Since:** 1.4, SAX 2.0
**See Also:** XMLFilter

,

XMLReader

,

EntityResolver

,

DTDHandler

,

ContentHandler

,

ErrorHandler

public class

XMLFilterImpl

extends

Object

implements

XMLFilter

,

EntityResolver

,

DTDHandler

,

ContentHandler

,

ErrorHandler

Base class for deriving an XML filter.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

This class is designed to sit between an

XMLReader

and the client application's event handlers. By default, it
does nothing but pass requests up to the reader and events
on to the handlers unmodified, but subclasses can override
specific methods to modify the event stream or the configuration
requests as they pass through.

This class is designed to sit between an

XMLReader

and the client application's event handlers. By default, it
does nothing but pass requests up to the reader and events
on to the handlers unmodified, but subclasses can override
specific methods to modify the event stream or the configuration
requests as they pass through.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

XMLFilterImpl

()

Construct an empty XML filter, with no parent.

XMLFilterImpl

​(

XMLReader

parent)

Construct an XML filter with the specified parent.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

characters

​(char[] ch,
int start,
int length)

Filter a character data event.

void

endDocument

()

Filter an end document event.

void

endElement

​(

String

uri,

String

localName,

String

qName)

Filter an end element event.

void

endPrefixMapping

​(

String

prefix)

Filter an end Namespace prefix mapping event.

void

error

​(

SAXParseException

e)

Filter an error event.

void

fatalError

​(

SAXParseException

e)

Filter a fatal error event.

ContentHandler

getContentHandler

()

Get the content event handler.

DTDHandler

getDTDHandler

()

Get the current DTD event handler.

EntityResolver

getEntityResolver

()

Get the current entity resolver.

ErrorHandler

getErrorHandler

()

Get the current error event handler.

boolean

getFeature

​(

String

name)

Look up the value of a feature.

XMLReader

getParent

()

Get the parent reader.

Object

getProperty

​(

String

name)

Look up the value of a property.

void

ignorableWhitespace

​(char[] ch,
int start,
int length)

Filter an ignorable whitespace event.

void

notationDecl

​(

String

name,

String

publicId,

String

systemId)

Filter a notation declaration event.

void

parse

​(

String

systemId)

Parse a document.

void

parse

​(

InputSource

input)

Parse a document.

void

processingInstruction

​(

String

target,

String

data)

Filter a processing instruction event.

InputSource

resolveEntity

​(

String

publicId,

String

systemId)

Filter an external entity resolution.

void

setContentHandler

​(

ContentHandler

handler)

Set the content event handler.

void

setDocumentLocator

​(

Locator

locator)

Filter a new document locator event.

void

setDTDHandler

​(

DTDHandler

handler)

Set the DTD event handler.

void

setEntityResolver

​(

EntityResolver

resolver)

Set the entity resolver.

void

setErrorHandler

​(

ErrorHandler

handler)

Set the error event handler.

void

setFeature

​(

String

name,
boolean value)

Set the value of a feature.

void

setParent

​(

XMLReader

parent)

Set the parent reader.

void

setProperty

​(

String

name,

Object

value)

Set the value of a property.

void

skippedEntity

​(

String

name)

Filter a skipped entity event.

void

startDocument

()

Filter a start document event.

void

startElement

​(

String

uri,

String

localName,

String

qName,

Attributes

atts)

Filter a start element event.

void

startPrefixMapping

​(

String

prefix,

String

uri)

Filter a start Namespace prefix mapping event.

void

unparsedEntityDecl

​(

String

name,

String

publicId,

String

systemId,

String

notationName)

Filter an unparsed entity declaration event.

void

warning

​(

SAXParseException

e)

Filter a warning event.

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

Constructor Summary

Constructors

Constructor

Description

XMLFilterImpl

()

Construct an empty XML filter, with no parent.

XMLFilterImpl

​(

XMLReader

parent)

Construct an XML filter with the specified parent.

---

#### Constructor Summary

Construct an empty XML filter, with no parent.

Construct an XML filter with the specified parent.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

characters

​(char[] ch,
int start,
int length)

Filter a character data event.

void

endDocument

()

Filter an end document event.

void

endElement

​(

String

uri,

String

localName,

String

qName)

Filter an end element event.

void

endPrefixMapping

​(

String

prefix)

Filter an end Namespace prefix mapping event.

void

error

​(

SAXParseException

e)

Filter an error event.

void

fatalError

​(

SAXParseException

e)

Filter a fatal error event.

ContentHandler

getContentHandler

()

Get the content event handler.

DTDHandler

getDTDHandler

()

Get the current DTD event handler.

EntityResolver

getEntityResolver

()

Get the current entity resolver.

ErrorHandler

getErrorHandler

()

Get the current error event handler.

boolean

getFeature

​(

String

name)

Look up the value of a feature.

XMLReader

getParent

()

Get the parent reader.

Object

getProperty

​(

String

name)

Look up the value of a property.

void

ignorableWhitespace

​(char[] ch,
int start,
int length)

Filter an ignorable whitespace event.

void

notationDecl

​(

String

name,

String

publicId,

String

systemId)

Filter a notation declaration event.

void

parse

​(

String

systemId)

Parse a document.

void

parse

​(

InputSource

input)

Parse a document.

void

processingInstruction

​(

String

target,

String

data)

Filter a processing instruction event.

InputSource

resolveEntity

​(

String

publicId,

String

systemId)

Filter an external entity resolution.

void

setContentHandler

​(

ContentHandler

handler)

Set the content event handler.

void

setDocumentLocator

​(

Locator

locator)

Filter a new document locator event.

void

setDTDHandler

​(

DTDHandler

handler)

Set the DTD event handler.

void

setEntityResolver

​(

EntityResolver

resolver)

Set the entity resolver.

void

setErrorHandler

​(

ErrorHandler

handler)

Set the error event handler.

void

setFeature

​(

String

name,
boolean value)

Set the value of a feature.

void

setParent

​(

XMLReader

parent)

Set the parent reader.

void

setProperty

​(

String

name,

Object

value)

Set the value of a property.

void

skippedEntity

​(

String

name)

Filter a skipped entity event.

void

startDocument

()

Filter a start document event.

void

startElement

​(

String

uri,

String

localName,

String

qName,

Attributes

atts)

Filter a start element event.

void

startPrefixMapping

​(

String

prefix,

String

uri)

Filter a start Namespace prefix mapping event.

void

unparsedEntityDecl

​(

String

name,

String

publicId,

String

systemId,

String

notationName)

Filter an unparsed entity declaration event.

void

warning

​(

SAXParseException

e)

Filter a warning event.

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

---

#### Method Summary

Filter a character data event.

Filter an end document event.

Filter an end element event.

Filter an end Namespace prefix mapping event.

Filter an error event.

Filter a fatal error event.

Get the content event handler.

Get the current DTD event handler.

Get the current entity resolver.

Get the current error event handler.

Look up the value of a feature.

Get the parent reader.

Look up the value of a property.

Filter an ignorable whitespace event.

Filter a notation declaration event.

Parse a document.

Filter a processing instruction event.

Filter an external entity resolution.

Set the content event handler.

Filter a new document locator event.

Set the DTD event handler.

Set the entity resolver.

Set the error event handler.

Set the value of a feature.

Set the parent reader.

Set the value of a property.

Filter a skipped entity event.

Filter a start document event.

Filter a start element event.

Filter a start Namespace prefix mapping event.

Filter an unparsed entity declaration event.

Filter a warning event.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- XMLFilterImpl

```java
public XMLFilterImpl()
```

Construct an empty XML filter, with no parent.

This filter will have no parent: you must assign a parent
before you start a parse or do any configuration with
setFeature or setProperty, unless you use this as a pure event
consumer rather than as an

XMLReader

.

**See Also:** XMLReader.setFeature(java.lang.String, boolean)

,

XMLReader.setProperty(java.lang.String, java.lang.Object)

,

setParent(org.xml.sax.XMLReader)

- XMLFilterImpl

```java
public XMLFilterImpl​(
XMLReader
parent)
```

Construct an XML filter with the specified parent.

**See Also:** setParent(org.xml.sax.XMLReader)

,

getParent()

============ METHOD DETAIL ==========

- Method Detail

- setParent

```java
public void setParent​(
XMLReader
parent)
```

Set the parent reader.

This is the

XMLReader

from which
this filter will obtain its events and to which it will pass its
configuration requests. The parent may itself be another filter.

If there is no parent reader set, any attempt to parse
or to set or get a feature or property will fail.

**Specified by:** setParent

in interface

XMLFilter
**Parameters:** parent

- The parent XML reader.
**See Also:** getParent()

- getParent

```java
public
XMLReader
getParent()
```

Get the parent reader.

**Specified by:** getParent

in interface

XMLFilter
**Returns:** The parent XML reader, or null if none is set.
**See Also:** setParent(org.xml.sax.XMLReader)

- setFeature

```java
public void setFeature​(
String
name,
boolean value)
throws
SAXNotRecognizedException
,

SAXNotSupportedException
```

Set the value of a feature.

This will always fail if the parent is null.

**Specified by:** setFeature

in interface

XMLReader
**Parameters:** name

- The feature name.
**Parameters:** value

- The requested feature value.
**Throws:** SAXNotRecognizedException

- If the feature
value can't be assigned or retrieved from the parent.
**Throws:** SAXNotSupportedException

- When the
parent recognizes the feature name but
cannot set the requested value.
**See Also:** XMLReader.getFeature(java.lang.String)

- getFeature

```java
public boolean getFeature​(
String
name)
throws
SAXNotRecognizedException
,

SAXNotSupportedException
```

Look up the value of a feature.

This will always fail if the parent is null.

**Specified by:** getFeature

in interface

XMLReader
**Parameters:** name

- The feature name.
**Returns:** The current value of the feature.
**Throws:** SAXNotRecognizedException

- If the feature
value can't be assigned or retrieved from the parent.
**Throws:** SAXNotSupportedException

- When the
parent recognizes the feature name but
cannot determine its value at this time.
**See Also:** XMLReader.setFeature(java.lang.String, boolean)

- setProperty

```java
public void setProperty​(
String
name,

Object
value)
throws
SAXNotRecognizedException
,

SAXNotSupportedException
```

Set the value of a property.

This will always fail if the parent is null.

**Specified by:** setProperty

in interface

XMLReader
**Parameters:** name

- The property name.
**Parameters:** value

- The requested property value.
**Throws:** SAXNotRecognizedException

- If the property
value can't be assigned or retrieved from the parent.
**Throws:** SAXNotSupportedException

- When the
parent recognizes the property name but
cannot set the requested value.

- getProperty

```java
public
Object
getProperty​(
String
name)
throws
SAXNotRecognizedException
,

SAXNotSupportedException
```

Look up the value of a property.

**Specified by:** getProperty

in interface

XMLReader
**Parameters:** name

- The property name.
**Returns:** The current value of the property.
**Throws:** SAXNotRecognizedException

- If the property
value can't be assigned or retrieved from the parent.
**Throws:** SAXNotSupportedException

- When the
parent recognizes the property name but
cannot determine its value at this time.
**See Also:** XMLReader.setProperty(java.lang.String, java.lang.Object)

- setEntityResolver

```java
public void setEntityResolver​(
EntityResolver
resolver)
```

Set the entity resolver.

**Specified by:** setEntityResolver

in interface

XMLReader
**Parameters:** resolver

- The new entity resolver.
**See Also:** XMLReader.getEntityResolver()

- getEntityResolver

```java
public
EntityResolver
getEntityResolver()
```

Get the current entity resolver.

**Specified by:** getEntityResolver

in interface

XMLReader
**Returns:** The current entity resolver, or null if none was set.
**See Also:** XMLReader.setEntityResolver(org.xml.sax.EntityResolver)

- setDTDHandler

```java
public void setDTDHandler​(
DTDHandler
handler)
```

Set the DTD event handler.

**Specified by:** setDTDHandler

in interface

XMLReader
**Parameters:** handler

- the new DTD handler
**See Also:** XMLReader.getDTDHandler()

- getDTDHandler

```java
public
DTDHandler
getDTDHandler()
```

Get the current DTD event handler.

**Specified by:** getDTDHandler

in interface

XMLReader
**Returns:** The current DTD handler, or null if none was set.
**See Also:** XMLReader.setDTDHandler(org.xml.sax.DTDHandler)

- setContentHandler

```java
public void setContentHandler​(
ContentHandler
handler)
```

Set the content event handler.

**Specified by:** setContentHandler

in interface

XMLReader
**Parameters:** handler

- the new content handler
**See Also:** XMLReader.getContentHandler()

- getContentHandler

```java
public
ContentHandler
getContentHandler()
```

Get the content event handler.

**Specified by:** getContentHandler

in interface

XMLReader
**Returns:** The current content handler, or null if none was set.
**See Also:** XMLReader.setContentHandler(org.xml.sax.ContentHandler)

- setErrorHandler

```java
public void setErrorHandler​(
ErrorHandler
handler)
```

Set the error event handler.

**Specified by:** setErrorHandler

in interface

XMLReader
**Parameters:** handler

- the new error handler
**See Also:** XMLReader.getErrorHandler()

- getErrorHandler

```java
public
ErrorHandler
getErrorHandler()
```

Get the current error event handler.

**Specified by:** getErrorHandler

in interface

XMLReader
**Returns:** The current error handler, or null if none was set.
**See Also:** XMLReader.setErrorHandler(org.xml.sax.ErrorHandler)

- parse

```java
public void parse​(
InputSource
input)
throws
SAXException
,

IOException
```

Parse a document.

**Specified by:** parse

in interface

XMLReader
**Parameters:** input

- The input source for the document entity.
**Throws:** SAXException

- Any SAX exception, possibly
wrapping another exception.
**Throws:** IOException

- An IO exception from the parser,
possibly from a byte stream or character stream
supplied by the application.
**See Also:** InputSource

,

XMLReader.parse(java.lang.String)

,

XMLReader.setEntityResolver(org.xml.sax.EntityResolver)

,

XMLReader.setDTDHandler(org.xml.sax.DTDHandler)

,

XMLReader.setContentHandler(org.xml.sax.ContentHandler)

,

XMLReader.setErrorHandler(org.xml.sax.ErrorHandler)

- parse

```java
public void parse​(
String
systemId)
throws
SAXException
,

IOException
```

Parse a document.

**Specified by:** parse

in interface

XMLReader
**Parameters:** systemId

- The system identifier as a fully-qualified URI.
**Throws:** SAXException

- Any SAX exception, possibly
wrapping another exception.
**Throws:** IOException

- An IO exception from the parser,
possibly from a byte stream or character stream
supplied by the application.
**See Also:** XMLReader.parse(org.xml.sax.InputSource)

- resolveEntity

```java
public
InputSource
resolveEntity​(
String
publicId,

String
systemId)
throws
SAXException
,

IOException
```

Filter an external entity resolution.

**Specified by:** resolveEntity

in interface

EntityResolver
**Parameters:** publicId

- The entity's public identifier, or null.
**Parameters:** systemId

- The entity's system identifier.
**Returns:** A new InputSource or null for the default.
**Throws:** SAXException

- The client may throw
an exception during processing.
**Throws:** IOException

- The client may throw an
I/O-related exception while obtaining the
new InputSource.
**See Also:** InputSource

- notationDecl

```java
public void notationDecl​(
String
name,

String
publicId,

String
systemId)
throws
SAXException
```

Filter a notation declaration event.

**Specified by:** notationDecl

in interface

DTDHandler
**Parameters:** name

- The notation name.
**Parameters:** publicId

- The notation's public identifier, or null.
**Parameters:** systemId

- The notation's system identifier, or null.
**Throws:** SAXException

- The client may throw
an exception during processing.
**See Also:** DTDHandler.unparsedEntityDecl(java.lang.String, java.lang.String, java.lang.String, java.lang.String)

,

Attributes

- unparsedEntityDecl

```java
public void unparsedEntityDecl​(
String
name,

String
publicId,

String
systemId,

String
notationName)
throws
SAXException
```

Filter an unparsed entity declaration event.

**Specified by:** unparsedEntityDecl

in interface

DTDHandler
**Parameters:** name

- The entity name.
**Parameters:** publicId

- The entity's public identifier, or null.
**Parameters:** systemId

- The entity's system identifier, or null.
**Parameters:** notationName

- The name of the associated notation.
**Throws:** SAXException

- The client may throw
an exception during processing.
**See Also:** DTDHandler.notationDecl(java.lang.String, java.lang.String, java.lang.String)

,

Attributes

- setDocumentLocator

```java
public void setDocumentLocator​(
Locator
locator)
```

Filter a new document locator event.

**Specified by:** setDocumentLocator

in interface

ContentHandler
**Parameters:** locator

- The document locator.
**See Also:** Locator

- startDocument

```java
public void startDocument()
throws
SAXException
```

Filter a start document event.

**Specified by:** startDocument

in interface

ContentHandler
**Throws:** SAXException

- The client may throw
an exception during processing.
**See Also:** ContentHandler.endDocument()

- endDocument

```java
public void endDocument()
throws
SAXException
```

Filter an end document event.

**Specified by:** endDocument

in interface

ContentHandler
**Throws:** SAXException

- The client may throw
an exception during processing.
**See Also:** ContentHandler.startDocument()

- startPrefixMapping

```java
public void startPrefixMapping​(
String
prefix,

String
uri)
throws
SAXException
```

Filter a start Namespace prefix mapping event.

**Specified by:** startPrefixMapping

in interface

ContentHandler
**Parameters:** prefix

- The Namespace prefix.
**Parameters:** uri

- The Namespace URI.
**Throws:** SAXException

- The client may throw
an exception during processing.
**See Also:** ContentHandler.endPrefixMapping(java.lang.String)

,

ContentHandler.startElement(java.lang.String, java.lang.String, java.lang.String, org.xml.sax.Attributes)

- endPrefixMapping

```java
public void endPrefixMapping​(
String
prefix)
throws
SAXException
```

Filter an end Namespace prefix mapping event.

**Specified by:** endPrefixMapping

in interface

ContentHandler
**Parameters:** prefix

- The Namespace prefix.
**Throws:** SAXException

- The client may throw
an exception during processing.
**See Also:** ContentHandler.startPrefixMapping(java.lang.String, java.lang.String)

,

ContentHandler.endElement(java.lang.String, java.lang.String, java.lang.String)

- startElement

```java
public void startElement​(
String
uri,

String
localName,

String
qName,

Attributes
atts)
throws
SAXException
```

Filter a start element event.

**Specified by:** startElement

in interface

ContentHandler
**Parameters:** uri

- The element's Namespace URI, or the empty string.
**Parameters:** localName

- The element's local name, or the empty string.
**Parameters:** qName

- The element's qualified (prefixed) name, or the empty
string.
**Parameters:** atts

- The element's attributes.
**Throws:** SAXException

- The client may throw
an exception during processing.
**See Also:** ContentHandler.endElement(java.lang.String, java.lang.String, java.lang.String)

,

Attributes

,

AttributesImpl

- endElement

```java
public void endElement​(
String
uri,

String
localName,

String
qName)
throws
SAXException
```

Filter an end element event.

**Specified by:** endElement

in interface

ContentHandler
**Parameters:** uri

- The element's Namespace URI, or the empty string.
**Parameters:** localName

- The element's local name, or the empty string.
**Parameters:** qName

- The element's qualified (prefixed) name, or the empty
string.
**Throws:** SAXException

- The client may throw
an exception during processing.

- characters

```java
public void characters​(char[] ch,
int start,
int length)
throws
SAXException
```

Filter a character data event.

**Specified by:** characters

in interface

ContentHandler
**Parameters:** ch

- An array of characters.
**Parameters:** start

- The starting position in the array.
**Parameters:** length

- The number of characters to use from the array.
**Throws:** SAXException

- The client may throw
an exception during processing.
**See Also:** ContentHandler.ignorableWhitespace(char[], int, int)

,

Locator

- ignorableWhitespace

```java
public void ignorableWhitespace​(char[] ch,
int start,
int length)
throws
SAXException
```

Filter an ignorable whitespace event.

**Specified by:** ignorableWhitespace

in interface

ContentHandler
**Parameters:** ch

- An array of characters.
**Parameters:** start

- The starting position in the array.
**Parameters:** length

- The number of characters to use from the array.
**Throws:** SAXException

- The client may throw
an exception during processing.
**See Also:** ContentHandler.characters(char[], int, int)

- processingInstruction

```java
public void processingInstruction​(
String
target,

String
data)
throws
SAXException
```

Filter a processing instruction event.

**Specified by:** processingInstruction

in interface

ContentHandler
**Parameters:** target

- The processing instruction target.
**Parameters:** data

- The text following the target.
**Throws:** SAXException

- The client may throw
an exception during processing.

- skippedEntity

```java
public void skippedEntity​(
String
name)
throws
SAXException
```

Filter a skipped entity event.

**Specified by:** skippedEntity

in interface

ContentHandler
**Parameters:** name

- The name of the skipped entity.
**Throws:** SAXException

- The client may throw
an exception during processing.

- warning

```java
public void warning​(
SAXParseException
e)
throws
SAXException
```

Filter a warning event.

**Specified by:** warning

in interface

ErrorHandler
**Parameters:** e

- The warning as an exception.
**Throws:** SAXException

- The client may throw
an exception during processing.
**See Also:** SAXParseException

- error

```java
public void error​(
SAXParseException
e)
throws
SAXException
```

Filter an error event.

**Specified by:** error

in interface

ErrorHandler
**Parameters:** e

- The error as an exception.
**Throws:** SAXException

- The client may throw
an exception during processing.
**See Also:** SAXParseException

- fatalError

```java
public void fatalError​(
SAXParseException
e)
throws
SAXException
```

Filter a fatal error event.

**Specified by:** fatalError

in interface

ErrorHandler
**Parameters:** e

- The error as an exception.
**Throws:** SAXException

- The client may throw
an exception during processing.
**See Also:** SAXParseException

Constructor Detail

- XMLFilterImpl

```java
public XMLFilterImpl()
```

Construct an empty XML filter, with no parent.

This filter will have no parent: you must assign a parent
before you start a parse or do any configuration with
setFeature or setProperty, unless you use this as a pure event
consumer rather than as an

XMLReader

.

**See Also:** XMLReader.setFeature(java.lang.String, boolean)

,

XMLReader.setProperty(java.lang.String, java.lang.Object)

,

setParent(org.xml.sax.XMLReader)

- XMLFilterImpl

```java
public XMLFilterImpl​(
XMLReader
parent)
```

Construct an XML filter with the specified parent.

**See Also:** setParent(org.xml.sax.XMLReader)

,

getParent()

---

#### Constructor Detail

XMLFilterImpl

```java
public XMLFilterImpl()
```

Construct an empty XML filter, with no parent.

This filter will have no parent: you must assign a parent
before you start a parse or do any configuration with
setFeature or setProperty, unless you use this as a pure event
consumer rather than as an

XMLReader

.

**See Also:** XMLReader.setFeature(java.lang.String, boolean)

,

XMLReader.setProperty(java.lang.String, java.lang.Object)

,

setParent(org.xml.sax.XMLReader)

---

#### XMLFilterImpl

public XMLFilterImpl()

Construct an empty XML filter, with no parent.

This filter will have no parent: you must assign a parent
before you start a parse or do any configuration with
setFeature or setProperty, unless you use this as a pure event
consumer rather than as an

XMLReader

.

This filter will have no parent: you must assign a parent
before you start a parse or do any configuration with
setFeature or setProperty, unless you use this as a pure event
consumer rather than as an

XMLReader

.

XMLFilterImpl

```java
public XMLFilterImpl​(
XMLReader
parent)
```

Construct an XML filter with the specified parent.

**See Also:** setParent(org.xml.sax.XMLReader)

,

getParent()

---

#### XMLFilterImpl

public XMLFilterImpl​(

XMLReader

parent)

Construct an XML filter with the specified parent.

Method Detail

- setParent

```java
public void setParent​(
XMLReader
parent)
```

Set the parent reader.

This is the

XMLReader

from which
this filter will obtain its events and to which it will pass its
configuration requests. The parent may itself be another filter.

If there is no parent reader set, any attempt to parse
or to set or get a feature or property will fail.

**Specified by:** setParent

in interface

XMLFilter
**Parameters:** parent

- The parent XML reader.
**See Also:** getParent()

- getParent

```java
public
XMLReader
getParent()
```

Get the parent reader.

**Specified by:** getParent

in interface

XMLFilter
**Returns:** The parent XML reader, or null if none is set.
**See Also:** setParent(org.xml.sax.XMLReader)

- setFeature

```java
public void setFeature​(
String
name,
boolean value)
throws
SAXNotRecognizedException
,

SAXNotSupportedException
```

Set the value of a feature.

This will always fail if the parent is null.

**Specified by:** setFeature

in interface

XMLReader
**Parameters:** name

- The feature name.
**Parameters:** value

- The requested feature value.
**Throws:** SAXNotRecognizedException

- If the feature
value can't be assigned or retrieved from the parent.
**Throws:** SAXNotSupportedException

- When the
parent recognizes the feature name but
cannot set the requested value.
**See Also:** XMLReader.getFeature(java.lang.String)

- getFeature

```java
public boolean getFeature​(
String
name)
throws
SAXNotRecognizedException
,

SAXNotSupportedException
```

Look up the value of a feature.

This will always fail if the parent is null.

**Specified by:** getFeature

in interface

XMLReader
**Parameters:** name

- The feature name.
**Returns:** The current value of the feature.
**Throws:** SAXNotRecognizedException

- If the feature
value can't be assigned or retrieved from the parent.
**Throws:** SAXNotSupportedException

- When the
parent recognizes the feature name but
cannot determine its value at this time.
**See Also:** XMLReader.setFeature(java.lang.String, boolean)

- setProperty

```java
public void setProperty​(
String
name,

Object
value)
throws
SAXNotRecognizedException
,

SAXNotSupportedException
```

Set the value of a property.

This will always fail if the parent is null.

**Specified by:** setProperty

in interface

XMLReader
**Parameters:** name

- The property name.
**Parameters:** value

- The requested property value.
**Throws:** SAXNotRecognizedException

- If the property
value can't be assigned or retrieved from the parent.
**Throws:** SAXNotSupportedException

- When the
parent recognizes the property name but
cannot set the requested value.

- getProperty

```java
public
Object
getProperty​(
String
name)
throws
SAXNotRecognizedException
,

SAXNotSupportedException
```

Look up the value of a property.

**Specified by:** getProperty

in interface

XMLReader
**Parameters:** name

- The property name.
**Returns:** The current value of the property.
**Throws:** SAXNotRecognizedException

- If the property
value can't be assigned or retrieved from the parent.
**Throws:** SAXNotSupportedException

- When the
parent recognizes the property name but
cannot determine its value at this time.
**See Also:** XMLReader.setProperty(java.lang.String, java.lang.Object)

- setEntityResolver

```java
public void setEntityResolver​(
EntityResolver
resolver)
```

Set the entity resolver.

**Specified by:** setEntityResolver

in interface

XMLReader
**Parameters:** resolver

- The new entity resolver.
**See Also:** XMLReader.getEntityResolver()

- getEntityResolver

```java
public
EntityResolver
getEntityResolver()
```

Get the current entity resolver.

**Specified by:** getEntityResolver

in interface

XMLReader
**Returns:** The current entity resolver, or null if none was set.
**See Also:** XMLReader.setEntityResolver(org.xml.sax.EntityResolver)

- setDTDHandler

```java
public void setDTDHandler​(
DTDHandler
handler)
```

Set the DTD event handler.

**Specified by:** setDTDHandler

in interface

XMLReader
**Parameters:** handler

- the new DTD handler
**See Also:** XMLReader.getDTDHandler()

- getDTDHandler

```java
public
DTDHandler
getDTDHandler()
```

Get the current DTD event handler.

**Specified by:** getDTDHandler

in interface

XMLReader
**Returns:** The current DTD handler, or null if none was set.
**See Also:** XMLReader.setDTDHandler(org.xml.sax.DTDHandler)

- setContentHandler

```java
public void setContentHandler​(
ContentHandler
handler)
```

Set the content event handler.

**Specified by:** setContentHandler

in interface

XMLReader
**Parameters:** handler

- the new content handler
**See Also:** XMLReader.getContentHandler()

- getContentHandler

```java
public
ContentHandler
getContentHandler()
```

Get the content event handler.

**Specified by:** getContentHandler

in interface

XMLReader
**Returns:** The current content handler, or null if none was set.
**See Also:** XMLReader.setContentHandler(org.xml.sax.ContentHandler)

- setErrorHandler

```java
public void setErrorHandler​(
ErrorHandler
handler)
```

Set the error event handler.

**Specified by:** setErrorHandler

in interface

XMLReader
**Parameters:** handler

- the new error handler
**See Also:** XMLReader.getErrorHandler()

- getErrorHandler

```java
public
ErrorHandler
getErrorHandler()
```

Get the current error event handler.

**Specified by:** getErrorHandler

in interface

XMLReader
**Returns:** The current error handler, or null if none was set.
**See Also:** XMLReader.setErrorHandler(org.xml.sax.ErrorHandler)

- parse

```java
public void parse​(
InputSource
input)
throws
SAXException
,

IOException
```

Parse a document.

**Specified by:** parse

in interface

XMLReader
**Parameters:** input

- The input source for the document entity.
**Throws:** SAXException

- Any SAX exception, possibly
wrapping another exception.
**Throws:** IOException

- An IO exception from the parser,
possibly from a byte stream or character stream
supplied by the application.
**See Also:** InputSource

,

XMLReader.parse(java.lang.String)

,

XMLReader.setEntityResolver(org.xml.sax.EntityResolver)

,

XMLReader.setDTDHandler(org.xml.sax.DTDHandler)

,

XMLReader.setContentHandler(org.xml.sax.ContentHandler)

,

XMLReader.setErrorHandler(org.xml.sax.ErrorHandler)

- parse

```java
public void parse​(
String
systemId)
throws
SAXException
,

IOException
```

Parse a document.

**Specified by:** parse

in interface

XMLReader
**Parameters:** systemId

- The system identifier as a fully-qualified URI.
**Throws:** SAXException

- Any SAX exception, possibly
wrapping another exception.
**Throws:** IOException

- An IO exception from the parser,
possibly from a byte stream or character stream
supplied by the application.
**See Also:** XMLReader.parse(org.xml.sax.InputSource)

- resolveEntity

```java
public
InputSource
resolveEntity​(
String
publicId,

String
systemId)
throws
SAXException
,

IOException
```

Filter an external entity resolution.

**Specified by:** resolveEntity

in interface

EntityResolver
**Parameters:** publicId

- The entity's public identifier, or null.
**Parameters:** systemId

- The entity's system identifier.
**Returns:** A new InputSource or null for the default.
**Throws:** SAXException

- The client may throw
an exception during processing.
**Throws:** IOException

- The client may throw an
I/O-related exception while obtaining the
new InputSource.
**See Also:** InputSource

- notationDecl

```java
public void notationDecl​(
String
name,

String
publicId,

String
systemId)
throws
SAXException
```

Filter a notation declaration event.

**Specified by:** notationDecl

in interface

DTDHandler
**Parameters:** name

- The notation name.
**Parameters:** publicId

- The notation's public identifier, or null.
**Parameters:** systemId

- The notation's system identifier, or null.
**Throws:** SAXException

- The client may throw
an exception during processing.
**See Also:** DTDHandler.unparsedEntityDecl(java.lang.String, java.lang.String, java.lang.String, java.lang.String)

,

Attributes

- unparsedEntityDecl

```java
public void unparsedEntityDecl​(
String
name,

String
publicId,

String
systemId,

String
notationName)
throws
SAXException
```

Filter an unparsed entity declaration event.

**Specified by:** unparsedEntityDecl

in interface

DTDHandler
**Parameters:** name

- The entity name.
**Parameters:** publicId

- The entity's public identifier, or null.
**Parameters:** systemId

- The entity's system identifier, or null.
**Parameters:** notationName

- The name of the associated notation.
**Throws:** SAXException

- The client may throw
an exception during processing.
**See Also:** DTDHandler.notationDecl(java.lang.String, java.lang.String, java.lang.String)

,

Attributes

- setDocumentLocator

```java
public void setDocumentLocator​(
Locator
locator)
```

Filter a new document locator event.

**Specified by:** setDocumentLocator

in interface

ContentHandler
**Parameters:** locator

- The document locator.
**See Also:** Locator

- startDocument

```java
public void startDocument()
throws
SAXException
```

Filter a start document event.

**Specified by:** startDocument

in interface

ContentHandler
**Throws:** SAXException

- The client may throw
an exception during processing.
**See Also:** ContentHandler.endDocument()

- endDocument

```java
public void endDocument()
throws
SAXException
```

Filter an end document event.

**Specified by:** endDocument

in interface

ContentHandler
**Throws:** SAXException

- The client may throw
an exception during processing.
**See Also:** ContentHandler.startDocument()

- startPrefixMapping

```java
public void startPrefixMapping​(
String
prefix,

String
uri)
throws
SAXException
```

Filter a start Namespace prefix mapping event.

**Specified by:** startPrefixMapping

in interface

ContentHandler
**Parameters:** prefix

- The Namespace prefix.
**Parameters:** uri

- The Namespace URI.
**Throws:** SAXException

- The client may throw
an exception during processing.
**See Also:** ContentHandler.endPrefixMapping(java.lang.String)

,

ContentHandler.startElement(java.lang.String, java.lang.String, java.lang.String, org.xml.sax.Attributes)

- endPrefixMapping

```java
public void endPrefixMapping​(
String
prefix)
throws
SAXException
```

Filter an end Namespace prefix mapping event.

**Specified by:** endPrefixMapping

in interface

ContentHandler
**Parameters:** prefix

- The Namespace prefix.
**Throws:** SAXException

- The client may throw
an exception during processing.
**See Also:** ContentHandler.startPrefixMapping(java.lang.String, java.lang.String)

,

ContentHandler.endElement(java.lang.String, java.lang.String, java.lang.String)

- startElement

```java
public void startElement​(
String
uri,

String
localName,

String
qName,

Attributes
atts)
throws
SAXException
```

Filter a start element event.

**Specified by:** startElement

in interface

ContentHandler
**Parameters:** uri

- The element's Namespace URI, or the empty string.
**Parameters:** localName

- The element's local name, or the empty string.
**Parameters:** qName

- The element's qualified (prefixed) name, or the empty
string.
**Parameters:** atts

- The element's attributes.
**Throws:** SAXException

- The client may throw
an exception during processing.
**See Also:** ContentHandler.endElement(java.lang.String, java.lang.String, java.lang.String)

,

Attributes

,

AttributesImpl

- endElement

```java
public void endElement​(
String
uri,

String
localName,

String
qName)
throws
SAXException
```

Filter an end element event.

**Specified by:** endElement

in interface

ContentHandler
**Parameters:** uri

- The element's Namespace URI, or the empty string.
**Parameters:** localName

- The element's local name, or the empty string.
**Parameters:** qName

- The element's qualified (prefixed) name, or the empty
string.
**Throws:** SAXException

- The client may throw
an exception during processing.

- characters

```java
public void characters​(char[] ch,
int start,
int length)
throws
SAXException
```

Filter a character data event.

**Specified by:** characters

in interface

ContentHandler
**Parameters:** ch

- An array of characters.
**Parameters:** start

- The starting position in the array.
**Parameters:** length

- The number of characters to use from the array.
**Throws:** SAXException

- The client may throw
an exception during processing.
**See Also:** ContentHandler.ignorableWhitespace(char[], int, int)

,

Locator

- ignorableWhitespace

```java
public void ignorableWhitespace​(char[] ch,
int start,
int length)
throws
SAXException
```

Filter an ignorable whitespace event.

**Specified by:** ignorableWhitespace

in interface

ContentHandler
**Parameters:** ch

- An array of characters.
**Parameters:** start

- The starting position in the array.
**Parameters:** length

- The number of characters to use from the array.
**Throws:** SAXException

- The client may throw
an exception during processing.
**See Also:** ContentHandler.characters(char[], int, int)

- processingInstruction

```java
public void processingInstruction​(
String
target,

String
data)
throws
SAXException
```

Filter a processing instruction event.

**Specified by:** processingInstruction

in interface

ContentHandler
**Parameters:** target

- The processing instruction target.
**Parameters:** data

- The text following the target.
**Throws:** SAXException

- The client may throw
an exception during processing.

- skippedEntity

```java
public void skippedEntity​(
String
name)
throws
SAXException
```

Filter a skipped entity event.

**Specified by:** skippedEntity

in interface

ContentHandler
**Parameters:** name

- The name of the skipped entity.
**Throws:** SAXException

- The client may throw
an exception during processing.

- warning

```java
public void warning​(
SAXParseException
e)
throws
SAXException
```

Filter a warning event.

**Specified by:** warning

in interface

ErrorHandler
**Parameters:** e

- The warning as an exception.
**Throws:** SAXException

- The client may throw
an exception during processing.
**See Also:** SAXParseException

- error

```java
public void error​(
SAXParseException
e)
throws
SAXException
```

Filter an error event.

**Specified by:** error

in interface

ErrorHandler
**Parameters:** e

- The error as an exception.
**Throws:** SAXException

- The client may throw
an exception during processing.
**See Also:** SAXParseException

- fatalError

```java
public void fatalError​(
SAXParseException
e)
throws
SAXException
```

Filter a fatal error event.

**Specified by:** fatalError

in interface

ErrorHandler
**Parameters:** e

- The error as an exception.
**Throws:** SAXException

- The client may throw
an exception during processing.
**See Also:** SAXParseException

---

#### Method Detail

setParent

```java
public void setParent​(
XMLReader
parent)
```

Set the parent reader.

This is the

XMLReader

from which
this filter will obtain its events and to which it will pass its
configuration requests. The parent may itself be another filter.

If there is no parent reader set, any attempt to parse
or to set or get a feature or property will fail.

**Specified by:** setParent

in interface

XMLFilter
**Parameters:** parent

- The parent XML reader.
**See Also:** getParent()

---

#### setParent

public void setParent​(

XMLReader

parent)

Set the parent reader.

This is the

XMLReader

from which
this filter will obtain its events and to which it will pass its
configuration requests. The parent may itself be another filter.

If there is no parent reader set, any attempt to parse
or to set or get a feature or property will fail.

This is the

XMLReader

from which
this filter will obtain its events and to which it will pass its
configuration requests. The parent may itself be another filter.

If there is no parent reader set, any attempt to parse
or to set or get a feature or property will fail.

getParent

```java
public
XMLReader
getParent()
```

Get the parent reader.

**Specified by:** getParent

in interface

XMLFilter
**Returns:** The parent XML reader, or null if none is set.
**See Also:** setParent(org.xml.sax.XMLReader)

---

#### getParent

public

XMLReader

getParent()

Get the parent reader.

setFeature

```java
public void setFeature​(
String
name,
boolean value)
throws
SAXNotRecognizedException
,

SAXNotSupportedException
```

Set the value of a feature.

This will always fail if the parent is null.

**Specified by:** setFeature

in interface

XMLReader
**Parameters:** name

- The feature name.
**Parameters:** value

- The requested feature value.
**Throws:** SAXNotRecognizedException

- If the feature
value can't be assigned or retrieved from the parent.
**Throws:** SAXNotSupportedException

- When the
parent recognizes the feature name but
cannot set the requested value.
**See Also:** XMLReader.getFeature(java.lang.String)

---

#### setFeature

public void setFeature​(

String

name,
boolean value)
throws

SAXNotRecognizedException

,

SAXNotSupportedException

Set the value of a feature.

This will always fail if the parent is null.

This will always fail if the parent is null.

getFeature

```java
public boolean getFeature​(
String
name)
throws
SAXNotRecognizedException
,

SAXNotSupportedException
```

Look up the value of a feature.

This will always fail if the parent is null.

**Specified by:** getFeature

in interface

XMLReader
**Parameters:** name

- The feature name.
**Returns:** The current value of the feature.
**Throws:** SAXNotRecognizedException

- If the feature
value can't be assigned or retrieved from the parent.
**Throws:** SAXNotSupportedException

- When the
parent recognizes the feature name but
cannot determine its value at this time.
**See Also:** XMLReader.setFeature(java.lang.String, boolean)

---

#### getFeature

public boolean getFeature​(

String

name)
throws

SAXNotRecognizedException

,

SAXNotSupportedException

Look up the value of a feature.

This will always fail if the parent is null.

This will always fail if the parent is null.

setProperty

```java
public void setProperty​(
String
name,

Object
value)
throws
SAXNotRecognizedException
,

SAXNotSupportedException
```

Set the value of a property.

This will always fail if the parent is null.

**Specified by:** setProperty

in interface

XMLReader
**Parameters:** name

- The property name.
**Parameters:** value

- The requested property value.
**Throws:** SAXNotRecognizedException

- If the property
value can't be assigned or retrieved from the parent.
**Throws:** SAXNotSupportedException

- When the
parent recognizes the property name but
cannot set the requested value.

---

#### setProperty

public void setProperty​(

String

name,

Object

value)
throws

SAXNotRecognizedException

,

SAXNotSupportedException

Set the value of a property.

This will always fail if the parent is null.

This will always fail if the parent is null.

getProperty

```java
public
Object
getProperty​(
String
name)
throws
SAXNotRecognizedException
,

SAXNotSupportedException
```

Look up the value of a property.

**Specified by:** getProperty

in interface

XMLReader
**Parameters:** name

- The property name.
**Returns:** The current value of the property.
**Throws:** SAXNotRecognizedException

- If the property
value can't be assigned or retrieved from the parent.
**Throws:** SAXNotSupportedException

- When the
parent recognizes the property name but
cannot determine its value at this time.
**See Also:** XMLReader.setProperty(java.lang.String, java.lang.Object)

---

#### getProperty

public

Object

getProperty​(

String

name)
throws

SAXNotRecognizedException

,

SAXNotSupportedException

Look up the value of a property.

setEntityResolver

```java
public void setEntityResolver​(
EntityResolver
resolver)
```

Set the entity resolver.

**Specified by:** setEntityResolver

in interface

XMLReader
**Parameters:** resolver

- The new entity resolver.
**See Also:** XMLReader.getEntityResolver()

---

#### setEntityResolver

public void setEntityResolver​(

EntityResolver

resolver)

Set the entity resolver.

getEntityResolver

```java
public
EntityResolver
getEntityResolver()
```

Get the current entity resolver.

**Specified by:** getEntityResolver

in interface

XMLReader
**Returns:** The current entity resolver, or null if none was set.
**See Also:** XMLReader.setEntityResolver(org.xml.sax.EntityResolver)

---

#### getEntityResolver

public

EntityResolver

getEntityResolver()

Get the current entity resolver.

setDTDHandler

```java
public void setDTDHandler​(
DTDHandler
handler)
```

Set the DTD event handler.

**Specified by:** setDTDHandler

in interface

XMLReader
**Parameters:** handler

- the new DTD handler
**See Also:** XMLReader.getDTDHandler()

---

#### setDTDHandler

public void setDTDHandler​(

DTDHandler

handler)

Set the DTD event handler.

getDTDHandler

```java
public
DTDHandler
getDTDHandler()
```

Get the current DTD event handler.

**Specified by:** getDTDHandler

in interface

XMLReader
**Returns:** The current DTD handler, or null if none was set.
**See Also:** XMLReader.setDTDHandler(org.xml.sax.DTDHandler)

---

#### getDTDHandler

public

DTDHandler

getDTDHandler()

Get the current DTD event handler.

setContentHandler

```java
public void setContentHandler​(
ContentHandler
handler)
```

Set the content event handler.

**Specified by:** setContentHandler

in interface

XMLReader
**Parameters:** handler

- the new content handler
**See Also:** XMLReader.getContentHandler()

---

#### setContentHandler

public void setContentHandler​(

ContentHandler

handler)

Set the content event handler.

getContentHandler

```java
public
ContentHandler
getContentHandler()
```

Get the content event handler.

**Specified by:** getContentHandler

in interface

XMLReader
**Returns:** The current content handler, or null if none was set.
**See Also:** XMLReader.setContentHandler(org.xml.sax.ContentHandler)

---

#### getContentHandler

public

ContentHandler

getContentHandler()

Get the content event handler.

setErrorHandler

```java
public void setErrorHandler​(
ErrorHandler
handler)
```

Set the error event handler.

**Specified by:** setErrorHandler

in interface

XMLReader
**Parameters:** handler

- the new error handler
**See Also:** XMLReader.getErrorHandler()

---

#### setErrorHandler

public void setErrorHandler​(

ErrorHandler

handler)

Set the error event handler.

getErrorHandler

```java
public
ErrorHandler
getErrorHandler()
```

Get the current error event handler.

**Specified by:** getErrorHandler

in interface

XMLReader
**Returns:** The current error handler, or null if none was set.
**See Also:** XMLReader.setErrorHandler(org.xml.sax.ErrorHandler)

---

#### getErrorHandler

public

ErrorHandler

getErrorHandler()

Get the current error event handler.

parse

```java
public void parse​(
InputSource
input)
throws
SAXException
,

IOException
```

Parse a document.

**Specified by:** parse

in interface

XMLReader
**Parameters:** input

- The input source for the document entity.
**Throws:** SAXException

- Any SAX exception, possibly
wrapping another exception.
**Throws:** IOException

- An IO exception from the parser,
possibly from a byte stream or character stream
supplied by the application.
**See Also:** InputSource

,

XMLReader.parse(java.lang.String)

,

XMLReader.setEntityResolver(org.xml.sax.EntityResolver)

,

XMLReader.setDTDHandler(org.xml.sax.DTDHandler)

,

XMLReader.setContentHandler(org.xml.sax.ContentHandler)

,

XMLReader.setErrorHandler(org.xml.sax.ErrorHandler)

---

#### parse

public void parse​(

InputSource

input)
throws

SAXException

,

IOException

Parse a document.

parse

```java
public void parse​(
String
systemId)
throws
SAXException
,

IOException
```

Parse a document.

**Specified by:** parse

in interface

XMLReader
**Parameters:** systemId

- The system identifier as a fully-qualified URI.
**Throws:** SAXException

- Any SAX exception, possibly
wrapping another exception.
**Throws:** IOException

- An IO exception from the parser,
possibly from a byte stream or character stream
supplied by the application.
**See Also:** XMLReader.parse(org.xml.sax.InputSource)

---

#### parse

public void parse​(

String

systemId)
throws

SAXException

,

IOException

Parse a document.

resolveEntity

```java
public
InputSource
resolveEntity​(
String
publicId,

String
systemId)
throws
SAXException
,

IOException
```

Filter an external entity resolution.

**Specified by:** resolveEntity

in interface

EntityResolver
**Parameters:** publicId

- The entity's public identifier, or null.
**Parameters:** systemId

- The entity's system identifier.
**Returns:** A new InputSource or null for the default.
**Throws:** SAXException

- The client may throw
an exception during processing.
**Throws:** IOException

- The client may throw an
I/O-related exception while obtaining the
new InputSource.
**See Also:** InputSource

---

#### resolveEntity

public

InputSource

resolveEntity​(

String

publicId,

String

systemId)
throws

SAXException

,

IOException

Filter an external entity resolution.

notationDecl

```java
public void notationDecl​(
String
name,

String
publicId,

String
systemId)
throws
SAXException
```

Filter a notation declaration event.

**Specified by:** notationDecl

in interface

DTDHandler
**Parameters:** name

- The notation name.
**Parameters:** publicId

- The notation's public identifier, or null.
**Parameters:** systemId

- The notation's system identifier, or null.
**Throws:** SAXException

- The client may throw
an exception during processing.
**See Also:** DTDHandler.unparsedEntityDecl(java.lang.String, java.lang.String, java.lang.String, java.lang.String)

,

Attributes

---

#### notationDecl

public void notationDecl​(

String

name,

String

publicId,

String

systemId)
throws

SAXException

Filter a notation declaration event.

unparsedEntityDecl

```java
public void unparsedEntityDecl​(
String
name,

String
publicId,

String
systemId,

String
notationName)
throws
SAXException
```

Filter an unparsed entity declaration event.

**Specified by:** unparsedEntityDecl

in interface

DTDHandler
**Parameters:** name

- The entity name.
**Parameters:** publicId

- The entity's public identifier, or null.
**Parameters:** systemId

- The entity's system identifier, or null.
**Parameters:** notationName

- The name of the associated notation.
**Throws:** SAXException

- The client may throw
an exception during processing.
**See Also:** DTDHandler.notationDecl(java.lang.String, java.lang.String, java.lang.String)

,

Attributes

---

#### unparsedEntityDecl

public void unparsedEntityDecl​(

String

name,

String

publicId,

String

systemId,

String

notationName)
throws

SAXException

Filter an unparsed entity declaration event.

setDocumentLocator

```java
public void setDocumentLocator​(
Locator
locator)
```

Filter a new document locator event.

**Specified by:** setDocumentLocator

in interface

ContentHandler
**Parameters:** locator

- The document locator.
**See Also:** Locator

---

#### setDocumentLocator

public void setDocumentLocator​(

Locator

locator)

Filter a new document locator event.

startDocument

```java
public void startDocument()
throws
SAXException
```

Filter a start document event.

**Specified by:** startDocument

in interface

ContentHandler
**Throws:** SAXException

- The client may throw
an exception during processing.
**See Also:** ContentHandler.endDocument()

---

#### startDocument

public void startDocument()
throws

SAXException

Filter a start document event.

endDocument

```java
public void endDocument()
throws
SAXException
```

Filter an end document event.

**Specified by:** endDocument

in interface

ContentHandler
**Throws:** SAXException

- The client may throw
an exception during processing.
**See Also:** ContentHandler.startDocument()

---

#### endDocument

public void endDocument()
throws

SAXException

Filter an end document event.

startPrefixMapping

```java
public void startPrefixMapping​(
String
prefix,

String
uri)
throws
SAXException
```

Filter a start Namespace prefix mapping event.

**Specified by:** startPrefixMapping

in interface

ContentHandler
**Parameters:** prefix

- The Namespace prefix.
**Parameters:** uri

- The Namespace URI.
**Throws:** SAXException

- The client may throw
an exception during processing.
**See Also:** ContentHandler.endPrefixMapping(java.lang.String)

,

ContentHandler.startElement(java.lang.String, java.lang.String, java.lang.String, org.xml.sax.Attributes)

---

#### startPrefixMapping

public void startPrefixMapping​(

String

prefix,

String

uri)
throws

SAXException

Filter a start Namespace prefix mapping event.

endPrefixMapping

```java
public void endPrefixMapping​(
String
prefix)
throws
SAXException
```

Filter an end Namespace prefix mapping event.

**Specified by:** endPrefixMapping

in interface

ContentHandler
**Parameters:** prefix

- The Namespace prefix.
**Throws:** SAXException

- The client may throw
an exception during processing.
**See Also:** ContentHandler.startPrefixMapping(java.lang.String, java.lang.String)

,

ContentHandler.endElement(java.lang.String, java.lang.String, java.lang.String)

---

#### endPrefixMapping

public void endPrefixMapping​(

String

prefix)
throws

SAXException

Filter an end Namespace prefix mapping event.

startElement

```java
public void startElement​(
String
uri,

String
localName,

String
qName,

Attributes
atts)
throws
SAXException
```

Filter a start element event.

**Specified by:** startElement

in interface

ContentHandler
**Parameters:** uri

- The element's Namespace URI, or the empty string.
**Parameters:** localName

- The element's local name, or the empty string.
**Parameters:** qName

- The element's qualified (prefixed) name, or the empty
string.
**Parameters:** atts

- The element's attributes.
**Throws:** SAXException

- The client may throw
an exception during processing.
**See Also:** ContentHandler.endElement(java.lang.String, java.lang.String, java.lang.String)

,

Attributes

,

AttributesImpl

---

#### startElement

public void startElement​(

String

uri,

String

localName,

String

qName,

Attributes

atts)
throws

SAXException

Filter a start element event.

endElement

```java
public void endElement​(
String
uri,

String
localName,

String
qName)
throws
SAXException
```

Filter an end element event.

**Specified by:** endElement

in interface

ContentHandler
**Parameters:** uri

- The element's Namespace URI, or the empty string.
**Parameters:** localName

- The element's local name, or the empty string.
**Parameters:** qName

- The element's qualified (prefixed) name, or the empty
string.
**Throws:** SAXException

- The client may throw
an exception during processing.

---

#### endElement

public void endElement​(

String

uri,

String

localName,

String

qName)
throws

SAXException

Filter an end element event.

characters

```java
public void characters​(char[] ch,
int start,
int length)
throws
SAXException
```

Filter a character data event.

**Specified by:** characters

in interface

ContentHandler
**Parameters:** ch

- An array of characters.
**Parameters:** start

- The starting position in the array.
**Parameters:** length

- The number of characters to use from the array.
**Throws:** SAXException

- The client may throw
an exception during processing.
**See Also:** ContentHandler.ignorableWhitespace(char[], int, int)

,

Locator

---

#### characters

public void characters​(char[] ch,
int start,
int length)
throws

SAXException

Filter a character data event.

ignorableWhitespace

```java
public void ignorableWhitespace​(char[] ch,
int start,
int length)
throws
SAXException
```

Filter an ignorable whitespace event.

**Specified by:** ignorableWhitespace

in interface

ContentHandler
**Parameters:** ch

- An array of characters.
**Parameters:** start

- The starting position in the array.
**Parameters:** length

- The number of characters to use from the array.
**Throws:** SAXException

- The client may throw
an exception during processing.
**See Also:** ContentHandler.characters(char[], int, int)

---

#### ignorableWhitespace

public void ignorableWhitespace​(char[] ch,
int start,
int length)
throws

SAXException

Filter an ignorable whitespace event.

processingInstruction

```java
public void processingInstruction​(
String
target,

String
data)
throws
SAXException
```

Filter a processing instruction event.

**Specified by:** processingInstruction

in interface

ContentHandler
**Parameters:** target

- The processing instruction target.
**Parameters:** data

- The text following the target.
**Throws:** SAXException

- The client may throw
an exception during processing.

---

#### processingInstruction

public void processingInstruction​(

String

target,

String

data)
throws

SAXException

Filter a processing instruction event.

skippedEntity

```java
public void skippedEntity​(
String
name)
throws
SAXException
```

Filter a skipped entity event.

**Specified by:** skippedEntity

in interface

ContentHandler
**Parameters:** name

- The name of the skipped entity.
**Throws:** SAXException

- The client may throw
an exception during processing.

---

#### skippedEntity

public void skippedEntity​(

String

name)
throws

SAXException

Filter a skipped entity event.

warning

```java
public void warning​(
SAXParseException
e)
throws
SAXException
```

Filter a warning event.

**Specified by:** warning

in interface

ErrorHandler
**Parameters:** e

- The warning as an exception.
**Throws:** SAXException

- The client may throw
an exception during processing.
**See Also:** SAXParseException

---

#### warning

public void warning​(

SAXParseException

e)
throws

SAXException

Filter a warning event.

error

```java
public void error​(
SAXParseException
e)
throws
SAXException
```

Filter an error event.

**Specified by:** error

in interface

ErrorHandler
**Parameters:** e

- The error as an exception.
**Throws:** SAXException

- The client may throw
an exception during processing.
**See Also:** SAXParseException

---

#### error

public void error​(

SAXParseException

e)
throws

SAXException

Filter an error event.

fatalError

```java
public void fatalError​(
SAXParseException
e)
throws
SAXException
```

Filter a fatal error event.

**Specified by:** fatalError

in interface

ErrorHandler
**Parameters:** e

- The error as an exception.
**Throws:** SAXException

- The client may throw
an exception during processing.
**See Also:** SAXParseException

---

#### fatalError

public void fatalError​(

SAXParseException

e)
throws

SAXException

Filter a fatal error event.

---

