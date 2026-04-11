# Interface RasterOp

**Source:** `java.desktop\java\awt\image\RasterOp.html`

### Class Description

```java
public interface
RasterOp
```

This interface describes single-input/single-output
operations performed on Raster objects. It is implemented by such
classes as AffineTransformOp, ConvolveOp, and LookupOp. The Source
and Destination objects must contain the appropriate number
of bands for the particular classes implementing this interface.
Otherwise, an exception is thrown. This interface cannot be used to
describe more sophisticated Ops such as ones that take multiple sources.
Each class implementing this interface will specify whether or not it
will allow an in-place filtering operation (i.e. source object equal
to the destination object). Note that the restriction to single-input
operations means that the values of destination pixels prior to the
operation are not used as input to the filter operation.

**All Known Implementing Classes:** AffineTransformOp

,

BandCombineOp

,

ColorConvertOp

,

ConvolveOp

,

LookupOp

,

RescaleOp

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### WritableRaster
filter​(
Raster
src,

WritableRaster
dest)

Performs a single-input/single-output operation from a source Raster
to a destination Raster. If the destination Raster is null, a
new Raster will be created. The IllegalArgumentException may be thrown
if the source and/or destination Raster is incompatible with the types
of Rasters allowed by the class implementing this filter.

**Parameters:**
- src

- the source

Raster
- dest

- the destination

WritableRaster

**Returns:**
- a

WritableRaster

that represents the result of
the filtering operation.

---

#### Rectangle2D
getBounds2D​(
Raster
src)

Returns the bounding box of the filtered destination Raster.
The IllegalArgumentException may be thrown if the source Raster
is incompatible with the types of Rasters allowed
by the class implementing this filter.

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

#### WritableRaster
createCompatibleDestRaster​(
Raster
src)

Creates a zeroed destination Raster with the correct size and number of
bands.
The IllegalArgumentException may be thrown if the source Raster
is incompatible with the types of Rasters allowed
by the class implementing this filter.

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

#### Point2D
getPoint2D​(
Point2D
srcPt,

Point2D
dstPt)

Returns the location of the destination point given a
point in the source Raster. If dstPt is non-null, it
will be used to hold the return value.

**Parameters:**
- srcPt

- the source

Point2D
- dstPt

- the destination

Point2D

**Returns:**
- the location of the destination point.

---

#### RenderingHints
getRenderingHints()

Returns the rendering hints for this RasterOp. Returns
null if no hints have been set.

**Returns:**
- the

RenderingHints

object of this

RasterOp

.

---

### Additional Sections

#### Interface RasterOp

**All Known Implementing Classes:** AffineTransformOp

,

BandCombineOp

,

ColorConvertOp

,

ConvolveOp

,

LookupOp

,

RescaleOp

```java
public interface
RasterOp
```

This interface describes single-input/single-output
operations performed on Raster objects. It is implemented by such
classes as AffineTransformOp, ConvolveOp, and LookupOp. The Source
and Destination objects must contain the appropriate number
of bands for the particular classes implementing this interface.
Otherwise, an exception is thrown. This interface cannot be used to
describe more sophisticated Ops such as ones that take multiple sources.
Each class implementing this interface will specify whether or not it
will allow an in-place filtering operation (i.e. source object equal
to the destination object). Note that the restriction to single-input
operations means that the values of destination pixels prior to the
operation are not used as input to the filter operation.

**See Also:** AffineTransformOp

,

BandCombineOp

,

ColorConvertOp

,

ConvolveOp

,

LookupOp

,

RescaleOp

public interface

RasterOp

This interface describes single-input/single-output
operations performed on Raster objects. It is implemented by such
classes as AffineTransformOp, ConvolveOp, and LookupOp. The Source
and Destination objects must contain the appropriate number
of bands for the particular classes implementing this interface.
Otherwise, an exception is thrown. This interface cannot be used to
describe more sophisticated Ops such as ones that take multiple sources.
Each class implementing this interface will specify whether or not it
will allow an in-place filtering operation (i.e. source object equal
to the destination object). Note that the restriction to single-input
operations means that the values of destination pixels prior to the
operation are not used as input to the filter operation.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

WritableRaster

createCompatibleDestRaster

