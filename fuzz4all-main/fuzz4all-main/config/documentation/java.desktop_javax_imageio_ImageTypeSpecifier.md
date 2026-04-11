# Class ImageTypeSpecifier

**Source:** `java.desktop\javax\imageio\ImageTypeSpecifier.html`

### Class Description

```java
public class
ImageTypeSpecifier

extends
Object
```

A class that allows the format of an image (in particular, its

SampleModel

and

ColorModel

) to be
specified in a convenient manner.

---

### Field Details

#### protected
ColorModel
colorModel

The

ColorModel

to be used as a prototype.

---

#### protected
SampleModel
sampleModel

A

SampleModel

to be used as a prototype.

---

### Constructor Details

#### public ImageTypeSpecifier​(
ColorModel
colorModel,

SampleModel
sampleModel)

Constructs an

ImageTypeSpecifier

directly
from a

ColorModel

and a

SampleModel

.
It is the caller's responsibility to supply compatible
parameters.

**Parameters:**
- colorModel

- a

ColorModel

.
- sampleModel

- a

SampleModel

.

**Throws:**
- IllegalArgumentException

- if either parameter is

null

.
- IllegalArgumentException

- if

sampleModel

is not compatible with

colorModel

.

---

#### public ImageTypeSpecifier​(
RenderedImage
image)

Constructs an

ImageTypeSpecifier

from a

RenderedImage

. If a

BufferedImage

is
being used, one of the factory methods

createFromRenderedImage

or

createFromBufferedImageType

should be used instead in
order to get a more accurate result.

**Parameters:**
- image

- a

RenderedImage

.

**Throws:**
- IllegalArgumentException

- if the argument is

null

.

---

### Method Details

#### public static
ImageTypeSpecifier
createPacked​(
ColorSpace
colorSpace,
int redMask,
int greenMask,
int blueMask,
int alphaMask,
int transferType,
boolean isAlphaPremultiplied)

Returns a specifier for a packed image format that will use a

DirectColorModel

and a packed

SampleModel

to store each pixel packed into in a
single byte, short, or int.

**Parameters:**
- colorSpace

- the desired

ColorSpace

.
- redMask

- a contiguous mask indicated the position of the
red channel.
- greenMask

- a contiguous mask indicated the position of the
green channel.
- blueMask

- a contiguous mask indicated the position of the
blue channel.
- alphaMask

- a contiguous mask indicated the position of the
alpha channel.
- transferType

- the desired

SampleModel

transfer type.
- isAlphaPremultiplied

-

true

if the color channels
will be premultipled by the alpha channel.

**Returns:**
- an

ImageTypeSpecifier

with the desired
characteristics.

**Throws:**
- IllegalArgumentException

- if

colorSpace

is

null

.
- IllegalArgumentException

- if

colorSpace

is not of type

TYPE_RGB

.
- IllegalArgumentException

- if no mask has at least 1
bit set.
- IllegalArgumentException

- if

transferType

if not one of

DataBuffer.TYPE_BYTE

,

DataBuffer.TYPE_USHORT

, or

DataBuffer.TYPE_INT

.

---

#### public static
ImageTypeSpecifier
createInterleaved​(
ColorSpace
colorSpace,
int[] bandOffsets,
int dataType,
boolean hasAlpha,
boolean isAlphaPremultiplied)

Returns a specifier for an interleaved image format that will
use a

ComponentColorModel

and a

PixelInterleavedSampleModel

to store each pixel
component in a separate byte, short, or int.

**Parameters:**
- colorSpace

- the desired

ColorSpace

.
- bandOffsets

- an array of

int

s indicating the
offsets for each band.
- dataType

- the desired data type, as one of the enumerations
from the

DataBuffer

class.
- hasAlpha

-

true

if an alpha channel is desired.
- isAlphaPremultiplied

-

true

if the color channels
will be premultipled by the alpha channel.

**Returns:**
- an

ImageTypeSpecifier

with the desired
characteristics.

**Throws:**
- IllegalArgumentException

- if

colorSpace

is

null

.
- IllegalArgumentException

- if

bandOffsets

is

null

.
- IllegalArgumentException

- if

dataType

is
not one of the legal

DataBuffer.TYPE_*

constants.
- IllegalArgumentException

- if

bandOffsets.length

does not equal the number of
color space components, plus 1 if

hasAlpha

is

true

.

---

#### public static
ImageTypeSpecifier
createBanded​(
ColorSpace
colorSpace,
int[] bankIndices,
int[] bandOffsets,
int dataType,
boolean hasAlpha,
boolean isAlphaPremultiplied)

Returns a specifier for a banded image format that will use a

ComponentColorModel

and a

BandedSampleModel

to store each channel in a
separate array.

**Parameters:**
- colorSpace

- the desired

ColorSpace

.
- bankIndices

- an array of

int

s indicating the
bank in which each band will be stored.
- bandOffsets

- an array of

int

s indicating the
starting offset of each band within its bank.
- dataType

- the desired data type, as one of the enumerations
from the

DataBuffer

class.
- hasAlpha

-

true

if an alpha channel is desired.
- isAlphaPremultiplied

-

true

if the color channels
will be premultipled by the alpha channel.

**Returns:**
- an

ImageTypeSpecifier

with the desired
characteristics.

**Throws:**
- IllegalArgumentException

- if

colorSpace

is

null

.
- IllegalArgumentException

- if

bankIndices

is

null

.
- IllegalArgumentException

- if

bandOffsets

is

null

.
- IllegalArgumentException

- if the lengths of

bankIndices

and

bandOffsets

differ.
- IllegalArgumentException

- if

bandOffsets.length

does not equal the number of
color space components, plus 1 if

hasAlpha

is

true

.
- IllegalArgumentException

- if

dataType

is
not one of the legal

DataBuffer.TYPE_*

constants.

---

#### public static
ImageTypeSpecifier
createGrayscale​(int bits,
int dataType,
boolean isSigned)

Returns a specifier for a grayscale image format that will pack
pixels of the given bit depth into array elements of
the specified data type.

**Parameters:**
- bits

- the number of bits per gray value (1, 2, 4, 8, or 16).
- dataType

- the desired data type, as one of the enumerations
from the

DataBuffer

class.
- isSigned

-

true

if negative values are to
be represented.

**Returns:**
- an

ImageTypeSpecifier

with the desired
characteristics.

**Throws:**
- IllegalArgumentException

- if

bits

is
not one of 1, 2, 4, 8, or 16.
- IllegalArgumentException

- if

dataType

is
not one of

DataBuffer.TYPE_BYTE

,

DataBuffer.TYPE_SHORT

, or

DataBuffer.TYPE_USHORT

.
- IllegalArgumentException

- if

bits

is
larger than the bit size of the given

dataType

.

---

#### public static
ImageTypeSpecifier
createGrayscale​(int bits,
int dataType,
boolean isSigned,
boolean isAlphaPremultiplied)

Returns a specifier for a grayscale plus alpha image format
that will pack pixels of the given bit depth into array
elements of the specified data type.

**Parameters:**
- bits

- the number of bits per gray value (1, 2, 4, 8, or 16).
- dataType

- the desired data type, as one of the enumerations
from the

DataBuffer

class.
- isSigned

-

true

if negative values are to
be represented.
- isAlphaPremultiplied

-

true

if the luminance channel
will be premultipled by the alpha channel.

**Returns:**
- an

ImageTypeSpecifier

with the desired
characteristics.

**Throws:**
- IllegalArgumentException

- if

bits

is
not one of 1, 2, 4, 8, or 16.
- IllegalArgumentException

- if

dataType

is
not one of

DataBuffer.TYPE_BYTE

,

DataBuffer.TYPE_SHORT

, or

DataBuffer.TYPE_USHORT

.
- IllegalArgumentException

- if

bits

is
larger than the bit size of the given

dataType

.

---

#### public static
ImageTypeSpecifier
createIndexed​(byte[] redLUT,
byte[] greenLUT,
byte[] blueLUT,
byte[] alphaLUT,
int bits,
int dataType)

Returns a specifier for an indexed-color image format that will pack
index values of the given bit depth into array elements of
the specified data type.

**Parameters:**
- redLUT

- an array of

byte

s containing
the red values for each index.
- greenLUT

- an array of

byte

s containing * the
green values for each index.
- blueLUT

- an array of

byte

s containing the
blue values for each index.
- alphaLUT

- an array of

byte

s containing the
alpha values for each index, or

null

to create a
fully opaque LUT.
- bits

- the number of bits in each index.
- dataType

- the desired output type, as one of the enumerations
from the

DataBuffer

class.

**Returns:**
- an

ImageTypeSpecifier

with the desired
characteristics.

**Throws:**
- IllegalArgumentException

- if

redLUT

is

null

.
- IllegalArgumentException

- if

greenLUT

is

null

.
- IllegalArgumentException

- if

blueLUT

is

null

.
- IllegalArgumentException

- if

bits

is
not one of 1, 2, 4, 8, or 16.
- IllegalArgumentException

- if the
non-

null

LUT parameters do not have lengths of
exactly

1 << bits

.
- IllegalArgumentException

- if

dataType

is
not one of

DataBuffer.TYPE_BYTE

,

DataBuffer.TYPE_SHORT

,

DataBuffer.TYPE_USHORT

,
or

DataBuffer.TYPE_INT

.
- IllegalArgumentException

- if

bits

is
larger than the bit size of the given

dataType

.

---

#### public static
ImageTypeSpecifier
createFromBufferedImageType​(int bufferedImageType)

Returns an

ImageTypeSpecifier

