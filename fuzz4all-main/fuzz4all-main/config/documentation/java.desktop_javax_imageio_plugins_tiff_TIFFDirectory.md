# Class TIFFDirectory

**Source:** `java.desktop\javax\imageio\plugins\tiff\TIFFDirectory.html`

### Class Description

```java
public class
TIFFDirectory

extends
Object

implements
Cloneable
```

A convenience class for simplifying interaction with TIFF native
image metadata. A TIFF image metadata tree represents an Image File
Directory (IFD) from a TIFF 6.0 stream. An IFD consists of a number of
IFD Entries each of which associates an identifying tag number with
a compatible value. A

TIFFDirectory

instance corresponds
to an IFD and contains a set of

TIFFField

s each of which
corresponds to an IFD Entry in the IFD.

When reading, a

TIFFDirectory

may be created by passing
the value returned by

ImageReader.getImageMetadata()

to

createFromMetadata()

. The

TIFFField

s in the directory may then
be obtained using the accessor methods provided in this class.

When writing, an

IIOMetadata

object for use by one of the

write()

methods of

ImageWriter

may be
created from a

TIFFDirectory

by

getAsMetadata()

.
The

TIFFDirectory

itself may be created by construction or
from the

IIOMetadata

object returned by

ImageWriter.getDefaultImageMetadata()

. The

TIFFField

s in the
directory may be set using the mutator methods provided in this class.

A

TIFFDirectory

is aware of the tag numbers in the
group of

TIFFTagSet

s associated with it. When
a

TIFFDirectory

is created from a native image metadata
object, these tag sets are derived from the

tagSets

attribute
of the

TIFFIFD

node.

A

TIFFDirectory

might also have a parent

TIFFTag

.
This will occur if the directory represents an IFD other than the root
IFD of the image. The parent tag is the tag of the IFD Entry which is a
pointer to the IFD represented by this

TIFFDirectory

. The

TIFFTag.isIFDPointer()

method of this parent

TIFFTag

must return

true

. When a

TIFFDirectory

is
created from a native image metadata object, the parent tag set is set
from the

parentTagName

attribute of the corresponding

TIFFIFD

node. Note that a

TIFFDirectory

instance
which has a non-

null

parent tag will be contained in the
data field of a

TIFFField

instance which has a tag field
equal to the contained directory's parent tag.

As an example consider an Exif image. The

TIFFDirectory

instance corresponding to the Exif IFD in the Exif stream would have parent
tag

TAG_EXIF_IFD_POINTER

and would include

ExifTIFFTagSet

in its group of known tag sets.
The

TIFFDirectory

corresponding to this Exif IFD will be
contained in the data field of a

TIFFField

which will in turn
be contained in the

TIFFDirectory

corresponding to the primary
IFD of the Exif image which will itself have a

null

-valued
parent tag.

Note that this implementation is not synchronized.

If multiple
threads use a

TIFFDirectory

instance concurrently, and at
least one of the threads modifies the directory, for example, by adding
or removing

TIFFField

s or

TIFFTagSet

s, it

must

be synchronized externally.

**All Implemented Interfaces:** Cloneable

---

### Field Details

*No entries found.*

### Constructor Details

#### public TIFFDirectory​(
TIFFTagSet
[] tagSets,

TIFFTag
parentTag)

Constructs a

TIFFDirectory

which is aware of a given
group of

TIFFTagSet

s. An optional parent

TIFFTag

may also be specified.

**Parameters:**
- tagSets

- The

TIFFTagSets

associated with this
directory.
- parentTag

- The parent

TIFFTag

of this directory;
may be

null

.

**Throws:**
- NullPointerException

- if

tagSets

is

null

.

---

### Method Details

#### public static
TIFFDirectory
createFromMetadata​(
IIOMetadata
tiffImageMetadata)
throws
IIOInvalidTreeException

Creates a

TIFFDirectory

instance from the contents of
an image metadata object. The supplied object must support an image
metadata format supported by the TIFF

ImageWriter

plug-in. This will usually be either the TIFF native image metadata
format

javax_imageio_tiff_image_1.0

or the Java
Image I/O standard metadata format

javax_imageio_1.0

.

**Parameters:**
- tiffImageMetadata

- A metadata object which supports a compatible
image metadata format.

**Returns:**
- A

TIFFDirectory

populated from the contents of
the supplied metadata object.

**Throws:**
- NullPointerException

- if

tiffImageMetadata

is

null

.
- IllegalArgumentException

- if

tiffImageMetadata

does not support a compatible image metadata format.
- IIOInvalidTreeException

- if the supplied metadata object
cannot be parsed.

---

#### public
TIFFTagSet
[] getTagSets()

Returns the

TIFFTagSet

s of which this directory is aware.

**Returns:**
- The

TIFFTagSet

s associated with this

TIFFDirectory

.

---

#### public void addTagSet​(
TIFFTagSet
tagSet)

