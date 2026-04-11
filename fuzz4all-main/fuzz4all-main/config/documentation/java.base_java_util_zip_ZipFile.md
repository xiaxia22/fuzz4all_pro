# Class ZipFile

**Source:** `java.base\java\util\zip\ZipFile.html`

### Class Description

```java
public class
ZipFile

extends
Object

implements
Closeable
```

This class is used to read entries from a zip file.

Unless otherwise noted, passing a

null

argument to a constructor
or method in this class will cause a

NullPointerException

to be
thrown.

**All Implemented Interfaces:** Closeable

,

AutoCloseable

---

### Field Details

#### public static final int OPEN_READ

Mode flag to open a zip file for reading.

**See Also:**
- Constant Field Values

---

#### public static final int OPEN_DELETE

Mode flag to open a zip file and mark it for deletion. The file will be
deleted some time between the moment that it is opened and the moment
that it is closed, but its contents will remain accessible via the

ZipFile

object until either the close method is invoked or the
virtual machine exits.

**See Also:**
- Constant Field Values

---

#### public static final long LOCSIG

**See Also:**
- Constant Field Values

---

#### public static final long EXTSIG

**See Also:**
- Constant Field Values

---

#### public static final long CENSIG

**See Also:**
- Constant Field Values

---

#### public static final long ENDSIG

**See Also:**
- Constant Field Values

---

#### public static final int LOCHDR

**See Also:**
- Constant Field Values

---

#### public static final int EXTHDR

**See Also:**
- Constant Field Values

---

#### public static final int CENHDR

**See Also:**
- Constant Field Values

---

#### public static final int ENDHDR

**See Also:**
- Constant Field Values

---

#### public static final int LOCVER

**See Also:**
- Constant Field Values

---

#### public static final int LOCFLG

**See Also:**
- Constant Field Values

---

#### public static final int LOCHOW

**See Also:**
- Constant Field Values

---

#### public static final int LOCTIM

**See Also:**
- Constant Field Values

---

#### public static final int LOCCRC

**See Also:**
- Constant Field Values

---

#### public static final int LOCSIZ

**See Also:**
- Constant Field Values

---

#### public static final int LOCLEN

**See Also:**
- Constant Field Values

---

#### public static final int LOCNAM

**See Also:**
- Constant Field Values

---

#### public static final int LOCEXT

**See Also:**
- Constant Field Values

---

#### public static final int EXTCRC

**See Also:**
- Constant Field Values

---

#### public static final int EXTSIZ

**See Also:**
- Constant Field Values

---

#### public static final int EXTLEN

**See Also:**
- Constant Field Values

---

#### public static final int CENVEM

**See Also:**
- Constant Field Values

---

#### public static final int CENVER

**See Also:**
- Constant Field Values

---

#### public static final int CENFLG

**See Also:**
- Constant Field Values

---

#### public static final int CENHOW

**See Also:**
- Constant Field Values

---

#### public static final int CENTIM

**See Also:**
- Constant Field Values

---

#### public static final int CENCRC

**See Also:**
- Constant Field Values

---

#### public static final int CENSIZ

**See Also:**
- Constant Field Values

---

#### public static final int CENLEN

**See Also:**
- Constant Field Values

---

#### public static final int CENNAM

**See Also:**
- Constant Field Values

---

#### public static final int CENEXT

**See Also:**
- Constant Field Values

---

#### public static final int CENCOM

**See Also:**
- Constant Field Values

---

#### public static final int CENDSK

**See Also:**
- Constant Field Values

---

#### public static final int CENATT

**See Also:**
- Constant Field Values

---

#### public static final int CENATX

**See Also:**
- Constant Field Values

---

#### public static final int CENOFF

**See Also:**
- Constant Field Values

---

#### public static final int ENDSUB

**See Also:**
- Constant Field Values

---

#### public static final int ENDTOT

**See Also:**
- Constant Field Values

---

#### public static final int ENDSIZ

**See Also:**
- Constant Field Values

---

#### public static final int ENDOFF

**See Also:**
- Constant Field Values

---

#### public static final int ENDCOM

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public ZipFile​(
String
name)
throws
IOException

Opens a zip file for reading.

First, if there is a security manager, its

checkRead

method is called with the

name

argument as its argument
to ensure the read is allowed.

The UTF-8

charset

is used to
decode the entry names and comments.

**Parameters:**
- name

- the name of the zip file

**Throws:**
- ZipException

- if a ZIP format error has occurred
- IOException

- if an I/O error has occurred
- SecurityException

- if a security manager exists and its

checkRead

method doesn't allow read access to the file.

**See Also:**
- SecurityManager.checkRead(java.lang.String)

---

#### public ZipFile​(
File
file,
int mode)
throws
IOException

Opens a new

ZipFile

to read from the specified

File

object in the specified mode. The mode argument
must be either

OPEN_READ

or

OPEN_READ | OPEN_DELETE

.

First, if there is a security manager, its

checkRead

method is called with the

name

argument as its argument to
ensure the read is allowed.

The UTF-8

charset

is used to
decode the entry names and comments

**Parameters:**
- file

- the ZIP file to be opened for reading
- mode

- the mode in which the file is to be opened

**Throws:**
- ZipException

- if a ZIP format error has occurred
- IOException

- if an I/O error has occurred
- SecurityException

- if a security manager exists and
its

checkRead

method
doesn't allow read access to the file,
or its

checkDelete

method doesn't allow deleting
the file when the

OPEN_DELETE

flag is set.
- IllegalArgumentException

- if the

mode

argument is invalid

**See Also:**
- SecurityManager.checkRead(java.lang.String)

**Since:**
- 1.3

---

#### public ZipFile​(
File
file)
throws
ZipException
,

IOException

Opens a ZIP file for reading given the specified File object.

The UTF-8

charset

is used to
decode the entry names and comments.

**Parameters:**
- file

- the ZIP file to be opened for reading

**Throws:**
- ZipException

- if a ZIP format error has occurred
- IOException

- if an I/O error has occurred

---

#### public ZipFile​(
File
file,
int mode,

Charset
charset)
throws
IOException

Opens a new

ZipFile

to read from the specified

File

object in the specified mode. The mode argument
must be either

OPEN_READ

or

OPEN_READ | OPEN_DELETE

.

First, if there is a security manager, its

checkRead

method is called with the

name

argument as its argument to
ensure the read is allowed.

**Parameters:**
- file

- the ZIP file to be opened for reading
- mode

- the mode in which the file is to be opened
- charset

- the

charset

to
be used to decode the ZIP entry name and comment that are not
encoded by using UTF-8 encoding (indicated by entry's general
purpose flag).

**Throws:**
- ZipException

- if a ZIP format error has occurred
- IOException

- if an I/O error has occurred
- SecurityException

- if a security manager exists and its

checkRead

method doesn't allow read access to the file,or its

checkDelete

method doesn't allow deleting the
file when the

OPEN_DELETE

flag is set
- IllegalArgumentException

- if the

mode

argument is invalid

**See Also:**
- SecurityManager.checkRead(java.lang.String)

**Since:**
- 1.7

---

#### public ZipFile​(
String
name,

Charset
charset)
throws
IOException

Opens a zip file for reading.

First, if there is a security manager, its

checkRead

method is called with the

name

argument as its argument
to ensure the read is allowed.

**Parameters:**
- name

- the name of the zip file
- charset

- the

charset

to
be used to decode the ZIP entry name and comment that are not
encoded by using UTF-8 encoding (indicated by entry's general
purpose flag).

**Throws:**
- ZipException

