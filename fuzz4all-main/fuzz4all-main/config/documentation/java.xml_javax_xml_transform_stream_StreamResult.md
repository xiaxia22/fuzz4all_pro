# Class StreamResult

**Source:** `java.xml\javax\xml\transform\stream\StreamResult.html`

### Class Description

```java
public class
StreamResult

extends
Object

implements
Result
```

Acts as an holder for a transformation result,
which may be XML, plain Text, HTML, or some other form of markup.

**All Implemented Interfaces:** Result

---

### Field Details

#### public static final
String
FEATURE

If

TransformerFactory.getFeature(java.lang.String)

returns true when passed this value as an argument,
the Transformer supports Result output of this type.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public StreamResult()

Zero-argument default constructor.

---

#### public StreamResult​(
OutputStream
outputStream)

Construct a StreamResult from a byte stream. Normally,
a stream should be used rather than a reader, so that
the transformer may use instructions contained in the
transformation instructions to control the encoding.

**Parameters:**
- outputStream

- A valid OutputStream reference.

---

#### public StreamResult​(
Writer
writer)

Construct a StreamResult from a character stream. Normally,
a stream should be used rather than a reader, so that
the transformer may use instructions contained in the
transformation instructions to control the encoding. However,
there are times when it is useful to write to a character
stream, such as when using a StringWriter.

**Parameters:**
- writer

- A valid Writer reference.

---

#### public StreamResult​(
String
systemId)

Construct a StreamResult from a URL.

**Parameters:**
- systemId

- Must be a String that conforms to the URI syntax.

---

#### public StreamResult​(
File
f)

Construct a StreamResult from a File.

**Parameters:**
- f

- Must a non-null File reference.

---

### Method Details

#### public void setOutputStream​(
OutputStream
outputStream)

Set the ByteStream that is to be written to. Normally,
a stream should be used rather than a reader, so that
the transformer may use instructions contained in the
transformation instructions to control the encoding.

**Parameters:**
- outputStream

- A valid OutputStream reference.

---

#### public
OutputStream
getOutputStream()

Get the byte stream that was set with setOutputStream.

**Returns:**
- The byte stream that was set with setOutputStream, or null
if setOutputStream or the ByteStream constructor was not called.

---

#### public void setWriter​(
Writer
writer)

Set the writer that is to receive the result. Normally,
a stream should be used rather than a writer, so that
the transformer may use instructions contained in the
transformation instructions to control the encoding. However,
there are times when it is useful to write to a writer,
such as when using a StringWriter.

**Parameters:**
- writer

- A valid Writer reference.

---

#### public
Writer
getWriter()

Get the character stream that was set with setWriter.

**Returns:**
- The character stream that was set with setWriter, or null
if setWriter or the Writer constructor was not called.

---

#### public void setSystemId​(
String
systemId)

Set the systemID that may be used in association
with the byte or character stream, or, if neither is set, use
this value as a writeable URI (probably a file name).

**Specified by:**
- setSystemId

in interface

Result

**Parameters:**
- systemId

- The system identifier as a URI string.

---

#### public void setSystemId​(
File
f)

Set the system ID from a

File

reference.

**Parameters:**
- f

- Must a non-null File reference.

---

#### public
String
getSystemId()

Get the system identifier that was set with setSystemId.

**Specified by:**
- getSystemId

in interface

Result

**Returns:**
- The system identifier that was set with setSystemId, or null
if setSystemId was not called.

---

### Additional Sections

#### Class StreamResult

java.lang.Object

- javax.xml.transform.stream.StreamResult

javax.xml.transform.stream.StreamResult

**All Implemented Interfaces:** Result

```java
public class
StreamResult

extends
Object

implements
Result
```

Acts as an holder for a transformation result,
which may be XML, plain Text, HTML, or some other form of markup.

**Since:** 1.4

public class

StreamResult

extends

Object

implements

Result

Acts as an holder for a transformation result,
which may be XML, plain Text, HTML, or some other form of markup.

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
the Transformer supports Result output of this type.

- Fields declared in interface javax.xml.transform.

Result

PI_DISABLE_OUTPUT_ESCAPING

,

PI_ENABLE_OUTPUT_ESCAPING

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

StreamResult

()

Zero-argument default constructor.

StreamResult

​(

File

f)

Construct a StreamResult from a File.

StreamResult

​(

OutputStream

outputStream)

Construct a StreamResult from a byte stream.

StreamResult

​(

Writer

writer)

Construct a StreamResult from a character stream.

StreamResult

​(

String

systemId)

Construct a StreamResult from a URL.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

OutputStream

getOutputStream

()

Get the byte stream that was set with setOutputStream.

String

