# Class JarOutputStream

**Source:** `java.base\java\util\jar\JarOutputStream.html`

### Class Description

```java
public class
JarOutputStream

extends
ZipOutputStream
```

The

JarOutputStream

class is used to write the contents
of a JAR file to any output stream. It extends the class

java.util.zip.ZipOutputStream

with support
for writing an optional

Manifest

entry. The

Manifest

can be used to specify meta-information about
the JAR file and its entries.

**All Implemented Interfaces:** Closeable

,

Flushable

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

#### public JarOutputStream​(
OutputStream
out,

Manifest
man)
throws
IOException

Creates a new

JarOutputStream

with the specified

Manifest

. The manifest is written as the first
entry to the output stream.

**Parameters:**
- out

- the actual output stream
- man

- the optional

Manifest

**Throws:**
- IOException

- if an I/O error has occurred

---

#### public JarOutputStream​(
OutputStream
out)
throws
IOException

Creates a new

JarOutputStream

with no manifest.

**Parameters:**
- out

- the actual output stream

**Throws:**
- IOException

- if an I/O error has occurred

---

### Method Details

#### public void putNextEntry​(
ZipEntry
ze)
throws
IOException

Begins writing a new JAR file entry and positions the stream
to the start of the entry data. This method will also close
any previous entry. The default compression method will be
used if no compression method was specified for the entry.
The current time will be used if the entry has no set modification
time.

**Overrides:**
- putNextEntry

in class

ZipOutputStream

**Parameters:**
- ze

- the ZIP/JAR entry to be written

**Throws:**
- ZipException

- if a ZIP error has occurred
- IOException

- if an I/O error has occurred

---

### Additional Sections

#### Class JarOutputStream

java.lang.Object

- java.io.OutputStream
- - java.io.FilterOutputStream
- - java.util.zip.DeflaterOutputStream
- - java.util.zip.ZipOutputStream
- - java.util.jar.JarOutputStream

java.io.OutputStream

- java.io.FilterOutputStream
- - java.util.zip.DeflaterOutputStream
- - java.util.zip.ZipOutputStream
- - java.util.jar.JarOutputStream

java.io.FilterOutputStream

- java.util.zip.DeflaterOutputStream
- - java.util.zip.ZipOutputStream
- - java.util.jar.JarOutputStream

java.util.zip.DeflaterOutputStream

- java.util.zip.ZipOutputStream
- - java.util.jar.JarOutputStream

java.util.zip.ZipOutputStream

- java.util.jar.JarOutputStream

java.util.jar.JarOutputStream

**All Implemented Interfaces:** Closeable

,

Flushable

,

AutoCloseable

```java
public class
JarOutputStream

extends
ZipOutputStream
```

The

JarOutputStream

class is used to write the contents
of a JAR file to any output stream. It extends the class

java.util.zip.ZipOutputStream

with support
for writing an optional

Manifest

entry. The

Manifest

can be used to specify meta-information about
the JAR file and its entries.

**Since:** 1.2
**See Also:** Manifest

,

ZipOutputStream

public class

JarOutputStream

extends

ZipOutputStream

The

JarOutputStream

class is used to write the contents
of a JAR file to any output stream. It extends the class

java.util.zip.ZipOutputStream

with support
for writing an optional

Manifest

entry. The

Manifest

can be used to specify meta-information about
the JAR file and its entries.

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

ZipOutputStream

DEFLATED

,

STORED

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

JarOutputStream

​(

OutputStream

out)

Creates a new

JarOutputStream

with no manifest.

JarOutputStream

​(

OutputStream

out,

Manifest

man)

Creates a new

JarOutputStream

with the specified

Manifest

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

putNextEntry

​(

ZipEntry

ze)

Begins writing a new JAR file entry and positions the stream
to the start of the entry data.

- Methods declared in class java.util.zip.

ZipOutputStream

close

,

closeEntry

,

finish

,

setComment

,

setLevel

,

setMethod

,

write

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

ZipOutputStream

DEFLATED

,

STORED

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

Fields declared in class java.util.zip.

ZipOutputStream

DEFLATED

,

STORED

---

#### Fields declared in class java.util.zip. ZipOutputStream

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

JarOutputStream

​(

OutputStream

out)

Creates a new

JarOutputStream

with no manifest.

JarOutputStream

​(

OutputStream

out,

Manifest

man)

Creates a new

JarOutputStream

with the specified

Manifest

.

---

#### Constructor Summary

Creates a new

JarOutputStream

with no manifest.

Creates a new

JarOutputStream

with the specified

Manifest

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

putNextEntry

​(

ZipEntry

ze)

Begins writing a new JAR file entry and positions the stream
to the start of the entry data.

- Methods declared in class java.util.zip.

ZipOutputStream

close

,

closeEntry

,

