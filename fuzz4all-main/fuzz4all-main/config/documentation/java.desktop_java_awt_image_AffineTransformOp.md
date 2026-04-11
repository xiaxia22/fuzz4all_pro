# Class AffineTransformOp

**Source:** `java.desktop\java\awt\image\AffineTransformOp.html`

### Class Description

```java
public class
AffineTransformOp

extends
Object

implements
BufferedImageOp
,
RasterOp
```

This class uses an affine transform to perform a linear mapping from
2D coordinates in the source image or

Raster

to 2D coordinates
in the destination image or

Raster

.
The type of interpolation that is used is specified through a constructor,
either by a

RenderingHints

object or by one of the integer
interpolation types defined in this class.

If a

RenderingHints

object is specified in the constructor, the
interpolation hint and the rendering quality hint are used to set
the interpolation type for this operation. The color rendering hint
and the dithering hint can be used when color conversion is required.

Note that the following constraints have to be met:

- The source and destination must be different.

For

Raster

objects, the number of bands in the source must
be equal to the number of bands in the destination.

**All Implemented Interfaces:** BufferedImageOp

,

RasterOp

---

### Field Details

#### @Native

public static final int TYPE_NEAREST_NEIGHBOR

Nearest-neighbor interpolation type.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int TYPE_BILINEAR

Bilinear interpolation type.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int TYPE_BICUBIC

Bicubic interpolation type.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public AffineTransformOp​(
AffineTransform
xform,

RenderingHints
hints)

Constructs an

AffineTransformOp

given an affine transform.
The interpolation type is determined from the

RenderingHints

object. If the interpolation hint is
defined, it will be used. Otherwise, if the rendering quality hint is
defined, the interpolation type is determined from its value. If no
hints are specified (

hints

is null),
the interpolation type is

TYPE_NEAREST_NEIGHBOR

.

**Parameters:**
- xform

- The

AffineTransform

to use for the
operation.
- hints

- The

RenderingHints

object used to specify
the interpolation type for the operation.

**Throws:**
- ImagingOpException

- if the transform is non-invertible.

**See Also:**
- RenderingHints.KEY_INTERPOLATION

,

RenderingHints.KEY_RENDERING

---

#### public AffineTransformOp​(
AffineTransform
xform,
int interpolationType)

Constructs an

AffineTransformOp

given an affine transform
and the interpolation type.

**Parameters:**
- xform

- The

AffineTransform

to use for the operation.
- interpolationType

- One of the integer
interpolation type constants defined by this class:

TYPE_NEAREST_NEIGHBOR

,

TYPE_BILINEAR

,

TYPE_BICUBIC

.

**Throws:**
- ImagingOpException

- if the transform is non-invertible.

---

### Method Details

#### public final int getInterpolationType()

Returns the interpolation type used by this op.

**Returns:**
- the interpolation type.

**See Also:**
- TYPE_NEAREST_NEIGHBOR

,

TYPE_BILINEAR

,

TYPE_BICUBIC

---

#### public final
BufferedImage
filter​(
BufferedImage
src,

BufferedImage
dst)

Transforms the source

BufferedImage

and stores the results
in the destination

BufferedImage

.
If the color models for the two images do not match, a color
conversion into the destination color model is performed.
If the destination image is null,
a

BufferedImage

is created with the source

ColorModel

.

The coordinates of the rectangle returned by

getBounds2D(BufferedImage)

are not necessarily the same as the coordinates of the

BufferedImage

returned by this method. If the
upper-left corner coordinates of the rectangle are
negative then this part of the rectangle is not drawn. If the
upper-left corner coordinates of the rectangle are positive
then the filtered image is drawn at that position in the
destination

BufferedImage

.

An

IllegalArgumentException

is thrown if the source is
the same as the destination.

**Specified by:**
- filter

in interface

BufferedImageOp

**Parameters:**
- src

- The

BufferedImage

to transform.
- dst

- The

BufferedImage

in which to store the results
of the transformation.

**Returns:**
- The filtered

BufferedImage

.

**Throws:**
- IllegalArgumentException

- if

src

and

dst

are the same
- ImagingOpException

- if the image cannot be transformed
because of a data-processing error that might be
caused by an invalid image format, tile format, or
image-processing operation, or any other unsupported
operation.

---

#### public final
WritableRaster
filter​(
Raster
src,

WritableRaster
dst)

Transforms the source

Raster

and stores the results in
the destination

Raster

. This operation performs the
transform band by band.

If the destination

Raster

is null, a new

Raster

is created.
An

IllegalArgumentException

may be thrown if the source is
the same as the destination or if the number of bands in
the source is not equal to the number of bands in the
destination.

The coordinates of the rectangle returned by

getBounds2D(Raster)

are not necessarily the same as the coordinates of the

WritableRaster

returned by this method. If the
upper-left corner coordinates of rectangle are negative then
this part of the rectangle is not drawn. If the coordinates
of the rectangle are positive then the filtered image is drawn at
that position in the destination

Raster

.

**Specified by:**
- filter

in interface

RasterOp

**Parameters:**
- src

- The

Raster

to transform.
- dst

- The

Raster

in which to store the results of the
transformation.

**Returns:**
- The transformed

Raster

.

**Throws:**
- ImagingOpException

- if the raster cannot be transformed
because of a data-processing error that might be
caused by an invalid image format, tile format, or
image-processing operation, or any other unsupported
operation.

---

#### public final
Rectangle2D
getBounds2D​(
BufferedImage
src)

Returns the bounding box of the transformed destination. The
rectangle returned is the actual bounding box of the
transformed points. The coordinates of the upper-left corner
of the returned rectangle might not be (0, 0).