Adds an element to the group of

TIFFTagSet

s of which this
directory is aware.

**Parameters:**
- tagSet

- The

TIFFTagSet

to add.

**Throws:**
- NullPointerException

- if

tagSet

is

null

.

---

#### public void removeTagSet​(
TIFFTagSet
tagSet)

Removes an element from the group of

TIFFTagSet

s of which this
directory is aware.

**Parameters:**
- tagSet

- The

TIFFTagSet

to remove.

**Throws:**
- NullPointerException

- if

tagSet

is

null

.

---

#### public
TIFFTag
getParentTag()

Returns the parent

TIFFTag

of this directory if one
has been defined or

null

otherwise.

**Returns:**
- The parent

TIFFTag

of this

TIFFDiectory

or

null

.

---

#### public
TIFFTag
getTag​(int tagNumber)

Returns the

TIFFTag

which has tag number equal to

tagNumber

or

null

if no such tag
exists in the

TIFFTagSet

s associated with this
directory.

**Parameters:**
- tagNumber

- The tag number of interest.

**Returns:**
- The corresponding

TIFFTag

or

null

.

---

#### public int getNumTIFFFields()

Returns the number of

TIFFField

s in this directory.

**Returns:**
- The number of

TIFFField

s in this

TIFFDirectory

.

---

#### public boolean containsTIFFField​(int tagNumber)

Determines whether a TIFF field with the given tag number is
contained in this directory.

**Parameters:**
- tagNumber

- The tag number.

**Returns:**
- Whether a

TIFFTag

with tag number equal to

tagNumber

is present in this

TIFFDirectory

.

---

#### public void addTIFFField​(
TIFFField
f)

Adds a TIFF field to the directory.

**Parameters:**
- f

- The field to add.

**Throws:**
- NullPointerException

- if

f

is

null

.

---

#### public
TIFFField
getTIFFField​(int tagNumber)

Retrieves a TIFF field from the directory.

**Parameters:**
- tagNumber

- The tag number of the tag associated with the field.

**Returns:**
- A

TIFFField

with the requested tag number of

null

if no such field is present.

---

#### public void removeTIFFField​(int tagNumber)

Removes a TIFF field from the directory.

**Parameters:**
- tagNumber

- The tag number of the tag associated with the field.

---

#### public
TIFFField
[] getTIFFFields()

Retrieves all TIFF fields from the directory.

**Returns:**
- An array of all TIFF fields in order of numerically increasing
tag number.

---

#### public void removeTIFFFields()

Removes all TIFF fields from the directory.

---

#### public
IIOMetadata
getAsMetadata()

Converts the directory to a metadata object.

**Returns:**
- A metadata instance initialized from the contents of this

TIFFDirectory

.

---

#### public
TIFFDirectory
clone()
throws
CloneNotSupportedException

Clones the directory and all the fields contained therein.

**Overrides:**
- clone

in class

Object

**Returns:**
- A clone of this

TIFFDirectory

.

**Throws:**
- CloneNotSupportedException

- if the instance cannot be cloned.

**See Also:**
- Cloneable

---

### Additional Sections

#### Class TIFFDirectory

java.lang.Object

- javax.imageio.plugins.tiff.TIFFDirectory

javax.imageio.plugins.tiff.TIFFDirectory

**All Implemented Interfaces:** Cloneable

```java
public class
TIFFDirectory

extends
Object

implements
Cloneable
```

A convenience class for simplifying interaction with TIFF native
image metadata. A TIFF image metadata tree represents an Image File
Directory (IFD) from a TIFF 6.0 stream. An IFD consists of a number of
IFD Entries each of which associates an identifying tag number with
a compatible value. A

TIFFDirectory

instance corresponds
to an IFD and contains a set of

TIFFField

s each of which
corresponds to an IFD Entry in the IFD.

When reading, a

TIFFDirectory

may be created by passing
the value returned by

ImageReader.getImageMetadata()

to

createFromMetadata()

. The

TIFFField

s in the directory may then
be obtained using the accessor methods provided in this class.

When writing, an

IIOMetadata

object for use by one of the

write()

methods of

ImageWriter

may be
created from a

TIFFDirectory

by

getAsMetadata()

.
The

TIFFDirectory

itself may be created by construction or
from the

IIOMetadata

object returned by

ImageWriter.getDefaultImageMetadata()

. The

TIFFField

s in the
directory may be set using the mutator methods provided in this class.

A

TIFFDirectory

is aware of the tag numbers in the
group of

TIFFTagSet

s associated with it. When
a

TIFFDirectory

is created from a native image metadata
object, these tag sets are derived from the

tagSets

attribute
of the

TIFFIFD

node.

A

TIFFDirectory

might also have a parent

TIFFTag

.
This will occur if the directory represents an IFD other than the root
IFD of the image. The parent tag is the tag of the IFD Entry which is a
pointer to the IFD represented by this

TIFFDirectory

. The

