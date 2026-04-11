# Class XMLReaderAdapter

**Source:** `java.xml\org\xml\sax\helpers\XMLReaderAdapter.html`

### Class Description

```java
public class
XMLReaderAdapter

extends
Object

implements
Parser
,
ContentHandler
```

Adapt a SAX2 XMLReader as a SAX1 Parser.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

This class wraps a SAX2

XMLReader

and makes it act as a SAX1

Parser

. The XMLReader
must support a true value for the
http://xml.org/sax/features/namespace-prefixes property or parsing will fail
with a

SAXException

; if the XMLReader
supports a false value for the http://xml.org/sax/features/namespaces
property, that will also be used to improve efficiency.

**All Implemented Interfaces:** ContentHandler

,

Parser

---

### Field Details

*No entries found.*

### Constructor Details

#### public XMLReaderAdapter()
throws
SAXException

Create a new adapter.

Use the "org.xml.sax.driver" property to locate the SAX2
driver to embed.

**Throws:**
- SAXException

- If the embedded driver
cannot be instantiated or if the
org.xml.sax.driver property is not specified.

---

#### public XMLReaderAdapter​(
XMLReader
xmlReader)

Create a new adapter.

Create a new adapter, wrapped around a SAX2 XMLReader.
The adapter will make the XMLReader act like a SAX1
Parser.

**Parameters:**
- xmlReader

- The SAX2 XMLReader to wrap.

**Throws:**
- NullPointerException

- If the argument is null.

---

### Method Details

#### public void setLocale​(
Locale
locale)
throws
SAXException

Set the locale for error reporting.

This is not supported in SAX2, and will always throw
an exception.

**Specified by:**
- setLocale

in interface

Parser

**Parameters:**
- locale

- the locale for error reporting.

**Throws:**
- SAXException

- Thrown unless overridden.

**See Also:**
- Parser.setLocale(java.util.Locale)

---

#### public void setEntityResolver​(
EntityResolver
resolver)

Register the entity resolver.

**Specified by:**
- setEntityResolver

in interface

Parser

**Parameters:**
- resolver

- The new resolver.

**See Also:**
- Parser.setEntityResolver(org.xml.sax.EntityResolver)

---

#### public void setDTDHandler​(
DTDHandler
handler)

Register the DTD event handler.

**Specified by:**
- setDTDHandler

in interface

Parser

**Parameters:**
- handler

- The new DTD event handler.

**See Also:**
- Parser.setDTDHandler(org.xml.sax.DTDHandler)

---

#### public void setDocumentHandler​(
DocumentHandler
handler)

Register the SAX1 document event handler.

Note that the SAX1 document handler has no Namespace
support.

**Specified by:**
- setDocumentHandler

in interface

Parser

**Parameters:**
- handler

- The new SAX1 document event handler.

**See Also:**
- Parser.setDocumentHandler(org.xml.sax.DocumentHandler)

---

#### public void setErrorHandler​(
ErrorHandler
handler)

Register the error event handler.

**Specified by:**
- setErrorHandler

in interface

Parser

**Parameters:**
- handler

- The new error event handler.

**See Also:**
- Parser.setErrorHandler(org.xml.sax.ErrorHandler)

---

#### public void parse​(
String
systemId)
throws
IOException
,

SAXException

Parse the document.

This method will throw an exception if the embedded
XMLReader does not support the
http://xml.org/sax/features/namespace-prefixes property.

**Specified by:**
- parse

in interface

Parser

**Parameters:**
- systemId

- The absolute URL of the document.

**Throws:**
- IOException

- If there is a problem reading
the raw content of the document.
- SAXException

- If there is a problem
processing the document.

**See Also:**
- parse(org.xml.sax.InputSource)

,

Parser.parse(java.lang.String)

---

#### public void parse​(
InputSource
input)
throws
IOException
,

SAXException

Parse the document.

This method will throw an exception if the embedded
XMLReader does not support the
http://xml.org/sax/features/namespace-prefixes property.

**Specified by:**
- parse

in interface

Parser

**Parameters:**
- input

- An input source for the document.

**Throws:**
- IOException

- If there is a problem reading
the raw content of the document.
- SAXException

- If there is a problem
processing the document.

**See Also:**
- parse(java.lang.String)

,

Parser.parse(org.xml.sax.InputSource)

---

#### public void setDocumentLocator​(
Locator
locator)

Set a document locator.

**Specified by:**
- setDocumentLocator

in interface

ContentHandler

**Parameters:**
- locator

- The document locator.

**See Also:**
- ContentHandler.setDocumentLocator(org.xml.sax.Locator)

---

#### public void startDocument()
throws
SAXException

Start document event.

**Specified by:**
- startDocument

in interface

ContentHandler

**Throws:**
- SAXException

- The client may raise a
processing exception.

**See Also:**
- ContentHandler.startDocument()

---

#### public void endDocument()
throws
SAXException

End document event.

**Specified by:**
- endDocument

in interface

ContentHandler

**Throws:**
- SAXException

- The client may raise a
processing exception.

