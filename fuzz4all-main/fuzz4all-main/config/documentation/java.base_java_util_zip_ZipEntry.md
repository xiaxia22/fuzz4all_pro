# Class ZipEntry

**Source:** `java.base\java\util\zip\ZipEntry.html`

### Class Description

```java
public class
ZipEntry

extends
Object

implements
Cloneable
```

This class is used to represent a ZIP file entry.

**All Implemented Interfaces:** Cloneable

---

### Field Details

#### public static final int STORED

Compression method for uncompressed entries.

**See Also:**
- Constant Field Values

---

#### public static final int DEFLATED

Compression method for compressed (deflated) entries.

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

#### public ZipEntry​(
String
name)

Creates a new zip entry with the specified name.

**Parameters:**
- name

- The entry name

**Throws:**
- NullPointerException

- if the entry name is null
- IllegalArgumentException

- if the entry name is longer than
0xFFFF bytes

---

#### public ZipEntry​(
ZipEntry
e)

Creates a new zip entry with fields taken from the specified
zip entry.

**Parameters:**
- e

- A zip Entry object

**Throws:**
- NullPointerException

- if the entry object is null

---

### Method Details

#### public
String
getName()

Returns the name of the entry.

**Returns:**
- the name of the entry

---

#### public void setTime​(long time)

Sets the last modification time of the entry.

If the entry is output to a ZIP file or ZIP file formatted
output stream the last modification time set by this method will
be stored into the

date and time fields

of the zip file
entry and encoded in standard

MS-DOS date and time format

.
The

default TimeZone

is
used to convert the epoch time to the MS-DOS data and time.

**Parameters:**
- time

- The last modification time of the entry in milliseconds
since the epoch

**See Also:**
- getTime()

,

getLastModifiedTime()

---

#### public long getTime()

Returns the last modification time of the entry.

If the entry is read from a ZIP file or ZIP file formatted
input stream, this is the last modification time from the

date and time fields

of the zip file entry. The

default TimeZone

is used
to convert the standard MS-DOS formatted date and time to the
epoch time.

**Returns:**
- The last modification time of the entry in milliseconds
since the epoch, or -1 if not specified

**See Also:**
- setTime(long)

,

setLastModifiedTime(FileTime)

---

#### public void setTimeLocal​(
LocalDateTime
time)

Sets the last modification time of the entry in local date-time.

If the entry is output to a ZIP file or ZIP file formatted
output stream the last modification time set by this method will
be stored into the

date and time fields

of the zip file
entry and encoded in standard

MS-DOS date and time format

.
If the date-time set is out of the range of the standard

MS-DOS date and time format

, the time will also be stored into
zip file entry's extended timestamp fields in

optional
extra data

in UTC time. The

system default TimeZone

is used to convert the local date-time
to UTC time.

LocalDateTime

uses a precision of nanoseconds, whereas
this class uses a precision of milliseconds. The conversion will
truncate any excess precision information as though the amount in
nanoseconds was subject to integer division by one million.

**Parameters:**
- time

- The last modification time of the entry in local date-time

**See Also:**
- getTimeLocal()

**Since:**
- 9

---

#### public
LocalDateTime
getTimeLocal()

Returns the last modification time of the entry in local date-time.

If the entry is read from a ZIP file or ZIP file formatted
input stream, this is the last modification time from the zip
file entry's

optional extra data

if the extended timestamp
fields are present. Otherwise, the last modification time is read
from entry's standard MS-DOS formatted

date and time fields

.

The

system default TimeZone

is used to convert the UTC time to local date-time.

**Returns:**
- The last modification time of the entry in local date-time

**See Also:**
- setTimeLocal(LocalDateTime)

**Since:**
- 9

---

#### public
ZipEntry
setLastModifiedTime​(
FileTime
time)

Sets the last modification time of the entry.

When output to a ZIP file or ZIP file formatted output stream
the last modification time set by this method will be stored into
zip file entry's

date and time fields

in

standard
MS-DOS date and time format

), and the extended timestamp fields
in

optional extra data

in UTC time.

**Parameters:**
- time

- The last modification time of the entry

**Returns:**
- This zip entry

**Throws:**
- NullPointerException

- if the

time

is null

**See Also:**
- getLastModifiedTime()

**Since:**
- 1.8

---

#### public
FileTime
getLastModifiedTime()

Returns the last modification time of the entry.

If the entry is read from a ZIP file or ZIP file formatted
input stream, this is the last modification time from the zip
file entry's

optional extra data

if the extended timestamp
fields are present. Otherwise the last modification time is read
from the entry's

date and time fields

, the

default TimeZone

is used to convert
the standard MS-DOS formatted date and time to the epoch time.

**Returns:**
- The last modification time of the entry, null if not specified

**See Also:**
- setLastModifiedTime(FileTime)

**Since:**
- 1.8

---

#### public
ZipEntry
setLastAccessTime​(
FileTime
time)

Sets the last access time of the entry.

If set, the last access time will be stored into the extended
timestamp fields of entry's

optional extra data

, when output
to a ZIP file or ZIP file formatted stream.

**Parameters:**
- time

- The last access time of the entry

**Returns:**
- This zip entry

**Throws:**
- NullPointerException

- if the

time

is null

**See Also:**
- getLastAccessTime()

**Since:**
- 1.8

---

#### public
FileTime
getLastAccessTime()

Returns the last access time of the entry.

The last access time is from the extended timestamp fields
of entry's

optional extra data

when read from a ZIP file
or ZIP file formatted stream.

**Returns:**
- The last access time of the entry, null if not specified

**See Also:**
- setLastAccessTime(FileTime)

**Since:**
- 1.8

---

#### public
ZipEntry
setCreationTime​(
FileTime
time)

Sets the creation time of the entry.

If set, the creation time will be stored into the extended
timestamp fields of entry's

optional extra data

, when
output to a ZIP file or ZIP file formatted stream.

**Parameters:**
- time

- The creation time of the entry

**Returns:**
- This zip entry

**Throws:**
- NullPointerException

- if the

time

is null

**See Also:**
- getCreationTime()

**Since:**
- 1.8

---

#### public
FileTime
getCreationTime()

Returns the creation time of the entry.

The creation time is from the extended timestamp fields of
entry's

optional extra data

when read from a ZIP file
or ZIP file formatted stream.

**Returns:**
- the creation time of the entry, null if not specified

**See Also:**
- setCreationTime(FileTime)

**Since:**
- 1.8

---

#### public void setSize​(long size)

Sets the uncompressed size of the entry data.

**Parameters:**
- size

- the uncompressed size in bytes

**Throws:**
- IllegalArgumentException

- if the specified size is less
than 0, is greater than 0xFFFFFFFF when

ZIP64 format

is not supported,
or is less than 0 when ZIP64 is supported

**See Also:**
- getSize()

---

#### public long getSize()

Returns the uncompressed size of the entry data.

**Returns:**
- the uncompressed size of the entry data, or -1 if not known

