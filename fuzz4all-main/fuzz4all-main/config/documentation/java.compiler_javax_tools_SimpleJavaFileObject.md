# Class SimpleJavaFileObject

**Source:** `java.compiler\javax\tools\SimpleJavaFileObject.html`

### Class Description

```java
public class
SimpleJavaFileObject

extends
Object

implements
JavaFileObject
```

Provides simple implementations for most methods in JavaFileObject.
This class is designed to be subclassed and used as a basis for
JavaFileObject implementations. Subclasses can override the
implementation and specification of any method of this class as
long as the general contract of JavaFileObject is obeyed.

**All Implemented Interfaces:** FileObject

,

JavaFileObject

---

### Field Details

#### protected final
URI
uri

A URI for this file object.

---

#### protected final
JavaFileObject.Kind
kind

The kind of this file object.

---

### Constructor Details

#### protected SimpleJavaFileObject​(
URI
uri,

JavaFileObject.Kind
kind)

Construct a SimpleJavaFileObject of the given kind and with the
given URI.

**Parameters:**
- uri

- the URI for this file object
- kind

- the kind of this file object

---

### Method Details

#### public
InputStream
openInputStream()
throws
IOException

This implementation always throws

UnsupportedOperationException

. Subclasses can change this
behavior as long as the contract of

FileObject

is
obeyed.

**Specified by:**
- openInputStream

in interface

FileObject

**Returns:**
- an InputStream

**Throws:**
- IOException

- if an I/O error occurred

---

#### public
OutputStream
openOutputStream()
throws
IOException

This implementation always throws

UnsupportedOperationException

. Subclasses can change this
behavior as long as the contract of

FileObject

is
obeyed.

**Specified by:**
- openOutputStream

in interface

FileObject

**Returns:**
- an OutputStream

**Throws:**
- IOException

- if an I/O error occurred

---

#### public
Reader
openReader​(boolean ignoreEncodingErrors)
throws
IOException

Wraps the result of

getCharContent(boolean)

in a Reader.
Subclasses can change this behavior as long as the contract of

FileObject

is obeyed.

**Specified by:**
- openReader

in interface

FileObject

**Parameters:**
- ignoreEncodingErrors

- ignore encoding errors if true

**Returns:**
- a Reader wrapping the result of getCharContent

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

This implementation always throws

UnsupportedOperationException

. Subclasses can change this
behavior as long as the contract of

FileObject

is
obeyed.

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
- IOException

- if an I/O error occurred

---

#### public
Writer
openWriter()
throws
IOException

Wraps the result of openOutputStream in a Writer. Subclasses
can change this behavior as long as the contract of

FileObject

is obeyed.

**Specified by:**
- openWriter

in interface

FileObject

**Returns:**
- a Writer wrapping the result of openOutputStream

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

#### public long getLastModified()

This implementation returns

0L

. Subclasses can change
this behavior as long as the contract of

FileObject

is
obeyed.

**Specified by:**
- getLastModified

in interface

FileObject

**Returns:**
- 0L

---

#### public boolean delete()

This implementation does nothing. Subclasses can change this
behavior as long as the contract of

FileObject

is
obeyed.

**Specified by:**
- delete

in interface

FileObject

**Returns:**
- false

---

#### public
JavaFileObject.Kind
getKind()

Description copied from interface:

JavaFileObject

**Specified by:**
- getKind

in interface

JavaFileObject

**Returns:**
- this.kind

---

#### public boolean isNameCompatible​(
String
simpleName,

JavaFileObject.Kind
kind)

This implementation compares the path of its URI to the given
simple name. This method returns true if the given kind is
equal to the kind of this object, and if the path is equal to

simpleName + kind.extension

or if it ends with

"/" + simpleName + kind.extension

.

This method calls

getKind()

and

FileObject.toUri()

and
does not access the fields

uri

and

kind

directly.

Subclasses can change this behavior as long as the contract
of

JavaFileObject

is obeyed.

**Specified by:**
- isNameCompatible

in interface

JavaFileObject

**Parameters:**
- simpleName

- a simple name of a class
- kind

- a kind

**Returns:**
- true

if this file object is compatible; false
otherwise

---

#### public
NestingKind
getNestingKind()

