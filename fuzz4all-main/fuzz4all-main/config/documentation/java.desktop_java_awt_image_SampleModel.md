# Class SampleModel

**Source:** `java.desktop\java\awt\image\SampleModel.html`

### Class Description

```java
public abstract class
SampleModel

extends
Object
```

This abstract class defines an interface for extracting samples of pixels
in an image. All image data is expressed as a collection of pixels.
Each pixel consists of a number of samples. A sample is a datum
for one band of an image and a band consists of all samples of a
particular type in an image. For example, a pixel might contain
three samples representing its red, green and blue components.
There are three bands in the image containing this pixel. One band
consists of all the red samples from all pixels in the
image. The second band consists of all the green samples and
the remaining band consists of all of the blue samples. The pixel
can be stored in various formats. For example, all samples from
a particular band can be stored contiguously or all samples from a
single pixel can be stored contiguously.

Subclasses of SampleModel specify the types of samples they can
represent (e.g. unsigned 8-bit byte, signed 16-bit short, etc.)
and may specify how the samples are organized in memory.
In the Java 2D(tm) API, built-in image processing operators may
not operate on all possible sample types, but generally will work
for unsigned integral samples of 16 bits or less. Some operators
support a wider variety of sample types.

A collection of pixels is represented as a Raster, which consists of
a DataBuffer and a SampleModel. The SampleModel allows access to
samples in the DataBuffer and may provide low-level information that
a programmer can use to directly manipulate samples and pixels in the
DataBuffer.

This class is generally a fall back method for dealing with
images. More efficient code will cast the SampleModel to the
appropriate subclass and extract the information needed to directly
manipulate pixels in the DataBuffer.

**Direct Known Subclasses:** ComponentSampleModel

,

MultiPixelPackedSampleModel

,

SinglePixelPackedSampleModel

---

### Field Details

#### protected int width

Width in pixels of the region of image data that this SampleModel
describes.

---

#### protected int height

Height in pixels of the region of image data that this SampleModel
describes.

---

#### protected int numBands

Number of bands of the image data that this SampleModel describes.

---

#### protected int dataType

Data type of the DataBuffer storing the pixel data.

**See Also:**
- DataBuffer

---

### Constructor Details

#### public SampleModel​(int dataType,
int w,
int h,
int numBands)

Constructs a SampleModel with the specified parameters.

**Parameters:**
- dataType

- The data type of the DataBuffer storing the pixel data.
- w

- The width (in pixels) of the region of image data.
- h

- The height (in pixels) of the region of image data.
- numBands

- The number of bands of the image data.

**Throws:**
- IllegalArgumentException

- if

w

or

h

is not greater than 0
- IllegalArgumentException

- if the product of

w

and

h

is greater than

Integer.MAX_VALUE
- IllegalArgumentException

- if

dataType

is not
one of the supported data types

---

### Method Details

#### public final int getWidth()

Returns the width in pixels.

**Returns:**
- the width in pixels of the region of image data
that this

SampleModel

describes.

---

#### public final int getHeight()

Returns the height in pixels.

**Returns:**
- the height in pixels of the region of image data
that this

SampleModel

describes.

---

#### public final int getNumBands()

Returns the total number of bands of image data.

**Returns:**
- the number of bands of image data that this

SampleModel

describes.

---

#### public abstract int getNumDataElements()

Returns the number of data elements needed to transfer a pixel
via the getDataElements and setDataElements methods. When pixels
are transferred via these methods, they may be transferred in a
packed or unpacked format, depending on the implementation of the
SampleModel. Using these methods, pixels are transferred as an
array of getNumDataElements() elements of a primitive type given
by getTransferType(). The TransferType may or may not be the same
as the storage DataType.

**Returns:**
- the number of data elements.

**See Also:**
- getDataElements(int, int, Object, DataBuffer)

,

getDataElements(int, int, int, int, Object, DataBuffer)

,

setDataElements(int, int, Object, DataBuffer)

,

setDataElements(int, int, int, int, Object, DataBuffer)

,

getTransferType()

---

#### public final int getDataType()

Returns the data type of the DataBuffer storing the pixel data.

**Returns:**
- the data type.

---

#### public int getTransferType()

Returns the TransferType used to transfer pixels via the
getDataElements and setDataElements methods. When pixels
are transferred via these methods, they may be transferred in a
packed or unpacked format, depending on the implementation of the
SampleModel. Using these methods, pixels are transferred as an
array of getNumDataElements() elements of a primitive type given
by getTransferType(). The TransferType may or may not be the same
as the storage DataType. The TransferType will be one of the types
defined in DataBuffer.

**Returns:**
- the transfer type.

**See Also:**
- getDataElements(int, int, Object, DataBuffer)

,

getDataElements(int, int, int, int, Object, DataBuffer)

,

setDataElements(int, int, Object, DataBuffer)

,

setDataElements(int, int, int, int, Object, DataBuffer)

,

getNumDataElements()

,

DataBuffer

---

#### public int[] getPixel​(int x,
int y,
int[] iArray,

DataBuffer
data)

Returns the samples for a specified pixel in an int array,
one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Parameters:**
- x

- The X coordinate of the pixel location
- y

- The Y coordinate of the pixel location
- iArray

- If non-null, returns the samples in this array
- data

- The DataBuffer containing the image data

**Returns:**
- the samples for the specified pixel.

**Throws:**
- NullPointerException

- if data is null.
- ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if iArray is too small to hold the output.

**See Also:**
- setPixel(int, int, int[], DataBuffer)

---

#### public abstract
Object
getDataElements​(int x,
int y,

Object
obj,

DataBuffer
data)

Returns data for a single pixel in a primitive array of type
TransferType. For image data supported by the Java 2D API, this
will be one of DataBuffer.TYPE_BYTE, DataBuffer.TYPE_USHORT,
DataBuffer.TYPE_INT, DataBuffer.TYPE_SHORT, DataBuffer.TYPE_FLOAT,
or DataBuffer.TYPE_DOUBLE. Data may be returned in a packed format,
thus increasing efficiency for data transfers. Generally, obj
should be passed in as null, so that the Object will be created
automatically and will be of the right primitive data type.

The following code illustrates transferring data for one pixel from
DataBuffer

db1

, whose storage layout is described by
SampleModel

sm1

, to DataBuffer

db2

, whose
storage layout is described by SampleModel

sm2

.
The transfer will generally be more efficient than using
getPixel/setPixel.

```java
SampleModel sm1, sm2;
DataBuffer db1, db2;
sm2.setDataElements(x, y, sm1.getDataElements(x, y, null, db1), db2);
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
- the data elements for the specified pixel.

**Throws:**
- NullPointerException

- if data is null.
- ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if obj is too small to hold the output.

**See Also:**
- getNumDataElements()

,

getTransferType()

,

DataBuffer

,

setDataElements(int, int, Object, DataBuffer)

---

#### public
Object
getDataElements​(int x,
int y,
int w,
int h,

Object
obj,

DataBuffer
data)

Returns the pixel data for the specified rectangle of pixels in a
primitive array of type TransferType.
For image data supported by the Java 2D API, this
will be one of DataBuffer.TYPE_BYTE, DataBuffer.TYPE_USHORT,
DataBuffer.TYPE_INT, DataBuffer.TYPE_SHORT, DataBuffer.TYPE_FLOAT,
or DataBuffer.TYPE_DOUBLE. Data may be returned in a packed format,
thus increasing efficiency for data transfers. Generally, obj
should be passed in as null, so that the Object will be created
automatically and will be of the right primitive data type.

The following code illustrates transferring data for a rectangular
region of pixels from
DataBuffer

db1

, whose storage layout is described by
SampleModel

sm1

, to DataBuffer

db2

, whose
storage layout is described by SampleModel

sm2

.
The transfer will generally be more efficient than using
getPixels/setPixels.

```java
SampleModel sm1, sm2;
DataBuffer db1, db2;
sm2.setDataElements(x, y, w, h, sm1.getDataElements(x, y, w,
h, null, db1), db2);
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

**Parameters:**
- x

- The minimum X coordinate of the pixel rectangle.
- y

- The minimum Y coordinate of the pixel rectangle.
- w

- The width of the pixel rectangle.
- h

- The height of the pixel rectangle.
- obj

- If non-null, a primitive array in which to return
the pixel data.
- data

- The DataBuffer containing the image data.

**Returns:**
- the data elements for the specified region of pixels.

**Throws:**
- NullPointerException

- if data is null.
- ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if obj is too small to hold the output.

**See Also:**
- getNumDataElements()

,

getTransferType()

,

setDataElements(int, int, int, int, Object, DataBuffer)

,

DataBuffer

---

#### public abstract void setDataElements​(int x,
int y,

Object
obj,

DataBuffer
data)

Sets the data for a single pixel in the specified DataBuffer from a
primitive array of type TransferType. For image data supported by
the Java 2D API, this will be one of DataBuffer.TYPE_BYTE,
DataBuffer.TYPE_USHORT, DataBuffer.TYPE_INT, DataBuffer.TYPE_SHORT,
DataBuffer.TYPE_FLOAT, or DataBuffer.TYPE_DOUBLE. Data in the array
may be in a packed format, thus increasing efficiency for data
transfers.

The following code illustrates transferring data for one pixel from
DataBuffer

db1

, whose storage layout is described by
SampleModel

sm1

, to DataBuffer

db2

, whose
storage layout is described by SampleModel

sm2

.
The transfer will generally be more efficient than using
getPixel/setPixel.

```java
SampleModel sm1, sm2;
DataBuffer db1, db2;
sm2.setDataElements(x, y, sm1.getDataElements(x, y, null, db1),
db2);
```

Using getDataElements/setDataElements to transfer between two
DataBuffer/SampleModel pairs is legitimate if the SampleModels have
the same number of bands, corresponding bands have the same number of
bits per sample, and the TransferTypes are the same.

obj must be a primitive array of type TransferType. Otherwise,
a ClassCastException is thrown. An
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds, or if obj is not large enough to hold the pixel data.

**Parameters:**
- x

- The X coordinate of the pixel location.
- y

- The Y coordinate of the pixel location.
- obj

- A primitive array containing pixel data.
- data

- The DataBuffer containing the image data.

**Throws:**
- NullPointerException

- if data is null.
- ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if obj is too small to hold the input.

**See Also:**
- getNumDataElements()

,

getTransferType()

,

getDataElements(int, int, Object, DataBuffer)

,

DataBuffer

---

#### public void setDataElements​(int x,
int y,
int w,
int h,

Object
obj,

DataBuffer
data)

Sets the data for a rectangle of pixels in the specified DataBuffer
from a primitive array of type TransferType. For image data supported
by the Java 2D API, this will be one of DataBuffer.TYPE_BYTE,
DataBuffer.TYPE_USHORT, DataBuffer.TYPE_INT, DataBuffer.TYPE_SHORT,
DataBuffer.TYPE_FLOAT, or DataBuffer.TYPE_DOUBLE. Data in the array
may be in a packed format, thus increasing efficiency for data
transfers.

The following code illustrates transferring data for a rectangular
region of pixels from
DataBuffer

db1

, whose storage layout is described by
SampleModel

sm1

, to DataBuffer

db2

, whose
storage layout is described by SampleModel

sm2

.
The transfer will generally be more efficient than using
getPixels/setPixels.

```java
SampleModel sm1, sm2;
DataBuffer db1, db2;
sm2.setDataElements(x, y, w, h, sm1.getDataElements(x, y, w, h,
null, db1), db2);
```

Using getDataElements/setDataElements to transfer between two
DataBuffer/SampleModel pairs is legitimate if the SampleModels have
the same number of bands, corresponding bands have the same number of
bits per sample, and the TransferTypes are the same.

obj must be a primitive array of type TransferType. Otherwise,
a ClassCastException is thrown. An
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds, or if obj is not large enough to hold the pixel data.

**Parameters:**
- x

- The minimum X coordinate of the pixel rectangle.
- y

- The minimum Y coordinate of the pixel rectangle.
- w

- The width of the pixel rectangle.
- h

- The height of the pixel rectangle.
- obj

- A primitive array containing pixel data.
- data

- The DataBuffer containing the image data.

**Throws:**
- NullPointerException

- if data is null.
- ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if obj is too small to hold the input.

**See Also:**
- getNumDataElements()

,

getTransferType()

,

getDataElements(int, int, int, int, Object, DataBuffer)

,

DataBuffer

---

#### public float[] getPixel​(int x,
int y,
float[] fArray,

DataBuffer
data)

Returns the samples for the specified pixel in an array of float.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Parameters:**
- x

- The X coordinate of the pixel location.
- y

- The Y coordinate of the pixel location.
- fArray

- If non-null, returns the samples in this array.
- data

- The DataBuffer containing the image data.

**Returns:**
- the samples for the specified pixel.

**Throws:**
- NullPointerException

- if data is null.
- ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if fArray is too small to hold the output.

**See Also:**
- setPixel(int, int, float[], DataBuffer)

---

#### public double[] getPixel​(int x,
int y,
double[] dArray,

DataBuffer
data)

Returns the samples for the specified pixel in an array of double.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Parameters:**
- x

- The X coordinate of the pixel location.
- y

- The Y coordinate of the pixel location.
- dArray

- If non-null, returns the samples in this array.
- data

- The DataBuffer containing the image data.

**Returns:**
- the samples for the specified pixel.

**Throws:**
- NullPointerException

- if data is null.
- ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if dArray is too small to hold the output.

**See Also:**
- setPixel(int, int, double[], DataBuffer)

---

#### public int[] getPixels​(int x,
int y,
int w,
int h,
int[] iArray,

DataBuffer
data)

Returns all samples for a rectangle of pixels in an
int array, one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

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
- the samples for the specified region of pixels.

**Throws:**
- NullPointerException

- if data is null.
- ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if iArray is too small to hold the output.

**See Also:**
- setPixels(int, int, int, int, int[], DataBuffer)

---

#### public float[] getPixels​(int x,
int y,
int w,
int h,
float[] fArray,

DataBuffer
data)

Returns all samples for a rectangle of pixels in a float
array, one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Parameters:**
- x

- The X coordinate of the upper left pixel location.
- y

- The Y coordinate of the upper left pixel location.
- w

- The width of the pixel rectangle.
- h

- The height of the pixel rectangle.
- fArray

- If non-null, returns the samples in this array.
- data

- The DataBuffer containing the image data.

**Returns:**
- the samples for the specified region of pixels.

**Throws:**
- NullPointerException

- if data is null.
- ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if fArray is too small to hold the output.

**See Also:**
- setPixels(int, int, int, int, float[], DataBuffer)

---

#### public double[] getPixels​(int x,
int y,
int w,
int h,
double[] dArray,

DataBuffer
data)

Returns all samples for a rectangle of pixels in a double
array, one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Parameters:**
- x

- The X coordinate of the upper left pixel location.
- y

- The Y coordinate of the upper left pixel location.
- w

- The width of the pixel rectangle.
- h

- The height of the pixel rectangle.
- dArray

- If non-null, returns the samples in this array.
- data

- The DataBuffer containing the image data.

**Returns:**
- the samples for the specified region of pixels.

**Throws:**
- NullPointerException

- if data is null.
- ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if dArray is too small to hold the output.

**See Also:**
- setPixels(int, int, int, int, double[], DataBuffer)

---

#### public abstract int getSample​(int x,
int y,
int b,