that encodes
one of the standard

BufferedImage

types
(other than

TYPE_CUSTOM

).

**Parameters:**
- bufferedImageType

- an int representing one of the standard

BufferedImage

types.

**Returns:**
- an

ImageTypeSpecifier

with the desired
characteristics.

**Throws:**
- IllegalArgumentException

- if

bufferedImageType

is not one of the standard
types, or is equal to

TYPE_CUSTOM

.

**See Also:**
- BufferedImage

,

BufferedImage.TYPE_INT_RGB

,

BufferedImage.TYPE_INT_ARGB

,

BufferedImage.TYPE_INT_ARGB_PRE

,

BufferedImage.TYPE_INT_BGR

,

BufferedImage.TYPE_3BYTE_BGR

,

BufferedImage.TYPE_4BYTE_ABGR

,

BufferedImage.TYPE_4BYTE_ABGR_PRE

,

BufferedImage.TYPE_USHORT_565_RGB

,

BufferedImage.TYPE_USHORT_555_RGB

,

BufferedImage.TYPE_BYTE_GRAY

,

BufferedImage.TYPE_USHORT_GRAY

,

BufferedImage.TYPE_BYTE_BINARY

,

BufferedImage.TYPE_BYTE_INDEXED

---

#### public static
ImageTypeSpecifier
createFromRenderedImage​(
RenderedImage
image)

Returns an

ImageTypeSpecifier

that encodes the
layout of a

RenderedImage

(which may be a

BufferedImage

).

**Parameters:**
- image

- a

RenderedImage

.

**Returns:**
- an

ImageTypeSpecifier

with the desired
characteristics.

**Throws:**
- IllegalArgumentException

- if

image

is

null

.

---

#### public int getBufferedImageType()

Returns an int containing one of the enumerated constant values
describing image formats from

BufferedImage

.

**Returns:**
- an

int

representing a

BufferedImage

type.

**See Also:**
- BufferedImage

,

BufferedImage.TYPE_CUSTOM

,

BufferedImage.TYPE_INT_RGB

,

BufferedImage.TYPE_INT_ARGB

,

BufferedImage.TYPE_INT_ARGB_PRE

,

BufferedImage.TYPE_INT_BGR

,

BufferedImage.TYPE_3BYTE_BGR

,

BufferedImage.TYPE_4BYTE_ABGR

,

BufferedImage.TYPE_4BYTE_ABGR_PRE

,

BufferedImage.TYPE_USHORT_565_RGB

,

BufferedImage.TYPE_USHORT_555_RGB

,

BufferedImage.TYPE_BYTE_GRAY

,

BufferedImage.TYPE_USHORT_GRAY

,

BufferedImage.TYPE_BYTE_BINARY

,

BufferedImage.TYPE_BYTE_INDEXED

---

#### public int getNumComponents()

Return the number of color components
specified by this object. This is the same value as returned by

ColorModel.getNumComponents

**Returns:**
- the number of components in the image.

---

#### public int getNumBands()

Return the number of bands
specified by this object. This is the same value as returned by

SampleModel.getNumBands

**Returns:**
- the number of bands in the image.

---

#### public int getBitsPerBand​(int band)

Return the number of bits used to represent samples of the given band.

**Parameters:**
- band

- the index of the band to be queried, as an
int.

**Returns:**
- an int specifying a number of bits.

**Throws:**
- IllegalArgumentException

- if

band

is
negative or greater than the largest band index.

---

#### public
SampleModel
getSampleModel()

Returns a

SampleModel

based on the settings
encapsulated within this object. The width and height of the

SampleModel

will be set to arbitrary values.

**Returns:**
- a

SampleModel

with arbitrary dimensions.

---

#### public
SampleModel
getSampleModel​(int width,
int height)

Returns a

SampleModel

based on the settings
encapsulated within this object. The width and height of the

SampleModel

will be set to the supplied values.

**Parameters:**
- width

- the desired width of the returned

SampleModel

.
- height

- the desired height of the returned

SampleModel

.

**Returns:**
- a

SampleModel

with the given dimensions.

**Throws:**
- IllegalArgumentException

- if either

width

or

height

are negative or zero.
- IllegalArgumentException

- if the product of

width

and

height

is greater than

Integer.MAX_VALUE

---

#### public
ColorModel
getColorModel()

Returns the

ColorModel

specified by this object.

**Returns:**
- a

ColorModel

.

---

#### public
BufferedImage
createBufferedImage​(int width,
int height)

Creates a

BufferedImage

with a given width and
height according to the specification embodied in this object.

**Parameters:**
- width

- the desired width of the returned

BufferedImage

.
- height

- the desired height of the returned

BufferedImage

.

**Returns:**
- a new

BufferedImage

**Throws:**
- IllegalArgumentException

- if either

width

or

height

are negative or zero.
- IllegalArgumentException

- if the product of

width

and

height

is greater than

Integer.MAX_VALUE

, or if the number of array
elements needed to store the image is greater than

Integer.MAX_VALUE

.

---

#### public boolean equals​(
Object
o)

Returns

true

if the given

Object

is
an

ImageTypeSpecifier

and has a

SampleModel

and

ColorModel

that are
equal to those of this object.

**Overrides:**
- equals

in class

Object

**Parameters:**
- o

- the

Object

to be compared for equality.

**Returns:**
- true

if the given object is an equivalent

ImageTypeSpecifier

.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns the hash code for this ImageTypeSpecifier.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code for this ImageTypeSpecifier

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

### Additional Sections

#### Class ImageTypeSpecifier

java.lang.Object

- javax.imageio.ImageTypeSpecifier

javax.imageio.ImageTypeSpecifier

```java
public class
ImageTypeSpecifier

extends
Object
```

A class that allows the format of an image (in particular, its

SampleModel

and

ColorModel

) to be
specified in a convenient manner.

public class

ImageTypeSpecifier

extends

Object

A class that allows the format of an image (in particular, its

SampleModel

and

ColorModel

) to be
specified in a convenient manner.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

ColorModel

colorModel

The

ColorModel

to be used as a prototype.

protected

SampleModel

sampleModel

A

SampleModel

to be used as a prototype.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ImageTypeSpecifier

​(

ColorModel

colorModel,

SampleModel

sampleModel)

Constructs an

ImageTypeSpecifier

directly
from a

ColorModel

and a

SampleModel

.

ImageTypeSpecifier

​(

RenderedImage

image)

Constructs an

ImageTypeSpecifier

from a

RenderedImage

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

ImageTypeSpecifier

createBanded

​(

ColorSpace

colorSpace,
int[] bankIndices,
int[] bandOffsets,
int dataType,
boolean hasAlpha,
boolean isAlphaPremultiplied)

Returns a specifier for a banded image format that will use a

ComponentColorModel

and a

BandedSampleModel

to store each channel in a
separate array.

BufferedImage

createBufferedImage

​(int width,
int height)

Creates a

BufferedImage

with a given width and
height according to the specification embodied in this object.

static

ImageTypeSpecifier

createFromBufferedImageType

​(int bufferedImageType)

Returns an

ImageTypeSpecifier

that encodes
one of the standard

BufferedImage

types
(other than

TYPE_CUSTOM

).

static

ImageTypeSpecifier

createFromRenderedImage

​(

RenderedImage

image)

Returns an

ImageTypeSpecifier

that encodes the
layout of a

RenderedImage

(which may be a

BufferedImage

).

static

ImageTypeSpecifier

createGrayscale

​(int bits,
int dataType,
boolean isSigned)

Returns a specifier for a grayscale image format that will pack
pixels of the given bit depth into array elements of
the specified data type.

static

ImageTypeSpecifier

createGrayscale

​(int bits,
int dataType,
boolean isSigned,
boolean isAlphaPremultiplied)

Returns a specifier for a grayscale plus alpha image format
that will pack pixels of the given bit depth into array
elements of the specified data type.

static

ImageTypeSpecifier

createIndexed

​(byte[] redLUT,
byte[] greenLUT,
byte[] blueLUT,
byte[] alphaLUT,
int bits,
int dataType)

Returns a specifier for an indexed-color image format that will pack
index values of the given bit depth into array elements of
the specified data type.

static

ImageTypeSpecifier

createInterleaved

​(

ColorSpace

colorSpace,
int[] bandOffsets,
int dataType,
boolean hasAlpha,
boolean isAlphaPremultiplied)

Returns a specifier for an interleaved image format that will
use a

ComponentColorModel

and a

PixelInterleavedSampleModel

to store each pixel
component in a separate byte, short, or int.

static

ImageTypeSpecifier

createPacked

​(

ColorSpace

colorSpace,
int redMask,
int greenMask,
int blueMask,
int alphaMask,
int transferType,
boolean isAlphaPremultiplied)

Returns a specifier for a packed image format that will use a

DirectColorModel

and a packed

SampleModel

to store each pixel packed into in a
single byte, short, or int.

boolean

equals

​(

Object

o)

Returns

true

if the given

Object

is
an

ImageTypeSpecifier

and has a

SampleModel

and

ColorModel

that are
equal to those of this object.

int

getBitsPerBand

​(int band)

Return the number of bits used to represent samples of the given band.

int

getBufferedImageType

()

Returns an int containing one of the enumerated constant values
describing image formats from

BufferedImage

.

ColorModel

getColorModel

()

Returns the

ColorModel

specified by this object.

int

getNumBands

()

Return the number of bands
specified by this object.

int

getNumComponents

()

Return the number of color components
specified by this object.

SampleModel

getSampleModel

()

Returns a

SampleModel

