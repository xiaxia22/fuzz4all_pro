# Class InputSource

**Source:** `java.xml\org\xml\sax\InputSource.html`

### Class Description

```java
public class
InputSource

extends
Object
```

A single input source for an XML entity.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

This class allows a SAX application to encapsulate information
about an input source in a single object, which may include
a public identifier, a system identifier, a byte stream (possibly
with a specified encoding), and/or a character stream.

There are two places that the application can deliver an
input source to the parser: as the argument to the Parser.parse
method, or as the return value of the EntityResolver.resolveEntity
method.

The SAX parser will use the InputSource object to determine how
to read XML input. If there is a character stream available, the
parser will read that stream directly, disregarding any text
encoding declaration found in that stream.
If there is no character stream, but there is
a byte stream, the parser will use that byte stream, using the
encoding specified in the InputSource or else (if no encoding is
specified) autodetecting the character encoding using an algorithm
such as the one in the XML specification. If neither a character
stream nor a
byte stream is available, the parser will attempt to open a URI
connection to the resource identified by the system
identifier.

An InputSource object belongs to the application: the SAX parser
shall never modify it in any way (it may modify a copy if
necessary). However, standard processing of both byte and
character streams is to close them on as part of end-of-parse cleanup,
so applications should not attempt to re-use such streams after they
have been handed to a parser.

**Since:** 1.4, SAX 1.0
**See Also:** XMLReader.parse(org.xml.sax.InputSource)

,

EntityResolver.resolveEntity(java.lang.String, java.lang.String)

,

InputStream

,

Reader

---

### Field Details

*No entries found.*

### Constructor Details

#### public InputSource()

Zero-argument default constructor.

**See Also:**
- setPublicId(java.lang.String)

,

setSystemId(java.lang.String)

,

setByteStream(java.io.InputStream)

,

setCharacterStream(java.io.Reader)

,

setEncoding(java.lang.String)

---

#### public InputSource​(
String
systemId)

Create a new input source with a system identifier.

Applications may use setPublicId to include a
public identifier as well, or setEncoding to specify
the character encoding, if known.

If the system identifier is a URL, it must be fully
resolved (it may not be a relative URL).

**Parameters:**
- systemId

- The system identifier (URI).

**See Also:**
- setPublicId(java.lang.String)

,

setSystemId(java.lang.String)

,

setByteStream(java.io.InputStream)

,

setEncoding(java.lang.String)

,

setCharacterStream(java.io.Reader)

---

#### public InputSource​(
InputStream
byteStream)

Create a new input source with a byte stream.

Application writers should use setSystemId() to provide a base
for resolving relative URIs, may use setPublicId to include a
public identifier, and may use setEncoding to specify the object's
character encoding.

**Parameters:**
- byteStream

- The raw byte stream containing the document.

**See Also:**
- setPublicId(java.lang.String)

,

setSystemId(java.lang.String)

,

setEncoding(java.lang.String)

,

setByteStream(java.io.InputStream)

,

setCharacterStream(java.io.Reader)

---

#### public InputSource​(
Reader
characterStream)

Create a new input source with a character stream.

Application writers should use setSystemId() to provide a base
for resolving relative URIs, and may use setPublicId to include a
public identifier.

The character stream shall not include a byte order mark.

**See Also:**
- setPublicId(java.lang.String)

,

setSystemId(java.lang.String)

,

setByteStream(java.io.InputStream)

,

setCharacterStream(java.io.Reader)

---

### Method Details

#### public void setPublicId​(
String
publicId)

Set the public identifier for this input source.

The public identifier is always optional: if the application
writer includes one, it will be provided as part of the
location information.

**Parameters:**
- publicId

- The public identifier as a string.

**See Also:**
- getPublicId()

,

Locator.getPublicId()

,

SAXParseException.getPublicId()

---

#### public
String
getPublicId()

Get the public identifier for this input source.

**Returns:**
- The public identifier, or null if none was supplied.

**See Also:**
- setPublicId(java.lang.String)

---

#### public void setSystemId​(
String
systemId)

Set the system identifier for this input source.

The system identifier is optional if there is a byte stream
or a character stream, but it is still useful to provide one,
since the application can use it to resolve relative URIs
and can include it in error messages and warnings (the parser
will attempt to open a connection to the URI only if
there is no byte stream or character stream specified).

If the application knows the character encoding of the
object pointed to by the system identifier, it can register
the encoding using the setEncoding method.

If the system identifier is a URL, it must be fully
resolved (it may not be a relative URL).

**Parameters:**
- systemId

- The system identifier as a string.

**See Also:**
- setEncoding(java.lang.String)

,

getSystemId()

,

Locator.getSystemId()

,

SAXParseException.getSystemId()

---

#### public
String
getSystemId()

Get the system identifier for this input source.

The getEncoding method will return the character encoding
of the object pointed to, or null if unknown.

