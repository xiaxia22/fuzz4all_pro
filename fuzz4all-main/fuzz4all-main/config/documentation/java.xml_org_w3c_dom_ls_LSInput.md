# Interface LSInput

**Source:** `java.xml\org\w3c\dom\ls\LSInput.html`

### Class Description

```java
public interface
LSInput
```

This interface represents an input source for data.

This interface allows an application to encapsulate information about
an input source in a single object, which may include a public
identifier, a system identifier, a byte stream (possibly with a specified
encoding), a base URI, and/or a character stream.

The exact definitions of a byte stream and a character stream are
binding dependent.

The application is expected to provide objects that implement this
interface whenever such objects are needed. The application can either
provide its own objects that implement this interface, or it can use the
generic factory method

DOMImplementationLS.createLSInput()

to create objects that implement this interface.

The

LSParser

will use the

LSInput

object to
determine how to read data. The

LSParser

will look at the
different inputs specified in the

LSInput

in the following
order to know which one to read from, the first one that is not null and
not an empty string will be used:

- LSInput.characterStream
- LSInput.byteStream
- LSInput.stringData
- LSInput.systemId
- LSInput.publicId

If all inputs are null, the

LSParser

will report a

DOMError

with its

DOMError.type

set to

"no-input-specified"

and its

DOMError.severity

set to

DOMError.SEVERITY_FATAL_ERROR

.

LSInput

objects belong to the application. The DOM
implementation will never modify them (though it may make copies and
modify the copies, if necessary).

See also the

Document Object Model (DOM) Level 3 Load
and Save Specification

.

**Since:** 1.5

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Reader
getCharacterStream()

An attribute of a language and binding dependent type that represents
a stream of 16-bit units. The application must encode the stream
using UTF-16 (defined in [Unicode] and in [ISO/IEC 10646]). It is not a requirement to have an XML declaration when
using character streams. If an XML declaration is present, the value
of the encoding attribute will be ignored.

---

#### void setCharacterStream​(
Reader
characterStream)

An attribute of a language and binding dependent type that represents
a stream of 16-bit units. The application must encode the stream
using UTF-16 (defined in [Unicode] and in [ISO/IEC 10646]). It is not a requirement to have an XML declaration when
using character streams. If an XML declaration is present, the value
of the encoding attribute will be ignored.

---

#### InputStream
getByteStream()

An attribute of a language and binding dependent type that represents
a stream of bytes.

If the application knows the character encoding of the byte
stream, it should set the encoding attribute. Setting the encoding in
this way will override any encoding specified in an XML declaration
in the data.

---

#### void setByteStream​(
InputStream
byteStream)

An attribute of a language and binding dependent type that represents
a stream of bytes.

If the application knows the character encoding of the byte
stream, it should set the encoding attribute. Setting the encoding in
this way will override any encoding specified in an XML declaration
in the data.

---

#### String
getStringData()

String data to parse. If provided, this will always be treated as a
sequence of 16-bit units (UTF-16 encoded characters). It is not a
requirement to have an XML declaration when using

stringData

. If an XML declaration is present, the value
of the encoding attribute will be ignored.

---

#### void setStringData​(
String
stringData)

String data to parse. If provided, this will always be treated as a
sequence of 16-bit units (UTF-16 encoded characters). It is not a
requirement to have an XML declaration when using

stringData

. If an XML declaration is present, the value
of the encoding attribute will be ignored.

---

#### String
getSystemId()

The system identifier, a URI reference [

IETF RFC 2396

], for this
input source. The system identifier is optional if there is a byte
stream, a character stream, or string data. It is still useful to
provide one, since the application will use it to resolve any
relative URIs and can include it in error messages and warnings. (The
LSParser will only attempt to fetch the resource identified by the
URI reference if there is no other input available in the input
source.)

If the application knows the character encoding of the object
pointed to by the system identifier, it can set the encoding using
the

encoding

attribute.

If the specified system ID is a relative URI reference (see
section 5 in [

IETF RFC 2396

]), the DOM
implementation will attempt to resolve the relative URI with the

baseURI

as the base, if that fails, the behavior is
implementation dependent.

---

#### void setSystemId​(
String
systemId)

The system identifier, a URI reference [

IETF RFC 2396

], for this
input source. The system identifier is optional if there is a byte
stream, a character stream, or string data. It is still useful to
provide one, since the application will use it to resolve any
relative URIs and can include it in error messages and warnings. (The
LSParser will only attempt to fetch the resource identified by the
URI reference if there is no other input available in the input
source.)

If the application knows the character encoding of the object
pointed to by the system identifier, it can set the encoding using
the

encoding

attribute.

If the specified system ID is a relative URI reference (see
section 5 in [

IETF RFC 2396

]), the DOM
implementation will attempt to resolve the relative URI with the

baseURI

as the base, if that fails, the behavior is
implementation dependent.

---

#### String
getPublicId()

The public identifier for this input source. This may be mapped to an
input source using an implementation dependent mechanism (such as
catalogues or other mappings). The public identifier, if specified,
may also be reported as part of the location information when errors
are reported.

---

#### void setPublicId​(
String
publicId)

The public identifier for this input source. This may be mapped to an
input source using an implementation dependent mechanism (such as
catalogues or other mappings). The public identifier, if specified,
may also be reported as part of the location information when errors
are reported.

