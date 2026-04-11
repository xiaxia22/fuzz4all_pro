# Interface Locator2

**Source:** `java.xml\org\xml\sax\ext\Locator2.html`

### Class Description

```java
public interface
Locator2

extends
Locator
```

SAX2 extension to augment the entity information provided
though a

Locator

.
If an implementation supports this extension, the Locator
provided in

ContentHandler.setDocumentLocator()

will implement this
interface, and the

http://xml.org/sax/features/use-locator2

feature
flag will have the value

true

.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

XMLReader implementations are not required to support this
information, and it is not part of core-only SAX2 distributions.

**All Superinterfaces:** Locator

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
getXMLVersion()

Returns the version of XML used for the entity. This will
normally be the identifier from the current entity's

<?xml version='...' ...?>

declaration,
or be defaulted by the parser.

**Returns:**
- Identifier for the XML version being used to interpret
the entity's text, or null if that information is not yet
available in the current parsing state.

---

#### String
getEncoding()

Returns the name of the character encoding for the entity.
If the encoding was declared externally (for example, in a MIME
Content-Type header), that will be the name returned. Else if there
was an

<?xml ...encoding='...'?>

declaration at
the start of the document, that encoding name will be returned.
Otherwise the encoding will been inferred (normally to be UTF-8, or
some UTF-16 variant), and that inferred name will be returned.

When an

InputSource

is used
to provide an entity's character stream, this method returns the
encoding provided in that input stream.

Note that some recent W3C specifications require that text
in some encodings be normalized, using Unicode Normalization
Form C, before processing. Such normalization must be performed
by applications, and would normally be triggered based on the
value returned by this method.

Encoding names may be those used by the underlying JVM,
and comparisons should be case-insensitive.

**Returns:**
- Name of the character encoding being used to interpret
* the entity's text, or null if this was not provided for a *
character stream passed through an InputSource or is otherwise
not yet available in the current parsing state.

---

### Additional Sections

#### Interface Locator2

**All Superinterfaces:** Locator

**All Known Implementing Classes:** Locator2Impl

```java
public interface
Locator2

extends
Locator
```

SAX2 extension to augment the entity information provided
though a

Locator

.
If an implementation supports this extension, the Locator
provided in

ContentHandler.setDocumentLocator()

will implement this
interface, and the

http://xml.org/sax/features/use-locator2

feature
flag will have the value

true

.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

XMLReader implementations are not required to support this
information, and it is not part of core-only SAX2 distributions.

**Since:** 1.5, SAX 2.0 (extensions 1.1 alpha)

public interface

Locator2

extends

Locator

SAX2 extension to augment the entity information provided
though a

Locator

.
If an implementation supports this extension, the Locator
provided in

ContentHandler.setDocumentLocator()

will implement this
interface, and the

http://xml.org/sax/features/use-locator2

feature
flag will have the value

true

.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

XMLReader implementations are not required to support this
information, and it is not part of core-only SAX2 distributions.

XMLReader implementations are not required to support this
information, and it is not part of core-only SAX2 distributions.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getEncoding

()

Returns the name of the character encoding for the entity.

String

getXMLVersion

()

Returns the version of XML used for the entity.

- Methods declared in interface org.xml.sax.

Locator

getColumnNumber

,

getLineNumber

,

getPublicId

,

getSystemId

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getEncoding

()

Returns the name of the character encoding for the entity.

String

getXMLVersion

()

Returns the version of XML used for the entity.

- Methods declared in interface org.xml.sax.

Locator

getColumnNumber

,

getLineNumber

,

getPublicId

,

getSystemId

---

#### Method Summary

Returns the name of the character encoding for the entity.

Returns the version of XML used for the entity.

Methods declared in interface org.xml.sax.

Locator

getColumnNumber

,

getLineNumber

,

getPublicId

,

getSystemId

---

#### Methods declared in interface org.xml.sax. Locator

============ METHOD DETAIL ==========

- Method Detail

- getXMLVersion

```java
String
getXMLVersion()
```

Returns the version of XML used for the entity. This will
normally be the identifier from the current entity's

<?xml version='...' ...?>

declaration,
or be defaulted by the parser.

**Returns:** Identifier for the XML version being used to interpret
the entity's text, or null if that information is not yet
available in the current parsing state.

- getEncoding

```java
String
getEncoding()
```

Returns the name of the character encoding for the entity.
If the encoding was declared externally (for example, in a MIME
Content-Type header), that will be the name returned. Else if there
was an

<?xml ...encoding='...'?>

declaration at
the start of the document, that encoding name will be returned.
Otherwise the encoding will been inferred (normally to be UTF-8, or
some UTF-16 variant), and that inferred name will be returned.

When an

InputSource

is used
to provide an entity's character stream, this method returns the
encoding provided in that input stream.