**See Also:**
- setSize(long)

---

#### public long getCompressedSize()

Returns the size of the compressed entry data.

In the case of a stored entry, the compressed size will be the same
as the uncompressed size of the entry.

**Returns:**
- the size of the compressed entry data, or -1 if not known

**See Also:**
- setCompressedSize(long)

---

#### public void setCompressedSize​(long csize)

Sets the size of the compressed entry data.

**Parameters:**
- csize

- the compressed size to set

**See Also:**
- getCompressedSize()

---

#### public void setCrc​(long crc)

Sets the CRC-32 checksum of the uncompressed entry data.

**Parameters:**
- crc

- the CRC-32 value

**Throws:**
- IllegalArgumentException

- if the specified CRC-32 value is
less than 0 or greater than 0xFFFFFFFF

**See Also:**
- getCrc()

---

#### public long getCrc()

Returns the CRC-32 checksum of the uncompressed entry data.

**Returns:**
- the CRC-32 checksum of the uncompressed entry data, or -1 if
not known

**See Also:**
- setCrc(long)

---

#### public void setMethod​(int method)

Sets the compression method for the entry.

**Parameters:**
- method

- the compression method, either STORED or DEFLATED

**Throws:**
- IllegalArgumentException

- if the specified compression
method is invalid

**See Also:**
- getMethod()

---

#### public int getMethod()

Returns the compression method of the entry.

**Returns:**
- the compression method of the entry, or -1 if not specified

**See Also:**
- setMethod(int)

---

#### public void setExtra​(byte[] extra)

Sets the optional extra field data for the entry.

Invoking this method may change this entry's last modification
time, last access time and creation time, if the

extra

field
data includes the extensible timestamp fields, such as

NTFS tag
0x0001

or

Info-ZIP Extended Timestamp

, as specified in

Info-ZIP
Application Note 970311

.

**Parameters:**
- extra

- The extra field data bytes

**Throws:**
- IllegalArgumentException

- if the length of the specified
extra field data is greater than 0xFFFF bytes

**See Also:**
- getExtra()

---

#### public byte[] getExtra()

Returns the extra field data for the entry.

**Returns:**
- the extra field data for the entry, or null if none

**See Also:**
- setExtra(byte[])

---

#### public void setComment​(
String
comment)

Sets the optional comment string for the entry.

ZIP entry comments have maximum length of 0xffff. If the length of the
specified comment string is greater than 0xFFFF bytes after encoding, only
the first 0xFFFF bytes are output to the ZIP file entry.

**Parameters:**
- comment

- the comment string

**See Also:**
- getComment()

---

#### public
String
getComment()

Returns the comment string for the entry.

**Returns:**
- the comment string for the entry, or null if none

**See Also:**
- setComment(String)

---

#### public boolean isDirectory()

Returns true if this is a directory entry. A directory entry is
defined to be one whose name ends with a '/'.

**Returns:**
- true if this is a directory entry

---

#### public
String
toString()

Returns a string representation of the ZIP entry.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of the object.

---

#### public int hashCode()

Returns the hash code value for this entry.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code value for this object.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public
Object
clone()

Returns a copy of this entry.

**Overrides:**
- clone

in class

Object

**Returns:**
- a clone of this instance.

**See Also:**
- Cloneable

---

### Additional Sections

#### Class ZipEntry

java.lang.Object

- java.util.zip.ZipEntry

java.util.zip.ZipEntry

**All Implemented Interfaces:** Cloneable

**Direct Known Subclasses:** JarEntry

```java
public class
ZipEntry

extends
Object

implements
Cloneable
```

This class is used to represent a ZIP file entry.

**Since:** 1.1

public class

ZipEntry

extends

Object

implements

Cloneable

This class is used to represent a ZIP file entry.

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

Compression method for compressed (deflated) entries.

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

Compression method for uncompressed entries.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ZipEntry

​(

String

name)

Creates a new zip entry with the specified name.

ZipEntry

​(

ZipEntry

e)

Creates a new zip entry with fields taken from the specified
zip entry.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Returns a copy of this entry.

String

getComment

()

Returns the comment string for the entry.

long

getCompressedSize

()

Returns the size of the compressed entry data.

long

getCrc

()

Returns the CRC-32 checksum of the uncompressed entry data.

FileTime

getCreationTime

()

Returns the creation time of the entry.

byte[]

getExtra

()

Returns the extra field data for the entry.

FileTime

getLastAccessTime

()

Returns the last access time of the entry.

FileTime

getLastModifiedTime

()

Returns the last modification time of the entry.

int

getMethod

()

Returns the compression method of the entry.

String

getName

()

Returns the name of the entry.

long

getSize

()

Returns the uncompressed size of the entry data.

long

getTime

()

Returns the last modification time of the entry.

LocalDateTime

getTimeLocal

()

Returns the last modification time of the entry in local date-time.

int

hashCode

()

Returns the hash code value for this entry.

boolean

isDirectory

()

Returns true if this is a directory entry.

void

setComment

​(

String

comment)

Sets the optional comment string for the entry.

void

setCompressedSize

​(long csize)

Sets the size of the compressed entry data.

void

setCrc

​(long crc)

Sets the CRC-32 checksum of the uncompressed entry data.

ZipEntry

setCreationTime

​(

FileTime

time)

Sets the creation time of the entry.

void

setExtra

​(byte[] extra)

Sets the optional extra field data for the entry.

ZipEntry

setLastAccessTime

​(

FileTime

time)

Sets the last access time of the entry.

ZipEntry

setLastModifiedTime

​(

FileTime

time)

Sets the last modification time of the entry.

void

setMethod

​(int method)

Sets the compression method for the entry.

void

setSize

​(long size)

Sets the uncompressed size of the entry data.

void

setTime

​(long time)

Sets the last modification time of the entry.

void

setTimeLocal

​(

LocalDateTime

time)

Sets the last modification time of the entry in local date-time.

String

toString

()

Returns a string representation of the ZIP entry.

- Methods declared in class java.lang.

Object

equals

,

finalize

,

getClass

,

notify

,

notifyAll

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

Compression method for compressed (deflated) entries.

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

Compression method for uncompressed entries.

---

#### Field Summary

Compression method for compressed (deflated) entries.

Compression method for uncompressed entries.

Constructor Summary

Constructors

Constructor

Description

ZipEntry

​(

String

name)

Creates a new zip entry with the specified name.

ZipEntry

​(

ZipEntry

e)

Creates a new zip entry with fields taken from the specified
zip entry.

---

#### Constructor Summary

Creates a new zip entry with the specified name.

Creates a new zip entry with fields taken from the specified
zip entry.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Returns a copy of this entry.

String

getComment

()

Returns the comment string for the entry.

long

getCompressedSize

()

Returns the size of the compressed entry data.

long

getCrc

()

Returns the CRC-32 checksum of the uncompressed entry data.

FileTime

getCreationTime

()

Returns the creation time of the entry.

byte[]

getExtra

()