**Specified by:**
- getBounds2D

in interface

BufferedImageOp

**Parameters:**
- src

- The

BufferedImage

to be transformed.

**Returns:**
- The

Rectangle2D

representing the destination's
bounding box.

---

#### public final
Rectangle2D
getBounds2D​(
Raster
src)

Returns the bounding box of the transformed destination. The
rectangle returned will be the actual bounding box of the
transformed points. The coordinates of the upper-left corner
of the returned rectangle might not be (0, 0).

**Specified by:**
- getBounds2D

in interface

RasterOp

**Parameters:**
- src

- The

Raster

to be transformed.

**Returns:**
- The

Rectangle2D

representing the destination's
bounding box.

---

#### public
BufferedImage
createCompatibleDestImage​(
BufferedImage
src,

ColorModel
destCM)

Creates a zeroed destination image with the correct size and number of
bands. A

RasterFormatException

may be thrown if the
transformed width or height is equal to 0.

If

destCM

is null,
an appropriate

ColorModel

is used; this

ColorModel

may have
an alpha channel even if the source

ColorModel

is opaque.

**Specified by:**
- createCompatibleDestImage

in interface

BufferedImageOp

**Parameters:**
- src

- The

BufferedImage

to be transformed.
- destCM

-

ColorModel

of the destination. If null,
an appropriate

ColorModel

is used.

**Returns:**
- The zeroed destination image.

---

#### public
WritableRaster
createCompatibleDestRaster​(
Raster
src)

Creates a zeroed destination

Raster

with the correct size
and number of bands. A

RasterFormatException

may be thrown
if the transformed width or height is equal to 0.

**Specified by:**
- createCompatibleDestRaster

in interface

RasterOp

**Parameters:**
- src

- The

Raster

to be transformed.

**Returns:**
- The zeroed destination

Raster

.

---

#### public final
Point2D
getPoint2D​(
Point2D
srcPt,

Point2D
dstPt)

Returns the location of the corresponding destination point given a
point in the source. If

dstPt

is specified, it
is used to hold the return value.

**Specified by:**
- getPoint2D

in interface

BufferedImageOp
- getPoint2D

in interface

RasterOp

**Parameters:**
- srcPt

- The

Point2D

that represents the source
point.
- dstPt

- The

Point2D

in which to store the result.

**Returns:**
- The

Point2D

in the destination that corresponds to
the specified point in the source.

---

#### public final
AffineTransform
getTransform()

Returns the affine transform used by this transform operation.

**Returns:**
- The

AffineTransform

associated with this op.

---

#### public final
RenderingHints
getRenderingHints()

Returns the rendering hints used by this transform operation.

**Specified by:**
- getRenderingHints

in interface

BufferedImageOp
- getRenderingHints

in interface

RasterOp

**Returns:**
- The

RenderingHints

object associated with this op.

---

### Additional Sections

#### Class AffineTransformOp

java.lang.Object

- java.awt.image.AffineTransformOp

java.awt.image.AffineTransformOp

**All Implemented Interfaces:** BufferedImageOp

,

RasterOp

```java
public class
AffineTransformOp

extends
Object

implements
BufferedImageOp
,
RasterOp
```

This class uses an affine transform to perform a linear mapping from
2D coordinates in the source image or

Raster

to 2D coordinates
in the destination image or

Raster

.
The type of interpolation that is used is specified through a constructor,
either by a

RenderingHints

object or by one of the integer
interpolation types defined in this class.

If a

RenderingHints

object is specified in the constructor, the
interpolation hint and the rendering quality hint are used to set
the interpolation type for this operation. The color rendering hint
and the dithering hint can be used when color conversion is required.

Note that the following constraints have to be met:

- The source and destination must be different.

For

Raster

objects, the number of bands in the source must
be equal to the number of bands in the destination.

**See Also:** AffineTransform

,

BufferedImageFilter

,

RenderingHints.KEY_INTERPOLATION

,

RenderingHints.KEY_RENDERING

,

RenderingHints.KEY_COLOR_RENDERING

,

RenderingHints.KEY_DITHERING

public class

AffineTransformOp

extends

Object

implements

BufferedImageOp

,

RasterOp

This class uses an affine transform to perform a linear mapping from
2D coordinates in the source image or

Raster

to 2D coordinates
in the destination image or

Raster

.
The type of interpolation that is used is specified through a constructor,
either by a

RenderingHints

object or by one of the integer
interpolation types defined in this class.

If a

RenderingHints

object is specified in the constructor, the
interpolation hint and the rendering quality hint are used to set
the interpolation type for this operation. The color rendering hint
and the dithering hint can be used when color conversion is required.

Note that the following constraints have to be met:

- The source and destination must be different.

For

Raster

objects, the number of bands in the source must
be equal to the number of bands in the destination.

If a

RenderingHints

object is specified in the constructor, the
interpolation hint and the rendering quality hint are used to set
the interpolation type for this operation. The color rendering hint
and the dithering hint can be used when color conversion is required.

Note that the following constraints have to be met:

- The source and destination must be different.

For

Raster

objects, the number of bands in the source must
be equal to the number of bands in the destination.

Note that the following constraints have to be met:

- The source and destination must be different.

For

Raster

objects, the number of bands in the source must
be equal to the number of bands in the destination.

The source and destination must be different.

For

Raster

objects, the number of bands in the source must
be equal to the number of bands in the destination.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

TYPE_BICUBIC

Bicubic interpolation type.

static int

TYPE_BILINEAR

Bilinear interpolation type.

static int

TYPE_NEAREST_NEIGHBOR

Nearest-neighbor interpolation type.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AffineTransformOp

