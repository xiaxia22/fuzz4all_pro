# Class PixelInterleavedSampleModel

**Source:** `java.desktop\java\awt\image\PixelInterleavedSampleModel.html`

### Class Description

```java
public class
PixelInterleavedSampleModel

extends
ComponentSampleModel
```

This class represents image data which is stored in a pixel interleaved
fashion and for
which each sample of a pixel occupies one data element of the DataBuffer.
It subclasses ComponentSampleModel but provides a more efficient
implementation for accessing pixel interleaved image data than is provided
by ComponentSampleModel. This class
stores sample data for all bands in a single bank of the
DataBuffer. Accessor methods are provided so that image data can be
manipulated directly. Pixel stride is the number of
data array elements between two samples for the same band on the same
scanline. Scanline stride is the number of data array elements between
a given sample and the corresponding sample in the same column of the next
scanline. Band offsets denote the number
of data array elements from the first data array element of the bank
of the DataBuffer holding each band to the first sample of the band.
The bands are numbered from 0 to N-1.
Bank indices denote the correspondence between a bank of the data buffer
and a band of image data.
This class supports

TYPE_BYTE

,

TYPE_USHORT

,

TYPE_SHORT

,

TYPE_INT

,

TYPE_FLOAT

and

TYPE_DOUBLE

datatypes.

---

### Field Details

*No entries found.*

### Constructor Details

#### public PixelInterleavedSampleModel​(int dataType,
int w,
int h,
int pixelStride,
int scanlineStride,
int[] bandOffsets)

Constructs a PixelInterleavedSampleModel with the specified parameters.
The number of bands will be given by the length of the bandOffsets
array.

**Parameters:**
- dataType

- The data type for storing samples.
- w

- The width (in pixels) of the region of
image data described.
- h

- The height (in pixels) of the region of
image data described.
- pixelStride

- The pixel stride of the image data.
- scanlineStride

- The line stride of the image data.
- bandOffsets

- The offsets of all bands.

**Throws:**
- IllegalArgumentException

- if

w

or

h

is not greater than 0
- IllegalArgumentException

- if any offset between bands is
greater than the scanline stride
- IllegalArgumentException

- if the product of

pixelStride

and

w

is greater
than

scanlineStride
- IllegalArgumentException

- if

pixelStride

is
less than any offset between bands
- IllegalArgumentException

- if

dataType

is not
one of the supported data types

---

### Method Details

#### public
SampleModel
createCompatibleSampleModel​(int w,
int h)

Creates a new PixelInterleavedSampleModel with the specified
width and height. The new PixelInterleavedSampleModel will have the
same number of bands, storage data type, and pixel stride
as this PixelInterleavedSampleModel. The band offsets may be
compressed such that the minimum of all of the band offsets is zero.

**Overrides:**
- createCompatibleSampleModel

in class

ComponentSampleModel

**Parameters:**
- w

- the width of the resulting

SampleModel
- h

- the height of the resulting

SampleModel

**Returns:**
- a new

SampleModel

with the specified width
and height.

**Throws:**
- IllegalArgumentException

- if

w

or

h

is not greater than 0

---

#### public
SampleModel
createSubsetSampleModel​(int[] bands)

Creates a new PixelInterleavedSampleModel with a subset of the
bands of this PixelInterleavedSampleModel. The new
PixelInterleavedSampleModel can be used with any DataBuffer that the
existing PixelInterleavedSampleModel can be used with. The new
PixelInterleavedSampleModel/DataBuffer combination will represent
an image with a subset of the bands of the original
PixelInterleavedSampleModel/DataBuffer combination.

**Overrides:**
- createSubsetSampleModel

in class

ComponentSampleModel

**Parameters:**
- bands

- a subset of bands from this

ComponentSampleModel

**Returns:**
- a

ComponentSampleModel

created with a subset
of bands from this

ComponentSampleModel

.

---

### Additional Sections

#### Class PixelInterleavedSampleModel

java.lang.Object

- java.awt.image.SampleModel
- - java.awt.image.ComponentSampleModel
- - java.awt.image.PixelInterleavedSampleModel

java.awt.image.SampleModel

- java.awt.image.ComponentSampleModel
- - java.awt.image.PixelInterleavedSampleModel

java.awt.image.ComponentSampleModel

