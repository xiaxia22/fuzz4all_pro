# Class StreamSource

**Source:** `java.xml\javax\xml\transform\stream\StreamSource.html`

### Class Description

```java
public class
StreamSource

extends
Object

implements
Source
```

Acts as an holder for a transformation Source in the form
of a stream of XML markup.

Note:

Due to their internal use of either a

Reader

or

InputStream

instance,

StreamSource

instances may only be used once.

**All Implemented Interfaces:** Source

---

### Field Details

#### public static final
String
FEATURE

If

TransformerFactory.getFeature(java.lang.String)

returns true when passed this value as an argument,
the Transformer supports Source input of this type.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public StreamSource()

Zero-argument default constructor. If this constructor is used, and
no Stream source is set using

setInputStream(java.io.InputStream inputStream)

or

setReader(java.io.Reader reader)

, then the

Transformer

will
create an empty source

InputStream

using

new InputStream()

.

**See Also:**
- Transformer.transform(Source xmlSource, Result outputTarget)

---

#### public StreamSource​(
InputStream
inputStream)

Construct a StreamSource from a byte stream. Normally,
a stream should be used rather than a reader, so
the XML parser can resolve character encoding specified
by the XML declaration.

If this constructor is used to process a stylesheet, normally
setSystemId should also be called, so that relative URI references
can be resolved.

**Parameters:**
- inputStream

- A valid InputStream reference to an XML stream.

---

#### public StreamSource​(
InputStream
inputStream,

String
systemId)

Construct a StreamSource from a byte stream. Normally,
a stream should be used rather than a reader, so that
the XML parser can resolve character encoding specified
by the XML declaration.

This constructor allows the systemID to be set in addition
to the input stream, which allows relative URIs
to be processed.

**Parameters:**
- inputStream

- A valid InputStream reference to an XML stream.
- systemId

- Must be a String that conforms to the URI syntax.

---

#### public StreamSource​(
Reader
reader)

Construct a StreamSource from a character reader. Normally,
a stream should be used rather than a reader, so that
the XML parser can resolve character encoding specified
by the XML declaration. However, in many cases the encoding
of the input stream is already resolved, as in the case of
reading XML from a StringReader.

**Parameters:**
- reader

- A valid Reader reference to an XML character stream.

---

#### public StreamSource​(
Reader
reader,

String
systemId)

Construct a StreamSource from a character reader. Normally,
a stream should be used rather than a reader, so that
the XML parser may resolve character encoding specified
by the XML declaration. However, in many cases the encoding
of the input stream is already resolved, as in the case of
reading XML from a StringReader.

**Parameters:**
- reader

- A valid Reader reference to an XML character stream.
- systemId

- Must be a String that conforms to the URI syntax.

---

#### public StreamSource​(
String
systemId)

Construct a StreamSource from a URL.

**Parameters:**
- systemId

- Must be a String that conforms to the URI syntax.

---

#### public StreamSource​(
File
f)

Construct a StreamSource from a File.

**Parameters:**
- f

- Must a non-null File reference.

---

### Method Details

#### public void setInputStream​(
InputStream
inputStream)

Set the byte stream to be used as input. Normally,
a stream should be used rather than a reader, so that
the XML parser can resolve character encoding specified
by the XML declaration.

If this Source object is used to process a stylesheet, normally
setSystemId should also be called, so that relative URL references
can be resolved.

**Parameters:**
- inputStream

- A valid InputStream reference to an XML stream.

---

#### public
InputStream
getInputStream()

Get the byte stream that was set with setByteStream.

**Returns:**
- The byte stream that was set with setByteStream, or null
if setByteStream or the ByteStream constructor was not called.

---

#### public void setReader​(
Reader
reader)

Set the input to be a character reader. Normally,
a stream should be used rather than a reader, so that
the XML parser can resolve character encoding specified
by the XML declaration. However, in many cases the encoding
of the input stream is already resolved, as in the case of
reading XML from a StringReader.

**Parameters:**
- reader

- A valid Reader reference to an XML CharacterStream.

---

#### public
Reader
getReader()

