# Interface DeclHandler

**Source:** `java.xml\org\xml\sax\ext\DeclHandler.html`

### Class Description

```java
public interface
DeclHandler
```

SAX2 extension handler for DTD declaration events.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

This is an optional extension handler for SAX2 to provide more
complete information about DTD declarations in an XML document.
XML readers are not required to recognize this handler, and it
is not part of core-only SAX2 distributions.

Note that data-related DTD declarations (unparsed entities and
notations) are already reported through the

DTDHandler

interface.

If you are using the declaration handler together with a lexical
handler, all of the events will occur between the

startDTD

and the

endDTD

events.

To set the DeclHandler for an XML reader, use the

setProperty

method
with the property name

http://xml.org/sax/properties/declaration-handler

and an object implementing this interface (or null) as the value.
If the reader does not report declaration events, it will throw a

SAXNotRecognizedException

when you attempt to register the handler.

**All Known Implementing Classes:** DefaultHandler2

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void elementDecl​(
String
name,

String
model)
throws
SAXException

Report an element type declaration.

The content model will consist of the string "EMPTY", the
string "ANY", or a parenthesised group, optionally followed
by an occurrence indicator. The model will be normalized so
that all parameter entities are fully resolved and all whitespace
is removed,and will include the enclosing parentheses. Other
normalization (such as removing redundant parentheses or
simplifying occurrence indicators) is at the discretion of the
parser.

**Parameters:**
- name

- The element type name.
- model

- The content model as a normalized string.

**Throws:**
- SAXException

- The application may raise an exception.

---

#### void attributeDecl​(
String
eName,

String
aName,

String
type,

String
mode,

String
value)
throws
SAXException

Report an attribute type declaration.

Only the effective (first) declaration for an attribute will
be reported. The type will be one of the strings "CDATA",
"ID", "IDREF", "IDREFS", "NMTOKEN", "NMTOKENS", "ENTITY",
"ENTITIES", a parenthesized token group with
the separator "|" and all whitespace removed, or the word
"NOTATION" followed by a space followed by a parenthesized
token group with all whitespace removed.

The value will be the value as reported to applications,
appropriately normalized and with entity and character
references expanded.

**Parameters:**
- eName

- The name of the associated element.
- aName

- The name of the attribute.
- type

- A string representing the attribute type.
- mode

- A string representing the attribute defaulting mode
("#IMPLIED", "#REQUIRED", or "#FIXED") or null if
none of these applies.
- value

- A string representing the attribute's default value,
or null if there is none.

**Throws:**
- SAXException

- The application may raise an exception.

---

#### void internalEntityDecl​(
String
name,

String
value)
throws
SAXException

Report an internal entity declaration.

Only the effective (first) declaration for each entity
will be reported. All parameter entities in the value
will be expanded, but general entities will not.

**Parameters:**
- name

- The name of the entity. If it is a parameter
entity, the name will begin with '%'.
- value

- The replacement text of the entity.

**Throws:**
- SAXException

- The application may raise an exception.

**See Also:**
- externalEntityDecl(java.lang.String, java.lang.String, java.lang.String)

,

DTDHandler.unparsedEntityDecl(java.lang.String, java.lang.String, java.lang.String, java.lang.String)

---

#### void externalEntityDecl​(
String
name,

String
publicId,

String
systemId)
throws
SAXException

Report a parsed external entity declaration.

Only the effective (first) declaration for each entity
will be reported.

If the system identifier is a URL, the parser must resolve it
fully before passing it to the application.

**Parameters:**
- name

- The name of the entity. If it is a parameter
entity, the name will begin with '%'.
- publicId

- The entity's public identifier, or null if none
was given.
- systemId

- The entity's system identifier.

**Throws:**
- SAXException

- The application may raise an exception.

**See Also:**
- internalEntityDecl(java.lang.String, java.lang.String)

,

DTDHandler.unparsedEntityDecl(java.lang.String, java.lang.String, java.lang.String, java.lang.String)

