# Class RescaleOp

**Source:** `java.desktop\java\awt\image\RescaleOp.html`

### Class Description

```java
public class
RescaleOp

extends
Object

implements
BufferedImageOp
,
RasterOp
```

This class performs a pixel-by-pixel rescaling of the data in the
source image by multiplying the sample values for each pixel by a scale
factor and then adding an offset. The scaled sample values are clipped
to the minimum/maximum representable in the destination image.

The pseudo code for the rescaling operation is as follows:

```java
for each pixel from Source object {
for each band/component of the pixel {
dstElement = (srcElement*scaleFactor) + offset
}
}
```

For Rasters, rescaling operates on bands. The number of
sets of scaling constants may be one, in which case the same constants
are applied to all bands, or it must equal the number of Source
Raster bands.

For BufferedImages, rescaling operates on color and alpha components.
The number of sets of scaling constants may be one, in which case the
same constants are applied to all color (but not alpha) components.
Otherwise, the number of sets of scaling constants may
equal the number of Source color components, in which case no
rescaling of the alpha component (if present) is performed.
If neither of these cases apply, the number of sets of scaling constants
must equal the number of Source color components plus alpha components,
in which case all color and alpha components are rescaled.

BufferedImage sources with premultiplied alpha data are treated in the same
manner as non-premultiplied images for purposes of rescaling. That is,
the rescaling is done per band on the raw data of the BufferedImage source
without regard to whether the data is premultiplied. If a color conversion
is required to the destination ColorModel, the premultiplied state of
both source and destination will be taken into account for this step.

Images with an IndexColorModel cannot be rescaled.

If a RenderingHints object is specified in the constructor, the
color rendering hint and the dithering hint may be used when color
conversion is required.

Note that in-place operation is allowed (i.e. the source and destination can
be the same object).

**All Implemented Interfaces:** BufferedImageOp

,

RasterOp

---

### Field Details

*No entries found.*

### Constructor Details

#### public RescaleOp​(float[] scaleFactors,
float[] offsets,

RenderingHints
hints)

Constructs a new RescaleOp with the desired scale factors
and offsets. The length of the scaleFactor and offset arrays
must meet the restrictions stated in the class comments above.
The RenderingHints argument may be null.

**Parameters:**
- scaleFactors

- the specified scale factors
- offsets

- the specified offsets
- hints

- the specified

RenderingHints

, or

null

---

#### public RescaleOp​(float scaleFactor,
float offset,

RenderingHints
hints)

Constructs a new RescaleOp with the desired scale factor
and offset. The scaleFactor and offset will be applied to
all bands in a source Raster and to all color (but not alpha)
components in a BufferedImage.
The RenderingHints argument may be null.

**Parameters:**
- scaleFactor

- the specified scale factor
- offset

- the specified offset
- hints

- the specified

RenderingHints

, or

null

---

### Method Details

#### public final float[] getScaleFactors​(float[] scaleFactors)

Returns the scale factors in the given array. The array is also
returned for convenience. If scaleFactors is null, a new array
will be allocated.

**Parameters:**
- scaleFactors

- the array to contain the scale factors of
this

RescaleOp

**Returns:**
- the scale factors of this

RescaleOp

.

---

#### public final float[] getOffsets​(float[] offsets)

Returns the offsets in the given array. The array is also returned
for convenience. If offsets is null, a new array
will be allocated.

**Parameters:**
- offsets

- the array to contain the offsets of
this

RescaleOp

**Returns:**
- the offsets of this

RescaleOp

.

---

#### public final int getNumFactors()

Returns the number of scaling factors and offsets used in this
RescaleOp.

**Returns:**
- the number of scaling factors and offsets of this

RescaleOp

.

---

#### public final
BufferedImage
filter​(
BufferedImage
src,

BufferedImage
dst)

Rescales the source BufferedImage.
If the color model in the source image is not the same as that
in the destination image, the pixels will be converted
in the destination. If the destination image is null,
a BufferedImage will be created with the source ColorModel.
An IllegalArgumentException may be thrown if the number of
scaling factors/offsets in this object does not meet the
restrictions stated in the class comments above, or if the
source image has an IndexColorModel.

**Specified by:**
- filter

in interface

BufferedImageOp

**Parameters:**
- src

- the

BufferedImage

to be filtered
- dst

- the destination for the filtering operation
or

null

**Returns:**
- the filtered

BufferedImage

.

**Throws:**
- IllegalArgumentException

- if the

ColorModel

of

src

is an

IndexColorModel

,
or if the number of scaling factors and offsets in this

RescaleOp

do not meet the requirements
stated in the class comments, or if the source and
destination images differ in size.

---

#### public final
WritableRaster
filter​(
Raster
src,

WritableRaster
dst)

Rescales the pixel data in the source Raster.
If the destination Raster is null, a new Raster will be created.
The source and destination must have the same number of bands.
Otherwise, an IllegalArgumentException is thrown.
Note that the number of scaling factors/offsets in this object must
meet the restrictions stated in the class comments above.
Otherwise, an IllegalArgumentException is thrown.