​(

AffineTransform

xform,
int interpolationType)

Constructs an

AffineTransformOp

given an affine transform
and the interpolation type.

AffineTransformOp

​(

AffineTransform

xform,

RenderingHints

hints)

Constructs an

AffineTransformOp

given an affine transform.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

BufferedImage

createCompatibleDestImage

​(

BufferedImage

src,

ColorModel

destCM)

Creates a zeroed destination image with the correct size and number of
bands.

WritableRaster

createCompatibleDestRaster

​(

Raster

src)

Creates a zeroed destination

Raster

with the correct size
and number of bands.

BufferedImage

filter

​(

BufferedImage

src,

BufferedImage

dst)

Transforms the source

BufferedImage

and stores the results
in the destination

BufferedImage

.

WritableRaster

filter

​(

Raster

src,

WritableRaster

dst)

Transforms the source

Raster

and stores the results in
the destination

Raster

.

Rectangle2D

getBounds2D

​(

BufferedImage

src)

Returns the bounding box of the transformed destination.

Rectangle2D

getBounds2D

​(

Raster

src)

Returns the bounding box of the transformed destination.

int

getInterpolationType

()

Returns the interpolation type used by this op.

Point2D

getPoint2D

​(

Point2D

srcPt,

Point2D

dstPt)

Returns the location of the corresponding destination point given a
point in the source.

RenderingHints

getRenderingHints

()

Returns the rendering hints used by this transform operation.

AffineTransform

getTransform

()

Returns the affine transform used by this transform operation.

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

TYPE_BICUBIC

Bicubic interpolation type.

static int

TYPE_BILINEAR

Bilinear interpolation type.

static int

TYPE_NEAREST_NEIGHBOR

Nearest-neighbor interpolation type.

---

#### Field Summary

Bicubic interpolation type.

Bilinear interpolation type.

Nearest-neighbor interpolation type.

Constructor Summary

Constructors

Constructor

Description

AffineTransformOp

​(

AffineTransform

xform,
int interpolationType)

Constructs an

AffineTransformOp

given an affine transform
and the interpolation type.

AffineTransformOp

​(

AffineTransform

xform,

RenderingHints

hints)

Constructs an

AffineTransformOp

given an affine transform.

---

#### Constructor Summary

Constructs an

AffineTransformOp

given an affine transform
and the interpolation type.

Constructs an

AffineTransformOp

given an affine transform.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

BufferedImage

createCompatibleDestImage

​(

BufferedImage

src,

ColorModel

destCM)

Creates a zeroed destination image with the correct size and number of
bands.

WritableRaster

createCompatibleDestRaster

​(

Raster

src)

Creates a zeroed destination

Raster

with the correct size
and number of bands.

BufferedImage

filter

​(

BufferedImage

src,

BufferedImage

dst)

Transforms the source

BufferedImage

and stores the results
in the destination

BufferedImage

.

WritableRaster

filter

​(

Raster

src,

WritableRaster

dst)

Transforms the source

Raster

and stores the results in
the destination

Raster

.

Rectangle2D

getBounds2D

​(

BufferedImage

src)

Returns the bounding box of the transformed destination.

Rectangle2D

getBounds2D

​(

Raster

src)

Returns the bounding box of the transformed destination.

int

getInterpolationType

()

Returns the interpolation type used by this op.

Point2D

getPoint2D

​(

Point2D

srcPt,

Point2D

dstPt)

Returns the location of the corresponding destination point given a
point in the source.

RenderingHints

getRenderingHints

()

Returns the rendering hints used by this transform operation.

AffineTransform

getTransform

()

Returns the affine transform used by this transform operation.

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

Creates a zeroed destination image with the correct size and number of
bands.

Creates a zeroed destination

Raster

with the correct size
and number of bands.

Transforms the source

BufferedImage

and stores the results
in the destination

BufferedImage

.

Transforms the source

Raster

and stores the results in
the destination

Raster

.

Returns the bounding box of the transformed destination.

Returns the interpolation type used by this op.

Returns the location of the corresponding destination point given a
point in the source.

Returns the rendering hints used by this transform operation.

Returns the affine transform used by this transform operation.

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

- TYPE_NEAREST_NEIGHBOR

```java
@Native

public static final int TYPE_NEAREST_NEIGHBOR
```

Nearest-neighbor interpolation type.

**See Also:** Constant Field Values

- TYPE_BILINEAR

```java
@Native

public static final int TYPE_BILINEAR
```

Bilinear interpolation type.

**See Also:** Constant Field Values

- TYPE_BICUBIC

```java
@Native

public static final int TYPE_BICUBIC
```

Bicubic interpolation type.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- AffineTransformOp

```java
public AffineTransformOp​(
AffineTransform
xform,

RenderingHints
hints)
```

Constructs an

AffineTransformOp

given an affine transform.
The interpolation type is determined from the

RenderingHints

object. If the interpolation hint is
defined, it will be used. Otherwise, if the rendering quality hint is
defined, the interpolation type is determined from its value. If no
hints are specified (

hints

is null),
the interpolation type is

TYPE_NEAREST_NEIGHBOR

.

**Parameters:** xform

- The

AffineTransform

to use for the
operation.
**Parameters:** hints

- The

RenderingHints

object used to specify
the interpolation type for the operation.
**Throws:** ImagingOpException

- if the transform is non-invertible.
**See Also:** RenderingHints.KEY_INTERPOLATION

,

RenderingHints.KEY_RENDERING

- AffineTransformOp

```java
public AffineTransformOp​(
AffineTransform
xform,
int interpolationType)
```

Constructs an

AffineTransformOp

