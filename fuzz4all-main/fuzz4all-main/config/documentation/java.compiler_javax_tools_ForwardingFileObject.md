# Class ForwardingFileObject<F extends FileObject >

**Source:** `java.compiler\javax\tools\ForwardingFileObject.html`

### Class Description

```java
public class
ForwardingFileObject<F extends
FileObject
>

extends
Object

implements
FileObject
```

Forwards calls to a given file object. Subclasses of this class
might override some of these methods and might also provide
additional fields and methods.

**Type Parameters:** F

- the kind of file object forwarded to by this object

---

### Field Details

#### protected final
F
extends
FileObject
fileObject

The file object which all methods are delegated to.

---

### Constructor Details

#### protected ForwardingFileObject​(
F
fileObject)

Creates a new instance of ForwardingFileObject.

**Parameters:**
- fileObject

- delegate to this file object

---

### Method Details

#### public
InputStream
openInputStream()
throws
IOException

Description copied from interface:

FileObject

**Specified by:**
- openInputStream

in interface

FileObject

**Returns:**
- an InputStream

**Throws:**
- IllegalStateException

- if this file object was
opened for writing and does not support reading
- UnsupportedOperationException

- if this kind of file
object does not support byte access
- IOException

- if an I/O error occurred

---

#### public
OutputStream
openOutputStream()
throws
IOException

Description copied from interface:

FileObject

**Specified by:**
- openOutputStream

in interface

FileObject

**Returns:**
- an OutputStream

**Throws:**
- IllegalStateException

- if this file object was
opened for reading and does not support writing
- UnsupportedOperationException

- if this kind of
file object does not support byte access
- IOException

- if an I/O error occurred

---

#### public
Reader
openReader​(boolean ignoreEncodingErrors)
throws
IOException

Description copied from interface:

FileObject

**Specified by:**
- openReader

in interface

FileObject

**Parameters:**
- ignoreEncodingErrors

- ignore encoding errors if true

**Returns:**
- a Reader

**Throws:**
- IllegalStateException

- if this file object was
opened for writing and does not support reading
- UnsupportedOperationException

- if this kind of
file object does not support character access
- IOException

- if an I/O error occurred

---

#### public
CharSequence
getCharContent​(boolean ignoreEncodingErrors)
throws
IOException

Description copied from interface:

FileObject

**Specified by:**
- getCharContent

in interface

FileObject

**Parameters:**
- ignoreEncodingErrors

- ignore encoding errors if true

**Returns:**
- a CharSequence if available;

null

otherwise

**Throws:**
- IllegalStateException

- if this file object was
opened for writing and does not support reading
- UnsupportedOperationException

- if this kind of
file object does not support character access
- IOException

- if an I/O error occurred

---

#### public
Writer
openWriter()
throws
IOException

Description copied from interface:

FileObject

**Specified by:**
- openWriter

in interface

FileObject

**Returns:**
- a Writer

**Throws:**
- IllegalStateException

- if this file object was
opened for reading and does not support writing
- UnsupportedOperationException

- if this kind of
file object does not support character access
- IOException

- if an I/O error occurred

---

### Additional Sections

#### Class ForwardingFileObject<F extends FileObject >

java.lang.Object

- javax.tools.ForwardingFileObject<F>

javax.tools.ForwardingFileObject<F>

**Type Parameters:** F

- the kind of file object forwarded to by this object

**All Implemented Interfaces:** FileObject

**Direct Known Subclasses:** ForwardingJavaFileObject

```java
public class
ForwardingFileObject<F extends
FileObject
>

extends
Object

implements
FileObject
```

Forwards calls to a given file object. Subclasses of this class
might override some of these methods and might also provide
additional fields and methods.

**Since:** 1.6

public class

ForwardingFileObject<F extends

FileObject

>

extends

Object

implements

FileObject

Forwards calls to a given file object. Subclasses of this class
might override some of these methods and might also provide
additional fields and methods.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

F

fileObject

The file object which all methods are delegated to.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

ForwardingFileObject

​(

F

fileObject)

Creates a new instance of ForwardingFileObject.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

CharSequence

getCharContent

​(boolean ignoreEncodingErrors)

Returns the character content of this file object, if available.

InputStream

