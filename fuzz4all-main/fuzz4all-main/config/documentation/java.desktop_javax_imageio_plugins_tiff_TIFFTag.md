# Class TIFFTag

**Source:** `java.desktop\javax\imageio\plugins\tiff\TIFFTag.html`

### Class Description

```java
public class
TIFFTag

extends
Object
```

A class defining the notion of a TIFF tag. A TIFF tag is a key
that may appear in an Image File Directory (IFD). In the IFD
each tag has some data associated with it, which may consist of zero
or more values of a given data type. The combination of a tag and a
value is known as an IFD Entry or TIFF Field.

The actual tag values used in the root IFD of a standard ("baseline")
tiff stream are defined in the

BaselineTIFFTagSet

class.

**Since:** 9
**See Also:** BaselineTIFFTagSet

,

TIFFField

,

TIFFTagSet

---

### Field Details

#### public static final int TIFF_BYTE

Flag for 8 bit unsigned integers.

**See Also:**
- Constant Field Values

---

#### public static final int TIFF_ASCII

Flag for null-terminated ASCII strings.

**See Also:**
- Constant Field Values

---

#### public static final int TIFF_SHORT

Flag for 16 bit unsigned integers.

**See Also:**
- Constant Field Values

---

#### public static final int TIFF_LONG

Flag for 32 bit unsigned integers.

**See Also:**
- Constant Field Values

---

#### public static final int TIFF_RATIONAL

Flag for pairs of 32 bit unsigned integers.

**See Also:**
- Constant Field Values

---

#### public static final int TIFF_SBYTE

Flag for 8 bit signed integers.

**See Also:**
- Constant Field Values

---

#### public static final int TIFF_UNDEFINED

Flag for 8 bit uninterpreted bytes.

**See Also:**
- Constant Field Values

---

#### public static final int TIFF_SSHORT

Flag for 16 bit signed integers.

**See Also:**
- Constant Field Values

---

#### public static final int TIFF_SLONG

Flag for 32 bit signed integers.

**See Also:**
- Constant Field Values

---

#### public static final int TIFF_SRATIONAL

Flag for pairs of 32 bit signed integers.

**See Also:**
- Constant Field Values

---

#### public static final int TIFF_FLOAT

Flag for 32 bit IEEE floats.

**See Also:**
- Constant Field Values

---

#### public static final int TIFF_DOUBLE

Flag for 64 bit IEEE doubles.

**See Also:**
- Constant Field Values

---

#### public static final int TIFF_IFD_POINTER

Flag for IFD pointer defined in TIFF Tech Note 1 in
TIFF Specification Supplement 1.

**See Also:**
- Constant Field Values

---

#### public static final int MIN_DATATYPE

The numerically smallest constant representing a TIFF data type.

**See Also:**
- Constant Field Values

---

#### public static final int MAX_DATATYPE

The numerically largest constant representing a TIFF data type.

**See Also:**
- Constant Field Values

---

#### public static final
String
UNKNOWN_TAG_NAME

The name assigned to a tag with an unknown tag number. Such
a tag may be created for example when reading an IFD and a
tag number is encountered which is not in any of the

TIFFTagSet

s known to the reader.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public TIFFTag​(
String
name,
int number,
int dataTypes,
int count)

Constructs a

TIFFTag

with a given name, tag number, set
of legal data types, and value count. A negative value count signifies
that either an arbitrary number of values is legal or the required count
is determined by the values of other fields in the IFD. A non-negative
count specifies the number of values which an associated field must
contain. The tag will have no associated

TIFFTagSet

.

If there are mnemonic names to be associated with the legal
data values for the tag,

addValueName()

should be called on the new instance for each name.
Mnemonic names apply only to tags which have integral data type.

See the documentation for

getDataTypes()

for an explanation of how the set
of data types is to be converted into a bit mask.

**Parameters:**
- name

- the name of the tag.
- number

- the number used to represent the tag.
- dataTypes

- a bit mask indicating the set of legal data
types for this tag.
- count

- the value count for this tag.

**Throws:**
- NullPointerException

- if name is null.
- IllegalArgumentException

- if number is negative or dataTypes
is negative or specifies an out of range type.

---

#### public TIFFTag​(
String
name,
int number,

TIFFTagSet
tagSet)

Constructs a

TIFFTag

with a given name, tag number and

TIFFTagSet

to which it refers. The legal data types are
set to include

TIFF_LONG

and

TIFF_IFD_POINTER

and the
value count is unity. The

TIFFTagSet

will
represent the set of

TIFFTag

s which appear in the IFD
pointed to. A

TIFFTag

represents an IFD pointer if and
only if

tagSet

is non-

null

or the data
type

TIFF_IFD_POINTER

is legal.

**Parameters:**
- name

- the name of the tag.
- number

- the number used to represent the tag.
- tagSet

- the

TIFFTagSet

to which this tag belongs.

**Throws:**
- NullPointerException

- if name or tagSet is null.
- IllegalArgumentException

- if number is negative.

**See Also:**
- TIFFTag(String, int, int, int)

---

#### public TIFFTag​(
String
name,
int number,
int dataTypes)

Constructs a

TIFFTag

with a given name, tag number,
and set of legal data types. The value count of the tag will be
undefined and it will have no associated

TIFFTagSet

.

**Parameters:**
- name

- the name of the tag.
- number

- the number used to represent the tag.
- dataTypes

- a bit mask indicating the set of legal data
types for this tag.

**Throws:**
- NullPointerException

- if name is null.
- IllegalArgumentException

- if number is negative or dataTypes
is negative or specifies an out of range type.

**See Also:**
- TIFFTag(String, int, int, int)

---

### Method Details

#### public static int getSizeOfType​(int dataType)

Returns the number of bytes used to store a value of the given
data type.

**Parameters:**
- dataType

- the data type to be queried.

**Returns:**
- the number of bytes used to store the given data type.

**Throws:**
- IllegalArgumentException

- if

datatype

is
less than

MIN_DATATYPE

or greater than

MAX_DATATYPE

.

---

#### public
String
getName()

Returns the name of the tag, as it will appear in image metadata.

**Returns:**
- the tag name, as a

String

.

---

#### public int getNumber()

Returns the integer used to represent the tag.

**Returns:**
- the tag number, as an

int

.

---

#### public int getDataTypes()

Returns a bit mask indicating the set of data types that may
be used to store the data associated with the tag.
For example, a tag that can store both SHORT and LONG values
would return a value of:

```java
(1 << TIFFTag.TIFF_SHORT) | (1 << TIFFTag.TIFF_LONG)
```

**Returns:**
- an

int

containing a bitmask encoding the
set of valid data types.

---

#### public int getCount()

