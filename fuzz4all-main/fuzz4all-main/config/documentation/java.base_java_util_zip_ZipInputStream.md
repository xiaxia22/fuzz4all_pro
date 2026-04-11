# Class ZipInputStream

**Source:** `java.base\java\util\zip\ZipInputStream.html`

### Class Description

```java
public class
ZipInputStream

extends
InflaterInputStream
```

This class implements an input stream filter for reading files in the
ZIP file format. Includes support for both compressed and uncompressed
entries.

**All Implemented Interfaces:** Closeable

,

AutoCloseable

---

### Field Details

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

#### public ZipInputStream​(
InputStream
in)

Creates a new ZIP input stream.

The UTF-8

charset

is used to
decode the entry names.

**Parameters:**
- in

- the actual input stream

---

#### public ZipInputStream​(
InputStream
in,

Charset
charset)

Creates a new ZIP input stream.

**Parameters:**
- in

- the actual input stream
- charset

- The

charset

to be
used to decode the ZIP entry name (ignored if the

language
encoding bit

of the ZIP entry's general purpose bit
flag is set).

**Since:**
- 1.7

---

### Method Details

#### public
ZipEntry
getNextEntry()
throws
IOException

Reads the next ZIP file entry and positions the stream at the
beginning of the entry data.

**Returns:**
- the next ZIP file entry, or null if there are no more entries

**Throws:**
- ZipException

- if a ZIP file error has occurred
- IOException

- if an I/O error has occurred

---

#### public void closeEntry()
throws
IOException

Closes the current ZIP entry and positions the stream for reading the
next entry.

**Throws:**
- ZipException

- if a ZIP file error has occurred
- IOException

- if an I/O error has occurred

---

#### public int available()
throws
IOException

Returns 0 after EOF has reached for the current entry data,
otherwise always return 1.

Programs should not count on this method to return the actual number
of bytes that could be read without blocking.

**Overrides:**
- available

in class

InflaterInputStream

**Returns:**
- 1 before EOF and 0 after EOF has reached for current entry.

**Throws:**
- IOException

- if an I/O error occurs.

---

#### public int read​(byte[] b,
int off,
int len)
throws
IOException

Reads from the current ZIP entry into an array of bytes.
If

len

is not zero, the method
blocks until some input is available; otherwise, no
bytes are read and

0

is returned.

**Overrides:**
- read

in class

InflaterInputStream

**Parameters:**
- b

- the buffer into which the data is read
- off

- the start offset in the destination array

b
- len

- the maximum number of bytes read

**Returns:**
- the actual number of bytes read, or -1 if the end of the
entry is reached

**Throws:**
- NullPointerException

- if

b

is

null

.
- IndexOutOfBoundsException

- if

off

is negative,

len

is negative, or

len

is greater than

b.length - off
- ZipException

- if a ZIP file error has occurred
- IOException

- if an I/O error has occurred

**See Also:**
- FilterInputStream.in

---

#### public long skip​(long n)
throws
IOException

Skips specified number of bytes in the current ZIP entry.

**Overrides:**
- skip

in class

InflaterInputStream

**Parameters:**
- n

- the number of bytes to skip

**Returns:**
- the actual number of bytes skipped

**Throws:**
- ZipException

- if a ZIP file error has occurred
- IOException

- if an I/O error has occurred
- IllegalArgumentException

- if

n < 0

---

#### public void close()
throws
IOException

Closes this input stream and releases any system resources associated
with the stream.

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

InflaterInputStream

**Throws:**
- IOException

- if an I/O error has occurred

**See Also:**
- FilterInputStream.in

---

#### protected
ZipEntry
createZipEntry​(
String
name)

Creates a new

ZipEntry

object for the specified
entry name.

**Parameters:**
- name

- the ZIP file entry name

**Returns:**
- the ZipEntry just created

---

### Additional Sections

#### Class ZipInputStream

java.lang.Object

- java.io.InputStream
- - java.io.FilterInputStream
- - java.util.zip.InflaterInputStream
- - java.util.zip.ZipInputStream

java.io.InputStream

- java.io.FilterInputStream
- - java.util.zip.InflaterInputStream
- - java.util.zip.ZipInputStream

