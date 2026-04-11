# Class DefaultHandler2

**Source:** `java.xml\org\xml\sax\ext\DefaultHandler2.html`

### Class Description

```java
public class
DefaultHandler2

extends
DefaultHandler

implements
LexicalHandler
,
DeclHandler
,
EntityResolver2
```

This class extends the SAX2 base handler class to support the
SAX2

LexicalHandler

,

DeclHandler

, and

EntityResolver2

extensions. Except for overriding the
original SAX1

resolveEntity()

method the added handler methods just return. Subclassers may
override everything on a method-by-method basis.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

Note:

this class might yet learn that the

ContentHandler.setDocumentLocator()

call might be passed a

Locator2

object, and that the

ContentHandler.startElement()

call might be passed a

Attributes2

object.

**All Implemented Interfaces:** ContentHandler

,

DTDHandler

,

EntityResolver

,

ErrorHandler

,

DeclHandler

,

EntityResolver2

,

LexicalHandler

---

### Field Details

*No entries found.*

### Constructor Details

#### public DefaultHandler2()

Constructs a handler which ignores all parsing events.

---

### Method Details

#### public
InputSource
getExternalSubset​(
String
name,

String
baseURI)
throws
SAXException
,

IOException

Tells the parser that if no external subset has been declared
in the document text, none should be used.

**Specified by:**
- getExternalSubset

in interface

EntityResolver2

**Parameters:**
- name

- Identifies the document root element. This name comes
from a DOCTYPE declaration (where available) or from the actual
root element.
- baseURI

- The document's base URI, serving as an additional
hint for selecting the external subset. This is always an absolute
URI, unless it is null because the XMLReader was given an InputSource
without one.

**Returns:**
- An InputSource object describing the new external subset
to be used by the parser, or null to indicate that no external
subset is provided.

**Throws:**
- SAXException

- Any SAX exception, possibly wrapping
another exception.
- IOException

- Probably indicating a failure to create
a new InputStream or Reader, or an illegal URL.

---

#### public
InputSource
resolveEntity​(
String
name,

String
publicId,

String
baseURI,

String
systemId)
throws
SAXException
,

IOException

Tells the parser to resolve the systemId against the baseURI
and read the entity text from that resulting absolute URI.
Note that because the older

DefaultHandler.resolveEntity()

,
method is overridden to call this one, this method may sometimes
be invoked with null

name

and

baseURI

, and
with the

systemId

already absolutized.

**Specified by:**
- resolveEntity

in interface

EntityResolver2

**Parameters:**
- name

- Identifies the external entity being resolved.
Either "[dtd]" for the external subset, or a name starting
with "%" to indicate a parameter entity, or else the name of
a general entity. This is never null when invoked by a SAX2
parser.
- publicId

- The public identifier of the external entity being
referenced (normalized as required by the XML specification), or
null if none was supplied.
- baseURI

- The URI with respect to which relative systemIDs
are interpreted. This is always an absolute URI, unless it is
null (likely because the XMLReader was given an InputSource without
one). This URI is defined by the XML specification to be the one
associated with the "<" starting the relevant declaration.
- systemId

- The system identifier of the external entity
being referenced; either a relative or absolute URI.
This is never null when invoked by a SAX2 parser; only declared
entities, and any external subset, are resolved by such parsers.

**Returns:**
- An InputSource object describing the new input source to
be used by the parser. Returning null directs the parser to
resolve the system ID against the base URI and open a connection
to resulting URI.

**Throws:**
- SAXException

- Any SAX exception, possibly wrapping
another exception.
- IOException

- Probably indicating a failure to create
a new InputStream or Reader, or an illegal URL.

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

Invokes

EntityResolver2.resolveEntity()

with null entity name and base URI.
You only need to override that method to use this class.

**Specified by:**
- resolveEntity

in interface

EntityResolver

**Overrides:**
- resolveEntity

in class

DefaultHandler

**Parameters:**
- publicId

- The public identifier, or null if none is
available.
- systemId

- The system identifier provided in the XML
document.

**Returns:**
- The new input source, or null to require the
default behaviour.

**Throws:**
- SAXException

- Any SAX exception, possibly
wrapping another exception.
- IOException

- If there is an error setting
up the new input source.

**See Also:**
- EntityResolver.resolveEntity(java.lang.String, java.lang.String)

---

