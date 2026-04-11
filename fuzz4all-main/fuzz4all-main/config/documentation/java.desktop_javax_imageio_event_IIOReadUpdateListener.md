# Interface IIOReadUpdateListener

**Source:** `java.desktop\javax\imageio\event\IIOReadUpdateListener.html`

### Class Description

```java
public interface
IIOReadUpdateListener

extends
EventListener
```

An interface used by

ImageReader

implementations to
notify callers of their image and thumbnail reading methods of
pixel updates.

**All Superinterfaces:** EventListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void passStarted​(
ImageReader
source,

BufferedImage
theImage,
int pass,
int minPass,
int maxPass,
int minX,
int minY,
int periodX,
int periodY,
int[] bands)

Reports that the current read operation is about to begin a
progressive pass. Readers of formats that support progressive
encoding should use this to notify clients when each pass is
completed when reading a progressively encoded image.

An estimate of the area that will be updated by the pass is
indicated by the

minX

,

minY

,

width

, and

height

parameters. If the
pass is interlaced, that is, it only updates selected rows or
columns, the

periodX

and

periodY

parameters will indicate the degree of subsampling. The set of
bands that may be affected is indicated by the value of

bands

.

**Parameters:**
- source

- the

ImageReader

object calling this
method.
- theImage

- the

BufferedImage

being updated.
- pass

- the number of the pass that is about to begin,
starting with 0.
- minPass

- the index of the first pass that will be decoded.
- maxPass

- the index of the last pass that will be decoded.
- minX

- the X coordinate of the leftmost updated column
of pixels.
- minY

- the Y coordinate of the uppermost updated row
of pixels.
- periodX

- the horizontal spacing between updated pixels;
a value of 1 means no gaps.
- periodY

- the vertical spacing between updated pixels;
a value of 1 means no gaps.
- bands

- an array of

int

s indicating the
set bands that may be updated.

---

#### void imageUpdate​(
ImageReader
source,

BufferedImage
theImage,
int minX,
int minY,
int width,
int height,
int periodX,
int periodY,
int[] bands)

Reports that a given region of the image has been updated.
The application might choose to redisplay the specified area,
for example, in order to provide a progressive display effect,
or perform other incremental processing.

Note that different image format readers may produce
decoded pixels in a variety of different orders. Many readers
will produce pixels in a simple top-to-bottom,
left-to-right-order, but others may use multiple passes of
interlacing, tiling, etc. The sequence of updates may even
differ from call to call depending on network speeds, for
example. A call to this method does not guarantee that all the
specified pixels have actually been updated, only that some
activity has taken place within some subregion of the one
specified.

The particular

ImageReader

implementation may
choose how often to provide updates. Each update specifies
that a given region of the image has been updated since the
last update. A region is described by its spatial bounding box
(

minX

,

minY

,

width

, and

height

); X and Y subsampling factors
(

periodX

and

periodY

); and a set of
updated bands (

bands

). For example, the update:

```java
minX = 10
minY = 20
width = 3
height = 4
periodX = 2
periodY = 3
bands = { 1, 3 }
```

would indicate that bands 1 and 3 of the following pixels were
updated:

```java
(10, 20) (12, 20) (14, 20)
(10, 23) (12, 23) (14, 23)
(10, 26) (12, 26) (14, 26)
(10, 29) (12, 29) (14, 29)
```

**Parameters:**
- source

- the

ImageReader

object calling this method.
- theImage

- the

BufferedImage

being updated.
- minX

- the X coordinate of the leftmost updated column
of pixels.
- minY

- the Y coordinate of the uppermost updated row
of pixels.
- width

- the number of updated pixels horizontally.
- height

- the number of updated pixels vertically.
- periodX

- the horizontal spacing between updated pixels;
a value of 1 means no gaps.
- periodY

- the vertical spacing between updated pixels;
a value of 1 means no gaps.
- bands

- an array of

int

s indicating which
bands are being updated.

---

#### void passComplete​(
ImageReader
source,

BufferedImage
theImage)

Reports that the current read operation has completed a
progressive pass. Readers of formats that support
progressive encoding should use this to notify clients when
each pass is completed when reading a progressively
encoded image.

**Parameters:**
- source

- the

ImageReader

object calling this
method.
- theImage

- the

BufferedImage

being updated.

**See Also:**
- ImageReadParam.setSourceProgressivePasses(int, int)

---

#### void thumbnailPassStarted​(
ImageReader
source,

BufferedImage
theThumbnail,
int pass,
int minPass,
int maxPass,
int minX,
int minY,
int periodX,
int periodY,
int[] bands)

Reports that the current thumbnail read operation is about to
begin a progressive pass. Readers of formats that support
progressive encoding should use this to notify clients when
each pass is completed when reading a progressively encoded
thumbnail image.

**Parameters:**
- source

- the

ImageReader

object calling this
method.
- theThumbnail

- the

BufferedImage