based on the settings
encapsulated within this object.

SampleModel

getSampleModel

​(int width,
int height)

Returns a

SampleModel

based on the settings
encapsulated within this object.

int

hashCode

()

Returns the hash code for this ImageTypeSpecifier.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

protected

ColorModel

colorModel

The

ColorModel

to be used as a prototype.

protected

SampleModel

sampleModel

A

SampleModel

to be used as a prototype.

---

#### Field Summary

The

ColorModel

to be used as a prototype.

A

SampleModel

to be used as a prototype.

Constructor Summary

Constructors

Constructor

Description

ImageTypeSpecifier

​(

ColorModel

colorModel,

SampleModel

sampleModel)

Constructs an

ImageTypeSpecifier

directly
from a

ColorModel

and a

SampleModel

.

ImageTypeSpecifier

​(

RenderedImage

image)

Constructs an

ImageTypeSpecifier

from a

RenderedImage

.

---

#### Constructor Summary

Constructs an

ImageTypeSpecifier

directly
from a

ColorModel

and a

SampleModel

.

Constructs an

ImageTypeSpecifier

from a

RenderedImage

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

ImageTypeSpecifier

createBanded

​(

ColorSpace

colorSpace,
int[] bankIndices,
int[] bandOffsets,
int dataType,
boolean hasAlpha,
boolean isAlphaPremultiplied)

Returns a specifier for a banded image format that will use a

ComponentColorModel

and a

BandedSampleModel

to store each channel in a
separate array.

BufferedImage

createBufferedImage

​(int width,
int height)

Creates a

BufferedImage

with a given width and
height according to the specification embodied in this object.

static

ImageTypeSpecifier

createFromBufferedImageType

​(int bufferedImageType)

Returns an

ImageTypeSpecifier

that encodes
one of the standard

BufferedImage

types
(other than

TYPE_CUSTOM

).

static

ImageTypeSpecifier

createFromRenderedImage

​(

RenderedImage

image)

Returns an

ImageTypeSpecifier

that encodes the
layout of a

RenderedImage

(which may be a

BufferedImage

).

static

ImageTypeSpecifier

createGrayscale

​(int bits,
int dataType,
boolean isSigned)

Returns a specifier for a grayscale image format that will pack
pixels of the given bit depth into array elements of
the specified data type.

static

ImageTypeSpecifier

createGrayscale

​(int bits,
int dataType,
boolean isSigned,
boolean isAlphaPremultiplied)

Returns a specifier for a grayscale plus alpha image format
that will pack pixels of the given bit depth into array
elements of the specified data type.

static

ImageTypeSpecifier

createIndexed

​(byte[] redLUT,
byte[] greenLUT,
byte[] blueLUT,
byte[] alphaLUT,
int bits,
int dataType)

Returns a specifier for an indexed-color image format that will pack
index values of the given bit depth into array elements of
the specified data type.

static

ImageTypeSpecifier

createInterleaved

​(

ColorSpace

colorSpace,
int[] bandOffsets,
int dataType,
boolean hasAlpha,
boolean isAlphaPremultiplied)

Returns a specifier for an interleaved image format that will
use a

ComponentColorModel

and a

PixelInterleavedSampleModel

to store each pixel
component in a separate byte, short, or int.

static

ImageTypeSpecifier

createPacked

​(

ColorSpace

colorSpace,
int redMask,
int greenMask,
int blueMask,
int alphaMask,
int transferType,
boolean isAlphaPremultiplied)

Returns a specifier for a packed image format that will use a

DirectColorModel

and a packed

SampleModel

to store each pixel packed into in a
single byte, short, or int.

boolean

equals

​(

Object

o)

Returns

true

if the given

Object

is
an

ImageTypeSpecifier

and has a

SampleModel

and

ColorModel

that are
equal to those of this object.

int

getBitsPerBand

​(int band)

Return the number of bits used to represent samples of the given band.

int

getBufferedImageType

()

Returns an int containing one of the enumerated constant values
describing image formats from

BufferedImage

.

ColorModel

getColorModel

()

Returns the

ColorModel

specified by this object.

int

getNumBands

()

Return the number of bands
specified by this object.

int

getNumComponents

()

Return the number of color components
specified by this object.

SampleModel

getSampleModel

()

Returns a

SampleModel

based on the settings
encapsulated within this object.

SampleModel

getSampleModel

​(int width,
int height)

Returns a

SampleModel

based on the settings
encapsulated within this object.

int

hashCode

()

Returns the hash code for this ImageTypeSpecifier.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

Returns a specifier for a banded image format that will use a

ComponentColorModel

and a

BandedSampleModel

to store each channel in a
separate array.

Creates a

BufferedImage

with a given width and
height according to the specification embodied in this object.

Returns an

ImageTypeSpecifier

that encodes
one of the standard

BufferedImage

types
(other than

TYPE_CUSTOM

).

Returns an

ImageTypeSpecifier

that encodes the
layout of a

RenderedImage

(which may be a

BufferedImage

).

Returns a specifier for a grayscale image format that will pack
pixels of the given bit depth into array elements of
the specified data type.

Returns a specifier for a grayscale plus alpha image format
that will pack pixels of the given bit depth into array
elements of the specified data type.

Returns a specifier for an indexed-color image format that will pack
index values of the given bit depth into array elements of
the specified data type.

Returns a specifier for an interleaved image format that will
use a

ComponentColorModel

and a

PixelInterleavedSampleModel

to store each pixel
component in a separate byte, short, or int.

Returns a specifier for a packed image format that will use a

DirectColorModel

and a packed

SampleModel

to store each pixel packed into in a
single byte, short, or int.

Returns

true

if the given

Object

is
an

ImageTypeSpecifier

and has a

SampleModel

and

ColorModel

that are
equal to those of this object.

Return the number of bits used to represent samples of the given band.

Returns an int containing one of the enumerated constant values
describing image formats from

BufferedImage

.

Returns the

ColorModel

specified by this object.

Return the number of bands
specified by this object.

Return the number of color components
specified by this object.

Returns a

SampleModel

based on the settings
encapsulated within this object.

Returns the hash code for this ImageTypeSpecifier.

Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

- colorModel

```java
protected
ColorModel
colorModel
```

The

ColorModel

to be used as a prototype.

- sampleModel

```java
protected
SampleModel
sampleModel
```

A

SampleModel

to be used as a prototype.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ImageTypeSpecifier

```java
public ImageTypeSpecifier​(
ColorModel
colorModel,

SampleModel
sampleModel)
```

Constructs an

ImageTypeSpecifier

directly
from a

ColorModel

and a

SampleModel

.
It is the caller's responsibility to supply compatible
parameters.

**Parameters:** colorModel

- a

ColorModel

.
**Parameters:** sampleModel

- a

SampleModel

.
**Throws:** IllegalArgumentException

- if either parameter is

null

.
**Throws:** IllegalArgumentException

- if

sampleModel

is not compatible with

colorModel

.

- ImageTypeSpecifier

```java
public ImageTypeSpecifier​(
RenderedImage
image)
```

Constructs an

ImageTypeSpecifier

from a

RenderedImage

. If a

BufferedImage

is
being used, one of the factory methods

createFromRenderedImage

or

createFromBufferedImageType

should be used instead in
order to get a more accurate result.

**Parameters:** image

- a

RenderedImage

.
**Throws:** IllegalArgumentException

- if the argument is

null

.

============ METHOD DETAIL ==========

- Method Detail

- createPacked

```java
public static
ImageTypeSpecifier
createPacked​(
ColorSpace
colorSpace,
int redMask,
int greenMask,
int blueMask,
int alphaMask,
int transferType,
boolean isAlphaPremultiplied)
```

Returns a specifier for a packed image format that will use a

DirectColorModel

and a packed

SampleModel

to store each pixel packed into in a
single byte, short, or int.

**Parameters:** colorSpace

- the desired

ColorSpace

.
**Parameters:** redMask

- a contiguous mask indicated the position of the
red channel.
**Parameters:** greenMask

- a contiguous mask indicated the position of the
green channel.
**Parameters:** blueMask

- a contiguous mask indicated the position of the
blue channel.
**Parameters:** alphaMask

- a contiguous mask indicated the position of the
alpha channel.
**Parameters:** transferType

- the desired

SampleModel

transfer type.
**Parameters:** isAlphaPremultiplied

-

true

if the color channels
will be premultipled by the alpha channel.
**Returns:** an

ImageTypeSpecifier

with the desired
characteristics.
**Throws:** IllegalArgumentException

- if

colorSpace

is

null

.
**Throws:** IllegalArgumentException

- if

colorSpace

is not of type

TYPE_RGB

.
**Throws:** IllegalArgumentException

- if no mask has at least 1
bit set.
**Throws:** IllegalArgumentException

- if

transferType

if not one of

DataBuffer.TYPE_BYTE

,

DataBuffer.TYPE_USHORT

, or

DataBuffer.TYPE_INT

.

- createInterleaved

```java
public static
ImageTypeSpecifier
createInterleaved​(
ColorSpace
colorSpace,
int[] bandOffsets,
int dataType,
boolean hasAlpha,
boolean isAlphaPremultiplied)
```

Returns a specifier for an interleaved image format that will
use a

ComponentColorModel

and a

PixelInterleavedSampleModel

to store each pixel
component in a separate byte, short, or int.

**Parameters:** colorSpace

- the desired

ColorSpace

.
**Parameters:** bandOffsets

- an array of

int

s indicating the
offsets for each band.
**Parameters:** dataType

- the desired data type, as one of the enumerations
from the

