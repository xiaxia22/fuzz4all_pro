# Class IndexColorModel

**Source:** `java.desktop\java\awt\image\IndexColorModel.html`

### Class Description

```java
public class
IndexColorModel

extends
ColorModel
```

The

IndexColorModel

class is a

ColorModel

class that works with pixel values consisting of a
single sample that is an index into a fixed colormap in the default
sRGB color space. The colormap specifies red, green, blue, and
optional alpha components corresponding to each index. All components
are represented in the colormap as 8-bit unsigned integral values.
Some constructors allow the caller to specify "holes" in the colormap
by indicating which colormap entries are valid and which represent
unusable colors via the bits set in a

BigInteger

object.
This color model is similar to an X11 PseudoColor visual.

Some constructors provide a means to specify an alpha component
for each pixel in the colormap, while others either provide no
such means or, in some cases, a flag to indicate whether the
colormap data contains alpha values. If no alpha is supplied to
the constructor, an opaque alpha component (alpha = 1.0) is
assumed for each entry.
An optional transparent pixel value can be supplied that indicates a
pixel to be made completely transparent, regardless of any alpha
component supplied or assumed for that pixel value.
Note that the color components in the colormap of an

IndexColorModel

objects are never pre-multiplied with
the alpha components.

The transparency of an

IndexColorModel

object is
determined by examining the alpha components of the colors in the
colormap and choosing the most specific value after considering
the optional alpha values and any transparent index specified.
The transparency value is

Transparency.OPAQUE

only if all valid colors in
the colormap are opaque and there is no valid transparent pixel.
If all valid colors
in the colormap are either completely opaque (alpha = 1.0) or
completely transparent (alpha = 0.0), which typically occurs when
a valid transparent pixel is specified,
the value is

Transparency.BITMASK

.
Otherwise, the value is

Transparency.TRANSLUCENT

, indicating
that some valid color has an alpha component that is
neither completely transparent nor completely opaque
(0.0 < alpha < 1.0).

If an

IndexColorModel

object has
a transparency value of

Transparency.OPAQUE

,
then the

hasAlpha

and

getNumComponents

methods
(both inherited from

ColorModel

)
return false and 3, respectively.
For any other transparency value,

hasAlpha

returns true
and

getNumComponents

returns 4.

The values used to index into the colormap are taken from the least
significant

n

bits of pixel representations where

n

is based on the pixel size specified in the constructor.
For pixel sizes smaller than 8 bits,

n

is rounded up to a
power of two (3 becomes 4 and 5,6,7 become 8).
For pixel sizes between 8 and 16 bits,

n

is equal to the
pixel size.
Pixel sizes larger than 16 bits are not supported by this class.
Higher order bits beyond

n

are ignored in pixel representations.
Index values greater than or equal to the map size, but less than
2

n

, are undefined and return 0 for all color and
alpha components.

For those methods that use a primitive array pixel representation of
type

transferType

, the array length is always one.
The transfer types supported are

DataBuffer.TYPE_BYTE

and

DataBuffer.TYPE_USHORT

. A single int pixel
representation is valid for all objects of this class, since it is
always possible to represent pixel values used with this class in a
single int. Therefore, methods that use this representation do
not throw an

IllegalArgumentException

due to an invalid
pixel value.

Many of the methods in this class are final. The reason for
this is that the underlying native graphics code makes assumptions
about the layout and operation of this class and those assumptions
are reflected in the implementations of the methods here that are
marked final. You can subclass this class for other reasons, but
you cannot override or modify the behaviour of those methods.

**All Implemented Interfaces:** Transparency

---

### Field Details

*No entries found.*

### Constructor Details

#### public IndexColorModel​(int bits,
int size,
byte[] r,
byte[] g,
byte[] b)

Constructs an

IndexColorModel

from the specified
arrays of red, green, and blue components. Pixels described
by this color model all have alpha components of 255
unnormalized (1.0 normalized), which means they
are fully opaque. All of the arrays specifying the color
components must have at least the specified number of entries.
The

ColorSpace

is the default sRGB space.
Since there is no alpha information in any of the arguments
to this constructor, the transparency value is always

Transparency.OPAQUE

.
The transfer type is the smallest of

DataBuffer.TYPE_BYTE

or

DataBuffer.TYPE_USHORT

that can hold a single pixel.

**Parameters:**
- bits

- the number of bits each pixel occupies
- size

- the size of the color component arrays
- r

- the array of red color components
- g

- the array of green color components
- b

- the array of blue color components

**Throws:**
- IllegalArgumentException

- if

bits

is less
than 1 or greater than 16
- IllegalArgumentException

- if

size

is less
than 1

---

#### public IndexColorModel​(int bits,
int size,
byte[] r,
byte[] g,
byte[] b,
int trans)

Constructs an

IndexColorModel

from the given arrays
of red, green, and blue components. Pixels described by this color
model all have alpha components of 255 unnormalized
(1.0 normalized), which means they are fully opaque, except
for the indicated pixel to be made transparent. All of the arrays
specifying the color components must have at least the specified
number of entries.
The

ColorSpace

is the default sRGB space.
The transparency value may be

Transparency.OPAQUE

or

Transparency.BITMASK

depending on the arguments, as
specified in the

class description

above.
The transfer type is the smallest of

DataBuffer.TYPE_BYTE

or

DataBuffer.TYPE_USHORT

that can hold a
single pixel.

**Parameters:**
- bits

- the number of bits each pixel occupies
- size

- the size of the color component arrays
- r

- the array of red color components
- g

- the array of green color components
- b

- the array of blue color components
- trans

- the index of the transparent pixel

**Throws:**
- IllegalArgumentException

- if

bits

is less than
1 or greater than 16
- IllegalArgumentException

- if

size

is less than
1

---

#### public IndexColorModel​(int bits,
int size,
byte[] r,
byte[] g,
byte[] b,
byte[] a)

Constructs an

IndexColorModel

from the given
arrays of red, green, blue and alpha components. All of the
arrays specifying the components must have at least the specified
number of entries.
The

ColorSpace

is the default sRGB space.
The transparency value may be any of

Transparency.OPAQUE

,

Transparency.BITMASK

,
or

Transparency.TRANSLUCENT

depending on the arguments, as specified
in the

class description

above.
The transfer type is the smallest of

DataBuffer.TYPE_BYTE

or

DataBuffer.TYPE_USHORT

that can hold a single pixel.

**Parameters:**
- bits

- the number of bits each pixel occupies
- size

- the size of the color component arrays
- r

- the array of red color components
- g

- the array of green color components
- b

- the array of blue color components
- a

- the array of alpha value components

**Throws:**
- IllegalArgumentException

- if

bits

is less
than 1 or greater than 16
- IllegalArgumentException

- if

size

is less
than 1

---

#### public IndexColorModel​(int bits,
int size,
byte[] cmap,
int start,
boolean hasalpha)

Constructs an

IndexColorModel

from a single
array of interleaved red, green, blue and optional alpha
components. The array must have enough values in it to
fill all of the needed component arrays of the specified
size. The

ColorSpace

is the default sRGB space.
The transparency value may be any of

Transparency.OPAQUE

,

Transparency.BITMASK

,
or

Transparency.TRANSLUCENT

depending on the arguments, as specified
in the

class description

above.
The transfer type is the smallest of

DataBuffer.TYPE_BYTE

or

DataBuffer.TYPE_USHORT

that can hold a single pixel.

**Parameters:**
- bits

- the number of bits each pixel occupies
- size

- the size of the color component arrays
- cmap

- the array of color components
- start

- the starting offset of the first color component
- hasalpha

- indicates whether alpha values are contained in
the

cmap

array

**Throws:**
- IllegalArgumentException

- if

bits

is less
than 1 or greater than 16
- IllegalArgumentException

- if

size

is less
than 1

---

#### public IndexColorModel​(int bits,
int size,
byte[] cmap,
int start,
boolean hasalpha,
int trans)

Constructs an

IndexColorModel

from a single array of
interleaved red, green, blue and optional alpha components. The
specified transparent index represents a pixel that is made
entirely transparent regardless of any alpha value specified
for it. The array must have enough values in it to fill all
of the needed component arrays of the specified size.
The

ColorSpace

is the default sRGB space.
The transparency value may be any of

Transparency.OPAQUE

,

Transparency.BITMASK

,
or

Transparency.TRANSLUCENT

depending on the arguments, as specified
in the

class description

above.
The transfer type is the smallest of

DataBuffer.TYPE_BYTE

or

DataBuffer.TYPE_USHORT

that can hold a single pixel.

**Parameters:**
- bits

- the number of bits each pixel occupies
- size

- the size of the color component arrays
- cmap

- the array of color components
- start

- the starting offset of the first color component
- hasalpha

- indicates whether alpha values are contained in
the

cmap

array
- trans

- the index of the fully transparent pixel

**Throws:**
- IllegalArgumentException

- if

bits

is less than
1 or greater than 16
- IllegalArgumentException

- if

size

is less than
1

---

#### public IndexColorModel​(int bits,
int size,
int[] cmap,
int start,
boolean hasalpha,
int trans,
int transferType)

Constructs an

IndexColorModel

from an array of
ints where each int is comprised of red, green, blue, and
optional alpha components in the default RGB color model format.
The specified transparent index represents a pixel that is made
entirely transparent regardless of any alpha value specified
for it. The array must have enough values in it to fill all
of the needed component arrays of the specified size.
The

ColorSpace

is the default sRGB space.
The transparency value may be any of

Transparency.OPAQUE

,

Transparency.BITMASK

,
or

Transparency.TRANSLUCENT

depending on the arguments, as specified
in the

class description

above.

**Parameters:**
- bits

- the number of bits each pixel occupies
- size

- the size of the color component arrays
- cmap

- the array of color components
- start

- the starting offset of the first color component
- hasalpha

- indicates whether alpha values are contained in
the

cmap

array
- trans

- the index of the fully transparent pixel
- transferType

- the data type of the array used to represent
pixel values. The data type must be either

DataBuffer.TYPE_BYTE

or

DataBuffer.TYPE_USHORT

.

**Throws:**
- IllegalArgumentException

- if

bits

is less
than 1 or greater than 16
- IllegalArgumentException

- if

size

is less
than 1
- IllegalArgumentException

- if

transferType

is not
one of

DataBuffer.TYPE_BYTE

or

DataBuffer.TYPE_USHORT

---

#### public IndexColorModel​(int bits,
int size,
int[] cmap,
int start,
int transferType,

BigInteger
validBits)

Constructs an

IndexColorModel

from an

int

array where each

int

is
comprised of red, green, blue, and alpha
components in the default RGB color model format.
The array must have enough values in it to fill all
of the needed component arrays of the specified size.
The

ColorSpace

is the default sRGB space.
The transparency value may be any of

Transparency.OPAQUE

,

Transparency.BITMASK

,
or

Transparency.TRANSLUCENT

depending on the arguments, as specified
in the

class description

above.
The transfer type must be one of

DataBuffer.TYPE_BYTE

DataBuffer.TYPE_USHORT

.
The

BigInteger

object specifies the valid/invalid pixels
in the

cmap

array. A pixel is valid if the

BigInteger

value at that index is set, and is invalid
if the

BigInteger

bit at that index is not set.

**Parameters:**
- bits

- the number of bits each pixel occupies
- size

- the size of the color component array
- cmap

- the array of color components
- start

- the starting offset of the first color component
- transferType

- the specified data type
- validBits

- a

BigInteger

object. If a bit is
set in the BigInteger, the pixel at that index is valid.
If a bit is not set, the pixel at that index
is considered invalid. If null, all pixels are valid.
Only bits from 0 to the map size are considered.

**Throws:**
- IllegalArgumentException

- if

bits

is less
than 1 or greater than 16
- IllegalArgumentException

- if

size

is less
than 1
- IllegalArgumentException

- if

transferType

is not
one of

DataBuffer.TYPE_BYTE

or

DataBuffer.TYPE_USHORT

**Since:**
- 1.3

---

### Method Details

#### public int getTransparency()

Returns the transparency. Returns either OPAQUE, BITMASK,
or TRANSLUCENT

**Specified by:**
- getTransparency

in interface

Transparency

**Overrides:**
- getTransparency

in class

ColorModel

**Returns:**
- the transparency of this

IndexColorModel

**See Also:**
- Transparency.OPAQUE

,

Transparency.BITMASK

,

Transparency.TRANSLUCENT

---

#### public int[] getComponentSize()

Returns an array of the number of bits for each color/alpha component.
The array contains the color components in the order red, green,
blue, followed by the alpha component, if present.

**Overrides:**
- getComponentSize

in class

ColorModel

**Returns:**
- an array containing the number of bits of each color
and alpha component of this

IndexColorModel

---

#### public final int getMapSize()

Returns the size of the color/alpha component arrays in this

IndexColorModel

.

**Returns:**
- the size of the color and alpha component arrays.

---

#### public final int getTransparentPixel()

Returns the index of a transparent pixel in this

IndexColorModel

or -1 if there is no pixel
with an alpha value of 0. If a transparent pixel was
explicitly specified in one of the constructors by its
index, then that index will be preferred, otherwise,
the index of any pixel which happens to be fully transparent
may be returned.

**Returns:**
- the index of a transparent pixel in this

IndexColorModel

object, or -1 if there
is no such pixel

---

#### public final void getReds​(byte[] r)

Copies the array of red color components into the specified array.
Only the initial entries of the array as specified by

getMapSize

are written.

**Parameters:**
- r

- the specified array into which the elements of the
array of red color components are copied

---

#### public final void getGreens​(byte[] g)

Copies the array of green color components into the specified array.
Only the initial entries of the array as specified by

getMapSize

are written.

**Parameters:**
- g

- the specified array into which the elements of the
array of green color components are copied

---

#### public final void getBlues​(byte[] b)

Copies the array of blue color components into the specified array.
Only the initial entries of the array as specified by

getMapSize

are written.

**Parameters:**
- b

- the specified array into which the elements of the
array of blue color components are copied

---

#### public final void getAlphas​(byte[] a)

Copies the array of alpha transparency components into the
specified array. Only the initial entries of the array as specified
by

getMapSize

are written.

**Parameters:**
- a

- the specified array into which the elements of the
array of alpha components are copied

---

#### public final void getRGBs​(int[] rgb)

Converts data for each index from the color and alpha component
arrays to an int in the default RGB ColorModel format and copies
the resulting 32-bit ARGB values into the specified array. Only
the initial entries of the array as specified by

getMapSize

are
written.

**Parameters:**
- rgb

- the specified array into which the converted ARGB
values from this array of color and alpha components
are copied.

---

#### public final int getRed​(int pixel)

Returns the red color component for the specified pixel, scaled
from 0 to 255 in the default RGB ColorSpace, sRGB. The pixel value
is specified as an int.
Only the lower

n

bits of the pixel value, as specified in the

class description

above, are used to
calculate the returned value.
The returned value is a non pre-multiplied value.

**Specified by:**
- getRed

in class

ColorModel

**Parameters:**
- pixel

- the specified pixel

**Returns:**
- the value of the red color component for the specified pixel

---

#### public final int getGreen​(int pixel)

Returns the green color component for the specified pixel, scaled
from 0 to 255 in the default RGB ColorSpace, sRGB. The pixel value
is specified as an int.
Only the lower

n

bits of the pixel value, as specified in the

class description

above, are used to
calculate the returned value.
The returned value is a non pre-multiplied value.

**Specified by:**
- getGreen

in class

ColorModel

**Parameters:**
- pixel

- the specified pixel

**Returns:**
- the value of the green color component for the specified pixel

---

#### public final int getBlue​(int pixel)

Returns the blue color component for the specified pixel, scaled
from 0 to 255 in the default RGB ColorSpace, sRGB. The pixel value
is specified as an int.
Only the lower

n

bits of the pixel value, as specified in the

class description

above, are used to
calculate the returned value.
The returned value is a non pre-multiplied value.

**Specified by:**
- getBlue

in class

ColorModel

**Parameters:**
- pixel

- the specified pixel

**Returns:**
- the value of the blue color component for the specified pixel

---

#### public final int getAlpha​(int pixel)

Returns the alpha component for the specified pixel, scaled
from 0 to 255. The pixel value is specified as an int.
Only the lower

n

bits of the pixel value, as specified in the

class description

above, are used to
calculate the returned value.

**Specified by:**
- getAlpha

in class

ColorModel

**Parameters:**
- pixel

- the specified pixel

**Returns:**
- the value of the alpha component for the specified pixel

---

#### public final int getRGB​(int pixel)

Returns the color/alpha components of the pixel in the default
RGB color model format. The pixel value is specified as an int.
Only the lower

n

bits of the pixel value, as specified in the

class description

above, are used to
calculate the returned value.
The returned value is in a non pre-multiplied format.

**Overrides:**
- getRGB

in class

ColorModel

**Parameters:**
- pixel

- the specified pixel

**Returns:**
- the color and alpha components of the specified pixel

**See Also:**
- ColorModel.getRGBdefault()

---

#### public
Object
getDataElements​(int rgb,

Object
pixel)

Returns a data element array representation of a pixel in this
ColorModel, given an integer pixel representation in the
default RGB color model. This array can then be passed to the

setDataElements

method of a

WritableRaster

object. If the pixel variable is

null

, a new array is allocated. If

pixel

is not

null

, it must be
a primitive array of type

transferType

; otherwise, a

ClassCastException

is thrown. An

ArrayIndexOutOfBoundsException

is
thrown if

pixel

is not large enough to hold a pixel
value for this

ColorModel

. The pixel array is returned.

Since

IndexColorModel

can be subclassed, subclasses
inherit the implementation of this method and if they don't
override it then they throw an exception if they use an
unsupported

transferType

.

**Overrides:**
- getDataElements

in class

ColorModel

**Parameters:**
- rgb

- the integer pixel representation in the default RGB
color model
- pixel

- the specified pixel

**Returns:**
- an array representation of the specified pixel in this

IndexColorModel

.

**Throws:**
- ClassCastException

- if

pixel

is not a primitive array of type

transferType
- ArrayIndexOutOfBoundsException

- if

pixel

is not large enough to hold a pixel value
for this

ColorModel
- UnsupportedOperationException

- if

transferType

is invalid

**See Also:**
- WritableRaster.setDataElements(int, int, java.lang.Object)

,

SampleModel.setDataElements(int, int, java.lang.Object, java.awt.image.DataBuffer)

---

#### public int[] getComponents​(int pixel,
int[] components,
int offset)

Returns an array of unnormalized color/alpha components for a
specified pixel in this

ColorModel

. The pixel value
is specified as an int. If the

components

array is

null

,
a new array is allocated that contains

offset + getNumComponents()

elements.
The

components

array is returned,
with the alpha component included
only if

hasAlpha

returns true.
Color/alpha components are stored in the

components

array starting
at

offset

even if the array is allocated by this method.
An

ArrayIndexOutOfBoundsException

is thrown if the

components

array is not

null

and is
not large enough to hold all the color and alpha components
starting at

offset

.

**Overrides:**
- getComponents

in class

ColorModel

**Parameters:**
- pixel

- the specified pixel
- components

- the array to receive the color and alpha
components of the specified pixel
- offset

- the offset into the

components

array at
which to start storing the color and alpha components

**Returns:**
- an array containing the color and alpha components of the
specified pixel starting at the specified offset.

**See Also:**
- ColorModel.hasAlpha()

,

ColorModel.getNumComponents()

---

#### public int[] getComponents​(
Object
pixel,
int[] components,
int offset)

Returns an array of unnormalized color/alpha components for
a specified pixel in this

ColorModel

. The pixel
value is specified by an array of data elements of type

transferType

passed in as an object reference.
If

pixel