---

### Additional Sections

#### Interface DeclHandler

**All Known Implementing Classes:** DefaultHandler2

```java
public interface
DeclHandler
```

SAX2 extension handler for DTD declaration events.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

This is an optional extension handler for SAX2 to provide more
complete information about DTD declarations in an XML document.
XML readers are not required to recognize this handler, and it
is not part of core-only SAX2 distributions.

Note that data-related DTD declarations (unparsed entities and
notations) are already reported through the

DTDHandler

interface.

If you are using the declaration handler together with a lexical
handler, all of the events will occur between the

startDTD

and the

endDTD

events.

To set the DeclHandler for an XML reader, use the

setProperty

method
with the property name

http://xml.org/sax/properties/declaration-handler

and an object implementing this interface (or null) as the value.
If the reader does not report declaration events, it will throw a

SAXNotRecognizedException

when you attempt to register the handler.

**Since:** 1.4, SAX 2.0 (extensions 1.0)

public interface

DeclHandler

SAX2 extension handler for DTD declaration events.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

This is an optional extension handler for SAX2 to provide more
complete information about DTD declarations in an XML document.
XML readers are not required to recognize this handler, and it
is not part of core-only SAX2 distributions.

Note that data-related DTD declarations (unparsed entities and
notations) are already reported through the

DTDHandler

interface.

If you are using the declaration handler together with a lexical
handler, all of the events will occur between the

startDTD

and the

endDTD

events.

To set the DeclHandler for an XML reader, use the

setProperty

method
with the property name

http://xml.org/sax/properties/declaration-handler

and an object implementing this interface (or null) as the value.
If the reader does not report declaration events, it will throw a

SAXNotRecognizedException

when you attempt to register the handler.

This is an optional extension handler for SAX2 to provide more
complete information about DTD declarations in an XML document.
XML readers are not required to recognize this handler, and it
is not part of core-only SAX2 distributions.

Note that data-related DTD declarations (unparsed entities and
notations) are already reported through the

DTDHandler

interface.

If you are using the declaration handler together with a lexical
handler, all of the events will occur between the

startDTD

and the

endDTD

events.

To set the DeclHandler for an XML reader, use the

setProperty

method
with the property name

http://xml.org/sax/properties/declaration-handler

and an object implementing this interface (or null) as the value.
If the reader does not report declaration events, it will throw a

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

attributeDecl

​(

String

eName,

String

aName,

String

type,

String

mode,

String

value)

Report an attribute type declaration.

void

elementDecl

​(

String

name,

String

model)

Report an element type declaration.

void

externalEntityDecl

​(

String

name,

String

publicId,

String

systemId)

Report a parsed external entity declaration.

void

internalEntityDecl

​(

String

name,

String

value)

Report an internal entity declaration.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

attributeDecl

​(

String

eName,

String

aName,

String

type,

String

mode,

String

value)

Report an attribute type declaration.

void

elementDecl

​(

String

name,

String

model)

Report an element type declaration.

void

externalEntityDecl

​(

String

name,

String

publicId,

String

systemId)

Report a parsed external entity declaration.

void

internalEntityDecl

​(

String

name,

String

value)

Report an internal entity declaration.

---

#### Method Summary

Report an attribute type declaration.

Report an element type declaration.

Report a parsed external entity declaration.

Report an internal entity declaration.

============ METHOD DETAIL ==========

- Method Detail

- elementDecl

```java
void elementDecl​(
String
name,

String
model)
throws
SAXException
```

Report an element type declaration.

The content model will consist of the string "EMPTY", the
string "ANY", or a parenthesised group, optionally followed
by an occurrence indicator. The model will be normalized so
that all parameter entities are fully resolved and all whitespace
is removed,and will include the enclosing parentheses. Other
normalization (such as removing redundant parentheses or
simplifying occurrence indicators) is at the discretion of the
parser.

**Parameters:** name

- The element type name.
**Parameters:** model