DataBuffer
data)

Returns the sample in a specified band for the pixel located
at (x,y) as an int.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

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
- the sample in a specified band for the specified pixel.

**Throws:**
- NullPointerException

- if data is null.
- ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds.

**See Also:**
- setSample(int, int, int, int, DataBuffer)

---

#### public float getSampleFloat​(int x,
int y,
int b,

DataBuffer
data)

Returns the sample in a specified band
for the pixel located at (x,y) as a float.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

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
- the sample in a specified band for the specified pixel.

**Throws:**
- NullPointerException

- if data is null.
- ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds.

---

#### public double getSampleDouble​(int x,
int y,
int b,

DataBuffer
data)

Returns the sample in a specified band
for a pixel located at (x,y) as a double.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

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
- the sample in a specified band for the specified pixel.

**Throws:**
- NullPointerException

- if data is null.
- ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds.

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
- the samples for the specified band for the specified region
of pixels.

**Throws:**
- NullPointerException

- if data is null.
- ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds, or if iArray is too small to
hold the output.

**See Also:**
- setSamples(int, int, int, int, int, int[], DataBuffer)

---

#### public float[] getSamples​(int x,
int y,
int w,
int h,
int b,
float[] fArray,

DataBuffer
data)

Returns the samples for a specified band for the specified rectangle
of pixels in a float array, one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

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
- fArray

- If non-null, returns the samples in this array.
- data

- The DataBuffer containing the image data.

**Returns:**
- the samples for the specified band for the specified region
of pixels.

**Throws:**
- NullPointerException

- if data is null.
- ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds, or if fArray is too small to
hold the output.

**See Also:**
- setSamples(int, int, int, int, int, float[], DataBuffer)

---

#### public double[] getSamples​(int x,
int y,
int w,
int h,
int b,
double[] dArray,

DataBuffer
data)

Returns the samples for a specified band for a specified rectangle
of pixels in a double array, one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

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
- dArray

- If non-null, returns the samples in this array.
- data

- The DataBuffer containing the image data.

**Returns:**
- the samples for the specified band for the specified region
of pixels.

**Throws:**
- NullPointerException

- if data is null.
- ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds, or if dArray is too small to
hold the output.

**See Also:**
- setSamples(int, int, int, int, int, double[], DataBuffer)

---

#### public void setPixel​(int x,
int y,
int[] iArray,

DataBuffer
data)

Sets a pixel in the DataBuffer using an int array of samples for input.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Parameters:**
- x

- The X coordinate of the pixel location.
- y

- The Y coordinate of the pixel location.
- iArray

- The input samples in an int array.
- data

- The DataBuffer containing the image data.

**Throws:**
- NullPointerException

- if iArray or data is null.
- ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if iArray is too small to hold the input.

**See Also:**
- getPixel(int, int, int[], DataBuffer)

---

#### public void setPixel​(int x,
int y,
float[] fArray,

DataBuffer
data)

Sets a pixel in the DataBuffer using a float array of samples for input.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Parameters:**
- x

- The X coordinate of the pixel location.
- y

- The Y coordinate of the pixel location.
- fArray

- The input samples in a float array.
- data

- The DataBuffer containing the image data.

**Throws:**
- NullPointerException

- if fArray or data is null.
- ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if fArray is too small to hold the input.

**See Also:**
- getPixel(int, int, float[], DataBuffer)

---

#### public void setPixel​(int x,
int y,
double[] dArray,

DataBuffer
data)

Sets a pixel in the DataBuffer using a double array of samples
for input.

**Parameters:**
- x

- The X coordinate of the pixel location.
- y

- The Y coordinate of the pixel location.
- dArray

- The input samples in a double array.
- data

- The DataBuffer containing the image data.

**Throws:**
- NullPointerException

- if dArray or data is null.
- ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if fArray is too small to hold the input.

**See Also:**
- getPixel(int, int, double[], DataBuffer)

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

**Throws:**
- NullPointerException

- if iArray or data is null.
- ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if iArray is too small to hold the input.

**See Also:**
- getPixels(int, int, int, int, int[], DataBuffer)

---

#### public void setPixels​(int x,
int y,
int w,
int h,
float[] fArray,

DataBuffer
data)

Sets all samples for a rectangle of pixels from a float array containing
one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Parameters:**
- x

- The X coordinate of the upper left pixel location.
- y

- The Y coordinate of the upper left pixel location.
- w

- The width of the pixel rectangle.
- h

- The height of the pixel rectangle.
- fArray

- The input samples in a float array.
- data

- The DataBuffer containing the image data.

**Throws:**
- NullPointerException

- if fArray or data is null.
- ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if fArray is too small to hold the input.

**See Also:**
- getPixels(int, int, int, int, float[], DataBuffer)

---

#### public void setPixels​(int x,
int y,
int w,
int h,
double[] dArray,

DataBuffer
data)

Sets all samples for a rectangle of pixels from a double array
containing one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Parameters:**
- x

- The X coordinate of the upper left pixel location.
- y

- The Y coordinate of the upper left pixel location.
- w

- The width of the pixel rectangle.
- h

- The height of the pixel rectangle.
- dArray

- The input samples in a double array.
- data

- The DataBuffer containing the image data.

**Throws:**
- NullPointerException

- if dArray or data is null.
- ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if dArray is too small to hold the input.

**See Also:**
- getPixels(int, int, int, int, double[], DataBuffer)

---

#### public abstract void setSample​(int x,
int y,
int b,
int s,

DataBuffer
data)

Sets a sample in the specified band for the pixel located at (x,y)
in the DataBuffer using an int for input.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

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

**Throws:**
- NullPointerException

- if data is null.
- ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds.

**See Also:**
- getSample(int, int, int, DataBuffer)

---

#### public void setSample​(int x,
int y,
int b,
float s,

DataBuffer
data)

Sets a sample in the specified band for the pixel located at (x,y)
in the DataBuffer using a float for input.
The default implementation of this method casts the input
float sample to an int and then calls the

setSample(int, int, int, DataBuffer)

method using
that int value.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Parameters:**
- x

- The X coordinate of the pixel location.
- y

- The Y coordinate of the pixel location.
- b

- The band to set.
- s

- The input sample as a float.
- data

- The DataBuffer containing the image data.

**Throws:**
- NullPointerException

- if data is null.
- ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds.

**See Also:**
- getSample(int, int, int, DataBuffer)

---

#### public void setSample​(int x,
int y,
int b,
double s,

DataBuffer
data)

Sets a sample in the specified band for the pixel located at (x,y)
in the DataBuffer using a double for input.
The default implementation of this method casts the input
double sample to an int and then calls the

setSample(int, int, int, DataBuffer)

method using
that int value.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Parameters:**
- x

- The X coordinate of the pixel location.
- y

- The Y coordinate of the pixel location.
- b

- The band to set.
- s

- The input sample as a double.
- data

- The DataBuffer containing the image data.

**Throws:**
- NullPointerException

- if data is null.
- ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds.

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

**Throws:**
- NullPointerException

- if iArray or data is null.
- ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds, or if iArray is too small to
hold the input.

**See Also:**
- getSamples(int, int, int, int, int, int[], DataBuffer)

---

#### public void setSamples​(int x,
int y,
int w,
int h,
int b,
float[] fArray,

DataBuffer
data)

Sets the samples in the specified band for the specified rectangle
of pixels from a float array containing one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

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
- fArray

- The input samples in a float array.
- data

- The DataBuffer containing the image data.

**Throws:**
- NullPointerException

- if fArray or data is null.
- ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds, or if fArray is too small to
hold the input.

**See Also:**
- getSamples(int, int, int, int, int, float[], DataBuffer)

---

#### public void setSamples​(int x,
int y,
int w,
int h,
int b,
double[] dArray,

DataBuffer
data)

Sets the samples in the specified band for the specified rectangle
of pixels from a double array containing one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

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
- dArray

- The input samples in a double array.
- data

- The DataBuffer containing the image data.

**Throws:**
- NullPointerException

- if dArray or data is null.
- ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds, or if dArray is too small to
hold the input.

**See Also:**
- getSamples(int, int, int, int, int, double[], DataBuffer)

---

#### public abstract
SampleModel
createCompatibleSampleModel​(int w,
int h)

Creates a SampleModel which describes data in this SampleModel's
format, but with a different width and height.

**Parameters:**
- w

- the width of the image data
- h

- the height of the image data

**Returns:**
- a

SampleModel

describing the same image
data as this

SampleModel

, but with a
different size.

---

#### public abstract
SampleModel
createSubsetSampleModel​(int[] bands)

Creates a new SampleModel
with a subset of the bands of this
SampleModel.

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

---

#### public abstract
DataBuffer
createDataBuffer()

Creates a DataBuffer that corresponds to this SampleModel.
The DataBuffer's width and height will match this SampleModel's.

**Returns:**
- a

DataBuffer

corresponding to this

SampleModel

.

---

#### public abstract int[] getSampleSize()

Returns the size in bits of samples for all bands.

**Returns:**
- the size of samples for all bands.

---

#### public abstract int getSampleSize​(int band)

Returns the size in bits of samples for the specified band.

**Parameters:**
- band

- the specified band

**Returns:**
- the size of the samples of the specified band.

---

### Additional Sections

#### Class SampleModel

java.lang.Object

- java.awt.image.SampleModel

java.awt.image.SampleModel

**Direct Known Subclasses:** ComponentSampleModel

,

MultiPixelPackedSampleModel

,

SinglePixelPackedSampleModel

```java
public abstract class
SampleModel

extends
Object
```

This abstract class defines an interface for extracting samples of pixels
in an image. All image data is expressed as a collection of pixels.
Each pixel consists of a number of samples. A sample is a datum
for one band of an image and a band consists of all samples of a
particular type in an image. For example, a pixel might contain
three samples representing its red, green and blue components.
There are three bands in the image containing this pixel. One band
consists of all the red samples from all pixels in the
image. The second band consists of all the green samples and
the remaining band consists of all of the blue samples. The pixel
can be stored in various formats. For example, all samples from
a particular band can be stored contiguously or all samples from a
single pixel can be stored contiguously.

Subclasses of SampleModel specify the types of samples they can
represent (e.g. unsigned 8-bit byte, signed 16-bit short, etc.)
and may specify how the samples are organized in memory.
In the Java 2D(tm) API, built-in image processing operators may
not operate on all possible sample types, but generally will work
for unsigned integral samples of 16 bits or less. Some operators
support a wider variety of sample types.

A collection of pixels is represented as a Raster, which consists of
a DataBuffer and a SampleModel. The SampleModel allows access to
samples in the DataBuffer and may provide low-level information that
a programmer can use to directly manipulate samples and pixels in the
DataBuffer.

This class is generally a fall back method for dealing with
images. More efficient code will cast the SampleModel to the
appropriate subclass and extract the information needed to directly
manipulate pixels in the DataBuffer.

**See Also:** DataBuffer

,

Raster

,

ComponentSampleModel

,

PixelInterleavedSampleModel

,

BandedSampleModel

,

MultiPixelPackedSampleModel

,

SinglePixelPackedSampleModel

public abstract class

SampleModel

extends

Object

This abstract class defines an interface for extracting samples of pixels
in an image. All image data is expressed as a collection of pixels.
Each pixel consists of a number of samples. A sample is a datum
for one band of an image and a band consists of all samples of a
particular type in an image. For example, a pixel might contain
three samples representing its red, green and blue components.
There are three bands in the image containing this pixel. One band
consists of all the red samples from all pixels in the
image. The second band consists of all the green samples and
the remaining band consists of all of the blue samples. The pixel
can be stored in various formats. For example, all samples from
a particular band can be stored contiguously or all samples from a
single pixel can be stored contiguously.

Subclasses of SampleModel specify the types of samples they can
represent (e.g. unsigned 8-bit byte, signed 16-bit short, etc.)
and may specify how the samples are organized in memory.
In the Java 2D(tm) API, built-in image processing operators may
not operate on all possible sample types, but generally will work
for unsigned integral samples of 16 bits or less. Some operators
support a wider variety of sample types.

A collection of pixels is represented as a Raster, which consists of
a DataBuffer and a SampleModel. The SampleModel allows access to
samples in the DataBuffer and may provide low-level information that
a programmer can use to directly manipulate samples and pixels in the
DataBuffer.

This class is generally a fall back method for dealing with
images. More efficient code will cast the SampleModel to the
appropriate subclass and extract the information needed to directly
manipulate pixels in the DataBuffer.

Subclasses of SampleModel specify the types of samples they can
represent (e.g. unsigned 8-bit byte, signed 16-bit short, etc.)
and may specify how the samples are organized in memory.
In the Java 2D(tm) API, built-in image processing operators may
not operate on all possible sample types, but generally will work
for unsigned integral samples of 16 bits or less. Some operators
support a wider variety of sample types.

A collection of pixels is represented as a Raster, which consists of
a DataBuffer and a SampleModel. The SampleModel allows access to
samples in the DataBuffer and may provide low-level information that
a programmer can use to directly manipulate samples and pixels in the
DataBuffer.

This class is generally a fall back method for dealing with
images. More efficient code will cast the SampleModel to the
appropriate subclass and extract the information needed to directly
manipulate pixels in the DataBuffer.

A collection of pixels is represented as a Raster, which consists of
a DataBuffer and a SampleModel. The SampleModel allows access to
samples in the DataBuffer and may provide low-level information that
a programmer can use to directly manipulate samples and pixels in the
DataBuffer.

This class is generally a fall back method for dealing with
images. More efficient code will cast the SampleModel to the
appropriate subclass and extract the information needed to directly
manipulate pixels in the DataBuffer.

This class is generally a fall back method for dealing with
images. More efficient code will cast the SampleModel to the
appropriate subclass and extract the information needed to directly
manipulate pixels in the DataBuffer.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected int

dataType

Data type of the DataBuffer storing the pixel data.

protected int

height

Height in pixels of the region of image data that this SampleModel
describes.

protected int

numBands

Number of bands of the image data that this SampleModel describes.

protected int

width

Width in pixels of the region of image data that this SampleModel
describes.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SampleModel

​(int dataType,
int w,
int h,
int numBands)

Constructs a SampleModel with the specified parameters.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

SampleModel

createCompatibleSampleModel

​(int w,
int h)

Creates a SampleModel which describes data in this SampleModel's
format, but with a different width and height.

abstract

DataBuffer

createDataBuffer

()

Creates a DataBuffer that corresponds to this SampleModel.

abstract

SampleModel

createSubsetSampleModel

​(int[] bands)

Creates a new SampleModel
with a subset of the bands of this
SampleModel.

Object

getDataElements

​(int x,
int y,
int w,
int h,

Object

obj,

DataBuffer

data)

Returns the pixel data for the specified rectangle of pixels in a
primitive array of type TransferType.

abstract

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

getDataType

()

Returns the data type of the DataBuffer storing the pixel data.

int

getHeight

()

Returns the height in pixels.

int

getNumBands

()

Returns the total number of bands of image data.

abstract int

getNumDataElements

()

Returns the number of data elements needed to transfer a pixel
via the getDataElements and setDataElements methods.

double[]

getPixel

​(int x,
int y,
double[] dArray,

DataBuffer

data)

Returns the samples for the specified pixel in an array of double.

float[]

getPixel

​(int x,
int y,
float[] fArray,

DataBuffer

data)