**See Also:**
- ContentHandler.endDocument()

---

#### public void startPrefixMapping​(
String
prefix,

String
uri)

Adapt a SAX2 start prefix mapping event.

**Specified by:**
- startPrefixMapping

in interface

ContentHandler

**Parameters:**
- prefix

- The prefix being mapped.
- uri

- The Namespace URI being mapped to.

**See Also:**
- ContentHandler.startPrefixMapping(java.lang.String, java.lang.String)

---

#### public void endPrefixMapping​(
String
prefix)

Adapt a SAX2 end prefix mapping event.

**Specified by:**
- endPrefixMapping

in interface

ContentHandler

**Parameters:**
- prefix

- The prefix being mapped.

**See Also:**
- ContentHandler.endPrefixMapping(java.lang.String)

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

Adapt a SAX2 start element event.

**Specified by:**
- startElement

in interface

ContentHandler

**Parameters:**
- uri

- The Namespace URI.
- localName

- The Namespace local name.
- qName

- The qualified (prefixed) name.
- atts

- The SAX2 attributes.

**Throws:**
- SAXException

- The client may raise a
processing exception.

**See Also:**
- ContentHandler.endDocument()

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

Adapt a SAX2 end element event.

**Specified by:**
- endElement

in interface

ContentHandler

**Parameters:**
- uri

- The Namespace URI.
- localName

- The Namespace local name.
- qName

- The qualified (prefixed) name.

**Throws:**
- SAXException

- The client may raise a
processing exception.

**See Also:**
- ContentHandler.endElement(java.lang.String, java.lang.String, java.lang.String)

---

#### public void characters​(char[] ch,
int start,
int length)
throws
SAXException

Adapt a SAX2 characters event.

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

- The number of characters to use.

**Throws:**
- SAXException

- The client may raise a
processing exception.

**See Also:**
- ContentHandler.characters(char[], int, int)

---

#### public void ignorableWhitespace​(char[] ch,
int start,
int length)
throws
SAXException

Adapt a SAX2 ignorable whitespace event.

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

- The number of characters to use.

**Throws:**
- SAXException

- The client may raise a
processing exception.

**See Also:**
- ContentHandler.ignorableWhitespace(char[], int, int)

---

#### public void processingInstruction​(
String
target,

String
data)
throws
SAXException

Adapt a SAX2 processing instruction event.

**Specified by:**
- processingInstruction

in interface

ContentHandler

**Parameters:**
- target

- The processing instruction target.
- data

- The remainder of the processing instruction

**Throws:**
- SAXException

- The client may raise a
processing exception.

**See Also:**
- ContentHandler.processingInstruction(java.lang.String, java.lang.String)

---

#### public void skippedEntity​(
String
name)
throws
SAXException

Adapt a SAX2 skipped entity event.

**Specified by:**
- skippedEntity

in interface

ContentHandler

**Parameters:**
- name

- The name of the skipped entity.

**Throws:**
- SAXException

- Throwable by subclasses.

**See Also:**
- ContentHandler.skippedEntity(java.lang.String)

---

### Additional Sections

#### Class XMLReaderAdapter

java.lang.Object

- org.xml.sax.helpers.XMLReaderAdapter

org.xml.sax.helpers.XMLReaderAdapter

**All Implemented Interfaces:** ContentHandler

,

Parser

```java
public class
XMLReaderAdapter

extends
Object

implements
Parser
,
ContentHandler
```

Adapt a SAX2 XMLReader as a SAX1 Parser.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

This class wraps a SAX2

XMLReader

and makes it act as a SAX1

Parser

. The XMLReader
must support a true value for the
http://xml.org/sax/features/namespace-prefixes property or parsing will fail
with a

SAXException

; if the XMLReader
supports a false value for the http://xml.org/sax/features/namespaces
property, that will also be used to improve efficiency.

**Since:** 1.4, SAX 2.0
**See Also:** Parser

,

XMLReader

public class

XMLReaderAdapter

extends

Object

implements

Parser

,

ContentHandler

Adapt a SAX2 XMLReader as a SAX1 Parser.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

This class wraps a SAX2

XMLReader

and makes it act as a SAX1

Parser

. The XMLReader
must support a true value for the
http://xml.org/sax/features/namespace-prefixes property or parsing will fail
with a

SAXException

; if the XMLReader
supports a false value for the http://xml.org/sax/features/namespaces
property, that will also be used to improve efficiency.

This class wraps a SAX2

XMLReader

and makes it act as a SAX1

Parser

. The XMLReader
must support a true value for the
http://xml.org/sax/features/namespace-prefixes property or parsing will fail
with a

SAXException

; if the XMLReader
supports a false value for the http://xml.org/sax/features/namespaces
property, that will also be used to improve efficiency.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

XMLReaderAdapter

()

Create a new adapter.

XMLReaderAdapter

​(

XMLReader

xmlReader)

Create a new adapter.

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

Adapt a SAX2 characters event.

void

endDocument

()

End document event.

void

endElement

​(

String

uri,

String

localName,

String

qName)