- The content model as a normalized string.
**Throws:** SAXException

- The application may raise an exception.

- attributeDecl

```java
void attributeDecl​(
String
eName,

String
aName,

String
type,

String
mode,

String
value)
throws
SAXException
```

Report an attribute type declaration.

Only the effective (first) declaration for an attribute will
be reported. The type will be one of the strings "CDATA",
"ID", "IDREF", "IDREFS", "NMTOKEN", "NMTOKENS", "ENTITY",
"ENTITIES", a parenthesized token group with
the separator "|" and all whitespace removed, or the word
"NOTATION" followed by a space followed by a parenthesized
token group with all whitespace removed.

The value will be the value as reported to applications,
appropriately normalized and with entity and character
references expanded.

**Parameters:** eName

- The name of the associated element.
**Parameters:** aName

- The name of the attribute.
**Parameters:** type

- A string representing the attribute type.
**Parameters:** mode

- A string representing the attribute defaulting mode
("#IMPLIED", "#REQUIRED", or "#FIXED") or null if
none of these applies.
**Parameters:** value

- A string representing the attribute's default value,
or null if there is none.
**Throws:** SAXException

- The application may raise an exception.

- internalEntityDecl

```java
void internalEntityDecl​(
String
name,

String
value)
throws
SAXException
```

Report an internal entity declaration.

Only the effective (first) declaration for each entity
will be reported. All parameter entities in the value
will be expanded, but general entities will not.

**Parameters:** name

- The name of the entity. If it is a parameter
entity, the name will begin with '%'.
**Parameters:** value

- The replacement text of the entity.
**Throws:** SAXException

- The application may raise an exception.
**See Also:** externalEntityDecl(java.lang.String, java.lang.String, java.lang.String)

,

DTDHandler.unparsedEntityDecl(java.lang.String, java.lang.String, java.lang.String, java.lang.String)

- externalEntityDecl

```java
void externalEntityDecl​(
String
name,

String
publicId,

String
systemId)
throws
SAXException
```

Report a parsed external entity declaration.

Only the effective (first) declaration for each entity
will be reported.

If the system identifier is a URL, the parser must resolve it
fully before passing it to the application.

**Parameters:** name

- The name of the entity. If it is a parameter
entity, the name will begin with '%'.
**Parameters:** publicId

- The entity's public identifier, or null if none
was given.
**Parameters:** systemId

- The entity's system identifier.
**Throws:** SAXException

- The application may raise an exception.
**See Also:** internalEntityDecl(java.lang.String, java.lang.String)

,

DTDHandler.unparsedEntityDecl(java.lang.String, java.lang.String, java.lang.String, java.lang.String)

Method Detail

- elementDecl

```java
void elementDecl​(
String
name,

String
model)
throws
SAXException
```

Report an element type declaration.

The content model will consist of the string "EMPTY", the
string "ANY", or a parenthesised group, optionally followed
by an occurrence indicator. The model will be normalized so
that all parameter entities are fully resolved and all whitespace
is removed,and will include the enclosing parentheses. Other
normalization (such as removing redundant parentheses or
simplifying occurrence indicators) is at the discretion of the
parser.

**Parameters:** name

- The element type name.
**Parameters:** model

- The content model as a normalized string.
**Throws:** SAXException

- The application may raise an exception.

- attributeDecl

```java
void attributeDecl​(
String
eName,

String
aName,

String
type,

String
mode,

String
value)
throws
SAXException
```

Report an attribute type declaration.

Only the effective (first) declaration for an attribute will
be reported. The type will be one of the strings "CDATA",
"ID", "IDREF", "IDREFS", "NMTOKEN", "NMTOKENS", "ENTITY",
"ENTITIES", a parenthesized token group with
the separator "|" and all whitespace removed, or the word
"NOTATION" followed by a space followed by a parenthesized
token group with all whitespace removed.

The value will be the value as reported to applications,
appropriately normalized and with entity and character
references expanded.