java.io.FilterInputStream

- java.util.zip.InflaterInputStream
- - java.util.zip.ZipInputStream

java.util.zip.InflaterInputStream

- java.util.zip.ZipInputStream

java.util.zip.ZipInputStream

**All Implemented Interfaces:** Closeable

,

AutoCloseable

**Direct Known Subclasses:** JarInputStream

```java
public class
ZipInputStream

extends
InflaterInputStream
```

This class implements an input stream filter for reading files in the
ZIP file format. Includes support for both compressed and uncompressed
entries.

**Since:** 1.1

public class

ZipInputStream

extends

InflaterInputStream

This class implements an input stream filter for reading files in the
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

- Fields declared in class java.util.zip.

InflaterInputStream

buf

,

inf

,

len

- Fields declared in class java.io.

FilterInputStream

in

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ZipInputStream

​(

InputStream

in)

Creates a new ZIP input stream.

ZipInputStream

​(

InputStream

in,

Charset

charset)

Creates a new ZIP input stream.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

available

()

Returns 0 after EOF has reached for the current entry data,
otherwise always return 1.

void

close

()

Closes this input stream and releases any system resources associated
with the stream.

void

closeEntry

()

Closes the current ZIP entry and positions the stream for reading the
next entry.

protected

ZipEntry

createZipEntry

​(

String

name)

Creates a new

ZipEntry

object for the specified
entry name.

ZipEntry

getNextEntry

()

Reads the next ZIP file entry and positions the stream at the
beginning of the entry data.

int

read

​(byte[] b,
int off,
int len)

Reads from the current ZIP entry into an array of bytes.

long

skip

​(long n)

Skips specified number of bytes in the current ZIP entry.

- Methods declared in class java.util.zip.

InflaterInputStream

fill

,

mark

,

markSupported

,

read

,

reset

- Methods declared in class java.io.

FilterInputStream

read

- Methods declared in class java.io.

InputStream

nullInputStream

,

readAllBytes

,

readNBytes

,

readNBytes

,

transferTo

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

- Fields declared in class java.util.zip.

InflaterInputStream

buf

,

inf

,

len

- Fields declared in class java.io.

FilterInputStream

in

---

#### Field Summary

Fields declared in class java.util.zip.

InflaterInputStream

buf

,

inf

,

len

---

#### Fields declared in class java.util.zip. InflaterInputStream

Fields declared in class java.io.

FilterInputStream

in

---

#### Fields declared in class java.io. FilterInputStream

Constructor Summary

Constructors

Constructor

Description

ZipInputStream

​(

InputStream

in)

Creates a new ZIP input stream.

ZipInputStream

​(

InputStream

in,

Charset

charset)

Creates a new ZIP input stream.

---

#### Constructor Summary

Creates a new ZIP input stream.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

available

()

Returns 0 after EOF has reached for the current entry data,
otherwise always return 1.

void

close

()

Closes this input stream and releases any system resources associated
with the stream.

void

closeEntry

()

Closes the current ZIP entry and positions the stream for reading the
next entry.

protected

ZipEntry

createZipEntry

​(

String

name)

Creates a new

ZipEntry

object for the specified
entry name.

ZipEntry

getNextEntry

()

Reads the next ZIP file entry and positions the stream at the
beginning of the entry data.

int

read

​(byte[] b,
int off,
int len)

Reads from the current ZIP entry into an array of bytes.

long

skip

​(long n)

Skips specified number of bytes in the current ZIP entry.

- Methods declared in class java.util.zip.

InflaterInputStream

fill

,

mark

,

markSupported

,

read

,

reset

- Methods declared in class java.io.

FilterInputStream

read

- Methods declared in class java.io.

InputStream

nullInputStream

,

readAllBytes

,

readNBytes

,

readNBytes

,

transferTo

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

Returns 0 after EOF has reached for the current entry data,
otherwise always return 1.

Closes this input stream and releases any system resources associated
with the stream.

Closes the current ZIP entry and positions the stream for reading the
next entry.

Creates a new

ZipEntry

object for the specified
entry name.

Reads the next ZIP file entry and positions the stream at the
beginning of the entry data.

Reads from the current ZIP entry into an array of bytes.