TIFFTag.isIFDPointer()

method of this parent

TIFFTag

must return

true

. When a

TIFFDirectory

is
created from a native image metadata object, the parent tag set is set
from the

parentTagName

attribute of the corresponding

TIFFIFD

node. Note that a

TIFFDirectory

instance
which has a non-

null

parent tag will be contained in the
data field of a

TIFFField

instance which has a tag field
equal to the contained directory's parent tag.

As an example consider an Exif image. The

TIFFDirectory

instance corresponding to the Exif IFD in the Exif stream would have parent
tag

TAG_EXIF_IFD_POINTER

and would include

ExifTIFFTagSet

in its group of known tag sets.
The

TIFFDirectory

corresponding to this Exif IFD will be
contained in the data field of a

TIFFField

which will in turn
be contained in the

TIFFDirectory

corresponding to the primary
IFD of the Exif image which will itself have a

null

-valued
parent tag.

Note that this implementation is not synchronized.

If multiple
threads use a

TIFFDirectory

instance concurrently, and at
least one of the threads modifies the directory, for example, by adding
or removing

TIFFField

s or

TIFFTagSet

s, it

must

be synchronized externally.

**Since:** 9
**See Also:** IIOMetadata

,

TIFFField

,

TIFFTag

,

TIFFTagSet

public class

TIFFDirectory

extends

Object

implements

Cloneable

A convenience class for simplifying interaction with TIFF native
image metadata. A TIFF image metadata tree represents an Image File
Directory (IFD) from a TIFF 6.0 stream. An IFD consists of a number of
IFD Entries each of which associates an identifying tag number with
a compatible value. A

TIFFDirectory

instance corresponds
to an IFD and contains a set of

TIFFField

s each of which
corresponds to an IFD Entry in the IFD.

When reading, a

TIFFDirectory

may be created by passing
the value returned by

ImageReader.getImageMetadata()

to

createFromMetadata()

. The

TIFFField

s in the directory may then
be obtained using the accessor methods provided in this class.

When writing, an

IIOMetadata

object for use by one of the

write()

methods of

ImageWriter

may be
created from a

TIFFDirectory

by

getAsMetadata()

.
The

TIFFDirectory

itself may be created by construction or
from the

IIOMetadata

object returned by

ImageWriter.getDefaultImageMetadata()

. The

TIFFField

s in the
directory may be set using the mutator methods provided in this class.

A

TIFFDirectory

is aware of the tag numbers in the
group of

TIFFTagSet

s associated with it. When
a

TIFFDirectory

is created from a native image metadata
object, these tag sets are derived from the

tagSets

attribute
of the

TIFFIFD

node.

A

TIFFDirectory

might also have a parent

TIFFTag

.
This will occur if the directory represents an IFD other than the root
IFD of the image. The parent tag is the tag of the IFD Entry which is a
pointer to the IFD represented by this

TIFFDirectory

. The

TIFFTag.isIFDPointer()

method of this parent

TIFFTag

must return

true

. When a

TIFFDirectory

is
created from a native image metadata object, the parent tag set is set
from the

parentTagName

attribute of the corresponding

TIFFIFD

node. Note that a

TIFFDirectory

instance
which has a non-

null

parent tag will be contained in the
data field of a

TIFFField

instance which has a tag field
equal to the contained directory's parent tag.

As an example consider an Exif image. The

TIFFDirectory

instance corresponding to the Exif IFD in the Exif stream would have parent
tag

TAG_EXIF_IFD_POINTER

and would include

ExifTIFFTagSet

in its group of known tag sets.
The

TIFFDirectory

corresponding to this Exif IFD will be
contained in the data field of a

TIFFField

which will in turn
be contained in the

TIFFDirectory

corresponding to the primary
IFD of the Exif image which will itself have a

null

-valued
parent tag.

Note that this implementation is not synchronized.

If multiple
threads use a

TIFFDirectory

instance concurrently, and at
least one of the threads modifies the directory, for example, by adding
or removing

TIFFField

s or

TIFFTagSet

s, it

must

be synchronized externally.

When reading, a

TIFFDirectory

may be created by passing
the value returned by

ImageReader.getImageMetadata()

to

createFromMetadata()

. The

TIFFField

s in the directory may then
be obtained using the accessor methods provided in this class.

When writing, an

IIOMetadata

object for use by one of the

write()

methods of

ImageWriter

may be
created from a

TIFFDirectory

by

getAsMetadata()

.
The

TIFFDirectory

itself may be created by construction or
from the

IIOMetadata

object returned by

ImageWriter.getDefaultImageMetadata()

. The

TIFFField

s in the
directory may be set using the mutator methods provided in this class.

A

TIFFDirectory

is aware of the tag numbers in the
group of

TIFFTagSet

s associated with it. When
a

TIFFDirectory

is created from a native image metadata
object, these tag sets are derived from the

tagSets

attribute
of the

TIFFIFD

