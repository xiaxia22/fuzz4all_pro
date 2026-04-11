# Class ConvolveOp

**Source:** `java.desktop\java\awt\image\ConvolveOp.html`

### Class Description

```java
public class
ConvolveOp

extends
Object

implements
BufferedImageOp
,
RasterOp
```

This class implements a convolution from the source
to the destination.
Convolution using a convolution kernel is a spatial operation that
computes the output pixel from an input pixel by multiplying the kernel
with the surround of the input pixel.
This allows the output pixel to be affected by the immediate neighborhood
in a way that can be mathematically specified with a kernel.

This class operates with BufferedImage data in which color components are
premultiplied with the alpha component. If the Source BufferedImage has
an alpha component, and the color components are not premultiplied with
the alpha component, then the data are premultiplied before being
convolved. If the Destination has color components which are not
premultiplied, then alpha is divided out before storing into the
Destination (if alpha is 0, the color components are set to 0). If the
Destination has no alpha component, then the resulting alpha is discarded
after first dividing it out of the color components.

Rasters are treated as having no alpha channel. If the above treatment
of the alpha channel in BufferedImages is not desired, it may be avoided
by getting the Raster of a source BufferedImage and using the filter method
of this class which works with Rasters.

If a RenderingHints object is specified in the constructor, the
color rendering hint and the dithering hint may be used when color
conversion is required.

Note that the Source and the Destination may not be the same object.

**All Implemented Interfaces:** BufferedImageOp

,

RasterOp

---

### Field Details

#### @Native

public static final int EDGE_ZERO_FILL

Pixels at the edge of the destination image are set to zero. This
is the default.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int EDGE_NO_OP

Pixels at the edge of the source image are copied to
the corresponding pixels in the destination without modification.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public ConvolveOp​(
Kernel
kernel,
int edgeCondition,

RenderingHints
hints)

Constructs a ConvolveOp given a Kernel, an edge condition, and a
RenderingHints object (which may be null).

**Parameters:**
- kernel

- the specified

Kernel
- edgeCondition

- the specified edge condition
- hints

- the specified

RenderingHints

object

**See Also:**
- Kernel

,

EDGE_NO_OP

,

EDGE_ZERO_FILL

,

RenderingHints

---

#### public ConvolveOp​(
Kernel
kernel)

Constructs a ConvolveOp given a Kernel. The edge condition
will be EDGE_ZERO_FILL.

**Parameters:**
- kernel

- the specified

Kernel

**See Also:**
- Kernel

,

EDGE_ZERO_FILL

---

### Method Details

#### public int getEdgeCondition()

Returns the edge condition.

**Returns:**
- the edge condition of this

ConvolveOp

.

**See Also:**
- EDGE_NO_OP

,

EDGE_ZERO_FILL

---

#### public final
Kernel
getKernel()

Returns the Kernel.

**Returns:**
- the

Kernel

of this

ConvolveOp

.

---

#### public final
BufferedImage
filter​(
BufferedImage
src,

BufferedImage
dst)

Performs a convolution on BufferedImages. Each component of the
source image will be convolved (including the alpha component, if
present).
If the color model in the source image is not the same as that
in the destination image, the pixels will be converted
in the destination. If the destination image is null,
a BufferedImage will be created with the source ColorModel.
The IllegalArgumentException may be thrown if the source is the
same as the destination.

**Specified by:**
- filter

in interface

BufferedImageOp

**Parameters:**
- src

- the source

BufferedImage

to filter
- dst

- the destination

BufferedImage

for the
filtered

src

**Returns:**
- the filtered

BufferedImage

**Throws:**
- NullPointerException

- if

src

is

null
- IllegalArgumentException

- if

src

equals

dst
- ImagingOpException

- if

src

cannot be filtered

---

#### public final
WritableRaster
filter​(
Raster
src,

WritableRaster
dst)

Performs a convolution on Rasters. Each band of the source Raster
will be convolved.
The source and destination must have the same number of bands.
If the destination Raster is null, a new Raster will be created.
The IllegalArgumentException may be thrown if the source is
the same as the destination.

**Specified by:**
- filter

in interface

RasterOp

**Parameters:**
- src

- the source

Raster

to filter
- dst

- the destination

WritableRaster

for the
filtered

src

**Returns:**
- the filtered

WritableRaster

**Throws:**
- NullPointerException

- if

src

is

null
- ImagingOpException

- if

src