Adapt a SAX2 end element event.

void

endPrefixMapping

​(

String

prefix)

Adapt a SAX2 end prefix mapping event.

void

ignorableWhitespace

​(char[] ch,
int start,
int length)

Adapt a SAX2 ignorable whitespace event.

void

parse

​(

String

systemId)

Parse the document.

void

parse

​(

InputSource

input)

Parse the document.

void

processingInstruction

​(

String

target,

String

data)

Adapt a SAX2 processing instruction event.

void

setDocumentHandler

​(

DocumentHandler

handler)

Register the SAX1 document event handler.

void

setDocumentLocator

​(

Locator

locator)

Set a document locator.

void

setDTDHandler

​(

DTDHandler

handler)

Register the DTD event handler.

void

setEntityResolver

​(

EntityResolver

resolver)

Register the entity resolver.

void

setErrorHandler

​(

ErrorHandler

handler)

Register the error event handler.

void

setLocale

​(

Locale

locale)

Set the locale for error reporting.

void

skippedEntity

​(

String

name)

Adapt a SAX2 skipped entity event.

void

startDocument

()

Start document event.

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

Adapt a SAX2 start element event.

void

startPrefixMapping

​(

String

prefix,

String

uri)

Adapt a SAX2 start prefix mapping event.

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

XMLReaderAdapter

()

Create a new adapter.

XMLReaderAdapter

​(

XMLReader

xmlReader)

Create a new adapter.

---

#### Constructor Summary

Create a new adapter.

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

Adapt a SAX2 characters event.

void

endDocument

()

End document event.

void

endElement

​(

String

uri,

String

localName,

String

qName)

Adapt a SAX2 end element event.

void

endPrefixMapping

​(

String

prefix)

Adapt a SAX2 end prefix mapping event.

void

ignorableWhitespace

​(char[] ch,
int start,
int length)

Adapt a SAX2 ignorable whitespace event.

void

parse

​(

String

systemId)

Parse the document.

void

parse

​(

InputSource

input)

Parse the document.

void

processingInstruction

​(

String

target,

String

data)

Adapt a SAX2 processing instruction event.

void

setDocumentHandler

​(

DocumentHandler

handler)

Register the SAX1 document event handler.

void

setDocumentLocator

​(

Locator

locator)

Set a document locator.

void

setDTDHandler

​(

DTDHandler

handler)

Register the DTD event handler.

void

setEntityResolver

​(

EntityResolver

resolver)

Register the entity resolver.

void

setErrorHandler

​(

ErrorHandler

handler)

Register the error event handler.

void

setLocale

​(

Locale

locale)

Set the locale for error reporting.

void

skippedEntity

​(

String

name)

Adapt a SAX2 skipped entity event.

void

startDocument

()

Start document event.

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

Adapt a SAX2 start element event.

void

startPrefixMapping

​(

String

prefix,

String

uri)

Adapt a SAX2 start prefix mapping event.

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

Adapt a SAX2 characters event.

End document event.

Adapt a SAX2 end element event.

Adapt a SAX2 end prefix mapping event.

Adapt a SAX2 ignorable whitespace event.

Parse the document.

Adapt a SAX2 processing instruction event.

Register the SAX1 document event handler.

Set a document locator.

Register the DTD event handler.

Register the entity resolver.

Register the error event handler.

Set the locale for error reporting.

Adapt a SAX2 skipped entity event.

Start document event.

Adapt a SAX2 start element event.

Adapt a SAX2 start prefix mapping event.

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

- XMLReaderAdapter

```java
public XMLReaderAdapter()
throws
SAXException
```

Create a new adapter.

Use the "org.xml.sax.driver" property to locate the SAX2
driver to embed.

**Throws:** SAXException

- If the embedded driver
cannot be instantiated or if the
org.xml.sax.driver property is not specified.

- XMLReaderAdapter

```java
public XMLReaderAdapter​(
XMLReader
xmlReader)
```

Create a new adapter.

Create a new adapter, wrapped around a SAX2 XMLReader.
The adapter will make the XMLReader act like a SAX1
Parser.

**Parameters:** xmlReader

- The SAX2 XMLReader to wrap.
**Throws:** NullPointerException

- If the argument is null.

============ METHOD DETAIL ==========

- Method Detail

- setLocale

```java
public void setLocale​(
Locale
locale)
throws
SAXException
```

Set the locale for error reporting.

This is not supported in SAX2, and will always throw
an exception.

**Specified by:** setLocale

in interface

Parser
**Parameters:** locale

- the locale for error reporting.
**Throws:** SAXException

- Thrown unless overridden.
**See Also:** Parser.setLocale(java.util.Locale)

- setEntityResolver

```java
public void setEntityResolver​(
EntityResolver
resolver)
```

Register the entity resolver.

**Specified by:** setEntityResolver

in interface

Parser
**Parameters:** resolver

- The new resolver.
**See Also:** Parser.setEntityResolver(org.xml.sax.EntityResolver)

- setDTDHandler

