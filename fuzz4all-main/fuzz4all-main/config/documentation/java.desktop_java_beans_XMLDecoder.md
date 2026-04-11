# Class XMLDecoder

**Source:** `java.desktop\java\beans\XMLDecoder.html`

### Class Description

```java
public class
XMLDecoder

extends
Object

implements
AutoCloseable
```

The

XMLDecoder

class is used to read XML documents
created using the

XMLEncoder

and is used just like
the

ObjectInputStream

. For example, one can use
the following fragment to read the first object defined
in an XML document written by the

XMLEncoder

class:

```java
XMLDecoder d = new XMLDecoder(
new BufferedInputStream(
new FileInputStream("Test.xml")));
Object result = d.readObject();
d.close();
```

For more information you might also want to check out

Long Term Persistence of JavaBeans Components: XML Schema

,
an article in

The Swing Connection.

**All Implemented Interfaces:** AutoCloseable

---

### Field Details

*No entries found.*

### Constructor Details

#### public XMLDecoder​(
InputStream
in)

Creates a new input stream for reading archives
created by the

XMLEncoder

class.

**Parameters:**
- in

- The underlying stream.

**See Also:**
- XMLEncoder(java.io.OutputStream)

---

#### public XMLDecoder​(
InputStream
in,

Object
owner)

Creates a new input stream for reading archives
created by the

XMLEncoder

class.

**Parameters:**
- in

- The underlying stream.
- owner

- The owner of this stream.

---

#### public XMLDecoder​(
InputStream
in,

Object
owner,

ExceptionListener
exceptionListener)

Creates a new input stream for reading archives
created by the

XMLEncoder

class.

**Parameters:**
- in

- the underlying stream.
- owner

- the owner of this stream.
- exceptionListener

- the exception handler for the stream;
if

null

the default exception listener will be used.

---

#### public XMLDecoder​(
InputStream
in,

Object
owner,

ExceptionListener
exceptionListener,

ClassLoader
cl)

Creates a new input stream for reading archives
created by the

XMLEncoder

class.

**Parameters:**
- in

- the underlying stream.

null

may be passed without
error, though the resulting XMLDecoder will be useless
- owner

- the owner of this stream.

null

is a legal
value
- exceptionListener

- the exception handler for the stream, or

null

to use the default
- cl

- the class loader used for instantiating objects.

null

indicates that the default class loader should
be used

**Since:**
- 1.5

---

#### public XMLDecoder​(
InputSource
is)

Creates a new decoder to parse XML archives
created by the

XMLEncoder

class.
If the input source

is

is

null

,
no exception is thrown and no parsing is performed.
This behavior is similar to behavior of other constructors
that use

InputStream

as a parameter.

**Parameters:**
- is

- the input source to parse

**Since:**
- 1.7

---

### Method Details

#### public void close()

This method closes the input stream associated
with this stream.

**Specified by:**
- close

in interface

AutoCloseable

---

#### public void setExceptionListener​(
ExceptionListener
exceptionListener)

Sets the exception handler for this stream to

exceptionListener

.
The exception handler is notified when this stream catches recoverable
exceptions.

**Parameters:**
- exceptionListener

- The exception handler for this stream;
if

null

the default exception listener will be used.

**See Also:**
- getExceptionListener()

---

#### public
ExceptionListener
getExceptionListener()

Gets the exception handler for this stream.

**Returns:**
- The exception handler for this stream.
Will return the default exception listener if this has not explicitly been set.

**See Also:**
- setExceptionListener(java.beans.ExceptionListener)

---

#### public
Object
readObject()

Reads the next object from the underlying input stream.

**Returns:**
- the next object read

**Throws:**
- ArrayIndexOutOfBoundsException

- if the stream contains no objects
(or no more objects)

**See Also:**
- XMLEncoder.writeObject(java.lang.Object)

---

#### public void setOwner​(
Object
owner)

Sets the owner of this decoder to

owner

.

**Parameters:**
- owner

- The owner of this decoder.

**See Also:**
- getOwner()

---

#### public
Object
getOwner()

Gets the owner of this decoder.

**Returns:**
- The owner of this decoder.

**See Also:**
- setOwner(java.lang.Object)

---