**Specified by:**
- filter

in interface

RasterOp

**Parameters:**
- src

- the

Raster

to be filtered
- dst

- the destination for the filtering operation
or

null

**Returns:**
- the filtered

WritableRaster

.

**Throws:**
- IllegalArgumentException

- if

src

and

dst

do not have the same number of bands,
or if the number of scaling factors and offsets in this

RescaleOp

do not meet the requirements
stated in the class comments, or if the source and
destination rasters differ in size.

---

#### public final
Rectangle2D
getBounds2D​(
BufferedImage
src)

Returns the bounding box of the rescaled destination image. Since
this is not a geometric operation, the bounding box does not
change.

**Specified by:**
- getBounds2D

in interface

BufferedImageOp

**Parameters:**
- src

- The

BufferedImage

to be filtered

**Returns:**
- The

Rectangle2D

representing the destination
image's bounding box.

---

#### public final
Rectangle2D
getBounds2D​(
Raster
src)

Returns the bounding box of the rescaled destination Raster. Since
this is not a geometric operation, the bounding box does not
change.

**Specified by:**
- getBounds2D

in interface

RasterOp

**Parameters:**
- src

- the rescaled destination

Raster

**Returns:**
- the bounds of the specified

Raster

.

---

#### public
BufferedImage
createCompatibleDestImage​(
BufferedImage
src,

ColorModel
destCM)

Creates a zeroed destination image with the correct size and number of
bands.

**Specified by:**
- createCompatibleDestImage

in interface

BufferedImageOp

**Parameters:**
- src

- Source image for the filter operation.
- destCM

- ColorModel of the destination. If null, the
ColorModel of the source will be used.

**Returns:**
- the zeroed-destination image.

---

#### public
WritableRaster
createCompatibleDestRaster​(
Raster
src)

Creates a zeroed-destination

Raster

with the correct
size and number of bands, given this source.

**Specified by:**
- createCompatibleDestRaster

in interface

RasterOp

**Parameters:**
- src

- the source

Raster

**Returns:**
- the zeroed-destination

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

Returns the location of the destination point given a
point in the source. If dstPt is non-null, it will
be used to hold the return value. Since this is not a geometric
operation, the srcPt will equal the dstPt.

**Specified by:**
- getPoint2D

in interface

BufferedImageOp
- getPoint2D

in interface

RasterOp

**Parameters:**
- srcPt

- a point in the source image
- dstPt

- the destination point or

null

**Returns:**
- the location of the destination point.

---

#### public final
RenderingHints
getRenderingHints()

Returns the rendering hints for this op.

**Specified by:**
- getRenderingHints

in interface

BufferedImageOp
- getRenderingHints

in interface

RasterOp

**Returns:**
- the rendering hints of this

RescaleOp

.

---

### Additional Sections

#### Class RescaleOp

java.lang.Object

- java.awt.image.RescaleOp

java.awt.image.RescaleOp

**All Implemented Interfaces:** BufferedImageOp

,

RasterOp

```java
public class
RescaleOp

extends
Object

implements
BufferedImageOp
,
RasterOp
```

This class performs a pixel-by-pixel rescaling of the data in the
source image by multiplying the sample values for each pixel by a scale
factor and then adding an offset. The scaled sample values are clipped
to the minimum/maximum representable in the destination image.

The pseudo code for the rescaling operation is as follows:

```java
for each pixel from Source object {
for each band/component of the pixel {
dstElement = (srcElement*scaleFactor) + offset
}
}
```

For Rasters, rescaling operates on bands. The number of
sets of scaling constants may be one, in which case the same constants
are applied to all bands, or it must equal the number of Source
Raster bands.

For BufferedImages, rescaling operates on color and alpha components.
The number of sets of scaling constants may be one, in which case the
same constants are applied to all color (but not alpha) components.
Otherwise, the number of sets of scaling constants may
equal the number of Source color components, in which case no
rescaling of the alpha component (if present) is performed.
If neither of these cases apply, the number of sets of scaling constants
must equal the number of Source color components plus alpha components,
in which case all color and alpha components are rescaled.

BufferedImage sources with premultiplied alpha data are treated in the same
manner as non-premultiplied images for purposes of rescaling. That is,
the rescaling is done per band on the raw data of the BufferedImage source
without regard to whether the data is premultiplied. If a color conversion
is required to the destination ColorModel, the premultiplied state of
both source and destination will be taken into account for this step.

Images with an IndexColorModel cannot be rescaled.

If a RenderingHints object is specified in the constructor, the
color rendering hint and the dithering hint may be used when color
conversion is required.

Note that in-place operation is allowed (i.e. the source and destination can
be the same object).

**See Also:** RenderingHints.KEY_COLOR_RENDERING

,

RenderingHints.KEY_DITHERING

public class

RescaleOp

extends

Object

implements

BufferedImageOp

,

RasterOp

This class performs a pixel-by-pixel rescaling of the data in the
source image by multiplying the sample values for each pixel by a scale
factor and then adding an offset. The scaled sample values are clipped
to the minimum/maximum representable in the destination image.

