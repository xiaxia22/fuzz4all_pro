# Interface ErrorHandler

**Source:** `java.xml\org\xml\sax\ErrorHandler.html`

### Class Description

```java
public interface
ErrorHandler
```

Basic interface for SAX error handlers.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

If a SAX application needs to implement customized error
handling, it must implement this interface and then register an
instance with the XML reader using the

setErrorHandler

method. The parser will then report all errors and warnings
through this interface.

WARNING:

If an application does

not

register an ErrorHandler, XML parsing errors will go unreported,
except that

SAXParseException

s will be thrown for fatal errors.
In order to detect validity errors, an ErrorHandler that does something
with

error()

calls must be registered.

For XML processing errors, a SAX driver must use this interface
in preference to throwing an exception: it is up to the application
to decide whether to throw an exception for different types of
errors and warnings. Note, however, that there is no requirement that
the parser continue to report additional errors after a call to

fatalError

. In other words, a SAX driver class
may throw an exception after reporting any fatalError.
Also parsers may throw appropriate exceptions for non-XML errors.
For example,

XMLReader.parse()

would throw
an IOException for errors accessing entities or the document.

**All Known Implementing Classes:** DefaultHandler

,

DefaultHandler2

,

HandlerBase

,

XMLFilterImpl

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void warning​(
SAXParseException
exception)
throws
SAXException

Receive notification of a warning.

SAX parsers will use this method to report conditions that
are not errors or fatal errors as defined by the XML
recommendation. The default behaviour is to take no
action.

The SAX parser must continue to provide normal parsing events
after invoking this method: it should still be possible for the
application to process the document through to the end.

Filters may use this method to report other, non-XML warnings
as well.

**Parameters:**
- exception

- The warning information encapsulated in a
SAX parse exception.

**Throws:**
- SAXException

- Any SAX exception, possibly
wrapping another exception.

**See Also:**
- SAXParseException

---

#### void error​(
SAXParseException
exception)
throws
SAXException

Receive notification of a recoverable error.

This corresponds to the definition of "error" in section 1.2
of the W3C XML 1.0 Recommendation. For example, a validating
parser would use this callback to report the violation of a
validity constraint. The default behaviour is to take no
action.

The SAX parser must continue to provide normal parsing
events after invoking this method: it should still be possible
for the application to process the document through to the end.
If the application cannot do so, then the parser should report
a fatal error even if the XML recommendation does not require
it to do so.

Filters may use this method to report other, non-XML errors
as well.

**Parameters:**
- exception

- The error information encapsulated in a
SAX parse exception.

**Throws:**
- SAXException

- Any SAX exception, possibly
wrapping another exception.

**See Also:**
- SAXParseException

---

#### void fatalError​(
SAXParseException
exception)
throws
SAXException

Receive notification of a non-recoverable error.

There is an apparent contradiction between the
documentation for this method and the documentation for

ContentHandler.endDocument()

. Until this ambiguity
is resolved in a future major release, clients should make no
assumptions about whether endDocument() will or will not be
invoked when the parser has reported a fatalError() or thrown
an exception.

This corresponds to the definition of "fatal error" in
section 1.2 of the W3C XML 1.0 Recommendation. For example, a
parser would use this callback to report the violation of a
well-formedness constraint.

The application must assume that the document is unusable
after the parser has invoked this method, and should continue
(if at all) only for the sake of collecting additional error
messages: in fact, SAX parsers are free to stop reporting any
other events once this method has been invoked.

**Parameters:**
- exception

- The error information encapsulated in a
SAX parse exception.

**Throws:**
- SAXException

- Any SAX exception, possibly
wrapping another exception.

**See Also:**
- SAXParseException

---

### Additional Sections

#### Interface ErrorHandler

**All Known Implementing Classes:** DefaultHandler

,

DefaultHandler2

,

HandlerBase

,

XMLFilterImpl

```java
public interface
ErrorHandler
```

Basic interface for SAX error handlers.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

If a SAX application needs to implement customized error
handling, it must implement this interface and then register an
instance with the XML reader using the

setErrorHandler

method. The parser will then report all errors and warnings
through this interface.

WARNING:

If an application does

not

register an ErrorHandler, XML parsing errors will go unreported,
except that

SAXParseException

s will be thrown for fatal errors.
In order to detect validity errors, an ErrorHandler that does something
with

error()

calls must be registered.

For XML processing errors, a SAX driver must use this interface
in preference to throwing an exception: it is up to the application
to decide whether to throw an exception for different types of
errors and warnings. Note, however, that there is no requirement that
the parser continue to report additional errors after a call to