If the system ID is a URL, it will be fully resolved.

**Returns:**
- The system identifier, or null if none was supplied.

**See Also:**
- setSystemId(java.lang.String)

,

getEncoding()

---

#### public void setByteStream​(
InputStream
byteStream)

Set the byte stream for this input source.

The SAX parser will ignore this if there is also a character
stream specified, but it will use a byte stream in preference
to opening a URI connection itself.

If the application knows the character encoding of the
byte stream, it should set it with the setEncoding method.

**Parameters:**
- byteStream

- A byte stream containing an XML document or
other entity.

**See Also:**
- setEncoding(java.lang.String)

,

getByteStream()

,

getEncoding()

,

InputStream

---

#### public
InputStream
getByteStream()

Get the byte stream for this input source.

The getEncoding method will return the character
encoding for this byte stream, or null if unknown.

**Returns:**
- The byte stream, or null if none was supplied.

**See Also:**
- getEncoding()

,

setByteStream(java.io.InputStream)

---

#### public void setEncoding​(
String
encoding)

Set the character encoding, if known.

The encoding must be a string acceptable for an
XML encoding declaration (see section 4.3.3 of the XML 1.0
recommendation).

This method has no effect when the application provides a
character stream.

**Parameters:**
- encoding

- A string describing the character encoding.

**See Also:**
- setSystemId(java.lang.String)

,

setByteStream(java.io.InputStream)

,

getEncoding()

---

#### public
String
getEncoding()

Get the character encoding for a byte stream or URI.
This value will be ignored when the application provides a
character stream.

**Returns:**
- The encoding, or null if none was supplied.

**See Also:**
- setByteStream(java.io.InputStream)

,

getSystemId()

,

getByteStream()

---

#### public void setCharacterStream​(
Reader
characterStream)

Set the character stream for this input source.

If there is a character stream specified, the SAX parser
will ignore any byte stream and will not attempt to open
a URI connection to the system identifier.

**Parameters:**
- characterStream

- The character stream containing the
XML document or other entity.

**See Also:**
- getCharacterStream()

,

Reader

---

#### public
Reader
getCharacterStream()

Get the character stream for this input source.

**Returns:**
- The character stream, or null if none was supplied.

**See Also:**
- setCharacterStream(java.io.Reader)

---

#### public boolean isEmpty()

Indicates whether the

InputSource

object is empty. Empty is
defined as follows:

- All of the input sources, including the public identifier, system
identifier, byte stream, and character stream, are

null

.
- The public identifier and system identifier are

null

, and
byte and character stream are either

null

or contain no byte
or character.

Note that this method will reset the byte stream if it is provided, or
the character stream if the byte stream is not provided.

In case of error while checking the byte or character stream, the method
will return false to allow the XML processor to handle the error.

**Returns:**
- true if the

InputSource

object is empty, false otherwise

---

### Additional Sections

#### Class InputSource

java.lang.Object

- org.xml.sax.InputSource

org.xml.sax.InputSource

```java
public class
InputSource

extends
Object
```

A single input source for an XML entity.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

This class allows a SAX application to encapsulate information
about an input source in a single object, which may include
a public identifier, a system identifier, a byte stream (possibly
with a specified encoding), and/or a character stream.

There are two places that the application can deliver an
input source to the parser: as the argument to the Parser.parse
method, or as the return value of the EntityResolver.resolveEntity
method.

The SAX parser will use the InputSource object to determine how
to read XML input. If there is a character stream available, the
parser will read that stream directly, disregarding any text
encoding declaration found in that stream.
If there is no character stream, but there is
a byte stream, the parser will use that byte stream, using the
encoding specified in the InputSource or else (if no encoding is
specified) autodetecting the character encoding using an algorithm
such as the one in the XML specification. If neither a character
stream nor a
byte stream is available, the parser will attempt to open a URI
connection to the resource identified by the system
identifier.

An InputSource object belongs to the application: the SAX parser
shall never modify it in any way (it may modify a copy if
necessary). However, standard processing of both byte and
character streams is to close them on as part of end-of-parse cleanup,
so applications should not attempt to re-use such streams after they
have been handed to a parser.

**Since:** 1.4, SAX 1.0
**See Also:** XMLReader.parse(org.xml.sax.InputSource)

,

EntityResolver.resolveEntity(java.lang.String, java.lang.String)

,

InputStream

,

Reader

public class

InputSource

extends

Object

A single input source for an XML entity.

This module, both source code and documentation, is in the
Public Domain, and comes with

NO WARRANTY

.

See

http://www.saxproject.org

for further information.

This class allows a SAX application to encapsulate information
about an input source in a single object, which may include
a public identifier, a system identifier, a byte stream (possibly
with a specified encoding), and/or a character stream.

There are two places that the application can deliver an
input source to the parser: as the argument to the Parser.parse
method, or as the return value of the EntityResolver.resolveEntity
method.