The pseudo code for the rescaling operation is as follows:

```java
for each pixel from Source object {
for each band/component of the pixel {
dstElement = (srcElement*scaleFactor) + offset
}
}
```

For Rasters, rescaling operates on bands. The number of
sets of scaling constants may be one, in which case the same constants
are applied to all bands, or it must equal the number of Source
Raster bands.

For BufferedImages, rescaling operates on color and alpha components.
The number of sets of scaling constants may be one, in which case the
same constants are applied to all color (but not alpha) components.
Otherwise, the number of sets of scaling constants may
equal the number of Source color components, in which case no
rescaling of the alpha component (if present) is performed.
If neither of these cases apply, the number of sets of scaling constants
must equal the number of Source color components plus alpha components,
in which case all color and alpha components are rescaled.

BufferedImage sources with premultiplied alpha data are treated in the same
manner as non-premultiplied images for purposes of rescaling. That is,
the rescaling is done per band on the raw data of the BufferedImage source
without regard to whether the data is premultiplied. If a color conversion
is required to the destination ColorModel, the premultiplied state of
both source and destination will be taken into account for this step.

Images with an IndexColorModel cannot be rescaled.

If a RenderingHints object is specified in the constructor, the
color rendering hint and the dithering hint may be used when color
conversion is required.

Note that in-place operation is allowed (i.e. the source and destination can
be the same object).

The pseudo code for the rescaling operation is as follows:

```java
for each pixel from Source object {
for each band/component of the pixel {
dstElement = (srcElement*scaleFactor) + offset
}
}
```

For Rasters, rescaling operates on bands. The number of
sets of scaling constants may be one, in which case the same constants
are applied to all bands, or it must equal the number of Source
Raster bands.

For BufferedImages, rescaling operates on color and alpha components.
The number of sets of scaling constants may be one, in which case the
same constants are applied to all color (but not alpha) components.
Otherwise, the number of sets of scaling constants may
equal the number of Source color components, in which case no
rescaling of the alpha component (if present) is performed.
If neither of these cases apply, the number of sets of scaling constants
must equal the number of Source color components plus alpha components,
in which case all color and alpha components are rescaled.

BufferedImage sources with premultiplied alpha data are treated in the same
manner as non-premultiplied images for purposes of rescaling. That is,
the rescaling is done per band on the raw data of the BufferedImage source
without regard to whether the data is premultiplied. If a color conversion
is required to the destination ColorModel, the premultiplied state of
both source and destination will be taken into account for this step.

Images with an IndexColorModel cannot be rescaled.

If a RenderingHints object is specified in the constructor, the
color rendering hint and the dithering hint may be used when color
conversion is required.

Note that in-place operation is allowed (i.e. the source and destination can
be the same object).

for each pixel from Source object {
for each band/component of the pixel {
dstElement = (srcElement*scaleFactor) + offset
}
}

For Rasters, rescaling operates on bands. The number of
sets of scaling constants may be one, in which case the same constants
are applied to all bands, or it must equal the number of Source
Raster bands.

For BufferedImages, rescaling operates on color and alpha components.
The number of sets of scaling constants may be one, in which case the
same constants are applied to all color (but not alpha) components.
Otherwise, the number of sets of scaling constants may
equal the number of Source color components, in which case no
rescaling of the alpha component (if present) is performed.
If neither of these cases apply, the number of sets of scaling constants
must equal the number of Source color components plus alpha components,
in which case all color and alpha components are rescaled.

BufferedImage sources with premultiplied alpha data are treated in the same
manner as non-premultiplied images for purposes of rescaling. That is,
the rescaling is done per band on the raw data of the BufferedImage source
without regard to whether the data is premultiplied. If a color conversion
is required to the destination ColorModel, the premultiplied state of
both source and destination will be taken into account for this step.

Images with an IndexColorModel cannot be rescaled.

If a RenderingHints object is specified in the constructor, the
color rendering hint and the dithering hint may be used when color
conversion is required.

Note that in-place operation is allowed (i.e. the source and destination can
be the same object).

For BufferedImages, rescaling operates on color and alpha components.
The number of sets of scaling constants may be one, in which case the
same constants are applied to all color (but not alpha) components.
Otherwise, the number of sets of scaling constants may
equal the number of Source color components, in which case no
rescaling of the alpha component (if present) is performed.
If neither of these cases apply, the number of sets of scaling constants
must equal the number of Source color components plus alpha components,
in which case all color and alpha components are rescaled.

BufferedImage sources with premultiplied alpha data are treated in the same
manner as non-premultiplied images for purposes of rescaling. That is,
the rescaling is done per band on the raw data of the BufferedImage source
without regard to whether the data is premultiplied. If a color conversion
is required to the destination ColorModel, the premultiplied state of
both source and destination will be taken into account for this step.

Images with an IndexColorModel cannot be rescaled.

If a RenderingHints object is specified in the constructor, the
color rendering hint and the dithering hint may be used when color
conversion is required.