is not a primitive array of type

transferType

, a

ClassCastException

is thrown. An

ArrayIndexOutOfBoundsException

is thrown if

pixel

is not large enough to hold
a pixel value for this

ColorModel

. If the

components

array is

null

, a new array
is allocated that contains

offset + getNumComponents()

elements.
The

components

array is returned,
with the alpha component included
only if

hasAlpha

returns true.
Color/alpha components are stored in the

components

array starting at

offset

even if the array is
allocated by this method. An

ArrayIndexOutOfBoundsException

is also
thrown if the

components

array is not

null

and is not large enough to hold all the color
and alpha components starting at

offset

.

Since

IndexColorModel

can be subclassed, subclasses
inherit the implementation of this method and if they don't
override it then they throw an exception if they use an
unsupported

transferType

.

**Overrides:**
- getComponents

in class

ColorModel

**Parameters:**
- pixel

- the specified pixel
- components

- an array that receives the color and alpha
components of the specified pixel
- offset

- the index into the

components

array at
which to begin storing the color and alpha components of the
specified pixel

**Returns:**
- an array containing the color and alpha components of the
specified pixel starting at the specified offset.

**Throws:**
- ArrayIndexOutOfBoundsException

- if

pixel

is not large enough to hold a pixel value for this

ColorModel

or if the

components

array is not

null

and is not large enough to hold all the color
and alpha components starting at

offset
- ClassCastException

- if

pixel

is not a
primitive array of type

transferType
- UnsupportedOperationException

- if

transferType

is not one of the supported transfer types

**See Also:**
- ColorModel.hasAlpha()

,

ColorModel.getNumComponents()

---

#### public int getDataElement​(int[] components,
int offset)

Returns a pixel value represented as an int in this

ColorModel

given an array of unnormalized
color/alpha components. An

ArrayIndexOutOfBoundsException

is thrown if the

components

array is not large
enough to hold all of the color and alpha components starting
at

offset

. Since

ColorModel

can be subclassed, subclasses inherit the
implementation of this method and if they don't override it then
they throw an exception if they use an unsupported transferType.

**Overrides:**
- getDataElement

in class

ColorModel

**Parameters:**
- components

- an array of unnormalized color and alpha
components
- offset

- the index into

components

at which to
begin retrieving the color and alpha components

**Returns:**
- an

int

pixel value in this

ColorModel

corresponding to the specified components.

**Throws:**
- ArrayIndexOutOfBoundsException

- if
the

components

array is not large enough to
hold all of the color and alpha components starting at

offset
- UnsupportedOperationException

- if

transferType

is invalid

---

#### public
Object
getDataElements​(int[] components,
int offset,

Object
pixel)

Returns a data element array representation of a pixel in this

ColorModel

given an array of unnormalized color/alpha
components. This array can then be passed to the

setDataElements

method of a

WritableRaster

object. An

ArrayIndexOutOfBoundsException

is
thrown if the

components

array is not large enough to hold all of the
color and alpha components starting at

offset

.
If the pixel variable is

null

, a new array
is allocated. If

pixel

is not

null

,
it must be a primitive array of type

transferType

;
otherwise, a

ClassCastException

is thrown.
An

ArrayIndexOutOfBoundsException

is thrown if pixel
is not large enough to hold a pixel value for this

ColorModel

.

Since

IndexColorModel

can be subclassed, subclasses
inherit the implementation of this method and if they don't
override it then they throw an exception if they use an
unsupported

transferType

**Overrides:**
- getDataElements

in class

ColorModel

**Parameters:**
- components

- an array of unnormalized color and alpha
components
- offset

- the index into

components

at which to
begin retrieving color and alpha components
- pixel

- the

Object

representing an array of color
and alpha components

**Returns:**
- an

Object

representing an array of color and
alpha components.

**Throws:**
- ClassCastException

- if

pixel

is not a primitive array of type

transferType
- ArrayIndexOutOfBoundsException

- if

pixel

is not large enough to hold a pixel value
for this

ColorModel

or the

components

array is not large enough to hold all of the color and alpha
components starting at

offset
- UnsupportedOperationException

- if

transferType

is not one of the supported transfer types

**See Also:**
- WritableRaster.setDataElements(int, int, java.lang.Object)

,

SampleModel.setDataElements(int, int, java.lang.Object, java.awt.image.DataBuffer)

---

#### public
WritableRaster
createCompatibleWritableRaster​(int w,
int h)

Creates a

WritableRaster

with the specified width
and height that has a data layout (

SampleModel

)
compatible with this

ColorModel

. This method
only works for color models with 16 or fewer bits per pixel.

Since

IndexColorModel

can be subclassed, any
subclass that supports greater than 16 bits per pixel must
override this method.

**Overrides:**
- createCompatibleWritableRaster

in class

ColorModel

**Parameters:**
- w

- the width to apply to the new

WritableRaster
- h

- the height to apply to the new

WritableRaster

**Returns:**
- a

WritableRaster

object with the specified
width and height.

**Throws:**
- UnsupportedOperationException

- if the number of bits in a
pixel is greater than 16

**See Also:**
- WritableRaster

,

SampleModel

---

#### public boolean isCompatibleRaster​(
Raster
raster)

Returns

true

if

raster

is compatible
with this

ColorModel

or

false

if it
is not compatible with this

ColorModel

.

**Overrides:**
- isCompatibleRaster

in class

ColorModel

**Parameters:**
- raster

- the

Raster

object to test for compatibility

**Returns:**
- true

if

raster

is compatible
with this

ColorModel

;

false

otherwise.

---

#### public
SampleModel
createCompatibleSampleModel​(int w,
int h)

Creates a

SampleModel

with the specified
width and height that has a data layout compatible with
this

ColorModel

.

**Overrides:**
- createCompatibleSampleModel

in class

ColorModel

**Parameters:**
- w

- the width to apply to the new

SampleModel
- h

- the height to apply to the new

SampleModel

**Returns:**
- a

SampleModel

object with the specified
width and height.

**Throws:**
- IllegalArgumentException

- if

w

or

h

is not greater than 0

**See Also:**
- SampleModel

---

#### public boolean isCompatibleSampleModel​(
SampleModel
sm)

Checks if the specified

SampleModel

is compatible
with this

ColorModel

. If

sm

is

null

, this method returns

false

.

**Overrides:**
- isCompatibleSampleModel

in class

ColorModel

**Parameters:**
- sm

- the specified

SampleModel

,
or

null

**Returns:**
- true

if the specified

SampleModel

is compatible with this

ColorModel

;

false

otherwise.

**See Also:**
- SampleModel

---

#### public
BufferedImage
convertToIntDiscrete​(
Raster
raster,
boolean forceARGB)

Returns a new

BufferedImage

of TYPE_INT_ARGB or
TYPE_INT_RGB that has a

Raster

with pixel data
computed by expanding the indices in the source

Raster

using the color/alpha component arrays of this

ColorModel

.
Only the lower

n

bits of each index value in the source

Raster

, as specified in the

class description

above, are used to
compute the color/alpha values in the returned image.
If

forceARGB

is

true

, a TYPE_INT_ARGB image is
returned regardless of whether or not this

ColorModel

has an alpha component array or a transparent pixel.

**Parameters:**
- raster

- the specified

Raster
- forceARGB

- if

true

, the returned

BufferedImage

is TYPE_INT_ARGB; otherwise it is
TYPE_INT_RGB

**Returns:**
- a

BufferedImage

created with the specified

Raster

**Throws:**
- IllegalArgumentException

- if the raster argument is not
compatible with this IndexColorModel

---

#### public boolean isValid​(int pixel)

Returns whether or not the pixel is valid.

**Parameters:**
- pixel

- the specified pixel value

**Returns:**
- true

if

pixel

is valid;

false

otherwise.

**Since:**
- 1.3

---

#### public boolean isValid()

Returns whether or not all of the pixels are valid.

**Returns:**
- true

if all pixels are valid;

false

otherwise.

**Since:**
- 1.3

---

#### public
BigInteger
getValidPixels()

Returns a

BigInteger

that indicates the valid/invalid
pixels in the colormap. A bit is valid if the

BigInteger

value at that index is set, and is invalid
if the

BigInteger

value at that index is not set.
The only valid ranges to query in the

BigInteger

are
between 0 and the map size.

**Returns:**
- a

BigInteger

indicating the valid/invalid pixels.

**Since:**
- 1.3

---

#### @Deprecated
(
since
="9")
public void finalize()

Disposes of system resources associated with this

ColorModel

once this

ColorModel

is no
longer referenced.

**Overrides:**
- finalize

in class

ColorModel

**See Also:**
- WeakReference

,

PhantomReference

---

#### public
String
toString()

Returns the

String

representation of the contents of
this

ColorModel

object.

**Overrides:**
- toString

in class

ColorModel

**Returns:**
- a

String

representing the contents of this

ColorModel

object.

---

#### public boolean equals​(
Object
obj)

Tests if the specified

Object

is an
instance of

IndexColorModel

and if it equals this

IndexColorModel

**Overrides:**
- equals

in class

ColorModel

**Parameters:**
- obj

- the

Object

to test for equality

**Returns:**
- true

if the specified

Object

equals this

IndexColorModel

;

false

otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns the hash code for IndexColorModel.

**Overrides:**
- hashCode

in class

ColorModel

**Returns:**
- a hash code for IndexColorModel

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

### Additional Sections

#### Class IndexColorModel

java.lang.Object

- java.awt.image.ColorModel
- - java.awt.image.IndexColorModel

java.awt.image.ColorModel

- java.awt.image.IndexColorModel

java.awt.image.IndexColorModel

**All Implemented Interfaces:** Transparency

```java
public class
IndexColorModel

extends
ColorModel
```

The

IndexColorModel

class is a

ColorModel

class that works with pixel values consisting of a
single sample that is an index into a fixed colormap in the default
sRGB color space. The colormap specifies red, green, blue, and
optional alpha components corresponding to each index. All components
are represented in the colormap as 8-bit unsigned integral values.
Some constructors allow the caller to specify "holes" in the colormap
by indicating which colormap entries are valid and which represent
unusable colors via the bits set in a

BigInteger

object.
This color model is similar to an X11 PseudoColor visual.

Some constructors provide a means to specify an alpha component
for each pixel in the colormap, while others either provide no
such means or, in some cases, a flag to indicate whether the
colormap data contains alpha values. If no alpha is supplied to
the constructor, an opaque alpha component (alpha = 1.0) is
assumed for each entry.
An optional transparent pixel value can be supplied that indicates a
pixel to be made completely transparent, regardless of any alpha
component supplied or assumed for that pixel value.
Note that the color components in the colormap of an

IndexColorModel

objects are never pre-multiplied with
the alpha components.

The transparency of an

IndexColorModel

object is
determined by examining the alpha components of the colors in the
colormap and choosing the most specific value after considering
the optional alpha values and any transparent index specified.
The transparency value is

Transparency.OPAQUE

only if all valid colors in
the colormap are opaque and there is no valid transparent pixel.
If all valid colors
in the colormap are either completely opaque (alpha = 1.0) or
completely transparent (alpha = 0.0), which typically occurs when
a valid transparent pixel is specified,
the value is

Transparency.BITMASK

.
Otherwise, the value is

Transparency.TRANSLUCENT

, indicating
that some valid color has an alpha component that is
neither completely transparent nor completely opaque
(0.0 < alpha < 1.0).

If an

IndexColorModel

object has
a transparency value of

Transparency.OPAQUE

,
then the

hasAlpha

and

getNumComponents

methods
(both inherited from

ColorModel

)
return false and 3, respectively.
For any other transparency value,

hasAlpha

returns true
and

getNumComponents

returns 4.

The values used to index into the colormap are taken from the least
significant

n

bits of pixel representations where

n

is based on the pixel size specified in the constructor.
For pixel sizes smaller than 8 bits,

n

is rounded up to a
power of two (3 becomes 4 and 5,6,7 become 8).
For pixel sizes between 8 and 16 bits,

n

is equal to the
pixel size.
Pixel sizes larger than 16 bits are not supported by this class.
Higher order bits beyond

n

are ignored in pixel representations.
Index values greater than or equal to the map size, but less than
2

n

, are undefined and return 0 for all color and
alpha components.

For those methods that use a primitive array pixel representation of
type

transferType

, the array length is always one.
The transfer types supported are

DataBuffer.TYPE_BYTE

and

DataBuffer.TYPE_USHORT

. A single int pixel
representation is valid for all objects of this class, since it is
always possible to represent pixel values used with this class in a
single int. Therefore, methods that use this representation do
not throw an

IllegalArgumentException

due to an invalid
pixel value.

Many of the methods in this class are final. The reason for
this is that the underlying native graphics code makes assumptions
about the layout and operation of this class and those assumptions
are reflected in the implementations of the methods here that are
marked final. You can subclass this class for other reasons, but
you cannot override or modify the behaviour of those methods.

**See Also:** ColorModel

,

ColorSpace

,

DataBuffer

public class

IndexColorModel

extends

ColorModel

The

IndexColorModel

class is a

ColorModel

class that works with pixel values consisting of a
single sample that is an index into a fixed colormap in the default
sRGB color space. The colormap specifies red, green, blue, and
optional alpha components corresponding to each index. All components
are represented in the colormap as 8-bit unsigned integral values.
Some constructors allow the caller to specify "holes" in the colormap
by indicating which colormap entries are valid and which represent
unusable colors via the bits set in a

BigInteger

object.
This color model is similar to an X11 PseudoColor visual.

Some constructors provide a means to specify an alpha component
for each pixel in the colormap, while others either provide no
such means or, in some cases, a flag to indicate whether the
colormap data contains alpha values. If no alpha is supplied to
the constructor, an opaque alpha component (alpha = 1.0) is
assumed for each entry.
An optional transparent pixel value can be supplied that indicates a
pixel to be made completely transparent, regardless of any alpha
component supplied or assumed for that pixel value.
Note that the color components in the colormap of an

IndexColorModel

objects are never pre-multiplied with
the alpha components.

The transparency of an

IndexColorModel

object is
determined by examining the alpha components of the colors in the
colormap and choosing the most specific value after considering
the optional alpha values and any transparent index specified.
The transparency value is

Transparency.OPAQUE

only if all valid colors in
the colormap are opaque and there is no valid transparent pixel.
If all valid colors
in the colormap are either completely opaque (alpha = 1.0) or
completely transparent (alpha = 0.0), which typically occurs when
a valid transparent pixel is specified,
the value is

Transparency.BITMASK

.
Otherwise, the value is

Transparency.TRANSLUCENT

, indicating
that some valid color has an alpha component that is
neither completely transparent nor completely opaque
(0.0 < alpha < 1.0).

If an

IndexColorModel

object has
a transparency value of

Transparency.OPAQUE

,
then the

hasAlpha

and

getNumComponents

methods
(both inherited from

ColorModel

)
return false and 3, respectively.
For any other transparency value,

hasAlpha

returns true
and

getNumComponents

returns 4.

The values used to index into the colormap are taken from the least
significant

n

bits of pixel representations where

n

is based on the pixel size specified in the constructor.
For pixel sizes smaller than 8 bits,

n

is rounded up to a
power of two (3 becomes 4 and 5,6,7 become 8).
For pixel sizes between 8 and 16 bits,

n

is equal to the
pixel size.
Pixel sizes larger than 16 bits are not supported by this class.
Higher order bits beyond

n

are ignored in pixel representations.
Index values greater than or equal to the map size, but less than
2

n

, are undefined and return 0 for all color and
alpha components.

For those methods that use a primitive array pixel representation of
type

transferType

, the array length is always one.
The transfer types supported are

DataBuffer.TYPE_BYTE

and

DataBuffer.TYPE_USHORT

. A single int pixel
representation is valid for all objects of this class, since it is
always possible to represent pixel values used with this class in a
single int. Therefore, methods that use this representation do
not throw an

IllegalArgumentException

due to an invalid
pixel value.

Many of the methods in this class are final. The reason for
this is that the underlying native graphics code makes assumptions
about the layout and operation of this class and those assumptions
are reflected in the implementations of the methods here that are
marked final. You can subclass this class for other reasons, but
you cannot override or modify the behaviour of those methods.

Some constructors provide a means to specify an alpha component
for each pixel in the colormap, while others either provide no
such means or, in some cases, a flag to indicate whether the
colormap data contains alpha values. If no alpha is supplied to
the constructor, an opaque alpha component (alpha = 1.0) is
assumed for each entry.
An optional transparent pixel value can be supplied that indicates a
pixel to be made completely transparent, regardless of any alpha
component supplied or assumed for that pixel value.
Note that the color components in the colormap of an

IndexColorModel

objects are never pre-multiplied with
the alpha components.

The transparency of an

IndexColorModel

object is
determined by examining the alpha components of the colors in the
colormap and choosing the most specific value after considering
the optional alpha values and any transparent index specified.
The transparency value is

Transparency.OPAQUE

only if all valid colors in
the colormap are opaque and there is no valid transparent pixel.
If all valid colors
in the colormap are either completely opaque (alpha = 1.0) or
completely transparent (alpha = 0.0), which typically occurs when
a valid transparent pixel is specified,
the value is

Transparency.BITMASK

.
Otherwise, the value is

Transparency.TRANSLUCENT

, indicating
that some valid color has an alpha component that is
neither completely transparent nor completely opaque
(0.0 < alpha < 1.0).

If an

IndexColorModel

object has
a transparency value of

Transparency.OPAQUE

,
then the

hasAlpha

and

getNumComponents

methods
(both inherited from

ColorModel

)
return false and 3, respectively.
For any other transparency value,

hasAlpha

returns true
and

getNumComponents

returns 4.

The values used to index into the colormap are taken from the least
significant

n

bits of pixel representations where

n

is based on the pixel size specified in the constructor.
For pixel sizes smaller than 8 bits,

n

is rounded up to a
power of two (3 becomes 4 and 5,6,7 become 8).
For pixel sizes between 8 and 16 bits,

n

is equal to the
pixel size.
Pixel sizes larger than 16 bits are not supported by this class.
Higher order bits beyond

n

are ignored in pixel representations.
Index values greater than or equal to the map size, but less than
2

n

, are undefined and return 0 for all color and
alpha components.

For those methods that use a primitive array pixel representation of
type

transferType

, the array length is always one.
The transfer types supported are

DataBuffer.TYPE_BYTE

and

DataBuffer.TYPE_USHORT

. A single int pixel
representation is valid for all objects of this class, since it is
always possible to represent pixel values used with this class in a
single int. Therefore, methods that use this representation do
not throw an

IllegalArgumentException

due to an invalid
pixel value.

Many of the methods in this class are final. The reason for
this is that the underlying native graphics code makes assumptions
about the layout and operation of this class and those assumptions
are reflected in the implementations of the methods here that are
marked final. You can subclass this class for other reasons, but
you cannot override or modify the behaviour of those methods.

The transparency of an

IndexColorModel

object is
determined by examining the alpha components of the colors in the
colormap and choosing the most specific value after considering
the optional alpha values and any transparent index specified.
The transparency value is

Transparency.OPAQUE

only if all valid colors in
the colormap are opaque and there is no valid transparent pixel.
If all valid colors
in the colormap are either completely opaque (alpha = 1.0) or
completely transparent (alpha = 0.0), which typically occurs when
a valid transparent pixel is specified,
the value is

Transparency.BITMASK

.
Otherwise, the value is

Transparency.TRANSLUCENT

, indicating
that some valid color has an alpha component that is
neither completely transparent nor completely opaque
(0.0 < alpha < 1.0).

If an

IndexColorModel

object has
a transparency value of

Transparency.OPAQUE

,
then the

hasAlpha

and

getNumComponents