The SAX parser will use the InputSource object to determine how
to read XML input. If there is a character stream available, the
parser will read that stream directly, disregarding any text
encoding declaration found in that stream.
If there is no character stream, but there is
a byte stream, the parser will use that byte stream, using the
encoding specified in the InputSource or else (if no encoding is
specified) autodetecting the character encoding using an algorithm
such as the one in the XML specification. If neither a character
stream nor a
byte stream is available, the parser will attempt to open a URI
connection to the resource identified by the system
identifier.

An InputSource object belongs to the application: the SAX parser
shall never modify it in any way (it may modify a copy if
necessary). However, standard processing of both byte and
character streams is to close them on as part of end-of-parse cleanup,
so applications should not attempt to re-use such streams after they
have been handed to a parser.

This class allows a SAX application to encapsulate information
about an input source in a single object, which may include
a public identifier, a system identifier, a byte stream (possibly
with a specified encoding), and/or a character stream.

There are two places that the application can deliver an
input source to the parser: as the argument to the Parser.parse
method, or as the return value of the EntityResolver.resolveEntity
method.

The SAX parser will use the InputSource object to determine how
to read XML input. If there is a character stream available, the
parser will read that stream directly, disregarding any text
encoding declaration found in that stream.
If there is no character stream, but there is
a byte stream, the parser will use that byte stream, using the
encoding specified in the InputSource or else (if no encoding is
specified) autodetecting the character encoding using an algorithm
such as the one in the XML specification. If neither a character
stream nor a
byte stream is available, the parser will attempt to open a URI
connection to the resource identified by the system
identifier.

An InputSource object belongs to the application: the SAX parser
shall never modify it in any way (it may modify a copy if
necessary). However, standard processing of both byte and
character streams is to close them on as part of end-of-parse cleanup,
so applications should not attempt to re-use such streams after they
have been handed to a parser.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

InputSource

()

Zero-argument default constructor.

InputSource

​(

InputStream

byteStream)

Create a new input source with a byte stream.

InputSource

​(

Reader

characterStream)

Create a new input source with a character stream.

InputSource

​(

String

systemId)

Create a new input source with a system identifier.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

InputStream

getByteStream

()

Get the byte stream for this input source.

Reader

getCharacterStream

()

Get the character stream for this input source.

String

getEncoding

()

Get the character encoding for a byte stream or URI.

String

getPublicId

()

Get the public identifier for this input source.

String

getSystemId

()

Get the system identifier for this input source.

boolean

isEmpty

()

Indicates whether the

InputSource

object is empty.

void

setByteStream

​(

InputStream

byteStream)

Set the byte stream for this input source.

void

setCharacterStream

​(

Reader

characterStream)

Set the character stream for this input source.

void

setEncoding

​(

String

encoding)

Set the character encoding, if known.

void

setPublicId

​(

String

publicId)

Set the public identifier for this input source.

void

setSystemId

​(

String

systemId)

Set the system identifier for this input source.

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

InputSource

()

Zero-argument default constructor.

InputSource

​(

InputStream

byteStream)

Create a new input source with a byte stream.

InputSource

​(

Reader

characterStream)

Create a new input source with a character stream.

InputSource

​(

String

systemId)

Create a new input source with a system identifier.

---

#### Constructor Summary

Zero-argument default constructor.

Create a new input source with a byte stream.

Create a new input source with a character stream.

Create a new input source with a system identifier.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

InputStream

getByteStream

()

Get the byte stream for this input source.

Reader

getCharacterStream

()

Get the character stream for this input source.

String

getEncoding

()

Get the character encoding for a byte stream or URI.

String

getPublicId

()

Get the public identifier for this input source.

String

getSystemId

()

Get the system identifier for this input source.

boolean

isEmpty

()

Indicates whether the

InputSource

object is empty.

void

setByteStream

​(

InputStream

byteStream)

Set the byte stream for this input source.

void

setCharacterStream

​(

Reader

characterStream)

Set the character stream for this input source.

void

setEncoding

​(

String

encoding)

Set the character encoding, if known.

void

setPublicId

​(

String

publicId)

Set the public identifier for this input source.

void

setSystemId

​(

String

systemId)

Set the system identifier for this input source.

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

Get the byte stream for this input source.

Get the character stream for this input source.

Get the character encoding for a byte stream or URI.

Get the public identifier for this input source.

Get the system identifier for this input source.

Indicates whether the

InputSource

object is empty.

Set the byte stream for this input source.

Set the character stream for this input source.

Set the character encoding, if known.

Set the public identifier for this input source.

Set the system identifier for this input source.

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

- InputSource

```java
public InputSource()
```

Zero-argument default constructor.

**See Also:** setPublicId(java.lang.String)

,

setSystemId(java.lang.String)

,

setByteStream(java.io.InputStream)

,

setCharacterStream(java.io.Reader)

,

