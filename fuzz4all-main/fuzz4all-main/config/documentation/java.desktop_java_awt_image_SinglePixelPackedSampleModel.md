# Class SinglePixelPackedSampleModel

**Source:** `java.desktop\java\awt\image\SinglePixelPackedSampleModel.html`

### Class Description

```java
public class
SinglePixelPackedSampleModel

extends
SampleModel
```

This class represents pixel data packed such that the N samples which make
up a single pixel are stored in a single data array element, and each data
data array element holds samples for only one pixel.
This class supports

TYPE_BYTE

,

TYPE_USHORT

,

TYPE_INT

data types.
All data array elements reside
in the first bank of a DataBuffer. Accessor methods are provided so
that the image data can be manipulated directly. Scanline stride is the
number of data array elements between a given sample and the corresponding
sample in the same column of the next scanline. Bit masks are the masks
required to extract the samples representing the bands of the pixel.
Bit offsets are the offsets in bits into the data array
element of the samples representing the bands of the pixel.

The following code illustrates extracting the bits of the sample
representing band

b

for pixel

x,y

from DataBuffer

data

:

```java
int sample = data.getElem(y * scanlineStride + x);
sample = (sample & bitMasks[b]) >>> bitOffsets[b];
```

---

### Field Details

*No entries found.*

### Constructor Details

#### public SinglePixelPackedSampleModel​(int dataType,
int w,
int h,
int[] bitMasks)

Constructs a SinglePixelPackedSampleModel with bitMasks.length bands.
Each sample is stored in a data array element in the position of
its corresponding bit mask. Each bit mask must be contiguous and
masks must not overlap. Bit masks exceeding data type capacity are
truncated.

**Parameters:**
- dataType

- The data type for storing samples.
- w

- The width (in pixels) of the region of the
image data described.
- h

- The height (in pixels) of the region of the
image data described.
- bitMasks

- The bit masks for all bands.

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

#### public SinglePixelPackedSampleModel​(int dataType,
int w,
int h,
int scanlineStride,
int[] bitMasks)

Constructs a SinglePixelPackedSampleModel with bitMasks.length bands
and a scanline stride equal to scanlineStride data array elements.
Each sample is stored in a data array element in the position of
its corresponding bit mask. Each bit mask must be contiguous and
masks must not overlap. Bit masks exceeding data type capacity are
truncated.

**Parameters:**
- dataType

- The data type for storing samples.
- w

- The width (in pixels) of the region of
image data described.
- h

- The height (in pixels) of the region of
image data described.
- scanlineStride

- The line stride of the image data.
- bitMasks

- The bit masks for all bands.

**Throws:**
- IllegalArgumentException

- if

w

or

h

is not greater than 0
- IllegalArgumentException

- if any mask in

bitMask

is not contiguous
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

#### public int getNumDataElements()

Returns the number of data elements needed to transfer one pixel
via the getDataElements and setDataElements methods.
For a SinglePixelPackedSampleModel, this is one.

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

#### public
SampleModel
createCompatibleSampleModel​(int w,
int h)

Creates a new SinglePixelPackedSampleModel with the specified
width and height. The new SinglePixelPackedSampleModel will have the
same storage data type and bit masks as this
SinglePixelPackedSampleModel.

**Specified by:**
- createCompatibleSampleModel

in class

SampleModel

**Parameters:**
- w

- the width of the resulting

SampleModel
- h

- the height of the resulting

SampleModel

**Returns:**
- a

SinglePixelPackedSampleModel

with the
specified width and height.

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

Creates a DataBuffer that corresponds to this
SinglePixelPackedSampleModel. The DataBuffer's data type and size
will be consistent with this SinglePixelPackedSampleModel. The
DataBuffer will have a single bank.

**Specified by:**
- createDataBuffer

in class

SampleModel

**Returns:**
- a

DataBuffer

corresponding to this

SampleModel

.

---

#### public int[] getSampleSize()

Returns the number of bits per sample for all bands.

**Specified by:**
- getSampleSize

in class

SampleModel

**Returns:**
- the size of samples for all bands.

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
- the size of the samples of the specified band.

---

#### public int getOffset​(int x,
int y)

Returns the offset (in data array elements) of pixel (x,y).
The data element containing pixel

x,y

can be retrieved from a DataBuffer

data

with a
SinglePixelPackedSampleModel

sppsm

as:

```java
data.getElem(sppsm.getOffset(x, y));
```

**Parameters:**
- x

- the X coordinate of the specified pixel
- y

- the Y coordinate of the specified pixel

**Returns:**
- the offset of the specified pixel.

---

#### public int[] getBitOffsets()

Returns the bit offsets into the data array element representing
a pixel for all bands.

**Returns:**
- the bit offsets representing a pixel for all bands.

---

#### public int[] getBitMasks()

Returns the bit masks for all bands.

**Returns:**
- the bit masks for all bands.

---

#### public int getScanlineStride()

Returns the scanline stride of this SinglePixelPackedSampleModel.

**Returns:**
- the scanline stride of this

SinglePixelPackedSampleModel

.

---

#### public
SampleModel
createSubsetSampleModel​(int[] bands)

This creates a new SinglePixelPackedSampleModel with a subset of the
bands of this SinglePixelPackedSampleModel. The new
SinglePixelPackedSampleModel can be used with any DataBuffer that the
existing SinglePixelPackedSampleModel can be used with. The new
SinglePixelPackedSampleModel/DataBuffer combination will represent
an image with a subset of the bands of the original
SinglePixelPackedSampleModel/DataBuffer combination.

**Specified by:**
- createSubsetSampleModel

in class

SampleModel

**Parameters:**
- bands

- the subset of bands of this

SampleModel

**Returns:**
- a

SampleModel

with a subset of bands of this

SampleModel

.

**Throws:**
- RasterFormatException

- if the length of the bands argument is
greater than the number of bands in
the sample model.

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
TransferType. For a SinglePixelPackedSampleModel, the array will
have one element, and the type will be the same as the storage
data type. Generally, obj
should be passed in as null, so that the Object will be created
automatically and will be of the right primitive data type.

The following code illustrates transferring data for one pixel from
DataBuffer

db1

, whose storage layout is described by
SinglePixelPackedSampleModel

sppsm1

, to
DataBuffer

db2

, whose storage layout is described by
SinglePixelPackedSampleModel

sppsm2

.
The transfer will generally be more efficient than using
getPixel/setPixel.

```java
SinglePixelPackedSampleModel sppsm1, sppsm2;
DataBufferInt db1, db2;
sppsm2.setDataElements(x, y, sppsm1.getDataElements(x, y, null,
db1), db2);
```

Using getDataElements/setDataElements to transfer between two
DataBuffer/SampleModel pairs is legitimate if the SampleModels have
the same number of bands, corresponding bands have the same number of
bits per sample, and the TransferTypes are the same.

If obj is non-null, it should be a primitive array of type TransferType.
Otherwise, a ClassCastException is thrown. An
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds, or if obj is non-null and is not large enough to hold
the pixel data.

**Specified by:**
- getDataElements

in class

SampleModel

**Parameters:**
- x

- The X coordinate of the pixel location.
- y

- The Y coordinate of the pixel location.
- obj

- If non-null, a primitive array in which to return
the pixel data.
- data

- The DataBuffer containing the image data.

**Returns:**
- the data for the specified pixel.

**See Also:**
- setDataElements(int, int, Object, DataBuffer)

---

#### public int[] getPixel​(int x,
int y,
int[] iArray,

DataBuffer
data)

Returns all samples in for the specified pixel in an int array.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Overrides:**
- getPixel

in class

SampleModel

**Parameters:**
- x

- The X coordinate of the pixel location.
- y

- The Y coordinate of the pixel location.
- iArray

- If non-null, returns the samples in this array
- data

- The DataBuffer containing the image data.

**Returns:**
- all samples for the specified pixel.

**See Also:**
- setPixel(int, int, int[], DataBuffer)

---

#### public int[] getPixels​(int x,
int y,
int w,
int h,
int[] iArray,

DataBuffer
data)

Returns all samples for the specified rectangle of pixels in
an int array, one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Overrides:**
- getPixels

in class

SampleModel

**Parameters:**
- x

- The X coordinate of the upper left pixel location.
- y

- The Y coordinate of the upper left pixel location.
- w

- The width of the pixel rectangle.
- h

- The height of the pixel rectangle.
- iArray

- If non-null, returns the samples in this array.
- data

- The DataBuffer containing the image data.

**Returns:**
- all samples for the specified region of pixels.

**See Also:**
- setPixels(int, int, int, int, int[], DataBuffer)

---

#### public int getSample​(int x,
int y,
int b,

DataBuffer
data)

Returns as int the sample in a specified band for the pixel
located at (x,y).
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Specified by:**
- getSample

in class

SampleModel

**Parameters:**
- x

- The X coordinate of the pixel location.
- y

