# Interface DTDHandler

**Source:** `java.xml\org\xml\sax\DTDHandler.html`

### Class Description

```java
public interface
DTDHandler
```

Receive notification of basic DTD-related events.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

If a SAX application needs information about notations and
unparsed entities, then the application implements this
interface and registers an instance with the SAX parser using
the parser's setDTDHandler method. The parser uses the
instance to report notation and unparsed entity declarations to
the application.

Note that this interface includes only those DTD events that
the XML recommendation

requires

processors to report:
notation and unparsed entity declarations.

The SAX parser may report these events in any order, regardless
of the order in which the notations and unparsed entities were
declared; however, all DTD events must be reported after the
document handler's startDocument event, and before the first
startElement event.
(If the

LexicalHandler

is
used, these events must also be reported before the endDTD event.)

It is up to the application to store the information for
future use (perhaps in a hash table or object tree).
If the application encounters attributes of type "NOTATION",
"ENTITY", or "ENTITIES", it can use the information that it
obtained through this interface to find the entity and/or
notation corresponding with the attribute value.

**All Known Subinterfaces:** TransformerHandler

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void notationDecl​(
String
name,

String
publicId,

String
systemId)
throws
SAXException

Receive notification of a notation declaration event.

It is up to the application to record the notation for later
reference, if necessary;
notations may appear as attribute values and in unparsed entity
declarations, and are sometime used with processing instruction
target names.

At least one of publicId and systemId must be non-null.
If a system identifier is present, and it is a URL, the SAX
parser must resolve it fully before passing it to the
application through this event.

There is no guarantee that the notation declaration will be
reported before any unparsed entities that use it.

**Parameters:**
- name

- The notation name.
- publicId

- The notation's public identifier, or null if
none was given.
- systemId

- The notation's system identifier, or null if
none was given.

**Throws:**
- SAXException

- Any SAX exception, possibly
wrapping another exception.

**See Also:**
- unparsedEntityDecl(java.lang.String, java.lang.String, java.lang.String, java.lang.String)

,

Attributes

---

#### void unparsedEntityDecl​(
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

Receive notification of an unparsed entity declaration event.

Note that the notation name corresponds to a notation
reported by the

notationDecl

event.
It is up to the application to record the entity for later
reference, if necessary;
unparsed entities may appear as attribute values.

If the system identifier is a URL, the parser must resolve it
fully before passing it to the application.

**Parameters:**
- name

- The unparsed entity's name.
- publicId

- The entity's public identifier, or null if none
was given.
- systemId

- The entity's system identifier.
- notationName

- The name of the associated notation.

**Throws:**
- SAXException

- Any SAX exception, possibly
wrapping another exception.

**See Also:**
- notationDecl(java.lang.String, java.lang.String, java.lang.String)

,

Attributes

---

### Additional Sections

#### Interface DTDHandler

**All Known Subinterfaces:** TransformerHandler

**All Known Implementing Classes:** DefaultHandler

,

DefaultHandler2

,

HandlerBase

,

XMLFilterImpl

```java
public interface
DTDHandler
```

Receive notification of basic DTD-related events.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

If a SAX application needs information about notations and
unparsed entities, then the application implements this
interface and registers an instance with the SAX parser using
the parser's setDTDHandler method. The parser uses the
instance to report notation and unparsed entity declarations to
the application.

Note that this interface includes only those DTD events that
the XML recommendation

requires

processors to report:
notation and unparsed entity declarations.

The SAX parser may report these events in any order, regardless
of the order in which the notations and unparsed entities were
declared; however, all DTD events must be reported after the
document handler's startDocument event, and before the first
startElement event.
(If the

LexicalHandler

is
used, these events must also be reported before the endDTD event.)

It is up to the application to store the information for
future use (perhaps in a hash table or object tree).
If the application encounters attributes of type "NOTATION",
"ENTITY", or "ENTITIES", it can use the information that it
obtained through this interface to find the entity and/or
notation corresponding with the attribute value.

**Since:** 1.4, SAX 1.0
**See Also:** XMLReader.setDTDHandler(org.xml.sax.DTDHandler)

public interface

DTDHandler

Receive notification of basic DTD-related events.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

If a SAX application needs information about notations and
unparsed entities, then the application implements this
interface and registers an instance with the SAX parser using
the parser's setDTDHandler method. The parser uses the
instance to report notation and unparsed entity declarations to
the application.

Note that this interface includes only those DTD events that
the XML recommendation

