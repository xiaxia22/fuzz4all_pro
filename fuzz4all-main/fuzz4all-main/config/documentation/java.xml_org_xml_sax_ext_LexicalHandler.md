# Interface LexicalHandler

**Source:** `java.xml\org\xml\sax\ext\LexicalHandler.html`

### Class Description

```java
public interface
LexicalHandler
```

SAX2 extension handler for lexical events.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

This is an optional extension handler for SAX2 to provide
lexical information about an XML document, such as comments
and CDATA section boundaries.
XML readers are not required to recognize this handler, and it
is not part of core-only SAX2 distributions.

The events in the lexical handler apply to the entire document,
not just to the document element, and all lexical handler events
must appear between the content handler's startDocument and
endDocument events.

To set the LexicalHandler for an XML reader, use the

setProperty

method
with the property name

http://xml.org/sax/properties/lexical-handler

and an object implementing this interface (or null) as the value.
If the reader does not report lexical events, it will throw a

SAXNotRecognizedException

when you attempt to register the handler.

**All Known Subinterfaces:** TransformerHandler

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void startDTD​(
String
name,

String
publicId,

String
systemId)
throws
SAXException

Report the start of DTD declarations, if any.

This method is intended to report the beginning of the
DOCTYPE declaration; if the document has no DOCTYPE declaration,
this method will not be invoked.

All declarations reported through

DTDHandler

or

DeclHandler

events must appear
between the startDTD and

endDTD

events.
Declarations are assumed to belong to the internal DTD subset
unless they appear between

startEntity

and

endEntity

events. Comments and
processing instructions from the DTD should also be reported
between the startDTD and endDTD events, in their original
order of (logical) occurrence; they are not required to
appear in their correct locations relative to DTDHandler
or DeclHandler events, however.

Note that the start/endDTD events will appear within
the start/endDocument events from ContentHandler and
before the first

startElement

event.

**Parameters:**
- name

- The document type name.
- publicId

- The declared public identifier for the
external DTD subset, or null if none was declared.
- systemId

- The declared system identifier for the
external DTD subset, or null if none was declared.
(Note that this is not resolved against the document
base URI.)

**Throws:**
- SAXException

- The application may raise an
exception.

**See Also:**
- endDTD()

,

startEntity(java.lang.String)

---

#### void endDTD()
throws
SAXException

Report the end of DTD declarations.

This method is intended to report the end of the
DOCTYPE declaration; if the document has no DOCTYPE declaration,
this method will not be invoked.

**Throws:**
- SAXException

- The application may raise an exception.

**See Also:**
- startDTD(java.lang.String, java.lang.String, java.lang.String)

---

#### void startEntity​(
String
name)
throws
SAXException

Report the beginning of some internal and external XML entities.

The reporting of parameter entities (including
the external DTD subset) is optional, and SAX2 drivers that
report LexicalHandler events may not implement it; you can use the

http://xml.org/sax/features/lexical-handler/parameter-entities

feature to query or control the reporting of parameter entities.

General entities are reported with their regular names,
parameter entities have '%' prepended to their names, and
the external DTD subset has the pseudo-entity name "[dtd]".

When a SAX2 driver is providing these events, all other
events must be properly nested within start/end entity
events. There is no additional requirement that events from

DeclHandler

or

DTDHandler

be properly ordered.

Note that skipped entities will be reported through the

skippedEntity

event, which is part of the ContentHandler interface.

Because of the streaming event model that SAX uses, some
entity boundaries cannot be reported under any
circumstances:

- general entities within attribute values
- parameter entities within declarations

These will be silently expanded, with no indication of where
the original entity boundaries were.

Note also that the boundaries of character references (which
are not really entities anyway) are not reported.

All start/endEntity events must be properly nested.

**Parameters:**
- name

- The name of the entity. If it is a parameter
entity, the name will begin with '%', and if it is the
external DTD subset, it will be "[dtd]".

**Throws:**
- SAXException