Get the character stream that was set with setReader.

**Returns:**
- The character stream that was set with setReader, or null
if setReader or the Reader constructor was not called.

---

#### public void setPublicId​(
String
publicId)

Set the public identifier for this Source.

The public identifier is always optional: if the application
writer includes one, it will be provided as part of the
location information.

**Parameters:**
- publicId

- The public identifier as a string.

---

#### public
String
getPublicId()

Get the public identifier that was set with setPublicId.

**Returns:**
- The public identifier that was set with setPublicId, or null
if setPublicId was not called.

---

#### public void setSystemId​(
String
systemId)

Set the system identifier for this Source.

The system identifier is optional if there is a byte stream
or a character stream, but it is still useful to provide one,
since the application can use it to resolve relative URIs
and can include it in error messages and warnings (the parser
will attempt to open a connection to the URI only if
there is no byte stream or character stream specified).

**Specified by:**
- setSystemId

in interface

Source

**Parameters:**
- systemId

- The system identifier as a URL string.

---

#### public
String
getSystemId()

Get the system identifier that was set with setSystemId.

**Specified by:**
- getSystemId

in interface

Source

**Returns:**
- The system identifier that was set with setSystemId, or null
if setSystemId was not called.

---

#### public void setSystemId​(
File
f)

Set the system ID from a File reference.

**Parameters:**
- f

- Must a non-null File reference.

---

#### public boolean isEmpty()

Indicates whether the

StreamSource

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

or contain no byte or
character.

Note that this method will reset the byte stream if it is provided, or
the character stream if the byte stream is not provided.

In case of error while checking the byte or character stream, the method
will return false to allow the XML processor to handle the error.

**Specified by:**
- isEmpty

in interface

Source

**Returns:**
- true if the

StreamSource

object is empty, false otherwise

---

### Additional Sections

#### Class StreamSource

java.lang.Object

- javax.xml.transform.stream.StreamSource

javax.xml.transform.stream.StreamSource

**All Implemented Interfaces:** Source

```java
public class
StreamSource

extends
Object

implements
Source
```

Acts as an holder for a transformation Source in the form
of a stream of XML markup.

Note:

Due to their internal use of either a

Reader

or

InputStream

instance,

StreamSource

instances may only be used once.

**Since:** 1.4

public class

StreamSource

extends

Object

implements

Source

Acts as an holder for a transformation Source in the form
of a stream of XML markup.

Note:

Due to their internal use of either a

Reader

or

InputStream

instance,

StreamSource

instances may only be used once.

Acts as an holder for a transformation Source in the form
of a stream of XML markup.

Note:

Due to their internal use of either a

Reader

or

InputStream

instance,

StreamSource

instances may only be used once.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

FEATURE

If

TransformerFactory.getFeature(java.lang.String)

returns true when passed this value as an argument,
the Transformer supports Source input of this type.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

StreamSource

()

Zero-argument default constructor.

StreamSource

​(

File

f)

Construct a StreamSource from a File.

StreamSource

​(

InputStream

inputStream)

Construct a StreamSource from a byte stream.

StreamSource

​(

InputStream

inputStream,

String

systemId)

Construct a StreamSource from a byte stream.

StreamSource

​(

Reader

reader)

Construct a StreamSource from a character reader.

StreamSource

​(

Reader

reader,

String

systemId)

Construct a StreamSource from a character reader.

StreamSource

​(

String

systemId)

Construct a StreamSource from a URL.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

InputStream

getInputStream

()

Get the byte stream that was set with setByteStream.

String

getPublicId

()

Get the public identifier that was set with setPublicId.

Reader

getReader

()

Get the character stream that was set with setReader.

String

getSystemId

()

Get the system identifier that was set with setSystemId.

boolean

isEmpty

()

Indicates whether the

StreamSource

object is empty.

void

setInputStream

​(

InputStream

inputStream)

Set the byte stream to be used as input.

void

setPublicId

​(

String

publicId)

Set the public identifier for this Source.

void

setReader

​(

Reader

reader)

Set the input to be a character reader.

