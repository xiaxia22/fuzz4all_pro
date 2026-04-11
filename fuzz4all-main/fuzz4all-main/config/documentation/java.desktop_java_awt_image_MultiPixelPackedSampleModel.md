# Class MultiPixelPackedSampleModel

**Source:** `java.desktop\java\awt\image\MultiPixelPackedSampleModel.html`

### Class Description

```java
public class
MultiPixelPackedSampleModel

extends
SampleModel
```

The

MultiPixelPackedSampleModel

class represents
one-banded images and can pack multiple one-sample
pixels into one data element. Pixels are not allowed to span data elements.
The data type can be DataBuffer.TYPE_BYTE, DataBuffer.TYPE_USHORT,
or DataBuffer.TYPE_INT. Each pixel must be a power of 2 number of bits
and a power of 2 number of pixels must fit exactly in one data element.
Pixel bit stride is equal to the number of bits per pixel. Scanline
stride is in data elements and the last several data elements might be
padded with unused pixels. Data bit offset is the offset in bits from
the beginning of the

DataBuffer

to the first pixel and must be
a multiple of pixel bit stride.

The following code illustrates extracting the bits for pixel

x, y

from

DataBuffer data

and storing the pixel data in data elements of type

dataType

:

```java
int dataElementSize = DataBuffer.getDataTypeSize(dataType);
int bitnum = dataBitOffset + x*pixelBitStride;
int element = data.getElem(y*scanlineStride + bitnum/dataElementSize);
int shift = dataElementSize - (bitnum & (dataElementSize-1))
- pixelBitStride;
int pixel = (element >> shift) & ((1 << pixelBitStride) - 1);
```

---

### Field Details

*No entries found.*

### Constructor Details

#### public MultiPixelPackedSampleModel​(int dataType,
int w,
int h,
int numberOfBits)

Constructs a

MultiPixelPackedSampleModel

with the
specified data type, width, height and number of bits per pixel.

**Parameters:**
- dataType

- the data type for storing samples
- w

- the width, in pixels, of the region of
image data described
- h

- the height, in pixels, of the region of
image data described
- numberOfBits

- the number of bits per pixel

**Throws:**
- IllegalArgumentException

- if

dataType

is not
either

DataBuffer.TYPE_BYTE

,

DataBuffer.TYPE_USHORT

, or

DataBuffer.TYPE_INT

---

#### public MultiPixelPackedSampleModel​(int dataType,
int w,
int h,
int numberOfBits,
int scanlineStride,
int dataBitOffset)

Constructs a

MultiPixelPackedSampleModel

with
specified data type, width, height, number of bits per pixel,
scanline stride and data bit offset.

**Parameters:**
- dataType

- the data type for storing samples
- w

- the width, in pixels, of the region of
image data described
- h

- the height, in pixels, of the region of
image data described
- numberOfBits

- the number of bits per pixel
- scanlineStride

- the line stride of the image data
- dataBitOffset

- the data bit offset for the region of image
data described

**Throws:**
- RasterFormatException

- if the number of bits per pixel
is not a power of 2 or if a power of 2 number of
pixels do not fit in one data element.
- IllegalArgumentException

- if

w

or

h

is not greater than 0
- IllegalArgumentException

- if

dataType

is not
either

DataBuffer.TYPE_BYTE

,

DataBuffer.TYPE_USHORT

, or

DataBuffer.TYPE_INT

---

### Method Details

#### public
SampleModel
createCompatibleSampleModel​(int w,
int h)

Creates a new

MultiPixelPackedSampleModel

with the
specified width and height. The new

MultiPixelPackedSampleModel

has the
same storage data type and number of bits per pixel as this

MultiPixelPackedSampleModel

.

**Specified by:**
- createCompatibleSampleModel

in class

SampleModel

**Parameters:**
- w

- the specified width
- h

- the specified height

**Returns:**
- a

SampleModel

with the specified width and height
and with the same storage data type and number of bits per pixel
as this

MultiPixelPackedSampleModel

.

**Throws:**
- IllegalArgumentException

- if

w

or

h

is not greater than 0

---

#### public
DataBuffer
createDataBuffer()

Creates a

DataBuffer

that corresponds to this

MultiPixelPackedSampleModel

. The

DataBuffer

object's data type and size
is consistent with this

MultiPixelPackedSampleModel

.
The

DataBuffer

has a single bank.

**Specified by:**
- createDataBuffer

in class

SampleModel

**Returns:**
- a

DataBuffer

with the same data type and
size as this

MultiPixelPackedSampleModel

.

---

#### public int getNumDataElements()

Returns the number of data elements needed to transfer one pixel
via the

getDataElements(int, int, java.lang.Object, java.awt.image.DataBuffer)

and

setDataElements(int, int, java.lang.Object, java.awt.image.DataBuffer)

methods. For a

MultiPixelPackedSampleModel

, this is
one.

**Specified by:**
- getNumDataElements

in class

SampleModel

**Returns:**
- the number of data elements.

**See Also:**
- SampleModel.getDataElements(int, int, Object, DataBuffer)

,

SampleModel.getDataElements(int, int, int, int, Object, DataBuffer)

,

SampleModel.setDataElements(int, int, Object, DataBuffer)

,

SampleModel.setDataElements(int, int, int, int, Object, DataBuffer)

,

SampleModel.getTransferType()

---

#### public int[] getSampleSize()

Returns the number of bits per sample for all bands.

**Specified by:**
- getSampleSize

in class

SampleModel

**Returns:**
- the number of bits per sample.

---

#### public int getSampleSize​(int band)

Returns the number of bits per sample for the specified band.

**Specified by:**
- getSampleSize

in class

SampleModel

**Parameters:**
- band

- the specified band

**Returns:**
- the number of bits per sample for the specified band.

---

#### public int getOffset​(int x,
int y)

Returns the offset of pixel (x, y) in data array elements.

**Parameters:**
- x

- the X coordinate of the specified pixel
- y

- the Y coordinate of the specified pixel

**Returns:**
- the offset of the specified pixel.

---

#### public int getBitOffset​(int x)

Returns the offset, in bits, into the data element in which it is
stored for the

x

th pixel of a scanline.
This offset is the same for all scanlines.

**Parameters:**
- x

- the specified pixel

**Returns:**
- the bit offset of the specified pixel.

---

#### public int getScanlineStride()

Returns the scanline stride.

**Returns:**
- the scanline stride of this

MultiPixelPackedSampleModel

.

---

#### public int getPixelBitStride()

Returns the pixel bit stride in bits. This value is the same as
the number of bits per pixel.

**Returns:**
- the

pixelBitStride

of this

MultiPixelPackedSampleModel

.

---

#### public int getDataBitOffset()

Returns the data bit offset in bits.

**Returns:**
- the

dataBitOffset

of this

MultiPixelPackedSampleModel

.

---

#### public int getTransferType()

Returns the TransferType used to transfer pixels by way of the

getDataElements

and

setDataElements

methods. The TransferType might or might not be the same as the
storage DataType. The TransferType is one of
DataBuffer.TYPE_BYTE, DataBuffer.TYPE_USHORT,
or DataBuffer.TYPE_INT.

**Overrides:**
- getTransferType

in class

SampleModel

**Returns:**
- the transfertype.

**See Also:**
- SampleModel.getDataElements(int, int, Object, DataBuffer)

,

SampleModel.getDataElements(int, int, int, int, Object, DataBuffer)

,

SampleModel.setDataElements(int, int, Object, DataBuffer)

,

SampleModel.setDataElements(int, int, int, int, Object, DataBuffer)

,

SampleModel.getNumDataElements()

,

DataBuffer

---

#### public
SampleModel
createSubsetSampleModel​(int[] bands)

Creates a new

MultiPixelPackedSampleModel

with a
subset of the bands of this

MultiPixelPackedSampleModel

. Since a

MultiPixelPackedSampleModel

only has one band, the
bands argument must have a length of one and indicate the zeroth
band.

**Specified by:**
- createSubsetSampleModel

in class

SampleModel

**Parameters:**
- bands

- the specified bands

**Returns:**
- a new

SampleModel

with a subset of bands of
this

MultiPixelPackedSampleModel

.

**Throws:**
- RasterFormatException

- if the number of bands requested
is not one.
- IllegalArgumentException

- if

w

or

h

is not greater than 0

---

#### public int getSample​(int x,
int y,
int b,

DataBuffer
data)

Returns as

int

the sample in a specified band for the
pixel located at (x, y). An

ArrayIndexOutOfBoundsException

is thrown if the
coordinates are not in bounds.

**Specified by:**
- getSample

in class

SampleModel

**Parameters:**
- x

- the X coordinate of the specified pixel
- y

- the Y coordinate of the specified pixel
- b

- the band to return, which is assumed to be 0
- data

- the

DataBuffer

containing the image
data

**Returns:**
- the specified band containing the sample of the specified
pixel.

**Throws:**
- ArrayIndexOutOfBoundsException

- if the specified
coordinates are not in bounds.

**See Also:**
- setSample(int, int, int, int, DataBuffer)

---

#### public void setSample​(int x,
int y,
int b,
int s,

DataBuffer
data)

Sets a sample in the specified band for the pixel located at
(x, y) in the

DataBuffer

using an

int

for input.
An

ArrayIndexOutOfBoundsException

is thrown if the
coordinates are not in bounds.

**Specified by:**
- setSample

in class

SampleModel

**Parameters:**
- x

- the X coordinate of the specified pixel
- y

- the Y coordinate of the specified pixel
- b

- the band to return, which is assumed to be 0
- s

- the input sample as an

int
- data

- the

DataBuffer

where image data is stored

**Throws:**
- ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds.

**See Also:**
- getSample(int, int, int, DataBuffer)

---

#### public
Object
getDataElements​(int x,
int y,

Object
obj,

DataBuffer
data)

Returns data for a single pixel in a primitive array of type
TransferType. For a