```java
public void setDTDHandler​(
DTDHandler
handler)
```

Register the DTD event handler.

**Specified by:** setDTDHandler

in interface

Parser
**Parameters:** handler

- The new DTD event handler.
**See Also:** Parser.setDTDHandler(org.xml.sax.DTDHandler)

- setDocumentHandler

```java
public void setDocumentHandler​(
DocumentHandler
handler)
```

Register the SAX1 document event handler.

Note that the SAX1 document handler has no Namespace
support.

**Specified by:** setDocumentHandler

in interface

Parser
**Parameters:** handler

- The new SAX1 document event handler.
**See Also:** Parser.setDocumentHandler(org.xml.sax.DocumentHandler)

- setErrorHandler

```java
public void setErrorHandler​(
ErrorHandler
handler)
```

Register the error event handler.

**Specified by:** setErrorHandler

in interface

Parser
**Parameters:** handler

- The new error event handler.
**See Also:** Parser.setErrorHandler(org.xml.sax.ErrorHandler)

- parse

```java
public void parse​(
String
systemId)
throws
IOException
,

SAXException
```

Parse the document.

This method will throw an exception if the embedded
XMLReader does not support the
http://xml.org/sax/features/namespace-prefixes property.

**Specified by:** parse

in interface

Parser
**Parameters:** systemId

- The absolute URL of the document.
**Throws:** IOException

- If there is a problem reading
the raw content of the document.
**Throws:** SAXException

- If there is a problem
processing the document.
**See Also:** parse(org.xml.sax.InputSource)

,

Parser.parse(java.lang.String)

- parse

```java
public void parse​(
InputSource
input)
throws
IOException
,

SAXException
```

Parse the document.

This method will throw an exception if the embedded
XMLReader does not support the
http://xml.org/sax/features/namespace-prefixes property.

**Specified by:** parse

in interface

Parser
**Parameters:** input

- An input source for the document.
**Throws:** IOException

- If there is a problem reading
the raw content of the document.
**Throws:** SAXException

- If there is a problem
processing the document.
**See Also:** parse(java.lang.String)

,

Parser.parse(org.xml.sax.InputSource)

- setDocumentLocator

```java
public void setDocumentLocator​(
Locator
locator)
```

Set a document locator.

**Specified by:** setDocumentLocator

in interface

ContentHandler
**Parameters:** locator

- The document locator.
**See Also:** ContentHandler.setDocumentLocator(org.xml.sax.Locator)

- startDocument

```java
public void startDocument()
throws
SAXException
```

Start document event.

**Specified by:** startDocument

in interface

ContentHandler
**Throws:** SAXException

- The client may raise a
processing exception.
**See Also:** ContentHandler.startDocument()

- endDocument

```java
public void endDocument()
throws
SAXException
```

End document event.

**Specified by:** endDocument

in interface

ContentHandler
**Throws:** SAXException

- The client may raise a
processing exception.
**See Also:** ContentHandler.endDocument()

- startPrefixMapping

```java
public void startPrefixMapping​(
String
prefix,

String
uri)
```

Adapt a SAX2 start prefix mapping event.

**Specified by:** startPrefixMapping

in interface

ContentHandler
**Parameters:** prefix

- The prefix being mapped.
**Parameters:** uri

- The Namespace URI being mapped to.
**See Also:** ContentHandler.startPrefixMapping(java.lang.String, java.lang.String)

- endPrefixMapping

```java
public void endPrefixMapping​(
String
prefix)
```

Adapt a SAX2 end prefix mapping event.

**Specified by:** endPrefixMapping

in interface

ContentHandler
**Parameters:** prefix

- The prefix being mapped.
**See Also:** ContentHandler.endPrefixMapping(java.lang.String)

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

Adapt a SAX2 start element event.

**Specified by:** startElement

in interface

ContentHandler
**Parameters:** uri

- The Namespace URI.
**Parameters:** localName

- The Namespace local name.
**Parameters:** qName

- The qualified (prefixed) name.
**Parameters:** atts

- The SAX2 attributes.
**Throws:** SAXException

- The client may raise a
processing exception.
**See Also:** ContentHandler.endDocument()

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

Adapt a SAX2 end element event.

**Specified by:** endElement

in interface

ContentHandler
**Parameters:** uri

- The Namespace URI.
**Parameters:** localName

- The Namespace local name.
**Parameters:** qName

- The qualified (prefixed) name.
**Throws:** SAXException

- The client may raise a
processing exception.
**See Also:** ContentHandler.endElement(java.lang.String, java.lang.String, java.lang.String)

- characters

```java
public void characters​(char[] ch,
int start,
int length)
throws
SAXException
```

Adapt a SAX2 characters event.

**Specified by:** characters

in interface

ContentHandler
**Parameters:** ch

- An array of characters.
**Parameters:** start

- The starting position in the array.
**Parameters:** length

- The number of characters to use.
**Throws:** SAXException

- The client may raise a
processing exception.
**See Also:** ContentHandler.characters(char[], int, int)

- ignorableWhitespace