- java.awt.image.PixelInterleavedSampleModel

java.awt.image.PixelInterleavedSampleModel

```java
public class
PixelInterleavedSampleModel

extends
ComponentSampleModel
```

This class represents image data which is stored in a pixel interleaved
fashion and for
which each sample of a pixel occupies one data element of the DataBuffer.
It subclasses ComponentSampleModel but provides a more efficient
implementation for accessing pixel interleaved image data than is provided
by ComponentSampleModel. This class
stores sample data for all bands in a single bank of the
DataBuffer. Accessor methods are provided so that image data can be
manipulated directly. Pixel stride is the number of
data array elements between two samples for the same band on the same
scanline. Scanline stride is the number of data array elements between
a given sample and the corresponding sample in the same column of the next
scanline. Band offsets denote the number
of data array elements from the first data array element of the bank
of the DataBuffer holding each band to the first sample of the band.
The bands are numbered from 0 to N-1.
Bank indices denote the correspondence between a bank of the data buffer
and a band of image data.
This class supports

TYPE_BYTE

,

TYPE_USHORT

,

TYPE_SHORT

,

TYPE_INT

,

TYPE_FLOAT

and

TYPE_DOUBLE

datatypes.

public class

PixelInterleavedSampleModel

extends

ComponentSampleModel

This class represents image data which is stored in a pixel interleaved
fashion and for
which each sample of a pixel occupies one data element of the DataBuffer.
It subclasses ComponentSampleModel but provides a more efficient
implementation for accessing pixel interleaved image data than is provided
by ComponentSampleModel. This class
stores sample data for all bands in a single bank of the
DataBuffer. Accessor methods are provided so that image data can be
manipulated directly. Pixel stride is the number of
data array elements between two samples for the same band on the same
scanline. Scanline stride is the number of data array elements between
a given sample and the corresponding sample in the same column of the next
scanline. Band offsets denote the number
of data array elements from the first data array element of the bank
of the DataBuffer holding each band to the first sample of the band.
The bands are numbered from 0 to N-1.
Bank indices denote the correspondence between a bank of the data buffer
and a band of image data.
This class supports

TYPE_BYTE

,

TYPE_USHORT

,

TYPE_SHORT

,

TYPE_INT

,

TYPE_FLOAT

and

TYPE_DOUBLE

datatypes.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.awt.image.

ComponentSampleModel

bandOffsets

,

bankIndices

,

numBands

,

numBanks

,

pixelStride

,

scanlineStride

- Fields declared in class java.awt.image.

SampleModel

dataType

,

height

,

width

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

PixelInterleavedSampleModel

​(int dataType,
int w,
int h,
int pixelStride,
int scanlineStride,
int[] bandOffsets)

Constructs a PixelInterleavedSampleModel with the specified parameters.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

SampleModel

createCompatibleSampleModel

​(int w,
int h)

Creates a new PixelInterleavedSampleModel with the specified
width and height.

SampleModel

createSubsetSampleModel

​(int[] bands)

Creates a new PixelInterleavedSampleModel with a subset of the
bands of this PixelInterleavedSampleModel.

- Methods declared in class java.awt.image.

ComponentSampleModel

createDataBuffer

,

getBandOffsets

,

getBankIndices

,

getDataElements

,

getNumDataElements

,

getOffset

,

getOffset

,

getPixel

,

getPixels

,

getPixelStride

,

getSample

,

getSampleDouble

,

getSampleFloat

,

getSamples

,

getSampleSize

,

getSampleSize

,

getScanlineStride

,

setDataElements

,

setPixel

,

setPixels

,

setSample

,

setSample

,

setSample

,

setSamples

- Methods declared in class java.awt.image.

SampleModel

getDataElements

,

getDataType

,

getHeight

,

getNumBands

,

getPixel

,

getPixel

,

getPixels

,

getPixels

,

getSamples

,

getSamples

,

getTransferType

,

getWidth

,

setDataElements

,

setPixel

,

setPixel

,

setPixels

,

setPixels

,

setSamples

,

setSamples

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

- Fields declared in class java.awt.image.

ComponentSampleModel

bandOffsets

,

bankIndices

,

numBands

,

numBanks

,

pixelStride

,

scanlineStride

- Fields declared in class java.awt.image.