and

dst

do not have the same number of bands
- ImagingOpException

- if

src

cannot be filtered
- IllegalArgumentException

- if

src

equals

dst

---

#### public
BufferedImage
createCompatibleDestImage​(
BufferedImage
src,

ColorModel
destCM)

Creates a zeroed destination image with the correct size and number
of bands. If destCM is null, an appropriate ColorModel will be used.

**Specified by:**
- createCompatibleDestImage

in interface

BufferedImageOp

**Parameters:**
- src

- Source image for the filter operation.
- destCM

- ColorModel of the destination. Can be null.

**Returns:**
- a destination

BufferedImage

with the correct
size and number of bands.

---

#### public
WritableRaster
createCompatibleDestRaster​(
Raster
src)

Creates a zeroed destination Raster with the correct size and number
of bands, given this source.

**Specified by:**
- createCompatibleDestRaster

in interface

RasterOp

**Parameters:**
- src

- the source

Raster

**Returns:**
- a

WritableRaster

that is compatible with

src

---

#### public final
Rectangle2D
getBounds2D​(
BufferedImage
src)

Returns the bounding box of the filtered destination image. Since
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

Returns the bounding box of the filtered destination Raster. Since
this is not a geometric operation, the bounding box does not
change.

**Specified by:**
- getBounds2D

in interface

RasterOp

**Parameters:**
- src

- the source

Raster

**Returns:**
- a

Rectangle2D

that is the bounding box of
the

Raster

resulting from the filtering
operation.

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

- the

Point2D

that represents the point in
the source image
- dstPt

- The

Point2D

in which to store the result

**Returns:**
- The

Point2D

in the destination image that
corresponds to the specified point in the source image.

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
- The

RenderingHints

object for this

BufferedImageOp

. Returns
null if no hints have been set.

---

### Additional Sections

#### Class ConvolveOp

java.lang.Object

- java.awt.image.ConvolveOp

java.awt.image.ConvolveOp

**All Implemented Interfaces:** BufferedImageOp

,

RasterOp

```java
public class
ConvolveOp

extends
Object

implements
BufferedImageOp
,
RasterOp
```

This class implements a convolution from the source
to the destination.
Convolution using a convolution kernel is a spatial operation that
computes the output pixel from an input pixel by multiplying the kernel
with the surround of the input pixel.
This allows the output pixel to be affected by the immediate neighborhood
in a way that can be mathematically specified with a kernel.

This class operates with BufferedImage data in which color components are
premultiplied with the alpha component. If the Source BufferedImage has
an alpha component, and the color components are not premultiplied with
the alpha component, then the data are premultiplied before being
convolved. If the Destination has color components which are not
premultiplied, then alpha is divided out before storing into the
Destination (if alpha is 0, the color components are set to 0). If the
Destination has no alpha component, then the resulting alpha is discarded
after first dividing it out of the color components.

Rasters are treated as having no alpha channel. If the above treatment
of the alpha channel in BufferedImages is not desired, it may be avoided
by getting the Raster of a source BufferedImage and using the filter method
of this class which works with Rasters.

If a RenderingHints object is specified in the constructor, the
color rendering hint and the dithering hint may be used when color
conversion is required.

Note that the Source and the Destination may not be the same object.

**See Also:** Kernel

,

RenderingHints.KEY_COLOR_RENDERING

,

RenderingHints.KEY_DITHERING

public class

ConvolveOp

extends

Object

implements

BufferedImageOp

,

RasterOp

This class implements a convolution from the source
to the destination.
Convolution using a convolution kernel is a spatial operation that
computes the output pixel from an input pixel by multiplying the kernel
with the surround of the input pixel.
This allows the output pixel to be affected by the immediate neighborhood
in a way that can be mathematically specified with a kernel.

This class operates with BufferedImage data in which color components are
premultiplied with the alpha component. If the Source BufferedImage has
an alpha component, and the color components are not premultiplied with
the alpha component, then the data are premultiplied before being
convolved. If the Destination has color components which are not
premultiplied, then alpha is divided out before storing into the
Destination (if alpha is 0, the color components are set to 0). If the
Destination has no alpha component, then the resulting alpha is discarded
after first dividing it out of the color components.

Rasters are treated as having no alpha channel. If the above treatment
of the alpha channel in BufferedImages is not desired, it may be avoided
by getting the Raster of a source BufferedImage and using the filter method
of this class which works with Rasters.