Returns the extra field data for the entry.

FileTime

getLastAccessTime

()

Returns the last access time of the entry.

FileTime

getLastModifiedTime

()

Returns the last modification time of the entry.

int

getMethod

()

Returns the compression method of the entry.

String

getName

()

Returns the name of the entry.

long

getSize

()

Returns the uncompressed size of the entry data.

long

getTime

()

Returns the last modification time of the entry.

LocalDateTime

getTimeLocal

()

Returns the last modification time of the entry in local date-time.

int

hashCode

()

Returns the hash code value for this entry.

boolean

isDirectory

()

Returns true if this is a directory entry.

void

setComment

​(

String

comment)

Sets the optional comment string for the entry.

void

setCompressedSize

​(long csize)

Sets the size of the compressed entry data.

void

setCrc

​(long crc)

Sets the CRC-32 checksum of the uncompressed entry data.

ZipEntry

setCreationTime

​(

FileTime

time)

Sets the creation time of the entry.

void

setExtra

​(byte[] extra)

Sets the optional extra field data for the entry.

ZipEntry

setLastAccessTime

​(

FileTime

time)

Sets the last access time of the entry.

ZipEntry

setLastModifiedTime

​(

FileTime

time)

Sets the last modification time of the entry.

void

setMethod

​(int method)

Sets the compression method for the entry.

void

setSize

​(long size)

Sets the uncompressed size of the entry data.

void

setTime

​(long time)

Sets the last modification time of the entry.

void

setTimeLocal

​(

LocalDateTime

time)

Sets the last modification time of the entry in local date-time.

String

toString

()

Returns a string representation of the ZIP entry.

- Methods declared in class java.lang.

Object

equals

,

finalize

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Method Summary

Returns a copy of this entry.

Returns the comment string for the entry.

Returns the size of the compressed entry data.

Returns the CRC-32 checksum of the uncompressed entry data.

Returns the creation time of the entry.

Returns the extra field data for the entry.

Returns the last access time of the entry.

Returns the last modification time of the entry.

Returns the compression method of the entry.

Returns the name of the entry.

Returns the uncompressed size of the entry data.

Returns the last modification time of the entry in local date-time.

Returns the hash code value for this entry.

Returns true if this is a directory entry.

Sets the optional comment string for the entry.

Sets the size of the compressed entry data.

Sets the CRC-32 checksum of the uncompressed entry data.

Sets the creation time of the entry.

Sets the optional extra field data for the entry.

Sets the last access time of the entry.

Sets the last modification time of the entry.

Sets the compression method for the entry.

Sets the uncompressed size of the entry data.

Sets the last modification time of the entry in local date-time.

Returns a string representation of the ZIP entry.

Methods declared in class java.lang.

Object

equals

,

finalize

,

getClass

,

notify

,

notifyAll

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

Compression method for uncompressed entries.

**See Also:** Constant Field Values

- DEFLATED

```java
public static final int DEFLATED
```

Compression method for compressed (deflated) entries.

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

- ZipEntry

```java
public ZipEntry​(
String
name)
```

Creates a new zip entry with the specified name.

**Parameters:** name

- The entry name
**Throws:** NullPointerException

- if the entry name is null
**Throws:** IllegalArgumentException

- if the entry name is longer than
0xFFFF bytes

- ZipEntry

```java
public ZipEntry​(
ZipEntry
e)
```

Creates a new zip entry with fields taken from the specified
zip entry.

**Parameters:** e

- A zip Entry object
**Throws:** NullPointerException

- if the entry object is null

============ METHOD DETAIL ==========

- Method Detail

- getName

```java
public
String
getName()
```

Returns the name of the entry.

**Returns:** the name of the entry

- setTime

```java
public void setTime​(long time)
```

Sets the last modification time of the entry.

If the entry is output to a ZIP file or ZIP file formatted
output stream the last modification time set by this method will
be stored into the

date and time fields

of the zip file
entry and encoded in standard

MS-DOS date and time format

.
The

default TimeZone

is
used to convert the epoch time to the MS-DOS data and time.

**Parameters:** time

- The last modification time of the entry in milliseconds
since the epoch
**See Also:** getTime()

,

getLastModifiedTime()

- getTime

```java
public long getTime()
```

Returns the last modification time of the entry.

If the entry is read from a ZIP file or ZIP file formatted
input stream, this is the last modification time from the

date and time fields

of the zip file entry. The

default TimeZone

is used
to convert the standard MS-DOS formatted date and time to the
epoch time.

**Returns:** The last modification time of the entry in milliseconds
since the epoch, or -1 if not specified
**See Also:** setTime(long)

,

setLastModifiedTime(FileTime)

- setTimeLocal

```java
public void setTimeLocal​(
LocalDateTime
time)
```

Sets the last modification time of the entry in local date-time.

If the entry is output to a ZIP file or ZIP file formatted
output stream the last modification time set by this method will
be stored into the

date and time fields

of the zip file
entry and encoded in standard

MS-DOS date and time format

.
If the date-time set is out of the range of the standard

MS-DOS date and time format

, the time will also be stored into
zip file entry's extended timestamp fields in

optional
extra data

in UTC time. The

system default TimeZone

is used to convert the local date-time
to UTC time.

LocalDateTime

uses a precision of nanoseconds, whereas
this class uses a precision of milliseconds. The conversion will
truncate any excess precision information as though the amount in
nanoseconds was subject to integer division by one million.

**Parameters:** time

- The last modification time of the entry in local date-time
**Since:** 9
**See Also:** getTimeLocal()

- getTimeLocal

```java
public
LocalDateTime
getTimeLocal()
```

Returns the last modification time of the entry in local date-time.

If the entry is read from a ZIP file or ZIP file formatted
input stream, this is the last modification time from the zip
file entry's

optional extra data

if the extended timestamp
fields are present. Otherwise, the last modification time is read
from entry's standard MS-DOS formatted

date and time fields

.

The

system default TimeZone

is used to convert the UTC time to local date-time.

**Returns:** The last modification time of the entry in local date-time
**Since:** 9
**See Also:** setTimeLocal(LocalDateTime)

- setLastModifiedTime

```java
public
ZipEntry
setLastModifiedTime​(
FileTime
time)
```

Sets the last modification time of the entry.

When output to a ZIP file or ZIP file formatted output stream
the last modification time set by this method will be stored into
zip file entry's

date and time fields

in

standard
MS-DOS date and time format

), and the extended timestamp fields
in

optional extra data

in UTC time.

**Parameters:** time

- The last modification time of the entry
**Returns:** This zip entry
**Throws:** NullPointerException

- if the

time

is null
**Since:** 1.8
**See Also:** getLastModifiedTime()

- getLastModifiedTime

```java
public
FileTime
getLastModifiedTime()
```

Returns the last modification time of the entry.

If the entry is read from a ZIP file or ZIP file formatted
input stream, this is the last modification time from the zip
file entry's

optional extra data

if the extended timestamp
fields are present. Otherwise the last modification time is read
from the entry's