thumbnail
being updated.
- pass

- the number of the pass that is about to begin,
starting with 0.
- minPass

- the index of the first pass that will be decoded.
- maxPass

- the index of the last pass that will be decoded.
- minX

- the X coordinate of the leftmost updated column
of pixels.
- minY

- the Y coordinate of the uppermost updated row
of pixels.
- periodX

- the horizontal spacing between updated pixels;
a value of 1 means no gaps.
- periodY

- the vertical spacing between updated pixels;
a value of 1 means no gaps.
- bands

- an array of

int

s indicating the
set bands that may be updated.

**See Also:**
- passStarted(javax.imageio.ImageReader, java.awt.image.BufferedImage, int, int, int, int, int, int, int, int[])

---

#### void thumbnailUpdate​(
ImageReader
source,

BufferedImage
theThumbnail,
int minX,
int minY,
int width,
int height,
int periodX,
int periodY,
int[] bands)

Reports that a given region of a thumbnail image has been updated.
The application might choose to redisplay the specified area,
for example, in order to provide a progressive display effect,
or perform other incremental processing.

**Parameters:**
- source

- the

ImageReader

object calling this method.
- theThumbnail

- the

BufferedImage

thumbnail
being updated.
- minX

- the X coordinate of the leftmost updated column
of pixels.
- minY

- the Y coordinate of the uppermost updated row
of pixels.
- width

- the number of updated pixels horizontally.
- height

- the number of updated pixels vertically.
- periodX

- the horizontal spacing between updated pixels;
a value of 1 means no gaps.
- periodY

- the vertical spacing between updated pixels;
a value of 1 means no gaps.
- bands

- an array of

int

s indicating which
bands are being updated.

**See Also:**
- imageUpdate(javax.imageio.ImageReader, java.awt.image.BufferedImage, int, int, int, int, int, int, int[])

---

#### void thumbnailPassComplete​(
ImageReader
source,

BufferedImage
theThumbnail)

Reports that the current thumbnail read operation has completed
a progressive pass. Readers of formats that support
progressive encoding should use this to notify clients when
each pass is completed when reading a progressively encoded
thumbnail image.

**Parameters:**
- source

- the

ImageReader

object calling this
method.
- theThumbnail

- the

BufferedImage

thumbnail
being updated.

**See Also:**
- passComplete(javax.imageio.ImageReader, java.awt.image.BufferedImage)

---

### Additional Sections

#### Interface IIOReadUpdateListener

**All Superinterfaces:** EventListener

```java
public interface
IIOReadUpdateListener

extends
EventListener
```

An interface used by

ImageReader

implementations to
notify callers of their image and thumbnail reading methods of
pixel updates.

**See Also:** ImageReader.addIIOReadUpdateListener(javax.imageio.event.IIOReadUpdateListener)

,

ImageReader.removeIIOReadUpdateListener(javax.imageio.event.IIOReadUpdateListener)

public interface

IIOReadUpdateListener

extends

EventListener

An interface used by

ImageReader

implementations to
notify callers of their image and thumbnail reading methods of
pixel updates.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

imageUpdate

​(

ImageReader

source,

BufferedImage

theImage,
int minX,
int minY,
int width,
int height,
int periodX,
int periodY,
int[] bands)

Reports that a given region of the image has been updated.

void

passComplete

​(

ImageReader

source,

BufferedImage

theImage)

Reports that the current read operation has completed a
progressive pass.

void

passStarted

​(

ImageReader

source,

BufferedImage

theImage,
int pass,
int minPass,
int maxPass,
int minX,
int minY,
int periodX,
int periodY,
int[] bands)

Reports that the current read operation is about to begin a
progressive pass.

void

thumbnailPassComplete

​(

ImageReader

source,

BufferedImage

theThumbnail)

Reports that the current thumbnail read operation has completed
a progressive pass.

void

thumbnailPassStarted

​(

ImageReader

source,

BufferedImage

theThumbnail,
int pass,
int minPass,
int maxPass,
int minX,
int minY,
int periodX,
int periodY,
int[] bands)

Reports that the current thumbnail read operation is about to
begin a progressive pass.

void

thumbnailUpdate

​(

ImageReader

source,

BufferedImage

theThumbnail,
int minX,
int minY,
int width,
int height,
int periodX,
int periodY,
int[] bands)

Reports that a given region of a thumbnail image has been updated.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

imageUpdate

​(

ImageReader

source,

BufferedImage

theImage,
int minX,
int minY,
int width,
int height,
int periodX,
int periodY,
int[] bands)

Reports that a given region of the image has been updated.

void

passComplete

​(

ImageReader

source,

BufferedImage

theImage)

Reports that the current read operation has completed a
progressive pass.

void

passStarted

​(

ImageReader

source,

BufferedImage

theImage,
int pass,
int minPass,
int maxPass,
int minX,
int minY,
int periodX,
int periodY,
int[] bands)