#### public static
DefaultHandler
createHandler​(
Object
owner,

ExceptionListener
el,

ClassLoader
cl)

Creates a new handler for SAX parser
that can be used to parse embedded XML archives
created by the

XMLEncoder

class.

The

owner

should be used if parsed XML document contains
the method call within context of the <java> element.
The

null

value may cause illegal parsing in such case.
The same problem may occur, if the

owner

class
does not contain expected method to call. See details

here

.

**Parameters:**
- owner

- the owner of the default handler
that can be used as a value of <java> element
- el

- the exception handler for the parser,
or

null

to use the default exception handler
- cl

- the class loader used for instantiating objects,
or

null

to use the default class loader

**Returns:**
- an instance of

DefaultHandler

for SAX parser

**Since:**
- 1.7

---

### Additional Sections

#### Class XMLDecoder

java.lang.Object

- java.beans.XMLDecoder

java.beans.XMLDecoder

**All Implemented Interfaces:** AutoCloseable

```java
public class
XMLDecoder

extends
Object

implements
AutoCloseable
```

The

XMLDecoder

class is used to read XML documents
created using the

XMLEncoder

and is used just like
the

ObjectInputStream

. For example, one can use
the following fragment to read the first object defined
in an XML document written by the

XMLEncoder

class:

```java
XMLDecoder d = new XMLDecoder(
new BufferedInputStream(
new FileInputStream("Test.xml")));
Object result = d.readObject();
d.close();
```

For more information you might also want to check out

Long Term Persistence of JavaBeans Components: XML Schema

,
an article in

The Swing Connection.

**Since:** 1.4
**See Also:** XMLEncoder

,

ObjectInputStream

public class

XMLDecoder

extends

Object

implements

AutoCloseable

The

XMLDecoder

class is used to read XML documents
created using the

XMLEncoder

and is used just like
the

ObjectInputStream

. For example, one can use
the following fragment to read the first object defined
in an XML document written by the

XMLEncoder

class:

```java
XMLDecoder d = new XMLDecoder(
new BufferedInputStream(
new FileInputStream("Test.xml")));
Object result = d.readObject();
d.close();
```

For more information you might also want to check out

Long Term Persistence of JavaBeans Components: XML Schema

,
an article in

The Swing Connection.

XMLDecoder d = new XMLDecoder(
new BufferedInputStream(
new FileInputStream("Test.xml")));
Object result = d.readObject();
d.close();

For more information you might also want to check out

Long Term Persistence of JavaBeans Components: XML Schema

,
an article in

The Swing Connection.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

XMLDecoder

​(

InputStream

in)

Creates a new input stream for reading archives
created by the

XMLEncoder

class.

XMLDecoder

​(

InputStream

in,

Object

owner)

Creates a new input stream for reading archives
created by the

XMLEncoder

class.

XMLDecoder

​(

InputStream

in,

Object

owner,

ExceptionListener

exceptionListener)

Creates a new input stream for reading archives
created by the

XMLEncoder

class.

XMLDecoder

​(

InputStream

in,

Object

owner,

ExceptionListener

exceptionListener,

ClassLoader

cl)

Creates a new input stream for reading archives
created by the

XMLEncoder

class.

XMLDecoder

​(

InputSource

is)

Creates a new decoder to parse XML archives
created by the

XMLEncoder

class.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

close

()

This method closes the input stream associated
with this stream.

static

DefaultHandler

createHandler

​(

Object

owner,

ExceptionListener

el,

ClassLoader

cl)

Creates a new handler for SAX parser
that can be used to parse embedded XML archives
created by the

XMLEncoder

class.

ExceptionListener

getExceptionListener

()

Gets the exception handler for this stream.

Object

getOwner

()

Gets the owner of this decoder.

Object

readObject

()

Reads the next object from the underlying input stream.

void

setExceptionListener

​(

ExceptionListener

exceptionListener)

Sets the exception handler for this stream to

exceptionListener

.

void

setOwner

​(

Object

owner)

Sets the owner of this decoder to

owner

.

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

XMLDecoder

​(

InputStream

in)

Creates a new input stream for reading archives
created by the

XMLEncoder

class.

XMLDecoder

​(

InputStream

in,

Object

owner)

Creates a new input stream for reading archives
created by the