- if a ZIP format error has occurred
- IOException

- if an I/O error has occurred
- SecurityException

- if a security manager exists and its

checkRead

method doesn't allow read access to the file

**See Also:**
- SecurityManager.checkRead(java.lang.String)

**Since:**
- 1.7

---

#### public ZipFile​(
File
file,

Charset
charset)
throws
IOException

Opens a ZIP file for reading given the specified File object.

**Parameters:**
- file

- the ZIP file to be opened for reading
- charset

- The

charset

to be
used to decode the ZIP entry name and comment (ignored if
the

language
encoding bit

of the ZIP entry's general purpose bit
flag is set).

**Throws:**
- ZipException

- if a ZIP format error has occurred
- IOException

- if an I/O error has occurred

**Since:**
- 1.7

---

### Method Details

#### public
String
getComment()

Returns the zip file comment, or null if none.

**Returns:**
- the comment string for the zip file, or null if none

**Throws:**
- IllegalStateException

- if the zip file has been closed

**Since:**
- 1.7

---

#### public
ZipEntry
getEntry​(
String
name)

Returns the zip file entry for the specified name, or null
if not found.

**Parameters:**
- name

- the name of the entry

**Returns:**
- the zip file entry, or null if not found

**Throws:**
- IllegalStateException

- if the zip file has been closed

---

#### public
InputStream
getInputStream​(
ZipEntry
entry)
throws
IOException

Returns an input stream for reading the contents of the specified
zip file entry.

Closing this ZIP file will, in turn, close all input streams that
have been returned by invocations of this method.

**Parameters:**
- entry

- the zip file entry

**Returns:**
- the input stream for reading the contents of the specified
zip file entry.

**Throws:**
- ZipException

- if a ZIP format error has occurred
- IOException

- if an I/O error has occurred
- IllegalStateException

- if the zip file has been closed

---

#### public
String
getName()

Returns the path name of the ZIP file.

**Returns:**
- the path name of the ZIP file

---

#### public
Enumeration
<? extends
ZipEntry
> entries()

Returns an enumeration of the ZIP file entries.

**Returns:**
- an enumeration of the ZIP file entries

**Throws:**
- IllegalStateException

- if the zip file has been closed

---

#### public
Stream
<? extends
ZipEntry
> stream()

Returns an ordered

Stream

over the ZIP file entries.

Entries appear in the

Stream

in the order they appear in
the central directory of the ZIP file.

**Returns:**
- an ordered

Stream

of entries in this ZIP file

**Throws:**
- IllegalStateException

- if the zip file has been closed

**Since:**
- 1.8

---

#### public int size()

Returns the number of entries in the ZIP file.

**Returns:**
- the number of entries in the ZIP file

**Throws:**
- IllegalStateException

- if the zip file has been closed

---

#### public void close()
throws
IOException

Closes the ZIP file.

Closing this ZIP file will close all of the input streams
previously returned by invocations of the

getInputStream

method.

**Specified by:**
- close

in interface

AutoCloseable
- close

in interface

Closeable

**Throws:**
- IOException

- if an I/O error has occurred

---

#### @Deprecated
(
since
="9",

forRemoval
=true)
protected void finalize()
throws
IOException

Ensures that the system resources held by this ZipFile object are
released when there are no more references to it.

**Overrides:**
- finalize

in class

Object

**Throws:**
- IOException

- if an I/O error has occurred

**See Also:**
- WeakReference

,

PhantomReference

---

### Additional Sections

#### Class ZipFile

java.lang.Object

- java.util.zip.ZipFile

java.util.zip.ZipFile

**All Implemented Interfaces:** Closeable

,

AutoCloseable

**Direct Known Subclasses:** JarFile

```java
public class
ZipFile

extends
Object

implements
Closeable
```

This class is used to read entries from a zip file.

Unless otherwise noted, passing a

null

argument to a constructor
or method in this class will cause a

NullPointerException

to be
thrown.

**API Note:** To release resources used by this

ZipFile

, the

close()

method
should be called explicitly or by try-with-resources. Subclasses are responsible
for the cleanup of resources acquired by the subclass. Subclasses that override

finalize()

in order to perform cleanup should be modified to use alternative
cleanup mechanisms such as

Cleaner

and remove the overriding

finalize

method.
**Implementation Requirements:** If this

ZipFile

has been subclassed and the

close

method has
been overridden, the

close

method will be called by the finalization
when

ZipFile

is unreachable. But the subclasses should not depend on
this specific implementation; the finalization is not reliable and the

finalize

method is deprecated to be removed.
**Since:** 1.1

public class

ZipFile

extends

Object

implements

Closeable

This class is used to read entries from a zip file.

Unless otherwise noted, passing a

null

argument to a constructor
or method in this class will cause a

NullPointerException

to be
thrown.

Unless otherwise noted, passing a

null

argument to a constructor
or method in this class will cause a

NullPointerException

to be
thrown.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

CENATT

static int

CENATX

static int

CENCOM

static int

CENCRC

static int

CENDSK

static int

CENEXT

static int

CENFLG

static int

CENHDR

static int

CENHOW

static int

CENLEN

static int

CENNAM

static int

CENOFF

static long

CENSIG

static int

CENSIZ

static int

CENTIM

static int

CENVEM

static int

CENVER

static int

ENDCOM

static int

ENDHDR

static int

ENDOFF

static long

ENDSIG

static int

ENDSIZ

static int

ENDSUB

static int

ENDTOT

static int

EXTCRC

static int

EXTHDR

static int

EXTLEN

static long

EXTSIG

static int

EXTSIZ

static int

LOCCRC

static int

LOCEXT

static int

LOCFLG

static int

LOCHDR

static int

LOCHOW

static int

LOCLEN

static int

LOCNAM

static long

LOCSIG

static int

LOCSIZ

static int

LOCTIM

static int

LOCVER

static int

OPEN_DELETE

Mode flag to open a zip file and mark it for deletion.

static int

OPEN_READ

Mode flag to open a zip file for reading.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ZipFile

​(

File

file)

Opens a ZIP file for reading given the specified File object.

ZipFile

​(

File

file,
int mode)

Opens a new

ZipFile

to read from the specified

File

object in the specified mode.

ZipFile

​(

File

file,
int mode,

Charset

charset)

Opens a new

ZipFile

to read from the specified

File

object in the specified mode.

ZipFile

​(

File

file,

Charset

charset)

Opens a ZIP file for reading given the specified File object.

ZipFile

​(

String

name)

Opens a zip file for reading.

ZipFile

​(

String

name,

Charset

charset)

Opens a zip file for reading.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

void

close

()

Closes the ZIP file.

Enumeration

<? extends

ZipEntry

>

entries

()

Returns an enumeration of the ZIP file entries.

protected void

finalize

()

Deprecated, for removal: This API element is subject to removal in a future version.

The

finalize

method has been deprecated and will be
removed.

String

getComment

()

Returns the zip file comment, or null if none.

ZipEntry

getEntry

​(

String

name)

Returns the zip file entry for the specified name, or null
if not found.

InputStream

getInputStream

​(

ZipEntry

entry)

Returns an input stream for reading the contents of the specified
zip file entry.

String

getName

()

Returns the path name of the ZIP file.

int

size

()

Returns the number of entries in the ZIP file.

Stream

<? extends

ZipEntry

>

stream

()

Returns an ordered

Stream

over the ZIP file entries.

- Methods declared in class java.lang.

Object

clone

,

equals

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

static int

CENATT

static int

CENATX

static int

CENCOM