Reports that the current read operation is about to begin a
progressive pass.

void

thumbnailPassComplete

​(

ImageReader

source,

BufferedImage

theThumbnail)

Reports that the current thumbnail read operation has completed
a progressive pass.

void

thumbnailPassStarted

​(

ImageReader

source,

BufferedImage

theThumbnail,
int pass,
int minPass,
int maxPass,
int minX,
int minY,
int periodX,
int periodY,
int[] bands)

Reports that the current thumbnail read operation is about to
begin a progressive pass.

void

thumbnailUpdate

​(

ImageReader

source,

BufferedImage

theThumbnail,
int minX,
int minY,
int width,
int height,
int periodX,
int periodY,
int[] bands)

Reports that a given region of a thumbnail image has been updated.

---

#### Method Summary

Reports that a given region of the image has been updated.

Reports that the current read operation has completed a
progressive pass.

Reports that the current read operation is about to begin a
progressive pass.

Reports that the current thumbnail read operation has completed
a progressive pass.

Reports that the current thumbnail read operation is about to
begin a progressive pass.

Reports that a given region of a thumbnail image has been updated.

============ METHOD DETAIL ==========

- Method Detail

- passStarted

```java
void passStarted​(
ImageReader
source,

BufferedImage
theImage,
int pass,
int minPass,
int maxPass,
int minX,
int minY,
int periodX,
int periodY,
int[] bands)
```

Reports that the current read operation is about to begin a
progressive pass. Readers of formats that support progressive
encoding should use this to notify clients when each pass is
completed when reading a progressively encoded image.

An estimate of the area that will be updated by the pass is
indicated by the

minX

,

minY

,

width

, and

height

parameters. If the
pass is interlaced, that is, it only updates selected rows or
columns, the

periodX

and

periodY

parameters will indicate the degree of subsampling. The set of
bands that may be affected is indicated by the value of

bands

.

**Parameters:** source

- the

ImageReader

object calling this
method.
**Parameters:** theImage

- the

BufferedImage

being updated.
**Parameters:** pass

- the number of the pass that is about to begin,
starting with 0.
**Parameters:** minPass

- the index of the first pass that will be decoded.
**Parameters:** maxPass

- the index of the last pass that will be decoded.
**Parameters:** minX

- the X coordinate of the leftmost updated column
of pixels.
**Parameters:** minY

- the Y coordinate of the uppermost updated row
of pixels.
**Parameters:** periodX

- the horizontal spacing between updated pixels;
a value of 1 means no gaps.
**Parameters:** periodY

- the vertical spacing between updated pixels;
a value of 1 means no gaps.
**Parameters:** bands

- an array of

int

s indicating the
set bands that may be updated.

- imageUpdate

```java
void imageUpdate​(
ImageReader
source,

BufferedImage
theImage,
int minX,
int minY,
int width,
int height,
int periodX,
int periodY,
int[] bands)
```

Reports that a given region of the image has been updated.
The application might choose to redisplay the specified area,
for example, in order to provide a progressive display effect,
or perform other incremental processing.

Note that different image format readers may produce
decoded pixels in a variety of different orders. Many readers
will produce pixels in a simple top-to-bottom,
left-to-right-order, but others may use multiple passes of
interlacing, tiling, etc. The sequence of updates may even
differ from call to call depending on network speeds, for
example. A call to this method does not guarantee that all the
specified pixels have actually been updated, only that some
activity has taken place within some subregion of the one
specified.

The particular

ImageReader

implementation may
choose how often to provide updates. Each update specifies
that a given region of the image has been updated since the
last update. A region is described by its spatial bounding box
(

minX

,

minY

,

width

, and

height

); X and Y subsampling factors
(

periodX

and

periodY

); and a set of
updated bands (

bands

). For example, the update:

```java
minX = 10
minY = 20
width = 3
height = 4
periodX = 2
periodY = 3
bands = { 1, 3 }
```

would indicate that bands 1 and 3 of the following pixels were
updated:

```java
(10, 20) (12, 20) (14, 20)
(10, 23) (12, 23) (14, 23)
(10, 26) (12, 26) (14, 26)
(10, 29) (12, 29) (14, 29)
```

**Parameters:** source

- the

ImageReader

object calling this method.
**Parameters:** theImage

- the

BufferedImage

being updated.
**Parameters:** minX

- the X coordinate of the leftmost updated column
of pixels.
**Parameters:** minY

- the Y coordinate of the uppermost updated row
of pixels.
**Parameters:** width

- the number of updated pixels horizontally.
**Parameters:** height

- the number of updated pixels vertically.
**Parameters:** periodX

- the horizontal spacing between updated pixels;
a value of 1 means no gaps.
**Parameters:** periodY

- the vertical spacing between updated pixels;
a value of 1 means no gaps.
**Parameters:** bands

- an array of

int

s indicating which
bands are being updated.

- passComplete

```java
void passComplete​(
ImageReader
source,

BufferedImage
theImage)
```