MultiPixelPackedSampleModel

,
the array has one element, and the type is the smallest of
DataBuffer.TYPE_BYTE, DataBuffer.TYPE_USHORT, or DataBuffer.TYPE_INT
that can hold a single pixel. Generally,

obj

should be passed in as

null

, so that the

Object

is created automatically and is the
correct primitive data type.

The following code illustrates transferring data for one pixel from

DataBuffer db1

, whose storage layout is
described by

MultiPixelPackedSampleModel

mppsm1

, to

DataBuffer db2

,
whose storage layout is described by

MultiPixelPackedSampleModel mppsm2

.
The transfer is generally more efficient than using

getPixel

or

setPixel

.

```java
MultiPixelPackedSampleModel mppsm1, mppsm2;
DataBufferInt db1, db2;
mppsm2.setDataElements(x, y, mppsm1.getDataElements(x, y, null,
db1), db2);
```

Using

getDataElements

or

setDataElements

to transfer between two

DataBuffer/SampleModel

pairs
is legitimate if the

SampleModels

have the same number
of bands, corresponding bands have the same number of
bits per sample, and the TransferTypes are the same.

If

obj

is not

null

, it should be a
primitive array of type TransferType. Otherwise, a

ClassCastException

is thrown. An

ArrayIndexOutOfBoundsException

is thrown if the
coordinates are not in bounds, or if

obj

is not

null

and is not large enough to hold the pixel data.

**Specified by:**
- getDataElements

in class

SampleModel

**Parameters:**
- x

- the X coordinate of the specified pixel
- y

- the Y coordinate of the specified pixel
- obj

- a primitive array in which to return the pixel data or

null

.
- data

- the

DataBuffer

containing the image data.

**Returns:**
- an

Object

containing data for the specified
pixel.

**Throws:**
- ClassCastException

- if

obj

is not a
primitive array of type TransferType or is not

null
- ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if

obj

is not

null

or
not large enough to hold the pixel data

**See Also:**
- setDataElements(int, int, Object, DataBuffer)

---

#### public int[] getPixel​(int x,
int y,
int[] iArray,

DataBuffer
data)

Returns the specified single band pixel in the first element
of an

int

array.

ArrayIndexOutOfBoundsException

is thrown if the
coordinates are not in bounds.

**Overrides:**
- getPixel

in class

SampleModel

**Parameters:**
- x

- the X coordinate of the specified pixel
- y

- the Y coordinate of the specified pixel
- iArray

- the array containing the pixel to be returned or

null
- data

- the

DataBuffer

where image data is stored

**Returns:**
- an array containing the specified pixel.

**Throws:**
- ArrayIndexOutOfBoundsException

- if the coordinates
are not in bounds

**See Also:**
- setPixel(int, int, int[], DataBuffer)

---

#### public void setDataElements​(int x,
int y,

Object
obj,

DataBuffer
data)

Sets the data for a single pixel in the specified

DataBuffer

from a primitive array of type
TransferType. For a

MultiPixelPackedSampleModel

,
only the first element of the array holds valid data,
and the type must be the smallest of
DataBuffer.TYPE_BYTE, DataBuffer.TYPE_USHORT, or DataBuffer.TYPE_INT
that can hold a single pixel.

The following code illustrates transferring data for one pixel from

DataBuffer db1

, whose storage layout is
described by

MultiPixelPackedSampleModel

mppsm1

, to

DataBuffer db2

,
whose storage layout is described by

MultiPixelPackedSampleModel mppsm2

.
The transfer is generally more efficient than using

getPixel

or

setPixel

.

```java
MultiPixelPackedSampleModel mppsm1, mppsm2;
DataBufferInt db1, db2;
mppsm2.setDataElements(x, y, mppsm1.getDataElements(x, y, null,
db1), db2);
```

Using

getDataElements

or

setDataElements

to
transfer between two

DataBuffer/SampleModel

pairs is
legitimate if the

SampleModel

objects have
the same number of bands, corresponding bands have the same number of
bits per sample, and the TransferTypes are the same.

obj

must be a primitive array of type TransferType.
Otherwise, a

ClassCastException

is thrown. An

ArrayIndexOutOfBoundsException

is thrown if the
coordinates are not in bounds, or if

obj

is not large
enough to hold the pixel data.

**Specified by:**
- setDataElements

in class

SampleModel

**Parameters:**
- x

- the X coordinate of the pixel location
- y

- the Y coordinate of the pixel location
- obj

- a primitive array containing pixel data
- data

- the

DataBuffer

containing the image data

**See Also:**
- getDataElements(int, int, Object, DataBuffer)

---

#### public void setPixel​(int x,
int y,
int[] iArray,

DataBuffer
data)

Sets a pixel in the

DataBuffer

using an

int

array for input.

ArrayIndexOutOfBoundsException

is thrown if
the coordinates are not in bounds.

**Overrides:**
- setPixel

in class

SampleModel

**Parameters:**
- x

- the X coordinate of the pixel location
- y

- the Y coordinate of the pixel location
- iArray

- the input pixel in an

int

array
- data

- the

DataBuffer

containing the image data

**See Also:**
- getPixel(int, int, int[], DataBuffer)

---

### Additional Sections

#### Class MultiPixelPackedSampleModel

java.lang.Object

- java.awt.image.SampleModel
- - java.awt.image.MultiPixelPackedSampleModel

java.awt.image.SampleModel

- java.awt.image.MultiPixelPackedSampleModel

java.awt.image.MultiPixelPackedSampleModel

```java
public class
MultiPixelPackedSampleModel

extends
SampleModel
```

The

MultiPixelPackedSampleModel

class represents
one-banded images and can pack multiple one-sample
pixels into one data element. Pixels are not allowed to span data elements.
The data type can be DataBuffer.TYPE_BYTE, DataBuffer.TYPE_USHORT,
or DataBuffer.TYPE_INT. Each pixel must be a power of 2 number of bits
and a power of 2 number of pixels must fit exactly in one data element.
Pixel bit stride is equal to the number of bits per pixel. Scanline
stride is in data elements and the last several data elements might be
padded with unused pixels. Data bit offset is the offset in bits from
the beginning of the

DataBuffer

to the first pixel and must be
a multiple of pixel bit stride.

The following code illustrates extracting the bits for pixel

x, y

from

DataBuffer data

and storing the pixel data in data elements of type

dataType

:

```java
int dataElementSize = DataBuffer.getDataTypeSize(dataType);
int bitnum = dataBitOffset + x*pixelBitStride;
int element = data.getElem(y*scanlineStride + bitnum/dataElementSize);
int shift = dataElementSize - (bitnum & (dataElementSize-1))
- pixelBitStride;
int pixel = (element >> shift) & ((1 << pixelBitStride) - 1);
```

public class

MultiPixelPackedSampleModel

extends

SampleModel

The

MultiPixelPackedSampleModel

class represents
one-banded images and can pack multiple one-sample
pixels into one data element. Pixels are not allowed to span data elements.
The data type can be DataBuffer.TYPE_BYTE, DataBuffer.TYPE_USHORT,
or DataBuffer.TYPE_INT. Each pixel must be a power of 2 number of bits
and a power of 2 number of pixels must fit exactly in one data element.
Pixel bit stride is equal to the number of bits per pixel. Scanline
stride is in data elements and the last several data elements might be
padded with unused pixels. Data bit offset is the offset in bits from
the beginning of the

DataBuffer

to the first pixel and must be
a multiple of pixel bit stride.

The following code illustrates extracting the bits for pixel

x, y

from

DataBuffer data

and storing the pixel data in data elements of type

dataType

:

```java
int dataElementSize = DataBuffer.getDataTypeSize(dataType);
int bitnum = dataBitOffset + x*pixelBitStride;
int element = data.getElem(y*scanlineStride + bitnum/dataElementSize);
int shift = dataElementSize - (bitnum & (dataElementSize-1))
- pixelBitStride;
int pixel = (element >> shift) & ((1 << pixelBitStride) - 1);
```

The following code illustrates extracting the bits for pixel

x, y

from

DataBuffer data

and storing the pixel data in data elements of type

dataType

:

```java
int dataElementSize = DataBuffer.getDataTypeSize(dataType);
int bitnum = dataBitOffset + x*pixelBitStride;
int element = data.getElem(y*scanlineStride + bitnum/dataElementSize);
int shift = dataElementSize - (bitnum & (dataElementSize-1))
- pixelBitStride;
int pixel = (element >> shift) & ((1 << pixelBitStride) - 1);
```

int dataElementSize = DataBuffer.getDataTypeSize(dataType);
int bitnum = dataBitOffset + x*pixelBitStride;
int element = data.getElem(y*scanlineStride + bitnum/dataElementSize);
int shift = dataElementSize - (bitnum & (dataElementSize-1))
- pixelBitStride;
int pixel = (element >> shift) & ((1 << pixelBitStride) - 1);

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.awt.image.

SampleModel

dataType

,

height

,

numBands

,

width

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MultiPixelPackedSampleModel

​(int dataType,
int w,
int h,
int numberOfBits)

Constructs a

MultiPixelPackedSampleModel

with the
specified data type, width, height and number of bits per pixel.

MultiPixelPackedSampleModel

​(int dataType,
int w,
int h,
int numberOfBits,
int scanlineStride,
int dataBitOffset)

Constructs a

MultiPixelPackedSampleModel

with
specified data type, width, height, number of bits per pixel,
scanline stride and data bit offset.

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

Creates a new

MultiPixelPackedSampleModel

with the
specified width and height.

DataBuffer

createDataBuffer

()

Creates a

DataBuffer

that corresponds to this

MultiPixelPackedSampleModel

.

SampleModel

createSubsetSampleModel

​(int[] bands)

Creates a new

MultiPixelPackedSampleModel

with a
subset of the bands of this

MultiPixelPackedSampleModel

