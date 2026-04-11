# Class ZipOutputStream

**Source:** `java.base\java\util\zip\ZipOutputStream.html`

### Class Description

```java
public class
ZipOutputStream

extends
DeflaterOutputStream
```

This class implements an output stream filter for writing files in the
ZIP file format. Includes support for both compressed and uncompressed
entries.

**All Implemented Interfaces:** Closeable

,

Flushable

,

AutoCloseable

---

### Field Details

#### public static final int STORED

Compression method for uncompressed (STORED) entries.

**See Also:**
- Constant Field Values

---

#### public static final int DEFLATED

Compression method for compressed (DEFLATED) entries.

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

#### public ZipOutputStream​(
OutputStream
out)

Creates a new ZIP output stream.

The UTF-8

charset

is used
to encode the entry names and comments.

**Parameters:**
- out

- the actual output stream

---

#### public ZipOutputStream​(
OutputStream
out,

Charset
charset)

Creates a new ZIP output stream.

**Parameters:**
- out

- the actual output stream
- charset

- the

charset

to be used to encode the entry names and comments

**Since:**
- 1.7

---

### Method Details

#### public void setComment​(
String
comment)

Sets the ZIP file comment.

**Parameters:**
- comment

- the comment string

**Throws:**
- IllegalArgumentException

- if the length of the specified
ZIP file comment is greater than 0xFFFF bytes

---

#### public void setMethod​(int method)

Sets the default compression method for subsequent entries. This
default will be used whenever the compression method is not specified
for an individual ZIP file entry, and is initially set to DEFLATED.

**Parameters:**
- method

- the default compression method

**Throws:**
- IllegalArgumentException

- if the specified compression method
is invalid

---

#### public void setLevel​(int level)

Sets the compression level for subsequent entries which are DEFLATED.
The default setting is DEFAULT_COMPRESSION.

**Parameters:**
- level

- the compression level (0-9)

**Throws:**
- IllegalArgumentException

- if the compression level is invalid

---

#### public void putNextEntry​(
ZipEntry
e)
throws
IOException

Begins writing a new ZIP file entry and positions the stream to the
start of the entry data. Closes the current entry if still active.
The default compression method will be used if no compression method
was specified for the entry, and the current time will be used if
the entry has no set modification time.

**Parameters:**
- e

- the ZIP entry to be written

**Throws:**
- ZipException

- if a ZIP format error has occurred
- IOException

- if an I/O error has occurred

---

#### public void closeEntry()
throws
IOException

Closes the current ZIP entry and positions the stream for writing
the next entry.

**Throws:**
- ZipException

- if a ZIP format error has occurred
- IOException

- if an I/O error has occurred

---

#### public void write​(byte[] b,
int off,
int len)
throws
IOException

Writes an array of bytes to the current ZIP entry data. This method
will block until all the bytes are written.

**Overrides:**
- write

in class

DeflaterOutputStream

**Parameters:**
- b

- the data to be written
- off

- the start offset in the data
- len

- the number of bytes that are written

**Throws:**
- ZipException

- if a ZIP file error has occurred
- IOException

- if an I/O error has occurred

**See Also:**
- FilterOutputStream.write(int)

---

#### public void finish()
throws
IOException

Finishes writing the contents of the ZIP output stream without closing
the underlying stream. Use this method when applying multiple filters
in succession to the same output stream.

**Overrides:**
- finish

in class

DeflaterOutputStream

**Throws:**
- ZipException

- if a ZIP file error has occurred
- IOException

- if an I/O exception has occurred

---

#### public void close()
throws
IOException

Closes the ZIP output stream as well as the stream being filtered.

**Specified by:**
- close

in interface

AutoCloseable
- close

in interface

Closeable

**Overrides:**
- close

in class

DeflaterOutputStream

**Throws:**
- ZipException

- if a ZIP file error has occurred
- IOException

- if an I/O error has occurred

**See Also:**
- FilterOutputStream.flush()

,

FilterOutputStream.out

---

### Additional Sections

#### Class ZipOutputStream

java.lang.Object

- java.io.OutputStream
- - java.io.FilterOutputStream
- - java.util.zip.DeflaterOutputStream
- - java.util.zip.ZipOutputStream

java.io.OutputStream

- java.io.FilterOutputStream
- - java.util.zip.DeflaterOutputStream
- - java.util.zip.ZipOutputStream

java.io.FilterOutputStream

- java.util.zip.DeflaterOutputStream
- - java.util.zip.ZipOutputStream