setEncoding(java.lang.String)

- InputSource

```java
public InputSource​(
String
systemId)
```

Create a new input source with a system identifier.

Applications may use setPublicId to include a
public identifier as well, or setEncoding to specify
the character encoding, if known.

If the system identifier is a URL, it must be fully
resolved (it may not be a relative URL).

**Parameters:** systemId

- The system identifier (URI).
**See Also:** setPublicId(java.lang.String)

,

setSystemId(java.lang.String)

,

setByteStream(java.io.InputStream)

,

setEncoding(java.lang.String)

,

setCharacterStream(java.io.Reader)

- InputSource

```java
public InputSource​(
InputStream
byteStream)
```

Create a new input source with a byte stream.

Application writers should use setSystemId() to provide a base
for resolving relative URIs, may use setPublicId to include a
public identifier, and may use setEncoding to specify the object's
character encoding.

**Parameters:** byteStream

- The raw byte stream containing the document.
**See Also:** setPublicId(java.lang.String)

,

setSystemId(java.lang.String)

,

setEncoding(java.lang.String)

,

setByteStream(java.io.InputStream)

,

setCharacterStream(java.io.Reader)

- InputSource

```java
public InputSource​(
Reader
characterStream)
```

Create a new input source with a character stream.

Application writers should use setSystemId() to provide a base
for resolving relative URIs, and may use setPublicId to include a
public identifier.

The character stream shall not include a byte order mark.

**See Also:** setPublicId(java.lang.String)

,

setSystemId(java.lang.String)

,

setByteStream(java.io.InputStream)

,

setCharacterStream(java.io.Reader)

============ METHOD DETAIL ==========

- Method Detail

- setPublicId

```java
public void setPublicId​(
String
publicId)
```

Set the public identifier for this input source.

The public identifier is always optional: if the application
writer includes one, it will be provided as part of the
location information.

**Parameters:** publicId

- The public identifier as a string.
**See Also:** getPublicId()

,

Locator.getPublicId()

,

SAXParseException.getPublicId()

- getPublicId

```java
public
String
getPublicId()
```

Get the public identifier for this input source.

**Returns:** The public identifier, or null if none was supplied.
**See Also:** setPublicId(java.lang.String)

- setSystemId

```java
public void setSystemId​(
String
systemId)
```

Set the system identifier for this input source.

The system identifier is optional if there is a byte stream
or a character stream, but it is still useful to provide one,
since the application can use it to resolve relative URIs
and can include it in error messages and warnings (the parser
will attempt to open a connection to the URI only if
there is no byte stream or character stream specified).

If the application knows the character encoding of the
object pointed to by the system identifier, it can register
the encoding using the setEncoding method.

If the system identifier is a URL, it must be fully
resolved (it may not be a relative URL).

**Parameters:** systemId

- The system identifier as a string.
**See Also:** setEncoding(java.lang.String)

,

getSystemId()

,

Locator.getSystemId()

,

SAXParseException.getSystemId()

- getSystemId

```java
public
String
getSystemId()
```

Get the system identifier for this input source.

The getEncoding method will return the character encoding
of the object pointed to, or null if unknown.

If the system ID is a URL, it will be fully resolved.

**Returns:** The system identifier, or null if none was supplied.
**See Also:** setSystemId(java.lang.String)

,

getEncoding()

- setByteStream

```java
public void setByteStream​(
InputStream
byteStream)
```

Set the byte stream for this input source.

The SAX parser will ignore this if there is also a character
stream specified, but it will use a byte stream in preference
to opening a URI connection itself.

If the application knows the character encoding of the
byte stream, it should set it with the setEncoding method.

**Parameters:** byteStream

- A byte stream containing an XML document or
other entity.
**See Also:** setEncoding(java.lang.String)

,

getByteStream()

,

getEncoding()

,

InputStream

- getByteStream

```java
public
InputStream
getByteStream()
```

Get the byte stream for this input source.

The getEncoding method will return the character
encoding for this byte stream, or null if unknown.

**Returns:** The byte stream, or null if none was supplied.
**See Also:** getEncoding()

,

setByteStream(java.io.InputStream)

- setEncoding

```java
public void setEncoding​(
String
encoding)
```

Set the character encoding, if known.

The encoding must be a string acceptable for an
XML encoding declaration (see section 4.3.3 of the XML 1.0
recommendation).

This method has no effect when the application provides a
character stream.

**Parameters:** encoding

- A string describing the character encoding.
**See Also:** setSystemId(java.lang.String)

,

setByteStream(java.io.InputStream)

,

getEncoding()

- getEncoding

```java
public
String
getEncoding()
```

Get the character encoding for a byte stream or URI.
This value will be ignored when the application provides a
character stream.

**Returns:** The encoding, or null if none was supplied.
**See Also:** setByteStream(java.io.InputStream)

,

getSystemId()

,

getByteStream()

- setCharacterStream