​(

Raster

src)

Creates a zeroed destination Raster with the correct size and number of
bands.

WritableRaster

filter

​(

Raster

src,

WritableRaster

dest)

Performs a single-input/single-output operation from a source Raster
to a destination Raster.

Rectangle2D

getBounds2D

​(

Raster

src)

Returns the bounding box of the filtered destination Raster.

Point2D

getPoint2D

​(

Point2D

srcPt,

Point2D

dstPt)

Returns the location of the destination point given a
point in the source Raster.

RenderingHints

getRenderingHints

()

Returns the rendering hints for this RasterOp.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

WritableRaster

createCompatibleDestRaster

​(

Raster

src)

Creates a zeroed destination Raster with the correct size and number of
bands.

WritableRaster

filter

​(

Raster

src,

WritableRaster

dest)

Performs a single-input/single-output operation from a source Raster
to a destination Raster.

Rectangle2D

getBounds2D

​(

Raster

src)

Returns the bounding box of the filtered destination Raster.

Point2D

getPoint2D

​(

Point2D

srcPt,

Point2D

dstPt)

Returns the location of the destination point given a
point in the source Raster.

RenderingHints

getRenderingHints

()

Returns the rendering hints for this RasterOp.

---

#### Method Summary

Creates a zeroed destination Raster with the correct size and number of
bands.

Performs a single-input/single-output operation from a source Raster
to a destination Raster.

Returns the bounding box of the filtered destination Raster.

Returns the location of the destination point given a
point in the source Raster.

Returns the rendering hints for this RasterOp.

============ METHOD DETAIL ==========

- Method Detail

- filter

```java
WritableRaster
filter​(
Raster
src,

WritableRaster
dest)
```

Performs a single-input/single-output operation from a source Raster
to a destination Raster. If the destination Raster is null, a
new Raster will be created. The IllegalArgumentException may be thrown
if the source and/or destination Raster is incompatible with the types
of Rasters allowed by the class implementing this filter.

**Parameters:** src

- the source

Raster
**Parameters:** dest

- the destination

WritableRaster
**Returns:** a

WritableRaster

that represents the result of
the filtering operation.

- getBounds2D

```java
Rectangle2D
getBounds2D​(
Raster
src)
```

Returns the bounding box of the filtered destination Raster.
The IllegalArgumentException may be thrown if the source Raster
is incompatible with the types of Rasters allowed
by the class implementing this filter.

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

- createCompatibleDestRaster

```java
WritableRaster
createCompatibleDestRaster​(
Raster
src)
```

Creates a zeroed destination Raster with the correct size and number of
bands.
The IllegalArgumentException may be thrown if the source Raster
is incompatible with the types of Rasters allowed
by the class implementing this filter.

**Parameters:** src

- the source

Raster
**Returns:** a

WritableRaster

that is compatible with

src

- getPoint2D

```java
Point2D
getPoint2D​(
Point2D
srcPt,

Point2D
dstPt)
```

Returns the location of the destination point given a
point in the source Raster. If dstPt is non-null, it
will be used to hold the return value.

**Parameters:** srcPt

- the source

Point2D
**Parameters:** dstPt

- the destination

Point2D
**Returns:** the location of the destination point.

- getRenderingHints

```java
RenderingHints
getRenderingHints()
```

Returns the rendering hints for this RasterOp. Returns
null if no hints have been set.

**Returns:** the

RenderingHints

object of this

RasterOp

.

Method Detail

- filter

```java
WritableRaster
filter​(
Raster
src,

WritableRaster
dest)
```

Performs a single-input/single-output operation from a source Raster
to a destination Raster. If the destination Raster is null, a
new Raster will be created. The IllegalArgumentException may be thrown
if the source and/or destination Raster is incompatible with the types
of Rasters allowed by the class implementing this filter.

**Parameters:** src

- the source

Raster
**Parameters:** dest

- the destination

WritableRaster
**Returns:** a

WritableRaster

that represents the result of
the filtering operation.

- getBounds2D

```java
Rectangle2D
getBounds2D​(
Raster
src)
```

Returns the bounding box of the filtered destination Raster.
The IllegalArgumentException may be thrown if the source Raster
is incompatible with the types of Rasters allowed
by the class implementing this filter.

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