node.

A

TIFFDirectory

might also have a parent

TIFFTag

.
This will occur if the directory represents an IFD other than the root
IFD of the image. The parent tag is the tag of the IFD Entry which is a
pointer to the IFD represented by this

TIFFDirectory

. The

TIFFTag.isIFDPointer()

method of this parent

TIFFTag

must return

true

. When a

TIFFDirectory

is
created from a native image metadata object, the parent tag set is set
from the

parentTagName

attribute of the corresponding

TIFFIFD

node. Note that a

TIFFDirectory

instance
which has a non-

null

parent tag will be contained in the
data field of a

TIFFField

instance which has a tag field
equal to the contained directory's parent tag.

As an example consider an Exif image. The

TIFFDirectory

instance corresponding to the Exif IFD in the Exif stream would have parent
tag

TAG_EXIF_IFD_POINTER

and would include

ExifTIFFTagSet

in its group of known tag sets.
The

TIFFDirectory

corresponding to this Exif IFD will be
contained in the data field of a

TIFFField

which will in turn
be contained in the

TIFFDirectory

corresponding to the primary
IFD of the Exif image which will itself have a

null

-valued
parent tag.

Note that this implementation is not synchronized.

If multiple
threads use a

TIFFDirectory

instance concurrently, and at
least one of the threads modifies the directory, for example, by adding
or removing

TIFFField

s or

TIFFTagSet

s, it

must

be synchronized externally.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

TIFFDirectory

​(

TIFFTagSet

[] tagSets,

TIFFTag

parentTag)

Constructs a

TIFFDirectory

which is aware of a given
group of

TIFFTagSet

s.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addTagSet

​(

TIFFTagSet

tagSet)

Adds an element to the group of

TIFFTagSet

s of which this
directory is aware.

void

addTIFFField

​(

TIFFField

f)

Adds a TIFF field to the directory.

TIFFDirectory

clone

()

Clones the directory and all the fields contained therein.

boolean

containsTIFFField

​(int tagNumber)

Determines whether a TIFF field with the given tag number is
contained in this directory.

static

TIFFDirectory

createFromMetadata

​(

IIOMetadata

tiffImageMetadata)

Creates a

TIFFDirectory

instance from the contents of
an image metadata object.

IIOMetadata

getAsMetadata

()

Converts the directory to a metadata object.

int

getNumTIFFFields

()

Returns the number of

TIFFField

s in this directory.

TIFFTag

getParentTag

()

Returns the parent

TIFFTag

of this directory if one
has been defined or

null

otherwise.

TIFFTag

getTag

​(int tagNumber)

Returns the

TIFFTag

which has tag number equal to

tagNumber

or

null

if no such tag
exists in the

TIFFTagSet

s associated with this
directory.

TIFFTagSet

[]

getTagSets

()

Returns the

TIFFTagSet

s of which this directory is aware.

TIFFField

getTIFFField

​(int tagNumber)

Retrieves a TIFF field from the directory.

TIFFField

[]

getTIFFFields

()

Retrieves all TIFF fields from the directory.

void

removeTagSet

​(

TIFFTagSet

tagSet)

Removes an element from the group of

TIFFTagSet

s of which this
directory is aware.

void

removeTIFFField

​(int tagNumber)

Removes a TIFF field from the directory.

void

removeTIFFFields

()

Removes all TIFF fields from the directory.

- Methods declared in class java.lang.

Object

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

Constructor Summary

Constructors

Constructor

Description

TIFFDirectory

​(

TIFFTagSet

[] tagSets,

TIFFTag

parentTag)

Constructs a

TIFFDirectory

which is aware of a given
group of

TIFFTagSet

s.

---

#### Constructor Summary

Constructs a

TIFFDirectory

which is aware of a given
group of

TIFFTagSet

s.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addTagSet

​(

TIFFTagSet

tagSet)

Adds an element to the group of

TIFFTagSet

s of which this
directory is aware.

void

addTIFFField

​(

TIFFField

f)

Adds a TIFF field to the directory.

TIFFDirectory

clone

()

Clones the directory and all the fields contained therein.

boolean

containsTIFFField

​(int tagNumber)

Determines whether a TIFF field with the given tag number is
contained in this directory.

static

TIFFDirectory

createFromMetadata

​(

IIOMetadata

tiffImageMetadata)

Creates a

TIFFDirectory

instance from the contents of
an image metadata object.

IIOMetadata

getAsMetadata

()

Converts the directory to a metadata object.

int

getNumTIFFFields

()

Returns the number of

TIFFField

s in this directory.

TIFFTag

getParentTag

()

Returns the parent

TIFFTag

of this directory if one
has been defined or

null

otherwise.

TIFFTag

getTag

​(int tagNumber)

Returns the

TIFFTag

which has tag number equal to

tagNumber

or

null

if no such tag
exists in the

TIFFTagSet

s associated with this
directory.

TIFFTagSet

