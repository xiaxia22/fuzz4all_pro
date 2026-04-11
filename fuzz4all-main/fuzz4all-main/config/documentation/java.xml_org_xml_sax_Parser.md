# Interface Parser

**Source:** `java.xml\org\xml\sax\Parser.html`

### Class Description

```java
@Deprecated
(
since
="1.5")
public interface
Parser
```

Basic interface for SAX (Simple API for XML) parsers.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

This was the main event supplier interface for SAX1; it has
been replaced in SAX2 by

XMLReader

,
which includes Namespace support and sophisticated configurability
and extensibility.

All SAX1 parsers must implement this basic interface: it allows
applications to register handlers for different types of events
and to initiate a parse from a URI, or a character stream.

All SAX1 parsers must also implement a zero-argument constructor
(though other constructors are also allowed).

SAX1 parsers are reusable but not re-entrant: the application
may reuse a parser object (possibly with a different input source)
once the first parse has completed successfully, but it may not
invoke the parse() methods recursively within a parse.

**All Known Implementing Classes:** XMLReaderAdapter

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void setLocale​(
Locale
locale)
throws
SAXException

Allow an application to request a locale for errors and warnings.

SAX parsers are not required to provide localisation for errors
and warnings; if they cannot support the requested locale,
however, they must throw a SAX exception. Applications may
not request a locale change in the middle of a parse.

**Parameters:**
- locale

- A Java Locale object.

**Throws:**
- SAXException

- Throws an exception
(using the previous or default locale) if the
requested locale is not supported.

**See Also:**
- SAXException

,

SAXParseException

---

#### void setEntityResolver​(
EntityResolver
resolver)

Allow an application to register a custom entity resolver.

If the application does not register an entity resolver, the
SAX parser will resolve system identifiers and open connections
to entities itself (this is the default behaviour implemented in
HandlerBase).

Applications may register a new or different entity resolver
in the middle of a parse, and the SAX parser must begin using
the new resolver immediately.

**Parameters:**
- resolver

- The object for resolving entities.

**See Also:**
- EntityResolver

,

HandlerBase

---

#### void setDTDHandler​(
DTDHandler
handler)

Allow an application to register a DTD event handler.

If the application does not register a DTD handler, all DTD
events reported by the SAX parser will be silently
ignored (this is the default behaviour implemented by
HandlerBase).

Applications may register a new or different
handler in the middle of a parse, and the SAX parser must
begin using the new handler immediately.

**Parameters:**
- handler

- The DTD handler.

**See Also:**
- DTDHandler

,

HandlerBase

---

#### void setDocumentHandler​(
DocumentHandler
handler)

Allow an application to register a document event handler.

If the application does not register a document handler, all
document events reported by the SAX parser will be silently
ignored (this is the default behaviour implemented by
HandlerBase).

Applications may register a new or different handler in the
middle of a parse, and the SAX parser must begin using the new
handler immediately.

**Parameters:**
- handler

- The document handler.

**See Also:**
- DocumentHandler

,

HandlerBase

---

#### void setErrorHandler​(
ErrorHandler
handler)

Allow an application to register an error event handler.

If the application does not register an error event handler,
all error events reported by the SAX parser will be silently
ignored, except for fatalError, which will throw a SAXException
(this is the default behaviour implemented by HandlerBase).

Applications may register a new or different handler in the
middle of a parse, and the SAX parser must begin using the new
handler immediately.

**Parameters:**
- handler

- The error handler.

**See Also:**
- ErrorHandler

,

SAXException

,

HandlerBase

---

#### void parse​(
InputSource
source)
throws
SAXException
,

IOException

Parse an XML document.

The application can use this method to instruct the SAX parser
to begin parsing an XML document from any valid input
source (a character stream, a byte stream, or a URI).

Applications may not invoke this method while a parse is in
progress (they should create a new Parser instead for each
additional XML document). Once a parse is complete, an
application may reuse the same Parser object, possibly with a
different input source.

**Parameters:**
- source

- The input source for the top-level of the
XML document.

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

parse(java.lang.String)

,

setEntityResolver(org.xml.sax.EntityResolver)

,

setDTDHandler(org.xml.sax.DTDHandler)

,

setDocumentHandler(org.xml.sax.DocumentHandler)

,

setErrorHandler(org.xml.sax.ErrorHandler)

---

#### void parse​(
String
systemId)
throws
SAXException
,

IOException

Parse an XML document from a system identifier (URI).