methods
(both inherited from

ColorModel

)
return false and 3, respectively.
For any other transparency value,

hasAlpha

returns true
and

getNumComponents

returns 4.

The values used to index into the colormap are taken from the least
significant

n

bits of pixel representations where

n

is based on the pixel size specified in the constructor.
For pixel sizes smaller than 8 bits,

n

is rounded up to a
power of two (3 becomes 4 and 5,6,7 become 8).
For pixel sizes between 8 and 16 bits,

n

is equal to the
pixel size.
Pixel sizes larger than 16 bits are not supported by this class.
Higher order bits beyond

n

are ignored in pixel representations.
Index values greater than or equal to the map size, but less than
2

n

, are undefined and return 0 for all color and
alpha components.

For those methods that use a primitive array pixel representation of
type

transferType

, the array length is always one.
The transfer types supported are

DataBuffer.TYPE_BYTE

and

DataBuffer.TYPE_USHORT

. A single int pixel
representation is valid for all objects of this class, since it is
always possible to represent pixel values used with this class in a
single int. Therefore, methods that use this representation do
not throw an

IllegalArgumentException

due to an invalid
pixel value.

Many of the methods in this class are final. The reason for
this is that the underlying native graphics code makes assumptions
about the layout and operation of this class and those assumptions
are reflected in the implementations of the methods here that are
marked final. You can subclass this class for other reasons, but
you cannot override or modify the behaviour of those methods.

If an

IndexColorModel

object has
a transparency value of

Transparency.OPAQUE

,
then the

hasAlpha

and

getNumComponents

methods
(both inherited from

ColorModel

)
return false and 3, respectively.
For any other transparency value,

hasAlpha

returns true
and

getNumComponents

returns 4.

The values used to index into the colormap are taken from the least
significant

n

bits of pixel representations where

n

is based on the pixel size specified in the constructor.
For pixel sizes smaller than 8 bits,

n

is rounded up to a
power of two (3 becomes 4 and 5,6,7 become 8).
For pixel sizes between 8 and 16 bits,

n

is equal to the
pixel size.
Pixel sizes larger than 16 bits are not supported by this class.
Higher order bits beyond

n

are ignored in pixel representations.
Index values greater than or equal to the map size, but less than
2

n

, are undefined and return 0 for all color and
alpha components.

For those methods that use a primitive array pixel representation of
type

transferType

, the array length is always one.
The transfer types supported are

DataBuffer.TYPE_BYTE

and

DataBuffer.TYPE_USHORT

. A single int pixel
representation is valid for all objects of this class, since it is
always possible to represent pixel values used with this class in a
single int. Therefore, methods that use this representation do
not throw an

IllegalArgumentException

due to an invalid
pixel value.

Many of the methods in this class are final. The reason for
this is that the underlying native graphics code makes assumptions
about the layout and operation of this class and those assumptions
are reflected in the implementations of the methods here that are
marked final. You can subclass this class for other reasons, but
you cannot override or modify the behaviour of those methods.

The values used to index into the colormap are taken from the least
significant

n

bits of pixel representations where

n

is based on the pixel size specified in the constructor.
For pixel sizes smaller than 8 bits,

n

is rounded up to a
power of two (3 becomes 4 and 5,6,7 become 8).
For pixel sizes between 8 and 16 bits,

n

is equal to the
pixel size.
Pixel sizes larger than 16 bits are not supported by this class.
Higher order bits beyond

n

are ignored in pixel representations.
Index values greater than or equal to the map size, but less than
2

n

, are undefined and return 0 for all color and
alpha components.

For those methods that use a primitive array pixel representation of
type

transferType

, the array length is always one.
The transfer types supported are

DataBuffer.TYPE_BYTE

and

DataBuffer.TYPE_USHORT

. A single int pixel
representation is valid for all objects of this class, since it is
always possible to represent pixel values used with this class in a
single int. Therefore, methods that use this representation do
not throw an

IllegalArgumentException

due to an invalid
pixel value.

Many of the methods in this class are final. The reason for
this is that the underlying native graphics code makes assumptions
about the layout and operation of this class and those assumptions
are reflected in the implementations of the methods here that are
marked final. You can subclass this class for other reasons, but
you cannot override or modify the behaviour of those methods.

For those methods that use a primitive array pixel representation of
type

transferType

, the array length is always one.
The transfer types supported are

DataBuffer.TYPE_BYTE

and

DataBuffer.TYPE_USHORT

. A single int pixel
representation is valid for all objects of this class, since it is
always possible to represent pixel values used with this class in a
single int. Therefore, methods that use this representation do
not throw an

IllegalArgumentException

due to an invalid
pixel value.

Many of the methods in this class are final. The reason for
this is that the underlying native graphics code makes assumptions
about the layout and operation of this class and those assumptions
are reflected in the implementations of the methods here that are
marked final. You can subclass this class for other reasons, but
you cannot override or modify the behaviour of those methods.

Many of the methods in this class are final. The reason for
this is that the underlying native graphics code makes assumptions
about the layout and operation of this class and those assumptions
are reflected in the implementations of the methods here that are
marked final. You can subclass this class for other reasons, but
you cannot override or modify the behaviour of those methods.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.awt.image.

ColorModel

pixel_bits

,

transferType

- Fields declared in interface java.awt.

Transparency

BITMASK

,

OPAQUE

,

TRANSLUCENT

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

IndexColorModel

​(int bits,
int size,
byte[] r,
byte[] g,
byte[] b)

Constructs an

IndexColorModel

from the specified
arrays of red, green, and blue components.

IndexColorModel

​(int bits,
int size,
byte[] r,
byte[] g,
byte[] b,
byte[] a)

Constructs an

IndexColorModel

from the given
arrays of red, green, blue and alpha components.

IndexColorModel

​(int bits,
int size,
byte[] r,
byte[] g,
byte[] b,
int trans)

Constructs an

IndexColorModel

from the given arrays
of red, green, and blue components.

IndexColorModel

​(int bits,
int size,
byte[] cmap,
int start,
boolean hasalpha)

Constructs an

IndexColorModel

from a single
array of interleaved red, green, blue and optional alpha
components.

IndexColorModel

​(int bits,
int size,
byte[] cmap,
int start,
boolean hasalpha,
int trans)

Constructs an

IndexColorModel

from a single array of
interleaved red, green, blue and optional alpha components.

IndexColorModel

​(int bits,
int size,
int[] cmap,
int start,
boolean hasalpha,
int trans,
int transferType)

Constructs an

IndexColorModel

from an array of
ints where each int is comprised of red, green, blue, and
optional alpha components in the default RGB color model format.

IndexColorModel

​(int bits,
int size,
int[] cmap,
int start,
int transferType,

BigInteger

validBits)

Constructs an

IndexColorModel

from an

int

array where each

int

is
comprised of red, green, blue, and alpha
components in the default RGB color model format.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

BufferedImage

convertToIntDiscrete

​(

Raster

raster,
boolean forceARGB)

Returns a new

BufferedImage

of TYPE_INT_ARGB or
TYPE_INT_RGB that has a

Raster

with pixel data
computed by expanding the indices in the source

Raster

using the color/alpha component arrays of this

ColorModel

.

SampleModel

createCompatibleSampleModel

​(int w,
int h)

Creates a

SampleModel

with the specified
width and height that has a data layout compatible with
this

ColorModel

.

WritableRaster

createCompatibleWritableRaster

​(int w,
int h)

Creates a

WritableRaster

with the specified width
and height that has a data layout (

SampleModel

)
compatible with this

ColorModel

.

boolean

equals

​(

Object

obj)

Tests if the specified

Object

is an
instance of

IndexColorModel

and if it equals this

IndexColorModel

void

finalize

()

Deprecated.

The

finalize

method has been deprecated.

int

getAlpha

​(int pixel)

Returns the alpha component for the specified pixel, scaled
from 0 to 255.

void

getAlphas

​(byte[] a)

Copies the array of alpha transparency components into the
specified array.

int

getBlue

​(int pixel)

Returns the blue color component for the specified pixel, scaled
from 0 to 255 in the default RGB ColorSpace, sRGB.

void

getBlues

​(byte[] b)

Copies the array of blue color components into the specified array.

int[]

getComponents

​(int pixel,
int[] components,
int offset)

Returns an array of unnormalized color/alpha components for a
specified pixel in this

ColorModel

.

int[]

getComponents

​(

Object

pixel,
int[] components,
int offset)

Returns an array of unnormalized color/alpha components for
a specified pixel in this

ColorModel

.

int[]

getComponentSize

()

Returns an array of the number of bits for each color/alpha component.

int

getDataElement

​(int[] components,
int offset)

Returns a pixel value represented as an int in this

ColorModel

given an array of unnormalized
color/alpha components.

Object

getDataElements

​(int[] components,
int offset,

Object

pixel)

Returns a data element array representation of a pixel in this

ColorModel

given an array of unnormalized color/alpha
components.

Object

getDataElements

​(int rgb,

Object

pixel)

Returns a data element array representation of a pixel in this
ColorModel, given an integer pixel representation in the
default RGB color model.

int

getGreen

​(int pixel)

Returns the green color component for the specified pixel, scaled
from 0 to 255 in the default RGB ColorSpace, sRGB.

void

getGreens

​(byte[] g)

Copies the array of green color components into the specified array.

int

getMapSize

()

Returns the size of the color/alpha component arrays in this

IndexColorModel

.

int

getRed

​(int pixel)

Returns the red color component for the specified pixel, scaled
from 0 to 255 in the default RGB ColorSpace, sRGB.

void

getReds

​(byte[] r)

Copies the array of red color components into the specified array.

int

getRGB

​(int pixel)

Returns the color/alpha components of the pixel in the default
RGB color model format.

void

getRGBs

​(int[] rgb)

Converts data for each index from the color and alpha component
arrays to an int in the default RGB ColorModel format and copies
the resulting 32-bit ARGB values into the specified array.

int

getTransparency

()

Returns the transparency.

int

getTransparentPixel

()

Returns the index of a transparent pixel in this

IndexColorModel

or -1 if there is no pixel
with an alpha value of 0.

BigInteger

getValidPixels

()

Returns a

BigInteger

that indicates the valid/invalid
pixels in the colormap.

int

hashCode

()

Returns the hash code for IndexColorModel.

boolean

isCompatibleRaster

​(

Raster

raster)

Returns

true

if

raster

is compatible
with this

ColorModel

or

false

if it
is not compatible with this

ColorModel

.

boolean

isCompatibleSampleModel

​(

SampleModel

sm)

Checks if the specified

SampleModel

is compatible
with this

ColorModel

.

boolean

isValid

()

Returns whether or not all of the pixels are valid.

boolean

isValid

​(int pixel)

Returns whether or not the pixel is valid.

String

toString

()

Returns the

String

representation of the contents of
this

ColorModel

object.

- Methods declared in class java.awt.image.

ColorModel

coerceData

,

getAlpha

,

getAlphaRaster

,

getBlue

,

getColorSpace

,

getComponentSize

,

getDataElement

,

getDataElements

,

getGreen

,

getNormalizedComponents

,

getNormalizedComponents

,

getNumColorComponents

,

getNumComponents

,

getPixelSize

,

getRed

,

getRGB

,

getRGBdefault

,

getTransferType

,

getUnnormalizedComponents

,

hasAlpha

,

isAlphaPremultiplied

- Methods declared in class java.lang.

Object

clone

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

Field Summary

- Fields declared in class java.awt.image.

ColorModel

pixel_bits

,

transferType

- Fields declared in interface java.awt.

Transparency

BITMASK

,

OPAQUE

,

TRANSLUCENT

---

#### Field Summary

Fields declared in class java.awt.image.

ColorModel

pixel_bits

,

transferType

---

#### Fields declared in class java.awt.image. ColorModel

Fields declared in interface java.awt.

Transparency

BITMASK

,

OPAQUE

,

TRANSLUCENT

---

#### Fields declared in interface java.awt. Transparency

Constructor Summary

Constructors

Constructor

Description

IndexColorModel

​(int bits,
int size,
byte[] r,
byte[] g,
byte[] b)

Constructs an

IndexColorModel

from the specified
arrays of red, green, and blue components.

IndexColorModel

​(int bits,
int size,
byte[] r,
byte[] g,
byte[] b,
byte[] a)

Constructs an

IndexColorModel

from the given
arrays of red, green, blue and alpha components.

IndexColorModel

​(int bits,
int size,
byte[] r,
byte[] g,
byte[] b,
int trans)

Constructs an

IndexColorModel

from the given arrays
of red, green, and blue components.

IndexColorModel

​(int bits,
int size,
byte[] cmap,
int start,
boolean hasalpha)

Constructs an

IndexColorModel

from a single
array of interleaved red, green, blue and optional alpha
components.

IndexColorModel

​(int bits,
int size,
byte[] cmap,
int start,
boolean hasalpha,
int trans)

Constructs an

IndexColorModel

from a single array of
interleaved red, green, blue and optional alpha components.

IndexColorModel

​(int bits,
int size,
int[] cmap,
int start,
boolean hasalpha,
int trans,
int transferType)

Constructs an

IndexColorModel

from an array of
ints where each int is comprised of red, green, blue, and
optional alpha components in the default RGB color model format.

IndexColorModel

​(int bits,
int size,
int[] cmap,
int start,
int transferType,

BigInteger

validBits)

Constructs an

IndexColorModel

from an

int

array where each

int

is
comprised of red, green, blue, and alpha
components in the default RGB color model format.

---

#### Constructor Summary

Constructs an

IndexColorModel

from the specified
arrays of red, green, and blue components.

Constructs an

IndexColorModel

from the given
arrays of red, green, blue and alpha components.

Constructs an

IndexColorModel

from the given arrays
of red, green, and blue components.

Constructs an

IndexColorModel

from a single
array of interleaved red, green, blue and optional alpha
components.

Constructs an

IndexColorModel

from a single array of
interleaved red, green, blue and optional alpha components.

Constructs an

IndexColorModel

from an array of
ints where each int is comprised of red, green, blue, and
optional alpha components in the default RGB color model format.

Constructs an

IndexColorModel

from an

int

array where each

int

is
comprised of red, green, blue, and alpha
components in the default RGB color model format.

Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

BufferedImage

convertToIntDiscrete

​(

Raster

raster,
boolean forceARGB)

Returns a new

BufferedImage

of TYPE_INT_ARGB or
TYPE_INT_RGB that has a

Raster

with pixel data
computed by expanding the indices in the source

Raster

using the color/alpha component arrays of this

ColorModel

.

SampleModel

createCompatibleSampleModel

​(int w,
int h)

Creates a

SampleModel

with the specified
width and height that has a data layout compatible with
this

ColorModel

.

WritableRaster

createCompatibleWritableRaster

​(int w,
int h)

Creates a

WritableRaster

with the specified width
and height that has a data layout (

SampleModel

)
compatible with this

ColorModel

.

boolean

equals

​(

Object

obj)

Tests if the specified

Object

is an
instance of

IndexColorModel

and if it equals this

IndexColorModel

void

finalize

()

Deprecated.

The

finalize

method has been deprecated.

int

getAlpha

​(int pixel)

Returns the alpha component for the specified pixel, scaled
from 0 to 255.

void

getAlphas

​(byte[] a)

Copies the array of alpha transparency components into the
specified array.

int

getBlue

​(int pixel)

Returns the blue color component for the specified pixel, scaled
from 0 to 255 in the default RGB ColorSpace, sRGB.

void

getBlues

​(byte[] b)

Copies the array of blue color components into the specified array.

int[]

getComponents

​(int pixel,
int[] components,
int offset)

Returns an array of unnormalized color/alpha components for a
specified pixel in this

ColorModel

.

int[]

getComponents

​(

Object

pixel,
int[] components,
int offset)

Returns an array of unnormalized color/alpha components for
a specified pixel in this

ColorModel

.

int[]

getComponentSize

()

Returns an array of the number of bits for each color/alpha component.

int

getDataElement

​(int[] components,
int offset)

Returns a pixel value represented as an int in this

ColorModel

given an array of unnormalized
color/alpha components.

Object

getDataElements

​(int[] components,
int offset,

Object

pixel)

Returns a data element array representation of a pixel in this

ColorModel

given an array of unnormalized color/alpha
components.

Object

getDataElements

​(int rgb,

Object

pixel)

Returns a data element array representation of a pixel in this
ColorModel, given an integer pixel representation in the
default RGB color model.

int

getGreen

​(int pixel)

Returns the green color component for the specified pixel, scaled
from 0 to 255 in the default RGB ColorSpace, sRGB.

void

getGreens

​(byte[] g)

Copies the array of green color components into the specified array.

int

getMapSize

()

Returns the size of the color/alpha component arrays in this

IndexColorModel

.

int

getRed

​(int pixel)

Returns the red color component for the specified pixel, scaled
from 0 to 255 in the default RGB ColorSpace, sRGB.

void

getReds

​(byte[] r)

Copies the array of red color components into the specified array.

int

getRGB

​(int pixel)

Returns the color/alpha components of the pixel in the default
RGB color model format.

void

getRGBs

​(int[] rgb)

Converts data for each index from the color and alpha component
arrays to an int in the default RGB ColorModel format and copies
the resulting 32-bit ARGB values into the specified array.

int

getTransparency

()

Returns the transparency.

int

getTransparentPixel

()

Returns the index of a transparent pixel in this

IndexColorModel

or -1 if there is no pixel
with an alpha value of 0.

BigInteger

getValidPixels

()

Returns a

BigInteger

that indicates the valid/invalid
pixels in the colormap.

int

hashCode

()

Returns the hash code for IndexColorModel.

boolean

isCompatibleRaster

​(

Raster

raster)

Returns

true

if

raster

is compatible
with this

ColorModel

or

false

if it
is not compatible with this

ColorModel

.

boolean

isCompatibleSampleModel

​(

SampleModel

sm)

Checks if the specified

SampleModel

is compatible
with this

ColorModel

.

boolean

isValid

()

Returns whether or not all of the pixels are valid.

boolean

isValid

​(int pixel)

Returns whether or not the pixel is valid.

String

toString

()

Returns the

String

representation of the contents of
this

ColorModel

object.

- Methods declared in class java.awt.image.

ColorModel

coerceData

,

getAlpha

,

getAlphaRaster

,

getBlue

,

getColorSpace

,

getComponentSize

,

getDataElement

,

getDataElements

,

getGreen

,

getNormalizedComponents

,

getNormalizedComponents

,

getNumColorComponents

,

getNumComponents

,

getPixelSize

,

getRed

,

getRGB

,

getRGBdefault

,

getTransferType

,

getUnnormalizedComponents

,

hasAlpha

,

isAlphaPremultiplied

- Methods declared in class java.lang.

Object

clone

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Method Summary

Returns a new

BufferedImage

of TYPE_INT_ARGB or
TYPE_INT_RGB that has a

Raster

with pixel data
computed by expanding the indices in the source

Raster

using the color/alpha component arrays of this

ColorModel

.

Creates a

SampleModel

with the specified
width and height that has a data layout compatible with
this

ColorModel

.

Creates a

WritableRaster

with the specified width
and height that has a data layout (

SampleModel

)
compatible with this

ColorModel

.

Tests if the specified

Object

is an
instance of

IndexColorModel

and if it equals this

IndexColorModel

Deprecated.

The

finalize

method has been deprecated.

Returns the alpha component for the specified pixel, scaled
from 0 to 255.

Copies the array of alpha transparency components into the
specified array.

Returns the blue color component for the specified pixel, scaled
from 0 to 255 in the default RGB ColorSpace, sRGB.

Copies the array of blue color components into the specified array.

Returns an array of unnormalized color/alpha components for a
specified pixel in this

ColorModel

.