This implementation returns

null

. Subclasses can
change this behavior as long as the contract of

JavaFileObject

is obeyed.

**Specified by:**
- getNestingKind

in interface

JavaFileObject

**Returns:**
- the nesting kind, or

null

if the nesting kind
is not known

---

#### public
Modifier
getAccessLevel()

This implementation returns

null

. Subclasses can
change this behavior as long as the contract of

JavaFileObject

is obeyed.

**Specified by:**
- getAccessLevel

in interface

JavaFileObject

**Returns:**
- the access level

---

### Additional Sections

#### Class SimpleJavaFileObject

java.lang.Object

- javax.tools.SimpleJavaFileObject

javax.tools.SimpleJavaFileObject

**All Implemented Interfaces:** FileObject

,

JavaFileObject

```java
public class
SimpleJavaFileObject

extends
Object

implements
JavaFileObject
```

Provides simple implementations for most methods in JavaFileObject.
This class is designed to be subclassed and used as a basis for
JavaFileObject implementations. Subclasses can override the
implementation and specification of any method of this class as
long as the general contract of JavaFileObject is obeyed.

**Since:** 1.6

public class

SimpleJavaFileObject

extends

Object

implements

JavaFileObject

Provides simple implementations for most methods in JavaFileObject.
This class is designed to be subclassed and used as a basis for
JavaFileObject implementations. Subclasses can override the
implementation and specification of any method of this class as
long as the general contract of JavaFileObject is obeyed.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in interface javax.tools.

JavaFileObject

JavaFileObject.Kind

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

JavaFileObject.Kind

kind

The kind of this file object.

protected

URI

uri

A URI for this file object.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

SimpleJavaFileObject

​(

URI

uri,

JavaFileObject.Kind

kind)

Construct a SimpleJavaFileObject of the given kind and with the
given URI.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

delete

()

This implementation does nothing.

Modifier

getAccessLevel

()

This implementation returns

null

.

CharSequence

getCharContent

​(boolean ignoreEncodingErrors)

This implementation always throws

UnsupportedOperationException

.

JavaFileObject.Kind

getKind

()

Returns the kind of this file object.

long

getLastModified

()

This implementation returns

0L

.

NestingKind

getNestingKind

()

This implementation returns

null

.

boolean

isNameCompatible

​(

String

simpleName,

JavaFileObject.Kind

kind)

This implementation compares the path of its URI to the given
simple name.

InputStream

openInputStream

()

This implementation always throws

UnsupportedOperationException

.

OutputStream

openOutputStream

()

This implementation always throws

UnsupportedOperationException

.

Reader

openReader

​(boolean ignoreEncodingErrors)

Wraps the result of

getCharContent(boolean)

in a Reader.

Writer

openWriter

()

Wraps the result of openOutputStream in a Writer.

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

getName

,

toUri

Nested Class Summary

- Nested classes/interfaces declared in interface javax.tools.

JavaFileObject

JavaFileObject.Kind

---

#### Nested Class Summary

Nested classes/interfaces declared in interface javax.tools.

JavaFileObject

JavaFileObject.Kind

---

#### Nested classes/interfaces declared in interface javax.tools. JavaFileObject

Field Summary

Fields

Modifier and Type

Field

Description

protected

JavaFileObject.Kind

kind

The kind of this file object.

protected

URI

uri

A URI for this file object.

---

#### Field Summary

The kind of this file object.

A URI for this file object.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

SimpleJavaFileObject

​(

URI

uri,

JavaFileObject.Kind

kind)

Construct a SimpleJavaFileObject of the given kind and with the
given URI.

---

#### Constructor Summary

Construct a SimpleJavaFileObject of the given kind and with the
given URI.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

delete

()

This implementation does nothing.

Modifier

getAccessLevel

()

This implementation returns

null

.

CharSequence

getCharContent

​(boolean ignoreEncodingErrors)

This implementation always throws

UnsupportedOperationException

.

JavaFileObject.Kind

getKind

()

Returns the kind of this file object.

long

getLastModified

()

This implementation returns

0L

.

NestingKind

getNestingKind

()

This implementation returns

null

.

boolean

isNameCompatible

​(

String

simpleName,

JavaFileObject.Kind

kind)