DataBuffer

class.
**Parameters:** hasAlpha

-

true

if an alpha channel is desired.
**Parameters:** isAlphaPremultiplied

-

true

if the color channels
will be premultipled by the alpha channel.
**Returns:** an

ImageTypeSpecifier

with the desired
characteristics.
**Throws:** IllegalArgumentException

- if

colorSpace

is

null

.
**Throws:** IllegalArgumentException

- if

bandOffsets

is

null

.
**Throws:** IllegalArgumentException

- if

dataType

is
not one of the legal

DataBuffer.TYPE_*

constants.
**Throws:** IllegalArgumentException

- if

bandOffsets.length

does not equal the number of
color space components, plus 1 if

hasAlpha

is

true

.

- createBanded

```java
public static
ImageTypeSpecifier
createBanded​(
ColorSpace
colorSpace,
int[] bankIndices,
int[] bandOffsets,
int dataType,
boolean hasAlpha,
boolean isAlphaPremultiplied)
```

Returns a specifier for a banded image format that will use a

ComponentColorModel

and a

BandedSampleModel

to store each channel in a
separate array.

**Parameters:** colorSpace

- the desired

ColorSpace

.
**Parameters:** bankIndices

- an array of

int

s indicating the
bank in which each band will be stored.
**Parameters:** bandOffsets

- an array of

int

s indicating the
starting offset of each band within its bank.
**Parameters:** dataType

- the desired data type, as one of the enumerations
from the

DataBuffer

class.
**Parameters:** hasAlpha

-

true

if an alpha channel is desired.
**Parameters:** isAlphaPremultiplied

-

true

if the color channels
will be premultipled by the alpha channel.
**Returns:** an

ImageTypeSpecifier

with the desired
characteristics.
**Throws:** IllegalArgumentException

- if

colorSpace

is

null

.
**Throws:** IllegalArgumentException

- if

bankIndices

is

null

.
**Throws:** IllegalArgumentException

- if

bandOffsets

is

null

.
**Throws:** IllegalArgumentException

- if the lengths of

bankIndices

and

bandOffsets

differ.
**Throws:** IllegalArgumentException

- if

bandOffsets.length

does not equal the number of
color space components, plus 1 if

hasAlpha

is

true

.
**Throws:** IllegalArgumentException

- if

dataType

is
not one of the legal

DataBuffer.TYPE_*

constants.

- createGrayscale

```java
public static
ImageTypeSpecifier
createGrayscale​(int bits,
int dataType,
boolean isSigned)
```

Returns a specifier for a grayscale image format that will pack
pixels of the given bit depth into array elements of
the specified data type.

**Parameters:** bits

- the number of bits per gray value (1, 2, 4, 8, or 16).
**Parameters:** dataType

- the desired data type, as one of the enumerations
from the

DataBuffer

class.
**Parameters:** isSigned

-

true

if negative values are to
be represented.
**Returns:** an

ImageTypeSpecifier

with the desired
characteristics.
**Throws:** IllegalArgumentException

- if

bits

is
not one of 1, 2, 4, 8, or 16.
**Throws:** IllegalArgumentException

- if

dataType

is
not one of

DataBuffer.TYPE_BYTE

,

DataBuffer.TYPE_SHORT

, or

DataBuffer.TYPE_USHORT

.
**Throws:** IllegalArgumentException

- if

bits

is
larger than the bit size of the given

dataType

.

- createGrayscale

```java
public static
ImageTypeSpecifier
createGrayscale​(int bits,
int dataType,
boolean isSigned,
boolean isAlphaPremultiplied)
```

Returns a specifier for a grayscale plus alpha image format
that will pack pixels of the given bit depth into array
elements of the specified data type.

**Parameters:** bits

- the number of bits per gray value (1, 2, 4, 8, or 16).
**Parameters:** dataType

- the desired data type, as one of the enumerations
from the

DataBuffer

class.
**Parameters:** isSigned

-

true

if negative values are to
be represented.
**Parameters:** isAlphaPremultiplied

-

true

if the luminance channel
will be premultipled by the alpha channel.
**Returns:** an

ImageTypeSpecifier

with the desired
characteristics.
**Throws:** IllegalArgumentException

- if

bits

is
not one of 1, 2, 4, 8, or 16.
**Throws:** IllegalArgumentException

- if

dataType

is
not one of

DataBuffer.TYPE_BYTE

,

DataBuffer.TYPE_SHORT

, or

DataBuffer.TYPE_USHORT

.
**Throws:** IllegalArgumentException

- if

bits

is
larger than the bit size of the given

dataType

.

- createIndexed

```java
public static
ImageTypeSpecifier
createIndexed​(byte[] redLUT,
byte[] greenLUT,
byte[] blueLUT,
byte[] alphaLUT,
int bits,
int dataType)
```

Returns a specifier for an indexed-color image format that will pack
index values of the given bit depth into array elements of
the specified data type.

**Parameters:** redLUT

- an array of

byte

s containing
the red values for each index.
**Parameters:** greenLUT

- an array of

byte

s containing * the
green values for each index.
**Parameters:** blueLUT

- an array of

byte

s containing the
blue values for each index.
**Parameters:** alphaLUT

- an array of

byte

s containing the
alpha values for each index, or

null

to create a
fully opaque LUT.
**Parameters:** bits

- the number of bits in each index.
**Parameters:** dataType

- the desired output type, as one of the enumerations
from the

DataBuffer

class.
**Returns:** an

ImageTypeSpecifier

with the desired
characteristics.
**Throws:** IllegalArgumentException

- if

redLUT

is

null

.
**Throws:** IllegalArgumentException

- if

greenLUT

is

null

.
**Throws:** IllegalArgumentException

- if

blueLUT

is

null

.
**Throws:** IllegalArgumentException

- if

bits

is
not one of 1, 2, 4, 8, or 16.
**Throws:** IllegalArgumentException

- if the
non-

null

LUT parameters do not have lengths of
exactly

1 << bits

.
**Throws:** IllegalArgumentException

- if

dataType

is
not one of

DataBuffer.TYPE_BYTE

,

DataBuffer.TYPE_SHORT

,

DataBuffer.TYPE_USHORT

,
or

DataBuffer.TYPE_INT

.
**Throws:** IllegalArgumentException

- if

bits

is
larger than the bit size of the given

dataType

.

- createFromBufferedImageType

```java
public static
ImageTypeSpecifier
createFromBufferedImageType​(int bufferedImageType)
```

Returns an

ImageTypeSpecifier

that encodes
one of the standard

BufferedImage

types
(other than

TYPE_CUSTOM

).

**Parameters:** bufferedImageType

- an int representing one of the standard

BufferedImage

types.
**Returns:** an

ImageTypeSpecifier

with the desired
characteristics.
**Throws:** IllegalArgumentException

- if

bufferedImageType

is not one of the standard
types, or is equal to

TYPE_CUSTOM

.
**See Also:** BufferedImage

,

BufferedImage.TYPE_INT_RGB

,

BufferedImage.TYPE_INT_ARGB

,

BufferedImage.TYPE_INT_ARGB_PRE

,

BufferedImage.TYPE_INT_BGR

,

BufferedImage.TYPE_3BYTE_BGR

,

BufferedImage.TYPE_4BYTE_ABGR

,

BufferedImage.TYPE_4BYTE_ABGR_PRE

,

BufferedImage.TYPE_USHORT_565_RGB

,

BufferedImage.TYPE_USHORT_555_RGB

,

BufferedImage.TYPE_BYTE_GRAY

,

BufferedImage.TYPE_USHORT_GRAY

,

BufferedImage.TYPE_BYTE_BINARY

,

BufferedImage.TYPE_BYTE_INDEXED

- createFromRenderedImage

```java
public static
ImageTypeSpecifier
createFromRenderedImage​(
RenderedImage
image)
```

Returns an

ImageTypeSpecifier

that encodes the
layout of a

RenderedImage

(which may be a

BufferedImage

).

**Parameters:** image

- a

RenderedImage

.
**Returns:** an

ImageTypeSpecifier

with the desired
characteristics.
**Throws:** IllegalArgumentException

- if

image

is

null

.

- getBufferedImageType

```java
public int getBufferedImageType()
```

Returns an int containing one of the enumerated constant values
describing image formats from

BufferedImage

.

**Returns:** an

int

representing a

BufferedImage

type.
**See Also:** BufferedImage

,

BufferedImage.TYPE_CUSTOM

,

BufferedImage.TYPE_INT_RGB

,

BufferedImage.TYPE_INT_ARGB

,

BufferedImage.TYPE_INT_ARGB_PRE

,

BufferedImage.TYPE_INT_BGR

,

BufferedImage.TYPE_3BYTE_BGR

,

BufferedImage.TYPE_4BYTE_ABGR

,

BufferedImage.TYPE_4BYTE_ABGR_PRE

,

BufferedImage.TYPE_USHORT_565_RGB

,

BufferedImage.TYPE_USHORT_555_RGB

,

BufferedImage.TYPE_BYTE_GRAY

,

BufferedImage.TYPE_USHORT_GRAY

,

BufferedImage.TYPE_BYTE_BINARY

,

BufferedImage.TYPE_BYTE_INDEXED

- getNumComponents

```java
public int getNumComponents()
```

Return the number of color components
specified by this object. This is the same value as returned by

ColorModel.getNumComponents

**Returns:** the number of components in the image.

- getNumBands

```java
public int getNumBands()
```

Return the number of bands
specified by this object. This is the same value as returned by

SampleModel.getNumBands

**Returns:** the number of bands in the image.