- The application may raise an exception.

**See Also:**
- endEntity(java.lang.String)

,

DeclHandler.internalEntityDecl(java.lang.String, java.lang.String)

,

DeclHandler.externalEntityDecl(java.lang.String, java.lang.String, java.lang.String)

---

#### void endEntity​(
String
name)
throws
SAXException

Report the end of an entity.

**Parameters:**
- name

- The name of the entity that is ending.

**Throws:**
- SAXException

- The application may raise an exception.

**See Also:**
- startEntity(java.lang.String)

---

#### void startCDATA()
throws
SAXException

Report the start of a CDATA section.

The contents of the CDATA section will be reported through
the regular

characters

event; this event is intended only to report
the boundary.

**Throws:**
- SAXException

- The application may raise an exception.

**See Also:**
- endCDATA()

---

#### void endCDATA()
throws
SAXException

Report the end of a CDATA section.

**Throws:**
- SAXException

- The application may raise an exception.

**See Also:**
- startCDATA()

---

#### void comment​(char[] ch,
int start,
int length)
throws
SAXException

Report an XML comment anywhere in the document.

This callback will be used for comments inside or outside the
document element, including comments in the external DTD
subset (if read). Comments in the DTD must be properly
nested inside start/endDTD and start/endEntity events (if
used).

**Parameters:**
- ch

- An array holding the characters in the comment.
- start

- The starting position in the array.
- length

- The number of characters to use from the array.

**Throws:**
- SAXException

- The application may raise an exception.

---

### Additional Sections

#### Interface LexicalHandler

**All Known Subinterfaces:** TransformerHandler

**All Known Implementing Classes:** DefaultHandler2

```java
public interface
LexicalHandler
```

SAX2 extension handler for lexical events.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

This is an optional extension handler for SAX2 to provide
lexical information about an XML document, such as comments
and CDATA section boundaries.
XML readers are not required to recognize this handler, and it
is not part of core-only SAX2 distributions.

The events in the lexical handler apply to the entire document,
not just to the document element, and all lexical handler events
must appear between the content handler's startDocument and
endDocument events.

To set the LexicalHandler for an XML reader, use the

setProperty

method
with the property name

http://xml.org/sax/properties/lexical-handler

and an object implementing this interface (or null) as the value.
If the reader does not report lexical events, it will throw a

SAXNotRecognizedException

when you attempt to register the handler.

**Since:** 1.4, SAX 2.0 (extensions 1.0)

public interface

LexicalHandler

SAX2 extension handler for lexical events.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

This is an optional extension handler for SAX2 to provide
lexical information about an XML document, such as comments
and CDATA section boundaries.
XML readers are not required to recognize this handler, and it
is not part of core-only SAX2 distributions.

The events in the lexical handler apply to the entire document,
not just to the document element, and all lexical handler events
must appear between the content handler's startDocument and
endDocument events.

To set the LexicalHandler for an XML reader, use the

setProperty

method
with the property name

http://xml.org/sax/properties/lexical-handler

and an object implementing this interface (or null) as the value.
If the reader does not report lexical events, it will throw a

SAXNotRecognizedException

when you attempt to register the handler.

This is an optional extension handler for SAX2 to provide
lexical information about an XML document, such as comments
and CDATA section boundaries.
XML readers are not required to recognize this handler, and it
is not part of core-only SAX2 distributions.

The events in the lexical handler apply to the entire document,
not just to the document element, and all lexical handler events
must appear between the content handler's startDocument and
endDocument events.

To set the LexicalHandler for an XML reader, use the

setProperty

method
with the property name

http://xml.org/sax/properties/lexical-handler

and an object implementing this interface (or null) as the value.
If the reader does not report lexical events, it will throw a

SAXNotRecognizedException

when you attempt to register the handler.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

comment

​(char[] ch,
int start,
int length)

Report an XML comment anywhere in the document.

void

endCDATA

()

Report the end of a CDATA section.