Note that in-place operation is allowed (i.e. the source and destination can
be the same object).

BufferedImage sources with premultiplied alpha data are treated in the same
manner as non-premultiplied images for purposes of rescaling. That is,
the rescaling is done per band on the raw data of the BufferedImage source
without regard to whether the data is premultiplied. If a color conversion
is required to the destination ColorModel, the premultiplied state of
both source and destination will be taken into account for this step.

Images with an IndexColorModel cannot be rescaled.

If a RenderingHints object is specified in the constructor, the
color rendering hint and the dithering hint may be used when color
conversion is required.

Note that in-place operation is allowed (i.e. the source and destination can
be the same object).

Images with an IndexColorModel cannot be rescaled.

If a RenderingHints object is specified in the constructor, the
color rendering hint and the dithering hint may be used when color
conversion is required.

Note that in-place operation is allowed (i.e. the source and destination can
be the same object).

If a RenderingHints object is specified in the constructor, the
color rendering hint and the dithering hint may be used when color
conversion is required.

Note that in-place operation is allowed (i.e. the source and destination can
be the same object).

Note that in-place operation is allowed (i.e. the source and destination can
be the same object).

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

RescaleOp

​(float[] scaleFactors,
float[] offsets,

RenderingHints

hints)

Constructs a new RescaleOp with the desired scale factors
and offsets.

RescaleOp

​(float scaleFactor,
float offset,

RenderingHints

hints)

Constructs a new RescaleOp with the desired scale factor
and offset.

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

Creates a zeroed-destination

Raster

with the correct
size and number of bands, given this source.

BufferedImage

filter

​(

BufferedImage

src,

BufferedImage

dst)

Rescales the source BufferedImage.

WritableRaster

filter

​(

Raster

src,

WritableRaster

dst)

Rescales the pixel data in the source Raster.

Rectangle2D

getBounds2D

​(

BufferedImage

src)

Returns the bounding box of the rescaled destination image.

Rectangle2D

getBounds2D

​(

Raster

src)

Returns the bounding box of the rescaled destination Raster.

int

getNumFactors

()

Returns the number of scaling factors and offsets used in this
RescaleOp.

float[]

getOffsets

​(float[] offsets)

Returns the offsets in the given array.

Point2D

getPoint2D

​(

Point2D

srcPt,

Point2D

dstPt)

Returns the location of the destination point given a
point in the source.

RenderingHints

getRenderingHints

()

Returns the rendering hints for this op.

float[]

getScaleFactors

​(float[] scaleFactors)

Returns the scale factors in the given array.

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

Constructor Summary

Constructors

Constructor

Description

RescaleOp

​(float[] scaleFactors,
float[] offsets,

RenderingHints

hints)

Constructs a new RescaleOp with the desired scale factors
and offsets.

RescaleOp

​(float scaleFactor,
float offset,

RenderingHints

hints)

Constructs a new RescaleOp with the desired scale factor
and offset.

---

#### Constructor Summary

Constructs a new RescaleOp with the desired scale factors
and offsets.

Constructs a new RescaleOp with the desired scale factor
and offset.

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

Creates a zeroed-destination

Raster

with the correct
size and number of bands, given this source.

BufferedImage

filter

​(

BufferedImage

src,

BufferedImage

dst)

Rescales the source BufferedImage.

WritableRaster

filter

​(

Raster

src,

WritableRaster

dst)

Rescales the pixel data in the source Raster.

Rectangle2D

getBounds2D

​(

BufferedImage

src)

Returns the bounding box of the rescaled destination image.

Rectangle2D

getBounds2D

​(

Raster

src)

Returns the bounding box of the rescaled destination Raster.

int

getNumFactors

()

Returns the number of scaling factors and offsets used in this
RescaleOp.

float[]

getOffsets

​(float[] offsets)

Returns the offsets in the given array.

Point2D

getPoint2D

​(

Point2D

srcPt,

Point2D

dstPt)

Returns the location of the destination point given a
point in the source.

RenderingHints

getRenderingHints

()

Returns the rendering hints for this op.

float[]

getScaleFactors

​(float[] scaleFactors)

Returns the scale factors in the given array.

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

Creates a zeroed-destination

Raster

with the correct
size and number of bands, given this source.

Rescales the source BufferedImage.

Rescales the pixel data in the source Raster.

Returns the bounding box of the rescaled destination image.

Returns the bounding box of the rescaled destination Raster.

Returns the number of scaling factors and offsets used in this
RescaleOp.

Returns the offsets in the given array.

Returns the location of the destination point given a
point in the source.

Returns the rendering hints for this op.

Returns the scale factors in the given array.

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

- RescaleOp

```java
public RescaleOp​(float[] scaleFactors,
float[] offsets,

RenderingHints
hints)
```

Constructs a new RescaleOp with the desired scale factors
and offsets. The length of the scaleFactor and offset arrays
must meet the restrictions stated in the class comments above.
The RenderingHints argument may be null.

**Parameters:** scaleFactors