requires

processors to report:
notation and unparsed entity declarations.

The SAX parser may report these events in any order, regardless
of the order in which the notations and unparsed entities were
declared; however, all DTD events must be reported after the
document handler's startDocument event, and before the first
startElement event.
(If the

LexicalHandler

is
used, these events must also be reported before the endDTD event.)

It is up to the application to store the information for
future use (perhaps in a hash table or object tree).
If the application encounters attributes of type "NOTATION",
"ENTITY", or "ENTITIES", it can use the information that it
obtained through this interface to find the entity and/or
notation corresponding with the attribute value.

If a SAX application needs information about notations and
unparsed entities, then the application implements this
interface and registers an instance with the SAX parser using
the parser's setDTDHandler method. The parser uses the
instance to report notation and unparsed entity declarations to
the application.

Note that this interface includes only those DTD events that
the XML recommendation

requires

processors to report:
notation and unparsed entity declarations.

The SAX parser may report these events in any order, regardless
of the order in which the notations and unparsed entities were
declared; however, all DTD events must be reported after the
document handler's startDocument event, and before the first
startElement event.
(If the

LexicalHandler

is
used, these events must also be reported before the endDTD event.)

It is up to the application to store the information for
future use (perhaps in a hash table or object tree).
If the application encounters attributes of type "NOTATION",
"ENTITY", or "ENTITIES", it can use the information that it
obtained through this interface to find the entity and/or
notation corresponding with the attribute value.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

notationDecl

​(

String

name,

String

publicId,

String

systemId)

Receive notification of a notation declaration event.

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

Receive notification of an unparsed entity declaration event.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

notationDecl

​(

String

name,

String

publicId,

String

systemId)

Receive notification of a notation declaration event.

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

Receive notification of an unparsed entity declaration event.

---

#### Method Summary

Receive notification of a notation declaration event.

Receive notification of an unparsed entity declaration event.

============ METHOD DETAIL ==========

- Method Detail

- notationDecl

```java
void notationDecl​(
String
name,

String
publicId,

String
systemId)
throws
SAXException
```

Receive notification of a notation declaration event.

It is up to the application to record the notation for later
reference, if necessary;
notations may appear as attribute values and in unparsed entity
declarations, and are sometime used with processing instruction
target names.

At least one of publicId and systemId must be non-null.
If a system identifier is present, and it is a URL, the SAX
parser must resolve it fully before passing it to the
application through this event.

There is no guarantee that the notation declaration will be
reported before any unparsed entities that use it.

**Parameters:** name

- The notation name.
**Parameters:** publicId

- The notation's public identifier, or null if
none was given.
**Parameters:** systemId

- The notation's system identifier, or null if
none was given.
**Throws:** SAXException

- Any SAX exception, possibly
wrapping another exception.
**See Also:** unparsedEntityDecl(java.lang.String, java.lang.String, java.lang.String, java.lang.String)

,

Attributes

- unparsedEntityDecl