void

endDTD

()

Report the end of DTD declarations.

void

endEntity

​(

String

name)

Report the end of an entity.

void

startCDATA

()

Report the start of a CDATA section.

void

startDTD

​(

String

name,

String

publicId,

String

systemId)

Report the start of DTD declarations, if any.

void

startEntity

​(

String

name)

Report the beginning of some internal and external XML entities.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

comment

​(char[] ch,
int start,
int length)

Report an XML comment anywhere in the document.

void

endCDATA

()

Report the end of a CDATA section.

void

endDTD

()

Report the end of DTD declarations.

void

endEntity

​(

String

name)

Report the end of an entity.

void

startCDATA

()

Report the start of a CDATA section.

void

startDTD

​(

String

name,

String

publicId,

String

systemId)

Report the start of DTD declarations, if any.

void

startEntity

​(

String

name)

Report the beginning of some internal and external XML entities.

---

#### Method Summary

Report an XML comment anywhere in the document.

Report the end of a CDATA section.

Report the end of DTD declarations.

Report the end of an entity.

Report the start of a CDATA section.

Report the start of DTD declarations, if any.

Report the beginning of some internal and external XML entities.

============ METHOD DETAIL ==========

- Method Detail

- startDTD

```java
void startDTD​(
String
name,

String
publicId,

String
systemId)
throws
SAXException
```

Report the start of DTD declarations, if any.

This method is intended to report the beginning of the
DOCTYPE declaration; if the document has no DOCTYPE declaration,
this method will not be invoked.

All declarations reported through

DTDHandler

or

DeclHandler

events must appear
between the startDTD and

endDTD

events.
Declarations are assumed to belong to the internal DTD subset
unless they appear between

startEntity

and

endEntity

events. Comments and
processing instructions from the DTD should also be reported
between the startDTD and endDTD events, in their original
order of (logical) occurrence; they are not required to
appear in their correct locations relative to DTDHandler
or DeclHandler events, however.

Note that the start/endDTD events will appear within
the start/endDocument events from ContentHandler and
before the first

startElement

event.

**Parameters:** name

- The document type name.
**Parameters:** publicId

- The declared public identifier for the
external DTD subset, or null if none was declared.
**Parameters:** systemId

- The declared system identifier for the
external DTD subset, or null if none was declared.
(Note that this is not resolved against the document
base URI.)
**Throws:** SAXException

- The application may raise an
exception.
**See Also:** endDTD()

,

startEntity(java.lang.String)

- endDTD

```java
void endDTD()
throws
SAXException
```

Report the end of DTD declarations.

This method is intended to report the end of the
DOCTYPE declaration; if the document has no DOCTYPE declaration,
this method will not be invoked.

**Throws:** SAXException

- The application may raise an exception.
**See Also:** startDTD(java.lang.String, java.lang.String, java.lang.String)

- startEntity

```java
void startEntity​(
String
name)
throws
SAXException
```

Report the beginning of some internal and external XML entities.

The reporting of parameter entities (including
the external DTD subset) is optional, and SAX2 drivers that
report LexicalHandler events may not implement it; you can use the

http://xml.org/sax/features/lexical-handler/parameter-entities

feature to query or control the reporting of parameter entities.

General entities are reported with their regular names,
parameter entities have '%' prepended to their names, and
the external DTD subset has the pseudo-entity name "[dtd]".

When a SAX2 driver is providing these events, all other
events must be properly nested within start/end entity
events. There is no additional requirement that events from

DeclHandler

or

DTDHandler

be properly ordered.

Note that skipped entities will be reported through the

skippedEntity

event, which is part of the ContentHandler interface.

Because of the streaming event model that SAX uses, some
entity boundaries cannot be reported under any
circumstances:

- general entities within attribute values
- parameter entities within declarations

These will be silently expanded, with no indication of where
the original entity boundaries were.

Note also that the boundaries of character references (which
are not really entities anyway) are not reported.