java.util.zip.DeflaterOutputStream

- java.util.zip.ZipOutputStream

java.util.zip.ZipOutputStream

**All Implemented Interfaces:** Closeable

,

Flushable

,

AutoCloseable

**Direct Known Subclasses:** JarOutputStream

```java
public class
ZipOutputStream

extends
DeflaterOutputStream
```

This class implements an output stream filter for writing files in the
ZIP file format. Includes support for both compressed and uncompressed
entries.

**Since:** 1.1

public class

ZipOutputStream

extends

DeflaterOutputStream

This class implements an output stream filter for writing files in the
ZIP file format. Includes support for both compressed and uncompressed
entries.

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

DEFLATED

Compression method for compressed (DEFLATED) entries.

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

STORED

Compression method for uncompressed (STORED) entries.

- Fields declared in class java.util.zip.

DeflaterOutputStream

buf

,

def

- Fields declared in class java.io.

FilterOutputStream

out

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ZipOutputStream

​(

OutputStream

out)

Creates a new ZIP output stream.

ZipOutputStream

​(

OutputStream

out,

Charset

charset)

Creates a new ZIP output stream.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

close

()

Closes the ZIP output stream as well as the stream being filtered.

void

closeEntry

()

Closes the current ZIP entry and positions the stream for writing
the next entry.

void

finish

()

Finishes writing the contents of the ZIP output stream without closing
the underlying stream.

void

putNextEntry

​(

ZipEntry

e)

Begins writing a new ZIP file entry and positions the stream to the
start of the entry data.

void

setComment

​(

String

comment)

Sets the ZIP file comment.

void

setLevel

​(int level)

Sets the compression level for subsequent entries which are DEFLATED.

void

setMethod

​(int method)

Sets the default compression method for subsequent entries.

void

write

​(byte[] b,
int off,
int len)

Writes an array of bytes to the current ZIP entry data.

- Methods declared in class java.util.zip.

DeflaterOutputStream

deflate

,

flush

,

write

- Methods declared in class java.io.

FilterOutputStream

write

- Methods declared in class java.io.

OutputStream

nullOutputStream

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

DEFLATED

Compression method for compressed (DEFLATED) entries.

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

STORED

Compression method for uncompressed (STORED) entries.

- Fields declared in class java.util.zip.

DeflaterOutputStream

buf

,

def

- Fields declared in class java.io.

FilterOutputStream

out

---

#### Field Summary

Compression method for compressed (DEFLATED) entries.

Compression method for uncompressed (STORED) entries.

Fields declared in class java.util.zip.

DeflaterOutputStream

buf

,

def

---

#### Fields declared in class java.util.zip. DeflaterOutputStream

Fields declared in class java.io.

FilterOutputStream

out

---

#### Fields declared in class java.io. FilterOutputStream

Constructor Summary

Constructors

Constructor

Description

ZipOutputStream

​(

OutputStream

out)

Creates a new ZIP output stream.

ZipOutputStream

​(

OutputStream

out,

Charset

charset)

Creates a new ZIP output stream.

---

#### Constructor Summary

Creates a new ZIP output stream.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

close

()

Closes the ZIP output stream as well as the stream being filtered.

void

closeEntry

()

Closes the current ZIP entry and positions the stream for writing
the next entry.

void

finish

()

Finishes writing the contents of the ZIP output stream without closing
the underlying stream.

void

putNextEntry

​(

ZipEntry

e)

Begins writing a new ZIP file entry and positions the stream to the
start of the entry data.

void

setComment

​(

String

comment)

Sets the ZIP file comment.

void

setLevel

​(int level)

Sets the compression level for subsequent entries which are DEFLATED.

void

setMethod

​(int method)

Sets the default compression method for subsequent entries.

void

write

​(byte[] b,
int off,
int len)

Writes an array of bytes to the current ZIP entry data.

- Methods declared in class java.util.zip.

DeflaterOutputStream

deflate

,

flush

,

write

- Methods declared in class java.io.

FilterOutputStream

write

- Methods declared in class java.io.

OutputStream

nullOutputStream

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

Closes the ZIP output stream as well as the stream being filtered.

Closes the current ZIP entry and positions the stream for writing
the next entry.

Finishes writing the contents of the ZIP output stream without closing
the underlying stream.

Begins writing a new ZIP file entry and positions the stream to the
start of the entry data.

Sets the ZIP file comment.

Sets the compression level for subsequent entries which are DEFLATED.

Sets the default compression method for subsequent entries.