Returns the value count of this tag. If this value is positive, it
represents the required number of values for a

TIFFField

which has this tag. If the value is negative, the count is undefined.
In the latter case the count may be derived, e.g., the number of values
of the

BitsPerSample

field is

SamplesPerPixel

,
or it may be variable as in the case of most

US-ASCII

fields.

**Returns:**
- the value count of this tag.

---

#### public boolean isDataTypeOK​(int dataType)

Returns

true

if the given data type
may be used for the data associated with this tag.

**Parameters:**
- dataType

- the data type to be queried, one of

TIFF_BYTE

,

TIFF_SHORT

, etc.

**Returns:**
- a

boolean

indicating whether the given
data type may be used with this tag.

**Throws:**
- IllegalArgumentException

- if

datatype

is
less than

MIN_DATATYPE

or greater than

MAX_DATATYPE

.

---

#### public
TIFFTagSet
getTagSet()

Returns the

TIFFTagSet

of which this tag is a part.

**Returns:**
- the containing

TIFFTagSet

.

---

#### public boolean isIFDPointer()

Returns

true

if this tag is used to point to an IFD
structure containing additional tags. A

TIFFTag

represents
an IFD pointer if and only if its

TIFFTagSet

is
non-

null

or the data type

TIFF_IFD_POINTER

is
legal. This condition will be satisfied if and only if either

getTagSet() != null

or

isDataTypeOK(TIFF_IFD_POINTER) == true

.

Many TIFF extensions use the IFD mechanism in order to limit the
number of new tags that may appear in the root IFD.

**Returns:**
- true

if this tag points to an IFD.

---

#### public boolean hasValueNames()

Returns

true

if there are mnemonic names associated with
the set of legal values for the data associated with this tag. Mnemonic
names apply only to tags which have integral data type.

**Returns:**
- true

if mnemonic value names are available.

---

#### protected void addValueName​(int value,

String
name)

Adds a mnemonic name for a particular value that this tag's data may take
on. Mnemonic names apply only to tags which have integral data type.

**Parameters:**
- value

- the data value.
- name

- the name to associate with the value.

---

#### public
String
getValueName​(int value)

Returns the mnemonic name associated with a particular value
that this tag's data may take on, or

null

if
no name is present. Mnemonic names apply only to tags which have
integral data type.

**Parameters:**
- value

- the data value.

**Returns:**
- the mnemonic name associated with the value, as a

String

.

---

#### public int[] getNamedValues()

Returns an array of values for which mnemonic names are defined. The
method

getValueName()

will return
non-

null

only for values contained in the returned array.
Mnemonic names apply only to tags which have integral data type.

**Returns:**
- the values for which there is a mnemonic name.

---

### Additional Sections

#### Class TIFFTag

java.lang.Object

- javax.imageio.plugins.tiff.TIFFTag

javax.imageio.plugins.tiff.TIFFTag

```java
public class
TIFFTag

extends
Object
```

A class defining the notion of a TIFF tag. A TIFF tag is a key
that may appear in an Image File Directory (IFD). In the IFD
each tag has some data associated with it, which may consist of zero
or more values of a given data type. The combination of a tag and a
value is known as an IFD Entry or TIFF Field.

The actual tag values used in the root IFD of a standard ("baseline")
tiff stream are defined in the

BaselineTIFFTagSet

class.

**Since:** 9
**See Also:** BaselineTIFFTagSet

,

TIFFField

,

TIFFTagSet

public class

TIFFTag

extends

Object

A class defining the notion of a TIFF tag. A TIFF tag is a key
that may appear in an Image File Directory (IFD). In the IFD
each tag has some data associated with it, which may consist of zero
or more values of a given data type. The combination of a tag and a
value is known as an IFD Entry or TIFF Field.

The actual tag values used in the root IFD of a standard ("baseline")
tiff stream are defined in the

BaselineTIFFTagSet

class.

The actual tag values used in the root IFD of a standard ("baseline")
tiff stream are defined in the

BaselineTIFFTagSet

class.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

MAX_DATATYPE

The numerically largest constant representing a TIFF data type.

static int

MIN_DATATYPE

The numerically smallest constant representing a TIFF data type.

static int

TIFF_ASCII

Flag for null-terminated ASCII strings.

static int

TIFF_BYTE

Flag for 8 bit unsigned integers.

static int

TIFF_DOUBLE

Flag for 64 bit IEEE doubles.

static int

TIFF_FLOAT

Flag for 32 bit IEEE floats.

static int

TIFF_IFD_POINTER

Flag for IFD pointer defined in TIFF Tech Note 1 in
TIFF Specification Supplement 1.

static int

TIFF_LONG

Flag for 32 bit unsigned integers.

static int

TIFF_RATIONAL

Flag for pairs of 32 bit unsigned integers.

static int

TIFF_SBYTE

Flag for 8 bit signed integers.

static int

TIFF_SHORT

Flag for 16 bit unsigned integers.

static int

TIFF_SLONG

Flag for 32 bit signed integers.

static int

TIFF_SRATIONAL

Flag for pairs of 32 bit signed integers.

static int

TIFF_SSHORT

Flag for 16 bit signed integers.

static int

TIFF_UNDEFINED

Flag for 8 bit uninterpreted bytes.

static

String

UNKNOWN_TAG_NAME

The name assigned to a tag with an unknown tag number.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

TIFFTag

​(

String

name,
int number,
int dataTypes)

Constructs a

TIFFTag

with a given name, tag number,
and set of legal data types.

TIFFTag

​(

String

name,
int number,
int dataTypes,
int count)

Constructs a

TIFFTag

with a given name, tag number, set
of legal data types, and value count.

TIFFTag

​(

String

name,
int number,

TIFFTagSet

tagSet)

Constructs a

TIFFTag

with a given name, tag number and

TIFFTagSet

to which it refers.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

addValueName

​(int value,

String

name)

Adds a mnemonic name for a particular value that this tag's data may take
on.

int

getCount

()

Returns the value count of this tag.

int

getDataTypes

()

Returns a bit mask indicating the set of data types that may
be used to store the data associated with the tag.

String

getName

()

Returns the name of the tag, as it will appear in image metadata.

int[]

getNamedValues

()

Returns an array of values for which mnemonic names are defined.

int

getNumber

()

Returns the integer used to represent the tag.

static int

getSizeOfType

​(int dataType)

Returns the number of bytes used to store a value of the given
data type.

TIFFTagSet

getTagSet

()

Returns the

TIFFTagSet

of which this tag is a part.

String

getValueName

​(int value)

Returns the mnemonic name associated with a particular value
that this tag's data may take on, or

null

if
no name is present.

boolean

hasValueNames

()