.

int

getBitOffset

​(int x)

Returns the offset, in bits, into the data element in which it is
stored for the

x

th pixel of a scanline.

int

getDataBitOffset

()

Returns the data bit offset in bits.

Object

getDataElements

​(int x,
int y,

Object

obj,

DataBuffer

data)

Returns data for a single pixel in a primitive array of type
TransferType.

int

getNumDataElements

()

Returns the number of data elements needed to transfer one pixel
via the

getDataElements(int, int, java.lang.Object, java.awt.image.DataBuffer)

and

setDataElements(int, int, java.lang.Object, java.awt.image.DataBuffer)

methods.

int

getOffset

​(int x,
int y)

Returns the offset of pixel (x, y) in data array elements.

int[]

getPixel

​(int x,
int y,
int[] iArray,

DataBuffer

data)

Returns the specified single band pixel in the first element
of an

int

array.

int

getPixelBitStride

()

Returns the pixel bit stride in bits.

int

getSample

​(int x,
int y,
int b,

DataBuffer

data)

Returns as

int

the sample in a specified band for the
pixel located at (x, y).

int[]

getSampleSize

()

Returns the number of bits per sample for all bands.

int

getSampleSize

​(int band)

Returns the number of bits per sample for the specified band.

int

getScanlineStride

()

Returns the scanline stride.

int

getTransferType

()

Returns the TransferType used to transfer pixels by way of the

getDataElements

and

setDataElements

methods.

void

setDataElements

​(int x,
int y,

Object

obj,

DataBuffer

data)

Sets the data for a single pixel in the specified

DataBuffer

from a primitive array of type
TransferType.

void

setPixel

​(int x,
int y,
int[] iArray,

DataBuffer

data)

Sets a pixel in the

DataBuffer

using an

int

array for input.

void

setSample

​(int x,
int y,
int b,
int s,

DataBuffer

data)

Sets a sample in the specified band for the pixel located at
(x, y) in the

DataBuffer

using an

int

for input.

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

getPixels

,

getSampleDouble

,

getSampleFloat

,

getSamples

,

getSamples

,

getSamples

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

setPixels

,

setSample

,

setSample

,

setSamples

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

SampleModel

dataType

,

height

,

numBands

,

width

---

#### Field Summary

Fields declared in class java.awt.image.

SampleModel

dataType

,

height

,

numBands

,

width

---

#### Fields declared in class java.awt.image. SampleModel

Constructor Summary

Constructors

Constructor

Description

MultiPixelPackedSampleModel

​(int dataType,
int w,
int h,
int numberOfBits)

Constructs a

MultiPixelPackedSampleModel

with the
specified data type, width, height and number of bits per pixel.

MultiPixelPackedSampleModel

​(int dataType,
int w,
int h,
int numberOfBits,
int scanlineStride,
int dataBitOffset)

Constructs a

MultiPixelPackedSampleModel

with
specified data type, width, height, number of bits per pixel,
scanline stride and data bit offset.

---

#### Constructor Summary

Constructs a

MultiPixelPackedSampleModel

with the
specified data type, width, height and number of bits per pixel.

Constructs a

MultiPixelPackedSampleModel

with
specified data type, width, height, number of bits per pixel,
scanline stride and data bit offset.

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

Creates a new

MultiPixelPackedSampleModel

with the
specified width and height.

DataBuffer

createDataBuffer

()

Creates a

DataBuffer

that corresponds to this

MultiPixelPackedSampleModel

.

SampleModel

createSubsetSampleModel

​(int[] bands)

Creates a new

MultiPixelPackedSampleModel

with a
subset of the bands of this

MultiPixelPackedSampleModel

.

int

getBitOffset

​(int x)

Returns the offset, in bits, into the data element in which it is
stored for the

x

th pixel of a scanline.

int

getDataBitOffset

()

Returns the data bit offset in bits.

Object

getDataElements

​(int x,
int y,

Object

obj,

DataBuffer

data)

Returns data for a single pixel in a primitive array of type
TransferType.

int

getNumDataElements

()

Returns the number of data elements needed to transfer one pixel
via the

getDataElements(int, int, java.lang.Object, java.awt.image.DataBuffer)

and

setDataElements(int, int, java.lang.Object, java.awt.image.DataBuffer)

methods.

int

getOffset

​(int x,
int y)

Returns the offset of pixel (x, y) in data array elements.

int[]

getPixel

​(int x,
int y,
int[] iArray,

DataBuffer

data)

Returns the specified single band pixel in the first element
of an

int

array.

int

getPixelBitStride

()

Returns the pixel bit stride in bits.

int

getSample

​(int x,
int y,
int b,

DataBuffer

data)

Returns as

int

the sample in a specified band for the
pixel located at (x, y).

int[]

getSampleSize

()

Returns the number of bits per sample for all bands.

int

getSampleSize

​(int band)

Returns the number of bits per sample for the specified band.

int

getScanlineStride

()

Returns the scanline stride.

int

getTransferType

()

Returns the TransferType used to transfer pixels by way of the

getDataElements

and

setDataElements

methods.

void

setDataElements

​(int x,
int y,

Object

obj,

DataBuffer

data)

Sets the data for a single pixel in the specified

DataBuffer

from a primitive array of type
TransferType.

void

setPixel

​(int x,
int y,
int[] iArray,

DataBuffer

data)

Sets a pixel in the

DataBuffer

using an

int

array for input.

void

setSample

​(int x,
int y,
int b,
int s,

DataBuffer

data)

Sets a sample in the specified band for the pixel located at
(x, y) in the

DataBuffer

using an

int

for input.

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

getPixels

,

getSampleDouble

,

getSampleFloat

,

getSamples

,

getSamples

,

getSamples

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

setPixels

,

setSample

,

setSample

,

setSamples

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

Creates a new

MultiPixelPackedSampleModel

with the
specified width and height.

Creates a

DataBuffer

that corresponds to this

MultiPixelPackedSampleModel

.

Creates a new

MultiPixelPackedSampleModel

with a
subset of the bands of this

MultiPixelPackedSampleModel

.

Returns the offset, in bits, into the data element in which it is
stored for the

x

th pixel of a scanline.

Returns the data bit offset in bits.

Returns data for a single pixel in a primitive array of type
TransferType.

Returns the number of data elements needed to transfer one pixel
via the

getDataElements(int, int, java.lang.Object, java.awt.image.DataBuffer)

and

setDataElements(int, int, java.lang.Object, java.awt.image.DataBuffer)

methods.

Returns the offset of pixel (x, y) in data array elements.

Returns the specified single band pixel in the first element
of an

int

array.

Returns the pixel bit stride in bits.

Returns as

int

the sample in a specified band for the
pixel located at (x, y).

Returns the number of bits per sample for all bands.

Returns the number of bits per sample for the specified band.

Returns the scanline stride.

Returns the TransferType used to transfer pixels by way of the

getDataElements

and

setDataElements

methods.

Sets the data for a single pixel in the specified

DataBuffer

from a primitive array of type
TransferType.

Sets a pixel in the

DataBuffer

using an

int

array for input.

Sets a sample in the specified band for the pixel located at
(x, y) in the

DataBuffer

using an

int

for input.

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

getPixels

,

getSampleDouble

,

getSampleFloat

,

getSamples

,

getSamples

,

getSamples

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

setPixels

,

setSample

,

setSample

,

setSamples

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

- MultiPixelPackedSampleModel

```java
public MultiPixelPackedSampleModel​(int dataType,
int w,
int h,
int numberOfBits)
```

Constructs a

MultiPixelPackedSampleModel

with the
specified data type, width, height and number of bits per pixel.

**Parameters:** dataType

- the data type for storing samples
**Parameters:** w

- the width, in pixels, of the region of
image data described
**Parameters:** h

- the height, in pixels, of the region of
image data described
**Parameters:** numberOfBits

- the number of bits per pixel
**Throws:** IllegalArgumentException

- if

dataType

is not
either

DataBuffer.TYPE_BYTE

,

DataBuffer.TYPE_USHORT

, or

DataBuffer.TYPE_INT

- MultiPixelPackedSampleModel

```java
public MultiPixelPackedSampleModel​(int dataType,
int w,
int h,
int numberOfBits,
int scanlineStride,
int dataBitOffset)
```

Constructs a

MultiPixelPackedSampleModel

with
specified data type, width, height, number of bits per pixel,
scanline stride and data bit offset.

**Parameters:** dataType

- the data type for storing samples
**Parameters:** w

- the width, in pixels, of the region of
image data described
**Parameters:** h

- the height, in pixels, of the region of
image data described
**Parameters:** numberOfBits

- the number of bits per pixel
**Parameters:** scanlineStride

- the line stride of the image data
**Parameters:** dataBitOffset

- the data bit offset for the region of image
data described
**Throws:** RasterFormatException

- if the number of bits per pixel
is not a power of 2 or if a power of 2 number of
pixels do not fit in one data element.
**Throws:** IllegalArgumentException

- if

w

or

h

is not greater than 0
**Throws:** IllegalArgumentException

- if

dataType

is not
either

DataBuffer.TYPE_BYTE

,

DataBuffer.TYPE_USHORT

, or

DataBuffer.TYPE_INT

============ METHOD DETAIL ==========

- Method Detail

- createCompatibleSampleModel

```java
public
SampleModel
createCompatibleSampleModel​(int w,
int h)
```

Creates a new

MultiPixelPackedSampleModel

with the
specified width and height. The new

MultiPixelPackedSampleModel

has the
same storage data type and number of bits per pixel as this

MultiPixelPackedSampleModel

.

**Specified by:** createCompatibleSampleModel

in class

SampleModel
**Parameters:** w

- the specified width
**Parameters:** h

- the specified height
**Returns:** a

SampleModel

with the specified width and height
and with the same storage data type and number of bits per pixel
as this

MultiPixelPackedSampleModel