Skips specified number of bytes in the current ZIP entry.

Methods declared in class java.util.zip.

InflaterInputStream

fill

,

mark

,

markSupported

,

read

,

reset

---

#### Methods declared in class java.util.zip. InflaterInputStream

Methods declared in class java.io.

FilterInputStream

read

---

#### Methods declared in class java.io. FilterInputStream

Methods declared in class java.io.

InputStream

nullInputStream

,

readAllBytes

,

readNBytes

,

readNBytes

,

transferTo

---

#### Methods declared in class java.io. InputStream

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

- ZipInputStream

```java
public ZipInputStream​(
InputStream
in)
```

Creates a new ZIP input stream.

The UTF-8

charset

is used to
decode the entry names.

**Parameters:** in

- the actual input stream

- ZipInputStream

```java
public ZipInputStream​(
InputStream
in,

Charset
charset)
```

Creates a new ZIP input stream.

**Parameters:** in

- the actual input stream
**Parameters:** charset

- The

charset

to be
used to decode the ZIP entry name (ignored if the

language
encoding bit

of the ZIP entry's general purpose bit
flag is set).
**Since:** 1.7

============ METHOD DETAIL ==========

- Method Detail

- getNextEntry

```java
public
ZipEntry
getNextEntry()
throws
IOException
```

Reads the next ZIP file entry and positions the stream at the
beginning of the entry data.

**Returns:** the next ZIP file entry, or null if there are no more entries
**Throws:** ZipException

- if a ZIP file error has occurred
**Throws:** IOException

- if an I/O error has occurred

- closeEntry

```java
public void closeEntry()
throws
IOException
```

Closes the current ZIP entry and positions the stream for reading the
next entry.

**Throws:** ZipException

- if a ZIP file error has occurred
**Throws:** IOException

- if an I/O error has occurred

- available

```java
public int available()
throws
IOException
```

Returns 0 after EOF has reached for the current entry data,
otherwise always return 1.

Programs should not count on this method to return the actual number
of bytes that could be read without blocking.

**Overrides:** available

in class

InflaterInputStream
**Returns:** 1 before EOF and 0 after EOF has reached for current entry.
**Throws:** IOException

- if an I/O error occurs.

- read

```java
public int read​(byte[] b,
int off,
int len)
throws
IOException
```

Reads from the current ZIP entry into an array of bytes.
If

len

is not zero, the method
blocks until some input is available; otherwise, no
bytes are read and

0

is returned.

**Overrides:** read

in class

InflaterInputStream
**Parameters:** b

- the buffer into which the data is read
**Parameters:** off

- the start offset in the destination array

b
**Parameters:** len

- the maximum number of bytes read
**Returns:** the actual number of bytes read, or -1 if the end of the
entry is reached
**Throws:** NullPointerException

- if

b

is

null

.
**Throws:** IndexOutOfBoundsException

- if

off

is negative,

len

is negative, or

len

is greater than

b.length - off
**Throws:** ZipException

- if a ZIP file error has occurred
**Throws:** IOException

- if an I/O error has occurred
**See Also:** FilterInputStream.in

- skip

```java
public long skip​(long n)
throws
IOException
```

Skips specified number of bytes in the current ZIP entry.

**Overrides:** skip

in class

InflaterInputStream
**Parameters:** n

- the number of bytes to skip
**Returns:** the actual number of bytes skipped
**Throws:** ZipException

- if a ZIP file error has occurred
**Throws:** IOException

- if an I/O error has occurred
**Throws:** IllegalArgumentException

- if

n < 0

- close

```java
public void close()
throws
IOException
```

Closes this input stream and releases any system resources associated
with the stream.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Overrides:** close

in class

InflaterInputStream
**Throws:** IOException

- if an I/O error has occurred
**See Also:** FilterInputStream.in

- createZipEntry

```java
protected
ZipEntry
createZipEntry​(
String
name)
```

Creates a new

ZipEntry

object for the specified
entry name.

**Parameters:** name

- the ZIP file entry name
**Returns:** the ZipEntry just created

Field Detail

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

- ZipInputStream

```java
public ZipInputStream​(
InputStream
in)
```

