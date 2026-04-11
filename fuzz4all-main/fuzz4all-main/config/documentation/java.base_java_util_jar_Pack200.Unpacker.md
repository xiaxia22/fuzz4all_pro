# Interface Pack200.Unpacker

**Source:** `java.base\java\util\jar\Pack200.Unpacker.html`

### Class Description

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public static interface
Pack200.Unpacker
```

The unpacker engine converts the packed stream to a JAR file.
An instance of the engine can be obtained
using

Pack200.newUnpacker()

.

Every JAR file produced by this engine will include the string
"

PACK200

" as a zip file comment.
This allows a deployer to detect if a JAR archive was packed and unpacked.

Note: Unless otherwise noted, passing a

null

argument to a
constructor or method in this class will cause a

NullPointerException

to be thrown.

This version of the unpacker is compatible with all previous versions.

**Enclosing class:** Pack200

---

### Field Details

#### static final
String
KEEP

The string "keep", a possible value for certain properties.

**See Also:**
- DEFLATE_HINT

,

Constant Field Values

---

#### static final
String
TRUE

The string "true", a possible value for certain properties.

**See Also:**
- DEFLATE_HINT

,

Constant Field Values

---

#### static final
String
FALSE

The string "false", a possible value for certain properties.

**See Also:**
- DEFLATE_HINT

,

Constant Field Values

---

#### static final
String
DEFLATE_HINT

Property indicating that the unpacker should
ignore all transmitted values for DEFLATE_HINT,
replacing them by the given value,

TRUE

or

FALSE

.
The default value is the special string

KEEP

,
which asks the unpacker to preserve all transmitted
deflation hints.

**See Also:**
- Constant Field Values

---

#### static final
String
PROGRESS

The unpacker's progress as a percentage, as periodically
updated by the unpacker.
Values of 0 - 100 are normal, and -1 indicates a stall.
Progress can be monitored by polling the value of this
property.

At a minimum, the unpacker must set progress to 0
at the beginning of an unpacking operation, and to 100
at the end.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### SortedMap
<
String
,​
String
> properties()

Get the set of this engine's properties. This set is
a "live view", so that changing its
contents immediately affects the Unpacker engine, and
changes from the engine (such as progress indications)
are immediately visible in the map.

The property map may contain pre-defined implementation
specific and default properties. Users are encouraged to
read the information and fully understand the implications,
before modifying pre-existing properties.

Implementation specific properties are prefixed with a
package name associated with the implementor, beginning
with

com.

or a similar prefix.
All property names beginning with

pack.

and

unpack.

are reserved for use by this API.

Unknown properties may be ignored or rejected with an
unspecified error, and invalid entries may cause an
unspecified error to be thrown.

**Returns:**
- A sorted association of option key strings to option values.

---

#### void unpack​(
InputStream
in,

JarOutputStream
out)
throws
IOException

Read a Pack200 archive, and write the encoded JAR to
a JarOutputStream.
The entire contents of the input stream will be read.
It may be more efficient to read the Pack200 archive
to a file and pass the File object, using the alternate
method described below.

Closes its input but not its output. (The output can accumulate more elements.)

**Parameters:**
- in

- an InputStream.
- out

- a JarOutputStream.

**Throws:**
- IOException

- if an error is encountered.

---

#### void unpack​(
File
in,

JarOutputStream
out)
throws
IOException

Read a Pack200 archive, and write the encoded JAR to
a JarOutputStream.

Does not close its output. (The output can accumulate more elements.)

**Parameters:**
- in

- a File.
- out

- a JarOutputStream.

**Throws:**
- IOException

- if an error is encountered.

---

### Additional Sections

#### Interface Pack200.Unpacker

**Enclosing class:** Pack200

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public static interface
Pack200.Unpacker
```

Deprecated, for removal: This API element is subject to removal in a future version.

This interface is deprecated, and is planned for removal in a
future release.

The unpacker engine converts the packed stream to a JAR file.
An instance of the engine can be obtained
using

Pack200.newUnpacker()

.

Every JAR file produced by this engine will include the string
"

PACK200

" as a zip file comment.
This allows a deployer to detect if a JAR archive was packed and unpacked.

Note: Unless otherwise noted, passing a

null

argument to a
constructor or method in this class will cause a

NullPointerException

to be thrown.

This version of the unpacker is compatible with all previous versions.

