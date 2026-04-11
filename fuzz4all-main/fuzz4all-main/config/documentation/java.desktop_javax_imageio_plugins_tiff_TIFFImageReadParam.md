# Class TIFFImageReadParam

**Source:** `java.desktop\javax\imageio\plugins\tiff\TIFFImageReadParam.html`

### Class Description

```java
public final class
TIFFImageReadParam

extends
ImageReadParam
```

A subclass of

ImageReadParam

allowing control over
the TIFF reading process.

Because TIFF is an extensible format, the reader requires
information about any tags used by TIFF extensions in order to emit
meaningful metadata. Also, TIFF extensions may define new
compression types. Both types of information about extensions may
be provided by this interface.

Additional TIFF tags must be organized into

TIFFTagSet

s. A

TIFFTagSet

may be
provided to the reader by means of the

addAllowedTagSet

method. By default, the tag sets

BaselineTIFFTagSet

,

FaxTIFFTagSet

,

ExifParentTIFFTagSet

, and

GeoTIFFTagSet

are included.

Forcing reading of fields corresponding to

TIFFTag

s
not in any of the allowed

TIFFTagSet

s may be effected via

setReadUnknownTags

.

**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

#### public TIFFImageReadParam()

Constructs a

TIFFImageReadParam

. Tags defined by
the

TIFFTagSet

s

BaselineTIFFTagSet

,

FaxTIFFTagSet

,

ExifParentTIFFTagSet

, and

GeoTIFFTagSet

will be supported.

**See Also:**
- BaselineTIFFTagSet

,

FaxTIFFTagSet

,

ExifParentTIFFTagSet

,

GeoTIFFTagSet

---

### Method Details

#### public void addAllowedTagSet​(
TIFFTagSet
tagSet)

Adds a

TIFFTagSet

object to the list of allowed
tag sets. Attempting to add a duplicate object to the list
has no effect.

**Parameters:**
- tagSet

- a

TIFFTagSet

.

**Throws:**
- IllegalArgumentException

- if

tagSet

is

null

.

---

#### public void removeAllowedTagSet​(
TIFFTagSet
tagSet)

Removes a

TIFFTagSet

object from the list of
allowed tag sets. Removal is based on the

equals

method of the

TIFFTagSet

, which is normally
defined as reference equality.

**Parameters:**
- tagSet

- a

TIFFTagSet

.

**Throws:**
- IllegalArgumentException

- if

tagSet

is

null

.

---

#### public
List
<
TIFFTagSet
> getAllowedTagSets()

Returns a

List

containing the allowed

TIFFTagSet

objects.

**Returns:**
- a

List

of

TIFFTagSet

s.

---

#### public void setReadUnknownTags​(boolean readUnknownTags)

Set whether to read fields corresponding to

TIFFTag

s not in
the allowed

TIFFTagSet

s. The default setting is

false

.
If the TIFF

ImageReader

is ignoring metadata, then a setting
of

true

is overridden as all metadata are ignored except those
essential to reading the image itself.

**Parameters:**
- readUnknownTags

- Whether to read fields of unrecognized tags

---

#### public boolean getReadUnknownTags()

Retrieve the setting of whether to read fields corresponding to unknown

TIFFTag

s.

**Returns:**
- Whether to read fields of unrecognized tags

---

### Additional Sections

#### Class TIFFImageReadParam

java.lang.Object

- javax.imageio.IIOParam
- - javax.imageio.ImageReadParam
- - javax.imageio.plugins.tiff.TIFFImageReadParam

javax.imageio.IIOParam

- javax.imageio.ImageReadParam
- - javax.imageio.plugins.tiff.TIFFImageReadParam

javax.imageio.ImageReadParam

- javax.imageio.plugins.tiff.TIFFImageReadParam

javax.imageio.plugins.tiff.TIFFImageReadParam

```java
public final class
TIFFImageReadParam

extends
ImageReadParam
```

A subclass of

ImageReadParam

allowing control over
the TIFF reading process.

Because TIFF is an extensible format, the reader requires
information about any tags used by TIFF extensions in order to emit
meaningful metadata. Also, TIFF extensions may define new
compression types. Both types of information about extensions may
be provided by this interface.

Additional TIFF tags must be organized into

TIFFTagSet

s. A

TIFFTagSet

may be
provided to the reader by means of the

addAllowedTagSet