All start/endEntity events must be properly nested.

**Parameters:** name

- The name of the entity. If it is a parameter
entity, the name will begin with '%', and if it is the
external DTD subset, it will be "[dtd]".
**Throws:** SAXException

- The application may raise an exception.
**See Also:** endEntity(java.lang.String)

,

DeclHandler.internalEntityDecl(java.lang.String, java.lang.String)

,

DeclHandler.externalEntityDecl(java.lang.String, java.lang.String, java.lang.String)

- endEntity

```java
void endEntity​(
String
name)
throws
SAXException
```

Report the end of an entity.

**Parameters:** name

- The name of the entity that is ending.
**Throws:** SAXException

- The application may raise an exception.
**See Also:** startEntity(java.lang.String)

- startCDATA

```java
void startCDATA()
throws
SAXException
```

Report the start of a CDATA section.

The contents of the CDATA section will be reported through
the regular

characters

event; this event is intended only to report
the boundary.

**Throws:** SAXException

- The application may raise an exception.
**See Also:** endCDATA()

- endCDATA

```java
void endCDATA()
throws
SAXException
```

Report the end of a CDATA section.

**Throws:** SAXException

- The application may raise an exception.
**See Also:** startCDATA()

- comment

```java
void comment​(char[] ch,
int start,
int length)
throws
SAXException
```

Report an XML comment anywhere in the document.

This callback will be used for comments inside or outside the
document element, including comments in the external DTD
subset (if read). Comments in the DTD must be properly
nested inside start/endDTD and start/endEntity events (if
used).

**Parameters:** ch

- An array holding the characters in the comment.
**Parameters:** start

- The starting position in the array.
**Parameters:** length

- The number of characters to use from the array.
**Throws:** SAXException

- The application may raise an exception.

Method Detail

- startDTD

```java
void startDTD​(
String
name,

String
publicId,

String
systemId)
throws
SAXException
```

Report the start of DTD declarations, if any.

This method is intended to report the beginning of the
DOCTYPE declaration; if the document has no DOCTYPE declaration,
this method will not be invoked.

All declarations reported through

DTDHandler

or

DeclHandler

events must appear
between the startDTD and

endDTD

events.
Declarations are assumed to belong to the internal DTD subset
unless they appear between

startEntity

and

endEntity

events. Comments and
processing instructions from the DTD should also be reported
between the startDTD and endDTD events, in their original
order of (logical) occurrence; they are not required to
appear in their correct locations relative to DTDHandler
or DeclHandler events, however.

Note that the start/endDTD events will appear within
the start/endDocument events from ContentHandler and
before the first

startElement

event.

**Parameters:** name

- The document type name.
**Parameters:** publicId

- The declared public identifier for the
external DTD subset, or null if none was declared.
**Parameters:** systemId

- The declared system identifier for the
external DTD subset, or null if none was declared.
(Note that this is not resolved against the document
base URI.)
**Throws:** SAXException

- The application may raise an
exception.
**See Also:** endDTD()

,

startEntity(java.lang.String)

- endDTD

```java
void endDTD()
throws
SAXException
```

Report the end of DTD declarations.

This method is intended to report the end of the
DOCTYPE declaration; if the document has no DOCTYPE declaration,
this method will not be invoked.

**Throws:** SAXException

- The application may raise an exception.
**See Also:** startDTD(java.lang.String, java.lang.String, java.lang.String)

- startEntity

```java
void startEntity​(
String
name)
throws
SAXException
```

Report the beginning of some internal and external XML entities.

The reporting of parameter entities (including
the external DTD subset) is optional, and SAX2 drivers that
report LexicalHandler events may not implement it; you can use the

http://xml.org/sax/features/lexical-handler/parameter-entities

feature to query or control the reporting of parameter entities.

General entities are reported with their regular names,
parameter entities have '%' prepended to their names, and
the external DTD subset has the pseudo-entity name "[dtd]".