**Since:** 1.5

@Deprecated

(

since

="11",

forRemoval

=true)
public static interface

Pack200.Unpacker

The unpacker engine converts the packed stream to a JAR file.
An instance of the engine can be obtained
using

Pack200.newUnpacker()

.

Every JAR file produced by this engine will include the string
"

PACK200

" as a zip file comment.
This allows a deployer to detect if a JAR archive was packed and unpacked.

Note: Unless otherwise noted, passing a

null

argument to a
constructor or method in this class will cause a

NullPointerException

to be thrown.

This version of the unpacker is compatible with all previous versions.

Every JAR file produced by this engine will include the string
"

PACK200

" as a zip file comment.
This allows a deployer to detect if a JAR archive was packed and unpacked.

Note: Unless otherwise noted, passing a

null

argument to a
constructor or method in this class will cause a

NullPointerException

to be thrown.

This version of the unpacker is compatible with all previous versions.

Note: Unless otherwise noted, passing a

null

argument to a
constructor or method in this class will cause a

NullPointerException

to be thrown.

This version of the unpacker is compatible with all previous versions.

This version of the unpacker is compatible with all previous versions.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

DEFLATE_HINT

Deprecated, for removal: This API element is subject to removal in a future version.

Property indicating that the unpacker should
ignore all transmitted values for DEFLATE_HINT,
replacing them by the given value,

TRUE

or

FALSE

.

static

String

FALSE

Deprecated, for removal: This API element is subject to removal in a future version.

The string "false", a possible value for certain properties.

static

String

KEEP

Deprecated, for removal: This API element is subject to removal in a future version.

The string "keep", a possible value for certain properties.

static

String

PROGRESS

Deprecated, for removal: This API element is subject to removal in a future version.

The unpacker's progress as a percentage, as periodically
updated by the unpacker.

static

String

TRUE

Deprecated, for removal: This API element is subject to removal in a future version.

The string "true", a possible value for certain properties.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

SortedMap

<

String

,​

String

>

properties

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get the set of this engine's properties.

void

unpack

​(

File

in,

JarOutputStream

out)

Deprecated, for removal: This API element is subject to removal in a future version.

Read a Pack200 archive, and write the encoded JAR to
a JarOutputStream.

void

unpack

​(

InputStream

in,

JarOutputStream

out)

Deprecated, for removal: This API element is subject to removal in a future version.

Read a Pack200 archive, and write the encoded JAR to
a JarOutputStream.

Field Summary

Fields

Modifier and Type

Field

Description

static

String

DEFLATE_HINT

Deprecated, for removal: This API element is subject to removal in a future version.

Property indicating that the unpacker should
ignore all transmitted values for DEFLATE_HINT,
replacing them by the given value,

TRUE

or

FALSE

.

static

String

FALSE

Deprecated, for removal: This API element is subject to removal in a future version.

The string "false", a possible value for certain properties.

static

String

KEEP

Deprecated, for removal: This API element is subject to removal in a future version.

The string "keep", a possible value for certain properties.

static

String

PROGRESS

Deprecated, for removal: This API element is subject to removal in a future version.

The unpacker's progress as a percentage, as periodically
updated by the unpacker.

static

String

TRUE

Deprecated, for removal: This API element is subject to removal in a future version.

The string "true", a possible value for certain properties.

---

#### Field Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Property indicating that the unpacker should
ignore all transmitted values for DEFLATE_HINT,
replacing them by the given value,

TRUE

or

FALSE

.

The string "false", a possible value for certain properties.

The string "keep", a possible value for certain properties.

The unpacker's progress as a percentage, as periodically
updated by the unpacker.

The string "true", a possible value for certain properties.

Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

SortedMap

<

String

,​

String

>

properties

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get the set of this engine's properties.

void

unpack

​(

File

in,

JarOutputStream

out)

Deprecated, for removal: This API element is subject to removal in a future version.

Read a Pack200 archive, and write the encoded JAR to
a JarOutputStream.

void

unpack

​(

InputStream

in,

JarOutputStream

out)

Deprecated, for removal: This API element is subject to removal in a future version.

Read a Pack200 archive, and write the encoded JAR to
a JarOutputStream.

---

#### Method Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Get the set of this engine's properties.

Read a Pack200 archive, and write the encoded JAR to
a JarOutputStream.