- the specified scale factors
**Parameters:** offsets

- the specified offsets
**Parameters:** hints

- the specified

RenderingHints

, or

null

- RescaleOp

```java
public RescaleOp​(float scaleFactor,
float offset,

RenderingHints
hints)
```

Constructs a new RescaleOp with the desired scale factor
and offset. The scaleFactor and offset will be applied to
all bands in a source Raster and to all color (but not alpha)
components in a BufferedImage.
The RenderingHints argument may be null.

**Parameters:** scaleFactor

- the specified scale factor
**Parameters:** offset

- the specified offset
**Parameters:** hints

- the specified

RenderingHints

, or

null

============ METHOD DETAIL ==========

- Method Detail

- getScaleFactors

```java
public final float[] getScaleFactors​(float[] scaleFactors)
```

Returns the scale factors in the given array. The array is also
returned for convenience. If scaleFactors is null, a new array
will be allocated.

**Parameters:** scaleFactors

- the array to contain the scale factors of
this

RescaleOp
**Returns:** the scale factors of this

RescaleOp

.

- getOffsets

```java
public final float[] getOffsets​(float[] offsets)
```

Returns the offsets in the given array. The array is also returned
for convenience. If offsets is null, a new array
will be allocated.

**Parameters:** offsets

- the array to contain the offsets of
this

RescaleOp
**Returns:** the offsets of this

RescaleOp

.

- getNumFactors

```java
public final int getNumFactors()
```

Returns the number of scaling factors and offsets used in this
RescaleOp.

**Returns:** the number of scaling factors and offsets of this

RescaleOp

.

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

Rescales the source BufferedImage.
If the color model in the source image is not the same as that
in the destination image, the pixels will be converted
in the destination. If the destination image is null,
a BufferedImage will be created with the source ColorModel.
An IllegalArgumentException may be thrown if the number of
scaling factors/offsets in this object does not meet the
restrictions stated in the class comments above, or if the
source image has an IndexColorModel.

**Specified by:** filter

in interface

BufferedImageOp
**Parameters:** src

- the

BufferedImage

to be filtered
**Parameters:** dst

- the destination for the filtering operation
or

null
**Returns:** the filtered

BufferedImage

.
**Throws:** IllegalArgumentException

- if the

ColorModel

of

src

is an

IndexColorModel

,
or if the number of scaling factors and offsets in this

RescaleOp

do not meet the requirements
stated in the class comments, or if the source and
destination images differ in size.

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

Rescales the pixel data in the source Raster.
If the destination Raster is null, a new Raster will be created.
The source and destination must have the same number of bands.
Otherwise, an IllegalArgumentException is thrown.
Note that the number of scaling factors/offsets in this object must
meet the restrictions stated in the class comments above.
Otherwise, an IllegalArgumentException is thrown.

**Specified by:** filter

in interface

RasterOp
**Parameters:** src

- the

Raster

to be filtered
**Parameters:** dst

- the destination for the filtering operation
or

null
**Returns:** the filtered

WritableRaster

.
**Throws:** IllegalArgumentException

- if

src

and

dst

do not have the same number of bands,
or if the number of scaling factors and offsets in this

RescaleOp

do not meet the requirements
stated in the class comments, or if the source and
destination rasters differ in size.

- getBounds2D

```java
public final
Rectangle2D
getBounds2D​(
BufferedImage
src)
```

Returns the bounding box of the rescaled destination image. Since
this is not a geometric operation, the bounding box does not
change.

**Specified by:** getBounds2D

in interface

BufferedImageOp
**Parameters:** src

- The

BufferedImage

to be filtered
**Returns:** The

Rectangle2D

representing the destination
image's bounding box.

- getBounds2D

```java
public final
Rectangle2D
getBounds2D​(
Raster
src)
```

Returns the bounding box of the rescaled destination Raster. Since
this is not a geometric operation, the bounding box does not
change.

**Specified by:** getBounds2D

in interface

RasterOp
**Parameters:** src

- the rescaled destination

Raster
**Returns:** the bounds of the specified

Raster

.

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
bands.

**Specified by:** createCompatibleDestImage

in interface

BufferedImageOp
**Parameters:** src

- Source image for the filter operation.
**Parameters:** destCM

- ColorModel of the destination. If null, the
ColorModel of the source will be used.
**Returns:** the zeroed-destination image.

- createCompatibleDestRaster

```java
public
WritableRaster
createCompatibleDestRaster​(
Raster
src)
```

Creates a zeroed-destination

Raster

with the correct
size and number of bands, given this source.

**Specified by:** createCompatibleDestRaster

in interface

RasterOp
**Parameters:** src

- the source

Raster
**Returns:** the zeroed-destination

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

Returns the location of the destination point given a
point in the source. If dstPt is non-null, it will
be used to hold the return value. Since this is not a geometric
operation, the srcPt will equal the dstPt.

**Specified by:** getPoint2D

in interface

BufferedImageOp
**Specified by:** getPoint2D

in interface

RasterOp
**Parameters:** srcPt