void

setSystemId

​(

File

f)

Set the system ID from a File reference.

void

setSystemId

​(

String

systemId)

Set the system identifier for this Source.

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

Field Summary

Fields

Modifier and Type

Field

Description

static

String

FEATURE

If

TransformerFactory.getFeature(java.lang.String)

returns true when passed this value as an argument,
the Transformer supports Source input of this type.

---

#### Field Summary

If

TransformerFactory.getFeature(java.lang.String)

returns true when passed this value as an argument,
the Transformer supports Source input of this type.

Constructor Summary

Constructors

Constructor

Description

StreamSource

()

Zero-argument default constructor.

StreamSource

​(

File

f)

Construct a StreamSource from a File.

StreamSource

​(

InputStream

inputStream)

Construct a StreamSource from a byte stream.

StreamSource

​(

InputStream

inputStream,

String

systemId)

Construct a StreamSource from a byte stream.

StreamSource

​(

Reader

reader)

Construct a StreamSource from a character reader.

StreamSource

​(

Reader

reader,

String

systemId)

Construct a StreamSource from a character reader.

StreamSource

​(

String

systemId)

Construct a StreamSource from a URL.

---

#### Constructor Summary

Zero-argument default constructor.

Construct a StreamSource from a File.

Construct a StreamSource from a byte stream.

Construct a StreamSource from a character reader.

Construct a StreamSource from a URL.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

InputStream

getInputStream

()

Get the byte stream that was set with setByteStream.

String

getPublicId

()

Get the public identifier that was set with setPublicId.

Reader

getReader

()

Get the character stream that was set with setReader.

String

getSystemId

()

Get the system identifier that was set with setSystemId.

boolean

isEmpty

()

Indicates whether the

StreamSource

object is empty.

void

setInputStream

​(

InputStream

inputStream)

Set the byte stream to be used as input.

void

setPublicId

​(

String

publicId)

Set the public identifier for this Source.

void

setReader

​(

Reader

reader)

Set the input to be a character reader.

void

setSystemId

​(

File

f)

Set the system ID from a File reference.

void

setSystemId

​(

String

systemId)

Set the system identifier for this Source.

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

Get the byte stream that was set with setByteStream.

Get the public identifier that was set with setPublicId.

Get the character stream that was set with setReader.

Get the system identifier that was set with setSystemId.

Indicates whether the

StreamSource

object is empty.

Set the byte stream to be used as input.

Set the public identifier for this Source.

Set the input to be a character reader.

Set the system ID from a File reference.

Set the system identifier for this Source.

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

============ FIELD DETAIL ===========

- Field Detail

- FEATURE

```java
public static final
String
FEATURE
```

If

TransformerFactory.getFeature(java.lang.String)

returns true when passed this value as an argument,
the Transformer supports Source input of this type.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- StreamSource

```java
public StreamSource()
```

Zero-argument default constructor. If this constructor is used, and
no Stream source is set using

setInputStream(java.io.InputStream inputStream)

or

setReader(java.io.Reader reader)

, then the

Transformer

will
create an empty source

InputStream

using

new InputStream()

.

**See Also:** Transformer.transform(Source xmlSource, Result outputTarget)

- StreamSource

```java
public StreamSource​(
InputStream
inputStream)
```

Construct a StreamSource from a byte stream. Normally,
a stream should be used rather than a reader, so
the XML parser can resolve character encoding specified
by the XML declaration.

If this constructor is used to process a stylesheet, normally
setSystemId should also be called, so that relative URI references
can be resolved.

**Parameters:** inputStream

- A valid InputStream reference to an XML stream.

- StreamSource

```java
public StreamSource​(
InputStream
inputStream,

String
systemId)
```

Construct a StreamSource from a byte stream. Normally,
a stream should be used rather than a reader, so that
the XML parser can resolve character encoding specified
by the XML declaration.

This constructor allows the systemID to be set in addition
to the input stream, which allows relative URIs
to be processed.

**Parameters:** inputStream

- A valid InputStream reference to an XML stream.
**Parameters:** systemId

