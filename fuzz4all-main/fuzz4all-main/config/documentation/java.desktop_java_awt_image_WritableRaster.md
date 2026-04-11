# Class WritableRaster

**Source:** `java.desktop\java\awt\image\WritableRaster.html`

### Class Description

```java
public class
WritableRaster

extends
Raster
```

This class extends Raster to provide pixel writing capabilities.
Refer to the class comment for Raster for descriptions of how
a Raster stores pixels.

The constructors of this class are protected. To instantiate
a WritableRaster, use one of the createWritableRaster factory methods
in the Raster class.

---

### Field Details

*No entries found.*

### Constructor Details

#### protected WritableRaster​(
SampleModel
sampleModel,

Point
origin)

Constructs a WritableRaster with the given SampleModel. The
WritableRaster's upper left corner is origin and it is the
same size as the SampleModel. A DataBuffer large enough to
describe the WritableRaster is automatically created.

**Parameters:**
- sampleModel

- The SampleModel that specifies the layout.
- origin

- The Point that specifies the origin.

**Throws:**
- RasterFormatException

- if computing either

origin.x + sampleModel.getWidth()

or

origin.y + sampleModel.getHeight()

results
in integer overflow

---

#### protected WritableRaster​(
SampleModel
sampleModel,

DataBuffer
dataBuffer,

Point
origin)

Constructs a WritableRaster with the given SampleModel and DataBuffer.
The WritableRaster's upper left corner is origin and it is the same
size as the SampleModel. The DataBuffer is not initialized and must
be compatible with SampleModel.

**Parameters:**
- sampleModel

- The SampleModel that specifies the layout.
- dataBuffer

- The DataBuffer that contains the image data.
- origin

- The Point that specifies the origin.

**Throws:**
- RasterFormatException

- if computing either

origin.x + sampleModel.getWidth()

or

origin.y + sampleModel.getHeight()

results
in integer overflow

---

#### protected WritableRaster​(
SampleModel
sampleModel,

DataBuffer
dataBuffer,

Rectangle
aRegion,

Point
sampleModelTranslate,

WritableRaster
parent)

Constructs a WritableRaster with the given SampleModel, DataBuffer,
and parent. aRegion specifies the bounding rectangle of the new
Raster. When translated into the base Raster's coordinate
system, aRegion must be contained by the base Raster.
(The base Raster is the Raster's ancestor which has no parent.)
sampleModelTranslate specifies the sampleModelTranslateX and
sampleModelTranslateY values of the new Raster.

Note that this constructor should generally be called by other
constructors or create methods, it should not be used directly.

**Parameters:**
- sampleModel

- The SampleModel that specifies the layout.
- dataBuffer

- The DataBuffer that contains the image data.
- aRegion

- The Rectangle that specifies the image area.
- sampleModelTranslate

- The Point that specifies the translation
from SampleModel to Raster coordinates.
- parent

- The parent (if any) of this raster.

**Throws:**
- RasterFormatException

- if

aRegion

has width
or height less than or equal to zero, or computing either

aRegion.x + aRegion.width

or

aRegion.y + aRegion.height

results in integer
overflow

---

### Method Details

#### public
WritableRaster
getWritableParent()

Returns the parent WritableRaster (if any) of this WritableRaster,
or else null.

**Returns:**
- the parent of this

WritableRaster

, or

null

.

---

#### public
WritableRaster
createWritableTranslatedChild​(int childMinX,
int childMinY)

Create a WritableRaster with the same size, SampleModel and DataBuffer
as this one, but with a different location. The new WritableRaster
will possess a reference to the current WritableRaster, accessible
through its getParent() and getWritableParent() methods.

**Parameters:**
- childMinX

- X coord of the upper left corner of the new Raster.
- childMinY

- Y coord of the upper left corner of the new Raster.

**Returns:**
- a

WritableRaster

the same as this one except
for the specified location.

**Throws:**
- RasterFormatException

- if computing either

childMinX + this.getWidth()

or

childMinY + this.getHeight()

results in integer
overflow

---

#### public
WritableRaster
createWritableChild​(int parentX,
int parentY,
int w,
int h,
int childMinX,
int childMinY,
int[] bandList)

Returns a new WritableRaster which shares all or part of this
WritableRaster's DataBuffer. The new WritableRaster will
possess a reference to the current WritableRaster, accessible
through its getParent() and getWritableParent() methods.

The parentX, parentY, width and height parameters form a
Rectangle in this WritableRaster's coordinate space, indicating
the area of pixels to be shared. An error will be thrown if
this Rectangle is not contained with the bounds of the current
WritableRaster.

The new WritableRaster may additionally be translated to a
different coordinate system for the plane than that used by the current
WritableRaster. The childMinX and childMinY parameters give
the new (x, y) coordinate of the upper-left pixel of the
returned WritableRaster; the coordinate (childMinX, childMinY)
in the new WritableRaster will map to the same pixel as the
coordinate (parentX, parentY) in the current WritableRaster.

The new WritableRaster may be defined to contain only a
subset of the bands of the current WritableRaster, possibly
reordered, by means of the bandList parameter. If bandList is
null, it is taken to include all of the bands of the current
WritableRaster in their current order.

To create a new WritableRaster that contains a subregion of
the current WritableRaster, but shares its coordinate system
and bands, this method should be called with childMinX equal to
parentX, childMinY equal to parentY, and bandList equal to
null.

**Parameters:**
- parentX

- X coordinate of the upper left corner in this
WritableRaster's coordinates.
- parentY

- Y coordinate of the upper left corner in this
WritableRaster's coordinates.
- w

- Width of the region starting at (parentX, parentY).
- h

- Height of the region starting at (parentX, parentY).
- childMinX

- X coordinate of the upper left corner of
the returned WritableRaster.
- childMinY

- Y coordinate of the upper left corner of
the returned WritableRaster.
- bandList

- Array of band indices, or null to use all bands.

**Returns:**
- a

WritableRaster

sharing all or part of the

DataBuffer

of this

WritableRaster

.

**Throws:**
- RasterFormatException

- if the subregion is outside of the
raster bounds.
- RasterFormatException

- if

w

or

h

is less than or equal to zero, or computing any of

parentX + w

,

parentY + h

,

childMinX + w

, or

childMinY + h

results in integer
overflow

---

#### public void setDataElements​(int x,
int y,

Object
inData)

Sets the data for a single pixel from a
primitive array of type TransferType. For image data supported by
the Java 2D(tm) API, this will be one of DataBuffer.TYPE_BYTE,
DataBuffer.TYPE_USHORT, DataBuffer.TYPE_INT, DataBuffer.TYPE_SHORT,
DataBuffer.TYPE_FLOAT, or DataBuffer.TYPE_DOUBLE. Data in the array
may be in a packed format, thus increasing efficiency for data
transfers.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds, or if inData is not large enough to hold the pixel data.
However, explicit bounds checking is not guaranteed.
A ClassCastException will be thrown if the input object is not null
and references anything other than an array of TransferType.

**Parameters:**
- x

- The X coordinate of the pixel location.
- y

- The Y coordinate of the pixel location.
- inData

- An object reference to an array of type defined by
getTransferType() and length getNumDataElements()
containing the pixel data to place at x,y.

**Throws:**
- ArrayIndexOutOfBoundsException

- if the coordinates are not
in bounds, or if inData is too small to hold the input.

**See Also:**
- SampleModel.setDataElements(int, int, Object, DataBuffer)

---

#### public void setDataElements​(int x,
int y,

Raster
inRaster)

Sets the data for a rectangle of pixels from an input Raster.
The input Raster must be compatible with this WritableRaster
in that they must have the same number of bands, corresponding bands
must have the same number of bits per sample, the TransferTypes
and NumDataElements must be the same, and the packing used by
the getDataElements/setDataElements must be identical.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

**Parameters:**
- x

- The X coordinate of the pixel location.
- y

- The Y coordinate of the pixel location.
- inRaster

- Raster containing data to place at x,y.

**Throws:**
- NullPointerException

- if inRaster is null.
- ArrayIndexOutOfBoundsException

- if the coordinates are not
in bounds.

---

#### public void setDataElements​(int x,
int y,
int w,
int h,

Object
inData)

Sets the data for a rectangle of pixels from a
primitive array of type TransferType. For image data supported by
the Java 2D API, this will be one of DataBuffer.TYPE_BYTE,
DataBuffer.TYPE_USHORT, DataBuffer.TYPE_INT, DataBuffer.TYPE_SHORT,
DataBuffer.TYPE_FLOAT, or DataBuffer.TYPE_DOUBLE. Data in the array
may be in a packed format, thus increasing efficiency for data
transfers.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds, or if inData is not large enough to hold the pixel data.
However, explicit bounds checking is not guaranteed.
A ClassCastException will be thrown if the input object is not null
and references anything other than an array of TransferType.

**Parameters:**
- x

- The X coordinate of the upper left pixel location.
- y

- The Y coordinate of the upper left pixel location.
- w

- Width of the pixel rectangle.
- h

- Height of the pixel rectangle.
- inData

- An object reference to an array of type defined by
getTransferType() and length w*h*getNumDataElements()
containing the pixel data to place between x,y and
x+w-1, y+h-1.

**Throws:**
- NullPointerException

- if inData is null.
- ArrayIndexOutOfBoundsException

- if the coordinates are not
in bounds, or if inData is too small to hold the input.

**See Also:**
- SampleModel.setDataElements(int, int, int, int, Object, DataBuffer)

---

#### public void setRect​(
Raster
srcRaster)

Copies pixels from Raster srcRaster to this WritableRaster. Each pixel
in srcRaster is copied to the same x,y address in this raster, unless
the address falls outside the bounds of this raster. srcRaster
must have the same number of bands as this WritableRaster. The
copy is a simple copy of source samples to the corresponding destination
samples.

If all samples of both source and destination Rasters are of
integral type and less than or equal to 32 bits in size, then calling
this method is equivalent to executing the following code for all

x,y

addresses valid in both Rasters.

```java
Raster srcRaster;
WritableRaster dstRaster;
for (int b = 0; b < srcRaster.getNumBands(); b++) {
dstRaster.setSample(x, y, b, srcRaster.getSample(x, y, b));
}
```

Thus, when copying an integral type source to an integral type
destination, if the source sample size is greater than the destination
sample size for a particular band, the high order bits of the source
sample are truncated. If the source sample size is less than the
destination size for a particular band, the high order bits of the
destination are zero-extended or sign-extended depending on whether
srcRaster's SampleModel treats the sample as a signed or unsigned
quantity.

When copying a float or double source to an integral type destination,
each source sample is cast to the destination type. When copying an
integral type source to a float or double destination, the source
is first converted to a 32-bit int (if necessary), using the above
rules for integral types, and then the int is cast to float or
double.

**Parameters:**
- srcRaster

- The Raster from which to copy pixels.

**Throws:**
- NullPointerException

- if srcRaster is null.

---

#### public void setRect​(int dx,
int dy,

Raster
srcRaster)

Copies pixels from Raster srcRaster to this WritableRaster.
For each (x, y) address in srcRaster, the corresponding pixel
is copied to address (x+dx, y+dy) in this WritableRaster,
unless (x+dx, y+dy) falls outside the bounds of this raster.
srcRaster must have the same number of bands as this WritableRaster.
The copy is a simple copy of source samples to the corresponding
destination samples. For details, see

setRect(Raster)

.

**Parameters:**
- dx

- The X translation factor from src space to dst space
of the copy.
- dy

- The Y translation factor from src space to dst space
of the copy.
- srcRaster

- The Raster from which to copy pixels.

**Throws:**
- NullPointerException

- if srcRaster is null.

---