Returns

true

if there are mnemonic names associated with
the set of legal values for the data associated with this tag.

boolean

isDataTypeOK

​(int dataType)

Returns

true

if the given data type
may be used for the data associated with this tag.

boolean

isIFDPointer

()

Returns

true

if this tag is used to point to an IFD
structure containing additional tags.

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

MAX_DATATYPE

The numerically largest constant representing a TIFF data type.

static int

MIN_DATATYPE

The numerically smallest constant representing a TIFF data type.

static int

TIFF_ASCII

Flag for null-terminated ASCII strings.

static int

TIFF_BYTE

Flag for 8 bit unsigned integers.

static int

TIFF_DOUBLE

Flag for 64 bit IEEE doubles.

static int

TIFF_FLOAT

Flag for 32 bit IEEE floats.

static int

TIFF_IFD_POINTER

Flag for IFD pointer defined in TIFF Tech Note 1 in
TIFF Specification Supplement 1.

static int

TIFF_LONG

Flag for 32 bit unsigned integers.

static int

TIFF_RATIONAL

Flag for pairs of 32 bit unsigned integers.

static int

TIFF_SBYTE

Flag for 8 bit signed integers.

static int

TIFF_SHORT

Flag for 16 bit unsigned integers.

static int

TIFF_SLONG

Flag for 32 bit signed integers.

static int

TIFF_SRATIONAL

Flag for pairs of 32 bit signed integers.

static int

TIFF_SSHORT

Flag for 16 bit signed integers.

static int

TIFF_UNDEFINED

Flag for 8 bit uninterpreted bytes.

static

String

UNKNOWN_TAG_NAME

The name assigned to a tag with an unknown tag number.

---

#### Field Summary

The numerically largest constant representing a TIFF data type.

The numerically smallest constant representing a TIFF data type.

Flag for null-terminated ASCII strings.

Flag for 8 bit unsigned integers.

Flag for 64 bit IEEE doubles.

Flag for 32 bit IEEE floats.

Flag for IFD pointer defined in TIFF Tech Note 1 in
TIFF Specification Supplement 1.

Flag for 32 bit unsigned integers.

Flag for pairs of 32 bit unsigned integers.

Flag for 8 bit signed integers.

Flag for 16 bit unsigned integers.

Flag for 32 bit signed integers.

Flag for pairs of 32 bit signed integers.

Flag for 16 bit signed integers.

Flag for 8 bit uninterpreted bytes.

The name assigned to a tag with an unknown tag number.

Constructor Summary

Constructors

Constructor

Description

TIFFTag

​(

String

name,
int number,
int dataTypes)

Constructs a

TIFFTag

with a given name, tag number,
and set of legal data types.

TIFFTag

​(

String

name,
int number,
int dataTypes,
int count)

Constructs a

TIFFTag

with a given name, tag number, set
of legal data types, and value count.

TIFFTag

​(

String

name,
int number,

TIFFTagSet

tagSet)

Constructs a

TIFFTag

with a given name, tag number and

TIFFTagSet

to which it refers.

---

#### Constructor Summary

Constructs a

TIFFTag

with a given name, tag number,
and set of legal data types.

Constructs a

TIFFTag

with a given name, tag number, set
of legal data types, and value count.

Constructs a

TIFFTag

with a given name, tag number and

TIFFTagSet

to which it refers.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

addValueName

​(int value,

String

name)

Adds a mnemonic name for a particular value that this tag's data may take
on.

int

getCount

()

Returns the value count of this tag.

int

getDataTypes

()

Returns a bit mask indicating the set of data types that may
be used to store the data associated with the tag.

String

getName

()

Returns the name of the tag, as it will appear in image metadata.

int[]

getNamedValues

()

Returns an array of values for which mnemonic names are defined.

int

getNumber

()

Returns the integer used to represent the tag.

static int

getSizeOfType

​(int dataType)

Returns the number of bytes used to store a value of the given
data type.

TIFFTagSet

getTagSet

()

Returns the

TIFFTagSet

of which this tag is a part.

String

getValueName

​(int value)

Returns the mnemonic name associated with a particular value
that this tag's data may take on, or

null

if
no name is present.

boolean

hasValueNames

()

Returns

true

if there are mnemonic names associated with
the set of legal values for the data associated with this tag.

boolean

isDataTypeOK

​(int dataType)

Returns

true

if the given data type
may be used for the data associated with this tag.

boolean

isIFDPointer

()

Returns

true

if this tag is used to point to an IFD
structure containing additional tags.

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

Adds a mnemonic name for a particular value that this tag's data may take
on.

Returns the value count of this tag.

Returns a bit mask indicating the set of data types that may
be used to store the data associated with the tag.

Returns the name of the tag, as it will appear in image metadata.

Returns an array of values for which mnemonic names are defined.

Returns the integer used to represent the tag.

Returns the number of bytes used to store a value of the given
data type.

Returns the

TIFFTagSet

of which this tag is a part.

Returns the mnemonic name associated with a particular value
that this tag's data may take on, or

null

if
no name is present.

Returns

true

if there are mnemonic names associated with
the set of legal values for the data associated with this tag.

Returns

true

if the given data type
may be used for the data associated with this tag.

Returns

true

if this tag is used to point to an IFD
structure containing additional tags.

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

- TIFF_BYTE

```java
public static final int TIFF_BYTE
```

Flag for 8 bit unsigned integers.

**See Also:** Constant Field Values

- TIFF_ASCII

```java
public static final int TIFF_ASCII
```

Flag for null-terminated ASCII strings.

**See Also:** Constant Field Values

- TIFF_SHORT

```java
public static final int TIFF_SHORT
```

Flag for 16 bit unsigned integers.

**See Also:** Constant Field Values

- TIFF_LONG

```java
public static final int TIFF_LONG
```

Flag for 32 bit unsigned integers.

**See Also:** Constant Field Values

- TIFF_RATIONAL

```java
public static final int TIFF_RATIONAL
```

Flag for pairs of 32 bit unsigned integers.

**See Also:** Constant Field Values

- TIFF_SBYTE

```java
public static final int TIFF_SBYTE
```

Flag for 8 bit signed integers.

**See Also:** Constant Field Values

- TIFF_UNDEFINED

```java
public static final int TIFF_UNDEFINED
```

Flag for 8 bit uninterpreted bytes.

**See Also:** Constant Field Values

- TIFF_SSHORT

```java
public static final int TIFF_SSHORT
```

Flag for 16 bit signed integers.

**See Also:** Constant Field Values

- TIFF_SLONG

```java
public static final int TIFF_SLONG
```

Flag for 32 bit signed integers.

**See Also:** Constant Field Values

- TIFF_SRATIONAL

