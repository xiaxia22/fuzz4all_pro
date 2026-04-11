# Class JarFile

**Source:** `java.base\java\util\jar\JarFile.html`

### Class Description

```java
public class
JarFile

extends
ZipFile
```

The

JarFile

class is used to read the contents of a jar file
from any file that can be opened with

java.io.RandomAccessFile

.
It extends the class

java.util.zip.ZipFile

with support
for reading an optional

Manifest

entry, and support for
processing multi-release jar files. The

Manifest

can be used
to specify meta-information about the jar file and its entries.

A multi-release jar file

is a jar file that
contains a manifest with a main attribute named "Multi-Release",
a set of "base" entries, some of which are public classes with public
or protected methods that comprise the public interface of the jar file,
and a set of "versioned" entries contained in subdirectories of the
"META-INF/versions" directory. The versioned entries are partitioned by the
major version of the Java platform. A versioned entry, with a version

n

,

8 < n

, in the "META-INF/versions/{n}" directory overrides
the base entry as well as any entry with a version number

i

where

8 < i < n

.

By default, a

JarFile

for a multi-release jar file is configured
to process the multi-release jar file as if it were a plain (unversioned) jar
file, and as such an entry name is associated with at most one base entry.
The

JarFile

may be configured to process a multi-release jar file by
creating the

JarFile

with the

JarFile(File, boolean, int, Runtime.Version)

constructor. The

Runtime.Version

object sets a maximum version used when searching for
versioned entries. When so configured, an entry name
can correspond with at most one base entry and zero or more versioned
entries. A search is required to associate the entry name with the latest
versioned entry whose version is less than or equal to the maximum version
(see

getEntry(String)

).

Class loaders that utilize

JarFile

to load classes from the
contents of

JarFile

entries should construct the

JarFile

by invoking the

JarFile(File, boolean, int, Runtime.Version)

constructor with the value

Runtime.version()

assigned to the last
argument. This assures that classes compatible with the major
version of the running JVM are loaded from multi-release jar files.

If the

verify

flag is on when opening a signed jar file, the content
of the jar entry is verified against the signature embedded inside the manifest
that is associated with its

path name

. For a
multi-release jar file, the content of a versioned entry is verfieid against
its own signature and

JarEntry.getCodeSigners()

returns its own signers.

Please note that the verification process does not include validating the
signer's certificate. A caller should inspect the return value of

JarEntry.getCodeSigners()

to further determine if the signature
can be trusted.

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

#### public static final
String
MANIFEST_NAME

The JAR manifest file name.

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

#### public JarFile​(
String
name)
throws
IOException

Creates a new

JarFile

to read from the specified
file

name

. The

JarFile

will be verified if
it is signed.

**Parameters:**
- name

- the name of the jar file to be opened for reading

**Throws:**
- IOException

- if an I/O error has occurred
- SecurityException

- if access to the file is denied
by the SecurityManager

---

#### public JarFile​(
String
name,
boolean verify)
throws
IOException

Creates a new

JarFile

to read from the specified
file

name

.

**Parameters:**
- name

- the name of the jar file to be opened for reading
- verify

- whether or not to verify the jar file if
it is signed.

**Throws:**
- IOException

- if an I/O error has occurred
- SecurityException

- if access to the file is denied
by the SecurityManager

---

#### public JarFile​(
File
file)
throws
IOException

Creates a new

JarFile

to read from the specified

File

object. The

JarFile

will be verified if
it is signed.

**Parameters:**
- file

- the jar file to be opened for reading

**Throws:**
- IOException

- if an I/O error has occurred
- SecurityException

- if access to the file is denied
by the SecurityManager

---

#### public JarFile​(
File
file,
boolean verify)
throws
IOException

Creates a new

JarFile

to read from the specified

File

object.

**Parameters:**
- file

- the jar file to be opened for reading
- verify

- whether or not to verify the jar file if
it is signed.

**Throws:**
- IOException

- if an I/O error has occurred
- SecurityException

- if access to the file is denied
by the SecurityManager.

---

#### public JarFile​(
File
file,
boolean verify,
int mode)
throws
IOException

Creates a new

JarFile

to read from the specified

File

object in the specified mode. The mode argument
must be either

OPEN_READ

or

OPEN_READ | OPEN_DELETE

.

**Parameters:**
- file

- the jar file to be opened for reading
- verify

- whether or not to verify the jar file if
it is signed.
- mode

- the mode in which the file is to be opened

**Throws:**
- IOException

- if an I/O error has occurred
- IllegalArgumentException

- if the

mode

argument is invalid
- SecurityException

- if access to the file is denied
by the SecurityManager

**Since:**
- 1.3

---

#### public JarFile​(
File
file,
boolean verify,
int mode,

Runtime.Version
version)
throws
IOException

Creates a new

JarFile

to read from the specified

File

object in the specified mode. The mode argument
must be either

OPEN_READ

or

OPEN_READ | OPEN_DELETE

.
The version argument, after being converted to a canonical form, is
used to configure the

JarFile

for processing
multi-release jar files.

The canonical form derived from the version parameter is

Runtime.Version.parse(Integer.toString(n))

where

n

is

Math.max(version.feature(), JarFile.baseVersion().feature())

.

**Parameters:**
- file

- the jar file to be opened for reading
- verify

- whether or not to verify the jar file if
it is signed.
- mode

- the mode in which the file is to be opened
- version

- specifies the release version for a multi-release jar file

**Throws:**
- IOException

- if an I/O error has occurred
- IllegalArgumentException

- if the

mode

argument is invalid
- SecurityException

- if access to the file is denied
by the SecurityManager
- NullPointerException

- if

version

is

null

**Since:**
- 9

---

### Method Details

#### public static
Runtime.Version
baseVersion()

Returns the version that represents the unversioned configuration of a
multi-release jar file.

**Returns:**
- the version that represents the unversioned configuration

**Since:**
- 9

---

#### public static
Runtime.Version
runtimeVersion()

Returns the version that represents the effective runtime versioned
configuration of a multi-release jar file.

By default the feature version number of the returned

Version

will
be equal to the feature version number of

Runtime.version()

.
However, if the

jdk.util.jar.version

property is set, the
returned

Version

is derived from that property and feature version
numbers may not be equal.

**Returns:**
- the version that represents the runtime versioned configuration

**Since:**
- 9

---

#### public final
Runtime.Version
getVersion()

Returns the maximum version used when searching for versioned entries.

If this

JarFile

is not a multi-release jar file or is not
configured to be processed as such, then the version returned will be the
same as that returned from

baseVersion()

.

**Returns:**
- the maximum version

**Since:**
- 9

---

#### public final boolean isMultiRelease()

Indicates whether or not this jar file is a multi-release jar file.

**Returns:**
- true if this JarFile is a multi-release jar file

**Since:**
- 9

---

#### public
Manifest
getManifest()
throws
IOException

Returns the jar file manifest, or

null

if none.

**Returns:**
- the jar file manifest, or

null

if none

**Throws:**
- IllegalStateException

- may be thrown if the jar file has been closed
- IOException

- if an I/O error has occurred

---

#### public
JarEntry
getJarEntry​(
String
name)

Returns the

JarEntry

for the given base entry name or

null

if not found.

If this

JarFile

is a multi-release jar file and is configured
to be processed as such, then a search is performed to find and return
a

JarEntry

that is the latest versioned entry associated with the
given entry name. The returned

JarEntry

is the versioned entry
corresponding to the given base entry name prefixed with the string

"META-INF/versions/{n}/"

, for the largest value of

n

for
which an entry exists. If such a versioned entry does not exist, then
the

JarEntry

for the base entry is returned, otherwise

null

is returned if no entries are found. The initial value for
the version

n

is the maximum version as returned by the method

getVersion()

.

**Parameters:**
- name

- the jar file entry name

**Returns:**
- the

JarEntry

for the given entry name, or
the versioned entry name, or

null

if not found

**Throws:**
- IllegalStateException

- may be thrown if the jar file has been closed

**See Also:**
- JarEntry

**Implementation Requirements:**
- This implementation invokes

getEntry(String)

.

---

#### public
ZipEntry
getEntry​(
String
name)