- Must be a String that conforms to the URI syntax.

- StreamSource

```java
public StreamSource​(
Reader
reader)
```

Construct a StreamSource from a character reader. Normally,
a stream should be used rather than a reader, so that
the XML parser can resolve character encoding specified
by the XML declaration. However, in many cases the encoding
of the input stream is already resolved, as in the case of
reading XML from a StringReader.

**Parameters:** reader

- A valid Reader reference to an XML character stream.

- StreamSource

```java
public StreamSource​(
Reader
reader,

String
systemId)
```

Construct a StreamSource from a character reader. Normally,
a stream should be used rather than a reader, so that
the XML parser may resolve character encoding specified
by the XML declaration. However, in many cases the encoding
of the input stream is already resolved, as in the case of
reading XML from a StringReader.

**Parameters:** reader

- A valid Reader reference to an XML character stream.
**Parameters:** systemId

- Must be a String that conforms to the URI syntax.

- StreamSource

```java
public StreamSource​(
String
systemId)
```

Construct a StreamSource from a URL.

**Parameters:** systemId

- Must be a String that conforms to the URI syntax.

- StreamSource

```java
public StreamSource​(
File
f)
```

Construct a StreamSource from a File.

**Parameters:** f

- Must a non-null File reference.

============ METHOD DETAIL ==========

- Method Detail

- setInputStream

```java
public void setInputStream​(
InputStream
inputStream)
```

Set the byte stream to be used as input. Normally,
a stream should be used rather than a reader, so that
the XML parser can resolve character encoding specified
by the XML declaration.

If this Source object is used to process a stylesheet, normally
setSystemId should also be called, so that relative URL references
can be resolved.

**Parameters:** inputStream

- A valid InputStream reference to an XML stream.

- getInputStream

```java
public
InputStream
getInputStream()
```

Get the byte stream that was set with setByteStream.

**Returns:** The byte stream that was set with setByteStream, or null
if setByteStream or the ByteStream constructor was not called.

- setReader

```java
public void setReader​(
Reader
reader)
```

Set the input to be a character reader. Normally,
a stream should be used rather than a reader, so that
the XML parser can resolve character encoding specified
by the XML declaration. However, in many cases the encoding
of the input stream is already resolved, as in the case of
reading XML from a StringReader.

**Parameters:** reader

- A valid Reader reference to an XML CharacterStream.

- getReader

```java
public
Reader
getReader()
```

Get the character stream that was set with setReader.

**Returns:** The character stream that was set with setReader, or null
if setReader or the Reader constructor was not called.

- setPublicId

```java
public void setPublicId​(
String
publicId)
```

Set the public identifier for this Source.

The public identifier is always optional: if the application
writer includes one, it will be provided as part of the
location information.

**Parameters:** publicId

- The public identifier as a string.

- getPublicId

```java
public
String
getPublicId()
```

Get the public identifier that was set with setPublicId.

**Returns:** The public identifier that was set with setPublicId, or null
if setPublicId was not called.

- setSystemId

```java
public void setSystemId​(
String
systemId)
```

Set the system identifier for this Source.

The system identifier is optional if there is a byte stream
or a character stream, but it is still useful to provide one,
since the application can use it to resolve relative URIs
and can include it in error messages and warnings (the parser
will attempt to open a connection to the URI only if
there is no byte stream or character stream specified).

**Specified by:** setSystemId

in interface

Source
**Parameters:** systemId

- The system identifier as a URL string.

- getSystemId

```java
public
String
getSystemId()
```

Get the system identifier that was set with setSystemId.

**Specified by:** getSystemId

in interface

Source
**Returns:** The system identifier that was set with setSystemId, or null
if setSystemId was not called.

- setSystemId

```java
public void setSystemId​(
File
f)
```

Set the system ID from a File reference.

**Parameters:** f

- Must a non-null File reference.

- isEmpty

```java
public boolean isEmpty()
```

Indicates whether the

StreamSource

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

or contain no byte or
character.

Note that this method will reset the byte stream if it is provided, or
the character stream if the byte stream is not provided.