```java
public static final int TIFF_SRATIONAL
```

Flag for pairs of 32 bit signed integers.

**See Also:** Constant Field Values

- TIFF_FLOAT

```java
public static final int TIFF_FLOAT
```

Flag for 32 bit IEEE floats.

**See Also:** Constant Field Values

- TIFF_DOUBLE

```java
public static final int TIFF_DOUBLE
```

Flag for 64 bit IEEE doubles.

**See Also:** Constant Field Values

- TIFF_IFD_POINTER

```java
public static final int TIFF_IFD_POINTER
```

Flag for IFD pointer defined in TIFF Tech Note 1 in
TIFF Specification Supplement 1.

**See Also:** Constant Field Values

- MIN_DATATYPE

```java
public static final int MIN_DATATYPE
```

The numerically smallest constant representing a TIFF data type.

**See Also:** Constant Field Values

- MAX_DATATYPE

```java
public static final int MAX_DATATYPE
```

The numerically largest constant representing a TIFF data type.

**See Also:** Constant Field Values

- UNKNOWN_TAG_NAME

```java
public static final
String
UNKNOWN_TAG_NAME
```

The name assigned to a tag with an unknown tag number. Such
a tag may be created for example when reading an IFD and a
tag number is encountered which is not in any of the

TIFFTagSet

s known to the reader.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- TIFFTag

```java
public TIFFTag​(
String
name,
int number,
int dataTypes,
int count)
```

Constructs a

TIFFTag

with a given name, tag number, set
of legal data types, and value count. A negative value count signifies
that either an arbitrary number of values is legal or the required count
is determined by the values of other fields in the IFD. A non-negative
count specifies the number of values which an associated field must
contain. The tag will have no associated

TIFFTagSet

.

If there are mnemonic names to be associated with the legal
data values for the tag,

addValueName()

should be called on the new instance for each name.
Mnemonic names apply only to tags which have integral data type.

See the documentation for

getDataTypes()

for an explanation of how the set
of data types is to be converted into a bit mask.

**Parameters:** name

- the name of the tag.
**Parameters:** number

- the number used to represent the tag.
**Parameters:** dataTypes

- a bit mask indicating the set of legal data
types for this tag.
**Parameters:** count

- the value count for this tag.
**Throws:** NullPointerException

- if name is null.
**Throws:** IllegalArgumentException

- if number is negative or dataTypes
is negative or specifies an out of range type.

- TIFFTag

```java
public TIFFTag​(
String
name,
int number,

TIFFTagSet
tagSet)
```

Constructs a

TIFFTag

with a given name, tag number and

TIFFTagSet

to which it refers. The legal data types are
set to include

TIFF_LONG

and

TIFF_IFD_POINTER

and the
value count is unity. The

TIFFTagSet

will
represent the set of

TIFFTag

s which appear in the IFD
pointed to. A

TIFFTag

represents an IFD pointer if and
only if

tagSet

is non-

null

or the data
type

TIFF_IFD_POINTER

is legal.

**Parameters:** name

- the name of the tag.
**Parameters:** number

- the number used to represent the tag.
**Parameters:** tagSet

- the

TIFFTagSet

to which this tag belongs.
**Throws:** NullPointerException

- if name or tagSet is null.
**Throws:** IllegalArgumentException

- if number is negative.
**See Also:** TIFFTag(String, int, int, int)

- TIFFTag

```java
public TIFFTag​(
String
name,
int number,
int dataTypes)
```

Constructs a

TIFFTag

with a given name, tag number,
and set of legal data types. The value count of the tag will be
undefined and it will have no associated

TIFFTagSet

.

**Parameters:** name

- the name of the tag.
**Parameters:** number

- the number used to represent the tag.
**Parameters:** dataTypes

- a bit mask indicating the set of legal data
types for this tag.
**Throws:** NullPointerException

- if name is null.
**Throws:** IllegalArgumentException

- if number is negative or dataTypes
is negative or specifies an out of range type.
**See Also:** TIFFTag(String, int, int, int)

============ METHOD DETAIL ==========

- Method Detail

- getSizeOfType

```java
public static int getSizeOfType​(int dataType)
```

Returns the number of bytes used to store a value of the given
data type.

**Parameters:** dataType

- the data type to be queried.
**Returns:** the number of bytes used to store the given data type.
**Throws:** IllegalArgumentException

- if

datatype

is
less than

MIN_DATATYPE

or greater than

MAX_DATATYPE

.

- getName

```java
public
String
getName()
```

Returns the name of the tag, as it will appear in image metadata.

**Returns:** the tag name, as a

String

.

- getNumber

```java
public int getNumber()
```

Returns the integer used to represent the tag.

**Returns:** the tag number, as an

int

.

- getDataTypes

```java
public int getDataTypes()
```

Returns a bit mask indicating the set of data types that may
be used to store the data associated with the tag.
For example, a tag that can store both SHORT and LONG values
would return a value of:

```java
(1 << TIFFTag.TIFF_SHORT) | (1 << TIFFTag.TIFF_LONG)
```

**Returns:** an

int

containing a bitmask encoding the
set of valid data types.

- getCount

```java
public int getCount()
```

Returns the value count of this tag. If this value is positive, it
represents the required number of values for a

TIFFField

which has this tag. If the value is negative, the count is undefined.
In the latter case the count may be derived, e.g., the number of values
of the

BitsPerSample

field is

SamplesPerPixel

,
or it may be variable as in the case of most

US-ASCII

fields.

**Returns:** the value count of this tag.

- isDataTypeOK

```java
public boolean isDataTypeOK​(int dataType)
```

Returns

true

if the given data type
may be used for the data associated with this tag.

**Parameters:** dataType

- the data type to be queried, one of

TIFF_BYTE

,

TIFF_SHORT

, etc.
**Returns:** a

boolean

indicating whether the given
data type may be used with this tag.
**Throws:** IllegalArgumentException

- if

datatype

is
less than

MIN_DATATYPE

or greater than

MAX_DATATYPE

.

- getTagSet

```java
public
TIFFTagSet
getTagSet()
```

Returns the

TIFFTagSet

of which this tag is a part.

**Returns:** the containing

TIFFTagSet

.

- isIFDPointer

```java
public boolean isIFDPointer()
```

Returns

true

if this tag is used to point to an IFD
structure containing additional tags. A

TIFFTag

represents
an IFD pointer if and only if its

TIFFTagSet

is
non-

null

or the data type

TIFF_IFD_POINTER

is
legal. This condition will be satisfied if and only if either

getTagSet() != null

or

isDataTypeOK(TIFF_IFD_POINTER) == true

.