given an affine transform
and the interpolation type.

**Parameters:** xform

- The

AffineTransform

to use for the operation.
**Parameters:** interpolationType

- One of the integer
interpolation type constants defined by this class:

TYPE_NEAREST_NEIGHBOR

,

TYPE_BILINEAR

,

TYPE_BICUBIC

.
**Throws:** ImagingOpException

- if the transform is non-invertible.

============ METHOD DETAIL ==========

- Method Detail

- getInterpolationType

```java
public final int getInterpolationType()
```

Returns the interpolation type used by this op.

**Returns:** the interpolation type.
**See Also:** TYPE_NEAREST_NEIGHBOR

,

TYPE_BILINEAR

,

TYPE_BICUBIC

- filter

```java
public final
BufferedImage
filter​(
BufferedImage
src,

BufferedImage
dst)
```

Transforms the source

BufferedImage

and stores the results
in the destination

BufferedImage

.
If the color models for the two images do not match, a color
conversion into the destination color model is performed.
If the destination image is null,
a

BufferedImage

is created with the source

ColorModel

.

The coordinates of the rectangle returned by

getBounds2D(BufferedImage)

are not necessarily the same as the coordinates of the

BufferedImage

returned by this method. If the
upper-left corner coordinates of the rectangle are
negative then this part of the rectangle is not drawn. If the
upper-left corner coordinates of the rectangle are positive
then the filtered image is drawn at that position in the
destination

BufferedImage

.

An

IllegalArgumentException

is thrown if the source is
the same as the destination.

**Specified by:** filter

in interface

BufferedImageOp
**Parameters:** src

- The

BufferedImage

to transform.
**Parameters:** dst

- The

BufferedImage

in which to store the results
of the transformation.
**Returns:** The filtered

BufferedImage

.
**Throws:** IllegalArgumentException

- if

src

and

dst

are the same
**Throws:** ImagingOpException

- if the image cannot be transformed
because of a data-processing error that might be
caused by an invalid image format, tile format, or
image-processing operation, or any other unsupported
operation.

- filter

```java
public final
WritableRaster
filter​(
Raster
src,

WritableRaster
dst)
```

Transforms the source

Raster

and stores the results in
the destination

Raster

. This operation performs the
transform band by band.

If the destination

Raster

is null, a new

Raster

is created.
An

IllegalArgumentException

may be thrown if the source is
the same as the destination or if the number of bands in
the source is not equal to the number of bands in the
destination.

The coordinates of the rectangle returned by

getBounds2D(Raster)

are not necessarily the same as the coordinates of the

WritableRaster

returned by this method. If the
upper-left corner coordinates of rectangle are negative then
this part of the rectangle is not drawn. If the coordinates
of the rectangle are positive then the filtered image is drawn at
that position in the destination

Raster

.

**Specified by:** filter

in interface

RasterOp
**Parameters:** src

- The

Raster

to transform.
**Parameters:** dst

- The

Raster

in which to store the results of the
transformation.
**Returns:** The transformed

Raster

.
**Throws:** ImagingOpException

- if the raster cannot be transformed
because of a data-processing error that might be
caused by an invalid image format, tile format, or
image-processing operation, or any other unsupported
operation.

- getBounds2D

```java
public final
Rectangle2D
getBounds2D​(
BufferedImage
src)
```

Returns the bounding box of the transformed destination. The
rectangle returned is the actual bounding box of the
transformed points. The coordinates of the upper-left corner
of the returned rectangle might not be (0, 0).

**Specified by:** getBounds2D

in interface

BufferedImageOp
**Parameters:** src

- The

BufferedImage

to be transformed.
**Returns:** The

Rectangle2D

representing the destination's
bounding box.

- getBounds2D

```java
public final
Rectangle2D
getBounds2D​(
Raster
src)
```

Returns the bounding box of the transformed destination. The
rectangle returned will be the actual bounding box of the
transformed points. The coordinates of the upper-left corner
of the returned rectangle might not be (0, 0).

**Specified by:** getBounds2D

in interface

RasterOp
**Parameters:** src

- The

Raster

to be transformed.
**Returns:** The

Rectangle2D

representing the destination's
bounding box.

- createCompatibleDestImage

```java
public
BufferedImage
createCompatibleDestImage​(
BufferedImage
src,

ColorModel
destCM)
```

Creates a zeroed destination image with the correct size and number of
bands. A

RasterFormatException

may be thrown if the
transformed width or height is equal to 0.

If

destCM

is null,
an appropriate

ColorModel

is used; this

ColorModel

may have
an alpha channel even if the source

ColorModel

is opaque.

**Specified by:** createCompatibleDestImage

in interface

BufferedImageOp
**Parameters:** src

- The

BufferedImage

to be transformed.
**Parameters:** destCM

-

ColorModel

of the destination. If null,
an appropriate

ColorModel

is used.
**Returns:** The zeroed destination image.

- createCompatibleDestRaster

```java
public
WritableRaster
createCompatibleDestRaster​(
Raster
src)
```

Creates a zeroed destination

Raster

with the correct size
and number of bands. A

RasterFormatException

may be thrown
if the transformed width or height is equal to 0.

**Specified by:** createCompatibleDestRaster

in interface

RasterOp
**Parameters:** src

- The

Raster

to be transformed.
**Returns:** The zeroed destination

Raster

.

- getPoint2D

```java
public final
Point2D
getPoint2D​(
Point2D
srcPt,

Point2D
dstPt)
```

Returns the location of the corresponding destination point given a
point in the source. If

dstPt

is specified, it
is used to hold the return value.

**Specified by:** getPoint2D

in interface

BufferedImageOp
**Specified by:** getPoint2D