#### public void setPixel​(int x,
int y,
int[] iArray)

Sets a pixel in the DataBuffer using an int array of samples for input.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

**Parameters:**
- x

- The X coordinate of the pixel location.
- y

- The Y coordinate of the pixel location.
- iArray

- The input samples in a int array.

**Throws:**
- NullPointerException

- if iArray is null.
- ArrayIndexOutOfBoundsException

- if the coordinates are not
in bounds, or if iArray is too small to hold the input.

---

#### public void setPixel​(int x,
int y,
float[] fArray)

Sets a pixel in the DataBuffer using a float array of samples for input.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

**Parameters:**
- x

- The X coordinate of the pixel location.
- y

- The Y coordinate of the pixel location.
- fArray

- The input samples in a float array.

**Throws:**
- NullPointerException

- if fArray is null.
- ArrayIndexOutOfBoundsException

- if the coordinates are not
in bounds, or if fArray is too small to hold the input.

---

#### public void setPixel​(int x,
int y,
double[] dArray)

Sets a pixel in the DataBuffer using a double array of samples for input.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

**Parameters:**
- x

- The X coordinate of the pixel location.
- y

- The Y coordinate of the pixel location.
- dArray

- The input samples in a double array.

**Throws:**
- NullPointerException

- if dArray is null.
- ArrayIndexOutOfBoundsException

- if the coordinates are not
in bounds, or if dArray is too small to hold the input.

---

#### public void setPixels​(int x,
int y,
int w,
int h,
int[] iArray)

Sets all samples for a rectangle of pixels from an int array containing
one sample per array element.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

**Parameters:**
- x

- The X coordinate of the upper left pixel location.
- y

- The Y coordinate of the upper left pixel location.
- w

- Width of the pixel rectangle.
- h

- Height of the pixel rectangle.
- iArray

- The input int pixel array.

**Throws:**
- NullPointerException

- if iArray is null.
- ArrayIndexOutOfBoundsException

- if the coordinates are not
in bounds, or if iArray is too small to hold the input.

---

#### public void setPixels​(int x,
int y,
int w,
int h,
float[] fArray)

Sets all samples for a rectangle of pixels from a float array containing
one sample per array element.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

**Parameters:**
- x

- The X coordinate of the upper left pixel location.
- y

- The Y coordinate of the upper left pixel location.
- w

- Width of the pixel rectangle.
- h

- Height of the pixel rectangle.
- fArray

- The input float pixel array.

**Throws:**
- NullPointerException

- if fArray is null.
- ArrayIndexOutOfBoundsException

- if the coordinates are not
in bounds, or if fArray is too small to hold the input.

---

#### public void setPixels​(int x,
int y,
int w,
int h,
double[] dArray)

Sets all samples for a rectangle of pixels from a double array containing
one sample per array element.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

**Parameters:**
- x

- The X coordinate of the upper left pixel location.
- y

- The Y coordinate of the upper left pixel location.
- w

- Width of the pixel rectangle.
- h

- Height of the pixel rectangle.
- dArray

- The input double pixel array.

**Throws:**
- NullPointerException

- if dArray is null.
- ArrayIndexOutOfBoundsException

- if the coordinates are not
in bounds, or if dArray is too small to hold the input.

---

#### public void setSample​(int x,
int y,
int b,
int s)

Sets a sample in the specified band for the pixel located at (x,y)
in the DataBuffer using an int for input.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

**Parameters:**
- x

- The X coordinate of the pixel location.
- y

- The Y coordinate of the pixel location.
- b

- The band to set.
- s

- The input sample.

**Throws:**
- ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds.

---

#### public void setSample​(int x,
int y,
int b,
float s)

Sets a sample in the specified band for the pixel located at (x,y)
in the DataBuffer using a float for input.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

**Parameters:**
- x

- The X coordinate of the pixel location.
- y

- The Y coordinate of the pixel location.
- b

- The band to set.
- s

- The input sample as a float.

**Throws:**
- ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds.

---

#### public void setSample​(int x,
int y,
int b,
double s)

Sets a sample in the specified band for the pixel located at (x,y)
in the DataBuffer using a double for input.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

**Parameters:**
- x

- The X coordinate of the pixel location.
- y

- The Y coordinate of the pixel location.
- b

- The band to set.
- s

- The input sample as a double.

**Throws:**
- ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds.

---

#### public void setSamples​(int x,
int y,
int w,
int h,
int b,
int[] iArray)

Sets the samples in the specified band for the specified rectangle
of pixels from an int array containing one sample per array element.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

**Parameters:**
- x

- The X coordinate of the upper left pixel location.
- y

- The Y coordinate of the upper left pixel location.
- w

- Width of the pixel rectangle.
- h

- Height of the pixel rectangle.
- b

- The band to set.
- iArray

- The input int sample array.

**Throws:**
- NullPointerException

- if iArray is null.
- ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds, or if iArray is too small to
hold the input.

---

#### public void setSamples​(int x,
int y,
int w,
int h,
int b,
float[] fArray)

Sets the samples in the specified band for the specified rectangle
of pixels from a float array containing one sample per array element.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

**Parameters:**
- x

- The X coordinate of the upper left pixel location.
- y

- The Y coordinate of the upper left pixel location.
- w

- Width of the pixel rectangle.
- h

- Height of the pixel rectangle.
- b

- The band to set.
- fArray

- The input float sample array.

**Throws:**
- NullPointerException

- if fArray is null.
- ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds, or if fArray is too small to
hold the input.

---

#### public void setSamples​(int x,
int y,
int w,
int h,
int b,
double[] dArray)

Sets the samples in the specified band for the specified rectangle
of pixels from a double array containing one sample per array element.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

**Parameters:**
- x

- The X coordinate of the upper left pixel location.
- y

- The Y coordinate of the upper left pixel location.
- w

- Width of the pixel rectangle.
- h

- Height of the pixel rectangle.
- b

- The band to set.
- dArray

- The input double sample array.

**Throws:**
- NullPointerException

- if dArray is null.
- ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds, or if dArray is too small to
hold the input.

---

### Additional Sections

#### Class WritableRaster

java.lang.Object

- java.awt.image.Raster
- - java.awt.image.WritableRaster

java.awt.image.Raster

- java.awt.image.WritableRaster

java.awt.image.WritableRaster

```java
public class
WritableRaster

extends
Raster
```

This class extends Raster to provide pixel writing capabilities.
Refer to the class comment for Raster for descriptions of how
a Raster stores pixels.

The constructors of this class are protected. To instantiate
a WritableRaster, use one of the createWritableRaster factory methods
in the Raster class.

public class

WritableRaster

extends

Raster

This class extends Raster to provide pixel writing capabilities.
Refer to the class comment for Raster for descriptions of how
a Raster stores pixels.

The constructors of this class are protected. To instantiate
a WritableRaster, use one of the createWritableRaster factory methods
in the Raster class.

The constructors of this class are protected. To instantiate
a WritableRaster, use one of the createWritableRaster factory methods
in the Raster class.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.awt.image.

Raster

dataBuffer

,

height

,

minX

,

minY

,

numBands

,

numDataElements

,

parent

,

sampleModel

,

sampleModelTranslateX

,

sampleModelTranslateY

,

width

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

WritableRaster

​(

SampleModel

sampleModel,

DataBuffer

dataBuffer,

Point

origin)

Constructs a WritableRaster with the given SampleModel and DataBuffer.

protected

WritableRaster

​(

SampleModel

sampleModel,

DataBuffer

dataBuffer,

Rectangle

aRegion,

Point

sampleModelTranslate,

WritableRaster

parent)

Constructs a WritableRaster with the given SampleModel, DataBuffer,
and parent.

protected

WritableRaster

​(

SampleModel

sampleModel,

Point

origin)

Constructs a WritableRaster with the given SampleModel.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

WritableRaster

createWritableChild

​(int parentX,
int parentY,
int w,
int h,
int childMinX,
int childMinY,
int[] bandList)

Returns a new WritableRaster which shares all or part of this
WritableRaster's DataBuffer.

WritableRaster

createWritableTranslatedChild

​(int childMinX,
int childMinY)

Create a WritableRaster with the same size, SampleModel and DataBuffer
as this one, but with a different location.

WritableRaster

getWritableParent

()

Returns the parent WritableRaster (if any) of this WritableRaster,
or else null.

void

setDataElements

​(int x,
int y,
int w,
int h,

Object

inData)

Sets the data for a rectangle of pixels from a
primitive array of type TransferType.

void

setDataElements

​(int x,
int y,

Raster

inRaster)

Sets the data for a rectangle of pixels from an input Raster.

void

setDataElements

​(int x,
int y,

Object

inData)

Sets the data for a single pixel from a
primitive array of type TransferType.

void

setPixel

​(int x,
int y,
double[] dArray)

Sets a pixel in the DataBuffer using a double array of samples for input.

void

setPixel

​(int x,
int y,
float[] fArray)

Sets a pixel in the DataBuffer using a float array of samples for input.

void

setPixel

​(int x,
int y,
int[] iArray)

Sets a pixel in the DataBuffer using an int array of samples for input.

void

setPixels

​(int x,
int y,
int w,
int h,
double[] dArray)

Sets all samples for a rectangle of pixels from a double array containing
one sample per array element.

void

setPixels

​(int x,
int y,
int w,
int h,
float[] fArray)

Sets all samples for a rectangle of pixels from a float array containing
one sample per array element.

void

setPixels

​(int x,
int y,
int w,
int h,
int[] iArray)

Sets all samples for a rectangle of pixels from an int array containing
one sample per array element.

void

setRect

​(int dx,
int dy,

Raster

srcRaster)

Copies pixels from Raster srcRaster to this WritableRaster.

void

setRect

​(

Raster

srcRaster)

Copies pixels from Raster srcRaster to this WritableRaster.

void

setSample

​(int x,
int y,
int b,
double s)

Sets a sample in the specified band for the pixel located at (x,y)
in the DataBuffer using a double for input.

void

setSample

​(int x,
int y,
int b,
float s)

Sets a sample in the specified band for the pixel located at (x,y)
in the DataBuffer using a float for input.

void

setSample

​(int x,
int y,
int b,
int s)

Sets a sample in the specified band for the pixel located at (x,y)
in the DataBuffer using an int for input.

void

setSamples

​(int x,
int y,
int w,
int h,
int b,
double[] dArray)

Sets the samples in the specified band for the specified rectangle
of pixels from a double array containing one sample per array element.

void

setSamples

​(int x,
int y,
int w,
int h,
int b,
float[] fArray)

Sets the samples in the specified band for the specified rectangle
of pixels from a float array containing one sample per array element.

void

setSamples

​(int x,
int y,
int w,
int h,
int b,
int[] iArray)

Sets the samples in the specified band for the specified rectangle
of pixels from an int array containing one sample per array element.

- Methods declared in class java.awt.image.

Raster

createBandedRaster

,

createBandedRaster

,

createBandedRaster

,

createChild

,

createCompatibleWritableRaster

,

createCompatibleWritableRaster

,

createCompatibleWritableRaster

,

createCompatibleWritableRaster

,

createInterleavedRaster

,

createInterleavedRaster

,

createInterleavedRaster

,

createPackedRaster

,

createPackedRaster

,

createPackedRaster

,

createPackedRaster

,

createRaster

,

createTranslatedChild

,

createWritableRaster

,

createWritableRaster

,

getBounds

,

getDataBuffer

,

getDataElements

,

getDataElements

,

getHeight

,

getMinX

,

getMinY

,

getNumBands

,

getNumDataElements

,

getParent

,

getPixel

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

getSample

,

getSampleDouble

,

getSampleFloat

,

getSampleModel

,

getSampleModelTranslateX