static int

CENCRC

static int

CENDSK

static int

CENEXT

static int

CENFLG

static int

CENHDR

static int

CENHOW

static int

CENLEN

static int

CENNAM

static int

CENOFF

static long

CENSIG

static int

CENSIZ

static int

CENTIM

static int

CENVEM

static int

CENVER

static int

ENDCOM

static int

ENDHDR

static int

ENDOFF

static long

ENDSIG

static int

ENDSIZ

static int

ENDSUB

static int

ENDTOT

static int

EXTCRC

static int

EXTHDR

static int

EXTLEN

static long

EXTSIG

static int

EXTSIZ

static int

LOCCRC

static int

LOCEXT

static int

LOCFLG

static int

LOCHDR

static int

LOCHOW

static int

LOCLEN

static int

LOCNAM

static long

LOCSIG

static int

LOCSIZ

static int

LOCTIM

static int

LOCVER

static int

OPEN_DELETE

Mode flag to open a zip file and mark it for deletion.

static int

OPEN_READ

Mode flag to open a zip file for reading.

---

#### Field Summary

Mode flag to open a zip file and mark it for deletion.

Mode flag to open a zip file for reading.

Constructor Summary

Constructors

Constructor

Description

ZipFile

​(

File

file)

Opens a ZIP file for reading given the specified File object.

ZipFile

​(

File

file,
int mode)

Opens a new

ZipFile

to read from the specified

File

object in the specified mode.

ZipFile

​(

File

file,
int mode,

Charset

charset)

Opens a new

ZipFile

to read from the specified

File

object in the specified mode.

ZipFile

​(

File

file,

Charset

charset)

Opens a ZIP file for reading given the specified File object.

ZipFile

​(

String

name)

Opens a zip file for reading.

ZipFile

​(

String

name,

Charset

charset)

Opens a zip file for reading.

---

#### Constructor Summary

Opens a ZIP file for reading given the specified File object.

Opens a new

ZipFile

to read from the specified

File

object in the specified mode.

Opens a zip file for reading.

Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

void

close

()

Closes the ZIP file.

Enumeration

<? extends

ZipEntry

>

entries

()

Returns an enumeration of the ZIP file entries.

protected void

finalize

()

Deprecated, for removal: This API element is subject to removal in a future version.

The

finalize

method has been deprecated and will be
removed.

String

getComment

()

Returns the zip file comment, or null if none.

ZipEntry

getEntry

​(

String

name)

Returns the zip file entry for the specified name, or null
if not found.

InputStream

getInputStream

​(

ZipEntry

entry)

Returns an input stream for reading the contents of the specified
zip file entry.

String

getName

()

Returns the path name of the ZIP file.

int

size

()

Returns the number of entries in the ZIP file.

Stream

<? extends

ZipEntry

>

stream

()

Returns an ordered

Stream

over the ZIP file entries.

- Methods declared in class java.lang.

Object

clone

,

equals

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

Closes the ZIP file.

Returns an enumeration of the ZIP file entries.

Deprecated, for removal: This API element is subject to removal in a future version.

The

finalize

method has been deprecated and will be
removed.

Returns the zip file comment, or null if none.

Returns the zip file entry for the specified name, or null
if not found.

Returns an input stream for reading the contents of the specified
zip file entry.

Returns the path name of the ZIP file.

Returns the number of entries in the ZIP file.

Returns an ordered

Stream

over the ZIP file entries.

Methods declared in class java.lang.

Object

clone

,

equals

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

- OPEN_READ

```java
public static final int OPEN_READ
```

Mode flag to open a zip file for reading.

**See Also:** Constant Field Values

- OPEN_DELETE

```java
public static final int OPEN_DELETE
```

Mode flag to open a zip file and mark it for deletion. The file will be
deleted some time between the moment that it is opened and the moment
that it is closed, but its contents will remain accessible via the

ZipFile

object until either the close method is invoked or the
virtual machine exits.

**See Also:** Constant Field Values

- LOCSIG

```java
public static final long LOCSIG
```

**See Also:** Constant Field Values

- EXTSIG

```java
public static final long EXTSIG
```

**See Also:** Constant Field Values

- CENSIG

```java
public static final long CENSIG
```

**See Also:** Constant Field Values

- ENDSIG

```java
public static final long ENDSIG
```

**See Also:** Constant Field Values

- LOCHDR

```java
public static final int LOCHDR
```

**See Also:** Constant Field Values

- EXTHDR

```java
public static final int EXTHDR
```

**See Also:** Constant Field Values

- CENHDR

```java
public static final int CENHDR
```

**See Also:** Constant Field Values

- ENDHDR

```java
public static final int ENDHDR
```

**See Also:** Constant Field Values

- LOCVER

```java
public static final int LOCVER
```

**See Also:** Constant Field Values

- LOCFLG

```java
public static final int LOCFLG
```

**See Also:** Constant Field Values

- LOCHOW

```java
public static final int LOCHOW
```

**See Also:** Constant Field Values

- LOCTIM

```java
public static final int LOCTIM
```

**See Also:** Constant Field Values

- LOCCRC

```java
public static final int LOCCRC
```

**See Also:** Constant Field Values

- LOCSIZ

```java
public static final int LOCSIZ
```

**See Also:** Constant Field Values

- LOCLEN

```java
public static final int LOCLEN
```

**See Also:** Constant Field Values

- LOCNAM

```java
public static final int LOCNAM
```

**See Also:** Constant Field Values

- LOCEXT

```java
public static final int LOCEXT
```

**See Also:** Constant Field Values

- EXTCRC

```java
public static final int EXTCRC
```

**See Also:** Constant Field Values

- EXTSIZ

```java
public static final int EXTSIZ
```

**See Also:** Constant Field Values

- EXTLEN

```java
public static final int EXTLEN
```

**See Also:** Constant Field Values

- CENVEM

```java
public static final int CENVEM
```

**See Also:** Constant Field Values

- CENVER

```java
public static final int CENVER
```

**See Also:** Constant Field Values

- CENFLG

```java
public static final int CENFLG
```

**See Also:** Constant Field Values

- CENHOW

```java
public static final int CENHOW
```

**See Also:** Constant Field Values

- CENTIM

```java
public static final int CENTIM
```

**See Also:** Constant Field Values

- CENCRC

```java
public static final int CENCRC
```

**See Also:** Constant Field Values

- CENSIZ

```java
public static final int CENSIZ
```

**See Also:** Constant Field Values

- CENLEN

```java
public static final int CENLEN
```

**See Also:** Constant Field Values

- CENNAM

```java
public static final int CENNAM
```

**See Also:** Constant Field Values

- CENEXT

```java
public static final int CENEXT
```

**See Also:** Constant Field Values

- CENCOM

```java
public static final int CENCOM
```

**See Also:** Constant Field Values

- CENDSK

```java
public static final int CENDSK
```

**See Also:** Constant Field Values

- CENATT

```java
public static final int CENATT
```

**See Also:** Constant Field Values

- CENATX

```java
public static final int CENATX
```

**See Also:** Constant Field Values

- CENOFF

```java
public static final int CENOFF
```

**See Also:** Constant Field Values

- ENDSUB

```java
public static final int ENDSUB
```

**See Also:** Constant Field Values

- ENDTOT

```java
public static final int ENDTOT
```

**See Also:** Constant Field Values

- ENDSIZ

```java
public static final int ENDSIZ
```

**See Also:** Constant Field Values

- ENDOFF

```java
public static final int ENDOFF
```

**See Also:** Constant Field Values

- ENDCOM