- getBitsPerBand

```java
public int getBitsPerBand​(int band)
```

Return the number of bits used to represent samples of the given band.

**Parameters:** band

- the index of the band to be queried, as an
int.
**Returns:** an int specifying a number of bits.
**Throws:** IllegalArgumentException

- if

band

is
negative or greater than the largest band index.

- getSampleModel

```java
public
SampleModel
getSampleModel()
```

Returns a

SampleModel

based on the settings
encapsulated within this object. The width and height of the

SampleModel

will be set to arbitrary values.

**Returns:** a

SampleModel

with arbitrary dimensions.

- getSampleModel

```java
public
SampleModel
getSampleModel​(int width,
int height)
```

Returns a

SampleModel

based on the settings
encapsulated within this object. The width and height of the

SampleModel

will be set to the supplied values.

**Parameters:** width

- the desired width of the returned

SampleModel

.
**Parameters:** height

- the desired height of the returned

SampleModel

.
**Returns:** a

SampleModel

with the given dimensions.
**Throws:** IllegalArgumentException

- if either

width

or

height

are negative or zero.
**Throws:** IllegalArgumentException

- if the product of

width

and

height

is greater than

Integer.MAX_VALUE

- getColorModel

```java
public
ColorModel
getColorModel()
```

Returns the

ColorModel

specified by this object.

**Returns:** a

ColorModel

.

- createBufferedImage

```java
public
BufferedImage
createBufferedImage​(int width,
int height)
```

Creates a

BufferedImage

with a given width and
height according to the specification embodied in this object.

**Parameters:** width

- the desired width of the returned

BufferedImage

.
**Parameters:** height

- the desired height of the returned

BufferedImage

.
**Returns:** a new

BufferedImage
**Throws:** IllegalArgumentException

- if either

width

or

height

are negative or zero.
**Throws:** IllegalArgumentException

- if the product of

width

and

height

is greater than

Integer.MAX_VALUE

, or if the number of array
elements needed to store the image is greater than

Integer.MAX_VALUE

.

- equals

```java
public boolean equals​(
Object
o)
```

Returns

true

if the given

Object

is
an

ImageTypeSpecifier

and has a

SampleModel

and

ColorModel

that are
equal to those of this object.

**Overrides:** equals

in class

Object
**Parameters:** o

- the

Object

to be compared for equality.
**Returns:** true

if the given object is an equivalent

ImageTypeSpecifier

.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code for this ImageTypeSpecifier.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this ImageTypeSpecifier
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

Field Detail

- colorModel

```java
protected
ColorModel
colorModel
```

The

ColorModel

to be used as a prototype.

- sampleModel

```java
protected
SampleModel
sampleModel
```

A

SampleModel

to be used as a prototype.

---

#### Field Detail

colorModel

```java
protected
ColorModel
colorModel
```

The

ColorModel

to be used as a prototype.

---

#### colorModel

protected

ColorModel

colorModel

The

ColorModel

to be used as a prototype.

sampleModel

```java
protected
SampleModel
sampleModel
```

A

SampleModel

to be used as a prototype.

---

#### sampleModel

protected

SampleModel

sampleModel

A

SampleModel

to be used as a prototype.

Constructor Detail

- ImageTypeSpecifier

```java
public ImageTypeSpecifier​(
ColorModel
colorModel,

SampleModel
sampleModel)
```

Constructs an

ImageTypeSpecifier

directly
from a

ColorModel

and a

SampleModel

.
It is the caller's responsibility to supply compatible
parameters.

**Parameters:** colorModel

- a

ColorModel

.
**Parameters:** sampleModel

- a

SampleModel

.
**Throws:** IllegalArgumentException

- if either parameter is

null

.
**Throws:** IllegalArgumentException

- if

sampleModel

is not compatible with

colorModel

.

- ImageTypeSpecifier

```java
public ImageTypeSpecifier​(
RenderedImage
image)
```

Constructs an

ImageTypeSpecifier

from a

RenderedImage

. If a

BufferedImage

is
being used, one of the factory methods

createFromRenderedImage

or

createFromBufferedImageType

should be used instead in
order to get a more accurate result.

**Parameters:** image

- a

RenderedImage

.
**Throws:** IllegalArgumentException

- if the argument is

null

.

---

#### Constructor Detail

ImageTypeSpecifier

```java
public ImageTypeSpecifier​(
ColorModel
colorModel,

SampleModel
sampleModel)
```

Constructs an

ImageTypeSpecifier

directly
from a

ColorModel

and a

SampleModel

.
It is the caller's responsibility to supply compatible
parameters.

**Parameters:** colorModel

- a

ColorModel

.
**Parameters:** sampleModel

- a

SampleModel

.
**Throws:** IllegalArgumentException

- if either parameter is

null

.
**Throws:** IllegalArgumentException

- if

sampleModel

is not compatible with

colorModel

.

---

#### ImageTypeSpecifier

public ImageTypeSpecifier​(

ColorModel

colorModel,

SampleModel

sampleModel)

Constructs an

ImageTypeSpecifier

directly
from a

ColorModel

and a

SampleModel

.
It is the caller's responsibility to supply compatible
parameters.

ImageTypeSpecifier

```java
public ImageTypeSpecifier​(
RenderedImage
image)
```

Constructs an

ImageTypeSpecifier

from a

RenderedImage

. If a

BufferedImage

is
being used, one of the factory methods

createFromRenderedImage

or

createFromBufferedImageType

should be used instead in
order to get a more accurate result.

**Parameters:** image

- a

RenderedImage

.
**Throws:** IllegalArgumentException

- if the argument is

null

.

---

#### ImageTypeSpecifier

public ImageTypeSpecifier​(

RenderedImage

image)

Constructs an

ImageTypeSpecifier

from a

RenderedImage

. If a

BufferedImage

is
being used, one of the factory methods

createFromRenderedImage

or

createFromBufferedImageType

should be used instead in
order to get a more accurate result.

Method Detail

- createPacked

```java
public static
ImageTypeSpecifier
createPacked​(
ColorSpace
colorSpace,
int redMask,
int greenMask,
int blueMask,
int alphaMask,
int transferType,
boolean isAlphaPremultiplied)
```

Returns a specifier for a packed image format that will use a

DirectColorModel

and a packed

SampleModel

to store each pixel packed into in a
single byte, short, or int.

**Parameters:** colorSpace

- the desired

ColorSpace

.
**Parameters:** redMask

- a contiguous mask indicated the position of the
red channel.
**Parameters:** greenMask

- a contiguous mask indicated the position of the
green channel.
**Parameters:** blueMask

- a contiguous mask indicated the position of the
blue channel.
**Parameters:** alphaMask

- a contiguous mask indicated the position of the
alpha channel.
**Parameters:** transferType

- the desired

SampleModel

transfer type.
**Parameters:** isAlphaPremultiplied

-

true

if the color channels
will be premultipled by the alpha channel.
**Returns:** an

ImageTypeSpecifier

with the desired
characteristics.
**Throws:** IllegalArgumentException

- if

colorSpace

is

null

.
**Throws:** IllegalArgumentException

- if

colorSpace

is not of type

TYPE_RGB

.
**Throws:** IllegalArgumentException

- if no mask has at least 1
bit set.
**Throws:** IllegalArgumentException

- if

transferType

if not one of

DataBuffer.TYPE_BYTE

,

DataBuffer.TYPE_USHORT

, or

DataBuffer.TYPE_INT

.

- createInterleaved

```java
public static
ImageTypeSpecifier
createInterleaved​(
ColorSpace
colorSpace,
int[] bandOffsets,
int dataType,
boolean hasAlpha,
boolean isAlphaPremultiplied)
```

Returns a specifier for an interleaved image format that will
use a

ComponentColorModel

and a

PixelInterleavedSampleModel

to store each pixel
component in a separate byte, short, or int.

**Parameters:** colorSpace

- the desired

ColorSpace

.
**Parameters:** bandOffsets

- an array of

int

s indicating the
offsets for each band.
**Parameters:** dataType

- the desired data type, as one of the enumerations
from the

DataBuffer

class.
**Parameters:** hasAlpha

-

true

if an alpha channel is desired.
**Parameters:** isAlphaPremultiplied

-

true

if the color channels
will be premultipled by the alpha channel.
**Returns:** an

ImageTypeSpecifier

with the desired
characteristics.
**Throws:** IllegalArgumentException

- if

colorSpace

is

null

.
**Throws:** IllegalArgumentException

- if

bandOffsets

is

null

.
**Throws:** IllegalArgumentException

- if

dataType

is
not one of the legal

DataBuffer.TYPE_*

constants.
**Throws:** IllegalArgumentException

- if

bandOffsets.length

does not equal the number of
color space components, plus 1 if

hasAlpha

is

true

.

- createBanded

```java
public static
ImageTypeSpecifier
createBanded​(
ColorSpace
colorSpace,
int[] bankIndices,
int[] bandOffsets,
int dataType,
boolean hasAlpha,
boolean isAlphaPremultiplied)
```

Returns a specifier for a banded image format that will use a

ComponentColorModel

and a

BandedSampleModel

to store each channel in a
separate array.

**Parameters:** colorSpace

- the desired

ColorSpace

.
**Parameters:** bankIndices

- an array of

int

s indicating the
bank in which each band will be stored.
**Parameters:** bandOffsets

- an array of

int

s indicating the
starting offset of each band within its bank.
**Parameters:** dataType

- the desired data type, as one of the enumerations
from the

DataBuffer

class.
**Parameters:** hasAlpha

-

true

