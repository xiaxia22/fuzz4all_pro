# Class BandCombineOp

**Source:** `java.desktop\java\awt\image\BandCombineOp.html`

### Class Description

```java
public class
BandCombineOp

extends
Object

implements
RasterOp
```

This class performs an arbitrary linear combination of the bands
in a

Raster

, using a specified matrix.

The width of the matrix must be equal to the number of bands in the
source

Raster

, optionally plus one. If there is one more
column in the matrix than the number of bands, there is an implied 1 at the
end of the vector of band samples representing a pixel. The height
of the matrix must be equal to the number of bands in the destination.

For example, a 3-banded

Raster

might have the following
transformation applied to each pixel in order to invert the second band of
the

Raster

.

```java
[ 1.0 0.0 0.0 0.0 ] [ b1 ]
[ 0.0 -1.0 0.0 255.0 ] x [ b2 ]
[ 0.0 0.0 1.0 0.0 ] [ b3 ]
[ 1 ]
```

Note that the source and destination can be the same object.

**All Implemented Interfaces:** RasterOp

---

### Field Details

*No entries found.*

### Constructor Details

#### public BandCombineOp​(float[][] matrix,

RenderingHints
hints)

Constructs a

BandCombineOp

with the specified matrix.
The width of the matrix must be equal to the number of bands in
the source

Raster

, optionally plus one. If there is one
more column in the matrix than the number of bands, there is an implied
1 at the end of the vector of band samples representing a pixel. The
height of the matrix must be equal to the number of bands in the
destination.

The first subscript is the row index and the second
is the column index. This operation uses none of the currently
defined rendering hints; the

RenderingHints

argument can be
null.

**Parameters:**
- matrix

- The matrix to use for the band combine operation.
- hints

- The

RenderingHints

object for this operation.
Not currently used so it can be null.

---

### Method Details

#### public final float[][] getMatrix()

Returns a copy of the linear combination matrix.

**Returns:**
- The matrix associated with this band combine operation.

---

#### public
WritableRaster
filter​(
Raster
src,

WritableRaster
dst)

Transforms the

Raster

using the matrix specified in the
constructor. An

IllegalArgumentException

may be thrown if
the number of bands in the source or destination is incompatible with
the matrix. See the class comments for more details.

If the destination is null, it will be created with a number of bands
equalling the number of rows in the matrix. No exception is thrown
if the operation causes a data overflow.

**Specified by:**
- filter

in interface

RasterOp

**Parameters:**
- src

- The

Raster

to be filtered.
- dst

- The

Raster

in which to store the results
of the filter operation.

**Returns:**
- The filtered

Raster

.

**Throws:**
- IllegalArgumentException

- If the number of bands in the
source or destination is incompatible with the matrix.

---

#### public final
Rectangle2D
getBounds2D​(
Raster
src)

Returns the bounding box of the transformed destination. Since
this is not a geometric operation, the bounding box is the same for
the source and destination.
An

IllegalArgumentException

may be thrown if the number of
bands in the source is incompatible with the matrix. See
the class comments for more details.

**Specified by:**
- getBounds2D

in interface

RasterOp

**Parameters:**
- src

- The

Raster

to be filtered.

**Returns:**
- The

Rectangle2D

representing the destination
image's bounding box.

**Throws:**
- IllegalArgumentException

- If the number of bands in the source
is incompatible with the matrix.

---

#### public
WritableRaster
createCompatibleDestRaster​(
Raster
src)

Creates a zeroed destination

Raster

with the correct size
and number of bands.
An

IllegalArgumentException

may be thrown if the number of
bands in the source is incompatible with the matrix. See
the class comments for more details.

**Specified by:**
- createCompatibleDestRaster

in interface

RasterOp

**Parameters:**
- src

- The

Raster

to be filtered.

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
point in the source

Raster

. If

dstPt

is
specified, it is used to hold the return value.
Since this is not a geometric operation, the point returned
is the same as the specified

srcPt

.

**Specified by:**
- getPoint2D

in interface

RasterOp

**Parameters:**
- srcPt

- The

Point2D

that represents the point in
the source

Raster
- dstPt

- The

Point2D

in which to store the result.

**Returns:**
- The

Point2D

in the destination image that
corresponds to the specified point in the source image.

---

#### public final
RenderingHints
getRenderingHints()

Returns the rendering hints for this operation.