.
**Throws:** IllegalArgumentException

- if

w

or

h

is not greater than 0

- createDataBuffer

```java
public
DataBuffer
createDataBuffer()
```

Creates a

DataBuffer

that corresponds to this

MultiPixelPackedSampleModel

. The

DataBuffer

object's data type and size
is consistent with this

MultiPixelPackedSampleModel

.
The

DataBuffer

has a single bank.

**Specified by:** createDataBuffer

in class

SampleModel
**Returns:** a

DataBuffer

with the same data type and
size as this

MultiPixelPackedSampleModel

.

- getNumDataElements

```java
public int getNumDataElements()
```

Returns the number of data elements needed to transfer one pixel
via the

getDataElements(int, int, java.lang.Object, java.awt.image.DataBuffer)

and

setDataElements(int, int, java.lang.Object, java.awt.image.DataBuffer)

methods. For a

MultiPixelPackedSampleModel

, this is
one.

**Specified by:** getNumDataElements

in class

SampleModel
**Returns:** the number of data elements.
**See Also:** SampleModel.getDataElements(int, int, Object, DataBuffer)

,

SampleModel.getDataElements(int, int, int, int, Object, DataBuffer)

,

SampleModel.setDataElements(int, int, Object, DataBuffer)

,

SampleModel.setDataElements(int, int, int, int, Object, DataBuffer)

,

SampleModel.getTransferType()

- getSampleSize

```java
public int[] getSampleSize()
```

Returns the number of bits per sample for all bands.

**Specified by:** getSampleSize

in class

SampleModel
**Returns:** the number of bits per sample.

- getSampleSize

```java
public int getSampleSize​(int band)
```

Returns the number of bits per sample for the specified band.

**Specified by:** getSampleSize

in class

SampleModel
**Parameters:** band

- the specified band
**Returns:** the number of bits per sample for the specified band.

- getOffset

```java
public int getOffset​(int x,
int y)
```

Returns the offset of pixel (x, y) in data array elements.

**Parameters:** x

- the X coordinate of the specified pixel
**Parameters:** y

- the Y coordinate of the specified pixel
**Returns:** the offset of the specified pixel.

- getBitOffset

```java
public int getBitOffset​(int x)
```

Returns the offset, in bits, into the data element in which it is
stored for the

x

th pixel of a scanline.
This offset is the same for all scanlines.

**Parameters:** x

- the specified pixel
**Returns:** the bit offset of the specified pixel.

- getScanlineStride

```java
public int getScanlineStride()
```

Returns the scanline stride.

**Returns:** the scanline stride of this

MultiPixelPackedSampleModel

.

- getPixelBitStride

```java
public int getPixelBitStride()
```

Returns the pixel bit stride in bits. This value is the same as
the number of bits per pixel.

**Returns:** the

pixelBitStride

of this

MultiPixelPackedSampleModel

.

- getDataBitOffset

```java
public int getDataBitOffset()
```

Returns the data bit offset in bits.

**Returns:** the

dataBitOffset

of this

MultiPixelPackedSampleModel

.

- getTransferType

```java
public int getTransferType()
```

Returns the TransferType used to transfer pixels by way of the

getDataElements

and

setDataElements

methods. The TransferType might or might not be the same as the
storage DataType. The TransferType is one of
DataBuffer.TYPE_BYTE, DataBuffer.TYPE_USHORT,
or DataBuffer.TYPE_INT.

**Overrides:** getTransferType

in class

SampleModel
**Returns:** the transfertype.
**See Also:** SampleModel.getDataElements(int, int, Object, DataBuffer)

,

SampleModel.getDataElements(int, int, int, int, Object, DataBuffer)

,

SampleModel.setDataElements(int, int, Object, DataBuffer)

,

SampleModel.setDataElements(int, int, int, int, Object, DataBuffer)

,

SampleModel.getNumDataElements()

,

DataBuffer

- createSubsetSampleModel

```java
public
SampleModel
createSubsetSampleModel​(int[] bands)
```

Creates a new

MultiPixelPackedSampleModel

with a
subset of the bands of this

MultiPixelPackedSampleModel

. Since a

MultiPixelPackedSampleModel

only has one band, the
bands argument must have a length of one and indicate the zeroth
band.

**Specified by:** createSubsetSampleModel

in class

SampleModel
**Parameters:** bands

- the specified bands
**Returns:** a new

SampleModel

with a subset of bands of
this

MultiPixelPackedSampleModel

.
**Throws:** RasterFormatException

- if the number of bands requested
is not one.
**Throws:** IllegalArgumentException

- if

w

or

h

is not greater than 0

- getSample

```java
public int getSample​(int x,
int y,
int b,

DataBuffer
data)
```

Returns as

int

the sample in a specified band for the
pixel located at (x, y). An

ArrayIndexOutOfBoundsException

is thrown if the
coordinates are not in bounds.

**Specified by:** getSample

in class

SampleModel
**Parameters:** x

- the X coordinate of the specified pixel
**Parameters:** y

- the Y coordinate of the specified pixel
**Parameters:** b

- the band to return, which is assumed to be 0
**Parameters:** data

- the

DataBuffer

containing the image
data
**Returns:** the specified band containing the sample of the specified
pixel.
**Throws:** ArrayIndexOutOfBoundsException

- if the specified
coordinates are not in bounds.
**See Also:** setSample(int, int, int, int, DataBuffer)

- setSample

```java
public void setSample​(int x,
int y,
int b,
int s,

DataBuffer
data)
```

Sets a sample in the specified band for the pixel located at
(x, y) in the

DataBuffer

using an

int

for input.
An

ArrayIndexOutOfBoundsException

is thrown if the
coordinates are not in bounds.

**Specified by:** setSample

in class

SampleModel
**Parameters:** x

- the X coordinate of the specified pixel
**Parameters:** y

- the Y coordinate of the specified pixel
**Parameters:** b

- the band to return, which is assumed to be 0
**Parameters:** s

- the input sample as an

int
**Parameters:** data

- the

DataBuffer

where image data is stored
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds.
**See Also:** getSample(int, int, int, DataBuffer)

- getDataElements

```java
public
Object
getDataElements​(int x,
int y,

Object
obj,

DataBuffer
data)
```

Returns data for a single pixel in a primitive array of type
TransferType. For a

MultiPixelPackedSampleModel

,
the array has one element, and the type is the smallest of
DataBuffer.TYPE_BYTE, DataBuffer.TYPE_USHORT, or DataBuffer.TYPE_INT
that can hold a single pixel. Generally,

obj

should be passed in as

null

, so that the

Object

is created automatically and is the
correct primitive data type.

The following code illustrates transferring data for one pixel from

DataBuffer db1

, whose storage layout is
described by

MultiPixelPackedSampleModel

mppsm1

, to

DataBuffer db2

,
whose storage layout is described by

MultiPixelPackedSampleModel mppsm2

.
The transfer is generally more efficient than using

getPixel

or

setPixel

.

```java
MultiPixelPackedSampleModel mppsm1, mppsm2;
DataBufferInt db1, db2;
mppsm2.setDataElements(x, y, mppsm1.getDataElements(x, y, null,
db1), db2);
```

Using

getDataElements

or

setDataElements

to transfer between two

DataBuffer/SampleModel

pairs
is legitimate if the

SampleModels

have the same number
of bands, corresponding bands have the same number of
bits per sample, and the TransferTypes are the same.

If

obj

is not

null

, it should be a
primitive array of type TransferType. Otherwise, a

ClassCastException

is thrown. An

ArrayIndexOutOfBoundsException

is thrown if the
coordinates are not in bounds, or if

obj

is not

null

and is not large enough to hold the pixel data.

**Specified by:** getDataElements

in class

SampleModel
**Parameters:** x

- the X coordinate of the specified pixel
**Parameters:** y

- the Y coordinate of the specified pixel
**Parameters:** obj

- a primitive array in which to return the pixel data or

null

.
**Parameters:** data

- the

DataBuffer

containing the image data.
**Returns:** an

Object

containing data for the specified
pixel.
**Throws:** ClassCastException

- if

obj

is not a
primitive array of type TransferType or is not

null
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if

obj

is not

null

or
not large enough to hold the pixel data
**See Also:** setDataElements(int, int, Object, DataBuffer)

- getPixel

```java
public int[] getPixel​(int x,
int y,
int[] iArray,

DataBuffer
data)
```

Returns the specified single band pixel in the first element
of an

int

array.

ArrayIndexOutOfBoundsException

is thrown if the
coordinates are not in bounds.

**Overrides:** getPixel

in class

SampleModel
**Parameters:** x

- the X coordinate of the specified pixel
**Parameters:** y

- the Y coordinate of the specified pixel
**Parameters:** iArray

- the array containing the pixel to be returned or

null
**Parameters:** data

- the

DataBuffer

where image data is stored
**Returns:** an array containing the specified pixel.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates
are not in bounds
**See Also:** setPixel(int, int, int[], DataBuffer)

- setDataElements

```java
public void setDataElements​(int x,
int y,

Object
obj,

DataBuffer
data)
```

Sets the data for a single pixel in the specified

DataBuffer

from a primitive array of type
TransferType. For a

MultiPixelPackedSampleModel

,
only the first element of the array holds valid data,
and the type must be the smallest of
DataBuffer.TYPE_BYTE, DataBuffer.TYPE_USHORT, or DataBuffer.TYPE_INT
that can hold a single pixel.

The following code illustrates transferring data for one pixel from

DataBuffer db1

, whose storage layout is
described by

MultiPixelPackedSampleModel

mppsm1

, to

DataBuffer db2

,
whose storage layout is described by

MultiPixelPackedSampleModel mppsm2

.
The transfer is generally more efficient than using

getPixel

or

setPixel

.

```java
MultiPixelPackedSampleModel mppsm1, mppsm2;
DataBufferInt db1, db2;
mppsm2.setDataElements(x, y, mppsm1.getDataElements(x, y, null,
db1), db2);
```