This method is a shortcut for the common case of reading a
document from a system identifier. It is the exact
equivalent of the following:

```java
parse(new InputSource(systemId));
```

If the system identifier is a URL, it must be fully resolved
by the application before it is passed to the parser.

**Parameters:**
- systemId

- The system identifier (URI).

**Throws:**
- SAXException

- Any SAX exception, possibly
wrapping another exception.
- IOException

- An IO exception from the parser,
possibly from a byte stream or character stream
supplied by the application.

**See Also:**
- parse(org.xml.sax.InputSource)

---

### Additional Sections

#### Interface Parser

**All Known Implementing Classes:** XMLReaderAdapter

```java
@Deprecated
(
since
="1.5")
public interface
Parser
```

Deprecated.

This interface has been replaced by the SAX2

XMLReader

interface, which includes Namespace support.

Basic interface for SAX (Simple API for XML) parsers.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

This was the main event supplier interface for SAX1; it has
been replaced in SAX2 by

XMLReader

,
which includes Namespace support and sophisticated configurability
and extensibility.

All SAX1 parsers must implement this basic interface: it allows
applications to register handlers for different types of events
and to initiate a parse from a URI, or a character stream.

All SAX1 parsers must also implement a zero-argument constructor
(though other constructors are also allowed).

SAX1 parsers are reusable but not re-entrant: the application
may reuse a parser object (possibly with a different input source)
once the first parse has completed successfully, but it may not
invoke the parse() methods recursively within a parse.

**Since:** 1.4, SAX 1.0
**See Also:** EntityResolver

,

DTDHandler

,

DocumentHandler

,

ErrorHandler

,

HandlerBase

,

InputSource

@Deprecated

(

since

="1.5")
public interface

Parser

Basic interface for SAX (Simple API for XML) parsers.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

This was the main event supplier interface for SAX1; it has
been replaced in SAX2 by

XMLReader

,
which includes Namespace support and sophisticated configurability
and extensibility.

All SAX1 parsers must implement this basic interface: it allows
applications to register handlers for different types of events
and to initiate a parse from a URI, or a character stream.

All SAX1 parsers must also implement a zero-argument constructor
(though other constructors are also allowed).

SAX1 parsers are reusable but not re-entrant: the application
may reuse a parser object (possibly with a different input source)
once the first parse has completed successfully, but it may not
invoke the parse() methods recursively within a parse.

This was the main event supplier interface for SAX1; it has
been replaced in SAX2 by

XMLReader

,
which includes Namespace support and sophisticated configurability
and extensibility.

All SAX1 parsers must implement this basic interface: it allows
applications to register handlers for different types of events
and to initiate a parse from a URI, or a character stream.

All SAX1 parsers must also implement a zero-argument constructor
(though other constructors are also allowed).

SAX1 parsers are reusable but not re-entrant: the application
may reuse a parser object (possibly with a different input source)
once the first parse has completed successfully, but it may not
invoke the parse() methods recursively within a parse.

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

parse

​(

String

systemId)

Deprecated.

Parse an XML document from a system identifier (URI).

void

parse

​(

InputSource

source)

Deprecated.

Parse an XML document.

void

setDocumentHandler

​(

DocumentHandler

handler)

Deprecated.

Allow an application to register a document event handler.

void

setDTDHandler

​(

DTDHandler

handler)

Deprecated.

Allow an application to register a DTD event handler.

void

setEntityResolver

​(

EntityResolver

resolver)

Deprecated.

Allow an application to register a custom entity resolver.

void

setErrorHandler

​(

ErrorHandler

handler)

Deprecated.

Allow an application to register an error event handler.

void

setLocale

​(

Locale

locale)

Deprecated.

Allow an application to request a locale for errors and warnings.

Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

void

parse

​(

String

systemId)

Deprecated.

Parse an XML document from a system identifier (URI).

void

parse

​(

InputSource

source)

Deprecated.

Parse an XML document.

void

setDocumentHandler

​(

DocumentHandler

handler)

Deprecated.

Allow an application to register a document event handler.

void

setDTDHandler

​(

DTDHandler

handler)

Deprecated.

Allow an application to register a DTD event handler.

void

setEntityResolver

​(

EntityResolver

resolver)

Deprecated.

Allow an application to register a custom entity resolver.

void

setErrorHandler

​(

ErrorHandler

handler)

Deprecated.

Allow an application to register an error event handler.

void

setLocale

​(

Locale

locale)

Deprecated.

Allow an application to request a locale for errors and warnings.