**Specified by:**
- getRenderingHints

in interface

RasterOp

**Returns:**
- The

RenderingHints

object associated with this
operation. Returns null if no hints have been set.

---

### Additional Sections

#### Class BandCombineOp

java.lang.Object

- java.awt.image.BandCombineOp

java.awt.image.BandCombineOp

**All Implemented Interfaces:** RasterOp

```java
public class
BandCombineOp

extends
Object

implements
RasterOp
```

This class performs an arbitrary linear combination of the bands
in a

Raster

, using a specified matrix.

The width of the matrix must be equal to the number of bands in the
source

Raster

, optionally plus one. If there is one more
column in the matrix than the number of bands, there is an implied 1 at the
end of the vector of band samples representing a pixel. The height
of the matrix must be equal to the number of bands in the destination.

For example, a 3-banded

Raster

might have the following
transformation applied to each pixel in order to invert the second band of
the

Raster

.

```java
[ 1.0 0.0 0.0 0.0 ] [ b1 ]
[ 0.0 -1.0 0.0 255.0 ] x [ b2 ]
[ 0.0 0.0 1.0 0.0 ] [ b3 ]
[ 1 ]
```

Note that the source and destination can be the same object.

public class

BandCombineOp

extends

Object

implements

RasterOp

This class performs an arbitrary linear combination of the bands
in a

Raster

, using a specified matrix.

The width of the matrix must be equal to the number of bands in the
source

Raster

, optionally plus one. If there is one more
column in the matrix than the number of bands, there is an implied 1 at the
end of the vector of band samples representing a pixel. The height
of the matrix must be equal to the number of bands in the destination.

For example, a 3-banded

Raster

might have the following
transformation applied to each pixel in order to invert the second band of
the

Raster

.

```java
[ 1.0 0.0 0.0 0.0 ] [ b1 ]
[ 0.0 -1.0 0.0 255.0 ] x [ b2 ]
[ 0.0 0.0 1.0 0.0 ] [ b3 ]
[ 1 ]
```

Note that the source and destination can be the same object.

The width of the matrix must be equal to the number of bands in the
source

Raster

, optionally plus one. If there is one more
column in the matrix than the number of bands, there is an implied 1 at the
end of the vector of band samples representing a pixel. The height
of the matrix must be equal to the number of bands in the destination.

For example, a 3-banded

Raster

might have the following
transformation applied to each pixel in order to invert the second band of
the

Raster

.

```java
[ 1.0 0.0 0.0 0.0 ] [ b1 ]
[ 0.0 -1.0 0.0 255.0 ] x [ b2 ]
[ 0.0 0.0 1.0 0.0 ] [ b3 ]
[ 1 ]
```

Note that the source and destination can be the same object.

For example, a 3-banded

Raster

might have the following
transformation applied to each pixel in order to invert the second band of
the

Raster

.

```java
[ 1.0 0.0 0.0 0.0 ] [ b1 ]
[ 0.0 -1.0 0.0 255.0 ] x [ b2 ]
[ 0.0 0.0 1.0 0.0 ] [ b3 ]
[ 1 ]
```

Note that the source and destination can be the same object.

[ 1.0 0.0 0.0 0.0 ] [ b1 ]
[ 0.0 -1.0 0.0 255.0 ] x [ b2 ]
[ 0.0 0.0 1.0 0.0 ] [ b3 ]
[ 1 ]

Note that the source and destination can be the same object.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BandCombineOp

​(float[][] matrix,

RenderingHints

hints)

Constructs a

BandCombineOp

with the specified matrix.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

WritableRaster

createCompatibleDestRaster

​(

Raster

src)

Creates a zeroed destination

Raster

with the correct size
and number of bands.

WritableRaster

filter

​(

Raster

src,

WritableRaster

dst)

Transforms the

Raster

using the matrix specified in the
constructor.

Rectangle2D

getBounds2D

​(

Raster

src)

Returns the bounding box of the transformed destination.

float[][]

getMatrix

()

Returns a copy of the linear combination matrix.

Point2D

getPoint2D

​(

Point2D

srcPt,

Point2D

dstPt)

Returns the location of the corresponding destination point given a
point in the source

Raster

.

RenderingHints

getRenderingHints

()

Returns the rendering hints for this operation.

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

BandCombineOp

​(float[][] matrix,

RenderingHints

hints)

