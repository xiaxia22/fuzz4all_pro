# Class StreamPrintService

**Source:** `java.desktop\javax\print\StreamPrintService.html`

### Class Description

```java
public abstract class
StreamPrintService

extends
Object

implements
PrintService
```

This class extends

PrintService

and represents a print service that
prints data in different formats to a client-provided output stream. This is
principally intended for services where the output format is a document type
suitable for viewing or archiving. The output format must be declared as a
mime type. This is equivalent to an output document flavor where the
representation class is always "java.io.OutputStream" An instance of the

StreamPrintService

class is obtained from a

StreamPrintServiceFactory

instance.

Note that a

StreamPrintService

is different from a

PrintService

, which supports a

Destination

attribute. A

StreamPrintService

always requires an output stream, whereas a

PrintService

optionally accepts a

Destination

. A

StreamPrintService

has no default destination for its formatted
output. Additionally a

StreamPrintService

is expected to generate
output in a format useful in other contexts.

StreamPrintService

's are
not expected to support the

Destination

attribute.

**All Implemented Interfaces:** PrintService

---

### Field Details

*No entries found.*

### Constructor Details

#### protected StreamPrintService​(
OutputStream
out)

Constructs a

StreamPrintService

object.

**Parameters:**
- out

- stream to which to send formatted print data

---

### Method Details

#### public
OutputStream
getOutputStream()

Gets the output stream.

**Returns:**
- the stream to which this service will send formatted print data

---

#### public abstract
String
getOutputFormat()

Returns the document format emitted by this print service. Must be in
mimetype format, compatible with the mime type components of

DocFlavors

**Returns:**
- mime type identifying the output format

**See Also:**
- DocFlavor

---

#### public void dispose()

Disposes this

StreamPrintService

. If a stream service cannot be
re-used, it must be disposed to indicate this. Typically the client will
call this method. Services which write data which cannot meaningfully be
appended to may also dispose the stream. This does not close the stream.
It just marks it as not for further use by this service.

---

#### public boolean isDisposed()

Returns a

boolean

indicating whether or not this

StreamPrintService

has been disposed. If this object has been
disposed, will return

true

. Used by services and client
applications to recognize streams to which no further data should be
written.

**Returns:**
- true

if this

StreamPrintService

has been
disposed;

false

otherwise

---

### Additional Sections

#### Class StreamPrintService

java.lang.Object

- javax.print.StreamPrintService

javax.print.StreamPrintService

**All Implemented Interfaces:** PrintService

```java
public abstract class
StreamPrintService

extends
Object

implements
PrintService
```

This class extends

PrintService

and represents a print service that
prints data in different formats to a client-provided output stream. This is
principally intended for services where the output format is a document type
suitable for viewing or archiving. The output format must be declared as a
mime type. This is equivalent to an output document flavor where the
representation class is always "java.io.OutputStream" An instance of the

StreamPrintService

class is obtained from a

StreamPrintServiceFactory

instance.

Note that a

StreamPrintService

is different from a

PrintService

, which supports a

Destination

attribute. A

StreamPrintService

always requires an output stream, whereas a

PrintService

optionally accepts a

Destination

. A

StreamPrintService

has no default destination for its formatted
output. Additionally a

StreamPrintService

is expected to generate
output in a format useful in other contexts.

StreamPrintService

's are
not expected to support the

Destination

attribute.

public abstract class

StreamPrintService

extends

Object

implements

PrintService

This class extends

PrintService

and represents a print service that
prints data in different formats to a client-provided output stream. This is
principally intended for services where the output format is a document type
suitable for viewing or archiving. The output format must be declared as a
mime type. This is equivalent to an output document flavor where the
representation class is always "java.io.OutputStream" An instance of the

StreamPrintService

class is obtained from a

StreamPrintServiceFactory

instance.

Note that a

StreamPrintService

is different from a

PrintService

, which supports a

Destination

attribute. A

StreamPrintService

always requires an output stream, whereas a

PrintService

optionally accepts a

Destination

. A

StreamPrintService

has no default destination for its formatted
output. Additionally a