openInputStream

()

Returns an InputStream for this file object.

OutputStream

openOutputStream

()

Returns an OutputStream for this file object.

Reader

openReader

​(boolean ignoreEncodingErrors)

Returns a reader for this object.

Writer

openWriter

()

Returns a Writer for this file object.

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

- Methods declared in interface javax.tools.

FileObject

delete

,

getLastModified

,

getName

,

toUri

Field Summary

Fields

Modifier and Type

Field

Description

protected

F

fileObject

The file object which all methods are delegated to.

---

#### Field Summary

The file object which all methods are delegated to.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

ForwardingFileObject

​(

F

fileObject)

Creates a new instance of ForwardingFileObject.

---

#### Constructor Summary

Creates a new instance of ForwardingFileObject.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

CharSequence

getCharContent

​(boolean ignoreEncodingErrors)

Returns the character content of this file object, if available.

InputStream

openInputStream

()

Returns an InputStream for this file object.

OutputStream

openOutputStream

()

Returns an OutputStream for this file object.

Reader

openReader

​(boolean ignoreEncodingErrors)

Returns a reader for this object.

Writer

openWriter

()

Returns a Writer for this file object.

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

- Methods declared in interface javax.tools.

FileObject

delete

,

getLastModified

,

getName

,

toUri

---

#### Method Summary

Returns the character content of this file object, if available.

Returns an InputStream for this file object.

Returns an OutputStream for this file object.

Returns a reader for this object.

Returns a Writer for this file object.

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

Methods declared in interface javax.tools.

FileObject

delete

,

getLastModified

,

getName

,

toUri

---

#### Methods declared in interface javax.tools. FileObject

============ FIELD DETAIL ===========

- Field Detail

- fileObject

```java
protected final
F
extends
FileObject
fileObject
```

The file object which all methods are delegated to.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ForwardingFileObject

```java
protected ForwardingFileObject​(
F
fileObject)
```

Creates a new instance of ForwardingFileObject.

**Parameters:** fileObject

- delegate to this file object

============ METHOD DETAIL ==========

- Method Detail

- openInputStream

```java
public
InputStream
openInputStream()
throws
IOException
```

Description copied from interface:

FileObject

Returns an InputStream for this file object.

**Specified by:** openInputStream

in interface

FileObject
**Returns:** an InputStream
**Throws:** IllegalStateException

- if this file object was
opened for writing and does not support reading
**Throws:** UnsupportedOperationException

- if this kind of file
object does not support byte access
**Throws:** IOException

- if an I/O error occurred

- openOutputStream

```java
public
OutputStream
openOutputStream()
throws
IOException
```

Description copied from interface:

FileObject

Returns an OutputStream for this file object.

**Specified by:** openOutputStream

in interface

FileObject
**Returns:** an OutputStream
**Throws:** IllegalStateException

- if this file object was
opened for reading and does not support writing
**Throws:** UnsupportedOperationException

- if this kind of
file object does not support byte access
**Throws:** IOException

- if an I/O error occurred

- openReader

```java
public
Reader
openReader​(boolean ignoreEncodingErrors)
throws
IOException
```

Description copied from interface:

FileObject

Returns a reader for this object. The returned reader will
replace bytes that cannot be decoded with the default
translation character. In addition, the reader may report a
diagnostic unless

ignoreEncodingErrors

is true.

**Specified by:** openReader

in interface

FileObject
**Parameters:** ignoreEncodingErrors

- ignore encoding errors if true
**Returns:** a Reader
**Throws:** IllegalStateException

- if this file object was
opened for writing and does not support reading
**Throws:** UnsupportedOperationException

- if this kind of
file object does not support character access
**Throws:** IOException

- if an I/O error occurred

- getCharContent

```java
public
CharSequence
getCharContent​(boolean ignoreEncodingErrors)
throws
IOException
```

Description copied from interface:

FileObject

Returns the character content of this file object, if available.
Any byte that cannot be decoded will be replaced by the default
translation character. In addition, a diagnostic may be
reported unless

ignoreEncodingErrors

is true.

**Specified by:** getCharContent

in interface

FileObject
**Parameters:** ignoreEncodingErrors

- ignore encoding errors if true
**Returns:** a CharSequence if available;