Constructs a

BandCombineOp

with the specified matrix.

---

#### Constructor Summary

Constructs a

BandCombineOp

with the specified matrix.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

WritableRaster

createCompatibleDestRaster

​(

Raster

src)

Creates a zeroed destination

Raster

with the correct size
and number of bands.

WritableRaster

filter

​(

Raster

src,

WritableRaster

dst)

Transforms the

Raster

using the matrix specified in the
constructor.

Rectangle2D

getBounds2D

​(

Raster

src)

Returns the bounding box of the transformed destination.

float[][]

getMatrix

()

Returns a copy of the linear combination matrix.

Point2D

getPoint2D

​(

Point2D

srcPt,

Point2D

dstPt)

Returns the location of the corresponding destination point given a
point in the source

Raster

.

RenderingHints

getRenderingHints

()

Returns the rendering hints for this operation.

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

Creates a zeroed destination

Raster

with the correct size
and number of bands.

Transforms the

Raster

using the matrix specified in the
constructor.

Returns the bounding box of the transformed destination.

Returns a copy of the linear combination matrix.

Returns the location of the corresponding destination point given a
point in the source

Raster

.

Returns the rendering hints for this operation.

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

- BandCombineOp

```java
public BandCombineOp​(float[][] matrix,

RenderingHints
hints)
```

Constructs a

BandCombineOp

with the specified matrix.
The width of the matrix must be equal to the number of bands in
the source

Raster

, optionally plus one. If there is one
more column in the matrix than the number of bands, there is an implied
1 at the end of the vector of band samples representing a pixel. The
height of the matrix must be equal to the number of bands in the
destination.

The first subscript is the row index and the second
is the column index. This operation uses none of the currently
defined rendering hints; the

RenderingHints

argument can be
null.

**Parameters:** matrix

- The matrix to use for the band combine operation.
**Parameters:** hints

- The

RenderingHints

object for this operation.
Not currently used so it can be null.

============ METHOD DETAIL ==========

- Method Detail

- getMatrix

```java
public final float[][] getMatrix()
```

Returns a copy of the linear combination matrix.

**Returns:** The matrix associated with this band combine operation.

- filter

```java
public
WritableRaster
filter​(
Raster
src,

WritableRaster
dst)
```

Transforms the

Raster

using the matrix specified in the
constructor. An

IllegalArgumentException

may be thrown if
the number of bands in the source or destination is incompatible with
the matrix. See the class comments for more details.

If the destination is null, it will be created with a number of bands
equalling the number of rows in the matrix. No exception is thrown
if the operation causes a data overflow.

**Specified by:** filter

in interface

RasterOp
**Parameters:** src

- The

Raster

to be filtered.
**Parameters:** dst

- The

Raster

in which to store the results
of the filter operation.
**Returns:** The filtered

Raster

.
**Throws:** IllegalArgumentException

- If the number of bands in the
source or destination is incompatible with the matrix.

- getBounds2D

```java
public final
Rectangle2D
getBounds2D​(
Raster
src)
```

Returns the bounding box of the transformed destination. Since
this is not a geometric operation, the bounding box is the same for
the source and destination.
An

IllegalArgumentException

may be thrown if the number of
bands in the source is incompatible with the matrix. See
the class comments for more details.

**Specified by:** getBounds2D

in interface

RasterOp
**Parameters:** src

- The

Raster

to be filtered.
**Returns:** The

Rectangle2D

representing the destination
image's bounding box.
**Throws:** IllegalArgumentException

- If the number of bands in the source
is incompatible with the matrix.

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
and number of bands.
An

IllegalArgumentException

may be thrown if the number of
bands in the source is incompatible with the matrix. See
the class comments for more details.

**Specified by:** createCompatibleDestRaster

in interface

RasterOp
**Parameters:** src

- The

Raster

to be filtered.
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
point in the source

Raster

. If

dstPt

is
specified, it is used to hold the return value.
Since this is not a geometric operation, the point returned
is the same as the specified

srcPt

.

**Specified by:** getPoint2D

in interface

RasterOp
**Parameters:** srcPt

- The

Point2D

that represents the point in
the source

Raster
**Parameters:** dstPt

- The

Point2D

in which to store the result.
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

Returns the rendering hints for this operation.

**Specified by:** getRenderingHints

in interface

RasterOp
**Returns:** The

RenderingHints

