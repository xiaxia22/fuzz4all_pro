# Class JarInputStream

**Source:** `java.base\java\util\jar\JarInputStream.html`

### Class Description

```java
public class
JarInputStream

extends
ZipInputStream
```

The

JarInputStream

class is used to read the contents of
a JAR file from any input stream. It extends the class

java.util.zip.ZipInputStream

with support for reading
an optional

Manifest

entry. The

Manifest

can be used to store meta-information about the JAR file and its entries.

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

#### public JarInputStream​(
InputStream
in)
throws
IOException

Creates a new

JarInputStream

and reads the optional
manifest. If a manifest is present, also attempts to verify
the signatures if the JarInputStream is signed.

**Parameters:**
- in

- the actual input stream

**Throws:**
- IOException

- if an I/O error has occurred

---

#### public JarInputStream​(
InputStream
in,
boolean verify)
throws
IOException

Creates a new

JarInputStream

and reads the optional
manifest. If a manifest is present and verify is true, also attempts
to verify the signatures if the JarInputStream is signed.

**Parameters:**
- in

- the actual input stream
- verify

- whether or not to verify the JarInputStream if
it is signed.

**Throws:**
- IOException

- if an I/O error has occurred

---

### Method Details

#### public
Manifest
getManifest()

Returns the

Manifest

for this JAR file, or

null

if none.

**Returns:**
- the

Manifest

for this JAR file, or

null

if none.

---

#### public
ZipEntry
getNextEntry()
throws
IOException

Reads the next ZIP file entry and positions the stream at the
beginning of the entry data. If verification has been enabled,
any invalid signature detected while positioning the stream for
the next entry will result in an exception.

**Overrides:**
- getNextEntry

in class

ZipInputStream

**Returns:**
- the next ZIP file entry, or null if there are no more entries

**Throws:**
- ZipException

- if a ZIP file error has occurred
- IOException

- if an I/O error has occurred
- SecurityException

- if any of the jar file entries
are incorrectly signed.

---

#### public
JarEntry
getNextJarEntry()
throws
IOException

Reads the next JAR file entry and positions the stream at the
beginning of the entry data. If verification has been enabled,
any invalid signature detected while positioning the stream for
the next entry will result in an exception.

**Returns:**
- the next JAR file entry, or null if there are no more entries

**Throws:**
- ZipException

- if a ZIP file error has occurred
- IOException

- if an I/O error has occurred
- SecurityException

- if any of the jar file entries
are incorrectly signed.

---

#### public int read​(byte[] b,
int off,
int len)
throws
IOException

Reads from the current JAR file entry into an array of bytes.
If

len

is not zero, the method
blocks until some input is available; otherwise, no
bytes are read and

0

is returned.
If verification has been enabled, any invalid signature
on the current entry will be reported at some point before the
end of the entry is reached.

**Overrides:**
- read

in class

ZipInputStream

**Parameters:**
- b

- the buffer into which the data is read
- off

- the start offset in the destination array

b
- len

- the maximum number of bytes to read

**Returns:**
- the actual number of bytes read, or -1 if the end of the
entry is reached

**Throws:**
- NullPointerException

- If

b

is

null

.
- IndexOutOfBoundsException

- If

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
- SecurityException

- if any of the jar file entries
are incorrectly signed.

**See Also:**
- FilterInputStream.in

---

#### protected
ZipEntry
createZipEntry​(
String
name)

Creates a new

JarEntry

(

ZipEntry

) for the
specified JAR file entry name. The manifest attributes of
the specified JAR file entry name will be copied to the new

JarEntry

.

**Overrides:**
- createZipEntry

in class

ZipInputStream

**Parameters:**
- name

- the name of the JAR/ZIP file entry

**Returns:**
- the

JarEntry

object just created

---

### Additional Sections

#### Class JarInputStream

java.lang.Object

- java.io.InputStream
- - java.io.FilterInputStream
- - java.util.zip.InflaterInputStream
- - java.util.zip.ZipInputStream
- - java.util.jar.JarInputStream