```java
public static final int ENDCOM
```

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ZipFile

```java
public ZipFile​(
String
name)
throws
IOException
```

Opens a zip file for reading.

First, if there is a security manager, its

checkRead

method is called with the

name

argument as its argument
to ensure the read is allowed.

The UTF-8

charset

is used to
decode the entry names and comments.

**Parameters:** name

- the name of the zip file
**Throws:** ZipException

- if a ZIP format error has occurred
**Throws:** IOException

- if an I/O error has occurred
**Throws:** SecurityException

- if a security manager exists and its

checkRead

method doesn't allow read access to the file.
**See Also:** SecurityManager.checkRead(java.lang.String)

- ZipFile

```java
public ZipFile​(
File
file,
int mode)
throws
IOException
```

Opens a new

ZipFile

to read from the specified

File

object in the specified mode. The mode argument
must be either

OPEN_READ

or

OPEN_READ | OPEN_DELETE

.

First, if there is a security manager, its

checkRead

method is called with the

name

argument as its argument to
ensure the read is allowed.

The UTF-8

charset

is used to
decode the entry names and comments

**Parameters:** file

- the ZIP file to be opened for reading
**Parameters:** mode

- the mode in which the file is to be opened
**Throws:** ZipException

- if a ZIP format error has occurred
**Throws:** IOException

- if an I/O error has occurred
**Throws:** SecurityException

- if a security manager exists and
its

checkRead

method
doesn't allow read access to the file,
or its

checkDelete

method doesn't allow deleting
the file when the

OPEN_DELETE

flag is set.
**Throws:** IllegalArgumentException

- if the

mode

argument is invalid
**Since:** 1.3
**See Also:** SecurityManager.checkRead(java.lang.String)

- ZipFile

```java
public ZipFile​(
File
file)
throws
ZipException
,

IOException
```

Opens a ZIP file for reading given the specified File object.

The UTF-8

charset

is used to
decode the entry names and comments.

**Parameters:** file

- the ZIP file to be opened for reading
**Throws:** ZipException

- if a ZIP format error has occurred
**Throws:** IOException

- if an I/O error has occurred

- ZipFile

```java
public ZipFile​(
File
file,
int mode,

Charset
charset)
throws
IOException
```

Opens a new

ZipFile

to read from the specified

File

object in the specified mode. The mode argument
must be either

OPEN_READ

or

OPEN_READ | OPEN_DELETE

.

First, if there is a security manager, its

checkRead

method is called with the

name

argument as its argument to
ensure the read is allowed.

**Parameters:** file

- the ZIP file to be opened for reading
**Parameters:** mode

- the mode in which the file is to be opened
**Parameters:** charset

- the

charset

to
be used to decode the ZIP entry name and comment that are not
encoded by using UTF-8 encoding (indicated by entry's general
purpose flag).
**Throws:** ZipException

- if a ZIP format error has occurred
**Throws:** IOException

- if an I/O error has occurred
**Throws:** SecurityException

- if a security manager exists and its

checkRead

method doesn't allow read access to the file,or its

checkDelete

method doesn't allow deleting the
file when the

OPEN_DELETE

flag is set
**Throws:** IllegalArgumentException

- if the

mode

argument is invalid
**Since:** 1.7
**See Also:** SecurityManager.checkRead(java.lang.String)

- ZipFile

```java
public ZipFile​(
String
name,

Charset
charset)
throws
IOException
```

Opens a zip file for reading.

First, if there is a security manager, its

checkRead

method is called with the

name

argument as its argument
to ensure the read is allowed.

**Parameters:** name

- the name of the zip file
**Parameters:** charset

- the

charset

to
be used to decode the ZIP entry name and comment that are not
encoded by using UTF-8 encoding (indicated by entry's general
purpose flag).
**Throws:** ZipException

- if a ZIP format error has occurred
**Throws:** IOException

- if an I/O error has occurred
**Throws:** SecurityException

- if a security manager exists and its

checkRead

method doesn't allow read access to the file
**Since:** 1.7
**See Also:** SecurityManager.checkRead(java.lang.String)

- ZipFile

```java
public ZipFile​(
File
file,

Charset
charset)
throws
IOException
```

Opens a ZIP file for reading given the specified File object.

**Parameters:** file

- the ZIP file to be opened for reading
**Parameters:** charset

- The

charset

to be
used to decode the ZIP entry name and comment (ignored if
the

language
encoding bit

of the ZIP entry's general purpose bit
flag is set).
**Throws:** ZipException

- if a ZIP format error has occurred
**Throws:** IOException

- if an I/O error has occurred
**Since:** 1.7

============ METHOD DETAIL ==========

- Method Detail

- getComment

```java
public
String
getComment()
```

Returns the zip file comment, or null if none.

**Returns:** the comment string for the zip file, or null if none
**Throws:** IllegalStateException

- if the zip file has been closed
**Since:** 1.7

- getEntry

```java
public
ZipEntry
getEntry​(
String
name)
```

Returns the zip file entry for the specified name, or null
if not found.

**Parameters:** name

- the name of the entry
**Returns:** the zip file entry, or null if not found
**Throws:** IllegalStateException

- if the zip file has been closed

- getInputStream

```java
public
InputStream
getInputStream​(
ZipEntry
entry)
throws
IOException
```

Returns an input stream for reading the contents of the specified
zip file entry.

Closing this ZIP file will, in turn, close all input streams that
have been returned by invocations of this method.

**Parameters:** entry

- the zip file entry
**Returns:** the input stream for reading the contents of the specified
zip file entry.
**Throws:** ZipException

- if a ZIP format error has occurred
**Throws:** IOException

- if an I/O error has occurred
**Throws:** IllegalStateException

- if the zip file has been closed

- getName

```java
public
String
getName()
```

Returns the path name of the ZIP file.

**Returns:** the path name of the ZIP file

- entries

```java
public
Enumeration
<? extends
ZipEntry
> entries()
```

Returns an enumeration of the ZIP file entries.

**Returns:** an enumeration of the ZIP file entries
**Throws:** IllegalStateException

- if the zip file has been closed

- stream

```java
public
Stream
<? extends
ZipEntry
> stream()
```

Returns an ordered

Stream

over the ZIP file entries.

Entries appear in the

Stream

in the order they appear in
the central directory of the ZIP file.

**Returns:** an ordered

Stream

of entries in this ZIP file
**Throws:** IllegalStateException

- if the zip file has been closed
**Since:** 1.8

- size

```java
public int size()
```

Returns the number of entries in the ZIP file.

**Returns:** the number of entries in the ZIP file
**Throws:** IllegalStateException

- if the zip file has been closed

- close

```java
public void close()
throws
IOException
```

Closes the ZIP file.

Closing this ZIP file will close all of the input streams
previously returned by invocations of the

getInputStream

method.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Throws:** IOException

- if an I/O error has occurred

- finalize

```java
@Deprecated
(
since
="9",

forRemoval
=true)
protected void finalize()
throws
IOException
```

Deprecated, for removal: This API element is subject to removal in a future version.

The

finalize

method has been deprecated and will be
removed. It is implemented as a no-op. Subclasses that override

finalize

in order to perform cleanup should be modified to
use alternative cleanup mechanisms and to remove the overriding

finalize

method. The recommended cleanup for ZipFile object
is to explicitly invoke

close

method when it is no longer in
use, or use try-with-resources. If the

close

is not invoked
explicitly the resources held by this object will be released when
the instance becomes unreachable.

Ensures that the system resources held by this ZipFile object are
released when there are no more references to it.

