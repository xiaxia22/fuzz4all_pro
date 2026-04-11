# Class JarEntry

**Source:** `java.base\java\util\jar\JarEntry.html`

### Class Description

```java
public class
JarEntry

extends
ZipEntry
```

This class is used to represent a JAR file entry.

**All Implemented Interfaces:** Cloneable

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

#### public JarEntry​(
String
name)

Creates a new

JarEntry

for the specified JAR file
entry name.

**Parameters:**
- name

- the JAR file entry name

**Throws:**
- NullPointerException

- if the entry name is

null
- IllegalArgumentException

- if the entry name is longer than
0xFFFF bytes.

---

#### public JarEntry​(
ZipEntry
ze)

Creates a new

JarEntry

with fields taken from the
specified

ZipEntry

object.

**Parameters:**
- ze

- the

ZipEntry

object to create the

JarEntry

from

---

#### public JarEntry​(
JarEntry
je)

Creates a new

JarEntry

with fields taken from the
specified

JarEntry

object.

**Parameters:**
- je

- the

JarEntry

to copy

---

### Method Details

#### public
Attributes
getAttributes()
throws
IOException

Returns the

Manifest

Attributes

for this
entry, or

null

if none.

**Returns:**
- the

Manifest

Attributes

for this
entry, or

null

if none

**Throws:**
- IOException

- if an I/O error has occurred

---

#### public
Certificate
[] getCertificates()

Returns the

Certificate

objects for this entry, or

null

if none. This method can only be called once
the

JarEntry

has been completely verified by reading
from the entry input stream until the end of the stream has been
reached. Otherwise, this method will return

null

.

The returned certificate array comprises all the signer certificates
that were used to verify this entry. Each signer certificate is
followed by its supporting certificate chain (which may be empty).
Each signer certificate and its supporting certificate chain are ordered
bottom-to-top (i.e., with the signer certificate first and the (root)
certificate authority last).

**Returns:**
- the

Certificate

objects for this entry, or

null

if none.

---

#### public
CodeSigner
[] getCodeSigners()

Returns the

CodeSigner

objects for this entry, or

null

if none. This method can only be called once
the

JarEntry

has been completely verified by reading
from the entry input stream until the end of the stream has been
reached. Otherwise, this method will return

null

.

The returned array comprises all the code signers that have signed
this entry.

**Returns:**
- the

CodeSigner

objects for this entry, or

null

if none.

**Since:**
- 1.5

---

#### public
String
getRealName()

Returns the real name of this

JarEntry

.

If this

JarEntry

is an entry of a

multi-release jar file

and the

JarFile

is configured to be processed as such, the name returned
by this method is the path name of the versioned entry that the

JarEntry

represents, rather than the path name of the base entry
that

ZipEntry.getName()

returns. If the

JarEntry

does not represent
a versioned entry of a multi-release

JarFile

or the

JarFile

is not configured for processing a multi-release jar file, this method
returns the same name that

ZipEntry.getName()

returns.

**Returns:**
- the real name of the JarEntry

**Since:**
- 10

---

### Additional Sections

#### Class JarEntry

java.lang.Object

- java.util.zip.ZipEntry
- - java.util.jar.JarEntry

java.util.zip.ZipEntry

- java.util.jar.JarEntry

java.util.jar.JarEntry

**All Implemented Interfaces:** Cloneable

```java
public class
JarEntry

extends
ZipEntry
```

This class is used to represent a JAR file entry.

**Since:** 1.2

public class

JarEntry

extends

ZipEntry

This class is used to represent a JAR file entry.

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

ZipEntry

DEFLATED

,

STORED

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

JarEntry

​(

String

name)

Creates a new

JarEntry

for the specified JAR file
entry name.

JarEntry

​(

JarEntry

je)

Creates a new

JarEntry

with fields taken from the
specified

JarEntry

object.

JarEntry

​(

ZipEntry

ze)

Creates a new

JarEntry

with fields taken from the
specified

ZipEntry

object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Attributes

getAttributes

()

Returns the

Manifest

Attributes

for this
entry, or

null

if none.

Certificate

[]

getCertificates

()

Returns the

Certificate

objects for this entry, or

null

if none.

CodeSigner

[]

getCodeSigners

()

Returns the

CodeSigner

objects for this entry, or

null

if none.

String

getRealName

()

Returns the real name of this

JarEntry

.

- Methods declared in class java.util.zip.

ZipEntry

clone

,

getComment

,

getCompressedSize

,

getCrc

,

getCreationTime

,

getExtra

,

getLastAccessTime

,

getLastModifiedTime

,

getMethod

,

getName

,

getSize

,

getTime

,

getTimeLocal