```java
public void ignorableWhitespace​(char[] ch,
int start,
int length)
throws
SAXException
```

Adapt a SAX2 ignorable whitespace event.

**Specified by:** ignorableWhitespace

in interface

ContentHandler
**Parameters:** ch

- An array of characters.
**Parameters:** start

- The starting position in the array.
**Parameters:** length

- The number of characters to use.
**Throws:** SAXException

- The client may raise a
processing exception.
**See Also:** ContentHandler.ignorableWhitespace(char[], int, int)

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

Adapt a SAX2 processing instruction event.

**Specified by:** processingInstruction

in interface

ContentHandler
**Parameters:** target

- The processing instruction target.
**Parameters:** data

- The remainder of the processing instruction
**Throws:** SAXException

- The client may raise a
processing exception.
**See Also:** ContentHandler.processingInstruction(java.lang.String, java.lang.String)

- skippedEntity

```java
public void skippedEntity​(
String
name)
throws
SAXException
```

Adapt a SAX2 skipped entity event.

**Specified by:** skippedEntity

in interface

ContentHandler
**Parameters:** name

- The name of the skipped entity.
**Throws:** SAXException

- Throwable by subclasses.
**See Also:** ContentHandler.skippedEntity(java.lang.String)

Constructor Detail

- XMLReaderAdapter

```java
public XMLReaderAdapter()
throws
SAXException
```

Create a new adapter.

Use the "org.xml.sax.driver" property to locate the SAX2
driver to embed.

**Throws:** SAXException

- If the embedded driver
cannot be instantiated or if the
org.xml.sax.driver property is not specified.

- XMLReaderAdapter

```java
public XMLReaderAdapter​(
XMLReader
xmlReader)
```

Create a new adapter.

Create a new adapter, wrapped around a SAX2 XMLReader.
The adapter will make the XMLReader act like a SAX1
Parser.

**Parameters:** xmlReader

- The SAX2 XMLReader to wrap.
**Throws:** NullPointerException

- If the argument is null.

---

#### Constructor Detail

XMLReaderAdapter

```java
public XMLReaderAdapter()
throws
SAXException
```

Create a new adapter.

Use the "org.xml.sax.driver" property to locate the SAX2
driver to embed.

**Throws:** SAXException

- If the embedded driver
cannot be instantiated or if the
org.xml.sax.driver property is not specified.

---

#### XMLReaderAdapter

public XMLReaderAdapter()
throws

SAXException

Create a new adapter.

Use the "org.xml.sax.driver" property to locate the SAX2
driver to embed.

Use the "org.xml.sax.driver" property to locate the SAX2
driver to embed.

XMLReaderAdapter

```java
public XMLReaderAdapter​(
XMLReader
xmlReader)
```

Create a new adapter.

Create a new adapter, wrapped around a SAX2 XMLReader.
The adapter will make the XMLReader act like a SAX1
Parser.

**Parameters:** xmlReader

- The SAX2 XMLReader to wrap.
**Throws:** NullPointerException

- If the argument is null.

---

#### XMLReaderAdapter

public XMLReaderAdapter​(

XMLReader

xmlReader)

Create a new adapter.

Create a new adapter, wrapped around a SAX2 XMLReader.
The adapter will make the XMLReader act like a SAX1
Parser.

Create a new adapter, wrapped around a SAX2 XMLReader.
The adapter will make the XMLReader act like a SAX1
Parser.

Method Detail

- setLocale

```java
public void setLocale​(
Locale
locale)
throws
SAXException
```

Set the locale for error reporting.

This is not supported in SAX2, and will always throw
an exception.

**Specified by:** setLocale

in interface

Parser
**Parameters:** locale

- the locale for error reporting.
**Throws:** SAXException

- Thrown unless overridden.
**See Also:** Parser.setLocale(java.util.Locale)

- setEntityResolver

```java
public void setEntityResolver​(
EntityResolver
resolver)
```

Register the entity resolver.

**Specified by:** setEntityResolver

in interface

Parser
**Parameters:** resolver

- The new resolver.
**See Also:** Parser.setEntityResolver(org.xml.sax.EntityResolver)

- setDTDHandler

```java
public void setDTDHandler​(
DTDHandler
handler)
```

Register the DTD event handler.

**Specified by:** setDTDHandler

in interface

Parser
**Parameters:** handler

- The new DTD event handler.
**See Also:** Parser.setDTDHandler(org.xml.sax.DTDHandler)

- setDocumentHandler

```java
public void setDocumentHandler​(
DocumentHandler
handler)
```

Register the SAX1 document event handler.

Note that the SAX1 document handler has no Namespace
support.

**Specified by:** setDocumentHandler

in interface

Parser
**Parameters:** handler

- The new SAX1 document event handler.
**See Also:** Parser.setDocumentHandler(org.xml.sax.DocumentHandler)

- setErrorHandler

```java
public void setErrorHandler​(
ErrorHandler
handler)
```

Register the error event handler.

**Specified by:** setErrorHandler

in interface

Parser
**Parameters:** handler