---

#### Method Summary

Deprecated.

Parse an XML document from a system identifier (URI).

Parse an XML document.

Allow an application to register a document event handler.

Allow an application to register a DTD event handler.

Allow an application to register a custom entity resolver.

Allow an application to register an error event handler.

Allow an application to request a locale for errors and warnings.

============ METHOD DETAIL ==========

- Method Detail

- setLocale

```java
void setLocale​(
Locale
locale)
throws
SAXException
```

Deprecated.

Allow an application to request a locale for errors and warnings.

SAX parsers are not required to provide localisation for errors
and warnings; if they cannot support the requested locale,
however, they must throw a SAX exception. Applications may
not request a locale change in the middle of a parse.

**Parameters:** locale

- A Java Locale object.
**Throws:** SAXException

- Throws an exception
(using the previous or default locale) if the
requested locale is not supported.
**See Also:** SAXException

,

SAXParseException

- setEntityResolver

```java
void setEntityResolver​(
EntityResolver
resolver)
```

Deprecated.

Allow an application to register a custom entity resolver.

If the application does not register an entity resolver, the
SAX parser will resolve system identifiers and open connections
to entities itself (this is the default behaviour implemented in
HandlerBase).

Applications may register a new or different entity resolver
in the middle of a parse, and the SAX parser must begin using
the new resolver immediately.

**Parameters:** resolver

- The object for resolving entities.
**See Also:** EntityResolver

,

HandlerBase

- setDTDHandler

```java
void setDTDHandler​(
DTDHandler
handler)
```

Deprecated.

Allow an application to register a DTD event handler.

If the application does not register a DTD handler, all DTD
events reported by the SAX parser will be silently
ignored (this is the default behaviour implemented by
HandlerBase).

Applications may register a new or different
handler in the middle of a parse, and the SAX parser must
begin using the new handler immediately.

**Parameters:** handler

- The DTD handler.
**See Also:** DTDHandler

,

HandlerBase

- setDocumentHandler

```java
void setDocumentHandler​(
DocumentHandler
handler)
```

Deprecated.

Allow an application to register a document event handler.

If the application does not register a document handler, all
document events reported by the SAX parser will be silently
ignored (this is the default behaviour implemented by
HandlerBase).

Applications may register a new or different handler in the
middle of a parse, and the SAX parser must begin using the new
handler immediately.

**Parameters:** handler

- The document handler.
**See Also:** DocumentHandler

,

HandlerBase

- setErrorHandler

```java
void setErrorHandler​(
ErrorHandler
handler)
```

Deprecated.

Allow an application to register an error event handler.

If the application does not register an error event handler,
all error events reported by the SAX parser will be silently
ignored, except for fatalError, which will throw a SAXException
(this is the default behaviour implemented by HandlerBase).

Applications may register a new or different handler in the
middle of a parse, and the SAX parser must begin using the new
handler immediately.

**Parameters:** handler

- The error handler.
**See Also:** ErrorHandler

,

SAXException

,

HandlerBase

- parse

```java
void parse​(
InputSource
source)
throws
SAXException
,

IOException
```

Deprecated.

Parse an XML document.

The application can use this method to instruct the SAX parser
to begin parsing an XML document from any valid input
source (a character stream, a byte stream, or a URI).

Applications may not invoke this method while a parse is in
progress (they should create a new Parser instead for each
additional XML document). Once a parse is complete, an
application may reuse the same Parser object, possibly with a
different input source.

**Parameters:** source

- The input source for the top-level of the
XML document.
**Throws:** SAXException

- Any SAX exception, possibly
wrapping another exception.
**Throws:** IOException

- An IO exception from the parser,
possibly from a byte stream or character stream
supplied by the application.
**See Also:** InputSource

,

parse(java.lang.String)

,

setEntityResolver(org.xml.sax.EntityResolver)

,

setDTDHandler(org.xml.sax.DTDHandler)

,

setDocumentHandler(org.xml.sax.DocumentHandler)

,

setErrorHandler(org.xml.sax.ErrorHandler)

- parse

```java
void parse​(
String
systemId)
throws
SAXException
,

IOException
```

Deprecated.

Parse an XML document from a system identifier (URI).

This method is a shortcut for the common case of reading a
document from a system identifier. It is the exact
equivalent of the following:

```java
parse(new InputSource(systemId));
```

If the system identifier is a URL, it must be fully resolved
by the application before it is passed to the parser.

**Parameters:** systemId