if an alpha channel is desired.
**Parameters:** isAlphaPremultiplied

-

true

if the color channels
will be premultipled by the alpha channel.
**Returns:** an

ImageTypeSpecifier

with the desired
characteristics.
**Throws:** IllegalArgumentException

- if

colorSpace

is

null

.
**Throws:** IllegalArgumentException

- if

bankIndices

is

null

.
**Throws:** IllegalArgumentException

- if

bandOffsets

is

null

.
**Throws:** IllegalArgumentException

- if the lengths of

bankIndices

and

bandOffsets

differ.
**Throws:** IllegalArgumentException

- if

bandOffsets.length

does not equal the number of
color space components, plus 1 if

hasAlpha

is

true

.
**Throws:** IllegalArgumentException

- if

dataType

is
not one of the legal

DataBuffer.TYPE_*

constants.

- createGrayscale

```java
public static
ImageTypeSpecifier
createGrayscale​(int bits,
int dataType,
boolean isSigned)
```

Returns a specifier for a grayscale image format that will pack
pixels of the given bit depth into array elements of
the specified data type.

**Parameters:** bits

- the number of bits per gray value (1, 2, 4, 8, or 16).
**Parameters:** dataType

- the desired data type, as one of the enumerations
from the

DataBuffer

class.
**Parameters:** isSigned

-

true

if negative values are to
be represented.
**Returns:** an

ImageTypeSpecifier

with the desired
characteristics.
**Throws:** IllegalArgumentException

- if

bits

is
not one of 1, 2, 4, 8, or 16.
**Throws:** IllegalArgumentException

- if

dataType

is
not one of

DataBuffer.TYPE_BYTE

,

DataBuffer.TYPE_SHORT

, or

DataBuffer.TYPE_USHORT

.
**Throws:** IllegalArgumentException

- if

bits

is
larger than the bit size of the given

dataType

.

- createGrayscale

```java
public static
ImageTypeSpecifier
createGrayscale​(int bits,
int dataType,
boolean isSigned,
boolean isAlphaPremultiplied)
```

Returns a specifier for a grayscale plus alpha image format
that will pack pixels of the given bit depth into array
elements of the specified data type.

**Parameters:** bits

- the number of bits per gray value (1, 2, 4, 8, or 16).
**Parameters:** dataType

- the desired data type, as one of the enumerations
from the

DataBuffer

class.
**Parameters:** isSigned

-

true

if negative values are to
be represented.
**Parameters:** isAlphaPremultiplied

-

true

if the luminance channel
will be premultipled by the alpha channel.
**Returns:** an

ImageTypeSpecifier

with the desired
characteristics.
**Throws:** IllegalArgumentException

- if

bits

is
not one of 1, 2, 4, 8, or 16.
**Throws:** IllegalArgumentException

- if

dataType

is
not one of

DataBuffer.TYPE_BYTE

,

DataBuffer.TYPE_SHORT

, or

DataBuffer.TYPE_USHORT

.
**Throws:** IllegalArgumentException

- if

bits

is
larger than the bit size of the given

dataType

.

- createIndexed

```java
public static
ImageTypeSpecifier
createIndexed​(byte[] redLUT,
byte[] greenLUT,
byte[] blueLUT,
byte[] alphaLUT,
int bits,
int dataType)
```

Returns a specifier for an indexed-color image format that will pack
index values of the given bit depth into array elements of
the specified data type.

**Parameters:** redLUT

- an array of

byte

s containing
the red values for each index.
**Parameters:** greenLUT

- an array of

byte

s containing * the
green values for each index.
**Parameters:** blueLUT

- an array of

byte

s containing the
blue values for each index.
**Parameters:** alphaLUT

- an array of

byte

s containing the
alpha values for each index, or

null

to create a
fully opaque LUT.
**Parameters:** bits

- the number of bits in each index.
**Parameters:** dataType

- the desired output type, as one of the enumerations
from the

DataBuffer

class.
**Returns:** an

ImageTypeSpecifier

with the desired
characteristics.
**Throws:** IllegalArgumentException

- if

redLUT

is

null

.
**Throws:** IllegalArgumentException

- if

greenLUT

is

null

.
**Throws:** IllegalArgumentException

- if

blueLUT

is

null

.
**Throws:** IllegalArgumentException

- if

bits

is
not one of 1, 2, 4, 8, or 16.
**Throws:** IllegalArgumentException

- if the
non-

null

LUT parameters do not have lengths of
exactly

1 << bits

.
**Throws:** IllegalArgumentException

- if

dataType

is
not one of

DataBuffer.TYPE_BYTE

,

DataBuffer.TYPE_SHORT

,

DataBuffer.TYPE_USHORT

,
or

DataBuffer.TYPE_INT

.
**Throws:** IllegalArgumentException

- if

bits

is
larger than the bit size of the given

dataType

.

- createFromBufferedImageType

```java
public static
ImageTypeSpecifier
createFromBufferedImageType​(int bufferedImageType)
```

Returns an

ImageTypeSpecifier

that encodes
one of the standard

BufferedImage

types
(other than

TYPE_CUSTOM

).

**Parameters:** bufferedImageType

- an int representing one of the standard

BufferedImage

types.
**Returns:** an

ImageTypeSpecifier

with the desired
characteristics.
**Throws:** IllegalArgumentException

- if

bufferedImageType

is not one of the standard
types, or is equal to

TYPE_CUSTOM

.
**See Also:** BufferedImage

,

BufferedImage.TYPE_INT_RGB

,

BufferedImage.TYPE_INT_ARGB

,

BufferedImage.TYPE_INT_ARGB_PRE

,

BufferedImage.TYPE_INT_BGR

,

BufferedImage.TYPE_3BYTE_BGR

,

BufferedImage.TYPE_4BYTE_ABGR

,

BufferedImage.TYPE_4BYTE_ABGR_PRE

,

BufferedImage.TYPE_USHORT_565_RGB

,

BufferedImage.TYPE_USHORT_555_RGB

,

BufferedImage.TYPE_BYTE_GRAY

,

BufferedImage.TYPE_USHORT_GRAY

,

BufferedImage.TYPE_BYTE_BINARY

,

BufferedImage.TYPE_BYTE_INDEXED

- createFromRenderedImage

```java
public static
ImageTypeSpecifier
createFromRenderedImage​(
RenderedImage
image)
```

Returns an

ImageTypeSpecifier

that encodes the
layout of a

RenderedImage

(which may be a

BufferedImage

).

**Parameters:** image

- a

RenderedImage

.
**Returns:** an

ImageTypeSpecifier

with the desired
characteristics.
**Throws:** IllegalArgumentException

- if

image

is

null

.

- getBufferedImageType

```java
public int getBufferedImageType()
```

Returns an int containing one of the enumerated constant values
describing image formats from

BufferedImage

.

**Returns:** an

int

representing a

BufferedImage

type.
**See Also:** BufferedImage

,

BufferedImage.TYPE_CUSTOM

,

BufferedImage.TYPE_INT_RGB

,

BufferedImage.TYPE_INT_ARGB

,

BufferedImage.TYPE_INT_ARGB_PRE

,

BufferedImage.TYPE_INT_BGR

,

BufferedImage.TYPE_3BYTE_BGR

,

BufferedImage.TYPE_4BYTE_ABGR

,

BufferedImage.TYPE_4BYTE_ABGR_PRE

,

BufferedImage.TYPE_USHORT_565_RGB

,

BufferedImage.TYPE_USHORT_555_RGB

,

BufferedImage.TYPE_BYTE_GRAY

,

BufferedImage.TYPE_USHORT_GRAY

,

BufferedImage.TYPE_BYTE_BINARY

,

BufferedImage.TYPE_BYTE_INDEXED

- getNumComponents

```java
public int getNumComponents()
```

Return the number of color components
specified by this object. This is the same value as returned by

ColorModel.getNumComponents

**Returns:** the number of components in the image.

- getNumBands

```java
public int getNumBands()
```

Return the number of bands
specified by this object. This is the same value as returned by

SampleModel.getNumBands

**Returns:** the number of bands in the image.

- getBitsPerBand

```java
public int getBitsPerBand​(int band)
```

Return the number of bits used to represent samples of the given band.

**Parameters:** band

- the index of the band to be queried, as an
int.
**Returns:** an int specifying a number of bits.
**Throws:** IllegalArgumentException

- if

band

is
negative or greater than the largest band index.

- getSampleModel

```java
public
SampleModel
getSampleModel()
```

Returns a

SampleModel

based on the settings
encapsulated within this object. The width and height of the

SampleModel

will be set to arbitrary values.

**Returns:** a

SampleModel

with arbitrary dimensions.

- getSampleModel

```java
public
SampleModel
getSampleModel​(int width,
int height)
```

Returns a

SampleModel

based on the settings
encapsulated within this object. The width and height of the

SampleModel

will be set to the supplied values.

**Parameters:** width

- the desired width of the returned

SampleModel

.
**Parameters:** height

- the desired height of the returned

SampleModel

.
**Returns:** a

SampleModel

with the given dimensions.
**Throws:** IllegalArgumentException

- if either

width

or

height

are negative or zero.
**Throws:** IllegalArgumentException

- if the product of

width

and

height

is greater than

Integer.MAX_VALUE

- getColorModel

```java
public
ColorModel
getColorModel()
```

Returns the

ColorModel

specified by this object.

**Returns:** a

ColorModel

.

- createBufferedImage

```java
public
BufferedImage
createBufferedImage​(int width,
int height)
```

Creates a

BufferedImage

with a given width and
height according to the specification embodied in this object.