Returns an array of unnormalized color/alpha components for
a specified pixel in this

ColorModel

.

Returns an array of the number of bits for each color/alpha component.

Returns a pixel value represented as an int in this

ColorModel

given an array of unnormalized
color/alpha components.

Returns a data element array representation of a pixel in this

ColorModel

given an array of unnormalized color/alpha
components.

Returns a data element array representation of a pixel in this
ColorModel, given an integer pixel representation in the
default RGB color model.

Returns the green color component for the specified pixel, scaled
from 0 to 255 in the default RGB ColorSpace, sRGB.

Copies the array of green color components into the specified array.

Returns the size of the color/alpha component arrays in this

IndexColorModel

.

Returns the red color component for the specified pixel, scaled
from 0 to 255 in the default RGB ColorSpace, sRGB.

Copies the array of red color components into the specified array.

Returns the color/alpha components of the pixel in the default
RGB color model format.

Converts data for each index from the color and alpha component
arrays to an int in the default RGB ColorModel format and copies
the resulting 32-bit ARGB values into the specified array.

Returns the transparency.

Returns the index of a transparent pixel in this

IndexColorModel

or -1 if there is no pixel
with an alpha value of 0.

Returns a

BigInteger

that indicates the valid/invalid
pixels in the colormap.

Returns the hash code for IndexColorModel.

Returns

true

if

raster

is compatible
with this

ColorModel

or

false

if it
is not compatible with this

ColorModel

.

Checks if the specified

SampleModel

is compatible
with this

ColorModel

.

Returns whether or not all of the pixels are valid.

Returns whether or not the pixel is valid.

Returns the

String

representation of the contents of
this

ColorModel

object.

Methods declared in class java.awt.image.

ColorModel

coerceData

,

getAlpha

,

getAlphaRaster

,

getBlue

,

getColorSpace

,

getComponentSize

,

getDataElement

,

getDataElements

,

getGreen

,

getNormalizedComponents

,

getNormalizedComponents

,

getNumColorComponents

,

getNumComponents

,

getPixelSize

,

getRed

,

getRGB

,

getRGBdefault

,

getTransferType

,

getUnnormalizedComponents

,

hasAlpha

,

isAlphaPremultiplied

---

#### Methods declared in class java.awt.image. ColorModel

Methods declared in class java.lang.

Object

clone

,

getClass

,

notify

,

notifyAll

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

- IndexColorModel

```java
public IndexColorModel​(int bits,
int size,
byte[] r,
byte[] g,
byte[] b)
```

Constructs an

IndexColorModel

from the specified
arrays of red, green, and blue components. Pixels described
by this color model all have alpha components of 255
unnormalized (1.0 normalized), which means they
are fully opaque. All of the arrays specifying the color
components must have at least the specified number of entries.
The

ColorSpace

is the default sRGB space.
Since there is no alpha information in any of the arguments
to this constructor, the transparency value is always

Transparency.OPAQUE

.
The transfer type is the smallest of

DataBuffer.TYPE_BYTE

or

DataBuffer.TYPE_USHORT

that can hold a single pixel.

**Parameters:** bits

- the number of bits each pixel occupies
**Parameters:** size

- the size of the color component arrays
**Parameters:** r

- the array of red color components
**Parameters:** g

- the array of green color components
**Parameters:** b

- the array of blue color components
**Throws:** IllegalArgumentException

- if

bits

is less
than 1 or greater than 16
**Throws:** IllegalArgumentException

- if

size

is less
than 1

- IndexColorModel

```java
public IndexColorModel​(int bits,
int size,
byte[] r,
byte[] g,
byte[] b,
int trans)
```

Constructs an

IndexColorModel

from the given arrays
of red, green, and blue components. Pixels described by this color
model all have alpha components of 255 unnormalized
(1.0 normalized), which means they are fully opaque, except
for the indicated pixel to be made transparent. All of the arrays
specifying the color components must have at least the specified
number of entries.
The

ColorSpace

is the default sRGB space.
The transparency value may be

Transparency.OPAQUE

or

Transparency.BITMASK

depending on the arguments, as
specified in the

class description

above.
The transfer type is the smallest of

DataBuffer.TYPE_BYTE

or

DataBuffer.TYPE_USHORT

that can hold a
single pixel.

**Parameters:** bits

- the number of bits each pixel occupies
**Parameters:** size

- the size of the color component arrays
**Parameters:** r

- the array of red color components
**Parameters:** g

- the array of green color components
**Parameters:** b

- the array of blue color components
**Parameters:** trans

- the index of the transparent pixel
**Throws:** IllegalArgumentException

- if

bits

is less than
1 or greater than 16
**Throws:** IllegalArgumentException

- if

size

is less than
1

- IndexColorModel

```java
public IndexColorModel​(int bits,
int size,
byte[] r,
byte[] g,
byte[] b,
byte[] a)
```

Constructs an

IndexColorModel

from the given
arrays of red, green, blue and alpha components. All of the
arrays specifying the components must have at least the specified
number of entries.
The

ColorSpace

is the default sRGB space.
The transparency value may be any of

Transparency.OPAQUE

,

Transparency.BITMASK

,
or

Transparency.TRANSLUCENT

depending on the arguments, as specified
in the

class description

above.
The transfer type is the smallest of

DataBuffer.TYPE_BYTE

or

DataBuffer.TYPE_USHORT

that can hold a single pixel.

**Parameters:** bits

- the number of bits each pixel occupies
**Parameters:** size

- the size of the color component arrays
**Parameters:** r

- the array of red color components
**Parameters:** g

- the array of green color components
**Parameters:** b

- the array of blue color components
**Parameters:** a

- the array of alpha value components
**Throws:** IllegalArgumentException

- if

bits

is less
than 1 or greater than 16
**Throws:** IllegalArgumentException

- if

size

is less
than 1

- IndexColorModel

```java
public IndexColorModel​(int bits,
int size,
byte[] cmap,
int start,
boolean hasalpha)
```

Constructs an

IndexColorModel

from a single
array of interleaved red, green, blue and optional alpha
components. The array must have enough values in it to
fill all of the needed component arrays of the specified
size. The

ColorSpace

is the default sRGB space.
The transparency value may be any of

Transparency.OPAQUE

,

Transparency.BITMASK

,
or

Transparency.TRANSLUCENT

depending on the arguments, as specified
in the

class description

above.
The transfer type is the smallest of

DataBuffer.TYPE_BYTE

or

DataBuffer.TYPE_USHORT

that can hold a single pixel.

**Parameters:** bits

- the number of bits each pixel occupies
**Parameters:** size

- the size of the color component arrays
**Parameters:** cmap

- the array of color components
**Parameters:** start

- the starting offset of the first color component
**Parameters:** hasalpha

- indicates whether alpha values are contained in
the

cmap

array
**Throws:** IllegalArgumentException

- if

bits

is less
than 1 or greater than 16
**Throws:** IllegalArgumentException

- if

size

is less
than 1

- IndexColorModel

```java
public IndexColorModel​(int bits,
int size,
byte[] cmap,
int start,
boolean hasalpha,
int trans)
```

Constructs an

IndexColorModel

from a single array of
interleaved red, green, blue and optional alpha components. The
specified transparent index represents a pixel that is made
entirely transparent regardless of any alpha value specified
for it. The array must have enough values in it to fill all
of the needed component arrays of the specified size.
The

ColorSpace

is the default sRGB space.
The transparency value may be any of

Transparency.OPAQUE

,

Transparency.BITMASK

,
or

Transparency.TRANSLUCENT

depending on the arguments, as specified
in the

class description

above.
The transfer type is the smallest of

DataBuffer.TYPE_BYTE

or

DataBuffer.TYPE_USHORT

that can hold a single pixel.

**Parameters:** bits

- the number of bits each pixel occupies
**Parameters:** size

- the size of the color component arrays
**Parameters:** cmap

- the array of color components
**Parameters:** start

- the starting offset of the first color component
**Parameters:** hasalpha

- indicates whether alpha values are contained in
the

cmap

array
**Parameters:** trans

- the index of the fully transparent pixel
**Throws:** IllegalArgumentException

- if

bits

is less than
1 or greater than 16
**Throws:** IllegalArgumentException

- if

size

is less than
1

- IndexColorModel

```java
public IndexColorModel​(int bits,
int size,
int[] cmap,
int start,
boolean hasalpha,
int trans,
int transferType)
```

Constructs an

IndexColorModel

from an array of
ints where each int is comprised of red, green, blue, and
optional alpha components in the default RGB color model format.
The specified transparent index represents a pixel that is made
entirely transparent regardless of any alpha value specified
for it. The array must have enough values in it to fill all
of the needed component arrays of the specified size.
The

ColorSpace

is the default sRGB space.
The transparency value may be any of

Transparency.OPAQUE

,

Transparency.BITMASK

,
or

Transparency.TRANSLUCENT

depending on the arguments, as specified
in the

class description

above.

**Parameters:** bits

- the number of bits each pixel occupies
**Parameters:** size

- the size of the color component arrays
**Parameters:** cmap

- the array of color components
**Parameters:** start

- the starting offset of the first color component
**Parameters:** hasalpha

- indicates whether alpha values are contained in
the

cmap

array
**Parameters:** trans

- the index of the fully transparent pixel
**Parameters:** transferType

- the data type of the array used to represent
pixel values. The data type must be either

DataBuffer.TYPE_BYTE

or

DataBuffer.TYPE_USHORT

.
**Throws:** IllegalArgumentException

- if

bits

is less
than 1 or greater than 16
**Throws:** IllegalArgumentException

- if

size

is less
than 1
**Throws:** IllegalArgumentException

- if

transferType

is not
one of

DataBuffer.TYPE_BYTE

or

DataBuffer.TYPE_USHORT

- IndexColorModel

```java
public IndexColorModel​(int bits,
int size,
int[] cmap,
int start,
int transferType,

BigInteger
validBits)
```

Constructs an

IndexColorModel

from an

int

array where each

int

is
comprised of red, green, blue, and alpha
components in the default RGB color model format.
The array must have enough values in it to fill all
of the needed component arrays of the specified size.
The

ColorSpace

is the default sRGB space.
The transparency value may be any of

Transparency.OPAQUE

,

Transparency.BITMASK

,
or

Transparency.TRANSLUCENT

depending on the arguments, as specified
in the

class description

above.
The transfer type must be one of

DataBuffer.TYPE_BYTE

DataBuffer.TYPE_USHORT

.
The

BigInteger

object specifies the valid/invalid pixels
in the

cmap

array. A pixel is valid if the

BigInteger

value at that index is set, and is invalid
if the

BigInteger

bit at that index is not set.

**Parameters:** bits

- the number of bits each pixel occupies
**Parameters:** size

- the size of the color component array
**Parameters:** cmap

- the array of color components
**Parameters:** start

- the starting offset of the first color component
**Parameters:** transferType

- the specified data type
**Parameters:** validBits

- a

BigInteger

object. If a bit is
set in the BigInteger, the pixel at that index is valid.
If a bit is not set, the pixel at that index
is considered invalid. If null, all pixels are valid.
Only bits from 0 to the map size are considered.
**Throws:** IllegalArgumentException

- if

bits

is less
than 1 or greater than 16
**Throws:** IllegalArgumentException

- if

size

is less
than 1
**Throws:** IllegalArgumentException

- if

transferType

is not
one of

DataBuffer.TYPE_BYTE

or

DataBuffer.TYPE_USHORT
**Since:** 1.3

============ METHOD DETAIL ==========

- Method Detail

- getTransparency

```java
public int getTransparency()
```

Returns the transparency. Returns either OPAQUE, BITMASK,
or TRANSLUCENT

**Specified by:** getTransparency

in interface

Transparency
**Overrides:** getTransparency

in class

ColorModel
**Returns:** the transparency of this

IndexColorModel
**See Also:** Transparency.OPAQUE

,

Transparency.BITMASK

,

Transparency.TRANSLUCENT

- getComponentSize

```java
public int[] getComponentSize()
```

Returns an array of the number of bits for each color/alpha component.
The array contains the color components in the order red, green,
blue, followed by the alpha component, if present.

**Overrides:** getComponentSize

in class

ColorModel
**Returns:** an array containing the number of bits of each color
and alpha component of this

IndexColorModel

- getMapSize

```java
public final int getMapSize()
```

Returns the size of the color/alpha component arrays in this

IndexColorModel

.

**Returns:** the size of the color and alpha component arrays.

- getTransparentPixel

```java
public final int getTransparentPixel()
```

Returns the index of a transparent pixel in this

IndexColorModel

or -1 if there is no pixel
with an alpha value of 0. If a transparent pixel was
explicitly specified in one of the constructors by its
index, then that index will be preferred, otherwise,
the index of any pixel which happens to be fully transparent
may be returned.

**Returns:** the index of a transparent pixel in this

IndexColorModel

object, or -1 if there
is no such pixel

- getReds

```java
public final void getReds​(byte[] r)
```

Copies the array of red color components into the specified array.
Only the initial entries of the array as specified by

getMapSize

are written.

**Parameters:** r

- the specified array into which the elements of the
array of red color components are copied

- getGreens

```java
public final void getGreens​(byte[] g)
```

Copies the array of green color components into the specified array.
Only the initial entries of the array as specified by

getMapSize

are written.

**Parameters:** g

- the specified array into which the elements of the
array of green color components are copied

- getBlues

```java
public final void getBlues​(byte[] b)
```

Copies the array of blue color components into the specified array.
Only the initial entries of the array as specified by

getMapSize

are written.

**Parameters:** b

- the specified array into which the elements of the
array of blue color components are copied

- getAlphas

```java
public final void getAlphas​(byte[] a)
```

Copies the array of alpha transparency components into the
specified array. Only the initial entries of the array as specified
by

getMapSize

are written.

**Parameters:** a

- the specified array into which the elements of the
array of alpha components are copied

- getRGBs

```java
public final void getRGBs​(int[] rgb)
```

Converts data for each index from the color and alpha component
arrays to an int in the default RGB ColorModel format and copies
the resulting 32-bit ARGB values into the specified array. Only
the initial entries of the array as specified by

getMapSize

are
written.

**Parameters:** rgb

- the specified array into which the converted ARGB
values from this array of color and alpha components
are copied.

- getRed

```java
public final int getRed​(int pixel)
```

Returns the red color component for the specified pixel, scaled
from 0 to 255 in the default RGB ColorSpace, sRGB. The pixel value
is specified as an int.
Only the lower

n

bits of the pixel value, as specified in the

class description

above, are used to
calculate the returned value.
The returned value is a non pre-multiplied value.

**Specified by:** getRed

in class

ColorModel
**Parameters:** pixel

- the specified pixel
**Returns:** the value of the red color component for the specified pixel

- getGreen

```java
public final int getGreen​(int pixel)
```

Returns the green color component for the specified pixel, scaled
from 0 to 255 in the default RGB ColorSpace, sRGB. The pixel value
is specified as an int.
Only the lower

n

bits of the pixel value, as specified in the

class description

above, are used to
calculate the returned value.
The returned value is a non pre-multiplied value.

**Specified by:** getGreen

in class

ColorModel
**Parameters:** pixel

- the specified pixel
**Returns:** the value of the green color component for the specified pixel

- getBlue

```java
public final int getBlue​(int pixel)
```

Returns the blue color component for the specified pixel, scaled
from 0 to 255 in the default RGB ColorSpace, sRGB. The pixel value
is specified as an int.
Only the lower

n

bits of the pixel value, as specified in the

class description

above, are used to
calculate the returned value.
The returned value is a non pre-multiplied value.

**Specified by:** getBlue

in class

ColorModel
**Parameters:** pixel

- the specified pixel
**Returns:** the value of the blue color component for the specified pixel

- getAlpha

```java
public final int getAlpha​(int pixel)
```

Returns the alpha component for the specified pixel, scaled
from 0 to 255. The pixel value is specified as an int.
Only the lower

n

bits of the pixel value, as specified in the

class description

above, are used to
calculate the returned value.

**Specified by:** getAlpha

in class

ColorModel
**Parameters:** pixel

- the specified pixel
**Returns:** the value of the alpha component for the specified pixel

- getRGB

```java
public final int getRGB​(int pixel)
```

Returns the color/alpha components of the pixel in the default
RGB color model format. The pixel value is specified as an int.
Only the lower

n

bits of the pixel value, as specified in the

class description

above, are used to
calculate the returned value.
The returned value is in a non pre-multiplied format.

**Overrides:** getRGB

in class

ColorModel
**Parameters:** pixel

- the specified pixel
**Returns:** the color and alpha components of the specified pixel
**See Also:** ColorModel.getRGBdefault()

- getDataElements

```java
public
Object
getDataElements​(int rgb,

Object
pixel)
```

Returns a data element array representation of a pixel in this
ColorModel, given an integer pixel representation in the
default RGB color model. This array can then be passed to the

setDataElements

method of a

WritableRaster

object. If the pixel variable is

null

, a new array is allocated. If

pixel

is not

null

, it must be
a primitive array of type

transferType

; otherwise, a

ClassCastException

is thrown. An

ArrayIndexOutOfBoundsException

is
thrown if

pixel

is not large enough to hold a pixel
value for this

ColorModel

. The pixel array is returned.

Since

IndexColorModel

can be subclassed, subclasses
inherit the implementation of this method and if they don't
override it then they throw an exception if they use an
unsupported

transferType

.

**Overrides:** getDataElements

in class

ColorModel
**Parameters:** rgb

- the integer pixel representation in the default RGB
color model
**Parameters:** pixel

- the specified pixel
**Returns:** an array representation of the specified pixel in this

IndexColorModel

.
**Throws:** ClassCastException

- if

pixel

is not a primitive array of type

transferType
**Throws:** ArrayIndexOutOfBoundsException

- if

pixel

is not large enough to hold a pixel value
for this

ColorModel
**Throws:** UnsupportedOperationException

- if

transferType

is invalid
**See Also:** WritableRaster.setDataElements(int, int, java.lang.Object)

,

SampleModel.setDataElements(int, int, java.lang.Object, java.awt.image.DataBuffer)

- getComponents

```java
public int[] getComponents​(int pixel,
int[] components,
int offset)
```

Returns an array of unnormalized color/alpha components for a
specified pixel in this

ColorModel

. The pixel value
is specified as an int. If the

components

array is

null

,
a new array is allocated that contains

offset + getNumComponents()

elements.
The

components

array is returned,
with the alpha component included
only if

hasAlpha

returns true.
Color/alpha components are stored in the

components

array starting
at

offset

even if the array is allocated by this method.
An

ArrayIndexOutOfBoundsException

is thrown if the

components

array is not

null

and is
not large enough to hold all the color and alpha components
starting at

offset

.

**Overrides:** getComponents

in class

ColorModel
**Parameters:** pixel

- the specified pixel
**Parameters:** components

- the array to receive the color and alpha
components of the specified pixel
**Parameters:** offset

- the offset into the

components

array at
which to start storing the color and alpha components
**Returns:** an array containing the color and alpha components of the
specified pixel starting at the specified offset.
**See Also:** ColorModel.hasAlpha()

,

ColorModel.getNumComponents()

- getComponents

```java
public int[] getComponents​(
Object
pixel,
int[] components,
int offset)
```

Returns an array of unnormalized color/alpha components for
a specified pixel in this

ColorModel

. The pixel
value is specified by an array of data elements of type

transferType

passed in as an object reference.
If

pixel

is not a primitive array of type

transferType

, a

ClassCastException

is thrown. An

ArrayIndexOutOfBoundsException

is thrown if

pixel

is not large enough to hold
a pixel value for this

ColorModel

. If the

components

array is

null

, a new array
is allocated that contains

offset + getNumComponents()