- The Y coordinate of the pixel location.
- b

- The band to return.
- data

- The DataBuffer containing the image data.

**Returns:**
- the sample in a specified band for the specified
pixel.

**See Also:**
- setSample(int, int, int, int, DataBuffer)

---

#### public int[] getSamples​(int x,
int y,
int w,
int h,
int b,
int[] iArray,

DataBuffer
data)

Returns the samples for a specified band for the specified rectangle
of pixels in an int array, one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Overrides:**
- getSamples

in class

SampleModel

**Parameters:**
- x

- The X coordinate of the upper left pixel location.
- y

- The Y coordinate of the upper left pixel location.
- w

- The width of the pixel rectangle.
- h

- The height of the pixel rectangle.
- b

- The band to return.
- iArray

- If non-null, returns the samples in this array.
- data

- The DataBuffer containing the image data.

**Returns:**
- the samples for the specified band for the specified
region of pixels.

**See Also:**
- setSamples(int, int, int, int, int, int[], DataBuffer)

---

#### public void setDataElements​(int x,
int y,

Object
obj,

DataBuffer
data)

Sets the data for a single pixel in the specified DataBuffer from a
primitive array of type TransferType. For a
SinglePixelPackedSampleModel, only the first element of the array
will hold valid data, and the type of the array must be the same as
the storage data type of the SinglePixelPackedSampleModel.

The following code illustrates transferring data for one pixel from
DataBuffer

db1

, whose storage layout is described by
SinglePixelPackedSampleModel

sppsm1

,
to DataBuffer

db2

, whose storage layout is described by
SinglePixelPackedSampleModel

sppsm2

.
The transfer will generally be more efficient than using
getPixel/setPixel.

```java
SinglePixelPackedSampleModel sppsm1, sppsm2;
DataBufferInt db1, db2;
sppsm2.setDataElements(x, y, sppsm1.getDataElements(x, y, null,
db1), db2);
```

Using getDataElements/setDataElements to transfer between two
DataBuffer/SampleModel pairs is legitimate if the SampleModels have
the same number of bands, corresponding bands have the same number of
bits per sample, and the TransferTypes are the same.

obj must be a primitive array of type TransferType. Otherwise,
a ClassCastException is thrown. An
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds, or if obj is not large enough to hold the pixel data.

**Specified by:**
- setDataElements

in class

SampleModel

**Parameters:**
- x

- The X coordinate of the pixel location.
- y

- The Y coordinate of the pixel location.
- obj

- A primitive array containing pixel data.
- data

- The DataBuffer containing the image data.

**See Also:**
- getDataElements(int, int, Object, DataBuffer)

---

#### public void setPixel​(int x,
int y,
int[] iArray,

DataBuffer
data)

Sets a pixel in the DataBuffer using an int array of samples for input.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Overrides:**
- setPixel

in class

SampleModel

**Parameters:**
- x

- The X coordinate of the pixel location.
- y

- The Y coordinate of the pixel location.
- iArray

- The input samples in an int array.
- data

- The DataBuffer containing the image data.

**See Also:**
- getPixel(int, int, int[], DataBuffer)

---

#### public void setPixels​(int x,
int y,
int w,
int h,
int[] iArray,

DataBuffer
data)

Sets all samples for a rectangle of pixels from an int array containing
one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Overrides:**
- setPixels

in class

SampleModel

**Parameters:**
- x

- The X coordinate of the upper left pixel location.
- y

- The Y coordinate of the upper left pixel location.
- w

- The width of the pixel rectangle.
- h

- The height of the pixel rectangle.
- iArray

- The input samples in an int array.
- data

- The DataBuffer containing the image data.

**See Also:**
- getPixels(int, int, int, int, int[], DataBuffer)

---

#### public void setSample​(int x,
int y,
int b,
int s,

DataBuffer
data)

Sets a sample in the specified band for the pixel located at (x,y)
in the DataBuffer using an int for input.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Specified by:**
- setSample

in class

SampleModel

**Parameters:**
- x

- The X coordinate of the pixel location.
- y

- The Y coordinate of the pixel location.
- b

- The band to set.
- s

- The input sample as an int.
- data

- The DataBuffer containing the image data.

**See Also:**
- getSample(int, int, int, DataBuffer)

---

#### public void setSamples​(int x,
int y,
int w,
int h,
int b,
int[] iArray,

DataBuffer
data)

Sets the samples in the specified band for the specified rectangle
of pixels from an int array containing one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Overrides:**
- setSamples

in class

SampleModel

**Parameters:**
- x

- The X coordinate of the upper left pixel location.
- y

- The Y coordinate of the upper left pixel location.
- w

- The width of the pixel rectangle.
- h

- The height of the pixel rectangle.
- b

- The band to set.
- iArray

- The input samples in an int array.
- data

- The DataBuffer containing the image data.

**See Also:**
- getSamples(int, int, int, int, int, int[], DataBuffer)

---

### Additional Sections

#### Class SinglePixelPackedSampleModel

java.lang.Object

- java.awt.image.SampleModel
- - java.awt.image.SinglePixelPackedSampleModel

java.awt.image.SampleModel

- java.awt.image.SinglePixelPackedSampleModel

java.awt.image.SinglePixelPackedSampleModel

```java
public class
SinglePixelPackedSampleModel

extends
SampleModel
```

This class represents pixel data packed such that the N samples which make
up a single pixel are stored in a single data array element, and each data
data array element holds samples for only one pixel.
This class supports

TYPE_BYTE

,

TYPE_USHORT

,

TYPE_INT

data types.
All data array elements reside
in the first bank of a DataBuffer. Accessor methods are provided so
that the image data can be manipulated directly. Scanline stride is the
number of data array elements between a given sample and the corresponding
sample in the same column of the next scanline. Bit masks are the masks
required to extract the samples representing the bands of the pixel.
Bit offsets are the offsets in bits into the data array
element of the samples representing the bands of the pixel.

The following code illustrates extracting the bits of the sample
representing band

b

for pixel

x,y

from DataBuffer

data

:

```java
int sample = data.getElem(y * scanlineStride + x);
sample = (sample & bitMasks[b]) >>> bitOffsets[b];
```

public class

SinglePixelPackedSampleModel

extends

SampleModel

This class represents pixel data packed such that the N samples which make
up a single pixel are stored in a single data array element, and each data
data array element holds samples for only one pixel.
This class supports

TYPE_BYTE

,

TYPE_USHORT

,

TYPE_INT

data types.
All data array elements reside
in the first bank of a DataBuffer. Accessor methods are provided so
that the image data can be manipulated directly. Scanline stride is the
number of data array elements between a given sample and the corresponding
sample in the same column of the next scanline. Bit masks are the masks
required to extract the samples representing the bands of the pixel.
Bit offsets are the offsets in bits into the data array
element of the samples representing the bands of the pixel.

The following code illustrates extracting the bits of the sample
representing band

b

for pixel

x,y

from DataBuffer

data

:

```java
int sample = data.getElem(y * scanlineStride + x);
sample = (sample & bitMasks[b]) >>> bitOffsets[b];
```

The following code illustrates extracting the bits of the sample
representing band

b

for pixel

x,y

from DataBuffer

data

:

```java
int sample = data.getElem(y * scanlineStride + x);
sample = (sample & bitMasks[b]) >>> bitOffsets[b];
```

int sample = data.getElem(y * scanlineStride + x);
sample = (sample & bitMasks[b]) >>> bitOffsets[b];

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

SinglePixelPackedSampleModel

​(int dataType,
int w,
int h,
int[] bitMasks)

Constructs a SinglePixelPackedSampleModel with bitMasks.length bands.

SinglePixelPackedSampleModel

​(int dataType,
int w,
int h,
int scanlineStride,
int[] bitMasks)

Constructs a SinglePixelPackedSampleModel with bitMasks.length bands
and a scanline stride equal to scanlineStride data array elements.

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

Creates a new SinglePixelPackedSampleModel with the specified
width and height.

DataBuffer

createDataBuffer

()

Creates a DataBuffer that corresponds to this
SinglePixelPackedSampleModel.

SampleModel

createSubsetSampleModel

​(int[] bands)

This creates a new SinglePixelPackedSampleModel with a subset of the
bands of this SinglePixelPackedSampleModel.

int[]

getBitMasks

()

Returns the bit masks for all bands.

int[]

getBitOffsets

()

Returns the bit offsets into the data array element representing
a pixel for all bands.

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
via the getDataElements and setDataElements methods.

int

getOffset

​(int x,
int y)

Returns the offset (in data array elements) of pixel (x,y).

int[]

getPixel

​(int x,
int y,
int[] iArray,

DataBuffer

data)

Returns all samples in for the specified pixel in an int array.

int[]

getPixels

​(int x,
int y,
int w,
int h,
int[] iArray,

DataBuffer

data)

Returns all samples for the specified rectangle of pixels in
an int array, one sample per array element.