java.io.InputStream

- java.io.FilterInputStream
- - java.util.zip.InflaterInputStream
- - java.util.zip.ZipInputStream
- - java.util.jar.JarInputStream

java.io.FilterInputStream

- java.util.zip.InflaterInputStream
- - java.util.zip.ZipInputStream
- - java.util.jar.JarInputStream

java.util.zip.InflaterInputStream

- java.util.zip.ZipInputStream
- - java.util.jar.JarInputStream

java.util.zip.ZipInputStream

- java.util.jar.JarInputStream

java.util.jar.JarInputStream

**All Implemented Interfaces:** Closeable

,

AutoCloseable

```java
public class
JarInputStream

extends
ZipInputStream
```

The

JarInputStream

class is used to read the contents of
a JAR file from any input stream. It extends the class

java.util.zip.ZipInputStream

with support for reading
an optional

Manifest

entry. The

Manifest

can be used to store meta-information about the JAR file and its entries.

**Since:** 1.2
**See Also:** Manifest

,

ZipInputStream

public class

JarInputStream

extends

ZipInputStream

The

JarInputStream

class is used to read the contents of
a JAR file from any input stream. It extends the class

java.util.zip.ZipInputStream

with support for reading
an optional

Manifest

entry. The

Manifest

can be used to store meta-information about the JAR file and its entries.

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

JarInputStream

​(

InputStream

in)

Creates a new

JarInputStream

and reads the optional
manifest.

JarInputStream

​(

InputStream

in,
boolean verify)

Creates a new

JarInputStream

and reads the optional
manifest.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

ZipEntry

createZipEntry

​(

String

name)

Creates a new

JarEntry

(

ZipEntry

) for the
specified JAR file entry name.

Manifest

getManifest

()

Returns the

Manifest

for this JAR file, or

null

if none.

ZipEntry

getNextEntry

()

Reads the next ZIP file entry and positions the stream at the
beginning of the entry data.

JarEntry

getNextJarEntry

()

Reads the next JAR file entry and positions the stream at the
beginning of the entry data.

int

read

​(byte[] b,
int off,
int len)

Reads from the current JAR file entry into an array of bytes.

- Methods declared in class java.util.zip.

ZipInputStream

available

,

close

,

closeEntry

,

skip

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

JarInputStream

​(

InputStream

in)

Creates a new

JarInputStream

and reads the optional
manifest.

JarInputStream

​(

InputStream

in,
boolean verify)

Creates a new

JarInputStream

and reads the optional
manifest.

---

#### Constructor Summary

Creates a new

JarInputStream

and reads the optional
manifest.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

ZipEntry

createZipEntry

​(

String

name)

Creates a new

JarEntry

(

ZipEntry

) for the
specified JAR file entry name.

Manifest

getManifest

()

Returns the

Manifest

for this JAR file, or

null

if none.

ZipEntry

getNextEntry

()

Reads the next ZIP file entry and positions the stream at the
beginning of the entry data.

JarEntry

getNextJarEntry

()

Reads the next JAR file entry and positions the stream at the
beginning of the entry data.

int

read

​(byte[] b,
int off,
int len)

Reads from the current JAR file entry into an array of bytes.

- Methods declared in class java.util.zip.

ZipInputStream

available

,

close

,

closeEntry

,

skip

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

Creates a new

JarEntry

(

ZipEntry

) for the
specified JAR file entry name.

Returns the

Manifest

for this JAR file, or

null

if none.

Reads the next ZIP file entry and positions the stream at the
beginning of the entry data.

Reads the next JAR file entry and positions the stream at the
beginning of the entry data.

Reads from the current JAR file entry into an array of bytes.

Methods declared in class java.util.zip.

ZipInputStream

available

,

close

,

closeEntry

,

skip

---

#### Methods declared in class java.util.zip. ZipInputStream

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

- JarInputStream

```java
public JarInputStream​(
InputStream
in)
throws
IOException
```