---

#### String
getBaseURI()

The base URI to be used (see section 5.1.4 in [

IETF RFC 2396

]) for
resolving a relative

systemId

to an absolute URI.

If, when used, the base URI is itself a relative URI, an empty
string, or null, the behavior is implementation dependent.

---

#### void setBaseURI​(
String
baseURI)

The base URI to be used (see section 5.1.4 in [

IETF RFC 2396

]) for
resolving a relative

systemId

to an absolute URI.

If, when used, the base URI is itself a relative URI, an empty
string, or null, the behavior is implementation dependent.

---

#### String
getEncoding()

The character encoding, if known. The encoding must be a string
acceptable for an XML encoding declaration ([

XML 1.0

] section
4.3.3 "Character Encoding in Entities").

This attribute has no effect when the application provides a
character stream or string data. For other sources of input, an
encoding specified by means of this attribute will override any
encoding specified in the XML declaration or the Text declaration, or
an encoding obtained from a higher level protocol, such as HTTP [

IETF RFC 2616

].

---

#### void setEncoding​(
String
encoding)

The character encoding, if known. The encoding must be a string
acceptable for an XML encoding declaration ([

XML 1.0

] section
4.3.3 "Character Encoding in Entities").

This attribute has no effect when the application provides a
character stream or string data. For other sources of input, an
encoding specified by means of this attribute will override any
encoding specified in the XML declaration or the Text declaration, or
an encoding obtained from a higher level protocol, such as HTTP [

IETF RFC 2616

].

---

#### boolean getCertifiedText()

If set to true, assume that the input is certified (see section 2.13
in [

XML 1.1

]) when
parsing [

XML 1.1

].

---

#### void setCertifiedText​(boolean certifiedText)

If set to true, assume that the input is certified (see section 2.13
in [

XML 1.1

]) when
parsing [

XML 1.1

].

---

### Additional Sections

#### Interface LSInput

```java
public interface
LSInput
```

This interface represents an input source for data.

This interface allows an application to encapsulate information about
an input source in a single object, which may include a public
identifier, a system identifier, a byte stream (possibly with a specified
encoding), a base URI, and/or a character stream.

The exact definitions of a byte stream and a character stream are
binding dependent.

The application is expected to provide objects that implement this
interface whenever such objects are needed. The application can either
provide its own objects that implement this interface, or it can use the
generic factory method

DOMImplementationLS.createLSInput()

to create objects that implement this interface.

The

LSParser

will use the

LSInput

object to
determine how to read data. The

LSParser

will look at the
different inputs specified in the

LSInput

in the following
order to know which one to read from, the first one that is not null and
not an empty string will be used:

- LSInput.characterStream
- LSInput.byteStream
- LSInput.stringData
- LSInput.systemId
- LSInput.publicId

If all inputs are null, the

LSParser

will report a

DOMError

with its

DOMError.type

set to

"no-input-specified"

and its

DOMError.severity

set to

DOMError.SEVERITY_FATAL_ERROR

.

LSInput

objects belong to the application. The DOM
implementation will never modify them (though it may make copies and
modify the copies, if necessary).

See also the

Document Object Model (DOM) Level 3 Load
and Save Specification

.

**Since:** 1.5

public interface

LSInput

This interface represents an input source for data.

This interface allows an application to encapsulate information about
an input source in a single object, which may include a public
identifier, a system identifier, a byte stream (possibly with a specified
encoding), a base URI, and/or a character stream.

The exact definitions of a byte stream and a character stream are
binding dependent.

The application is expected to provide objects that implement this
interface whenever such objects are needed. The application can either
provide its own objects that implement this interface, or it can use the
generic factory method

DOMImplementationLS.createLSInput()

to create objects that implement this interface.

The

LSParser

will use the

LSInput

object to
determine how to read data. The

LSParser

will look at the
different inputs specified in the

LSInput

in the following
order to know which one to read from, the first one that is not null and
not an empty string will be used:

- LSInput.characterStream
- LSInput.byteStream
- LSInput.stringData
- LSInput.systemId
- LSInput.publicId

If all inputs are null, the

LSParser

will report a

DOMError

with its

DOMError.type

set to

"no-input-specified"

and its

DOMError.severity

set to

DOMError.SEVERITY_FATAL_ERROR

.

LSInput

objects belong to the application. The DOM
implementation will never modify them (though it may make copies and
modify the copies, if necessary).

See also the

Document Object Model (DOM) Level 3 Load
and Save Specification

.

This interface allows an application to encapsulate information about
an input source in a single object, which may include a public
identifier, a system identifier, a byte stream (possibly with a specified
encoding), a base URI, and/or a character stream.

The exact definitions of a byte stream and a character stream are
binding dependent.

The application is expected to provide objects that implement this
interface whenever such objects are needed. The application can either
provide its own objects that implement this interface, or it can use the
generic factory method

DOMImplementationLS.createLSInput()

to create objects that implement this interface.

The

LSParser

will use the

LSInput

object to
determine how to read data. The

LSParser

will look at the
different inputs specified in the

LSInput

in the following
order to know which one to read from, the first one that is not null and
not an empty string will be used:

- LSInput.characterStream
- LSInput.byteStream
- LSInput.stringData
- LSInput.systemId
- LSInput.publicId