- createCompatibleDestRaster

```java
WritableRaster
createCompatibleDestRaster​(
Raster
src)
```

Creates a zeroed destination Raster with the correct size and number of
bands.
The IllegalArgumentException may be thrown if the source Raster
is incompatible with the types of Rasters allowed
by the class implementing this filter.

**Parameters:** src

- the source

Raster
**Returns:** a

WritableRaster

that is compatible with

src

- getPoint2D

```java
Point2D
getPoint2D​(
Point2D
srcPt,

Point2D
dstPt)
```

Returns the location of the destination point given a
point in the source Raster. If dstPt is non-null, it
will be used to hold the return value.

**Parameters:** srcPt

- the source

Point2D
**Parameters:** dstPt

- the destination

Point2D
**Returns:** the location of the destination point.

- getRenderingHints

```java
RenderingHints
getRenderingHints()
```

Returns the rendering hints for this RasterOp. Returns
null if no hints have been set.

**Returns:** the

RenderingHints

object of this

RasterOp

.

---

#### Method Detail

filter

```java
WritableRaster
filter​(
Raster
src,

WritableRaster
dest)
```

Performs a single-input/single-output operation from a source Raster
to a destination Raster. If the destination Raster is null, a
new Raster will be created. The IllegalArgumentException may be thrown
if the source and/or destination Raster is incompatible with the types
of Rasters allowed by the class implementing this filter.

**Parameters:** src

- the source

Raster
**Parameters:** dest

- the destination

WritableRaster
**Returns:** a

WritableRaster

that represents the result of
the filtering operation.

---

#### filter

WritableRaster

filter​(

Raster

src,

WritableRaster

dest)

Performs a single-input/single-output operation from a source Raster
to a destination Raster. If the destination Raster is null, a
new Raster will be created. The IllegalArgumentException may be thrown
if the source and/or destination Raster is incompatible with the types
of Rasters allowed by the class implementing this filter.

getBounds2D

```java
Rectangle2D
getBounds2D​(
Raster
src)
```

Returns the bounding box of the filtered destination Raster.
The IllegalArgumentException may be thrown if the source Raster
is incompatible with the types of Rasters allowed
by the class implementing this filter.

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

Rectangle2D

getBounds2D​(

Raster

src)

Returns the bounding box of the filtered destination Raster.
The IllegalArgumentException may be thrown if the source Raster
is incompatible with the types of Rasters allowed
by the class implementing this filter.

createCompatibleDestRaster

```java
WritableRaster
createCompatibleDestRaster​(
Raster
src)
```

Creates a zeroed destination Raster with the correct size and number of
bands.
The IllegalArgumentException may be thrown if the source Raster
is incompatible with the types of Rasters allowed
by the class implementing this filter.

**Parameters:** src

- the source

Raster
**Returns:** a

WritableRaster

that is compatible with

src

---

#### createCompatibleDestRaster

WritableRaster

createCompatibleDestRaster​(

Raster

src)

Creates a zeroed destination Raster with the correct size and number of
bands.
The IllegalArgumentException may be thrown if the source Raster
is incompatible with the types of Rasters allowed
by the class implementing this filter.

getPoint2D

```java
Point2D
getPoint2D​(
Point2D
srcPt,

Point2D
dstPt)
```

Returns the location of the destination point given a
point in the source Raster. If dstPt is non-null, it
will be used to hold the return value.

**Parameters:** srcPt

- the source

Point2D
**Parameters:** dstPt

- the destination

Point2D
**Returns:** the location of the destination point.

---

#### getPoint2D

Point2D

getPoint2D​(

Point2D

srcPt,

Point2D

dstPt)

Returns the location of the destination point given a
point in the source Raster. If dstPt is non-null, it
will be used to hold the return value.

getRenderingHints

```java
RenderingHints
getRenderingHints()
```

Returns the rendering hints for this RasterOp. Returns
null if no hints have been set.

**Returns:** the

RenderingHints

object of this

RasterOp

.

---

#### getRenderingHints

RenderingHints

getRenderingHints()

Returns the rendering hints for this RasterOp. Returns
null if no hints have been set.

---