If a RenderingHints object is specified in the constructor, the
color rendering hint and the dithering hint may be used when color
conversion is required.

Note that the Source and the Destination may not be the same object.

This class operates with BufferedImage data in which color components are
premultiplied with the alpha component. If the Source BufferedImage has
an alpha component, and the color components are not premultiplied with
the alpha component, then the data are premultiplied before being
convolved. If the Destination has color components which are not
premultiplied, then alpha is divided out before storing into the
Destination (if alpha is 0, the color components are set to 0). If the
Destination has no alpha component, then the resulting alpha is discarded
after first dividing it out of the color components.

Rasters are treated as having no alpha channel. If the above treatment
of the alpha channel in BufferedImages is not desired, it may be avoided
by getting the Raster of a source BufferedImage and using the filter method
of this class which works with Rasters.

If a RenderingHints object is specified in the constructor, the
color rendering hint and the dithering hint may be used when color
conversion is required.

Note that the Source and the Destination may not be the same object.

Rasters are treated as having no alpha channel. If the above treatment
of the alpha channel in BufferedImages is not desired, it may be avoided
by getting the Raster of a source BufferedImage and using the filter method
of this class which works with Rasters.

If a RenderingHints object is specified in the constructor, the
color rendering hint and the dithering hint may be used when color
conversion is required.

Note that the Source and the Destination may not be the same object.

If a RenderingHints object is specified in the constructor, the
color rendering hint and the dithering hint may be used when color
conversion is required.

Note that the Source and the Destination may not be the same object.

Note that the Source and the Destination may not be the same object.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

EDGE_NO_OP

Pixels at the edge of the source image are copied to
the corresponding pixels in the destination without modification.

static int

EDGE_ZERO_FILL

Pixels at the edge of the destination image are set to zero.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ConvolveOp

​(

Kernel

kernel)

Constructs a ConvolveOp given a Kernel.

ConvolveOp

​(

Kernel

kernel,
int edgeCondition,

RenderingHints

hints)

Constructs a ConvolveOp given a Kernel, an edge condition, and a
RenderingHints object (which may be null).

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

Creates a zeroed destination image with the correct size and number
of bands.

WritableRaster

createCompatibleDestRaster

​(

Raster

src)

Creates a zeroed destination Raster with the correct size and number
of bands, given this source.

BufferedImage

filter

​(

BufferedImage

src,

BufferedImage

dst)

Performs a convolution on BufferedImages.

WritableRaster

filter

​(

Raster

src,

WritableRaster

dst)

Performs a convolution on Rasters.

Rectangle2D

getBounds2D

​(

BufferedImage

src)

Returns the bounding box of the filtered destination image.

Rectangle2D

getBounds2D

​(

Raster

src)

Returns the bounding box of the filtered destination Raster.

int

getEdgeCondition

()

Returns the edge condition.

Kernel

getKernel

()

Returns the Kernel.

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

EDGE_NO_OP

Pixels at the edge of the source image are copied to
the corresponding pixels in the destination without modification.

static int

EDGE_ZERO_FILL

Pixels at the edge of the destination image are set to zero.

---

#### Field Summary

Pixels at the edge of the source image are copied to
the corresponding pixels in the destination without modification.

Pixels at the edge of the destination image are set to zero.

Constructor Summary

Constructors

Constructor

Description

ConvolveOp

​(

Kernel

kernel)

Constructs a ConvolveOp given a Kernel.

ConvolveOp

​(

Kernel

kernel,
int edgeCondition,

RenderingHints

hints)

Constructs a ConvolveOp given a Kernel, an edge condition, and a
RenderingHints object (which may be null).

---

#### Constructor Summary

Constructs a ConvolveOp given a Kernel.

Constructs a ConvolveOp given a Kernel, an edge condition, and a
RenderingHints object (which may be null).

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

Creates a zeroed destination image with the correct size and number
of bands.

WritableRaster

createCompatibleDestRaster

​(

Raster

src)

Creates a zeroed destination Raster with the correct size and number
of bands, given this source.

BufferedImage

filter

​(

BufferedImage

src,

BufferedImage

dst)

Performs a convolution on BufferedImages.

WritableRaster

filter

​(

Raster

src,

WritableRaster

dst)

Performs a convolution on Rasters.

Rectangle2D

getBounds2D

​(

BufferedImage

src)

Returns the bounding box of the filtered destination image.

Rectangle2D