When a SAX2 driver is providing these events, all other
events must be properly nested within start/end entity
events. There is no additional requirement that events from

DeclHandler

or

DTDHandler

be properly ordered.

Note that skipped entities will be reported through the

skippedEntity

event, which is part of the ContentHandler interface.

Because of the streaming event model that SAX uses, some
entity boundaries cannot be reported under any
circumstances:

- general entities within attribute values
- parameter entities within declarations

These will be silently expanded, with no indication of where
the original entity boundaries were.

Note also that the boundaries of character references (which
are not really entities anyway) are not reported.

All start/endEntity events must be properly nested.

**Parameters:** name

- The name of the entity. If it is a parameter
entity, the name will begin with '%', and if it is the
external DTD subset, it will be "[dtd]".
**Throws:** SAXException

- The application may raise an exception.
**See Also:** endEntity(java.lang.String)

,

DeclHandler.internalEntityDecl(java.lang.String, java.lang.String)

,

DeclHandler.externalEntityDecl(java.lang.String, java.lang.String, java.lang.String)

- endEntity

```java
void endEntity​(
String
name)
throws
SAXException
```

Report the end of an entity.

**Parameters:** name

- The name of the entity that is ending.
**Throws:** SAXException

- The application may raise an exception.
**See Also:** startEntity(java.lang.String)

- startCDATA

```java
void startCDATA()
throws
SAXException
```

Report the start of a CDATA section.

The contents of the CDATA section will be reported through
the regular

characters

event; this event is intended only to report
the boundary.

**Throws:** SAXException

- The application may raise an exception.
**See Also:** endCDATA()

- endCDATA

```java
void endCDATA()
throws
SAXException
```

Report the end of a CDATA section.

**Throws:** SAXException

- The application may raise an exception.
**See Also:** startCDATA()

- comment

```java
void comment​(char[] ch,
int start,
int length)
throws
SAXException
```

Report an XML comment anywhere in the document.

This callback will be used for comments inside or outside the
document element, including comments in the external DTD
subset (if read). Comments in the DTD must be properly
nested inside start/endDTD and start/endEntity events (if
used).

**Parameters:** ch

- An array holding the characters in the comment.
**Parameters:** start

- The starting position in the array.
**Parameters:** length

- The number of characters to use from the array.
**Throws:** SAXException

- The application may raise an exception.

---

#### Method Detail

startDTD

```java
void startDTD​(
String
name,

String
publicId,

String
systemId)
throws
SAXException
```

Report the start of DTD declarations, if any.

This method is intended to report the beginning of the
DOCTYPE declaration; if the document has no DOCTYPE declaration,
this method will not be invoked.

All declarations reported through

DTDHandler

or

DeclHandler

events must appear
between the startDTD and

endDTD

events.
Declarations are assumed to belong to the internal DTD subset
unless they appear between

startEntity

and

endEntity

events. Comments and
processing instructions from the DTD should also be reported
between the startDTD and endDTD events, in their original
order of (logical) occurrence; they are not required to
appear in their correct locations relative to DTDHandler
or DeclHandler events, however.

Note that the start/endDTD events will appear within
the start/endDocument events from ContentHandler and
before the first

startElement

event.

**Parameters:** name

- The document type name.
**Parameters:** publicId

- The declared public identifier for the
external DTD subset, or null if none was declared.
**Parameters:** systemId

- The declared system identifier for the
external DTD subset, or null if none was declared.
(Note that this is not resolved against the document
base URI.)
**Throws:** SAXException

- The application may raise an
exception.
**See Also:** endDTD()

,

startEntity(java.lang.String)

---

#### startDTD

void startDTD​(

String

name,

String

publicId,

String

systemId)
throws

SAXException

Report the start of DTD declarations, if any.

This method is intended to report the beginning of the
DOCTYPE declaration; if the document has no DOCTYPE declaration,
this method will not be invoked.

All declarations reported through

DTDHandler

or