**Parameters:** eName

- The name of the associated element.
**Parameters:** aName

- The name of the attribute.
**Parameters:** type

- A string representing the attribute type.
**Parameters:** mode

- A string representing the attribute defaulting mode
("#IMPLIED", "#REQUIRED", or "#FIXED") or null if
none of these applies.
**Parameters:** value

- A string representing the attribute's default value,
or null if there is none.
**Throws:** SAXException

- The application may raise an exception.

- internalEntityDecl

```java
void internalEntityDecl​(
String
name,

String
value)
throws
SAXException
```

Report an internal entity declaration.

Only the effective (first) declaration for each entity
will be reported. All parameter entities in the value
will be expanded, but general entities will not.

**Parameters:** name

- The name of the entity. If it is a parameter
entity, the name will begin with '%'.
**Parameters:** value

- The replacement text of the entity.
**Throws:** SAXException

- The application may raise an exception.
**See Also:** externalEntityDecl(java.lang.String, java.lang.String, java.lang.String)

,

DTDHandler.unparsedEntityDecl(java.lang.String, java.lang.String, java.lang.String, java.lang.String)

- externalEntityDecl

```java
void externalEntityDecl​(
String
name,

String
publicId,

String
systemId)
throws
SAXException
```

Report a parsed external entity declaration.

Only the effective (first) declaration for each entity
will be reported.

If the system identifier is a URL, the parser must resolve it
fully before passing it to the application.

**Parameters:** name

- The name of the entity. If it is a parameter
entity, the name will begin with '%'.
**Parameters:** publicId

- The entity's public identifier, or null if none
was given.
**Parameters:** systemId

- The entity's system identifier.
**Throws:** SAXException

- The application may raise an exception.
**See Also:** internalEntityDecl(java.lang.String, java.lang.String)

,

DTDHandler.unparsedEntityDecl(java.lang.String, java.lang.String, java.lang.String, java.lang.String)

---

#### Method Detail

elementDecl

```java
void elementDecl​(
String
name,

String
model)
throws
SAXException
```

Report an element type declaration.

The content model will consist of the string "EMPTY", the
string "ANY", or a parenthesised group, optionally followed
by an occurrence indicator. The model will be normalized so
that all parameter entities are fully resolved and all whitespace
is removed,and will include the enclosing parentheses. Other
normalization (such as removing redundant parentheses or
simplifying occurrence indicators) is at the discretion of the
parser.

**Parameters:** name

- The element type name.
**Parameters:** model

- The content model as a normalized string.
**Throws:** SAXException

- The application may raise an exception.

---

#### elementDecl

void elementDecl​(

String

name,

String

model)
throws

SAXException

Report an element type declaration.

The content model will consist of the string "EMPTY", the
string "ANY", or a parenthesised group, optionally followed
by an occurrence indicator. The model will be normalized so
that all parameter entities are fully resolved and all whitespace
is removed,and will include the enclosing parentheses. Other
normalization (such as removing redundant parentheses or
simplifying occurrence indicators) is at the discretion of the
parser.

The content model will consist of the string "EMPTY", the
string "ANY", or a parenthesised group, optionally followed
by an occurrence indicator. The model will be normalized so
that all parameter entities are fully resolved and all whitespace
is removed,and will include the enclosing parentheses. Other
normalization (such as removing redundant parentheses or
simplifying occurrence indicators) is at the discretion of the
parser.

attributeDecl

```java
void attributeDecl​(
String
eName,

String
aName,

String
type,

String
mode,

String
value)
throws
SAXException
```

Report an attribute type declaration.

Only the effective (first) declaration for an attribute will
be reported. The type will be one of the strings "CDATA",
"ID", "IDREF", "IDREFS", "NMTOKEN", "NMTOKENS", "ENTITY",
"ENTITIES", a parenthesized token group with
the separator "|" and all whitespace removed, or the word
"NOTATION" followed by a space followed by a parenthesized
token group with all whitespace removed.