If all inputs are null, the

LSParser

will report a

DOMError

with its

DOMError.type

set to

"no-input-specified"

and its

DOMError.severity

set to

DOMError.SEVERITY_FATAL_ERROR

.

LSInput

objects belong to the application. The DOM
implementation will never modify them (though it may make copies and
modify the copies, if necessary).

See also the

Document Object Model (DOM) Level 3 Load
and Save Specification

.

The exact definitions of a byte stream and a character stream are
binding dependent.

The application is expected to provide objects that implement this
interface whenever such objects are needed. The application can either
provide its own objects that implement this interface, or it can use the
generic factory method

DOMImplementationLS.createLSInput()

to create objects that implement this interface.

The

LSParser

will use the

LSInput

object to
determine how to read data. The

LSParser

will look at the
different inputs specified in the

LSInput

in the following
order to know which one to read from, the first one that is not null and
not an empty string will be used:

- LSInput.characterStream
- LSInput.byteStream
- LSInput.stringData
- LSInput.systemId
- LSInput.publicId

If all inputs are null, the

LSParser

will report a

DOMError

with its

DOMError.type

set to

"no-input-specified"

and its

DOMError.severity

set to

DOMError.SEVERITY_FATAL_ERROR

.

LSInput

objects belong to the application. The DOM
implementation will never modify them (though it may make copies and
modify the copies, if necessary).

See also the

Document Object Model (DOM) Level 3 Load
and Save Specification

.

The application is expected to provide objects that implement this
interface whenever such objects are needed. The application can either
provide its own objects that implement this interface, or it can use the
generic factory method

DOMImplementationLS.createLSInput()

to create objects that implement this interface.

The

LSParser

will use the

LSInput

object to
determine how to read data. The

LSParser

will look at the
different inputs specified in the

LSInput

in the following
order to know which one to read from, the first one that is not null and
not an empty string will be used:

- LSInput.characterStream
- LSInput.byteStream
- LSInput.stringData
- LSInput.systemId
- LSInput.publicId

If all inputs are null, the

LSParser

will report a

DOMError

with its

DOMError.type

set to

"no-input-specified"

and its

DOMError.severity

set to

DOMError.SEVERITY_FATAL_ERROR

.

LSInput

objects belong to the application. The DOM
implementation will never modify them (though it may make copies and
modify the copies, if necessary).

See also the

Document Object Model (DOM) Level 3 Load
and Save Specification

.

The

LSParser

will use the

LSInput

object to
determine how to read data. The

LSParser

will look at the
different inputs specified in the

LSInput

in the following
order to know which one to read from, the first one that is not null and
not an empty string will be used:

- LSInput.characterStream
- LSInput.byteStream
- LSInput.stringData
- LSInput.systemId
- LSInput.publicId

If all inputs are null, the

LSParser

will report a

DOMError

with its

DOMError.type

set to

"no-input-specified"

and its

DOMError.severity

set to

DOMError.SEVERITY_FATAL_ERROR

.

LSInput

objects belong to the application. The DOM
implementation will never modify them (though it may make copies and
modify the copies, if necessary).

See also the

Document Object Model (DOM) Level 3 Load
and Save Specification

.

LSInput.characterStream

LSInput.byteStream

LSInput.stringData

LSInput.systemId

LSInput.publicId

If all inputs are null, the

LSParser

will report a

DOMError

with its

DOMError.type

set to

"no-input-specified"

and its

DOMError.severity

set to

DOMError.SEVERITY_FATAL_ERROR

.

LSInput

objects belong to the application. The DOM
implementation will never modify them (though it may make copies and
modify the copies, if necessary).

See also the

Document Object Model (DOM) Level 3 Load
and Save Specification

.

LSInput

objects belong to the application. The DOM
implementation will never modify them (though it may make copies and
modify the copies, if necessary).

See also the

Document Object Model (DOM) Level 3 Load
and Save Specification

.

See also the

Document Object Model (DOM) Level 3 Load
and Save Specification

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getBaseURI

()

The base URI to be used (see section 5.1.4 in [

IETF RFC 2396

]) for
resolving a relative

systemId

to an absolute URI.

InputStream

getByteStream

()

An attribute of a language and binding dependent type that represents
a stream of bytes.

boolean

getCertifiedText

()

If set to true, assume that the input is certified (see section 2.13
in [

XML 1.1

]) when
parsing [

XML 1.1

].

Reader

getCharacterStream

()

An attribute of a language and binding dependent type that represents
a stream of 16-bit units.

String

getEncoding

()

The character encoding, if known.

String

getPublicId

()

The public identifier for this input source.

String

getStringData

()

String data to parse.

String

getSystemId

()

The system identifier, a URI reference [

IETF RFC 2396

], for this
input source.

void

setBaseURI

​(

String

baseURI)

The base URI to be used (see section 5.1.4 in [

IETF RFC 2396

]) for
resolving a relative

systemId

to an absolute URI.

void

setByteStream

​(

InputStream

byteStream)

An attribute of a language and binding dependent type that represents
a stream of bytes.

void

setCertifiedText

​(boolean certifiedText)

If set to true, assume that the input is certified (see section 2.13
in [

XML 1.1

]) when
parsing [

XML 1.1

].

void

setCharacterStream