object associated with this
operation. Returns null if no hints have been set.

Constructor Detail

- BandCombineOp

```java
public BandCombineOp​(float[][] matrix,

RenderingHints
hints)
```

Constructs a

BandCombineOp

with the specified matrix.
The width of the matrix must be equal to the number of bands in
the source

Raster

, optionally plus one. If there is one
more column in the matrix than the number of bands, there is an implied
1 at the end of the vector of band samples representing a pixel. The
height of the matrix must be equal to the number of bands in the
destination.

The first subscript is the row index and the second
is the column index. This operation uses none of the currently
defined rendering hints; the

RenderingHints

argument can be
null.

**Parameters:** matrix

- The matrix to use for the band combine operation.
**Parameters:** hints

- The

RenderingHints

object for this operation.
Not currently used so it can be null.

---

#### Constructor Detail

BandCombineOp

```java
public BandCombineOp​(float[][] matrix,

RenderingHints
hints)
```

Constructs a

BandCombineOp

with the specified matrix.
The width of the matrix must be equal to the number of bands in
the source

Raster

, optionally plus one. If there is one
more column in the matrix than the number of bands, there is an implied
1 at the end of the vector of band samples representing a pixel. The
height of the matrix must be equal to the number of bands in the
destination.

The first subscript is the row index and the second
is the column index. This operation uses none of the currently
defined rendering hints; the

RenderingHints

argument can be
null.

**Parameters:** matrix

- The matrix to use for the band combine operation.
**Parameters:** hints

- The

RenderingHints

object for this operation.
Not currently used so it can be null.

---

#### BandCombineOp

public BandCombineOp​(float[][] matrix,

RenderingHints

hints)

Constructs a

BandCombineOp

with the specified matrix.
The width of the matrix must be equal to the number of bands in
the source

Raster

, optionally plus one. If there is one
more column in the matrix than the number of bands, there is an implied
1 at the end of the vector of band samples representing a pixel. The
height of the matrix must be equal to the number of bands in the
destination.

The first subscript is the row index and the second
is the column index. This operation uses none of the currently
defined rendering hints; the

RenderingHints

argument can be
null.

The first subscript is the row index and the second
is the column index. This operation uses none of the currently
defined rendering hints; the

RenderingHints

argument can be
null.

Method Detail

- getMatrix

```java
public final float[][] getMatrix()
```

Returns a copy of the linear combination matrix.

**Returns:** The matrix associated with this band combine operation.

- filter

```java
public
WritableRaster
filter​(
Raster
src,

WritableRaster
dst)
```

Transforms the

Raster

using the matrix specified in the
constructor. An

IllegalArgumentException

may be thrown if
the number of bands in the source or destination is incompatible with
the matrix. See the class comments for more details.

If the destination is null, it will be created with a number of bands
equalling the number of rows in the matrix. No exception is thrown
if the operation causes a data overflow.

**Specified by:** filter

in interface

RasterOp
**Parameters:** src

- The

Raster

to be filtered.
**Parameters:** dst

- The

Raster

in which to store the results
of the filter operation.
**Returns:** The filtered

Raster

.
**Throws:** IllegalArgumentException

- If the number of bands in the
source or destination is incompatible with the matrix.

- getBounds2D

```java
public final
Rectangle2D
getBounds2D​(
Raster
src)
```

Returns the bounding box of the transformed destination. Since
this is not a geometric operation, the bounding box is the same for
the source and destination.
An

IllegalArgumentException

may be thrown if the number of
bands in the source is incompatible with the matrix. See
the class comments for more details.

**Specified by:** getBounds2D

in interface

RasterOp
**Parameters:** src

- The

Raster

to be filtered.
**Returns:** The

Rectangle2D

representing the destination
image's bounding box.
**Throws:** IllegalArgumentException

- If the number of bands in the source
is incompatible with the matrix.

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
and number of bands.
An

IllegalArgumentException

may be thrown if the number of
bands in the source is incompatible with the matrix. See
the class comments for more details.

**Specified by:** createCompatibleDestRaster

in interface

RasterOp
**Parameters:** src

- The

Raster

to be filtered.
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
point in the source

Raster

. If

dstPt

is
specified, it is used to hold the return value.
Since this is not a geometric operation, the point returned
is the same as the specified

srcPt

.

**Specified by:** getPoint2D

in interface