In case of error while checking the byte or character stream, the method
will return false to allow the XML processor to handle the error.

**Specified by:** isEmpty

in interface

Source
**Returns:** true if the

StreamSource

object is empty, false otherwise

Field Detail

- FEATURE

```java
public static final
String
FEATURE
```

If

TransformerFactory.getFeature(java.lang.String)

returns true when passed this value as an argument,
the Transformer supports Source input of this type.

**See Also:** Constant Field Values

---

#### Field Detail

FEATURE

```java
public static final
String
FEATURE
```

If

TransformerFactory.getFeature(java.lang.String)

returns true when passed this value as an argument,
the Transformer supports Source input of this type.

**See Also:** Constant Field Values

---

#### FEATURE

public static final

String

FEATURE

If

TransformerFactory.getFeature(java.lang.String)

returns true when passed this value as an argument,
the Transformer supports Source input of this type.

Constructor Detail

- StreamSource

```java
public StreamSource()
```

Zero-argument default constructor. If this constructor is used, and
no Stream source is set using

setInputStream(java.io.InputStream inputStream)

or

setReader(java.io.Reader reader)

, then the

Transformer

will
create an empty source

InputStream

using

new InputStream()

.

**See Also:** Transformer.transform(Source xmlSource, Result outputTarget)

- StreamSource

```java
public StreamSource​(
InputStream
inputStream)
```

Construct a StreamSource from a byte stream. Normally,
a stream should be used rather than a reader, so
the XML parser can resolve character encoding specified
by the XML declaration.

If this constructor is used to process a stylesheet, normally
setSystemId should also be called, so that relative URI references
can be resolved.

**Parameters:** inputStream

- A valid InputStream reference to an XML stream.

- StreamSource

```java
public StreamSource​(
InputStream
inputStream,

String
systemId)
```

Construct a StreamSource from a byte stream. Normally,
a stream should be used rather than a reader, so that
the XML parser can resolve character encoding specified
by the XML declaration.

This constructor allows the systemID to be set in addition
to the input stream, which allows relative URIs
to be processed.

**Parameters:** inputStream

- A valid InputStream reference to an XML stream.
**Parameters:** systemId

- Must be a String that conforms to the URI syntax.

- StreamSource

```java
public StreamSource​(
Reader
reader)
```

Construct a StreamSource from a character reader. Normally,
a stream should be used rather than a reader, so that
the XML parser can resolve character encoding specified
by the XML declaration. However, in many cases the encoding
of the input stream is already resolved, as in the case of
reading XML from a StringReader.

**Parameters:** reader

- A valid Reader reference to an XML character stream.

- StreamSource

```java
public StreamSource​(
Reader
reader,

String
systemId)
```

Construct a StreamSource from a character reader. Normally,
a stream should be used rather than a reader, so that
the XML parser may resolve character encoding specified
by the XML declaration. However, in many cases the encoding
of the input stream is already resolved, as in the case of
reading XML from a StringReader.

**Parameters:** reader

- A valid Reader reference to an XML character stream.
**Parameters:** systemId

- Must be a String that conforms to the URI syntax.

- StreamSource

```java
public StreamSource​(
String
systemId)
```

Construct a StreamSource from a URL.

**Parameters:** systemId

- Must be a String that conforms to the URI syntax.

- StreamSource

```java
public StreamSource​(
File
f)
```

Construct a StreamSource from a File.

**Parameters:** f

- Must a non-null File reference.

---

#### Constructor Detail

StreamSource

```java
public StreamSource()
```

Zero-argument default constructor. If this constructor is used, and
no Stream source is set using

setInputStream(java.io.InputStream inputStream)

or

setReader(java.io.Reader reader)

, then the

Transformer

will
create an empty source

InputStream

using

new InputStream()

.

**See Also:** Transformer.transform(Source xmlSource, Result outputTarget)

---

#### StreamSource

public StreamSource()

Zero-argument default constructor. If this constructor is used, and
no Stream source is set using

setInputStream(java.io.InputStream inputStream)

or

setReader(java.io.Reader reader)

, then the