Returns the

ZipEntry

for the given base entry name or

null

if not found.

If this

JarFile

is a multi-release jar file and is configured
to be processed as such, then a search is performed to find and return
a

ZipEntry

that is the latest versioned entry associated with the
given entry name. The returned

ZipEntry

is the versioned entry
corresponding to the given base entry name prefixed with the string

"META-INF/versions/{n}/"

, for the largest value of

n

for
which an entry exists. If such a versioned entry does not exist, then
the

ZipEntry

for the base entry is returned, otherwise

null

is returned if no entries are found. The initial value for
the version

n

is the maximum version as returned by the method

getVersion()

.

**Overrides:**
- getEntry

in class

ZipFile

**Parameters:**
- name

- the jar file entry name

**Returns:**
- the

ZipEntry

for the given entry name or
the versioned entry name or

null

if not found

**Throws:**
- IllegalStateException

- may be thrown if the jar file has been closed

**See Also:**
- ZipEntry

**Implementation Requirements:**
- This implementation may return a versioned entry for the requested name
even if there is not a corresponding base entry. This can occur
if there is a private or package-private versioned entry that matches.
If a subclass overrides this method, assure that the override method
invokes

super.getEntry(name)

to obtain all versioned entries.

---

#### public
Enumeration
<
JarEntry
> entries()

Returns an enumeration of the jar file entries.

**Overrides:**
- entries

in class

ZipFile

**Returns:**
- an enumeration of the jar file entries

**Throws:**
- IllegalStateException

- may be thrown if the jar file has been closed

---

#### public
Stream
<
JarEntry
> stream()

Returns an ordered

Stream

over the jar file entries.
Entries appear in the

Stream

in the order they appear in
the central directory of the jar file.

**Overrides:**
- stream

in class

ZipFile

**Returns:**
- an ordered

Stream

of entries in this jar file

**Throws:**
- IllegalStateException

- if the jar file has been closed

**Since:**
- 1.8

---

#### public
Stream
<
JarEntry
> versionedStream()

Returns a

Stream

of the versioned jar file entries.

If this

JarFile

is a multi-release jar file and is configured to
be processed as such, then an entry in the stream is the latest versioned entry
associated with the corresponding base entry name. The maximum version of the
latest versioned entry is the version returned by

getVersion()

.
The returned stream may include an entry that only exists as a versioned entry.

If the jar file is not a multi-release jar file or the

JarFile

is not
configured for processing a multi-release jar file, this method returns the
same stream that

stream()

returns.

**Returns:**
- stream of versioned entries

**Since:**
- 10

---

#### public
InputStream
getInputStream​(
ZipEntry
ze)
throws
IOException

Returns an input stream for reading the contents of the specified
zip file entry.

**Overrides:**
- getInputStream

in class

ZipFile

**Parameters:**
- ze

- the zip file entry

**Returns:**
- an input stream for reading the contents of the specified
zip file entry

**Throws:**
- ZipException

- if a zip file format error has occurred
- IOException

- if an I/O error has occurred
- SecurityException

- if any of the jar file entries
are incorrectly signed.
- IllegalStateException

- may be thrown if the jar file has been closed

---

### Additional Sections

#### Class JarFile

java.lang.Object

- java.util.zip.ZipFile
- - java.util.jar.JarFile

java.util.zip.ZipFile

- java.util.jar.JarFile

java.util.jar.JarFile

**All Implemented Interfaces:** Closeable

,

AutoCloseable

```java
public class
JarFile

extends
ZipFile
```

The

JarFile

class is used to read the contents of a jar file
from any file that can be opened with

java.io.RandomAccessFile

.
It extends the class

java.util.zip.ZipFile

with support
for reading an optional

Manifest

entry, and support for
processing multi-release jar files. The

Manifest

can be used
to specify meta-information about the jar file and its entries.

A multi-release jar file

is a jar file that
contains a manifest with a main attribute named "Multi-Release",
a set of "base" entries, some of which are public classes with public
or protected methods that comprise the public interface of the jar file,
and a set of "versioned" entries contained in subdirectories of the
"META-INF/versions" directory. The versioned entries are partitioned by the
major version of the Java platform. A versioned entry, with a version

n

,

8 < n

, in the "META-INF/versions/{n}" directory overrides
the base entry as well as any entry with a version number

i

where

8 < i < n

.

By default, a

JarFile

for a multi-release jar file is configured
to process the multi-release jar file as if it were a plain (unversioned) jar
file, and as such an entry name is associated with at most one base entry.
The

JarFile

may be configured to process a multi-release jar file by
creating the

JarFile

with the

JarFile(File, boolean, int, Runtime.Version)

constructor. The

Runtime.Version

object sets a maximum version used when searching for
versioned entries. When so configured, an entry name
can correspond with at most one base entry and zero or more versioned
entries. A search is required to associate the entry name with the latest
versioned entry whose version is less than or equal to the maximum version
(see

getEntry(String)

).

Class loaders that utilize

JarFile

to load classes from the
contents of

JarFile

entries should construct the

JarFile

by invoking the

JarFile(File, boolean, int, Runtime.Version)

constructor with the value

Runtime.version()

assigned to the last
argument. This assures that classes compatible with the major
version of the running JVM are loaded from multi-release jar files.

If the

verify

flag is on when opening a signed jar file, the content
of the jar entry is verified against the signature embedded inside the manifest
that is associated with its

path name

. For a
multi-release jar file, the content of a versioned entry is verfieid against
its own signature and

JarEntry.getCodeSigners()

returns its own signers.

Please note that the verification process does not include validating the
signer's certificate. A caller should inspect the return value of

JarEntry.getCodeSigners()

to further determine if the signature
can be trusted.

Unless otherwise noted, passing a

null

argument to a constructor
or method in this class will cause a

NullPointerException

to be
thrown.

**Implementation Note:** If the API can not be used to configure a

JarFile

(e.g. to override
the configuration of a compiled application or library), two

System

properties are available.

- jdk.util.jar.version

can be assigned a value that is the

String

representation of a non-negative integer

<= Runtime.version().feature()

. The value is used to set the effective
runtime version to something other than the default value obtained by
evaluating

Runtime.version().feature()

. The effective runtime version
is the version that the

JarFile(File, boolean, int, Runtime.Version)

constructor uses when the value of the last argument is

JarFile.runtimeVersion()

.
- jdk.util.jar.enableMultiRelease

can be assigned one of the three

String

values

true

,

false

, or

force

. The
value

true

, the default value, enables multi-release jar file
processing. The value

false

disables multi-release jar processing,
ignoring the "Multi-Release" manifest attribute, and the versioned
directories in a multi-release jar file if they exist. Furthermore,
the method

isMultiRelease()

returns

false

. The value

force

causes the

JarFile

to be initialized to runtime
versioning after construction. It effectively does the same as this code:

(new JarFile(File, boolean, int, JarFile.runtimeVersion())

.
**Since:** 1.2
**See Also:** Manifest

,

ZipFile

,

JarEntry

public class

JarFile

extends

ZipFile

The

JarFile

class is used to read the contents of a jar file
from any file that can be opened with

java.io.RandomAccessFile

.
It extends the class

java.util.zip.ZipFile

with support
for reading an optional

Manifest

entry, and support for
processing multi-release jar files. The

Manifest

can be used
to specify meta-information about the jar file and its entries.

A multi-release jar file

is a jar file that
contains a manifest with a main attribute named "Multi-Release",
a set of "base" entries, some of which are public classes with public
or protected methods that comprise the public interface of the jar file,
and a set of "versioned" entries contained in subdirectories of the
"META-INF/versions" directory. The versioned entries are partitioned by the
major version of the Java platform. A versioned entry, with a version

n

,

8 < n

, in the "META-INF/versions/{n}" directory overrides
the base entry as well as any entry with a version number

i

where

8 < i < n

.

By default, a

JarFile

for a multi-release jar file is configured
to process the multi-release jar file as if it were a plain (unversioned) jar
file, and as such an entry name is associated with at most one base entry.
The

JarFile

may be configured to process a multi-release jar file by
creating the

JarFile

with the

JarFile(File, boolean, int, Runtime.Version)

constructor. The

Runtime.Version

object sets a maximum version used when searching for
versioned entries. When so configured, an entry name
can correspond with at most one base entry and zero or more versioned
entries. A search is required to associate the entry name with the latest
versioned entry whose version is less than or equal to the maximum version
(see

getEntry(String)

).

Class loaders that utilize

JarFile

to load classes from the
contents of

JarFile

entries should construct the

JarFile

by invoking the

JarFile(File, boolean, int, Runtime.Version)

constructor with the value

Runtime.version()

assigned to the last
argument. This assures that classes compatible with the major
version of the running JVM are loaded from multi-release jar files.

If the

verify

flag is on when opening a signed jar file, the content
of the jar entry is verified against the signature embedded inside the manifest
that is associated with its

path name

. For a
multi-release jar file, the content of a versioned entry is verfieid against
its own signature and

JarEntry.getCodeSigners()

returns its own signers.

Please note that the verification process does not include validating the
signer's certificate. A caller should inspect the return value of

JarEntry.getCodeSigners()

to further determine if the signature
can be trusted.

Unless otherwise noted, passing a

null

argument to a constructor
or method in this class will cause a

NullPointerException

to be
thrown.

A multi-release jar file

is a jar file that
contains a manifest with a main attribute named "Multi-Release",
a set of "base" entries, some of which are public classes with public
or protected methods that comprise the public interface of the jar file,
and a set of "versioned" entries contained in subdirectories of the
"META-INF/versions" directory. The versioned entries are partitioned by the
major version of the Java platform. A versioned entry, with a version

n

,

8 < n

, in the "META-INF/versions/{n}" directory overrides
the base entry as well as any entry with a version number

i

where

8 < i < n

.

By default, a

JarFile

for a multi-release jar file is configured
to process the multi-release jar file as if it were a plain (unversioned) jar
file, and as such an entry name is associated with at most one base entry.
The

JarFile

may be configured to process a multi-release jar file by
creating the

JarFile

with the

JarFile(File, boolean, int, Runtime.Version)

constructor. The

Runtime.Version

object sets a maximum version used when searching for
versioned entries. When so configured, an entry name
can correspond with at most one base entry and zero or more versioned
entries. A search is required to associate the entry name with the latest
versioned entry whose version is less than or equal to the maximum version
(see

getEntry(String)

).

Class loaders that utilize

JarFile

to load classes from the
contents of

JarFile

entries should construct the

JarFile

by invoking the

JarFile(File, boolean, int, Runtime.Version)

constructor with the value

Runtime.version()

assigned to the last
argument. This assures that classes compatible with the major
version of the running JVM are loaded from multi-release jar files.

If the

verify

flag is on when opening a signed jar file, the content
of the jar entry is verified against the signature embedded inside the manifest
that is associated with its

path name

. For a
multi-release jar file, the content of a versioned entry is verfieid against
its own signature and

JarEntry.getCodeSigners()

returns its own signers.

Please note that the verification process does not include validating the
signer's certificate. A caller should inspect the return value of

JarEntry.getCodeSigners()

to further determine if the signature
can be trusted.

Unless otherwise noted, passing a

null

argument to a constructor
or method in this class will cause a

NullPointerException

to be
thrown.

By default, a

JarFile

for a multi-release jar file is configured
to process the multi-release jar file as if it were a plain (unversioned) jar
file, and as such an entry name is associated with at most one base entry.
The

JarFile

may be configured to process a multi-release jar file by
creating the

JarFile

with the

JarFile(File, boolean, int, Runtime.Version)

constructor. The

Runtime.Version

object sets a maximum version used when searching for
versioned entries. When so configured, an entry name
can correspond with at most one base entry and zero or more versioned
entries. A search is required to associate the entry name with the latest
versioned entry whose version is less than or equal to the maximum version
(see

getEntry(String)

).

Class loaders that utilize

JarFile

to load classes from the
contents of

JarFile

entries should construct the

JarFile

by invoking the

JarFile(File, boolean, int, Runtime.Version)

constructor with the value

Runtime.version()

assigned to the last
argument. This assures that classes compatible with the major
version of the running JVM are loaded from multi-release jar files.

If the

verify

flag is on when opening a signed jar file, the content
of the jar entry is verified against the signature embedded inside the manifest
that is associated with its

path name

. For a
multi-release jar file, the content of a versioned entry is verfieid against
its own signature and

JarEntry.getCodeSigners()

returns its own signers.

Please note that the verification process does not include validating the
signer's certificate. A caller should inspect the return value of

JarEntry.getCodeSigners()

to further determine if the signature
can be trusted.

Unless otherwise noted, passing a

null

argument to a constructor
or method in this class will cause a

NullPointerException

to be
thrown.

Class loaders that utilize

JarFile

to load classes from the
contents of

JarFile

entries should construct the

JarFile

by invoking the

JarFile(File, boolean, int, Runtime.Version)

constructor with the value

Runtime.version()

assigned to the last
argument. This assures that classes compatible with the major
version of the running JVM are loaded from multi-release jar files.

If the

verify

flag is on when opening a signed jar file, the content
of the jar entry is verified against the signature embedded inside the manifest
that is associated with its

path name

. For a
multi-release jar file, the content of a versioned entry is verfieid against
its own signature and

JarEntry.getCodeSigners()

returns its own signers.

Please note that the verification process does not include validating the
signer's certificate. A caller should inspect the return value of

JarEntry.getCodeSigners()

to further determine if the signature
can be trusted.

Unless otherwise noted, passing a

null

argument to a constructor
or method in this class will cause a

NullPointerException

to be
thrown.

If the

verify

flag is on when opening a signed jar file, the content
of the jar entry is verified against the signature embedded inside the manifest
that is associated with its

path name

. For a
multi-release jar file, the content of a versioned entry is verfieid against
its own signature and

JarEntry.getCodeSigners()

returns its own signers.

Please note that the verification process does not include validating the
signer's certificate. A caller should inspect the return value of

JarEntry.getCodeSigners()

to further determine if the signature
can be trusted.

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

If the API can not be used to configure a

JarFile

(e.g. to override
the configuration of a compiled application or library), two

System

properties are available.

- jdk.util.jar.version

can be assigned a value that is the

String

representation of a non-negative integer

<= Runtime.version().feature()

. The value is used to set the effective
runtime version to something other than the default value obtained by
evaluating

Runtime.version().feature()

. The effective runtime version
is the version that the

JarFile(File, boolean, int, Runtime.Version)

constructor uses when the value of the last argument is

JarFile.runtimeVersion()

.
- jdk.util.jar.enableMultiRelease

can be assigned one of the three

String

values

true

,

false

, or

force

. The
value

true

, the default value, enables multi-release jar file
processing. The value

false

disables multi-release jar processing,
ignoring the "Multi-Release" manifest attribute, and the versioned
directories in a multi-release jar file if they exist. Furthermore,
the method

isMultiRelease()

returns

false

. The value

force

causes the

JarFile

to be initialized to runtime
versioning after construction. It effectively does the same as this code:

(new JarFile(File, boolean, int, JarFile.runtimeVersion())

.

jdk.util.jar.version

can be assigned a value that is the

String

representation of a non-negative integer

<= Runtime.version().feature()

. The value is used to set the effective
runtime version to something other than the default value obtained by
evaluating

Runtime.version().feature()

. The effective runtime version
is the version that the

JarFile(File, boolean, int, Runtime.Version)

constructor uses when the value of the last argument is

JarFile.runtimeVersion()

.

jdk.util.jar.enableMultiRelease

can be assigned one of the three

String

values

true

,

false

, or

force

. The
value

true

, the default value, enables multi-release jar file
processing. The value

false

disables multi-release jar processing,
ignoring the "Multi-Release" manifest attribute, and the versioned
directories in a multi-release jar file if they exist. Furthermore,
the method

isMultiRelease()

returns

false

. The value

force

causes the

JarFile

to be initialized to runtime
versioning after construction. It effectively does the same as this code:

(new JarFile(File, boolean, int, JarFile.runtimeVersion())

.

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

static

String

MANIFEST_NAME

The JAR manifest file name.

- Fields declared in class java.util.zip.

ZipFile

OPEN_DELETE

,

OPEN_READ

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

JarFile

​(

File

file)

Creates a new

JarFile

to read from the specified

File

object.

JarFile

​(

File

file,
boolean verify)

Creates a new

JarFile

to read from the specified

File

object.

JarFile

​(

File

file,
boolean verify,
int mode)

Creates a new

JarFile

to read from the specified

File

object in the specified mode.

JarFile

​(

File

file,
boolean verify,
int mode,

Runtime.Version

version)

Creates a new

JarFile

to read from the specified

File

object in the specified mode.

JarFile

​(

String

name)

Creates a new

JarFile

to read from the specified
file

name

.

JarFile

​(

String

name,
boolean verify)

Creates a new

JarFile

to read from the specified
file

name

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

Runtime.Version

baseVersion

()

Returns the version that represents the unversioned configuration of a
multi-release jar file.

Enumeration

<

JarEntry

>

entries

()

Returns an enumeration of the jar file entries.

ZipEntry

getEntry

​(

String

name)

Returns the

ZipEntry

for the given base entry name or

null

if not found.

InputStream

getInputStream

​(

ZipEntry

ze)

Returns an input stream for reading the contents of the specified
zip file entry.

JarEntry

getJarEntry

​(

String

name)

Returns the

JarEntry

for the given base entry name or

null

if not found.

Manifest

getManifest

()

Returns the jar file manifest, or

null

if none.

Runtime.Version

getVersion

()

Returns the maximum version used when searching for versioned entries.

boolean

isMultiRelease

()

Indicates whether or not this jar file is a multi-release jar file.

static

Runtime.Version

runtimeVersion

()

Returns the version that represents the effective runtime versioned
configuration of a multi-release jar file.

Stream

<

JarEntry

>

stream

()

Returns an ordered

Stream

over the jar file entries.

Stream

<

JarEntry

>

versionedStream

()

Returns a

Stream

of the versioned jar file entries.

- Methods declared in class java.util.zip.

ZipFile

close

,

finalize

,

getComment

,

getName

,

size

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

static

String

MANIFEST_NAME

The JAR manifest file name.

- Fields declared in class java.util.zip.

ZipFile

OPEN_DELETE

,

OPEN_READ

---

#### Field Summary

The JAR manifest file name.

Fields declared in class java.util.zip.

ZipFile

OPEN_DELETE

,

OPEN_READ

---

#### Fields declared in class java.util.zip. ZipFile

Constructor Summary

Constructors

Constructor

Description

JarFile

​(

File

file)

Creates a new

JarFile

to read from the specified

File

object.

JarFile

​(

File

file,
boolean verify)

Creates a new

JarFile

to read from the specified

File

object.

JarFile

​(

File

file,
boolean verify,
int mode)

Creates a new

JarFile

to read from the specified

File

object in the specified mode.

JarFile

​(

File

file,
boolean verify,
int mode,

Runtime.Version

version)

Creates a new

JarFile

to read from the specified

File

object in the specified mode.

JarFile

​(

String

name)

Creates a new

JarFile

to read from the specified
file

name

.

JarFile

​(

String

name,
boolean verify)

Creates a new

JarFile

to read from the specified
file

name

.

---

#### Constructor Summary

Creates a new

JarFile

to read from the specified

File

object.

Creates a new

JarFile

to read from the specified

File

object in the specified mode.

Creates a new

JarFile

to read from the specified
file

name

.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

Runtime.Version

baseVersion

()

Returns the version that represents the unversioned configuration of a
multi-release jar file.

Enumeration

<

JarEntry

>

entries

()

Returns an enumeration of the jar file entries.

ZipEntry

getEntry

​(

String

name)

Returns the

ZipEntry

for the given base entry name or

null

if not found.

InputStream

getInputStream

​(

ZipEntry

ze)

Returns an input stream for reading the contents of the specified
zip file entry.

JarEntry

getJarEntry

​(

String

name)

Returns the

JarEntry

for the given base entry name or

null

if not found.

Manifest

getManifest

()

Returns the jar file manifest, or

null

if none.

Runtime.Version

getVersion

()

Returns the maximum version used when searching for versioned entries.

boolean

isMultiRelease

()

Indicates whether or not this jar file is a multi-release jar file.

static

Runtime.Version

runtimeVersion

()

Returns the version that represents the effective runtime versioned
configuration of a multi-release jar file.

Stream

<

JarEntry

>

stream

()

Returns an ordered

Stream

over the jar file entries.

Stream

<

JarEntry

>

versionedStream

()

Returns a

Stream

of the versioned jar file entries.

- Methods declared in class java.util.zip.

ZipFile

close

,

finalize

,

getComment

,

getName

,

size

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

Returns the version that represents the unversioned configuration of a
multi-release jar file.

Returns an enumeration of the jar file entries.

Returns the

ZipEntry

for the given base entry name or

null

if not found.

Returns an input stream for reading the contents of the specified
zip file entry.

Returns the

JarEntry

for the given base entry name or

null

if not found.

Returns the jar file manifest, or

null

if none.

Returns the maximum version used when searching for versioned entries.

Indicates whether or not this jar file is a multi-release jar file.

Returns the version that represents the effective runtime versioned
configuration of a multi-release jar file.

Returns an ordered

Stream

over the jar file entries.

Returns a

Stream

of the versioned jar file entries.

Methods declared in class java.util.zip.

ZipFile

close

,

finalize

,

getComment

,

getName

,

size

---

#### Methods declared in class java.util.zip. ZipFile

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

- MANIFEST_NAME

```java
public static final
String
MANIFEST_NAME
```

The JAR manifest file name.

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

- JarFile

```java
public JarFile​(
String
name)
throws
IOException
```

Creates a new

JarFile

to read from the specified
file

name

. The

JarFile

will be verified if
it is signed.

**Parameters:** name

- the name of the jar file to be opened for reading
**Throws:** IOException

- if an I/O error has occurred
**Throws:** SecurityException

- if access to the file is denied
by the SecurityManager

- JarFile

```java
public JarFile​(
String
name,
boolean verify)
throws
IOException
```

Creates a new

JarFile

to read from the specified
file

name

.

**Parameters:** name

- the name of the jar file to be opened for reading
**Parameters:** verify

- whether or not to verify the jar file if
it is signed.
**Throws:** IOException

- if an I/O error has occurred
**Throws:** SecurityException

- if access to the file is denied
by the SecurityManager

- JarFile

```java
public JarFile​(
File
file)
throws
IOException
```

Creates a new

JarFile

to read from the specified

File

object. The

JarFile

will be verified if
it is signed.

**Parameters:** file

- the jar file to be opened for reading
**Throws:** IOException

- if an I/O error has occurred
**Throws:** SecurityException

- if access to the file is denied
by the SecurityManager

- JarFile

```java
public JarFile​(
File
file,
boolean verify)
throws
IOException
```

Creates a new

JarFile

to read from the specified

File

object.

**Parameters:** file

- the jar file to be opened for reading
**Parameters:** verify

- whether or not to verify the jar file if
it is signed.
**Throws:** IOException

- if an I/O error has occurred
**Throws:** SecurityException

- if access to the file is denied
by the SecurityManager.

- JarFile

```java
public JarFile​(
File
file,
boolean verify,
int mode)
throws
IOException
```

Creates a new

JarFile

to read from the specified

File

object in the specified mode. The mode argument
must be either

OPEN_READ

or

OPEN_READ | OPEN_DELETE

.

**Parameters:** file

- the jar file to be opened for reading
**Parameters:** verify

- whether or not to verify the jar file if
it is signed.
**Parameters:** mode

- the mode in which the file is to be opened
**Throws:** IOException

- if an I/O error has occurred
**Throws:** IllegalArgumentException

- if the

mode

argument is invalid
**Throws:** SecurityException

- if access to the file is denied
by the SecurityManager
**Since:** 1.3

- JarFile

```java
public JarFile​(
File
file,
boolean verify,
int mode,

Runtime.Version
version)
throws
IOException
```

Creates a new

JarFile

to read from the specified

File

object in the specified mode. The mode argument
must be either

OPEN_READ

or

OPEN_READ | OPEN_DELETE

.
The version argument, after being converted to a canonical form, is
used to configure the

JarFile

for processing
multi-release jar files.

The canonical form derived from the version parameter is

Runtime.Version.parse(Integer.toString(n))

where

n

is

Math.max(version.feature(), JarFile.baseVersion().feature())

.

**Parameters:** file

- the jar file to be opened for reading
**Parameters:** verify

- whether or not to verify the jar file if
it is signed.
**Parameters:** mode

- the mode in which the file is to be opened
**Parameters:** version

- specifies the release version for a multi-release jar file
**Throws:** IOException

- if an I/O error has occurred
**Throws:** IllegalArgumentException

- if the

mode

argument is invalid
**Throws:** SecurityException

- if access to the file is denied
by the SecurityManager
**Throws:** NullPointerException

- if

version

is

null
**Since:** 9

============ METHOD DETAIL ==========

- Method Detail

- baseVersion

```java
public static
Runtime.Version
baseVersion()
```

Returns the version that represents the unversioned configuration of a
multi-release jar file.

**Returns:** the version that represents the unversioned configuration
**Since:** 9

- runtimeVersion

```java
public static
Runtime.Version
runtimeVersion()
```

Returns the version that represents the effective runtime versioned
configuration of a multi-release jar file.

By default the feature version number of the returned

Version

will
be equal to the feature version number of

Runtime.version()

.
However, if the

jdk.util.jar.version

property is set, the
returned

Version

is derived from that property and feature version
numbers may not be equal.

**Returns:** the version that represents the runtime versioned configuration
**Since:** 9

- getVersion

```java
public final
Runtime.Version
getVersion()
```

Returns the maximum version used when searching for versioned entries.

If this

JarFile

is not a multi-release jar file or is not
configured to be processed as such, then the version returned will be the
same as that returned from

baseVersion()

.

**Returns:** the maximum version
**Since:** 9

- isMultiRelease

```java
public final boolean isMultiRelease()
```

Indicates whether or not this jar file is a multi-release jar file.

**Returns:** true if this JarFile is a multi-release jar file
**Since:** 9

- getManifest

```java
public
Manifest
getManifest()
throws
IOException
```

Returns the jar file manifest, or

null

if none.

**Returns:** the jar file manifest, or

null

if none
**Throws:** IllegalStateException

- may be thrown if the jar file has been closed
**Throws:** IOException

- if an I/O error has occurred

- getJarEntry

```java
public
JarEntry
getJarEntry​(
String
name)
```

Returns the

JarEntry

for the given base entry name or

null

if not found.

If this

JarFile

is a multi-release jar file and is configured
to be processed as such, then a search is performed to find and return
a

JarEntry

that is the latest versioned entry associated with the
given entry name. The returned

JarEntry

is the versioned entry
corresponding to the given base entry name prefixed with the string

"META-INF/versions/{n}/"

, for the largest value of

n

for
which an entry exists. If such a versioned entry does not exist, then
the

JarEntry

for the base entry is returned, otherwise

null

is returned if no entries are found. The initial value for
the version

n

is the maximum version as returned by the method

getVersion()

.

**Implementation Requirements:** This implementation invokes

getEntry(String)

.
**Parameters:** name

- the jar file entry name
**Returns:** the

JarEntry

for the given entry name, or
the versioned entry name, or

null

if not found
**Throws:** IllegalStateException

- may be thrown if the jar file has been closed
**See Also:** JarEntry

- getEntry

```java
public
ZipEntry
getEntry​(
String
name)
```

Returns the

ZipEntry

for the given base entry name or

null

if not found.

If this

JarFile

is a multi-release jar file and is configured
to be processed as such, then a search is performed to find and return
a

ZipEntry

that is the latest versioned entry associated with the
given entry name. The returned

ZipEntry

is the versioned entry
corresponding to the given base entry name prefixed with the string

"META-INF/versions/{n}/"

, for the largest value of

n

for
which an entry exists. If such a versioned entry does not exist, then
the

ZipEntry

for the base entry is returned, otherwise

null

is returned if no entries are found. The initial value for
the version

n

is the maximum version as returned by the method

getVersion()

.

**Overrides:** getEntry

in class

ZipFile
**Implementation Requirements:** This implementation may return a versioned entry for the requested name
even if there is not a corresponding base entry. This can occur
if there is a private or package-private versioned entry that matches.
If a subclass overrides this method, assure that the override method
invokes

super.getEntry(name)

to obtain all versioned entries.
**Parameters:** name

- the jar file entry name
**Returns:** the

ZipEntry

for the given entry name or
the versioned entry name or

null

if not found
**Throws:** IllegalStateException

- may be thrown if the jar file has been closed
**See Also:** ZipEntry

- entries

```java
public
Enumeration
<
JarEntry
> entries()
```

Returns an enumeration of the jar file entries.

**Overrides:** entries

in class

ZipFile
**Returns:** an enumeration of the jar file entries
**Throws:** IllegalStateException

- may be thrown if the jar file has been closed

- stream

```java
public
Stream
<
JarEntry
> stream()
```

Returns an ordered

Stream

over the jar file entries.
Entries appear in the

Stream

in the order they appear in
the central directory of the jar file.

**Overrides:** stream

in class

ZipFile
**Returns:** an ordered

Stream

of entries in this jar file
**Throws:** IllegalStateException

- if the jar file has been closed
**Since:** 1.8

- versionedStream

```java
public
Stream
<
JarEntry
> versionedStream()
```

Returns a

Stream

of the versioned jar file entries.

If this

JarFile

is a multi-release jar file and is configured to
be processed as such, then an entry in the stream is the latest versioned entry
associated with the corresponding base entry name. The maximum version of the
latest versioned entry is the version returned by

getVersion()

.
The returned stream may include an entry that only exists as a versioned entry.

If the jar file is not a multi-release jar file or the

JarFile

is not
configured for processing a multi-release jar file, this method returns the
same stream that

stream()

returns.

**Returns:** stream of versioned entries
**Since:** 10

- getInputStream

```java
public
InputStream
getInputStream​(
ZipEntry
ze)
throws
IOException
```

Returns an input stream for reading the contents of the specified
zip file entry.

**Overrides:** getInputStream

in class

ZipFile
**Parameters:** ze

- the zip file entry
**Returns:** an input stream for reading the contents of the specified
zip file entry
**Throws:** ZipException

- if a zip file format error has occurred
**Throws:** IOException

- if an I/O error has occurred
**Throws:** SecurityException

- if any of the jar file entries
are incorrectly signed.
**Throws:** IllegalStateException

- may be thrown if the jar file has been closed

Field Detail

- MANIFEST_NAME

```java
public static final
String
MANIFEST_NAME
```

The JAR manifest file name.

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

MANIFEST_NAME

```java
public static final
String
MANIFEST_NAME
```

The JAR manifest file name.

**See Also:** Constant Field Values

---

#### MANIFEST_NAME

public static final

String

MANIFEST_NAME

The JAR manifest file name.

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

- JarFile

```java
public JarFile​(
String
name)
throws
IOException
```

Creates a new

JarFile

to read from the specified
file

name

. The

JarFile

will be verified if
it is signed.

**Parameters:** name

- the name of the jar file to be opened for reading
**Throws:** IOException

- if an I/O error has occurred
**Throws:** SecurityException

- if access to the file is denied
by the SecurityManager

- JarFile

```java
public JarFile​(
String
name,
boolean verify)
throws
IOException
```

Creates a new

JarFile

to read from the specified
file

name

.

**Parameters:** name

- the name of the jar file to be opened for reading
**Parameters:** verify

- whether or not to verify the jar file if
it is signed.
**Throws:** IOException

- if an I/O error has occurred
**Throws:** SecurityException

- if access to the file is denied
by the SecurityManager

- JarFile

```java
public JarFile​(
File
file)
throws
IOException
```

Creates a new

JarFile

to read from the specified

File

object. The

JarFile

will be verified if
it is signed.

**Parameters:** file

- the jar file to be opened for reading
**Throws:** IOException

- if an I/O error has occurred
**Throws:** SecurityException

- if access to the file is denied
by the SecurityManager

- JarFile

```java
public JarFile​(
File
file,
boolean verify)
throws
IOException
```

Creates a new

JarFile

to read from the specified

File

object.

**Parameters:** file

- the jar file to be opened for reading
**Parameters:** verify

- whether or not to verify the jar file if
it is signed.
**Throws:** IOException

- if an I/O error has occurred
**Throws:** SecurityException

- if access to the file is denied
by the SecurityManager.

- JarFile

```java
public JarFile​(
File
file,
boolean verify,
int mode)
throws
IOException
```

Creates a new

JarFile

to read from the specified

File

object in the specified mode. The mode argument
must be either

OPEN_READ

or

OPEN_READ | OPEN_DELETE

.

**Parameters:** file

- the jar file to be opened for reading
**Parameters:** verify

- whether or not to verify the jar file if
it is signed.
**Parameters:** mode

- the mode in which the file is to be opened
**Throws:** IOException

- if an I/O error has occurred
**Throws:** IllegalArgumentException

- if the

mode

argument is invalid
**Throws:** SecurityException

- if access to the file is denied
by the SecurityManager
**Since:** 1.3

- JarFile

```java
public JarFile​(
File
file,
boolean verify,
int mode,

Runtime.Version
version)
throws
IOException
```

Creates a new

JarFile

to read from the specified

File

object in the specified mode. The mode argument
must be either

OPEN_READ

or

OPEN_READ | OPEN_DELETE

.
The version argument, after being converted to a canonical form, is
used to configure the

JarFile

for processing
multi-release jar files.

The canonical form derived from the version parameter is

Runtime.Version.parse(Integer.toString(n))

where

n

is

Math.max(version.feature(), JarFile.baseVersion().feature())

.

**Parameters:** file

- the jar file to be opened for reading
**Parameters:** verify

- whether or not to verify the jar file if
it is signed.
**Parameters:** mode

- the mode in which the file is to be opened
**Parameters:** version

- specifies the release version for a multi-release jar file
**Throws:** IOException

- if an I/O error has occurred
**Throws:** IllegalArgumentException

- if the

mode

argument is invalid
**Throws:** SecurityException

- if access to the file is denied
by the SecurityManager
**Throws:** NullPointerException

- if

version

is

null
**Since:** 9

---

#### Constructor Detail

JarFile

```java
public JarFile​(
String
name)
throws
IOException
```

Creates a new

JarFile

to read from the specified
file

name

. The

JarFile

will be verified if
it is signed.

**Parameters:** name

- the name of the jar file to be opened for reading
**Throws:** IOException

- if an I/O error has occurred
**Throws:** SecurityException

- if access to the file is denied
by the SecurityManager

---

#### JarFile

public JarFile​(

String

name)
throws

IOException

Creates a new

JarFile

to read from the specified
file

name

. The

JarFile

will be verified if
it is signed.

JarFile

```java
public JarFile​(
String
name,
boolean verify)
throws
IOException
```

Creates a new

JarFile

to read from the specified
file

name

.

**Parameters:** name

- the name of the jar file to be opened for reading
**Parameters:** verify

- whether or not to verify the jar file if
it is signed.
**Throws:** IOException

- if an I/O error has occurred
**Throws:** SecurityException

- if access to the file is denied
by the SecurityManager

---

#### JarFile

public JarFile​(

String

name,
boolean verify)
throws

IOException

Creates a new

JarFile

to read from the specified
file

name

.

JarFile

```java
public JarFile​(
File
file)
throws
IOException
```

Creates a new

JarFile

to read from the specified

File

object. The

JarFile

will be verified if
it is signed.

**Parameters:** file

- the jar file to be opened for reading
**Throws:** IOException

- if an I/O error has occurred
**Throws:** SecurityException

- if access to the file is denied
by the SecurityManager

---

#### JarFile

public JarFile​(

File

file)
throws

IOException

Creates a new

JarFile

to read from the specified

File

object. The

JarFile

will be verified if
it is signed.

JarFile

```java
public JarFile​(
File
file,
boolean verify)
throws
IOException
```

Creates a new

JarFile

to read from the specified

File

object.

**Parameters:** file

- the jar file to be opened for reading
**Parameters:** verify

- whether or not to verify the jar file if
it is signed.
**Throws:** IOException

- if an I/O error has occurred
**Throws:** SecurityException

- if access to the file is denied
by the SecurityManager.

---

#### JarFile

public JarFile​(

File

file,
boolean verify)
throws

IOException

Creates a new

JarFile

to read from the specified

File

object.

JarFile

```java
public JarFile​(
File
file,
boolean verify,
int mode)
throws
IOException
```

Creates a new

JarFile

to read from the specified

File

object in the specified mode. The mode argument
must be either

OPEN_READ

or

OPEN_READ | OPEN_DELETE

.

**Parameters:** file

- the jar file to be opened for reading
**Parameters:** verify

- whether or not to verify the jar file if
it is signed.
**Parameters:** mode

- the mode in which the file is to be opened
**Throws:** IOException

- if an I/O error has occurred
**Throws:** IllegalArgumentException

- if the

mode

argument is invalid
**Throws:** SecurityException

- if access to the file is denied
by the SecurityManager
**Since:** 1.3

---

#### JarFile

public JarFile​(

File

file,
boolean verify,
int mode)
throws

IOException

Creates a new

JarFile

to read from the specified

File

object in the specified mode. The mode argument
must be either

OPEN_READ

or

OPEN_READ | OPEN_DELETE

.

JarFile

```java
public JarFile​(
File
file,
boolean verify,
int mode,

Runtime.Version
version)
throws
IOException
```

Creates a new

JarFile

to read from the specified

File

object in the specified mode. The mode argument
must be either

OPEN_READ

or

OPEN_READ | OPEN_DELETE

.
The version argument, after being converted to a canonical form, is
used to configure the

JarFile

for processing
multi-release jar files.

The canonical form derived from the version parameter is

Runtime.Version.parse(Integer.toString(n))

where

n

is

Math.max(version.feature(), JarFile.baseVersion().feature())

.

**Parameters:** file

- the jar file to be opened for reading
**Parameters:** verify

- whether or not to verify the jar file if
it is signed.
**Parameters:** mode

- the mode in which the file is to be opened
**Parameters:** version

- specifies the release version for a multi-release jar file
**Throws:** IOException

- if an I/O error has occurred
**Throws:** IllegalArgumentException

- if the

mode

argument is invalid
**Throws:** SecurityException

- if access to the file is denied
by the SecurityManager
**Throws:** NullPointerException

- if

version

is

null
**Since:** 9

---

#### JarFile

public JarFile​(

File

file,
boolean verify,
int mode,

Runtime.Version

version)
throws

IOException

Creates a new

JarFile

to read from the specified

File

object in the specified mode. The mode argument
must be either

OPEN_READ

or

OPEN_READ | OPEN_DELETE

.
The version argument, after being converted to a canonical form, is
used to configure the

JarFile

for processing
multi-release jar files.

The canonical form derived from the version parameter is

Runtime.Version.parse(Integer.toString(n))

where

n

is

Math.max(version.feature(), JarFile.baseVersion().feature())

.

The canonical form derived from the version parameter is

Runtime.Version.parse(Integer.toString(n))

where

n

is

Math.max(version.feature(), JarFile.baseVersion().feature())

.

Method Detail

- baseVersion

```java
public static
Runtime.Version
baseVersion()
```

Returns the version that represents the unversioned configuration of a
multi-release jar file.

**Returns:** the version that represents the unversioned configuration
**Since:** 9

- runtimeVersion

```java
public static
Runtime.Version
runtimeVersion()
```

Returns the version that represents the effective runtime versioned
configuration of a multi-release jar file.

By default the feature version number of the returned

Version

will
be equal to the feature version number of

Runtime.version()

.
However, if the

jdk.util.jar.version

property is set, the
returned

Version

is derived from that property and feature version
numbers may not be equal.

**Returns:** the version that represents the runtime versioned configuration
**Since:** 9

- getVersion

```java
public final
Runtime.Version
getVersion()
```

Returns the maximum version used when searching for versioned entries.

If this

JarFile

is not a multi-release jar file or is not
configured to be processed as such, then the version returned will be the
same as that returned from

baseVersion()

.

**Returns:** the maximum version
**Since:** 9

- isMultiRelease

```java
public final boolean isMultiRelease()
```

Indicates whether or not this jar file is a multi-release jar file.

**Returns:** true if this JarFile is a multi-release jar file
**Since:** 9

- getManifest

```java
public
Manifest
getManifest()
throws
IOException
```

Returns the jar file manifest, or

null

if none.

**Returns:** the jar file manifest, or

null

if none
**Throws:** IllegalStateException

- may be thrown if the jar file has been closed
**Throws:** IOException

- if an I/O error has occurred

- getJarEntry

```java
public
JarEntry
getJarEntry​(
String
name)
```

Returns the

JarEntry

for the given base entry name or

null

if not found.

If this

JarFile

is a multi-release jar file and is configured
to be processed as such, then a search is performed to find and return
a

JarEntry

that is the latest versioned entry associated with the
given entry name. The returned

JarEntry

is the versioned entry
corresponding to the given base entry name prefixed with the string

"META-INF/versions/{n}/"

, for the largest value of

n

for
which an entry exists. If such a versioned entry does not exist, then
the

JarEntry

for the base entry is returned, otherwise

null

is returned if no entries are found. The initial value for
the version

n

is the maximum version as returned by the method

getVersion()

.

**Implementation Requirements:** This implementation invokes

getEntry(String)

.
**Parameters:** name

- the jar file entry name
**Returns:** the

JarEntry

for the given entry name, or
the versioned entry name, or

null

if not found
**Throws:** IllegalStateException

- may be thrown if the jar file has been closed
**See Also:** JarEntry

- getEntry

```java
public
ZipEntry
getEntry​(
String
name)
```

Returns the

ZipEntry

for the given base entry name or

null

if not found.

If this

JarFile

is a multi-release jar file and is configured
to be processed as such, then a search is performed to find and return
a

ZipEntry

that is the latest versioned entry associated with the
given entry name. The returned

ZipEntry

is the versioned entry
corresponding to the given base entry name prefixed with the string

"META-INF/versions/{n}/"

, for the largest value of

n

for
which an entry exists. If such a versioned entry does not exist, then
the

ZipEntry

for the base entry is returned, otherwise

null

is returned if no entries are found. The initial value for
the version

n

is the maximum version as returned by the method

getVersion()

.

**Overrides:** getEntry

in class

ZipFile
**Implementation Requirements:** This implementation may return a versioned entry for the requested name
even if there is not a corresponding base entry. This can occur
if there is a private or package-private versioned entry that matches.
If a subclass overrides this method, assure that the override method
invokes

super.getEntry(name)

to obtain all versioned entries.
**Parameters:** name

- the jar file entry name
**Returns:** the

ZipEntry

for the given entry name or
the versioned entry name or

null

if not found
**Throws:** IllegalStateException

- may be thrown if the jar file has been closed
**See Also:** ZipEntry

- entries

```java
public
Enumeration
<
JarEntry
> entries()
```

Returns an enumeration of the jar file entries.

**Overrides:** entries

in class

ZipFile
**Returns:** an enumeration of the jar file entries
**Throws:** IllegalStateException

- may be thrown if the jar file has been closed

- stream

```java
public
Stream
<
JarEntry
> stream()
```

Returns an ordered

Stream

over the jar file entries.
Entries appear in the

Stream

in the order they appear in
the central directory of the jar file.

**Overrides:** stream

in class

ZipFile
**Returns:** an ordered

Stream

of entries in this jar file
**Throws:** IllegalStateException

- if the jar file has been closed
**Since:** 1.8

- versionedStream

```java
public
Stream
<
JarEntry
> versionedStream()
```

Returns a

Stream

of the versioned jar file entries.

If this

JarFile

is a multi-release jar file and is configured to
be processed as such, then an entry in the stream is the latest versioned entry
associated with the corresponding base entry name. The maximum version of the
latest versioned entry is the version returned by

getVersion()

.
The returned stream may include an entry that only exists as a versioned entry.

If the jar file is not a multi-release jar file or the

JarFile

is not
configured for processing a multi-release jar file, this method returns the
same stream that

stream()

returns.

**Returns:** stream of versioned entries
**Since:** 10

- getInputStream

```java
public
InputStream
getInputStream​(
ZipEntry
ze)
throws
IOException
```

Returns an input stream for reading the contents of the specified
zip file entry.

**Overrides:** getInputStream

in class

ZipFile
**Parameters:** ze

- the zip file entry
**Returns:** an input stream for reading the contents of the specified
zip file entry
**Throws:** ZipException

- if a zip file format error has occurred
**Throws:** IOException

- if an I/O error has occurred
**Throws:** SecurityException

- if any of the jar file entries
are incorrectly signed.
**Throws:** IllegalStateException

- may be thrown if the jar file has been closed

---

#### Method Detail

baseVersion

```java
public static
Runtime.Version
baseVersion()
```

Returns the version that represents the unversioned configuration of a
multi-release jar file.

**Returns:** the version that represents the unversioned configuration
**Since:** 9

---

#### baseVersion

public static

Runtime.Version

baseVersion()

Returns the version that represents the unversioned configuration of a
multi-release jar file.

runtimeVersion

```java
public static
Runtime.Version
runtimeVersion()
```

Returns the version that represents the effective runtime versioned
configuration of a multi-release jar file.

By default the feature version number of the returned

Version

will
be equal to the feature version number of

Runtime.version()

.
However, if the

jdk.util.jar.version

property is set, the
returned

Version

is derived from that property and feature version
numbers may not be equal.

**Returns:** the version that represents the runtime versioned configuration
**Since:** 9

---

#### runtimeVersion

public static

Runtime.Version

runtimeVersion()

Returns the version that represents the effective runtime versioned
configuration of a multi-release jar file.

By default the feature version number of the returned

Version

will
be equal to the feature version number of

Runtime.version()

.
However, if the

jdk.util.jar.version

property is set, the
returned

Version

is derived from that property and feature version
numbers may not be equal.

By default the feature version number of the returned

Version

will
be equal to the feature version number of

Runtime.version()

.
However, if the

jdk.util.jar.version

property is set, the
returned

Version

is derived from that property and feature version
numbers may not be equal.

getVersion

```java
public final
Runtime.Version
getVersion()
```

Returns the maximum version used when searching for versioned entries.

If this

JarFile

is not a multi-release jar file or is not
configured to be processed as such, then the version returned will be the
same as that returned from

baseVersion()

.

**Returns:** the maximum version
**Since:** 9

---

#### getVersion

public final

Runtime.Version

getVersion()

Returns the maximum version used when searching for versioned entries.

If this

JarFile

is not a multi-release jar file or is not
configured to be processed as such, then the version returned will be the
same as that returned from

baseVersion()

.

If this

JarFile

is not a multi-release jar file or is not
configured to be processed as such, then the version returned will be the
same as that returned from

baseVersion()

.

isMultiRelease

```java
public final boolean isMultiRelease()
```

Indicates whether or not this jar file is a multi-release jar file.

**Returns:** true if this JarFile is a multi-release jar file
**Since:** 9

---

#### isMultiRelease

public final boolean isMultiRelease()

Indicates whether or not this jar file is a multi-release jar file.

getManifest

```java
public
Manifest
getManifest()
throws
IOException
```

Returns the jar file manifest, or

null

if none.

**Returns:** the jar file manifest, or

null

if none
**Throws:** IllegalStateException

- may be thrown if the jar file has been closed
**Throws:** IOException

- if an I/O error has occurred

---

#### getManifest

public

Manifest

getManifest()
throws

IOException

Returns the jar file manifest, or

null

if none.

getJarEntry

```java
public
JarEntry
getJarEntry​(
String
name)
```

Returns the

JarEntry

for the given base entry name or

null

if not found.

If this

JarFile

is a multi-release jar file and is configured
to be processed as such, then a search is performed to find and return
a

JarEntry

that is the latest versioned entry associated with the
given entry name. The returned

JarEntry

is the versioned entry
corresponding to the given base entry name prefixed with the string

"META-INF/versions/{n}/"

, for the largest value of

n

for
which an entry exists. If such a versioned entry does not exist, then
the

JarEntry

for the base entry is returned, otherwise

null

is returned if no entries are found. The initial value for
the version

n

is the maximum version as returned by the method

getVersion()

.

**Implementation Requirements:** This implementation invokes

getEntry(String)

.
**Parameters:** name

- the jar file entry name
**Returns:** the

JarEntry

for the given entry name, or
the versioned entry name, or

null

if not found
**Throws:** IllegalStateException

- may be thrown if the jar file has been closed
**See Also:** JarEntry

---

#### getJarEntry

public

JarEntry

getJarEntry​(

String

name)

Returns the

JarEntry

for the given base entry name or

null

if not found.

If this

JarFile

is a multi-release jar file and is configured
to be processed as such, then a search is performed to find and return
a

JarEntry

that is the latest versioned entry associated with the
given entry name. The returned

JarEntry

is the versioned entry
corresponding to the given base entry name prefixed with the string

"META-INF/versions/{n}/"

, for the largest value of

n

for
which an entry exists. If such a versioned entry does not exist, then
the

JarEntry

for the base entry is returned, otherwise

null

is returned if no entries are found. The initial value for
the version

n

is the maximum version as returned by the method

getVersion()

.

If this

JarFile

is a multi-release jar file and is configured
to be processed as such, then a search is performed to find and return
a

JarEntry

that is the latest versioned entry associated with the
given entry name. The returned

JarEntry

is the versioned entry
corresponding to the given base entry name prefixed with the string

"META-INF/versions/{n}/"

, for the largest value of

n

for
which an entry exists. If such a versioned entry does not exist, then
the

JarEntry

for the base entry is returned, otherwise

null

is returned if no entries are found. The initial value for
the version

n

is the maximum version as returned by the method

getVersion()

.

This implementation invokes

getEntry(String)

.

getEntry

```java
public
ZipEntry
getEntry​(
String
name)
```

Returns the

ZipEntry

for the given base entry name or

null

if not found.

If this

JarFile

is a multi-release jar file and is configured
to be processed as such, then a search is performed to find and return
a

ZipEntry

that is the latest versioned entry associated with the
given entry name. The returned

ZipEntry

is the versioned entry
corresponding to the given base entry name prefixed with the string

"META-INF/versions/{n}/"

, for the largest value of

n

for
which an entry exists. If such a versioned entry does not exist, then
the

ZipEntry

for the base entry is returned, otherwise

null

is returned if no entries are found. The initial value for
the version

n

is the maximum version as returned by the method

getVersion()

.

**Overrides:** getEntry

in class

ZipFile
**Implementation Requirements:** This implementation may return a versioned entry for the requested name
even if there is not a corresponding base entry. This can occur
if there is a private or package-private versioned entry that matches.
If a subclass overrides this method, assure that the override method
invokes

super.getEntry(name)

to obtain all versioned entries.
**Parameters:** name

- the jar file entry name
**Returns:** the

ZipEntry

for the given entry name or
the versioned entry name or

null

if not found
**Throws:** IllegalStateException

- may be thrown if the jar file has been closed
**See Also:** ZipEntry

---

#### getEntry

public

ZipEntry

getEntry​(

String

name)

Returns the

ZipEntry

for the given base entry name or

null

if not found.

If this

JarFile

is a multi-release jar file and is configured
to be processed as such, then a search is performed to find and return
a

ZipEntry

that is the latest versioned entry associated with the
given entry name. The returned

ZipEntry

is the versioned entry
corresponding to the given base entry name prefixed with the string

"META-INF/versions/{n}/"

, for the largest value of

n

for
which an entry exists. If such a versioned entry does not exist, then
the

ZipEntry

for the base entry is returned, otherwise

null

is returned if no entries are found. The initial value for
the version

n

is the maximum version as returned by the method

getVersion()

.

If this

JarFile

is a multi-release jar file and is configured
to be processed as such, then a search is performed to find and return
a

ZipEntry

that is the latest versioned entry associated with the
given entry name. The returned

ZipEntry

is the versioned entry
corresponding to the given base entry name prefixed with the string

"META-INF/versions/{n}/"

, for the largest value of

n

for
which an entry exists. If such a versioned entry does not exist, then
the

ZipEntry

for the base entry is returned, otherwise

null

is returned if no entries are found. The initial value for
the version

n

is the maximum version as returned by the method

getVersion()

.

This implementation may return a versioned entry for the requested name
even if there is not a corresponding base entry. This can occur
if there is a private or package-private versioned entry that matches.
If a subclass overrides this method, assure that the override method
invokes

super.getEntry(name)

to obtain all versioned entries.

entries

```java
public
Enumeration
<
JarEntry
> entries()
```

Returns an enumeration of the jar file entries.

**Overrides:** entries

in class

ZipFile
**Returns:** an enumeration of the jar file entries
**Throws:** IllegalStateException

- may be thrown if the jar file has been closed

---

#### entries

public

Enumeration

<

JarEntry

> entries()

Returns an enumeration of the jar file entries.

stream

```java
public
Stream
<
JarEntry
> stream()
```

Returns an ordered

Stream

over the jar file entries.
Entries appear in the

Stream

in the order they appear in
the central directory of the jar file.

**Overrides:** stream

in class

ZipFile
**Returns:** an ordered

Stream

of entries in this jar file
**Throws:** IllegalStateException

- if the jar file has been closed
**Since:** 1.8

---

#### stream

public

Stream

<

JarEntry

> stream()

Returns an ordered

Stream

over the jar file entries.
Entries appear in the

Stream

in the order they appear in
the central directory of the jar file.

versionedStream

```java
public
Stream
<
JarEntry
> versionedStream()
```

Returns a

Stream

of the versioned jar file entries.

If this

JarFile

is a multi-release jar file and is configured to
be processed as such, then an entry in the stream is the latest versioned entry
associated with the corresponding base entry name. The maximum version of the
latest versioned entry is the version returned by

getVersion()

.
The returned stream may include an entry that only exists as a versioned entry.

If the jar file is not a multi-release jar file or the

JarFile

is not
configured for processing a multi-release jar file, this method returns the
same stream that

stream()

returns.

**Returns:** stream of versioned entries
**Since:** 10

---

#### versionedStream

public

Stream

<

JarEntry

> versionedStream()

Returns a

Stream

of the versioned jar file entries.

If this

JarFile

is a multi-release jar file and is configured to
be processed as such, then an entry in the stream is the latest versioned entry
associated with the corresponding base entry name. The maximum version of the
latest versioned entry is the version returned by

getVersion()

.
The returned stream may include an entry that only exists as a versioned entry.

If the jar file is not a multi-release jar file or the

JarFile

is not
configured for processing a multi-release jar file, this method returns the
same stream that

stream()

returns.

If this

JarFile

is a multi-release jar file and is configured to
be processed as such, then an entry in the stream is the latest versioned entry
associated with the corresponding base entry name. The maximum version of the
latest versioned entry is the version returned by

getVersion()

.
The returned stream may include an entry that only exists as a versioned entry.

If the jar file is not a multi-release jar file or the

JarFile

is not
configured for processing a multi-release jar file, this method returns the
same stream that

stream()

returns.

getInputStream

```java
public
InputStream
getInputStream​(
ZipEntry
ze)
throws
IOException
```

Returns an input stream for reading the contents of the specified
zip file entry.

**Overrides:** getInputStream

in class

ZipFile
**Parameters:** ze

- the zip file entry
**Returns:** an input stream for reading the contents of the specified
zip file entry
**Throws:** ZipException

- if a zip file format error has occurred
**Throws:** IOException

- if an I/O error has occurred
**Throws:** SecurityException

- if any of the jar file entries
are incorrectly signed.
**Throws:** IllegalStateException

- may be thrown if the jar file has been closed

---

#### getInputStream

public

InputStream

getInputStream​(

ZipEntry

ze)
throws

IOException

Returns an input stream for reading the contents of the specified
zip file entry.

---