Writes an array of bytes to the current ZIP entry data.

Methods declared in class java.util.zip.

DeflaterOutputStream

deflate

,

flush

,

write

---

#### Methods declared in class java.util.zip. DeflaterOutputStream

Methods declared in class java.io.

FilterOutputStream

write

---

#### Methods declared in class java.io. FilterOutputStream

Methods declared in class java.io.

OutputStream

nullOutputStream

---

#### Methods declared in class java.io. OutputStream

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

- STORED

```java
public static final int STORED
```

Compression method for uncompressed (STORED) entries.

**See Also:** Constant Field Values

- DEFLATED

```java
public static final int DEFLATED
```

Compression method for compressed (DEFLATED) entries.

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

- ZipOutputStream

```java
public ZipOutputStream​(
OutputStream
out)
```

Creates a new ZIP output stream.

The UTF-8

charset

is used
to encode the entry names and comments.

**Parameters:** out

- the actual output stream

- ZipOutputStream

```java
public ZipOutputStream​(
OutputStream
out,

Charset
charset)
```

Creates a new ZIP output stream.

**Parameters:** out

- the actual output stream
**Parameters:** charset

- the

charset

to be used to encode the entry names and comments
**Since:** 1.7

============ METHOD DETAIL ==========

- Method Detail

- setComment

```java
public void setComment​(
String
comment)
```

Sets the ZIP file comment.

**Parameters:** comment

- the comment string
**Throws:** IllegalArgumentException

- if the length of the specified
ZIP file comment is greater than 0xFFFF bytes

- setMethod

```java
public void setMethod​(int method)
```

Sets the default compression method for subsequent entries. This
default will be used whenever the compression method is not specified
for an individual ZIP file entry, and is initially set to DEFLATED.

**Parameters:** method

- the default compression method
**Throws:** IllegalArgumentException

- if the specified compression method
is invalid

- setLevel

```java
public void setLevel​(int level)
```

Sets the compression level for subsequent entries which are DEFLATED.
The default setting is DEFAULT_COMPRESSION.

**Parameters:** level

- the compression level (0-9)
**Throws:** IllegalArgumentException

- if the compression level is invalid

- putNextEntry

```java
public void putNextEntry​(
ZipEntry
e)
throws
IOException
```

Begins writing a new ZIP file entry and positions the stream to the
start of the entry data. Closes the current entry if still active.
The default compression method will be used if no compression method
was specified for the entry, and the current time will be used if
the entry has no set modification time.

**Parameters:** e

- the ZIP entry to be written
**Throws:** ZipException

- if a ZIP format error has occurred
**Throws:** IOException

- if an I/O error has occurred

- closeEntry

```java
public void closeEntry()
throws
IOException
```

Closes the current ZIP entry and positions the stream for writing
the next entry.

**Throws:** ZipException

- if a ZIP format error has occurred
**Throws:** IOException

- if an I/O error has occurred

- write

```java
public void write​(byte[] b,
int off,
int len)
throws
IOException
```

Writes an array of bytes to the current ZIP entry data. This method
will block until all the bytes are written.

**Overrides:** write

in class

DeflaterOutputStream
**Parameters:** b

- the data to be written
**Parameters:** off

- the start offset in the data
**Parameters:** len

- the number of bytes that are written
**Throws:** ZipException

- if a ZIP file error has occurred
**Throws:** IOException

- if an I/O error has occurred
**See Also:** FilterOutputStream.write(int)

- finish

```java
public void finish()
throws
IOException
```

Finishes writing the contents of the ZIP output stream without closing
the underlying stream. Use this method when applying multiple filters
in succession to the same output stream.

**Overrides:** finish

in class

DeflaterOutputStream
**Throws:** ZipException

- if a ZIP file error has occurred
**Throws:** IOException

- if an I/O exception has occurred

- close

```java
public void close()
throws
IOException
```

Closes the ZIP output stream as well as the stream being filtered.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Overrides:** close

in class

DeflaterOutputStream
**Throws:** ZipException

- if a ZIP file error has occurred
**Throws:** IOException

- if an I/O error has occurred
**See Also:** FilterOutputStream.flush()

,

FilterOutputStream.out

Field Detail

- STORED

```java
public static final int STORED
```

Compression method for uncompressed (STORED) entries.

**See Also:** Constant Field Values

- DEFLATED

```java
public static final int DEFLATED
```

Compression method for compressed (DEFLATED) entries.

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

STORED

```java
public static final int STORED
```

Compression method for uncompressed (STORED) entries.