Using

getDataElements

or

setDataElements

to
transfer between two

DataBuffer/SampleModel

pairs is
legitimate if the

SampleModel

objects have
the same number of bands, corresponding bands have the same number of
bits per sample, and the TransferTypes are the same.

obj

must be a primitive array of type TransferType.
Otherwise, a

ClassCastException

is thrown. An

ArrayIndexOutOfBoundsException

is thrown if the
coordinates are not in bounds, or if

obj

is not large
enough to hold the pixel data.

**Specified by:** setDataElements

in class

SampleModel
**Parameters:** x

- the X coordinate of the pixel location
**Parameters:** y

- the Y coordinate of the pixel location
**Parameters:** obj

- a primitive array containing pixel data
**Parameters:** data

- the

DataBuffer

containing the image data
**See Also:** getDataElements(int, int, Object, DataBuffer)

- setPixel

```java
public void setPixel​(int x,
int y,
int[] iArray,

DataBuffer
data)
```

Sets a pixel in the

DataBuffer

using an

int

array for input.

ArrayIndexOutOfBoundsException

is thrown if
the coordinates are not in bounds.

**Overrides:** setPixel

in class

SampleModel
**Parameters:** x

- the X coordinate of the pixel location
**Parameters:** y

- the Y coordinate of the pixel location
**Parameters:** iArray

- the input pixel in an

int

array
**Parameters:** data

- the

DataBuffer

containing the image data
**See Also:** getPixel(int, int, int[], DataBuffer)

Constructor Detail

- MultiPixelPackedSampleModel

```java
public MultiPixelPackedSampleModel​(int dataType,
int w,
int h,
int numberOfBits)
```

Constructs a

MultiPixelPackedSampleModel

with the
specified data type, width, height and number of bits per pixel.

**Parameters:** dataType

- the data type for storing samples
**Parameters:** w

- the width, in pixels, of the region of
image data described
**Parameters:** h

- the height, in pixels, of the region of
image data described
**Parameters:** numberOfBits

- the number of bits per pixel
**Throws:** IllegalArgumentException

- if

dataType

is not
either

DataBuffer.TYPE_BYTE

,

DataBuffer.TYPE_USHORT

, or

DataBuffer.TYPE_INT

- MultiPixelPackedSampleModel

```java
public MultiPixelPackedSampleModel​(int dataType,
int w,
int h,
int numberOfBits,
int scanlineStride,
int dataBitOffset)
```

Constructs a

MultiPixelPackedSampleModel

with
specified data type, width, height, number of bits per pixel,
scanline stride and data bit offset.

**Parameters:** dataType

- the data type for storing samples
**Parameters:** w

- the width, in pixels, of the region of
image data described
**Parameters:** h

- the height, in pixels, of the region of
image data described
**Parameters:** numberOfBits

- the number of bits per pixel
**Parameters:** scanlineStride

- the line stride of the image data
**Parameters:** dataBitOffset

- the data bit offset for the region of image
data described
**Throws:** RasterFormatException

- if the number of bits per pixel
is not a power of 2 or if a power of 2 number of
pixels do not fit in one data element.
**Throws:** IllegalArgumentException

- if

w

or

h

is not greater than 0
**Throws:** IllegalArgumentException

- if

dataType

is not
either

DataBuffer.TYPE_BYTE

,

DataBuffer.TYPE_USHORT

, or

DataBuffer.TYPE_INT

---

#### Constructor Detail

MultiPixelPackedSampleModel

```java
public MultiPixelPackedSampleModel​(int dataType,
int w,
int h,
int numberOfBits)
```

Constructs a

MultiPixelPackedSampleModel

with the
specified data type, width, height and number of bits per pixel.

**Parameters:** dataType

- the data type for storing samples
**Parameters:** w

- the width, in pixels, of the region of
image data described
**Parameters:** h

- the height, in pixels, of the region of
image data described
**Parameters:** numberOfBits

- the number of bits per pixel
**Throws:** IllegalArgumentException

- if

dataType

is not
either

DataBuffer.TYPE_BYTE

,

DataBuffer.TYPE_USHORT

, or

DataBuffer.TYPE_INT

---

#### MultiPixelPackedSampleModel

public MultiPixelPackedSampleModel​(int dataType,
int w,
int h,
int numberOfBits)

Constructs a

MultiPixelPackedSampleModel

with the
specified data type, width, height and number of bits per pixel.

MultiPixelPackedSampleModel

```java
public MultiPixelPackedSampleModel​(int dataType,
int w,
int h,
int numberOfBits,
int scanlineStride,
int dataBitOffset)
```

Constructs a

MultiPixelPackedSampleModel

with
specified data type, width, height, number of bits per pixel,
scanline stride and data bit offset.

**Parameters:** dataType

- the data type for storing samples
**Parameters:** w

- the width, in pixels, of the region of
image data described
**Parameters:** h

- the height, in pixels, of the region of
image data described
**Parameters:** numberOfBits

- the number of bits per pixel
**Parameters:** scanlineStride

- the line stride of the image data
**Parameters:** dataBitOffset

- the data bit offset for the region of image
data described
**Throws:** RasterFormatException

- if the number of bits per pixel
is not a power of 2 or if a power of 2 number of
pixels do not fit in one data element.
**Throws:** IllegalArgumentException

- if

w

or

h

is not greater than 0
**Throws:** IllegalArgumentException

- if

dataType

is not
either

DataBuffer.TYPE_BYTE

,

DataBuffer.TYPE_USHORT

, or

DataBuffer.TYPE_INT

---

#### MultiPixelPackedSampleModel

public MultiPixelPackedSampleModel​(int dataType,
int w,
int h,
int numberOfBits,
int scanlineStride,
int dataBitOffset)

Constructs a

MultiPixelPackedSampleModel

with
specified data type, width, height, number of bits per pixel,
scanline stride and data bit offset.

Method Detail

- createCompatibleSampleModel

```java
public
SampleModel
createCompatibleSampleModel​(int w,
int h)
```

Creates a new

MultiPixelPackedSampleModel

with the
specified width and height. The new

MultiPixelPackedSampleModel

has the
same storage data type and number of bits per pixel as this

MultiPixelPackedSampleModel

.

**Specified by:** createCompatibleSampleModel

in class

SampleModel
**Parameters:** w

- the specified width
**Parameters:** h

- the specified height
**Returns:** a

SampleModel

with the specified width and height
and with the same storage data type and number of bits per pixel
as this

MultiPixelPackedSampleModel

.
**Throws:** IllegalArgumentException

- if

w

or

h

is not greater than 0

- createDataBuffer

```java
public
DataBuffer
createDataBuffer()
```

Creates a

DataBuffer

that corresponds to this

MultiPixelPackedSampleModel

. The

DataBuffer

object's data type and size
is consistent with this

MultiPixelPackedSampleModel

.
The

DataBuffer

has a single bank.

**Specified by:** createDataBuffer

in class

SampleModel
**Returns:** a

DataBuffer

with the same data type and
size as this

MultiPixelPackedSampleModel

.

- getNumDataElements

```java
public int getNumDataElements()
```

Returns the number of data elements needed to transfer one pixel
via the

getDataElements(int, int, java.lang.Object, java.awt.image.DataBuffer)

and

setDataElements(int, int, java.lang.Object, java.awt.image.DataBuffer)

methods. For a

MultiPixelPackedSampleModel

, this is
one.

**Specified by:** getNumDataElements

in class

SampleModel
**Returns:** the number of data elements.
**See Also:** SampleModel.getDataElements(int, int, Object, DataBuffer)

,

SampleModel.getDataElements(int, int, int, int, Object, DataBuffer)

,

SampleModel.setDataElements(int, int, Object, DataBuffer)

,

SampleModel.setDataElements(int, int, int, int, Object, DataBuffer)

,

SampleModel.getTransferType()

- getSampleSize

```java
public int[] getSampleSize()
```

Returns the number of bits per sample for all bands.

**Specified by:** getSampleSize

in class

SampleModel
**Returns:** the number of bits per sample.

- getSampleSize

```java
public int getSampleSize​(int band)
```

Returns the number of bits per sample for the specified band.

**Specified by:** getSampleSize

in class

SampleModel
**Parameters:** band

- the specified band
**Returns:** the number of bits per sample for the specified band.

- getOffset

```java
public int getOffset​(int x,
int y)
```

Returns the offset of pixel (x, y) in data array elements.

**Parameters:** x

- the X coordinate of the specified pixel
**Parameters:** y

- the Y coordinate of the specified pixel
**Returns:** the offset of the specified pixel.

- getBitOffset

```java
public int getBitOffset​(int x)
```

Returns the offset, in bits, into the data element in which it is
stored for the

x

th pixel of a scanline.
This offset is the same for all scanlines.

**Parameters:** x

- the specified pixel
**Returns:** the bit offset of the specified pixel.

- getScanlineStride

```java
public int getScanlineStride()
```

Returns the scanline stride.

**Returns:** the scanline stride of this

MultiPixelPackedSampleModel

.

- getPixelBitStride

```java
public int getPixelBitStride()
```

Returns the pixel bit stride in bits. This value is the same as
the number of bits per pixel.

**Returns:** the

pixelBitStride

of this

MultiPixelPackedSampleModel

.

- getDataBitOffset

```java
public int getDataBitOffset()
```

Returns the data bit offset in bits.

**Returns:** the

dataBitOffset

of this

MultiPixelPackedSampleModel

.

- getTransferType

```java
public int getTransferType()
```

Returns the TransferType used to transfer pixels by way of the

getDataElements

and

setDataElements

methods. The TransferType might or might not be the same as the
storage DataType. The TransferType is one of
DataBuffer.TYPE_BYTE, DataBuffer.TYPE_USHORT,
or DataBuffer.TYPE_INT.