fatalError

. In other words, a SAX driver class
may throw an exception after reporting any fatalError.
Also parsers may throw appropriate exceptions for non-XML errors.
For example,

XMLReader.parse()

would throw
an IOException for errors accessing entities or the document.

**Since:** 1.4, SAX 1.0
**See Also:** XMLReader.setErrorHandler(org.xml.sax.ErrorHandler)

,

SAXParseException

public interface

ErrorHandler

Basic interface for SAX error handlers.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

If a SAX application needs to implement customized error
handling, it must implement this interface and then register an
instance with the XML reader using the

setErrorHandler

method. The parser will then report all errors and warnings
through this interface.

WARNING:

If an application does

not

register an ErrorHandler, XML parsing errors will go unreported,
except that

SAXParseException

s will be thrown for fatal errors.
In order to detect validity errors, an ErrorHandler that does something
with

error()

calls must be registered.

For XML processing errors, a SAX driver must use this interface
in preference to throwing an exception: it is up to the application
to decide whether to throw an exception for different types of
errors and warnings. Note, however, that there is no requirement that
the parser continue to report additional errors after a call to

fatalError

. In other words, a SAX driver class
may throw an exception after reporting any fatalError.
Also parsers may throw appropriate exceptions for non-XML errors.
For example,

XMLReader.parse()

would throw
an IOException for errors accessing entities or the document.

If a SAX application needs to implement customized error
handling, it must implement this interface and then register an
instance with the XML reader using the

setErrorHandler

method. The parser will then report all errors and warnings
through this interface.

WARNING:

If an application does

not

register an ErrorHandler, XML parsing errors will go unreported,
except that

SAXParseException

s will be thrown for fatal errors.
In order to detect validity errors, an ErrorHandler that does something
with

error()

calls must be registered.

For XML processing errors, a SAX driver must use this interface
in preference to throwing an exception: it is up to the application
to decide whether to throw an exception for different types of
errors and warnings. Note, however, that there is no requirement that
the parser continue to report additional errors after a call to

fatalError

. In other words, a SAX driver class
may throw an exception after reporting any fatalError.
Also parsers may throw appropriate exceptions for non-XML errors.
For example,

XMLReader.parse()

would throw
an IOException for errors accessing entities or the document.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

error

​(

SAXParseException

exception)

Receive notification of a recoverable error.

void

fatalError

​(

SAXParseException

exception)

Receive notification of a non-recoverable error.

void

warning

​(

SAXParseException

exception)

Receive notification of a warning.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

error

​(

SAXParseException

exception)

Receive notification of a recoverable error.

void

fatalError

​(

SAXParseException

exception)

Receive notification of a non-recoverable error.

void

warning

​(

SAXParseException

exception)

Receive notification of a warning.

---

#### Method Summary

Receive notification of a recoverable error.

Receive notification of a non-recoverable error.

Receive notification of a warning.

============ METHOD DETAIL ==========

- Method Detail

- warning

```java
void warning​(
SAXParseException
exception)
throws
SAXException
```

Receive notification of a warning.

SAX parsers will use this method to report conditions that
are not errors or fatal errors as defined by the XML
recommendation. The default behaviour is to take no
action.

The SAX parser must continue to provide normal parsing events
after invoking this method: it should still be possible for the
application to process the document through to the end.

Filters may use this method to report other, non-XML warnings
as well.

**Parameters:** exception

- The warning information encapsulated in a
SAX parse exception.
**Throws:** SAXException

- Any SAX exception, possibly
wrapping another exception.
**See Also:** SAXParseException

- error

```java
void error​(
SAXParseException
exception)
throws
SAXException
```

Receive notification of a recoverable error.

This corresponds to the definition of "error" in section 1.2
of the W3C XML 1.0 Recommendation. For example, a validating
parser would use this callback to report the violation of a
validity constraint. The default behaviour is to take no
action.

The SAX parser must continue to provide normal parsing
events after invoking this method: it should still be possible
for the application to process the document through to the end.
If the application cannot do so, then the parser should report
a fatal error even if the XML recommendation does not require
it to do so.

Filters may use this method to report other, non-XML errors
as well.

**Parameters:** exception

- The error information encapsulated in a
SAX parse exception.
**Throws:** SAXException

- Any SAX exception, possibly
wrapping another exception.
**See Also:** SAXParseException

- fatalError

```java
void fatalError​(
SAXParseException
exception)
throws
SAXException
```