XMLEncoder

class.

XMLDecoder

​(

InputStream

in,

Object

owner,

ExceptionListener

exceptionListener)

Creates a new input stream for reading archives
created by the

XMLEncoder

class.

XMLDecoder

​(

InputStream

in,

Object

owner,

ExceptionListener

exceptionListener,

ClassLoader

cl)

Creates a new input stream for reading archives
created by the

XMLEncoder

class.

XMLDecoder

​(

InputSource

is)

Creates a new decoder to parse XML archives
created by the

XMLEncoder

class.

---

#### Constructor Summary

Creates a new input stream for reading archives
created by the

XMLEncoder

class.

Creates a new decoder to parse XML archives
created by the

XMLEncoder

class.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

close

()

This method closes the input stream associated
with this stream.

static

DefaultHandler

createHandler

​(

Object

owner,

ExceptionListener

el,

ClassLoader

cl)

Creates a new handler for SAX parser
that can be used to parse embedded XML archives
created by the

XMLEncoder

class.

ExceptionListener

getExceptionListener

()

Gets the exception handler for this stream.

Object

getOwner

()

Gets the owner of this decoder.

Object

readObject

()

Reads the next object from the underlying input stream.

void

setExceptionListener

​(

ExceptionListener

exceptionListener)

Sets the exception handler for this stream to

exceptionListener

.

void

setOwner

​(

Object

owner)

Sets the owner of this decoder to

owner

.

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

This method closes the input stream associated
with this stream.

Creates a new handler for SAX parser
that can be used to parse embedded XML archives
created by the

XMLEncoder

class.

Gets the exception handler for this stream.

Gets the owner of this decoder.

Reads the next object from the underlying input stream.

Sets the exception handler for this stream to

exceptionListener

.

Sets the owner of this decoder to

owner

.

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

- XMLDecoder

```java
public XMLDecoder​(
InputStream
in)
```

Creates a new input stream for reading archives
created by the

XMLEncoder

class.

**Parameters:** in

- The underlying stream.
**See Also:** XMLEncoder(java.io.OutputStream)

- XMLDecoder

```java
public XMLDecoder​(
InputStream
in,

Object
owner)
```

Creates a new input stream for reading archives
created by the

XMLEncoder

class.

**Parameters:** in

- The underlying stream.
**Parameters:** owner

- The owner of this stream.

- XMLDecoder

```java
public XMLDecoder​(
InputStream
in,

Object
owner,

ExceptionListener
exceptionListener)
```

Creates a new input stream for reading archives
created by the

XMLEncoder

class.

**Parameters:** in

- the underlying stream.
**Parameters:** owner

- the owner of this stream.
**Parameters:** exceptionListener

- the exception handler for the stream;
if

null

the default exception listener will be used.

- XMLDecoder

```java
public XMLDecoder​(
InputStream
in,

Object
owner,

ExceptionListener
exceptionListener,

ClassLoader
cl)
```

Creates a new input stream for reading archives
created by the

XMLEncoder

class.

**Parameters:** in

- the underlying stream.

null

may be passed without
error, though the resulting XMLDecoder will be useless
**Parameters:** owner

- the owner of this stream.

null

is a legal
value
**Parameters:** exceptionListener

- the exception handler for the stream, or

null

to use the default
**Parameters:** cl

- the class loader used for instantiating objects.

null

indicates that the default class loader should
be used
**Since:** 1.5

- XMLDecoder

```java
public XMLDecoder​(
InputSource
is)
```

Creates a new decoder to parse XML archives
created by the

XMLEncoder

class.
If the input source

is

is

null

,
no exception is thrown and no parsing is performed.
This behavior is similar to behavior of other constructors
that use

InputStream

as a parameter.

**Parameters:** is

- the input source to parse
**Since:** 1.7

============ METHOD DETAIL ==========

- Method Detail

- close

```java
public void close()
```

This method closes the input stream associated
with this stream.

**Specified by:** close

in interface

AutoCloseable

- setExceptionListener

```java
public void setExceptionListener​(
ExceptionListener
exceptionListener)
```

Sets the exception handler for this stream to

exceptionListener

.
The exception handler is notified when this stream catches recoverable
exceptions.

**Parameters:** exceptionListener