,

hashCode

,

isDirectory

,

setComment

,

setCompressedSize

,

setCrc

,

setCreationTime

,

setExtra

,

setLastAccessTime

,

setLastModifiedTime

,

setMethod

,

setSize

,

setTime

,

setTimeLocal

,

toString

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

ZipEntry

DEFLATED

,

STORED

---

#### Field Summary

Fields declared in class java.util.zip.

ZipEntry

DEFLATED

,

STORED

---

#### Fields declared in class java.util.zip. ZipEntry

Constructor Summary

Constructors

Constructor

Description

JarEntry

​(

String

name)

Creates a new

JarEntry

for the specified JAR file
entry name.

JarEntry

​(

JarEntry

je)

Creates a new

JarEntry

with fields taken from the
specified

JarEntry

object.

JarEntry

​(

ZipEntry

ze)

Creates a new

JarEntry

with fields taken from the
specified

ZipEntry

object.

---

#### Constructor Summary

Creates a new

JarEntry

for the specified JAR file
entry name.

Creates a new

JarEntry

with fields taken from the
specified

JarEntry

object.

Creates a new

JarEntry

with fields taken from the
specified

ZipEntry

object.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Attributes

getAttributes

()

Returns the

Manifest

Attributes

for this
entry, or

null

if none.

Certificate

[]

getCertificates

()

Returns the

Certificate

objects for this entry, or

null

if none.

CodeSigner

[]

getCodeSigners

()

Returns the

CodeSigner

objects for this entry, or

null

if none.

String

getRealName

()

Returns the real name of this

JarEntry

.

- Methods declared in class java.util.zip.

ZipEntry

clone

,

getComment

,

getCompressedSize

,

getCrc

,

getCreationTime

,

getExtra

,

getLastAccessTime

,

getLastModifiedTime

,

getMethod

,

getName

,

getSize

,

getTime

,

getTimeLocal

,

hashCode

,

isDirectory

,

setComment

,

setCompressedSize

,

setCrc

,

setCreationTime

,

setExtra

,

setLastAccessTime

,

setLastModifiedTime

,

setMethod

,

setSize

,

setTime

,

setTimeLocal

,

toString

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

Returns the

Manifest

Attributes

for this
entry, or

null

if none.

Returns the

Certificate

objects for this entry, or

null

if none.

Returns the

CodeSigner

objects for this entry, or

null

if none.

Returns the real name of this

JarEntry

.

Methods declared in class java.util.zip.

ZipEntry

clone

,

getComment

,

getCompressedSize

,

getCrc

,

getCreationTime

,

getExtra

,

getLastAccessTime

,

getLastModifiedTime

,

getMethod

,

getName

,

getSize

,

getTime

,

getTimeLocal

,

hashCode

,

isDirectory

,

setComment

,

setCompressedSize

,

setCrc

,

setCreationTime

,

setExtra

,

setLastAccessTime

,

setLastModifiedTime

,

setMethod

,

setSize

,

setTime

,

setTimeLocal

,

toString

---

#### Methods declared in class java.util.zip. ZipEntry

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

- JarEntry

```java
public JarEntry​(
String
name)
```

Creates a new

JarEntry

for the specified JAR file
entry name.

**Parameters:** name

- the JAR file entry name
**Throws:** NullPointerException

- if the entry name is

null
**Throws:** IllegalArgumentException

- if the entry name is longer than
0xFFFF bytes.

- JarEntry

```java
public JarEntry​(
ZipEntry
ze)
```

Creates a new

JarEntry

with fields taken from the
specified

ZipEntry

object.

**Parameters:** ze

- the

ZipEntry

object to create the

JarEntry

from

- JarEntry

```java
public JarEntry​(
JarEntry
je)
```

Creates a new

JarEntry

with fields taken from the
specified

JarEntry

object.

**Parameters:** je

- the

JarEntry

to copy

============ METHOD DETAIL ==========

- Method Detail

- getAttributes

```java
public
Attributes
getAttributes()
throws
IOException
```

Returns the

Manifest

Attributes

for this
entry, or

null

if none.

**Returns:** the

Manifest

Attributes

for this
entry, or

null

if none
**Throws:** IOException

- if an I/O error has occurred

- getCertificates

```java
public
Certificate
[] getCertificates()
```

Returns the

Certificate

objects for this entry, or

null

if none. This method can only be called once
the

JarEntry

has been completely verified by reading
from the entry input stream until the end of the stream has been
reached. Otherwise, this method will return

null

.

The returned certificate array comprises all the signer certificates
that were used to verify this entry. Each signer certificate is
followed by its supporting certificate chain (which may be empty).
Each signer certificate and its supporting certificate chain are ordered
bottom-to-top (i.e., with the signer certificate first and the (root)
certificate authority last).