method. By default, the tag sets

BaselineTIFFTagSet

,

FaxTIFFTagSet

,

ExifParentTIFFTagSet

, and

GeoTIFFTagSet

are included.

Forcing reading of fields corresponding to

TIFFTag

s
not in any of the allowed

TIFFTagSet

s may be effected via

setReadUnknownTags

.

**Since:** 9

public final class

TIFFImageReadParam

extends

ImageReadParam

A subclass of

ImageReadParam

allowing control over
the TIFF reading process.

Because TIFF is an extensible format, the reader requires
information about any tags used by TIFF extensions in order to emit
meaningful metadata. Also, TIFF extensions may define new
compression types. Both types of information about extensions may
be provided by this interface.

Additional TIFF tags must be organized into

TIFFTagSet

s. A

TIFFTagSet

may be
provided to the reader by means of the

addAllowedTagSet

method. By default, the tag sets

BaselineTIFFTagSet

,

FaxTIFFTagSet

,

ExifParentTIFFTagSet

, and

GeoTIFFTagSet

are included.

Forcing reading of fields corresponding to

TIFFTag

s
not in any of the allowed

TIFFTagSet

s may be effected via

setReadUnknownTags

.

Because TIFF is an extensible format, the reader requires
information about any tags used by TIFF extensions in order to emit
meaningful metadata. Also, TIFF extensions may define new
compression types. Both types of information about extensions may
be provided by this interface.

Additional TIFF tags must be organized into

TIFFTagSet

s. A

TIFFTagSet

may be
provided to the reader by means of the

addAllowedTagSet

method. By default, the tag sets

BaselineTIFFTagSet

,

FaxTIFFTagSet

,

ExifParentTIFFTagSet

, and

GeoTIFFTagSet

are included.

Forcing reading of fields corresponding to

TIFFTag

s
not in any of the allowed

TIFFTagSet

s may be effected via

setReadUnknownTags

.

Additional TIFF tags must be organized into

TIFFTagSet

s. A

TIFFTagSet

may be
provided to the reader by means of the

addAllowedTagSet

method. By default, the tag sets

BaselineTIFFTagSet

,

FaxTIFFTagSet

,

ExifParentTIFFTagSet

, and

GeoTIFFTagSet

are included.

Forcing reading of fields corresponding to

TIFFTag

s
not in any of the allowed

TIFFTagSet

s may be effected via

setReadUnknownTags

.

Forcing reading of fields corresponding to

TIFFTag

s
not in any of the allowed

TIFFTagSet

s may be effected via

setReadUnknownTags

.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.imageio.

ImageReadParam

canSetSourceRenderSize

,

destination

,

destinationBands

,

minProgressivePass

,

numProgressivePasses

,

sourceRenderSize

- Fields declared in class javax.imageio.

IIOParam

controller

,

defaultController

,

destinationOffset

,

destinationType

,

sourceBands

,

sourceRegion

,

sourceXSubsampling

,

sourceYSubsampling

,

subsamplingXOffset

,

subsamplingYOffset

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

TIFFImageReadParam

()

Constructs a

TIFFImageReadParam

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

addAllowedTagSet

​(

TIFFTagSet

tagSet)

Adds a

TIFFTagSet

object to the list of allowed
tag sets.

List

<

TIFFTagSet

>

getAllowedTagSets

()

Returns a

List

containing the allowed

TIFFTagSet

objects.

boolean

getReadUnknownTags

()

Retrieve the setting of whether to read fields corresponding to unknown

TIFFTag

s.

void

removeAllowedTagSet

​(

TIFFTagSet

tagSet)

Removes a

TIFFTagSet

object from the list of
allowed tag sets.

void

setReadUnknownTags

​(boolean readUnknownTags)

Set whether to read fields corresponding to

TIFFTag

s not in
the allowed

TIFFTagSet

s.

- Methods declared in class javax.imageio.

ImageReadParam

canSetSourceRenderSize

,

getDestination

,

getDestinationBands

,

getSourceMaxProgressivePass

,

getSourceMinProgressivePass

,

getSourceNumProgressivePasses

,

getSourceRenderSize

,

setDestination

,

setDestinationBands

,

setSourceProgressivePasses

,

setSourceRenderSize

- Methods declared in class javax.imageio.

IIOParam

activateController

,

getController

,

getDefaultController

,

getDestinationOffset

,