date and time fields

, the

default TimeZone

is used to convert
the standard MS-DOS formatted date and time to the epoch time.

**Returns:** The last modification time of the entry, null if not specified
**Since:** 1.8
**See Also:** setLastModifiedTime(FileTime)

- setLastAccessTime

```java
public
ZipEntry
setLastAccessTime​(
FileTime
time)
```

Sets the last access time of the entry.

If set, the last access time will be stored into the extended
timestamp fields of entry's

optional extra data

, when output
to a ZIP file or ZIP file formatted stream.

**Parameters:** time

- The last access time of the entry
**Returns:** This zip entry
**Throws:** NullPointerException

- if the

time

is null
**Since:** 1.8
**See Also:** getLastAccessTime()

- getLastAccessTime

```java
public
FileTime
getLastAccessTime()
```

Returns the last access time of the entry.

The last access time is from the extended timestamp fields
of entry's

optional extra data

when read from a ZIP file
or ZIP file formatted stream.

**Returns:** The last access time of the entry, null if not specified
**Since:** 1.8
**See Also:** setLastAccessTime(FileTime)

- setCreationTime

```java
public
ZipEntry
setCreationTime​(
FileTime
time)
```

Sets the creation time of the entry.

If set, the creation time will be stored into the extended
timestamp fields of entry's

optional extra data

, when
output to a ZIP file or ZIP file formatted stream.

**Parameters:** time

- The creation time of the entry
**Returns:** This zip entry
**Throws:** NullPointerException

- if the

time

is null
**Since:** 1.8
**See Also:** getCreationTime()

- getCreationTime

```java
public
FileTime
getCreationTime()
```

Returns the creation time of the entry.

The creation time is from the extended timestamp fields of
entry's

optional extra data

when read from a ZIP file
or ZIP file formatted stream.

**Returns:** the creation time of the entry, null if not specified
**Since:** 1.8
**See Also:** setCreationTime(FileTime)

- setSize

```java
public void setSize​(long size)
```

Sets the uncompressed size of the entry data.

**Parameters:** size

- the uncompressed size in bytes
**Throws:** IllegalArgumentException

- if the specified size is less
than 0, is greater than 0xFFFFFFFF when

ZIP64 format

is not supported,
or is less than 0 when ZIP64 is supported
**See Also:** getSize()

- getSize

```java
public long getSize()
```

Returns the uncompressed size of the entry data.

**Returns:** the uncompressed size of the entry data, or -1 if not known
**See Also:** setSize(long)

- getCompressedSize

```java
public long getCompressedSize()
```

Returns the size of the compressed entry data.

In the case of a stored entry, the compressed size will be the same
as the uncompressed size of the entry.

**Returns:** the size of the compressed entry data, or -1 if not known
**See Also:** setCompressedSize(long)

- setCompressedSize

```java
public void setCompressedSize​(long csize)
```

Sets the size of the compressed entry data.

**Parameters:** csize

- the compressed size to set
**See Also:** getCompressedSize()

- setCrc

```java
public void setCrc​(long crc)
```

Sets the CRC-32 checksum of the uncompressed entry data.

**Parameters:** crc

- the CRC-32 value
**Throws:** IllegalArgumentException

- if the specified CRC-32 value is
less than 0 or greater than 0xFFFFFFFF
**See Also:** getCrc()

- getCrc

```java
public long getCrc()
```

Returns the CRC-32 checksum of the uncompressed entry data.

**Returns:** the CRC-32 checksum of the uncompressed entry data, or -1 if
not known
**See Also:** setCrc(long)

- setMethod

```java
public void setMethod​(int method)
```

Sets the compression method for the entry.

**Parameters:** method

- the compression method, either STORED or DEFLATED
**Throws:** IllegalArgumentException

- if the specified compression
method is invalid
**See Also:** getMethod()

- getMethod

```java
public int getMethod()
```

Returns the compression method of the entry.

**Returns:** the compression method of the entry, or -1 if not specified
**See Also:** setMethod(int)

- setExtra

```java
public void setExtra​(byte[] extra)
```

Sets the optional extra field data for the entry.

Invoking this method may change this entry's last modification
time, last access time and creation time, if the

extra

field
data includes the extensible timestamp fields, such as

NTFS tag
0x0001

or

Info-ZIP Extended Timestamp

, as specified in

Info-ZIP
Application Note 970311

.

**Parameters:** extra

- The extra field data bytes
**Throws:** IllegalArgumentException

- if the length of the specified
extra field data is greater than 0xFFFF bytes
**See Also:** getExtra()

- getExtra

```java
public byte[] getExtra()
```

Returns the extra field data for the entry.

**Returns:** the extra field data for the entry, or null if none
**See Also:** setExtra(byte[])

- setComment

```java
public void setComment​(
String
comment)
```

Sets the optional comment string for the entry.

ZIP entry comments have maximum length of 0xffff. If the length of the
specified comment string is greater than 0xFFFF bytes after encoding, only
the first 0xFFFF bytes are output to the ZIP file entry.

**Parameters:** comment

- the comment string
**See Also:** getComment()

- getComment

```java
public
String
getComment()
```

Returns the comment string for the entry.

**Returns:** the comment string for the entry, or null if none
**See Also:** setComment(String)

- isDirectory

```java
public boolean isDirectory()
```

Returns true if this is a directory entry. A directory entry is
defined to be one whose name ends with a '/'.

**Returns:** true if this is a directory entry

- toString

```java
public
String
toString()
```

Returns a string representation of the ZIP entry.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this entry.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- clone

```java
public
Object
clone()
```

Returns a copy of this entry.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**See Also:** Cloneable

Field Detail

- STORED

```java
public static final int STORED
```

Compression method for uncompressed entries.

**See Also:** Constant Field Values

- DEFLATED

```java
public static final int DEFLATED
```

Compression method for compressed (deflated) entries.

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

Compression method for uncompressed entries.

**See Also:** Constant Field Values

---

#### STORED

public static final int STORED

Compression method for uncompressed entries.

DEFLATED

```java
public static final int DEFLATED
```

Compression method for compressed (deflated) entries.

**See Also:** Constant Field Values

---

#### DEFLATED

public static final int DEFLATED

Compression method for compressed (deflated) entries.

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

- ZipEntry

```java
public ZipEntry​(
String
name)
```

Creates a new zip entry with the specified name.

**Parameters:** name

- The entry name
**Throws:** NullPointerException

- if the entry name is null
**Throws:** IllegalArgumentException

- if the entry name is longer than
0xFFFF bytes

- ZipEntry

```java
public ZipEntry​(
ZipEntry
e)
```

Creates a new zip entry with fields taken from the specified
zip entry.

**Parameters:** e

- A zip Entry object
**Throws:** NullPointerException

- if the entry object is null

---

#### Constructor Detail

ZipEntry

```java
public ZipEntry​(
String
name)
```

Creates a new zip entry with the specified name.

**Parameters:** name