in interface

RasterOp
**Parameters:** srcPt

- The

Point2D

that represents the source
point.
**Parameters:** dstPt

- The

Point2D

in which to store the result.
**Returns:** The

Point2D

in the destination that corresponds to
the specified point in the source.

- getTransform

```java
public final
AffineTransform
getTransform()
```

Returns the affine transform used by this transform operation.

**Returns:** The

AffineTransform

associated with this op.

- getRenderingHints

```java
public final
RenderingHints
getRenderingHints()
```

Returns the rendering hints used by this transform operation.

**Specified by:** getRenderingHints

in interface

BufferedImageOp
**Specified by:** getRenderingHints

in interface

RasterOp
**Returns:** The

RenderingHints

object associated with this op.

Field Detail

- TYPE_NEAREST_NEIGHBOR

```java
@Native

public static final int TYPE_NEAREST_NEIGHBOR
```

Nearest-neighbor interpolation type.

**See Also:** Constant Field Values

- TYPE_BILINEAR

```java
@Native

public static final int TYPE_BILINEAR
```

Bilinear interpolation type.

**See Also:** Constant Field Values

- TYPE_BICUBIC

```java
@Native

public static final int TYPE_BICUBIC
```

Bicubic interpolation type.

**See Also:** Constant Field Values

---

#### Field Detail

TYPE_NEAREST_NEIGHBOR

```java
@Native

public static final int TYPE_NEAREST_NEIGHBOR
```

Nearest-neighbor interpolation type.

**See Also:** Constant Field Values

---

#### TYPE_NEAREST_NEIGHBOR

@Native

public static final int TYPE_NEAREST_NEIGHBOR

Nearest-neighbor interpolation type.

TYPE_BILINEAR

```java
@Native

public static final int TYPE_BILINEAR
```

Bilinear interpolation type.

**See Also:** Constant Field Values

---

#### TYPE_BILINEAR

@Native

public static final int TYPE_BILINEAR

Bilinear interpolation type.

TYPE_BICUBIC

```java
@Native

public static final int TYPE_BICUBIC
```

Bicubic interpolation type.

**See Also:** Constant Field Values

---

#### TYPE_BICUBIC

@Native

public static final int TYPE_BICUBIC

Bicubic interpolation type.

Constructor Detail

- AffineTransformOp

```java
public AffineTransformOp​(
AffineTransform
xform,

RenderingHints
hints)
```

Constructs an

AffineTransformOp

given an affine transform.
The interpolation type is determined from the

RenderingHints

object. If the interpolation hint is
defined, it will be used. Otherwise, if the rendering quality hint is
defined, the interpolation type is determined from its value. If no
hints are specified (

hints

is null),
the interpolation type is

TYPE_NEAREST_NEIGHBOR

.

**Parameters:** xform

- The

AffineTransform

to use for the
operation.
**Parameters:** hints

- The

RenderingHints

object used to specify
the interpolation type for the operation.
**Throws:** ImagingOpException

- if the transform is non-invertible.
**See Also:** RenderingHints.KEY_INTERPOLATION

,

RenderingHints.KEY_RENDERING

- AffineTransformOp

```java
public AffineTransformOp​(
AffineTransform
xform,
int interpolationType)
```

Constructs an

AffineTransformOp

given an affine transform
and the interpolation type.

**Parameters:** xform

- The

AffineTransform

to use for the operation.
**Parameters:** interpolationType

- One of the integer
interpolation type constants defined by this class:

TYPE_NEAREST_NEIGHBOR

,

TYPE_BILINEAR

,

TYPE_BICUBIC

.
**Throws:** ImagingOpException

- if the transform is non-invertible.

---

#### Constructor Detail

AffineTransformOp

```java
public AffineTransformOp​(
AffineTransform
xform,

RenderingHints
hints)
```

Constructs an

AffineTransformOp

given an affine transform.
The interpolation type is determined from the

RenderingHints

object. If the interpolation hint is
defined, it will be used. Otherwise, if the rendering quality hint is
defined, the interpolation type is determined from its value. If no
hints are specified (

hints

is null),
the interpolation type is

TYPE_NEAREST_NEIGHBOR

.

**Parameters:** xform

- The

AffineTransform

to use for the
operation.
**Parameters:** hints

- The

RenderingHints

object used to specify
the interpolation type for the operation.
**Throws:** ImagingOpException

- if the transform is non-invertible.
**See Also:** RenderingHints.KEY_INTERPOLATION

,

RenderingHints.KEY_RENDERING

---

#### AffineTransformOp

public AffineTransformOp​(

AffineTransform

xform,

RenderingHints

hints)

Constructs an

AffineTransformOp

given an affine transform.
The interpolation type is determined from the

RenderingHints

object. If the interpolation hint is
defined, it will be used. Otherwise, if the rendering quality hint is
defined, the interpolation type is determined from its value. If no
hints are specified (

hints

is null),
the interpolation type is

TYPE_NEAREST_NEIGHBOR

.

AffineTransformOp

```java
public AffineTransformOp​(
AffineTransform
xform,
int interpolationType)
```

Constructs an

AffineTransformOp

given an affine transform
and the interpolation type.

**Parameters:** xform

- The

AffineTransform

to use for the operation.
**Parameters:** interpolationType

- One of the integer
interpolation type constants defined by this class:

TYPE_NEAREST_NEIGHBOR

,

TYPE_BILINEAR

,

TYPE_BICUBIC

.
**Throws:** ImagingOpException

- if the transform is non-invertible.

---

#### AffineTransformOp

public AffineTransformOp​(

AffineTransform

xform,
int interpolationType)