getDestinationType

,

getSourceBands

,

getSourceRegion

,

getSourceXSubsampling

,

getSourceYSubsampling

,

getSubsamplingXOffset

,

getSubsamplingYOffset

,

hasController

,

setController

,

setDestinationOffset

,

setDestinationType

,

setSourceBands

,

setSourceRegion

,

setSourceSubsampling

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

- Fields declared in class javax.imageio.

ImageReadParam

canSetSourceRenderSize

,

destination

,

destinationBands

,

minProgressivePass

,

numProgressivePasses

,

sourceRenderSize

- Fields declared in class javax.imageio.

IIOParam

controller

,

defaultController

,

destinationOffset

,

destinationType

,

sourceBands

,

sourceRegion

,

sourceXSubsampling

,

sourceYSubsampling

,

subsamplingXOffset

,

subsamplingYOffset

---

#### Field Summary

Fields declared in class javax.imageio.

ImageReadParam

canSetSourceRenderSize

,

destination

,

destinationBands

,

minProgressivePass

,

numProgressivePasses

,

sourceRenderSize

---

#### Fields declared in class javax.imageio. ImageReadParam

Fields declared in class javax.imageio.

IIOParam

controller

,

defaultController

,

destinationOffset

,

destinationType

,

sourceBands

,

sourceRegion

,

sourceXSubsampling

,

sourceYSubsampling

,

subsamplingXOffset

,

subsamplingYOffset

---

#### Fields declared in class javax.imageio. IIOParam

Constructor Summary

Constructors

Constructor

Description

TIFFImageReadParam

()

Constructs a

TIFFImageReadParam

.

---

#### Constructor Summary

Constructs a

TIFFImageReadParam

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addAllowedTagSet

​(

TIFFTagSet

tagSet)

Adds a

TIFFTagSet

object to the list of allowed
tag sets.

List

<

TIFFTagSet

>

getAllowedTagSets

()

Returns a

List

containing the allowed

TIFFTagSet

objects.

boolean

getReadUnknownTags

()

Retrieve the setting of whether to read fields corresponding to unknown

TIFFTag

s.

void

removeAllowedTagSet

​(

TIFFTagSet

tagSet)

Removes a

TIFFTagSet

object from the list of
allowed tag sets.

void

setReadUnknownTags

​(boolean readUnknownTags)

Set whether to read fields corresponding to

TIFFTag

s not in
the allowed

TIFFTagSet

s.

- Methods declared in class javax.imageio.

ImageReadParam

canSetSourceRenderSize

,

getDestination

,

getDestinationBands

,

getSourceMaxProgressivePass

,

getSourceMinProgressivePass

,

getSourceNumProgressivePasses

,

getSourceRenderSize

,

setDestination

,

setDestinationBands

,

setSourceProgressivePasses

,

setSourceRenderSize

- Methods declared in class javax.imageio.

IIOParam

activateController

,

getController

,

getDefaultController

,

getDestinationOffset

,

getDestinationType

,

getSourceBands

,

getSourceRegion

,

getSourceXSubsampling

,

getSourceYSubsampling

,

getSubsamplingXOffset

,

getSubsamplingYOffset

,

hasController

,

setController

,

setDestinationOffset

,

setDestinationType

,

setSourceBands

,

setSourceRegion

,

setSourceSubsampling

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

Adds a

TIFFTagSet

object to the list of allowed
tag sets.

Returns a

List

containing the allowed

TIFFTagSet

objects.

Retrieve the setting of whether to read fields corresponding to unknown

TIFFTag

s.

Removes a

TIFFTagSet

object from the list of
allowed tag sets.

Set whether to read fields corresponding to

TIFFTag

s not in
the allowed

TIFFTagSet

s.

Methods declared in class javax.imageio.

ImageReadParam

canSetSourceRenderSize

,

getDestination

,

getDestinationBands

,

getSourceMaxProgressivePass

,

getSourceMinProgressivePass

,

getSourceNumProgressivePasses

,

getSourceRenderSize

,

setDestination

,

setDestinationBands

,

setSourceProgressivePasses

,

setSourceRenderSize

---

#### Methods declared in class javax.imageio. ImageReadParam

Methods declared in class javax.imageio.

IIOParam

activateController

,

getController

,

getDefaultController

,

getDestinationOffset

,

getDestinationType

,

getSourceBands

,