elements.
The

components

array is returned,
with the alpha component included
only if

hasAlpha

returns true.
Color/alpha components are stored in the

components

array starting at

offset

even if the array is
allocated by this method. An

ArrayIndexOutOfBoundsException

is also
thrown if the

components

array is not

null

and is not large enough to hold all the color
and alpha components starting at

offset

.

Since

IndexColorModel

can be subclassed, subclasses
inherit the implementation of this method and if they don't
override it then they throw an exception if they use an
unsupported

transferType

.

**Overrides:** getComponents

in class

ColorModel
**Parameters:** pixel

- the specified pixel
**Parameters:** components

- an array that receives the color and alpha
components of the specified pixel
**Parameters:** offset

- the index into the

components

array at
which to begin storing the color and alpha components of the
specified pixel
**Returns:** an array containing the color and alpha components of the
specified pixel starting at the specified offset.
**Throws:** ArrayIndexOutOfBoundsException

- if

pixel

is not large enough to hold a pixel value for this

ColorModel

or if the

components

array is not

null

and is not large enough to hold all the color
and alpha components starting at

offset
**Throws:** ClassCastException

- if

pixel

is not a
primitive array of type

transferType
**Throws:** UnsupportedOperationException

- if

transferType

is not one of the supported transfer types
**See Also:** ColorModel.hasAlpha()

,

ColorModel.getNumComponents()

- getDataElement

```java
public int getDataElement​(int[] components,
int offset)
```

Returns a pixel value represented as an int in this

ColorModel

given an array of unnormalized
color/alpha components. An

ArrayIndexOutOfBoundsException

is thrown if the

components

array is not large
enough to hold all of the color and alpha components starting
at

offset

. Since

ColorModel

can be subclassed, subclasses inherit the
implementation of this method and if they don't override it then
they throw an exception if they use an unsupported transferType.

**Overrides:** getDataElement

in class

ColorModel
**Parameters:** components

- an array of unnormalized color and alpha
components
**Parameters:** offset

- the index into

components

at which to
begin retrieving the color and alpha components
**Returns:** an

int

pixel value in this

ColorModel

corresponding to the specified components.
**Throws:** ArrayIndexOutOfBoundsException

- if
the

components

array is not large enough to
hold all of the color and alpha components starting at

offset
**Throws:** UnsupportedOperationException

- if

transferType

is invalid

- getDataElements

```java
public
Object
getDataElements​(int[] components,
int offset,

Object
pixel)
```

Returns a data element array representation of a pixel in this

ColorModel

given an array of unnormalized color/alpha
components. This array can then be passed to the

setDataElements

method of a

WritableRaster

object. An

ArrayIndexOutOfBoundsException

is
thrown if the

components

array is not large enough to hold all of the
color and alpha components starting at

offset

.
If the pixel variable is

null

, a new array
is allocated. If

pixel

is not

null

,
it must be a primitive array of type

transferType

;
otherwise, a

ClassCastException

is thrown.
An

ArrayIndexOutOfBoundsException

is thrown if pixel
is not large enough to hold a pixel value for this

ColorModel

.

Since

IndexColorModel

can be subclassed, subclasses
inherit the implementation of this method and if they don't
override it then they throw an exception if they use an
unsupported

transferType

**Overrides:** getDataElements

in class

ColorModel
**Parameters:** components

- an array of unnormalized color and alpha
components
**Parameters:** offset

- the index into

components

at which to
begin retrieving color and alpha components
**Parameters:** pixel

- the

Object

representing an array of color
and alpha components
**Returns:** an

Object

representing an array of color and
alpha components.
**Throws:** ClassCastException

- if

pixel

is not a primitive array of type

transferType
**Throws:** ArrayIndexOutOfBoundsException

- if

pixel

is not large enough to hold a pixel value
for this

ColorModel

or the

components

array is not large enough to hold all of the color and alpha
components starting at

offset
**Throws:** UnsupportedOperationException

- if

transferType

is not one of the supported transfer types
**See Also:** WritableRaster.setDataElements(int, int, java.lang.Object)

,

SampleModel.setDataElements(int, int, java.lang.Object, java.awt.image.DataBuffer)

- createCompatibleWritableRaster

```java
public
WritableRaster
createCompatibleWritableRaster​(int w,
int h)
```

Creates a

WritableRaster

with the specified width
and height that has a data layout (

SampleModel

)
compatible with this

ColorModel

. This method
only works for color models with 16 or fewer bits per pixel.

Since

IndexColorModel

can be subclassed, any
subclass that supports greater than 16 bits per pixel must
override this method.

**Overrides:** createCompatibleWritableRaster

in class

ColorModel
**Parameters:** w

- the width to apply to the new

WritableRaster
**Parameters:** h

- the height to apply to the new

WritableRaster
**Returns:** a

WritableRaster

object with the specified
width and height.
**Throws:** UnsupportedOperationException

- if the number of bits in a
pixel is greater than 16
**See Also:** WritableRaster

,

SampleModel

- isCompatibleRaster

```java
public boolean isCompatibleRaster​(
Raster
raster)
```

Returns

true

if

raster

is compatible
with this

ColorModel

or

false

if it
is not compatible with this

ColorModel

.

**Overrides:** isCompatibleRaster

in class

ColorModel
**Parameters:** raster

- the

Raster

object to test for compatibility
**Returns:** true

if

raster

is compatible
with this

ColorModel

;

false

otherwise.

- createCompatibleSampleModel

```java
public
SampleModel
createCompatibleSampleModel​(int w,
int h)
```

Creates a

SampleModel

with the specified
width and height that has a data layout compatible with
this

ColorModel

.

**Overrides:** createCompatibleSampleModel

in class

ColorModel
**Parameters:** w

- the width to apply to the new

SampleModel
**Parameters:** h

- the height to apply to the new

SampleModel
**Returns:** a

SampleModel

object with the specified
width and height.
**Throws:** IllegalArgumentException

- if

w

or

h

is not greater than 0
**See Also:** SampleModel

- isCompatibleSampleModel

```java
public boolean isCompatibleSampleModel​(
SampleModel
sm)
```

Checks if the specified

SampleModel

is compatible
with this

ColorModel

. If

sm

is

null

, this method returns

false

.

**Overrides:** isCompatibleSampleModel

in class

ColorModel
**Parameters:** sm

- the specified

SampleModel

,
or

null
**Returns:** true

if the specified

SampleModel

is compatible with this

ColorModel

;

false

otherwise.
**See Also:** SampleModel

- convertToIntDiscrete

```java
public
BufferedImage
convertToIntDiscrete​(
Raster
raster,
boolean forceARGB)
```

Returns a new

BufferedImage

of TYPE_INT_ARGB or
TYPE_INT_RGB that has a

Raster

with pixel data
computed by expanding the indices in the source

Raster

using the color/alpha component arrays of this

ColorModel

.
Only the lower

n

bits of each index value in the source

Raster

, as specified in the

class description

above, are used to
compute the color/alpha values in the returned image.
If

forceARGB

is

true

, a TYPE_INT_ARGB image is
returned regardless of whether or not this

ColorModel

has an alpha component array or a transparent pixel.

**Parameters:** raster

- the specified

Raster
**Parameters:** forceARGB

- if

true

, the returned

BufferedImage

is TYPE_INT_ARGB; otherwise it is
TYPE_INT_RGB
**Returns:** a

BufferedImage

created with the specified

Raster
**Throws:** IllegalArgumentException

- if the raster argument is not
compatible with this IndexColorModel

- isValid

```java
public boolean isValid​(int pixel)
```

Returns whether or not the pixel is valid.

**Parameters:** pixel

- the specified pixel value
**Returns:** true

if

pixel

is valid;

false

otherwise.
**Since:** 1.3

- isValid

```java
public boolean isValid()
```

Returns whether or not all of the pixels are valid.

**Returns:** true

if all pixels are valid;

false

otherwise.
**Since:** 1.3

- getValidPixels

```java
public
BigInteger
getValidPixels()
```

Returns a

BigInteger

that indicates the valid/invalid
pixels in the colormap. A bit is valid if the

BigInteger

value at that index is set, and is invalid
if the

BigInteger

value at that index is not set.
The only valid ranges to query in the

BigInteger

are
between 0 and the map size.

**Returns:** a

BigInteger

indicating the valid/invalid pixels.
**Since:** 1.3

- finalize

```java
@Deprecated
(
since
="9")
public void finalize()
```

Deprecated.

The

finalize

method has been deprecated.
Subclasses that override

finalize

in order to perform cleanup
should be modified to use alternative cleanup mechanisms and
to remove the overriding

finalize

method.
When overriding the

finalize

method, its implementation must explicitly
ensure that

super.finalize()

is invoked as described in

Object.finalize()

.
See the specification for

Object.finalize()

for further
information about migration options.

Disposes of system resources associated with this

ColorModel

once this

ColorModel

is no
longer referenced.

**Overrides:** finalize

in class

ColorModel
**See Also:** WeakReference

,

PhantomReference

- toString

```java
public
String
toString()
```

Returns the

String

representation of the contents of
this

ColorModel

object.

**Overrides:** toString

in class

ColorModel
**Returns:** a

String

representing the contents of this

ColorModel

object.

- equals

```java
public boolean equals​(
Object
obj)
```

Tests if the specified

Object

is an
instance of

IndexColorModel

and if it equals this

IndexColorModel

**Overrides:** equals

in class

ColorModel
**Parameters:** obj

- the

Object

to test for equality
**Returns:** true

if the specified

Object

equals this

IndexColorModel

;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code for IndexColorModel.

**Overrides:** hashCode

in class

ColorModel
**Returns:** a hash code for IndexColorModel
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

Constructor Detail

- IndexColorModel

```java
public IndexColorModel​(int bits,
int size,
byte[] r,
byte[] g,
byte[] b)
```

Constructs an

IndexColorModel

from the specified
arrays of red, green, and blue components. Pixels described
by this color model all have alpha components of 255
unnormalized (1.0 normalized), which means they
are fully opaque. All of the arrays specifying the color
components must have at least the specified number of entries.
The

ColorSpace

is the default sRGB space.
Since there is no alpha information in any of the arguments
to this constructor, the transparency value is always

Transparency.OPAQUE

.
The transfer type is the smallest of

DataBuffer.TYPE_BYTE

or

DataBuffer.TYPE_USHORT

that can hold a single pixel.

**Parameters:** bits

- the number of bits each pixel occupies
**Parameters:** size

- the size of the color component arrays
**Parameters:** r

- the array of red color components
**Parameters:** g

- the array of green color components
**Parameters:** b

- the array of blue color components
**Throws:** IllegalArgumentException

- if

bits

is less
than 1 or greater than 16
**Throws:** IllegalArgumentException

- if

size

is less
than 1

- IndexColorModel

```java
public IndexColorModel​(int bits,
int size,
byte[] r,
byte[] g,
byte[] b,
int trans)
```

Constructs an

IndexColorModel

from the given arrays
of red, green, and blue components. Pixels described by this color
model all have alpha components of 255 unnormalized
(1.0 normalized), which means they are fully opaque, except
for the indicated pixel to be made transparent. All of the arrays
specifying the color components must have at least the specified
number of entries.
The

ColorSpace

is the default sRGB space.
The transparency value may be

Transparency.OPAQUE

or

Transparency.BITMASK

depending on the arguments, as
specified in the

class description

above.
The transfer type is the smallest of

DataBuffer.TYPE_BYTE

or

DataBuffer.TYPE_USHORT

that can hold a
single pixel.

**Parameters:** bits

- the number of bits each pixel occupies
**Parameters:** size

- the size of the color component arrays
**Parameters:** r

- the array of red color components
**Parameters:** g

- the array of green color components
**Parameters:** b

- the array of blue color components
**Parameters:** trans

- the index of the transparent pixel
**Throws:** IllegalArgumentException

- if

bits

is less than
1 or greater than 16
**Throws:** IllegalArgumentException

- if

size

is less than
1

- IndexColorModel

```java
public IndexColorModel​(int bits,
int size,
byte[] r,
byte[] g,
byte[] b,
byte[] a)
```

Constructs an

IndexColorModel

from the given
arrays of red, green, blue and alpha components. All of the
arrays specifying the components must have at least the specified
number of entries.
The

ColorSpace

is the default sRGB space.
The transparency value may be any of

Transparency.OPAQUE

,

Transparency.BITMASK

,
or

Transparency.TRANSLUCENT

depending on the arguments, as specified
in the

class description

above.
The transfer type is the smallest of

DataBuffer.TYPE_BYTE

or

DataBuffer.TYPE_USHORT

that can hold a single pixel.

**Parameters:** bits

- the number of bits each pixel occupies
**Parameters:** size

- the size of the color component arrays
**Parameters:** r

- the array of red color components
**Parameters:** g

- the array of green color components
**Parameters:** b

- the array of blue color components
**Parameters:** a

- the array of alpha value components
**Throws:** IllegalArgumentException

- if

bits

is less
than 1 or greater than 16
**Throws:** IllegalArgumentException

- if

size

is less
than 1

- IndexColorModel

```java
public IndexColorModel​(int bits,
int size,
byte[] cmap,
int start,
boolean hasalpha)
```

Constructs an

IndexColorModel

from a single
array of interleaved red, green, blue and optional alpha
components. The array must have enough values in it to
fill all of the needed component arrays of the specified
size. The

ColorSpace

is the default sRGB space.
The transparency value may be any of

Transparency.OPAQUE

,

Transparency.BITMASK

,
or

Transparency.TRANSLUCENT

depending on the arguments, as specified
in the

class description

above.
The transfer type is the smallest of

DataBuffer.TYPE_BYTE

or

DataBuffer.TYPE_USHORT

that can hold a single pixel.

**Parameters:** bits

- the number of bits each pixel occupies
**Parameters:** size

- the size of the color component arrays
**Parameters:** cmap

- the array of color components
**Parameters:** start

- the starting offset of the first color component
**Parameters:** hasalpha

- indicates whether alpha values are contained in
the

cmap

array
**Throws:** IllegalArgumentException

- if

bits

is less
than 1 or greater than 16
**Throws:** IllegalArgumentException

- if

size

is less
than 1

- IndexColorModel

```java
public IndexColorModel​(int bits,
int size,
byte[] cmap,
int start,
boolean hasalpha,
int trans)
```

Constructs an

IndexColorModel

from a single array of
interleaved red, green, blue and optional alpha components. The
specified transparent index represents a pixel that is made
entirely transparent regardless of any alpha value specified
for it. The array must have enough values in it to fill all
of the needed component arrays of the specified size.
The

ColorSpace

is the default sRGB space.
The transparency value may be any of

Transparency.OPAQUE

,

Transparency.BITMASK

,
or

Transparency.TRANSLUCENT

depending on the arguments, as specified
in the

class description

above.
The transfer type is the smallest of

DataBuffer.TYPE_BYTE

or

DataBuffer.TYPE_USHORT

that can hold a single pixel.

**Parameters:** bits

- the number of bits each pixel occupies
**Parameters:** size

- the size of the color component arrays
**Parameters:** cmap

- the array of color components
**Parameters:** start

- the starting offset of the first color component
**Parameters:** hasalpha

- indicates whether alpha values are contained in
the

cmap

array
**Parameters:** trans

- the index of the fully transparent pixel
**Throws:** IllegalArgumentException

- if

bits

is less than
1 or greater than 16
**Throws:** IllegalArgumentException

- if

size

is less than
1

- IndexColorModel

```java
public IndexColorModel​(int bits,
int size,
int[] cmap,
int start,
boolean hasalpha,
int trans,
int transferType)
```

Constructs an

IndexColorModel

from an array of
ints where each int is comprised of red, green, blue, and
optional alpha components in the default RGB color model format.
The specified transparent index represents a pixel that is made
entirely transparent regardless of any alpha value specified
for it. The array must have enough values in it to fill all
of the needed component arrays of the specified size.
The

ColorSpace

is the default sRGB space.
The transparency value may be any of

Transparency.OPAQUE

,

Transparency.BITMASK

,
or

Transparency.TRANSLUCENT

depending on the arguments, as specified
in the

class description

above.

**Parameters:** bits

- the number of bits each pixel occupies
**Parameters:** size

- the size of the color component arrays
**Parameters:** cmap

- the array of color components
**Parameters:** start

- the starting offset of the first color component
**Parameters:** hasalpha

- indicates whether alpha values are contained in
the

cmap

array
**Parameters:** trans

- the index of the fully transparent pixel
**Parameters:** transferType

- the data type of the array used to represent
pixel values. The data type must be either

DataBuffer.TYPE_BYTE

or

DataBuffer.TYPE_USHORT

.
**Throws:** IllegalArgumentException

- if

bits

is less
than 1 or greater than 16
**Throws:** IllegalArgumentException

- if

size

is less
than 1
**Throws:** IllegalArgumentException

- if

transferType

is not
one of

DataBuffer.TYPE_BYTE

or

DataBuffer.TYPE_USHORT

- IndexColorModel

```java
public IndexColorModel​(int bits,
int size,
int[] cmap,
int start,
int transferType,

BigInteger
validBits)
```

Constructs an

IndexColorModel

from an

int

array where each

int

is
comprised of red, green, blue, and alpha
components in the default RGB color model format.
The array must have enough values in it to fill all
of the needed component arrays of the specified size.
The

ColorSpace

is the default sRGB space.
The transparency value may be any of

Transparency.OPAQUE

,

Transparency.BITMASK

,
or

Transparency.TRANSLUCENT

depending on the arguments, as specified
in the

class description

above.
The transfer type must be one of

DataBuffer.TYPE_BYTE

DataBuffer.TYPE_USHORT

.
The

BigInteger

object specifies the valid/invalid pixels
in the

cmap

array. A pixel is valid if the

BigInteger

value at that index is set, and is invalid
if the

BigInteger

bit at that index is not set.

**Parameters:** bits

- the number of bits each pixel occupies
**Parameters:** size

- the size of the color component array
**Parameters:** cmap

- the array of color components
**Parameters:** start

- the starting offset of the first color component
**Parameters:** transferType

- the specified data type
**Parameters:** validBits

- a

BigInteger

object. If a bit is
set in the BigInteger, the pixel at that index is valid.
If a bit is not set, the pixel at that index
is considered invalid. If null, all pixels are valid.
Only bits from 0 to the map size are considered.
**Throws:** IllegalArgumentException

- if

bits

is less
than 1 or greater than 16
**Throws:** IllegalArgumentException

- if

size

is less
than 1
**Throws:** IllegalArgumentException

- if

transferType

is not
one of

DataBuffer.TYPE_BYTE

or

DataBuffer.TYPE_USHORT
**Since:** 1.3

---

#### Constructor Detail

IndexColorModel

```java
public IndexColorModel​(int bits,
int size,
byte[] r,
byte[] g,
byte[] b)
```

Constructs an

IndexColorModel

from the specified
arrays of red, green, and blue components. Pixels described
by this color model all have alpha components of 255
unnormalized (1.0 normalized), which means they
are fully opaque. All of the arrays specifying the color
components must have at least the specified number of entries.
The

ColorSpace

is the default sRGB space.
Since there is no alpha information in any of the arguments
to this constructor, the transparency value is always

Transparency.OPAQUE

.
The transfer type is the smallest of

DataBuffer.TYPE_BYTE

or

DataBuffer.TYPE_USHORT

that can hold a single pixel.

**Parameters:** bits

- the number of bits each pixel occupies
**Parameters:** size

- the size of the color component arrays
**Parameters:** r

- the array of red color components
**Parameters:** g

- the array of green color components
**Parameters:** b

- the array of blue color components
**Throws:** IllegalArgumentException

- if

bits

is less
than 1 or greater than 16
**Throws:** IllegalArgumentException