### Additional Sections

#### Class DefaultHandler2

java.lang.Object

- org.xml.sax.helpers.DefaultHandler
- - org.xml.sax.ext.DefaultHandler2

org.xml.sax.helpers.DefaultHandler

- org.xml.sax.ext.DefaultHandler2

org.xml.sax.ext.DefaultHandler2

**All Implemented Interfaces:** ContentHandler

,

DTDHandler

,

EntityResolver

,

ErrorHandler

,

DeclHandler

,

EntityResolver2

,

LexicalHandler

```java
public class
DefaultHandler2

extends
DefaultHandler

implements
LexicalHandler
,
DeclHandler
,
EntityResolver2
```

This class extends the SAX2 base handler class to support the
SAX2

LexicalHandler

,

DeclHandler

, and

EntityResolver2

extensions. Except for overriding the
original SAX1

resolveEntity()

method the added handler methods just return. Subclassers may
override everything on a method-by-method basis.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

Note:

this class might yet learn that the

ContentHandler.setDocumentLocator()

call might be passed a

Locator2

object, and that the

ContentHandler.startElement()

call might be passed a

Attributes2

object.

**Since:** 1.5, SAX 2.0 (extensions 1.1 alpha)

public class

DefaultHandler2

extends

DefaultHandler

implements

LexicalHandler

,

DeclHandler

,

EntityResolver2

This class extends the SAX2 base handler class to support the
SAX2

LexicalHandler

,

DeclHandler

, and

EntityResolver2

extensions. Except for overriding the
original SAX1

resolveEntity()

method the added handler methods just return. Subclassers may
override everything on a method-by-method basis.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

Note:

this class might yet learn that the

ContentHandler.setDocumentLocator()

call might be passed a

Locator2

object, and that the

ContentHandler.startElement()

call might be passed a

Attributes2

object.

Note:

this class might yet learn that the

ContentHandler.setDocumentLocator()

call might be passed a

Locator2

object, and that the

ContentHandler.startElement()

call might be passed a

Attributes2

object.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DefaultHandler2

()

Constructs a handler which ignores all parsing events.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

InputSource

getExternalSubset

​(

String

name,

String

baseURI)

Tells the parser that if no external subset has been declared
in the document text, none should be used.

InputSource

resolveEntity

​(

String

publicId,

String

systemId)

Invokes

EntityResolver2.resolveEntity()

with null entity name and base URI.

InputSource

resolveEntity

​(

String

name,

String

publicId,

String

baseURI,

String

systemId)

Tells the parser to resolve the systemId against the baseURI
and read the entity text from that resulting absolute URI.

- Methods declared in class org.xml.sax.helpers.

DefaultHandler

characters

,

endDocument

,

endElement

,

endPrefixMapping

,

error

,

fatalError

,

ignorableWhitespace

,

notationDecl

,

processingInstruction

,

setDocumentLocator

,

skippedEntity

,

startDocument

,

startElement

,

startPrefixMapping

,

unparsedEntityDecl

,

warning

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

- Methods declared in interface org.xml.sax.ext.

DeclHandler

attributeDecl

,

elementDecl

,

externalEntityDecl

,

internalEntityDecl

- Methods declared in interface org.xml.sax.ext.

LexicalHandler

comment

,

endCDATA

,

endDTD

,

endEntity

,

startCDATA

,

startDTD

,

startEntity

Constructor Summary

Constructors

Constructor

Description

DefaultHandler2

()

Constructs a handler which ignores all parsing events.

---

#### Constructor Summary

Constructs a handler which ignores all parsing events.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

InputSource

getExternalSubset

​(

String

name,

String

baseURI)

Tells the parser that if no external subset has been declared
in the document text, none should be used.

InputSource

resolveEntity

​(

String

publicId,

String

systemId)

Invokes

EntityResolver2.resolveEntity()

with null entity name and base URI.

InputSource

resolveEntity

​(

String

name,

String

publicId,

String

baseURI,

String

systemId)

Tells the parser to resolve the systemId against the baseURI
and read the entity text from that resulting absolute URI.

- Methods declared in class org.xml.sax.helpers.

DefaultHandler

characters

,

endDocument

,

endElement

,

endPrefixMapping

,

error

,

fatalError

,

ignorableWhitespace

,

notationDecl

,

processingInstruction

,

setDocumentLocator

,