- The entry name
**Throws:** NullPointerException

- if the entry name is null
**Throws:** IllegalArgumentException

- if the entry name is longer than
0xFFFF bytes

---

#### ZipEntry

public ZipEntry​(

String

name)

Creates a new zip entry with the specified name.

ZipEntry

```java
public ZipEntry​(
ZipEntry
e)
```

Creates a new zip entry with fields taken from the specified
zip entry.

**Parameters:** e

- A zip Entry object
**Throws:** NullPointerException

- if the entry object is null

---

#### ZipEntry

public ZipEntry​(

ZipEntry

e)

Creates a new zip entry with fields taken from the specified
zip entry.

Method Detail

- getName

```java
public
String
getName()
```

Returns the name of the entry.

**Returns:** the name of the entry

- setTime

```java
public void setTime​(long time)
```

Sets the last modification time of the entry.

If the entry is output to a ZIP file or ZIP file formatted
output stream the last modification time set by this method will
be stored into the

date and time fields

of the zip file
entry and encoded in standard

MS-DOS date and time format

.
The

default TimeZone

is
used to convert the epoch time to the MS-DOS data and time.

**Parameters:** time

- The last modification time of the entry in milliseconds
since the epoch
**See Also:** getTime()

,

getLastModifiedTime()

- getTime

```java
public long getTime()
```

Returns the last modification time of the entry.

If the entry is read from a ZIP file or ZIP file formatted
input stream, this is the last modification time from the

date and time fields

of the zip file entry. The

default TimeZone

is used
to convert the standard MS-DOS formatted date and time to the
epoch time.

**Returns:** The last modification time of the entry in milliseconds
since the epoch, or -1 if not specified
**See Also:** setTime(long)

,

setLastModifiedTime(FileTime)

- setTimeLocal

```java
public void setTimeLocal​(
LocalDateTime
time)
```

Sets the last modification time of the entry in local date-time.

If the entry is output to a ZIP file or ZIP file formatted
output stream the last modification time set by this method will
be stored into the

date and time fields

of the zip file
entry and encoded in standard

MS-DOS date and time format

.
If the date-time set is out of the range of the standard

MS-DOS date and time format

, the time will also be stored into
zip file entry's extended timestamp fields in

optional
extra data

in UTC time. The

system default TimeZone

is used to convert the local date-time
to UTC time.

LocalDateTime

uses a precision of nanoseconds, whereas
this class uses a precision of milliseconds. The conversion will
truncate any excess precision information as though the amount in
nanoseconds was subject to integer division by one million.

**Parameters:** time

- The last modification time of the entry in local date-time
**Since:** 9
**See Also:** getTimeLocal()

- getTimeLocal

```java
public
LocalDateTime
getTimeLocal()
```

Returns the last modification time of the entry in local date-time.

If the entry is read from a ZIP file or ZIP file formatted
input stream, this is the last modification time from the zip
file entry's

optional extra data

if the extended timestamp
fields are present. Otherwise, the last modification time is read
from entry's standard MS-DOS formatted

date and time fields

.

The

system default TimeZone

is used to convert the UTC time to local date-time.

**Returns:** The last modification time of the entry in local date-time
**Since:** 9
**See Also:** setTimeLocal(LocalDateTime)

- setLastModifiedTime

```java
public
ZipEntry
setLastModifiedTime​(
FileTime
time)
```

Sets the last modification time of the entry.

When output to a ZIP file or ZIP file formatted output stream
the last modification time set by this method will be stored into
zip file entry's

date and time fields

in

standard
MS-DOS date and time format

), and the extended timestamp fields
in

optional extra data

in UTC time.

**Parameters:** time

- The last modification time of the entry
**Returns:** This zip entry
**Throws:** NullPointerException

- if the

time

is null
**Since:** 1.8
**See Also:** getLastModifiedTime()

- getLastModifiedTime

```java
public
FileTime
getLastModifiedTime()
```

Returns the last modification time of the entry.

If the entry is read from a ZIP file or ZIP file formatted
input stream, this is the last modification time from the zip
file entry's

optional extra data

if the extended timestamp
fields are present. Otherwise the last modification time is read
from the entry's

date and time fields

, the

default TimeZone

is used to convert
the standard MS-DOS formatted date and time to the epoch time.

**Returns:** The last modification time of the entry, null if not specified
**Since:** 1.8
**See Also:** setLastModifiedTime(FileTime)

- setLastAccessTime

```java
public
ZipEntry
setLastAccessTime​(
FileTime
time)
```

Sets the last access time of the entry.

If set, the last access time will be stored into the extended
timestamp fields of entry's

optional extra data

, when output
to a ZIP file or ZIP file formatted stream.

**Parameters:** time

- The last access time of the entry
**Returns:** This zip entry
**Throws:** NullPointerException

- if the

time

is null
**Since:** 1.8
**See Also:** getLastAccessTime()

- getLastAccessTime

```java
public
FileTime
getLastAccessTime()
```

Returns the last access time of the entry.

The last access time is from the extended timestamp fields
of entry's

optional extra data

when read from a ZIP file
or ZIP file formatted stream.

**Returns:** The last access time of the entry, null if not specified
**Since:** 1.8
**See Also:** setLastAccessTime(FileTime)

- setCreationTime

```java
public
ZipEntry
setCreationTime​(
FileTime
time)
```

Sets the creation time of the entry.

If set, the creation time will be stored into the extended
timestamp fields of entry's

optional extra data

, when
output to a ZIP file or ZIP file formatted stream.

**Parameters:** time

- The creation time of the entry
**Returns:** This zip entry
**Throws:** NullPointerException

- if the

time

is null
**Since:** 1.8
**See Also:** getCreationTime()

- getCreationTime

```java
public
FileTime
getCreationTime()
```

Returns the creation time of the entry.

The creation time is from the extended timestamp fields of
entry's

optional extra data

when read from a ZIP file
or ZIP file formatted stream.

**Returns:** the creation time of the entry, null if not specified
**Since:** 1.8
**See Also:** setCreationTime(FileTime)

- setSize

```java
public void setSize​(long size)
```

Sets the uncompressed size of the entry data.

**Parameters:** size

- the uncompressed size in bytes
**Throws:** IllegalArgumentException

- if the specified size is less
than 0, is greater than 0xFFFFFFFF when

ZIP64 format

is not supported,
or is less than 0 when ZIP64 is supported
**See Also:** getSize()

- getSize

```java
public long getSize()
```

Returns the uncompressed size of the entry data.

**Returns:** the uncompressed size of the entry data, or -1 if not known
**See Also:** setSize(long)

- getCompressedSize

```java
public long getCompressedSize()
```

Returns the size of the compressed entry data.

In the case of a stored entry, the compressed size will be the same
as the uncompressed size of the entry.

**Returns:** the size of the compressed entry data, or -1 if not known
**See Also:** setCompressedSize(long)

- setCompressedSize

```java
public void setCompressedSize​(long csize)
```

Sets the size of the compressed entry data.