- if

size

is less
than 1

---

#### IndexColorModel

public IndexColorModel​(int bits,
int size,
byte[] r,
byte[] g,
byte[] b)

Constructs an

IndexColorModel

from the specified
arrays of red, green, and blue components. Pixels described
by this color model all have alpha components of 255
unnormalized (1.0 normalized), which means they
are fully opaque. All of the arrays specifying the color
components must have at least the specified number of entries.
The

ColorSpace

is the default sRGB space.
Since there is no alpha information in any of the arguments
to this constructor, the transparency value is always

Transparency.OPAQUE

.
The transfer type is the smallest of

DataBuffer.TYPE_BYTE

or

DataBuffer.TYPE_USHORT

that can hold a single pixel.

IndexColorModel

```java
public IndexColorModel​(int bits,
int size,
byte[] r,
byte[] g,
byte[] b,
int trans)
```

Constructs an

IndexColorModel

from the given arrays
of red, green, and blue components. Pixels described by this color
model all have alpha components of 255 unnormalized
(1.0 normalized), which means they are fully opaque, except
for the indicated pixel to be made transparent. All of the arrays
specifying the color components must have at least the specified
number of entries.
The

ColorSpace

is the default sRGB space.
The transparency value may be

Transparency.OPAQUE

or

Transparency.BITMASK

depending on the arguments, as
specified in the

class description

above.
The transfer type is the smallest of

DataBuffer.TYPE_BYTE

or

DataBuffer.TYPE_USHORT

that can hold a
single pixel.

**Parameters:** bits

- the number of bits each pixel occupies
**Parameters:** size

- the size of the color component arrays
**Parameters:** r

- the array of red color components
**Parameters:** g

- the array of green color components
**Parameters:** b

- the array of blue color components
**Parameters:** trans

- the index of the transparent pixel
**Throws:** IllegalArgumentException

- if

bits

is less than
1 or greater than 16
**Throws:** IllegalArgumentException

- if

size

is less than
1

---

#### IndexColorModel

public IndexColorModel​(int bits,
int size,
byte[] r,
byte[] g,
byte[] b,
int trans)

Constructs an

IndexColorModel

from the given arrays
of red, green, and blue components. Pixels described by this color
model all have alpha components of 255 unnormalized
(1.0 normalized), which means they are fully opaque, except
for the indicated pixel to be made transparent. All of the arrays
specifying the color components must have at least the specified
number of entries.
The

ColorSpace

is the default sRGB space.
The transparency value may be

Transparency.OPAQUE

or

Transparency.BITMASK

depending on the arguments, as
specified in the

class description

above.
The transfer type is the smallest of

DataBuffer.TYPE_BYTE

or

DataBuffer.TYPE_USHORT

that can hold a
single pixel.

IndexColorModel

```java
public IndexColorModel​(int bits,
int size,
byte[] r,
byte[] g,
byte[] b,
byte[] a)
```

Constructs an

IndexColorModel

from the given
arrays of red, green, blue and alpha components. All of the
arrays specifying the components must have at least the specified
number of entries.
The

ColorSpace

is the default sRGB space.
The transparency value may be any of

Transparency.OPAQUE

,

Transparency.BITMASK

,
or

Transparency.TRANSLUCENT

depending on the arguments, as specified
in the

class description

above.
The transfer type is the smallest of

DataBuffer.TYPE_BYTE

or

DataBuffer.TYPE_USHORT

that can hold a single pixel.

**Parameters:** bits

- the number of bits each pixel occupies
**Parameters:** size

- the size of the color component arrays
**Parameters:** r

- the array of red color components
**Parameters:** g

- the array of green color components
**Parameters:** b

- the array of blue color components
**Parameters:** a

- the array of alpha value components
**Throws:** IllegalArgumentException

- if

bits

is less
than 1 or greater than 16
**Throws:** IllegalArgumentException

- if

size

is less
than 1

---

#### IndexColorModel

public IndexColorModel​(int bits,
int size,
byte[] r,
byte[] g,
byte[] b,
byte[] a)

Constructs an

IndexColorModel

from the given
arrays of red, green, blue and alpha components. All of the
arrays specifying the components must have at least the specified
number of entries.
The

ColorSpace

is the default sRGB space.
The transparency value may be any of

Transparency.OPAQUE

,

Transparency.BITMASK

,
or

Transparency.TRANSLUCENT

depending on the arguments, as specified
in the

class description

above.
The transfer type is the smallest of

DataBuffer.TYPE_BYTE

or

DataBuffer.TYPE_USHORT

that can hold a single pixel.

IndexColorModel

```java
public IndexColorModel​(int bits,
int size,
byte[] cmap,
int start,
boolean hasalpha)
```

Constructs an

IndexColorModel

from a single
array of interleaved red, green, blue and optional alpha
components. The array must have enough values in it to
fill all of the needed component arrays of the specified
size. The

ColorSpace

is the default sRGB space.
The transparency value may be any of

Transparency.OPAQUE

,

Transparency.BITMASK

,
or

Transparency.TRANSLUCENT

depending on the arguments, as specified
in the

class description

above.
The transfer type is the smallest of

DataBuffer.TYPE_BYTE

or

DataBuffer.TYPE_USHORT

that can hold a single pixel.

**Parameters:** bits

- the number of bits each pixel occupies
**Parameters:** size

- the size of the color component arrays
**Parameters:** cmap

- the array of color components
**Parameters:** start

- the starting offset of the first color component
**Parameters:** hasalpha

- indicates whether alpha values are contained in
the

cmap

array
**Throws:** IllegalArgumentException

- if

bits

is less
than 1 or greater than 16
**Throws:** IllegalArgumentException

- if

size

is less
than 1

---

#### IndexColorModel

public IndexColorModel​(int bits,
int size,
byte[] cmap,
int start,
boolean hasalpha)

Constructs an

IndexColorModel

from a single
array of interleaved red, green, blue and optional alpha
components. The array must have enough values in it to
fill all of the needed component arrays of the specified
size. The

ColorSpace

is the default sRGB space.
The transparency value may be any of

Transparency.OPAQUE

,

Transparency.BITMASK

,
or

Transparency.TRANSLUCENT

depending on the arguments, as specified
in the

class description

above.
The transfer type is the smallest of

DataBuffer.TYPE_BYTE

or

DataBuffer.TYPE_USHORT

that can hold a single pixel.

IndexColorModel

```java
public IndexColorModel​(int bits,
int size,
byte[] cmap,
int start,
boolean hasalpha,
int trans)
```

Constructs an

IndexColorModel

from a single array of
interleaved red, green, blue and optional alpha components. The
specified transparent index represents a pixel that is made
entirely transparent regardless of any alpha value specified
for it. The array must have enough values in it to fill all
of the needed component arrays of the specified size.
The

ColorSpace

is the default sRGB space.
The transparency value may be any of

Transparency.OPAQUE

,

Transparency.BITMASK

,
or

Transparency.TRANSLUCENT

depending on the arguments, as specified
in the

class description

above.
The transfer type is the smallest of

DataBuffer.TYPE_BYTE

or

DataBuffer.TYPE_USHORT

that can hold a single pixel.

**Parameters:** bits

- the number of bits each pixel occupies
**Parameters:** size

- the size of the color component arrays
**Parameters:** cmap

- the array of color components
**Parameters:** start

- the starting offset of the first color component
**Parameters:** hasalpha

- indicates whether alpha values are contained in
the

cmap

array
**Parameters:** trans

- the index of the fully transparent pixel
**Throws:** IllegalArgumentException

- if

bits

is less than
1 or greater than 16
**Throws:** IllegalArgumentException

- if

size

is less than
1

---

#### IndexColorModel

public IndexColorModel​(int bits,
int size,
byte[] cmap,
int start,
boolean hasalpha,
int trans)

Constructs an

IndexColorModel

from a single array of
interleaved red, green, blue and optional alpha components. The
specified transparent index represents a pixel that is made
entirely transparent regardless of any alpha value specified
for it. The array must have enough values in it to fill all
of the needed component arrays of the specified size.
The

ColorSpace

is the default sRGB space.
The transparency value may be any of

Transparency.OPAQUE

,

Transparency.BITMASK

,
or

Transparency.TRANSLUCENT

depending on the arguments, as specified
in the

class description

above.
The transfer type is the smallest of

DataBuffer.TYPE_BYTE

or

DataBuffer.TYPE_USHORT

that can hold a single pixel.

IndexColorModel

```java
public IndexColorModel​(int bits,
int size,
int[] cmap,
int start,
boolean hasalpha,
int trans,
int transferType)
```

Constructs an

IndexColorModel

from an array of
ints where each int is comprised of red, green, blue, and
optional alpha components in the default RGB color model format.
The specified transparent index represents a pixel that is made
entirely transparent regardless of any alpha value specified
for it. The array must have enough values in it to fill all
of the needed component arrays of the specified size.
The

ColorSpace

is the default sRGB space.
The transparency value may be any of

Transparency.OPAQUE

,

Transparency.BITMASK

,
or

Transparency.TRANSLUCENT

depending on the arguments, as specified
in the

class description

above.

**Parameters:** bits

- the number of bits each pixel occupies
**Parameters:** size

- the size of the color component arrays
**Parameters:** cmap

- the array of color components
**Parameters:** start

- the starting offset of the first color component
**Parameters:** hasalpha

- indicates whether alpha values are contained in
the

cmap

array
**Parameters:** trans

- the index of the fully transparent pixel
**Parameters:** transferType

- the data type of the array used to represent
pixel values. The data type must be either

DataBuffer.TYPE_BYTE

or

DataBuffer.TYPE_USHORT

.
**Throws:** IllegalArgumentException

- if

bits

is less
than 1 or greater than 16
**Throws:** IllegalArgumentException

- if

size

is less
than 1
**Throws:** IllegalArgumentException

- if

transferType

is not
one of

DataBuffer.TYPE_BYTE

or

DataBuffer.TYPE_USHORT

---

#### IndexColorModel

public IndexColorModel​(int bits,
int size,
int[] cmap,
int start,
boolean hasalpha,
int trans,
int transferType)

Constructs an

IndexColorModel

from an array of
ints where each int is comprised of red, green, blue, and
optional alpha components in the default RGB color model format.
The specified transparent index represents a pixel that is made
entirely transparent regardless of any alpha value specified
for it. The array must have enough values in it to fill all
of the needed component arrays of the specified size.
The

ColorSpace

is the default sRGB space.
The transparency value may be any of

Transparency.OPAQUE

,

Transparency.BITMASK

,
or

Transparency.TRANSLUCENT

depending on the arguments, as specified
in the

class description

above.

IndexColorModel

```java
public IndexColorModel​(int bits,
int size,
int[] cmap,
int start,
int transferType,

BigInteger
validBits)
```

Constructs an

IndexColorModel

from an

int

array where each

int

is
comprised of red, green, blue, and alpha
components in the default RGB color model format.
The array must have enough values in it to fill all
of the needed component arrays of the specified size.
The

ColorSpace

is the default sRGB space.
The transparency value may be any of

Transparency.OPAQUE

,

Transparency.BITMASK

,
or

Transparency.TRANSLUCENT

depending on the arguments, as specified
in the

class description

above.
The transfer type must be one of

DataBuffer.TYPE_BYTE

DataBuffer.TYPE_USHORT

.
The

BigInteger

object specifies the valid/invalid pixels
in the

cmap

array. A pixel is valid if the

BigInteger

value at that index is set, and is invalid
if the

BigInteger

bit at that index is not set.

**Parameters:** bits

- the number of bits each pixel occupies
**Parameters:** size

- the size of the color component array
**Parameters:** cmap

- the array of color components
**Parameters:** start

- the starting offset of the first color component
**Parameters:** transferType

- the specified data type
**Parameters:** validBits

- a

BigInteger

object. If a bit is
set in the BigInteger, the pixel at that index is valid.
If a bit is not set, the pixel at that index
is considered invalid. If null, all pixels are valid.
Only bits from 0 to the map size are considered.
**Throws:** IllegalArgumentException

- if

bits

is less
than 1 or greater than 16
**Throws:** IllegalArgumentException

- if

size

is less
than 1
**Throws:** IllegalArgumentException

- if

transferType

is not
one of

DataBuffer.TYPE_BYTE

or

DataBuffer.TYPE_USHORT
**Since:** 1.3

---

#### IndexColorModel

public IndexColorModel​(int bits,
int size,
int[] cmap,
int start,
int transferType,

BigInteger

validBits)

Constructs an

IndexColorModel

from an

int

array where each

int

is
comprised of red, green, blue, and alpha
components in the default RGB color model format.
The array must have enough values in it to fill all
of the needed component arrays of the specified size.
The

ColorSpace

is the default sRGB space.
The transparency value may be any of

Transparency.OPAQUE

,

Transparency.BITMASK

,
or

Transparency.TRANSLUCENT

depending on the arguments, as specified
in the

class description

above.
The transfer type must be one of

DataBuffer.TYPE_BYTE

DataBuffer.TYPE_USHORT

.
The

BigInteger

object specifies the valid/invalid pixels
in the

cmap

array. A pixel is valid if the

BigInteger

value at that index is set, and is invalid
if the

BigInteger

bit at that index is not set.

Method Detail

- getTransparency

```java
public int getTransparency()
```

Returns the transparency. Returns either OPAQUE, BITMASK,
or TRANSLUCENT

**Specified by:** getTransparency

in interface

Transparency
**Overrides:** getTransparency

in class

ColorModel
**Returns:** the transparency of this

IndexColorModel
**See Also:** Transparency.OPAQUE

,

Transparency.BITMASK

,

Transparency.TRANSLUCENT

- getComponentSize

```java
public int[] getComponentSize()
```

Returns an array of the number of bits for each color/alpha component.
The array contains the color components in the order red, green,
blue, followed by the alpha component, if present.

**Overrides:** getComponentSize

in class

ColorModel
**Returns:** an array containing the number of bits of each color
and alpha component of this

IndexColorModel

- getMapSize

```java
public final int getMapSize()
```

Returns the size of the color/alpha component arrays in this

IndexColorModel

.

**Returns:** the size of the color and alpha component arrays.

- getTransparentPixel

```java
public final int getTransparentPixel()
```

Returns the index of a transparent pixel in this

IndexColorModel

or -1 if there is no pixel
with an alpha value of 0. If a transparent pixel was
explicitly specified in one of the constructors by its
index, then that index will be preferred, otherwise,
the index of any pixel which happens to be fully transparent
may be returned.

**Returns:** the index of a transparent pixel in this

IndexColorModel

object, or -1 if there
is no such pixel

- getReds

```java
public final void getReds​(byte[] r)
```

Copies the array of red color components into the specified array.
Only the initial entries of the array as specified by

getMapSize

are written.

**Parameters:** r

- the specified array into which the elements of the
array of red color components are copied

- getGreens

```java
public final void getGreens​(byte[] g)
```

Copies the array of green color components into the specified array.
Only the initial entries of the array as specified by

getMapSize

are written.

**Parameters:** g

- the specified array into which the elements of the
array of green color components are copied

- getBlues

```java
public final void getBlues​(byte[] b)
```

Copies the array of blue color components into the specified array.
Only the initial entries of the array as specified by

getMapSize

are written.

**Parameters:** b

- the specified array into which the elements of the
array of blue color components are copied

- getAlphas

```java
public final void getAlphas​(byte[] a)
```

Copies the array of alpha transparency components into the
specified array. Only the initial entries of the array as specified
by

getMapSize

are written.

**Parameters:** a

- the specified array into which the elements of the
array of alpha components are copied

- getRGBs

```java
public final void getRGBs​(int[] rgb)
```

Converts data for each index from the color and alpha component
arrays to an int in the default RGB ColorModel format and copies
the resulting 32-bit ARGB values into the specified array. Only
the initial entries of the array as specified by

getMapSize

are
written.

**Parameters:** rgb

- the specified array into which the converted ARGB
values from this array of color and alpha components
are copied.

- getRed

```java
public final int getRed​(int pixel)
```

Returns the red color component for the specified pixel, scaled
from 0 to 255 in the default RGB ColorSpace, sRGB. The pixel value
is specified as an int.
Only the lower

n

bits of the pixel value, as specified in the

class description

above, are used to
calculate the returned value.
The returned value is a non pre-multiplied value.

**Specified by:** getRed

in class

ColorModel
**Parameters:** pixel

- the specified pixel
**Returns:** the value of the red color component for the specified pixel

- getGreen

```java
public final int getGreen​(int pixel)
```

Returns the green color component for the specified pixel, scaled
from 0 to 255 in the default RGB ColorSpace, sRGB. The pixel value
is specified as an int.
Only the lower

n

bits of the pixel value, as specified in the

class description

above, are used to
calculate the returned value.
The returned value is a non pre-multiplied value.

**Specified by:** getGreen

in class

ColorModel
**Parameters:** pixel

- the specified pixel
**Returns:** the value of the green color component for the specified pixel

- getBlue

```java
public final int getBlue​(int pixel)
```

Returns the blue color component for the specified pixel, scaled
from 0 to 255 in the default RGB ColorSpace, sRGB. The pixel value
is specified as an int.
Only the lower

n

bits of the pixel value, as specified in the

class description

above, are used to
calculate the returned value.
The returned value is a non pre-multiplied value.

**Specified by:** getBlue

in class

ColorModel
**Parameters:** pixel

- the specified pixel
**Returns:** the value of the blue color component for the specified pixel

- getAlpha

```java
public final int getAlpha​(int pixel)
```

Returns the alpha component for the specified pixel, scaled
from 0 to 255. The pixel value is specified as an int.
Only the lower

n

bits of the pixel value, as specified in the

class description

above, are used to
calculate the returned value.

**Specified by:** getAlpha

in class

ColorModel
**Parameters:** pixel

- the specified pixel
**Returns:** the value of the alpha component for the specified pixel

- getRGB

```java
public final int getRGB​(int pixel)
```

Returns the color/alpha components of the pixel in the default
RGB color model format. The pixel value is specified as an int.
Only the lower

n

bits of the pixel value, as specified in the

class description

above, are used to
calculate the returned value.
The returned value is in a non pre-multiplied format.

**Overrides:** getRGB

in class

ColorModel
**Parameters:** pixel

- the specified pixel
**Returns:** the color and alpha components of the specified pixel
**See Also:** ColorModel.getRGBdefault()

- getDataElements

```java
public
Object
getDataElements​(int rgb,

Object
pixel)
```

Returns a data element array representation of a pixel in this
ColorModel, given an integer pixel representation in the
default RGB color model. This array can then be passed to the

setDataElements

method of a

WritableRaster

object. If the pixel variable is

null

, a new array is allocated. If

pixel

is not

null

, it must be
a primitive array of type

transferType

; otherwise, a

ClassCastException

is thrown. An

ArrayIndexOutOfBoundsException

is
thrown if

pixel

is not large enough to hold a pixel
value for this

ColorModel

. The pixel array is returned.

Since

IndexColorModel

can be subclassed, subclasses
inherit the implementation of this method and if they don't
override it then they throw an exception if they use an
unsupported

transferType

.

**Overrides:** getDataElements

in class

ColorModel
**Parameters:** rgb

- the integer pixel representation in the default RGB
color model
**Parameters:** pixel

- the specified pixel
**Returns:** an array representation of the specified pixel in this

IndexColorModel

.
**Throws:** ClassCastException

- if

pixel

is not a primitive array of type

transferType
**Throws:** ArrayIndexOutOfBoundsException

- if

pixel

is not large enough to hold a pixel value
for this

ColorModel
**Throws:** UnsupportedOperationException

- if

transferType

is invalid
**See Also:** WritableRaster.setDataElements(int, int, java.lang.Object)