```java
public void setCharacterStream​(
Reader
characterStream)
```

Set the character stream for this input source.

If there is a character stream specified, the SAX parser
will ignore any byte stream and will not attempt to open
a URI connection to the system identifier.

**Parameters:** characterStream

- The character stream containing the
XML document or other entity.
**See Also:** getCharacterStream()

,

Reader

- getCharacterStream

```java
public
Reader
getCharacterStream()
```

Get the character stream for this input source.

**Returns:** The character stream, or null if none was supplied.
**See Also:** setCharacterStream(java.io.Reader)

- isEmpty

```java
public boolean isEmpty()
```

Indicates whether the

InputSource

object is empty. Empty is
defined as follows:

- All of the input sources, including the public identifier, system
identifier, byte stream, and character stream, are

null

.
- The public identifier and system identifier are

null

, and
byte and character stream are either

null

or contain no byte
or character.

Note that this method will reset the byte stream if it is provided, or
the character stream if the byte stream is not provided.

In case of error while checking the byte or character stream, the method
will return false to allow the XML processor to handle the error.

**Returns:** true if the

InputSource

object is empty, false otherwise

Constructor Detail

- InputSource

```java
public InputSource()
```

Zero-argument default constructor.

**See Also:** setPublicId(java.lang.String)

,

setSystemId(java.lang.String)

,

setByteStream(java.io.InputStream)

,

setCharacterStream(java.io.Reader)

,

setEncoding(java.lang.String)

- InputSource

```java
public InputSource​(
String
systemId)
```

Create a new input source with a system identifier.

Applications may use setPublicId to include a
public identifier as well, or setEncoding to specify
the character encoding, if known.

If the system identifier is a URL, it must be fully
resolved (it may not be a relative URL).

**Parameters:** systemId

- The system identifier (URI).
**See Also:** setPublicId(java.lang.String)

,

setSystemId(java.lang.String)

,

setByteStream(java.io.InputStream)

,

setEncoding(java.lang.String)

,

setCharacterStream(java.io.Reader)

- InputSource

```java
public InputSource​(
InputStream
byteStream)
```

Create a new input source with a byte stream.

Application writers should use setSystemId() to provide a base
for resolving relative URIs, may use setPublicId to include a
public identifier, and may use setEncoding to specify the object's
character encoding.

**Parameters:** byteStream

- The raw byte stream containing the document.
**See Also:** setPublicId(java.lang.String)

,

setSystemId(java.lang.String)

,

setEncoding(java.lang.String)

,

setByteStream(java.io.InputStream)

,

setCharacterStream(java.io.Reader)

- InputSource

```java
public InputSource​(
Reader
characterStream)
```

Create a new input source with a character stream.

Application writers should use setSystemId() to provide a base
for resolving relative URIs, and may use setPublicId to include a
public identifier.

The character stream shall not include a byte order mark.

**See Also:** setPublicId(java.lang.String)

,

setSystemId(java.lang.String)

,

setByteStream(java.io.InputStream)

,

setCharacterStream(java.io.Reader)

---

#### Constructor Detail

InputSource

```java
public InputSource()
```

Zero-argument default constructor.

**See Also:** setPublicId(java.lang.String)

,

setSystemId(java.lang.String)

,

setByteStream(java.io.InputStream)

,

setCharacterStream(java.io.Reader)

,

setEncoding(java.lang.String)

---

#### InputSource

public InputSource()

Zero-argument default constructor.

InputSource

```java
public InputSource​(
String
systemId)
```

Create a new input source with a system identifier.

Applications may use setPublicId to include a
public identifier as well, or setEncoding to specify
the character encoding, if known.

If the system identifier is a URL, it must be fully
resolved (it may not be a relative URL).

**Parameters:** systemId

- The system identifier (URI).
**See Also:** setPublicId(java.lang.String)

,

setSystemId(java.lang.String)

,

setByteStream(java.io.InputStream)

,

setEncoding(java.lang.String)

,

setCharacterStream(java.io.Reader)

---

#### InputSource

public InputSource​(

String

systemId)

Create a new input source with a system identifier.

Applications may use setPublicId to include a
public identifier as well, or setEncoding to specify
the character encoding, if known.

If the system identifier is a URL, it must be fully
resolved (it may not be a relative URL).

Applications may use setPublicId to include a
public identifier as well, or setEncoding to specify
the character encoding, if known.

If the system identifier is a URL, it must be fully
resolved (it may not be a relative URL).

InputSource

```java
public InputSource​(
InputStream
byteStream)
```

Create a new input source with a byte stream.

Application writers should use setSystemId() to provide a base
for resolving relative URIs, may use setPublicId to include a
public identifier, and may use setEncoding to specify the object's
character encoding.

**Parameters:** byteStream

- The raw byte stream containing the document.
**See Also:** setPublicId(java.lang.String)

,

setSystemId(java.lang.String)