StreamPrintService

is expected to generate
output in a format useful in other contexts.

StreamPrintService

's are
not expected to support the

Destination

attribute.

Note that a

StreamPrintService

is different from a

PrintService

, which supports a

Destination

attribute. A

StreamPrintService

always requires an output stream, whereas a

PrintService

optionally accepts a

Destination

. A

StreamPrintService

has no default destination for its formatted
output. Additionally a

StreamPrintService

is expected to generate
output in a format useful in other contexts.

StreamPrintService

's are
not expected to support the

Destination

attribute.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

StreamPrintService

​(

OutputStream

out)

Constructs a

StreamPrintService

object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

void

dispose

()

Disposes this

StreamPrintService

.

abstract

String

getOutputFormat

()

Returns the document format emitted by this print service.

OutputStream

getOutputStream

()

Gets the output stream.

boolean

isDisposed

()

Returns a

boolean

indicating whether or not this

StreamPrintService

has been disposed.

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

- Methods declared in interface javax.print.

PrintService

addPrintServiceAttributeListener

,

createPrintJob

,

equals

,

getAttribute

,

getAttributes

,

getDefaultAttributeValue

,

getName

,

getServiceUIFactory

,

getSupportedAttributeCategories

,

getSupportedAttributeValues

,

getSupportedDocFlavors

,

getUnsupportedAttributes

,

hashCode

,

isAttributeCategorySupported

,

isAttributeValueSupported

,

isDocFlavorSupported

,

removePrintServiceAttributeListener

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

StreamPrintService

​(

OutputStream

out)

Constructs a

StreamPrintService

object.

---

#### Constructor Summary

Constructs a

StreamPrintService

object.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

void

dispose

()

Disposes this

StreamPrintService

.

abstract

String

getOutputFormat

()

Returns the document format emitted by this print service.

OutputStream

getOutputStream

()

Gets the output stream.

boolean

isDisposed

()

Returns a

boolean

indicating whether or not this

StreamPrintService

has been disposed.

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

- Methods declared in interface javax.print.

PrintService

addPrintServiceAttributeListener

,

createPrintJob

,

equals

,

getAttribute

,

getAttributes

,

getDefaultAttributeValue

,

getName

,

getServiceUIFactory

,

getSupportedAttributeCategories

,

getSupportedAttributeValues

,

getSupportedDocFlavors

,

getUnsupportedAttributes

,

hashCode

,

isAttributeCategorySupported

,

isAttributeValueSupported

,

isDocFlavorSupported

,

removePrintServiceAttributeListener

---

#### Method Summary

Disposes this

StreamPrintService

.

Returns the document format emitted by this print service.

Gets the output stream.

Returns a

boolean

indicating whether or not this

StreamPrintService

has been disposed.

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

Methods declared in interface javax.print.

PrintService

addPrintServiceAttributeListener

,

createPrintJob

,

equals

,

getAttribute

,

getAttributes

,

getDefaultAttributeValue

,

getName

,

getServiceUIFactory

,

getSupportedAttributeCategories

,

getSupportedAttributeValues

,

getSupportedDocFlavors

,

getUnsupportedAttributes

,

hashCode

,

isAttributeCategorySupported

,

isAttributeValueSupported

,

isDocFlavorSupported

,

removePrintServiceAttributeListener

---

#### Methods declared in interface javax.print. PrintService

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- StreamPrintService

```java
protected StreamPrintService​(
OutputStream
out)
```

Constructs a

StreamPrintService

object.

**Parameters:** out

- stream to which to send formatted print data

============ METHOD DETAIL ==========

- Method Detail

- getOutputStream

```java
public
OutputStream
getOutputStream()
```

Gets the output stream.

**Returns:** the stream to which this service will send formatted print data

- getOutputFormat

```java
public abstract
String
getOutputFormat()
```

Returns the document format emitted by this print service. Must be in
mimetype format, compatible with the mime type components of

DocFlavors

**Returns:** mime type identifying the output format
**See Also:** DocFlavor

- dispose

```java
public void dispose()
```