,

SampleModel.setDataElements(int, int, java.lang.Object, java.awt.image.DataBuffer)

- getComponents

```java
public int[] getComponents​(int pixel,
int[] components,
int offset)
```

Returns an array of unnormalized color/alpha components for a
specified pixel in this

ColorModel

. The pixel value
is specified as an int. If the

components

array is

null

,
a new array is allocated that contains

offset + getNumComponents()

elements.
The

components

array is returned,
with the alpha component included
only if

hasAlpha

returns true.
Color/alpha components are stored in the

components

array starting
at

offset

even if the array is allocated by this method.
An

ArrayIndexOutOfBoundsException

is thrown if the

components

array is not

null

and is
not large enough to hold all the color and alpha components
starting at

offset

.

**Overrides:** getComponents

in class

ColorModel
**Parameters:** pixel

- the specified pixel
**Parameters:** components

- the array to receive the color and alpha
components of the specified pixel
**Parameters:** offset

- the offset into the

components

array at
which to start storing the color and alpha components
**Returns:** an array containing the color and alpha components of the
specified pixel starting at the specified offset.
**See Also:** ColorModel.hasAlpha()

,

ColorModel.getNumComponents()

- getComponents

```java
public int[] getComponents​(
Object
pixel,
int[] components,
int offset)
```

Returns an array of unnormalized color/alpha components for
a specified pixel in this

ColorModel

. The pixel
value is specified by an array of data elements of type

transferType

passed in as an object reference.
If

pixel

is not a primitive array of type

transferType

, a

ClassCastException

is thrown. An

ArrayIndexOutOfBoundsException

is thrown if

pixel

is not large enough to hold
a pixel value for this

ColorModel

. If the

components

array is

null

, a new array
is allocated that contains

offset + getNumComponents()

elements.
The

components

array is returned,
with the alpha component included
only if

hasAlpha

returns true.
Color/alpha components are stored in the

components

array starting at

offset

even if the array is
allocated by this method. An

ArrayIndexOutOfBoundsException

is also
thrown if the

components

array is not

null

and is not large enough to hold all the color
and alpha components starting at

offset

.

Since

IndexColorModel

can be subclassed, subclasses
inherit the implementation of this method and if they don't
override it then they throw an exception if they use an
unsupported

transferType

.

**Overrides:** getComponents

in class

ColorModel
**Parameters:** pixel

- the specified pixel
**Parameters:** components

- an array that receives the color and alpha
components of the specified pixel
**Parameters:** offset

- the index into the

components

array at
which to begin storing the color and alpha components of the
specified pixel
**Returns:** an array containing the color and alpha components of the
specified pixel starting at the specified offset.
**Throws:** ArrayIndexOutOfBoundsException

- if

pixel

is not large enough to hold a pixel value for this

ColorModel

or if the

components

array is not

null

and is not large enough to hold all the color
and alpha components starting at

offset
**Throws:** ClassCastException

- if

pixel

is not a
primitive array of type

transferType
**Throws:** UnsupportedOperationException

- if

transferType

is not one of the supported transfer types
**See Also:** ColorModel.hasAlpha()

,

ColorModel.getNumComponents()

- getDataElement

```java
public int getDataElement​(int[] components,
int offset)
```

Returns a pixel value represented as an int in this

ColorModel

given an array of unnormalized
color/alpha components. An

ArrayIndexOutOfBoundsException

is thrown if the

components

array is not large
enough to hold all of the color and alpha components starting
at

offset

. Since

ColorModel

can be subclassed, subclasses inherit the
implementation of this method and if they don't override it then
they throw an exception if they use an unsupported transferType.

**Overrides:** getDataElement

in class

ColorModel
**Parameters:** components

- an array of unnormalized color and alpha
components
**Parameters:** offset

- the index into

components

at which to
begin retrieving the color and alpha components
**Returns:** an

int

pixel value in this

ColorModel

corresponding to the specified components.
**Throws:** ArrayIndexOutOfBoundsException

- if
the

components

array is not large enough to
hold all of the color and alpha components starting at

offset
**Throws:** UnsupportedOperationException

- if

transferType

is invalid

- getDataElements

```java
public
Object
getDataElements​(int[] components,
int offset,

Object
pixel)
```

Returns a data element array representation of a pixel in this

ColorModel

given an array of unnormalized color/alpha
components. This array can then be passed to the

setDataElements

method of a

WritableRaster

object. An

ArrayIndexOutOfBoundsException

is
thrown if the

components

array is not large enough to hold all of the
color and alpha components starting at

offset

.
If the pixel variable is

null

, a new array
is allocated. If

pixel

is not

null

,
it must be a primitive array of type

transferType

;
otherwise, a

ClassCastException

is thrown.
An

ArrayIndexOutOfBoundsException

is thrown if pixel
is not large enough to hold a pixel value for this

ColorModel

.

Since

IndexColorModel

can be subclassed, subclasses
inherit the implementation of this method and if they don't
override it then they throw an exception if they use an
unsupported

transferType

**Overrides:** getDataElements

in class

ColorModel
**Parameters:** components

- an array of unnormalized color and alpha
components
**Parameters:** offset

- the index into

components

at which to
begin retrieving color and alpha components
**Parameters:** pixel

- the

Object

representing an array of color
and alpha components
**Returns:** an

Object

representing an array of color and
alpha components.
**Throws:** ClassCastException

- if

pixel

is not a primitive array of type

transferType
**Throws:** ArrayIndexOutOfBoundsException

- if

pixel

is not large enough to hold a pixel value
for this

ColorModel

or the

components

array is not large enough to hold all of the color and alpha
components starting at

offset
**Throws:** UnsupportedOperationException

- if

transferType

is not one of the supported transfer types
**See Also:** WritableRaster.setDataElements(int, int, java.lang.Object)

,

SampleModel.setDataElements(int, int, java.lang.Object, java.awt.image.DataBuffer)

- createCompatibleWritableRaster

```java
public
WritableRaster
createCompatibleWritableRaster​(int w,
int h)
```

Creates a

WritableRaster

with the specified width
and height that has a data layout (

SampleModel

)
compatible with this

ColorModel

. This method
only works for color models with 16 or fewer bits per pixel.

Since

IndexColorModel

can be subclassed, any
subclass that supports greater than 16 bits per pixel must
override this method.

**Overrides:** createCompatibleWritableRaster

in class

ColorModel
**Parameters:** w

- the width to apply to the new

WritableRaster
**Parameters:** h

- the height to apply to the new

WritableRaster
**Returns:** a

WritableRaster

object with the specified
width and height.
**Throws:** UnsupportedOperationException

- if the number of bits in a
pixel is greater than 16
**See Also:** WritableRaster

,

SampleModel

- isCompatibleRaster

```java
public boolean isCompatibleRaster​(
Raster
raster)
```

Returns

true

if

raster

is compatible
with this

ColorModel

or

false

if it
is not compatible with this

ColorModel

.

**Overrides:** isCompatibleRaster

in class

ColorModel
**Parameters:** raster

- the

Raster

object to test for compatibility
**Returns:** true

if

raster

is compatible
with this

ColorModel

;

false

otherwise.

- createCompatibleSampleModel

```java
public
SampleModel
createCompatibleSampleModel​(int w,
int h)
```

Creates a

SampleModel

with the specified
width and height that has a data layout compatible with
this

ColorModel

.

**Overrides:** createCompatibleSampleModel

in class

ColorModel
**Parameters:** w

- the width to apply to the new

SampleModel
**Parameters:** h

- the height to apply to the new

SampleModel
**Returns:** a

SampleModel

object with the specified
width and height.
**Throws:** IllegalArgumentException

- if

w

or

h

is not greater than 0
**See Also:** SampleModel

- isCompatibleSampleModel

```java
public boolean isCompatibleSampleModel​(
SampleModel
sm)
```

Checks if the specified

SampleModel

is compatible
with this

ColorModel

. If

sm

is

null

, this method returns

false

.

**Overrides:** isCompatibleSampleModel

in class

ColorModel
**Parameters:** sm

- the specified

SampleModel

,
or

null
**Returns:** true

if the specified

SampleModel

is compatible with this

ColorModel

;

false

otherwise.
**See Also:** SampleModel

- convertToIntDiscrete

```java
public
BufferedImage
convertToIntDiscrete​(
Raster
raster,
boolean forceARGB)
```

Returns a new

BufferedImage

of TYPE_INT_ARGB or
TYPE_INT_RGB that has a

Raster

with pixel data
computed by expanding the indices in the source

Raster

using the color/alpha component arrays of this

ColorModel

.
Only the lower

n

bits of each index value in the source

Raster

, as specified in the

class description

above, are used to
compute the color/alpha values in the returned image.
If

forceARGB

is

true

, a TYPE_INT_ARGB image is
returned regardless of whether or not this

ColorModel

has an alpha component array or a transparent pixel.

**Parameters:** raster

- the specified

Raster
**Parameters:** forceARGB

- if

true

, the returned

BufferedImage

is TYPE_INT_ARGB; otherwise it is
TYPE_INT_RGB
**Returns:** a

BufferedImage

created with the specified

Raster
**Throws:** IllegalArgumentException

- if the raster argument is not
compatible with this IndexColorModel

- isValid

```java
public boolean isValid​(int pixel)
```

Returns whether or not the pixel is valid.

**Parameters:** pixel

- the specified pixel value
**Returns:** true

if

pixel

is valid;

false

otherwise.
**Since:** 1.3

- isValid

```java
public boolean isValid()
```

Returns whether or not all of the pixels are valid.

**Returns:** true

if all pixels are valid;

false

otherwise.
**Since:** 1.3

- getValidPixels

```java
public
BigInteger
getValidPixels()
```

Returns a

BigInteger

that indicates the valid/invalid
pixels in the colormap. A bit is valid if the

BigInteger

value at that index is set, and is invalid
if the

BigInteger

value at that index is not set.
The only valid ranges to query in the

BigInteger

are
between 0 and the map size.

**Returns:** a

BigInteger

indicating the valid/invalid pixels.
**Since:** 1.3

- finalize

```java
@Deprecated
(
since
="9")
public void finalize()
```

Deprecated.

The

finalize

method has been deprecated.
Subclasses that override

finalize

in order to perform cleanup
should be modified to use alternative cleanup mechanisms and
to remove the overriding

finalize

method.
When overriding the

finalize

method, its implementation must explicitly
ensure that

super.finalize()

is invoked as described in

Object.finalize()

.
See the specification for

Object.finalize()

for further
information about migration options.

Disposes of system resources associated with this

ColorModel

once this

ColorModel

is no
longer referenced.

**Overrides:** finalize

in class

ColorModel
**See Also:** WeakReference

,

PhantomReference

- toString

```java
public
String
toString()
```

Returns the

String

representation of the contents of
this

ColorModel

object.

**Overrides:** toString

in class

ColorModel
**Returns:** a

String

representing the contents of this

ColorModel

object.

- equals

```java
public boolean equals​(
Object
obj)
```

Tests if the specified

Object

is an
instance of

IndexColorModel

and if it equals this

IndexColorModel

**Overrides:** equals

in class

ColorModel
**Parameters:** obj

- the

Object

to test for equality
**Returns:** true

if the specified

Object

equals this

IndexColorModel

;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code for IndexColorModel.

**Overrides:** hashCode

in class

ColorModel
**Returns:** a hash code for IndexColorModel
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### Method Detail

getTransparency

```java
public int getTransparency()
```

Returns the transparency. Returns either OPAQUE, BITMASK,
or TRANSLUCENT

**Specified by:** getTransparency

in interface

Transparency
**Overrides:** getTransparency

in class

ColorModel
**Returns:** the transparency of this

IndexColorModel
**See Also:** Transparency.OPAQUE

,

Transparency.BITMASK

,

Transparency.TRANSLUCENT

---

#### getTransparency

public int getTransparency()

Returns the transparency. Returns either OPAQUE, BITMASK,
or TRANSLUCENT

getComponentSize

```java
public int[] getComponentSize()
```

Returns an array of the number of bits for each color/alpha component.
The array contains the color components in the order red, green,
blue, followed by the alpha component, if present.

**Overrides:** getComponentSize

in class

ColorModel
**Returns:** an array containing the number of bits of each color
and alpha component of this

IndexColorModel

---

#### getComponentSize

public int[] getComponentSize()

Returns an array of the number of bits for each color/alpha component.
The array contains the color components in the order red, green,
blue, followed by the alpha component, if present.

getMapSize

```java
public final int getMapSize()
```

Returns the size of the color/alpha component arrays in this

IndexColorModel

.

**Returns:** the size of the color and alpha component arrays.

---

#### getMapSize

public final int getMapSize()

Returns the size of the color/alpha component arrays in this

IndexColorModel

.

getTransparentPixel

```java
public final int getTransparentPixel()
```

Returns the index of a transparent pixel in this

IndexColorModel

or -1 if there is no pixel
with an alpha value of 0. If a transparent pixel was
explicitly specified in one of the constructors by its
index, then that index will be preferred, otherwise,
the index of any pixel which happens to be fully transparent
may be returned.

**Returns:** the index of a transparent pixel in this

IndexColorModel

object, or -1 if there
is no such pixel

---

#### getTransparentPixel

public final int getTransparentPixel()

Returns the index of a transparent pixel in this

IndexColorModel

or -1 if there is no pixel
with an alpha value of 0. If a transparent pixel was
explicitly specified in one of the constructors by its
index, then that index will be preferred, otherwise,
the index of any pixel which happens to be fully transparent
may be returned.

getReds

```java
public final void getReds​(byte[] r)
```

Copies the array of red color components into the specified array.
Only the initial entries of the array as specified by

getMapSize

are written.

**Parameters:** r

- the specified array into which the elements of the
array of red color components are copied

---

#### getReds

public final void getReds​(byte[] r)

Copies the array of red color components into the specified array.
Only the initial entries of the array as specified by

getMapSize

are written.

getGreens

```java
public final void getGreens​(byte[] g)
```

Copies the array of green color components into the specified array.
Only the initial entries of the array as specified by

getMapSize

are written.

**Parameters:** g

- the specified array into which the elements of the
array of green color components are copied

---

#### getGreens

public final void getGreens​(byte[] g)

Copies the array of green color components into the specified array.
Only the initial entries of the array as specified by

getMapSize

are written.

getBlues

```java
public final void getBlues​(byte[] b)
```

Copies the array of blue color components into the specified array.
Only the initial entries of the array as specified by

getMapSize

are written.

**Parameters:** b

- the specified array into which the elements of the
array of blue color components are copied

---

#### getBlues

public final void getBlues​(byte[] b)

Copies the array of blue color components into the specified array.
Only the initial entries of the array as specified by

getMapSize

are written.

getAlphas

```java
public final void getAlphas​(byte[] a)
```

Copies the array of alpha transparency components into the
specified array. Only the initial entries of the array as specified
by

getMapSize

are written.

**Parameters:** a

- the specified array into which the elements of the
array of alpha components are copied

---

#### getAlphas

public final void getAlphas​(byte[] a)

Copies the array of alpha transparency components into the
specified array. Only the initial entries of the array as specified
by

getMapSize

are written.

getRGBs

```java
public final void getRGBs​(int[] rgb)
```

Converts data for each index from the color and alpha component
arrays to an int in the default RGB ColorModel format and copies
the resulting 32-bit ARGB values into the specified array. Only
the initial entries of the array as specified by

getMapSize

are
written.

**Parameters:** rgb

- the specified array into which the converted ARGB
values from this array of color and alpha components
are copied.

---

#### getRGBs

public final void getRGBs​(int[] rgb)

Converts data for each index from the color and alpha component
arrays to an int in the default RGB ColorModel format and copies
the resulting 32-bit ARGB values into the specified array. Only
the initial entries of the array as specified by

getMapSize

are
written.

getRed

```java
public final int getRed​(int pixel)
```

Returns the red color component for the specified pixel, scaled
from 0 to 255 in the default RGB ColorSpace, sRGB. The pixel value
is specified as an int.
Only the lower

n

bits of the pixel value, as specified in the

class description

above, are used to
calculate the returned value.
The returned value is a non pre-multiplied value.

**Specified by:** getRed

in class

ColorModel
**Parameters:** pixel

- the specified pixel
**Returns:** the value of the red color component for the specified pixel

---

#### getRed

public final int getRed​(int pixel)

Returns the red color component for the specified pixel, scaled
from 0 to 255 in the default RGB ColorSpace, sRGB. The pixel value
is specified as an int.
Only the lower

n

bits of the pixel value, as specified in the

class description

above, are used to
calculate the returned value.
The returned value is a non pre-multiplied value.

getGreen

```java
public final int getGreen​(int pixel)
```

Returns the green color component for the specified pixel, scaled
from 0 to 255 in the default RGB ColorSpace, sRGB. The pixel value
is specified as an int.
Only the lower

n

bits of the pixel value, as specified in the

class description

above, are used to
calculate the returned value.
The returned value is a non pre-multiplied value.

**Specified by:** getGreen

in class

ColorModel
**Parameters:** pixel

- the specified pixel
**Returns:** the value of the green color component for the specified pixel

---

#### getGreen

public final int getGreen​(int pixel)

Returns the green color component for the specified pixel, scaled
from 0 to 255 in the default RGB ColorSpace, sRGB. The pixel value
is specified as an int.
Only the lower

n

bits of the pixel value, as specified in the

class description

above, are used to
calculate the returned value.
The returned value is a non pre-multiplied value.

getBlue

```java
public final int getBlue​(int pixel)
```

Returns the blue color component for the specified pixel, scaled
from 0 to 255 in the default RGB ColorSpace, sRGB. The pixel value
is specified as an int.
Only the lower

n

bits of the pixel value, as specified in the

class description

above, are used to
calculate the returned value.
The returned value is a non pre-multiplied value.

**Specified by:** getBlue

in class

ColorModel
**Parameters:** pixel

- the specified pixel
**Returns:** the value of the blue color component for the specified pixel

---

#### getBlue

public final int getBlue​(int pixel)

Returns the blue color component for the specified pixel, scaled
from 0 to 255 in the default RGB ColorSpace, sRGB. The pixel value
is specified as an int.
Only the lower

n

bits of the pixel value, as specified in the

class description

above, are used to
calculate the returned value.
The returned value is a non pre-multiplied value.

getAlpha

```java
public final int getAlpha​(int pixel)
```

Returns the alpha component for the specified pixel, scaled
from 0 to 255. The pixel value is specified as an int.
Only the lower

n

bits of the pixel value, as specified in the

class description

above, are used to
calculate the returned value.

**Specified by:** getAlpha

in class

ColorModel
**Parameters:** pixel

- the specified pixel
**Returns:** the value of the alpha component for the specified pixel

---

#### getAlpha

public final int getAlpha​(int pixel)

Returns the alpha component for the specified pixel, scaled
from 0 to 255. The pixel value is specified as an int.
Only the lower

n

bits of the pixel value, as specified in the

class description

above, are used to
calculate the returned value.

getRGB

```java
public final int getRGB​(int pixel)
```

Returns the color/alpha components of the pixel in the default
RGB color model format. The pixel value is specified as an int.
Only the lower

n

bits of the pixel value, as specified in the

class description

above, are used to
calculate the returned value.
The returned value is in a non pre-multiplied format.

**Overrides:** getRGB

in class

ColorModel
**Parameters:** pixel

- the specified pixel
**Returns:** the color and alpha components of the specified pixel
**See Also:** ColorModel.getRGBdefault()

---

#### getRGB

public final int getRGB​(int pixel)

Returns the color/alpha components of the pixel in the default
RGB color model format. The pixel value is specified as an int.
Only the lower

n

bits of the pixel value, as specified in the