int

getSample

​(int x,
int y,
int b,

DataBuffer

data)

Returns as int the sample in a specified band for the pixel
located at (x,y).

int[]

getSamples

​(int x,
int y,
int w,
int h,
int b,
int[] iArray,

DataBuffer

data)

Returns the samples for a specified band for the specified rectangle
of pixels in an int array, one sample per array element.

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

Returns the scanline stride of this SinglePixelPackedSampleModel.

void

setDataElements

​(int x,
int y,

Object

obj,

DataBuffer

data)

Sets the data for a single pixel in the specified DataBuffer from a
primitive array of type TransferType.

void

setPixel

​(int x,
int y,
int[] iArray,

DataBuffer

data)

Sets a pixel in the DataBuffer using an int array of samples for input.

void

setPixels

​(int x,
int y,
int w,
int h,
int[] iArray,

DataBuffer

data)

Sets all samples for a rectangle of pixels from an int array containing
one sample per array element.

void

setSample

​(int x,
int y,
int b,
int s,

DataBuffer

data)

Sets a sample in the specified band for the pixel located at (x,y)
in the DataBuffer using an int for input.

void

setSamples

​(int x,
int y,
int w,
int h,
int b,
int[] iArray,

DataBuffer

data)

Sets the samples in the specified band for the specified rectangle
of pixels from an int array containing one sample per array element.

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

getSampleDouble

,

getSampleFloat

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

setSample

,

setSample

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

SinglePixelPackedSampleModel

​(int dataType,
int w,
int h,
int[] bitMasks)

Constructs a SinglePixelPackedSampleModel with bitMasks.length bands.

SinglePixelPackedSampleModel

​(int dataType,
int w,
int h,
int scanlineStride,
int[] bitMasks)

Constructs a SinglePixelPackedSampleModel with bitMasks.length bands
and a scanline stride equal to scanlineStride data array elements.

---

#### Constructor Summary

Constructs a SinglePixelPackedSampleModel with bitMasks.length bands.

Constructs a SinglePixelPackedSampleModel with bitMasks.length bands
and a scanline stride equal to scanlineStride data array elements.

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

Creates a new SinglePixelPackedSampleModel with the specified
width and height.

DataBuffer

createDataBuffer

()

Creates a DataBuffer that corresponds to this
SinglePixelPackedSampleModel.

SampleModel

createSubsetSampleModel

​(int[] bands)

This creates a new SinglePixelPackedSampleModel with a subset of the
bands of this SinglePixelPackedSampleModel.

int[]

getBitMasks

()

Returns the bit masks for all bands.

int[]

getBitOffsets

()

Returns the bit offsets into the data array element representing
a pixel for all bands.

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
via the getDataElements and setDataElements methods.

int

getOffset

​(int x,
int y)

Returns the offset (in data array elements) of pixel (x,y).

int[]

getPixel

​(int x,
int y,
int[] iArray,

DataBuffer

data)

Returns all samples in for the specified pixel in an int array.

int[]

getPixels

​(int x,
int y,
int w,
int h,
int[] iArray,

DataBuffer

data)

Returns all samples for the specified rectangle of pixels in
an int array, one sample per array element.

int

getSample

​(int x,
int y,
int b,

DataBuffer

data)

Returns as int the sample in a specified band for the pixel
located at (x,y).

int[]

getSamples

​(int x,
int y,
int w,
int h,
int b,
int[] iArray,

DataBuffer

data)

Returns the samples for a specified band for the specified rectangle
of pixels in an int array, one sample per array element.

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

Returns the scanline stride of this SinglePixelPackedSampleModel.

void

setDataElements

​(int x,
int y,

Object

obj,

DataBuffer

data)

Sets the data for a single pixel in the specified DataBuffer from a
primitive array of type TransferType.

void

setPixel

​(int x,
int y,
int[] iArray,

DataBuffer

data)

Sets a pixel in the DataBuffer using an int array of samples for input.

void

setPixels

​(int x,
int y,
int w,
int h,
int[] iArray,

DataBuffer

data)

Sets all samples for a rectangle of pixels from an int array containing
one sample per array element.

void

setSample

​(int x,
int y,
int b,
int s,

DataBuffer

data)

Sets a sample in the specified band for the pixel located at (x,y)
in the DataBuffer using an int for input.

void

setSamples

​(int x,
int y,
int w,
int h,
int b,
int[] iArray,

DataBuffer

data)

Sets the samples in the specified band for the specified rectangle
of pixels from an int array containing one sample per array element.

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

getSampleDouble

,

getSampleFloat

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

setSample

,

setSample

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

Creates a new SinglePixelPackedSampleModel with the specified
width and height.

Creates a DataBuffer that corresponds to this
SinglePixelPackedSampleModel.

This creates a new SinglePixelPackedSampleModel with a subset of the
bands of this SinglePixelPackedSampleModel.

Returns the bit masks for all bands.

Returns the bit offsets into the data array element representing
a pixel for all bands.

Returns data for a single pixel in a primitive array of type
TransferType.

Returns the number of data elements needed to transfer one pixel
via the getDataElements and setDataElements methods.

Returns the offset (in data array elements) of pixel (x,y).

Returns all samples in for the specified pixel in an int array.

Returns all samples for the specified rectangle of pixels in
an int array, one sample per array element.

Returns as int the sample in a specified band for the pixel
located at (x,y).

Returns the samples for a specified band for the specified rectangle
of pixels in an int array, one sample per array element.

Returns the number of bits per sample for all bands.

Returns the number of bits per sample for the specified band.

Returns the scanline stride of this SinglePixelPackedSampleModel.

Sets the data for a single pixel in the specified DataBuffer from a
primitive array of type TransferType.

Sets a pixel in the DataBuffer using an int array of samples for input.

Sets all samples for a rectangle of pixels from an int array containing
one sample per array element.

Sets a sample in the specified band for the pixel located at (x,y)
in the DataBuffer using an int for input.

Sets the samples in the specified band for the specified rectangle
of pixels from an int array containing one sample per array element.

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

getSampleDouble

,

getSampleFloat

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

setSample

,

setSample

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

- SinglePixelPackedSampleModel

```java
public SinglePixelPackedSampleModel​(int dataType,
int w,
int h,
int[] bitMasks)
```

Constructs a SinglePixelPackedSampleModel with bitMasks.length bands.
Each sample is stored in a data array element in the position of
its corresponding bit mask. Each bit mask must be contiguous and
masks must not overlap. Bit masks exceeding data type capacity are
truncated.

**Parameters:** dataType

- The data type for storing samples.
**Parameters:** w

- The width (in pixels) of the region of the
image data described.
**Parameters:** h

- The height (in pixels) of the region of the
image data described.
**Parameters:** bitMasks

- The bit masks for all bands.
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

- SinglePixelPackedSampleModel

```java
public SinglePixelPackedSampleModel​(int dataType,
int w,
int h,
int scanlineStride,
int[] bitMasks)
```

Constructs a SinglePixelPackedSampleModel with bitMasks.length bands
and a scanline stride equal to scanlineStride data array elements.
Each sample is stored in a data array element in the position of
its corresponding bit mask. Each bit mask must be contiguous and
masks must not overlap. Bit masks exceeding data type capacity are
truncated.

**Parameters:** dataType

- The data type for storing samples.
**Parameters:** w

- The width (in pixels) of the region of
image data described.
**Parameters:** h

- The height (in pixels) of the region of
image data described.
**Parameters:** scanlineStride

- The line stride of the image data.
**Parameters:** bitMasks

- The bit masks for all bands.
**Throws:** IllegalArgumentException

- if

w

or

h

is not greater than 0
**Throws:** IllegalArgumentException

- if any mask in

bitMask

is not contiguous
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

- getNumDataElements

```java
public int getNumDataElements()
```

Returns the number of data elements needed to transfer one pixel
via the getDataElements and setDataElements methods.
For a SinglePixelPackedSampleModel, this is one.

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

- createCompatibleSampleModel

```java
public
SampleModel
createCompatibleSampleModel​(int w,
int h)
```

Creates a new SinglePixelPackedSampleModel with the specified
width and height. The new SinglePixelPackedSampleModel will have the
same storage data type and bit masks as this
SinglePixelPackedSampleModel.

**Specified by:** createCompatibleSampleModel

in class

SampleModel
**Parameters:** w

- the width of the resulting

SampleModel
**Parameters:** h

- the height of the resulting

SampleModel
**Returns:** a

SinglePixelPackedSampleModel

with the
specified width and height.
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

Creates a DataBuffer that corresponds to this
SinglePixelPackedSampleModel. The DataBuffer's data type and size
will be consistent with this SinglePixelPackedSampleModel. The
DataBuffer will have a single bank.

**Specified by:** createDataBuffer

in class

SampleModel
**Returns:** a

DataBuffer

corresponding to this

SampleModel

.

- getSampleSize