skippedEntity

,

startDocument

,

startElement

,

startPrefixMapping

,

unparsedEntityDecl

,

warning

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

- Methods declared in interface org.xml.sax.ext.

DeclHandler

attributeDecl

,

elementDecl

,

externalEntityDecl

,

internalEntityDecl

- Methods declared in interface org.xml.sax.ext.

LexicalHandler

comment

,

endCDATA

,

endDTD

,

endEntity

,

startCDATA

,

startDTD

,

startEntity

---

#### Method Summary

Tells the parser that if no external subset has been declared
in the document text, none should be used.

Invokes

EntityResolver2.resolveEntity()

with null entity name and base URI.

Tells the parser to resolve the systemId against the baseURI
and read the entity text from that resulting absolute URI.

Methods declared in class org.xml.sax.helpers.

DefaultHandler

characters

,

endDocument

,

endElement

,

endPrefixMapping

,

error

,

fatalError

,

ignorableWhitespace

,

notationDecl

,

processingInstruction

,

setDocumentLocator

,

skippedEntity

,

startDocument

,

startElement

,

startPrefixMapping

,

unparsedEntityDecl

,

warning

---

#### Methods declared in class org.xml.sax.helpers. DefaultHandler

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

Methods declared in interface org.xml.sax.ext.

DeclHandler

attributeDecl

,

elementDecl

,

externalEntityDecl

,

internalEntityDecl

---

#### Methods declared in interface org.xml.sax.ext. DeclHandler

Methods declared in interface org.xml.sax.ext.

LexicalHandler

comment

,

endCDATA

,

endDTD

,

endEntity

,

startCDATA

,

startDTD

,

startEntity

---

#### Methods declared in interface org.xml.sax.ext. LexicalHandler

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DefaultHandler2

```java
public DefaultHandler2()
```

Constructs a handler which ignores all parsing events.

============ METHOD DETAIL ==========

- Method Detail

- getExternalSubset

```java
public
InputSource
getExternalSubset​(
String
name,

String
baseURI)
throws
SAXException
,

IOException
```

Tells the parser that if no external subset has been declared
in the document text, none should be used.

**Specified by:** getExternalSubset

in interface

EntityResolver2
**Parameters:** name

- Identifies the document root element. This name comes
from a DOCTYPE declaration (where available) or from the actual
root element.
**Parameters:** baseURI

- The document's base URI, serving as an additional
hint for selecting the external subset. This is always an absolute
URI, unless it is null because the XMLReader was given an InputSource
without one.
**Returns:** An InputSource object describing the new external subset
to be used by the parser, or null to indicate that no external
subset is provided.
**Throws:** SAXException

- Any SAX exception, possibly wrapping
another exception.
**Throws:** IOException

- Probably indicating a failure to create
a new InputStream or Reader, or an illegal URL.

- resolveEntity

```java
public
InputSource
resolveEntity​(
String
name,

String
publicId,

String
baseURI,

String
systemId)
throws
SAXException
,

IOException
```

Tells the parser to resolve the systemId against the baseURI
and read the entity text from that resulting absolute URI.
Note that because the older

DefaultHandler.resolveEntity()

,
method is overridden to call this one, this method may sometimes
be invoked with null

name

and

baseURI

, and
with the

systemId

already absolutized.

**Specified by:** resolveEntity

in interface

EntityResolver2
**Parameters:** name

- Identifies the external entity being resolved.
Either "[dtd]" for the external subset, or a name starting
with "%" to indicate a parameter entity, or else the name of
a general entity. This is never null when invoked by a SAX2
parser.
**Parameters:** publicId

- The public identifier of the external entity being
referenced (normalized as required by the XML specification), or
null if none was supplied.
**Parameters:** baseURI

- The URI with respect to which relative systemIDs
are interpreted. This is always an absolute URI, unless it is
null (likely because the XMLReader was given an InputSource without
one). This URI is defined by the XML specification to be the one
associated with the "<" starting the relevant declaration.
**Parameters:** systemId

- The system identifier of the external entity
being referenced; either a relative or absolute URI.
This is never null when invoked by a SAX2 parser; only declared
entities, and any external subset, are resolved by such parsers.
**Returns:** An InputSource object describing the new input source to
be used by the parser. Returning null directs the parser to
resolve the system ID against the base URI and open a connection
to resulting URI.
**Throws:** SAXException