,

setEncoding(java.lang.String)

,

setByteStream(java.io.InputStream)

,

setCharacterStream(java.io.Reader)

---

#### InputSource

public InputSource​(

InputStream

byteStream)

Create a new input source with a byte stream.

Application writers should use setSystemId() to provide a base
for resolving relative URIs, may use setPublicId to include a
public identifier, and may use setEncoding to specify the object's
character encoding.

Application writers should use setSystemId() to provide a base
for resolving relative URIs, may use setPublicId to include a
public identifier, and may use setEncoding to specify the object's
character encoding.

InputSource

```java
public InputSource​(
Reader
characterStream)
```

Create a new input source with a character stream.

Application writers should use setSystemId() to provide a base
for resolving relative URIs, and may use setPublicId to include a
public identifier.

The character stream shall not include a byte order mark.

**See Also:** setPublicId(java.lang.String)

,

setSystemId(java.lang.String)

,

setByteStream(java.io.InputStream)

,

setCharacterStream(java.io.Reader)

---

#### InputSource

public InputSource​(

Reader

characterStream)

Create a new input source with a character stream.

Application writers should use setSystemId() to provide a base
for resolving relative URIs, and may use setPublicId to include a
public identifier.

The character stream shall not include a byte order mark.

Application writers should use setSystemId() to provide a base
for resolving relative URIs, and may use setPublicId to include a
public identifier.

The character stream shall not include a byte order mark.

Method Detail

- setPublicId

```java
public void setPublicId​(
String
publicId)
```

Set the public identifier for this input source.

The public identifier is always optional: if the application
writer includes one, it will be provided as part of the
location information.

**Parameters:** publicId

- The public identifier as a string.
**See Also:** getPublicId()

,

Locator.getPublicId()

,

SAXParseException.getPublicId()

- getPublicId

```java
public
String
getPublicId()
```

Get the public identifier for this input source.

**Returns:** The public identifier, or null if none was supplied.
**See Also:** setPublicId(java.lang.String)

- setSystemId

```java
public void setSystemId​(
String
systemId)
```

Set the system identifier for this input source.

The system identifier is optional if there is a byte stream
or a character stream, but it is still useful to provide one,
since the application can use it to resolve relative URIs
and can include it in error messages and warnings (the parser
will attempt to open a connection to the URI only if
there is no byte stream or character stream specified).

If the application knows the character encoding of the
object pointed to by the system identifier, it can register
the encoding using the setEncoding method.

If the system identifier is a URL, it must be fully
resolved (it may not be a relative URL).

**Parameters:** systemId

- The system identifier as a string.
**See Also:** setEncoding(java.lang.String)

,

getSystemId()

,

Locator.getSystemId()

,

SAXParseException.getSystemId()

- getSystemId

```java
public
String
getSystemId()
```

Get the system identifier for this input source.

The getEncoding method will return the character encoding
of the object pointed to, or null if unknown.

If the system ID is a URL, it will be fully resolved.

**Returns:** The system identifier, or null if none was supplied.
**See Also:** setSystemId(java.lang.String)

,

getEncoding()

- setByteStream

```java
public void setByteStream​(
InputStream
byteStream)
```

Set the byte stream for this input source.

The SAX parser will ignore this if there is also a character
stream specified, but it will use a byte stream in preference
to opening a URI connection itself.

If the application knows the character encoding of the
byte stream, it should set it with the setEncoding method.

**Parameters:** byteStream

- A byte stream containing an XML document or
other entity.
**See Also:** setEncoding(java.lang.String)

,

getByteStream()

,

getEncoding()

,

InputStream

- getByteStream

```java
public
InputStream
getByteStream()
```

Get the byte stream for this input source.

The getEncoding method will return the character
encoding for this byte stream, or null if unknown.

**Returns:** The byte stream, or null if none was supplied.
**See Also:** getEncoding()

,

setByteStream(java.io.InputStream)

- setEncoding

```java
public void setEncoding​(
String
encoding)
```

Set the character encoding, if known.

The encoding must be a string acceptable for an
XML encoding declaration (see section 4.3.3 of the XML 1.0
recommendation).

This method has no effect when the application provides a
character stream.

**Parameters:** encoding

- A string describing the character encoding.
**See Also:** setSystemId(java.lang.String)

,

setByteStream(java.io.InputStream)

,

getEncoding()

- getEncoding

```java
public
String
getEncoding()
```

Get the character encoding for a byte stream or URI.
This value will be ignored when the application provides a
character stream.

**Returns:** The encoding, or null if none was supplied.
**See Also:** setByteStream(java.io.InputStream)

,

getSystemId()

,

getByteStream()

- setCharacterStream

```java
public void setCharacterStream​(
Reader
characterStream)
```

Set the character stream for this input source.

If there is a character stream specified, the SAX parser
will ignore any byte stream and will not attempt to open
a URI connection to the system identifier.