Transformer

will
create an empty source

InputStream

using

new InputStream()

.

StreamSource

```java
public StreamSource​(
InputStream
inputStream)
```

Construct a StreamSource from a byte stream. Normally,
a stream should be used rather than a reader, so
the XML parser can resolve character encoding specified
by the XML declaration.

If this constructor is used to process a stylesheet, normally
setSystemId should also be called, so that relative URI references
can be resolved.

**Parameters:** inputStream

- A valid InputStream reference to an XML stream.

---

#### StreamSource

public StreamSource​(

InputStream

inputStream)

Construct a StreamSource from a byte stream. Normally,
a stream should be used rather than a reader, so
the XML parser can resolve character encoding specified
by the XML declaration.

If this constructor is used to process a stylesheet, normally
setSystemId should also be called, so that relative URI references
can be resolved.

If this constructor is used to process a stylesheet, normally
setSystemId should also be called, so that relative URI references
can be resolved.

StreamSource

```java
public StreamSource​(
InputStream
inputStream,

String
systemId)
```

Construct a StreamSource from a byte stream. Normally,
a stream should be used rather than a reader, so that
the XML parser can resolve character encoding specified
by the XML declaration.

This constructor allows the systemID to be set in addition
to the input stream, which allows relative URIs
to be processed.

**Parameters:** inputStream

- A valid InputStream reference to an XML stream.
**Parameters:** systemId

- Must be a String that conforms to the URI syntax.

---

#### StreamSource

public StreamSource​(

InputStream

inputStream,

String

systemId)

Construct a StreamSource from a byte stream. Normally,
a stream should be used rather than a reader, so that
the XML parser can resolve character encoding specified
by the XML declaration.

This constructor allows the systemID to be set in addition
to the input stream, which allows relative URIs
to be processed.

This constructor allows the systemID to be set in addition
to the input stream, which allows relative URIs
to be processed.

StreamSource

```java
public StreamSource​(
Reader
reader)
```

Construct a StreamSource from a character reader. Normally,
a stream should be used rather than a reader, so that
the XML parser can resolve character encoding specified
by the XML declaration. However, in many cases the encoding
of the input stream is already resolved, as in the case of
reading XML from a StringReader.

**Parameters:** reader

- A valid Reader reference to an XML character stream.

---

#### StreamSource

public StreamSource​(

Reader

reader)

Construct a StreamSource from a character reader. Normally,
a stream should be used rather than a reader, so that
the XML parser can resolve character encoding specified
by the XML declaration. However, in many cases the encoding
of the input stream is already resolved, as in the case of
reading XML from a StringReader.

StreamSource

```java
public StreamSource​(
Reader
reader,

String
systemId)
```

Construct a StreamSource from a character reader. Normally,
a stream should be used rather than a reader, so that
the XML parser may resolve character encoding specified
by the XML declaration. However, in many cases the encoding
of the input stream is already resolved, as in the case of
reading XML from a StringReader.

**Parameters:** reader

- A valid Reader reference to an XML character stream.
**Parameters:** systemId

- Must be a String that conforms to the URI syntax.

---

#### StreamSource

public StreamSource​(

Reader

reader,

String

systemId)

Construct a StreamSource from a character reader. Normally,
a stream should be used rather than a reader, so that
the XML parser may resolve character encoding specified
by the XML declaration. However, in many cases the encoding
of the input stream is already resolved, as in the case of
reading XML from a StringReader.

StreamSource

```java
public StreamSource​(
String
systemId)
```

Construct a StreamSource from a URL.

**Parameters:** systemId

- Must be a String that conforms to the URI syntax.

---

#### StreamSource

public StreamSource​(

String

systemId)

Construct a StreamSource from a URL.

StreamSource

```java
public StreamSource​(
File
f)
```

Construct a StreamSource from a File.

**Parameters:** f

- Must a non-null File reference.

---

#### StreamSource

public StreamSource​(

File

f)

Construct a StreamSource from a File.

Method Detail

- setInputStream

```java
public void setInputStream​(
InputStream
inputStream)
```