​(

Reader

characterStream)

An attribute of a language and binding dependent type that represents
a stream of 16-bit units.

void

setEncoding

​(

String

encoding)

The character encoding, if known.

void

setPublicId

​(

String

publicId)

The public identifier for this input source.

void

setStringData

​(

String

stringData)

String data to parse.

void

setSystemId

​(

String

systemId)

The system identifier, a URI reference [

IETF RFC 2396

], for this
input source.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getBaseURI

()

The base URI to be used (see section 5.1.4 in [

IETF RFC 2396

]) for
resolving a relative

systemId

to an absolute URI.

InputStream

getByteStream

()

An attribute of a language and binding dependent type that represents
a stream of bytes.

boolean

getCertifiedText

()

If set to true, assume that the input is certified (see section 2.13
in [

XML 1.1

]) when
parsing [

XML 1.1

].

Reader

getCharacterStream

()

An attribute of a language and binding dependent type that represents
a stream of 16-bit units.

String

getEncoding

()

The character encoding, if known.

String

getPublicId

()

The public identifier for this input source.

String

getStringData

()

String data to parse.

String

getSystemId

()

The system identifier, a URI reference [

IETF RFC 2396

], for this
input source.

void

setBaseURI

​(

String

baseURI)

The base URI to be used (see section 5.1.4 in [

IETF RFC 2396

]) for
resolving a relative

systemId

to an absolute URI.

void

setByteStream

​(

InputStream

byteStream)

An attribute of a language and binding dependent type that represents
a stream of bytes.

void

setCertifiedText

​(boolean certifiedText)

If set to true, assume that the input is certified (see section 2.13
in [

XML 1.1

]) when
parsing [

XML 1.1

].

void

setCharacterStream

​(

Reader

characterStream)

An attribute of a language and binding dependent type that represents
a stream of 16-bit units.

void

setEncoding

​(

String

encoding)

The character encoding, if known.

void

setPublicId

​(

String

publicId)

The public identifier for this input source.

void

setStringData

​(

String

stringData)

String data to parse.

void

setSystemId

​(

String

systemId)

The system identifier, a URI reference [

IETF RFC 2396

], for this
input source.

---

#### Method Summary

The base URI to be used (see section 5.1.4 in [

IETF RFC 2396

]) for
resolving a relative

systemId

to an absolute URI.

An attribute of a language and binding dependent type that represents
a stream of bytes.

If set to true, assume that the input is certified (see section 2.13
in [

XML 1.1

]) when
parsing [

XML 1.1

].

An attribute of a language and binding dependent type that represents
a stream of 16-bit units.

The character encoding, if known.

The public identifier for this input source.

String data to parse.

The system identifier, a URI reference [

IETF RFC 2396

], for this
input source.

============ METHOD DETAIL ==========

- Method Detail

- getCharacterStream

```java
Reader
getCharacterStream()
```

An attribute of a language and binding dependent type that represents
a stream of 16-bit units. The application must encode the stream
using UTF-16 (defined in [Unicode] and in [ISO/IEC 10646]). It is not a requirement to have an XML declaration when
using character streams. If an XML declaration is present, the value
of the encoding attribute will be ignored.

- setCharacterStream

```java
void setCharacterStream​(
Reader
characterStream)
```

An attribute of a language and binding dependent type that represents
a stream of 16-bit units. The application must encode the stream
using UTF-16 (defined in [Unicode] and in [ISO/IEC 10646]). It is not a requirement to have an XML declaration when
using character streams. If an XML declaration is present, the value
of the encoding attribute will be ignored.

- getByteStream

```java
InputStream
getByteStream()
```

An attribute of a language and binding dependent type that represents
a stream of bytes.

If the application knows the character encoding of the byte
stream, it should set the encoding attribute. Setting the encoding in
this way will override any encoding specified in an XML declaration
in the data.

- setByteStream

```java
void setByteStream​(
InputStream
byteStream)
```

An attribute of a language and binding dependent type that represents
a stream of bytes.

If the application knows the character encoding of the byte
stream, it should set the encoding attribute. Setting the encoding in
this way will override any encoding specified in an XML declaration
in the data.

- getStringData

```java
String
getStringData()
```

String data to parse. If provided, this will always be treated as a
sequence of 16-bit units (UTF-16 encoded characters). It is not a
requirement to have an XML declaration when using

stringData

. If an XML declaration is present, the value
of the encoding attribute will be ignored.

- setStringData

```java
void setStringData​(
String
stringData)
```

String data to parse. If provided, this will always be treated as a
sequence of 16-bit units (UTF-16 encoded characters). It is not a
requirement to have an XML declaration when using

stringData

. If an XML declaration is present, the value
of the encoding attribute will be ignored.

- getSystemId

```java
String
getSystemId()
```

The system identifier, a URI reference [

IETF RFC 2396

], for this
input source. The system identifier is optional if there is a byte
stream, a character stream, or string data. It is still useful to
provide one, since the application will use it to resolve any
relative URIs and can include it in error messages and warnings. (The
LSParser will only attempt to fetch the resource identified by the
URI reference if there is no other input available in the input
source.)

If the application knows the character encoding of the object
pointed to by the system identifier, it can set the encoding using
the

encoding

attribute.