**Overrides:** getTransferType

in class

SampleModel
**Returns:** the transfertype.
**See Also:** SampleModel.getDataElements(int, int, Object, DataBuffer)

,

SampleModel.getDataElements(int, int, int, int, Object, DataBuffer)

,

SampleModel.setDataElements(int, int, Object, DataBuffer)

,

SampleModel.setDataElements(int, int, int, int, Object, DataBuffer)

,

SampleModel.getNumDataElements()

,

DataBuffer

- createSubsetSampleModel

```java
public
SampleModel
createSubsetSampleModel​(int[] bands)
```

Creates a new

MultiPixelPackedSampleModel

with a
subset of the bands of this

MultiPixelPackedSampleModel

. Since a

MultiPixelPackedSampleModel

only has one band, the
bands argument must have a length of one and indicate the zeroth
band.

**Specified by:** createSubsetSampleModel

in class

SampleModel
**Parameters:** bands

- the specified bands
**Returns:** a new

SampleModel

with a subset of bands of
this

MultiPixelPackedSampleModel

.
**Throws:** RasterFormatException

- if the number of bands requested
is not one.
**Throws:** IllegalArgumentException

- if

w

or

h

is not greater than 0

- getSample

```java
public int getSample​(int x,
int y,
int b,

DataBuffer
data)
```

Returns as

int

the sample in a specified band for the
pixel located at (x, y). An

ArrayIndexOutOfBoundsException

is thrown if the
coordinates are not in bounds.

**Specified by:** getSample

in class

SampleModel
**Parameters:** x

- the X coordinate of the specified pixel
**Parameters:** y

- the Y coordinate of the specified pixel
**Parameters:** b

- the band to return, which is assumed to be 0
**Parameters:** data

- the

DataBuffer

containing the image
data
**Returns:** the specified band containing the sample of the specified
pixel.
**Throws:** ArrayIndexOutOfBoundsException

- if the specified
coordinates are not in bounds.
**See Also:** setSample(int, int, int, int, DataBuffer)

- setSample

```java
public void setSample​(int x,
int y,
int b,
int s,

DataBuffer
data)
```

Sets a sample in the specified band for the pixel located at
(x, y) in the

DataBuffer

using an

int

for input.
An

ArrayIndexOutOfBoundsException

is thrown if the
coordinates are not in bounds.

**Specified by:** setSample

in class

SampleModel
**Parameters:** x

- the X coordinate of the specified pixel
**Parameters:** y

- the Y coordinate of the specified pixel
**Parameters:** b

- the band to return, which is assumed to be 0
**Parameters:** s

- the input sample as an

int
**Parameters:** data

- the

DataBuffer

where image data is stored
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds.
**See Also:** getSample(int, int, int, DataBuffer)

- getDataElements

```java
public
Object
getDataElements​(int x,
int y,

Object
obj,

DataBuffer
data)
```

Returns data for a single pixel in a primitive array of type
TransferType. For a

MultiPixelPackedSampleModel

,
the array has one element, and the type is the smallest of
DataBuffer.TYPE_BYTE, DataBuffer.TYPE_USHORT, or DataBuffer.TYPE_INT
that can hold a single pixel. Generally,

obj

should be passed in as

null

, so that the

Object

is created automatically and is the
correct primitive data type.

The following code illustrates transferring data for one pixel from

DataBuffer db1

, whose storage layout is
described by

MultiPixelPackedSampleModel

mppsm1

, to

DataBuffer db2

,
whose storage layout is described by

MultiPixelPackedSampleModel mppsm2

.
The transfer is generally more efficient than using

getPixel

or

setPixel

.

```java
MultiPixelPackedSampleModel mppsm1, mppsm2;
DataBufferInt db1, db2;
mppsm2.setDataElements(x, y, mppsm1.getDataElements(x, y, null,
db1), db2);
```

Using

getDataElements

or

setDataElements

to transfer between two

DataBuffer/SampleModel

pairs
is legitimate if the

SampleModels

have the same number
of bands, corresponding bands have the same number of
bits per sample, and the TransferTypes are the same.

If

obj

is not

null

, it should be a
primitive array of type TransferType. Otherwise, a

ClassCastException

is thrown. An

ArrayIndexOutOfBoundsException

is thrown if the
coordinates are not in bounds, or if

obj

is not

null

and is not large enough to hold the pixel data.

**Specified by:** getDataElements

in class

SampleModel
**Parameters:** x

- the X coordinate of the specified pixel
**Parameters:** y

- the Y coordinate of the specified pixel
**Parameters:** obj

- a primitive array in which to return the pixel data or

null

.
**Parameters:** data

- the

DataBuffer

containing the image data.
**Returns:** an

Object

containing data for the specified
pixel.
**Throws:** ClassCastException

- if

obj

is not a
primitive array of type TransferType or is not

null
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if

obj

is not

null

or
not large enough to hold the pixel data
**See Also:** setDataElements(int, int, Object, DataBuffer)

- getPixel

```java
public int[] getPixel​(int x,
int y,
int[] iArray,

DataBuffer
data)
```

Returns the specified single band pixel in the first element
of an

int

array.

ArrayIndexOutOfBoundsException

is thrown if the
coordinates are not in bounds.

**Overrides:** getPixel

in class

SampleModel
**Parameters:** x

- the X coordinate of the specified pixel
**Parameters:** y

- the Y coordinate of the specified pixel
**Parameters:** iArray

- the array containing the pixel to be returned or

null
**Parameters:** data

- the

DataBuffer

where image data is stored
**Returns:** an array containing the specified pixel.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates
are not in bounds
**See Also:** setPixel(int, int, int[], DataBuffer)

- setDataElements

```java
public void setDataElements​(int x,
int y,

Object
obj,

DataBuffer
data)
```

Sets the data for a single pixel in the specified

DataBuffer

from a primitive array of type
TransferType. For a

MultiPixelPackedSampleModel

,
only the first element of the array holds valid data,
and the type must be the smallest of
DataBuffer.TYPE_BYTE, DataBuffer.TYPE_USHORT, or DataBuffer.TYPE_INT
that can hold a single pixel.

The following code illustrates transferring data for one pixel from

DataBuffer db1

, whose storage layout is
described by

MultiPixelPackedSampleModel

mppsm1

, to

DataBuffer db2

,
whose storage layout is described by

MultiPixelPackedSampleModel mppsm2

.
The transfer is generally more efficient than using

getPixel

or

setPixel

.

```java
MultiPixelPackedSampleModel mppsm1, mppsm2;
DataBufferInt db1, db2;
mppsm2.setDataElements(x, y, mppsm1.getDataElements(x, y, null,
db1), db2);
```

Using

getDataElements

or

setDataElements

to
transfer between two

DataBuffer/SampleModel

pairs is
legitimate if the

SampleModel

objects have
the same number of bands, corresponding bands have the same number of
bits per sample, and the TransferTypes are the same.

obj

must be a primitive array of type TransferType.
Otherwise, a

ClassCastException

is thrown. An

ArrayIndexOutOfBoundsException

is thrown if the
coordinates are not in bounds, or if

obj

is not large
enough to hold the pixel data.

**Specified by:** setDataElements

in class

SampleModel
**Parameters:** x

- the X coordinate of the pixel location
**Parameters:** y

- the Y coordinate of the pixel location
**Parameters:** obj

- a primitive array containing pixel data
**Parameters:** data

- the

DataBuffer

containing the image data
**See Also:** getDataElements(int, int, Object, DataBuffer)

- setPixel

```java
public void setPixel​(int x,
int y,
int[] iArray,

DataBuffer
data)
```

Sets a pixel in the

DataBuffer

using an

int

array for input.

ArrayIndexOutOfBoundsException

is thrown if
the coordinates are not in bounds.

**Overrides:** setPixel

in class

SampleModel
**Parameters:** x

- the X coordinate of the pixel location
**Parameters:** y

- the Y coordinate of the pixel location
**Parameters:** iArray

- the input pixel in an

int

array
**Parameters:** data

- the

DataBuffer

containing the image data
**See Also:** getPixel(int, int, int[], DataBuffer)

---

#### Method Detail

createCompatibleSampleModel

```java
public
SampleModel
createCompatibleSampleModel​(int w,
int h)
```

Creates a new

MultiPixelPackedSampleModel

with the
specified width and height. The new

MultiPixelPackedSampleModel

has the
same storage data type and number of bits per pixel as this

MultiPixelPackedSampleModel

.

**Specified by:** createCompatibleSampleModel

in class

SampleModel
**Parameters:** w

- the specified width
**Parameters:** h

- the specified height
**Returns:** a

SampleModel

with the specified width and height
and with the same storage data type and number of bits per pixel
as this

MultiPixelPackedSampleModel

.
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

Creates a new

MultiPixelPackedSampleModel

with the
specified width and height. The new

MultiPixelPackedSampleModel

has the
same storage data type and number of bits per pixel as this

MultiPixelPackedSampleModel

.

createDataBuffer

```java
public
DataBuffer
createDataBuffer()
```

Creates a

DataBuffer

that corresponds to this

MultiPixelPackedSampleModel

. The

DataBuffer

object's data type and size
is consistent with this

MultiPixelPackedSampleModel

.
The

DataBuffer

has a single bank.

**Specified by:** createDataBuffer

in class

SampleModel
**Returns:** a

DataBuffer

with the same data type and
size as this

MultiPixelPackedSampleModel

.

---

#### createDataBuffer

public

DataBuffer

createDataBuffer()

Creates a

DataBuffer

that corresponds to this

MultiPixelPackedSampleModel

. The

DataBuffer

object's data type and size
is consistent with this

MultiPixelPackedSampleModel

.
The

DataBuffer

has a single bank.

getNumDataElements

```java
public int getNumDataElements()
```

Returns the number of data elements needed to transfer one pixel
via the

getDataElements(int, int, java.lang.Object, java.awt.image.DataBuffer)