Constructs an

AffineTransformOp

given an affine transform
and the interpolation type.

Method Detail

- getInterpolationType

```java
public final int getInterpolationType()
```

Returns the interpolation type used by this op.

**Returns:** the interpolation type.
**See Also:** TYPE_NEAREST_NEIGHBOR

,

TYPE_BILINEAR

,

TYPE_BICUBIC

- filter

```java
public final
BufferedImage
filter​(
BufferedImage
src,

BufferedImage
dst)
```

Transforms the source

BufferedImage

and stores the results
in the destination

BufferedImage

.
If the color models for the two images do not match, a color
conversion into the destination color model is performed.
If the destination image is null,
a

BufferedImage

is created with the source

ColorModel

.

The coordinates of the rectangle returned by

getBounds2D(BufferedImage)

are not necessarily the same as the coordinates of the

BufferedImage

returned by this method. If the
upper-left corner coordinates of the rectangle are
negative then this part of the rectangle is not drawn. If the
upper-left corner coordinates of the rectangle are positive
then the filtered image is drawn at that position in the
destination

BufferedImage

.

An

IllegalArgumentException

is thrown if the source is
the same as the destination.

**Specified by:** filter

in interface

BufferedImageOp
**Parameters:** src

- The

BufferedImage

to transform.
**Parameters:** dst

- The

BufferedImage

in which to store the results
of the transformation.
**Returns:** The filtered

BufferedImage

.
**Throws:** IllegalArgumentException

- if

src

and

dst

are the same
**Throws:** ImagingOpException

- if the image cannot be transformed
because of a data-processing error that might be
caused by an invalid image format, tile format, or
image-processing operation, or any other unsupported
operation.

- filter

```java
public final
WritableRaster
filter​(
Raster
src,

WritableRaster
dst)
```

Transforms the source

Raster

and stores the results in
the destination

Raster

. This operation performs the
transform band by band.

If the destination

Raster

is null, a new

Raster

is created.
An

IllegalArgumentException

may be thrown if the source is
the same as the destination or if the number of bands in
the source is not equal to the number of bands in the
destination.

The coordinates of the rectangle returned by

getBounds2D(Raster)

are not necessarily the same as the coordinates of the

WritableRaster

returned by this method. If the
upper-left corner coordinates of rectangle are negative then
this part of the rectangle is not drawn. If the coordinates
of the rectangle are positive then the filtered image is drawn at
that position in the destination

Raster

.

**Specified by:** filter

in interface

RasterOp
**Parameters:** src

- The

Raster

to transform.
**Parameters:** dst

- The

Raster

in which to store the results of the
transformation.
**Returns:** The transformed

Raster

.
**Throws:** ImagingOpException

- if the raster cannot be transformed
because of a data-processing error that might be
caused by an invalid image format, tile format, or
image-processing operation, or any other unsupported
operation.

- getBounds2D

```java
public final
Rectangle2D
getBounds2D​(
BufferedImage
src)
```

Returns the bounding box of the transformed destination. The
rectangle returned is the actual bounding box of the
transformed points. The coordinates of the upper-left corner
of the returned rectangle might not be (0, 0).

**Specified by:** getBounds2D

in interface

BufferedImageOp
**Parameters:** src

- The

BufferedImage

to be transformed.
**Returns:** The

Rectangle2D

representing the destination's
bounding box.

- getBounds2D

```java
public final
Rectangle2D
getBounds2D​(
Raster
src)
```

Returns the bounding box of the transformed destination. The
rectangle returned will be the actual bounding box of the
transformed points. The coordinates of the upper-left corner
of the returned rectangle might not be (0, 0).

**Specified by:** getBounds2D

in interface

RasterOp
**Parameters:** src

- The

Raster

to be transformed.
**Returns:** The

Rectangle2D

representing the destination's
bounding box.

- createCompatibleDestImage

```java
public
BufferedImage
createCompatibleDestImage​(
BufferedImage
src,

ColorModel
destCM)
```

Creates a zeroed destination image with the correct size and number of
bands. A

RasterFormatException

may be thrown if the
transformed width or height is equal to 0.

If

destCM

is null,
an appropriate

ColorModel

is used; this

ColorModel

may have
an alpha channel even if the source

ColorModel

is opaque.

**Specified by:** createCompatibleDestImage

in interface

BufferedImageOp
**Parameters:** src

- The

BufferedImage

to be transformed.
**Parameters:** destCM

-

ColorModel

of the destination. If null,
an appropriate

ColorModel

is used.
**Returns:** The zeroed destination image.

- createCompatibleDestRaster

```java
public
WritableRaster
createCompatibleDestRaster​(
Raster
src)
```

Creates a zeroed destination

Raster

with the correct size
and number of bands. A

RasterFormatException

may be thrown
if the transformed width or height is equal to 0.

**Specified by:** createCompatibleDestRaster

in interface

RasterOp
**Parameters:** src

- The

Raster

to be transformed.
**Returns:** The zeroed destination

Raster

.

- getPoint2D

```java
public final
Point2D
getPoint2D​(
Point2D
srcPt,

Point2D
dstPt)
```

Returns the location of the corresponding destination point given a
point in the source. If

dstPt

is specified, it
is used to hold the return value.

**Specified by:** getPoint2D

in interface

BufferedImageOp
**Specified by:** getPoint2D

in interface

RasterOp
**Parameters:** srcPt

- The

Point2D

that represents the source
point.
**Parameters:** dstPt

- The

Point2D

in which to store the result.
**Returns:** The

Point2D

in the destination that corresponds to
the specified point in the source.

- getTransform

```java
public final
AffineTransform
getTransform()
```