If the specified system ID is a relative URI reference (see
section 5 in [

IETF RFC 2396

]), the DOM
implementation will attempt to resolve the relative URI with the

baseURI

as the base, if that fails, the behavior is
implementation dependent.

- setSystemId

```java
void setSystemId​(
String
systemId)
```

The system identifier, a URI reference [

IETF RFC 2396

], for this
input source. The system identifier is optional if there is a byte
stream, a character stream, or string data. It is still useful to
provide one, since the application will use it to resolve any
relative URIs and can include it in error messages and warnings. (The
LSParser will only attempt to fetch the resource identified by the
URI reference if there is no other input available in the input
source.)

If the application knows the character encoding of the object
pointed to by the system identifier, it can set the encoding using
the

encoding

attribute.

If the specified system ID is a relative URI reference (see
section 5 in [

IETF RFC 2396

]), the DOM
implementation will attempt to resolve the relative URI with the

baseURI

as the base, if that fails, the behavior is
implementation dependent.

- getPublicId

```java
String
getPublicId()
```

The public identifier for this input source. This may be mapped to an
input source using an implementation dependent mechanism (such as
catalogues or other mappings). The public identifier, if specified,
may also be reported as part of the location information when errors
are reported.

- setPublicId

```java
void setPublicId​(
String
publicId)
```

The public identifier for this input source. This may be mapped to an
input source using an implementation dependent mechanism (such as
catalogues or other mappings). The public identifier, if specified,
may also be reported as part of the location information when errors
are reported.

- getBaseURI

```java
String
getBaseURI()
```

The base URI to be used (see section 5.1.4 in [

IETF RFC 2396

]) for
resolving a relative

systemId

to an absolute URI.

If, when used, the base URI is itself a relative URI, an empty
string, or null, the behavior is implementation dependent.

- setBaseURI

```java
void setBaseURI​(
String
baseURI)
```

The base URI to be used (see section 5.1.4 in [

IETF RFC 2396

]) for
resolving a relative

systemId

to an absolute URI.

If, when used, the base URI is itself a relative URI, an empty
string, or null, the behavior is implementation dependent.

- getEncoding

```java
String
getEncoding()
```

The character encoding, if known. The encoding must be a string
acceptable for an XML encoding declaration ([

XML 1.0

] section
4.3.3 "Character Encoding in Entities").

This attribute has no effect when the application provides a
character stream or string data. For other sources of input, an
encoding specified by means of this attribute will override any
encoding specified in the XML declaration or the Text declaration, or
an encoding obtained from a higher level protocol, such as HTTP [

IETF RFC 2616

].

- setEncoding

```java
void setEncoding​(
String
encoding)
```

The character encoding, if known. The encoding must be a string
acceptable for an XML encoding declaration ([

XML 1.0

] section
4.3.3 "Character Encoding in Entities").

This attribute has no effect when the application provides a
character stream or string data. For other sources of input, an
encoding specified by means of this attribute will override any
encoding specified in the XML declaration or the Text declaration, or
an encoding obtained from a higher level protocol, such as HTTP [

IETF RFC 2616

].

- getCertifiedText

```java
boolean getCertifiedText()
```

If set to true, assume that the input is certified (see section 2.13
in [

XML 1.1

]) when
parsing [

XML 1.1

].

- setCertifiedText

```java
void setCertifiedText​(boolean certifiedText)
```

If set to true, assume that the input is certified (see section 2.13
in [

XML 1.1

]) when
parsing [

XML 1.1

].

Method Detail

- getCharacterStream

```java
Reader
getCharacterStream()
```

An attribute of a language and binding dependent type that represents
a stream of 16-bit units. The application must encode the stream
using UTF-16 (defined in [Unicode] and in [ISO/IEC 10646]). It is not a requirement to have an XML declaration when
using character streams. If an XML declaration is present, the value
of the encoding attribute will be ignored.

- setCharacterStream

```java
void setCharacterStream​(
Reader
characterStream)
```

An attribute of a language and binding dependent type that represents
a stream of 16-bit units. The application must encode the stream
using UTF-16 (defined in [Unicode] and in [ISO/IEC 10646]). It is not a requirement to have an XML declaration when
using character streams. If an XML declaration is present, the value
of the encoding attribute will be ignored.

- getByteStream

```java
InputStream
getByteStream()
```

An attribute of a language and binding dependent type that represents
a stream of bytes.

If the application knows the character encoding of the byte
stream, it should set the encoding attribute. Setting the encoding in
this way will override any encoding specified in an XML declaration
in the data.

- setByteStream

```java
void setByteStream​(
InputStream
byteStream)
```

An attribute of a language and binding dependent type that represents
a stream of bytes.

If the application knows the character encoding of the byte
stream, it should set the encoding attribute. Setting the encoding in
this way will override any encoding specified in an XML declaration
in the data.

- getStringData

```java
String
getStringData()
```

String data to parse. If provided, this will always be treated as a
sequence of 16-bit units (UTF-16 encoded characters). It is not a
requirement to have an XML declaration when using

stringData

. If an XML declaration is present, the value
of the encoding attribute will be ignored.

- setStringData

```java
void setStringData​(
String
stringData)
```

String data to parse. If provided, this will always be treated as a
sequence of 16-bit units (UTF-16 encoded characters). It is not a
requirement to have an XML declaration when using