DeclHandler

events must appear
between the startDTD and

endDTD

events.
Declarations are assumed to belong to the internal DTD subset
unless they appear between

startEntity

and

endEntity

events. Comments and
processing instructions from the DTD should also be reported
between the startDTD and endDTD events, in their original
order of (logical) occurrence; they are not required to
appear in their correct locations relative to DTDHandler
or DeclHandler events, however.

Note that the start/endDTD events will appear within
the start/endDocument events from ContentHandler and
before the first

startElement

event.

This method is intended to report the beginning of the
DOCTYPE declaration; if the document has no DOCTYPE declaration,
this method will not be invoked.

All declarations reported through

DTDHandler

or

DeclHandler

events must appear
between the startDTD and

endDTD

events.
Declarations are assumed to belong to the internal DTD subset
unless they appear between

startEntity

and

endEntity

events. Comments and
processing instructions from the DTD should also be reported
between the startDTD and endDTD events, in their original
order of (logical) occurrence; they are not required to
appear in their correct locations relative to DTDHandler
or DeclHandler events, however.

Note that the start/endDTD events will appear within
the start/endDocument events from ContentHandler and
before the first

startElement

event.

endDTD

```java
void endDTD()
throws
SAXException
```

Report the end of DTD declarations.

This method is intended to report the end of the
DOCTYPE declaration; if the document has no DOCTYPE declaration,
this method will not be invoked.

**Throws:** SAXException

- The application may raise an exception.
**See Also:** startDTD(java.lang.String, java.lang.String, java.lang.String)

---

#### endDTD

void endDTD()
throws

SAXException

Report the end of DTD declarations.

This method is intended to report the end of the
DOCTYPE declaration; if the document has no DOCTYPE declaration,
this method will not be invoked.

This method is intended to report the end of the
DOCTYPE declaration; if the document has no DOCTYPE declaration,
this method will not be invoked.

startEntity

```java
void startEntity​(
String
name)
throws
SAXException
```

Report the beginning of some internal and external XML entities.

The reporting of parameter entities (including
the external DTD subset) is optional, and SAX2 drivers that
report LexicalHandler events may not implement it; you can use the

http://xml.org/sax/features/lexical-handler/parameter-entities

feature to query or control the reporting of parameter entities.

General entities are reported with their regular names,
parameter entities have '%' prepended to their names, and
the external DTD subset has the pseudo-entity name "[dtd]".

When a SAX2 driver is providing these events, all other
events must be properly nested within start/end entity
events. There is no additional requirement that events from

DeclHandler

or

DTDHandler

be properly ordered.

Note that skipped entities will be reported through the

skippedEntity

event, which is part of the ContentHandler interface.

Because of the streaming event model that SAX uses, some
entity boundaries cannot be reported under any
circumstances:

- general entities within attribute values
- parameter entities within declarations

These will be silently expanded, with no indication of where
the original entity boundaries were.

Note also that the boundaries of character references (which
are not really entities anyway) are not reported.

All start/endEntity events must be properly nested.

**Parameters:** name

- The name of the entity. If it is a parameter
entity, the name will begin with '%', and if it is the
external DTD subset, it will be "[dtd]".
**Throws:** SAXException

- The application may raise an exception.
**See Also:** endEntity(java.lang.String)

,

DeclHandler.internalEntityDecl(java.lang.String, java.lang.String)

,

DeclHandler.externalEntityDecl(java.lang.String, java.lang.String, java.lang.String)

---

#### startEntity

void startEntity​(

String

name)
throws

SAXException

Report the beginning of some internal and external XML entities.

The reporting of parameter entities (including
the external DTD subset) is optional, and SAX2 drivers that
report LexicalHandler events may not implement it; you can use the

http://xml.org/sax/features/lexical-handler/parameter-entities

feature to query or control the reporting of parameter entities.

General entities are reported with their regular names,
parameter entities have '%' prepended to their names, and
the external DTD subset has the pseudo-entity name "[dtd]".