Returns the affine transform used by this transform operation.

**Returns:** The

AffineTransform

associated with this op.

- getRenderingHints

```java
public final
RenderingHints
getRenderingHints()
```

Returns the rendering hints used by this transform operation.

**Specified by:** getRenderingHints

in interface

BufferedImageOp
**Specified by:** getRenderingHints

in interface

RasterOp
**Returns:** The

RenderingHints

object associated with this op.

---

#### Method Detail

getInterpolationType

```java
public final int getInterpolationType()
```

Returns the interpolation type used by this op.

**Returns:** the interpolation type.
**See Also:** TYPE_NEAREST_NEIGHBOR

,

TYPE_BILINEAR

,

TYPE_BICUBIC

---

#### getInterpolationType

public final int getInterpolationType()

Returns the interpolation type used by this op.

filter

```java
public final
BufferedImage
filter​(
BufferedImage
src,

BufferedImage
dst)
```

Transforms the source

BufferedImage

and stores the results
in the destination

BufferedImage

.
If the color models for the two images do not match, a color
conversion into the destination color model is performed.
If the destination image is null,
a

BufferedImage

is created with the source

ColorModel

.

The coordinates of the rectangle returned by

getBounds2D(BufferedImage)

are not necessarily the same as the coordinates of the

BufferedImage

returned by this method. If the
upper-left corner coordinates of the rectangle are
negative then this part of the rectangle is not drawn. If the
upper-left corner coordinates of the rectangle are positive
then the filtered image is drawn at that position in the
destination

BufferedImage

.

An

IllegalArgumentException

is thrown if the source is
the same as the destination.

**Specified by:** filter

in interface

BufferedImageOp
**Parameters:** src

- The

BufferedImage

to transform.
**Parameters:** dst

- The

BufferedImage

in which to store the results
of the transformation.
**Returns:** The filtered

BufferedImage

.
**Throws:** IllegalArgumentException

- if

src

and

dst

are the same
**Throws:** ImagingOpException

- if the image cannot be transformed
because of a data-processing error that might be
caused by an invalid image format, tile format, or
image-processing operation, or any other unsupported
operation.

---

#### filter

public final

BufferedImage

filter​(

BufferedImage

src,

BufferedImage

dst)

Transforms the source

BufferedImage

and stores the results
in the destination

BufferedImage

.
If the color models for the two images do not match, a color
conversion into the destination color model is performed.
If the destination image is null,
a

BufferedImage

is created with the source

ColorModel

.

The coordinates of the rectangle returned by

getBounds2D(BufferedImage)

are not necessarily the same as the coordinates of the

BufferedImage

returned by this method. If the
upper-left corner coordinates of the rectangle are
negative then this part of the rectangle is not drawn. If the
upper-left corner coordinates of the rectangle are positive
then the filtered image is drawn at that position in the
destination

BufferedImage

.

An

IllegalArgumentException

is thrown if the source is
the same as the destination.

The coordinates of the rectangle returned by

getBounds2D(BufferedImage)

are not necessarily the same as the coordinates of the

BufferedImage

returned by this method. If the
upper-left corner coordinates of the rectangle are
negative then this part of the rectangle is not drawn. If the
upper-left corner coordinates of the rectangle are positive
then the filtered image is drawn at that position in the
destination

BufferedImage

.

An

IllegalArgumentException

is thrown if the source is
the same as the destination.

An

IllegalArgumentException

is thrown if the source is
the same as the destination.

filter

```java
public final
WritableRaster
filter​(
Raster
src,

WritableRaster
dst)
```

Transforms the source

Raster

and stores the results in
the destination

Raster

. This operation performs the
transform band by band.

If the destination

Raster

is null, a new

Raster

is created.
An

IllegalArgumentException

may be thrown if the source is
the same as the destination or if the number of bands in
the source is not equal to the number of bands in the
destination.

The coordinates of the rectangle returned by

getBounds2D(Raster)

are not necessarily the same as the coordinates of the

WritableRaster

returned by this method. If the
upper-left corner coordinates of rectangle are negative then
this part of the rectangle is not drawn. If the coordinates
of the rectangle are positive then the filtered image is drawn at
that position in the destination

Raster

.

**Specified by:** filter

in interface

RasterOp
**Parameters:** src

- The

Raster

to transform.
**Parameters:** dst

- The

Raster

in which to store the results of the
transformation.
**Returns:** The transformed

Raster

.
**Throws:** ImagingOpException

- if the raster cannot be transformed
because of a data-processing error that might be
caused by an invalid image format, tile format, or
image-processing operation, or any other unsupported
operation.

---

#### filter

public final

WritableRaster

filter​(

Raster

src,

WritableRaster

dst)

Transforms the source

Raster

and stores the results in
the destination

Raster

. This operation performs the
transform band by band.

If the destination

Raster

is null, a new

Raster

is created.
An

IllegalArgumentException

may be thrown if the source is
the same as the destination or if the number of bands in
the source is not equal to the number of bands in the
destination.

The coordinates of the rectangle returned by

getBounds2D(Raster)

are not necessarily the same as the coordinates of the

WritableRaster

returned by this method. If the
upper-left corner coordinates of rectangle are negative then
this part of the rectangle is not drawn. If the coordinates
of the rectangle are positive then the filtered image is drawn at
that position in the destination

Raster

.

If the destination

Raster

is null, a new

Raster

is created.
An

IllegalArgumentException

may be thrown if the source is
the same as the destination or if the number of bands in
the source is not equal to the number of bands in the
destination.

The coordinates of the rectangle returned by

getBounds2D(Raster)

are not necessarily the same as the coordinates of the

WritableRaster