null

otherwise
**Throws:** IllegalStateException

- if this file object was
opened for writing and does not support reading
**Throws:** UnsupportedOperationException

- if this kind of
file object does not support character access
**Throws:** IOException

- if an I/O error occurred

- openWriter

```java
public
Writer
openWriter()
throws
IOException
```

Description copied from interface:

FileObject

Returns a Writer for this file object.

**Specified by:** openWriter

in interface

FileObject
**Returns:** a Writer
**Throws:** IllegalStateException

- if this file object was
opened for reading and does not support writing
**Throws:** UnsupportedOperationException

- if this kind of
file object does not support character access
**Throws:** IOException

- if an I/O error occurred

Field Detail

- fileObject

```java
protected final
F
extends
FileObject
fileObject
```

The file object which all methods are delegated to.

---

#### Field Detail

fileObject

```java
protected final
F
extends
FileObject
fileObject
```

The file object which all methods are delegated to.

---

#### fileObject

protected final

F

extends

FileObject

fileObject

The file object which all methods are delegated to.

Constructor Detail

- ForwardingFileObject

```java
protected ForwardingFileObject​(
F
fileObject)
```

Creates a new instance of ForwardingFileObject.

**Parameters:** fileObject

- delegate to this file object

---

#### Constructor Detail

ForwardingFileObject

```java
protected ForwardingFileObject​(
F
fileObject)
```

Creates a new instance of ForwardingFileObject.

**Parameters:** fileObject

- delegate to this file object

---

#### ForwardingFileObject

protected ForwardingFileObject​(

F

fileObject)

Creates a new instance of ForwardingFileObject.

Method Detail

- openInputStream

```java
public
InputStream
openInputStream()
throws
IOException
```

Description copied from interface:

FileObject

Returns an InputStream for this file object.

**Specified by:** openInputStream

in interface

FileObject
**Returns:** an InputStream
**Throws:** IllegalStateException

- if this file object was
opened for writing and does not support reading
**Throws:** UnsupportedOperationException

- if this kind of file
object does not support byte access
**Throws:** IOException

- if an I/O error occurred

- openOutputStream

```java
public
OutputStream
openOutputStream()
throws
IOException
```

Description copied from interface:

FileObject

Returns an OutputStream for this file object.

**Specified by:** openOutputStream

in interface

FileObject
**Returns:** an OutputStream
**Throws:** IllegalStateException

- if this file object was
opened for reading and does not support writing
**Throws:** UnsupportedOperationException

- if this kind of
file object does not support byte access
**Throws:** IOException

- if an I/O error occurred

- openReader

```java
public
Reader
openReader​(boolean ignoreEncodingErrors)
throws
IOException
```

Description copied from interface:

FileObject

Returns a reader for this object. The returned reader will
replace bytes that cannot be decoded with the default
translation character. In addition, the reader may report a
diagnostic unless

ignoreEncodingErrors

is true.

**Specified by:** openReader

in interface

FileObject
**Parameters:** ignoreEncodingErrors

- ignore encoding errors if true
**Returns:** a Reader
**Throws:** IllegalStateException

- if this file object was
opened for writing and does not support reading
**Throws:** UnsupportedOperationException

- if this kind of
file object does not support character access
**Throws:** IOException

- if an I/O error occurred

- getCharContent

```java
public
CharSequence
getCharContent​(boolean ignoreEncodingErrors)
throws
IOException
```

Description copied from interface:

FileObject

Returns the character content of this file object, if available.
Any byte that cannot be decoded will be replaced by the default
translation character. In addition, a diagnostic may be
reported unless

ignoreEncodingErrors

is true.

**Specified by:** getCharContent

in interface

FileObject
**Parameters:** ignoreEncodingErrors

- ignore encoding errors if true
**Returns:** a CharSequence if available;

null

otherwise
**Throws:** IllegalStateException

- if this file object was
opened for writing and does not support reading
**Throws:** UnsupportedOperationException

- if this kind of
file object does not support character access
**Throws:** IOException

- if an I/O error occurred

- openWriter

```java
public
Writer
openWriter()
throws
IOException
```

Description copied from interface:

FileObject

Returns a Writer for this file object.

**Specified by:** openWriter

in interface