Many TIFF extensions use the IFD mechanism in order to limit the
number of new tags that may appear in the root IFD.

**Returns:** true

if this tag points to an IFD.

- hasValueNames

```java
public boolean hasValueNames()
```

Returns

true

if there are mnemonic names associated with
the set of legal values for the data associated with this tag. Mnemonic
names apply only to tags which have integral data type.

**Returns:** true

if mnemonic value names are available.

- addValueName

```java
protected void addValueName​(int value,

String
name)
```

Adds a mnemonic name for a particular value that this tag's data may take
on. Mnemonic names apply only to tags which have integral data type.

**Parameters:** value

- the data value.
**Parameters:** name

- the name to associate with the value.

- getValueName

```java
public
String
getValueName​(int value)
```

Returns the mnemonic name associated with a particular value
that this tag's data may take on, or

null

if
no name is present. Mnemonic names apply only to tags which have
integral data type.

**Parameters:** value

- the data value.
**Returns:** the mnemonic name associated with the value, as a

String

.

- getNamedValues

```java
public int[] getNamedValues()
```

Returns an array of values for which mnemonic names are defined. The
method

getValueName()

will return
non-

null

only for values contained in the returned array.
Mnemonic names apply only to tags which have integral data type.

**Returns:** the values for which there is a mnemonic name.

Field Detail

- TIFF_BYTE

```java
public static final int TIFF_BYTE
```

Flag for 8 bit unsigned integers.

**See Also:** Constant Field Values

- TIFF_ASCII

```java
public static final int TIFF_ASCII
```

Flag for null-terminated ASCII strings.

**See Also:** Constant Field Values

- TIFF_SHORT

```java
public static final int TIFF_SHORT
```

Flag for 16 bit unsigned integers.

**See Also:** Constant Field Values

- TIFF_LONG

```java
public static final int TIFF_LONG
```

Flag for 32 bit unsigned integers.

**See Also:** Constant Field Values

- TIFF_RATIONAL

```java
public static final int TIFF_RATIONAL
```

Flag for pairs of 32 bit unsigned integers.

**See Also:** Constant Field Values

- TIFF_SBYTE

```java
public static final int TIFF_SBYTE
```

Flag for 8 bit signed integers.

**See Also:** Constant Field Values

- TIFF_UNDEFINED

```java
public static final int TIFF_UNDEFINED
```

Flag for 8 bit uninterpreted bytes.

**See Also:** Constant Field Values

- TIFF_SSHORT

```java
public static final int TIFF_SSHORT
```

Flag for 16 bit signed integers.

**See Also:** Constant Field Values

- TIFF_SLONG

```java
public static final int TIFF_SLONG
```

Flag for 32 bit signed integers.

**See Also:** Constant Field Values

- TIFF_SRATIONAL

```java
public static final int TIFF_SRATIONAL
```

Flag for pairs of 32 bit signed integers.

**See Also:** Constant Field Values

- TIFF_FLOAT

```java
public static final int TIFF_FLOAT
```

Flag for 32 bit IEEE floats.

**See Also:** Constant Field Values

- TIFF_DOUBLE

```java
public static final int TIFF_DOUBLE
```

Flag for 64 bit IEEE doubles.

**See Also:** Constant Field Values

- TIFF_IFD_POINTER

```java
public static final int TIFF_IFD_POINTER
```

Flag for IFD pointer defined in TIFF Tech Note 1 in
TIFF Specification Supplement 1.

**See Also:** Constant Field Values

- MIN_DATATYPE

```java
public static final int MIN_DATATYPE
```

The numerically smallest constant representing a TIFF data type.

**See Also:** Constant Field Values

- MAX_DATATYPE

```java
public static final int MAX_DATATYPE
```

The numerically largest constant representing a TIFF data type.

**See Also:** Constant Field Values

- UNKNOWN_TAG_NAME

```java
public static final
String
UNKNOWN_TAG_NAME
```

The name assigned to a tag with an unknown tag number. Such
a tag may be created for example when reading an IFD and a
tag number is encountered which is not in any of the

TIFFTagSet

s known to the reader.

**See Also:** Constant Field Values

---

#### Field Detail

TIFF_BYTE

```java
public static final int TIFF_BYTE
```

Flag for 8 bit unsigned integers.

**See Also:** Constant Field Values

---

#### TIFF_BYTE

public static final int TIFF_BYTE

Flag for 8 bit unsigned integers.

TIFF_ASCII

```java
public static final int TIFF_ASCII
```

Flag for null-terminated ASCII strings.

**See Also:** Constant Field Values

---

#### TIFF_ASCII

public static final int TIFF_ASCII

Flag for null-terminated ASCII strings.

TIFF_SHORT

```java
public static final int TIFF_SHORT
```

Flag for 16 bit unsigned integers.

**See Also:** Constant Field Values

---

#### TIFF_SHORT

public static final int TIFF_SHORT

Flag for 16 bit unsigned integers.

TIFF_LONG

```java
public static final int TIFF_LONG
```

Flag for 32 bit unsigned integers.

**See Also:** Constant Field Values

---

#### TIFF_LONG

public static final int TIFF_LONG

Flag for 32 bit unsigned integers.

TIFF_RATIONAL

```java
public static final int TIFF_RATIONAL
```

Flag for pairs of 32 bit unsigned integers.

**See Also:** Constant Field Values

---

#### TIFF_RATIONAL

public static final int TIFF_RATIONAL

Flag for pairs of 32 bit unsigned integers.

TIFF_SBYTE

```java
public static final int TIFF_SBYTE
```

Flag for 8 bit signed integers.

**See Also:** Constant Field Values

---

#### TIFF_SBYTE

public static final int TIFF_SBYTE

Flag for 8 bit signed integers.

TIFF_UNDEFINED

```java
public static final int TIFF_UNDEFINED
```

Flag for 8 bit uninterpreted bytes.

**See Also:** Constant Field Values

---

#### TIFF_UNDEFINED

public static final int TIFF_UNDEFINED

Flag for 8 bit uninterpreted bytes.

TIFF_SSHORT

```java
public static final int TIFF_SSHORT
```

Flag for 16 bit signed integers.

**See Also:** Constant Field Values

---

#### TIFF_SSHORT

public static final int TIFF_SSHORT

Flag for 16 bit signed integers.

TIFF_SLONG

```java
public static final int TIFF_SLONG
```

Flag for 32 bit signed integers.

**See Also:** Constant Field Values

---

#### TIFF_SLONG

public static final int TIFF_SLONG

Flag for 32 bit signed integers.

TIFF_SRATIONAL

```java
public static final int TIFF_SRATIONAL
```

Flag for pairs of 32 bit signed integers.

**See Also:** Constant Field Values

---