Creates a new ZIP input stream.

The UTF-8

charset

is used to
decode the entry names.

**Parameters:** in

- the actual input stream

- ZipInputStream

```java
public ZipInputStream​(
InputStream
in,

Charset
charset)
```

Creates a new ZIP input stream.

**Parameters:** in

- the actual input stream
**Parameters:** charset

- The

charset

to be
used to decode the ZIP entry name (ignored if the

language
encoding bit

of the ZIP entry's general purpose bit
flag is set).
**Since:** 1.7

---

#### Constructor Detail

ZipInputStream

```java
public ZipInputStream​(
InputStream
in)
```

Creates a new ZIP input stream.

The UTF-8

charset

is used to
decode the entry names.

**Parameters:** in

- the actual input stream

---

#### ZipInputStream

public ZipInputStream​(

InputStream

in)

Creates a new ZIP input stream.

The UTF-8

charset

is used to
decode the entry names.

The UTF-8

charset

is used to
decode the entry names.

ZipInputStream

```java
public ZipInputStream​(
InputStream
in,

Charset
charset)
```

Creates a new ZIP input stream.

**Parameters:** in

- the actual input stream
**Parameters:** charset

- The

charset

to be
used to decode the ZIP entry name (ignored if the

language
encoding bit

of the ZIP entry's general purpose bit
flag is set).
**Since:** 1.7

---

#### ZipInputStream

public ZipInputStream​(

InputStream

in,

Charset

charset)

Creates a new ZIP input stream.

Method Detail

- getNextEntry

```java
public
ZipEntry
getNextEntry()
throws
IOException
```

Reads the next ZIP file entry and positions the stream at the
beginning of the entry data.

**Returns:** the next ZIP file entry, or null if there are no more entries
**Throws:** ZipException

- if a ZIP file error has occurred
**Throws:** IOException

- if an I/O error has occurred

- closeEntry

```java
public void closeEntry()
throws
IOException
```

Closes the current ZIP entry and positions the stream for reading the
next entry.

**Throws:** ZipException

- if a ZIP file error has occurred
**Throws:** IOException

- if an I/O error has occurred

- available

```java
public int available()
throws
IOException
```

Returns 0 after EOF has reached for the current entry data,
otherwise always return 1.

Programs should not count on this method to return the actual number
of bytes that could be read without blocking.

**Overrides:** available

in class

InflaterInputStream
**Returns:** 1 before EOF and 0 after EOF has reached for current entry.
**Throws:** IOException

- if an I/O error occurs.

- read

```java
public int read​(byte[] b,
int off,
int len)
throws
IOException
```

Reads from the current ZIP entry into an array of bytes.
If

len

is not zero, the method
blocks until some input is available; otherwise, no
bytes are read and

0

is returned.

**Overrides:** read

in class

InflaterInputStream
**Parameters:** b

- the buffer into which the data is read
**Parameters:** off

- the start offset in the destination array

b
**Parameters:** len

- the maximum number of bytes read
**Returns:** the actual number of bytes read, or -1 if the end of the
entry is reached
**Throws:** NullPointerException

- if

b

is

null

.
**Throws:** IndexOutOfBoundsException

- if

off

is negative,

len

is negative, or

len

is greater than

b.length - off
**Throws:** ZipException

- if a ZIP file error has occurred
**Throws:** IOException

- if an I/O error has occurred
**See Also:** FilterInputStream.in

- skip

```java
public long skip​(long n)
throws
IOException
```

Skips specified number of bytes in the current ZIP entry.

**Overrides:** skip

in class

InflaterInputStream
**Parameters:** n

- the number of bytes to skip
**Returns:** the actual number of bytes skipped
**Throws:** ZipException

- if a ZIP file error has occurred
**Throws:** IOException

- if an I/O error has occurred
**Throws:** IllegalArgumentException

- if

n < 0

- close

```java
public void close()
throws
IOException
```

Closes this input stream and releases any system resources associated
with the stream.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Overrides:** close

in class

InflaterInputStream
**Throws:** IOException

- if an I/O error has occurred
**See Also:** FilterInputStream.in

- createZipEntry

```java
protected
ZipEntry
createZipEntry​(
String
name)
```