**Returns:** the

Certificate

objects for this entry, or

null

if none.

- getCodeSigners

```java
public
CodeSigner
[] getCodeSigners()
```

Returns the

CodeSigner

objects for this entry, or

null

if none. This method can only be called once
the

JarEntry

has been completely verified by reading
from the entry input stream until the end of the stream has been
reached. Otherwise, this method will return

null

.

The returned array comprises all the code signers that have signed
this entry.

**Returns:** the

CodeSigner

objects for this entry, or

null

if none.
**Since:** 1.5

- getRealName

```java
public
String
getRealName()
```

Returns the real name of this

JarEntry

.

If this

JarEntry

is an entry of a

multi-release jar file

and the

JarFile

is configured to be processed as such, the name returned
by this method is the path name of the versioned entry that the

JarEntry

represents, rather than the path name of the base entry
that

ZipEntry.getName()

returns. If the

JarEntry

does not represent
a versioned entry of a multi-release

JarFile

or the

JarFile

is not configured for processing a multi-release jar file, this method
returns the same name that

ZipEntry.getName()

returns.

**Returns:** the real name of the JarEntry
**Since:** 10

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

- JarEntry

```java
public JarEntry​(
String
name)
```

Creates a new

JarEntry

for the specified JAR file
entry name.

**Parameters:** name

- the JAR file entry name
**Throws:** NullPointerException

- if the entry name is

null
**Throws:** IllegalArgumentException

- if the entry name is longer than
0xFFFF bytes.

- JarEntry

```java
public JarEntry​(
ZipEntry
ze)
```

Creates a new

JarEntry

with fields taken from the
specified

ZipEntry

object.

**Parameters:** ze

- the

ZipEntry

object to create the

JarEntry

from

- JarEntry

```java
public JarEntry​(
JarEntry
je)
```

Creates a new

JarEntry

with fields taken from the
specified

JarEntry

object.

**Parameters:** je

- the

JarEntry

to copy

---

#### Constructor Detail

JarEntry

```java
public JarEntry​(
String
name)
```

Creates a new

JarEntry

for the specified JAR file
entry name.

**Parameters:** name

- the JAR file entry name
**Throws:** NullPointerException

- if the entry name is

null
**Throws:** IllegalArgumentException

- if the entry name is longer than
0xFFFF bytes.

---

#### JarEntry

public JarEntry​(

String

name)

Creates a new

JarEntry

for the specified JAR file
entry name.

JarEntry

```java
public JarEntry​(
ZipEntry
ze)
```

Creates a new

JarEntry

with fields taken from the
specified

ZipEntry

object.

**Parameters:** ze

- the

ZipEntry

object to create the

JarEntry

from

---

#### JarEntry

public JarEntry​(

ZipEntry

ze)

Creates a new

JarEntry

with fields taken from the
specified

ZipEntry

object.

JarEntry

```java
public JarEntry​(
JarEntry
je)
```

Creates a new

JarEntry

with fields taken from the
specified

JarEntry

object.

**Parameters:** je

- the

JarEntry

to copy

---

#### JarEntry

public JarEntry​(

JarEntry

je)

Creates a new

JarEntry

with fields taken from the
specified

JarEntry

object.

Method Detail

- getAttributes

```java
public
Attributes
getAttributes()
throws
IOException
```

Returns the

Manifest

Attributes

for this
entry, or

null

if none.

**Returns:** the

Manifest

Attributes

for this
entry, or

null

if none
**Throws:** IOException

- if an I/O error has occurred

- getCertificates

```java
public
Certificate
[] getCertificates()
```

Returns the

Certificate

objects for this entry, or

null

if none. This method can only be called once
the

JarEntry

has been completely verified by reading
from the entry input stream until the end of the stream has been
reached. Otherwise, this method will return

null

.

The returned certificate array comprises all the signer certificates
that were used to verify this entry. Each signer certificate is
followed by its supporting certificate chain (which may be empty).
Each signer certificate and its supporting certificate chain are ordered
bottom-to-top (i.e., with the signer certificate first and the (root)
certificate authority last).

**Returns:** the

Certificate

objects for this entry, or

null

if none.

- getCodeSigners

```java
public
CodeSigner
[] getCodeSigners()
```

Returns the

CodeSigner

objects for this entry, or

null

if none. This method can only be called once
the

JarEntry

has been completely verified by reading
from the entry input stream until the end of the stream has been
reached. Otherwise, this method will return

null

.

The returned array comprises all the code signers that have signed
this entry.

**Returns:** the

CodeSigner