**Overrides:** finalize

in class

Object
**Throws:** IOException

- if an I/O error has occurred
**See Also:** WeakReference

,

PhantomReference

Field Detail

- OPEN_READ

```java
public static final int OPEN_READ
```

Mode flag to open a zip file for reading.

**See Also:** Constant Field Values

- OPEN_DELETE

```java
public static final int OPEN_DELETE
```

Mode flag to open a zip file and mark it for deletion. The file will be
deleted some time between the moment that it is opened and the moment
that it is closed, but its contents will remain accessible via the

ZipFile

object until either the close method is invoked or the
virtual machine exits.

**See Also:** Constant Field Values

- LOCSIG

```java
public static final long LOCSIG
```

**See Also:** Constant Field Values

- EXTSIG

```java
public static final long EXTSIG
```

**See Also:** Constant Field Values

- CENSIG

```java
public static final long CENSIG
```

**See Also:** Constant Field Values

- ENDSIG

```java
public static final long ENDSIG
```

**See Also:** Constant Field Values

- LOCHDR

```java
public static final int LOCHDR
```

**See Also:** Constant Field Values

- EXTHDR

```java
public static final int EXTHDR
```

**See Also:** Constant Field Values

- CENHDR

```java
public static final int CENHDR
```

**See Also:** Constant Field Values

- ENDHDR

```java
public static final int ENDHDR
```

**See Also:** Constant Field Values

- LOCVER

```java
public static final int LOCVER
```

**See Also:** Constant Field Values

- LOCFLG

```java
public static final int LOCFLG
```

**See Also:** Constant Field Values

- LOCHOW

```java
public static final int LOCHOW
```

**See Also:** Constant Field Values

- LOCTIM

```java
public static final int LOCTIM
```

**See Also:** Constant Field Values

- LOCCRC

```java
public static final int LOCCRC
```

**See Also:** Constant Field Values

- LOCSIZ

```java
public static final int LOCSIZ
```

**See Also:** Constant Field Values

- LOCLEN

```java
public static final int LOCLEN
```

**See Also:** Constant Field Values

- LOCNAM

```java
public static final int LOCNAM
```

**See Also:** Constant Field Values

- LOCEXT

```java
public static final int LOCEXT
```

**See Also:** Constant Field Values

- EXTCRC

```java
public static final int EXTCRC
```

**See Also:** Constant Field Values

- EXTSIZ

```java
public static final int EXTSIZ
```

**See Also:** Constant Field Values

- EXTLEN

```java
public static final int EXTLEN
```

**See Also:** Constant Field Values

- CENVEM

```java
public static final int CENVEM
```

**See Also:** Constant Field Values

- CENVER

```java
public static final int CENVER
```

**See Also:** Constant Field Values

- CENFLG

```java
public static final int CENFLG
```

**See Also:** Constant Field Values

- CENHOW

```java
public static final int CENHOW
```

**See Also:** Constant Field Values

- CENTIM

```java
public static final int CENTIM
```

**See Also:** Constant Field Values

- CENCRC

```java
public static final int CENCRC
```

**See Also:** Constant Field Values

- CENSIZ

```java
public static final int CENSIZ
```

**See Also:** Constant Field Values

- CENLEN

```java
public static final int CENLEN
```

**See Also:** Constant Field Values

- CENNAM

```java
public static final int CENNAM
```

**See Also:** Constant Field Values

- CENEXT

```java
public static final int CENEXT
```

**See Also:** Constant Field Values

- CENCOM

```java
public static final int CENCOM
```

**See Also:** Constant Field Values

- CENDSK

```java
public static final int CENDSK
```

**See Also:** Constant Field Values

- CENATT

```java
public static final int CENATT
```

**See Also:** Constant Field Values

- CENATX

```java
public static final int CENATX
```

**See Also:** Constant Field Values

- CENOFF

```java
public static final int CENOFF
```

**See Also:** Constant Field Values

- ENDSUB

```java
public static final int ENDSUB
```

**See Also:** Constant Field Values

- ENDTOT

```java
public static final int ENDTOT
```

**See Also:** Constant Field Values

- ENDSIZ

```java
public static final int ENDSIZ
```

**See Also:** Constant Field Values

- ENDOFF

```java
public static final int ENDOFF
```

**See Also:** Constant Field Values

- ENDCOM

```java
public static final int ENDCOM
```

**See Also:** Constant Field Values

---

#### Field Detail

OPEN_READ

```java
public static final int OPEN_READ
```

Mode flag to open a zip file for reading.

**See Also:** Constant Field Values

---

#### OPEN_READ

public static final int OPEN_READ

Mode flag to open a zip file for reading.

OPEN_DELETE

```java
public static final int OPEN_DELETE
```

Mode flag to open a zip file and mark it for deletion. The file will be
deleted some time between the moment that it is opened and the moment
that it is closed, but its contents will remain accessible via the

ZipFile

object until either the close method is invoked or the
virtual machine exits.

**See Also:** Constant Field Values

---

#### OPEN_DELETE

public static final int OPEN_DELETE

Mode flag to open a zip file and mark it for deletion. The file will be
deleted some time between the moment that it is opened and the moment
that it is closed, but its contents will remain accessible via the

ZipFile

object until either the close method is invoked or the
virtual machine exits.

LOCSIG

```java
public static final long LOCSIG
```

**See Also:** Constant Field Values

---

#### LOCSIG

public static final long LOCSIG

EXTSIG

```java
public static final long EXTSIG
```

**See Also:** Constant Field Values

---

#### EXTSIG

public static final long EXTSIG

CENSIG

```java
public static final long CENSIG
```

**See Also:** Constant Field Values

---

#### CENSIG

public static final long CENSIG

ENDSIG

```java
public static final long ENDSIG
```

**See Also:** Constant Field Values

---

#### ENDSIG

public static final long ENDSIG

LOCHDR

```java
public static final int LOCHDR
```

**See Also:** Constant Field Values

---

#### LOCHDR

public static final int LOCHDR

EXTHDR

```java
public static final int EXTHDR
```

**See Also:** Constant Field Values

---

#### EXTHDR

public static final int EXTHDR

CENHDR

```java
public static final int CENHDR
```

**See Also:** Constant Field Values

---

#### CENHDR

public static final int CENHDR

ENDHDR

```java
public static final int ENDHDR
```

**See Also:** Constant Field Values

---

#### ENDHDR

public static final int ENDHDR

LOCVER

```java
public static final int LOCVER
```

**See Also:** Constant Field Values

---

#### LOCVER

public static final int LOCVER

LOCFLG

```java
public static final int LOCFLG
```

**See Also:** Constant Field Values

---

#### LOCFLG

public static final int LOCFLG

LOCHOW

```java
public static final int LOCHOW
```

**See Also:** Constant Field Values

---

#### LOCHOW

public static final int LOCHOW

LOCTIM

```java
public static final int LOCTIM
```

**See Also:** Constant Field Values

---

#### LOCTIM

public static final int LOCTIM

LOCCRC

```java
public static final int LOCCRC
```

**See Also:** Constant Field Values

---

#### LOCCRC

public static final int LOCCRC

LOCSIZ

```java
public static final int LOCSIZ
```

**See Also:** Constant Field Values

---

#### LOCSIZ

public static final int LOCSIZ

LOCLEN

```java
public static final int LOCLEN
```

**See Also:** Constant Field Values

---

#### LOCLEN

public static final int LOCLEN

LOCNAM

```java
public static final int LOCNAM
```

**See Also:** Constant Field Values

---