- The system identifier (URI).
**Throws:** SAXException

- Any SAX exception, possibly
wrapping another exception.
**Throws:** IOException

- An IO exception from the parser,
possibly from a byte stream or character stream
supplied by the application.
**See Also:** parse(org.xml.sax.InputSource)

Method Detail

- setLocale

```java
void setLocale​(
Locale
locale)
throws
SAXException
```

Deprecated.

Allow an application to request a locale for errors and warnings.

SAX parsers are not required to provide localisation for errors
and warnings; if they cannot support the requested locale,
however, they must throw a SAX exception. Applications may
not request a locale change in the middle of a parse.

**Parameters:** locale

- A Java Locale object.
**Throws:** SAXException

- Throws an exception
(using the previous or default locale) if the
requested locale is not supported.
**See Also:** SAXException

,

SAXParseException

- setEntityResolver

```java
void setEntityResolver​(
EntityResolver
resolver)
```

Deprecated.

Allow an application to register a custom entity resolver.

If the application does not register an entity resolver, the
SAX parser will resolve system identifiers and open connections
to entities itself (this is the default behaviour implemented in
HandlerBase).

Applications may register a new or different entity resolver
in the middle of a parse, and the SAX parser must begin using
the new resolver immediately.

**Parameters:** resolver

- The object for resolving entities.
**See Also:** EntityResolver

,

HandlerBase

- setDTDHandler

```java
void setDTDHandler​(
DTDHandler
handler)
```

Deprecated.

Allow an application to register a DTD event handler.

If the application does not register a DTD handler, all DTD
events reported by the SAX parser will be silently
ignored (this is the default behaviour implemented by
HandlerBase).

Applications may register a new or different
handler in the middle of a parse, and the SAX parser must
begin using the new handler immediately.

**Parameters:** handler

- The DTD handler.
**See Also:** DTDHandler

,

HandlerBase

- setDocumentHandler

```java
void setDocumentHandler​(
DocumentHandler
handler)
```

Deprecated.

Allow an application to register a document event handler.

If the application does not register a document handler, all
document events reported by the SAX parser will be silently
ignored (this is the default behaviour implemented by
HandlerBase).

Applications may register a new or different handler in the
middle of a parse, and the SAX parser must begin using the new
handler immediately.

**Parameters:** handler

- The document handler.
**See Also:** DocumentHandler

,

HandlerBase

- setErrorHandler

```java
void setErrorHandler​(
ErrorHandler
handler)
```

Deprecated.

Allow an application to register an error event handler.

If the application does not register an error event handler,
all error events reported by the SAX parser will be silently
ignored, except for fatalError, which will throw a SAXException
(this is the default behaviour implemented by HandlerBase).

Applications may register a new or different handler in the
middle of a parse, and the SAX parser must begin using the new
handler immediately.

**Parameters:** handler

- The error handler.
**See Also:** ErrorHandler

,

SAXException

,

HandlerBase

- parse

```java
void parse​(
InputSource
source)
throws
SAXException
,

IOException
```

Deprecated.

Parse an XML document.

The application can use this method to instruct the SAX parser
to begin parsing an XML document from any valid input
source (a character stream, a byte stream, or a URI).

Applications may not invoke this method while a parse is in
progress (they should create a new Parser instead for each
additional XML document). Once a parse is complete, an
application may reuse the same Parser object, possibly with a
different input source.

**Parameters:** source

- The input source for the top-level of the
XML document.
**Throws:** SAXException

- Any SAX exception, possibly
wrapping another exception.
**Throws:** IOException

- An IO exception from the parser,
possibly from a byte stream or character stream
supplied by the application.
**See Also:** InputSource

,

parse(java.lang.String)

,

setEntityResolver(org.xml.sax.EntityResolver)

,

setDTDHandler(org.xml.sax.DTDHandler)

,

setDocumentHandler(org.xml.sax.DocumentHandler)

,

setErrorHandler(org.xml.sax.ErrorHandler)

- parse

```java
void parse​(
String
systemId)
throws
SAXException
,

IOException
```

Deprecated.

Parse an XML document from a system identifier (URI).

This method is a shortcut for the common case of reading a
document from a system identifier. It is the exact
equivalent of the following:

```java
parse(new InputSource(systemId));
```

If the system identifier is a URL, it must be fully resolved
by the application before it is passed to the parser.

**Parameters:** systemId

- The system identifier (URI).
**Throws:** SAXException

- Any SAX exception, possibly
wrapping another exception.
**Throws:** IOException