finish

,

setComment

,

setLevel

,

setMethod

,

write

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

Begins writing a new JAR file entry and positions the stream
to the start of the entry data.

Methods declared in class java.util.zip.

ZipOutputStream

close

,

closeEntry

,

finish

,

setComment

,

setLevel

,

setMethod

,

write

---

#### Methods declared in class java.util.zip. ZipOutputStream

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

- JarOutputStream

```java
public JarOutputStream​(
OutputStream
out,

Manifest
man)
throws
IOException
```

Creates a new

JarOutputStream

with the specified

Manifest

. The manifest is written as the first
entry to the output stream.

**Parameters:** out

- the actual output stream
**Parameters:** man

- the optional

Manifest
**Throws:** IOException

- if an I/O error has occurred

- JarOutputStream

```java
public JarOutputStream​(
OutputStream
out)
throws
IOException
```

Creates a new

JarOutputStream

with no manifest.

**Parameters:** out

- the actual output stream
**Throws:** IOException

- if an I/O error has occurred

============ METHOD DETAIL ==========

- Method Detail

- putNextEntry

```java
public void putNextEntry​(
ZipEntry
ze)
throws
IOException
```

Begins writing a new JAR file entry and positions the stream
to the start of the entry data. This method will also close
any previous entry. The default compression method will be
used if no compression method was specified for the entry.
The current time will be used if the entry has no set modification
time.

**Overrides:** putNextEntry

in class

ZipOutputStream
**Parameters:** ze

- the ZIP/JAR entry to be written
**Throws:** ZipException

- if a ZIP error has occurred
**Throws:** IOException

- if an I/O error has occurred

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

- JarOutputStream

```java
public JarOutputStream​(
OutputStream
out,

Manifest
man)
throws
IOException
```

Creates a new

JarOutputStream

with the specified

Manifest

. The manifest is written as the first
entry to the output stream.

**Parameters:** out

- the actual output stream
**Parameters:** man

- the optional

Manifest
**Throws:** IOException

- if an I/O error has occurred

- JarOutputStream

```java
public JarOutputStream​(
OutputStream
out)
throws
IOException
```

Creates a new

JarOutputStream

with no manifest.

**Parameters:** out

- the actual output stream
**Throws:** IOException

- if an I/O error has occurred

---

#### Constructor Detail

JarOutputStream

```java
public JarOutputStream​(
OutputStream
out,

Manifest
man)
throws
IOException
```

Creates a new

JarOutputStream

with the specified

Manifest

. The manifest is written as the first
entry to the output stream.

**Parameters:** out

- the actual output stream
**Parameters:** man

- the optional

Manifest
**Throws:** IOException

- if an I/O error has occurred

---

#### JarOutputStream

public JarOutputStream​(

OutputStream

out,

Manifest

man)
throws

IOException

Creates a new

JarOutputStream

with the specified

Manifest

. The manifest is written as the first
entry to the output stream.

JarOutputStream

```java
public JarOutputStream​(
OutputStream
out)
throws
IOException
```

Creates a new

JarOutputStream

with no manifest.

**Parameters:** out

- the actual output stream
**Throws:** IOException

- if an I/O error has occurred

---

#### JarOutputStream

public JarOutputStream​(

OutputStream

out)
throws

IOException

Creates a new

JarOutputStream

with no manifest.

Method Detail

- putNextEntry

```java
public void putNextEntry​(
ZipEntry
ze)
throws
IOException
```

Begins writing a new JAR file entry and positions the stream
to the start of the entry data. This method will also close
any previous entry. The default compression method will be
used if no compression method was specified for the entry.
The current time will be used if the entry has no set modification
time.

**Overrides:** putNextEntry

in class

ZipOutputStream
**Parameters:** ze

- the ZIP/JAR entry to be written
**Throws:** ZipException

- if a ZIP error has occurred
**Throws:** IOException

- if an I/O error has occurred

---

#### Method Detail

putNextEntry

```java
public void putNextEntry​(
ZipEntry
ze)
throws
IOException
```

Begins writing a new JAR file entry and positions the stream
to the start of the entry data. This method will also close
any previous entry. The default compression method will be
used if no compression method was specified for the entry.
The current time will be used if the entry has no set modification
time.

**Overrides:** putNextEntry

in class

ZipOutputStream
**Parameters:** ze

- the ZIP/JAR entry to be written
**Throws:** ZipException

- if a ZIP error has occurred
**Throws:** IOException

- if an I/O error has occurred

---

#### putNextEntry

public void putNextEntry​(

ZipEntry

ze)
throws

IOException

Begins writing a new JAR file entry and positions the stream
to the start of the entry data. This method will also close
any previous entry. The default compression method will be
used if no compression method was specified for the entry.
The current time will be used if the entry has no set modification
time.

---