getSourceRegion

,

getSourceXSubsampling

,

getSourceYSubsampling

,

getSubsamplingXOffset

,

getSubsamplingYOffset

,

hasController

,

setController

,

setDestinationOffset

,

setDestinationType

,

setSourceBands

,

setSourceRegion

,

setSourceSubsampling

---

#### Methods declared in class javax.imageio. IIOParam

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- TIFFImageReadParam

```java
public TIFFImageReadParam()
```

Constructs a

TIFFImageReadParam

. Tags defined by
the

TIFFTagSet

s

BaselineTIFFTagSet

,

FaxTIFFTagSet

,

ExifParentTIFFTagSet

, and

GeoTIFFTagSet

will be supported.

**See Also:** BaselineTIFFTagSet

,

FaxTIFFTagSet

,

ExifParentTIFFTagSet

,

GeoTIFFTagSet

============ METHOD DETAIL ==========

- Method Detail

- addAllowedTagSet

```java
public void addAllowedTagSet​(
TIFFTagSet
tagSet)
```

Adds a

TIFFTagSet

object to the list of allowed
tag sets. Attempting to add a duplicate object to the list
has no effect.

**Parameters:** tagSet

- a

TIFFTagSet

.
**Throws:** IllegalArgumentException

- if

tagSet

is

null

.

- removeAllowedTagSet

```java
public void removeAllowedTagSet​(
TIFFTagSet
tagSet)
```

Removes a

TIFFTagSet

object from the list of
allowed tag sets. Removal is based on the

equals

method of the

TIFFTagSet

, which is normally
defined as reference equality.

**Parameters:** tagSet

- a

TIFFTagSet

.
**Throws:** IllegalArgumentException

- if

tagSet

is

null

.

- getAllowedTagSets

```java
public
List
<
TIFFTagSet
> getAllowedTagSets()
```

Returns a

List

containing the allowed

TIFFTagSet

objects.

**Returns:** a

List

of

TIFFTagSet

s.

- setReadUnknownTags

```java
public void setReadUnknownTags​(boolean readUnknownTags)
```

Set whether to read fields corresponding to

TIFFTag

s not in
the allowed

TIFFTagSet

s. The default setting is

false

.
If the TIFF

ImageReader

is ignoring metadata, then a setting
of

true

is overridden as all metadata are ignored except those
essential to reading the image itself.

**Parameters:** readUnknownTags

- Whether to read fields of unrecognized tags

- getReadUnknownTags

```java
public boolean getReadUnknownTags()
```

Retrieve the setting of whether to read fields corresponding to unknown

TIFFTag

s.

**Returns:** Whether to read fields of unrecognized tags

Constructor Detail

- TIFFImageReadParam

```java
public TIFFImageReadParam()
```

Constructs a

TIFFImageReadParam

. Tags defined by
the

TIFFTagSet

s

BaselineTIFFTagSet

,

FaxTIFFTagSet

,

ExifParentTIFFTagSet

, and

GeoTIFFTagSet

will be supported.

**See Also:** BaselineTIFFTagSet

,

FaxTIFFTagSet

,

ExifParentTIFFTagSet

,

GeoTIFFTagSet

---

#### Constructor Detail

TIFFImageReadParam

```java
public TIFFImageReadParam()
```

Constructs a

TIFFImageReadParam

. Tags defined by
the

TIFFTagSet

s

BaselineTIFFTagSet

,

FaxTIFFTagSet

,

ExifParentTIFFTagSet

, and

GeoTIFFTagSet

will be supported.

**See Also:** BaselineTIFFTagSet

,

FaxTIFFTagSet

,

ExifParentTIFFTagSet

,

GeoTIFFTagSet

---

#### TIFFImageReadParam

public TIFFImageReadParam()

Constructs a

TIFFImageReadParam

. Tags defined by
the

TIFFTagSet

s

BaselineTIFFTagSet

,

FaxTIFFTagSet

,

ExifParentTIFFTagSet

, and

GeoTIFFTagSet

will be supported.

Method Detail

- addAllowedTagSet

```java
public void addAllowedTagSet​(
TIFFTagSet
tagSet)
```

Adds a

TIFFTagSet

object to the list of allowed
tag sets. Attempting to add a duplicate object to the list
has no effect.

**Parameters:** tagSet

- a

TIFFTagSet

.
**Throws:** IllegalArgumentException