Reports that the current read operation has completed a
progressive pass. Readers of formats that support
progressive encoding should use this to notify clients when
each pass is completed when reading a progressively
encoded image.

**Parameters:** source

- the

ImageReader

object calling this
method.
**Parameters:** theImage

- the

BufferedImage

being updated.
**See Also:** ImageReadParam.setSourceProgressivePasses(int, int)

- thumbnailPassStarted

```java
void thumbnailPassStarted​(
ImageReader
source,

BufferedImage
theThumbnail,
int pass,
int minPass,
int maxPass,
int minX,
int minY,
int periodX,
int periodY,
int[] bands)
```

Reports that the current thumbnail read operation is about to
begin a progressive pass. Readers of formats that support
progressive encoding should use this to notify clients when
each pass is completed when reading a progressively encoded
thumbnail image.

**Parameters:** source

- the

ImageReader

object calling this
method.
**Parameters:** theThumbnail

- the

BufferedImage

thumbnail
being updated.
**Parameters:** pass

- the number of the pass that is about to begin,
starting with 0.
**Parameters:** minPass

- the index of the first pass that will be decoded.
**Parameters:** maxPass

- the index of the last pass that will be decoded.
**Parameters:** minX

- the X coordinate of the leftmost updated column
of pixels.
**Parameters:** minY

- the Y coordinate of the uppermost updated row
of pixels.
**Parameters:** periodX

- the horizontal spacing between updated pixels;
a value of 1 means no gaps.
**Parameters:** periodY

- the vertical spacing between updated pixels;
a value of 1 means no gaps.
**Parameters:** bands

- an array of

int

s indicating the
set bands that may be updated.
**See Also:** passStarted(javax.imageio.ImageReader, java.awt.image.BufferedImage, int, int, int, int, int, int, int, int[])

- thumbnailUpdate

```java
void thumbnailUpdate​(
ImageReader
source,

BufferedImage
theThumbnail,
int minX,
int minY,
int width,
int height,
int periodX,
int periodY,
int[] bands)
```

Reports that a given region of a thumbnail image has been updated.
The application might choose to redisplay the specified area,
for example, in order to provide a progressive display effect,
or perform other incremental processing.

**Parameters:** source

- the

ImageReader

object calling this method.
**Parameters:** theThumbnail

- the

BufferedImage

thumbnail
being updated.
**Parameters:** minX

- the X coordinate of the leftmost updated column
of pixels.
**Parameters:** minY

- the Y coordinate of the uppermost updated row
of pixels.
**Parameters:** width

- the number of updated pixels horizontally.
**Parameters:** height

- the number of updated pixels vertically.
**Parameters:** periodX

- the horizontal spacing between updated pixels;
a value of 1 means no gaps.
**Parameters:** periodY

- the vertical spacing between updated pixels;
a value of 1 means no gaps.
**Parameters:** bands

- an array of

int

s indicating which
bands are being updated.
**See Also:** imageUpdate(javax.imageio.ImageReader, java.awt.image.BufferedImage, int, int, int, int, int, int, int[])

- thumbnailPassComplete

```java
void thumbnailPassComplete​(
ImageReader
source,

BufferedImage
theThumbnail)
```

Reports that the current thumbnail read operation has completed
a progressive pass. Readers of formats that support
progressive encoding should use this to notify clients when
each pass is completed when reading a progressively encoded
thumbnail image.

**Parameters:** source

- the

ImageReader

object calling this
method.
**Parameters:** theThumbnail

- the

BufferedImage

thumbnail
being updated.
**See Also:** passComplete(javax.imageio.ImageReader, java.awt.image.BufferedImage)

Method Detail

- passStarted

```java
void passStarted​(
ImageReader
source,

BufferedImage
theImage,
int pass,
int minPass,
int maxPass,
int minX,
int minY,
int periodX,
int periodY,
int[] bands)
```

Reports that the current read operation is about to begin a
progressive pass. Readers of formats that support progressive
encoding should use this to notify clients when each pass is
completed when reading a progressively encoded image.

An estimate of the area that will be updated by the pass is
indicated by the

minX

,

minY

,

width

, and

height

parameters. If the
pass is interlaced, that is, it only updates selected rows or
columns, the

periodX

and

periodY

parameters will indicate the degree of subsampling. The set of
bands that may be affected is indicated by the value of

bands

.

**Parameters:** source

- the

ImageReader

object calling this
method.
**Parameters:** theImage

- the

BufferedImage

being updated.
**Parameters:** pass

- the number of the pass that is about to begin,
starting with 0.
**Parameters:** minPass

- the index of the first pass that will be decoded.
**Parameters:** maxPass

- the index of the last pass that will be decoded.
**Parameters:** minX

- the X coordinate of the leftmost updated column
of pixels.
**Parameters:** minY

- the Y coordinate of the uppermost updated row
of pixels.
**Parameters:** periodX