and

setDataElements(int, int, java.lang.Object, java.awt.image.DataBuffer)

methods. For a

MultiPixelPackedSampleModel

, this is
one.

**Specified by:** getNumDataElements

in class

SampleModel
**Returns:** the number of data elements.
**See Also:** SampleModel.getDataElements(int, int, Object, DataBuffer)

,

SampleModel.getDataElements(int, int, int, int, Object, DataBuffer)

,

SampleModel.setDataElements(int, int, Object, DataBuffer)

,

SampleModel.setDataElements(int, int, int, int, Object, DataBuffer)

,

SampleModel.getTransferType()

---

#### getNumDataElements

public int getNumDataElements()

Returns the number of data elements needed to transfer one pixel
via the

getDataElements(int, int, java.lang.Object, java.awt.image.DataBuffer)

and

setDataElements(int, int, java.lang.Object, java.awt.image.DataBuffer)

methods. For a

MultiPixelPackedSampleModel

, this is
one.

getSampleSize

```java
public int[] getSampleSize()
```

Returns the number of bits per sample for all bands.

**Specified by:** getSampleSize

in class

SampleModel
**Returns:** the number of bits per sample.

---

#### getSampleSize

public int[] getSampleSize()

Returns the number of bits per sample for all bands.

getSampleSize

```java
public int getSampleSize​(int band)
```

Returns the number of bits per sample for the specified band.

**Specified by:** getSampleSize

in class

SampleModel
**Parameters:** band

- the specified band
**Returns:** the number of bits per sample for the specified band.

---

#### getSampleSize

public int getSampleSize​(int band)

Returns the number of bits per sample for the specified band.

getOffset

```java
public int getOffset​(int x,
int y)
```

Returns the offset of pixel (x, y) in data array elements.

**Parameters:** x

- the X coordinate of the specified pixel
**Parameters:** y

- the Y coordinate of the specified pixel
**Returns:** the offset of the specified pixel.

---

#### getOffset

public int getOffset​(int x,
int y)

Returns the offset of pixel (x, y) in data array elements.

getBitOffset

```java
public int getBitOffset​(int x)
```

Returns the offset, in bits, into the data element in which it is
stored for the

x

th pixel of a scanline.
This offset is the same for all scanlines.

**Parameters:** x

- the specified pixel
**Returns:** the bit offset of the specified pixel.

---

#### getBitOffset

public int getBitOffset​(int x)

Returns the offset, in bits, into the data element in which it is
stored for the

x

th pixel of a scanline.
This offset is the same for all scanlines.

getScanlineStride

```java
public int getScanlineStride()
```

Returns the scanline stride.

**Returns:** the scanline stride of this

MultiPixelPackedSampleModel

.

---

#### getScanlineStride

public int getScanlineStride()

Returns the scanline stride.

getPixelBitStride

```java
public int getPixelBitStride()
```

Returns the pixel bit stride in bits. This value is the same as
the number of bits per pixel.

**Returns:** the

pixelBitStride

of this

MultiPixelPackedSampleModel

.

---

#### getPixelBitStride

public int getPixelBitStride()

Returns the pixel bit stride in bits. This value is the same as
the number of bits per pixel.

getDataBitOffset

```java
public int getDataBitOffset()
```

Returns the data bit offset in bits.

**Returns:** the

dataBitOffset

of this

MultiPixelPackedSampleModel

.

---

#### getDataBitOffset

public int getDataBitOffset()

Returns the data bit offset in bits.

getTransferType

```java
public int getTransferType()
```

Returns the TransferType used to transfer pixels by way of the

getDataElements

and

setDataElements

methods. The TransferType might or might not be the same as the
storage DataType. The TransferType is one of
DataBuffer.TYPE_BYTE, DataBuffer.TYPE_USHORT,
or DataBuffer.TYPE_INT.

**Overrides:** getTransferType

in class

SampleModel
**Returns:** the transfertype.
**See Also:** SampleModel.getDataElements(int, int, Object, DataBuffer)

,

SampleModel.getDataElements(int, int, int, int, Object, DataBuffer)

,

SampleModel.setDataElements(int, int, Object, DataBuffer)

,

SampleModel.setDataElements(int, int, int, int, Object, DataBuffer)

,

SampleModel.getNumDataElements()

,

DataBuffer

---

#### getTransferType

public int getTransferType()

Returns the TransferType used to transfer pixels by way of the

getDataElements

and

setDataElements

methods. The TransferType might or might not be the same as the
storage DataType. The TransferType is one of
DataBuffer.TYPE_BYTE, DataBuffer.TYPE_USHORT,
or DataBuffer.TYPE_INT.

createSubsetSampleModel

```java
public
SampleModel
createSubsetSampleModel​(int[] bands)
```

Creates a new

MultiPixelPackedSampleModel

with a
subset of the bands of this

MultiPixelPackedSampleModel

. Since a

MultiPixelPackedSampleModel

only has one band, the
bands argument must have a length of one and indicate the zeroth
band.

**Specified by:** createSubsetSampleModel

in class

SampleModel
**Parameters:** bands

- the specified bands
**Returns:** a new

SampleModel

with a subset of bands of
this

MultiPixelPackedSampleModel

.
**Throws:** RasterFormatException

- if the number of bands requested
is not one.
**Throws:** IllegalArgumentException

- if

w

or

h

is not greater than 0

---

#### createSubsetSampleModel

public

SampleModel

createSubsetSampleModel​(int[] bands)

Creates a new

MultiPixelPackedSampleModel

with a
subset of the bands of this

MultiPixelPackedSampleModel

. Since a

MultiPixelPackedSampleModel

only has one band, the
bands argument must have a length of one and indicate the zeroth
band.

getSample

```java
public int getSample​(int x,
int y,
int b,

DataBuffer
data)
```

Returns as

int

the sample in a specified band for the
pixel located at (x, y). An

ArrayIndexOutOfBoundsException

is thrown if the
coordinates are not in bounds.

**Specified by:** getSample

in class

SampleModel
**Parameters:** x

- the X coordinate of the specified pixel
**Parameters:** y

- the Y coordinate of the specified pixel
**Parameters:** b

- the band to return, which is assumed to be 0
**Parameters:** data

- the

DataBuffer

containing the image
data
**Returns:** the specified band containing the sample of the specified
pixel.
**Throws:** ArrayIndexOutOfBoundsException

- if the specified
coordinates are not in bounds.
**See Also:** setSample(int, int, int, int, DataBuffer)

---

#### getSample

public int getSample​(int x,
int y,
int b,

DataBuffer

data)

Returns as

int

the sample in a specified band for the
pixel located at (x, y). An

ArrayIndexOutOfBoundsException

is thrown if the
coordinates are not in bounds.

setSample

```java
public void setSample​(int x,
int y,
int b,
int s,

DataBuffer
data)
```

Sets a sample in the specified band for the pixel located at
(x, y) in the

DataBuffer

using an

int

for input.
An

ArrayIndexOutOfBoundsException

is thrown if the
coordinates are not in bounds.

**Specified by:** setSample

in class

SampleModel
**Parameters:** x

- the X coordinate of the specified pixel
**Parameters:** y

- the Y coordinate of the specified pixel
**Parameters:** b

- the band to return, which is assumed to be 0
**Parameters:** s

- the input sample as an

int
**Parameters:** data

- the

DataBuffer

where image data is stored
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds.
**See Also:** getSample(int, int, int, DataBuffer)

---

#### setSample

public void setSample​(int x,
int y,
int b,
int s,

DataBuffer

data)

Sets a sample in the specified band for the pixel located at
(x, y) in the

DataBuffer

using an

int

for input.
An

ArrayIndexOutOfBoundsException

is thrown if the
coordinates are not in bounds.

getDataElements

```java
public
Object
getDataElements​(int x,
int y,

Object
obj,

DataBuffer
data)
```

Returns data for a single pixel in a primitive array of type
TransferType. For a

MultiPixelPackedSampleModel

,
the array has one element, and the type is the smallest of
DataBuffer.TYPE_BYTE, DataBuffer.TYPE_USHORT, or DataBuffer.TYPE_INT
that can hold a single pixel. Generally,

obj

should be passed in as

null

, so that the

Object

is created automatically and is the
correct primitive data type.

The following code illustrates transferring data for one pixel from

DataBuffer db1

, whose storage layout is
described by

MultiPixelPackedSampleModel

mppsm1

, to

DataBuffer db2

,
whose storage layout is described by

MultiPixelPackedSampleModel mppsm2

.
The transfer is generally more efficient than using

getPixel

or

setPixel

.

```java
MultiPixelPackedSampleModel mppsm1, mppsm2;
DataBufferInt db1, db2;
mppsm2.setDataElements(x, y, mppsm1.getDataElements(x, y, null,
db1), db2);
```

Using

getDataElements

or

setDataElements

to transfer between two

DataBuffer/SampleModel

pairs
is legitimate if the

SampleModels

have the same number
of bands, corresponding bands have the same number of
bits per sample, and the TransferTypes are the same.

If

obj

is not

null

, it should be a
primitive array of type TransferType. Otherwise, a

ClassCastException

is thrown. An

ArrayIndexOutOfBoundsException

is thrown if the
coordinates are not in bounds, or if

obj

is not

null

and is not large enough to hold the pixel data.

**Specified by:** getDataElements

in class

SampleModel
**Parameters:** x

- the X coordinate of the specified pixel
**Parameters:** y

- the Y coordinate of the specified pixel
**Parameters:** obj

- a primitive array in which to return the pixel data or

null

.
**Parameters:** data

- the

DataBuffer

containing the image data.
**Returns:** an

Object

containing data for the specified
pixel.
**Throws:** ClassCastException

- if

obj

is not a
primitive array of type TransferType or is not

null
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if

obj

is not

null