- An IO exception from the parser,
possibly from a byte stream or character stream
supplied by the application.
**See Also:** parse(org.xml.sax.InputSource)

---

#### Method Detail

setLocale

```java
void setLocale​(
Locale
locale)
throws
SAXException
```

Deprecated.

Allow an application to request a locale for errors and warnings.

SAX parsers are not required to provide localisation for errors
and warnings; if they cannot support the requested locale,
however, they must throw a SAX exception. Applications may
not request a locale change in the middle of a parse.

**Parameters:** locale

- A Java Locale object.
**Throws:** SAXException

- Throws an exception
(using the previous or default locale) if the
requested locale is not supported.
**See Also:** SAXException

,

SAXParseException

---

#### setLocale

void setLocale​(

Locale

locale)
throws

SAXException

Allow an application to request a locale for errors and warnings.

SAX parsers are not required to provide localisation for errors
and warnings; if they cannot support the requested locale,
however, they must throw a SAX exception. Applications may
not request a locale change in the middle of a parse.

SAX parsers are not required to provide localisation for errors
and warnings; if they cannot support the requested locale,
however, they must throw a SAX exception. Applications may
not request a locale change in the middle of a parse.

setEntityResolver

```java
void setEntityResolver​(
EntityResolver
resolver)
```

Deprecated.

Allow an application to register a custom entity resolver.

If the application does not register an entity resolver, the
SAX parser will resolve system identifiers and open connections
to entities itself (this is the default behaviour implemented in
HandlerBase).

Applications may register a new or different entity resolver
in the middle of a parse, and the SAX parser must begin using
the new resolver immediately.

**Parameters:** resolver

- The object for resolving entities.
**See Also:** EntityResolver

,

HandlerBase

---

#### setEntityResolver

void setEntityResolver​(

EntityResolver

resolver)

Allow an application to register a custom entity resolver.

If the application does not register an entity resolver, the
SAX parser will resolve system identifiers and open connections
to entities itself (this is the default behaviour implemented in
HandlerBase).

Applications may register a new or different entity resolver
in the middle of a parse, and the SAX parser must begin using
the new resolver immediately.

If the application does not register an entity resolver, the
SAX parser will resolve system identifiers and open connections
to entities itself (this is the default behaviour implemented in
HandlerBase).

Applications may register a new or different entity resolver
in the middle of a parse, and the SAX parser must begin using
the new resolver immediately.

setDTDHandler

```java
void setDTDHandler​(
DTDHandler
handler)
```

Deprecated.

Allow an application to register a DTD event handler.

If the application does not register a DTD handler, all DTD
events reported by the SAX parser will be silently
ignored (this is the default behaviour implemented by
HandlerBase).

Applications may register a new or different
handler in the middle of a parse, and the SAX parser must
begin using the new handler immediately.

**Parameters:** handler

- The DTD handler.
**See Also:** DTDHandler

,

HandlerBase

---

#### setDTDHandler

void setDTDHandler​(

DTDHandler

handler)

Allow an application to register a DTD event handler.

If the application does not register a DTD handler, all DTD
events reported by the SAX parser will be silently
ignored (this is the default behaviour implemented by
HandlerBase).

Applications may register a new or different
handler in the middle of a parse, and the SAX parser must
begin using the new handler immediately.

If the application does not register a DTD handler, all DTD
events reported by the SAX parser will be silently
ignored (this is the default behaviour implemented by
HandlerBase).

Applications may register a new or different
handler in the middle of a parse, and the SAX parser must
begin using the new handler immediately.

setDocumentHandler

```java
void setDocumentHandler​(
DocumentHandler
handler)
```

Deprecated.

Allow an application to register a document event handler.

If the application does not register a document handler, all
document events reported by the SAX parser will be silently
ignored (this is the default behaviour implemented by
HandlerBase).

Applications may register a new or different handler in the
middle of a parse, and the SAX parser must begin using the new
handler immediately.

**Parameters:** handler

- The document handler.
**See Also:** DocumentHandler

,

HandlerBase

---

#### setDocumentHandler

void setDocumentHandler​(

DocumentHandler

handler)

Allow an application to register a document event handler.

If the application does not register a document handler, all
document events reported by the SAX parser will be silently
ignored (this is the default behaviour implemented by
HandlerBase).

Applications may register a new or different handler in the
middle of a parse, and the SAX parser must begin using the new
handler immediately.

If the application does not register a document handler, all
document events reported by the SAX parser will be silently
ignored (this is the default behaviour implemented by
HandlerBase).