[]

getTagSets

()

Returns the

TIFFTagSet

s of which this directory is aware.

TIFFField

getTIFFField

​(int tagNumber)

Retrieves a TIFF field from the directory.

TIFFField

[]

getTIFFFields

()

Retrieves all TIFF fields from the directory.

void

removeTagSet

​(

TIFFTagSet

tagSet)

Removes an element from the group of

TIFFTagSet

s of which this
directory is aware.

void

removeTIFFField

​(int tagNumber)

Removes a TIFF field from the directory.

void

removeTIFFFields

()

Removes all TIFF fields from the directory.

- Methods declared in class java.lang.

Object

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

Adds an element to the group of

TIFFTagSet

s of which this
directory is aware.

Adds a TIFF field to the directory.

Clones the directory and all the fields contained therein.

Determines whether a TIFF field with the given tag number is
contained in this directory.

Creates a

TIFFDirectory

instance from the contents of
an image metadata object.

Converts the directory to a metadata object.

Returns the number of

TIFFField

s in this directory.

Returns the parent

TIFFTag

of this directory if one
has been defined or

null

otherwise.

Returns the

TIFFTag

which has tag number equal to

tagNumber

or

null

if no such tag
exists in the

TIFFTagSet

s associated with this
directory.

Returns the

TIFFTagSet

s of which this directory is aware.

Retrieves a TIFF field from the directory.

Retrieves all TIFF fields from the directory.

Removes an element from the group of

TIFFTagSet

s of which this
directory is aware.

Removes a TIFF field from the directory.

Removes all TIFF fields from the directory.

Methods declared in class java.lang.

Object

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- TIFFDirectory

```java
public TIFFDirectory​(
TIFFTagSet
[] tagSets,

TIFFTag
parentTag)
```

Constructs a

TIFFDirectory

which is aware of a given
group of

TIFFTagSet

s. An optional parent

TIFFTag

may also be specified.

**Parameters:** tagSets

- The

TIFFTagSets

associated with this
directory.
**Parameters:** parentTag

- The parent

TIFFTag

of this directory;
may be

null

.
**Throws:** NullPointerException

- if

tagSets

is

null

.

============ METHOD DETAIL ==========

- Method Detail

- createFromMetadata

```java
public static
TIFFDirectory
createFromMetadata​(
IIOMetadata
tiffImageMetadata)
throws
IIOInvalidTreeException
```

Creates a

TIFFDirectory

instance from the contents of
an image metadata object. The supplied object must support an image
metadata format supported by the TIFF

ImageWriter

plug-in. This will usually be either the TIFF native image metadata
format

javax_imageio_tiff_image_1.0

or the Java
Image I/O standard metadata format

javax_imageio_1.0

.

**Parameters:** tiffImageMetadata

- A metadata object which supports a compatible
image metadata format.
**Returns:** A

TIFFDirectory

populated from the contents of
the supplied metadata object.
**Throws:** NullPointerException

- if

tiffImageMetadata

is

null

.
**Throws:** IllegalArgumentException

- if

tiffImageMetadata

does not support a compatible image metadata format.
**Throws:** IIOInvalidTreeException

- if the supplied metadata object
cannot be parsed.

- getTagSets

```java
public
TIFFTagSet
[] getTagSets()
```

Returns the

TIFFTagSet

s of which this directory is aware.

**Returns:** The

TIFFTagSet

s associated with this

TIFFDirectory

.

- addTagSet

```java
public void addTagSet​(
TIFFTagSet
tagSet)
```

Adds an element to the group of

TIFFTagSet

s of which this
directory is aware.

**Parameters:** tagSet

- The

TIFFTagSet

to add.
**Throws:** NullPointerException

- if

tagSet

is

null

.

- removeTagSet

```java
public void removeTagSet​(
TIFFTagSet
tagSet)
```

Removes an element from the group of

TIFFTagSet

s of which this
directory is aware.

**Parameters:** tagSet

- The

TIFFTagSet

to remove.
**Throws:** NullPointerException

- if

tagSet

is

null

.

- getParentTag

```java
public
TIFFTag
getParentTag()
```

Returns the parent

TIFFTag

of this directory if one
has been defined or

null

otherwise.

**Returns:** The parent

TIFFTag

of this

TIFFDiectory

or

null

.

- getTag

```java
public
TIFFTag
getTag​(int tagNumber)
```

Returns the

TIFFTag

which has tag number equal to

tagNumber

or

null

if no such tag
exists in the

TIFFTagSet

s associated with this
directory.

**Parameters:** tagNumber

- The tag number of interest.
**Returns:** The corresponding

TIFFTag

or

null

.

- getNumTIFFFields

```java
public int getNumTIFFFields()
```

Returns the number of

TIFFField

s in this directory.

**Returns:** The number of

TIFFField

s in this

TIFFDirectory

.

- containsTIFFField

```java
public boolean containsTIFFField​(int tagNumber)
```