- The new error event handler.
**See Also:** Parser.setErrorHandler(org.xml.sax.ErrorHandler)

- parse

```java
public void parse​(
String
systemId)
throws
IOException
,

SAXException
```

Parse the document.

This method will throw an exception if the embedded
XMLReader does not support the
http://xml.org/sax/features/namespace-prefixes property.

**Specified by:** parse

in interface

Parser
**Parameters:** systemId

- The absolute URL of the document.
**Throws:** IOException

- If there is a problem reading
the raw content of the document.
**Throws:** SAXException

- If there is a problem
processing the document.
**See Also:** parse(org.xml.sax.InputSource)

,

Parser.parse(java.lang.String)

- parse

```java
public void parse​(
InputSource
input)
throws
IOException
,

SAXException
```

Parse the document.

This method will throw an exception if the embedded
XMLReader does not support the
http://xml.org/sax/features/namespace-prefixes property.

**Specified by:** parse

in interface

Parser
**Parameters:** input

- An input source for the document.
**Throws:** IOException

- If there is a problem reading
the raw content of the document.
**Throws:** SAXException

- If there is a problem
processing the document.
**See Also:** parse(java.lang.String)

,

Parser.parse(org.xml.sax.InputSource)

- setDocumentLocator

```java
public void setDocumentLocator​(
Locator
locator)
```

Set a document locator.

**Specified by:** setDocumentLocator

in interface

ContentHandler
**Parameters:** locator

- The document locator.
**See Also:** ContentHandler.setDocumentLocator(org.xml.sax.Locator)

- startDocument

```java
public void startDocument()
throws
SAXException
```

Start document event.

**Specified by:** startDocument

in interface

ContentHandler
**Throws:** SAXException

- The client may raise a
processing exception.
**See Also:** ContentHandler.startDocument()

- endDocument

```java
public void endDocument()
throws
SAXException
```

End document event.

**Specified by:** endDocument

in interface

ContentHandler
**Throws:** SAXException

- The client may raise a
processing exception.
**See Also:** ContentHandler.endDocument()

- startPrefixMapping

```java
public void startPrefixMapping​(
String
prefix,

String
uri)
```

Adapt a SAX2 start prefix mapping event.

**Specified by:** startPrefixMapping

in interface

ContentHandler
**Parameters:** prefix

- The prefix being mapped.
**Parameters:** uri

- The Namespace URI being mapped to.
**See Also:** ContentHandler.startPrefixMapping(java.lang.String, java.lang.String)

- endPrefixMapping

```java
public void endPrefixMapping​(
String
prefix)
```

Adapt a SAX2 end prefix mapping event.

**Specified by:** endPrefixMapping

in interface

ContentHandler
**Parameters:** prefix

- The prefix being mapped.
**See Also:** ContentHandler.endPrefixMapping(java.lang.String)

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

Adapt a SAX2 start element event.

**Specified by:** startElement

in interface

ContentHandler
**Parameters:** uri

- The Namespace URI.
**Parameters:** localName

- The Namespace local name.
**Parameters:** qName

- The qualified (prefixed) name.
**Parameters:** atts

- The SAX2 attributes.
**Throws:** SAXException

- The client may raise a
processing exception.
**See Also:** ContentHandler.endDocument()

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

Adapt a SAX2 end element event.

**Specified by:** endElement

in interface

ContentHandler
**Parameters:** uri

- The Namespace URI.
**Parameters:** localName

- The Namespace local name.
**Parameters:** qName

- The qualified (prefixed) name.
**Throws:** SAXException

- The client may raise a
processing exception.
**See Also:** ContentHandler.endElement(java.lang.String, java.lang.String, java.lang.String)

- characters

```java
public void characters​(char[] ch,
int start,
int length)
throws
SAXException
```

Adapt a SAX2 characters event.

**Specified by:** characters

in interface

ContentHandler
**Parameters:** ch

- An array of characters.
**Parameters:** start

- The starting position in the array.
**Parameters:** length

- The number of characters to use.
**Throws:** SAXException

- The client may raise a
processing exception.
**See Also:** ContentHandler.characters(char[], int, int)

- ignorableWhitespace

```java
public void ignorableWhitespace​(char[] ch,
int start,
int length)
throws
SAXException
```

Adapt a SAX2 ignorable whitespace event.

**Specified by:** ignorableWhitespace

in interface

ContentHandler
**Parameters:** ch

- An array of characters.
**Parameters:** start

- The starting position in the array.
**Parameters:** length

- The number of characters to use.
**Throws:** SAXException

- The client may raise a
processing exception.
**See Also:** ContentHandler.ignorableWhitespace(char[], int, int)

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

Adapt a SAX2 processing instruction event.

**Specified by:** processingInstruction

in interface

ContentHandler
**Parameters:** target

- The processing instruction target.
**Parameters:** data

- The remainder of the processing instruction
**Throws:** SAXException

- The client may raise a
processing exception.
**See Also:** ContentHandler.processingInstruction(java.lang.String, java.lang.String)

- skippedEntity