Set the byte stream to be used as input. Normally,
a stream should be used rather than a reader, so that
the XML parser can resolve character encoding specified
by the XML declaration.

If this Source object is used to process a stylesheet, normally
setSystemId should also be called, so that relative URL references
can be resolved.

**Parameters:** inputStream

- A valid InputStream reference to an XML stream.

- getInputStream

```java
public
InputStream
getInputStream()
```

Get the byte stream that was set with setByteStream.

**Returns:** The byte stream that was set with setByteStream, or null
if setByteStream or the ByteStream constructor was not called.

- setReader

```java
public void setReader​(
Reader
reader)
```

Set the input to be a character reader. Normally,
a stream should be used rather than a reader, so that
the XML parser can resolve character encoding specified
by the XML declaration. However, in many cases the encoding
of the input stream is already resolved, as in the case of
reading XML from a StringReader.

**Parameters:** reader

- A valid Reader reference to an XML CharacterStream.

- getReader

```java
public
Reader
getReader()
```

Get the character stream that was set with setReader.

**Returns:** The character stream that was set with setReader, or null
if setReader or the Reader constructor was not called.

- setPublicId

```java
public void setPublicId​(
String
publicId)
```

Set the public identifier for this Source.

The public identifier is always optional: if the application
writer includes one, it will be provided as part of the
location information.

**Parameters:** publicId

- The public identifier as a string.

- getPublicId

```java
public
String
getPublicId()
```

Get the public identifier that was set with setPublicId.

**Returns:** The public identifier that was set with setPublicId, or null
if setPublicId was not called.

- setSystemId

```java
public void setSystemId​(
String
systemId)
```

Set the system identifier for this Source.

The system identifier is optional if there is a byte stream
or a character stream, but it is still useful to provide one,
since the application can use it to resolve relative URIs
and can include it in error messages and warnings (the parser
will attempt to open a connection to the URI only if
there is no byte stream or character stream specified).

**Specified by:** setSystemId

in interface

Source
**Parameters:** systemId

- The system identifier as a URL string.

- getSystemId

```java
public
String
getSystemId()
```

Get the system identifier that was set with setSystemId.

**Specified by:** getSystemId

in interface

Source
**Returns:** The system identifier that was set with setSystemId, or null
if setSystemId was not called.

- setSystemId

```java
public void setSystemId​(
File
f)
```

Set the system ID from a File reference.

**Parameters:** f

- Must a non-null File reference.

- isEmpty

```java
public boolean isEmpty()
```

Indicates whether the

StreamSource

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

or contain no byte or
character.

Note that this method will reset the byte stream if it is provided, or
the character stream if the byte stream is not provided.

In case of error while checking the byte or character stream, the method
will return false to allow the XML processor to handle the error.

**Specified by:** isEmpty

in interface

Source
**Returns:** true if the

StreamSource

object is empty, false otherwise

---

#### Method Detail

setInputStream

```java
public void setInputStream​(
InputStream
inputStream)
```

Set the byte stream to be used as input. Normally,
a stream should be used rather than a reader, so that
the XML parser can resolve character encoding specified
by the XML declaration.

If this Source object is used to process a stylesheet, normally
setSystemId should also be called, so that relative URL references
can be resolved.

**Parameters:** inputStream

- A valid InputStream reference to an XML stream.

---

#### setInputStream

public void setInputStream​(

InputStream

inputStream)

Set the byte stream to be used as input. Normally,
a stream should be used rather than a reader, so that
the XML parser can resolve character encoding specified
by the XML declaration.

If this Source object is used to process a stylesheet, normally
setSystemId should also be called, so that relative URL references
can be resolved.

If this Source object is used to process a stylesheet, normally
setSystemId should also be called, so that relative URL references
can be resolved.

getInputStream

```java
public
InputStream
getInputStream()
```

Get the byte stream that was set with setByteStream.

**Returns:** The byte stream that was set with setByteStream, or null
if setByteStream or the ByteStream constructor was not called.

---

#### getInputStream

public

InputStream

getInputStream()

Get the byte stream that was set with setByteStream.