```java
public int[] getSampleSize()
```

Returns the number of bits per sample for all bands.

**Specified by:** getSampleSize

in class

SampleModel
**Returns:** the size of samples for all bands.

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
**Returns:** the size of the samples of the specified band.

- getOffset

```java
public int getOffset​(int x,
int y)
```

Returns the offset (in data array elements) of pixel (x,y).
The data element containing pixel

x,y

can be retrieved from a DataBuffer

data

with a
SinglePixelPackedSampleModel

sppsm

as:

```java
data.getElem(sppsm.getOffset(x, y));
```

**Parameters:** x

- the X coordinate of the specified pixel
**Parameters:** y

- the Y coordinate of the specified pixel
**Returns:** the offset of the specified pixel.

- getBitOffsets

```java
public int[] getBitOffsets()
```

Returns the bit offsets into the data array element representing
a pixel for all bands.

**Returns:** the bit offsets representing a pixel for all bands.

- getBitMasks

```java
public int[] getBitMasks()
```

Returns the bit masks for all bands.

**Returns:** the bit masks for all bands.

- getScanlineStride

```java
public int getScanlineStride()
```

Returns the scanline stride of this SinglePixelPackedSampleModel.

**Returns:** the scanline stride of this

SinglePixelPackedSampleModel

.

- createSubsetSampleModel

```java
public
SampleModel
createSubsetSampleModel​(int[] bands)
```

This creates a new SinglePixelPackedSampleModel with a subset of the
bands of this SinglePixelPackedSampleModel. The new
SinglePixelPackedSampleModel can be used with any DataBuffer that the
existing SinglePixelPackedSampleModel can be used with. The new
SinglePixelPackedSampleModel/DataBuffer combination will represent
an image with a subset of the bands of the original
SinglePixelPackedSampleModel/DataBuffer combination.

**Specified by:** createSubsetSampleModel

in class

SampleModel
**Parameters:** bands

- the subset of bands of this

SampleModel
**Returns:** a

SampleModel

with a subset of bands of this

SampleModel

.
**Throws:** RasterFormatException

- if the length of the bands argument is
greater than the number of bands in
the sample model.

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
TransferType. For a SinglePixelPackedSampleModel, the array will
have one element, and the type will be the same as the storage
data type. Generally, obj
should be passed in as null, so that the Object will be created
automatically and will be of the right primitive data type.

The following code illustrates transferring data for one pixel from
DataBuffer

db1

, whose storage layout is described by
SinglePixelPackedSampleModel

sppsm1

, to
DataBuffer

db2

, whose storage layout is described by
SinglePixelPackedSampleModel

sppsm2

.
The transfer will generally be more efficient than using
getPixel/setPixel.

```java
SinglePixelPackedSampleModel sppsm1, sppsm2;
DataBufferInt db1, db2;
sppsm2.setDataElements(x, y, sppsm1.getDataElements(x, y, null,
db1), db2);
```

Using getDataElements/setDataElements to transfer between two
DataBuffer/SampleModel pairs is legitimate if the SampleModels have
the same number of bands, corresponding bands have the same number of
bits per sample, and the TransferTypes are the same.

If obj is non-null, it should be a primitive array of type TransferType.
Otherwise, a ClassCastException is thrown. An
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds, or if obj is non-null and is not large enough to hold
the pixel data.

**Specified by:** getDataElements

in class

SampleModel
**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** obj

- If non-null, a primitive array in which to return
the pixel data.
**Parameters:** data

- The DataBuffer containing the image data.
**Returns:** the data for the specified pixel.
**See Also:** setDataElements(int, int, Object, DataBuffer)

- getPixel

```java
public int[] getPixel​(int x,
int y,
int[] iArray,

DataBuffer
data)
```

Returns all samples in for the specified pixel in an int array.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Overrides:** getPixel

in class

SampleModel
**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** iArray

- If non-null, returns the samples in this array
**Parameters:** data

- The DataBuffer containing the image data.
**Returns:** all samples for the specified pixel.
**See Also:** setPixel(int, int, int[], DataBuffer)

- getPixels

```java
public int[] getPixels​(int x,
int y,
int w,
int h,
int[] iArray,

DataBuffer
data)
```

Returns all samples for the specified rectangle of pixels in
an int array, one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Overrides:** getPixels

in class

SampleModel
**Parameters:** x

- The X coordinate of the upper left pixel location.
**Parameters:** y

- The Y coordinate of the upper left pixel location.
**Parameters:** w

- The width of the pixel rectangle.
**Parameters:** h

- The height of the pixel rectangle.
**Parameters:** iArray

- If non-null, returns the samples in this array.
**Parameters:** data

- The DataBuffer containing the image data.
**Returns:** all samples for the specified region of pixels.
**See Also:** setPixels(int, int, int, int, int[], DataBuffer)

- getSample

```java
public int getSample​(int x,
int y,
int b,

DataBuffer
data)
```

Returns as int the sample in a specified band for the pixel
located at (x,y).
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Specified by:** getSample

in class

SampleModel
**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** b

- The band to return.
**Parameters:** data

- The DataBuffer containing the image data.
**Returns:** the sample in a specified band for the specified
pixel.
**See Also:** setSample(int, int, int, int, DataBuffer)

- getSamples

```java
public int[] getSamples​(int x,
int y,
int w,
int h,
int b,
int[] iArray,

DataBuffer
data)
```

Returns the samples for a specified band for the specified rectangle
of pixels in an int array, one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Overrides:** getSamples

in class

SampleModel
**Parameters:** x

- The X coordinate of the upper left pixel location.
**Parameters:** y

- The Y coordinate of the upper left pixel location.
**Parameters:** w

- The width of the pixel rectangle.
**Parameters:** h

- The height of the pixel rectangle.
**Parameters:** b

- The band to return.
**Parameters:** iArray

- If non-null, returns the samples in this array.
**Parameters:** data

- The DataBuffer containing the image data.
**Returns:** the samples for the specified band for the specified
region of pixels.
**See Also:** setSamples(int, int, int, int, int, int[], DataBuffer)

- setDataElements

```java
public void setDataElements​(int x,
int y,

Object
obj,

DataBuffer
data)
```

Sets the data for a single pixel in the specified DataBuffer from a
primitive array of type TransferType. For a
SinglePixelPackedSampleModel, only the first element of the array
will hold valid data, and the type of the array must be the same as
the storage data type of the SinglePixelPackedSampleModel.

The following code illustrates transferring data for one pixel from
DataBuffer

db1

, whose storage layout is described by
SinglePixelPackedSampleModel

sppsm1

,
to DataBuffer

db2

, whose storage layout is described by
SinglePixelPackedSampleModel

sppsm2

.
The transfer will generally be more efficient than using
getPixel/setPixel.

```java
SinglePixelPackedSampleModel sppsm1, sppsm2;
DataBufferInt db1, db2;
sppsm2.setDataElements(x, y, sppsm1.getDataElements(x, y, null,
db1), db2);
```

Using getDataElements/setDataElements to transfer between two
DataBuffer/SampleModel pairs is legitimate if the SampleModels have
the same number of bands, corresponding bands have the same number of
bits per sample, and the TransferTypes are the same.

obj must be a primitive array of type TransferType. Otherwise,
a ClassCastException is thrown. An
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds, or if obj is not large enough to hold the pixel data.

**Specified by:** setDataElements

in class

SampleModel
**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** obj

- A primitive array containing pixel data.
**Parameters:** data

- The DataBuffer containing the image data.
**See Also:** getDataElements(int, int, Object, DataBuffer)

- setPixel

```java
public void setPixel​(int x,
int y,
int[] iArray,

DataBuffer
data)
```

Sets a pixel in the DataBuffer using an int array of samples for input.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Overrides:** setPixel

in class

SampleModel
**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** iArray

- The input samples in an int array.
**Parameters:** data

- The DataBuffer containing the image data.
**See Also:** getPixel(int, int, int[], DataBuffer)

- setPixels

```java
public void setPixels​(int x,
int y,
int w,
int h,
int[] iArray,

DataBuffer
data)
```

Sets all samples for a rectangle of pixels from an int array containing
one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Overrides:** setPixels

in class

SampleModel
**Parameters:** x

- The X coordinate of the upper left pixel location.
**Parameters:** y

- The Y coordinate of the upper left pixel location.
**Parameters:** w

- The width of the pixel rectangle.
**Parameters:** h

- The height of the pixel rectangle.
**Parameters:** iArray

- The input samples in an int array.
**Parameters:** data

- The DataBuffer containing the image data.
**See Also:** getPixels(int, int, int, int, int[], DataBuffer)

- setSample

```java
public void setSample​(int x,
int y,
int b,
int s,

DataBuffer
data)
```

Sets a sample in the specified band for the pixel located at (x,y)
in the DataBuffer using an int for input.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Specified by:** setSample

in class

SampleModel
**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** b