This implementation compares the path of its URI to the given
simple name.

InputStream

openInputStream

()

This implementation always throws

UnsupportedOperationException

.

OutputStream

openOutputStream

()

This implementation always throws

UnsupportedOperationException

.

Reader

openReader

​(boolean ignoreEncodingErrors)

Wraps the result of

getCharContent(boolean)

in a Reader.

Writer

openWriter

()

Wraps the result of openOutputStream in a Writer.

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

getName

,

toUri

---

#### Method Summary

This implementation does nothing.

This implementation returns

null

.

This implementation always throws

UnsupportedOperationException

.

Returns the kind of this file object.

This implementation returns

0L

.

This implementation compares the path of its URI to the given
simple name.

Wraps the result of

getCharContent(boolean)

in a Reader.

Wraps the result of openOutputStream in a Writer.

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

getName

,

toUri

---

#### Methods declared in interface javax.tools. FileObject

============ FIELD DETAIL ===========

- Field Detail

- uri

```java
protected final
URI
uri
```

A URI for this file object.

- kind

```java
protected final
JavaFileObject.Kind
kind
```

The kind of this file object.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SimpleJavaFileObject

```java
protected SimpleJavaFileObject​(
URI
uri,

JavaFileObject.Kind
kind)
```

Construct a SimpleJavaFileObject of the given kind and with the
given URI.

**Parameters:** uri

- the URI for this file object
**Parameters:** kind

- the kind of this file object

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

This implementation always throws

UnsupportedOperationException

. Subclasses can change this
behavior as long as the contract of

FileObject

is
obeyed.

**Specified by:** openInputStream

in interface

FileObject
**Returns:** an InputStream
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

This implementation always throws

UnsupportedOperationException

. Subclasses can change this
behavior as long as the contract of

FileObject

is
obeyed.

**Specified by:** openOutputStream

in interface

FileObject
**Returns:** an OutputStream
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

Wraps the result of

getCharContent(boolean)

in a Reader.
Subclasses can change this behavior as long as the contract of

FileObject

is obeyed.

**Specified by:** openReader

in interface

FileObject
**Parameters:** ignoreEncodingErrors

- ignore encoding errors if true
**Returns:** a Reader wrapping the result of getCharContent
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

This implementation always throws

UnsupportedOperationException

. Subclasses can change this
behavior as long as the contract of

FileObject

is
obeyed.

**Specified by:** getCharContent

in interface

FileObject
**Parameters:** ignoreEncodingErrors

- ignore encoding errors if true
**Returns:** a CharSequence if available;

null

otherwise
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

Wraps the result of openOutputStream in a Writer. Subclasses
can change this behavior as long as the contract of

FileObject

is obeyed.

**Specified by:** openWriter

in interface

FileObject
**Returns:** a Writer wrapping the result of openOutputStream
**Throws:** IllegalStateException

- if this file object was
opened for reading and does not support writing
**Throws:** UnsupportedOperationException

- if this kind of
file object does not support character access
**Throws:** IOException

- if an I/O error occurred

- getLastModified

```java
public long getLastModified()
```

This implementation returns

0L

. Subclasses can change
this behavior as long as the contract of

FileObject

is
obeyed.

**Specified by:** getLastModified

in interface

FileObject
**Returns:** 0L

- delete

```java
public boolean delete()
```

This implementation does nothing. Subclasses can change this
behavior as long as the contract of

FileObject

is
obeyed.

**Specified by:** delete

in interface

FileObject
**Returns:** false

- getKind

```java
public
JavaFileObject.Kind
getKind()
```

Description copied from interface:

JavaFileObject

Returns the kind of this file object.

**Specified by:** getKind

in interface

JavaFileObject
**Returns:** this.kind

- isNameCompatible

```java
public boolean isNameCompatible​(
String
simpleName,

JavaFileObject.Kind
kind)
```

This implementation compares the path of its URI to the given
simple name. This method returns true if the given kind is
equal to the kind of this object, and if the path is equal to

simpleName + kind.extension

or if it ends with

"/" + simpleName + kind.extension

.

This method calls

getKind()

and

FileObject.toUri()

and
does not access the fields

uri

and

kind

directly.