#### LOCNAM

public static final int LOCNAM

LOCEXT

```java
public static final int LOCEXT
```

**See Also:** Constant Field Values

---

#### LOCEXT

public static final int LOCEXT

EXTCRC

```java
public static final int EXTCRC
```

**See Also:** Constant Field Values

---

#### EXTCRC

public static final int EXTCRC

EXTSIZ

```java
public static final int EXTSIZ
```

**See Also:** Constant Field Values

---

#### EXTSIZ

public static final int EXTSIZ

EXTLEN

```java
public static final int EXTLEN
```

**See Also:** Constant Field Values

---

#### EXTLEN

public static final int EXTLEN

CENVEM

```java
public static final int CENVEM
```

**See Also:** Constant Field Values

---

#### CENVEM

public static final int CENVEM

CENVER

```java
public static final int CENVER
```

**See Also:** Constant Field Values

---

#### CENVER

public static final int CENVER

CENFLG

```java
public static final int CENFLG
```

**See Also:** Constant Field Values

---

#### CENFLG

public static final int CENFLG

CENHOW

```java
public static final int CENHOW
```

**See Also:** Constant Field Values

---

#### CENHOW

public static final int CENHOW

CENTIM

```java
public static final int CENTIM
```

**See Also:** Constant Field Values

---

#### CENTIM

public static final int CENTIM

CENCRC

```java
public static final int CENCRC
```

**See Also:** Constant Field Values

---

#### CENCRC

public static final int CENCRC

CENSIZ

```java
public static final int CENSIZ
```

**See Also:** Constant Field Values

---

#### CENSIZ

public static final int CENSIZ

CENLEN

```java
public static final int CENLEN
```

**See Also:** Constant Field Values

---

#### CENLEN

public static final int CENLEN

CENNAM

```java
public static final int CENNAM
```

**See Also:** Constant Field Values

---

#### CENNAM

public static final int CENNAM

CENEXT

```java
public static final int CENEXT
```

**See Also:** Constant Field Values

---

#### CENEXT

public static final int CENEXT

CENCOM

```java
public static final int CENCOM
```

**See Also:** Constant Field Values

---

#### CENCOM

public static final int CENCOM

CENDSK

```java
public static final int CENDSK
```

**See Also:** Constant Field Values

---

#### CENDSK

public static final int CENDSK

CENATT

```java
public static final int CENATT
```

**See Also:** Constant Field Values

---

#### CENATT

public static final int CENATT

CENATX

```java
public static final int CENATX
```

**See Also:** Constant Field Values

---

#### CENATX

public static final int CENATX

CENOFF

```java
public static final int CENOFF
```

**See Also:** Constant Field Values

---

#### CENOFF

public static final int CENOFF

ENDSUB

```java
public static final int ENDSUB
```

**See Also:** Constant Field Values

---

#### ENDSUB

public static final int ENDSUB

ENDTOT

```java
public static final int ENDTOT
```

**See Also:** Constant Field Values

---

#### ENDTOT

public static final int ENDTOT

ENDSIZ

```java
public static final int ENDSIZ
```

**See Also:** Constant Field Values

---

#### ENDSIZ

public static final int ENDSIZ

ENDOFF

```java
public static final int ENDOFF
```

**See Also:** Constant Field Values

---

#### ENDOFF

public static final int ENDOFF

ENDCOM

```java
public static final int ENDCOM
```

**See Also:** Constant Field Values

---

#### ENDCOM

public static final int ENDCOM

Constructor Detail

- ZipFile

```java
public ZipFile​(
String
name)
throws
IOException
```

Opens a zip file for reading.

First, if there is a security manager, its

checkRead

method is called with the

name

argument as its argument
to ensure the read is allowed.

The UTF-8

charset

is used to
decode the entry names and comments.

**Parameters:** name

- the name of the zip file
**Throws:** ZipException

- if a ZIP format error has occurred
**Throws:** IOException

- if an I/O error has occurred
**Throws:** SecurityException

- if a security manager exists and its

checkRead

method doesn't allow read access to the file.
**See Also:** SecurityManager.checkRead(java.lang.String)

- ZipFile

```java
public ZipFile​(
File
file,
int mode)
throws
IOException
```

Opens a new

ZipFile

to read from the specified

File

object in the specified mode. The mode argument
must be either

OPEN_READ

or

OPEN_READ | OPEN_DELETE

.

First, if there is a security manager, its

checkRead

method is called with the

name

argument as its argument to
ensure the read is allowed.

The UTF-8

charset

is used to
decode the entry names and comments

**Parameters:** file

- the ZIP file to be opened for reading
**Parameters:** mode

- the mode in which the file is to be opened
**Throws:** ZipException

- if a ZIP format error has occurred
**Throws:** IOException

- if an I/O error has occurred
**Throws:** SecurityException

- if a security manager exists and
its

checkRead

method
doesn't allow read access to the file,
or its

checkDelete

method doesn't allow deleting
the file when the

OPEN_DELETE

flag is set.
**Throws:** IllegalArgumentException

- if the

mode

argument is invalid
**Since:** 1.3
**See Also:** SecurityManager.checkRead(java.lang.String)

- ZipFile

```java
public ZipFile​(
File
file)
throws
ZipException
,

IOException
```

Opens a ZIP file for reading given the specified File object.

The UTF-8

charset

is used to
decode the entry names and comments.

**Parameters:** file

- the ZIP file to be opened for reading
**Throws:** ZipException

- if a ZIP format error has occurred
**Throws:** IOException

- if an I/O error has occurred

- ZipFile

```java
public ZipFile​(
File
file,
int mode,

Charset
charset)
throws
IOException
```

Opens a new

ZipFile

to read from the specified

File

object in the specified mode. The mode argument
must be either

OPEN_READ

or

OPEN_READ | OPEN_DELETE

.

First, if there is a security manager, its

checkRead

method is called with the

name

argument as its argument to
ensure the read is allowed.

**Parameters:** file

- the ZIP file to be opened for reading
**Parameters:** mode

- the mode in which the file is to be opened
**Parameters:** charset

- the

charset

to
be used to decode the ZIP entry name and comment that are not
encoded by using UTF-8 encoding (indicated by entry's general
purpose flag).
**Throws:** ZipException

- if a ZIP format error has occurred
**Throws:** IOException

- if an I/O error has occurred
**Throws:** SecurityException

- if a security manager exists and its

checkRead

method doesn't allow read access to the file,or its

checkDelete

method doesn't allow deleting the
file when the

OPEN_DELETE

flag is set
**Throws:** IllegalArgumentException

- if the

mode

argument is invalid
**Since:** 1.7
**See Also:** SecurityManager.checkRead(java.lang.String)

- ZipFile

```java
public ZipFile​(
String
name,

Charset
charset)
throws
IOException
```

Opens a zip file for reading.

First, if there is a security manager, its

checkRead

method is called with the

name

argument as its argument
to ensure the read is allowed.

**Parameters:** name

- the name of the zip file
**Parameters:** charset

- the

charset

to
be used to decode the ZIP entry name and comment that are not
encoded by using UTF-8 encoding (indicated by entry's general
purpose flag).
**Throws:** ZipException

- if a ZIP format error has occurred
**Throws:** IOException

- if an I/O error has occurred
**Throws:** SecurityException

- if a security manager exists and its

checkRead

method doesn't allow read access to the file
**Since:** 1.7
**See Also:** SecurityManager.checkRead(java.lang.String)

- ZipFile

```java
public ZipFile​(
File
file,

Charset
charset)
throws
IOException
```