Returns the samples for the specified pixel in an array of float.

int[]

getPixel

​(int x,
int y,
int[] iArray,

DataBuffer

data)

Returns the samples for a specified pixel in an int array,
one sample per array element.

double[]

getPixels

​(int x,
int y,
int w,
int h,
double[] dArray,

DataBuffer

data)

Returns all samples for a rectangle of pixels in a double
array, one sample per array element.

float[]

getPixels

​(int x,
int y,
int w,
int h,
float[] fArray,

DataBuffer

data)

Returns all samples for a rectangle of pixels in a float
array, one sample per array element.

int[]

getPixels

​(int x,
int y,
int w,
int h,
int[] iArray,

DataBuffer

data)

Returns all samples for a rectangle of pixels in an
int array, one sample per array element.

abstract int

getSample

​(int x,
int y,
int b,

DataBuffer

data)

Returns the sample in a specified band for the pixel located
at (x,y) as an int.

double

getSampleDouble

​(int x,
int y,
int b,

DataBuffer

data)

Returns the sample in a specified band
for a pixel located at (x,y) as a double.

float

getSampleFloat

​(int x,
int y,
int b,

DataBuffer

data)

Returns the sample in a specified band
for the pixel located at (x,y) as a float.

double[]

getSamples

​(int x,
int y,
int w,
int h,
int b,
double[] dArray,

DataBuffer

data)

Returns the samples for a specified band for a specified rectangle
of pixels in a double array, one sample per array element.

float[]

getSamples

​(int x,
int y,
int w,
int h,
int b,
float[] fArray,

DataBuffer

data)

Returns the samples for a specified band for the specified rectangle
of pixels in a float array, one sample per array element.

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

abstract int[]

getSampleSize

()

Returns the size in bits of samples for all bands.

abstract int

getSampleSize

​(int band)

Returns the size in bits of samples for the specified band.

int

getTransferType

()

Returns the TransferType used to transfer pixels via the
getDataElements and setDataElements methods.

int

getWidth

()

Returns the width in pixels.

void

setDataElements

​(int x,
int y,
int w,
int h,

Object

obj,

DataBuffer

data)

Sets the data for a rectangle of pixels in the specified DataBuffer
from a primitive array of type TransferType.

abstract void

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
double[] dArray,

DataBuffer

data)

Sets a pixel in the DataBuffer using a double array of samples
for input.

void

setPixel

​(int x,
int y,
float[] fArray,

DataBuffer

data)

Sets a pixel in the DataBuffer using a float array of samples for input.

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
double[] dArray,

DataBuffer

data)

Sets all samples for a rectangle of pixels from a double array
containing one sample per array element.

void

setPixels

​(int x,
int y,
int w,
int h,
float[] fArray,

DataBuffer

data)

Sets all samples for a rectangle of pixels from a float array containing
one sample per array element.

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
double s,

DataBuffer

data)

Sets a sample in the specified band for the pixel located at (x,y)
in the DataBuffer using a double for input.

void

setSample

​(int x,
int y,
int b,
float s,

DataBuffer

data)

Sets a sample in the specified band for the pixel located at (x,y)
in the DataBuffer using a float for input.

abstract void

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
double[] dArray,

DataBuffer

data)

Sets the samples in the specified band for the specified rectangle
of pixels from a double array containing one sample per array element.

void

setSamples

​(int x,
int y,
int w,
int h,
int b,
float[] fArray,

DataBuffer

data)

Sets the samples in the specified band for the specified rectangle
of pixels from a float array containing one sample per array element.

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

protected int

dataType

Data type of the DataBuffer storing the pixel data.

protected int

height

Height in pixels of the region of image data that this SampleModel
describes.

protected int

numBands

Number of bands of the image data that this SampleModel describes.

protected int

width

Width in pixels of the region of image data that this SampleModel
describes.

---

#### Field Summary

Data type of the DataBuffer storing the pixel data.

Height in pixels of the region of image data that this SampleModel
describes.

Number of bands of the image data that this SampleModel describes.

Width in pixels of the region of image data that this SampleModel
describes.

Constructor Summary

Constructors

Constructor

Description

SampleModel

​(int dataType,
int w,
int h,
int numBands)

Constructs a SampleModel with the specified parameters.

---

#### Constructor Summary

Constructs a SampleModel with the specified parameters.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

SampleModel

createCompatibleSampleModel

​(int w,
int h)

Creates a SampleModel which describes data in this SampleModel's
format, but with a different width and height.

abstract

DataBuffer

createDataBuffer

()

Creates a DataBuffer that corresponds to this SampleModel.

abstract

SampleModel

createSubsetSampleModel

​(int[] bands)

Creates a new SampleModel
with a subset of the bands of this
SampleModel.

Object

getDataElements

​(int x,
int y,
int w,
int h,

Object

obj,

DataBuffer

data)

Returns the pixel data for the specified rectangle of pixels in a
primitive array of type TransferType.

abstract

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

getDataType

()

Returns the data type of the DataBuffer storing the pixel data.

int

getHeight

()

Returns the height in pixels.

int

getNumBands

()

Returns the total number of bands of image data.

abstract int

getNumDataElements

()

Returns the number of data elements needed to transfer a pixel
via the getDataElements and setDataElements methods.

double[]

getPixel

​(int x,
int y,
double[] dArray,

DataBuffer

data)

Returns the samples for the specified pixel in an array of double.

float[]

getPixel

​(int x,
int y,
float[] fArray,

DataBuffer

data)

Returns the samples for the specified pixel in an array of float.

int[]

getPixel

​(int x,
int y,
int[] iArray,

DataBuffer

data)

Returns the samples for a specified pixel in an int array,
one sample per array element.

double[]

getPixels

​(int x,
int y,
int w,
int h,
double[] dArray,

DataBuffer

data)

Returns all samples for a rectangle of pixels in a double
array, one sample per array element.

float[]

getPixels

​(int x,
int y,
int w,
int h,
float[] fArray,

DataBuffer

data)

Returns all samples for a rectangle of pixels in a float
array, one sample per array element.

int[]

getPixels

​(int x,
int y,
int w,
int h,
int[] iArray,

DataBuffer

data)

Returns all samples for a rectangle of pixels in an
int array, one sample per array element.

abstract int

getSample

​(int x,
int y,
int b,

DataBuffer

data)

Returns the sample in a specified band for the pixel located
at (x,y) as an int.

double

getSampleDouble

​(int x,
int y,
int b,

DataBuffer

data)

Returns the sample in a specified band
for a pixel located at (x,y) as a double.

float

getSampleFloat

​(int x,
int y,
int b,

DataBuffer

data)

Returns the sample in a specified band
for the pixel located at (x,y) as a float.

double[]

getSamples

​(int x,
int y,
int w,
int h,
int b,
double[] dArray,

DataBuffer

data)

Returns the samples for a specified band for a specified rectangle
of pixels in a double array, one sample per array element.

float[]

getSamples

​(int x,
int y,
int w,
int h,
int b,
float[] fArray,

DataBuffer

data)

Returns the samples for a specified band for the specified rectangle
of pixels in a float array, one sample per array element.

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

abstract int[]

getSampleSize

()

Returns the size in bits of samples for all bands.

abstract int

getSampleSize

​(int band)

Returns the size in bits of samples for the specified band.

int

getTransferType

()

Returns the TransferType used to transfer pixels via the
getDataElements and setDataElements methods.

int

getWidth

()

Returns the width in pixels.

void

setDataElements

​(int x,
int y,
int w,
int h,

Object

obj,

DataBuffer

data)

Sets the data for a rectangle of pixels in the specified DataBuffer
from a primitive array of type TransferType.

abstract void

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
double[] dArray,

DataBuffer

data)

Sets a pixel in the DataBuffer using a double array of samples
for input.

void

setPixel

​(int x,
int y,
float[] fArray,

DataBuffer

data)

Sets a pixel in the DataBuffer using a float array of samples for input.

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
double[] dArray,

DataBuffer

data)

Sets all samples for a rectangle of pixels from a double array
containing one sample per array element.

void

setPixels

​(int x,
int y,
int w,
int h,
float[] fArray,

DataBuffer

data)

Sets all samples for a rectangle of pixels from a float array containing
one sample per array element.

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
double s,

DataBuffer

data)

Sets a sample in the specified band for the pixel located at (x,y)
in the DataBuffer using a double for input.

void

setSample

​(int x,
int y,
int b,
float s,

DataBuffer

data)

Sets a sample in the specified band for the pixel located at (x,y)
in the DataBuffer using a float for input.

abstract void

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
double[] dArray,

DataBuffer

data)

Sets the samples in the specified band for the specified rectangle
of pixels from a double array containing one sample per array element.

void

setSamples

​(int x,
int y,
int w,
int h,
int b,
float[] fArray,

DataBuffer

data)

Sets the samples in the specified band for the specified rectangle
of pixels from a float array containing one sample per array element.

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

Creates a SampleModel which describes data in this SampleModel's
format, but with a different width and height.

Creates a DataBuffer that corresponds to this SampleModel.

Creates a new SampleModel
with a subset of the bands of this
SampleModel.

Returns the pixel data for the specified rectangle of pixels in a
primitive array of type TransferType.

Returns data for a single pixel in a primitive array of type
TransferType.

Returns the data type of the DataBuffer storing the pixel data.

Returns the height in pixels.

Returns the total number of bands of image data.

Returns the number of data elements needed to transfer a pixel
via the getDataElements and setDataElements methods.

Returns the samples for the specified pixel in an array of double.

Returns the samples for the specified pixel in an array of float.

Returns the samples for a specified pixel in an int array,
one sample per array element.

Returns all samples for a rectangle of pixels in a double
array, one sample per array element.

Returns all samples for a rectangle of pixels in a float
array, one sample per array element.

Returns all samples for a rectangle of pixels in an
int array, one sample per array element.

Returns the sample in a specified band for the pixel located
at (x,y) as an int.

Returns the sample in a specified band
for a pixel located at (x,y) as a double.

Returns the sample in a specified band
for the pixel located at (x,y) as a float.

Returns the samples for a specified band for a specified rectangle
of pixels in a double array, one sample per array element.

Returns the samples for a specified band for the specified rectangle
of pixels in a float array, one sample per array element.

Returns the samples for a specified band for the specified rectangle
of pixels in an int array, one sample per array element.

Returns the size in bits of samples for all bands.

Returns the size in bits of samples for the specified band.

Returns the TransferType used to transfer pixels via the
getDataElements and setDataElements methods.

Returns the width in pixels.

Sets the data for a rectangle of pixels in the specified DataBuffer
from a primitive array of type TransferType.

Sets the data for a single pixel in the specified DataBuffer from a
primitive array of type TransferType.

Sets a pixel in the DataBuffer using a double array of samples
for input.

Sets a pixel in the DataBuffer using a float array of samples for input.

Sets a pixel in the DataBuffer using an int array of samples for input.

Sets all samples for a rectangle of pixels from a double array
containing one sample per array element.

Sets all samples for a rectangle of pixels from a float array containing
one sample per array element.

Sets all samples for a rectangle of pixels from an int array containing
one sample per array element.

Sets a sample in the specified band for the pixel located at (x,y)
in the DataBuffer using a double for input.

Sets a sample in the specified band for the pixel located at (x,y)
in the DataBuffer using a float for input.

Sets a sample in the specified band for the pixel located at (x,y)
in the DataBuffer using an int for input.

Sets the samples in the specified band for the specified rectangle
of pixels from a double array containing one sample per array element.

Sets the samples in the specified band for the specified rectangle
of pixels from a float array containing one sample per array element.

Sets the samples in the specified band for the specified rectangle
of pixels from an int array containing one sample per array element.

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

- width

```java
protected int width
```

Width in pixels of the region of image data that this SampleModel
describes.

- height

```java
protected int height
```

Height in pixels of the region of image data that this SampleModel
describes.

- numBands

```java
protected int numBands
```

Number of bands of the image data that this SampleModel describes.

- dataType

```java
protected int dataType
```

Data type of the DataBuffer storing the pixel data.

**See Also:** DataBuffer

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SampleModel

```java
public SampleModel​(int dataType,
int w,
int h,
int numBands)
```

Constructs a SampleModel with the specified parameters.

**Parameters:** dataType

- The data type of the DataBuffer storing the pixel data.
**Parameters:** w

- The width (in pixels) of the region of image data.
**Parameters:** h

- The height (in pixels) of the region of image data.
**Parameters:** numBands

- The number of bands of the image data.
**Throws:** IllegalArgumentException

- if

w

or

h

is not greater than 0
**Throws:** IllegalArgumentException

- if the product of

w

and

h

is greater than

Integer.MAX_VALUE
**Throws:** IllegalArgumentException

- if

dataType

is not
one of the supported data types

============ METHOD DETAIL ==========

- Method Detail

- getWidth

```java
public final int getWidth()
```

Returns the width in pixels.

**Returns:** the width in pixels of the region of image data
that this

SampleModel

describes.

- getHeight

```java
public final int getHeight()
```

Returns the height in pixels.

**Returns:** the height in pixels of the region of image data
that this

SampleModel

describes.

- getNumBands

```java
public final int getNumBands()
```

Returns the total number of bands of image data.

**Returns:** the number of bands of image data that this

SampleModel

describes.

- getNumDataElements

```java
public abstract int getNumDataElements()
```

Returns the number of data elements needed to transfer a pixel
via the getDataElements and setDataElements methods. When pixels
are transferred via these methods, they may be transferred in a
packed or unpacked format, depending on the implementation of the
SampleModel. Using these methods, pixels are transferred as an
array of getNumDataElements() elements of a primitive type given
by getTransferType(). The TransferType may or may not be the same
as the storage DataType.

**Returns:** the number of data elements.
**See Also:** getDataElements(int, int, Object, DataBuffer)

,

getDataElements(int, int, int, int, Object, DataBuffer)

,

setDataElements(int, int, Object, DataBuffer)

,

setDataElements(int, int, int, int, Object, DataBuffer)

,

getTransferType()

- getDataType

```java
public final int getDataType()
```

Returns the data type of the DataBuffer storing the pixel data.

**Returns:** the data type.

- getTransferType

```java
public int getTransferType()
```

Returns the TransferType used to transfer pixels via the
getDataElements and setDataElements methods. When pixels
are transferred via these methods, they may be transferred in a
packed or unpacked format, depending on the implementation of the
SampleModel. Using these methods, pixels are transferred as an
array of getNumDataElements() elements of a primitive type given
by getTransferType(). The TransferType may or may not be the same
as the storage DataType. The TransferType will be one of the types
defined in DataBuffer.

**Returns:** the transfer type.
**See Also:** getDataElements(int, int, Object, DataBuffer)

,

getDataElements(int, int, int, int, Object, DataBuffer)

,

setDataElements(int, int, Object, DataBuffer)

,

setDataElements(int, int, int, int, Object, DataBuffer)

,

getNumDataElements()

,

DataBuffer

- getPixel

```java
public int[] getPixel​(int x,
int y,
int[] iArray,

DataBuffer
data)
```

Returns the samples for a specified pixel in an int array,
one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Parameters:** x

- The X coordinate of the pixel location
**Parameters:** y

- The Y coordinate of the pixel location
**Parameters:** iArray

- If non-null, returns the samples in this array
**Parameters:** data