Creates a new

ZipEntry

object for the specified
entry name.

**Parameters:** name

- the ZIP file entry name
**Returns:** the ZipEntry just created

---

#### Method Detail

getNextEntry

```java
public
ZipEntry
getNextEntry()
throws
IOException
```

Reads the next ZIP file entry and positions the stream at the
beginning of the entry data.

**Returns:** the next ZIP file entry, or null if there are no more entries
**Throws:** ZipException

- if a ZIP file error has occurred
**Throws:** IOException

- if an I/O error has occurred

---

#### getNextEntry

public

ZipEntry

getNextEntry()
throws

IOException

Reads the next ZIP file entry and positions the stream at the
beginning of the entry data.

closeEntry

```java
public void closeEntry()
throws
IOException
```

Closes the current ZIP entry and positions the stream for reading the
next entry.

**Throws:** ZipException

- if a ZIP file error has occurred
**Throws:** IOException

- if an I/O error has occurred

---

#### closeEntry

public void closeEntry()
throws

IOException

Closes the current ZIP entry and positions the stream for reading the
next entry.

available

```java
public int available()
throws
IOException
```

Returns 0 after EOF has reached for the current entry data,
otherwise always return 1.

Programs should not count on this method to return the actual number
of bytes that could be read without blocking.

**Overrides:** available

in class

InflaterInputStream
**Returns:** 1 before EOF and 0 after EOF has reached for current entry.
**Throws:** IOException

- if an I/O error occurs.

---

#### available

public int available()
throws

IOException

Returns 0 after EOF has reached for the current entry data,
otherwise always return 1.

Programs should not count on this method to return the actual number
of bytes that could be read without blocking.

Programs should not count on this method to return the actual number
of bytes that could be read without blocking.

read

```java
public int read​(byte[] b,
int off,
int len)
throws
IOException
```

Reads from the current ZIP entry into an array of bytes.
If

len

is not zero, the method
blocks until some input is available; otherwise, no
bytes are read and

0

is returned.

**Overrides:** read

in class

InflaterInputStream
**Parameters:** b

- the buffer into which the data is read
**Parameters:** off

- the start offset in the destination array

b
**Parameters:** len

- the maximum number of bytes read
**Returns:** the actual number of bytes read, or -1 if the end of the
entry is reached
**Throws:** NullPointerException

- if

b

is

null

.
**Throws:** IndexOutOfBoundsException

- if

off

is negative,

len

is negative, or

len

is greater than

b.length - off
**Throws:** ZipException

- if a ZIP file error has occurred
**Throws:** IOException

- if an I/O error has occurred
**See Also:** FilterInputStream.in

---

#### read

public int read​(byte[] b,
int off,
int len)
throws

IOException

Reads from the current ZIP entry into an array of bytes.
If

len

is not zero, the method
blocks until some input is available; otherwise, no
bytes are read and

0

is returned.

skip

```java
public long skip​(long n)
throws
IOException
```

Skips specified number of bytes in the current ZIP entry.

**Overrides:** skip

in class

InflaterInputStream
**Parameters:** n

- the number of bytes to skip
**Returns:** the actual number of bytes skipped
**Throws:** ZipException

- if a ZIP file error has occurred
**Throws:** IOException

- if an I/O error has occurred
**Throws:** IllegalArgumentException

- if

n < 0

---

#### skip

public long skip​(long n)
throws

IOException

Skips specified number of bytes in the current ZIP entry.

close

```java
public void close()
throws
IOException
```

Closes this input stream and releases any system resources associated
with the stream.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Overrides:** close

in class

InflaterInputStream
**Throws:** IOException

- if an I/O error has occurred
**See Also:** FilterInputStream.in

---

#### close

public void close()
throws

IOException

Closes this input stream and releases any system resources associated
with the stream.

createZipEntry

```java
protected
ZipEntry
createZipEntry​(
String
name)
```

Creates a new

ZipEntry

object for the specified
entry name.

**Parameters:** name

- the ZIP file entry name
**Returns:** the ZipEntry just created

---

#### createZipEntry

protected

ZipEntry

createZipEntry​(

String

name)

Creates a new

ZipEntry

object for the specified
entry name.

---