getBounds2D

​(

Raster

src)

Returns the bounding box of the filtered destination Raster.

int

getEdgeCondition

()

Returns the edge condition.

Kernel

getKernel

()

Returns the Kernel.

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

Creates a zeroed destination image with the correct size and number
of bands.

Creates a zeroed destination Raster with the correct size and number
of bands, given this source.

Performs a convolution on BufferedImages.

Performs a convolution on Rasters.

Returns the bounding box of the filtered destination image.

Returns the bounding box of the filtered destination Raster.

Returns the edge condition.

Returns the Kernel.

Returns the location of the destination point given a
point in the source.

Returns the rendering hints for this op.

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

- EDGE_ZERO_FILL

```java
@Native

public static final int EDGE_ZERO_FILL
```

Pixels at the edge of the destination image are set to zero. This
is the default.

**See Also:** Constant Field Values

- EDGE_NO_OP

```java
@Native

public static final int EDGE_NO_OP
```

Pixels at the edge of the source image are copied to
the corresponding pixels in the destination without modification.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ConvolveOp

```java
public ConvolveOp​(
Kernel
kernel,
int edgeCondition,

RenderingHints
hints)
```

Constructs a ConvolveOp given a Kernel, an edge condition, and a
RenderingHints object (which may be null).

**Parameters:** kernel

- the specified

Kernel
**Parameters:** edgeCondition

- the specified edge condition
**Parameters:** hints

- the specified

RenderingHints

object
**See Also:** Kernel

,

EDGE_NO_OP

,

EDGE_ZERO_FILL

,

RenderingHints

- ConvolveOp

```java
public ConvolveOp​(
Kernel
kernel)
```

Constructs a ConvolveOp given a Kernel. The edge condition
will be EDGE_ZERO_FILL.

**Parameters:** kernel

- the specified

Kernel
**See Also:** Kernel

,

EDGE_ZERO_FILL

============ METHOD DETAIL ==========

- Method Detail

- getEdgeCondition

```java
public int getEdgeCondition()
```

Returns the edge condition.

**Returns:** the edge condition of this

ConvolveOp

.
**See Also:** EDGE_NO_OP

,

EDGE_ZERO_FILL

- getKernel

```java
public final
Kernel
getKernel()
```

Returns the Kernel.

**Returns:** the

Kernel

of this

ConvolveOp

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

Performs a convolution on BufferedImages. Each component of the
source image will be convolved (including the alpha component, if
present).
If the color model in the source image is not the same as that
in the destination image, the pixels will be converted
in the destination. If the destination image is null,
a BufferedImage will be created with the source ColorModel.
The IllegalArgumentException may be thrown if the source is the
same as the destination.

**Specified by:** filter

in interface

BufferedImageOp
**Parameters:** src

- the source

BufferedImage

to filter
**Parameters:** dst

- the destination

BufferedImage

for the
filtered

src
**Returns:** the filtered

BufferedImage
**Throws:** NullPointerException

- if

src

is

null
**Throws:** IllegalArgumentException

- if

src

equals

dst
**Throws:** ImagingOpException

- if

src

cannot be filtered

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

Performs a convolution on Rasters. Each band of the source Raster
will be convolved.
The source and destination must have the same number of bands.
If the destination Raster is null, a new Raster will be created.
The IllegalArgumentException may be thrown if the source is
the same as the destination.

**Specified by:** filter

in interface

RasterOp
**Parameters:** src

- the source

Raster

to filter
**Parameters:** dst

- the destination

WritableRaster

for the
filtered

src
**Returns:** the filtered

WritableRaster
**Throws:** NullPointerException

- if

src

is

null
**Throws:** ImagingOpException

- if

src

and

dst

do not have the same number of bands
**Throws:** ImagingOpException

- if

src

cannot be filtered
**Throws:** IllegalArgumentException

- if

src

equals

dst

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

Creates a zeroed destination image with the correct size and number
of bands. If destCM is null, an appropriate ColorModel will be used.

**Specified by:** createCompatibleDestImage

in interface

BufferedImageOp
**Parameters:** src

- Source image for the filter operation.
**Parameters:** destCM

- ColorModel of the destination. Can be null.
**Returns:** a destination

BufferedImage

with the correct
size and number of bands.

- createCompatibleDestRaster

```java
public
WritableRaster
createCompatibleDestRaster​(
Raster
src)
```