,

getSampleModelTranslateY

,

getSamples

,

getSamples

,

getSamples

,

getTransferType

,

getWidth

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

Raster

dataBuffer

,

height

,

minX

,

minY

,

numBands

,

numDataElements

,

parent

,

sampleModel

,

sampleModelTranslateX

,

sampleModelTranslateY

,

width

---

#### Field Summary

Fields declared in class java.awt.image.

Raster

dataBuffer

,

height

,

minX

,

minY

,

numBands

,

numDataElements

,

parent

,

sampleModel

,

sampleModelTranslateX

,

sampleModelTranslateY

,

width

---

#### Fields declared in class java.awt.image. Raster

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

WritableRaster

​(

SampleModel

sampleModel,

DataBuffer

dataBuffer,

Point

origin)

Constructs a WritableRaster with the given SampleModel and DataBuffer.

protected

WritableRaster

​(

SampleModel

sampleModel,

DataBuffer

dataBuffer,

Rectangle

aRegion,

Point

sampleModelTranslate,

WritableRaster

parent)

Constructs a WritableRaster with the given SampleModel, DataBuffer,
and parent.

protected

WritableRaster

​(

SampleModel

sampleModel,

Point

origin)

Constructs a WritableRaster with the given SampleModel.

---

#### Constructor Summary

Constructs a WritableRaster with the given SampleModel and DataBuffer.

Constructs a WritableRaster with the given SampleModel, DataBuffer,
and parent.

Constructs a WritableRaster with the given SampleModel.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

WritableRaster

createWritableChild

​(int parentX,
int parentY,
int w,
int h,
int childMinX,
int childMinY,
int[] bandList)

Returns a new WritableRaster which shares all or part of this
WritableRaster's DataBuffer.

WritableRaster

createWritableTranslatedChild

​(int childMinX,
int childMinY)

Create a WritableRaster with the same size, SampleModel and DataBuffer
as this one, but with a different location.

WritableRaster

getWritableParent

()

Returns the parent WritableRaster (if any) of this WritableRaster,
or else null.

void

setDataElements

​(int x,
int y,
int w,
int h,

Object

inData)

Sets the data for a rectangle of pixels from a
primitive array of type TransferType.

void

setDataElements

​(int x,
int y,

Raster

inRaster)

Sets the data for a rectangle of pixels from an input Raster.

void

setDataElements

​(int x,
int y,

Object

inData)

Sets the data for a single pixel from a
primitive array of type TransferType.

void

setPixel

​(int x,
int y,
double[] dArray)

Sets a pixel in the DataBuffer using a double array of samples for input.

void

setPixel

​(int x,
int y,
float[] fArray)

Sets a pixel in the DataBuffer using a float array of samples for input.

void

setPixel

​(int x,
int y,
int[] iArray)

Sets a pixel in the DataBuffer using an int array of samples for input.

void

setPixels

​(int x,
int y,
int w,
int h,
double[] dArray)

Sets all samples for a rectangle of pixels from a double array containing
one sample per array element.

void

setPixels

​(int x,
int y,
int w,
int h,
float[] fArray)

Sets all samples for a rectangle of pixels from a float array containing
one sample per array element.

void

setPixels

​(int x,
int y,
int w,
int h,
int[] iArray)

Sets all samples for a rectangle of pixels from an int array containing
one sample per array element.

void

setRect

​(int dx,
int dy,

Raster

srcRaster)

Copies pixels from Raster srcRaster to this WritableRaster.

void

setRect

​(

Raster

srcRaster)

Copies pixels from Raster srcRaster to this WritableRaster.

void

setSample

​(int x,
int y,
int b,
double s)

Sets a sample in the specified band for the pixel located at (x,y)
in the DataBuffer using a double for input.

void

setSample

​(int x,
int y,
int b,
float s)

Sets a sample in the specified band for the pixel located at (x,y)
in the DataBuffer using a float for input.

void

setSample

​(int x,
int y,
int b,
int s)

Sets a sample in the specified band for the pixel located at (x,y)
in the DataBuffer using an int for input.

void

setSamples

​(int x,
int y,
int w,
int h,
int b,
double[] dArray)

Sets the samples in the specified band for the specified rectangle
of pixels from a double array containing one sample per array element.

void

setSamples

​(int x,
int y,
int w,
int h,
int b,
float[] fArray)

Sets the samples in the specified band for the specified rectangle
of pixels from a float array containing one sample per array element.

void

setSamples

​(int x,
int y,
int w,
int h,
int b,
int[] iArray)

Sets the samples in the specified band for the specified rectangle
of pixels from an int array containing one sample per array element.

- Methods declared in class java.awt.image.

Raster

createBandedRaster

,

createBandedRaster

,

createBandedRaster

,

createChild

,

createCompatibleWritableRaster

,

createCompatibleWritableRaster

,

createCompatibleWritableRaster

,

createCompatibleWritableRaster

,

createInterleavedRaster

,

createInterleavedRaster

,

createInterleavedRaster

,

createPackedRaster

,

createPackedRaster

,

createPackedRaster

,

createPackedRaster

,

createRaster

,

createTranslatedChild

,

createWritableRaster

,

createWritableRaster

,

getBounds

,

getDataBuffer

,

getDataElements

,

getDataElements

,

getHeight

,

getMinX

,

getMinY

,

getNumBands

,

getNumDataElements

,

getParent

,

getPixel

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

getSample

,

getSampleDouble

,

getSampleFloat

,

getSampleModel

,

getSampleModelTranslateX

,

getSampleModelTranslateY

,

getSamples

,

getSamples

,

getSamples

,

getTransferType

,

getWidth

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

Returns a new WritableRaster which shares all or part of this
WritableRaster's DataBuffer.

Create a WritableRaster with the same size, SampleModel and DataBuffer
as this one, but with a different location.

Returns the parent WritableRaster (if any) of this WritableRaster,
or else null.

Sets the data for a rectangle of pixels from a
primitive array of type TransferType.

Sets the data for a rectangle of pixels from an input Raster.

Sets the data for a single pixel from a
primitive array of type TransferType.

Sets a pixel in the DataBuffer using a double array of samples for input.

Sets a pixel in the DataBuffer using a float array of samples for input.

Sets a pixel in the DataBuffer using an int array of samples for input.

Sets all samples for a rectangle of pixels from a double array containing
one sample per array element.

Sets all samples for a rectangle of pixels from a float array containing
one sample per array element.

Sets all samples for a rectangle of pixels from an int array containing
one sample per array element.

Copies pixels from Raster srcRaster to this WritableRaster.

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

Methods declared in class java.awt.image.

Raster

createBandedRaster

,

createBandedRaster

,

createBandedRaster

,

createChild

,

createCompatibleWritableRaster

,

createCompatibleWritableRaster

,

createCompatibleWritableRaster

,

createCompatibleWritableRaster

,

createInterleavedRaster

,

createInterleavedRaster

,

createInterleavedRaster

,

createPackedRaster

,

createPackedRaster

,

createPackedRaster

,

createPackedRaster

,

createRaster

,

createTranslatedChild

,

createWritableRaster

,

createWritableRaster

,

getBounds

,

getDataBuffer

,

getDataElements

,

getDataElements

,

getHeight

,

getMinX

,

getMinY

,

getNumBands

,

getNumDataElements

,

getParent

,

getPixel

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

getSample

,

getSampleDouble

,

getSampleFloat

,

getSampleModel

,

getSampleModelTranslateX

,

getSampleModelTranslateY

,

getSamples

,

getSamples

,

getSamples

,

getTransferType

,

getWidth

---

#### Methods declared in class java.awt.image. Raster

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

- WritableRaster

```java
protected WritableRaster​(
SampleModel
sampleModel,

Point
origin)
```

Constructs a WritableRaster with the given SampleModel. The
WritableRaster's upper left corner is origin and it is the
same size as the SampleModel. A DataBuffer large enough to
describe the WritableRaster is automatically created.

**Parameters:** sampleModel

- The SampleModel that specifies the layout.
**Parameters:** origin

- The Point that specifies the origin.
**Throws:** RasterFormatException

- if computing either

origin.x + sampleModel.getWidth()

or

origin.y + sampleModel.getHeight()

results
in integer overflow

- WritableRaster

```java
protected WritableRaster​(
SampleModel
sampleModel,

DataBuffer
dataBuffer,

Point
origin)
```

Constructs a WritableRaster with the given SampleModel and DataBuffer.
The WritableRaster's upper left corner is origin and it is the same
size as the SampleModel. The DataBuffer is not initialized and must
be compatible with SampleModel.

**Parameters:** sampleModel

- The SampleModel that specifies the layout.
**Parameters:** dataBuffer

- The DataBuffer that contains the image data.
**Parameters:** origin

- The Point that specifies the origin.
**Throws:** RasterFormatException

- if computing either

origin.x + sampleModel.getWidth()

or

origin.y + sampleModel.getHeight()

results
in integer overflow

- WritableRaster

```java
protected WritableRaster​(
SampleModel
sampleModel,

DataBuffer
dataBuffer,

Rectangle
aRegion,

Point
sampleModelTranslate,

WritableRaster
parent)
```