Opens a ZIP file for reading given the specified File object.

**Parameters:** file

- the ZIP file to be opened for reading
**Parameters:** charset

- The

charset

to be
used to decode the ZIP entry name and comment (ignored if
the

language
encoding bit

of the ZIP entry's general purpose bit
flag is set).
**Throws:** ZipException

- if a ZIP format error has occurred
**Throws:** IOException

- if an I/O error has occurred
**Since:** 1.7

---

#### Constructor Detail

ZipFile

```java
public ZipFile​(
String
name)
throws
IOException
```

Opens a zip file for reading.

First, if there is a security manager, its

checkRead

method is called with the

name

argument as its argument
to ensure the read is allowed.

The UTF-8

charset

is used to
decode the entry names and comments.

**Parameters:** name

- the name of the zip file
**Throws:** ZipException

- if a ZIP format error has occurred
**Throws:** IOException

- if an I/O error has occurred
**Throws:** SecurityException

- if a security manager exists and its

checkRead

method doesn't allow read access to the file.
**See Also:** SecurityManager.checkRead(java.lang.String)

---

#### ZipFile

public ZipFile​(

String

name)
throws

IOException

Opens a zip file for reading.

First, if there is a security manager, its

checkRead

method is called with the

name

argument as its argument
to ensure the read is allowed.

The UTF-8

charset

is used to
decode the entry names and comments.

First, if there is a security manager, its

checkRead

method is called with the

name

argument as its argument
to ensure the read is allowed.

The UTF-8

charset

is used to
decode the entry names and comments.

The UTF-8

charset

is used to
decode the entry names and comments.

ZipFile

```java
public ZipFile​(
File
file,
int mode)
throws
IOException
```

Opens a new

ZipFile

to read from the specified

File

object in the specified mode. The mode argument
must be either

OPEN_READ

or

OPEN_READ | OPEN_DELETE

.

First, if there is a security manager, its

checkRead

method is called with the

name

argument as its argument to
ensure the read is allowed.

The UTF-8

charset

is used to
decode the entry names and comments

**Parameters:** file

- the ZIP file to be opened for reading
**Parameters:** mode

- the mode in which the file is to be opened
**Throws:** ZipException

- if a ZIP format error has occurred
**Throws:** IOException

- if an I/O error has occurred
**Throws:** SecurityException

- if a security manager exists and
its

checkRead

method
doesn't allow read access to the file,
or its

checkDelete

method doesn't allow deleting
the file when the

OPEN_DELETE

flag is set.
**Throws:** IllegalArgumentException

- if the

mode

argument is invalid
**Since:** 1.3
**See Also:** SecurityManager.checkRead(java.lang.String)

---

#### ZipFile

public ZipFile​(

File

file,
int mode)
throws

IOException

Opens a new

ZipFile

to read from the specified

File

object in the specified mode. The mode argument
must be either

OPEN_READ

or

OPEN_READ | OPEN_DELETE

.

First, if there is a security manager, its

checkRead

method is called with the

name

argument as its argument to
ensure the read is allowed.

The UTF-8

charset

is used to
decode the entry names and comments

First, if there is a security manager, its

checkRead

method is called with the

name

argument as its argument to
ensure the read is allowed.

The UTF-8

charset

is used to
decode the entry names and comments

The UTF-8

charset

is used to
decode the entry names and comments

ZipFile

```java
public ZipFile​(
File
file)
throws
ZipException
,

IOException
```

Opens a ZIP file for reading given the specified File object.

The UTF-8

charset

is used to
decode the entry names and comments.

**Parameters:** file

- the ZIP file to be opened for reading
**Throws:** ZipException

- if a ZIP format error has occurred
**Throws:** IOException

- if an I/O error has occurred

---

#### ZipFile

public ZipFile​(

File

file)
throws

ZipException

,

IOException

Opens a ZIP file for reading given the specified File object.

The UTF-8

charset

is used to
decode the entry names and comments.

The UTF-8

charset

is used to
decode the entry names and comments.

ZipFile

```java
public ZipFile​(
File
file,
int mode,

Charset
charset)
throws
IOException
```

Opens a new

ZipFile

to read from the specified

File

object in the specified mode. The mode argument
must be either

OPEN_READ

or

OPEN_READ | OPEN_DELETE

.

First, if there is a security manager, its

checkRead

method is called with the

name

argument as its argument to
ensure the read is allowed.

**Parameters:** file

- the ZIP file to be opened for reading
**Parameters:** mode

- the mode in which the file is to be opened
**Parameters:** charset

- the

charset

to
be used to decode the ZIP entry name and comment that are not
encoded by using UTF-8 encoding (indicated by entry's general
purpose flag).
**Throws:** ZipException

- if a ZIP format error has occurred
**Throws:** IOException

- if an I/O error has occurred
**Throws:** SecurityException

- if a security manager exists and its

checkRead

method doesn't allow read access to the file,or its

checkDelete

method doesn't allow deleting the
file when the

OPEN_DELETE

flag is set
**Throws:** IllegalArgumentException

- if the

mode

argument is invalid
**Since:** 1.7
**See Also:** SecurityManager.checkRead(java.lang.String)

---

#### ZipFile

public ZipFile​(

File

file,
int mode,

Charset

charset)
throws

IOException

Opens a new

ZipFile

to read from the specified

File

object in the specified mode. The mode argument
must be either

OPEN_READ

or

OPEN_READ | OPEN_DELETE

.

First, if there is a security manager, its

checkRead

method is called with the

name

argument as its argument to
ensure the read is allowed.

First, if there is a security manager, its

checkRead

method is called with the

name

argument as its argument to
ensure the read is allowed.

ZipFile

```java
public ZipFile​(
String
name,

Charset
charset)
throws
IOException
```

Opens a zip file for reading.

First, if there is a security manager, its

checkRead

method is called with the

name

argument as its argument
to ensure the read is allowed.

**Parameters:** name

- the name of the zip file
**Parameters:** charset

- the

charset

to
be used to decode the ZIP entry name and comment that are not
encoded by using UTF-8 encoding (indicated by entry's general
purpose flag).
**Throws:** ZipException

- if a ZIP format error has occurred
**Throws:** IOException

- if an I/O error has occurred
**Throws:** SecurityException

- if a security manager exists and its

checkRead

method doesn't allow read access to the file
**Since:** 1.7
**See Also:** SecurityManager.checkRead(java.lang.String)

---

#### ZipFile

public ZipFile​(

String

name,

Charset

charset)
throws

IOException

Opens a zip file for reading.

First, if there is a security manager, its

checkRead

method is called with the

name

argument as its argument
to ensure the read is allowed.

First, if there is a security manager, its

checkRead

method is called with the

name

argument as its argument
to ensure the read is allowed.

ZipFile

```java
public ZipFile​(
File
file,

Charset
charset)
throws
IOException
```

Opens a ZIP file for reading given the specified File object.

**Parameters:** file

- the ZIP file to be opened for reading
**Parameters:** charset

- The

charset

to be
used to decode the ZIP entry name and comment (ignored if
the

language
encoding bit

of the ZIP entry's general purpose bit
flag is set).
**Throws:** ZipException

- if a ZIP format error has occurred
**Throws:** IOException

- if an I/O error has occurred
**Since:** 1.7

---

#### ZipFile

public ZipFile​(

File

file,

Charset

charset)
throws

IOException

Opens a ZIP file for reading given the specified File object.

Method Detail

- getComment

```java
public
String
getComment()
```

Returns the zip file comment, or null if none.