- a point in the source image
**Parameters:** dstPt

- the destination point or

null
**Returns:** the location of the destination point.

- getRenderingHints

```java
public final
RenderingHints
getRenderingHints()
```

Returns the rendering hints for this op.

**Specified by:** getRenderingHints

in interface

BufferedImageOp
**Specified by:** getRenderingHints

in interface

RasterOp
**Returns:** the rendering hints of this

RescaleOp

.

Constructor Detail

- RescaleOp

```java
public RescaleOp​(float[] scaleFactors,
float[] offsets,

RenderingHints
hints)
```

Constructs a new RescaleOp with the desired scale factors
and offsets. The length of the scaleFactor and offset arrays
must meet the restrictions stated in the class comments above.
The RenderingHints argument may be null.

**Parameters:** scaleFactors

- the specified scale factors
**Parameters:** offsets

- the specified offsets
**Parameters:** hints

- the specified

RenderingHints

, or

null

- RescaleOp

```java
public RescaleOp​(float scaleFactor,
float offset,

RenderingHints
hints)
```

Constructs a new RescaleOp with the desired scale factor
and offset. The scaleFactor and offset will be applied to
all bands in a source Raster and to all color (but not alpha)
components in a BufferedImage.
The RenderingHints argument may be null.

**Parameters:** scaleFactor

- the specified scale factor
**Parameters:** offset

- the specified offset
**Parameters:** hints

- the specified

RenderingHints

, or

null

---

#### Constructor Detail

RescaleOp

```java
public RescaleOp​(float[] scaleFactors,
float[] offsets,

RenderingHints
hints)
```

Constructs a new RescaleOp with the desired scale factors
and offsets. The length of the scaleFactor and offset arrays
must meet the restrictions stated in the class comments above.
The RenderingHints argument may be null.

**Parameters:** scaleFactors

- the specified scale factors
**Parameters:** offsets

- the specified offsets
**Parameters:** hints

- the specified

RenderingHints

, or

null

---

#### RescaleOp

public RescaleOp​(float[] scaleFactors,
float[] offsets,

RenderingHints

hints)

Constructs a new RescaleOp with the desired scale factors
and offsets. The length of the scaleFactor and offset arrays
must meet the restrictions stated in the class comments above.
The RenderingHints argument may be null.

RescaleOp

```java
public RescaleOp​(float scaleFactor,
float offset,

RenderingHints
hints)
```

Constructs a new RescaleOp with the desired scale factor
and offset. The scaleFactor and offset will be applied to
all bands in a source Raster and to all color (but not alpha)
components in a BufferedImage.
The RenderingHints argument may be null.

**Parameters:** scaleFactor

- the specified scale factor
**Parameters:** offset

- the specified offset
**Parameters:** hints

- the specified

RenderingHints

, or

null

---

#### RescaleOp

public RescaleOp​(float scaleFactor,
float offset,

RenderingHints

hints)

Constructs a new RescaleOp with the desired scale factor
and offset. The scaleFactor and offset will be applied to
all bands in a source Raster and to all color (but not alpha)
components in a BufferedImage.
The RenderingHints argument may be null.

Method Detail

- getScaleFactors

```java
public final float[] getScaleFactors​(float[] scaleFactors)
```

Returns the scale factors in the given array. The array is also
returned for convenience. If scaleFactors is null, a new array
will be allocated.

**Parameters:** scaleFactors

- the array to contain the scale factors of
this

RescaleOp
**Returns:** the scale factors of this

RescaleOp

.

- getOffsets

```java
public final float[] getOffsets​(float[] offsets)
```

Returns the offsets in the given array. The array is also returned
for convenience. If offsets is null, a new array
will be allocated.

**Parameters:** offsets

- the array to contain the offsets of
this

RescaleOp
**Returns:** the offsets of this

RescaleOp

.

- getNumFactors

```java
public final int getNumFactors()
```

Returns the number of scaling factors and offsets used in this
RescaleOp.

**Returns:** the number of scaling factors and offsets of this

RescaleOp

.

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

Rescales the source BufferedImage.
If the color model in the source image is not the same as that
in the destination image, the pixels will be converted
in the destination. If the destination image is null,
a BufferedImage will be created with the source ColorModel.
An IllegalArgumentException may be thrown if the number of
scaling factors/offsets in this object does not meet the
restrictions stated in the class comments above, or if the
source image has an IndexColorModel.

**Specified by:** filter

in interface

BufferedImageOp
**Parameters:** src

- the

BufferedImage

to be filtered
**Parameters:** dst

- the destination for the filtering operation
or

null
**Returns:** the filtered

BufferedImage

.
**Throws:** IllegalArgumentException

- if the

ColorModel

of

src

is an

IndexColorModel

,
or if the number of scaling factors and offsets in this

RescaleOp

do not meet the requirements
stated in the class comments, or if the source and
destination images differ in size.

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

Rescales the pixel data in the source Raster.
If the destination Raster is null, a new Raster will be created.
The source and destination must have the same number of bands.
Otherwise, an IllegalArgumentException is thrown.
Note that the number of scaling factors/offsets in this object must
meet the restrictions stated in the class comments above.
Otherwise, an IllegalArgumentException is thrown.