Disposes this

StreamPrintService

. If a stream service cannot be
re-used, it must be disposed to indicate this. Typically the client will
call this method. Services which write data which cannot meaningfully be
appended to may also dispose the stream. This does not close the stream.
It just marks it as not for further use by this service.

- isDisposed

```java
public boolean isDisposed()
```

Returns a

boolean

indicating whether or not this

StreamPrintService

has been disposed. If this object has been
disposed, will return

true

. Used by services and client
applications to recognize streams to which no further data should be
written.

**Returns:** true

if this

StreamPrintService

has been
disposed;

false

otherwise

Constructor Detail

- StreamPrintService

```java
protected StreamPrintService​(
OutputStream
out)
```

Constructs a

StreamPrintService

object.

**Parameters:** out

- stream to which to send formatted print data

---

#### Constructor Detail

StreamPrintService

```java
protected StreamPrintService​(
OutputStream
out)
```

Constructs a

StreamPrintService

object.

**Parameters:** out

- stream to which to send formatted print data

---

#### StreamPrintService

protected StreamPrintService​(

OutputStream

out)

Constructs a

StreamPrintService

object.

Method Detail

- getOutputStream

```java
public
OutputStream
getOutputStream()
```

Gets the output stream.

**Returns:** the stream to which this service will send formatted print data

- getOutputFormat

```java
public abstract
String
getOutputFormat()
```

Returns the document format emitted by this print service. Must be in
mimetype format, compatible with the mime type components of

DocFlavors

**Returns:** mime type identifying the output format
**See Also:** DocFlavor

- dispose

```java
public void dispose()
```

Disposes this

StreamPrintService

. If a stream service cannot be
re-used, it must be disposed to indicate this. Typically the client will
call this method. Services which write data which cannot meaningfully be
appended to may also dispose the stream. This does not close the stream.
It just marks it as not for further use by this service.

- isDisposed

```java
public boolean isDisposed()
```

Returns a

boolean

indicating whether or not this

StreamPrintService

has been disposed. If this object has been
disposed, will return

true

. Used by services and client
applications to recognize streams to which no further data should be
written.

**Returns:** true

if this

StreamPrintService

has been
disposed;

false

otherwise

---

#### Method Detail

getOutputStream

```java
public
OutputStream
getOutputStream()
```

Gets the output stream.

**Returns:** the stream to which this service will send formatted print data

---

#### getOutputStream

public

OutputStream

getOutputStream()

Gets the output stream.

getOutputFormat

```java
public abstract
String
getOutputFormat()
```

Returns the document format emitted by this print service. Must be in
mimetype format, compatible with the mime type components of

DocFlavors

**Returns:** mime type identifying the output format
**See Also:** DocFlavor

---

#### getOutputFormat

public abstract

String

getOutputFormat()

Returns the document format emitted by this print service. Must be in
mimetype format, compatible with the mime type components of

DocFlavors

dispose

```java
public void dispose()
```

Disposes this

StreamPrintService

. If a stream service cannot be
re-used, it must be disposed to indicate this. Typically the client will
call this method. Services which write data which cannot meaningfully be
appended to may also dispose the stream. This does not close the stream.
It just marks it as not for further use by this service.

---

#### dispose

public void dispose()

Disposes this

StreamPrintService

. If a stream service cannot be
re-used, it must be disposed to indicate this. Typically the client will
call this method. Services which write data which cannot meaningfully be
appended to may also dispose the stream. This does not close the stream.
It just marks it as not for further use by this service.

isDisposed

```java
public boolean isDisposed()
```

Returns a

boolean

indicating whether or not this

StreamPrintService

has been disposed. If this object has been
disposed, will return

true

. Used by services and client
applications to recognize streams to which no further data should be
written.

**Returns:** true

if this

StreamPrintService

has been
disposed;

false

otherwise

---

#### isDisposed

public boolean isDisposed()

Returns a

boolean

indicating whether or not this

StreamPrintService

has been disposed. If this object has been
disposed, will return

true

. Used by services and client
applications to recognize streams to which no further data should be
written.

---