stringData

. If an XML declaration is present, the value
of the encoding attribute will be ignored.

- getSystemId

```java
String
getSystemId()
```

The system identifier, a URI reference [

IETF RFC 2396

], for this
input source. The system identifier is optional if there is a byte
stream, a character stream, or string data. It is still useful to
provide one, since the application will use it to resolve any
relative URIs and can include it in error messages and warnings. (The
LSParser will only attempt to fetch the resource identified by the
URI reference if there is no other input available in the input
source.)

If the application knows the character encoding of the object
pointed to by the system identifier, it can set the encoding using
the

encoding

attribute.

If the specified system ID is a relative URI reference (see
section 5 in [

IETF RFC 2396

]), the DOM
implementation will attempt to resolve the relative URI with the

baseURI

as the base, if that fails, the behavior is
implementation dependent.

- setSystemId

```java
void setSystemId​(
String
systemId)
```

The system identifier, a URI reference [

IETF RFC 2396

], for this
input source. The system identifier is optional if there is a byte
stream, a character stream, or string data. It is still useful to
provide one, since the application will use it to resolve any
relative URIs and can include it in error messages and warnings. (The
LSParser will only attempt to fetch the resource identified by the
URI reference if there is no other input available in the input
source.)

If the application knows the character encoding of the object
pointed to by the system identifier, it can set the encoding using
the

encoding

attribute.

If the specified system ID is a relative URI reference (see
section 5 in [

IETF RFC 2396

]), the DOM
implementation will attempt to resolve the relative URI with the

baseURI

as the base, if that fails, the behavior is
implementation dependent.

- getPublicId

```java
String
getPublicId()
```

The public identifier for this input source. This may be mapped to an
input source using an implementation dependent mechanism (such as
catalogues or other mappings). The public identifier, if specified,
may also be reported as part of the location information when errors
are reported.

- setPublicId

```java
void setPublicId​(
String
publicId)
```

The public identifier for this input source. This may be mapped to an
input source using an implementation dependent mechanism (such as
catalogues or other mappings). The public identifier, if specified,
may also be reported as part of the location information when errors
are reported.

- getBaseURI

```java
String
getBaseURI()
```

The base URI to be used (see section 5.1.4 in [

IETF RFC 2396

]) for
resolving a relative

systemId

to an absolute URI.

If, when used, the base URI is itself a relative URI, an empty
string, or null, the behavior is implementation dependent.

- setBaseURI

```java
void setBaseURI​(
String
baseURI)
```

The base URI to be used (see section 5.1.4 in [

IETF RFC 2396

]) for
resolving a relative

systemId

to an absolute URI.

If, when used, the base URI is itself a relative URI, an empty
string, or null, the behavior is implementation dependent.

- getEncoding

```java
String
getEncoding()
```

The character encoding, if known. The encoding must be a string
acceptable for an XML encoding declaration ([

XML 1.0

] section
4.3.3 "Character Encoding in Entities").

This attribute has no effect when the application provides a
character stream or string data. For other sources of input, an
encoding specified by means of this attribute will override any
encoding specified in the XML declaration or the Text declaration, or
an encoding obtained from a higher level protocol, such as HTTP [

IETF RFC 2616

].

- setEncoding

```java
void setEncoding​(
String
encoding)
```

The character encoding, if known. The encoding must be a string
acceptable for an XML encoding declaration ([

XML 1.0

] section
4.3.3 "Character Encoding in Entities").

This attribute has no effect when the application provides a
character stream or string data. For other sources of input, an
encoding specified by means of this attribute will override any
encoding specified in the XML declaration or the Text declaration, or
an encoding obtained from a higher level protocol, such as HTTP [

IETF RFC 2616

].

- getCertifiedText

```java
boolean getCertifiedText()
```

If set to true, assume that the input is certified (see section 2.13
in [

XML 1.1

]) when
parsing [

XML 1.1

].

- setCertifiedText

```java
void setCertifiedText​(boolean certifiedText)
```

If set to true, assume that the input is certified (see section 2.13
in [

XML 1.1

]) when
parsing [

XML 1.1

].

---

#### Method Detail

getCharacterStream

```java
Reader
getCharacterStream()
```

An attribute of a language and binding dependent type that represents
a stream of 16-bit units. The application must encode the stream
using UTF-16 (defined in [Unicode] and in [ISO/IEC 10646]). It is not a requirement to have an XML declaration when
using character streams. If an XML declaration is present, the value
of the encoding attribute will be ignored.

---

#### getCharacterStream

Reader

getCharacterStream()

An attribute of a language and binding dependent type that represents
a stream of 16-bit units. The application must encode the stream
using UTF-16 (defined in [Unicode] and in [ISO/IEC 10646]). It is not a requirement to have an XML declaration when
using character streams. If an XML declaration is present, the value
of the encoding attribute will be ignored.

setCharacterStream

```java
void setCharacterStream​(
Reader
characterStream)
```

An attribute of a language and binding dependent type that represents
a stream of 16-bit units. The application must encode the stream
using UTF-16 (defined in [Unicode] and in [ISO/IEC 10646]). It is not a requirement to have an XML declaration when
using character streams. If an XML declaration is present, the value
of the encoding attribute will be ignored.

---

#### setCharacterStream