**Parameters:** csize

- the compressed size to set
**See Also:** getCompressedSize()

- setCrc

```java
public void setCrc​(long crc)
```

Sets the CRC-32 checksum of the uncompressed entry data.

**Parameters:** crc

- the CRC-32 value
**Throws:** IllegalArgumentException

- if the specified CRC-32 value is
less than 0 or greater than 0xFFFFFFFF
**See Also:** getCrc()

- getCrc

```java
public long getCrc()
```

Returns the CRC-32 checksum of the uncompressed entry data.

**Returns:** the CRC-32 checksum of the uncompressed entry data, or -1 if
not known
**See Also:** setCrc(long)

- setMethod

```java
public void setMethod​(int method)
```

Sets the compression method for the entry.

**Parameters:** method

- the compression method, either STORED or DEFLATED
**Throws:** IllegalArgumentException

- if the specified compression
method is invalid
**See Also:** getMethod()

- getMethod

```java
public int getMethod()
```

Returns the compression method of the entry.

**Returns:** the compression method of the entry, or -1 if not specified
**See Also:** setMethod(int)

- setExtra

```java
public void setExtra​(byte[] extra)
```

Sets the optional extra field data for the entry.

Invoking this method may change this entry's last modification
time, last access time and creation time, if the

extra

field
data includes the extensible timestamp fields, such as

NTFS tag
0x0001

or

Info-ZIP Extended Timestamp

, as specified in

Info-ZIP
Application Note 970311

.

**Parameters:** extra

- The extra field data bytes
**Throws:** IllegalArgumentException

- if the length of the specified
extra field data is greater than 0xFFFF bytes
**See Also:** getExtra()

- getExtra

```java
public byte[] getExtra()
```

Returns the extra field data for the entry.

**Returns:** the extra field data for the entry, or null if none
**See Also:** setExtra(byte[])

- setComment

```java
public void setComment​(
String
comment)
```

Sets the optional comment string for the entry.

ZIP entry comments have maximum length of 0xffff. If the length of the
specified comment string is greater than 0xFFFF bytes after encoding, only
the first 0xFFFF bytes are output to the ZIP file entry.

**Parameters:** comment

- the comment string
**See Also:** getComment()

- getComment

```java
public
String
getComment()
```

Returns the comment string for the entry.

**Returns:** the comment string for the entry, or null if none
**See Also:** setComment(String)

- isDirectory

```java
public boolean isDirectory()
```

Returns true if this is a directory entry. A directory entry is
defined to be one whose name ends with a '/'.

**Returns:** true if this is a directory entry

- toString

```java
public
String
toString()
```

Returns a string representation of the ZIP entry.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this entry.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- clone

```java
public
Object
clone()
```

Returns a copy of this entry.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**See Also:** Cloneable

---

#### Method Detail

getName

```java
public
String
getName()
```

Returns the name of the entry.

**Returns:** the name of the entry

---

#### getName

public

String

getName()

Returns the name of the entry.

setTime

```java
public void setTime​(long time)
```

Sets the last modification time of the entry.

If the entry is output to a ZIP file or ZIP file formatted
output stream the last modification time set by this method will
be stored into the

date and time fields

of the zip file
entry and encoded in standard

MS-DOS date and time format

.
The

default TimeZone

is
used to convert the epoch time to the MS-DOS data and time.

**Parameters:** time

- The last modification time of the entry in milliseconds
since the epoch
**See Also:** getTime()

,

getLastModifiedTime()

---

#### setTime

public void setTime​(long time)

Sets the last modification time of the entry.

If the entry is output to a ZIP file or ZIP file formatted
output stream the last modification time set by this method will
be stored into the

date and time fields

of the zip file
entry and encoded in standard

MS-DOS date and time format

.
The

default TimeZone

is
used to convert the epoch time to the MS-DOS data and time.

If the entry is output to a ZIP file or ZIP file formatted
output stream the last modification time set by this method will
be stored into the

date and time fields

of the zip file
entry and encoded in standard

MS-DOS date and time format

.
The

default TimeZone

is
used to convert the epoch time to the MS-DOS data and time.

getTime

```java
public long getTime()
```

Returns the last modification time of the entry.

If the entry is read from a ZIP file or ZIP file formatted
input stream, this is the last modification time from the

date and time fields

of the zip file entry. The

default TimeZone

is used
to convert the standard MS-DOS formatted date and time to the
epoch time.

**Returns:** The last modification time of the entry in milliseconds
since the epoch, or -1 if not specified
**See Also:** setTime(long)

,

setLastModifiedTime(FileTime)

---

#### getTime

public long getTime()

Returns the last modification time of the entry.

If the entry is read from a ZIP file or ZIP file formatted
input stream, this is the last modification time from the

date and time fields

of the zip file entry. The

default TimeZone

is used
to convert the standard MS-DOS formatted date and time to the
epoch time.

If the entry is read from a ZIP file or ZIP file formatted
input stream, this is the last modification time from the

date and time fields

of the zip file entry. The

default TimeZone

is used
to convert the standard MS-DOS formatted date and time to the
epoch time.

setTimeLocal

```java
public void setTimeLocal​(
LocalDateTime
time)
```

Sets the last modification time of the entry in local date-time.

If the entry is output to a ZIP file or ZIP file formatted
output stream the last modification time set by this method will
be stored into the

date and time fields

of the zip file
entry and encoded in standard

MS-DOS date and time format

.
If the date-time set is out of the range of the standard

MS-DOS date and time format

, the time will also be stored into
zip file entry's extended timestamp fields in

optional
extra data

in UTC time. The

system default TimeZone

is used to convert the local date-time
to UTC time.

LocalDateTime

uses a precision of nanoseconds, whereas
this class uses a precision of milliseconds. The conversion will
truncate any excess precision information as though the amount in
nanoseconds was subject to integer division by one million.

**Parameters:** time

- The last modification time of the entry in local date-time
**Since:** 9
**See Also:** getTimeLocal()

---

#### setTimeLocal

public void setTimeLocal​(

LocalDateTime

time)

Sets the last modification time of the entry in local date-time.

If the entry is output to a ZIP file or ZIP file formatted
output stream the last modification time set by this method will
be stored into the

date and time fields

of the zip file
entry and encoded in standard

MS-DOS date and time format

.
If the date-time set is out of the range of the standard

MS-DOS date and time format

, the time will also be stored into
zip file entry's extended timestamp fields in

optional
extra data

in UTC time. The

system default TimeZone

is used to convert the local date-time
to UTC time.

LocalDateTime

uses a precision of nanoseconds, whereas
this class uses a precision of milliseconds. The conversion will
truncate any excess precision information as though the amount in
nanoseconds was subject to integer division by one million.

If the entry is output to a ZIP file or ZIP file formatted
output stream the last modification time set by this method will
be stored into the

date and time fields

of the zip file
entry and encoded in standard

MS-DOS date and time format

.
If the date-time set is out of the range of the standard