setReader

```java
public void setReader​(
Reader
reader)
```

Set the input to be a character reader. Normally,
a stream should be used rather than a reader, so that
the XML parser can resolve character encoding specified
by the XML declaration. However, in many cases the encoding
of the input stream is already resolved, as in the case of
reading XML from a StringReader.

**Parameters:** reader

- A valid Reader reference to an XML CharacterStream.

---

#### setReader

public void setReader​(

Reader

reader)

Set the input to be a character reader. Normally,
a stream should be used rather than a reader, so that
the XML parser can resolve character encoding specified
by the XML declaration. However, in many cases the encoding
of the input stream is already resolved, as in the case of
reading XML from a StringReader.

getReader

```java
public
Reader
getReader()
```

Get the character stream that was set with setReader.

**Returns:** The character stream that was set with setReader, or null
if setReader or the Reader constructor was not called.

---

#### getReader

public

Reader

getReader()

Get the character stream that was set with setReader.

setPublicId

```java
public void setPublicId​(
String
publicId)
```

Set the public identifier for this Source.

The public identifier is always optional: if the application
writer includes one, it will be provided as part of the
location information.

**Parameters:** publicId

- The public identifier as a string.

---

#### setPublicId

public void setPublicId​(

String

publicId)

Set the public identifier for this Source.

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

Get the public identifier that was set with setPublicId.

**Returns:** The public identifier that was set with setPublicId, or null
if setPublicId was not called.

---

#### getPublicId

public

String

getPublicId()

Get the public identifier that was set with setPublicId.

setSystemId

```java
public void setSystemId​(
String
systemId)
```

Set the system identifier for this Source.

The system identifier is optional if there is a byte stream
or a character stream, but it is still useful to provide one,
since the application can use it to resolve relative URIs
and can include it in error messages and warnings (the parser
will attempt to open a connection to the URI only if
there is no byte stream or character stream specified).

**Specified by:** setSystemId

in interface

Source
**Parameters:** systemId

- The system identifier as a URL string.

---

#### setSystemId

public void setSystemId​(

String

systemId)

Set the system identifier for this Source.

The system identifier is optional if there is a byte stream
or a character stream, but it is still useful to provide one,
since the application can use it to resolve relative URIs
and can include it in error messages and warnings (the parser
will attempt to open a connection to the URI only if
there is no byte stream or character stream specified).

The system identifier is optional if there is a byte stream
or a character stream, but it is still useful to provide one,
since the application can use it to resolve relative URIs
and can include it in error messages and warnings (the parser
will attempt to open a connection to the URI only if
there is no byte stream or character stream specified).

getSystemId

```java
public
String
getSystemId()
```

Get the system identifier that was set with setSystemId.

**Specified by:** getSystemId

in interface

Source
**Returns:** The system identifier that was set with setSystemId, or null
if setSystemId was not called.

---

#### getSystemId

public

String

getSystemId()

Get the system identifier that was set with setSystemId.

setSystemId

```java
public void setSystemId​(
File
f)
```

Set the system ID from a File reference.

**Parameters:** f

- Must a non-null File reference.

---

#### setSystemId

public void setSystemId​(

File

f)

Set the system ID from a File reference.

isEmpty

```java
public boolean isEmpty()
```

Indicates whether the

StreamSource

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

or contain no byte or
character.

Note that this method will reset the byte stream if it is provided, or
the character stream if the byte stream is not provided.

In case of error while checking the byte or character stream, the method
will return false to allow the XML processor to handle the error.

**Specified by:** isEmpty

in interface

Source
**Returns:** true if the

StreamSource

object is empty, false otherwise

---

#### isEmpty

public boolean isEmpty()

Indicates whether the

StreamSource

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

or contain no byte or
character.

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

or contain no byte or
character.

Note that this method will reset the byte stream if it is provided, or
the character stream if the byte stream is not provided.

Note that this method will reset the byte stream if it is provided, or
the character stream if the byte stream is not provided.

In case of error while checking the byte or character stream, the method
will return false to allow the XML processor to handle the error.

---