**Parameters:** characterStream

- The character stream containing the
XML document or other entity.
**See Also:** getCharacterStream()

,

Reader

- getCharacterStream

```java
public
Reader
getCharacterStream()
```

Get the character stream for this input source.

**Returns:** The character stream, or null if none was supplied.
**See Also:** setCharacterStream(java.io.Reader)

- isEmpty

```java
public boolean isEmpty()
```

Indicates whether the

InputSource

object is empty. Empty is
defined as follows:

- All of the input sources, including the public identifier, system
identifier, byte stream, and character stream, are

null

.
- The public identifier and system identifier are

null

, and
byte and character stream are either

null

or contain no byte
or character.

Note that this method will reset the byte stream if it is provided, or
the character stream if the byte stream is not provided.

In case of error while checking the byte or character stream, the method
will return false to allow the XML processor to handle the error.

**Returns:** true if the

InputSource

object is empty, false otherwise

---

#### Method Detail

setPublicId

```java
public void setPublicId​(
String
publicId)
```

Set the public identifier for this input source.

The public identifier is always optional: if the application
writer includes one, it will be provided as part of the
location information.

**Parameters:** publicId

- The public identifier as a string.
**See Also:** getPublicId()

,

Locator.getPublicId()

,

SAXParseException.getPublicId()

---

#### setPublicId

public void setPublicId​(

String

publicId)

Set the public identifier for this input source.

The public identifier is always optional: if the application
writer includes one, it will be provided as part of the
location information.

The public identifier is always optional: if the application
writer includes one, it will be provided as part of the
location information.

getPublicId

```java
public
String
getPublicId()
```

Get the public identifier for this input source.

**Returns:** The public identifier, or null if none was supplied.
**See Also:** setPublicId(java.lang.String)

---

#### getPublicId

public

String

getPublicId()

Get the public identifier for this input source.

setSystemId

```java
public void setSystemId​(
String
systemId)
```

Set the system identifier for this input source.

The system identifier is optional if there is a byte stream
or a character stream, but it is still useful to provide one,
since the application can use it to resolve relative URIs
and can include it in error messages and warnings (the parser
will attempt to open a connection to the URI only if
there is no byte stream or character stream specified).

If the application knows the character encoding of the
object pointed to by the system identifier, it can register
the encoding using the setEncoding method.

If the system identifier is a URL, it must be fully
resolved (it may not be a relative URL).

**Parameters:** systemId

- The system identifier as a string.
**See Also:** setEncoding(java.lang.String)

,

getSystemId()

,

Locator.getSystemId()

,

SAXParseException.getSystemId()

---

#### setSystemId

public void setSystemId​(

String

systemId)

Set the system identifier for this input source.

The system identifier is optional if there is a byte stream
or a character stream, but it is still useful to provide one,
since the application can use it to resolve relative URIs
and can include it in error messages and warnings (the parser
will attempt to open a connection to the URI only if
there is no byte stream or character stream specified).

If the application knows the character encoding of the
object pointed to by the system identifier, it can register
the encoding using the setEncoding method.

If the system identifier is a URL, it must be fully
resolved (it may not be a relative URL).

The system identifier is optional if there is a byte stream
or a character stream, but it is still useful to provide one,
since the application can use it to resolve relative URIs
and can include it in error messages and warnings (the parser
will attempt to open a connection to the URI only if
there is no byte stream or character stream specified).

If the application knows the character encoding of the
object pointed to by the system identifier, it can register
the encoding using the setEncoding method.

If the system identifier is a URL, it must be fully
resolved (it may not be a relative URL).

getSystemId

```java
public
String
getSystemId()
```

Get the system identifier for this input source.

The getEncoding method will return the character encoding
of the object pointed to, or null if unknown.

If the system ID is a URL, it will be fully resolved.

**Returns:** The system identifier, or null if none was supplied.
**See Also:** setSystemId(java.lang.String)

,

getEncoding()

---

#### getSystemId

public

String

getSystemId()

Get the system identifier for this input source.

The getEncoding method will return the character encoding
of the object pointed to, or null if unknown.

If the system ID is a URL, it will be fully resolved.

The getEncoding method will return the character encoding
of the object pointed to, or null if unknown.

If the system ID is a URL, it will be fully resolved.

setByteStream

```java
public void setByteStream​(
InputStream
byteStream)
```

Set the byte stream for this input source.

The SAX parser will ignore this if there is also a character
stream specified, but it will use a byte stream in preference
to opening a URI connection itself.

If the application knows the character encoding of the
byte stream, it should set it with the setEncoding method.

**Parameters:** byteStream

- A byte stream containing an XML document or
other entity.
**See Also:** setEncoding(java.lang.String)

,

getByteStream()

,

getEncoding()

,

InputStream

---

#### setByteStream

public void setByteStream​(

InputStream

byteStream)