getSystemId

()

Get the system identifier that was set with setSystemId.

Writer

getWriter

()

Get the character stream that was set with setWriter.

void

setOutputStream

​(

OutputStream

outputStream)

Set the ByteStream that is to be written to.

void

setSystemId

​(

File

f)

Set the system ID from a

File

reference.

void

setSystemId

​(

String

systemId)

Set the systemID that may be used in association
with the byte or character stream, or, if neither is set, use
this value as a writeable URI (probably a file name).

void

setWriter

​(

Writer

writer)

Set the writer that is to receive the result.

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
the Transformer supports Result output of this type.

- Fields declared in interface javax.xml.transform.

Result

PI_DISABLE_OUTPUT_ESCAPING

,

PI_ENABLE_OUTPUT_ESCAPING

---

#### Field Summary

If

TransformerFactory.getFeature(java.lang.String)

returns true when passed this value as an argument,
the Transformer supports Result output of this type.

Fields declared in interface javax.xml.transform.

Result

PI_DISABLE_OUTPUT_ESCAPING

,

PI_ENABLE_OUTPUT_ESCAPING

---

#### Fields declared in interface javax.xml.transform. Result

Constructor Summary

Constructors

Constructor

Description

StreamResult

()

Zero-argument default constructor.

StreamResult

​(

File

f)

Construct a StreamResult from a File.

StreamResult

​(

OutputStream

outputStream)

Construct a StreamResult from a byte stream.

StreamResult

​(

Writer

writer)

Construct a StreamResult from a character stream.

StreamResult

​(

String

systemId)

Construct a StreamResult from a URL.

---

#### Constructor Summary

Zero-argument default constructor.

Construct a StreamResult from a File.

Construct a StreamResult from a byte stream.

Construct a StreamResult from a character stream.

Construct a StreamResult from a URL.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

OutputStream

getOutputStream

()

Get the byte stream that was set with setOutputStream.

String

getSystemId

()

Get the system identifier that was set with setSystemId.

Writer

getWriter

()

Get the character stream that was set with setWriter.

void

setOutputStream

​(

OutputStream

outputStream)

Set the ByteStream that is to be written to.

void

setSystemId

​(

File

f)

Set the system ID from a

File

reference.

void

setSystemId

​(

String

systemId)

Set the systemID that may be used in association
with the byte or character stream, or, if neither is set, use
this value as a writeable URI (probably a file name).

void

setWriter

​(

Writer

writer)

Set the writer that is to receive the result.

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

Get the byte stream that was set with setOutputStream.

Get the system identifier that was set with setSystemId.

Get the character stream that was set with setWriter.

Set the ByteStream that is to be written to.

Set the system ID from a

File

reference.

Set the systemID that may be used in association
with the byte or character stream, or, if neither is set, use
this value as a writeable URI (probably a file name).

Set the writer that is to receive the result.

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
the Transformer supports Result output of this type.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- StreamResult

```java
public StreamResult()
```

Zero-argument default constructor.

- StreamResult

```java
public StreamResult​(
OutputStream
outputStream)
```

Construct a StreamResult from a byte stream. Normally,
a stream should be used rather than a reader, so that
the transformer may use instructions contained in the
transformation instructions to control the encoding.

**Parameters:** outputStream

- A valid OutputStream reference.

- StreamResult

```java
public StreamResult​(
Writer
writer)
```

Construct a StreamResult from a character stream. Normally,
a stream should be used rather than a reader, so that
the transformer may use instructions contained in the
transformation instructions to control the encoding. However,
there are times when it is useful to write to a character
stream, such as when using a StringWriter.

**Parameters:** writer

- A valid Writer reference.

- StreamResult

```java
public StreamResult​(
String
systemId)
```

Construct a StreamResult from a URL.

**Parameters:** systemId

- Must be a String that conforms to the URI syntax.

- StreamResult

```java
public StreamResult​(
File
f)
```

Construct a StreamResult from a File.

**Parameters:** f

- Must a non-null File reference.

============ METHOD DETAIL ==========

- Method Detail

- setOutputStream

```java
public void setOutputStream​(
OutputStream
outputStream)
```

Set the ByteStream that is to be written to. Normally,
a stream should be used rather than a reader, so that
the transformer may use instructions contained in the
transformation instructions to control the encoding.

**Parameters:** outputStream

- A valid OutputStream reference.

- getOutputStream

```java
public
OutputStream
getOutputStream()
```

Get the byte stream that was set with setOutputStream.

**Returns:** The byte stream that was set with setOutputStream, or null
if setOutputStream or the ByteStream constructor was not called.

- setWriter

```java
public void setWriter​(
Writer
writer)
```