MS-DOS date and time format

, the time will also be stored into
zip file entry's extended timestamp fields in

optional
extra data

in UTC time. The

system default TimeZone

is used to convert the local date-time
to UTC time.

LocalDateTime

uses a precision of nanoseconds, whereas
this class uses a precision of milliseconds. The conversion will
truncate any excess precision information as though the amount in
nanoseconds was subject to integer division by one million.

LocalDateTime

uses a precision of nanoseconds, whereas
this class uses a precision of milliseconds. The conversion will
truncate any excess precision information as though the amount in
nanoseconds was subject to integer division by one million.

getTimeLocal

```java
public
LocalDateTime
getTimeLocal()
```

Returns the last modification time of the entry in local date-time.

If the entry is read from a ZIP file or ZIP file formatted
input stream, this is the last modification time from the zip
file entry's

optional extra data

if the extended timestamp
fields are present. Otherwise, the last modification time is read
from entry's standard MS-DOS formatted

date and time fields

.

The

system default TimeZone

is used to convert the UTC time to local date-time.

**Returns:** The last modification time of the entry in local date-time
**Since:** 9
**See Also:** setTimeLocal(LocalDateTime)

---

#### getTimeLocal

public

LocalDateTime

getTimeLocal()

Returns the last modification time of the entry in local date-time.

If the entry is read from a ZIP file or ZIP file formatted
input stream, this is the last modification time from the zip
file entry's

optional extra data

if the extended timestamp
fields are present. Otherwise, the last modification time is read
from entry's standard MS-DOS formatted

date and time fields

.

The

system default TimeZone

is used to convert the UTC time to local date-time.

If the entry is read from a ZIP file or ZIP file formatted
input stream, this is the last modification time from the zip
file entry's

optional extra data

if the extended timestamp
fields are present. Otherwise, the last modification time is read
from entry's standard MS-DOS formatted

date and time fields

.

The

system default TimeZone

is used to convert the UTC time to local date-time.

The

system default TimeZone

is used to convert the UTC time to local date-time.

setLastModifiedTime

```java
public
ZipEntry
setLastModifiedTime​(
FileTime
time)
```

Sets the last modification time of the entry.

When output to a ZIP file or ZIP file formatted output stream
the last modification time set by this method will be stored into
zip file entry's

date and time fields

in

standard
MS-DOS date and time format

), and the extended timestamp fields
in

optional extra data

in UTC time.

**Parameters:** time

- The last modification time of the entry
**Returns:** This zip entry
**Throws:** NullPointerException

- if the

time

is null
**Since:** 1.8
**See Also:** getLastModifiedTime()

---

#### setLastModifiedTime

public

ZipEntry

setLastModifiedTime​(

FileTime

time)

Sets the last modification time of the entry.

When output to a ZIP file or ZIP file formatted output stream
the last modification time set by this method will be stored into
zip file entry's

date and time fields

in

standard
MS-DOS date and time format

), and the extended timestamp fields
in

optional extra data

in UTC time.

When output to a ZIP file or ZIP file formatted output stream
the last modification time set by this method will be stored into
zip file entry's

date and time fields

in

standard
MS-DOS date and time format

), and the extended timestamp fields
in

optional extra data

in UTC time.

getLastModifiedTime

```java
public
FileTime
getLastModifiedTime()
```

Returns the last modification time of the entry.

If the entry is read from a ZIP file or ZIP file formatted
input stream, this is the last modification time from the zip
file entry's

optional extra data

if the extended timestamp
fields are present. Otherwise the last modification time is read
from the entry's

date and time fields

, the

default TimeZone

is used to convert
the standard MS-DOS formatted date and time to the epoch time.

**Returns:** The last modification time of the entry, null if not specified
**Since:** 1.8
**See Also:** setLastModifiedTime(FileTime)

---

#### getLastModifiedTime

public

FileTime

getLastModifiedTime()

Returns the last modification time of the entry.

If the entry is read from a ZIP file or ZIP file formatted
input stream, this is the last modification time from the zip
file entry's

optional extra data

if the extended timestamp
fields are present. Otherwise the last modification time is read
from the entry's

date and time fields

, the

default TimeZone

is used to convert
the standard MS-DOS formatted date and time to the epoch time.

If the entry is read from a ZIP file or ZIP file formatted
input stream, this is the last modification time from the zip
file entry's

optional extra data

if the extended timestamp
fields are present. Otherwise the last modification time is read
from the entry's

date and time fields

, the

default TimeZone

is used to convert
the standard MS-DOS formatted date and time to the epoch time.

setLastAccessTime

```java
public
ZipEntry
setLastAccessTime​(
FileTime
time)
```

Sets the last access time of the entry.

If set, the last access time will be stored into the extended
timestamp fields of entry's

optional extra data

, when output
to a ZIP file or ZIP file formatted stream.

**Parameters:** time

- The last access time of the entry
**Returns:** This zip entry
**Throws:** NullPointerException

- if the

time

is null
**Since:** 1.8
**See Also:** getLastAccessTime()

---

#### setLastAccessTime

public

ZipEntry

setLastAccessTime​(

FileTime

time)

Sets the last access time of the entry.

If set, the last access time will be stored into the extended
timestamp fields of entry's

optional extra data

, when output
to a ZIP file or ZIP file formatted stream.

If set, the last access time will be stored into the extended
timestamp fields of entry's

optional extra data

, when output
to a ZIP file or ZIP file formatted stream.

getLastAccessTime

```java
public
FileTime
getLastAccessTime()
```

Returns the last access time of the entry.

The last access time is from the extended timestamp fields
of entry's

optional extra data

when read from a ZIP file
or ZIP file formatted stream.

**Returns:** The last access time of the entry, null if not specified
**Since:** 1.8
**See Also:** setLastAccessTime(FileTime)

---

#### getLastAccessTime

public

FileTime

getLastAccessTime()

Returns the last access time of the entry.

The last access time is from the extended timestamp fields
of entry's

optional extra data

when read from a ZIP file
or ZIP file formatted stream.

The last access time is from the extended timestamp fields
of entry's

optional extra data

when read from a ZIP file
or ZIP file formatted stream.

setCreationTime

```java
public
ZipEntry
setCreationTime​(
FileTime
time)
```

Sets the creation time of the entry.

If set, the creation time will be stored into the extended
timestamp fields of entry's

optional extra data

, when
output to a ZIP file or ZIP file formatted stream.

**Parameters:** time

- The creation time of the entry
**Returns:** This zip entry
**Throws:** NullPointerException

- if the

time

is null
**Since:** 1.8
**See Also:** getCreationTime()

---

#### setCreationTime

public

ZipEntry

setCreationTime​(

FileTime

time)

Sets the creation time of the entry.

If set, the creation time will be stored into the extended
timestamp fields of entry's

optional extra data

, when
output to a ZIP file or ZIP file formatted stream.

If set, the creation time will be stored into the extended
timestamp fields of entry's

optional extra data

, when
output to a ZIP file or ZIP file formatted stream.