Receive notification of a non-recoverable error.

There is an apparent contradiction between the
documentation for this method and the documentation for

ContentHandler.endDocument()

. Until this ambiguity
is resolved in a future major release, clients should make no
assumptions about whether endDocument() will or will not be
invoked when the parser has reported a fatalError() or thrown
an exception.

This corresponds to the definition of "fatal error" in
section 1.2 of the W3C XML 1.0 Recommendation. For example, a
parser would use this callback to report the violation of a
well-formedness constraint.

The application must assume that the document is unusable
after the parser has invoked this method, and should continue
(if at all) only for the sake of collecting additional error
messages: in fact, SAX parsers are free to stop reporting any
other events once this method has been invoked.

**Parameters:** exception

- The error information encapsulated in a
SAX parse exception.
**Throws:** SAXException

- Any SAX exception, possibly
wrapping another exception.
**See Also:** SAXParseException

Method Detail

- warning

```java
void warning​(
SAXParseException
exception)
throws
SAXException
```

Receive notification of a warning.

SAX parsers will use this method to report conditions that
are not errors or fatal errors as defined by the XML
recommendation. The default behaviour is to take no
action.

The SAX parser must continue to provide normal parsing events
after invoking this method: it should still be possible for the
application to process the document through to the end.

Filters may use this method to report other, non-XML warnings
as well.

**Parameters:** exception

- The warning information encapsulated in a
SAX parse exception.
**Throws:** SAXException

- Any SAX exception, possibly
wrapping another exception.
**See Also:** SAXParseException

- error

```java
void error​(
SAXParseException
exception)
throws
SAXException
```

Receive notification of a recoverable error.

This corresponds to the definition of "error" in section 1.2
of the W3C XML 1.0 Recommendation. For example, a validating
parser would use this callback to report the violation of a
validity constraint. The default behaviour is to take no
action.

The SAX parser must continue to provide normal parsing
events after invoking this method: it should still be possible
for the application to process the document through to the end.
If the application cannot do so, then the parser should report
a fatal error even if the XML recommendation does not require
it to do so.

Filters may use this method to report other, non-XML errors
as well.

**Parameters:** exception

- The error information encapsulated in a
SAX parse exception.
**Throws:** SAXException

- Any SAX exception, possibly
wrapping another exception.
**See Also:** SAXParseException

- fatalError

```java
void fatalError​(
SAXParseException
exception)
throws
SAXException
```

Receive notification of a non-recoverable error.

There is an apparent contradiction between the
documentation for this method and the documentation for

ContentHandler.endDocument()

. Until this ambiguity
is resolved in a future major release, clients should make no
assumptions about whether endDocument() will or will not be
invoked when the parser has reported a fatalError() or thrown
an exception.

This corresponds to the definition of "fatal error" in
section 1.2 of the W3C XML 1.0 Recommendation. For example, a
parser would use this callback to report the violation of a
well-formedness constraint.

The application must assume that the document is unusable
after the parser has invoked this method, and should continue
(if at all) only for the sake of collecting additional error
messages: in fact, SAX parsers are free to stop reporting any
other events once this method has been invoked.

**Parameters:** exception

- The error information encapsulated in a
SAX parse exception.
**Throws:** SAXException

- Any SAX exception, possibly
wrapping another exception.
**See Also:** SAXParseException

---

#### Method Detail

warning

```java
void warning​(
SAXParseException
exception)
throws
SAXException
```

Receive notification of a warning.

SAX parsers will use this method to report conditions that
are not errors or fatal errors as defined by the XML
recommendation. The default behaviour is to take no
action.

The SAX parser must continue to provide normal parsing events
after invoking this method: it should still be possible for the
application to process the document through to the end.

Filters may use this method to report other, non-XML warnings
as well.

**Parameters:** exception

- The warning information encapsulated in a
SAX parse exception.
**Throws:** SAXException

- Any SAX exception, possibly
wrapping another exception.
**See Also:** SAXParseException

---

#### warning

void warning​(

SAXParseException

exception)
throws

SAXException

Receive notification of a warning.

SAX parsers will use this method to report conditions that
are not errors or fatal errors as defined by the XML
recommendation. The default behaviour is to take no
action.

The SAX parser must continue to provide normal parsing events
after invoking this method: it should still be possible for the
application to process the document through to the end.

Filters may use this method to report other, non-XML warnings
as well.

SAX parsers will use this method to report conditions that
are not errors or fatal errors as defined by the XML
recommendation. The default behaviour is to take no
action.