- The exception handler for this stream;
if

null

the default exception listener will be used.
**See Also:** getExceptionListener()

- getExceptionListener

```java
public
ExceptionListener
getExceptionListener()
```

Gets the exception handler for this stream.

**Returns:** The exception handler for this stream.
Will return the default exception listener if this has not explicitly been set.
**See Also:** setExceptionListener(java.beans.ExceptionListener)

- readObject

```java
public
Object
readObject()
```

Reads the next object from the underlying input stream.

**Returns:** the next object read
**Throws:** ArrayIndexOutOfBoundsException

- if the stream contains no objects
(or no more objects)
**See Also:** XMLEncoder.writeObject(java.lang.Object)

- setOwner

```java
public void setOwner​(
Object
owner)
```

Sets the owner of this decoder to

owner

.

**Parameters:** owner

- The owner of this decoder.
**See Also:** getOwner()

- getOwner

```java
public
Object
getOwner()
```

Gets the owner of this decoder.

**Returns:** The owner of this decoder.
**See Also:** setOwner(java.lang.Object)

- createHandler

```java
public static
DefaultHandler
createHandler​(
Object
owner,

ExceptionListener
el,

ClassLoader
cl)
```

Creates a new handler for SAX parser
that can be used to parse embedded XML archives
created by the

XMLEncoder

class.

The

owner

should be used if parsed XML document contains
the method call within context of the <java> element.
The

null

value may cause illegal parsing in such case.
The same problem may occur, if the

owner

class
does not contain expected method to call. See details

here

.

**Parameters:** owner

- the owner of the default handler
that can be used as a value of <java> element
**Parameters:** el

- the exception handler for the parser,
or

null

to use the default exception handler
**Parameters:** cl

- the class loader used for instantiating objects,
or

null

to use the default class loader
**Returns:** an instance of

DefaultHandler

for SAX parser
**Since:** 1.7

Constructor Detail

- XMLDecoder

```java
public XMLDecoder​(
InputStream
in)
```

Creates a new input stream for reading archives
created by the

XMLEncoder

class.

**Parameters:** in

- The underlying stream.
**See Also:** XMLEncoder(java.io.OutputStream)

- XMLDecoder

```java
public XMLDecoder​(
InputStream
in,

Object
owner)
```

Creates a new input stream for reading archives
created by the

XMLEncoder

class.

**Parameters:** in

- The underlying stream.
**Parameters:** owner

- The owner of this stream.

- XMLDecoder

```java
public XMLDecoder​(
InputStream
in,

Object
owner,

ExceptionListener
exceptionListener)
```

Creates a new input stream for reading archives
created by the

XMLEncoder

class.

**Parameters:** in

- the underlying stream.
**Parameters:** owner

- the owner of this stream.
**Parameters:** exceptionListener

- the exception handler for the stream;
if

null

the default exception listener will be used.

- XMLDecoder

```java
public XMLDecoder​(
InputStream
in,

Object
owner,

ExceptionListener
exceptionListener,

ClassLoader
cl)
```

Creates a new input stream for reading archives
created by the

XMLEncoder

class.

**Parameters:** in

- the underlying stream.

null

may be passed without
error, though the resulting XMLDecoder will be useless
**Parameters:** owner

- the owner of this stream.

null

is a legal
value
**Parameters:** exceptionListener

- the exception handler for the stream, or

null

to use the default
**Parameters:** cl

- the class loader used for instantiating objects.

null

indicates that the default class loader should
be used
**Since:** 1.5

- XMLDecoder

```java
public XMLDecoder​(
InputSource
is)
```

Creates a new decoder to parse XML archives
created by the

XMLEncoder

class.
If the input source

is

is

null

,
no exception is thrown and no parsing is performed.
This behavior is similar to behavior of other constructors
that use

InputStream

as a parameter.

**Parameters:** is

- the input source to parse
**Since:** 1.7

---

#### Constructor Detail

XMLDecoder

```java
public XMLDecoder​(
InputStream
in)
```

Creates a new input stream for reading archives
created by the

XMLEncoder

class.

**Parameters:** in

- The underlying stream.
**See Also:** XMLEncoder(java.io.OutputStream)

---

#### XMLDecoder