**Parameters:** width

- the desired width of the returned

BufferedImage

.
**Parameters:** height

- the desired height of the returned

BufferedImage

.
**Returns:** a new

BufferedImage
**Throws:** IllegalArgumentException

- if either

width

or

height

are negative or zero.
**Throws:** IllegalArgumentException

- if the product of

width

and

height

is greater than

Integer.MAX_VALUE

, or if the number of array
elements needed to store the image is greater than

Integer.MAX_VALUE

.

- equals

```java
public boolean equals​(
Object
o)
```

Returns

true

if the given

Object

is
an

ImageTypeSpecifier

and has a

SampleModel

and

ColorModel

that are
equal to those of this object.

**Overrides:** equals

in class

Object
**Parameters:** o

- the

Object

to be compared for equality.
**Returns:** true

if the given object is an equivalent

ImageTypeSpecifier

.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code for this ImageTypeSpecifier.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this ImageTypeSpecifier
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### Method Detail

createPacked

```java
public static
ImageTypeSpecifier
createPacked​(
ColorSpace
colorSpace,
int redMask,
int greenMask,
int blueMask,
int alphaMask,
int transferType,
boolean isAlphaPremultiplied)
```

Returns a specifier for a packed image format that will use a

DirectColorModel

and a packed

SampleModel

to store each pixel packed into in a
single byte, short, or int.

**Parameters:** colorSpace

- the desired

ColorSpace

.
**Parameters:** redMask

- a contiguous mask indicated the position of the
red channel.
**Parameters:** greenMask

- a contiguous mask indicated the position of the
green channel.
**Parameters:** blueMask

- a contiguous mask indicated the position of the
blue channel.
**Parameters:** alphaMask

- a contiguous mask indicated the position of the
alpha channel.
**Parameters:** transferType

- the desired

SampleModel

transfer type.
**Parameters:** isAlphaPremultiplied

-

true

if the color channels
will be premultipled by the alpha channel.
**Returns:** an

ImageTypeSpecifier

with the desired
characteristics.
**Throws:** IllegalArgumentException

- if

colorSpace

is

null

.
**Throws:** IllegalArgumentException

- if

colorSpace

is not of type

TYPE_RGB

.
**Throws:** IllegalArgumentException

- if no mask has at least 1
bit set.
**Throws:** IllegalArgumentException

- if

transferType

if not one of

DataBuffer.TYPE_BYTE

,

DataBuffer.TYPE_USHORT

, or

DataBuffer.TYPE_INT

.

---

#### createPacked

public static

ImageTypeSpecifier

createPacked​(

ColorSpace

colorSpace,
int redMask,
int greenMask,
int blueMask,
int alphaMask,
int transferType,
boolean isAlphaPremultiplied)

Returns a specifier for a packed image format that will use a

DirectColorModel

and a packed

SampleModel

to store each pixel packed into in a
single byte, short, or int.

createInterleaved

```java
public static
ImageTypeSpecifier
createInterleaved​(
ColorSpace
colorSpace,
int[] bandOffsets,
int dataType,
boolean hasAlpha,
boolean isAlphaPremultiplied)
```

Returns a specifier for an interleaved image format that will
use a

ComponentColorModel

and a

PixelInterleavedSampleModel

to store each pixel
component in a separate byte, short, or int.

**Parameters:** colorSpace

- the desired

ColorSpace

.
**Parameters:** bandOffsets

- an array of

int

s indicating the
offsets for each band.
**Parameters:** dataType

- the desired data type, as one of the enumerations
from the

DataBuffer

class.
**Parameters:** hasAlpha

-

true

if an alpha channel is desired.
**Parameters:** isAlphaPremultiplied

-

true

if the color channels
will be premultipled by the alpha channel.
**Returns:** an

ImageTypeSpecifier

with the desired
characteristics.
**Throws:** IllegalArgumentException

- if

colorSpace

is

null

.
**Throws:** IllegalArgumentException

- if

bandOffsets

is

null

.
**Throws:** IllegalArgumentException

- if

dataType

is
not one of the legal

DataBuffer.TYPE_*

constants.
**Throws:** IllegalArgumentException

- if

bandOffsets.length

does not equal the number of
color space components, plus 1 if

hasAlpha

is

true

.

---

#### createInterleaved

public static

ImageTypeSpecifier

createInterleaved​(

ColorSpace

colorSpace,
int[] bandOffsets,
int dataType,
boolean hasAlpha,
boolean isAlphaPremultiplied)

Returns a specifier for an interleaved image format that will
use a

ComponentColorModel

and a

PixelInterleavedSampleModel

to store each pixel
component in a separate byte, short, or int.

createBanded

```java
public static
ImageTypeSpecifier
createBanded​(
ColorSpace
colorSpace,
int[] bankIndices,
int[] bandOffsets,
int dataType,
boolean hasAlpha,
boolean isAlphaPremultiplied)
```

Returns a specifier for a banded image format that will use a

ComponentColorModel

and a

BandedSampleModel

to store each channel in a
separate array.

**Parameters:** colorSpace

- the desired

ColorSpace

.
**Parameters:** bankIndices

- an array of

int

s indicating the
bank in which each band will be stored.
**Parameters:** bandOffsets

- an array of

int

s indicating the
starting offset of each band within its bank.
**Parameters:** dataType

- the desired data type, as one of the enumerations
from the

DataBuffer

class.
**Parameters:** hasAlpha

-

true

if an alpha channel is desired.
**Parameters:** isAlphaPremultiplied

-

true

if the color channels
will be premultipled by the alpha channel.
**Returns:** an

ImageTypeSpecifier

with the desired
characteristics.
**Throws:** IllegalArgumentException

- if

colorSpace

is

null

.
**Throws:** IllegalArgumentException

- if

bankIndices

is

null

.
**Throws:** IllegalArgumentException

- if

bandOffsets

is

null

.
**Throws:** IllegalArgumentException

- if the lengths of

bankIndices

and

bandOffsets

differ.
**Throws:** IllegalArgumentException

- if

bandOffsets.length

does not equal the number of
color space components, plus 1 if

hasAlpha

is

true

.
**Throws:** IllegalArgumentException

- if

dataType

is
not one of the legal

DataBuffer.TYPE_*

constants.

---

#### createBanded

public static

ImageTypeSpecifier

createBanded​(

ColorSpace

colorSpace,
int[] bankIndices,
int[] bandOffsets,
int dataType,
boolean hasAlpha,
boolean isAlphaPremultiplied)

Returns a specifier for a banded image format that will use a

ComponentColorModel

and a

BandedSampleModel

to store each channel in a
separate array.

createGrayscale

```java
public static
ImageTypeSpecifier
createGrayscale​(int bits,
int dataType,
boolean isSigned)
```

Returns a specifier for a grayscale image format that will pack
pixels of the given bit depth into array elements of
the specified data type.

**Parameters:** bits

- the number of bits per gray value (1, 2, 4, 8, or 16).
**Parameters:** dataType

- the desired data type, as one of the enumerations
from the

DataBuffer

class.
**Parameters:** isSigned

-

true

if negative values are to
be represented.
**Returns:** an

ImageTypeSpecifier

with the desired
characteristics.
**Throws:** IllegalArgumentException

- if

bits

is
not one of 1, 2, 4, 8, or 16.
**Throws:** IllegalArgumentException

- if

dataType

is
not one of

DataBuffer.TYPE_BYTE

,

DataBuffer.TYPE_SHORT

, or

DataBuffer.TYPE_USHORT

.
**Throws:** IllegalArgumentException

- if

bits

is
larger than the bit size of the given

dataType

.

---

#### createGrayscale

public static

ImageTypeSpecifier

createGrayscale​(int bits,
int dataType,
boolean isSigned)

Returns a specifier for a grayscale image format that will pack
pixels of the given bit depth into array elements of
the specified data type.

createGrayscale

```java
public static
ImageTypeSpecifier
createGrayscale​(int bits,
int dataType,
boolean isSigned,
boolean isAlphaPremultiplied)
```

Returns a specifier for a grayscale plus alpha image format
that will pack pixels of the given bit depth into array
elements of the specified data type.

**Parameters:** bits

- the number of bits per gray value (1, 2, 4, 8, or 16).
**Parameters:** dataType

- the desired data type, as one of the enumerations
from the

DataBuffer

class.
**Parameters:** isSigned

-

true

if negative values are to
be represented.
**Parameters:** isAlphaPremultiplied

-

true

if the luminance channel
will be premultipled by the alpha channel.
**Returns:** an

ImageTypeSpecifier

with the desired
characteristics.
**Throws:** IllegalArgumentException

- if

bits

is
not one of 1, 2, 4, 8, or 16.
**Throws:** IllegalArgumentException

- if

dataType

is
not one of

DataBuffer.TYPE_BYTE

,

DataBuffer.TYPE_SHORT

, or

DataBuffer.TYPE_USHORT

.
**Throws:** IllegalArgumentException

- if

bits

is
larger than the bit size of the given

dataType

.

---

#### createGrayscale

public static

ImageTypeSpecifier

createGrayscale​(int bits,
int dataType,
boolean isSigned,
boolean isAlphaPremultiplied)

Returns a specifier for a grayscale plus alpha image format
that will pack pixels of the given bit depth into array
elements of the specified data type.

createIndexed

```java
public static
ImageTypeSpecifier
createIndexed​(byte[] redLUT,
byte[] greenLUT,
byte[] blueLUT,
byte[] alphaLUT,
int bits,
int dataType)
```