#### TIFF_SRATIONAL

public static final int TIFF_SRATIONAL

Flag for pairs of 32 bit signed integers.

TIFF_FLOAT

```java
public static final int TIFF_FLOAT
```

Flag for 32 bit IEEE floats.

**See Also:** Constant Field Values

---

#### TIFF_FLOAT

public static final int TIFF_FLOAT

Flag for 32 bit IEEE floats.

TIFF_DOUBLE

```java
public static final int TIFF_DOUBLE
```

Flag for 64 bit IEEE doubles.

**See Also:** Constant Field Values

---

#### TIFF_DOUBLE

public static final int TIFF_DOUBLE

Flag for 64 bit IEEE doubles.

TIFF_IFD_POINTER

```java
public static final int TIFF_IFD_POINTER
```

Flag for IFD pointer defined in TIFF Tech Note 1 in
TIFF Specification Supplement 1.

**See Also:** Constant Field Values

---

#### TIFF_IFD_POINTER

public static final int TIFF_IFD_POINTER

Flag for IFD pointer defined in TIFF Tech Note 1 in
TIFF Specification Supplement 1.

MIN_DATATYPE

```java
public static final int MIN_DATATYPE
```

The numerically smallest constant representing a TIFF data type.

**See Also:** Constant Field Values

---

#### MIN_DATATYPE

public static final int MIN_DATATYPE

The numerically smallest constant representing a TIFF data type.

MAX_DATATYPE

```java
public static final int MAX_DATATYPE
```

The numerically largest constant representing a TIFF data type.

**See Also:** Constant Field Values

---

#### MAX_DATATYPE

public static final int MAX_DATATYPE

The numerically largest constant representing a TIFF data type.

UNKNOWN_TAG_NAME

```java
public static final
String
UNKNOWN_TAG_NAME
```

The name assigned to a tag with an unknown tag number. Such
a tag may be created for example when reading an IFD and a
tag number is encountered which is not in any of the

TIFFTagSet

s known to the reader.

**See Also:** Constant Field Values

---

#### UNKNOWN_TAG_NAME

public static final

String

UNKNOWN_TAG_NAME

The name assigned to a tag with an unknown tag number. Such
a tag may be created for example when reading an IFD and a
tag number is encountered which is not in any of the

TIFFTagSet

s known to the reader.

Constructor Detail

- TIFFTag

```java
public TIFFTag​(
String
name,
int number,
int dataTypes,
int count)
```

Constructs a

TIFFTag

with a given name, tag number, set
of legal data types, and value count. A negative value count signifies
that either an arbitrary number of values is legal or the required count
is determined by the values of other fields in the IFD. A non-negative
count specifies the number of values which an associated field must
contain. The tag will have no associated

TIFFTagSet

.

If there are mnemonic names to be associated with the legal
data values for the tag,

addValueName()

should be called on the new instance for each name.
Mnemonic names apply only to tags which have integral data type.

See the documentation for

getDataTypes()

for an explanation of how the set
of data types is to be converted into a bit mask.

**Parameters:** name

- the name of the tag.
**Parameters:** number

- the number used to represent the tag.
**Parameters:** dataTypes

- a bit mask indicating the set of legal data
types for this tag.
**Parameters:** count

- the value count for this tag.
**Throws:** NullPointerException

- if name is null.
**Throws:** IllegalArgumentException

- if number is negative or dataTypes
is negative or specifies an out of range type.

- TIFFTag

```java
public TIFFTag​(
String
name,
int number,

TIFFTagSet
tagSet)
```

Constructs a

TIFFTag

with a given name, tag number and

TIFFTagSet

to which it refers. The legal data types are
set to include

TIFF_LONG

and

TIFF_IFD_POINTER

and the
value count is unity. The

TIFFTagSet

will
represent the set of

TIFFTag

s which appear in the IFD
pointed to. A

TIFFTag

represents an IFD pointer if and
only if

tagSet

is non-

null

or the data
type

TIFF_IFD_POINTER

is legal.

**Parameters:** name

- the name of the tag.
**Parameters:** number

- the number used to represent the tag.
**Parameters:** tagSet

- the

TIFFTagSet

to which this tag belongs.
**Throws:** NullPointerException

- if name or tagSet is null.
**Throws:** IllegalArgumentException

- if number is negative.
**See Also:** TIFFTag(String, int, int, int)

- TIFFTag

```java
public TIFFTag​(
String
name,
int number,
int dataTypes)
```

Constructs a

TIFFTag

with a given name, tag number,
and set of legal data types. The value count of the tag will be
undefined and it will have no associated

TIFFTagSet

.

**Parameters:** name

- the name of the tag.
**Parameters:** number

- the number used to represent the tag.
**Parameters:** dataTypes

- a bit mask indicating the set of legal data
types for this tag.
**Throws:** NullPointerException

- if name is null.
**Throws:** IllegalArgumentException

- if number is negative or dataTypes
is negative or specifies an out of range type.
**See Also:** TIFFTag(String, int, int, int)

---

#### Constructor Detail

TIFFTag

```java
public TIFFTag​(
String
name,
int number,
int dataTypes,
int count)
```

Constructs a

TIFFTag

with a given name, tag number, set
of legal data types, and value count. A negative value count signifies
that either an arbitrary number of values is legal or the required count
is determined by the values of other fields in the IFD. A non-negative
count specifies the number of values which an associated field must
contain. The tag will have no associated

TIFFTagSet

.

If there are mnemonic names to be associated with the legal
data values for the tag,

addValueName()

should be called on the new instance for each name.
Mnemonic names apply only to tags which have integral data type.

See the documentation for

getDataTypes()

for an explanation of how the set
of data types is to be converted into a bit mask.

**Parameters:** name

- the name of the tag.
**Parameters:** number

- the number used to represent the tag.
**Parameters:** dataTypes

- a bit mask indicating the set of legal data
types for this tag.
**Parameters:** count

- the value count for this tag.
**Throws:** NullPointerException

- if name is null.
**Throws:** IllegalArgumentException

- if number is negative or dataTypes
is negative or specifies an out of range type.

---

#### TIFFTag

public TIFFTag​(

String

name,
int number,
int dataTypes,
int count)

Constructs a

TIFFTag

with a given name, tag number, set
of legal data types, and value count. A negative value count signifies
that either an arbitrary number of values is legal or the required count
is determined by the values of other fields in the IFD. A non-negative
count specifies the number of values which an associated field must
contain. The tag will have no associated

TIFFTagSet

.

If there are mnemonic names to be associated with the legal
data values for the tag,

addValueName()

should be called on the new instance for each name.
Mnemonic names apply only to tags which have integral data type.

See the documentation for

getDataTypes()