```java
public void skippedEntity​(
String
name)
throws
SAXException
```

Adapt a SAX2 skipped entity event.

**Specified by:** skippedEntity

in interface

ContentHandler
**Parameters:** name

- The name of the skipped entity.
**Throws:** SAXException

- Throwable by subclasses.
**See Also:** ContentHandler.skippedEntity(java.lang.String)

---

#### Method Detail

setLocale

```java
public void setLocale​(
Locale
locale)
throws
SAXException
```

Set the locale for error reporting.

This is not supported in SAX2, and will always throw
an exception.

**Specified by:** setLocale

in interface

Parser
**Parameters:** locale

- the locale for error reporting.
**Throws:** SAXException

- Thrown unless overridden.
**See Also:** Parser.setLocale(java.util.Locale)

---

#### setLocale

public void setLocale​(

Locale

locale)
throws

SAXException

Set the locale for error reporting.

This is not supported in SAX2, and will always throw
an exception.

This is not supported in SAX2, and will always throw
an exception.

setEntityResolver

```java
public void setEntityResolver​(
EntityResolver
resolver)
```

Register the entity resolver.

**Specified by:** setEntityResolver

in interface

Parser
**Parameters:** resolver

- The new resolver.
**See Also:** Parser.setEntityResolver(org.xml.sax.EntityResolver)

---

#### setEntityResolver

public void setEntityResolver​(

EntityResolver

resolver)

Register the entity resolver.

setDTDHandler

```java
public void setDTDHandler​(
DTDHandler
handler)
```

Register the DTD event handler.

**Specified by:** setDTDHandler

in interface

Parser
**Parameters:** handler

- The new DTD event handler.
**See Also:** Parser.setDTDHandler(org.xml.sax.DTDHandler)

---

#### setDTDHandler

public void setDTDHandler​(

DTDHandler

handler)

Register the DTD event handler.

setDocumentHandler

```java
public void setDocumentHandler​(
DocumentHandler
handler)
```

Register the SAX1 document event handler.

Note that the SAX1 document handler has no Namespace
support.

**Specified by:** setDocumentHandler

in interface

Parser
**Parameters:** handler

- The new SAX1 document event handler.
**See Also:** Parser.setDocumentHandler(org.xml.sax.DocumentHandler)

---

#### setDocumentHandler

public void setDocumentHandler​(

DocumentHandler

handler)

Register the SAX1 document event handler.

Note that the SAX1 document handler has no Namespace
support.

Note that the SAX1 document handler has no Namespace
support.

setErrorHandler

```java
public void setErrorHandler​(
ErrorHandler
handler)
```

Register the error event handler.

**Specified by:** setErrorHandler

in interface

Parser
**Parameters:** handler

- The new error event handler.
**See Also:** Parser.setErrorHandler(org.xml.sax.ErrorHandler)

---

#### setErrorHandler

public void setErrorHandler​(

ErrorHandler

handler)

Register the error event handler.

parse

```java
public void parse​(
String
systemId)
throws
IOException
,

SAXException
```

Parse the document.

This method will throw an exception if the embedded
XMLReader does not support the
http://xml.org/sax/features/namespace-prefixes property.

**Specified by:** parse

in interface

Parser
**Parameters:** systemId

- The absolute URL of the document.
**Throws:** IOException

- If there is a problem reading
the raw content of the document.
**Throws:** SAXException

- If there is a problem
processing the document.
**See Also:** parse(org.xml.sax.InputSource)

,

Parser.parse(java.lang.String)

---

#### parse

public void parse​(

String

systemId)
throws

IOException

,

SAXException

Parse the document.

This method will throw an exception if the embedded
XMLReader does not support the
http://xml.org/sax/features/namespace-prefixes property.

This method will throw an exception if the embedded
XMLReader does not support the
http://xml.org/sax/features/namespace-prefixes property.

parse

```java
public void parse​(
InputSource
input)
throws
IOException
,

SAXException
```

Parse the document.

This method will throw an exception if the embedded
XMLReader does not support the
http://xml.org/sax/features/namespace-prefixes property.

**Specified by:** parse

in interface

Parser
**Parameters:** input

- An input source for the document.
**Throws:** IOException

- If there is a problem reading
the raw content of the document.
**Throws:** SAXException

- If there is a problem
processing the document.
**See Also:** parse(java.lang.String)

,

Parser.parse(org.xml.sax.InputSource)

---

#### parse

public void parse​(

InputSource

input)
throws

IOException

,

SAXException

Parse the document.

This method will throw an exception if the embedded
XMLReader does not support the
http://xml.org/sax/features/namespace-prefixes property.

This method will throw an exception if the embedded
XMLReader does not support the
http://xml.org/sax/features/namespace-prefixes property.

setDocumentLocator

```java
public void setDocumentLocator​(
Locator
locator)
```

Set a document locator.

**Specified by:** setDocumentLocator

in interface

ContentHandler
**Parameters:** locator

- The document locator.
**See Also:** ContentHandler.setDocumentLocator(org.xml.sax.Locator)

---