============ FIELD DETAIL ===========

- Field Detail

- KEEP

```java
static final
String
KEEP
```

Deprecated, for removal: This API element is subject to removal in a future version.

The string "keep", a possible value for certain properties.

**See Also:** DEFLATE_HINT

,

Constant Field Values

- TRUE

```java
static final
String
TRUE
```

Deprecated, for removal: This API element is subject to removal in a future version.

The string "true", a possible value for certain properties.

**See Also:** DEFLATE_HINT

,

Constant Field Values

- FALSE

```java
static final
String
FALSE
```

Deprecated, for removal: This API element is subject to removal in a future version.

The string "false", a possible value for certain properties.

**See Also:** DEFLATE_HINT

,

Constant Field Values

- DEFLATE_HINT

```java
static final
String
DEFLATE_HINT
```

Deprecated, for removal: This API element is subject to removal in a future version.

Property indicating that the unpacker should
ignore all transmitted values for DEFLATE_HINT,
replacing them by the given value,

TRUE

or

FALSE

.
The default value is the special string

KEEP

,
which asks the unpacker to preserve all transmitted
deflation hints.

**See Also:** Constant Field Values

- PROGRESS

```java
static final
String
PROGRESS
```

Deprecated, for removal: This API element is subject to removal in a future version.

The unpacker's progress as a percentage, as periodically
updated by the unpacker.
Values of 0 - 100 are normal, and -1 indicates a stall.
Progress can be monitored by polling the value of this
property.

At a minimum, the unpacker must set progress to 0
at the beginning of an unpacking operation, and to 100
at the end.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- properties

```java
SortedMap
<
String
,​
String
> properties()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the set of this engine's properties. This set is
a "live view", so that changing its
contents immediately affects the Unpacker engine, and
changes from the engine (such as progress indications)
are immediately visible in the map.

The property map may contain pre-defined implementation
specific and default properties. Users are encouraged to
read the information and fully understand the implications,
before modifying pre-existing properties.

Implementation specific properties are prefixed with a
package name associated with the implementor, beginning
with

com.

or a similar prefix.
All property names beginning with

pack.

and

unpack.

are reserved for use by this API.

Unknown properties may be ignored or rejected with an
unspecified error, and invalid entries may cause an
unspecified error to be thrown.

**Returns:** A sorted association of option key strings to option values.

- unpack

```java
void unpack​(
InputStream
in,

JarOutputStream
out)
throws
IOException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Read a Pack200 archive, and write the encoded JAR to
a JarOutputStream.
The entire contents of the input stream will be read.
It may be more efficient to read the Pack200 archive
to a file and pass the File object, using the alternate
method described below.

Closes its input but not its output. (The output can accumulate more elements.)

**Parameters:** in

- an InputStream.
**Parameters:** out

- a JarOutputStream.
**Throws:** IOException

- if an error is encountered.

- unpack