public XMLDecoder​(

InputStream

in)

Creates a new input stream for reading archives
created by the

XMLEncoder

class.

XMLDecoder

```java
public XMLDecoder​(
InputStream
in,

Object
owner)
```

Creates a new input stream for reading archives
created by the

XMLEncoder

class.

**Parameters:** in

- The underlying stream.
**Parameters:** owner

- The owner of this stream.

---

#### XMLDecoder

public XMLDecoder​(

InputStream

in,

Object

owner)

Creates a new input stream for reading archives
created by the

XMLEncoder

class.

XMLDecoder

```java
public XMLDecoder​(
InputStream
in,

Object
owner,

ExceptionListener
exceptionListener)
```

Creates a new input stream for reading archives
created by the

XMLEncoder

class.

**Parameters:** in

- the underlying stream.
**Parameters:** owner

- the owner of this stream.
**Parameters:** exceptionListener

- the exception handler for the stream;
if

null

the default exception listener will be used.

---

#### XMLDecoder

public XMLDecoder​(

InputStream

in,

Object

owner,

ExceptionListener

exceptionListener)

Creates a new input stream for reading archives
created by the

XMLEncoder

class.

XMLDecoder

```java
public XMLDecoder​(
InputStream
in,

Object
owner,

ExceptionListener
exceptionListener,

ClassLoader
cl)
```

Creates a new input stream for reading archives
created by the

XMLEncoder

class.

**Parameters:** in

- the underlying stream.

null

may be passed without
error, though the resulting XMLDecoder will be useless
**Parameters:** owner

- the owner of this stream.

null

is a legal
value
**Parameters:** exceptionListener

- the exception handler for the stream, or

null

to use the default
**Parameters:** cl

- the class loader used for instantiating objects.

null

indicates that the default class loader should
be used
**Since:** 1.5

---

#### XMLDecoder

public XMLDecoder​(

InputStream

in,

Object

owner,

ExceptionListener

exceptionListener,

ClassLoader

cl)

Creates a new input stream for reading archives
created by the

XMLEncoder

class.

XMLDecoder

```java
public XMLDecoder​(
InputSource
is)
```

Creates a new decoder to parse XML archives
created by the

XMLEncoder

class.
If the input source

is

is

null

,
no exception is thrown and no parsing is performed.
This behavior is similar to behavior of other constructors
that use

InputStream

as a parameter.

**Parameters:** is

- the input source to parse
**Since:** 1.7

---

#### XMLDecoder

public XMLDecoder​(

InputSource

is)

Creates a new decoder to parse XML archives
created by the

XMLEncoder

class.
If the input source

is

is

null

,
no exception is thrown and no parsing is performed.
This behavior is similar to behavior of other constructors
that use

InputStream

as a parameter.

Method Detail

- close

```java
public void close()
```

This method closes the input stream associated
with this stream.

**Specified by:** close

in interface

AutoCloseable

- setExceptionListener

```java
public void setExceptionListener​(
ExceptionListener
exceptionListener)
```

Sets the exception handler for this stream to

exceptionListener

.
The exception handler is notified when this stream catches recoverable
exceptions.

**Parameters:** exceptionListener

- The exception handler for this stream;
if

null

the default exception listener will be used.
**See Also:** getExceptionListener()

- getExceptionListener

```java
public
ExceptionListener
getExceptionListener()
```

Gets the exception handler for this stream.

**Returns:** The exception handler for this stream.
Will return the default exception listener if this has not explicitly been set.
**See Also:** setExceptionListener(java.beans.ExceptionListener)

- readObject

```java
public
Object
readObject()
```

Reads the next object from the underlying input stream.

**Returns:** the next object read
**Throws:** ArrayIndexOutOfBoundsException

- if the stream contains no objects
(or no more objects)
**See Also:** XMLEncoder.writeObject(java.lang.Object)

- setOwner

```java
public void setOwner​(
Object
owner)
```

Sets the owner of this decoder to

owner

.

**Parameters:** owner

- The owner of this decoder.
**See Also:** getOwner()

- getOwner

```java
public
Object
getOwner()
```

Gets the owner of this decoder.

**Returns:** The owner of this decoder.
**See Also:** setOwner(java.lang.Object)

- createHandler