Determines whether a TIFF field with the given tag number is
contained in this directory.

**Parameters:** tagNumber

- The tag number.
**Returns:** Whether a

TIFFTag

with tag number equal to

tagNumber

is present in this

TIFFDirectory

.

- addTIFFField

```java
public void addTIFFField​(
TIFFField
f)
```

Adds a TIFF field to the directory.

**Parameters:** f

- The field to add.
**Throws:** NullPointerException

- if

f

is

null

.

- getTIFFField

```java
public
TIFFField
getTIFFField​(int tagNumber)
```

Retrieves a TIFF field from the directory.

**Parameters:** tagNumber

- The tag number of the tag associated with the field.
**Returns:** A

TIFFField

with the requested tag number of

null

if no such field is present.

- removeTIFFField

```java
public void removeTIFFField​(int tagNumber)
```

Removes a TIFF field from the directory.

**Parameters:** tagNumber

- The tag number of the tag associated with the field.

- getTIFFFields

```java
public
TIFFField
[] getTIFFFields()
```

Retrieves all TIFF fields from the directory.

**Returns:** An array of all TIFF fields in order of numerically increasing
tag number.

- removeTIFFFields

```java
public void removeTIFFFields()
```

Removes all TIFF fields from the directory.

- getAsMetadata

```java
public
IIOMetadata
getAsMetadata()
```

Converts the directory to a metadata object.

**Returns:** A metadata instance initialized from the contents of this

TIFFDirectory

.

- clone

```java
public
TIFFDirectory
clone()
throws
CloneNotSupportedException
```

Clones the directory and all the fields contained therein.

**Overrides:** clone

in class

Object
**Returns:** A clone of this

TIFFDirectory

.
**Throws:** CloneNotSupportedException

- if the instance cannot be cloned.
**See Also:** Cloneable

Constructor Detail

- TIFFDirectory

```java
public TIFFDirectory​(
TIFFTagSet
[] tagSets,

TIFFTag
parentTag)
```

Constructs a

TIFFDirectory

which is aware of a given
group of

TIFFTagSet

s. An optional parent

TIFFTag

may also be specified.

**Parameters:** tagSets

- The

TIFFTagSets

associated with this
directory.
**Parameters:** parentTag

- The parent

TIFFTag

of this directory;
may be

null

.
**Throws:** NullPointerException

- if

tagSets

is

null

.

---

#### Constructor Detail

TIFFDirectory

```java
public TIFFDirectory​(
TIFFTagSet
[] tagSets,

TIFFTag
parentTag)
```

Constructs a

TIFFDirectory

which is aware of a given
group of

TIFFTagSet

s. An optional parent

TIFFTag

may also be specified.

**Parameters:** tagSets

- The

TIFFTagSets

associated with this
directory.
**Parameters:** parentTag

- The parent

TIFFTag

of this directory;
may be

null

.
**Throws:** NullPointerException

- if

tagSets

is

null

.

---

#### TIFFDirectory

public TIFFDirectory​(

TIFFTagSet

[] tagSets,

TIFFTag

parentTag)

Constructs a

TIFFDirectory

which is aware of a given
group of

TIFFTagSet

s. An optional parent

TIFFTag

may also be specified.

Method Detail

- createFromMetadata

```java
public static
TIFFDirectory
createFromMetadata​(
IIOMetadata
tiffImageMetadata)
throws
IIOInvalidTreeException
```

Creates a

TIFFDirectory

instance from the contents of
an image metadata object. The supplied object must support an image
metadata format supported by the TIFF

ImageWriter

plug-in. This will usually be either the TIFF native image metadata
format

javax_imageio_tiff_image_1.0

or the Java
Image I/O standard metadata format

javax_imageio_1.0

.

**Parameters:** tiffImageMetadata

- A metadata object which supports a compatible
image metadata format.
**Returns:** A

TIFFDirectory

populated from the contents of
the supplied metadata object.
**Throws:** NullPointerException

- if

tiffImageMetadata

is

null

.
**Throws:** IllegalArgumentException

- if

tiffImageMetadata

does not support a compatible image metadata format.
**Throws:** IIOInvalidTreeException

- if the supplied metadata object
cannot be parsed.

- getTagSets

```java
public
TIFFTagSet
[] getTagSets()
```

Returns the

TIFFTagSet

s of which this directory is aware.

**Returns:** The

TIFFTagSet

s associated with this

TIFFDirectory

.

- addTagSet

```java
public void addTagSet​(
TIFFTagSet
tagSet)
```

Adds an element to the group of

TIFFTagSet

s of which this
directory is aware.

**Parameters:** tagSet

- The

TIFFTagSet

to add.
**Throws:** NullPointerException

- if

tagSet

is

null

.

- removeTagSet

```java
public void removeTagSet​(
TIFFTagSet
tagSet)
```

Removes an element from the group of

TIFFTagSet

s of which this
directory is aware.