**Specified by:** filter

in interface

RasterOp
**Parameters:** src

- the

Raster

to be filtered
**Parameters:** dst

- the destination for the filtering operation
or

null
**Returns:** the filtered

WritableRaster

.
**Throws:** IllegalArgumentException

- if

src

and

dst

do not have the same number of bands,
or if the number of scaling factors and offsets in this

RescaleOp

do not meet the requirements
stated in the class comments, or if the source and
destination rasters differ in size.

- getBounds2D

```java
public final
Rectangle2D
getBounds2D​(
BufferedImage
src)
```

Returns the bounding box of the rescaled destination image. Since
this is not a geometric operation, the bounding box does not
change.

**Specified by:** getBounds2D

in interface

BufferedImageOp
**Parameters:** src

- The

BufferedImage

to be filtered
**Returns:** The

Rectangle2D

representing the destination
image's bounding box.

- getBounds2D

```java
public final
Rectangle2D
getBounds2D​(
Raster
src)
```

Returns the bounding box of the rescaled destination Raster. Since
this is not a geometric operation, the bounding box does not
change.

**Specified by:** getBounds2D

in interface

RasterOp
**Parameters:** src

- the rescaled destination

Raster
**Returns:** the bounds of the specified

Raster

.

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
bands.

**Specified by:** createCompatibleDestImage

in interface

BufferedImageOp
**Parameters:** src

- Source image for the filter operation.
**Parameters:** destCM

- ColorModel of the destination. If null, the
ColorModel of the source will be used.
**Returns:** the zeroed-destination image.

- createCompatibleDestRaster

```java
public
WritableRaster
createCompatibleDestRaster​(
Raster
src)
```

Creates a zeroed-destination

Raster

with the correct
size and number of bands, given this source.

**Specified by:** createCompatibleDestRaster

in interface

RasterOp
**Parameters:** src

- the source

Raster
**Returns:** the zeroed-destination

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

Returns the location of the destination point given a
point in the source. If dstPt is non-null, it will
be used to hold the return value. Since this is not a geometric
operation, the srcPt will equal the dstPt.

**Specified by:** getPoint2D

in interface

BufferedImageOp
**Specified by:** getPoint2D

in interface

RasterOp
**Parameters:** srcPt

- a point in the source image
**Parameters:** dstPt

- the destination point or

null
**Returns:** the location of the destination point.

- getRenderingHints

```java
public final
RenderingHints
getRenderingHints()
```

Returns the rendering hints for this op.

**Specified by:** getRenderingHints

in interface

BufferedImageOp
**Specified by:** getRenderingHints

in interface

RasterOp
**Returns:** the rendering hints of this

RescaleOp

.

---

#### Method Detail

getScaleFactors

```java
public final float[] getScaleFactors​(float[] scaleFactors)
```

Returns the scale factors in the given array. The array is also
returned for convenience. If scaleFactors is null, a new array
will be allocated.

**Parameters:** scaleFactors

- the array to contain the scale factors of
this

RescaleOp
**Returns:** the scale factors of this

RescaleOp

.

---

#### getScaleFactors

public final float[] getScaleFactors​(float[] scaleFactors)

Returns the scale factors in the given array. The array is also
returned for convenience. If scaleFactors is null, a new array
will be allocated.

getOffsets

```java
public final float[] getOffsets​(float[] offsets)
```

Returns the offsets in the given array. The array is also returned
for convenience. If offsets is null, a new array
will be allocated.

**Parameters:** offsets

- the array to contain the offsets of
this

RescaleOp
**Returns:** the offsets of this

RescaleOp

.

---

#### getOffsets

public final float[] getOffsets​(float[] offsets)

Returns the offsets in the given array. The array is also returned
for convenience. If offsets is null, a new array
will be allocated.

getNumFactors

```java
public final int getNumFactors()
```

Returns the number of scaling factors and offsets used in this
RescaleOp.

**Returns:** the number of scaling factors and offsets of this

RescaleOp

.

---

#### getNumFactors

public final int getNumFactors()

Returns the number of scaling factors and offsets used in this
RescaleOp.

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

Rescales the source BufferedImage.
If the color model in the source image is not the same as that
in the destination image, the pixels will be converted
in the destination. If the destination image is null,
a BufferedImage will be created with the source ColorModel.
An IllegalArgumentException may be thrown if the number of
scaling factors/offsets in this object does not meet the
restrictions stated in the class comments above, or if the
source image has an IndexColorModel.

**Specified by:** filter

in interface

BufferedImageOp
**Parameters:** src

- the

BufferedImage

to be filtered
**Parameters:** dst

- the destination for the filtering operation
or

null
**Returns:** the filtered

BufferedImage

.
**Throws:** IllegalArgumentException

- if the

ColorModel

of

src

is an

IndexColorModel

,
or if the number of scaling factors and offsets in this

RescaleOp