class description

above, are used to
calculate the returned value.
The returned value is in a non pre-multiplied format.

getDataElements

```java
public
Object
getDataElements​(int rgb,

Object
pixel)
```

Returns a data element array representation of a pixel in this
ColorModel, given an integer pixel representation in the
default RGB color model. This array can then be passed to the

setDataElements

method of a

WritableRaster

object. If the pixel variable is

null

, a new array is allocated. If

pixel

is not

null

, it must be
a primitive array of type

transferType

; otherwise, a

ClassCastException

is thrown. An

ArrayIndexOutOfBoundsException

is
thrown if

pixel

is not large enough to hold a pixel
value for this

ColorModel

. The pixel array is returned.

Since

IndexColorModel

can be subclassed, subclasses
inherit the implementation of this method and if they don't
override it then they throw an exception if they use an
unsupported

transferType

.

**Overrides:** getDataElements

in class

ColorModel
**Parameters:** rgb

- the integer pixel representation in the default RGB
color model
**Parameters:** pixel

- the specified pixel
**Returns:** an array representation of the specified pixel in this

IndexColorModel

.
**Throws:** ClassCastException

- if

pixel

is not a primitive array of type

transferType
**Throws:** ArrayIndexOutOfBoundsException

- if

pixel

is not large enough to hold a pixel value
for this

ColorModel
**Throws:** UnsupportedOperationException

- if

transferType

is invalid
**See Also:** WritableRaster.setDataElements(int, int, java.lang.Object)

,

SampleModel.setDataElements(int, int, java.lang.Object, java.awt.image.DataBuffer)

---

#### getDataElements

public

Object

getDataElements​(int rgb,

Object

pixel)

Returns a data element array representation of a pixel in this
ColorModel, given an integer pixel representation in the
default RGB color model. This array can then be passed to the

setDataElements

method of a

WritableRaster

object. If the pixel variable is

null

, a new array is allocated. If

pixel

is not

null

, it must be
a primitive array of type

transferType

; otherwise, a

ClassCastException

is thrown. An

ArrayIndexOutOfBoundsException

is
thrown if

pixel

is not large enough to hold a pixel
value for this

ColorModel

. The pixel array is returned.

Since

IndexColorModel

can be subclassed, subclasses
inherit the implementation of this method and if they don't
override it then they throw an exception if they use an
unsupported

transferType

.

Since

IndexColorModel

can be subclassed, subclasses
inherit the implementation of this method and if they don't
override it then they throw an exception if they use an
unsupported

transferType

.

getComponents

```java
public int[] getComponents​(int pixel,
int[] components,
int offset)
```

Returns an array of unnormalized color/alpha components for a
specified pixel in this

ColorModel

. The pixel value
is specified as an int. If the

components

array is

null

,
a new array is allocated that contains

offset + getNumComponents()

elements.
The

components

array is returned,
with the alpha component included
only if

hasAlpha

returns true.
Color/alpha components are stored in the

components

array starting
at

offset

even if the array is allocated by this method.
An

ArrayIndexOutOfBoundsException

is thrown if the

components

array is not

null

and is
not large enough to hold all the color and alpha components
starting at

offset

.

**Overrides:** getComponents

in class

ColorModel
**Parameters:** pixel

- the specified pixel
**Parameters:** components

- the array to receive the color and alpha
components of the specified pixel
**Parameters:** offset

- the offset into the

components

array at
which to start storing the color and alpha components
**Returns:** an array containing the color and alpha components of the
specified pixel starting at the specified offset.
**See Also:** ColorModel.hasAlpha()

,

ColorModel.getNumComponents()

---

#### getComponents

public int[] getComponents​(int pixel,
int[] components,
int offset)

Returns an array of unnormalized color/alpha components for a
specified pixel in this

ColorModel

. The pixel value
is specified as an int. If the

components

array is

null

,
a new array is allocated that contains

offset + getNumComponents()

elements.
The

components

array is returned,
with the alpha component included
only if

hasAlpha

returns true.
Color/alpha components are stored in the

components

array starting
at

offset

even if the array is allocated by this method.
An

ArrayIndexOutOfBoundsException

is thrown if the

components

array is not

null

and is
not large enough to hold all the color and alpha components
starting at

offset

.

getComponents

```java
public int[] getComponents​(
Object
pixel,
int[] components,
int offset)
```

Returns an array of unnormalized color/alpha components for
a specified pixel in this

ColorModel

. The pixel
value is specified by an array of data elements of type

transferType

passed in as an object reference.
If

pixel

is not a primitive array of type

transferType

, a

ClassCastException

is thrown. An

ArrayIndexOutOfBoundsException

is thrown if

pixel

is not large enough to hold
a pixel value for this

ColorModel

. If the

components

array is

null

, a new array
is allocated that contains

offset + getNumComponents()

elements.
The

components

array is returned,
with the alpha component included
only if

hasAlpha

returns true.
Color/alpha components are stored in the

components

array starting at

offset

even if the array is
allocated by this method. An

ArrayIndexOutOfBoundsException

is also
thrown if the

components

array is not

null

and is not large enough to hold all the color
and alpha components starting at

offset

.

Since

IndexColorModel

can be subclassed, subclasses
inherit the implementation of this method and if they don't
override it then they throw an exception if they use an
unsupported

transferType

.

**Overrides:** getComponents

in class

ColorModel
**Parameters:** pixel

- the specified pixel
**Parameters:** components

- an array that receives the color and alpha
components of the specified pixel
**Parameters:** offset

- the index into the

components

array at
which to begin storing the color and alpha components of the
specified pixel
**Returns:** an array containing the color and alpha components of the
specified pixel starting at the specified offset.
**Throws:** ArrayIndexOutOfBoundsException

- if

pixel

is not large enough to hold a pixel value for this

ColorModel

or if the

components

array is not

null

and is not large enough to hold all the color
and alpha components starting at

offset
**Throws:** ClassCastException

- if

pixel

is not a
primitive array of type

transferType
**Throws:** UnsupportedOperationException

- if

transferType

is not one of the supported transfer types
**See Also:** ColorModel.hasAlpha()

,

ColorModel.getNumComponents()

---

#### getComponents

public int[] getComponents​(

Object

pixel,
int[] components,
int offset)

Returns an array of unnormalized color/alpha components for
a specified pixel in this

ColorModel

. The pixel
value is specified by an array of data elements of type

transferType

passed in as an object reference.
If

pixel

is not a primitive array of type

transferType

, a

ClassCastException

is thrown. An

ArrayIndexOutOfBoundsException

is thrown if

pixel

is not large enough to hold
a pixel value for this

ColorModel

. If the

components

array is

null

, a new array
is allocated that contains

offset + getNumComponents()

elements.
The

components

array is returned,
with the alpha component included
only if

hasAlpha

returns true.
Color/alpha components are stored in the

components

array starting at

offset

even if the array is
allocated by this method. An

ArrayIndexOutOfBoundsException

is also
thrown if the

components

array is not

null

and is not large enough to hold all the color
and alpha components starting at

offset

.

Since

IndexColorModel

can be subclassed, subclasses
inherit the implementation of this method and if they don't
override it then they throw an exception if they use an
unsupported

transferType

.

Since

IndexColorModel

can be subclassed, subclasses
inherit the implementation of this method and if they don't
override it then they throw an exception if they use an
unsupported

transferType

.

getDataElement

```java
public int getDataElement​(int[] components,
int offset)
```

Returns a pixel value represented as an int in this

ColorModel

given an array of unnormalized
color/alpha components. An

ArrayIndexOutOfBoundsException

is thrown if the

components

array is not large
enough to hold all of the color and alpha components starting
at

offset

. Since

ColorModel

can be subclassed, subclasses inherit the
implementation of this method and if they don't override it then
they throw an exception if they use an unsupported transferType.

**Overrides:** getDataElement

in class

ColorModel
**Parameters:** components

- an array of unnormalized color and alpha
components
**Parameters:** offset

- the index into

components

at which to
begin retrieving the color and alpha components
**Returns:** an

int

pixel value in this

ColorModel

corresponding to the specified components.
**Throws:** ArrayIndexOutOfBoundsException

- if
the

components

array is not large enough to
hold all of the color and alpha components starting at

offset
**Throws:** UnsupportedOperationException

- if

transferType

is invalid

---

#### getDataElement

public int getDataElement​(int[] components,
int offset)

Returns a pixel value represented as an int in this

ColorModel

given an array of unnormalized
color/alpha components. An

ArrayIndexOutOfBoundsException

is thrown if the

components

array is not large
enough to hold all of the color and alpha components starting
at

offset

. Since

ColorModel

can be subclassed, subclasses inherit the
implementation of this method and if they don't override it then
they throw an exception if they use an unsupported transferType.

getDataElements

```java
public
Object
getDataElements​(int[] components,
int offset,

Object
pixel)
```

Returns a data element array representation of a pixel in this

ColorModel

given an array of unnormalized color/alpha
components. This array can then be passed to the

setDataElements

method of a

WritableRaster

object. An

ArrayIndexOutOfBoundsException

is
thrown if the

components

array is not large enough to hold all of the
color and alpha components starting at

offset

.
If the pixel variable is

null

, a new array
is allocated. If

pixel

is not

null

,
it must be a primitive array of type

transferType

;
otherwise, a

ClassCastException

is thrown.
An

ArrayIndexOutOfBoundsException

is thrown if pixel
is not large enough to hold a pixel value for this

ColorModel

.

Since

IndexColorModel

can be subclassed, subclasses
inherit the implementation of this method and if they don't
override it then they throw an exception if they use an
unsupported

transferType

**Overrides:** getDataElements

in class

ColorModel
**Parameters:** components

- an array of unnormalized color and alpha
components
**Parameters:** offset

- the index into

components

at which to
begin retrieving color and alpha components
**Parameters:** pixel

- the

Object

representing an array of color
and alpha components
**Returns:** an

Object

representing an array of color and
alpha components.
**Throws:** ClassCastException

- if

pixel

is not a primitive array of type

transferType
**Throws:** ArrayIndexOutOfBoundsException

- if

pixel

is not large enough to hold a pixel value
for this

ColorModel

or the

components

array is not large enough to hold all of the color and alpha
components starting at

offset
**Throws:** UnsupportedOperationException

- if

transferType

is not one of the supported transfer types
**See Also:** WritableRaster.setDataElements(int, int, java.lang.Object)

,

SampleModel.setDataElements(int, int, java.lang.Object, java.awt.image.DataBuffer)

---

#### getDataElements

public

Object

getDataElements​(int[] components,
int offset,

Object

pixel)

Returns a data element array representation of a pixel in this

ColorModel

given an array of unnormalized color/alpha
components. This array can then be passed to the

setDataElements

method of a

WritableRaster

object. An

ArrayIndexOutOfBoundsException

is
thrown if the

components

array is not large enough to hold all of the
color and alpha components starting at

offset

.
If the pixel variable is

null

, a new array
is allocated. If

pixel

is not

null

,
it must be a primitive array of type

transferType

;
otherwise, a

ClassCastException

is thrown.
An

ArrayIndexOutOfBoundsException

is thrown if pixel
is not large enough to hold a pixel value for this

ColorModel

.

Since

IndexColorModel

can be subclassed, subclasses
inherit the implementation of this method and if they don't
override it then they throw an exception if they use an
unsupported

transferType

Since

IndexColorModel

can be subclassed, subclasses
inherit the implementation of this method and if they don't
override it then they throw an exception if they use an
unsupported

transferType

createCompatibleWritableRaster

```java
public
WritableRaster
createCompatibleWritableRaster​(int w,
int h)
```

Creates a

WritableRaster

with the specified width
and height that has a data layout (

SampleModel

)
compatible with this

ColorModel

. This method
only works for color models with 16 or fewer bits per pixel.

Since

IndexColorModel

can be subclassed, any
subclass that supports greater than 16 bits per pixel must
override this method.

**Overrides:** createCompatibleWritableRaster

in class

ColorModel
**Parameters:** w

- the width to apply to the new

WritableRaster
**Parameters:** h

- the height to apply to the new

WritableRaster
**Returns:** a

WritableRaster

object with the specified
width and height.
**Throws:** UnsupportedOperationException

- if the number of bits in a
pixel is greater than 16
**See Also:** WritableRaster

,

SampleModel

---

#### createCompatibleWritableRaster

public

WritableRaster

createCompatibleWritableRaster​(int w,
int h)

Creates a

WritableRaster

with the specified width
and height that has a data layout (

SampleModel

)
compatible with this

ColorModel

. This method
only works for color models with 16 or fewer bits per pixel.

Since

IndexColorModel

can be subclassed, any
subclass that supports greater than 16 bits per pixel must
override this method.

Since

IndexColorModel

can be subclassed, any
subclass that supports greater than 16 bits per pixel must
override this method.

isCompatibleRaster

```java
public boolean isCompatibleRaster​(
Raster
raster)
```

Returns

true

if

raster

is compatible
with this

ColorModel

or

false

if it
is not compatible with this

ColorModel

.

**Overrides:** isCompatibleRaster

in class

ColorModel
**Parameters:** raster

- the

Raster

object to test for compatibility
**Returns:** true

if

raster

is compatible
with this

ColorModel

;

false

otherwise.

---

#### isCompatibleRaster

public boolean isCompatibleRaster​(

Raster

raster)

Returns

true

if

raster

is compatible
with this

ColorModel

or

false

if it
is not compatible with this

ColorModel

.

createCompatibleSampleModel

```java
public
SampleModel
createCompatibleSampleModel​(int w,
int h)
```

Creates a

SampleModel

with the specified
width and height that has a data layout compatible with
this

ColorModel

.

**Overrides:** createCompatibleSampleModel

in class

ColorModel
**Parameters:** w

- the width to apply to the new

SampleModel
**Parameters:** h

- the height to apply to the new

SampleModel
**Returns:** a

SampleModel

object with the specified
width and height.
**Throws:** IllegalArgumentException

- if

w

or

h

is not greater than 0
**See Also:** SampleModel

---

#### createCompatibleSampleModel

public

SampleModel

createCompatibleSampleModel​(int w,
int h)

Creates a

SampleModel

with the specified
width and height that has a data layout compatible with
this

ColorModel

.

isCompatibleSampleModel

```java
public boolean isCompatibleSampleModel​(
SampleModel
sm)
```

Checks if the specified

SampleModel

is compatible
with this

ColorModel

. If

sm

is

null

, this method returns

false

.

**Overrides:** isCompatibleSampleModel

in class

ColorModel
**Parameters:** sm

- the specified

SampleModel

,
or

null
**Returns:** true

if the specified

SampleModel

is compatible with this

ColorModel

;

false

otherwise.
**See Also:** SampleModel

---

#### isCompatibleSampleModel

public boolean isCompatibleSampleModel​(

SampleModel

sm)

Checks if the specified

SampleModel

is compatible
with this

ColorModel

. If

sm

is

null

, this method returns

false

.

convertToIntDiscrete

```java
public
BufferedImage
convertToIntDiscrete​(
Raster
raster,
boolean forceARGB)
```

Returns a new

BufferedImage

of TYPE_INT_ARGB or
TYPE_INT_RGB that has a

Raster

with pixel data
computed by expanding the indices in the source

Raster

using the color/alpha component arrays of this

ColorModel

.
Only the lower

n

bits of each index value in the source

Raster

, as specified in the

class description

above, are used to
compute the color/alpha values in the returned image.
If

forceARGB

is

true

, a TYPE_INT_ARGB image is
returned regardless of whether or not this

ColorModel

has an alpha component array or a transparent pixel.

**Parameters:** raster

- the specified

Raster
**Parameters:** forceARGB

- if

true

, the returned

BufferedImage

is TYPE_INT_ARGB; otherwise it is
TYPE_INT_RGB
**Returns:** a

BufferedImage

created with the specified

Raster
**Throws:** IllegalArgumentException

- if the raster argument is not
compatible with this IndexColorModel

---

#### convertToIntDiscrete

public

BufferedImage

convertToIntDiscrete​(

Raster

raster,
boolean forceARGB)

Returns a new

BufferedImage

of TYPE_INT_ARGB or
TYPE_INT_RGB that has a

Raster

with pixel data
computed by expanding the indices in the source

Raster

using the color/alpha component arrays of this

ColorModel

.
Only the lower

n

bits of each index value in the source

Raster

, as specified in the

class description

above, are used to
compute the color/alpha values in the returned image.
If

forceARGB

is

true

, a TYPE_INT_ARGB image is
returned regardless of whether or not this

ColorModel

has an alpha component array or a transparent pixel.

isValid

```java
public boolean isValid​(int pixel)
```

Returns whether or not the pixel is valid.

**Parameters:** pixel

- the specified pixel value
**Returns:** true

if

pixel

is valid;

false

otherwise.
**Since:** 1.3

---

#### isValid

public boolean isValid​(int pixel)

Returns whether or not the pixel is valid.

isValid

```java
public boolean isValid()
```

Returns whether or not all of the pixels are valid.

**Returns:** true

if all pixels are valid;

false

otherwise.
**Since:** 1.3

---

#### isValid

public boolean isValid()

Returns whether or not all of the pixels are valid.

getValidPixels

```java
public
BigInteger
getValidPixels()
```

Returns a

BigInteger

that indicates the valid/invalid
pixels in the colormap. A bit is valid if the

BigInteger

value at that index is set, and is invalid
if the

BigInteger

value at that index is not set.
The only valid ranges to query in the

BigInteger

are
between 0 and the map size.

**Returns:** a

BigInteger

indicating the valid/invalid pixels.
**Since:** 1.3

---

#### getValidPixels

public

BigInteger

getValidPixels()

Returns a

BigInteger

that indicates the valid/invalid
pixels in the colormap. A bit is valid if the

BigInteger

value at that index is set, and is invalid
if the

BigInteger

value at that index is not set.
The only valid ranges to query in the

BigInteger

are
between 0 and the map size.

finalize

```java
@Deprecated
(
since
="9")
public void finalize()
```

Deprecated.

The

finalize

method has been deprecated.
Subclasses that override

finalize

in order to perform cleanup
should be modified to use alternative cleanup mechanisms and
to remove the overriding

finalize

method.
When overriding the

finalize

method, its implementation must explicitly
ensure that

super.finalize()

is invoked as described in

Object.finalize()

.
See the specification for

Object.finalize()

for further
information about migration options.

Disposes of system resources associated with this

ColorModel

once this

ColorModel

is no
longer referenced.

**Overrides:** finalize

in class

ColorModel
**See Also:** WeakReference

,

PhantomReference

---

#### finalize

@Deprecated

(

since

="9")
public void finalize()

Disposes of system resources associated with this

ColorModel

once this

ColorModel

is no
longer referenced.

toString

```java
public
String
toString()
```

Returns the

String

representation of the contents of
this

ColorModel

object.

**Overrides:** toString

in class

ColorModel
**Returns:** a

String

representing the contents of this

ColorModel

object.

---

#### toString

public

String

toString()

Returns the

String

representation of the contents of
this

ColorModel

object.

equals

```java
public boolean equals​(
Object
obj)
```

Tests if the specified

Object

is an
instance of

IndexColorModel

and if it equals this

IndexColorModel

**Overrides:** equals

in class

ColorModel
**Parameters:** obj

- the

Object

to test for equality
**Returns:** true

if the specified

Object

equals this

IndexColorModel

;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Tests if the specified

Object

is an
instance of

IndexColorModel

and if it equals this

IndexColorModel

hashCode

```java
public int hashCode()
```

Returns the hash code for IndexColorModel.

**Overrides:** hashCode

in class

ColorModel
**Returns:** a hash code for IndexColorModel
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns the hash code for IndexColorModel.

---