**See Also:** Constant Field Values

---

#### STORED

public static final int STORED

Compression method for uncompressed (STORED) entries.

DEFLATED

```java
public static final int DEFLATED
```

Compression method for compressed (DEFLATED) entries.

**See Also:** Constant Field Values

---

#### DEFLATED

public static final int DEFLATED

Compression method for compressed (DEFLATED) entries.

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

- ZipOutputStream

```java
public ZipOutputStream​(
OutputStream
out)
```

Creates a new ZIP output stream.

The UTF-8

charset

is used
to encode the entry names and comments.

**Parameters:** out

- the actual output stream

- ZipOutputStream

```java
public ZipOutputStream​(
OutputStream
out,

Charset
charset)
```

Creates a new ZIP output stream.

**Parameters:** out

- the actual output stream
**Parameters:** charset

- the

charset

to be used to encode the entry names and comments
**Since:** 1.7

---

#### Constructor Detail

ZipOutputStream

```java
public ZipOutputStream​(
OutputStream
out)
```

Creates a new ZIP output stream.

The UTF-8

charset

is used
to encode the entry names and comments.

**Parameters:** out

- the actual output stream

---

#### ZipOutputStream

public ZipOutputStream​(

OutputStream

out)

Creates a new ZIP output stream.

The UTF-8

charset

is used
to encode the entry names and comments.

The UTF-8

charset

is used
to encode the entry names and comments.

ZipOutputStream

```java
public ZipOutputStream​(
OutputStream
out,

Charset
charset)
```

Creates a new ZIP output stream.

**Parameters:** out

- the actual output stream
**Parameters:** charset

- the

charset

to be used to encode the entry names and comments
**Since:** 1.7

---

#### ZipOutputStream

public ZipOutputStream​(

OutputStream

out,

Charset

charset)

Creates a new ZIP output stream.

Method Detail

- setComment

```java
public void setComment​(
String
comment)
```

Sets the ZIP file comment.

**Parameters:** comment

- the comment string
**Throws:** IllegalArgumentException

- if the length of the specified
ZIP file comment is greater than 0xFFFF bytes

- setMethod

```java
public void setMethod​(int method)
```

Sets the default compression method for subsequent entries. This
default will be used whenever the compression method is not specified
for an individual ZIP file entry, and is initially set to DEFLATED.

**Parameters:** method

- the default compression method
**Throws:** IllegalArgumentException

- if the specified compression method
is invalid

- setLevel

```java
public void setLevel​(int level)
```

Sets the compression level for subsequent entries which are DEFLATED.
The default setting is DEFAULT_COMPRESSION.

**Parameters:** level

- the compression level (0-9)
**Throws:** IllegalArgumentException

- if the compression level is invalid

- putNextEntry

```java
public void putNextEntry​(
ZipEntry
e)
throws
IOException
```

Begins writing a new ZIP file entry and positions the stream to the
start of the entry data. Closes the current entry if still active.
The default compression method will be used if no compression method
was specified for the entry, and the current time will be used if
the entry has no set modification time.

**Parameters:** e

- the ZIP entry to be written
**Throws:** ZipException

- if a ZIP format error has occurred
**Throws:** IOException

- if an I/O error has occurred

- closeEntry

```java
public void closeEntry()
throws
IOException
```

Closes the current ZIP entry and positions the stream for writing
the next entry.

**Throws:** ZipException

- if a ZIP format error has occurred
**Throws:** IOException

- if an I/O error has occurred

- write

```java
public void write​(byte[] b,
int off,
int len)
throws
IOException
```

Writes an array of bytes to the current ZIP entry data. This method
will block until all the bytes are written.

**Overrides:** write

in class

DeflaterOutputStream
**Parameters:** b

- the data to be written
**Parameters:** off

- the start offset in the data
**Parameters:** len

- the number of bytes that are written
**Throws:** ZipException

- if a ZIP file error has occurred
**Throws:** IOException

- if an I/O error has occurred
**See Also:** FilterOutputStream.write(int)

- finish

```java
public void finish()
throws
IOException
```

Finishes writing the contents of the ZIP output stream without closing
the underlying stream. Use this method when applying multiple filters
in succession to the same output stream.

**Overrides:** finish

in class

DeflaterOutputStream
**Throws:** ZipException

- if a ZIP file error has occurred
**Throws:** IOException

- if an I/O exception has occurred

- close

```java
public void close()
throws
IOException
```

Closes the ZIP output stream as well as the stream being filtered.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Overrides:** close