**Parameters:** tagSet

- The

TIFFTagSet

to remove.
**Throws:** NullPointerException

- if

tagSet

is

null

.

- getParentTag

```java
public
TIFFTag
getParentTag()
```

Returns the parent

TIFFTag

of this directory if one
has been defined or

null

otherwise.

**Returns:** The parent

TIFFTag

of this

TIFFDiectory

or

null

.

- getTag

```java
public
TIFFTag
getTag​(int tagNumber)
```

Returns the

TIFFTag

which has tag number equal to

tagNumber

or

null

if no such tag
exists in the

TIFFTagSet

s associated with this
directory.

**Parameters:** tagNumber

- The tag number of interest.
**Returns:** The corresponding

TIFFTag

or

null

.

- getNumTIFFFields

```java
public int getNumTIFFFields()
```

Returns the number of

TIFFField

s in this directory.

**Returns:** The number of

TIFFField

s in this

TIFFDirectory

.

- containsTIFFField

```java
public boolean containsTIFFField​(int tagNumber)
```

Determines whether a TIFF field with the given tag number is
contained in this directory.

**Parameters:** tagNumber

- The tag number.
**Returns:** Whether a

TIFFTag

with tag number equal to

tagNumber

is present in this

TIFFDirectory

.

- addTIFFField

```java
public void addTIFFField​(
TIFFField
f)
```

Adds a TIFF field to the directory.

**Parameters:** f

- The field to add.
**Throws:** NullPointerException

- if

f

is

null

.

- getTIFFField

```java
public
TIFFField
getTIFFField​(int tagNumber)
```

Retrieves a TIFF field from the directory.

**Parameters:** tagNumber

- The tag number of the tag associated with the field.
**Returns:** A

TIFFField

with the requested tag number of

null

if no such field is present.

- removeTIFFField

```java
public void removeTIFFField​(int tagNumber)
```

Removes a TIFF field from the directory.

**Parameters:** tagNumber

- The tag number of the tag associated with the field.

- getTIFFFields

```java
public
TIFFField
[] getTIFFFields()
```

Retrieves all TIFF fields from the directory.

**Returns:** An array of all TIFF fields in order of numerically increasing
tag number.

- removeTIFFFields

```java
public void removeTIFFFields()
```

Removes all TIFF fields from the directory.

- getAsMetadata

```java
public
IIOMetadata
getAsMetadata()
```

Converts the directory to a metadata object.

**Returns:** A metadata instance initialized from the contents of this

TIFFDirectory

.

- clone

```java
public
TIFFDirectory
clone()
throws
CloneNotSupportedException
```

Clones the directory and all the fields contained therein.

**Overrides:** clone

in class

Object
**Returns:** A clone of this

TIFFDirectory

.
**Throws:** CloneNotSupportedException

- if the instance cannot be cloned.
**See Also:** Cloneable

---

#### Method Detail

createFromMetadata

```java
public static
TIFFDirectory
createFromMetadata​(
IIOMetadata
tiffImageMetadata)
throws
IIOInvalidTreeException
```

Creates a

TIFFDirectory

instance from the contents of
an image metadata object. The supplied object must support an image
metadata format supported by the TIFF

ImageWriter

plug-in. This will usually be either the TIFF native image metadata
format

javax_imageio_tiff_image_1.0

or the Java
Image I/O standard metadata format

javax_imageio_1.0

.

**Parameters:** tiffImageMetadata

- A metadata object which supports a compatible
image metadata format.
**Returns:** A

TIFFDirectory

populated from the contents of
the supplied metadata object.
**Throws:** NullPointerException

- if

tiffImageMetadata

is

null

.
**Throws:** IllegalArgumentException

- if

tiffImageMetadata

does not support a compatible image metadata format.
**Throws:** IIOInvalidTreeException

- if the supplied metadata object
cannot be parsed.

---

#### createFromMetadata

public static

TIFFDirectory

createFromMetadata​(

IIOMetadata

tiffImageMetadata)
throws

IIOInvalidTreeException

Creates a

TIFFDirectory

instance from the contents of
an image metadata object. The supplied object must support an image
metadata format supported by the TIFF

ImageWriter

plug-in. This will usually be either the TIFF native image metadata
format

javax_imageio_tiff_image_1.0

or the Java
Image I/O standard metadata format

javax_imageio_1.0

.

getTagSets

```java
public
TIFFTagSet
[] getTagSets()
```

Returns the

TIFFTagSet

s of which this directory is aware.

**Returns:** The

TIFFTagSet

s associated with this

TIFFDirectory

.

---

#### getTagSets

public

TIFFTagSet

[] getTagSets()

Returns the

TIFFTagSet

s of which this directory is aware.

addTagSet

```java
public void addTagSet​(
TIFFTagSet
tagSet)
```

Adds an element to the group of

TIFFTagSet

s of which this
directory is aware.

**Parameters:** tagSet

- The