- The DataBuffer containing the image data
**Returns:** the samples for the specified pixel.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if iArray is too small to hold the output.
**See Also:** setPixel(int, int, int[], DataBuffer)

- getDataElements

```java
public abstract
Object
getDataElements​(int x,
int y,

Object
obj,

DataBuffer
data)
```

Returns data for a single pixel in a primitive array of type
TransferType. For image data supported by the Java 2D API, this
will be one of DataBuffer.TYPE_BYTE, DataBuffer.TYPE_USHORT,
DataBuffer.TYPE_INT, DataBuffer.TYPE_SHORT, DataBuffer.TYPE_FLOAT,
or DataBuffer.TYPE_DOUBLE. Data may be returned in a packed format,
thus increasing efficiency for data transfers. Generally, obj
should be passed in as null, so that the Object will be created
automatically and will be of the right primitive data type.

The following code illustrates transferring data for one pixel from
DataBuffer

db1

, whose storage layout is described by
SampleModel

sm1

, to DataBuffer

db2

, whose
storage layout is described by SampleModel

sm2

.
The transfer will generally be more efficient than using
getPixel/setPixel.

```java
SampleModel sm1, sm2;
DataBuffer db1, db2;
sm2.setDataElements(x, y, sm1.getDataElements(x, y, null, db1), db2);
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

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** obj

- If non-null, a primitive array in which to return
the pixel data.
**Parameters:** data

- The DataBuffer containing the image data.
**Returns:** the data elements for the specified pixel.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if obj is too small to hold the output.
**See Also:** getNumDataElements()

,

getTransferType()

,

DataBuffer

,

setDataElements(int, int, Object, DataBuffer)

- getDataElements

```java
public
Object
getDataElements​(int x,
int y,
int w,
int h,

Object
obj,

DataBuffer
data)
```

Returns the pixel data for the specified rectangle of pixels in a
primitive array of type TransferType.
For image data supported by the Java 2D API, this
will be one of DataBuffer.TYPE_BYTE, DataBuffer.TYPE_USHORT,
DataBuffer.TYPE_INT, DataBuffer.TYPE_SHORT, DataBuffer.TYPE_FLOAT,
or DataBuffer.TYPE_DOUBLE. Data may be returned in a packed format,
thus increasing efficiency for data transfers. Generally, obj
should be passed in as null, so that the Object will be created
automatically and will be of the right primitive data type.

The following code illustrates transferring data for a rectangular
region of pixels from
DataBuffer

db1

, whose storage layout is described by
SampleModel

sm1

, to DataBuffer

db2

, whose
storage layout is described by SampleModel

sm2

.
The transfer will generally be more efficient than using
getPixels/setPixels.

```java
SampleModel sm1, sm2;
DataBuffer db1, db2;
sm2.setDataElements(x, y, w, h, sm1.getDataElements(x, y, w,
h, null, db1), db2);
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

**Parameters:** x

- The minimum X coordinate of the pixel rectangle.
**Parameters:** y

- The minimum Y coordinate of the pixel rectangle.
**Parameters:** w

- The width of the pixel rectangle.
**Parameters:** h

- The height of the pixel rectangle.
**Parameters:** obj

- If non-null, a primitive array in which to return
the pixel data.
**Parameters:** data

- The DataBuffer containing the image data.
**Returns:** the data elements for the specified region of pixels.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if obj is too small to hold the output.
**See Also:** getNumDataElements()

,

getTransferType()

,

setDataElements(int, int, int, int, Object, DataBuffer)

,

DataBuffer

- setDataElements

```java
public abstract void setDataElements​(int x,
int y,

Object
obj,

DataBuffer
data)
```

Sets the data for a single pixel in the specified DataBuffer from a
primitive array of type TransferType. For image data supported by
the Java 2D API, this will be one of DataBuffer.TYPE_BYTE,
DataBuffer.TYPE_USHORT, DataBuffer.TYPE_INT, DataBuffer.TYPE_SHORT,
DataBuffer.TYPE_FLOAT, or DataBuffer.TYPE_DOUBLE. Data in the array
may be in a packed format, thus increasing efficiency for data
transfers.

The following code illustrates transferring data for one pixel from
DataBuffer

db1

, whose storage layout is described by
SampleModel

sm1

, to DataBuffer

db2

, whose
storage layout is described by SampleModel

sm2

.
The transfer will generally be more efficient than using
getPixel/setPixel.

```java
SampleModel sm1, sm2;
DataBuffer db1, db2;
sm2.setDataElements(x, y, sm1.getDataElements(x, y, null, db1),
db2);
```

Using getDataElements/setDataElements to transfer between two
DataBuffer/SampleModel pairs is legitimate if the SampleModels have
the same number of bands, corresponding bands have the same number of
bits per sample, and the TransferTypes are the same.

obj must be a primitive array of type TransferType. Otherwise,
a ClassCastException is thrown. An
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds, or if obj is not large enough to hold the pixel data.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** obj

- A primitive array containing pixel data.
**Parameters:** data

- The DataBuffer containing the image data.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if obj is too small to hold the input.
**See Also:** getNumDataElements()

,

getTransferType()

,

getDataElements(int, int, Object, DataBuffer)

,

DataBuffer

- setDataElements

```java
public void setDataElements​(int x,
int y,
int w,
int h,

Object
obj,

DataBuffer
data)
```

Sets the data for a rectangle of pixels in the specified DataBuffer
from a primitive array of type TransferType. For image data supported
by the Java 2D API, this will be one of DataBuffer.TYPE_BYTE,
DataBuffer.TYPE_USHORT, DataBuffer.TYPE_INT, DataBuffer.TYPE_SHORT,
DataBuffer.TYPE_FLOAT, or DataBuffer.TYPE_DOUBLE. Data in the array
may be in a packed format, thus increasing efficiency for data
transfers.

The following code illustrates transferring data for a rectangular
region of pixels from
DataBuffer

db1

, whose storage layout is described by
SampleModel

sm1

, to DataBuffer

db2

, whose
storage layout is described by SampleModel

sm2

.
The transfer will generally be more efficient than using
getPixels/setPixels.

```java
SampleModel sm1, sm2;
DataBuffer db1, db2;
sm2.setDataElements(x, y, w, h, sm1.getDataElements(x, y, w, h,
null, db1), db2);
```

Using getDataElements/setDataElements to transfer between two
DataBuffer/SampleModel pairs is legitimate if the SampleModels have
the same number of bands, corresponding bands have the same number of
bits per sample, and the TransferTypes are the same.

obj must be a primitive array of type TransferType. Otherwise,
a ClassCastException is thrown. An
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds, or if obj is not large enough to hold the pixel data.

**Parameters:** x

- The minimum X coordinate of the pixel rectangle.
**Parameters:** y

- The minimum Y coordinate of the pixel rectangle.
**Parameters:** w

- The width of the pixel rectangle.
**Parameters:** h

- The height of the pixel rectangle.
**Parameters:** obj

- A primitive array containing pixel data.
**Parameters:** data

- The DataBuffer containing the image data.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if obj is too small to hold the input.
**See Also:** getNumDataElements()

,

getTransferType()

,

getDataElements(int, int, int, int, Object, DataBuffer)

,

DataBuffer

- getPixel

```java
public float[] getPixel​(int x,
int y,
float[] fArray,

DataBuffer
data)
```

Returns the samples for the specified pixel in an array of float.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** fArray

- If non-null, returns the samples in this array.
**Parameters:** data

- The DataBuffer containing the image data.
**Returns:** the samples for the specified pixel.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if fArray is too small to hold the output.
**See Also:** setPixel(int, int, float[], DataBuffer)

- getPixel

```java
public double[] getPixel​(int x,
int y,
double[] dArray,

DataBuffer
data)
```

Returns the samples for the specified pixel in an array of double.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** dArray

- If non-null, returns the samples in this array.
**Parameters:** data

- The DataBuffer containing the image data.
**Returns:** the samples for the specified pixel.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if dArray is too small to hold the output.
**See Also:** setPixel(int, int, double[], DataBuffer)

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

Returns all samples for a rectangle of pixels in an
int array, one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

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
**Returns:** the samples for the specified region of pixels.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if iArray is too small to hold the output.
**See Also:** setPixels(int, int, int, int, int[], DataBuffer)

- getPixels

```java
public float[] getPixels​(int x,
int y,
int w,
int h,
float[] fArray,

DataBuffer
data)
```

Returns all samples for a rectangle of pixels in a float
array, one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Parameters:** x

- The X coordinate of the upper left pixel location.
**Parameters:** y

- The Y coordinate of the upper left pixel location.
**Parameters:** w

- The width of the pixel rectangle.
**Parameters:** h

- The height of the pixel rectangle.
**Parameters:** fArray

- If non-null, returns the samples in this array.
**Parameters:** data

- The DataBuffer containing the image data.
**Returns:** the samples for the specified region of pixels.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if fArray is too small to hold the output.
**See Also:** setPixels(int, int, int, int, float[], DataBuffer)

- getPixels

```java
public double[] getPixels​(int x,
int y,
int w,
int h,
double[] dArray,

DataBuffer
data)
```

Returns all samples for a rectangle of pixels in a double
array, one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Parameters:** x

- The X coordinate of the upper left pixel location.
**Parameters:** y

- The Y coordinate of the upper left pixel location.
**Parameters:** w

- The width of the pixel rectangle.
**Parameters:** h

- The height of the pixel rectangle.
**Parameters:** dArray

- If non-null, returns the samples in this array.
**Parameters:** data

- The DataBuffer containing the image data.
**Returns:** the samples for the specified region of pixels.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if dArray is too small to hold the output.
**See Also:** setPixels(int, int, int, int, double[], DataBuffer)

- getSample

```java
public abstract int getSample​(int x,
int y,
int b,

DataBuffer
data)
```

Returns the sample in a specified band for the pixel located
at (x,y) as an int.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** b

- The band to return.
**Parameters:** data

- The DataBuffer containing the image data.
**Returns:** the sample in a specified band for the specified pixel.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds.
**See Also:** setSample(int, int, int, int, DataBuffer)

- getSampleFloat

```java
public float getSampleFloat​(int x,
int y,
int b,

DataBuffer
data)
```

Returns the sample in a specified band
for the pixel located at (x,y) as a float.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** b

- The band to return.
**Parameters:** data

- The DataBuffer containing the image data.
**Returns:** the sample in a specified band for the specified pixel.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds.

- getSampleDouble

```java
public double getSampleDouble​(int x,
int y,
int b,

DataBuffer
data)
```

Returns the sample in a specified band
for a pixel located at (x,y) as a double.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** b

- The band to return.
**Parameters:** data

- The DataBuffer containing the image data.
**Returns:** the sample in a specified band for the specified pixel.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds.

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
**Returns:** the samples for the specified band for the specified region
of pixels.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds, or if iArray is too small to
hold the output.
**See Also:** setSamples(int, int, int, int, int, int[], DataBuffer)

- getSamples

```java
public float[] getSamples​(int x,
int y,
int w,
int h,
int b,
float[] fArray,

DataBuffer
data)
```

Returns the samples for a specified band for the specified rectangle
of pixels in a float array, one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

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
**Parameters:** fArray

- If non-null, returns the samples in this array.
**Parameters:** data

- The DataBuffer containing the image data.
**Returns:** the samples for the specified band for the specified region
of pixels.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds, or if fArray is too small to
hold the output.
**See Also:** setSamples(int, int, int, int, int, float[], DataBuffer)

- getSamples

```java
public double[] getSamples​(int x,
int y,
int w,
int h,
int b,
double[] dArray,

DataBuffer
data)
```

Returns the samples for a specified band for a specified rectangle
of pixels in a double array, one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

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
**Parameters:** dArray

- If non-null, returns the samples in this array.
**Parameters:** data

- The DataBuffer containing the image data.
**Returns:** the samples for the specified band for the specified region
of pixels.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds, or if dArray is too small to
hold the output.
**See Also:** setSamples(int, int, int, int, int, double[], DataBuffer)

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

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** iArray

- The input samples in an int array.
**Parameters:** data

- The DataBuffer containing the image data.
**Throws:** NullPointerException

- if iArray or data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if iArray is too small to hold the input.
**See Also:** getPixel(int, int, int[], DataBuffer)

- setPixel

```java
public void setPixel​(int x,
int y,
float[] fArray,

DataBuffer
data)
```

Sets a pixel in the DataBuffer using a float array of samples for input.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** fArray

- The input samples in a float array.
**Parameters:** data

- The DataBuffer containing the image data.
**Throws:** NullPointerException

- if fArray or data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if fArray is too small to hold the input.
**See Also:** getPixel(int, int, float[], DataBuffer)

- setPixel

```java
public void setPixel​(int x,
int y,
double[] dArray,

DataBuffer
data)
```

Sets a pixel in the DataBuffer using a double array of samples
for input.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** dArray

- The input samples in a double array.
**Parameters:** data

- The DataBuffer containing the image data.
**Throws:** NullPointerException

- if dArray or data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if fArray is too small to hold the input.
**See Also:** getPixel(int, int, double[], DataBuffer)

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
**Throws:** NullPointerException

- if iArray or data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if iArray is too small to hold the input.
**See Also:** getPixels(int, int, int, int, int[], DataBuffer)

- setPixels

```java
public void setPixels​(int x,
int y,
int w,
int h,
float[] fArray,

DataBuffer
data)
```

Sets all samples for a rectangle of pixels from a float array containing
one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Parameters:** x

- The X coordinate of the upper left pixel location.
**Parameters:** y

- The Y coordinate of the upper left pixel location.
**Parameters:** w

- The width of the pixel rectangle.
**Parameters:** h

- The height of the pixel rectangle.
**Parameters:** fArray

- The input samples in a float array.
**Parameters:** data

- The DataBuffer containing the image data.
**Throws:** NullPointerException

- if fArray or data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if fArray is too small to hold the input.
**See Also:** getPixels(int, int, int, int, float[], DataBuffer)

- setPixels

```java
public void setPixels​(int x,
int y,
int w,
int h,
double[] dArray,

DataBuffer
data)
```

Sets all samples for a rectangle of pixels from a double array
containing one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Parameters:** x

- The X coordinate of the upper left pixel location.
**Parameters:** y

- The Y coordinate of the upper left pixel location.
**Parameters:** w

- The width of the pixel rectangle.
**Parameters:** h

- The height of the pixel rectangle.
**Parameters:** dArray

- The input samples in a double array.
**Parameters:** data

- The DataBuffer containing the image data.
**Throws:** NullPointerException

- if dArray or data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if dArray is too small to hold the input.
**See Also:** getPixels(int, int, int, int, double[], DataBuffer)

- setSample