in class

DeflaterOutputStream
**Throws:** ZipException

- if a ZIP file error has occurred
**Throws:** IOException

- if an I/O error has occurred
**See Also:** FilterOutputStream.flush()

,

FilterOutputStream.out

---

#### Method Detail

setComment

```java
public void setComment​(
String
comment)
```

Sets the ZIP file comment.

**Parameters:** comment

- the comment string
**Throws:** IllegalArgumentException

- if the length of the specified
ZIP file comment is greater than 0xFFFF bytes

---

#### setComment

public void setComment​(

String

comment)

Sets the ZIP file comment.

setMethod

```java
public void setMethod​(int method)
```

Sets the default compression method for subsequent entries. This
default will be used whenever the compression method is not specified
for an individual ZIP file entry, and is initially set to DEFLATED.

**Parameters:** method

- the default compression method
**Throws:** IllegalArgumentException

- if the specified compression method
is invalid

---

#### setMethod

public void setMethod​(int method)

Sets the default compression method for subsequent entries. This
default will be used whenever the compression method is not specified
for an individual ZIP file entry, and is initially set to DEFLATED.

setLevel

```java
public void setLevel​(int level)
```

Sets the compression level for subsequent entries which are DEFLATED.
The default setting is DEFAULT_COMPRESSION.

**Parameters:** level

- the compression level (0-9)
**Throws:** IllegalArgumentException

- if the compression level is invalid

---

#### setLevel

public void setLevel​(int level)

Sets the compression level for subsequent entries which are DEFLATED.
The default setting is DEFAULT_COMPRESSION.

putNextEntry

```java
public void putNextEntry​(
ZipEntry
e)
throws
IOException
```

Begins writing a new ZIP file entry and positions the stream to the
start of the entry data. Closes the current entry if still active.
The default compression method will be used if no compression method
was specified for the entry, and the current time will be used if
the entry has no set modification time.

**Parameters:** e

- the ZIP entry to be written
**Throws:** ZipException

- if a ZIP format error has occurred
**Throws:** IOException

- if an I/O error has occurred

---

#### putNextEntry

public void putNextEntry​(

ZipEntry

e)
throws

IOException

Begins writing a new ZIP file entry and positions the stream to the
start of the entry data. Closes the current entry if still active.
The default compression method will be used if no compression method
was specified for the entry, and the current time will be used if
the entry has no set modification time.

closeEntry

```java
public void closeEntry()
throws
IOException
```

Closes the current ZIP entry and positions the stream for writing
the next entry.

**Throws:** ZipException

- if a ZIP format error has occurred
**Throws:** IOException

- if an I/O error has occurred

---

#### closeEntry

public void closeEntry()
throws

IOException

Closes the current ZIP entry and positions the stream for writing
the next entry.

write

```java
public void write​(byte[] b,
int off,
int len)
throws
IOException
```

Writes an array of bytes to the current ZIP entry data. This method
will block until all the bytes are written.

**Overrides:** write

in class

DeflaterOutputStream
**Parameters:** b

- the data to be written
**Parameters:** off

- the start offset in the data
**Parameters:** len

- the number of bytes that are written
**Throws:** ZipException

- if a ZIP file error has occurred
**Throws:** IOException

- if an I/O error has occurred
**See Also:** FilterOutputStream.write(int)

---

#### write

public void write​(byte[] b,
int off,
int len)
throws

IOException

Writes an array of bytes to the current ZIP entry data. This method
will block until all the bytes are written.

finish

```java
public void finish()
throws
IOException
```

Finishes writing the contents of the ZIP output stream without closing
the underlying stream. Use this method when applying multiple filters
in succession to the same output stream.

**Overrides:** finish

in class

DeflaterOutputStream
**Throws:** ZipException

- if a ZIP file error has occurred
**Throws:** IOException

- if an I/O exception has occurred

---

#### finish

public void finish()
throws

IOException

Finishes writing the contents of the ZIP output stream without closing
the underlying stream. Use this method when applying multiple filters
in succession to the same output stream.

close

```java
public void close()
throws
IOException
```

Closes the ZIP output stream as well as the stream being filtered.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Overrides:** close

in class

DeflaterOutputStream
**Throws:** ZipException

- if a ZIP file error has occurred
**Throws:** IOException

- if an I/O error has occurred
**See Also:** FilterOutputStream.flush()

,

FilterOutputStream.out

---

#### close

public void close()
throws

IOException

Closes the ZIP output stream as well as the stream being filtered.

---