Set the byte stream for this input source.

The SAX parser will ignore this if there is also a character
stream specified, but it will use a byte stream in preference
to opening a URI connection itself.

If the application knows the character encoding of the
byte stream, it should set it with the setEncoding method.

The SAX parser will ignore this if there is also a character
stream specified, but it will use a byte stream in preference
to opening a URI connection itself.

If the application knows the character encoding of the
byte stream, it should set it with the setEncoding method.

getByteStream

```java
public
InputStream
getByteStream()
```

Get the byte stream for this input source.

The getEncoding method will return the character
encoding for this byte stream, or null if unknown.

**Returns:** The byte stream, or null if none was supplied.
**See Also:** getEncoding()

,

setByteStream(java.io.InputStream)

---

#### getByteStream

public

InputStream

getByteStream()

Get the byte stream for this input source.

The getEncoding method will return the character
encoding for this byte stream, or null if unknown.

The getEncoding method will return the character
encoding for this byte stream, or null if unknown.

setEncoding

```java
public void setEncoding​(
String
encoding)
```

Set the character encoding, if known.

The encoding must be a string acceptable for an
XML encoding declaration (see section 4.3.3 of the XML 1.0
recommendation).

This method has no effect when the application provides a
character stream.

**Parameters:** encoding

- A string describing the character encoding.
**See Also:** setSystemId(java.lang.String)

,

setByteStream(java.io.InputStream)

,

getEncoding()

---

#### setEncoding

public void setEncoding​(

String

encoding)

Set the character encoding, if known.

The encoding must be a string acceptable for an
XML encoding declaration (see section 4.3.3 of the XML 1.0
recommendation).

This method has no effect when the application provides a
character stream.

The encoding must be a string acceptable for an
XML encoding declaration (see section 4.3.3 of the XML 1.0
recommendation).

This method has no effect when the application provides a
character stream.

getEncoding

```java
public
String
getEncoding()
```

Get the character encoding for a byte stream or URI.
This value will be ignored when the application provides a
character stream.

**Returns:** The encoding, or null if none was supplied.
**See Also:** setByteStream(java.io.InputStream)

,

getSystemId()

,

getByteStream()

---

#### getEncoding

public

String

getEncoding()

Get the character encoding for a byte stream or URI.
This value will be ignored when the application provides a
character stream.

setCharacterStream

```java
public void setCharacterStream​(
Reader
characterStream)
```

Set the character stream for this input source.

If there is a character stream specified, the SAX parser
will ignore any byte stream and will not attempt to open
a URI connection to the system identifier.

**Parameters:** characterStream

- The character stream containing the
XML document or other entity.
**See Also:** getCharacterStream()

,

Reader

---

#### setCharacterStream

public void setCharacterStream​(

Reader

characterStream)

Set the character stream for this input source.

If there is a character stream specified, the SAX parser
will ignore any byte stream and will not attempt to open
a URI connection to the system identifier.

If there is a character stream specified, the SAX parser
will ignore any byte stream and will not attempt to open
a URI connection to the system identifier.

getCharacterStream

```java
public
Reader
getCharacterStream()
```

Get the character stream for this input source.

**Returns:** The character stream, or null if none was supplied.
**See Also:** setCharacterStream(java.io.Reader)

---

#### getCharacterStream

public

Reader

getCharacterStream()

Get the character stream for this input source.

isEmpty

```java
public boolean isEmpty()
```

Indicates whether the

InputSource

object is empty. Empty is
defined as follows:

- All of the input sources, including the public identifier, system
identifier, byte stream, and character stream, are

null

.
- The public identifier and system identifier are

null

, and
byte and character stream are either

null

or contain no byte
or character.

Note that this method will reset the byte stream if it is provided, or
the character stream if the byte stream is not provided.

In case of error while checking the byte or character stream, the method
will return false to allow the XML processor to handle the error.

**Returns:** true if the

InputSource

object is empty, false otherwise

---

#### isEmpty

public boolean isEmpty()

Indicates whether the

InputSource

object is empty. Empty is
defined as follows:

- All of the input sources, including the public identifier, system
identifier, byte stream, and character stream, are

null

.
- The public identifier and system identifier are

null

, and
byte and character stream are either

null

or contain no byte
or character.

Note that this method will reset the byte stream if it is provided, or
the character stream if the byte stream is not provided.

In case of error while checking the byte or character stream, the method
will return false to allow the XML processor to handle the error.

All of the input sources, including the public identifier, system
identifier, byte stream, and character stream, are

null

.

The public identifier and system identifier are

null

, and
byte and character stream are either

null

or contain no byte
or character.

Note that this method will reset the byte stream if it is provided, or
the character stream if the byte stream is not provided.

Note that this method will reset the byte stream if it is provided, or
the character stream if the byte stream is not provided.

In case of error while checking the byte or character stream, the method
will return false to allow the XML processor to handle the error.

---