returned by this method. If the
upper-left corner coordinates of rectangle are negative then
this part of the rectangle is not drawn. If the coordinates
of the rectangle are positive then the filtered image is drawn at
that position in the destination

Raster

.

The coordinates of the rectangle returned by

getBounds2D(Raster)

are not necessarily the same as the coordinates of the

WritableRaster

returned by this method. If the
upper-left corner coordinates of rectangle are negative then
this part of the rectangle is not drawn. If the coordinates
of the rectangle are positive then the filtered image is drawn at
that position in the destination

Raster

.

getBounds2D

```java
public final
Rectangle2D
getBounds2D​(
BufferedImage
src)
```

Returns the bounding box of the transformed destination. The
rectangle returned is the actual bounding box of the
transformed points. The coordinates of the upper-left corner
of the returned rectangle might not be (0, 0).

**Specified by:** getBounds2D

in interface

BufferedImageOp
**Parameters:** src

- The

BufferedImage

to be transformed.
**Returns:** The

Rectangle2D

representing the destination's
bounding box.

---

#### getBounds2D

public final

Rectangle2D

getBounds2D​(

BufferedImage

src)

Returns the bounding box of the transformed destination. The
rectangle returned is the actual bounding box of the
transformed points. The coordinates of the upper-left corner
of the returned rectangle might not be (0, 0).

getBounds2D

```java
public final
Rectangle2D
getBounds2D​(
Raster
src)
```

Returns the bounding box of the transformed destination. The
rectangle returned will be the actual bounding box of the
transformed points. The coordinates of the upper-left corner
of the returned rectangle might not be (0, 0).

**Specified by:** getBounds2D

in interface

RasterOp
**Parameters:** src

- The

Raster

to be transformed.
**Returns:** The

Rectangle2D

representing the destination's
bounding box.

---

#### getBounds2D

public final

Rectangle2D

getBounds2D​(

Raster

src)

Returns the bounding box of the transformed destination. The
rectangle returned will be the actual bounding box of the
transformed points. The coordinates of the upper-left corner
of the returned rectangle might not be (0, 0).

createCompatibleDestImage

```java
public
BufferedImage
createCompatibleDestImage​(
BufferedImage
src,

ColorModel
destCM)
```

Creates a zeroed destination image with the correct size and number of
bands. A

RasterFormatException

may be thrown if the
transformed width or height is equal to 0.

If

destCM

is null,
an appropriate

ColorModel

is used; this

ColorModel

may have
an alpha channel even if the source

ColorModel

is opaque.

**Specified by:** createCompatibleDestImage

in interface

BufferedImageOp
**Parameters:** src

- The

BufferedImage

to be transformed.
**Parameters:** destCM

-

ColorModel

of the destination. If null,
an appropriate

ColorModel

is used.
**Returns:** The zeroed destination image.

---

#### createCompatibleDestImage

public

BufferedImage

createCompatibleDestImage​(

BufferedImage

src,

ColorModel

destCM)

Creates a zeroed destination image with the correct size and number of
bands. A

RasterFormatException

may be thrown if the
transformed width or height is equal to 0.

If

destCM

is null,
an appropriate

ColorModel

is used; this

ColorModel

may have
an alpha channel even if the source

ColorModel

is opaque.

If

destCM

is null,
an appropriate

ColorModel

is used; this

ColorModel

may have
an alpha channel even if the source

ColorModel

is opaque.

createCompatibleDestRaster

```java
public
WritableRaster
createCompatibleDestRaster​(
Raster
src)
```

Creates a zeroed destination

Raster

with the correct size
and number of bands. A

RasterFormatException

may be thrown
if the transformed width or height is equal to 0.

**Specified by:** createCompatibleDestRaster

in interface

RasterOp
**Parameters:** src

- The

Raster

to be transformed.
**Returns:** The zeroed destination

Raster

.

---

#### createCompatibleDestRaster

public

WritableRaster

createCompatibleDestRaster​(

Raster

src)

Creates a zeroed destination

Raster

with the correct size
and number of bands. A

RasterFormatException

may be thrown
if the transformed width or height is equal to 0.

getPoint2D

```java
public final
Point2D
getPoint2D​(
Point2D
srcPt,

Point2D
dstPt)
```

Returns the location of the corresponding destination point given a
point in the source. If

dstPt

is specified, it
is used to hold the return value.

**Specified by:** getPoint2D

in interface

BufferedImageOp
**Specified by:** getPoint2D

in interface

RasterOp
**Parameters:** srcPt

- The

Point2D

that represents the source
point.
**Parameters:** dstPt

- The

Point2D

in which to store the result.
**Returns:** The

Point2D

in the destination that corresponds to
the specified point in the source.

---

#### getPoint2D

public final

Point2D

getPoint2D​(

Point2D

srcPt,

Point2D

dstPt)

Returns the location of the corresponding destination point given a
point in the source. If

dstPt

is specified, it
is used to hold the return value.

getTransform

```java
public final
AffineTransform
getTransform()
```

Returns the affine transform used by this transform operation.

**Returns:** The

AffineTransform

associated with this op.

---

#### getTransform

public final

AffineTransform

getTransform()

Returns the affine transform used by this transform operation.

getRenderingHints

```java
public final
RenderingHints
getRenderingHints()
```

Returns the rendering hints used by this transform operation.

**Specified by:** getRenderingHints

in interface

BufferedImageOp
**Specified by:** getRenderingHints

in interface

RasterOp
**Returns:** The

RenderingHints

object associated with this op.

---

#### getRenderingHints

public final

RenderingHints

getRenderingHints()

Returns the rendering hints used by this transform operation.

---