for an explanation of how the set
of data types is to be converted into a bit mask.

If there are mnemonic names to be associated with the legal
data values for the tag,

addValueName()

should be called on the new instance for each name.
Mnemonic names apply only to tags which have integral data type.

See the documentation for

getDataTypes()

for an explanation of how the set
of data types is to be converted into a bit mask.

TIFFTag

```java
public TIFFTag​(
String
name,
int number,

TIFFTagSet
tagSet)
```

Constructs a

TIFFTag

with a given name, tag number and

TIFFTagSet

to which it refers. The legal data types are
set to include

TIFF_LONG

and

TIFF_IFD_POINTER

and the
value count is unity. The

TIFFTagSet

will
represent the set of

TIFFTag

s which appear in the IFD
pointed to. A

TIFFTag

represents an IFD pointer if and
only if

tagSet

is non-

null

or the data
type

TIFF_IFD_POINTER

is legal.

**Parameters:** name

- the name of the tag.
**Parameters:** number

- the number used to represent the tag.
**Parameters:** tagSet

- the

TIFFTagSet

to which this tag belongs.
**Throws:** NullPointerException

- if name or tagSet is null.
**Throws:** IllegalArgumentException

- if number is negative.
**See Also:** TIFFTag(String, int, int, int)

---

#### TIFFTag

public TIFFTag​(

String

name,
int number,

TIFFTagSet

tagSet)

Constructs a

TIFFTag

with a given name, tag number and

TIFFTagSet

to which it refers. The legal data types are
set to include

TIFF_LONG

and

TIFF_IFD_POINTER

and the
value count is unity. The

TIFFTagSet

will
represent the set of

TIFFTag

s which appear in the IFD
pointed to. A

TIFFTag

represents an IFD pointer if and
only if

tagSet

is non-

null

or the data
type

TIFF_IFD_POINTER

is legal.

TIFFTag

```java
public TIFFTag​(
String
name,
int number,
int dataTypes)
```

Constructs a

TIFFTag

with a given name, tag number,
and set of legal data types. The value count of the tag will be
undefined and it will have no associated

TIFFTagSet

.

**Parameters:** name

- the name of the tag.
**Parameters:** number

- the number used to represent the tag.
**Parameters:** dataTypes

- a bit mask indicating the set of legal data
types for this tag.
**Throws:** NullPointerException

- if name is null.
**Throws:** IllegalArgumentException

- if number is negative or dataTypes
is negative or specifies an out of range type.
**See Also:** TIFFTag(String, int, int, int)

---

#### TIFFTag

public TIFFTag​(

String

name,
int number,
int dataTypes)

Constructs a

TIFFTag

with a given name, tag number,
and set of legal data types. The value count of the tag will be
undefined and it will have no associated

TIFFTagSet

.

Method Detail

- getSizeOfType

```java
public static int getSizeOfType​(int dataType)
```

Returns the number of bytes used to store a value of the given
data type.

**Parameters:** dataType

- the data type to be queried.
**Returns:** the number of bytes used to store the given data type.
**Throws:** IllegalArgumentException

- if

datatype

is
less than

MIN_DATATYPE

or greater than

MAX_DATATYPE

.

- getName

```java
public
String
getName()
```

Returns the name of the tag, as it will appear in image metadata.

**Returns:** the tag name, as a

String

.

- getNumber

```java
public int getNumber()
```

Returns the integer used to represent the tag.

**Returns:** the tag number, as an

int

.

- getDataTypes

```java
public int getDataTypes()
```

Returns a bit mask indicating the set of data types that may
be used to store the data associated with the tag.
For example, a tag that can store both SHORT and LONG values
would return a value of:

```java
(1 << TIFFTag.TIFF_SHORT) | (1 << TIFFTag.TIFF_LONG)
```

**Returns:** an

int

containing a bitmask encoding the
set of valid data types.

- getCount

```java
public int getCount()
```

Returns the value count of this tag. If this value is positive, it
represents the required number of values for a

TIFFField

which has this tag. If the value is negative, the count is undefined.
In the latter case the count may be derived, e.g., the number of values
of the

BitsPerSample

field is

SamplesPerPixel

,
or it may be variable as in the case of most

US-ASCII

fields.

**Returns:** the value count of this tag.

- isDataTypeOK

```java
public boolean isDataTypeOK​(int dataType)
```

Returns

true

if the given data type
may be used for the data associated with this tag.

**Parameters:** dataType

- the data type to be queried, one of

TIFF_BYTE

,

TIFF_SHORT

, etc.
**Returns:** a

boolean

indicating whether the given
data type may be used with this tag.
**Throws:** IllegalArgumentException

- if

datatype

is
less than

MIN_DATATYPE

or greater than

MAX_DATATYPE

.

- getTagSet

```java
public
TIFFTagSet
getTagSet()
```

Returns the

TIFFTagSet

of which this tag is a part.

**Returns:** the containing

TIFFTagSet

.

- isIFDPointer

```java
public boolean isIFDPointer()
```

Returns

true

if this tag is used to point to an IFD
structure containing additional tags. A

TIFFTag

represents
an IFD pointer if and only if its

TIFFTagSet

is
non-

null

or the data type

TIFF_IFD_POINTER

is
legal. This condition will be satisfied if and only if either

getTagSet() != null

or

isDataTypeOK(TIFF_IFD_POINTER) == true

.

Many TIFF extensions use the IFD mechanism in order to limit the
number of new tags that may appear in the root IFD.

**Returns:** true

if this tag points to an IFD.

- hasValueNames

```java
public boolean hasValueNames()
```

Returns

true

if there are mnemonic names associated with
the set of legal values for the data associated with this tag. Mnemonic
names apply only to tags which have integral data type.

**Returns:** true

if mnemonic value names are available.

- addValueName

```java
protected void addValueName​(int value,

String
name)
```

Adds a mnemonic name for a particular value that this tag's data may take
on. Mnemonic names apply only to tags which have integral data type.

**Parameters:** value

- the data value.
**Parameters:** name

- the name to associate with the value.

- getValueName

```java
public
String
getValueName​(int value)
```

Returns the mnemonic name associated with a particular value
that this tag's data may take on, or

null

if
no name is present. Mnemonic names apply only to tags which have
integral data type.

**Parameters:** value

- the data value.
**Returns:** the mnemonic name associated with the value, as a

String

.

- getNamedValues

```java
public int[] getNamedValues()
```

Returns an array of values for which mnemonic names are defined. The
method

getValueName()

will return
non-

null

only for values contained in the returned array.
Mnemonic names apply only to tags which have integral data type.

**Returns:** the values for which there is a mnemonic name.

---

#### Method Detail