objects for this entry, or

null

if none.
**Since:** 1.5

- getRealName

```java
public
String
getRealName()
```

Returns the real name of this

JarEntry

.

If this

JarEntry

is an entry of a

multi-release jar file

and the

JarFile

is configured to be processed as such, the name returned
by this method is the path name of the versioned entry that the

JarEntry

represents, rather than the path name of the base entry
that

ZipEntry.getName()

returns. If the

JarEntry

does not represent
a versioned entry of a multi-release

JarFile

or the

JarFile

is not configured for processing a multi-release jar file, this method
returns the same name that

ZipEntry.getName()

returns.

**Returns:** the real name of the JarEntry
**Since:** 10

---

#### Method Detail

getAttributes

```java
public
Attributes
getAttributes()
throws
IOException
```

Returns the

Manifest

Attributes

for this
entry, or

null

if none.

**Returns:** the

Manifest

Attributes

for this
entry, or

null

if none
**Throws:** IOException

- if an I/O error has occurred

---

#### getAttributes

public

Attributes

getAttributes()
throws

IOException

Returns the

Manifest

Attributes

for this
entry, or

null

if none.

getCertificates

```java
public
Certificate
[] getCertificates()
```

Returns the

Certificate

objects for this entry, or

null

if none. This method can only be called once
the

JarEntry

has been completely verified by reading
from the entry input stream until the end of the stream has been
reached. Otherwise, this method will return

null

.

The returned certificate array comprises all the signer certificates
that were used to verify this entry. Each signer certificate is
followed by its supporting certificate chain (which may be empty).
Each signer certificate and its supporting certificate chain are ordered
bottom-to-top (i.e., with the signer certificate first and the (root)
certificate authority last).

**Returns:** the

Certificate

objects for this entry, or

null

if none.

---

#### getCertificates

public

Certificate

[] getCertificates()

Returns the

Certificate

objects for this entry, or

null

if none. This method can only be called once
the

JarEntry

has been completely verified by reading
from the entry input stream until the end of the stream has been
reached. Otherwise, this method will return

null

.

The returned certificate array comprises all the signer certificates
that were used to verify this entry. Each signer certificate is
followed by its supporting certificate chain (which may be empty).
Each signer certificate and its supporting certificate chain are ordered
bottom-to-top (i.e., with the signer certificate first and the (root)
certificate authority last).

The returned certificate array comprises all the signer certificates
that were used to verify this entry. Each signer certificate is
followed by its supporting certificate chain (which may be empty).
Each signer certificate and its supporting certificate chain are ordered
bottom-to-top (i.e., with the signer certificate first and the (root)
certificate authority last).

getCodeSigners

```java
public
CodeSigner
[] getCodeSigners()
```

Returns the

CodeSigner

objects for this entry, or

null

if none. This method can only be called once
the

JarEntry

has been completely verified by reading
from the entry input stream until the end of the stream has been
reached. Otherwise, this method will return

null

.

The returned array comprises all the code signers that have signed
this entry.

**Returns:** the

CodeSigner

objects for this entry, or

null

if none.
**Since:** 1.5

---

#### getCodeSigners

public

CodeSigner

[] getCodeSigners()

Returns the

CodeSigner

objects for this entry, or

null

if none. This method can only be called once
the

JarEntry

has been completely verified by reading
from the entry input stream until the end of the stream has been
reached. Otherwise, this method will return

null

.

The returned array comprises all the code signers that have signed
this entry.

The returned array comprises all the code signers that have signed
this entry.

getRealName

```java
public
String
getRealName()
```

Returns the real name of this

JarEntry

.

If this

JarEntry

is an entry of a

multi-release jar file

and the

JarFile

is configured to be processed as such, the name returned
by this method is the path name of the versioned entry that the

JarEntry

represents, rather than the path name of the base entry
that

ZipEntry.getName()

returns. If the

JarEntry

does not represent
a versioned entry of a multi-release

JarFile

or the

JarFile

is not configured for processing a multi-release jar file, this method
returns the same name that

ZipEntry.getName()

returns.

**Returns:** the real name of the JarEntry
**Since:** 10

---

#### getRealName

public

String

getRealName()

Returns the real name of this

JarEntry

.

If this

JarEntry

is an entry of a

multi-release jar file

and the

JarFile

is configured to be processed as such, the name returned
by this method is the path name of the versioned entry that the

JarEntry

represents, rather than the path name of the base entry
that

ZipEntry.getName()

returns. If the

JarEntry

does not represent
a versioned entry of a multi-release

JarFile

or the

JarFile

is not configured for processing a multi-release jar file, this method
returns the same name that

ZipEntry.getName()

returns.

---