Creates a zeroed destination Raster with the correct size and number
of bands, given this source.

**Specified by:** createCompatibleDestRaster

in interface

RasterOp
**Parameters:** src

- the source

Raster
**Returns:** a

WritableRaster

that is compatible with

src

- getBounds2D

```java
public final
Rectangle2D
getBounds2D​(
BufferedImage
src)
```

Returns the bounding box of the filtered destination image. Since
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

Returns the bounding box of the filtered destination Raster. Since
this is not a geometric operation, the bounding box does not
change.

**Specified by:** getBounds2D

in interface

RasterOp
**Parameters:** src

- the source

Raster
**Returns:** a

Rectangle2D

that is the bounding box of
the

Raster

resulting from the filtering
operation.

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

- the

Point2D

that represents the point in
the source image
**Parameters:** dstPt

- The

Point2D

in which to store the result
**Returns:** The

Point2D

in the destination image that
corresponds to the specified point in the source image.

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
**Returns:** The

RenderingHints

object for this

BufferedImageOp

. Returns
null if no hints have been set.

Field Detail

- EDGE_ZERO_FILL

```java
@Native

public static final int EDGE_ZERO_FILL
```

Pixels at the edge of the destination image are set to zero. This
is the default.

**See Also:** Constant Field Values

- EDGE_NO_OP

```java
@Native

public static final int EDGE_NO_OP
```

Pixels at the edge of the source image are copied to
the corresponding pixels in the destination without modification.

**See Also:** Constant Field Values

---

#### Field Detail

EDGE_ZERO_FILL

```java
@Native

public static final int EDGE_ZERO_FILL
```

Pixels at the edge of the destination image are set to zero. This
is the default.

**See Also:** Constant Field Values

---

#### EDGE_ZERO_FILL

@Native

public static final int EDGE_ZERO_FILL

Pixels at the edge of the destination image are set to zero. This
is the default.

EDGE_NO_OP

```java
@Native

public static final int EDGE_NO_OP
```

Pixels at the edge of the source image are copied to
the corresponding pixels in the destination without modification.

**See Also:** Constant Field Values

---

#### EDGE_NO_OP

@Native

public static final int EDGE_NO_OP

Pixels at the edge of the source image are copied to
the corresponding pixels in the destination without modification.

Constructor Detail

- ConvolveOp

```java
public ConvolveOp​(
Kernel
kernel,
int edgeCondition,

RenderingHints
hints)
```

Constructs a ConvolveOp given a Kernel, an edge condition, and a
RenderingHints object (which may be null).

**Parameters:** kernel

- the specified

Kernel
**Parameters:** edgeCondition

- the specified edge condition
**Parameters:** hints

- the specified

RenderingHints

object
**See Also:** Kernel

,

EDGE_NO_OP

,

EDGE_ZERO_FILL

,

RenderingHints

- ConvolveOp

```java
public ConvolveOp​(
Kernel
kernel)
```

Constructs a ConvolveOp given a Kernel. The edge condition
will be EDGE_ZERO_FILL.

**Parameters:** kernel

- the specified

Kernel
**See Also:** Kernel

,

EDGE_ZERO_FILL

---

#### Constructor Detail

ConvolveOp

```java
public ConvolveOp​(
Kernel
kernel,
int edgeCondition,

RenderingHints
hints)
```

Constructs a ConvolveOp given a Kernel, an edge condition, and a
RenderingHints object (which may be null).

**Parameters:** kernel

- the specified

Kernel
**Parameters:** edgeCondition

- the specified edge condition
**Parameters:** hints

- the specified

RenderingHints

object
**See Also:** Kernel

,

EDGE_NO_OP

,

EDGE_ZERO_FILL

,

RenderingHints

---

#### ConvolveOp

public ConvolveOp​(

Kernel

kernel,
int edgeCondition,

RenderingHints

hints)

Constructs a ConvolveOp given a Kernel, an edge condition, and a
RenderingHints object (which may be null).

ConvolveOp

```java
public ConvolveOp​(
Kernel
kernel)
```

Constructs a ConvolveOp given a Kernel. The edge condition
will be EDGE_ZERO_FILL.

**Parameters:** kernel

- the specified

Kernel
**See Also:** Kernel

,

EDGE_ZERO_FILL

---

#### ConvolveOp

public ConvolveOp​(

Kernel

kernel)

Constructs a ConvolveOp given a Kernel. The edge condition
will be EDGE_ZERO_FILL.