- The band to set.
**Parameters:** s

- The input sample as an int.
**Parameters:** data

- The DataBuffer containing the image data.
**See Also:** getSample(int, int, int, DataBuffer)

- setSamples

```java
public void setSamples​(int x,
int y,
int w,
int h,
int b,
int[] iArray,

DataBuffer
data)
```

Sets the samples in the specified band for the specified rectangle
of pixels from an int array containing one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Overrides:** setSamples

in class

SampleModel
**Parameters:** x

- The X coordinate of the upper left pixel location.
**Parameters:** y

- The Y coordinate of the upper left pixel location.
**Parameters:** w

- The width of the pixel rectangle.
**Parameters:** h

- The height of the pixel rectangle.
**Parameters:** b

- The band to set.
**Parameters:** iArray

- The input samples in an int array.
**Parameters:** data

- The DataBuffer containing the image data.
**See Also:** getSamples(int, int, int, int, int, int[], DataBuffer)

Constructor Detail

- SinglePixelPackedSampleModel

```java
public SinglePixelPackedSampleModel​(int dataType,
int w,
int h,
int[] bitMasks)
```

Constructs a SinglePixelPackedSampleModel with bitMasks.length bands.
Each sample is stored in a data array element in the position of
its corresponding bit mask. Each bit mask must be contiguous and
masks must not overlap. Bit masks exceeding data type capacity are
truncated.

**Parameters:** dataType

- The data type for storing samples.
**Parameters:** w

- The width (in pixels) of the region of the
image data described.
**Parameters:** h

- The height (in pixels) of the region of the
image data described.
**Parameters:** bitMasks

- The bit masks for all bands.
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

- SinglePixelPackedSampleModel

```java
public SinglePixelPackedSampleModel​(int dataType,
int w,
int h,
int scanlineStride,
int[] bitMasks)
```

Constructs a SinglePixelPackedSampleModel with bitMasks.length bands
and a scanline stride equal to scanlineStride data array elements.
Each sample is stored in a data array element in the position of
its corresponding bit mask. Each bit mask must be contiguous and
masks must not overlap. Bit masks exceeding data type capacity are
truncated.

**Parameters:** dataType

- The data type for storing samples.
**Parameters:** w

- The width (in pixels) of the region of
image data described.
**Parameters:** h

- The height (in pixels) of the region of
image data described.
**Parameters:** scanlineStride

- The line stride of the image data.
**Parameters:** bitMasks

- The bit masks for all bands.
**Throws:** IllegalArgumentException

- if

w

or

h

is not greater than 0
**Throws:** IllegalArgumentException

- if any mask in

bitMask

is not contiguous
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

SinglePixelPackedSampleModel

```java
public SinglePixelPackedSampleModel​(int dataType,
int w,
int h,
int[] bitMasks)
```

Constructs a SinglePixelPackedSampleModel with bitMasks.length bands.
Each sample is stored in a data array element in the position of
its corresponding bit mask. Each bit mask must be contiguous and
masks must not overlap. Bit masks exceeding data type capacity are
truncated.

**Parameters:** dataType

- The data type for storing samples.
**Parameters:** w

- The width (in pixels) of the region of the
image data described.
**Parameters:** h

- The height (in pixels) of the region of the
image data described.
**Parameters:** bitMasks

- The bit masks for all bands.
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

#### SinglePixelPackedSampleModel

public SinglePixelPackedSampleModel​(int dataType,
int w,
int h,
int[] bitMasks)

Constructs a SinglePixelPackedSampleModel with bitMasks.length bands.
Each sample is stored in a data array element in the position of
its corresponding bit mask. Each bit mask must be contiguous and
masks must not overlap. Bit masks exceeding data type capacity are
truncated.

SinglePixelPackedSampleModel

```java
public SinglePixelPackedSampleModel​(int dataType,
int w,
int h,
int scanlineStride,
int[] bitMasks)
```

Constructs a SinglePixelPackedSampleModel with bitMasks.length bands
and a scanline stride equal to scanlineStride data array elements.
Each sample is stored in a data array element in the position of
its corresponding bit mask. Each bit mask must be contiguous and
masks must not overlap. Bit masks exceeding data type capacity are
truncated.

**Parameters:** dataType

- The data type for storing samples.
**Parameters:** w

- The width (in pixels) of the region of
image data described.
**Parameters:** h

- The height (in pixels) of the region of
image data described.
**Parameters:** scanlineStride

- The line stride of the image data.
**Parameters:** bitMasks

- The bit masks for all bands.
**Throws:** IllegalArgumentException

- if

w

or

h

is not greater than 0
**Throws:** IllegalArgumentException

- if any mask in

bitMask

is not contiguous
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

#### SinglePixelPackedSampleModel

public SinglePixelPackedSampleModel​(int dataType,
int w,
int h,
int scanlineStride,
int[] bitMasks)

Constructs a SinglePixelPackedSampleModel with bitMasks.length bands
and a scanline stride equal to scanlineStride data array elements.
Each sample is stored in a data array element in the position of
its corresponding bit mask. Each bit mask must be contiguous and
masks must not overlap. Bit masks exceeding data type capacity are
truncated.

Method Detail

- getNumDataElements

```java
public int getNumDataElements()
```

Returns the number of data elements needed to transfer one pixel
via the getDataElements and setDataElements methods.
For a SinglePixelPackedSampleModel, this is one.

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

- createCompatibleSampleModel

```java
public
SampleModel
createCompatibleSampleModel​(int w,
int h)
```

Creates a new SinglePixelPackedSampleModel with the specified
width and height. The new SinglePixelPackedSampleModel will have the
same storage data type and bit masks as this
SinglePixelPackedSampleModel.

**Specified by:** createCompatibleSampleModel

in class

SampleModel
**Parameters:** w

- the width of the resulting

SampleModel
**Parameters:** h

- the height of the resulting

SampleModel
**Returns:** a

SinglePixelPackedSampleModel

with the
specified width and height.
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

Creates a DataBuffer that corresponds to this
SinglePixelPackedSampleModel. The DataBuffer's data type and size
will be consistent with this SinglePixelPackedSampleModel. The
DataBuffer will have a single bank.

**Specified by:** createDataBuffer

in class

SampleModel
**Returns:** a

DataBuffer

corresponding to this

SampleModel

.

- getSampleSize

```java
public int[] getSampleSize()
```

Returns the number of bits per sample for all bands.

**Specified by:** getSampleSize

in class

SampleModel
**Returns:** the size of samples for all bands.

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
**Returns:** the size of the samples of the specified band.

- getOffset

```java
public int getOffset​(int x,
int y)
```

Returns the offset (in data array elements) of pixel (x,y).
The data element containing pixel

x,y

can be retrieved from a DataBuffer

data

with a
SinglePixelPackedSampleModel

sppsm

as:

```java
data.getElem(sppsm.getOffset(x, y));
```

**Parameters:** x

- the X coordinate of the specified pixel
**Parameters:** y

- the Y coordinate of the specified pixel
**Returns:** the offset of the specified pixel.

- getBitOffsets

```java
public int[] getBitOffsets()
```

Returns the bit offsets into the data array element representing
a pixel for all bands.

**Returns:** the bit offsets representing a pixel for all bands.

- getBitMasks

```java
public int[] getBitMasks()
```

Returns the bit masks for all bands.

**Returns:** the bit masks for all bands.

- getScanlineStride

```java
public int getScanlineStride()
```

Returns the scanline stride of this SinglePixelPackedSampleModel.

**Returns:** the scanline stride of this

SinglePixelPackedSampleModel

.

- createSubsetSampleModel

```java
public
SampleModel
createSubsetSampleModel​(int[] bands)
```

This creates a new SinglePixelPackedSampleModel with a subset of the
bands of this SinglePixelPackedSampleModel. The new
SinglePixelPackedSampleModel can be used with any DataBuffer that the
existing SinglePixelPackedSampleModel can be used with. The new
SinglePixelPackedSampleModel/DataBuffer combination will represent
an image with a subset of the bands of the original
SinglePixelPackedSampleModel/DataBuffer combination.

**Specified by:** createSubsetSampleModel

in class

SampleModel
**Parameters:** bands

- the subset of bands of this

SampleModel
**Returns:** a

SampleModel

with a subset of bands of this

SampleModel

.
**Throws:** RasterFormatException

- if the length of the bands argument is
greater than the number of bands in
the sample model.

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
TransferType. For a SinglePixelPackedSampleModel, the array will
have one element, and the type will be the same as the storage
data type. Generally, obj
should be passed in as null, so that the Object will be created
automatically and will be of the right primitive data type.

The following code illustrates transferring data for one pixel from
DataBuffer

db1

, whose storage layout is described by
SinglePixelPackedSampleModel

sppsm1

, to
DataBuffer

db2

, whose storage layout is described by
SinglePixelPackedSampleModel

sppsm2

.
The transfer will generally be more efficient than using
getPixel/setPixel.