```java
void unparsedEntityDecl​(
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

Receive notification of an unparsed entity declaration event.

Note that the notation name corresponds to a notation
reported by the

notationDecl

event.
It is up to the application to record the entity for later
reference, if necessary;
unparsed entities may appear as attribute values.

If the system identifier is a URL, the parser must resolve it
fully before passing it to the application.

**Parameters:** name

- The unparsed entity's name.
**Parameters:** publicId

- The entity's public identifier, or null if none
was given.
**Parameters:** systemId

- The entity's system identifier.
**Parameters:** notationName

- The name of the associated notation.
**Throws:** SAXException

- Any SAX exception, possibly
wrapping another exception.
**See Also:** notationDecl(java.lang.String, java.lang.String, java.lang.String)

,

Attributes

Method Detail

- notationDecl

```java
void notationDecl​(
String
name,

String
publicId,

String
systemId)
throws
SAXException
```

Receive notification of a notation declaration event.

It is up to the application to record the notation for later
reference, if necessary;
notations may appear as attribute values and in unparsed entity
declarations, and are sometime used with processing instruction
target names.

At least one of publicId and systemId must be non-null.
If a system identifier is present, and it is a URL, the SAX
parser must resolve it fully before passing it to the
application through this event.

There is no guarantee that the notation declaration will be
reported before any unparsed entities that use it.

**Parameters:** name

- The notation name.
**Parameters:** publicId

- The notation's public identifier, or null if
none was given.
**Parameters:** systemId

- The notation's system identifier, or null if
none was given.
**Throws:** SAXException

- Any SAX exception, possibly
wrapping another exception.
**See Also:** unparsedEntityDecl(java.lang.String, java.lang.String, java.lang.String, java.lang.String)

,

Attributes

- unparsedEntityDecl

```java
void unparsedEntityDecl​(
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

Receive notification of an unparsed entity declaration event.

Note that the notation name corresponds to a notation
reported by the

notationDecl

event.
It is up to the application to record the entity for later
reference, if necessary;
unparsed entities may appear as attribute values.

If the system identifier is a URL, the parser must resolve it
fully before passing it to the application.

**Parameters:** name

- The unparsed entity's name.
**Parameters:** publicId

- The entity's public identifier, or null if none
was given.
**Parameters:** systemId

- The entity's system identifier.
**Parameters:** notationName

- The name of the associated notation.
**Throws:** SAXException

- Any SAX exception, possibly
wrapping another exception.
**See Also:** notationDecl(java.lang.String, java.lang.String, java.lang.String)

,

Attributes

---

#### Method Detail

notationDecl

```java
void notationDecl​(
String
name,

String
publicId,

String
systemId)
throws
SAXException
```

Receive notification of a notation declaration event.

It is up to the application to record the notation for later
reference, if necessary;
notations may appear as attribute values and in unparsed entity
declarations, and are sometime used with processing instruction
target names.

At least one of publicId and systemId must be non-null.
If a system identifier is present, and it is a URL, the SAX
parser must resolve it fully before passing it to the
application through this event.

There is no guarantee that the notation declaration will be
reported before any unparsed entities that use it.

**Parameters:** name

- The notation name.
**Parameters:** publicId

- The notation's public identifier, or null if
none was given.
**Parameters:** systemId

- The notation's system identifier, or null if
none was given.
**Throws:** SAXException

- Any SAX exception, possibly
wrapping another exception.
**See Also:** unparsedEntityDecl(java.lang.String, java.lang.String, java.lang.String, java.lang.String)

,

Attributes

---

#### notationDecl

void notationDecl​(

String

name,

String

publicId,

String

systemId)
throws

SAXException

Receive notification of a notation declaration event.

It is up to the application to record the notation for later
reference, if necessary;
notations may appear as attribute values and in unparsed entity
declarations, and are sometime used with processing instruction
target names.

At least one of publicId and systemId must be non-null.
If a system identifier is present, and it is a URL, the SAX
parser must resolve it fully before passing it to the
application through this event.

There is no guarantee that the notation declaration will be
reported before any unparsed entities that use it.

It is up to the application to record the notation for later
reference, if necessary;
notations may appear as attribute values and in unparsed entity
declarations, and are sometime used with processing instruction
target names.

At least one of publicId and systemId must be non-null.
If a system identifier is present, and it is a URL, the SAX
parser must resolve it fully before passing it to the
application through this event.

There is no guarantee that the notation declaration will be
reported before any unparsed entities that use it.

unparsedEntityDecl

```java
void unparsedEntityDecl​(
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

Receive notification of an unparsed entity declaration event.

Note that the notation name corresponds to a notation
reported by the

notationDecl

event.
It is up to the application to record the entity for later
reference, if necessary;
unparsed entities may appear as attribute values.

If the system identifier is a URL, the parser must resolve it
fully before passing it to the application.

**Parameters:** name

- The unparsed entity's name.
**Parameters:** publicId

- The entity's public identifier, or null if none
was given.
**Parameters:** systemId

- The entity's system identifier.
**Parameters:** notationName

- The name of the associated notation.
**Throws:** SAXException

- Any SAX exception, possibly
wrapping another exception.
**See Also:** notationDecl(java.lang.String, java.lang.String, java.lang.String)

,

Attributes

---

#### unparsedEntityDecl

void unparsedEntityDecl​(

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

Receive notification of an unparsed entity declaration event.

Note that the notation name corresponds to a notation
reported by the

notationDecl

event.
It is up to the application to record the entity for later
reference, if necessary;
unparsed entities may appear as attribute values.

If the system identifier is a URL, the parser must resolve it
fully before passing it to the application.

Note that the notation name corresponds to a notation
reported by the

notationDecl

event.
It is up to the application to record the entity for later
reference, if necessary;
unparsed entities may appear as attribute values.

If the system identifier is a URL, the parser must resolve it
fully before passing it to the application.

---