```java
public abstract void setSample​(int x,
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
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds.
**See Also:** getSample(int, int, int, DataBuffer)

- setSample

```java
public void setSample​(int x,
int y,
int b,
float s,

DataBuffer
data)
```

Sets a sample in the specified band for the pixel located at (x,y)
in the DataBuffer using a float for input.
The default implementation of this method casts the input
float sample to an int and then calls the

setSample(int, int, int, DataBuffer)

method using
that int value.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** b

- The band to set.
**Parameters:** s

- The input sample as a float.
**Parameters:** data

- The DataBuffer containing the image data.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds.
**See Also:** getSample(int, int, int, DataBuffer)

- setSample

```java
public void setSample​(int x,
int y,
int b,
double s,

DataBuffer
data)
```

Sets a sample in the specified band for the pixel located at (x,y)
in the DataBuffer using a double for input.
The default implementation of this method casts the input
double sample to an int and then calls the

setSample(int, int, int, DataBuffer)

method using
that int value.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** b

- The band to set.
**Parameters:** s

- The input sample as a double.
**Parameters:** data

- The DataBuffer containing the image data.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds.
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
**Throws:** NullPointerException

- if iArray or data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds, or if iArray is too small to
hold the input.
**See Also:** getSamples(int, int, int, int, int, int[], DataBuffer)

- setSamples

```java
public void setSamples​(int x,
int y,
int w,
int h,
int b,
float[] fArray,

DataBuffer
data)
```

Sets the samples in the specified band for the specified rectangle
of pixels from a float array containing one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

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
**Parameters:** fArray

- The input samples in a float array.
**Parameters:** data

- The DataBuffer containing the image data.
**Throws:** NullPointerException

- if fArray or data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds, or if fArray is too small to
hold the input.
**See Also:** getSamples(int, int, int, int, int, float[], DataBuffer)

- setSamples

```java
public void setSamples​(int x,
int y,
int w,
int h,
int b,
double[] dArray,

DataBuffer
data)
```

Sets the samples in the specified band for the specified rectangle
of pixels from a double array containing one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

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
**Parameters:** dArray

- The input samples in a double array.
**Parameters:** data

- The DataBuffer containing the image data.
**Throws:** NullPointerException

- if dArray or data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds, or if dArray is too small to
hold the input.
**See Also:** getSamples(int, int, int, int, int, double[], DataBuffer)

- createCompatibleSampleModel

```java
public abstract
SampleModel
createCompatibleSampleModel​(int w,
int h)
```

Creates a SampleModel which describes data in this SampleModel's
format, but with a different width and height.

**Parameters:** w

- the width of the image data
**Parameters:** h

- the height of the image data
**Returns:** a

SampleModel

describing the same image
data as this

SampleModel

, but with a
different size.

- createSubsetSampleModel

```java
public abstract
SampleModel
createSubsetSampleModel​(int[] bands)
```

Creates a new SampleModel
with a subset of the bands of this
SampleModel.

**Parameters:** bands

- the subset of bands of this

SampleModel
**Returns:** a

SampleModel

with a subset of bands of this

SampleModel

.

- createDataBuffer

```java
public abstract
DataBuffer
createDataBuffer()
```

Creates a DataBuffer that corresponds to this SampleModel.
The DataBuffer's width and height will match this SampleModel's.

**Returns:** a

DataBuffer

corresponding to this

SampleModel

.

- getSampleSize

```java
public abstract int[] getSampleSize()
```

Returns the size in bits of samples for all bands.

**Returns:** the size of samples for all bands.

- getSampleSize

```java
public abstract int getSampleSize​(int band)
```

Returns the size in bits of samples for the specified band.

**Parameters:** band

- the specified band
**Returns:** the size of the samples of the specified band.

Field Detail

- width

```java
protected int width
```

Width in pixels of the region of image data that this SampleModel
describes.

- height

```java
protected int height
```

Height in pixels of the region of image data that this SampleModel
describes.

- numBands

```java
protected int numBands
```

Number of bands of the image data that this SampleModel describes.

- dataType

```java
protected int dataType
```

Data type of the DataBuffer storing the pixel data.

**See Also:** DataBuffer

---

#### Field Detail

width

```java
protected int width
```

Width in pixels of the region of image data that this SampleModel
describes.

---

#### width

protected int width

Width in pixels of the region of image data that this SampleModel
describes.

height

```java
protected int height
```

Height in pixels of the region of image data that this SampleModel
describes.

---

#### height

protected int height

Height in pixels of the region of image data that this SampleModel
describes.

numBands

```java
protected int numBands
```

Number of bands of the image data that this SampleModel describes.

---

#### numBands

protected int numBands

Number of bands of the image data that this SampleModel describes.

dataType

```java
protected int dataType
```

Data type of the DataBuffer storing the pixel data.

**See Also:** DataBuffer

---

#### dataType

protected int dataType

Data type of the DataBuffer storing the pixel data.

Constructor Detail

- SampleModel

```java
public SampleModel​(int dataType,
int w,
int h,
int numBands)
```

Constructs a SampleModel with the specified parameters.

**Parameters:** dataType

- The data type of the DataBuffer storing the pixel data.
**Parameters:** w

- The width (in pixels) of the region of image data.
**Parameters:** h

- The height (in pixels) of the region of image data.
**Parameters:** numBands

- The number of bands of the image data.
**Throws:** IllegalArgumentException

- if

w

or

h

is not greater than 0
**Throws:** IllegalArgumentException

- if the product of

w

and

h

is greater than

Integer.MAX_VALUE
**Throws:** IllegalArgumentException

- if

dataType

is not
one of the supported data types

---

#### Constructor Detail

SampleModel

```java
public SampleModel​(int dataType,
int w,
int h,
int numBands)
```

Constructs a SampleModel with the specified parameters.

**Parameters:** dataType

- The data type of the DataBuffer storing the pixel data.
**Parameters:** w

- The width (in pixels) of the region of image data.
**Parameters:** h

- The height (in pixels) of the region of image data.
**Parameters:** numBands

- The number of bands of the image data.
**Throws:** IllegalArgumentException

- if

w

or

h

is not greater than 0
**Throws:** IllegalArgumentException

- if the product of

w

and

h

is greater than

Integer.MAX_VALUE
**Throws:** IllegalArgumentException

- if

dataType

is not
one of the supported data types

---

#### SampleModel

public SampleModel​(int dataType,
int w,
int h,
int numBands)

Constructs a SampleModel with the specified parameters.

Method Detail

- getWidth

```java
public final int getWidth()
```

Returns the width in pixels.

**Returns:** the width in pixels of the region of image data
that this

SampleModel

describes.

- getHeight

```java
public final int getHeight()
```

Returns the height in pixels.

**Returns:** the height in pixels of the region of image data
that this

SampleModel

describes.

- getNumBands

```java
public final int getNumBands()
```

Returns the total number of bands of image data.

**Returns:** the number of bands of image data that this

SampleModel

describes.

- getNumDataElements

```java
public abstract int getNumDataElements()
```

Returns the number of data elements needed to transfer a pixel
via the getDataElements and setDataElements methods. When pixels
are transferred via these methods, they may be transferred in a
packed or unpacked format, depending on the implementation of the
SampleModel. Using these methods, pixels are transferred as an
array of getNumDataElements() elements of a primitive type given
by getTransferType(). The TransferType may or may not be the same
as the storage DataType.

**Returns:** the number of data elements.
**See Also:** getDataElements(int, int, Object, DataBuffer)

,

getDataElements(int, int, int, int, Object, DataBuffer)

,

setDataElements(int, int, Object, DataBuffer)

,

setDataElements(int, int, int, int, Object, DataBuffer)

,

getTransferType()

- getDataType

```java
public final int getDataType()
```

Returns the data type of the DataBuffer storing the pixel data.

**Returns:** the data type.

- getTransferType

```java
public int getTransferType()
```

Returns the TransferType used to transfer pixels via the
getDataElements and setDataElements methods. When pixels
are transferred via these methods, they may be transferred in a
packed or unpacked format, depending on the implementation of the
SampleModel. Using these methods, pixels are transferred as an
array of getNumDataElements() elements of a primitive type given
by getTransferType(). The TransferType may or may not be the same
as the storage DataType. The TransferType will be one of the types
defined in DataBuffer.

**Returns:** the transfer type.
**See Also:** getDataElements(int, int, Object, DataBuffer)

,

getDataElements(int, int, int, int, Object, DataBuffer)

,

setDataElements(int, int, Object, DataBuffer)

,

setDataElements(int, int, int, int, Object, DataBuffer)

,

getNumDataElements()

,

DataBuffer

- getPixel

```java
public int[] getPixel​(int x,
int y,
int[] iArray,

DataBuffer
data)
```

Returns the samples for a specified pixel in an int array,
one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Parameters:** x

- The X coordinate of the pixel location
**Parameters:** y

- The Y coordinate of the pixel location
**Parameters:** iArray

- If non-null, returns the samples in this array
**Parameters:** data

- The DataBuffer containing the image data
**Returns:** the samples for the specified pixel.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if iArray is too small to hold the output.
**See Also:** setPixel(int, int, int[], DataBuffer)

- getDataElements

```java
public abstract
Object
getDataElements​(int x,
int y,

Object
obj,

DataBuffer
data)
```

Returns data for a single pixel in a primitive array of type
TransferType. For image data supported by the Java 2D API, this
will be one of DataBuffer.TYPE_BYTE, DataBuffer.TYPE_USHORT,
DataBuffer.TYPE_INT, DataBuffer.TYPE_SHORT, DataBuffer.TYPE_FLOAT,
or DataBuffer.TYPE_DOUBLE. Data may be returned in a packed format,
thus increasing efficiency for data transfers. Generally, obj
should be passed in as null, so that the Object will be created
automatically and will be of the right primitive data type.

The following code illustrates transferring data for one pixel from
DataBuffer

db1

, whose storage layout is described by
SampleModel

sm1

, to DataBuffer

db2

, whose
storage layout is described by SampleModel

sm2

.
The transfer will generally be more efficient than using
getPixel/setPixel.

```java
SampleModel sm1, sm2;
DataBuffer db1, db2;
sm2.setDataElements(x, y, sm1.getDataElements(x, y, null, db1), db2);
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

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** obj

- If non-null, a primitive array in which to return
the pixel data.
**Parameters:** data

- The DataBuffer containing the image data.
**Returns:** the data elements for the specified pixel.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if obj is too small to hold the output.
**See Also:** getNumDataElements()

,

getTransferType()

,

DataBuffer

,

setDataElements(int, int, Object, DataBuffer)

- getDataElements

```java
public
Object
getDataElements​(int x,
int y,
int w,
int h,

Object
obj,

DataBuffer
data)
```

Returns the pixel data for the specified rectangle of pixels in a
primitive array of type TransferType.
For image data supported by the Java 2D API, this
will be one of DataBuffer.TYPE_BYTE, DataBuffer.TYPE_USHORT,
DataBuffer.TYPE_INT, DataBuffer.TYPE_SHORT, DataBuffer.TYPE_FLOAT,
or DataBuffer.TYPE_DOUBLE. Data may be returned in a packed format,
thus increasing efficiency for data transfers. Generally, obj
should be passed in as null, so that the Object will be created
automatically and will be of the right primitive data type.

The following code illustrates transferring data for a rectangular
region of pixels from
DataBuffer

db1

, whose storage layout is described by
SampleModel

sm1

, to DataBuffer

db2

, whose
storage layout is described by SampleModel

sm2

.
The transfer will generally be more efficient than using
getPixels/setPixels.