```java
SinglePixelPackedSampleModel sppsm1, sppsm2;
DataBufferInt db1, db2;
sppsm2.setDataElements(x, y, sppsm1.getDataElements(x, y, null,
db1), db2);
```

Using getDataElements/setDataElements to transfer between two
DataBuffer/SampleModel pairs is legitimate if the SampleModels have
the same number of bands, corresponding bands have the same number of
bits per sample, and the TransferTypes are the same.

If obj is non-null, it should be a primitive array of type TransferType.
Otherwise, a ClassCastException is thrown. An
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds, or if obj is non-null and is not large enough to hold
the pixel data.

**Specified by:** getDataElements

in class

SampleModel
**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** obj

- If non-null, a primitive array in which to return
the pixel data.
**Parameters:** data

- The DataBuffer containing the image data.
**Returns:** the data for the specified pixel.
**See Also:** setDataElements(int, int, Object, DataBuffer)

- getPixel

```java
public int[] getPixel​(int x,
int y,
int[] iArray,

DataBuffer
data)
```

Returns all samples in for the specified pixel in an int array.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Overrides:** getPixel

in class

SampleModel
**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** iArray

- If non-null, returns the samples in this array
**Parameters:** data

- The DataBuffer containing the image data.
**Returns:** all samples for the specified pixel.
**See Also:** setPixel(int, int, int[], DataBuffer)

- getPixels

```java
public int[] getPixels​(int x,
int y,
int w,
int h,
int[] iArray,

DataBuffer
data)
```

Returns all samples for the specified rectangle of pixels in
an int array, one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Overrides:** getPixels

in class

SampleModel
**Parameters:** x

- The X coordinate of the upper left pixel location.
**Parameters:** y

- The Y coordinate of the upper left pixel location.
**Parameters:** w

- The width of the pixel rectangle.
**Parameters:** h

- The height of the pixel rectangle.
**Parameters:** iArray

- If non-null, returns the samples in this array.
**Parameters:** data

- The DataBuffer containing the image data.
**Returns:** all samples for the specified region of pixels.
**See Also:** setPixels(int, int, int, int, int[], DataBuffer)

- getSample

```java
public int getSample​(int x,
int y,
int b,

DataBuffer
data)
```

Returns as int the sample in a specified band for the pixel
located at (x,y).
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Specified by:** getSample

in class

SampleModel
**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** b

- The band to return.
**Parameters:** data

- The DataBuffer containing the image data.
**Returns:** the sample in a specified band for the specified
pixel.
**See Also:** setSample(int, int, int, int, DataBuffer)

- getSamples

```java
public int[] getSamples​(int x,
int y,
int w,
int h,
int b,
int[] iArray,

DataBuffer
data)
```

Returns the samples for a specified band for the specified rectangle
of pixels in an int array, one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Overrides:** getSamples

in class

SampleModel
**Parameters:** x

- The X coordinate of the upper left pixel location.
**Parameters:** y

- The Y coordinate of the upper left pixel location.
**Parameters:** w

- The width of the pixel rectangle.
**Parameters:** h

- The height of the pixel rectangle.
**Parameters:** b

- The band to return.
**Parameters:** iArray

- If non-null, returns the samples in this array.
**Parameters:** data

- The DataBuffer containing the image data.
**Returns:** the samples for the specified band for the specified
region of pixels.
**See Also:** setSamples(int, int, int, int, int, int[], DataBuffer)

- setDataElements

```java
public void setDataElements​(int x,
int y,

Object
obj,

DataBuffer
data)
```

Sets the data for a single pixel in the specified DataBuffer from a
primitive array of type TransferType. For a
SinglePixelPackedSampleModel, only the first element of the array
will hold valid data, and the type of the array must be the same as
the storage data type of the SinglePixelPackedSampleModel.

The following code illustrates transferring data for one pixel from
DataBuffer

db1

, whose storage layout is described by
SinglePixelPackedSampleModel

sppsm1

,
to DataBuffer

db2

, whose storage layout is described by
SinglePixelPackedSampleModel

sppsm2

.
The transfer will generally be more efficient than using
getPixel/setPixel.

```java
SinglePixelPackedSampleModel sppsm1, sppsm2;
DataBufferInt db1, db2;
sppsm2.setDataElements(x, y, sppsm1.getDataElements(x, y, null,
db1), db2);
```

Using getDataElements/setDataElements to transfer between two
DataBuffer/SampleModel pairs is legitimate if the SampleModels have
the same number of bands, corresponding bands have the same number of
bits per sample, and the TransferTypes are the same.

obj must be a primitive array of type TransferType. Otherwise,
a ClassCastException is thrown. An
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds, or if obj is not large enough to hold the pixel data.

**Specified by:** setDataElements

in class

SampleModel
**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** obj

- A primitive array containing pixel data.
**Parameters:** data

- The DataBuffer containing the image data.
**See Also:** getDataElements(int, int, Object, DataBuffer)

- setPixel

```java
public void setPixel​(int x,
int y,
int[] iArray,

DataBuffer
data)
```

Sets a pixel in the DataBuffer using an int array of samples for input.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Overrides:** setPixel

in class

SampleModel
**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** iArray

- The input samples in an int array.
**Parameters:** data

- The DataBuffer containing the image data.
**See Also:** getPixel(int, int, int[], DataBuffer)

- setPixels

```java
public void setPixels​(int x,
int y,
int w,
int h,
int[] iArray,

DataBuffer
data)
```

Sets all samples for a rectangle of pixels from an int array containing
one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Overrides:** setPixels

in class

SampleModel
**Parameters:** x

- The X coordinate of the upper left pixel location.
**Parameters:** y

- The Y coordinate of the upper left pixel location.
**Parameters:** w

- The width of the pixel rectangle.
**Parameters:** h

- The height of the pixel rectangle.
**Parameters:** iArray

- The input samples in an int array.
**Parameters:** data

- The DataBuffer containing the image data.
**See Also:** getPixels(int, int, int, int, int[], DataBuffer)

- setSample

```java
public void setSample​(int x,
int y,
int b,
int s,

DataBuffer
data)
```

Sets a sample in the specified band for the pixel located at (x,y)
in the DataBuffer using an int for input.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Specified by:** setSample

in class

SampleModel
**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** b

- The band to set.
**Parameters:** s

- The input sample as an int.
**Parameters:** data

- The DataBuffer containing the image data.
**See Also:** getSample(int, int, int, DataBuffer)

- setSamples

```java
public void setSamples​(int x,
int y,
int w,
int h,
int b,
int[] iArray,

DataBuffer
data)
```

Sets the samples in the specified band for the specified rectangle
of pixels from an int array containing one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Overrides:** setSamples

in class

SampleModel
**Parameters:** x

- The X coordinate of the upper left pixel location.
**Parameters:** y

- The Y coordinate of the upper left pixel location.
**Parameters:** w

- The width of the pixel rectangle.
**Parameters:** h

- The height of the pixel rectangle.
**Parameters:** b

- The band to set.
**Parameters:** iArray

- The input samples in an int array.
**Parameters:** data

- The DataBuffer containing the image data.
**See Also:** getSamples(int, int, int, int, int, int[], DataBuffer)

---

#### Method Detail

getNumDataElements

```java
public int getNumDataElements()
```

Returns the number of data elements needed to transfer one pixel
via the getDataElements and setDataElements methods.
For a SinglePixelPackedSampleModel, this is one.

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
via the getDataElements and setDataElements methods.
For a SinglePixelPackedSampleModel, this is one.

createCompatibleSampleModel

```java
public
SampleModel
createCompatibleSampleModel​(int w,
int h)
```

Creates a new SinglePixelPackedSampleModel with the specified
width and height. The new SinglePixelPackedSampleModel will have the
same storage data type and bit masks as this
SinglePixelPackedSampleModel.

**Specified by:** createCompatibleSampleModel

in class

SampleModel
**Parameters:** w

- the width of the resulting

SampleModel
**Parameters:** h

- the height of the resulting

SampleModel
**Returns:** a

SinglePixelPackedSampleModel

with the
specified width and height.
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

Creates a new SinglePixelPackedSampleModel with the specified
width and height. The new SinglePixelPackedSampleModel will have the
same storage data type and bit masks as this
SinglePixelPackedSampleModel.

createDataBuffer

```java
public
DataBuffer
createDataBuffer()
```

Creates a DataBuffer that corresponds to this
SinglePixelPackedSampleModel. The DataBuffer's data type and size
will be consistent with this SinglePixelPackedSampleModel. The
DataBuffer will have a single bank.

**Specified by:** createDataBuffer

in class

SampleModel
**Returns:** a

DataBuffer

corresponding to this

SampleModel

.

---

#### createDataBuffer

public

DataBuffer

createDataBuffer()