TIFFTagSet

to add.
**Throws:** NullPointerException

- if

tagSet

is

null

.

---

#### addTagSet

public void addTagSet​(

TIFFTagSet

tagSet)

Adds an element to the group of

TIFFTagSet

s of which this
directory is aware.

removeTagSet

```java
public void removeTagSet​(
TIFFTagSet
tagSet)
```

Removes an element from the group of

TIFFTagSet

s of which this
directory is aware.

**Parameters:** tagSet

- The

TIFFTagSet

to remove.
**Throws:** NullPointerException

- if

tagSet

is

null

.

---

#### removeTagSet

public void removeTagSet​(

TIFFTagSet

tagSet)

Removes an element from the group of

TIFFTagSet

s of which this
directory is aware.

getParentTag

```java
public
TIFFTag
getParentTag()
```

Returns the parent

TIFFTag

of this directory if one
has been defined or

null

otherwise.

**Returns:** The parent

TIFFTag

of this

TIFFDiectory

or

null

.

---

#### getParentTag

public

TIFFTag

getParentTag()

Returns the parent

TIFFTag

of this directory if one
has been defined or

null

otherwise.

getTag

```java
public
TIFFTag
getTag​(int tagNumber)
```

Returns the

TIFFTag

which has tag number equal to

tagNumber

or

null

if no such tag
exists in the

TIFFTagSet

s associated with this
directory.

**Parameters:** tagNumber

- The tag number of interest.
**Returns:** The corresponding

TIFFTag

or

null

.

---

#### getTag

public

TIFFTag

getTag​(int tagNumber)

Returns the

TIFFTag

which has tag number equal to

tagNumber

or

null

if no such tag
exists in the

TIFFTagSet

s associated with this
directory.

getNumTIFFFields

```java
public int getNumTIFFFields()
```

Returns the number of

TIFFField

s in this directory.

**Returns:** The number of

TIFFField

s in this

TIFFDirectory

.

---

#### getNumTIFFFields

public int getNumTIFFFields()

Returns the number of

TIFFField

s in this directory.

containsTIFFField

```java
public boolean containsTIFFField​(int tagNumber)
```

Determines whether a TIFF field with the given tag number is
contained in this directory.

**Parameters:** tagNumber

- The tag number.
**Returns:** Whether a

TIFFTag

with tag number equal to

tagNumber

is present in this

TIFFDirectory

.

---

#### containsTIFFField

public boolean containsTIFFField​(int tagNumber)

Determines whether a TIFF field with the given tag number is
contained in this directory.

addTIFFField

```java
public void addTIFFField​(
TIFFField
f)
```

Adds a TIFF field to the directory.

**Parameters:** f

- The field to add.
**Throws:** NullPointerException

- if

f

is

null

.

---

#### addTIFFField

public void addTIFFField​(

TIFFField

f)

Adds a TIFF field to the directory.

getTIFFField

```java
public
TIFFField
getTIFFField​(int tagNumber)
```

Retrieves a TIFF field from the directory.

**Parameters:** tagNumber

- The tag number of the tag associated with the field.
**Returns:** A

TIFFField

with the requested tag number of

null

if no such field is present.

---

#### getTIFFField

public

TIFFField

getTIFFField​(int tagNumber)

Retrieves a TIFF field from the directory.

removeTIFFField

```java
public void removeTIFFField​(int tagNumber)
```

Removes a TIFF field from the directory.

**Parameters:** tagNumber

- The tag number of the tag associated with the field.

---

#### removeTIFFField

public void removeTIFFField​(int tagNumber)

Removes a TIFF field from the directory.

getTIFFFields

```java
public
TIFFField
[] getTIFFFields()
```

Retrieves all TIFF fields from the directory.

**Returns:** An array of all TIFF fields in order of numerically increasing
tag number.

---

#### getTIFFFields

public

TIFFField

[] getTIFFFields()

Retrieves all TIFF fields from the directory.

removeTIFFFields

```java
public void removeTIFFFields()
```

Removes all TIFF fields from the directory.

---

#### removeTIFFFields

public void removeTIFFFields()

Removes all TIFF fields from the directory.

getAsMetadata

```java
public
IIOMetadata
getAsMetadata()
```

Converts the directory to a metadata object.

**Returns:** A metadata instance initialized from the contents of this

TIFFDirectory

.

---

#### getAsMetadata

public

IIOMetadata

getAsMetadata()

Converts the directory to a metadata object.

clone

```java
public
TIFFDirectory
clone()
throws
CloneNotSupportedException
```

Clones the directory and all the fields contained therein.

**Overrides:** clone

in class

Object
**Returns:** A clone of this

TIFFDirectory

.
**Throws:** CloneNotSupportedException

- if the instance cannot be cloned.
**See Also:** Cloneable

---

#### clone

public

TIFFDirectory

clone()
throws

CloneNotSupportedException

Clones the directory and all the fields contained therein.

---