SampleModel

dataType

,

height

,

width

---

#### Field Summary

Fields declared in class java.awt.image.

ComponentSampleModel

bandOffsets

,

bankIndices

,

numBands

,

numBanks

,

pixelStride

,

scanlineStride

---

#### Fields declared in class java.awt.image. ComponentSampleModel

Fields declared in class java.awt.image.

SampleModel

dataType

,

height

,

width

---

#### Fields declared in class java.awt.image. SampleModel

Constructor Summary

Constructors

Constructor

Description

PixelInterleavedSampleModel

​(int dataType,
int w,
int h,
int pixelStride,
int scanlineStride,
int[] bandOffsets)

Constructs a PixelInterleavedSampleModel with the specified parameters.

---

#### Constructor Summary

Constructs a PixelInterleavedSampleModel with the specified parameters.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

SampleModel

createCompatibleSampleModel

​(int w,
int h)

Creates a new PixelInterleavedSampleModel with the specified
width and height.

SampleModel

createSubsetSampleModel

​(int[] bands)

Creates a new PixelInterleavedSampleModel with a subset of the
bands of this PixelInterleavedSampleModel.

- Methods declared in class java.awt.image.

ComponentSampleModel

createDataBuffer

,

getBandOffsets

,

getBankIndices

,

getDataElements

,

getNumDataElements

,

getOffset

,

getOffset

,

getPixel

,

getPixels

,

getPixelStride

,

getSample

,

getSampleDouble

,

getSampleFloat

,

getSamples

,

getSampleSize

,

getSampleSize

,

getScanlineStride

,

setDataElements

,

setPixel

,

setPixels

,

setSample

,

setSample

,

setSample

,

setSamples

- Methods declared in class java.awt.image.

SampleModel

getDataElements

,

getDataType

,

getHeight

,

getNumBands

,

getPixel

,

getPixel

,

getPixels

,

getPixels

,

getSamples

,

getSamples

,

getTransferType

,

getWidth

,

setDataElements

,

setPixel

,

setPixel

,

setPixels

,

setPixels

,

setSamples

,

setSamples

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

Creates a new PixelInterleavedSampleModel with the specified
width and height.

Creates a new PixelInterleavedSampleModel with a subset of the
bands of this PixelInterleavedSampleModel.

Methods declared in class java.awt.image.

ComponentSampleModel

createDataBuffer

,

getBandOffsets

,

getBankIndices

,

getDataElements

,

getNumDataElements

,

getOffset

,

getOffset

,

getPixel

,

getPixels

,

getPixelStride

,

getSample

,

getSampleDouble

,

getSampleFloat

,

getSamples

,

getSampleSize

,

getSampleSize

,

getScanlineStride

,

setDataElements

,

setPixel

,

setPixels

,

setSample

,

setSample

,

setSample

,

setSamples

---

#### Methods declared in class java.awt.image. ComponentSampleModel

Methods declared in class java.awt.image.

SampleModel

getDataElements

,

getDataType

,

getHeight

,

getNumBands

,

getPixel

,

getPixel

,

getPixels

,

getPixels

,

getSamples

,

getSamples

,

getTransferType

,

getWidth

,

setDataElements

,

setPixel

,

setPixel

,

setPixels

,

setPixels

,

setSamples

,

setSamples

---

#### Methods declared in class java.awt.image. SampleModel

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

- PixelInterleavedSampleModel

```java
public PixelInterleavedSampleModel​(int dataType,
int w,
int h,
int pixelStride,
int scanlineStride,
int[] bandOffsets)
```

Constructs a PixelInterleavedSampleModel with the specified parameters.
The number of bands will be given by the length of the bandOffsets
array.

**Parameters:** dataType

- The data type for storing samples.
**Parameters:** w

- The width (in pixels) of the region of
image data described.
**Parameters:** h

- The height (in pixels) of the region of
image data described.
**Parameters:** pixelStride

- The pixel stride of the image data.
**Parameters:** scanlineStride

- The line stride of the image data.
**Parameters:** bandOffsets

- The offsets of all bands.
**Throws:** IllegalArgumentException

- if

w

or

h

is not greater than 0
**Throws:** IllegalArgumentException

- if any offset between bands is
greater than the scanline stride
**Throws:** IllegalArgumentException