Creates a new

JarInputStream

and reads the optional
manifest. If a manifest is present, also attempts to verify
the signatures if the JarInputStream is signed.

**Parameters:** in

- the actual input stream
**Throws:** IOException

- if an I/O error has occurred

- JarInputStream

```java
public JarInputStream​(
InputStream
in,
boolean verify)
throws
IOException
```

Creates a new

JarInputStream

and reads the optional
manifest. If a manifest is present and verify is true, also attempts
to verify the signatures if the JarInputStream is signed.

**Parameters:** in

- the actual input stream
**Parameters:** verify

- whether or not to verify the JarInputStream if
it is signed.
**Throws:** IOException

- if an I/O error has occurred

============ METHOD DETAIL ==========

- Method Detail

- getManifest

```java
public
Manifest
getManifest()
```

Returns the

Manifest

for this JAR file, or

null

if none.

**Returns:** the

Manifest

for this JAR file, or

null

if none.

- getNextEntry

```java
public
ZipEntry
getNextEntry()
throws
IOException
```

Reads the next ZIP file entry and positions the stream at the
beginning of the entry data. If verification has been enabled,
any invalid signature detected while positioning the stream for
the next entry will result in an exception.

**Overrides:** getNextEntry

in class

ZipInputStream
**Returns:** the next ZIP file entry, or null if there are no more entries
**Throws:** ZipException

- if a ZIP file error has occurred
**Throws:** IOException

- if an I/O error has occurred
**Throws:** SecurityException

- if any of the jar file entries
are incorrectly signed.

- getNextJarEntry

```java
public
JarEntry
getNextJarEntry()
throws
IOException
```

Reads the next JAR file entry and positions the stream at the
beginning of the entry data. If verification has been enabled,
any invalid signature detected while positioning the stream for
the next entry will result in an exception.

**Returns:** the next JAR file entry, or null if there are no more entries
**Throws:** ZipException

- if a ZIP file error has occurred
**Throws:** IOException

- if an I/O error has occurred
**Throws:** SecurityException

- if any of the jar file entries
are incorrectly signed.

- read

```java
public int read​(byte[] b,
int off,
int len)
throws
IOException
```

Reads from the current JAR file entry into an array of bytes.
If

len

is not zero, the method
blocks until some input is available; otherwise, no
bytes are read and

0

is returned.
If verification has been enabled, any invalid signature
on the current entry will be reported at some point before the
end of the entry is reached.

**Overrides:** read

in class

ZipInputStream
**Parameters:** b

- the buffer into which the data is read
**Parameters:** off

- the start offset in the destination array

b
**Parameters:** len

- the maximum number of bytes to read
**Returns:** the actual number of bytes read, or -1 if the end of the
entry is reached
**Throws:** NullPointerException

- If

b

is

null

.
**Throws:** IndexOutOfBoundsException

- If

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
**Throws:** SecurityException

- if any of the jar file entries
are incorrectly signed.
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

JarEntry

(

ZipEntry

) for the
specified JAR file entry name. The manifest attributes of
the specified JAR file entry name will be copied to the new

JarEntry

.

**Overrides:** createZipEntry

in class

ZipInputStream
**Parameters:** name

- the name of the JAR/ZIP file entry
**Returns:** the

JarEntry

object just created

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

- JarInputStream

```java
public JarInputStream​(
InputStream
in)
throws
IOException
```

Creates a new

JarInputStream

and reads the optional
manifest. If a manifest is present, also attempts to verify
the signatures if the JarInputStream is signed.

**Parameters:** in

- the actual input stream
**Throws:** IOException

- if an I/O error has occurred

- JarInputStream

```java
public JarInputStream​(
InputStream
in,
boolean verify)
throws
IOException
```

Creates a new

JarInputStream

and reads the optional
manifest. If a manifest is present and verify is true, also attempts
to verify the signatures if the JarInputStream is signed.

**Parameters:** in

- the actual input stream
**Parameters:** verify