do not meet the requirements
stated in the class comments, or if the source and
destination images differ in size.

---

#### filter

public final

BufferedImage

filter​(

BufferedImage

src,

BufferedImage

dst)

Rescales the source BufferedImage.
If the color model in the source image is not the same as that
in the destination image, the pixels will be converted
in the destination. If the destination image is null,
a BufferedImage will be created with the source ColorModel.
An IllegalArgumentException may be thrown if the number of
scaling factors/offsets in this object does not meet the
restrictions stated in the class comments above, or if the
source image has an IndexColorModel.

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

Rescales the pixel data in the source Raster.
If the destination Raster is null, a new Raster will be created.
The source and destination must have the same number of bands.
Otherwise, an IllegalArgumentException is thrown.
Note that the number of scaling factors/offsets in this object must
meet the restrictions stated in the class comments above.
Otherwise, an IllegalArgumentException is thrown.

**Specified by:** filter

in interface

RasterOp
**Parameters:** src

- the

Raster

to be filtered
**Parameters:** dst

- the destination for the filtering operation
or

null
**Returns:** the filtered

WritableRaster

.
**Throws:** IllegalArgumentException

- if

src

and

dst

do not have the same number of bands,
or if the number of scaling factors and offsets in this

RescaleOp

do not meet the requirements
stated in the class comments, or if the source and
destination rasters differ in size.

---

#### filter

public final

WritableRaster

filter​(

Raster

src,

WritableRaster

dst)

Rescales the pixel data in the source Raster.
If the destination Raster is null, a new Raster will be created.
The source and destination must have the same number of bands.
Otherwise, an IllegalArgumentException is thrown.
Note that the number of scaling factors/offsets in this object must
meet the restrictions stated in the class comments above.
Otherwise, an IllegalArgumentException is thrown.

getBounds2D

```java
public final
Rectangle2D
getBounds2D​(
BufferedImage
src)
```

Returns the bounding box of the rescaled destination image. Since
this is not a geometric operation, the bounding box does not
change.

**Specified by:** getBounds2D

in interface

BufferedImageOp
**Parameters:** src

- The

BufferedImage

to be filtered
**Returns:** The

Rectangle2D

representing the destination
image's bounding box.

---

#### getBounds2D

public final

Rectangle2D

getBounds2D​(

BufferedImage

src)

Returns the bounding box of the rescaled destination image. Since
this is not a geometric operation, the bounding box does not
change.

getBounds2D

```java
public final
Rectangle2D
getBounds2D​(
Raster
src)
```

Returns the bounding box of the rescaled destination Raster. Since
this is not a geometric operation, the bounding box does not
change.

**Specified by:** getBounds2D

in interface

RasterOp
**Parameters:** src

- the rescaled destination

Raster
**Returns:** the bounds of the specified

Raster

.

---

#### getBounds2D

public final

Rectangle2D

getBounds2D​(

Raster

src)

Returns the bounding box of the rescaled destination Raster. Since
this is not a geometric operation, the bounding box does not
change.

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
bands.

**Specified by:** createCompatibleDestImage

in interface

BufferedImageOp
**Parameters:** src

- Source image for the filter operation.
**Parameters:** destCM

- ColorModel of the destination. If null, the
ColorModel of the source will be used.
**Returns:** the zeroed-destination image.

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
bands.

createCompatibleDestRaster

```java
public
WritableRaster
createCompatibleDestRaster​(
Raster
src)
```

Creates a zeroed-destination

Raster

with the correct
size and number of bands, given this source.

**Specified by:** createCompatibleDestRaster

in interface

RasterOp
**Parameters:** src

- the source

Raster
**Returns:** the zeroed-destination

Raster

.

---

#### createCompatibleDestRaster

public

WritableRaster

createCompatibleDestRaster​(

Raster

src)

Creates a zeroed-destination

Raster

with the correct
size and number of bands, given this source.

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

Returns the location of the destination point given a
point in the source. If dstPt is non-null, it will
be used to hold the return value. Since this is not a geometric
operation, the srcPt will equal the dstPt.

**Specified by:** getPoint2D

in interface

BufferedImageOp
**Specified by:** getPoint2D

in interface

RasterOp
**Parameters:** srcPt

- a point in the source image
**Parameters:** dstPt

- the destination point or

null
**Returns:** the location of the destination point.

---

#### getPoint2D

public final

Point2D

getPoint2D​(

Point2D

srcPt,

Point2D

dstPt)

Returns the location of the destination point given a
point in the source. If dstPt is non-null, it will
be used to hold the return value. Since this is not a geometric
operation, the srcPt will equal the dstPt.

getRenderingHints

```java
public final
RenderingHints
getRenderingHints()
```

Returns the rendering hints for this op.

**Specified by:** getRenderingHints

in interface

BufferedImageOp
**Specified by:** getRenderingHints

in interface

RasterOp
**Returns:** the rendering hints of this

RescaleOp

.

---

#### getRenderingHints

public final

RenderingHints

getRenderingHints()

Returns the rendering hints for this op.

---