```java
void unpack​(
File
in,

JarOutputStream
out)
throws
IOException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Read a Pack200 archive, and write the encoded JAR to
a JarOutputStream.

Does not close its output. (The output can accumulate more elements.)

**Parameters:** in

- a File.
**Parameters:** out

- a JarOutputStream.
**Throws:** IOException

- if an error is encountered.

Field Detail

- KEEP

```java
static final
String
KEEP
```

Deprecated, for removal: This API element is subject to removal in a future version.

The string "keep", a possible value for certain properties.

**See Also:** DEFLATE_HINT

,

Constant Field Values

- TRUE

```java
static final
String
TRUE
```

Deprecated, for removal: This API element is subject to removal in a future version.

The string "true", a possible value for certain properties.

**See Also:** DEFLATE_HINT

,

Constant Field Values

- FALSE

```java
static final
String
FALSE
```

Deprecated, for removal: This API element is subject to removal in a future version.

The string "false", a possible value for certain properties.

**See Also:** DEFLATE_HINT

,

Constant Field Values

- DEFLATE_HINT

```java
static final
String
DEFLATE_HINT
```

Deprecated, for removal: This API element is subject to removal in a future version.

Property indicating that the unpacker should
ignore all transmitted values for DEFLATE_HINT,
replacing them by the given value,

TRUE

or

FALSE

.
The default value is the special string

KEEP

,
which asks the unpacker to preserve all transmitted
deflation hints.

**See Also:** Constant Field Values

- PROGRESS

```java
static final
String
PROGRESS
```

Deprecated, for removal: This API element is subject to removal in a future version.

The unpacker's progress as a percentage, as periodically
updated by the unpacker.
Values of 0 - 100 are normal, and -1 indicates a stall.
Progress can be monitored by polling the value of this
property.

At a minimum, the unpacker must set progress to 0
at the beginning of an unpacking operation, and to 100
at the end.

**See Also:** Constant Field Values

---

#### Field Detail

KEEP

```java
static final
String
KEEP
```

Deprecated, for removal: This API element is subject to removal in a future version.

The string "keep", a possible value for certain properties.

**See Also:** DEFLATE_HINT

,

Constant Field Values

---

#### KEEP

static final

String

KEEP

The string "keep", a possible value for certain properties.

TRUE

```java
static final
String
TRUE
```

Deprecated, for removal: This API element is subject to removal in a future version.

The string "true", a possible value for certain properties.

**See Also:** DEFLATE_HINT

,

Constant Field Values

---

#### TRUE

static final

String

TRUE

The string "true", a possible value for certain properties.

FALSE

```java
static final
String
FALSE
```

Deprecated, for removal: This API element is subject to removal in a future version.

The string "false", a possible value for certain properties.

**See Also:** DEFLATE_HINT

,

Constant Field Values

---

#### FALSE

static final

String

FALSE

The string "false", a possible value for certain properties.

DEFLATE_HINT

```java
static final
String
DEFLATE_HINT
```

Deprecated, for removal: This API element is subject to removal in a future version.

Property indicating that the unpacker should
ignore all transmitted values for DEFLATE_HINT,
replacing them by the given value,

TRUE

or

FALSE

.
The default value is the special string

KEEP

,
which asks the unpacker to preserve all transmitted
deflation hints.

**See Also:** Constant Field Values

---

#### DEFLATE_HINT

static final

String

DEFLATE_HINT

Property indicating that the unpacker should
ignore all transmitted values for DEFLATE_HINT,
replacing them by the given value,

TRUE

or

FALSE

.
The default value is the special string

KEEP

,
which asks the unpacker to preserve all transmitted
deflation hints.

PROGRESS

```java
static final
String
PROGRESS
```

Deprecated, for removal: This API element is subject to removal in a future version.

The unpacker's progress as a percentage, as periodically
updated by the unpacker.
Values of 0 - 100 are normal, and -1 indicates a stall.
Progress can be monitored by polling the value of this
property.

At a minimum, the unpacker must set progress to 0
at the beginning of an unpacking operation, and to 100
at the end.

**See Also:** Constant Field Values

---

#### PROGRESS

static final

String

PROGRESS

The unpacker's progress as a percentage, as periodically
updated by the unpacker.
Values of 0 - 100 are normal, and -1 indicates a stall.
Progress can be monitored by polling the value of this
property.

At a minimum, the unpacker must set progress to 0
at the beginning of an unpacking operation, and to 100
at the end.

At a minimum, the unpacker must set progress to 0
at the beginning of an unpacking operation, and to 100
at the end.

Method Detail

- properties

```java
SortedMap
<
String
,​
String
> properties()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the set of this engine's properties. This set is
a "live view", so that changing its
contents immediately affects the Unpacker engine, and
changes from the engine (such as progress indications)
are immediately visible in the map.

The property map may contain pre-defined implementation
specific and default properties. Users are encouraged to
read the information and fully understand the implications,
before modifying pre-existing properties.

Implementation specific properties are prefixed with a
package name associated with the implementor, beginning
with

com.

or a similar prefix.
All property names beginning with

pack.

and

unpack.

are reserved for use by this API.

Unknown properties may be ignored or rejected with an
unspecified error, and invalid entries may cause an
unspecified error to be thrown.

**Returns:** A sorted association of option key strings to option values.

- unpack

```java
void unpack​(
InputStream
in,

JarOutputStream
out)
throws
IOException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Read a Pack200 archive, and write the encoded JAR to
a JarOutputStream.
The entire contents of the input stream will be read.
It may be more efficient to read the Pack200 archive
to a file and pass the File object, using the alternate
method described below.

Closes its input but not its output. (The output can accumulate more elements.)

**Parameters:** in

- an InputStream.
**Parameters:** out

- a JarOutputStream.
**Throws:** IOException

- if an error is encountered.

- unpack

```java
void unpack​(
File
in,

JarOutputStream
out)
throws
IOException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Read a Pack200 archive, and write the encoded JAR to
a JarOutputStream.