- whether or not to verify the JarInputStream if
it is signed.
**Throws:** IOException

- if an I/O error has occurred

---

#### Constructor Detail

JarInputStream

```java
public JarInputStream​(
InputStream
in)
throws
IOException
```

Creates a new

JarInputStream

and reads the optional
manifest. If a manifest is present, also attempts to verify
the signatures if the JarInputStream is signed.

**Parameters:** in

- the actual input stream
**Throws:** IOException

- if an I/O error has occurred

---

#### JarInputStream

public JarInputStream​(

InputStream

in)
throws

IOException

Creates a new

JarInputStream

and reads the optional
manifest. If a manifest is present, also attempts to verify
the signatures if the JarInputStream is signed.

JarInputStream

```java
public JarInputStream​(
InputStream
in,
boolean verify)
throws
IOException
```

Creates a new

JarInputStream

and reads the optional
manifest. If a manifest is present and verify is true, also attempts
to verify the signatures if the JarInputStream is signed.

**Parameters:** in

- the actual input stream
**Parameters:** verify

- whether or not to verify the JarInputStream if
it is signed.
**Throws:** IOException

- if an I/O error has occurred

---

#### JarInputStream

public JarInputStream​(

InputStream

in,
boolean verify)
throws

IOException

Creates a new

JarInputStream

and reads the optional
manifest. If a manifest is present and verify is true, also attempts
to verify the signatures if the JarInputStream is signed.

Method Detail

- getManifest

```java
public
Manifest
getManifest()
```

Returns the

Manifest

for this JAR file, or

null

if none.

**Returns:** the

Manifest

for this JAR file, or

null

if none.

- getNextEntry

```java
public
ZipEntry
getNextEntry()
throws
IOException
```

Reads the next ZIP file entry and positions the stream at the
beginning of the entry data. If verification has been enabled,
any invalid signature detected while positioning the stream for
the next entry will result in an exception.

**Overrides:** getNextEntry

in class

ZipInputStream
**Returns:** the next ZIP file entry, or null if there are no more entries
**Throws:** ZipException

- if a ZIP file error has occurred
**Throws:** IOException

- if an I/O error has occurred
**Throws:** SecurityException

- if any of the jar file entries
are incorrectly signed.

- getNextJarEntry

```java
public
JarEntry
getNextJarEntry()
throws
IOException
```

Reads the next JAR file entry and positions the stream at the
beginning of the entry data. If verification has been enabled,
any invalid signature detected while positioning the stream for
the next entry will result in an exception.

**Returns:** the next JAR file entry, or null if there are no more entries
**Throws:** ZipException

- if a ZIP file error has occurred
**Throws:** IOException

- if an I/O error has occurred
**Throws:** SecurityException

- if any of the jar file entries
are incorrectly signed.

- read

```java
public int read​(byte[] b,
int off,
int len)
throws
IOException
```

Reads from the current JAR file entry into an array of bytes.
If

len

is not zero, the method
blocks until some input is available; otherwise, no
bytes are read and

0

is returned.
If verification has been enabled, any invalid signature
on the current entry will be reported at some point before the
end of the entry is reached.

**Overrides:** read

in class

ZipInputStream
**Parameters:** b

- the buffer into which the data is read
**Parameters:** off

- the start offset in the destination array

b
**Parameters:** len

- the maximum number of bytes to read
**Returns:** the actual number of bytes read, or -1 if the end of the
entry is reached
**Throws:** NullPointerException

- If

b

is

null

.
**Throws:** IndexOutOfBoundsException

- If

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
**Throws:** SecurityException

- if any of the jar file entries
are incorrectly signed.
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

JarEntry

(

ZipEntry

) for the
specified JAR file entry name. The manifest attributes of
the specified JAR file entry name will be copied to the new

JarEntry

.

**Overrides:** createZipEntry

in class

ZipInputStream
**Parameters:** name

- the name of the JAR/ZIP file entry
**Returns:** the