Subclasses can change this behavior as long as the contract
of

JavaFileObject

is obeyed.

**Specified by:** isNameCompatible

in interface

JavaFileObject
**Parameters:** simpleName

- a simple name of a class
**Parameters:** kind

- a kind
**Returns:** true

if this file object is compatible; false
otherwise

- getNestingKind

```java
public
NestingKind
getNestingKind()
```

This implementation returns

null

. Subclasses can
change this behavior as long as the contract of

JavaFileObject

is obeyed.

**Specified by:** getNestingKind

in interface

JavaFileObject
**Returns:** the nesting kind, or

null

if the nesting kind
is not known

- getAccessLevel

```java
public
Modifier
getAccessLevel()
```

This implementation returns

null

. Subclasses can
change this behavior as long as the contract of

JavaFileObject

is obeyed.

**Specified by:** getAccessLevel

in interface

JavaFileObject
**Returns:** the access level

Field Detail

- uri

```java
protected final
URI
uri
```

A URI for this file object.

- kind

```java
protected final
JavaFileObject.Kind
kind
```

The kind of this file object.

---

#### Field Detail

uri

```java
protected final
URI
uri
```

A URI for this file object.

---

#### uri

protected final

URI

uri

A URI for this file object.

kind

```java
protected final
JavaFileObject.Kind
kind
```

The kind of this file object.

---

#### kind

protected final

JavaFileObject.Kind

kind

The kind of this file object.

Constructor Detail

- SimpleJavaFileObject

```java
protected SimpleJavaFileObject​(
URI
uri,

JavaFileObject.Kind
kind)
```

Construct a SimpleJavaFileObject of the given kind and with the
given URI.

**Parameters:** uri

- the URI for this file object
**Parameters:** kind

- the kind of this file object

---

#### Constructor Detail

SimpleJavaFileObject

```java
protected SimpleJavaFileObject​(
URI
uri,

JavaFileObject.Kind
kind)
```

Construct a SimpleJavaFileObject of the given kind and with the
given URI.

**Parameters:** uri

- the URI for this file object
**Parameters:** kind

- the kind of this file object

---

#### SimpleJavaFileObject

protected SimpleJavaFileObject​(

URI

uri,

JavaFileObject.Kind

kind)

Construct a SimpleJavaFileObject of the given kind and with the
given URI.

Method Detail

- openInputStream

```java
public
InputStream
openInputStream()
throws
IOException
```

This implementation always throws

UnsupportedOperationException

. Subclasses can change this
behavior as long as the contract of

FileObject

is
obeyed.

**Specified by:** openInputStream

in interface

FileObject
**Returns:** an InputStream
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

This implementation always throws

UnsupportedOperationException

. Subclasses can change this
behavior as long as the contract of

FileObject

is
obeyed.

**Specified by:** openOutputStream

in interface

FileObject
**Returns:** an OutputStream
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

Wraps the result of

getCharContent(boolean)

in a Reader.
Subclasses can change this behavior as long as the contract of

FileObject

is obeyed.

**Specified by:** openReader

in interface

FileObject
**Parameters:** ignoreEncodingErrors

- ignore encoding errors if true
**Returns:** a Reader wrapping the result of getCharContent
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

This implementation always throws

UnsupportedOperationException

. Subclasses can change this
behavior as long as the contract of

FileObject

is
obeyed.

**Specified by:** getCharContent

in interface

FileObject
**Parameters:** ignoreEncodingErrors

- ignore encoding errors if true
**Returns:** a CharSequence if available;

null

otherwise
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

Wraps the result of openOutputStream in a Writer. Subclasses
can change this behavior as long as the contract of

FileObject

is obeyed.

**Specified by:** openWriter

in interface

FileObject
**Returns:** a Writer wrapping the result of openOutputStream
**Throws:** IllegalStateException

- if this file object was
opened for reading and does not support writing
**Throws:** UnsupportedOperationException

- if this kind of
file object does not support character access
**Throws:** IOException

- if an I/O error occurred

- getLastModified

```java
public long getLastModified()
```

This implementation returns

0L

. Subclasses can change
this behavior as long as the contract of

FileObject

is
obeyed.

**Specified by:** getLastModified

in interface