Creates a DataBuffer that corresponds to this
SinglePixelPackedSampleModel. The DataBuffer's data type and size
will be consistent with this SinglePixelPackedSampleModel. The
DataBuffer will have a single bank.

getSampleSize

```java
public int[] getSampleSize()
```

Returns the number of bits per sample for all bands.

**Specified by:** getSampleSize

in class

SampleModel
**Returns:** the size of samples for all bands.

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
**Returns:** the size of the samples of the specified band.

---

#### getSampleSize

public int getSampleSize​(int band)

Returns the number of bits per sample for the specified band.

getOffset

```java
public int getOffset​(int x,
int y)
```

Returns the offset (in data array elements) of pixel (x,y).
The data element containing pixel

x,y

can be retrieved from a DataBuffer

data

with a
SinglePixelPackedSampleModel

sppsm

as:

```java
data.getElem(sppsm.getOffset(x, y));
```

**Parameters:** x

- the X coordinate of the specified pixel
**Parameters:** y

- the Y coordinate of the specified pixel
**Returns:** the offset of the specified pixel.

---

#### getOffset

public int getOffset​(int x,
int y)

Returns the offset (in data array elements) of pixel (x,y).
The data element containing pixel

x,y

can be retrieved from a DataBuffer

data

with a
SinglePixelPackedSampleModel

sppsm

as:

```java
data.getElem(sppsm.getOffset(x, y));
```

data.getElem(sppsm.getOffset(x, y));

getBitOffsets

```java
public int[] getBitOffsets()
```

Returns the bit offsets into the data array element representing
a pixel for all bands.

**Returns:** the bit offsets representing a pixel for all bands.

---

#### getBitOffsets

public int[] getBitOffsets()

Returns the bit offsets into the data array element representing
a pixel for all bands.

getBitMasks

```java
public int[] getBitMasks()
```

Returns the bit masks for all bands.

**Returns:** the bit masks for all bands.

---

#### getBitMasks

public int[] getBitMasks()

Returns the bit masks for all bands.

getScanlineStride

```java
public int getScanlineStride()
```

Returns the scanline stride of this SinglePixelPackedSampleModel.

**Returns:** the scanline stride of this

SinglePixelPackedSampleModel

.

---

#### getScanlineStride

public int getScanlineStride()

Returns the scanline stride of this SinglePixelPackedSampleModel.

createSubsetSampleModel

```java
public
SampleModel
createSubsetSampleModel​(int[] bands)
```

This creates a new SinglePixelPackedSampleModel with a subset of the
bands of this SinglePixelPackedSampleModel. The new
SinglePixelPackedSampleModel can be used with any DataBuffer that the
existing SinglePixelPackedSampleModel can be used with. The new
SinglePixelPackedSampleModel/DataBuffer combination will represent
an image with a subset of the bands of the original
SinglePixelPackedSampleModel/DataBuffer combination.

**Specified by:** createSubsetSampleModel

in class

SampleModel
**Parameters:** bands

- the subset of bands of this

SampleModel
**Returns:** a

SampleModel

with a subset of bands of this

SampleModel

.
**Throws:** RasterFormatException

- if the length of the bands argument is
greater than the number of bands in
the sample model.

---

#### createSubsetSampleModel

public

SampleModel

createSubsetSampleModel​(int[] bands)

This creates a new SinglePixelPackedSampleModel with a subset of the
bands of this SinglePixelPackedSampleModel. The new
SinglePixelPackedSampleModel can be used with any DataBuffer that the
existing SinglePixelPackedSampleModel can be used with. The new
SinglePixelPackedSampleModel/DataBuffer combination will represent
an image with a subset of the bands of the original
SinglePixelPackedSampleModel/DataBuffer combination.

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
TransferType. For a SinglePixelPackedSampleModel, the array will
have one element, and the type will be the same as the storage
data type. Generally, obj
should be passed in as null, so that the Object will be created
automatically and will be of the right primitive data type.

The following code illustrates transferring data for one pixel from
DataBuffer

db1

, whose storage layout is described by
SinglePixelPackedSampleModel

sppsm1

, to
DataBuffer

db2

, whose storage layout is described by
SinglePixelPackedSampleModel

sppsm2

.
The transfer will generally be more efficient than using
getPixel/setPixel.

```java
SinglePixelPackedSampleModel sppsm1, sppsm2;
DataBufferInt db1, db2;
sppsm2.setDataElements(x, y, sppsm1.getDataElements(x, y, null,
db1), db2);
```

Using getDataElements/setDataElements to transfer between two
DataBuffer/SampleModel pairs is legitimate if the SampleModels have
the same number of bands, corresponding bands have the same number of
bits per sample, and the TransferTypes are the same.

If obj is non-null, it should be a primitive array of type TransferType.
Otherwise, a ClassCastException is thrown. An
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds, or if obj is non-null and is not large enough to hold
the pixel data.

**Specified by:** getDataElements

in class

SampleModel
**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** obj

- If non-null, a primitive array in which to return
the pixel data.
**Parameters:** data

- The DataBuffer containing the image data.
**Returns:** the data for the specified pixel.
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
TransferType. For a SinglePixelPackedSampleModel, the array will
have one element, and the type will be the same as the storage
data type. Generally, obj
should be passed in as null, so that the Object will be created
automatically and will be of the right primitive data type.

The following code illustrates transferring data for one pixel from
DataBuffer

db1

, whose storage layout is described by
SinglePixelPackedSampleModel

sppsm1

, to
DataBuffer

db2

, whose storage layout is described by
SinglePixelPackedSampleModel

sppsm2

.
The transfer will generally be more efficient than using
getPixel/setPixel.

```java
SinglePixelPackedSampleModel sppsm1, sppsm2;
DataBufferInt db1, db2;
sppsm2.setDataElements(x, y, sppsm1.getDataElements(x, y, null,
db1), db2);
```

Using getDataElements/setDataElements to transfer between two
DataBuffer/SampleModel pairs is legitimate if the SampleModels have
the same number of bands, corresponding bands have the same number of
bits per sample, and the TransferTypes are the same.

If obj is non-null, it should be a primitive array of type TransferType.
Otherwise, a ClassCastException is thrown. An
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds, or if obj is non-null and is not large enough to hold
the pixel data.

The following code illustrates transferring data for one pixel from
DataBuffer

db1

, whose storage layout is described by
SinglePixelPackedSampleModel

sppsm1

, to
DataBuffer

db2

, whose storage layout is described by
SinglePixelPackedSampleModel

sppsm2

.
The transfer will generally be more efficient than using
getPixel/setPixel.

```java
SinglePixelPackedSampleModel sppsm1, sppsm2;
DataBufferInt db1, db2;
sppsm2.setDataElements(x, y, sppsm1.getDataElements(x, y, null,
db1), db2);
```

Using getDataElements/setDataElements to transfer between two
DataBuffer/SampleModel pairs is legitimate if the SampleModels have
the same number of bands, corresponding bands have the same number of
bits per sample, and the TransferTypes are the same.

If obj is non-null, it should be a primitive array of type TransferType.
Otherwise, a ClassCastException is thrown. An
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds, or if obj is non-null and is not large enough to hold
the pixel data.

SinglePixelPackedSampleModel sppsm1, sppsm2;
DataBufferInt db1, db2;
sppsm2.setDataElements(x, y, sppsm1.getDataElements(x, y, null,
db1), db2);

If obj is non-null, it should be a primitive array of type TransferType.
Otherwise, a ClassCastException is thrown. An
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds, or if obj is non-null and is not large enough to hold
the pixel data.

getPixel

```java
public int[] getPixel​(int x,
int y,
int[] iArray,

DataBuffer
data)
```

Returns all samples in for the specified pixel in an int array.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Overrides:** getPixel

in class

SampleModel
**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** iArray

- If non-null, returns the samples in this array
**Parameters:** data

- The DataBuffer containing the image data.
**Returns:** all samples for the specified pixel.
**See Also:** setPixel(int, int, int[], DataBuffer)

---

#### getPixel

public int[] getPixel​(int x,
int y,
int[] iArray,

DataBuffer

data)

Returns all samples in for the specified pixel in an int array.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

getPixels

```java
public int[] getPixels​(int x,
int y,
int w,
int h,
int[] iArray,

DataBuffer
data)
```

Returns all samples for the specified rectangle of pixels in
an int array, one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Overrides:** getPixels

in class

SampleModel
**Parameters:** x

- The X coordinate of the upper left pixel location.
**Parameters:** y

- The Y coordinate of the upper left pixel location.
**Parameters:** w

- The width of the pixel rectangle.
**Parameters:** h

- The height of the pixel rectangle.
**Parameters:** iArray

- If non-null, returns the samples in this array.
**Parameters:** data

- The DataBuffer containing the image data.
**Returns:** all samples for the specified region of pixels.
**See Also:** setPixels(int, int, int, int, int[], DataBuffer)

---

#### getPixels