JarEntry

object just created

---

#### Method Detail

getManifest

```java
public
Manifest
getManifest()
```

Returns the

Manifest

for this JAR file, or

null

if none.

**Returns:** the

Manifest

for this JAR file, or

null

if none.

---

#### getManifest

public

Manifest

getManifest()

Returns the

Manifest

for this JAR file, or

null

if none.

getNextEntry

```java
public
ZipEntry
getNextEntry()
throws
IOException
```

Reads the next ZIP file entry and positions the stream at the
beginning of the entry data. If verification has been enabled,
any invalid signature detected while positioning the stream for
the next entry will result in an exception.

**Overrides:** getNextEntry

in class

ZipInputStream
**Returns:** the next ZIP file entry, or null if there are no more entries
**Throws:** ZipException

- if a ZIP file error has occurred
**Throws:** IOException

- if an I/O error has occurred
**Throws:** SecurityException

- if any of the jar file entries
are incorrectly signed.

---

#### getNextEntry

public

ZipEntry

getNextEntry()
throws

IOException

Reads the next ZIP file entry and positions the stream at the
beginning of the entry data. If verification has been enabled,
any invalid signature detected while positioning the stream for
the next entry will result in an exception.

getNextJarEntry

```java
public
JarEntry
getNextJarEntry()
throws
IOException
```

Reads the next JAR file entry and positions the stream at the
beginning of the entry data. If verification has been enabled,
any invalid signature detected while positioning the stream for
the next entry will result in an exception.

**Returns:** the next JAR file entry, or null if there are no more entries
**Throws:** ZipException

- if a ZIP file error has occurred
**Throws:** IOException

- if an I/O error has occurred
**Throws:** SecurityException

- if any of the jar file entries
are incorrectly signed.

---

#### getNextJarEntry

public

JarEntry

getNextJarEntry()
throws

IOException

Reads the next JAR file entry and positions the stream at the
beginning of the entry data. If verification has been enabled,
any invalid signature detected while positioning the stream for
the next entry will result in an exception.

read

```java
public int read​(byte[] b,
int off,
int len)
throws
IOException
```

Reads from the current JAR file entry into an array of bytes.
If

len

is not zero, the method
blocks until some input is available; otherwise, no
bytes are read and

0

is returned.
If verification has been enabled, any invalid signature
on the current entry will be reported at some point before the
end of the entry is reached.

**Overrides:** read

in class

ZipInputStream
**Parameters:** b

- the buffer into which the data is read
**Parameters:** off

- the start offset in the destination array

b
**Parameters:** len

- the maximum number of bytes to read
**Returns:** the actual number of bytes read, or -1 if the end of the
entry is reached
**Throws:** NullPointerException

- If

b

is

null

.
**Throws:** IndexOutOfBoundsException

- If

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
**Throws:** SecurityException

- if any of the jar file entries
are incorrectly signed.
**See Also:** FilterInputStream.in

---

#### read

public int read​(byte[] b,
int off,
int len)
throws

IOException

Reads from the current JAR file entry into an array of bytes.
If

len

is not zero, the method
blocks until some input is available; otherwise, no
bytes are read and

0

is returned.
If verification has been enabled, any invalid signature
on the current entry will be reported at some point before the
end of the entry is reached.

createZipEntry

```java
protected
ZipEntry
createZipEntry​(
String
name)
```

Creates a new

JarEntry

(

ZipEntry

) for the
specified JAR file entry name. The manifest attributes of
the specified JAR file entry name will be copied to the new

JarEntry

.

**Overrides:** createZipEntry

in class

ZipInputStream
**Parameters:** name

- the name of the JAR/ZIP file entry
**Returns:** the

JarEntry

object just created

---

#### createZipEntry

protected

ZipEntry

createZipEntry​(

String

name)

Creates a new

JarEntry

(

ZipEntry

) for the
specified JAR file entry name. The manifest attributes of
the specified JAR file entry name will be copied to the new

JarEntry

.

---