- the horizontal spacing between updated pixels;
a value of 1 means no gaps.
**Parameters:** periodY

- the vertical spacing between updated pixels;
a value of 1 means no gaps.
**Parameters:** bands

- an array of

int

s indicating the
set bands that may be updated.

- imageUpdate

```java
void imageUpdate​(
ImageReader
source,

BufferedImage
theImage,
int minX,
int minY,
int width,
int height,
int periodX,
int periodY,
int[] bands)
```

Reports that a given region of the image has been updated.
The application might choose to redisplay the specified area,
for example, in order to provide a progressive display effect,
or perform other incremental processing.

Note that different image format readers may produce
decoded pixels in a variety of different orders. Many readers
will produce pixels in a simple top-to-bottom,
left-to-right-order, but others may use multiple passes of
interlacing, tiling, etc. The sequence of updates may even
differ from call to call depending on network speeds, for
example. A call to this method does not guarantee that all the
specified pixels have actually been updated, only that some
activity has taken place within some subregion of the one
specified.

The particular

ImageReader

implementation may
choose how often to provide updates. Each update specifies
that a given region of the image has been updated since the
last update. A region is described by its spatial bounding box
(

minX

,

minY

,

width

, and

height

); X and Y subsampling factors
(

periodX

and

periodY

); and a set of
updated bands (

bands

). For example, the update:

```java
minX = 10
minY = 20
width = 3
height = 4
periodX = 2
periodY = 3
bands = { 1, 3 }
```

would indicate that bands 1 and 3 of the following pixels were
updated:

```java
(10, 20) (12, 20) (14, 20)
(10, 23) (12, 23) (14, 23)
(10, 26) (12, 26) (14, 26)
(10, 29) (12, 29) (14, 29)
```

**Parameters:** source

- the

ImageReader

object calling this method.
**Parameters:** theImage

- the

BufferedImage

being updated.
**Parameters:** minX

- the X coordinate of the leftmost updated column
of pixels.
**Parameters:** minY

- the Y coordinate of the uppermost updated row
of pixels.
**Parameters:** width

- the number of updated pixels horizontally.
**Parameters:** height

- the number of updated pixels vertically.
**Parameters:** periodX

- the horizontal spacing between updated pixels;
a value of 1 means no gaps.
**Parameters:** periodY

- the vertical spacing between updated pixels;
a value of 1 means no gaps.
**Parameters:** bands

- an array of

int

s indicating which
bands are being updated.

- passComplete

```java
void passComplete​(
ImageReader
source,

BufferedImage
theImage)
```

Reports that the current read operation has completed a
progressive pass. Readers of formats that support
progressive encoding should use this to notify clients when
each pass is completed when reading a progressively
encoded image.

**Parameters:** source

- the

ImageReader

object calling this
method.
**Parameters:** theImage

- the

BufferedImage

being updated.
**See Also:** ImageReadParam.setSourceProgressivePasses(int, int)

- thumbnailPassStarted

```java
void thumbnailPassStarted​(
ImageReader
source,

BufferedImage
theThumbnail,
int pass,
int minPass,
int maxPass,
int minX,
int minY,
int periodX,
int periodY,
int[] bands)
```

Reports that the current thumbnail read operation is about to
begin a progressive pass. Readers of formats that support
progressive encoding should use this to notify clients when
each pass is completed when reading a progressively encoded
thumbnail image.

**Parameters:** source

- the

ImageReader

object calling this
method.
**Parameters:** theThumbnail

- the

BufferedImage

thumbnail
being updated.
**Parameters:** pass

- the number of the pass that is about to begin,
starting with 0.
**Parameters:** minPass

- the index of the first pass that will be decoded.
**Parameters:** maxPass

- the index of the last pass that will be decoded.
**Parameters:** minX

- the X coordinate of the leftmost updated column
of pixels.
**Parameters:** minY

- the Y coordinate of the uppermost updated row
of pixels.
**Parameters:** periodX

- the horizontal spacing between updated pixels;
a value of 1 means no gaps.
**Parameters:** periodY

- the vertical spacing between updated pixels;
a value of 1 means no gaps.
**Parameters:** bands

- an array of

int

s indicating the
set bands that may be updated.
**See Also:** passStarted(javax.imageio.ImageReader, java.awt.image.BufferedImage, int, int, int, int, int, int, int, int[])

- thumbnailUpdate

```java
void thumbnailUpdate​(
ImageReader
source,

BufferedImage
theThumbnail,
int minX,
int minY,
int width,
int height,
int periodX,
int periodY,
int[] bands)
```

Reports that a given region of a thumbnail image has been updated.
The application might choose to redisplay the specified area,
for example, in order to provide a progressive display effect,
or perform other incremental processing.

**Parameters:** source

- the

ImageReader

object calling this method.
**Parameters:** theThumbnail

- the

BufferedImage

thumbnail
being updated.
**Parameters:** minX