```java
SampleModel sm1, sm2;
DataBuffer db1, db2;
sm2.setDataElements(x, y, w, h, sm1.getDataElements(x, y, w,
h, null, db1), db2);
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

**Parameters:** x

- The minimum X coordinate of the pixel rectangle.
**Parameters:** y

- The minimum Y coordinate of the pixel rectangle.
**Parameters:** w

- The width of the pixel rectangle.
**Parameters:** h

- The height of the pixel rectangle.
**Parameters:** obj

- If non-null, a primitive array in which to return
the pixel data.
**Parameters:** data

- The DataBuffer containing the image data.
**Returns:** the data elements for the specified region of pixels.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if obj is too small to hold the output.
**See Also:** getNumDataElements()

,

getTransferType()

,

setDataElements(int, int, int, int, Object, DataBuffer)

,

DataBuffer

- setDataElements

```java
public abstract void setDataElements​(int x,
int y,

Object
obj,

DataBuffer
data)
```

Sets the data for a single pixel in the specified DataBuffer from a
primitive array of type TransferType. For image data supported by
the Java 2D API, this will be one of DataBuffer.TYPE_BYTE,
DataBuffer.TYPE_USHORT, DataBuffer.TYPE_INT, DataBuffer.TYPE_SHORT,
DataBuffer.TYPE_FLOAT, or DataBuffer.TYPE_DOUBLE. Data in the array
may be in a packed format, thus increasing efficiency for data
transfers.

The following code illustrates transferring data for one pixel from
DataBuffer

db1

, whose storage layout is described by
SampleModel

sm1

, to DataBuffer

db2

, whose
storage layout is described by SampleModel

sm2

.
The transfer will generally be more efficient than using
getPixel/setPixel.

```java
SampleModel sm1, sm2;
DataBuffer db1, db2;
sm2.setDataElements(x, y, sm1.getDataElements(x, y, null, db1),
db2);
```

Using getDataElements/setDataElements to transfer between two
DataBuffer/SampleModel pairs is legitimate if the SampleModels have
the same number of bands, corresponding bands have the same number of
bits per sample, and the TransferTypes are the same.

obj must be a primitive array of type TransferType. Otherwise,
a ClassCastException is thrown. An
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds, or if obj is not large enough to hold the pixel data.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** obj

- A primitive array containing pixel data.
**Parameters:** data

- The DataBuffer containing the image data.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if obj is too small to hold the input.
**See Also:** getNumDataElements()

,

getTransferType()

,

getDataElements(int, int, Object, DataBuffer)

,

DataBuffer

- setDataElements

```java
public void setDataElements​(int x,
int y,
int w,
int h,

Object
obj,

DataBuffer
data)
```

Sets the data for a rectangle of pixels in the specified DataBuffer
from a primitive array of type TransferType. For image data supported
by the Java 2D API, this will be one of DataBuffer.TYPE_BYTE,
DataBuffer.TYPE_USHORT, DataBuffer.TYPE_INT, DataBuffer.TYPE_SHORT,
DataBuffer.TYPE_FLOAT, or DataBuffer.TYPE_DOUBLE. Data in the array
may be in a packed format, thus increasing efficiency for data
transfers.

The following code illustrates transferring data for a rectangular
region of pixels from
DataBuffer

db1

, whose storage layout is described by
SampleModel

sm1

, to DataBuffer

db2

, whose
storage layout is described by SampleModel

sm2

.
The transfer will generally be more efficient than using
getPixels/setPixels.

```java
SampleModel sm1, sm2;
DataBuffer db1, db2;
sm2.setDataElements(x, y, w, h, sm1.getDataElements(x, y, w, h,
null, db1), db2);
```

Using getDataElements/setDataElements to transfer between two
DataBuffer/SampleModel pairs is legitimate if the SampleModels have
the same number of bands, corresponding bands have the same number of
bits per sample, and the TransferTypes are the same.

obj must be a primitive array of type TransferType. Otherwise,
a ClassCastException is thrown. An
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds, or if obj is not large enough to hold the pixel data.

**Parameters:** x

- The minimum X coordinate of the pixel rectangle.
**Parameters:** y

- The minimum Y coordinate of the pixel rectangle.
**Parameters:** w

- The width of the pixel rectangle.
**Parameters:** h

- The height of the pixel rectangle.
**Parameters:** obj

- A primitive array containing pixel data.
**Parameters:** data

- The DataBuffer containing the image data.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if obj is too small to hold the input.
**See Also:** getNumDataElements()

,

getTransferType()

,

getDataElements(int, int, int, int, Object, DataBuffer)

,

DataBuffer

- getPixel

```java
public float[] getPixel​(int x,
int y,
float[] fArray,

DataBuffer
data)
```

Returns the samples for the specified pixel in an array of float.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** fArray

- If non-null, returns the samples in this array.
**Parameters:** data

- The DataBuffer containing the image data.
**Returns:** the samples for the specified pixel.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if fArray is too small to hold the output.
**See Also:** setPixel(int, int, float[], DataBuffer)

- getPixel

```java
public double[] getPixel​(int x,
int y,
double[] dArray,

DataBuffer
data)
```

Returns the samples for the specified pixel in an array of double.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** dArray

- If non-null, returns the samples in this array.
**Parameters:** data

- The DataBuffer containing the image data.
**Returns:** the samples for the specified pixel.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if dArray is too small to hold the output.
**See Also:** setPixel(int, int, double[], DataBuffer)

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

Returns all samples for a rectangle of pixels in an
int array, one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

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
**Returns:** the samples for the specified region of pixels.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if iArray is too small to hold the output.
**See Also:** setPixels(int, int, int, int, int[], DataBuffer)

- getPixels

```java
public float[] getPixels​(int x,
int y,
int w,
int h,
float[] fArray,

DataBuffer
data)
```

Returns all samples for a rectangle of pixels in a float
array, one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Parameters:** x

- The X coordinate of the upper left pixel location.
**Parameters:** y

- The Y coordinate of the upper left pixel location.
**Parameters:** w

- The width of the pixel rectangle.
**Parameters:** h

- The height of the pixel rectangle.
**Parameters:** fArray

- If non-null, returns the samples in this array.
**Parameters:** data

- The DataBuffer containing the image data.
**Returns:** the samples for the specified region of pixels.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if fArray is too small to hold the output.
**See Also:** setPixels(int, int, int, int, float[], DataBuffer)

- getPixels

```java
public double[] getPixels​(int x,
int y,
int w,
int h,
double[] dArray,

DataBuffer
data)
```

Returns all samples for a rectangle of pixels in a double
array, one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Parameters:** x

- The X coordinate of the upper left pixel location.
**Parameters:** y

- The Y coordinate of the upper left pixel location.
**Parameters:** w

- The width of the pixel rectangle.
**Parameters:** h

- The height of the pixel rectangle.
**Parameters:** dArray

- If non-null, returns the samples in this array.
**Parameters:** data

- The DataBuffer containing the image data.
**Returns:** the samples for the specified region of pixels.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if dArray is too small to hold the output.
**See Also:** setPixels(int, int, int, int, double[], DataBuffer)

- getSample

```java
public abstract int getSample​(int x,
int y,
int b,

DataBuffer
data)
```

Returns the sample in a specified band for the pixel located
at (x,y) as an int.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** b

- The band to return.
**Parameters:** data

- The DataBuffer containing the image data.
**Returns:** the sample in a specified band for the specified pixel.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds.
**See Also:** setSample(int, int, int, int, DataBuffer)

- getSampleFloat

```java
public float getSampleFloat​(int x,
int y,
int b,

DataBuffer
data)
```

Returns the sample in a specified band
for the pixel located at (x,y) as a float.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** b

- The band to return.
**Parameters:** data

- The DataBuffer containing the image data.
**Returns:** the sample in a specified band for the specified pixel.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds.

- getSampleDouble

```java
public double getSampleDouble​(int x,
int y,
int b,

DataBuffer
data)
```

Returns the sample in a specified band
for a pixel located at (x,y) as a double.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** b

- The band to return.
**Parameters:** data

- The DataBuffer containing the image data.
**Returns:** the sample in a specified band for the specified pixel.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds.

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
**Returns:** the samples for the specified band for the specified region
of pixels.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds, or if iArray is too small to
hold the output.
**See Also:** setSamples(int, int, int, int, int, int[], DataBuffer)

- getSamples

```java
public float[] getSamples​(int x,
int y,
int w,
int h,
int b,
float[] fArray,

DataBuffer
data)
```

Returns the samples for a specified band for the specified rectangle
of pixels in a float array, one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

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
**Parameters:** fArray

- If non-null, returns the samples in this array.
**Parameters:** data

- The DataBuffer containing the image data.
**Returns:** the samples for the specified band for the specified region
of pixels.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds, or if fArray is too small to
hold the output.
**See Also:** setSamples(int, int, int, int, int, float[], DataBuffer)

- getSamples

```java
public double[] getSamples​(int x,
int y,
int w,
int h,
int b,
double[] dArray,

DataBuffer
data)
```

Returns the samples for a specified band for a specified rectangle
of pixels in a double array, one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

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
**Parameters:** dArray

- If non-null, returns the samples in this array.
**Parameters:** data

- The DataBuffer containing the image data.
**Returns:** the samples for the specified band for the specified region
of pixels.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds, or if dArray is too small to
hold the output.
**See Also:** setSamples(int, int, int, int, int, double[], DataBuffer)

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

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** iArray

- The input samples in an int array.
**Parameters:** data

- The DataBuffer containing the image data.
**Throws:** NullPointerException

- if iArray or data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if iArray is too small to hold the input.
**See Also:** getPixel(int, int, int[], DataBuffer)

- setPixel

```java
public void setPixel​(int x,
int y,
float[] fArray,

DataBuffer
data)
```

Sets a pixel in the DataBuffer using a float array of samples for input.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** fArray

- The input samples in a float array.
**Parameters:** data

- The DataBuffer containing the image data.
**Throws:** NullPointerException

- if fArray or data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if fArray is too small to hold the input.
**See Also:** getPixel(int, int, float[], DataBuffer)

- setPixel

```java
public void setPixel​(int x,
int y,
double[] dArray,

DataBuffer
data)
```

Sets a pixel in the DataBuffer using a double array of samples
for input.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** dArray

- The input samples in a double array.
**Parameters:** data

- The DataBuffer containing the image data.
**Throws:** NullPointerException

- if dArray or data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if fArray is too small to hold the input.
**See Also:** getPixel(int, int, double[], DataBuffer)

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
**Throws:** NullPointerException

- if iArray or data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if iArray is too small to hold the input.
**See Also:** getPixels(int, int, int, int, int[], DataBuffer)

- setPixels

```java
public void setPixels​(int x,
int y,
int w,
int h,
float[] fArray,

DataBuffer
data)
```

Sets all samples for a rectangle of pixels from a float array containing
one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Parameters:** x

- The X coordinate of the upper left pixel location.
**Parameters:** y

- The Y coordinate of the upper left pixel location.
**Parameters:** w

- The width of the pixel rectangle.
**Parameters:** h

- The height of the pixel rectangle.
**Parameters:** fArray

- The input samples in a float array.
**Parameters:** data

- The DataBuffer containing the image data.
**Throws:** NullPointerException

- if fArray or data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if fArray is too small to hold the input.
**See Also:** getPixels(int, int, int, int, float[], DataBuffer)

- setPixels

```java
public void setPixels​(int x,
int y,
int w,
int h,
double[] dArray,

DataBuffer
data)
```

Sets all samples for a rectangle of pixels from a double array
containing one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Parameters:** x

- The X coordinate of the upper left pixel location.
**Parameters:** y

- The Y coordinate of the upper left pixel location.
**Parameters:** w

- The width of the pixel rectangle.
**Parameters:** h

- The height of the pixel rectangle.
**Parameters:** dArray

- The input samples in a double array.
**Parameters:** data

- The DataBuffer containing the image data.
**Throws:** NullPointerException

- if dArray or data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if dArray is too small to hold the input.
**See Also:** getPixels(int, int, int, int, double[], DataBuffer)

- setSample

```java
public abstract void setSample​(int x,
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
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds.
**See Also:** getSample(int, int, int, DataBuffer)

- setSample

```java
public void setSample​(int x,
int y,
int b,
float s,

DataBuffer
data)
```

Sets a sample in the specified band for the pixel located at (x,y)
in the DataBuffer using a float for input.
The default implementation of this method casts the input
float sample to an int and then calls the

setSample(int, int, int, DataBuffer)

method using
that int value.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** b

- The band to set.
**Parameters:** s

- The input sample as a float.
**Parameters:** data

- The DataBuffer containing the image data.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds.
**See Also:** getSample(int, int, int, DataBuffer)

- setSample

```java
public void setSample​(int x,
int y,
int b,
double s,

DataBuffer
data)
```

Sets a sample in the specified band for the pixel located at (x,y)
in the DataBuffer using a double for input.
The default implementation of this method casts the input
double sample to an int and then calls the

setSample(int, int, int, DataBuffer)

method using
that int value.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** b

- The band to set.
**Parameters:** s

- The input sample as a double.
**Parameters:** data

- The DataBuffer containing the image data.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds.
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
**Throws:** NullPointerException

- if iArray or data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds, or if iArray is too small to
hold the input.
**See Also:** getSamples(int, int, int, int, int, int[], DataBuffer)

- setSamples

```java
public void setSamples​(int x,
int y,
int w,
int h,
int b,
float[] fArray,

DataBuffer
data)
```

Sets the samples in the specified band for the specified rectangle
of pixels from a float array containing one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

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
**Parameters:** fArray

- The input samples in a float array.
**Parameters:** data

- The DataBuffer containing the image data.
**Throws:** NullPointerException

- if fArray or data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds, or if fArray is too small to
hold the input.
**See Also:** getSamples(int, int, int, int, int, float[], DataBuffer)

- setSamples

```java
public void setSamples​(int x,
int y,
int w,
int h,
int b,
double[] dArray,

DataBuffer
data)
```

Sets the samples in the specified band for the specified rectangle
of pixels from a double array containing one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

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
**Parameters:** dArray

- The input samples in a double array.
**Parameters:** data

- The DataBuffer containing the image data.
**Throws:** NullPointerException

- if dArray or data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds, or if dArray is too small to
hold the input.
**See Also:** getSamples(int, int, int, int, int, double[], DataBuffer)

- createCompatibleSampleModel

```java
public abstract
SampleModel
createCompatibleSampleModel​(int w,
int h)
```

Creates a SampleModel which describes data in this SampleModel's
format, but with a different width and height.

**Parameters:** w

- the width of the image data
**Parameters:** h

- the height of the image data
**Returns:** a

SampleModel

describing the same image
data as this

SampleModel

, but with a
different size.

- createSubsetSampleModel

```java
public abstract
SampleModel
createSubsetSampleModel​(int[] bands)
```

Creates a new SampleModel
with a subset of the bands of this
SampleModel.

**Parameters:** bands

- the subset of bands of this

SampleModel
**Returns:** a

SampleModel

with a subset of bands of this

SampleModel

.

- createDataBuffer

```java
public abstract
DataBuffer
createDataBuffer()
```

Creates a DataBuffer that corresponds to this SampleModel.
The DataBuffer's width and height will match this SampleModel's.

**Returns:** a

DataBuffer

corresponding to this

SampleModel

.

- getSampleSize

```java
public abstract int[] getSampleSize()
```

Returns the size in bits of samples for all bands.

**Returns:** the size of samples for all bands.

- getSampleSize

```java
public abstract int getSampleSize​(int band)
```

Returns the size in bits of samples for the specified band.

**Parameters:** band

- the specified band
**Returns:** the size of the samples of the specified band.

---

#### Method Detail

getWidth

```java
public final int getWidth()
```

Returns the width in pixels.

**Returns:** the width in pixels of the region of image data
that this

SampleModel

describes.

---

#### getWidth

public final int getWidth()

Returns the width in pixels.

getHeight

```java
public final int getHeight()
```

Returns the height in pixels.

**Returns:** the height in pixels of the region of image data
that this

SampleModel

describes.

---

#### getHeight

public final int getHeight()

Returns the height in pixels.

getNumBands

```java
public final int getNumBands()
```

Returns the total number of bands of image data.

**Returns:** the number of bands of image data that this

SampleModel

describes.

---

#### getNumBands

public final int getNumBands()

Returns the total number of bands of image data.

getNumDataElements

```java
public abstract int getNumDataElements()
```

Returns the number of data elements needed to transfer a pixel
via the getDataElements and setDataElements methods. When pixels
are transferred via these methods, they may be transferred in a
packed or unpacked format, depending on the implementation of the
SampleModel. Using these methods, pixels are transferred as an
array of getNumDataElements() elements of a primitive type given
by getTransferType(). The TransferType may or may not be the same
as the storage DataType.

**Returns:** the number of data elements.
**See Also:** getDataElements(int, int, Object, DataBuffer)

,

getDataElements(int, int, int, int, Object, DataBuffer)

,

setDataElements(int, int, Object, DataBuffer)

,

setDataElements(int, int, int, int, Object, DataBuffer)

,

getTransferType()

---

#### getNumDataElements

public abstract int getNumDataElements()

Returns the number of data elements needed to transfer a pixel
via the getDataElements and setDataElements methods. When pixels
are transferred via these methods, they may be transferred in a
packed or unpacked format, depending on the implementation of the
SampleModel. Using these methods, pixels are transferred as an
array of getNumDataElements() elements of a primitive type given
by getTransferType(). The TransferType may or may not be the same
as the storage DataType.

getDataType

```java
public final int getDataType()
```

Returns the data type of the DataBuffer storing the pixel data.

**Returns:** the data type.

---

#### getDataType

public final int getDataType()

Returns the data type of the DataBuffer storing the pixel data.

getTransferType

```java
public int getTransferType()
```

Returns the TransferType used to transfer pixels via the
getDataElements and setDataElements methods. When pixels
are transferred via these methods, they may be transferred in a
packed or unpacked format, depending on the implementation of the
SampleModel. Using these methods, pixels are transferred as an
array of getNumDataElements() elements of a primitive type given
by getTransferType(). The TransferType may or may not be the same
as the storage DataType. The TransferType will be one of the types
defined in DataBuffer.

**Returns:** the transfer type.
**See Also:** getDataElements(int, int, Object, DataBuffer)

,

getDataElements(int, int, int, int, Object, DataBuffer)

,

setDataElements(int, int, Object, DataBuffer)

,

setDataElements(int, int, int, int, Object, DataBuffer)

,

getNumDataElements()

,

DataBuffer

---

#### getTransferType

public int getTransferType()

Returns the TransferType used to transfer pixels via the
getDataElements and setDataElements methods. When pixels
are transferred via these methods, they may be transferred in a
packed or unpacked format, depending on the implementation of the
SampleModel. Using these methods, pixels are transferred as an
array of getNumDataElements() elements of a primitive type given
by getTransferType(). The TransferType may or may not be the same
as the storage DataType. The TransferType will be one of the types
defined in DataBuffer.

getPixel

```java
public int[] getPixel​(int x,
int y,
int[] iArray,

DataBuffer
data)
```

Returns the samples for a specified pixel in an int array,
one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Parameters:** x

- The X coordinate of the pixel location
**Parameters:** y

- The Y coordinate of the pixel location
**Parameters:** iArray

- If non-null, returns the samples in this array
**Parameters:** data

- The DataBuffer containing the image data
**Returns:** the samples for the specified pixel.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if iArray is too small to hold the output.
**See Also:** setPixel(int, int, int[], DataBuffer)

---

#### getPixel

public int[] getPixel​(int x,
int y,
int[] iArray,

DataBuffer

data)

Returns the samples for a specified pixel in an int array,
one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

getDataElements

```java
public abstract
Object
getDataElements​(int x,
int y,

Object
obj,

DataBuffer
data)
```

Returns data for a single pixel in a primitive array of type
TransferType. For image data supported by the Java 2D API, this
will be one of DataBuffer.TYPE_BYTE, DataBuffer.TYPE_USHORT,
DataBuffer.TYPE_INT, DataBuffer.TYPE_SHORT, DataBuffer.TYPE_FLOAT,
or DataBuffer.TYPE_DOUBLE. Data may be returned in a packed format,
thus increasing efficiency for data transfers. Generally, obj
should be passed in as null, so that the Object will be created
automatically and will be of the right primitive data type.

The following code illustrates transferring data for one pixel from
DataBuffer

db1

, whose storage layout is described by
SampleModel

sm1

, to DataBuffer

db2

, whose
storage layout is described by SampleModel

sm2

.
The transfer will generally be more efficient than using
getPixel/setPixel.

```java
SampleModel sm1, sm2;
DataBuffer db1, db2;
sm2.setDataElements(x, y, sm1.getDataElements(x, y, null, db1), db2);
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

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** obj

- If non-null, a primitive array in which to return
the pixel data.
**Parameters:** data

- The DataBuffer containing the image data.
**Returns:** the data elements for the specified pixel.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if obj is too small to hold the output.
**See Also:** getNumDataElements()

,

getTransferType()

,

DataBuffer

,

setDataElements(int, int, Object, DataBuffer)

---

#### getDataElements

public abstract

Object

getDataElements​(int x,
int y,

Object

obj,

DataBuffer

data)

Returns data for a single pixel in a primitive array of type
TransferType. For image data supported by the Java 2D API, this
will be one of DataBuffer.TYPE_BYTE, DataBuffer.TYPE_USHORT,
DataBuffer.TYPE_INT, DataBuffer.TYPE_SHORT, DataBuffer.TYPE_FLOAT,
or DataBuffer.TYPE_DOUBLE. Data may be returned in a packed format,
thus increasing efficiency for data transfers. Generally, obj
should be passed in as null, so that the Object will be created
automatically and will be of the right primitive data type.

The following code illustrates transferring data for one pixel from
DataBuffer

db1

, whose storage layout is described by
SampleModel

sm1

, to DataBuffer

db2

, whose
storage layout is described by SampleModel

sm2

.
The transfer will generally be more efficient than using
getPixel/setPixel.

```java
SampleModel sm1, sm2;
DataBuffer db1, db2;
sm2.setDataElements(x, y, sm1.getDataElements(x, y, null, db1), db2);
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
SampleModel

sm1

, to DataBuffer

db2

, whose
storage layout is described by SampleModel

sm2

.
The transfer will generally be more efficient than using
getPixel/setPixel.

```java
SampleModel sm1, sm2;
DataBuffer db1, db2;
sm2.setDataElements(x, y, sm1.getDataElements(x, y, null, db1), db2);
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

SampleModel sm1, sm2;
DataBuffer db1, db2;
sm2.setDataElements(x, y, sm1.getDataElements(x, y, null, db1), db2);

If obj is non-null, it should be a primitive array of type TransferType.
Otherwise, a ClassCastException is thrown. An
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds, or if obj is non-null and is not large enough to hold
the pixel data.

getDataElements

```java
public
Object
getDataElements​(int x,
int y,
int w,
int h,

Object
obj,

DataBuffer
data)
```

Returns the pixel data for the specified rectangle of pixels in a
primitive array of type TransferType.
For image data supported by the Java 2D API, this
will be one of DataBuffer.TYPE_BYTE, DataBuffer.TYPE_USHORT,
DataBuffer.TYPE_INT, DataBuffer.TYPE_SHORT, DataBuffer.TYPE_FLOAT,
or DataBuffer.TYPE_DOUBLE. Data may be returned in a packed format,
thus increasing efficiency for data transfers. Generally, obj
should be passed in as null, so that the Object will be created
automatically and will be of the right primitive data type.

The following code illustrates transferring data for a rectangular
region of pixels from
DataBuffer

db1

, whose storage layout is described by
SampleModel

sm1

, to DataBuffer

db2

, whose
storage layout is described by SampleModel

sm2

.
The transfer will generally be more efficient than using
getPixels/setPixels.

```java
SampleModel sm1, sm2;
DataBuffer db1, db2;
sm2.setDataElements(x, y, w, h, sm1.getDataElements(x, y, w,
h, null, db1), db2);
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

**Parameters:** x

- The minimum X coordinate of the pixel rectangle.
**Parameters:** y

- The minimum Y coordinate of the pixel rectangle.
**Parameters:** w

- The width of the pixel rectangle.
**Parameters:** h

- The height of the pixel rectangle.
**Parameters:** obj

- If non-null, a primitive array in which to return
the pixel data.
**Parameters:** data

- The DataBuffer containing the image data.
**Returns:** the data elements for the specified region of pixels.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if obj is too small to hold the output.
**See Also:** getNumDataElements()

,

getTransferType()

,

setDataElements(int, int, int, int, Object, DataBuffer)

,

DataBuffer

---

#### getDataElements

public

Object

getDataElements​(int x,
int y,
int w,
int h,

Object

obj,

DataBuffer

data)

Returns the pixel data for the specified rectangle of pixels in a
primitive array of type TransferType.
For image data supported by the Java 2D API, this
will be one of DataBuffer.TYPE_BYTE, DataBuffer.TYPE_USHORT,
DataBuffer.TYPE_INT, DataBuffer.TYPE_SHORT, DataBuffer.TYPE_FLOAT,
or DataBuffer.TYPE_DOUBLE. Data may be returned in a packed format,
thus increasing efficiency for data transfers. Generally, obj
should be passed in as null, so that the Object will be created
automatically and will be of the right primitive data type.

The following code illustrates transferring data for a rectangular
region of pixels from
DataBuffer

db1

, whose storage layout is described by
SampleModel

sm1

, to DataBuffer

db2

, whose
storage layout is described by SampleModel

sm2

.
The transfer will generally be more efficient than using
getPixels/setPixels.

```java
SampleModel sm1, sm2;
DataBuffer db1, db2;
sm2.setDataElements(x, y, w, h, sm1.getDataElements(x, y, w,
h, null, db1), db2);
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

The following code illustrates transferring data for a rectangular
region of pixels from
DataBuffer

db1

, whose storage layout is described by
SampleModel

sm1

, to DataBuffer

db2

, whose
storage layout is described by SampleModel

sm2

.
The transfer will generally be more efficient than using
getPixels/setPixels.

```java
SampleModel sm1, sm2;
DataBuffer db1, db2;
sm2.setDataElements(x, y, w, h, sm1.getDataElements(x, y, w,
h, null, db1), db2);
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

SampleModel sm1, sm2;
DataBuffer db1, db2;
sm2.setDataElements(x, y, w, h, sm1.getDataElements(x, y, w,
h, null, db1), db2);

If obj is non-null, it should be a primitive array of type TransferType.
Otherwise, a ClassCastException is thrown. An
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds, or if obj is non-null and is not large enough to hold
the pixel data.

setDataElements

```java
public abstract void setDataElements​(int x,
int y,

Object
obj,

DataBuffer
data)
```

Sets the data for a single pixel in the specified DataBuffer from a
primitive array of type TransferType. For image data supported by
the Java 2D API, this will be one of DataBuffer.TYPE_BYTE,
DataBuffer.TYPE_USHORT, DataBuffer.TYPE_INT, DataBuffer.TYPE_SHORT,
DataBuffer.TYPE_FLOAT, or DataBuffer.TYPE_DOUBLE. Data in the array
may be in a packed format, thus increasing efficiency for data
transfers.

The following code illustrates transferring data for one pixel from
DataBuffer

db1

, whose storage layout is described by
SampleModel

sm1

, to DataBuffer

db2

, whose
storage layout is described by SampleModel

sm2

.
The transfer will generally be more efficient than using
getPixel/setPixel.

```java
SampleModel sm1, sm2;
DataBuffer db1, db2;
sm2.setDataElements(x, y, sm1.getDataElements(x, y, null, db1),
db2);
```

Using getDataElements/setDataElements to transfer between two
DataBuffer/SampleModel pairs is legitimate if the SampleModels have
the same number of bands, corresponding bands have the same number of
bits per sample, and the TransferTypes are the same.

obj must be a primitive array of type TransferType. Otherwise,
a ClassCastException is thrown. An
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds, or if obj is not large enough to hold the pixel data.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** obj

- A primitive array containing pixel data.
**Parameters:** data

- The DataBuffer containing the image data.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if obj is too small to hold the input.
**See Also:** getNumDataElements()

,

getTransferType()

,

getDataElements(int, int, Object, DataBuffer)

,

DataBuffer

---

#### setDataElements

public abstract void setDataElements​(int x,
int y,

Object

obj,

DataBuffer

data)

Sets the data for a single pixel in the specified DataBuffer from a
primitive array of type TransferType. For image data supported by
the Java 2D API, this will be one of DataBuffer.TYPE_BYTE,
DataBuffer.TYPE_USHORT, DataBuffer.TYPE_INT, DataBuffer.TYPE_SHORT,
DataBuffer.TYPE_FLOAT, or DataBuffer.TYPE_DOUBLE. Data in the array
may be in a packed format, thus increasing efficiency for data
transfers.

The following code illustrates transferring data for one pixel from
DataBuffer

db1

, whose storage layout is described by
SampleModel

sm1

, to DataBuffer

db2

, whose
storage layout is described by SampleModel

sm2

.
The transfer will generally be more efficient than using
getPixel/setPixel.

```java
SampleModel sm1, sm2;
DataBuffer db1, db2;
sm2.setDataElements(x, y, sm1.getDataElements(x, y, null, db1),
db2);
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
SampleModel

sm1

, to DataBuffer

db2

, whose
storage layout is described by SampleModel

sm2

.
The transfer will generally be more efficient than using
getPixel/setPixel.

```java
SampleModel sm1, sm2;
DataBuffer db1, db2;
sm2.setDataElements(x, y, sm1.getDataElements(x, y, null, db1),
db2);
```

Using getDataElements/setDataElements to transfer between two
DataBuffer/SampleModel pairs is legitimate if the SampleModels have
the same number of bands, corresponding bands have the same number of
bits per sample, and the TransferTypes are the same.

obj must be a primitive array of type TransferType. Otherwise,
a ClassCastException is thrown. An
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds, or if obj is not large enough to hold the pixel data.

SampleModel sm1, sm2;
DataBuffer db1, db2;
sm2.setDataElements(x, y, sm1.getDataElements(x, y, null, db1),
db2);

obj must be a primitive array of type TransferType. Otherwise,
a ClassCastException is thrown. An
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds, or if obj is not large enough to hold the pixel data.

setDataElements

```java
public void setDataElements​(int x,
int y,
int w,
int h,

Object
obj,

DataBuffer
data)
```

Sets the data for a rectangle of pixels in the specified DataBuffer
from a primitive array of type TransferType. For image data supported
by the Java 2D API, this will be one of DataBuffer.TYPE_BYTE,
DataBuffer.TYPE_USHORT, DataBuffer.TYPE_INT, DataBuffer.TYPE_SHORT,
DataBuffer.TYPE_FLOAT, or DataBuffer.TYPE_DOUBLE. Data in the array
may be in a packed format, thus increasing efficiency for data
transfers.

The following code illustrates transferring data for a rectangular
region of pixels from
DataBuffer

db1

, whose storage layout is described by
SampleModel

sm1

, to DataBuffer

db2

, whose
storage layout is described by SampleModel

sm2

.
The transfer will generally be more efficient than using
getPixels/setPixels.

```java
SampleModel sm1, sm2;
DataBuffer db1, db2;
sm2.setDataElements(x, y, w, h, sm1.getDataElements(x, y, w, h,
null, db1), db2);
```

Using getDataElements/setDataElements to transfer between two
DataBuffer/SampleModel pairs is legitimate if the SampleModels have
the same number of bands, corresponding bands have the same number of
bits per sample, and the TransferTypes are the same.

obj must be a primitive array of type TransferType. Otherwise,
a ClassCastException is thrown. An
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds, or if obj is not large enough to hold the pixel data.

**Parameters:** x

- The minimum X coordinate of the pixel rectangle.
**Parameters:** y

- The minimum Y coordinate of the pixel rectangle.
**Parameters:** w

- The width of the pixel rectangle.
**Parameters:** h

- The height of the pixel rectangle.
**Parameters:** obj

- A primitive array containing pixel data.
**Parameters:** data

- The DataBuffer containing the image data.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if obj is too small to hold the input.
**See Also:** getNumDataElements()

,

getTransferType()

,

getDataElements(int, int, int, int, Object, DataBuffer)

,

DataBuffer

---

#### setDataElements

public void setDataElements​(int x,
int y,
int w,
int h,

Object

obj,

DataBuffer

data)

Sets the data for a rectangle of pixels in the specified DataBuffer
from a primitive array of type TransferType. For image data supported
by the Java 2D API, this will be one of DataBuffer.TYPE_BYTE,
DataBuffer.TYPE_USHORT, DataBuffer.TYPE_INT, DataBuffer.TYPE_SHORT,
DataBuffer.TYPE_FLOAT, or DataBuffer.TYPE_DOUBLE. Data in the array
may be in a packed format, thus increasing efficiency for data
transfers.

The following code illustrates transferring data for a rectangular
region of pixels from
DataBuffer

db1

, whose storage layout is described by
SampleModel

sm1

, to DataBuffer

db2

, whose
storage layout is described by SampleModel

sm2

.
The transfer will generally be more efficient than using
getPixels/setPixels.

```java
SampleModel sm1, sm2;
DataBuffer db1, db2;
sm2.setDataElements(x, y, w, h, sm1.getDataElements(x, y, w, h,
null, db1), db2);
```

Using getDataElements/setDataElements to transfer between two
DataBuffer/SampleModel pairs is legitimate if the SampleModels have
the same number of bands, corresponding bands have the same number of
bits per sample, and the TransferTypes are the same.

obj must be a primitive array of type TransferType. Otherwise,
a ClassCastException is thrown. An
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds, or if obj is not large enough to hold the pixel data.

The following code illustrates transferring data for a rectangular
region of pixels from
DataBuffer

db1

, whose storage layout is described by
SampleModel

sm1

, to DataBuffer

db2

, whose
storage layout is described by SampleModel

sm2

.
The transfer will generally be more efficient than using
getPixels/setPixels.

```java
SampleModel sm1, sm2;
DataBuffer db1, db2;
sm2.setDataElements(x, y, w, h, sm1.getDataElements(x, y, w, h,
null, db1), db2);
```

Using getDataElements/setDataElements to transfer between two
DataBuffer/SampleModel pairs is legitimate if the SampleModels have
the same number of bands, corresponding bands have the same number of
bits per sample, and the TransferTypes are the same.

obj must be a primitive array of type TransferType. Otherwise,
a ClassCastException is thrown. An
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds, or if obj is not large enough to hold the pixel data.

SampleModel sm1, sm2;
DataBuffer db1, db2;
sm2.setDataElements(x, y, w, h, sm1.getDataElements(x, y, w, h,
null, db1), db2);

obj must be a primitive array of type TransferType. Otherwise,
a ClassCastException is thrown. An
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds, or if obj is not large enough to hold the pixel data.

getPixel

```java
public float[] getPixel​(int x,
int y,
float[] fArray,

DataBuffer
data)
```

Returns the samples for the specified pixel in an array of float.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** fArray

- If non-null, returns the samples in this array.
**Parameters:** data

- The DataBuffer containing the image data.
**Returns:** the samples for the specified pixel.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if fArray is too small to hold the output.
**See Also:** setPixel(int, int, float[], DataBuffer)

---

#### getPixel

public float[] getPixel​(int x,
int y,
float[] fArray,

DataBuffer

data)

Returns the samples for the specified pixel in an array of float.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

getPixel

```java
public double[] getPixel​(int x,
int y,
double[] dArray,

DataBuffer
data)
```

Returns the samples for the specified pixel in an array of double.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** dArray

- If non-null, returns the samples in this array.
**Parameters:** data

- The DataBuffer containing the image data.
**Returns:** the samples for the specified pixel.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if dArray is too small to hold the output.
**See Also:** setPixel(int, int, double[], DataBuffer)

---

#### getPixel

public double[] getPixel​(int x,
int y,
double[] dArray,

DataBuffer

data)

Returns the samples for the specified pixel in an array of double.
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

Returns all samples for a rectangle of pixels in an
int array, one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

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
**Returns:** the samples for the specified region of pixels.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if iArray is too small to hold the output.
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

Returns all samples for a rectangle of pixels in an
int array, one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

getPixels

```java
public float[] getPixels​(int x,
int y,
int w,
int h,
float[] fArray,

DataBuffer
data)
```

Returns all samples for a rectangle of pixels in a float
array, one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Parameters:** x

- The X coordinate of the upper left pixel location.
**Parameters:** y

- The Y coordinate of the upper left pixel location.
**Parameters:** w

- The width of the pixel rectangle.
**Parameters:** h

- The height of the pixel rectangle.
**Parameters:** fArray

- If non-null, returns the samples in this array.
**Parameters:** data

- The DataBuffer containing the image data.
**Returns:** the samples for the specified region of pixels.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if fArray is too small to hold the output.
**See Also:** setPixels(int, int, int, int, float[], DataBuffer)

---

#### getPixels

public float[] getPixels​(int x,
int y,
int w,
int h,
float[] fArray,

DataBuffer

data)

Returns all samples for a rectangle of pixels in a float
array, one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

getPixels

```java
public double[] getPixels​(int x,
int y,
int w,
int h,
double[] dArray,

DataBuffer
data)
```

Returns all samples for a rectangle of pixels in a double
array, one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Parameters:** x

- The X coordinate of the upper left pixel location.
**Parameters:** y

- The Y coordinate of the upper left pixel location.
**Parameters:** w

- The width of the pixel rectangle.
**Parameters:** h

- The height of the pixel rectangle.
**Parameters:** dArray

- If non-null, returns the samples in this array.
**Parameters:** data

- The DataBuffer containing the image data.
**Returns:** the samples for the specified region of pixels.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if dArray is too small to hold the output.
**See Also:** setPixels(int, int, int, int, double[], DataBuffer)

---

#### getPixels

public double[] getPixels​(int x,
int y,
int w,
int h,
double[] dArray,

DataBuffer

data)

Returns all samples for a rectangle of pixels in a double
array, one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

getSample

```java
public abstract int getSample​(int x,
int y,
int b,

DataBuffer
data)
```

Returns the sample in a specified band for the pixel located
at (x,y) as an int.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** b

- The band to return.
**Parameters:** data

- The DataBuffer containing the image data.
**Returns:** the sample in a specified band for the specified pixel.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds.
**See Also:** setSample(int, int, int, int, DataBuffer)

---

#### getSample

public abstract int getSample​(int x,
int y,
int b,

DataBuffer

data)

Returns the sample in a specified band for the pixel located
at (x,y) as an int.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

getSampleFloat

```java
public float getSampleFloat​(int x,
int y,
int b,

DataBuffer
data)
```

Returns the sample in a specified band
for the pixel located at (x,y) as a float.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** b

- The band to return.
**Parameters:** data

- The DataBuffer containing the image data.
**Returns:** the sample in a specified band for the specified pixel.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds.

---

#### getSampleFloat

public float getSampleFloat​(int x,
int y,
int b,

DataBuffer

data)

Returns the sample in a specified band
for the pixel located at (x,y) as a float.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

getSampleDouble

```java
public double getSampleDouble​(int x,
int y,
int b,

DataBuffer
data)
```

Returns the sample in a specified band
for a pixel located at (x,y) as a double.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** b

- The band to return.
**Parameters:** data

- The DataBuffer containing the image data.
**Returns:** the sample in a specified band for the specified pixel.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds.

---

#### getSampleDouble

public double getSampleDouble​(int x,
int y,
int b,

DataBuffer

data)

Returns the sample in a specified band
for a pixel located at (x,y) as a double.
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
**Returns:** the samples for the specified band for the specified region
of pixels.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds, or if iArray is too small to
hold the output.
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

getSamples

```java
public float[] getSamples​(int x,
int y,
int w,
int h,
int b,
float[] fArray,

DataBuffer
data)
```

Returns the samples for a specified band for the specified rectangle
of pixels in a float array, one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

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
**Parameters:** fArray

- If non-null, returns the samples in this array.
**Parameters:** data

- The DataBuffer containing the image data.
**Returns:** the samples for the specified band for the specified region
of pixels.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds, or if fArray is too small to
hold the output.
**See Also:** setSamples(int, int, int, int, int, float[], DataBuffer)

---

#### getSamples

public float[] getSamples​(int x,
int y,
int w,
int h,
int b,
float[] fArray,

DataBuffer

data)

Returns the samples for a specified band for the specified rectangle
of pixels in a float array, one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

getSamples

```java
public double[] getSamples​(int x,
int y,
int w,
int h,
int b,
double[] dArray,

DataBuffer
data)
```

Returns the samples for a specified band for a specified rectangle
of pixels in a double array, one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

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
**Parameters:** dArray

- If non-null, returns the samples in this array.
**Parameters:** data

- The DataBuffer containing the image data.
**Returns:** the samples for the specified band for the specified region
of pixels.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds, or if dArray is too small to
hold the output.
**See Also:** setSamples(int, int, int, int, int, double[], DataBuffer)

---

#### getSamples

public double[] getSamples​(int x,
int y,
int w,
int h,
int b,
double[] dArray,

DataBuffer

data)

Returns the samples for a specified band for a specified rectangle
of pixels in a double array, one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

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

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** iArray

- The input samples in an int array.
**Parameters:** data

- The DataBuffer containing the image data.
**Throws:** NullPointerException

- if iArray or data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if iArray is too small to hold the input.
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

setPixel

```java
public void setPixel​(int x,
int y,
float[] fArray,

DataBuffer
data)
```

Sets a pixel in the DataBuffer using a float array of samples for input.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** fArray

- The input samples in a float array.
**Parameters:** data

- The DataBuffer containing the image data.
**Throws:** NullPointerException

- if fArray or data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if fArray is too small to hold the input.
**See Also:** getPixel(int, int, float[], DataBuffer)

---

#### setPixel

public void setPixel​(int x,
int y,
float[] fArray,

DataBuffer

data)

Sets a pixel in the DataBuffer using a float array of samples for input.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

setPixel

```java
public void setPixel​(int x,
int y,
double[] dArray,

DataBuffer
data)
```

Sets a pixel in the DataBuffer using a double array of samples
for input.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** dArray

- The input samples in a double array.
**Parameters:** data

- The DataBuffer containing the image data.
**Throws:** NullPointerException

- if dArray or data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if fArray is too small to hold the input.
**See Also:** getPixel(int, int, double[], DataBuffer)

---

#### setPixel

public void setPixel​(int x,
int y,
double[] dArray,

DataBuffer

data)

Sets a pixel in the DataBuffer using a double array of samples
for input.

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
**Throws:** NullPointerException

- if iArray or data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if iArray is too small to hold the input.
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

setPixels

```java
public void setPixels​(int x,
int y,
int w,
int h,
float[] fArray,

DataBuffer
data)
```

Sets all samples for a rectangle of pixels from a float array containing
one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Parameters:** x

- The X coordinate of the upper left pixel location.
**Parameters:** y

- The Y coordinate of the upper left pixel location.
**Parameters:** w

- The width of the pixel rectangle.
**Parameters:** h

- The height of the pixel rectangle.
**Parameters:** fArray

- The input samples in a float array.
**Parameters:** data

- The DataBuffer containing the image data.
**Throws:** NullPointerException

- if fArray or data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if fArray is too small to hold the input.
**See Also:** getPixels(int, int, int, int, float[], DataBuffer)

---

#### setPixels

public void setPixels​(int x,
int y,
int w,
int h,
float[] fArray,

DataBuffer

data)

Sets all samples for a rectangle of pixels from a float array containing
one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

setPixels

```java
public void setPixels​(int x,
int y,
int w,
int h,
double[] dArray,

DataBuffer
data)
```

Sets all samples for a rectangle of pixels from a double array
containing one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Parameters:** x

- The X coordinate of the upper left pixel location.
**Parameters:** y

- The Y coordinate of the upper left pixel location.
**Parameters:** w

- The width of the pixel rectangle.
**Parameters:** h

- The height of the pixel rectangle.
**Parameters:** dArray

- The input samples in a double array.
**Parameters:** data

- The DataBuffer containing the image data.
**Throws:** NullPointerException

- if dArray or data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are
not in bounds, or if dArray is too small to hold the input.
**See Also:** getPixels(int, int, int, int, double[], DataBuffer)

---

#### setPixels

public void setPixels​(int x,
int y,
int w,
int h,
double[] dArray,

DataBuffer

data)

Sets all samples for a rectangle of pixels from a double array
containing one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

setSample

```java
public abstract void setSample​(int x,
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
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds.
**See Also:** getSample(int, int, int, DataBuffer)

---

#### setSample

public abstract void setSample​(int x,
int y,
int b,
int s,

DataBuffer

data)

Sets a sample in the specified band for the pixel located at (x,y)
in the DataBuffer using an int for input.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

setSample

```java
public void setSample​(int x,
int y,
int b,
float s,

DataBuffer
data)
```

Sets a sample in the specified band for the pixel located at (x,y)
in the DataBuffer using a float for input.
The default implementation of this method casts the input
float sample to an int and then calls the

setSample(int, int, int, DataBuffer)

method using
that int value.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** b

- The band to set.
**Parameters:** s

- The input sample as a float.
**Parameters:** data

- The DataBuffer containing the image data.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds.
**See Also:** getSample(int, int, int, DataBuffer)

---

#### setSample

public void setSample​(int x,
int y,
int b,
float s,

DataBuffer

data)

Sets a sample in the specified band for the pixel located at (x,y)
in the DataBuffer using a float for input.
The default implementation of this method casts the input
float sample to an int and then calls the

setSample(int, int, int, DataBuffer)

method using
that int value.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

setSample

```java
public void setSample​(int x,
int y,
int b,
double s,

DataBuffer
data)
```

Sets a sample in the specified band for the pixel located at (x,y)
in the DataBuffer using a double for input.
The default implementation of this method casts the input
double sample to an int and then calls the

setSample(int, int, int, DataBuffer)

method using
that int value.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** b

- The band to set.
**Parameters:** s

- The input sample as a double.
**Parameters:** data

- The DataBuffer containing the image data.
**Throws:** NullPointerException

- if data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds.
**See Also:** getSample(int, int, int, DataBuffer)

---

#### setSample

public void setSample​(int x,
int y,
int b,
double s,

DataBuffer

data)

Sets a sample in the specified band for the pixel located at (x,y)
in the DataBuffer using a double for input.
The default implementation of this method casts the input
double sample to an int and then calls the

setSample(int, int, int, DataBuffer)

method using
that int value.
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
**Throws:** NullPointerException

- if iArray or data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds, or if iArray is too small to
hold the input.
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

setSamples

```java
public void setSamples​(int x,
int y,
int w,
int h,
int b,
float[] fArray,

DataBuffer
data)
```

Sets the samples in the specified band for the specified rectangle
of pixels from a float array containing one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

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
**Parameters:** fArray

- The input samples in a float array.
**Parameters:** data

- The DataBuffer containing the image data.
**Throws:** NullPointerException

- if fArray or data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds, or if fArray is too small to
hold the input.
**See Also:** getSamples(int, int, int, int, int, float[], DataBuffer)

---

#### setSamples

public void setSamples​(int x,
int y,
int w,
int h,
int b,
float[] fArray,

DataBuffer

data)

Sets the samples in the specified band for the specified rectangle
of pixels from a float array containing one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

setSamples

```java
public void setSamples​(int x,
int y,
int w,
int h,
int b,
double[] dArray,

DataBuffer
data)
```

Sets the samples in the specified band for the specified rectangle
of pixels from a double array containing one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

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
**Parameters:** dArray

- The input samples in a double array.
**Parameters:** data

- The DataBuffer containing the image data.
**Throws:** NullPointerException

- if dArray or data is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds, or if dArray is too small to
hold the input.
**See Also:** getSamples(int, int, int, int, int, double[], DataBuffer)

---

#### setSamples

public void setSamples​(int x,
int y,
int w,
int h,
int b,
double[] dArray,

DataBuffer

data)

Sets the samples in the specified band for the specified rectangle
of pixels from a double array containing one sample per array element.
ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.

createCompatibleSampleModel

```java
public abstract
SampleModel
createCompatibleSampleModel​(int w,
int h)
```

Creates a SampleModel which describes data in this SampleModel's
format, but with a different width and height.

**Parameters:** w

- the width of the image data
**Parameters:** h

- the height of the image data
**Returns:** a

SampleModel

describing the same image
data as this

SampleModel

, but with a
different size.

---

#### createCompatibleSampleModel

public abstract

SampleModel

createCompatibleSampleModel​(int w,
int h)

Creates a SampleModel which describes data in this SampleModel's
format, but with a different width and height.

createSubsetSampleModel

```java
public abstract
SampleModel
createSubsetSampleModel​(int[] bands)
```

Creates a new SampleModel
with a subset of the bands of this
SampleModel.

**Parameters:** bands

- the subset of bands of this

SampleModel
**Returns:** a

SampleModel

with a subset of bands of this

SampleModel

.

---

#### createSubsetSampleModel

public abstract

SampleModel

createSubsetSampleModel​(int[] bands)

Creates a new SampleModel
with a subset of the bands of this
SampleModel.

createDataBuffer

```java
public abstract
DataBuffer
createDataBuffer()
```

Creates a DataBuffer that corresponds to this SampleModel.
The DataBuffer's width and height will match this SampleModel's.

**Returns:** a

DataBuffer

corresponding to this

SampleModel

.

---

#### createDataBuffer

public abstract

DataBuffer

createDataBuffer()

Creates a DataBuffer that corresponds to this SampleModel.
The DataBuffer's width and height will match this SampleModel's.

getSampleSize

```java
public abstract int[] getSampleSize()
```

Returns the size in bits of samples for all bands.

**Returns:** the size of samples for all bands.

---

#### getSampleSize

public abstract int[] getSampleSize()

Returns the size in bits of samples for all bands.

getSampleSize

```java
public abstract int getSampleSize​(int band)
```

Returns the size in bits of samples for the specified band.

**Parameters:** band

- the specified band
**Returns:** the size of the samples of the specified band.

---

#### getSampleSize

public abstract int getSampleSize​(int band)

Returns the size in bits of samples for the specified band.

---