public int[] getPixels​(int x,
int y,
int w,
int h,
int[] iArray,

DataBuffer

data)

Returns all samples for the specified rectangle of pixels in
an int array, one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

getSample

```java
public int getSample​(int x,
int y,
int b,

DataBuffer
data)
```

Returns as int the sample in a specified band for the pixel
located at (x,y).
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Specified by:** getSample

in class

SampleModel
**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** b

- The band to return.
**Parameters:** data

- The DataBuffer containing the image data.
**Returns:** the sample in a specified band for the specified
pixel.
**See Also:** setSample(int, int, int, int, DataBuffer)

---

#### getSample

public int getSample​(int x,
int y,
int b,

DataBuffer

data)

Returns as int the sample in a specified band for the pixel
located at (x,y).
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

getSamples

```java
public int[] getSamples​(int x,
int y,
int w,
int h,
int b,
int[] iArray,

DataBuffer
data)
```

Returns the samples for a specified band for the specified rectangle
of pixels in an int array, one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Overrides:** getSamples

in class

SampleModel
**Parameters:** x

- The X coordinate of the upper left pixel location.
**Parameters:** y

- The Y coordinate of the upper left pixel location.
**Parameters:** w

- The width of the pixel rectangle.
**Parameters:** h

- The height of the pixel rectangle.
**Parameters:** b

- The band to return.
**Parameters:** iArray

- If non-null, returns the samples in this array.
**Parameters:** data

- The DataBuffer containing the image data.
**Returns:** the samples for the specified band for the specified
region of pixels.
**See Also:** setSamples(int, int, int, int, int, int[], DataBuffer)

---

#### getSamples

public int[] getSamples​(int x,
int y,
int w,
int h,
int b,
int[] iArray,

DataBuffer

data)

Returns the samples for a specified band for the specified rectangle
of pixels in an int array, one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

setDataElements

```java
public void setDataElements​(int x,
int y,

Object
obj,

DataBuffer
data)
```

Sets the data for a single pixel in the specified DataBuffer from a
primitive array of type TransferType. For a
SinglePixelPackedSampleModel, only the first element of the array
will hold valid data, and the type of the array must be the same as
the storage data type of the SinglePixelPackedSampleModel.

The following code illustrates transferring data for one pixel from
DataBuffer

db1

, whose storage layout is described by
SinglePixelPackedSampleModel

sppsm1

,
to DataBuffer

db2

, whose storage layout is described by
SinglePixelPackedSampleModel

sppsm2

.
The transfer will generally be more efficient than using
getPixel/setPixel.

```java
SinglePixelPackedSampleModel sppsm1, sppsm2;
DataBufferInt db1, db2;
sppsm2.setDataElements(x, y, sppsm1.getDataElements(x, y, null,
db1), db2);
```

Using getDataElements/setDataElements to transfer between two
DataBuffer/SampleModel pairs is legitimate if the SampleModels have
the same number of bands, corresponding bands have the same number of
bits per sample, and the TransferTypes are the same.

obj must be a primitive array of type TransferType. Otherwise,
a ClassCastException is thrown. An
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds, or if obj is not large enough to hold the pixel data.

**Specified by:** setDataElements

in class

SampleModel
**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** obj

- A primitive array containing pixel data.
**Parameters:** data

- The DataBuffer containing the image data.
**See Also:** getDataElements(int, int, Object, DataBuffer)

---

#### setDataElements

public void setDataElements​(int x,
int y,

Object

obj,

DataBuffer

data)

Sets the data for a single pixel in the specified DataBuffer from a
primitive array of type TransferType. For a
SinglePixelPackedSampleModel, only the first element of the array
will hold valid data, and the type of the array must be the same as
the storage data type of the SinglePixelPackedSampleModel.

The following code illustrates transferring data for one pixel from
DataBuffer

db1

, whose storage layout is described by
SinglePixelPackedSampleModel

sppsm1

,
to DataBuffer

db2

, whose storage layout is described by
SinglePixelPackedSampleModel

sppsm2

.
The transfer will generally be more efficient than using
getPixel/setPixel.

```java
SinglePixelPackedSampleModel sppsm1, sppsm2;
DataBufferInt db1, db2;
sppsm2.setDataElements(x, y, sppsm1.getDataElements(x, y, null,
db1), db2);
```

Using getDataElements/setDataElements to transfer between two
DataBuffer/SampleModel pairs is legitimate if the SampleModels have
the same number of bands, corresponding bands have the same number of
bits per sample, and the TransferTypes are the same.

obj must be a primitive array of type TransferType. Otherwise,
a ClassCastException is thrown. An
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds, or if obj is not large enough to hold the pixel data.

The following code illustrates transferring data for one pixel from
DataBuffer

db1

, whose storage layout is described by
SinglePixelPackedSampleModel

sppsm1

,
to DataBuffer

db2

, whose storage layout is described by
SinglePixelPackedSampleModel

sppsm2

.
The transfer will generally be more efficient than using
getPixel/setPixel.

```java
SinglePixelPackedSampleModel sppsm1, sppsm2;
DataBufferInt db1, db2;
sppsm2.setDataElements(x, y, sppsm1.getDataElements(x, y, null,
db1), db2);
```

Using getDataElements/setDataElements to transfer between two
DataBuffer/SampleModel pairs is legitimate if the SampleModels have
the same number of bands, corresponding bands have the same number of
bits per sample, and the TransferTypes are the same.

obj must be a primitive array of type TransferType. Otherwise,
a ClassCastException is thrown. An
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds, or if obj is not large enough to hold the pixel data.

SinglePixelPackedSampleModel sppsm1, sppsm2;
DataBufferInt db1, db2;
sppsm2.setDataElements(x, y, sppsm1.getDataElements(x, y, null,
db1), db2);

obj must be a primitive array of type TransferType. Otherwise,
a ClassCastException is thrown. An
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds, or if obj is not large enough to hold the pixel data.

setPixel

```java
public void setPixel​(int x,
int y,
int[] iArray,

DataBuffer
data)
```

Sets a pixel in the DataBuffer using an int array of samples for input.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Overrides:** setPixel

in class

SampleModel
**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** iArray

- The input samples in an int array.
**Parameters:** data

- The DataBuffer containing the image data.
**See Also:** getPixel(int, int, int[], DataBuffer)

---

#### setPixel

public void setPixel​(int x,
int y,
int[] iArray,

DataBuffer

data)

Sets a pixel in the DataBuffer using an int array of samples for input.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

setPixels

```java
public void setPixels​(int x,
int y,
int w,
int h,
int[] iArray,

DataBuffer
data)
```

Sets all samples for a rectangle of pixels from an int array containing
one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Overrides:** setPixels

in class

SampleModel
**Parameters:** x

- The X coordinate of the upper left pixel location.
**Parameters:** y

- The Y coordinate of the upper left pixel location.
**Parameters:** w

- The width of the pixel rectangle.
**Parameters:** h

- The height of the pixel rectangle.
**Parameters:** iArray

- The input samples in an int array.
**Parameters:** data

- The DataBuffer containing the image data.
**See Also:** getPixels(int, int, int, int, int[], DataBuffer)

---

#### setPixels

public void setPixels​(int x,
int y,
int w,
int h,
int[] iArray,

DataBuffer

data)

Sets all samples for a rectangle of pixels from an int array containing
one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

setSample

```java
public void setSample​(int x,
int y,
int b,
int s,

DataBuffer
data)
```

Sets a sample in the specified band for the pixel located at (x,y)
in the DataBuffer using an int for input.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Specified by:** setSample

in class

SampleModel
**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** b

- The band to set.
**Parameters:** s

- The input sample as an int.
**Parameters:** data

- The DataBuffer containing the image data.
**See Also:** getSample(int, int, int, DataBuffer)

---

#### setSample

public void setSample​(int x,
int y,
int b,
int s,

DataBuffer

data)

Sets a sample in the specified band for the pixel located at (x,y)
in the DataBuffer using an int for input.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

setSamples

```java
public void setSamples​(int x,
int y,
int w,
int h,
int b,
int[] iArray,

DataBuffer
data)
```

Sets the samples in the specified band for the specified rectangle
of pixels from an int array containing one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Overrides:** setSamples

in class

SampleModel
**Parameters:** x

- The X coordinate of the upper left pixel location.
**Parameters:** y

- The Y coordinate of the upper left pixel location.
**Parameters:** w

- The width of the pixel rectangle.
**Parameters:** h

- The height of the pixel rectangle.
**Parameters:** b

- The band to set.
**Parameters:** iArray

- The input samples in an int array.
**Parameters:** data

- The DataBuffer containing the image data.
**See Also:** getSamples(int, int, int, int, int, int[], DataBuffer)

---

#### setSamples

public void setSamples​(int x,
int y,
int w,
int h,
int b,
int[] iArray,

DataBuffer

data)

Sets the samples in the specified band for the specified rectangle
of pixels from an int array containing one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

---