```java
public static
DefaultHandler
createHandler​(
Object
owner,

ExceptionListener
el,

ClassLoader
cl)
```

Creates a new handler for SAX parser
that can be used to parse embedded XML archives
created by the

XMLEncoder

class.

The

owner

should be used if parsed XML document contains
the method call within context of the <java> element.
The

null

value may cause illegal parsing in such case.
The same problem may occur, if the

owner

class
does not contain expected method to call. See details

here

.

**Parameters:** owner

- the owner of the default handler
that can be used as a value of <java> element
**Parameters:** el

- the exception handler for the parser,
or

null

to use the default exception handler
**Parameters:** cl

- the class loader used for instantiating objects,
or

null

to use the default class loader
**Returns:** an instance of

DefaultHandler

for SAX parser
**Since:** 1.7

---

#### Method Detail

close

```java
public void close()
```

This method closes the input stream associated
with this stream.

**Specified by:** close

in interface

AutoCloseable

---

#### close

public void close()

This method closes the input stream associated
with this stream.

setExceptionListener

```java
public void setExceptionListener​(
ExceptionListener
exceptionListener)
```

Sets the exception handler for this stream to

exceptionListener

.
The exception handler is notified when this stream catches recoverable
exceptions.

**Parameters:** exceptionListener

- The exception handler for this stream;
if

null

the default exception listener will be used.
**See Also:** getExceptionListener()

---

#### setExceptionListener

public void setExceptionListener​(

ExceptionListener

exceptionListener)

Sets the exception handler for this stream to

exceptionListener

.
The exception handler is notified when this stream catches recoverable
exceptions.

getExceptionListener

```java
public
ExceptionListener
getExceptionListener()
```

Gets the exception handler for this stream.

**Returns:** The exception handler for this stream.
Will return the default exception listener if this has not explicitly been set.
**See Also:** setExceptionListener(java.beans.ExceptionListener)

---

#### getExceptionListener

public

ExceptionListener

getExceptionListener()

Gets the exception handler for this stream.

readObject

```java
public
Object
readObject()
```

Reads the next object from the underlying input stream.

**Returns:** the next object read
**Throws:** ArrayIndexOutOfBoundsException

- if the stream contains no objects
(or no more objects)
**See Also:** XMLEncoder.writeObject(java.lang.Object)

---

#### readObject

public

Object

readObject()

Reads the next object from the underlying input stream.

setOwner

```java
public void setOwner​(
Object
owner)
```

Sets the owner of this decoder to

owner

.

**Parameters:** owner

- The owner of this decoder.
**See Also:** getOwner()

---

#### setOwner

public void setOwner​(

Object

owner)

Sets the owner of this decoder to

owner

.

getOwner

```java
public
Object
getOwner()
```

Gets the owner of this decoder.

**Returns:** The owner of this decoder.
**See Also:** setOwner(java.lang.Object)

---

#### getOwner

public

Object

getOwner()

Gets the owner of this decoder.

createHandler

```java
public static
DefaultHandler
createHandler​(
Object
owner,

ExceptionListener
el,

ClassLoader
cl)
```

Creates a new handler for SAX parser
that can be used to parse embedded XML archives
created by the

XMLEncoder

class.

The

owner

should be used if parsed XML document contains
the method call within context of the <java> element.
The

null

value may cause illegal parsing in such case.
The same problem may occur, if the

owner

class
does not contain expected method to call. See details

here

.

**Parameters:** owner

- the owner of the default handler
that can be used as a value of <java> element
**Parameters:** el

- the exception handler for the parser,
or

null

to use the default exception handler
**Parameters:** cl

- the class loader used for instantiating objects,
or

null

to use the default class loader
**Returns:** an instance of

DefaultHandler

for SAX parser
**Since:** 1.7

---

#### createHandler

public static

DefaultHandler

createHandler​(

Object

owner,

ExceptionListener

el,

ClassLoader

cl)

Creates a new handler for SAX parser
that can be used to parse embedded XML archives
created by the

XMLEncoder

class.

The

owner

should be used if parsed XML document contains
the method call within context of the <java> element.
The

null

value may cause illegal parsing in such case.
The same problem may occur, if the

owner

class
does not contain expected method to call. See details

here

.

---