getSizeOfType

```java
public static int getSizeOfType​(int dataType)
```

Returns the number of bytes used to store a value of the given
data type.

**Parameters:** dataType

- the data type to be queried.
**Returns:** the number of bytes used to store the given data type.
**Throws:** IllegalArgumentException

- if

datatype

is
less than

MIN_DATATYPE

or greater than

MAX_DATATYPE

.

---

#### getSizeOfType

public static int getSizeOfType​(int dataType)

Returns the number of bytes used to store a value of the given
data type.

getName

```java
public
String
getName()
```

Returns the name of the tag, as it will appear in image metadata.

**Returns:** the tag name, as a

String

.

---

#### getName

public

String

getName()

Returns the name of the tag, as it will appear in image metadata.

getNumber

```java
public int getNumber()
```

Returns the integer used to represent the tag.

**Returns:** the tag number, as an

int

.

---

#### getNumber

public int getNumber()

Returns the integer used to represent the tag.

getDataTypes

```java
public int getDataTypes()
```

Returns a bit mask indicating the set of data types that may
be used to store the data associated with the tag.
For example, a tag that can store both SHORT and LONG values
would return a value of:

```java
(1 << TIFFTag.TIFF_SHORT) | (1 << TIFFTag.TIFF_LONG)
```

**Returns:** an

int

containing a bitmask encoding the
set of valid data types.

---

#### getDataTypes

public int getDataTypes()

Returns a bit mask indicating the set of data types that may
be used to store the data associated with the tag.
For example, a tag that can store both SHORT and LONG values
would return a value of:

```java
(1 << TIFFTag.TIFF_SHORT) | (1 << TIFFTag.TIFF_LONG)
```

(1 << TIFFTag.TIFF_SHORT) | (1 << TIFFTag.TIFF_LONG)

getCount

```java
public int getCount()
```

Returns the value count of this tag. If this value is positive, it
represents the required number of values for a

TIFFField

which has this tag. If the value is negative, the count is undefined.
In the latter case the count may be derived, e.g., the number of values
of the

BitsPerSample

field is

SamplesPerPixel

,
or it may be variable as in the case of most

US-ASCII

fields.

**Returns:** the value count of this tag.

---

#### getCount

public int getCount()

Returns the value count of this tag. If this value is positive, it
represents the required number of values for a

TIFFField

which has this tag. If the value is negative, the count is undefined.
In the latter case the count may be derived, e.g., the number of values
of the

BitsPerSample

field is

SamplesPerPixel

,
or it may be variable as in the case of most

US-ASCII

fields.

isDataTypeOK

```java
public boolean isDataTypeOK​(int dataType)
```

Returns

true

if the given data type
may be used for the data associated with this tag.

**Parameters:** dataType

- the data type to be queried, one of

TIFF_BYTE

,

TIFF_SHORT

, etc.
**Returns:** a

boolean

indicating whether the given
data type may be used with this tag.
**Throws:** IllegalArgumentException

- if

datatype

is
less than

MIN_DATATYPE

or greater than

MAX_DATATYPE

.

---

#### isDataTypeOK

public boolean isDataTypeOK​(int dataType)

Returns

true

if the given data type
may be used for the data associated with this tag.

getTagSet

```java
public
TIFFTagSet
getTagSet()
```

Returns the

TIFFTagSet

of which this tag is a part.

**Returns:** the containing

TIFFTagSet

.

---

#### getTagSet

public

TIFFTagSet

getTagSet()

Returns the

TIFFTagSet

of which this tag is a part.

isIFDPointer

```java
public boolean isIFDPointer()
```

Returns

true

if this tag is used to point to an IFD
structure containing additional tags. A

TIFFTag

represents
an IFD pointer if and only if its

TIFFTagSet

is
non-

null

or the data type

TIFF_IFD_POINTER

is
legal. This condition will be satisfied if and only if either

getTagSet() != null

or

isDataTypeOK(TIFF_IFD_POINTER) == true

.

Many TIFF extensions use the IFD mechanism in order to limit the
number of new tags that may appear in the root IFD.

**Returns:** true

if this tag points to an IFD.

---

#### isIFDPointer

public boolean isIFDPointer()

Returns

true

if this tag is used to point to an IFD
structure containing additional tags. A

TIFFTag

represents
an IFD pointer if and only if its

TIFFTagSet

is
non-

null

or the data type

TIFF_IFD_POINTER

is
legal. This condition will be satisfied if and only if either

getTagSet() != null

or

isDataTypeOK(TIFF_IFD_POINTER) == true

.

Many TIFF extensions use the IFD mechanism in order to limit the
number of new tags that may appear in the root IFD.

Many TIFF extensions use the IFD mechanism in order to limit the
number of new tags that may appear in the root IFD.

hasValueNames

```java
public boolean hasValueNames()
```

Returns

true

if there are mnemonic names associated with
the set of legal values for the data associated with this tag. Mnemonic
names apply only to tags which have integral data type.

**Returns:** true

if mnemonic value names are available.

---

#### hasValueNames

public boolean hasValueNames()

Returns

true

if there are mnemonic names associated with
the set of legal values for the data associated with this tag. Mnemonic
names apply only to tags which have integral data type.

addValueName

```java
protected void addValueName​(int value,

String
name)
```

Adds a mnemonic name for a particular value that this tag's data may take
on. Mnemonic names apply only to tags which have integral data type.

**Parameters:** value

- the data value.
**Parameters:** name

- the name to associate with the value.

---

#### addValueName

protected void addValueName​(int value,

String

name)

Adds a mnemonic name for a particular value that this tag's data may take
on. Mnemonic names apply only to tags which have integral data type.

getValueName

```java
public
String
getValueName​(int value)
```

Returns the mnemonic name associated with a particular value
that this tag's data may take on, or

null

if
no name is present. Mnemonic names apply only to tags which have
integral data type.

**Parameters:** value

- the data value.
**Returns:** the mnemonic name associated with the value, as a

String

.

---

#### getValueName

public

String

getValueName​(int value)

Returns the mnemonic name associated with a particular value
that this tag's data may take on, or

null

if
no name is present. Mnemonic names apply only to tags which have
integral data type.

getNamedValues

```java
public int[] getNamedValues()
```

Returns an array of values for which mnemonic names are defined. The
method

getValueName()

will return
non-

null

only for values contained in the returned array.
Mnemonic names apply only to tags which have integral data type.

**Returns:** the values for which there is a mnemonic name.

---

#### getNamedValues

public int[] getNamedValues()

Returns an array of values for which mnemonic names are defined. The
method

getValueName()

will return
non-

null

only for values contained in the returned array.
Mnemonic names apply only to tags which have integral data type.

---