or
not large enough to hold the pixel data
**See Also:** setDataElements(int, int, Object, DataBuffer)

---

#### getDataElements

public

Object

getDataElements​(int x,
int y,

Object

obj,

DataBuffer

data)

Returns data for a single pixel in a primitive array of type
TransferType. For a

MultiPixelPackedSampleModel

,
the array has one element, and the type is the smallest of
DataBuffer.TYPE_BYTE, DataBuffer.TYPE_USHORT, or DataBuffer.TYPE_INT
that can hold a single pixel. Generally,

obj

should be passed in as

null

, so that the

Object

is created automatically and is the
correct primitive data type.

The following code illustrates transferring data for one pixel from

DataBuffer db1

, whose storage layout is
described by

MultiPixelPackedSampleModel

mppsm1

, to

DataBuffer db2

,
whose storage layout is described by

MultiPixelPackedSampleModel mppsm2

.
The transfer is generally more efficient than using

getPixel

or

setPixel

.

```java
MultiPixelPackedSampleModel mppsm1, mppsm2;
DataBufferInt db1, db2;
mppsm2.setDataElements(x, y, mppsm1.getDataElements(x, y, null,
db1), db2);
```

Using

getDataElements

or

setDataElements

to transfer between two

DataBuffer/SampleModel

pairs
is legitimate if the

SampleModels

have the same number
of bands, corresponding bands have the same number of
bits per sample, and the TransferTypes are the same.

If

obj

is not

null

, it should be a
primitive array of type TransferType. Otherwise, a

ClassCastException

is thrown. An

ArrayIndexOutOfBoundsException

is thrown if the
coordinates are not in bounds, or if

obj

is not

null

and is not large enough to hold the pixel data.

The following code illustrates transferring data for one pixel from

DataBuffer db1

, whose storage layout is
described by

MultiPixelPackedSampleModel

mppsm1

, to

DataBuffer db2

,
whose storage layout is described by

MultiPixelPackedSampleModel mppsm2

.
The transfer is generally more efficient than using

getPixel

or

setPixel

.

```java
MultiPixelPackedSampleModel mppsm1, mppsm2;
DataBufferInt db1, db2;
mppsm2.setDataElements(x, y, mppsm1.getDataElements(x, y, null,
db1), db2);
```

Using

getDataElements

or

setDataElements

to transfer between two

DataBuffer/SampleModel

pairs
is legitimate if the

SampleModels

have the same number
of bands, corresponding bands have the same number of
bits per sample, and the TransferTypes are the same.

If

obj

is not

null

, it should be a
primitive array of type TransferType. Otherwise, a

ClassCastException

is thrown. An

ArrayIndexOutOfBoundsException

is thrown if the
coordinates are not in bounds, or if

obj

is not

null

and is not large enough to hold the pixel data.

MultiPixelPackedSampleModel mppsm1, mppsm2;
DataBufferInt db1, db2;
mppsm2.setDataElements(x, y, mppsm1.getDataElements(x, y, null,
db1), db2);

If

obj

is not

null

, it should be a
primitive array of type TransferType. Otherwise, a

ClassCastException

is thrown. An

ArrayIndexOutOfBoundsException

is thrown if the
coordinates are not in bounds, or if

obj

is not

null

and is not large enough to hold the pixel data.

getPixel

```java
public int[] getPixel​(int x,
int y,
int[] iArray,

DataBuffer
data)
```

Returns the specified single band pixel in the first element
of an

int

array.

ArrayIndexOutOfBoundsException

is thrown if the
coordinates are not in bounds.

**Overrides:** getPixel

in class

SampleModel
**Parameters:** x

- the X coordinate of the specified pixel
**Parameters:** y

- the Y coordinate of the specified pixel
**Parameters:** iArray

- the array containing the pixel to be returned or

null
**Parameters:** data

- the

DataBuffer

where image data is stored
**Returns:** an array containing the specified pixel.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates
are not in bounds
**See Also:** setPixel(int, int, int[], DataBuffer)

---

#### getPixel

public int[] getPixel​(int x,
int y,
int[] iArray,

DataBuffer

data)

Returns the specified single band pixel in the first element
of an

int

array.

ArrayIndexOutOfBoundsException

is thrown if the
coordinates are not in bounds.

setDataElements

```java
public void setDataElements​(int x,
int y,

Object
obj,

DataBuffer
data)
```

Sets the data for a single pixel in the specified

DataBuffer

from a primitive array of type
TransferType. For a

MultiPixelPackedSampleModel

,
only the first element of the array holds valid data,
and the type must be the smallest of
DataBuffer.TYPE_BYTE, DataBuffer.TYPE_USHORT, or DataBuffer.TYPE_INT
that can hold a single pixel.

The following code illustrates transferring data for one pixel from

DataBuffer db1

, whose storage layout is
described by

MultiPixelPackedSampleModel

mppsm1

, to

DataBuffer db2

,
whose storage layout is described by

MultiPixelPackedSampleModel mppsm2

.
The transfer is generally more efficient than using

getPixel

or

setPixel

.

```java
MultiPixelPackedSampleModel mppsm1, mppsm2;
DataBufferInt db1, db2;
mppsm2.setDataElements(x, y, mppsm1.getDataElements(x, y, null,
db1), db2);
```

Using

getDataElements

or

setDataElements

to
transfer between two

DataBuffer/SampleModel

pairs is
legitimate if the

SampleModel

objects have
the same number of bands, corresponding bands have the same number of
bits per sample, and the TransferTypes are the same.

obj

must be a primitive array of type TransferType.
Otherwise, a

ClassCastException

is thrown. An

ArrayIndexOutOfBoundsException

is thrown if the
coordinates are not in bounds, or if

obj

is not large
enough to hold the pixel data.

**Specified by:** setDataElements

in class

SampleModel
**Parameters:** x

- the X coordinate of the pixel location
**Parameters:** y

- the Y coordinate of the pixel location
**Parameters:** obj

- a primitive array containing pixel data
**Parameters:** data

- the

DataBuffer

containing the image data
**See Also:** getDataElements(int, int, Object, DataBuffer)

---

#### setDataElements

public void setDataElements​(int x,
int y,

Object

obj,

DataBuffer

data)

Sets the data for a single pixel in the specified

DataBuffer

from a primitive array of type
TransferType. For a

MultiPixelPackedSampleModel

,
only the first element of the array holds valid data,
and the type must be the smallest of
DataBuffer.TYPE_BYTE, DataBuffer.TYPE_USHORT, or DataBuffer.TYPE_INT
that can hold a single pixel.

The following code illustrates transferring data for one pixel from

DataBuffer db1

, whose storage layout is
described by

MultiPixelPackedSampleModel

mppsm1

, to

DataBuffer db2

,
whose storage layout is described by

MultiPixelPackedSampleModel mppsm2

.
The transfer is generally more efficient than using

getPixel

or

setPixel

.

```java
MultiPixelPackedSampleModel mppsm1, mppsm2;
DataBufferInt db1, db2;
mppsm2.setDataElements(x, y, mppsm1.getDataElements(x, y, null,
db1), db2);
```

Using

getDataElements

or

setDataElements

to
transfer between two

DataBuffer/SampleModel

pairs is
legitimate if the

SampleModel

objects have
the same number of bands, corresponding bands have the same number of
bits per sample, and the TransferTypes are the same.

obj

must be a primitive array of type TransferType.
Otherwise, a

ClassCastException

is thrown. An

ArrayIndexOutOfBoundsException

is thrown if the
coordinates are not in bounds, or if

obj

is not large
enough to hold the pixel data.

The following code illustrates transferring data for one pixel from

DataBuffer db1

, whose storage layout is
described by

MultiPixelPackedSampleModel

mppsm1

, to

DataBuffer db2

,
whose storage layout is described by

MultiPixelPackedSampleModel mppsm2

.
The transfer is generally more efficient than using

getPixel

or

setPixel

.

```java
MultiPixelPackedSampleModel mppsm1, mppsm2;
DataBufferInt db1, db2;
mppsm2.setDataElements(x, y, mppsm1.getDataElements(x, y, null,
db1), db2);
```

Using

getDataElements

or

setDataElements

to
transfer between two

DataBuffer/SampleModel

pairs is
legitimate if the

SampleModel

objects have
the same number of bands, corresponding bands have the same number of
bits per sample, and the TransferTypes are the same.

obj

must be a primitive array of type TransferType.
Otherwise, a

ClassCastException

is thrown. An

ArrayIndexOutOfBoundsException

is thrown if the
coordinates are not in bounds, or if

obj

is not large
enough to hold the pixel data.

MultiPixelPackedSampleModel mppsm1, mppsm2;
DataBufferInt db1, db2;
mppsm2.setDataElements(x, y, mppsm1.getDataElements(x, y, null,
db1), db2);

obj

must be a primitive array of type TransferType.
Otherwise, a

ClassCastException

is thrown. An

ArrayIndexOutOfBoundsException

is thrown if the
coordinates are not in bounds, or if

obj

is not large
enough to hold the pixel data.

setPixel

```java
public void setPixel​(int x,
int y,
int[] iArray,

DataBuffer
data)
```

Sets a pixel in the

DataBuffer

using an

int

array for input.

ArrayIndexOutOfBoundsException

is thrown if
the coordinates are not in bounds.

**Overrides:** setPixel

in class

SampleModel
**Parameters:** x

- the X coordinate of the pixel location
**Parameters:** y

- the Y coordinate of the pixel location
**Parameters:** iArray

- the input pixel in an

int

array
**Parameters:** data

- the

DataBuffer

containing the image data
**See Also:** getPixel(int, int, int[], DataBuffer)

---

#### setPixel

public void setPixel​(int x,
int y,
int[] iArray,

DataBuffer

data)

Sets a pixel in the

DataBuffer

using an

int

array for input.

ArrayIndexOutOfBoundsException

is thrown if
the coordinates are not in bounds.

---