Does not close its output. (The output can accumulate more elements.)

**Parameters:** in

- a File.
**Parameters:** out

- a JarOutputStream.
**Throws:** IOException

- if an error is encountered.

---

#### Method Detail

properties

```java
SortedMap
<
String
,​
String
> properties()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the set of this engine's properties. This set is
a "live view", so that changing its
contents immediately affects the Unpacker engine, and
changes from the engine (such as progress indications)
are immediately visible in the map.

The property map may contain pre-defined implementation
specific and default properties. Users are encouraged to
read the information and fully understand the implications,
before modifying pre-existing properties.

Implementation specific properties are prefixed with a
package name associated with the implementor, beginning
with

com.

or a similar prefix.
All property names beginning with

pack.

and

unpack.

are reserved for use by this API.

Unknown properties may be ignored or rejected with an
unspecified error, and invalid entries may cause an
unspecified error to be thrown.

**Returns:** A sorted association of option key strings to option values.

---

#### properties

SortedMap

<

String

,​

String

> properties()

Get the set of this engine's properties. This set is
a "live view", so that changing its
contents immediately affects the Unpacker engine, and
changes from the engine (such as progress indications)
are immediately visible in the map.

The property map may contain pre-defined implementation
specific and default properties. Users are encouraged to
read the information and fully understand the implications,
before modifying pre-existing properties.

Implementation specific properties are prefixed with a
package name associated with the implementor, beginning
with

com.

or a similar prefix.
All property names beginning with

pack.

and

unpack.

are reserved for use by this API.

Unknown properties may be ignored or rejected with an
unspecified error, and invalid entries may cause an
unspecified error to be thrown.

The property map may contain pre-defined implementation
specific and default properties. Users are encouraged to
read the information and fully understand the implications,
before modifying pre-existing properties.

Implementation specific properties are prefixed with a
package name associated with the implementor, beginning
with

com.

or a similar prefix.
All property names beginning with

pack.

and

unpack.

are reserved for use by this API.

Unknown properties may be ignored or rejected with an
unspecified error, and invalid entries may cause an
unspecified error to be thrown.

Implementation specific properties are prefixed with a
package name associated with the implementor, beginning
with

com.

or a similar prefix.
All property names beginning with

pack.

and

unpack.

are reserved for use by this API.

Unknown properties may be ignored or rejected with an
unspecified error, and invalid entries may cause an
unspecified error to be thrown.

Unknown properties may be ignored or rejected with an
unspecified error, and invalid entries may cause an
unspecified error to be thrown.

unpack

```java
void unpack​(
InputStream
in,

JarOutputStream
out)
throws
IOException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Read a Pack200 archive, and write the encoded JAR to
a JarOutputStream.
The entire contents of the input stream will be read.
It may be more efficient to read the Pack200 archive
to a file and pass the File object, using the alternate
method described below.

Closes its input but not its output. (The output can accumulate more elements.)

**Parameters:** in

- an InputStream.
**Parameters:** out

- a JarOutputStream.
**Throws:** IOException

- if an error is encountered.

---

#### unpack

void unpack​(

InputStream

in,

JarOutputStream

out)
throws

IOException

Read a Pack200 archive, and write the encoded JAR to
a JarOutputStream.
The entire contents of the input stream will be read.
It may be more efficient to read the Pack200 archive
to a file and pass the File object, using the alternate
method described below.

Closes its input but not its output. (The output can accumulate more elements.)

Closes its input but not its output. (The output can accumulate more elements.)

unpack

```java
void unpack​(
File
in,

JarOutputStream
out)
throws
IOException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Read a Pack200 archive, and write the encoded JAR to
a JarOutputStream.

Does not close its output. (The output can accumulate more elements.)

**Parameters:** in

- a File.
**Parameters:** out

- a JarOutputStream.
**Throws:** IOException

- if an error is encountered.

---

#### unpack

void unpack​(

File

in,

JarOutputStream

out)
throws

IOException

Read a Pack200 archive, and write the encoded JAR to
a JarOutputStream.

Does not close its output. (The output can accumulate more elements.)

Does not close its output. (The output can accumulate more elements.)

---