The SAX parser must continue to provide normal parsing events
after invoking this method: it should still be possible for the
application to process the document through to the end.

Filters may use this method to report other, non-XML warnings
as well.

error

```java
void error​(
SAXParseException
exception)
throws
SAXException
```

Receive notification of a recoverable error.

This corresponds to the definition of "error" in section 1.2
of the W3C XML 1.0 Recommendation. For example, a validating
parser would use this callback to report the violation of a
validity constraint. The default behaviour is to take no
action.

The SAX parser must continue to provide normal parsing
events after invoking this method: it should still be possible
for the application to process the document through to the end.
If the application cannot do so, then the parser should report
a fatal error even if the XML recommendation does not require
it to do so.

Filters may use this method to report other, non-XML errors
as well.

**Parameters:** exception

- The error information encapsulated in a
SAX parse exception.
**Throws:** SAXException

- Any SAX exception, possibly
wrapping another exception.
**See Also:** SAXParseException

---

#### error

void error​(

SAXParseException

exception)
throws

SAXException

Receive notification of a recoverable error.

This corresponds to the definition of "error" in section 1.2
of the W3C XML 1.0 Recommendation. For example, a validating
parser would use this callback to report the violation of a
validity constraint. The default behaviour is to take no
action.

The SAX parser must continue to provide normal parsing
events after invoking this method: it should still be possible
for the application to process the document through to the end.
If the application cannot do so, then the parser should report
a fatal error even if the XML recommendation does not require
it to do so.

Filters may use this method to report other, non-XML errors
as well.

This corresponds to the definition of "error" in section 1.2
of the W3C XML 1.0 Recommendation. For example, a validating
parser would use this callback to report the violation of a
validity constraint. The default behaviour is to take no
action.

The SAX parser must continue to provide normal parsing
events after invoking this method: it should still be possible
for the application to process the document through to the end.
If the application cannot do so, then the parser should report
a fatal error even if the XML recommendation does not require
it to do so.

Filters may use this method to report other, non-XML errors
as well.

fatalError

```java
void fatalError​(
SAXParseException
exception)
throws
SAXException
```

Receive notification of a non-recoverable error.

There is an apparent contradiction between the
documentation for this method and the documentation for

ContentHandler.endDocument()

. Until this ambiguity
is resolved in a future major release, clients should make no
assumptions about whether endDocument() will or will not be
invoked when the parser has reported a fatalError() or thrown
an exception.

This corresponds to the definition of "fatal error" in
section 1.2 of the W3C XML 1.0 Recommendation. For example, a
parser would use this callback to report the violation of a
well-formedness constraint.

The application must assume that the document is unusable
after the parser has invoked this method, and should continue
(if at all) only for the sake of collecting additional error
messages: in fact, SAX parsers are free to stop reporting any
other events once this method has been invoked.

**Parameters:** exception

- The error information encapsulated in a
SAX parse exception.
**Throws:** SAXException

- Any SAX exception, possibly
wrapping another exception.
**See Also:** SAXParseException

---

#### fatalError

void fatalError​(

SAXParseException

exception)
throws

SAXException

Receive notification of a non-recoverable error.

There is an apparent contradiction between the
documentation for this method and the documentation for

ContentHandler.endDocument()

. Until this ambiguity
is resolved in a future major release, clients should make no
assumptions about whether endDocument() will or will not be
invoked when the parser has reported a fatalError() or thrown
an exception.

This corresponds to the definition of "fatal error" in
section 1.2 of the W3C XML 1.0 Recommendation. For example, a
parser would use this callback to report the violation of a
well-formedness constraint.

The application must assume that the document is unusable
after the parser has invoked this method, and should continue
(if at all) only for the sake of collecting additional error
messages: in fact, SAX parsers are free to stop reporting any
other events once this method has been invoked.

There is an apparent contradiction between the
documentation for this method and the documentation for

ContentHandler.endDocument()

. Until this ambiguity
is resolved in a future major release, clients should make no
assumptions about whether endDocument() will or will not be
invoked when the parser has reported a fatalError() or thrown
an exception.

This corresponds to the definition of "fatal error" in
section 1.2 of the W3C XML 1.0 Recommendation. For example, a
parser would use this callback to report the violation of a
well-formedness constraint.

The application must assume that the document is unusable
after the parser has invoked this method, and should continue
(if at all) only for the sake of collecting additional error
messages: in fact, SAX parsers are free to stop reporting any
other events once this method has been invoked.

---