Note that some recent W3C specifications require that text
in some encodings be normalized, using Unicode Normalization
Form C, before processing. Such normalization must be performed
by applications, and would normally be triggered based on the
value returned by this method.

Encoding names may be those used by the underlying JVM,
and comparisons should be case-insensitive.

**Returns:** Name of the character encoding being used to interpret
* the entity's text, or null if this was not provided for a *
character stream passed through an InputSource or is otherwise
not yet available in the current parsing state.

Method Detail

- getXMLVersion

```java
String
getXMLVersion()
```

Returns the version of XML used for the entity. This will
normally be the identifier from the current entity's

<?xml version='...' ...?>

declaration,
or be defaulted by the parser.

**Returns:** Identifier for the XML version being used to interpret
the entity's text, or null if that information is not yet
available in the current parsing state.

- getEncoding

```java
String
getEncoding()
```

Returns the name of the character encoding for the entity.
If the encoding was declared externally (for example, in a MIME
Content-Type header), that will be the name returned. Else if there
was an

<?xml ...encoding='...'?>

declaration at
the start of the document, that encoding name will be returned.
Otherwise the encoding will been inferred (normally to be UTF-8, or
some UTF-16 variant), and that inferred name will be returned.

When an

InputSource

is used
to provide an entity's character stream, this method returns the
encoding provided in that input stream.

Note that some recent W3C specifications require that text
in some encodings be normalized, using Unicode Normalization
Form C, before processing. Such normalization must be performed
by applications, and would normally be triggered based on the
value returned by this method.

Encoding names may be those used by the underlying JVM,
and comparisons should be case-insensitive.

**Returns:** Name of the character encoding being used to interpret
* the entity's text, or null if this was not provided for a *
character stream passed through an InputSource or is otherwise
not yet available in the current parsing state.

---

#### Method Detail

getXMLVersion

```java
String
getXMLVersion()
```

Returns the version of XML used for the entity. This will
normally be the identifier from the current entity's

<?xml version='...' ...?>

declaration,
or be defaulted by the parser.

**Returns:** Identifier for the XML version being used to interpret
the entity's text, or null if that information is not yet
available in the current parsing state.

---

#### getXMLVersion

String

getXMLVersion()

Returns the version of XML used for the entity. This will
normally be the identifier from the current entity's

<?xml version='...' ...?>

declaration,
or be defaulted by the parser.

getEncoding

```java
String
getEncoding()
```

Returns the name of the character encoding for the entity.
If the encoding was declared externally (for example, in a MIME
Content-Type header), that will be the name returned. Else if there
was an

<?xml ...encoding='...'?>

declaration at
the start of the document, that encoding name will be returned.
Otherwise the encoding will been inferred (normally to be UTF-8, or
some UTF-16 variant), and that inferred name will be returned.

When an

InputSource

is used
to provide an entity's character stream, this method returns the
encoding provided in that input stream.

Note that some recent W3C specifications require that text
in some encodings be normalized, using Unicode Normalization
Form C, before processing. Such normalization must be performed
by applications, and would normally be triggered based on the
value returned by this method.

Encoding names may be those used by the underlying JVM,
and comparisons should be case-insensitive.

**Returns:** Name of the character encoding being used to interpret
* the entity's text, or null if this was not provided for a *
character stream passed through an InputSource or is otherwise
not yet available in the current parsing state.

---

#### getEncoding

String

getEncoding()

Returns the name of the character encoding for the entity.
If the encoding was declared externally (for example, in a MIME
Content-Type header), that will be the name returned. Else if there
was an

<?xml ...encoding='...'?>

declaration at
the start of the document, that encoding name will be returned.
Otherwise the encoding will been inferred (normally to be UTF-8, or
some UTF-16 variant), and that inferred name will be returned.

When an

InputSource

is used
to provide an entity's character stream, this method returns the
encoding provided in that input stream.

Note that some recent W3C specifications require that text
in some encodings be normalized, using Unicode Normalization
Form C, before processing. Such normalization must be performed
by applications, and would normally be triggered based on the
value returned by this method.

Encoding names may be those used by the underlying JVM,
and comparisons should be case-insensitive.

When an

InputSource

is used
to provide an entity's character stream, this method returns the
encoding provided in that input stream.

Note that some recent W3C specifications require that text
in some encodings be normalized, using Unicode Normalization
Form C, before processing. Such normalization must be performed
by applications, and would normally be triggered based on the
value returned by this method.

Encoding names may be those used by the underlying JVM,
and comparisons should be case-insensitive.

Note that some recent W3C specifications require that text
in some encodings be normalized, using Unicode Normalization
Form C, before processing. Such normalization must be performed
by applications, and would normally be triggered based on the
value returned by this method.

Encoding names may be those used by the underlying JVM,
and comparisons should be case-insensitive.

Encoding names may be those used by the underlying JVM,
and comparisons should be case-insensitive.

---