FileObject
**Returns:** 0L

- delete

```java
public boolean delete()
```

This implementation does nothing. Subclasses can change this
behavior as long as the contract of

FileObject

is
obeyed.

**Specified by:** delete

in interface

FileObject
**Returns:** false

- getKind

```java
public
JavaFileObject.Kind
getKind()
```

Description copied from interface:

JavaFileObject

Returns the kind of this file object.

**Specified by:** getKind

in interface

JavaFileObject
**Returns:** this.kind

- isNameCompatible

```java
public boolean isNameCompatible​(
String
simpleName,

JavaFileObject.Kind
kind)
```

This implementation compares the path of its URI to the given
simple name. This method returns true if the given kind is
equal to the kind of this object, and if the path is equal to

simpleName + kind.extension

or if it ends with

"/" + simpleName + kind.extension

.

This method calls

getKind()

and

FileObject.toUri()

and
does not access the fields

uri

and

kind

directly.

Subclasses can change this behavior as long as the contract
of

JavaFileObject

is obeyed.

**Specified by:** isNameCompatible

in interface

JavaFileObject
**Parameters:** simpleName

- a simple name of a class
**Parameters:** kind

- a kind
**Returns:** true

if this file object is compatible; false
otherwise

- getNestingKind

```java
public
NestingKind
getNestingKind()
```

This implementation returns

null

. Subclasses can
change this behavior as long as the contract of

JavaFileObject

is obeyed.

**Specified by:** getNestingKind

in interface

JavaFileObject
**Returns:** the nesting kind, or

null

if the nesting kind
is not known

- getAccessLevel

```java
public
Modifier
getAccessLevel()
```

This implementation returns

null

. Subclasses can
change this behavior as long as the contract of

JavaFileObject

is obeyed.

**Specified by:** getAccessLevel

in interface

JavaFileObject
**Returns:** the access level

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

This implementation always throws

UnsupportedOperationException

. Subclasses can change this
behavior as long as the contract of

FileObject

is
obeyed.

**Specified by:** openInputStream

in interface

FileObject
**Returns:** an InputStream
**Throws:** IOException

- if an I/O error occurred

---

#### openInputStream

public

InputStream

openInputStream()
throws

IOException

This implementation always throws

UnsupportedOperationException

. Subclasses can change this
behavior as long as the contract of

FileObject

is
obeyed.

openOutputStream

```java
public
OutputStream
openOutputStream()
throws
IOException
```

This implementation always throws

UnsupportedOperationException

. Subclasses can change this
behavior as long as the contract of

FileObject

is
obeyed.

**Specified by:** openOutputStream

in interface

FileObject
**Returns:** an OutputStream
**Throws:** IOException

- if an I/O error occurred

---

#### openOutputStream

public

OutputStream

openOutputStream()
throws

IOException

This implementation always throws

UnsupportedOperationException

. Subclasses can change this
behavior as long as the contract of

FileObject

is
obeyed.

openReader

```java
public
Reader
openReader​(boolean ignoreEncodingErrors)
throws
IOException
```

Wraps the result of

getCharContent(boolean)

in a Reader.
Subclasses can change this behavior as long as the contract of

FileObject

is obeyed.

**Specified by:** openReader

in interface

FileObject
**Parameters:** ignoreEncodingErrors

- ignore encoding errors if true
**Returns:** a Reader wrapping the result of getCharContent
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

Wraps the result of

getCharContent(boolean)

in a Reader.
Subclasses can change this behavior as long as the contract of

FileObject

is obeyed.

getCharContent

```java
public
CharSequence
getCharContent​(boolean ignoreEncodingErrors)
throws
IOException
```

This implementation always throws

UnsupportedOperationException

. Subclasses can change this
behavior as long as the contract of

FileObject

is
obeyed.

**Specified by:** getCharContent

in interface

FileObject
**Parameters:** ignoreEncodingErrors

- ignore encoding errors if true
**Returns:** a CharSequence if available;

null

otherwise
**Throws:** IOException

- if an I/O error occurred

---

#### getCharContent

public

CharSequence

getCharContent​(boolean ignoreEncodingErrors)
throws

IOException

This implementation always throws

UnsupportedOperationException