FileObject
**Returns:** a Writer
**Throws:** IllegalStateException

- if this file object was
opened for reading and does not support writing
**Throws:** UnsupportedOperationException

- if this kind of
file object does not support character access
**Throws:** IOException

- if an I/O error occurred

---

#### Method Detail

openInputStream

```java
public
InputStream
openInputStream()
throws
IOException
```

Description copied from interface:

FileObject

Returns an InputStream for this file object.

**Specified by:** openInputStream

in interface

FileObject
**Returns:** an InputStream
**Throws:** IllegalStateException

- if this file object was
opened for writing and does not support reading
**Throws:** UnsupportedOperationException

- if this kind of file
object does not support byte access
**Throws:** IOException

- if an I/O error occurred

---

#### openInputStream

public

InputStream

openInputStream()
throws

IOException

Description copied from interface:

FileObject

Returns an InputStream for this file object.

openOutputStream

```java
public
OutputStream
openOutputStream()
throws
IOException
```

Description copied from interface:

FileObject

Returns an OutputStream for this file object.

**Specified by:** openOutputStream

in interface

FileObject
**Returns:** an OutputStream
**Throws:** IllegalStateException

- if this file object was
opened for reading and does not support writing
**Throws:** UnsupportedOperationException

- if this kind of
file object does not support byte access
**Throws:** IOException

- if an I/O error occurred

---

#### openOutputStream

public

OutputStream

openOutputStream()
throws

IOException

Description copied from interface:

FileObject

Returns an OutputStream for this file object.

openReader

```java
public
Reader
openReader​(boolean ignoreEncodingErrors)
throws
IOException
```

Description copied from interface:

FileObject

Returns a reader for this object. The returned reader will
replace bytes that cannot be decoded with the default
translation character. In addition, the reader may report a
diagnostic unless

ignoreEncodingErrors

is true.

**Specified by:** openReader

in interface

FileObject
**Parameters:** ignoreEncodingErrors

- ignore encoding errors if true
**Returns:** a Reader
**Throws:** IllegalStateException

- if this file object was
opened for writing and does not support reading
**Throws:** UnsupportedOperationException

- if this kind of
file object does not support character access
**Throws:** IOException

- if an I/O error occurred

---

#### openReader

public

Reader

openReader​(boolean ignoreEncodingErrors)
throws

IOException

Description copied from interface:

FileObject

Returns a reader for this object. The returned reader will
replace bytes that cannot be decoded with the default
translation character. In addition, the reader may report a
diagnostic unless

ignoreEncodingErrors

is true.

getCharContent

```java
public
CharSequence
getCharContent​(boolean ignoreEncodingErrors)
throws
IOException
```

Description copied from interface:

FileObject

Returns the character content of this file object, if available.
Any byte that cannot be decoded will be replaced by the default
translation character. In addition, a diagnostic may be
reported unless

ignoreEncodingErrors

is true.

**Specified by:** getCharContent

in interface

FileObject
**Parameters:** ignoreEncodingErrors

- ignore encoding errors if true
**Returns:** a CharSequence if available;

null

otherwise
**Throws:** IllegalStateException

- if this file object was
opened for writing and does not support reading
**Throws:** UnsupportedOperationException

- if this kind of
file object does not support character access
**Throws:** IOException

- if an I/O error occurred

---

#### getCharContent

public

CharSequence

getCharContent​(boolean ignoreEncodingErrors)
throws

IOException

Description copied from interface:

FileObject

Returns the character content of this file object, if available.
Any byte that cannot be decoded will be replaced by the default
translation character. In addition, a diagnostic may be
reported unless

ignoreEncodingErrors

is true.

openWriter

```java
public
Writer
openWriter()
throws
IOException
```

Description copied from interface:

FileObject

Returns a Writer for this file object.

**Specified by:** openWriter

in interface

FileObject
**Returns:** a Writer
**Throws:** IllegalStateException

- if this file object was
opened for reading and does not support writing
**Throws:** UnsupportedOperationException

- if this kind of
file object does not support character access
**Throws:** IOException

- if an I/O error occurred

---

#### openWriter

public

Writer

openWriter()
throws

IOException

Description copied from interface:

FileObject

Returns a Writer for this file object.

---