- the X coordinate of the leftmost updated column
of pixels.
**Parameters:** minY

- the Y coordinate of the uppermost updated row
of pixels.
**Parameters:** width

- the number of updated pixels horizontally.
**Parameters:** height

- the number of updated pixels vertically.
**Parameters:** periodX

- the horizontal spacing between updated pixels;
a value of 1 means no gaps.
**Parameters:** periodY

- the vertical spacing between updated pixels;
a value of 1 means no gaps.
**Parameters:** bands

- an array of

int

s indicating which
bands are being updated.
**See Also:** imageUpdate(javax.imageio.ImageReader, java.awt.image.BufferedImage, int, int, int, int, int, int, int[])

- thumbnailPassComplete

```java
void thumbnailPassComplete​(
ImageReader
source,

BufferedImage
theThumbnail)
```

Reports that the current thumbnail read operation has completed
a progressive pass. Readers of formats that support
progressive encoding should use this to notify clients when
each pass is completed when reading a progressively encoded
thumbnail image.

**Parameters:** source

- the

ImageReader

object calling this
method.
**Parameters:** theThumbnail

- the

BufferedImage

thumbnail
being updated.
**See Also:** passComplete(javax.imageio.ImageReader, java.awt.image.BufferedImage)

---

#### Method Detail

passStarted

```java
void passStarted​(
ImageReader
source,

BufferedImage
theImage,
int pass,
int minPass,
int maxPass,
int minX,
int minY,
int periodX,
int periodY,
int[] bands)
```

Reports that the current read operation is about to begin a
progressive pass. Readers of formats that support progressive
encoding should use this to notify clients when each pass is
completed when reading a progressively encoded image.

An estimate of the area that will be updated by the pass is
indicated by the

minX

,

minY

,

width

, and

height

parameters. If the
pass is interlaced, that is, it only updates selected rows or
columns, the

periodX

and

periodY

parameters will indicate the degree of subsampling. The set of
bands that may be affected is indicated by the value of

bands

.

**Parameters:** source

- the

ImageReader

object calling this
method.
**Parameters:** theImage

- the

BufferedImage

being updated.
**Parameters:** pass

- the number of the pass that is about to begin,
starting with 0.
**Parameters:** minPass

- the index of the first pass that will be decoded.
**Parameters:** maxPass

- the index of the last pass that will be decoded.
**Parameters:** minX

- the X coordinate of the leftmost updated column
of pixels.
**Parameters:** minY

- the Y coordinate of the uppermost updated row
of pixels.
**Parameters:** periodX

- the horizontal spacing between updated pixels;
a value of 1 means no gaps.
**Parameters:** periodY

- the vertical spacing between updated pixels;
a value of 1 means no gaps.
**Parameters:** bands

- an array of

int

s indicating the
set bands that may be updated.

---

#### passStarted

void passStarted​(

ImageReader

source,

BufferedImage

theImage,
int pass,
int minPass,
int maxPass,
int minX,
int minY,
int periodX,
int periodY,
int[] bands)

Reports that the current read operation is about to begin a
progressive pass. Readers of formats that support progressive
encoding should use this to notify clients when each pass is
completed when reading a progressively encoded image.

An estimate of the area that will be updated by the pass is
indicated by the

minX

,

minY

,

width

, and

height

parameters. If the
pass is interlaced, that is, it only updates selected rows or
columns, the

periodX

and

periodY

parameters will indicate the degree of subsampling. The set of
bands that may be affected is indicated by the value of

bands

.

An estimate of the area that will be updated by the pass is
indicated by the

minX

,

minY

,

width

, and

height

parameters. If the
pass is interlaced, that is, it only updates selected rows or
columns, the

periodX

and

periodY

parameters will indicate the degree of subsampling. The set of
bands that may be affected is indicated by the value of

bands

.

imageUpdate

```java
void imageUpdate​(
ImageReader
source,

BufferedImage
theImage,
int minX,
int minY,
int width,
int height,
int periodX,
int periodY,
int[] bands)
```

Reports that a given region of the image has been updated.
The application might choose to redisplay the specified area,
for example, in order to provide a progressive display effect,
or perform other incremental processing.

Note that different image format readers may produce
decoded pixels in a variety of different orders. Many readers
will produce pixels in a simple top-to-bottom,
left-to-right-order, but others may use multiple passes of
interlacing, tiling, etc. The sequence of updates may even
differ from call to call depending on network speeds, for
example. A call to this method does not guarantee that all the
specified pixels have actually been updated, only that some
activity has taken place within some subregion of the one
specified.

The particular

ImageReader

implementation may
choose how often to provide updates. Each update specifies
that a given region of the image has been updated since the
last update. A region is described by its spatial bounding box
(

minX

,

minY

,

width

, and

height

); X and Y subsampling factors
(

periodX

and

periodY

); and a set of
updated bands (

bands

). For example, the update:

```java
minX = 10
minY = 20
width = 3
height = 4
periodX = 2
periodY = 3
bands = { 1, 3 }
```

would indicate that bands 1 and 3 of the following pixels were
updated:

```java
(10, 20) (12, 20) (14, 20)
(10, 23) (12, 23) (14, 23)
(10, 26) (12, 26) (14, 26)
(10, 29) (12, 29) (14, 29)
```

**Parameters:** source

- the

ImageReader

object calling this method.
**Parameters:** theImage

- the

BufferedImage

being updated.
**Parameters:** minX

- the X coordinate of the leftmost updated column
of pixels.
**Parameters:** minY

- the Y coordinate of the uppermost updated row
of pixels.
**Parameters:** width

- the number of updated pixels horizontally.
**Parameters:** height

- the number of updated pixels vertically.
**Parameters:** periodX

- the horizontal spacing between updated pixels;
a value of 1 means no gaps.
**Parameters:** periodY

- the vertical spacing between updated pixels;
a value of 1 means no gaps.
**Parameters:** bands

- an array of

int

s indicating which
bands are being updated.

---

#### imageUpdate

void imageUpdate​(

ImageReader

source,

BufferedImage

theImage,
int minX,
int minY,
int width,
int height,
int periodX,
int periodY,
int[] bands)

Reports that a given region of the image has been updated.
The application might choose to redisplay the specified area,
for example, in order to provide a progressive display effect,
or perform other incremental processing.

Note that different image format readers may produce
decoded pixels in a variety of different orders. Many readers
will produce pixels in a simple top-to-bottom,
left-to-right-order, but others may use multiple passes of
interlacing, tiling, etc. The sequence of updates may even
differ from call to call depending on network speeds, for
example. A call to this method does not guarantee that all the
specified pixels have actually been updated, only that some
activity has taken place within some subregion of the one
specified.

The particular

ImageReader

implementation may
choose how often to provide updates. Each update specifies
that a given region of the image has been updated since the
last update. A region is described by its spatial bounding box
(

minX

,

minY

,

width

, and

height

); X and Y subsampling factors
(

periodX

and

periodY

); and a set of
updated bands (

bands

). For example, the update:

```java
minX = 10
minY = 20
width = 3
height = 4
periodX = 2
periodY = 3
bands = { 1, 3 }
```

would indicate that bands 1 and 3 of the following pixels were
updated:

```java
(10, 20) (12, 20) (14, 20)
(10, 23) (12, 23) (14, 23)
(10, 26) (12, 26) (14, 26)
(10, 29) (12, 29) (14, 29)
```

Note that different image format readers may produce
decoded pixels in a variety of different orders. Many readers
will produce pixels in a simple top-to-bottom,
left-to-right-order, but others may use multiple passes of
interlacing, tiling, etc. The sequence of updates may even
differ from call to call depending on network speeds, for
example. A call to this method does not guarantee that all the
specified pixels have actually been updated, only that some
activity has taken place within some subregion of the one
specified.

The particular

ImageReader

implementation may
choose how often to provide updates. Each update specifies
that a given region of the image has been updated since the
last update. A region is described by its spatial bounding box
(

minX

,

minY

,

width

, and

height

); X and Y subsampling factors
(

periodX

and

periodY

); and a set of
updated bands (

bands

). For example, the update:

```java
minX = 10
minY = 20
width = 3
height = 4
periodX = 2
periodY = 3
bands = { 1, 3 }
```

would indicate that bands 1 and 3 of the following pixels were
updated:

```java
(10, 20) (12, 20) (14, 20)
(10, 23) (12, 23) (14, 23)
(10, 26) (12, 26) (14, 26)
(10, 29) (12, 29) (14, 29)
```

The particular

ImageReader

implementation may
choose how often to provide updates. Each update specifies
that a given region of the image has been updated since the
last update. A region is described by its spatial bounding box
(

minX

,

minY

,

width

, and

height

); X and Y subsampling factors
(

periodX

and

periodY

); and a set of
updated bands (

bands

). For example, the update:

```java
minX = 10
minY = 20
width = 3
height = 4
periodX = 2
periodY = 3
bands = { 1, 3 }
```

would indicate that bands 1 and 3 of the following pixels were
updated:

```java
(10, 20) (12, 20) (14, 20)
(10, 23) (12, 23) (14, 23)
(10, 26) (12, 26) (14, 26)
(10, 29) (12, 29) (14, 29)
```

minX = 10
minY = 20
width = 3
height = 4
periodX = 2
periodY = 3
bands = { 1, 3 }

(10, 20) (12, 20) (14, 20)
(10, 23) (12, 23) (14, 23)
(10, 26) (12, 26) (14, 26)
(10, 29) (12, 29) (14, 29)

passComplete

```java
void passComplete​(
ImageReader
source,

BufferedImage
theImage)
```

Reports that the current read operation has completed a
progressive pass. Readers of formats that support
progressive encoding should use this to notify clients when
each pass is completed when reading a progressively
encoded image.