- if

tagSet

is

null

.

- removeAllowedTagSet

```java
public void removeAllowedTagSet​(
TIFFTagSet
tagSet)
```

Removes a

TIFFTagSet

object from the list of
allowed tag sets. Removal is based on the

equals

method of the

TIFFTagSet

, which is normally
defined as reference equality.

**Parameters:** tagSet

- a

TIFFTagSet

.
**Throws:** IllegalArgumentException

- if

tagSet

is

null

.

- getAllowedTagSets

```java
public
List
<
TIFFTagSet
> getAllowedTagSets()
```

Returns a

List

containing the allowed

TIFFTagSet

objects.

**Returns:** a

List

of

TIFFTagSet

s.

- setReadUnknownTags

```java
public void setReadUnknownTags​(boolean readUnknownTags)
```

Set whether to read fields corresponding to

TIFFTag

s not in
the allowed

TIFFTagSet

s. The default setting is

false

.
If the TIFF

ImageReader

is ignoring metadata, then a setting
of

true

is overridden as all metadata are ignored except those
essential to reading the image itself.

**Parameters:** readUnknownTags

- Whether to read fields of unrecognized tags

- getReadUnknownTags

```java
public boolean getReadUnknownTags()
```

Retrieve the setting of whether to read fields corresponding to unknown

TIFFTag

s.

**Returns:** Whether to read fields of unrecognized tags

---

#### Method Detail

addAllowedTagSet

```java
public void addAllowedTagSet​(
TIFFTagSet
tagSet)
```

Adds a

TIFFTagSet

object to the list of allowed
tag sets. Attempting to add a duplicate object to the list
has no effect.

**Parameters:** tagSet

- a

TIFFTagSet

.
**Throws:** IllegalArgumentException

- if

tagSet

is

null

.

---

#### addAllowedTagSet

public void addAllowedTagSet​(

TIFFTagSet

tagSet)

Adds a

TIFFTagSet

object to the list of allowed
tag sets. Attempting to add a duplicate object to the list
has no effect.

removeAllowedTagSet

```java
public void removeAllowedTagSet​(
TIFFTagSet
tagSet)
```

Removes a

TIFFTagSet

object from the list of
allowed tag sets. Removal is based on the

equals

method of the

TIFFTagSet

, which is normally
defined as reference equality.

**Parameters:** tagSet

- a

TIFFTagSet

.
**Throws:** IllegalArgumentException

- if

tagSet

is

null

.

---

#### removeAllowedTagSet

public void removeAllowedTagSet​(

TIFFTagSet

tagSet)

Removes a

TIFFTagSet

object from the list of
allowed tag sets. Removal is based on the

equals

method of the

TIFFTagSet

, which is normally
defined as reference equality.

getAllowedTagSets

```java
public
List
<
TIFFTagSet
> getAllowedTagSets()
```

Returns a

List

containing the allowed

TIFFTagSet

objects.

**Returns:** a

List

of

TIFFTagSet

s.

---

#### getAllowedTagSets

public

List

<

TIFFTagSet

> getAllowedTagSets()

Returns a

List

containing the allowed

TIFFTagSet

objects.

setReadUnknownTags

```java
public void setReadUnknownTags​(boolean readUnknownTags)
```

Set whether to read fields corresponding to

TIFFTag

s not in
the allowed

TIFFTagSet

s. The default setting is

false

.
If the TIFF

ImageReader

is ignoring metadata, then a setting
of

true

is overridden as all metadata are ignored except those
essential to reading the image itself.

**Parameters:** readUnknownTags

- Whether to read fields of unrecognized tags

---

#### setReadUnknownTags

public void setReadUnknownTags​(boolean readUnknownTags)

Set whether to read fields corresponding to

TIFFTag

s not in
the allowed

TIFFTagSet

s. The default setting is

false

.
If the TIFF

ImageReader

is ignoring metadata, then a setting
of

true

is overridden as all metadata are ignored except those
essential to reading the image itself.

getReadUnknownTags

```java
public boolean getReadUnknownTags()
```

Retrieve the setting of whether to read fields corresponding to unknown

TIFFTag

s.

**Returns:** Whether to read fields of unrecognized tags

---

#### getReadUnknownTags

public boolean getReadUnknownTags()

Retrieve the setting of whether to read fields corresponding to unknown

TIFFTag

s.

---