Method Detail

- getEdgeCondition

```java
public int getEdgeCondition()
```

Returns the edge condition.

**Returns:** the edge condition of this

ConvolveOp

.
**See Also:** EDGE_NO_OP

,

EDGE_ZERO_FILL

- getKernel

```java
public final
Kernel
getKernel()
```

Returns the Kernel.

**Returns:** the

Kernel

of this

ConvolveOp

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

Performs a convolution on BufferedImages. Each component of the
source image will be convolved (including the alpha component, if
present).
If the color model in the source image is not the same as that
in the destination image, the pixels will be converted
in the destination. If the destination image is null,
a BufferedImage will be created with the source ColorModel.
The IllegalArgumentException may be thrown if the source is the
same as the destination.

**Specified by:** filter

in interface

BufferedImageOp
**Parameters:** src

- the source

BufferedImage

to filter
**Parameters:** dst

- the destination

BufferedImage

for the
filtered

src
**Returns:** the filtered

BufferedImage
**Throws:** NullPointerException

- if

src

is

null
**Throws:** IllegalArgumentException

- if

src

equals

dst
**Throws:** ImagingOpException

- if

src

cannot be filtered

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

Performs a convolution on Rasters. Each band of the source Raster
will be convolved.
The source and destination must have the same number of bands.
If the destination Raster is null, a new Raster will be created.
The IllegalArgumentException may be thrown if the source is
the same as the destination.

**Specified by:** filter

in interface

RasterOp
**Parameters:** src

- the source

Raster

to filter
**Parameters:** dst

- the destination

WritableRaster

for the
filtered

src
**Returns:** the filtered

WritableRaster
**Throws:** NullPointerException

- if

src

is

null
**Throws:** ImagingOpException

- if

src

and

dst

do not have the same number of bands
**Throws:** ImagingOpException

- if

src

cannot be filtered
**Throws:** IllegalArgumentException

- if

src

equals

dst

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

Creates a zeroed destination image with the correct size and number
of bands. If destCM is null, an appropriate ColorModel will be used.

**Specified by:** createCompatibleDestImage

in interface

BufferedImageOp
**Parameters:** src

- Source image for the filter operation.
**Parameters:** destCM

- ColorModel of the destination. Can be null.
**Returns:** a destination

BufferedImage

with the correct
size and number of bands.

- createCompatibleDestRaster

```java
public
WritableRaster
createCompatibleDestRaster​(
Raster
src)
```

Creates a zeroed destination Raster with the correct size and number
of bands, given this source.

**Specified by:** createCompatibleDestRaster

in interface

RasterOp
**Parameters:** src

- the source

Raster
**Returns:** a

WritableRaster

that is compatible with

src

- getBounds2D

```java
public final
Rectangle2D
getBounds2D​(
BufferedImage
src)
```

Returns the bounding box of the filtered destination image. Since
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

Returns the bounding box of the filtered destination Raster. Since
this is not a geometric operation, the bounding box does not
change.

**Specified by:** getBounds2D

in interface

RasterOp
**Parameters:** src

- the source

Raster
**Returns:** a

Rectangle2D

that is the bounding box of
the

Raster

resulting from the filtering
operation.

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

- the

Point2D

that represents the point in
the source image
**Parameters:** dstPt

- The

Point2D

in which to store the result
**Returns:** The

Point2D

in the destination image that
corresponds to the specified point in the source image.

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
**Returns:** The

RenderingHints

object for this

BufferedImageOp

. Returns
null if no hints have been set.

---

#### Method Detail

getEdgeCondition

```java
public int getEdgeCondition()
```

Returns the edge condition.

**Returns:** the edge condition of this

ConvolveOp

.
**See Also:** EDGE_NO_OP

,

EDGE_ZERO_FILL

---

#### getEdgeCondition

public int getEdgeCondition()

Returns the edge condition.

getKernel

```java
public final
Kernel
getKernel()
```

Returns the Kernel.

**Returns:** the

Kernel

of this

ConvolveOp

.

---

#### getKernel

public final

Kernel

getKernel()

Returns the Kernel.

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

Performs a convolution on BufferedImages. Each component of the
source image will be convolved (including the alpha component, if
present).
If the color model in the source image is not the same as that
in the destination image, the pixels will be converted
in the destination. If the destination image is null,
a BufferedImage will be created with the source ColorModel.
The IllegalArgumentException may be thrown if the source is the
same as the destination.