#### setDocumentLocator

public void setDocumentLocator​(

Locator

locator)

Set a document locator.

startDocument

```java
public void startDocument()
throws
SAXException
```

Start document event.

**Specified by:** startDocument

in interface

ContentHandler
**Throws:** SAXException

- The client may raise a
processing exception.
**See Also:** ContentHandler.startDocument()

---

#### startDocument

public void startDocument()
throws

SAXException

Start document event.

endDocument

```java
public void endDocument()
throws
SAXException
```

End document event.

**Specified by:** endDocument

in interface

ContentHandler
**Throws:** SAXException

- The client may raise a
processing exception.
**See Also:** ContentHandler.endDocument()

---

#### endDocument

public void endDocument()
throws

SAXException

End document event.

startPrefixMapping

```java
public void startPrefixMapping​(
String
prefix,

String
uri)
```

Adapt a SAX2 start prefix mapping event.

**Specified by:** startPrefixMapping

in interface

ContentHandler
**Parameters:** prefix

- The prefix being mapped.
**Parameters:** uri

- The Namespace URI being mapped to.
**See Also:** ContentHandler.startPrefixMapping(java.lang.String, java.lang.String)

---

#### startPrefixMapping

public void startPrefixMapping​(

String

prefix,

String

uri)

Adapt a SAX2 start prefix mapping event.

endPrefixMapping

```java
public void endPrefixMapping​(
String
prefix)
```

Adapt a SAX2 end prefix mapping event.

**Specified by:** endPrefixMapping

in interface

ContentHandler
**Parameters:** prefix

- The prefix being mapped.
**See Also:** ContentHandler.endPrefixMapping(java.lang.String)

---

#### endPrefixMapping

public void endPrefixMapping​(

String

prefix)

Adapt a SAX2 end prefix mapping event.

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

Adapt a SAX2 start element event.

**Specified by:** startElement

in interface

ContentHandler
**Parameters:** uri

- The Namespace URI.
**Parameters:** localName

- The Namespace local name.
**Parameters:** qName

- The qualified (prefixed) name.
**Parameters:** atts

- The SAX2 attributes.
**Throws:** SAXException

- The client may raise a
processing exception.
**See Also:** ContentHandler.endDocument()

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

Adapt a SAX2 start element event.

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

Adapt a SAX2 end element event.

**Specified by:** endElement

in interface

ContentHandler
**Parameters:** uri

- The Namespace URI.
**Parameters:** localName

- The Namespace local name.
**Parameters:** qName

- The qualified (prefixed) name.
**Throws:** SAXException

- The client may raise a
processing exception.
**See Also:** ContentHandler.endElement(java.lang.String, java.lang.String, java.lang.String)

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

Adapt a SAX2 end element event.

characters

```java
public void characters​(char[] ch,
int start,
int length)
throws
SAXException
```

Adapt a SAX2 characters event.

**Specified by:** characters

in interface

ContentHandler
**Parameters:** ch

- An array of characters.
**Parameters:** start

- The starting position in the array.
**Parameters:** length

- The number of characters to use.
**Throws:** SAXException

- The client may raise a
processing exception.
**See Also:** ContentHandler.characters(char[], int, int)

---

#### characters

public void characters​(char[] ch,
int start,
int length)
throws

SAXException

Adapt a SAX2 characters event.

ignorableWhitespace

```java
public void ignorableWhitespace​(char[] ch,
int start,
int length)
throws
SAXException
```

Adapt a SAX2 ignorable whitespace event.

**Specified by:** ignorableWhitespace

in interface

ContentHandler
**Parameters:** ch

- An array of characters.
**Parameters:** start

- The starting position in the array.
**Parameters:** length

- The number of characters to use.
**Throws:** SAXException

- The client may raise a
processing exception.
**See Also:** ContentHandler.ignorableWhitespace(char[], int, int)

---

#### ignorableWhitespace

public void ignorableWhitespace​(char[] ch,
int start,
int length)
throws

SAXException

Adapt a SAX2 ignorable whitespace event.

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

Adapt a SAX2 processing instruction event.

**Specified by:** processingInstruction

in interface

ContentHandler
**Parameters:** target

- The processing instruction target.
**Parameters:** data

- The remainder of the processing instruction
**Throws:** SAXException

- The client may raise a
processing exception.
**See Also:** ContentHandler.processingInstruction(java.lang.String, java.lang.String)

---

#### processingInstruction

public void processingInstruction​(

String

target,

String

data)
throws

SAXException

Adapt a SAX2 processing instruction event.

skippedEntity

```java
public void skippedEntity​(
String
name)
throws
SAXException
```

Adapt a SAX2 skipped entity event.

**Specified by:** skippedEntity

in interface

ContentHandler
**Parameters:** name

- The name of the skipped entity.
**Throws:** SAXException

- Throwable by subclasses.
**See Also:** ContentHandler.skippedEntity(java.lang.String)

---

#### skippedEntity

public void skippedEntity​(

String

name)
throws

SAXException

Adapt a SAX2 skipped entity event.

---