void setCharacterStream​(

Reader

characterStream)

An attribute of a language and binding dependent type that represents
a stream of 16-bit units. The application must encode the stream
using UTF-16 (defined in [Unicode] and in [ISO/IEC 10646]). It is not a requirement to have an XML declaration when
using character streams. If an XML declaration is present, the value
of the encoding attribute will be ignored.

getByteStream

```java
InputStream
getByteStream()
```

An attribute of a language and binding dependent type that represents
a stream of bytes.

If the application knows the character encoding of the byte
stream, it should set the encoding attribute. Setting the encoding in
this way will override any encoding specified in an XML declaration
in the data.

---

#### getByteStream

InputStream

getByteStream()

An attribute of a language and binding dependent type that represents
a stream of bytes.

If the application knows the character encoding of the byte
stream, it should set the encoding attribute. Setting the encoding in
this way will override any encoding specified in an XML declaration
in the data.

setByteStream

```java
void setByteStream​(
InputStream
byteStream)
```

An attribute of a language and binding dependent type that represents
a stream of bytes.

If the application knows the character encoding of the byte
stream, it should set the encoding attribute. Setting the encoding in
this way will override any encoding specified in an XML declaration
in the data.

---

#### setByteStream

void setByteStream​(

InputStream

byteStream)

An attribute of a language and binding dependent type that represents
a stream of bytes.

If the application knows the character encoding of the byte
stream, it should set the encoding attribute. Setting the encoding in
this way will override any encoding specified in an XML declaration
in the data.

getStringData

```java
String
getStringData()
```

String data to parse. If provided, this will always be treated as a
sequence of 16-bit units (UTF-16 encoded characters). It is not a
requirement to have an XML declaration when using

stringData

. If an XML declaration is present, the value
of the encoding attribute will be ignored.

---

#### getStringData

String

getStringData()

String data to parse. If provided, this will always be treated as a
sequence of 16-bit units (UTF-16 encoded characters). It is not a
requirement to have an XML declaration when using

stringData

. If an XML declaration is present, the value
of the encoding attribute will be ignored.

setStringData

```java
void setStringData​(
String
stringData)
```

String data to parse. If provided, this will always be treated as a
sequence of 16-bit units (UTF-16 encoded characters). It is not a
requirement to have an XML declaration when using

stringData

. If an XML declaration is present, the value
of the encoding attribute will be ignored.

---

#### setStringData

void setStringData​(

String

stringData)

String data to parse. If provided, this will always be treated as a
sequence of 16-bit units (UTF-16 encoded characters). It is not a
requirement to have an XML declaration when using

stringData

. If an XML declaration is present, the value
of the encoding attribute will be ignored.

getSystemId

```java
String
getSystemId()
```

The system identifier, a URI reference [

IETF RFC 2396

], for this
input source. The system identifier is optional if there is a byte
stream, a character stream, or string data. It is still useful to
provide one, since the application will use it to resolve any
relative URIs and can include it in error messages and warnings. (The
LSParser will only attempt to fetch the resource identified by the
URI reference if there is no other input available in the input
source.)

If the application knows the character encoding of the object
pointed to by the system identifier, it can set the encoding using
the

encoding

attribute.

If the specified system ID is a relative URI reference (see
section 5 in [

IETF RFC 2396

]), the DOM
implementation will attempt to resolve the relative URI with the

baseURI

as the base, if that fails, the behavior is
implementation dependent.

---

#### getSystemId

String

getSystemId()

The system identifier, a URI reference [

IETF RFC 2396

], for this
input source. The system identifier is optional if there is a byte
stream, a character stream, or string data. It is still useful to
provide one, since the application will use it to resolve any
relative URIs and can include it in error messages and warnings. (The
LSParser will only attempt to fetch the resource identified by the
URI reference if there is no other input available in the input
source.)

If the application knows the character encoding of the object
pointed to by the system identifier, it can set the encoding using
the

encoding

attribute.

If the specified system ID is a relative URI reference (see
section 5 in [

IETF RFC 2396

]), the DOM
implementation will attempt to resolve the relative URI with the

baseURI

as the base, if that fails, the behavior is
implementation dependent.

setSystemId

```java
void setSystemId​(
String
systemId)
```

The system identifier, a URI reference [

IETF RFC 2396

], for this
input source. The system identifier is optional if there is a byte
stream, a character stream, or string data. It is still useful to
provide one, since the application will use it to resolve any
relative URIs and can include it in error messages and warnings. (The
LSParser will only attempt to fetch the resource identified by the
URI reference if there is no other input available in the input
source.)

If the application knows the character encoding of the object
pointed to by the system identifier, it can set the encoding using
the

encoding

attribute.

If the specified system ID is a relative URI reference (see
section 5 in [

IETF RFC 2396

]), the DOM
implementation will attempt to resolve the relative URI with the

baseURI

as the base, if that fails, the behavior is
implementation dependent.

---

#### setSystemId

void setSystemId​(

String

systemId)

The system identifier, a URI reference [

IETF RFC 2396

], for this
input source. The system identifier is optional if there is a byte
stream, a character stream, or string data. It is still useful to
provide one, since the application will use it to resolve any
relative URIs and can include it in error messages and warnings. (The
LSParser will only attempt to fetch the resource identified by the
URI reference if there is no other input available in the input
source.)