Set the writer that is to receive the result. Normally,
a stream should be used rather than a writer, so that
the transformer may use instructions contained in the
transformation instructions to control the encoding. However,
there are times when it is useful to write to a writer,
such as when using a StringWriter.

**Parameters:** writer

- A valid Writer reference.

- getWriter

```java
public
Writer
getWriter()
```

Get the character stream that was set with setWriter.

**Returns:** The character stream that was set with setWriter, or null
if setWriter or the Writer constructor was not called.

- setSystemId

```java
public void setSystemId​(
String
systemId)
```

Set the systemID that may be used in association
with the byte or character stream, or, if neither is set, use
this value as a writeable URI (probably a file name).

**Specified by:** setSystemId

in interface

Result
**Parameters:** systemId

- The system identifier as a URI string.

- setSystemId

```java
public void setSystemId​(
File
f)
```

Set the system ID from a

File

reference.

**Parameters:** f

- Must a non-null File reference.

- getSystemId

```java
public
String
getSystemId()
```

Get the system identifier that was set with setSystemId.

**Specified by:** getSystemId

in interface

Result
**Returns:** The system identifier that was set with setSystemId, or null
if setSystemId was not called.

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
the Transformer supports Result output of this type.

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
the Transformer supports Result output of this type.

**See Also:** Constant Field Values

---

#### FEATURE

public static final

String

FEATURE

If

TransformerFactory.getFeature(java.lang.String)

returns true when passed this value as an argument,
the Transformer supports Result output of this type.

Constructor Detail

- StreamResult

```java
public StreamResult()
```

Zero-argument default constructor.

- StreamResult

```java
public StreamResult​(
OutputStream
outputStream)
```

Construct a StreamResult from a byte stream. Normally,
a stream should be used rather than a reader, so that
the transformer may use instructions contained in the
transformation instructions to control the encoding.

**Parameters:** outputStream

- A valid OutputStream reference.

- StreamResult

```java
public StreamResult​(
Writer
writer)
```

Construct a StreamResult from a character stream. Normally,
a stream should be used rather than a reader, so that
the transformer may use instructions contained in the
transformation instructions to control the encoding. However,
there are times when it is useful to write to a character
stream, such as when using a StringWriter.

**Parameters:** writer

- A valid Writer reference.

- StreamResult

```java
public StreamResult​(
String
systemId)
```

Construct a StreamResult from a URL.

**Parameters:** systemId

- Must be a String that conforms to the URI syntax.

- StreamResult

```java
public StreamResult​(
File
f)
```

Construct a StreamResult from a File.

**Parameters:** f

- Must a non-null File reference.

---

#### Constructor Detail

StreamResult

```java
public StreamResult()
```

Zero-argument default constructor.

---

#### StreamResult

public StreamResult()

Zero-argument default constructor.

StreamResult

```java
public StreamResult​(
OutputStream
outputStream)
```

Construct a StreamResult from a byte stream. Normally,
a stream should be used rather than a reader, so that
the transformer may use instructions contained in the
transformation instructions to control the encoding.

**Parameters:** outputStream

- A valid OutputStream reference.

---

#### StreamResult

public StreamResult​(

OutputStream

outputStream)

Construct a StreamResult from a byte stream. Normally,
a stream should be used rather than a reader, so that
the transformer may use instructions contained in the
transformation instructions to control the encoding.

StreamResult

```java
public StreamResult​(
Writer
writer)
```

Construct a StreamResult from a character stream. Normally,
a stream should be used rather than a reader, so that
the transformer may use instructions contained in the
transformation instructions to control the encoding. However,
there are times when it is useful to write to a character
stream, such as when using a StringWriter.

**Parameters:** writer

- A valid Writer reference.

---

#### StreamResult

public StreamResult​(

Writer

writer)

Construct a StreamResult from a character stream. Normally,
a stream should be used rather than a reader, so that
the transformer may use instructions contained in the
transformation instructions to control the encoding. However,
there are times when it is useful to write to a character
stream, such as when using a StringWriter.

StreamResult

```java
public StreamResult​(
String
systemId)
```

Construct a StreamResult from a URL.

**Parameters:** systemId

- Must be a String that conforms to the URI syntax.

---

#### StreamResult

public StreamResult​(

String

systemId)

Construct a StreamResult from a URL.

StreamResult

```java
public StreamResult​(
File
f)
```

Construct a StreamResult from a File.

**Parameters:** f

- Must a non-null File reference.

---

#### StreamResult

public StreamResult​(

File

f)

Construct a StreamResult from a File.

Method Detail

- setOutputStream

```java
public void setOutputStream​(
OutputStream
outputStream)
```