- if the product of

pixelStride

and

w

is greater
than

scanlineStride
**Throws:** IllegalArgumentException

- if

pixelStride

is
less than any offset between bands
**Throws:** IllegalArgumentException

- if

dataType

is not
one of the supported data types

============ METHOD DETAIL ==========

- Method Detail

- createCompatibleSampleModel

```java
public
SampleModel
createCompatibleSampleModel​(int w,
int h)
```

Creates a new PixelInterleavedSampleModel with the specified
width and height. The new PixelInterleavedSampleModel will have the
same number of bands, storage data type, and pixel stride
as this PixelInterleavedSampleModel. The band offsets may be
compressed such that the minimum of all of the band offsets is zero.

**Overrides:** createCompatibleSampleModel

in class

ComponentSampleModel
**Parameters:** w

- the width of the resulting

SampleModel
**Parameters:** h

- the height of the resulting

SampleModel
**Returns:** a new

SampleModel

with the specified width
and height.
**Throws:** IllegalArgumentException

- if

w

or

h

is not greater than 0

- createSubsetSampleModel

```java
public
SampleModel
createSubsetSampleModel​(int[] bands)
```

Creates a new PixelInterleavedSampleModel with a subset of the
bands of this PixelInterleavedSampleModel. The new
PixelInterleavedSampleModel can be used with any DataBuffer that the
existing PixelInterleavedSampleModel can be used with. The new
PixelInterleavedSampleModel/DataBuffer combination will represent
an image with a subset of the bands of the original
PixelInterleavedSampleModel/DataBuffer combination.

**Overrides:** createSubsetSampleModel

in class

ComponentSampleModel
**Parameters:** bands

- a subset of bands from this

ComponentSampleModel
**Returns:** a

ComponentSampleModel

created with a subset
of bands from this

ComponentSampleModel

.

Constructor Detail

- PixelInterleavedSampleModel

```java
public PixelInterleavedSampleModel​(int dataType,
int w,
int h,
int pixelStride,
int scanlineStride,
int[] bandOffsets)
```

Constructs a PixelInterleavedSampleModel with the specified parameters.
The number of bands will be given by the length of the bandOffsets
array.

**Parameters:** dataType

- The data type for storing samples.
**Parameters:** w

- The width (in pixels) of the region of
image data described.
**Parameters:** h

- The height (in pixels) of the region of
image data described.
**Parameters:** pixelStride

- The pixel stride of the image data.
**Parameters:** scanlineStride

- The line stride of the image data.
**Parameters:** bandOffsets

- The offsets of all bands.
**Throws:** IllegalArgumentException

- if

w

or

h

is not greater than 0
**Throws:** IllegalArgumentException

- if any offset between bands is
greater than the scanline stride
**Throws:** IllegalArgumentException

- if the product of

pixelStride

and

w

is greater
than

scanlineStride
**Throws:** IllegalArgumentException

- if

pixelStride

is
less than any offset between bands
**Throws:** IllegalArgumentException

- if

dataType

is not
one of the supported data types

---

#### Constructor Detail

PixelInterleavedSampleModel

```java
public PixelInterleavedSampleModel​(int dataType,
int w,
int h,
int pixelStride,
int scanlineStride,
int[] bandOffsets)
```

Constructs a PixelInterleavedSampleModel with the specified parameters.
The number of bands will be given by the length of the bandOffsets
array.

**Parameters:** dataType

- The data type for storing samples.
**Parameters:** w

- The width (in pixels) of the region of
image data described.
**Parameters:** h

- The height (in pixels) of the region of
image data described.
**Parameters:** pixelStride

- The pixel stride of the image data.
**Parameters:** scanlineStride

- The line stride of the image data.
**Parameters:** bandOffsets

- The offsets of all bands.
**Throws:** IllegalArgumentException

- if

w

or

h

is not greater than 0
**Throws:** IllegalArgumentException

- if any offset between bands is
greater than the scanline stride
**Throws:** IllegalArgumentException

- if the product of

pixelStride

and

w

is greater
than

scanlineStride
**Throws:** IllegalArgumentException

- if

pixelStride

is
less than any offset between bands
**Throws:** IllegalArgumentException

- if

dataType

is not
one of the supported data types

---

#### PixelInterleavedSampleModel