Applications may register a new or different handler in the
middle of a parse, and the SAX parser must begin using the new
handler immediately.

setErrorHandler

```java
void setErrorHandler​(
ErrorHandler
handler)
```

Deprecated.

Allow an application to register an error event handler.

If the application does not register an error event handler,
all error events reported by the SAX parser will be silently
ignored, except for fatalError, which will throw a SAXException
(this is the default behaviour implemented by HandlerBase).

Applications may register a new or different handler in the
middle of a parse, and the SAX parser must begin using the new
handler immediately.

**Parameters:** handler

- The error handler.
**See Also:** ErrorHandler

,

SAXException

,

HandlerBase

---

#### setErrorHandler

void setErrorHandler​(

ErrorHandler

handler)

Allow an application to register an error event handler.

If the application does not register an error event handler,
all error events reported by the SAX parser will be silently
ignored, except for fatalError, which will throw a SAXException
(this is the default behaviour implemented by HandlerBase).

Applications may register a new or different handler in the
middle of a parse, and the SAX parser must begin using the new
handler immediately.

If the application does not register an error event handler,
all error events reported by the SAX parser will be silently
ignored, except for fatalError, which will throw a SAXException
(this is the default behaviour implemented by HandlerBase).

Applications may register a new or different handler in the
middle of a parse, and the SAX parser must begin using the new
handler immediately.

parse

```java
void parse​(
InputSource
source)
throws
SAXException
,

IOException
```

Deprecated.

Parse an XML document.

The application can use this method to instruct the SAX parser
to begin parsing an XML document from any valid input
source (a character stream, a byte stream, or a URI).

Applications may not invoke this method while a parse is in
progress (they should create a new Parser instead for each
additional XML document). Once a parse is complete, an
application may reuse the same Parser object, possibly with a
different input source.

**Parameters:** source

- The input source for the top-level of the
XML document.
**Throws:** SAXException

- Any SAX exception, possibly
wrapping another exception.
**Throws:** IOException

- An IO exception from the parser,
possibly from a byte stream or character stream
supplied by the application.
**See Also:** InputSource

,

parse(java.lang.String)

,

setEntityResolver(org.xml.sax.EntityResolver)

,

setDTDHandler(org.xml.sax.DTDHandler)

,

setDocumentHandler(org.xml.sax.DocumentHandler)

,

setErrorHandler(org.xml.sax.ErrorHandler)

---

#### parse

void parse​(

InputSource

source)
throws

SAXException

,

IOException

Parse an XML document.

The application can use this method to instruct the SAX parser
to begin parsing an XML document from any valid input
source (a character stream, a byte stream, or a URI).

Applications may not invoke this method while a parse is in
progress (they should create a new Parser instead for each
additional XML document). Once a parse is complete, an
application may reuse the same Parser object, possibly with a
different input source.

The application can use this method to instruct the SAX parser
to begin parsing an XML document from any valid input
source (a character stream, a byte stream, or a URI).

Applications may not invoke this method while a parse is in
progress (they should create a new Parser instead for each
additional XML document). Once a parse is complete, an
application may reuse the same Parser object, possibly with a
different input source.

parse

```java
void parse​(
String
systemId)
throws
SAXException
,

IOException
```

Deprecated.

Parse an XML document from a system identifier (URI).

This method is a shortcut for the common case of reading a
document from a system identifier. It is the exact
equivalent of the following:

```java
parse(new InputSource(systemId));
```

If the system identifier is a URL, it must be fully resolved
by the application before it is passed to the parser.

**Parameters:** systemId

- The system identifier (URI).
**Throws:** SAXException

- Any SAX exception, possibly
wrapping another exception.
**Throws:** IOException

- An IO exception from the parser,
possibly from a byte stream or character stream
supplied by the application.
**See Also:** parse(org.xml.sax.InputSource)

---

#### parse

void parse​(

String

systemId)
throws

SAXException

,

IOException

Parse an XML document from a system identifier (URI).

This method is a shortcut for the common case of reading a
document from a system identifier. It is the exact
equivalent of the following:

```java
parse(new InputSource(systemId));
```

If the system identifier is a URL, it must be fully resolved
by the application before it is passed to the parser.

This method is a shortcut for the common case of reading a
document from a system identifier. It is the exact
equivalent of the following:

parse(new InputSource(systemId));

If the system identifier is a URL, it must be fully resolved
by the application before it is passed to the parser.

---