getCreationTime

```java
public
FileTime
getCreationTime()
```

Returns the creation time of the entry.

The creation time is from the extended timestamp fields of
entry's

optional extra data

when read from a ZIP file
or ZIP file formatted stream.

**Returns:** the creation time of the entry, null if not specified
**Since:** 1.8
**See Also:** setCreationTime(FileTime)

---

#### getCreationTime

public

FileTime

getCreationTime()

Returns the creation time of the entry.

The creation time is from the extended timestamp fields of
entry's

optional extra data

when read from a ZIP file
or ZIP file formatted stream.

The creation time is from the extended timestamp fields of
entry's

optional extra data

when read from a ZIP file
or ZIP file formatted stream.

setSize

```java
public void setSize​(long size)
```

Sets the uncompressed size of the entry data.

**Parameters:** size

- the uncompressed size in bytes
**Throws:** IllegalArgumentException

- if the specified size is less
than 0, is greater than 0xFFFFFFFF when

ZIP64 format

is not supported,
or is less than 0 when ZIP64 is supported
**See Also:** getSize()

---

#### setSize

public void setSize​(long size)

Sets the uncompressed size of the entry data.

getSize

```java
public long getSize()
```

Returns the uncompressed size of the entry data.

**Returns:** the uncompressed size of the entry data, or -1 if not known
**See Also:** setSize(long)

---

#### getSize

public long getSize()

Returns the uncompressed size of the entry data.

getCompressedSize

```java
public long getCompressedSize()
```

Returns the size of the compressed entry data.

In the case of a stored entry, the compressed size will be the same
as the uncompressed size of the entry.

**Returns:** the size of the compressed entry data, or -1 if not known
**See Also:** setCompressedSize(long)

---

#### getCompressedSize

public long getCompressedSize()

Returns the size of the compressed entry data.

In the case of a stored entry, the compressed size will be the same
as the uncompressed size of the entry.

In the case of a stored entry, the compressed size will be the same
as the uncompressed size of the entry.

setCompressedSize

```java
public void setCompressedSize​(long csize)
```

Sets the size of the compressed entry data.

**Parameters:** csize

- the compressed size to set
**See Also:** getCompressedSize()

---

#### setCompressedSize

public void setCompressedSize​(long csize)

Sets the size of the compressed entry data.

setCrc

```java
public void setCrc​(long crc)
```

Sets the CRC-32 checksum of the uncompressed entry data.

**Parameters:** crc

- the CRC-32 value
**Throws:** IllegalArgumentException

- if the specified CRC-32 value is
less than 0 or greater than 0xFFFFFFFF
**See Also:** getCrc()

---

#### setCrc

public void setCrc​(long crc)

Sets the CRC-32 checksum of the uncompressed entry data.

getCrc

```java
public long getCrc()
```

Returns the CRC-32 checksum of the uncompressed entry data.

**Returns:** the CRC-32 checksum of the uncompressed entry data, or -1 if
not known
**See Also:** setCrc(long)

---

#### getCrc

public long getCrc()

Returns the CRC-32 checksum of the uncompressed entry data.

setMethod

```java
public void setMethod​(int method)
```

Sets the compression method for the entry.

**Parameters:** method

- the compression method, either STORED or DEFLATED
**Throws:** IllegalArgumentException

- if the specified compression
method is invalid
**See Also:** getMethod()

---

#### setMethod

public void setMethod​(int method)

Sets the compression method for the entry.

getMethod

```java
public int getMethod()
```

Returns the compression method of the entry.

**Returns:** the compression method of the entry, or -1 if not specified
**See Also:** setMethod(int)

---

#### getMethod

public int getMethod()

Returns the compression method of the entry.

setExtra

```java
public void setExtra​(byte[] extra)
```

Sets the optional extra field data for the entry.

Invoking this method may change this entry's last modification
time, last access time and creation time, if the

extra

field
data includes the extensible timestamp fields, such as

NTFS tag
0x0001

or

Info-ZIP Extended Timestamp

, as specified in

Info-ZIP
Application Note 970311

.

**Parameters:** extra

- The extra field data bytes
**Throws:** IllegalArgumentException

- if the length of the specified
extra field data is greater than 0xFFFF bytes
**See Also:** getExtra()

---

#### setExtra

public void setExtra​(byte[] extra)

Sets the optional extra field data for the entry.

Invoking this method may change this entry's last modification
time, last access time and creation time, if the

extra

field
data includes the extensible timestamp fields, such as

NTFS tag
0x0001

or

Info-ZIP Extended Timestamp

, as specified in

Info-ZIP
Application Note 970311

.

Invoking this method may change this entry's last modification
time, last access time and creation time, if the

extra

field
data includes the extensible timestamp fields, such as

NTFS tag
0x0001

or

Info-ZIP Extended Timestamp

, as specified in

Info-ZIP
Application Note 970311

.

getExtra

```java
public byte[] getExtra()
```

Returns the extra field data for the entry.

**Returns:** the extra field data for the entry, or null if none
**See Also:** setExtra(byte[])

---

#### getExtra

public byte[] getExtra()

Returns the extra field data for the entry.

setComment

```java
public void setComment​(
String
comment)
```

Sets the optional comment string for the entry.

ZIP entry comments have maximum length of 0xffff. If the length of the
specified comment string is greater than 0xFFFF bytes after encoding, only
the first 0xFFFF bytes are output to the ZIP file entry.

**Parameters:** comment

- the comment string
**See Also:** getComment()

---

#### setComment

public void setComment​(

String

comment)

Sets the optional comment string for the entry.

ZIP entry comments have maximum length of 0xffff. If the length of the
specified comment string is greater than 0xFFFF bytes after encoding, only
the first 0xFFFF bytes are output to the ZIP file entry.

ZIP entry comments have maximum length of 0xffff. If the length of the
specified comment string is greater than 0xFFFF bytes after encoding, only
the first 0xFFFF bytes are output to the ZIP file entry.

getComment

```java
public
String
getComment()
```

Returns the comment string for the entry.

**Returns:** the comment string for the entry, or null if none
**See Also:** setComment(String)

---

#### getComment

public

String

getComment()

Returns the comment string for the entry.

isDirectory

```java
public boolean isDirectory()
```

Returns true if this is a directory entry. A directory entry is
defined to be one whose name ends with a '/'.

**Returns:** true if this is a directory entry

---

#### isDirectory

public boolean isDirectory()

Returns true if this is a directory entry. A directory entry is
defined to be one whose name ends with a '/'.

toString

```java
public
String
toString()
```

Returns a string representation of the ZIP entry.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### toString

public

String

toString()

Returns a string representation of the ZIP entry.

hashCode

```java
public int hashCode()
```

Returns the hash code value for this entry.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns the hash code value for this entry.

clone

```java
public
Object
clone()
```

Returns a copy of this entry.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**See Also:** Cloneable

---

#### clone

public

Object

clone()

Returns a copy of this entry.

---