Set the ByteStream that is to be written to. Normally,
a stream should be used rather than a reader, so that
the transformer may use instructions contained in the
transformation instructions to control the encoding.

**Parameters:** outputStream

- A valid OutputStream reference.

- getOutputStream

```java
public
OutputStream
getOutputStream()
```

Get the byte stream that was set with setOutputStream.

**Returns:** The byte stream that was set with setOutputStream, or null
if setOutputStream or the ByteStream constructor was not called.

- setWriter

```java
public void setWriter​(
Writer
writer)
```

Set the writer that is to receive the result. Normally,
a stream should be used rather than a writer, so that
the transformer may use instructions contained in the
transformation instructions to control the encoding. However,
there are times when it is useful to write to a writer,
such as when using a StringWriter.

**Parameters:** writer

- A valid Writer reference.

- getWriter

```java
public
Writer
getWriter()
```

Get the character stream that was set with setWriter.

**Returns:** The character stream that was set with setWriter, or null
if setWriter or the Writer constructor was not called.

- setSystemId

```java
public void setSystemId​(
String
systemId)
```

Set the systemID that may be used in association
with the byte or character stream, or, if neither is set, use
this value as a writeable URI (probably a file name).

**Specified by:** setSystemId

in interface

Result
**Parameters:** systemId

- The system identifier as a URI string.

- setSystemId

```java
public void setSystemId​(
File
f)
```

Set the system ID from a

File

reference.

**Parameters:** f

- Must a non-null File reference.

- getSystemId

```java
public
String
getSystemId()
```

Get the system identifier that was set with setSystemId.

**Specified by:** getSystemId

in interface

Result
**Returns:** The system identifier that was set with setSystemId, or null
if setSystemId was not called.

---

#### Method Detail

setOutputStream

```java
public void setOutputStream​(
OutputStream
outputStream)
```

Set the ByteStream that is to be written to. Normally,
a stream should be used rather than a reader, so that
the transformer may use instructions contained in the
transformation instructions to control the encoding.

**Parameters:** outputStream

- A valid OutputStream reference.

---

#### setOutputStream

public void setOutputStream​(

OutputStream

outputStream)

Set the ByteStream that is to be written to. Normally,
a stream should be used rather than a reader, so that
the transformer may use instructions contained in the
transformation instructions to control the encoding.

getOutputStream

```java
public
OutputStream
getOutputStream()
```

Get the byte stream that was set with setOutputStream.

**Returns:** The byte stream that was set with setOutputStream, or null
if setOutputStream or the ByteStream constructor was not called.

---

#### getOutputStream

public

OutputStream

getOutputStream()

Get the byte stream that was set with setOutputStream.

setWriter

```java
public void setWriter​(
Writer
writer)
```

Set the writer that is to receive the result. Normally,
a stream should be used rather than a writer, so that
the transformer may use instructions contained in the
transformation instructions to control the encoding. However,
there are times when it is useful to write to a writer,
such as when using a StringWriter.

**Parameters:** writer

- A valid Writer reference.

---

#### setWriter

public void setWriter​(

Writer

writer)

Set the writer that is to receive the result. Normally,
a stream should be used rather than a writer, so that
the transformer may use instructions contained in the
transformation instructions to control the encoding. However,
there are times when it is useful to write to a writer,
such as when using a StringWriter.

getWriter

```java
public
Writer
getWriter()
```

Get the character stream that was set with setWriter.

**Returns:** The character stream that was set with setWriter, or null
if setWriter or the Writer constructor was not called.

---

#### getWriter

public

Writer

getWriter()

Get the character stream that was set with setWriter.

setSystemId

```java
public void setSystemId​(
String
systemId)
```

Set the systemID that may be used in association
with the byte or character stream, or, if neither is set, use
this value as a writeable URI (probably a file name).

**Specified by:** setSystemId

in interface

Result
**Parameters:** systemId

- The system identifier as a URI string.

---

#### setSystemId

public void setSystemId​(

String

systemId)

Set the systemID that may be used in association
with the byte or character stream, or, if neither is set, use
this value as a writeable URI (probably a file name).

setSystemId

```java
public void setSystemId​(
File
f)
```

Set the system ID from a

File

reference.

**Parameters:** f

- Must a non-null File reference.

---

#### setSystemId

public void setSystemId​(

File

f)

Set the system ID from a

File

reference.

getSystemId

```java
public
String
getSystemId()
```

Get the system identifier that was set with setSystemId.

**Specified by:** getSystemId

in interface

Result
**Returns:** The system identifier that was set with setSystemId, or null
if setSystemId was not called.

---

#### getSystemId

public

String

getSystemId()

Get the system identifier that was set with setSystemId.

---