When a SAX2 driver is providing these events, all other
events must be properly nested within start/end entity
events. There is no additional requirement that events from

DeclHandler

or

DTDHandler

be properly ordered.

Note that skipped entities will be reported through the

skippedEntity

event, which is part of the ContentHandler interface.

Because of the streaming event model that SAX uses, some
entity boundaries cannot be reported under any
circumstances:

- general entities within attribute values
- parameter entities within declarations

These will be silently expanded, with no indication of where
the original entity boundaries were.

Note also that the boundaries of character references (which
are not really entities anyway) are not reported.

All start/endEntity events must be properly nested.

The reporting of parameter entities (including
the external DTD subset) is optional, and SAX2 drivers that
report LexicalHandler events may not implement it; you can use the

http://xml.org/sax/features/lexical-handler/parameter-entities

feature to query or control the reporting of parameter entities.

General entities are reported with their regular names,
parameter entities have '%' prepended to their names, and
the external DTD subset has the pseudo-entity name "[dtd]".

When a SAX2 driver is providing these events, all other
events must be properly nested within start/end entity
events. There is no additional requirement that events from

DeclHandler

or

DTDHandler

be properly ordered.

Note that skipped entities will be reported through the

skippedEntity

event, which is part of the ContentHandler interface.

Because of the streaming event model that SAX uses, some
entity boundaries cannot be reported under any
circumstances:

general entities within attribute values

parameter entities within declarations

These will be silently expanded, with no indication of where
the original entity boundaries were.

Note also that the boundaries of character references (which
are not really entities anyway) are not reported.

All start/endEntity events must be properly nested.

endEntity

```java
void endEntity​(
String
name)
throws
SAXException
```

Report the end of an entity.

**Parameters:** name

- The name of the entity that is ending.
**Throws:** SAXException

- The application may raise an exception.
**See Also:** startEntity(java.lang.String)

---

#### endEntity

void endEntity​(

String

name)
throws

SAXException

Report the end of an entity.

startCDATA

```java
void startCDATA()
throws
SAXException
```

Report the start of a CDATA section.

The contents of the CDATA section will be reported through
the regular

characters

event; this event is intended only to report
the boundary.

**Throws:** SAXException

- The application may raise an exception.
**See Also:** endCDATA()

---

#### startCDATA

void startCDATA()
throws

SAXException

Report the start of a CDATA section.

The contents of the CDATA section will be reported through
the regular

characters

event; this event is intended only to report
the boundary.

The contents of the CDATA section will be reported through
the regular

characters

event; this event is intended only to report
the boundary.

endCDATA

```java
void endCDATA()
throws
SAXException
```

Report the end of a CDATA section.

**Throws:** SAXException

- The application may raise an exception.
**See Also:** startCDATA()

---

#### endCDATA

void endCDATA()
throws

SAXException

Report the end of a CDATA section.

comment

```java
void comment​(char[] ch,
int start,
int length)
throws
SAXException
```

Report an XML comment anywhere in the document.

This callback will be used for comments inside or outside the
document element, including comments in the external DTD
subset (if read). Comments in the DTD must be properly
nested inside start/endDTD and start/endEntity events (if
used).

**Parameters:** ch

- An array holding the characters in the comment.
**Parameters:** start

- The starting position in the array.
**Parameters:** length

- The number of characters to use from the array.
**Throws:** SAXException

- The application may raise an exception.

---

#### comment

void comment​(char[] ch,
int start,
int length)
throws

SAXException

Report an XML comment anywhere in the document.

This callback will be used for comments inside or outside the
document element, including comments in the external DTD
subset (if read). Comments in the DTD must be properly
nested inside start/endDTD and start/endEntity events (if
used).

This callback will be used for comments inside or outside the
document element, including comments in the external DTD
subset (if read). Comments in the DTD must be properly
nested inside start/endDTD and start/endEntity events (if
used).

---