If the application knows the character encoding of the object
pointed to by the system identifier, it can set the encoding using
the

encoding

attribute.

If the specified system ID is a relative URI reference (see
section 5 in [

IETF RFC 2396

]), the DOM
implementation will attempt to resolve the relative URI with the

baseURI

as the base, if that fails, the behavior is
implementation dependent.

getPublicId

```java
String
getPublicId()
```

The public identifier for this input source. This may be mapped to an
input source using an implementation dependent mechanism (such as
catalogues or other mappings). The public identifier, if specified,
may also be reported as part of the location information when errors
are reported.

---

#### getPublicId

String

getPublicId()

The public identifier for this input source. This may be mapped to an
input source using an implementation dependent mechanism (such as
catalogues or other mappings). The public identifier, if specified,
may also be reported as part of the location information when errors
are reported.

setPublicId

```java
void setPublicId​(
String
publicId)
```

The public identifier for this input source. This may be mapped to an
input source using an implementation dependent mechanism (such as
catalogues or other mappings). The public identifier, if specified,
may also be reported as part of the location information when errors
are reported.

---

#### setPublicId

void setPublicId​(

String

publicId)

The public identifier for this input source. This may be mapped to an
input source using an implementation dependent mechanism (such as
catalogues or other mappings). The public identifier, if specified,
may also be reported as part of the location information when errors
are reported.

getBaseURI

```java
String
getBaseURI()
```

The base URI to be used (see section 5.1.4 in [

IETF RFC 2396

]) for
resolving a relative

systemId

to an absolute URI.

If, when used, the base URI is itself a relative URI, an empty
string, or null, the behavior is implementation dependent.

---

#### getBaseURI

String

getBaseURI()

The base URI to be used (see section 5.1.4 in [

IETF RFC 2396

]) for
resolving a relative

systemId

to an absolute URI.

If, when used, the base URI is itself a relative URI, an empty
string, or null, the behavior is implementation dependent.

setBaseURI

```java
void setBaseURI​(
String
baseURI)
```

The base URI to be used (see section 5.1.4 in [

IETF RFC 2396

]) for
resolving a relative

systemId

to an absolute URI.

If, when used, the base URI is itself a relative URI, an empty
string, or null, the behavior is implementation dependent.

---

#### setBaseURI

void setBaseURI​(

String

baseURI)

The base URI to be used (see section 5.1.4 in [

IETF RFC 2396

]) for
resolving a relative

systemId

to an absolute URI.

If, when used, the base URI is itself a relative URI, an empty
string, or null, the behavior is implementation dependent.

getEncoding

```java
String
getEncoding()
```

The character encoding, if known. The encoding must be a string
acceptable for an XML encoding declaration ([

XML 1.0

] section
4.3.3 "Character Encoding in Entities").

This attribute has no effect when the application provides a
character stream or string data. For other sources of input, an
encoding specified by means of this attribute will override any
encoding specified in the XML declaration or the Text declaration, or
an encoding obtained from a higher level protocol, such as HTTP [

IETF RFC 2616

].

---

#### getEncoding

String

getEncoding()

The character encoding, if known. The encoding must be a string
acceptable for an XML encoding declaration ([

XML 1.0

] section
4.3.3 "Character Encoding in Entities").

This attribute has no effect when the application provides a
character stream or string data. For other sources of input, an
encoding specified by means of this attribute will override any
encoding specified in the XML declaration or the Text declaration, or
an encoding obtained from a higher level protocol, such as HTTP [

IETF RFC 2616

].

setEncoding

```java
void setEncoding​(
String
encoding)
```

The character encoding, if known. The encoding must be a string
acceptable for an XML encoding declaration ([

XML 1.0

] section
4.3.3 "Character Encoding in Entities").

This attribute has no effect when the application provides a
character stream or string data. For other sources of input, an
encoding specified by means of this attribute will override any
encoding specified in the XML declaration or the Text declaration, or
an encoding obtained from a higher level protocol, such as HTTP [

IETF RFC 2616

].

---

#### setEncoding

void setEncoding​(

String

encoding)

The character encoding, if known. The encoding must be a string
acceptable for an XML encoding declaration ([

XML 1.0

] section
4.3.3 "Character Encoding in Entities").

This attribute has no effect when the application provides a
character stream or string data. For other sources of input, an
encoding specified by means of this attribute will override any
encoding specified in the XML declaration or the Text declaration, or
an encoding obtained from a higher level protocol, such as HTTP [

IETF RFC 2616

].

getCertifiedText

```java
boolean getCertifiedText()
```

If set to true, assume that the input is certified (see section 2.13
in [

XML 1.1

]) when
parsing [

XML 1.1

].

---

#### getCertifiedText

boolean getCertifiedText()

If set to true, assume that the input is certified (see section 2.13
in [

XML 1.1

]) when
parsing [

XML 1.1

].

setCertifiedText

```java
void setCertifiedText​(boolean certifiedText)
```

If set to true, assume that the input is certified (see section 2.13
in [

XML 1.1

]) when
parsing [

XML 1.1

].

---

#### setCertifiedText

void setCertifiedText​(boolean certifiedText)

If set to true, assume that the input is certified (see section 2.13
in [

XML 1.1

]) when
parsing [

XML 1.1

].

---