**Parameters:** source

- the

ImageReader

object calling this
method.
**Parameters:** theImage

- the

BufferedImage

being updated.
**See Also:** ImageReadParam.setSourceProgressivePasses(int, int)

---

#### passComplete

void passComplete​(

ImageReader

source,

BufferedImage

theImage)

Reports that the current read operation has completed a
progressive pass. Readers of formats that support
progressive encoding should use this to notify clients when
each pass is completed when reading a progressively
encoded image.

thumbnailPassStarted

```java
void thumbnailPassStarted​(
ImageReader
source,

BufferedImage
theThumbnail,
int pass,
int minPass,
int maxPass,
int minX,
int minY,
int periodX,
int periodY,
int[] bands)
```

Reports that the current thumbnail read operation is about to
begin a progressive pass. Readers of formats that support
progressive encoding should use this to notify clients when
each pass is completed when reading a progressively encoded
thumbnail image.

**Parameters:** source

- the

ImageReader

object calling this
method.
**Parameters:** theThumbnail

- the

BufferedImage

thumbnail
being updated.
**Parameters:** pass

- the number of the pass that is about to begin,
starting with 0.
**Parameters:** minPass

- the index of the first pass that will be decoded.
**Parameters:** maxPass

- the index of the last pass that will be decoded.
**Parameters:** minX

- the X coordinate of the leftmost updated column
of pixels.
**Parameters:** minY

- the Y coordinate of the uppermost updated row
of pixels.
**Parameters:** periodX

- the horizontal spacing between updated pixels;
a value of 1 means no gaps.
**Parameters:** periodY

- the vertical spacing between updated pixels;
a value of 1 means no gaps.
**Parameters:** bands

- an array of

int

s indicating the
set bands that may be updated.
**See Also:** passStarted(javax.imageio.ImageReader, java.awt.image.BufferedImage, int, int, int, int, int, int, int, int[])

---

#### thumbnailPassStarted

void thumbnailPassStarted​(

ImageReader

source,

BufferedImage

theThumbnail,
int pass,
int minPass,
int maxPass,
int minX,
int minY,
int periodX,
int periodY,
int[] bands)

Reports that the current thumbnail read operation is about to
begin a progressive pass. Readers of formats that support
progressive encoding should use this to notify clients when
each pass is completed when reading a progressively encoded
thumbnail image.

thumbnailUpdate

```java
void thumbnailUpdate​(
ImageReader
source,

BufferedImage
theThumbnail,
int minX,
int minY,
int width,
int height,
int periodX,
int periodY,
int[] bands)
```

Reports that a given region of a thumbnail image has been updated.
The application might choose to redisplay the specified area,
for example, in order to provide a progressive display effect,
or perform other incremental processing.

**Parameters:** source

- the

ImageReader

object calling this method.
**Parameters:** theThumbnail

- the

BufferedImage

thumbnail
being updated.
**Parameters:** minX

- the X coordinate of the leftmost updated column
of pixels.
**Parameters:** minY

- the Y coordinate of the uppermost updated row
of pixels.
**Parameters:** width

- the number of updated pixels horizontally.
**Parameters:** height

- the number of updated pixels vertically.
**Parameters:** periodX

- the horizontal spacing between updated pixels;
a value of 1 means no gaps.
**Parameters:** periodY

- the vertical spacing between updated pixels;
a value of 1 means no gaps.
**Parameters:** bands

- an array of

int

s indicating which
bands are being updated.
**See Also:** imageUpdate(javax.imageio.ImageReader, java.awt.image.BufferedImage, int, int, int, int, int, int, int[])

---

#### thumbnailUpdate

void thumbnailUpdate​(

ImageReader

source,

BufferedImage

theThumbnail,
int minX,
int minY,
int width,
int height,
int periodX,
int periodY,
int[] bands)

Reports that a given region of a thumbnail image has been updated.
The application might choose to redisplay the specified area,
for example, in order to provide a progressive display effect,
or perform other incremental processing.

thumbnailPassComplete

```java
void thumbnailPassComplete​(
ImageReader
source,

BufferedImage
theThumbnail)
```

Reports that the current thumbnail read operation has completed
a progressive pass. Readers of formats that support
progressive encoding should use this to notify clients when
each pass is completed when reading a progressively encoded
thumbnail image.

**Parameters:** source

- the

ImageReader

object calling this
method.
**Parameters:** theThumbnail

- the

BufferedImage

thumbnail
being updated.
**See Also:** passComplete(javax.imageio.ImageReader, java.awt.image.BufferedImage)

---

#### thumbnailPassComplete

void thumbnailPassComplete​(

ImageReader

source,

BufferedImage

theThumbnail)

Reports that the current thumbnail read operation has completed
a progressive pass. Readers of formats that support
progressive encoding should use this to notify clients when
each pass is completed when reading a progressively encoded
thumbnail image.

---