. Subclasses can change this
behavior as long as the contract of

FileObject

is
obeyed.

openWriter

```java
public
Writer
openWriter()
throws
IOException
```

Wraps the result of openOutputStream in a Writer. Subclasses
can change this behavior as long as the contract of

FileObject

is obeyed.

**Specified by:** openWriter

in interface

FileObject
**Returns:** a Writer wrapping the result of openOutputStream
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

Wraps the result of openOutputStream in a Writer. Subclasses
can change this behavior as long as the contract of

FileObject

is obeyed.

getLastModified

```java
public long getLastModified()
```

This implementation returns

0L

. Subclasses can change
this behavior as long as the contract of

FileObject

is
obeyed.

**Specified by:** getLastModified

in interface

FileObject
**Returns:** 0L

---

#### getLastModified

public long getLastModified()

This implementation returns

0L

. Subclasses can change
this behavior as long as the contract of

FileObject

is
obeyed.

delete

```java
public boolean delete()
```

This implementation does nothing. Subclasses can change this
behavior as long as the contract of

FileObject

is
obeyed.

**Specified by:** delete

in interface

FileObject
**Returns:** false

---

#### delete

public boolean delete()

This implementation does nothing. Subclasses can change this
behavior as long as the contract of

FileObject

is
obeyed.

getKind

```java
public
JavaFileObject.Kind
getKind()
```

Description copied from interface:

JavaFileObject

Returns the kind of this file object.

**Specified by:** getKind

in interface

JavaFileObject
**Returns:** this.kind

---

#### getKind

public

JavaFileObject.Kind

getKind()

Description copied from interface:

JavaFileObject

Returns the kind of this file object.

isNameCompatible

```java
public boolean isNameCompatible​(
String
simpleName,

JavaFileObject.Kind
kind)
```

This implementation compares the path of its URI to the given
simple name. This method returns true if the given kind is
equal to the kind of this object, and if the path is equal to

simpleName + kind.extension

or if it ends with

"/" + simpleName + kind.extension

.

This method calls

getKind()

and

FileObject.toUri()

and
does not access the fields

uri

and

kind

directly.

Subclasses can change this behavior as long as the contract
of

JavaFileObject

is obeyed.

**Specified by:** isNameCompatible

in interface

JavaFileObject
**Parameters:** simpleName

- a simple name of a class
**Parameters:** kind

- a kind
**Returns:** true

if this file object is compatible; false
otherwise

---

#### isNameCompatible

public boolean isNameCompatible​(

String

simpleName,

JavaFileObject.Kind

kind)

This implementation compares the path of its URI to the given
simple name. This method returns true if the given kind is
equal to the kind of this object, and if the path is equal to

simpleName + kind.extension

or if it ends with

"/" + simpleName + kind.extension

.

This method calls

getKind()

and

FileObject.toUri()

and
does not access the fields

uri

and

kind

directly.

Subclasses can change this behavior as long as the contract
of

JavaFileObject

is obeyed.

This method calls

getKind()

and

FileObject.toUri()

and
does not access the fields

uri

and

kind

directly.

Subclasses can change this behavior as long as the contract
of

JavaFileObject

is obeyed.

Subclasses can change this behavior as long as the contract
of

JavaFileObject

is obeyed.

getNestingKind

```java
public
NestingKind
getNestingKind()
```

This implementation returns

null

. Subclasses can
change this behavior as long as the contract of

JavaFileObject

is obeyed.

**Specified by:** getNestingKind

in interface

JavaFileObject
**Returns:** the nesting kind, or

null

if the nesting kind
is not known

---

#### getNestingKind

public

NestingKind

getNestingKind()

This implementation returns

null

. Subclasses can
change this behavior as long as the contract of

JavaFileObject

is obeyed.

getAccessLevel

```java
public
Modifier
getAccessLevel()
```

This implementation returns

null

. Subclasses can
change this behavior as long as the contract of

JavaFileObject

is obeyed.

**Specified by:** getAccessLevel

in interface

JavaFileObject
**Returns:** the access level

---

#### getAccessLevel

public

Modifier

getAccessLevel()

This implementation returns

null

. Subclasses can
change this behavior as long as the contract of

JavaFileObject

is obeyed.

---