- Any SAX exception, possibly wrapping
another exception.
**Throws:** IOException

- Probably indicating a failure to create
a new InputStream or Reader, or an illegal URL.

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

Invokes

EntityResolver2.resolveEntity()

with null entity name and base URI.
You only need to override that method to use this class.

**Specified by:** resolveEntity

in interface

EntityResolver
**Overrides:** resolveEntity

in class

DefaultHandler
**Parameters:** publicId

- The public identifier, or null if none is
available.
**Parameters:** systemId

- The system identifier provided in the XML
document.
**Returns:** The new input source, or null to require the
default behaviour.
**Throws:** SAXException

- Any SAX exception, possibly
wrapping another exception.
**Throws:** IOException

- If there is an error setting
up the new input source.
**See Also:** EntityResolver.resolveEntity(java.lang.String, java.lang.String)

Constructor Detail

- DefaultHandler2

```java
public DefaultHandler2()
```

Constructs a handler which ignores all parsing events.

---

#### Constructor Detail

DefaultHandler2

```java
public DefaultHandler2()
```

Constructs a handler which ignores all parsing events.

---

#### DefaultHandler2

public DefaultHandler2()

Constructs a handler which ignores all parsing events.

Method Detail

- getExternalSubset

```java
public
InputSource
getExternalSubset​(
String
name,

String
baseURI)
throws
SAXException
,

IOException
```

Tells the parser that if no external subset has been declared
in the document text, none should be used.

**Specified by:** getExternalSubset

in interface

EntityResolver2
**Parameters:** name

- Identifies the document root element. This name comes
from a DOCTYPE declaration (where available) or from the actual
root element.
**Parameters:** baseURI

- The document's base URI, serving as an additional
hint for selecting the external subset. This is always an absolute
URI, unless it is null because the XMLReader was given an InputSource
without one.
**Returns:** An InputSource object describing the new external subset
to be used by the parser, or null to indicate that no external
subset is provided.
**Throws:** SAXException

- Any SAX exception, possibly wrapping
another exception.
**Throws:** IOException

- Probably indicating a failure to create
a new InputStream or Reader, or an illegal URL.

- resolveEntity

```java
public
InputSource
resolveEntity​(
String
name,

String
publicId,

String
baseURI,

String
systemId)
throws
SAXException
,

IOException
```

Tells the parser to resolve the systemId against the baseURI
and read the entity text from that resulting absolute URI.
Note that because the older

DefaultHandler.resolveEntity()

,
method is overridden to call this one, this method may sometimes
be invoked with null

name

and

baseURI

, and
with the

systemId

already absolutized.

**Specified by:** resolveEntity

in interface

EntityResolver2
**Parameters:** name

- Identifies the external entity being resolved.
Either "[dtd]" for the external subset, or a name starting
with "%" to indicate a parameter entity, or else the name of
a general entity. This is never null when invoked by a SAX2
parser.
**Parameters:** publicId

- The public identifier of the external entity being
referenced (normalized as required by the XML specification), or
null if none was supplied.
**Parameters:** baseURI

- The URI with respect to which relative systemIDs
are interpreted. This is always an absolute URI, unless it is
null (likely because the XMLReader was given an InputSource without
one). This URI is defined by the XML specification to be the one
associated with the "<" starting the relevant declaration.
**Parameters:** systemId

- The system identifier of the external entity
being referenced; either a relative or absolute URI.
This is never null when invoked by a SAX2 parser; only declared
entities, and any external subset, are resolved by such parsers.
**Returns:** An InputSource object describing the new input source to
be used by the parser. Returning null directs the parser to
resolve the system ID against the base URI and open a connection
to resulting URI.
**Throws:** SAXException

- Any SAX exception, possibly wrapping
another exception.
**Throws:** IOException

- Probably indicating a failure to create
a new InputStream or Reader, or an illegal URL.

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

Invokes

EntityResolver2.resolveEntity()

with null entity name and base URI.
You only need to override that method to use this class.

**Specified by:** resolveEntity

in interface

EntityResolver
**Overrides:** resolveEntity

in class

DefaultHandler
**Parameters:** publicId

- The public identifier, or null if none is
available.
**Parameters:** systemId

- The system identifier provided in the XML
document.
**Returns:** The new input source, or null to require the
default behaviour.
**Throws:** SAXException