Returns a specifier for an indexed-color image format that will pack
index values of the given bit depth into array elements of
the specified data type.

**Parameters:** redLUT

- an array of

byte

s containing
the red values for each index.
**Parameters:** greenLUT

- an array of

byte

s containing * the
green values for each index.
**Parameters:** blueLUT

- an array of

byte

s containing the
blue values for each index.
**Parameters:** alphaLUT

- an array of

byte

s containing the
alpha values for each index, or

null

to create a
fully opaque LUT.
**Parameters:** bits

- the number of bits in each index.
**Parameters:** dataType

- the desired output type, as one of the enumerations
from the

DataBuffer

class.
**Returns:** an

ImageTypeSpecifier

with the desired
characteristics.
**Throws:** IllegalArgumentException

- if

redLUT

is

null

.
**Throws:** IllegalArgumentException

- if

greenLUT

is

null

.
**Throws:** IllegalArgumentException

- if

blueLUT

is

null

.
**Throws:** IllegalArgumentException

- if

bits

is
not one of 1, 2, 4, 8, or 16.
**Throws:** IllegalArgumentException

- if the
non-

null

LUT parameters do not have lengths of
exactly

1 << bits

.
**Throws:** IllegalArgumentException

- if

dataType

is
not one of

DataBuffer.TYPE_BYTE

,

DataBuffer.TYPE_SHORT

,

DataBuffer.TYPE_USHORT

,
or

DataBuffer.TYPE_INT

.
**Throws:** IllegalArgumentException

- if

bits

is
larger than the bit size of the given

dataType

.

---

#### createIndexed

public static

ImageTypeSpecifier

createIndexed​(byte[] redLUT,
byte[] greenLUT,
byte[] blueLUT,
byte[] alphaLUT,
int bits,
int dataType)

Returns a specifier for an indexed-color image format that will pack
index values of the given bit depth into array elements of
the specified data type.

createFromBufferedImageType

```java
public static
ImageTypeSpecifier
createFromBufferedImageType​(int bufferedImageType)
```

Returns an

ImageTypeSpecifier

that encodes
one of the standard

BufferedImage

types
(other than

TYPE_CUSTOM

).

**Parameters:** bufferedImageType

- an int representing one of the standard

BufferedImage

types.
**Returns:** an

ImageTypeSpecifier

with the desired
characteristics.
**Throws:** IllegalArgumentException

- if

bufferedImageType

is not one of the standard
types, or is equal to

TYPE_CUSTOM

.
**See Also:** BufferedImage

,

BufferedImage.TYPE_INT_RGB

,

BufferedImage.TYPE_INT_ARGB

,

BufferedImage.TYPE_INT_ARGB_PRE

,

BufferedImage.TYPE_INT_BGR

,

BufferedImage.TYPE_3BYTE_BGR

,

BufferedImage.TYPE_4BYTE_ABGR

,

BufferedImage.TYPE_4BYTE_ABGR_PRE

,

BufferedImage.TYPE_USHORT_565_RGB

,

BufferedImage.TYPE_USHORT_555_RGB

,

BufferedImage.TYPE_BYTE_GRAY

,

BufferedImage.TYPE_USHORT_GRAY

,

BufferedImage.TYPE_BYTE_BINARY

,

BufferedImage.TYPE_BYTE_INDEXED

---

#### createFromBufferedImageType

public static

ImageTypeSpecifier

createFromBufferedImageType​(int bufferedImageType)

Returns an

ImageTypeSpecifier

that encodes
one of the standard

BufferedImage

types
(other than

TYPE_CUSTOM

).

createFromRenderedImage

```java
public static
ImageTypeSpecifier
createFromRenderedImage​(
RenderedImage
image)
```

Returns an

ImageTypeSpecifier

that encodes the
layout of a

RenderedImage

(which may be a

BufferedImage

).

**Parameters:** image

- a

RenderedImage

.
**Returns:** an

ImageTypeSpecifier

with the desired
characteristics.
**Throws:** IllegalArgumentException

- if

image

is

null

.

---

#### createFromRenderedImage

public static

ImageTypeSpecifier

createFromRenderedImage​(

RenderedImage

image)

Returns an

ImageTypeSpecifier

that encodes the
layout of a

RenderedImage

(which may be a

BufferedImage

).

getBufferedImageType

```java
public int getBufferedImageType()
```

Returns an int containing one of the enumerated constant values
describing image formats from

BufferedImage

.

**Returns:** an

int

representing a

BufferedImage

type.
**See Also:** BufferedImage

,

BufferedImage.TYPE_CUSTOM

,

BufferedImage.TYPE_INT_RGB

,

BufferedImage.TYPE_INT_ARGB

,

BufferedImage.TYPE_INT_ARGB_PRE

,

BufferedImage.TYPE_INT_BGR

,

BufferedImage.TYPE_3BYTE_BGR

,

BufferedImage.TYPE_4BYTE_ABGR

,

BufferedImage.TYPE_4BYTE_ABGR_PRE

,

BufferedImage.TYPE_USHORT_565_RGB

,

BufferedImage.TYPE_USHORT_555_RGB

,

BufferedImage.TYPE_BYTE_GRAY

,

BufferedImage.TYPE_USHORT_GRAY

,

BufferedImage.TYPE_BYTE_BINARY

,

BufferedImage.TYPE_BYTE_INDEXED

---

#### getBufferedImageType

public int getBufferedImageType()

Returns an int containing one of the enumerated constant values
describing image formats from

BufferedImage

.

getNumComponents

```java
public int getNumComponents()
```

Return the number of color components
specified by this object. This is the same value as returned by

ColorModel.getNumComponents

**Returns:** the number of components in the image.

---

#### getNumComponents

public int getNumComponents()

Return the number of color components
specified by this object. This is the same value as returned by

ColorModel.getNumComponents

getNumBands

```java
public int getNumBands()
```

Return the number of bands
specified by this object. This is the same value as returned by

SampleModel.getNumBands

**Returns:** the number of bands in the image.

---

#### getNumBands

public int getNumBands()

Return the number of bands
specified by this object. This is the same value as returned by

SampleModel.getNumBands

getBitsPerBand

```java
public int getBitsPerBand​(int band)
```

Return the number of bits used to represent samples of the given band.

**Parameters:** band

- the index of the band to be queried, as an
int.
**Returns:** an int specifying a number of bits.
**Throws:** IllegalArgumentException

- if

band

is
negative or greater than the largest band index.

---

#### getBitsPerBand

public int getBitsPerBand​(int band)

Return the number of bits used to represent samples of the given band.

getSampleModel

```java
public
SampleModel
getSampleModel()
```

Returns a

SampleModel

based on the settings
encapsulated within this object. The width and height of the

SampleModel

will be set to arbitrary values.

**Returns:** a

SampleModel

with arbitrary dimensions.

---

#### getSampleModel

public

SampleModel

getSampleModel()

Returns a

SampleModel

based on the settings
encapsulated within this object. The width and height of the

SampleModel

will be set to arbitrary values.

getSampleModel

```java
public
SampleModel
getSampleModel​(int width,
int height)
```

Returns a

SampleModel

based on the settings
encapsulated within this object. The width and height of the

SampleModel

will be set to the supplied values.

**Parameters:** width

- the desired width of the returned

SampleModel

.
**Parameters:** height

- the desired height of the returned

SampleModel

.
**Returns:** a

SampleModel

with the given dimensions.
**Throws:** IllegalArgumentException

- if either

width

or

height

are negative or zero.
**Throws:** IllegalArgumentException

- if the product of

width

and

height

is greater than

Integer.MAX_VALUE

---

#### getSampleModel

public

SampleModel

getSampleModel​(int width,
int height)

Returns a

SampleModel

based on the settings
encapsulated within this object. The width and height of the

SampleModel

will be set to the supplied values.

getColorModel

```java
public
ColorModel
getColorModel()
```

Returns the

ColorModel

specified by this object.

**Returns:** a

ColorModel

.

---

#### getColorModel

public

ColorModel

getColorModel()

Returns the

ColorModel

specified by this object.

createBufferedImage

```java
public
BufferedImage
createBufferedImage​(int width,
int height)
```

Creates a

BufferedImage

with a given width and
height according to the specification embodied in this object.

**Parameters:** width

- the desired width of the returned

BufferedImage

.
**Parameters:** height

- the desired height of the returned

BufferedImage

.
**Returns:** a new

BufferedImage
**Throws:** IllegalArgumentException

- if either

width

or

height

are negative or zero.
**Throws:** IllegalArgumentException

- if the product of

width

and

height

is greater than

Integer.MAX_VALUE

, or if the number of array
elements needed to store the image is greater than

Integer.MAX_VALUE

.

---

#### createBufferedImage

public

BufferedImage

createBufferedImage​(int width,
int height)

Creates a

BufferedImage

with a given width and
height according to the specification embodied in this object.

equals

```java
public boolean equals​(
Object
o)
```

Returns

true

if the given

Object

is
an

ImageTypeSpecifier

and has a

SampleModel

and

ColorModel

that are
equal to those of this object.

**Overrides:** equals

in class

Object
**Parameters:** o

- the

Object

to be compared for equality.
**Returns:** true

if the given object is an equivalent

ImageTypeSpecifier

.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

o)

Returns

true

if the given

Object

is
an

ImageTypeSpecifier

and has a

SampleModel

and

ColorModel

that are
equal to those of this object.

hashCode

```java
public int hashCode()
```

Returns the hash code for this ImageTypeSpecifier.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this ImageTypeSpecifier
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns the hash code for this ImageTypeSpecifier.

---