Constructs a WritableRaster with the given SampleModel, DataBuffer,
and parent. aRegion specifies the bounding rectangle of the new
Raster. When translated into the base Raster's coordinate
system, aRegion must be contained by the base Raster.
(The base Raster is the Raster's ancestor which has no parent.)
sampleModelTranslate specifies the sampleModelTranslateX and
sampleModelTranslateY values of the new Raster.

Note that this constructor should generally be called by other
constructors or create methods, it should not be used directly.

**Parameters:** sampleModel

- The SampleModel that specifies the layout.
**Parameters:** dataBuffer

- The DataBuffer that contains the image data.
**Parameters:** aRegion

- The Rectangle that specifies the image area.
**Parameters:** sampleModelTranslate

- The Point that specifies the translation
from SampleModel to Raster coordinates.
**Parameters:** parent

- The parent (if any) of this raster.
**Throws:** RasterFormatException

- if

aRegion

has width
or height less than or equal to zero, or computing either

aRegion.x + aRegion.width

or

aRegion.y + aRegion.height

results in integer
overflow

============ METHOD DETAIL ==========

- Method Detail

- getWritableParent

```java
public
WritableRaster
getWritableParent()
```

Returns the parent WritableRaster (if any) of this WritableRaster,
or else null.

**Returns:** the parent of this

WritableRaster

, or

null

.

- createWritableTranslatedChild

```java
public
WritableRaster
createWritableTranslatedChild​(int childMinX,
int childMinY)
```

Create a WritableRaster with the same size, SampleModel and DataBuffer
as this one, but with a different location. The new WritableRaster
will possess a reference to the current WritableRaster, accessible
through its getParent() and getWritableParent() methods.

**Parameters:** childMinX

- X coord of the upper left corner of the new Raster.
**Parameters:** childMinY

- Y coord of the upper left corner of the new Raster.
**Returns:** a

WritableRaster

the same as this one except
for the specified location.
**Throws:** RasterFormatException

- if computing either

childMinX + this.getWidth()

or

childMinY + this.getHeight()

results in integer
overflow

- createWritableChild

```java
public
WritableRaster
createWritableChild​(int parentX,
int parentY,
int w,
int h,
int childMinX,
int childMinY,
int[] bandList)
```

Returns a new WritableRaster which shares all or part of this
WritableRaster's DataBuffer. The new WritableRaster will
possess a reference to the current WritableRaster, accessible
through its getParent() and getWritableParent() methods.

The parentX, parentY, width and height parameters form a
Rectangle in this WritableRaster's coordinate space, indicating
the area of pixels to be shared. An error will be thrown if
this Rectangle is not contained with the bounds of the current
WritableRaster.

The new WritableRaster may additionally be translated to a
different coordinate system for the plane than that used by the current
WritableRaster. The childMinX and childMinY parameters give
the new (x, y) coordinate of the upper-left pixel of the
returned WritableRaster; the coordinate (childMinX, childMinY)
in the new WritableRaster will map to the same pixel as the
coordinate (parentX, parentY) in the current WritableRaster.

The new WritableRaster may be defined to contain only a
subset of the bands of the current WritableRaster, possibly
reordered, by means of the bandList parameter. If bandList is
null, it is taken to include all of the bands of the current
WritableRaster in their current order.

To create a new WritableRaster that contains a subregion of
the current WritableRaster, but shares its coordinate system
and bands, this method should be called with childMinX equal to
parentX, childMinY equal to parentY, and bandList equal to
null.

**Parameters:** parentX

- X coordinate of the upper left corner in this
WritableRaster's coordinates.
**Parameters:** parentY

- Y coordinate of the upper left corner in this
WritableRaster's coordinates.
**Parameters:** w

- Width of the region starting at (parentX, parentY).
**Parameters:** h

- Height of the region starting at (parentX, parentY).
**Parameters:** childMinX

- X coordinate of the upper left corner of
the returned WritableRaster.
**Parameters:** childMinY

- Y coordinate of the upper left corner of
the returned WritableRaster.
**Parameters:** bandList

- Array of band indices, or null to use all bands.
**Returns:** a

WritableRaster

sharing all or part of the

DataBuffer

of this

WritableRaster

.
**Throws:** RasterFormatException

- if the subregion is outside of the
raster bounds.
**Throws:** RasterFormatException

- if

w

or

h

is less than or equal to zero, or computing any of

parentX + w

,

parentY + h

,

childMinX + w

, or

childMinY + h

results in integer
overflow

- setDataElements

```java
public void setDataElements​(int x,
int y,

Object
inData)
```

Sets the data for a single pixel from a
primitive array of type TransferType. For image data supported by
the Java 2D(tm) API, this will be one of DataBuffer.TYPE_BYTE,
DataBuffer.TYPE_USHORT, DataBuffer.TYPE_INT, DataBuffer.TYPE_SHORT,
DataBuffer.TYPE_FLOAT, or DataBuffer.TYPE_DOUBLE. Data in the array
may be in a packed format, thus increasing efficiency for data
transfers.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds, or if inData is not large enough to hold the pixel data.
However, explicit bounds checking is not guaranteed.
A ClassCastException will be thrown if the input object is not null
and references anything other than an array of TransferType.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** inData

- An object reference to an array of type defined by
getTransferType() and length getNumDataElements()
containing the pixel data to place at x,y.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are not
in bounds, or if inData is too small to hold the input.
**See Also:** SampleModel.setDataElements(int, int, Object, DataBuffer)

- setDataElements

```java
public void setDataElements​(int x,
int y,

Raster
inRaster)
```

Sets the data for a rectangle of pixels from an input Raster.
The input Raster must be compatible with this WritableRaster
in that they must have the same number of bands, corresponding bands
must have the same number of bits per sample, the TransferTypes
and NumDataElements must be the same, and the packing used by
the getDataElements/setDataElements must be identical.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** inRaster

- Raster containing data to place at x,y.
**Throws:** NullPointerException

- if inRaster is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are not
in bounds.

- setDataElements

```java
public void setDataElements​(int x,
int y,
int w,
int h,

Object
inData)
```

Sets the data for a rectangle of pixels from a
primitive array of type TransferType. For image data supported by
the Java 2D API, this will be one of DataBuffer.TYPE_BYTE,
DataBuffer.TYPE_USHORT, DataBuffer.TYPE_INT, DataBuffer.TYPE_SHORT,
DataBuffer.TYPE_FLOAT, or DataBuffer.TYPE_DOUBLE. Data in the array
may be in a packed format, thus increasing efficiency for data
transfers.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds, or if inData is not large enough to hold the pixel data.
However, explicit bounds checking is not guaranteed.
A ClassCastException will be thrown if the input object is not null
and references anything other than an array of TransferType.

**Parameters:** x

- The X coordinate of the upper left pixel location.
**Parameters:** y

- The Y coordinate of the upper left pixel location.
**Parameters:** w

- Width of the pixel rectangle.
**Parameters:** h

- Height of the pixel rectangle.
**Parameters:** inData

- An object reference to an array of type defined by
getTransferType() and length w*h*getNumDataElements()
containing the pixel data to place between x,y and
x+w-1, y+h-1.
**Throws:** NullPointerException

- if inData is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are not
in bounds, or if inData is too small to hold the input.
**See Also:** SampleModel.setDataElements(int, int, int, int, Object, DataBuffer)

- setRect

```java
public void setRect​(
Raster
srcRaster)
```

Copies pixels from Raster srcRaster to this WritableRaster. Each pixel
in srcRaster is copied to the same x,y address in this raster, unless
the address falls outside the bounds of this raster. srcRaster
must have the same number of bands as this WritableRaster. The
copy is a simple copy of source samples to the corresponding destination
samples.

If all samples of both source and destination Rasters are of
integral type and less than or equal to 32 bits in size, then calling
this method is equivalent to executing the following code for all

x,y

addresses valid in both Rasters.

```java
Raster srcRaster;
WritableRaster dstRaster;
for (int b = 0; b < srcRaster.getNumBands(); b++) {
dstRaster.setSample(x, y, b, srcRaster.getSample(x, y, b));
}
```

Thus, when copying an integral type source to an integral type
destination, if the source sample size is greater than the destination
sample size for a particular band, the high order bits of the source
sample are truncated. If the source sample size is less than the
destination size for a particular band, the high order bits of the
destination are zero-extended or sign-extended depending on whether
srcRaster's SampleModel treats the sample as a signed or unsigned
quantity.

When copying a float or double source to an integral type destination,
each source sample is cast to the destination type. When copying an
integral type source to a float or double destination, the source
is first converted to a 32-bit int (if necessary), using the above
rules for integral types, and then the int is cast to float or
double.

**Parameters:** srcRaster

- The Raster from which to copy pixels.
**Throws:** NullPointerException

- if srcRaster is null.

- setRect

```java
public void setRect​(int dx,
int dy,

Raster
srcRaster)
```

Copies pixels from Raster srcRaster to this WritableRaster.
For each (x, y) address in srcRaster, the corresponding pixel
is copied to address (x+dx, y+dy) in this WritableRaster,
unless (x+dx, y+dy) falls outside the bounds of this raster.
srcRaster must have the same number of bands as this WritableRaster.
The copy is a simple copy of source samples to the corresponding
destination samples. For details, see

setRect(Raster)

.

**Parameters:** dx

- The X translation factor from src space to dst space
of the copy.
**Parameters:** dy

- The Y translation factor from src space to dst space
of the copy.
**Parameters:** srcRaster

- The Raster from which to copy pixels.
**Throws:** NullPointerException

- if srcRaster is null.

- setPixel

```java
public void setPixel​(int x,
int y,
int[] iArray)
```

Sets a pixel in the DataBuffer using an int array of samples for input.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** iArray

- The input samples in a int array.
**Throws:** NullPointerException

- if iArray is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are not
in bounds, or if iArray is too small to hold the input.

- setPixel

```java
public void setPixel​(int x,
int y,
float[] fArray)
```

Sets a pixel in the DataBuffer using a float array of samples for input.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** fArray

- The input samples in a float array.
**Throws:** NullPointerException

- if fArray is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are not
in bounds, or if fArray is too small to hold the input.

- setPixel

```java
public void setPixel​(int x,
int y,
double[] dArray)
```

Sets a pixel in the DataBuffer using a double array of samples for input.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** dArray

- The input samples in a double array.
**Throws:** NullPointerException

- if dArray is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are not
in bounds, or if dArray is too small to hold the input.

- setPixels

```java
public void setPixels​(int x,
int y,
int w,
int h,
int[] iArray)
```

Sets all samples for a rectangle of pixels from an int array containing
one sample per array element.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

**Parameters:** x

- The X coordinate of the upper left pixel location.
**Parameters:** y

- The Y coordinate of the upper left pixel location.
**Parameters:** w

- Width of the pixel rectangle.
**Parameters:** h

- Height of the pixel rectangle.
**Parameters:** iArray

- The input int pixel array.
**Throws:** NullPointerException

- if iArray is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are not
in bounds, or if iArray is too small to hold the input.

- setPixels

```java
public void setPixels​(int x,
int y,
int w,
int h,
float[] fArray)
```

Sets all samples for a rectangle of pixels from a float array containing
one sample per array element.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

**Parameters:** x

- The X coordinate of the upper left pixel location.
**Parameters:** y

- The Y coordinate of the upper left pixel location.
**Parameters:** w

- Width of the pixel rectangle.
**Parameters:** h

- Height of the pixel rectangle.
**Parameters:** fArray

- The input float pixel array.
**Throws:** NullPointerException

- if fArray is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are not
in bounds, or if fArray is too small to hold the input.

- setPixels

```java
public void setPixels​(int x,
int y,
int w,
int h,
double[] dArray)
```

Sets all samples for a rectangle of pixels from a double array containing
one sample per array element.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

**Parameters:** x

- The X coordinate of the upper left pixel location.
**Parameters:** y

- The Y coordinate of the upper left pixel location.
**Parameters:** w

- Width of the pixel rectangle.
**Parameters:** h

- Height of the pixel rectangle.
**Parameters:** dArray

- The input double pixel array.
**Throws:** NullPointerException

- if dArray is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are not
in bounds, or if dArray is too small to hold the input.

- setSample

```java
public void setSample​(int x,
int y,
int b,
int s)
```

Sets a sample in the specified band for the pixel located at (x,y)
in the DataBuffer using an int for input.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** b

- The band to set.
**Parameters:** s

- The input sample.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds.

- setSample

```java
public void setSample​(int x,
int y,
int b,
float s)
```

Sets a sample in the specified band for the pixel located at (x,y)
in the DataBuffer using a float for input.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** b

- The band to set.
**Parameters:** s

- The input sample as a float.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds.

- setSample

```java
public void setSample​(int x,
int y,
int b,
double s)
```

Sets a sample in the specified band for the pixel located at (x,y)
in the DataBuffer using a double for input.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** b

- The band to set.
**Parameters:** s

- The input sample as a double.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds.

- setSamples

```java
public void setSamples​(int x,
int y,
int w,
int h,
int b,
int[] iArray)
```

Sets the samples in the specified band for the specified rectangle
of pixels from an int array containing one sample per array element.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

**Parameters:** x

- The X coordinate of the upper left pixel location.
**Parameters:** y

- The Y coordinate of the upper left pixel location.
**Parameters:** w

- Width of the pixel rectangle.
**Parameters:** h

- Height of the pixel rectangle.
**Parameters:** b

- The band to set.
**Parameters:** iArray

- The input int sample array.
**Throws:** NullPointerException

- if iArray is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds, or if iArray is too small to
hold the input.

- setSamples

```java
public void setSamples​(int x,
int y,
int w,
int h,
int b,
float[] fArray)
```

Sets the samples in the specified band for the specified rectangle
of pixels from a float array containing one sample per array element.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

**Parameters:** x

- The X coordinate of the upper left pixel location.
**Parameters:** y

- The Y coordinate of the upper left pixel location.
**Parameters:** w

- Width of the pixel rectangle.
**Parameters:** h

- Height of the pixel rectangle.
**Parameters:** b

- The band to set.
**Parameters:** fArray

- The input float sample array.
**Throws:** NullPointerException

- if fArray is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds, or if fArray is too small to
hold the input.

- setSamples

```java
public void setSamples​(int x,
int y,
int w,
int h,
int b,
double[] dArray)
```

Sets the samples in the specified band for the specified rectangle
of pixels from a double array containing one sample per array element.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

**Parameters:** x

- The X coordinate of the upper left pixel location.
**Parameters:** y

- The Y coordinate of the upper left pixel location.
**Parameters:** w

- Width of the pixel rectangle.
**Parameters:** h

- Height of the pixel rectangle.
**Parameters:** b

- The band to set.
**Parameters:** dArray

- The input double sample array.
**Throws:** NullPointerException

- if dArray is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds, or if dArray is too small to
hold the input.

Constructor Detail

- WritableRaster

```java
protected WritableRaster​(
SampleModel
sampleModel,

Point
origin)
```

Constructs a WritableRaster with the given SampleModel. The
WritableRaster's upper left corner is origin and it is the
same size as the SampleModel. A DataBuffer large enough to
describe the WritableRaster is automatically created.

**Parameters:** sampleModel

- The SampleModel that specifies the layout.
**Parameters:** origin

- The Point that specifies the origin.
**Throws:** RasterFormatException

- if computing either

origin.x + sampleModel.getWidth()

or

origin.y + sampleModel.getHeight()

results
in integer overflow

- WritableRaster

```java
protected WritableRaster​(
SampleModel
sampleModel,

DataBuffer
dataBuffer,

Point
origin)
```

Constructs a WritableRaster with the given SampleModel and DataBuffer.
The WritableRaster's upper left corner is origin and it is the same
size as the SampleModel. The DataBuffer is not initialized and must
be compatible with SampleModel.

**Parameters:** sampleModel

- The SampleModel that specifies the layout.
**Parameters:** dataBuffer

- The DataBuffer that contains the image data.
**Parameters:** origin

- The Point that specifies the origin.
**Throws:** RasterFormatException

- if computing either

origin.x + sampleModel.getWidth()

or

origin.y + sampleModel.getHeight()

results
in integer overflow

- WritableRaster

```java
protected WritableRaster​(
SampleModel
sampleModel,

DataBuffer
dataBuffer,

Rectangle
aRegion,

Point
sampleModelTranslate,

WritableRaster
parent)
```

Constructs a WritableRaster with the given SampleModel, DataBuffer,
and parent. aRegion specifies the bounding rectangle of the new
Raster. When translated into the base Raster's coordinate
system, aRegion must be contained by the base Raster.
(The base Raster is the Raster's ancestor which has no parent.)
sampleModelTranslate specifies the sampleModelTranslateX and
sampleModelTranslateY values of the new Raster.

Note that this constructor should generally be called by other
constructors or create methods, it should not be used directly.

**Parameters:** sampleModel

- The SampleModel that specifies the layout.
**Parameters:** dataBuffer

- The DataBuffer that contains the image data.
**Parameters:** aRegion

- The Rectangle that specifies the image area.
**Parameters:** sampleModelTranslate

- The Point that specifies the translation
from SampleModel to Raster coordinates.
**Parameters:** parent

- The parent (if any) of this raster.
**Throws:** RasterFormatException

- if

aRegion

has width
or height less than or equal to zero, or computing either

aRegion.x + aRegion.width

or

aRegion.y + aRegion.height

results in integer
overflow

---

#### Constructor Detail

WritableRaster

```java
protected WritableRaster​(
SampleModel
sampleModel,

Point
origin)
```

Constructs a WritableRaster with the given SampleModel. The
WritableRaster's upper left corner is origin and it is the
same size as the SampleModel. A DataBuffer large enough to
describe the WritableRaster is automatically created.

**Parameters:** sampleModel

- The SampleModel that specifies the layout.
**Parameters:** origin

- The Point that specifies the origin.
**Throws:** RasterFormatException

- if computing either

origin.x + sampleModel.getWidth()

or

origin.y + sampleModel.getHeight()

results
in integer overflow

---

#### WritableRaster

protected WritableRaster​(

SampleModel

sampleModel,

Point

origin)

Constructs a WritableRaster with the given SampleModel. The
WritableRaster's upper left corner is origin and it is the
same size as the SampleModel. A DataBuffer large enough to
describe the WritableRaster is automatically created.

WritableRaster

```java
protected WritableRaster​(
SampleModel
sampleModel,

DataBuffer
dataBuffer,

Point
origin)
```

Constructs a WritableRaster with the given SampleModel and DataBuffer.
The WritableRaster's upper left corner is origin and it is the same
size as the SampleModel. The DataBuffer is not initialized and must
be compatible with SampleModel.

**Parameters:** sampleModel

- The SampleModel that specifies the layout.
**Parameters:** dataBuffer

- The DataBuffer that contains the image data.
**Parameters:** origin

- The Point that specifies the origin.
**Throws:** RasterFormatException

- if computing either

origin.x + sampleModel.getWidth()

or

origin.y + sampleModel.getHeight()

results
in integer overflow

---

#### WritableRaster

protected WritableRaster​(

SampleModel

sampleModel,

DataBuffer

dataBuffer,

Point

origin)

Constructs a WritableRaster with the given SampleModel and DataBuffer.
The WritableRaster's upper left corner is origin and it is the same
size as the SampleModel. The DataBuffer is not initialized and must
be compatible with SampleModel.

WritableRaster

```java
protected WritableRaster​(
SampleModel
sampleModel,

DataBuffer
dataBuffer,

Rectangle
aRegion,

Point
sampleModelTranslate,

WritableRaster
parent)
```

Constructs a WritableRaster with the given SampleModel, DataBuffer,
and parent. aRegion specifies the bounding rectangle of the new
Raster. When translated into the base Raster's coordinate
system, aRegion must be contained by the base Raster.
(The base Raster is the Raster's ancestor which has no parent.)
sampleModelTranslate specifies the sampleModelTranslateX and
sampleModelTranslateY values of the new Raster.

Note that this constructor should generally be called by other
constructors or create methods, it should not be used directly.

**Parameters:** sampleModel

- The SampleModel that specifies the layout.
**Parameters:** dataBuffer

- The DataBuffer that contains the image data.
**Parameters:** aRegion

- The Rectangle that specifies the image area.
**Parameters:** sampleModelTranslate

- The Point that specifies the translation
from SampleModel to Raster coordinates.
**Parameters:** parent

- The parent (if any) of this raster.
**Throws:** RasterFormatException

- if

aRegion

has width
or height less than or equal to zero, or computing either

aRegion.x + aRegion.width

or

aRegion.y + aRegion.height

results in integer
overflow

---

#### WritableRaster

protected WritableRaster​(

SampleModel

sampleModel,

DataBuffer

dataBuffer,

Rectangle

aRegion,

Point

sampleModelTranslate,

WritableRaster

parent)

Constructs a WritableRaster with the given SampleModel, DataBuffer,
and parent. aRegion specifies the bounding rectangle of the new
Raster. When translated into the base Raster's coordinate
system, aRegion must be contained by the base Raster.
(The base Raster is the Raster's ancestor which has no parent.)
sampleModelTranslate specifies the sampleModelTranslateX and
sampleModelTranslateY values of the new Raster.

Note that this constructor should generally be called by other
constructors or create methods, it should not be used directly.

Method Detail

- getWritableParent

```java
public
WritableRaster
getWritableParent()
```

Returns the parent WritableRaster (if any) of this WritableRaster,
or else null.

**Returns:** the parent of this

WritableRaster

, or

null

.

- createWritableTranslatedChild

```java
public
WritableRaster
createWritableTranslatedChild​(int childMinX,
int childMinY)
```

Create a WritableRaster with the same size, SampleModel and DataBuffer
as this one, but with a different location. The new WritableRaster
will possess a reference to the current WritableRaster, accessible
through its getParent() and getWritableParent() methods.

**Parameters:** childMinX

- X coord of the upper left corner of the new Raster.
**Parameters:** childMinY

- Y coord of the upper left corner of the new Raster.
**Returns:** a

WritableRaster

the same as this one except
for the specified location.
**Throws:** RasterFormatException

- if computing either

childMinX + this.getWidth()

or

childMinY + this.getHeight()

results in integer
overflow

- createWritableChild

```java
public
WritableRaster
createWritableChild​(int parentX,
int parentY,
int w,
int h,
int childMinX,
int childMinY,
int[] bandList)
```

Returns a new WritableRaster which shares all or part of this
WritableRaster's DataBuffer. The new WritableRaster will
possess a reference to the current WritableRaster, accessible
through its getParent() and getWritableParent() methods.

The parentX, parentY, width and height parameters form a
Rectangle in this WritableRaster's coordinate space, indicating
the area of pixels to be shared. An error will be thrown if
this Rectangle is not contained with the bounds of the current
WritableRaster.

The new WritableRaster may additionally be translated to a
different coordinate system for the plane than that used by the current
WritableRaster. The childMinX and childMinY parameters give
the new (x, y) coordinate of the upper-left pixel of the
returned WritableRaster; the coordinate (childMinX, childMinY)
in the new WritableRaster will map to the same pixel as the
coordinate (parentX, parentY) in the current WritableRaster.

The new WritableRaster may be defined to contain only a
subset of the bands of the current WritableRaster, possibly
reordered, by means of the bandList parameter. If bandList is
null, it is taken to include all of the bands of the current
WritableRaster in their current order.

To create a new WritableRaster that contains a subregion of
the current WritableRaster, but shares its coordinate system
and bands, this method should be called with childMinX equal to
parentX, childMinY equal to parentY, and bandList equal to
null.

**Parameters:** parentX

- X coordinate of the upper left corner in this
WritableRaster's coordinates.
**Parameters:** parentY

- Y coordinate of the upper left corner in this
WritableRaster's coordinates.
**Parameters:** w

- Width of the region starting at (parentX, parentY).
**Parameters:** h

- Height of the region starting at (parentX, parentY).
**Parameters:** childMinX

- X coordinate of the upper left corner of
the returned WritableRaster.
**Parameters:** childMinY

- Y coordinate of the upper left corner of
the returned WritableRaster.
**Parameters:** bandList

- Array of band indices, or null to use all bands.
**Returns:** a

WritableRaster

sharing all or part of the

DataBuffer

of this

WritableRaster

.
**Throws:** RasterFormatException

- if the subregion is outside of the
raster bounds.
**Throws:** RasterFormatException

- if

w

or

h

is less than or equal to zero, or computing any of

parentX + w

,

parentY + h

,

childMinX + w

, or

childMinY + h

results in integer
overflow

- setDataElements

```java
public void setDataElements​(int x,
int y,

Object
inData)
```

Sets the data for a single pixel from a
primitive array of type TransferType. For image data supported by
the Java 2D(tm) API, this will be one of DataBuffer.TYPE_BYTE,
DataBuffer.TYPE_USHORT, DataBuffer.TYPE_INT, DataBuffer.TYPE_SHORT,
DataBuffer.TYPE_FLOAT, or DataBuffer.TYPE_DOUBLE. Data in the array
may be in a packed format, thus increasing efficiency for data
transfers.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds, or if inData is not large enough to hold the pixel data.
However, explicit bounds checking is not guaranteed.
A ClassCastException will be thrown if the input object is not null
and references anything other than an array of TransferType.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** inData

- An object reference to an array of type defined by
getTransferType() and length getNumDataElements()
containing the pixel data to place at x,y.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are not
in bounds, or if inData is too small to hold the input.
**See Also:** SampleModel.setDataElements(int, int, Object, DataBuffer)

- setDataElements

```java
public void setDataElements​(int x,
int y,

Raster
inRaster)
```

Sets the data for a rectangle of pixels from an input Raster.
The input Raster must be compatible with this WritableRaster
in that they must have the same number of bands, corresponding bands
must have the same number of bits per sample, the TransferTypes
and NumDataElements must be the same, and the packing used by
the getDataElements/setDataElements must be identical.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** inRaster

- Raster containing data to place at x,y.
**Throws:** NullPointerException

- if inRaster is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are not
in bounds.

- setDataElements

```java
public void setDataElements​(int x,
int y,
int w,
int h,

Object
inData)
```

Sets the data for a rectangle of pixels from a
primitive array of type TransferType. For image data supported by
the Java 2D API, this will be one of DataBuffer.TYPE_BYTE,
DataBuffer.TYPE_USHORT, DataBuffer.TYPE_INT, DataBuffer.TYPE_SHORT,
DataBuffer.TYPE_FLOAT, or DataBuffer.TYPE_DOUBLE. Data in the array
may be in a packed format, thus increasing efficiency for data
transfers.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds, or if inData is not large enough to hold the pixel data.
However, explicit bounds checking is not guaranteed.
A ClassCastException will be thrown if the input object is not null
and references anything other than an array of TransferType.

**Parameters:** x

- The X coordinate of the upper left pixel location.
**Parameters:** y

- The Y coordinate of the upper left pixel location.
**Parameters:** w

- Width of the pixel rectangle.
**Parameters:** h

- Height of the pixel rectangle.
**Parameters:** inData

- An object reference to an array of type defined by
getTransferType() and length w*h*getNumDataElements()
containing the pixel data to place between x,y and
x+w-1, y+h-1.
**Throws:** NullPointerException

- if inData is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are not
in bounds, or if inData is too small to hold the input.
**See Also:** SampleModel.setDataElements(int, int, int, int, Object, DataBuffer)

- setRect

```java
public void setRect​(
Raster
srcRaster)
```

Copies pixels from Raster srcRaster to this WritableRaster. Each pixel
in srcRaster is copied to the same x,y address in this raster, unless
the address falls outside the bounds of this raster. srcRaster
must have the same number of bands as this WritableRaster. The
copy is a simple copy of source samples to the corresponding destination
samples.

If all samples of both source and destination Rasters are of
integral type and less than or equal to 32 bits in size, then calling
this method is equivalent to executing the following code for all

x,y

addresses valid in both Rasters.

```java
Raster srcRaster;
WritableRaster dstRaster;
for (int b = 0; b < srcRaster.getNumBands(); b++) {
dstRaster.setSample(x, y, b, srcRaster.getSample(x, y, b));
}
```

Thus, when copying an integral type source to an integral type
destination, if the source sample size is greater than the destination
sample size for a particular band, the high order bits of the source
sample are truncated. If the source sample size is less than the
destination size for a particular band, the high order bits of the
destination are zero-extended or sign-extended depending on whether
srcRaster's SampleModel treats the sample as a signed or unsigned
quantity.

When copying a float or double source to an integral type destination,
each source sample is cast to the destination type. When copying an
integral type source to a float or double destination, the source
is first converted to a 32-bit int (if necessary), using the above
rules for integral types, and then the int is cast to float or
double.

**Parameters:** srcRaster

- The Raster from which to copy pixels.
**Throws:** NullPointerException

- if srcRaster is null.

- setRect

```java
public void setRect​(int dx,
int dy,

Raster
srcRaster)
```

Copies pixels from Raster srcRaster to this WritableRaster.
For each (x, y) address in srcRaster, the corresponding pixel
is copied to address (x+dx, y+dy) in this WritableRaster,
unless (x+dx, y+dy) falls outside the bounds of this raster.
srcRaster must have the same number of bands as this WritableRaster.
The copy is a simple copy of source samples to the corresponding
destination samples. For details, see

setRect(Raster)

.

**Parameters:** dx

- The X translation factor from src space to dst space
of the copy.
**Parameters:** dy

- The Y translation factor from src space to dst space
of the copy.
**Parameters:** srcRaster

- The Raster from which to copy pixels.
**Throws:** NullPointerException

- if srcRaster is null.

- setPixel

```java
public void setPixel​(int x,
int y,
int[] iArray)
```

Sets a pixel in the DataBuffer using an int array of samples for input.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** iArray

- The input samples in a int array.
**Throws:** NullPointerException

- if iArray is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are not
in bounds, or if iArray is too small to hold the input.

- setPixel

```java
public void setPixel​(int x,
int y,
float[] fArray)
```

Sets a pixel in the DataBuffer using a float array of samples for input.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** fArray

- The input samples in a float array.
**Throws:** NullPointerException

- if fArray is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are not
in bounds, or if fArray is too small to hold the input.

- setPixel

```java
public void setPixel​(int x,
int y,
double[] dArray)
```

Sets a pixel in the DataBuffer using a double array of samples for input.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** dArray

- The input samples in a double array.
**Throws:** NullPointerException

- if dArray is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are not
in bounds, or if dArray is too small to hold the input.

- setPixels

```java
public void setPixels​(int x,
int y,
int w,
int h,
int[] iArray)
```

Sets all samples for a rectangle of pixels from an int array containing
one sample per array element.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

**Parameters:** x

- The X coordinate of the upper left pixel location.
**Parameters:** y

- The Y coordinate of the upper left pixel location.
**Parameters:** w

- Width of the pixel rectangle.
**Parameters:** h

- Height of the pixel rectangle.
**Parameters:** iArray

- The input int pixel array.
**Throws:** NullPointerException

- if iArray is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are not
in bounds, or if iArray is too small to hold the input.

- setPixels

```java
public void setPixels​(int x,
int y,
int w,
int h,
float[] fArray)
```

Sets all samples for a rectangle of pixels from a float array containing
one sample per array element.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

**Parameters:** x

- The X coordinate of the upper left pixel location.
**Parameters:** y

- The Y coordinate of the upper left pixel location.
**Parameters:** w

- Width of the pixel rectangle.
**Parameters:** h

- Height of the pixel rectangle.
**Parameters:** fArray

- The input float pixel array.
**Throws:** NullPointerException

- if fArray is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are not
in bounds, or if fArray is too small to hold the input.

- setPixels

```java
public void setPixels​(int x,
int y,
int w,
int h,
double[] dArray)
```

Sets all samples for a rectangle of pixels from a double array containing
one sample per array element.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

**Parameters:** x

- The X coordinate of the upper left pixel location.
**Parameters:** y

- The Y coordinate of the upper left pixel location.
**Parameters:** w

- Width of the pixel rectangle.
**Parameters:** h

- Height of the pixel rectangle.
**Parameters:** dArray

- The input double pixel array.
**Throws:** NullPointerException

- if dArray is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are not
in bounds, or if dArray is too small to hold the input.

- setSample

```java
public void setSample​(int x,
int y,
int b,
int s)
```

Sets a sample in the specified band for the pixel located at (x,y)
in the DataBuffer using an int for input.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** b

- The band to set.
**Parameters:** s

- The input sample.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds.

- setSample

```java
public void setSample​(int x,
int y,
int b,
float s)
```

Sets a sample in the specified band for the pixel located at (x,y)
in the DataBuffer using a float for input.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** b

- The band to set.
**Parameters:** s

- The input sample as a float.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds.

- setSample

```java
public void setSample​(int x,
int y,
int b,
double s)
```

Sets a sample in the specified band for the pixel located at (x,y)
in the DataBuffer using a double for input.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** b

- The band to set.
**Parameters:** s

- The input sample as a double.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds.

- setSamples

```java
public void setSamples​(int x,
int y,
int w,
int h,
int b,
int[] iArray)
```

Sets the samples in the specified band for the specified rectangle
of pixels from an int array containing one sample per array element.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

**Parameters:** x

- The X coordinate of the upper left pixel location.
**Parameters:** y

- The Y coordinate of the upper left pixel location.
**Parameters:** w

- Width of the pixel rectangle.
**Parameters:** h

- Height of the pixel rectangle.
**Parameters:** b

- The band to set.
**Parameters:** iArray

- The input int sample array.
**Throws:** NullPointerException

- if iArray is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds, or if iArray is too small to
hold the input.

- setSamples

```java
public void setSamples​(int x,
int y,
int w,
int h,
int b,
float[] fArray)
```

Sets the samples in the specified band for the specified rectangle
of pixels from a float array containing one sample per array element.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

**Parameters:** x

- The X coordinate of the upper left pixel location.
**Parameters:** y

- The Y coordinate of the upper left pixel location.
**Parameters:** w

- Width of the pixel rectangle.
**Parameters:** h

- Height of the pixel rectangle.
**Parameters:** b

- The band to set.
**Parameters:** fArray

- The input float sample array.
**Throws:** NullPointerException

- if fArray is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds, or if fArray is too small to
hold the input.

- setSamples

```java
public void setSamples​(int x,
int y,
int w,
int h,
int b,
double[] dArray)
```

Sets the samples in the specified band for the specified rectangle
of pixels from a double array containing one sample per array element.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

**Parameters:** x

- The X coordinate of the upper left pixel location.
**Parameters:** y

- The Y coordinate of the upper left pixel location.
**Parameters:** w

- Width of the pixel rectangle.
**Parameters:** h

- Height of the pixel rectangle.
**Parameters:** b

- The band to set.
**Parameters:** dArray

- The input double sample array.
**Throws:** NullPointerException

- if dArray is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds, or if dArray is too small to
hold the input.

---

#### Method Detail

getWritableParent

```java
public
WritableRaster
getWritableParent()
```

Returns the parent WritableRaster (if any) of this WritableRaster,
or else null.

**Returns:** the parent of this

WritableRaster

, or

null

.

---

#### getWritableParent

public

WritableRaster

getWritableParent()

Returns the parent WritableRaster (if any) of this WritableRaster,
or else null.

createWritableTranslatedChild

```java
public
WritableRaster
createWritableTranslatedChild​(int childMinX,
int childMinY)
```

Create a WritableRaster with the same size, SampleModel and DataBuffer
as this one, but with a different location. The new WritableRaster
will possess a reference to the current WritableRaster, accessible
through its getParent() and getWritableParent() methods.

**Parameters:** childMinX

- X coord of the upper left corner of the new Raster.
**Parameters:** childMinY

- Y coord of the upper left corner of the new Raster.
**Returns:** a

WritableRaster

the same as this one except
for the specified location.
**Throws:** RasterFormatException

- if computing either

childMinX + this.getWidth()

or

childMinY + this.getHeight()

results in integer
overflow

---

#### createWritableTranslatedChild

public

WritableRaster

createWritableTranslatedChild​(int childMinX,
int childMinY)

Create a WritableRaster with the same size, SampleModel and DataBuffer
as this one, but with a different location. The new WritableRaster
will possess a reference to the current WritableRaster, accessible
through its getParent() and getWritableParent() methods.

createWritableChild

```java
public
WritableRaster
createWritableChild​(int parentX,
int parentY,
int w,
int h,
int childMinX,
int childMinY,
int[] bandList)
```

Returns a new WritableRaster which shares all or part of this
WritableRaster's DataBuffer. The new WritableRaster will
possess a reference to the current WritableRaster, accessible
through its getParent() and getWritableParent() methods.

The parentX, parentY, width and height parameters form a
Rectangle in this WritableRaster's coordinate space, indicating
the area of pixels to be shared. An error will be thrown if
this Rectangle is not contained with the bounds of the current
WritableRaster.

The new WritableRaster may additionally be translated to a
different coordinate system for the plane than that used by the current
WritableRaster. The childMinX and childMinY parameters give
the new (x, y) coordinate of the upper-left pixel of the
returned WritableRaster; the coordinate (childMinX, childMinY)
in the new WritableRaster will map to the same pixel as the
coordinate (parentX, parentY) in the current WritableRaster.

The new WritableRaster may be defined to contain only a
subset of the bands of the current WritableRaster, possibly
reordered, by means of the bandList parameter. If bandList is
null, it is taken to include all of the bands of the current
WritableRaster in their current order.

To create a new WritableRaster that contains a subregion of
the current WritableRaster, but shares its coordinate system
and bands, this method should be called with childMinX equal to
parentX, childMinY equal to parentY, and bandList equal to
null.

**Parameters:** parentX

- X coordinate of the upper left corner in this
WritableRaster's coordinates.
**Parameters:** parentY

- Y coordinate of the upper left corner in this
WritableRaster's coordinates.
**Parameters:** w

- Width of the region starting at (parentX, parentY).
**Parameters:** h

- Height of the region starting at (parentX, parentY).
**Parameters:** childMinX

- X coordinate of the upper left corner of
the returned WritableRaster.
**Parameters:** childMinY

- Y coordinate of the upper left corner of
the returned WritableRaster.
**Parameters:** bandList

- Array of band indices, or null to use all bands.
**Returns:** a

WritableRaster

sharing all or part of the

DataBuffer

of this

WritableRaster

.
**Throws:** RasterFormatException

- if the subregion is outside of the
raster bounds.
**Throws:** RasterFormatException

- if

w

or

h

is less than or equal to zero, or computing any of

parentX + w

,

parentY + h

,

childMinX + w

, or

childMinY + h

results in integer
overflow

---

#### createWritableChild

public

WritableRaster

createWritableChild​(int parentX,
int parentY,
int w,
int h,
int childMinX,
int childMinY,
int[] bandList)

Returns a new WritableRaster which shares all or part of this
WritableRaster's DataBuffer. The new WritableRaster will
possess a reference to the current WritableRaster, accessible
through its getParent() and getWritableParent() methods.

The parentX, parentY, width and height parameters form a
Rectangle in this WritableRaster's coordinate space, indicating
the area of pixels to be shared. An error will be thrown if
this Rectangle is not contained with the bounds of the current
WritableRaster.

The new WritableRaster may additionally be translated to a
different coordinate system for the plane than that used by the current
WritableRaster. The childMinX and childMinY parameters give
the new (x, y) coordinate of the upper-left pixel of the
returned WritableRaster; the coordinate (childMinX, childMinY)
in the new WritableRaster will map to the same pixel as the
coordinate (parentX, parentY) in the current WritableRaster.

The new WritableRaster may be defined to contain only a
subset of the bands of the current WritableRaster, possibly
reordered, by means of the bandList parameter. If bandList is
null, it is taken to include all of the bands of the current
WritableRaster in their current order.

To create a new WritableRaster that contains a subregion of
the current WritableRaster, but shares its coordinate system
and bands, this method should be called with childMinX equal to
parentX, childMinY equal to parentY, and bandList equal to
null.

The parentX, parentY, width and height parameters form a
Rectangle in this WritableRaster's coordinate space, indicating
the area of pixels to be shared. An error will be thrown if
this Rectangle is not contained with the bounds of the current
WritableRaster.

The new WritableRaster may additionally be translated to a
different coordinate system for the plane than that used by the current
WritableRaster. The childMinX and childMinY parameters give
the new (x, y) coordinate of the upper-left pixel of the
returned WritableRaster; the coordinate (childMinX, childMinY)
in the new WritableRaster will map to the same pixel as the
coordinate (parentX, parentY) in the current WritableRaster.

The new WritableRaster may be defined to contain only a
subset of the bands of the current WritableRaster, possibly
reordered, by means of the bandList parameter. If bandList is
null, it is taken to include all of the bands of the current
WritableRaster in their current order.

To create a new WritableRaster that contains a subregion of
the current WritableRaster, but shares its coordinate system
and bands, this method should be called with childMinX equal to
parentX, childMinY equal to parentY, and bandList equal to
null.

The new WritableRaster may additionally be translated to a
different coordinate system for the plane than that used by the current
WritableRaster. The childMinX and childMinY parameters give
the new (x, y) coordinate of the upper-left pixel of the
returned WritableRaster; the coordinate (childMinX, childMinY)
in the new WritableRaster will map to the same pixel as the
coordinate (parentX, parentY) in the current WritableRaster.

The new WritableRaster may be defined to contain only a
subset of the bands of the current WritableRaster, possibly
reordered, by means of the bandList parameter. If bandList is
null, it is taken to include all of the bands of the current
WritableRaster in their current order.

To create a new WritableRaster that contains a subregion of
the current WritableRaster, but shares its coordinate system
and bands, this method should be called with childMinX equal to
parentX, childMinY equal to parentY, and bandList equal to
null.

The new WritableRaster may be defined to contain only a
subset of the bands of the current WritableRaster, possibly
reordered, by means of the bandList parameter. If bandList is
null, it is taken to include all of the bands of the current
WritableRaster in their current order.

To create a new WritableRaster that contains a subregion of
the current WritableRaster, but shares its coordinate system
and bands, this method should be called with childMinX equal to
parentX, childMinY equal to parentY, and bandList equal to
null.

To create a new WritableRaster that contains a subregion of
the current WritableRaster, but shares its coordinate system
and bands, this method should be called with childMinX equal to
parentX, childMinY equal to parentY, and bandList equal to
null.

setDataElements

```java
public void setDataElements​(int x,
int y,

Object
inData)
```

Sets the data for a single pixel from a
primitive array of type TransferType. For image data supported by
the Java 2D(tm) API, this will be one of DataBuffer.TYPE_BYTE,
DataBuffer.TYPE_USHORT, DataBuffer.TYPE_INT, DataBuffer.TYPE_SHORT,
DataBuffer.TYPE_FLOAT, or DataBuffer.TYPE_DOUBLE. Data in the array
may be in a packed format, thus increasing efficiency for data
transfers.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds, or if inData is not large enough to hold the pixel data.
However, explicit bounds checking is not guaranteed.
A ClassCastException will be thrown if the input object is not null
and references anything other than an array of TransferType.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** inData

- An object reference to an array of type defined by
getTransferType() and length getNumDataElements()
containing the pixel data to place at x,y.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are not
in bounds, or if inData is too small to hold the input.
**See Also:** SampleModel.setDataElements(int, int, Object, DataBuffer)

---

#### setDataElements

public void setDataElements​(int x,
int y,

Object

inData)

Sets the data for a single pixel from a
primitive array of type TransferType. For image data supported by
the Java 2D(tm) API, this will be one of DataBuffer.TYPE_BYTE,
DataBuffer.TYPE_USHORT, DataBuffer.TYPE_INT, DataBuffer.TYPE_SHORT,
DataBuffer.TYPE_FLOAT, or DataBuffer.TYPE_DOUBLE. Data in the array
may be in a packed format, thus increasing efficiency for data
transfers.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds, or if inData is not large enough to hold the pixel data.
However, explicit bounds checking is not guaranteed.
A ClassCastException will be thrown if the input object is not null
and references anything other than an array of TransferType.

setDataElements

```java
public void setDataElements​(int x,
int y,

Raster
inRaster)
```

Sets the data for a rectangle of pixels from an input Raster.
The input Raster must be compatible with this WritableRaster
in that they must have the same number of bands, corresponding bands
must have the same number of bits per sample, the TransferTypes
and NumDataElements must be the same, and the packing used by
the getDataElements/setDataElements must be identical.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** inRaster

- Raster containing data to place at x,y.
**Throws:** NullPointerException

- if inRaster is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are not
in bounds.

---

#### setDataElements

public void setDataElements​(int x,
int y,

Raster

inRaster)

Sets the data for a rectangle of pixels from an input Raster.
The input Raster must be compatible with this WritableRaster
in that they must have the same number of bands, corresponding bands
must have the same number of bits per sample, the TransferTypes
and NumDataElements must be the same, and the packing used by
the getDataElements/setDataElements must be identical.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

setDataElements

```java
public void setDataElements​(int x,
int y,
int w,
int h,

Object
inData)
```

Sets the data for a rectangle of pixels from a
primitive array of type TransferType. For image data supported by
the Java 2D API, this will be one of DataBuffer.TYPE_BYTE,
DataBuffer.TYPE_USHORT, DataBuffer.TYPE_INT, DataBuffer.TYPE_SHORT,
DataBuffer.TYPE_FLOAT, or DataBuffer.TYPE_DOUBLE. Data in the array
may be in a packed format, thus increasing efficiency for data
transfers.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds, or if inData is not large enough to hold the pixel data.
However, explicit bounds checking is not guaranteed.
A ClassCastException will be thrown if the input object is not null
and references anything other than an array of TransferType.

**Parameters:** x

- The X coordinate of the upper left pixel location.
**Parameters:** y

- The Y coordinate of the upper left pixel location.
**Parameters:** w

- Width of the pixel rectangle.
**Parameters:** h

- Height of the pixel rectangle.
**Parameters:** inData

- An object reference to an array of type defined by
getTransferType() and length w*h*getNumDataElements()
containing the pixel data to place between x,y and
x+w-1, y+h-1.
**Throws:** NullPointerException

- if inData is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are not
in bounds, or if inData is too small to hold the input.
**See Also:** SampleModel.setDataElements(int, int, int, int, Object, DataBuffer)

---

#### setDataElements

public void setDataElements​(int x,
int y,
int w,
int h,

Object

inData)

Sets the data for a rectangle of pixels from a
primitive array of type TransferType. For image data supported by
the Java 2D API, this will be one of DataBuffer.TYPE_BYTE,
DataBuffer.TYPE_USHORT, DataBuffer.TYPE_INT, DataBuffer.TYPE_SHORT,
DataBuffer.TYPE_FLOAT, or DataBuffer.TYPE_DOUBLE. Data in the array
may be in a packed format, thus increasing efficiency for data
transfers.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds, or if inData is not large enough to hold the pixel data.
However, explicit bounds checking is not guaranteed.
A ClassCastException will be thrown if the input object is not null
and references anything other than an array of TransferType.

setRect

```java
public void setRect​(
Raster
srcRaster)
```

Copies pixels from Raster srcRaster to this WritableRaster. Each pixel
in srcRaster is copied to the same x,y address in this raster, unless
the address falls outside the bounds of this raster. srcRaster
must have the same number of bands as this WritableRaster. The
copy is a simple copy of source samples to the corresponding destination
samples.

If all samples of both source and destination Rasters are of
integral type and less than or equal to 32 bits in size, then calling
this method is equivalent to executing the following code for all

x,y

addresses valid in both Rasters.

```java
Raster srcRaster;
WritableRaster dstRaster;
for (int b = 0; b < srcRaster.getNumBands(); b++) {
dstRaster.setSample(x, y, b, srcRaster.getSample(x, y, b));
}
```

Thus, when copying an integral type source to an integral type
destination, if the source sample size is greater than the destination
sample size for a particular band, the high order bits of the source
sample are truncated. If the source sample size is less than the
destination size for a particular band, the high order bits of the
destination are zero-extended or sign-extended depending on whether
srcRaster's SampleModel treats the sample as a signed or unsigned
quantity.

When copying a float or double source to an integral type destination,
each source sample is cast to the destination type. When copying an
integral type source to a float or double destination, the source
is first converted to a 32-bit int (if necessary), using the above
rules for integral types, and then the int is cast to float or
double.

**Parameters:** srcRaster

- The Raster from which to copy pixels.
**Throws:** NullPointerException

- if srcRaster is null.

---

#### setRect

public void setRect​(

Raster

srcRaster)

Copies pixels from Raster srcRaster to this WritableRaster. Each pixel
in srcRaster is copied to the same x,y address in this raster, unless
the address falls outside the bounds of this raster. srcRaster
must have the same number of bands as this WritableRaster. The
copy is a simple copy of source samples to the corresponding destination
samples.

If all samples of both source and destination Rasters are of
integral type and less than or equal to 32 bits in size, then calling
this method is equivalent to executing the following code for all

x,y

addresses valid in both Rasters.

```java
Raster srcRaster;
WritableRaster dstRaster;
for (int b = 0; b < srcRaster.getNumBands(); b++) {
dstRaster.setSample(x, y, b, srcRaster.getSample(x, y, b));
}
```

Thus, when copying an integral type source to an integral type
destination, if the source sample size is greater than the destination
sample size for a particular band, the high order bits of the source
sample are truncated. If the source sample size is less than the
destination size for a particular band, the high order bits of the
destination are zero-extended or sign-extended depending on whether
srcRaster's SampleModel treats the sample as a signed or unsigned
quantity.

When copying a float or double source to an integral type destination,
each source sample is cast to the destination type. When copying an
integral type source to a float or double destination, the source
is first converted to a 32-bit int (if necessary), using the above
rules for integral types, and then the int is cast to float or
double.

If all samples of both source and destination Rasters are of
integral type and less than or equal to 32 bits in size, then calling
this method is equivalent to executing the following code for all

x,y

addresses valid in both Rasters.

```java
Raster srcRaster;
WritableRaster dstRaster;
for (int b = 0; b < srcRaster.getNumBands(); b++) {
dstRaster.setSample(x, y, b, srcRaster.getSample(x, y, b));
}
```

Thus, when copying an integral type source to an integral type
destination, if the source sample size is greater than the destination
sample size for a particular band, the high order bits of the source
sample are truncated. If the source sample size is less than the
destination size for a particular band, the high order bits of the
destination are zero-extended or sign-extended depending on whether
srcRaster's SampleModel treats the sample as a signed or unsigned
quantity.

When copying a float or double source to an integral type destination,
each source sample is cast to the destination type. When copying an
integral type source to a float or double destination, the source
is first converted to a 32-bit int (if necessary), using the above
rules for integral types, and then the int is cast to float or
double.

Raster srcRaster;
WritableRaster dstRaster;
for (int b = 0; b < srcRaster.getNumBands(); b++) {
dstRaster.setSample(x, y, b, srcRaster.getSample(x, y, b));
}

When copying a float or double source to an integral type destination,
each source sample is cast to the destination type. When copying an
integral type source to a float or double destination, the source
is first converted to a 32-bit int (if necessary), using the above
rules for integral types, and then the int is cast to float or
double.

setRect

```java
public void setRect​(int dx,
int dy,

Raster
srcRaster)
```

Copies pixels from Raster srcRaster to this WritableRaster.
For each (x, y) address in srcRaster, the corresponding pixel
is copied to address (x+dx, y+dy) in this WritableRaster,
unless (x+dx, y+dy) falls outside the bounds of this raster.
srcRaster must have the same number of bands as this WritableRaster.
The copy is a simple copy of source samples to the corresponding
destination samples. For details, see

setRect(Raster)

.

**Parameters:** dx

- The X translation factor from src space to dst space
of the copy.
**Parameters:** dy

- The Y translation factor from src space to dst space
of the copy.
**Parameters:** srcRaster

- The Raster from which to copy pixels.
**Throws:** NullPointerException

- if srcRaster is null.

---

#### setRect

public void setRect​(int dx,
int dy,

Raster

srcRaster)

Copies pixels from Raster srcRaster to this WritableRaster.
For each (x, y) address in srcRaster, the corresponding pixel
is copied to address (x+dx, y+dy) in this WritableRaster,
unless (x+dx, y+dy) falls outside the bounds of this raster.
srcRaster must have the same number of bands as this WritableRaster.
The copy is a simple copy of source samples to the corresponding
destination samples. For details, see

setRect(Raster)

.

setPixel

```java
public void setPixel​(int x,
int y,
int[] iArray)
```

Sets a pixel in the DataBuffer using an int array of samples for input.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** iArray

- The input samples in a int array.
**Throws:** NullPointerException

- if iArray is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are not
in bounds, or if iArray is too small to hold the input.

---

#### setPixel

public void setPixel​(int x,
int y,
int[] iArray)

Sets a pixel in the DataBuffer using an int array of samples for input.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

setPixel

```java
public void setPixel​(int x,
int y,
float[] fArray)
```

Sets a pixel in the DataBuffer using a float array of samples for input.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** fArray

- The input samples in a float array.
**Throws:** NullPointerException

- if fArray is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are not
in bounds, or if fArray is too small to hold the input.

---

#### setPixel

public void setPixel​(int x,
int y,
float[] fArray)

Sets a pixel in the DataBuffer using a float array of samples for input.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

setPixel

```java
public void setPixel​(int x,
int y,
double[] dArray)
```

Sets a pixel in the DataBuffer using a double array of samples for input.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** dArray

- The input samples in a double array.
**Throws:** NullPointerException

- if dArray is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are not
in bounds, or if dArray is too small to hold the input.

---

#### setPixel

public void setPixel​(int x,
int y,
double[] dArray)

Sets a pixel in the DataBuffer using a double array of samples for input.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

setPixels

```java
public void setPixels​(int x,
int y,
int w,
int h,
int[] iArray)
```

Sets all samples for a rectangle of pixels from an int array containing
one sample per array element.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

**Parameters:** x

- The X coordinate of the upper left pixel location.
**Parameters:** y

- The Y coordinate of the upper left pixel location.
**Parameters:** w

- Width of the pixel rectangle.
**Parameters:** h

- Height of the pixel rectangle.
**Parameters:** iArray

- The input int pixel array.
**Throws:** NullPointerException

- if iArray is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are not
in bounds, or if iArray is too small to hold the input.

---

#### setPixels

public void setPixels​(int x,
int y,
int w,
int h,
int[] iArray)

Sets all samples for a rectangle of pixels from an int array containing
one sample per array element.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

setPixels

```java
public void setPixels​(int x,
int y,
int w,
int h,
float[] fArray)
```

Sets all samples for a rectangle of pixels from a float array containing
one sample per array element.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

**Parameters:** x

- The X coordinate of the upper left pixel location.
**Parameters:** y

- The Y coordinate of the upper left pixel location.
**Parameters:** w

- Width of the pixel rectangle.
**Parameters:** h

- Height of the pixel rectangle.
**Parameters:** fArray

- The input float pixel array.
**Throws:** NullPointerException

- if fArray is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are not
in bounds, or if fArray is too small to hold the input.

---

#### setPixels

public void setPixels​(int x,
int y,
int w,
int h,
float[] fArray)

Sets all samples for a rectangle of pixels from a float array containing
one sample per array element.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

setPixels

```java
public void setPixels​(int x,
int y,
int w,
int h,
double[] dArray)
```

Sets all samples for a rectangle of pixels from a double array containing
one sample per array element.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

**Parameters:** x

- The X coordinate of the upper left pixel location.
**Parameters:** y

- The Y coordinate of the upper left pixel location.
**Parameters:** w

- Width of the pixel rectangle.
**Parameters:** h

- Height of the pixel rectangle.
**Parameters:** dArray

- The input double pixel array.
**Throws:** NullPointerException

- if dArray is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates are not
in bounds, or if dArray is too small to hold the input.

---

#### setPixels

public void setPixels​(int x,
int y,
int w,
int h,
double[] dArray)

Sets all samples for a rectangle of pixels from a double array containing
one sample per array element.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

setSample

```java
public void setSample​(int x,
int y,
int b,
int s)
```

Sets a sample in the specified band for the pixel located at (x,y)
in the DataBuffer using an int for input.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** b

- The band to set.
**Parameters:** s

- The input sample.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds.

---

#### setSample

public void setSample​(int x,
int y,
int b,
int s)

Sets a sample in the specified band for the pixel located at (x,y)
in the DataBuffer using an int for input.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

setSample

```java
public void setSample​(int x,
int y,
int b,
float s)
```

Sets a sample in the specified band for the pixel located at (x,y)
in the DataBuffer using a float for input.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** b

- The band to set.
**Parameters:** s

- The input sample as a float.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds.

---

#### setSample

public void setSample​(int x,
int y,
int b,
float s)

Sets a sample in the specified band for the pixel located at (x,y)
in the DataBuffer using a float for input.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

setSample

```java
public void setSample​(int x,
int y,
int b,
double s)
```

Sets a sample in the specified band for the pixel located at (x,y)
in the DataBuffer using a double for input.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

**Parameters:** x

- The X coordinate of the pixel location.
**Parameters:** y

- The Y coordinate of the pixel location.
**Parameters:** b

- The band to set.
**Parameters:** s

- The input sample as a double.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds.

---

#### setSample

public void setSample​(int x,
int y,
int b,
double s)

Sets a sample in the specified band for the pixel located at (x,y)
in the DataBuffer using a double for input.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

setSamples

```java
public void setSamples​(int x,
int y,
int w,
int h,
int b,
int[] iArray)
```

Sets the samples in the specified band for the specified rectangle
of pixels from an int array containing one sample per array element.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

**Parameters:** x

- The X coordinate of the upper left pixel location.
**Parameters:** y

- The Y coordinate of the upper left pixel location.
**Parameters:** w

- Width of the pixel rectangle.
**Parameters:** h

- Height of the pixel rectangle.
**Parameters:** b

- The band to set.
**Parameters:** iArray

- The input int sample array.
**Throws:** NullPointerException

- if iArray is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds, or if iArray is too small to
hold the input.

---

#### setSamples

public void setSamples​(int x,
int y,
int w,
int h,
int b,
int[] iArray)

Sets the samples in the specified band for the specified rectangle
of pixels from an int array containing one sample per array element.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

setSamples

```java
public void setSamples​(int x,
int y,
int w,
int h,
int b,
float[] fArray)
```

Sets the samples in the specified band for the specified rectangle
of pixels from a float array containing one sample per array element.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

**Parameters:** x

- The X coordinate of the upper left pixel location.
**Parameters:** y

- The Y coordinate of the upper left pixel location.
**Parameters:** w

- Width of the pixel rectangle.
**Parameters:** h

- Height of the pixel rectangle.
**Parameters:** b

- The band to set.
**Parameters:** fArray

- The input float sample array.
**Throws:** NullPointerException

- if fArray is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds, or if fArray is too small to
hold the input.

---

#### setSamples

public void setSamples​(int x,
int y,
int w,
int h,
int b,
float[] fArray)

Sets the samples in the specified band for the specified rectangle
of pixels from a float array containing one sample per array element.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

setSamples

```java
public void setSamples​(int x,
int y,
int w,
int h,
int b,
double[] dArray)
```

Sets the samples in the specified band for the specified rectangle
of pixels from a double array containing one sample per array element.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

**Parameters:** x

- The X coordinate of the upper left pixel location.
**Parameters:** y

- The Y coordinate of the upper left pixel location.
**Parameters:** w

- Width of the pixel rectangle.
**Parameters:** h

- Height of the pixel rectangle.
**Parameters:** b

- The band to set.
**Parameters:** dArray

- The input double sample array.
**Throws:** NullPointerException

- if dArray is null.
**Throws:** ArrayIndexOutOfBoundsException

- if the coordinates or
the band index are not in bounds, or if dArray is too small to
hold the input.

---

#### setSamples

public void setSamples​(int x,
int y,
int w,
int h,
int b,
double[] dArray)

Sets the samples in the specified band for the specified rectangle
of pixels from a double array containing one sample per array element.
An ArrayIndexOutOfBoundsException may be thrown if the coordinates are
not in bounds.
However, explicit bounds checking is not guaranteed.

---