**Returns:** the comment string for the zip file, or null if none
**Throws:** IllegalStateException

- if the zip file has been closed
**Since:** 1.7

- getEntry

```java
public
ZipEntry
getEntry​(
String
name)
```

Returns the zip file entry for the specified name, or null
if not found.

**Parameters:** name

- the name of the entry
**Returns:** the zip file entry, or null if not found
**Throws:** IllegalStateException

- if the zip file has been closed

- getInputStream

```java
public
InputStream
getInputStream​(
ZipEntry
entry)
throws
IOException
```

Returns an input stream for reading the contents of the specified
zip file entry.

Closing this ZIP file will, in turn, close all input streams that
have been returned by invocations of this method.

**Parameters:** entry

- the zip file entry
**Returns:** the input stream for reading the contents of the specified
zip file entry.
**Throws:** ZipException

- if a ZIP format error has occurred
**Throws:** IOException

- if an I/O error has occurred
**Throws:** IllegalStateException

- if the zip file has been closed

- getName

```java
public
String
getName()
```

Returns the path name of the ZIP file.

**Returns:** the path name of the ZIP file

- entries

```java
public
Enumeration
<? extends
ZipEntry
> entries()
```

Returns an enumeration of the ZIP file entries.

**Returns:** an enumeration of the ZIP file entries
**Throws:** IllegalStateException

- if the zip file has been closed

- stream

```java
public
Stream
<? extends
ZipEntry
> stream()
```

Returns an ordered

Stream

over the ZIP file entries.

Entries appear in the

Stream

in the order they appear in
the central directory of the ZIP file.

**Returns:** an ordered

Stream

of entries in this ZIP file
**Throws:** IllegalStateException

- if the zip file has been closed
**Since:** 1.8

- size

```java
public int size()
```

Returns the number of entries in the ZIP file.

**Returns:** the number of entries in the ZIP file
**Throws:** IllegalStateException

- if the zip file has been closed

- close

```java
public void close()
throws
IOException
```

Closes the ZIP file.

Closing this ZIP file will close all of the input streams
previously returned by invocations of the

getInputStream

method.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Throws:** IOException

- if an I/O error has occurred

- finalize

```java
@Deprecated
(
since
="9",

forRemoval
=true)
protected void finalize()
throws
IOException
```

Deprecated, for removal: This API element is subject to removal in a future version.

The

finalize

method has been deprecated and will be
removed. It is implemented as a no-op. Subclasses that override

finalize

in order to perform cleanup should be modified to
use alternative cleanup mechanisms and to remove the overriding

finalize

method. The recommended cleanup for ZipFile object
is to explicitly invoke

close

method when it is no longer in
use, or use try-with-resources. If the

close

is not invoked
explicitly the resources held by this object will be released when
the instance becomes unreachable.

Ensures that the system resources held by this ZipFile object are
released when there are no more references to it.

**Overrides:** finalize

in class

Object
**Throws:** IOException

- if an I/O error has occurred
**See Also:** WeakReference

,

PhantomReference

---

#### Method Detail

getComment

```java
public
String
getComment()
```

Returns the zip file comment, or null if none.

**Returns:** the comment string for the zip file, or null if none
**Throws:** IllegalStateException

- if the zip file has been closed
**Since:** 1.7

---

#### getComment

public

String

getComment()

Returns the zip file comment, or null if none.

getEntry

```java
public
ZipEntry
getEntry​(
String
name)
```

Returns the zip file entry for the specified name, or null
if not found.

**Parameters:** name

- the name of the entry
**Returns:** the zip file entry, or null if not found
**Throws:** IllegalStateException

- if the zip file has been closed

---

#### getEntry

public

ZipEntry

getEntry​(

String

name)

Returns the zip file entry for the specified name, or null
if not found.

getInputStream

```java
public
InputStream
getInputStream​(
ZipEntry
entry)
throws
IOException
```

Returns an input stream for reading the contents of the specified
zip file entry.

Closing this ZIP file will, in turn, close all input streams that
have been returned by invocations of this method.

**Parameters:** entry

- the zip file entry
**Returns:** the input stream for reading the contents of the specified
zip file entry.
**Throws:** ZipException

- if a ZIP format error has occurred
**Throws:** IOException

- if an I/O error has occurred
**Throws:** IllegalStateException

- if the zip file has been closed

---

#### getInputStream

public

InputStream

getInputStream​(

ZipEntry

entry)
throws

IOException

Returns an input stream for reading the contents of the specified
zip file entry.

Closing this ZIP file will, in turn, close all input streams that
have been returned by invocations of this method.

Closing this ZIP file will, in turn, close all input streams that
have been returned by invocations of this method.

getName

```java
public
String
getName()
```

Returns the path name of the ZIP file.

**Returns:** the path name of the ZIP file

---

#### getName

public

String

getName()

Returns the path name of the ZIP file.

entries

```java
public
Enumeration
<? extends
ZipEntry
> entries()
```

Returns an enumeration of the ZIP file entries.

**Returns:** an enumeration of the ZIP file entries
**Throws:** IllegalStateException

- if the zip file has been closed

---

#### entries

public

Enumeration

<? extends

ZipEntry

> entries()

Returns an enumeration of the ZIP file entries.

stream

```java
public
Stream
<? extends
ZipEntry
> stream()
```

Returns an ordered

Stream

over the ZIP file entries.

Entries appear in the

Stream

in the order they appear in
the central directory of the ZIP file.

**Returns:** an ordered

Stream

of entries in this ZIP file
**Throws:** IllegalStateException

- if the zip file has been closed
**Since:** 1.8

---

#### stream

public

Stream

<? extends

ZipEntry

> stream()

Returns an ordered

Stream

over the ZIP file entries.

Entries appear in the

Stream

in the order they appear in
the central directory of the ZIP file.

size

```java
public int size()
```

Returns the number of entries in the ZIP file.

**Returns:** the number of entries in the ZIP file
**Throws:** IllegalStateException

- if the zip file has been closed

---

#### size

public int size()

Returns the number of entries in the ZIP file.

close

```java
public void close()
throws
IOException
```

Closes the ZIP file.

Closing this ZIP file will close all of the input streams
previously returned by invocations of the

getInputStream

method.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Throws:** IOException

- if an I/O error has occurred

---

#### close

public void close()
throws

IOException

Closes the ZIP file.

Closing this ZIP file will close all of the input streams
previously returned by invocations of the

getInputStream

method.

Closing this ZIP file will close all of the input streams
previously returned by invocations of the

getInputStream

method.

finalize

```java
@Deprecated
(
since
="9",

forRemoval
=true)
protected void finalize()
throws
IOException
```

Deprecated, for removal: This API element is subject to removal in a future version.

The

finalize

method has been deprecated and will be
removed. It is implemented as a no-op. Subclasses that override

finalize

in order to perform cleanup should be modified to
use alternative cleanup mechanisms and to remove the overriding

finalize

method. The recommended cleanup for ZipFile object
is to explicitly invoke

close

method when it is no longer in
use, or use try-with-resources. If the

close

is not invoked
explicitly the resources held by this object will be released when
the instance becomes unreachable.

Ensures that the system resources held by this ZipFile object are
released when there are no more references to it.

**Overrides:** finalize

in class

Object
**Throws:** IOException

- if an I/O error has occurred
**See Also:** WeakReference

,

PhantomReference

---

#### finalize

@Deprecated

(

since

="9",

forRemoval

=true)
protected void finalize()
throws

IOException

Ensures that the system resources held by this ZipFile object are
released when there are no more references to it.

---