**Specified by:** filter

in interface

BufferedImageOp
**Parameters:** src

- the source

BufferedImage

to filter
**Parameters:** dst

- the destination

BufferedImage

for the
filtered

src
**Returns:** the filtered

BufferedImage
**Throws:** NullPointerException

- if

src

is

null
**Throws:** IllegalArgumentException

- if

src

equals

dst
**Throws:** ImagingOpException

- if

src

cannot be filtered

---

#### filter

public final

BufferedImage

filter​(

BufferedImage

src,

BufferedImage

dst)

Performs a convolution on BufferedImages. Each component of the
source image will be convolved (including the alpha component, if
present).
If the color model in the source image is not the same as that
in the destination image, the pixels will be converted
in the destination. If the destination image is null,
a BufferedImage will be created with the source ColorModel.
The IllegalArgumentException may be thrown if the source is the
same as the destination.

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

Performs a convolution on Rasters. Each band of the source Raster
will be convolved.
The source and destination must have the same number of bands.
If the destination Raster is null, a new Raster will be created.
The IllegalArgumentException may be thrown if the source is
the same as the destination.

**Specified by:** filter

in interface

RasterOp
**Parameters:** src

- the source

Raster

to filter
**Parameters:** dst

- the destination

WritableRaster

for the
filtered

src
**Returns:** the filtered

WritableRaster
**Throws:** NullPointerException

- if

src

is

null
**Throws:** ImagingOpException

- if

src

and

dst

do not have the same number of bands
**Throws:** ImagingOpException

- if

src

cannot be filtered
**Throws:** IllegalArgumentException

- if

src

equals

dst

---

#### filter

public final

WritableRaster

filter​(

Raster

src,

WritableRaster

dst)

Performs a convolution on Rasters. Each band of the source Raster
will be convolved.
The source and destination must have the same number of bands.
If the destination Raster is null, a new Raster will be created.
The IllegalArgumentException may be thrown if the source is
the same as the destination.

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

Creates a zeroed destination image with the correct size and number
of bands. If destCM is null, an appropriate ColorModel will be used.

**Specified by:** createCompatibleDestImage

in interface

BufferedImageOp
**Parameters:** src

- Source image for the filter operation.
**Parameters:** destCM

- ColorModel of the destination. Can be null.
**Returns:** a destination

BufferedImage

with the correct
size and number of bands.

---

#### createCompatibleDestImage

public

BufferedImage

createCompatibleDestImage​(

BufferedImage

src,

ColorModel

destCM)

Creates a zeroed destination image with the correct size and number
of bands. If destCM is null, an appropriate ColorModel will be used.

createCompatibleDestRaster

```java
public
WritableRaster
createCompatibleDestRaster​(
Raster
src)
```

Creates a zeroed destination Raster with the correct size and number
of bands, given this source.

**Specified by:** createCompatibleDestRaster

in interface

RasterOp
**Parameters:** src

- the source

Raster
**Returns:** a

WritableRaster

that is compatible with

src

---

#### createCompatibleDestRaster

public

WritableRaster

createCompatibleDestRaster​(

Raster

src)

Creates a zeroed destination Raster with the correct size and number
of bands, given this source.

getBounds2D

```java
public final
Rectangle2D
getBounds2D​(
BufferedImage
src)
```

Returns the bounding box of the filtered destination image. Since
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

Returns the bounding box of the filtered destination image. Since
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

Returns the bounding box of the filtered destination Raster. Since
this is not a geometric operation, the bounding box does not
change.

**Specified by:** getBounds2D

in interface

RasterOp
**Parameters:** src

- the source

Raster
**Returns:** a

Rectangle2D

that is the bounding box of
the

Raster

resulting from the filtering
operation.

---

#### getBounds2D

public final

Rectangle2D

getBounds2D​(

Raster

src)

Returns the bounding box of the filtered destination Raster. Since
this is not a geometric operation, the bounding box does not
change.

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

- the

Point2D

that represents the point in
the source image
**Parameters:** dstPt

- The

Point2D

in which to store the result
**Returns:** The

Point2D

in the destination image that
corresponds to the specified point in the source image.

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
**Returns:** The

RenderingHints

object for this

BufferedImageOp

. Returns
null if no hints have been set.

---

#### getRenderingHints

public final

RenderingHints

getRenderingHints()

Returns the rendering hints for this op.

---