The value will be the value as reported to applications,
appropriately normalized and with entity and character
references expanded.

**Parameters:** eName

- The name of the associated element.
**Parameters:** aName

- The name of the attribute.
**Parameters:** type

- A string representing the attribute type.
**Parameters:** mode

- A string representing the attribute defaulting mode
("#IMPLIED", "#REQUIRED", or "#FIXED") or null if
none of these applies.
**Parameters:** value

- A string representing the attribute's default value,
or null if there is none.
**Throws:** SAXException

- The application may raise an exception.

---

#### attributeDecl

void attributeDecl​(

String

eName,

String

aName,

String

type,

String

mode,

String

value)
throws

SAXException

Report an attribute type declaration.

Only the effective (first) declaration for an attribute will
be reported. The type will be one of the strings "CDATA",
"ID", "IDREF", "IDREFS", "NMTOKEN", "NMTOKENS", "ENTITY",
"ENTITIES", a parenthesized token group with
the separator "|" and all whitespace removed, or the word
"NOTATION" followed by a space followed by a parenthesized
token group with all whitespace removed.

The value will be the value as reported to applications,
appropriately normalized and with entity and character
references expanded.

Only the effective (first) declaration for an attribute will
be reported. The type will be one of the strings "CDATA",
"ID", "IDREF", "IDREFS", "NMTOKEN", "NMTOKENS", "ENTITY",
"ENTITIES", a parenthesized token group with
the separator "|" and all whitespace removed, or the word
"NOTATION" followed by a space followed by a parenthesized
token group with all whitespace removed.

The value will be the value as reported to applications,
appropriately normalized and with entity and character
references expanded.

internalEntityDecl

```java
void internalEntityDecl​(
String
name,

String
value)
throws
SAXException
```

Report an internal entity declaration.

Only the effective (first) declaration for each entity
will be reported. All parameter entities in the value
will be expanded, but general entities will not.

**Parameters:** name

- The name of the entity. If it is a parameter
entity, the name will begin with '%'.
**Parameters:** value

- The replacement text of the entity.
**Throws:** SAXException

- The application may raise an exception.
**See Also:** externalEntityDecl(java.lang.String, java.lang.String, java.lang.String)

,

DTDHandler.unparsedEntityDecl(java.lang.String, java.lang.String, java.lang.String, java.lang.String)

---

#### internalEntityDecl

void internalEntityDecl​(

String

name,

String

value)
throws

SAXException

Report an internal entity declaration.

Only the effective (first) declaration for each entity
will be reported. All parameter entities in the value
will be expanded, but general entities will not.

Only the effective (first) declaration for each entity
will be reported. All parameter entities in the value
will be expanded, but general entities will not.

externalEntityDecl

```java
void externalEntityDecl​(
String
name,

String
publicId,

String
systemId)
throws
SAXException
```

Report a parsed external entity declaration.

Only the effective (first) declaration for each entity
will be reported.

If the system identifier is a URL, the parser must resolve it
fully before passing it to the application.

**Parameters:** name

- The name of the entity. If it is a parameter
entity, the name will begin with '%'.
**Parameters:** publicId

- The entity's public identifier, or null if none
was given.
**Parameters:** systemId

- The entity's system identifier.
**Throws:** SAXException

- The application may raise an exception.
**See Also:** internalEntityDecl(java.lang.String, java.lang.String)

,

DTDHandler.unparsedEntityDecl(java.lang.String, java.lang.String, java.lang.String, java.lang.String)

---

#### externalEntityDecl

void externalEntityDecl​(

String

name,

String

publicId,

String

systemId)
throws

SAXException

Report a parsed external entity declaration.

Only the effective (first) declaration for each entity
will be reported.

If the system identifier is a URL, the parser must resolve it
fully before passing it to the application.

Only the effective (first) declaration for each entity
will be reported.

If the system identifier is a URL, the parser must resolve it
fully before passing it to the application.

---