RasterOp
**Parameters:** srcPt

- The

Point2D

that represents the point in
the source

Raster
**Parameters:** dstPt

- The

Point2D

in which to store the result.
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

Returns the rendering hints for this operation.

**Specified by:** getRenderingHints

in interface

RasterOp
**Returns:** The

RenderingHints

object associated with this
operation. Returns null if no hints have been set.

---

#### Method Detail

getMatrix

```java
public final float[][] getMatrix()
```

Returns a copy of the linear combination matrix.

**Returns:** The matrix associated with this band combine operation.

---

#### getMatrix

public final float[][] getMatrix()

Returns a copy of the linear combination matrix.

filter

```java
public
WritableRaster
filter​(
Raster
src,

WritableRaster
dst)
```

Transforms the

Raster

using the matrix specified in the
constructor. An

IllegalArgumentException

may be thrown if
the number of bands in the source or destination is incompatible with
the matrix. See the class comments for more details.

If the destination is null, it will be created with a number of bands
equalling the number of rows in the matrix. No exception is thrown
if the operation causes a data overflow.

**Specified by:** filter

in interface

RasterOp
**Parameters:** src

- The

Raster

to be filtered.
**Parameters:** dst

- The

Raster

in which to store the results
of the filter operation.
**Returns:** The filtered

Raster

.
**Throws:** IllegalArgumentException

- If the number of bands in the
source or destination is incompatible with the matrix.

---

#### filter

public

WritableRaster

filter​(

Raster

src,

WritableRaster

dst)

Transforms the

Raster

using the matrix specified in the
constructor. An

IllegalArgumentException

may be thrown if
the number of bands in the source or destination is incompatible with
the matrix. See the class comments for more details.

If the destination is null, it will be created with a number of bands
equalling the number of rows in the matrix. No exception is thrown
if the operation causes a data overflow.

If the destination is null, it will be created with a number of bands
equalling the number of rows in the matrix. No exception is thrown
if the operation causes a data overflow.

getBounds2D

```java
public final
Rectangle2D
getBounds2D​(
Raster
src)
```

Returns the bounding box of the transformed destination. Since
this is not a geometric operation, the bounding box is the same for
the source and destination.
An

IllegalArgumentException

may be thrown if the number of
bands in the source is incompatible with the matrix. See
the class comments for more details.

**Specified by:** getBounds2D

in interface

RasterOp
**Parameters:** src

- The

Raster

to be filtered.
**Returns:** The

Rectangle2D

representing the destination
image's bounding box.
**Throws:** IllegalArgumentException

- If the number of bands in the source
is incompatible with the matrix.

---

#### getBounds2D

public final

Rectangle2D

getBounds2D​(

Raster

src)

Returns the bounding box of the transformed destination. Since
this is not a geometric operation, the bounding box is the same for
the source and destination.
An

IllegalArgumentException

may be thrown if the number of
bands in the source is incompatible with the matrix. See
the class comments for more details.

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
and number of bands.
An

IllegalArgumentException

may be thrown if the number of
bands in the source is incompatible with the matrix. See
the class comments for more details.

**Specified by:** createCompatibleDestRaster

in interface

RasterOp
**Parameters:** src

- The

Raster

to be filtered.
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
and number of bands.
An

IllegalArgumentException

may be thrown if the number of
bands in the source is incompatible with the matrix. See
the class comments for more details.

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
point in the source

Raster

. If

dstPt

is
specified, it is used to hold the return value.
Since this is not a geometric operation, the point returned
is the same as the specified

srcPt

.

**Specified by:** getPoint2D

in interface

RasterOp
**Parameters:** srcPt

- The

Point2D

that represents the point in
the source

Raster
**Parameters:** dstPt

- The

Point2D

in which to store the result.
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

Returns the location of the corresponding destination point given a
point in the source

Raster

. If

dstPt

is
specified, it is used to hold the return value.
Since this is not a geometric operation, the point returned
is the same as the specified

srcPt

.

getRenderingHints

```java
public final
RenderingHints
getRenderingHints()
```

Returns the rendering hints for this operation.

**Specified by:** getRenderingHints

in interface

RasterOp
**Returns:** The

RenderingHints

object associated with this
operation. Returns null if no hints have been set.

---

#### getRenderingHints

public final

RenderingHints

getRenderingHints()

Returns the rendering hints for this operation.

---