public PixelInterleavedSampleModel​(int dataType,
int w,
int h,
int pixelStride,
int scanlineStride,
int[] bandOffsets)

Constructs a PixelInterleavedSampleModel with the specified parameters.
The number of bands will be given by the length of the bandOffsets
array.

Method Detail

- createCompatibleSampleModel

```java
public
SampleModel
createCompatibleSampleModel​(int w,
int h)
```

Creates a new PixelInterleavedSampleModel with the specified
width and height. The new PixelInterleavedSampleModel will have the
same number of bands, storage data type, and pixel stride
as this PixelInterleavedSampleModel. The band offsets may be
compressed such that the minimum of all of the band offsets is zero.

**Overrides:** createCompatibleSampleModel

in class

ComponentSampleModel
**Parameters:** w

- the width of the resulting

SampleModel
**Parameters:** h

- the height of the resulting

SampleModel
**Returns:** a new

SampleModel

with the specified width
and height.
**Throws:** IllegalArgumentException

- if

w

or

h

is not greater than 0

- createSubsetSampleModel

```java
public
SampleModel
createSubsetSampleModel​(int[] bands)
```

Creates a new PixelInterleavedSampleModel with a subset of the
bands of this PixelInterleavedSampleModel. The new
PixelInterleavedSampleModel can be used with any DataBuffer that the
existing PixelInterleavedSampleModel can be used with. The new
PixelInterleavedSampleModel/DataBuffer combination will represent
an image with a subset of the bands of the original
PixelInterleavedSampleModel/DataBuffer combination.

**Overrides:** createSubsetSampleModel

in class

ComponentSampleModel
**Parameters:** bands

- a subset of bands from this

ComponentSampleModel
**Returns:** a

ComponentSampleModel

created with a subset
of bands from this

ComponentSampleModel

.

---

#### Method Detail

createCompatibleSampleModel

```java
public
SampleModel
createCompatibleSampleModel​(int w,
int h)
```

Creates a new PixelInterleavedSampleModel with the specified
width and height. The new PixelInterleavedSampleModel will have the
same number of bands, storage data type, and pixel stride
as this PixelInterleavedSampleModel. The band offsets may be
compressed such that the minimum of all of the band offsets is zero.

**Overrides:** createCompatibleSampleModel

in class

ComponentSampleModel
**Parameters:** w

- the width of the resulting

SampleModel
**Parameters:** h

- the height of the resulting

SampleModel
**Returns:** a new

SampleModel

with the specified width
and height.
**Throws:** IllegalArgumentException

- if

w

or

h

is not greater than 0

---

#### createCompatibleSampleModel

public

SampleModel

createCompatibleSampleModel​(int w,
int h)

Creates a new PixelInterleavedSampleModel with the specified
width and height. The new PixelInterleavedSampleModel will have the
same number of bands, storage data type, and pixel stride
as this PixelInterleavedSampleModel. The band offsets may be
compressed such that the minimum of all of the band offsets is zero.

createSubsetSampleModel

```java
public
SampleModel
createSubsetSampleModel​(int[] bands)
```

Creates a new PixelInterleavedSampleModel with a subset of the
bands of this PixelInterleavedSampleModel. The new
PixelInterleavedSampleModel can be used with any DataBuffer that the
existing PixelInterleavedSampleModel can be used with. The new
PixelInterleavedSampleModel/DataBuffer combination will represent
an image with a subset of the bands of the original
PixelInterleavedSampleModel/DataBuffer combination.

**Overrides:** createSubsetSampleModel

in class

ComponentSampleModel
**Parameters:** bands

- a subset of bands from this

ComponentSampleModel
**Returns:** a

ComponentSampleModel

created with a subset
of bands from this

ComponentSampleModel

.

---

#### createSubsetSampleModel

public

SampleModel

createSubsetSampleModel​(int[] bands)

Creates a new PixelInterleavedSampleModel with a subset of the
bands of this PixelInterleavedSampleModel. The new
PixelInterleavedSampleModel can be used with any DataBuffer that the
existing PixelInterleavedSampleModel can be used with. The new
PixelInterleavedSampleModel/DataBuffer combination will represent
an image with a subset of the bands of the original
PixelInterleavedSampleModel/DataBuffer combination.

---