- Any SAX exception, possibly
wrapping another exception.
**Throws:** IOException

- If there is an error setting
up the new input source.
**See Also:** EntityResolver.resolveEntity(java.lang.String, java.lang.String)

---

#### Method Detail

getExternalSubset

```java
public
InputSource
getExternalSubset​(
String
name,

String
baseURI)
throws
SAXException
,

IOException
```

Tells the parser that if no external subset has been declared
in the document text, none should be used.

**Specified by:** getExternalSubset

in interface

EntityResolver2
**Parameters:** name

- Identifies the document root element. This name comes
from a DOCTYPE declaration (where available) or from the actual
root element.
**Parameters:** baseURI

- The document's base URI, serving as an additional
hint for selecting the external subset. This is always an absolute
URI, unless it is null because the XMLReader was given an InputSource
without one.
**Returns:** An InputSource object describing the new external subset
to be used by the parser, or null to indicate that no external
subset is provided.
**Throws:** SAXException

- Any SAX exception, possibly wrapping
another exception.
**Throws:** IOException

- Probably indicating a failure to create
a new InputStream or Reader, or an illegal URL.

---

#### getExternalSubset

public

InputSource

getExternalSubset​(

String

name,

String

baseURI)
throws

SAXException

,

IOException

Tells the parser that if no external subset has been declared
in the document text, none should be used.

resolveEntity

```java
public
InputSource
resolveEntity​(
String
name,

String
publicId,

String
baseURI,

String
systemId)
throws
SAXException
,

IOException
```

Tells the parser to resolve the systemId against the baseURI
and read the entity text from that resulting absolute URI.
Note that because the older

DefaultHandler.resolveEntity()

,
method is overridden to call this one, this method may sometimes
be invoked with null

name

and

baseURI

, and
with the

systemId

already absolutized.

**Specified by:** resolveEntity

in interface

EntityResolver2
**Parameters:** name

- Identifies the external entity being resolved.
Either "[dtd]" for the external subset, or a name starting
with "%" to indicate a parameter entity, or else the name of
a general entity. This is never null when invoked by a SAX2
parser.
**Parameters:** publicId

- The public identifier of the external entity being
referenced (normalized as required by the XML specification), or
null if none was supplied.
**Parameters:** baseURI

- The URI with respect to which relative systemIDs
are interpreted. This is always an absolute URI, unless it is
null (likely because the XMLReader was given an InputSource without
one). This URI is defined by the XML specification to be the one
associated with the "<" starting the relevant declaration.
**Parameters:** systemId

- The system identifier of the external entity
being referenced; either a relative or absolute URI.
This is never null when invoked by a SAX2 parser; only declared
entities, and any external subset, are resolved by such parsers.
**Returns:** An InputSource object describing the new input source to
be used by the parser. Returning null directs the parser to
resolve the system ID against the base URI and open a connection
to resulting URI.
**Throws:** SAXException

- Any SAX exception, possibly wrapping
another exception.
**Throws:** IOException

- Probably indicating a failure to create
a new InputStream or Reader, or an illegal URL.

---

#### resolveEntity

public

InputSource

resolveEntity​(

String

name,

String

publicId,

String

baseURI,

String

systemId)
throws

SAXException

,

IOException

Tells the parser to resolve the systemId against the baseURI
and read the entity text from that resulting absolute URI.
Note that because the older

DefaultHandler.resolveEntity()

,
method is overridden to call this one, this method may sometimes
be invoked with null

name

and

baseURI

, and
with the

systemId

already absolutized.

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

Invokes

EntityResolver2.resolveEntity()

with null entity name and base URI.
You only need to override that method to use this class.

**Specified by:** resolveEntity

in interface

EntityResolver
**Overrides:** resolveEntity

in class

DefaultHandler
**Parameters:** publicId

- The public identifier, or null if none is
available.
**Parameters:** systemId

- The system identifier provided in the XML
document.
**Returns:** The new input source, or null to require the
default behaviour.
**Throws:** SAXException

- Any SAX exception, possibly
wrapping another exception.
**Throws:** IOException

- If there is an error setting
up the new input source.
**See Also:** EntityResolver.resolveEntity(java.lang.String, java.lang.String)

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

Invokes

EntityResolver2.resolveEntity()

with null entity name and base URI.
You only need to override that method to use this class.

---

