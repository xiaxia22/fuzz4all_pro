# Class ImageReadParam

**Source:** `java.desktop\javax\imageio\ImageReadParam.html`

### Class Description

```java
public class
ImageReadParam

extends
IIOParam
```

A class describing how a stream is to be decoded. Instances of
this class or its subclasses are used to supply prescriptive
"how-to" information to instances of

ImageReader

.

An image encoded as part of a file or stream may be thought of
extending out in multiple dimensions: the spatial dimensions of
width and height, a number of bands, and a number of progressive
decoding passes. This class allows a contiguous (hyper)rectangular
subarea of the image in all of these dimensions to be selected for
decoding. Additionally, the spatial dimensions may be subsampled
discontinuously. Finally, color and format conversions may be
specified by controlling the

ColorModel

and

SampleModel

of the destination image, either by
providing a

BufferedImage

or by using an

ImageTypeSpecifier

.

An

ImageReadParam

object is used to specify how an
image, or a set of images, will be converted on input from
a stream in the context of the Java Image I/O framework. A plug-in for a
specific image format will return instances of

ImageReadParam

from the

getDefaultReadParam

method of its

ImageReader

implementation.

The state maintained by an instance of

ImageReadParam

is independent of any particular image
being decoded. When actual decoding takes place, the values set in
the read param are combined with the actual properties of the image
being decoded from the stream and the destination

BufferedImage

that will receive the decoded pixel
data. For example, the source region set using

setSourceRegion

will first be intersected with the
actual valid source area. The result will be translated by the
value returned by

getDestinationOffset

, and the
resulting rectangle intersected with the actual valid destination
area to yield the destination area that will be written.

The parameters specified by an

ImageReadParam

are
applied to an image as follows. First, if a rendering size has
been set by

setSourceRenderSize

, the entire decoded
image is rendered at the size given by

getSourceRenderSize

. Otherwise, the image has its
natural size given by

ImageReader.getWidth

and

ImageReader.getHeight

.

Next, the image is clipped against the source region
specified by

getSourceXOffset

,

getSourceYOffset

,

getSourceWidth

, and

getSourceHeight

.

The resulting region is then subsampled according to the
factors given in

IIOParam.setSourceSubsampling

. The first pixel,
the number of pixels per row, and the number of rows all depend
on the subsampling settings.
Call the minimum X and Y coordinates of the resulting rectangle
(

minX

,

minY

), its width

w

and its height

h

.

This rectangle is offset by
(

getDestinationOffset().x

,

getDestinationOffset().y

) and clipped against the
destination bounds. If no destination image has been set, the
destination is defined to have a width of

getDestinationOffset().x

+

w

, and a
height of

getDestinationOffset().y

+

h

so
that all pixels of the source region may be written to the
destination.

Pixels that land, after subsampling, within the destination
image, and that are written in one of the progressive passes
specified by

getSourceMinProgressivePass

and

getSourceNumProgressivePasses

are passed along to the
next step.

Finally, the source samples of each pixel are mapped into
destination bands according to the algorithm described in the
comment for

setDestinationBands

.

Plug-in writers may extend the functionality of

ImageReadParam

by providing a subclass that implements
additional, plug-in specific interfaces. It is up to the plug-in
to document what interfaces are available and how they are to be
used. Readers will silently ignore any extended features of an

ImageReadParam

subclass of which they are not aware.
Also, they may ignore any optional features that they normally
disable when creating their own

ImageReadParam

instances via

getDefaultReadParam

.

Note that unless a query method exists for a capability, it must
be supported by all

ImageReader

implementations
(

e.g.

source render size is optional, but subsampling must be
supported).

**Direct Known Subclasses:** JPEGImageReadParam

,

TIFFImageReadParam

---

### Field Details

#### protected boolean canSetSourceRenderSize

true

if this

ImageReadParam

allows
the source rendering dimensions to be set. By default, the
value is

false

. Subclasses must set this value
manually.

ImageReader

s that do not support setting of
the source render size should set this value to

false

.

---

#### protected
Dimension
sourceRenderSize

The desired rendering width and height of the source, if

canSetSourceRenderSize

is

true

, or

null

.

ImageReader

s that do not support setting of
the source render size may ignore this value.

---

#### protected
BufferedImage
destination

The current destination

BufferedImage

, or

null

if none has been set. By default, the value
is

null

.

---

#### protected int[] destinationBands

The set of destination bands to be used, as an array of

int

s. By default, the value is

null

,
indicating all destination bands should be written in order.

---

#### protected int minProgressivePass

The minimum index of a progressive pass to read from the
source. By default, the value is set to 0, which indicates
that passes starting with the first available pass should be
decoded.

Subclasses should ensure that this value is
non-negative.

---

#### protected int numProgressivePasses

The maximum number of progressive passes to read from the
source. By default, the value is set to

Integer.MAX_VALUE

, which indicates that passes up
to and including the last available pass should be decoded.

Subclasses should ensure that this value is positive.
Additionally, if the value is not

Integer.MAX_VALUE

, then

minProgressivePass + numProgressivePasses - 1

should not exceed

Integer.MAX_VALUE

.

---

### Constructor Details

#### public ImageReadParam()

Constructs an

ImageReadParam

.

---

### Method Details

#### public void setDestination​(
BufferedImage
destination)

Supplies a

BufferedImage

to be used as the
destination for decoded pixel data. The currently set image
will be written to by the

read

,

readAll

, and

readRaster

methods, and
a reference to it will be returned by those methods.

Pixel data from the aforementioned methods will be written
starting at the offset specified by

getDestinationOffset

.

If

destination

is

null

, a
newly-created

BufferedImage

will be returned by
those methods.

At the time of reading, the image is checked to verify that
its

ColorModel

and

SampleModel

correspond to one of the

ImageTypeSpecifier

s
returned from the

ImageReader

's

getImageTypes

method. If it does not, the reader
will throw an

IIOException

.

**Parameters:**
- destination

- the BufferedImage to be written to, or

null

.

**See Also:**
- getDestination()

---

#### public
BufferedImage
getDestination()

Returns the

BufferedImage

currently set by the

setDestination

method, or

null

if none is set.

**Returns:**
- the BufferedImage to be written to.

**See Also:**
- setDestination(java.awt.image.BufferedImage)

---

#### public void setDestinationBands​(int[] destinationBands)

Sets the indices of the destination bands where data
will be placed. Duplicate indices are not allowed.

A

null

value indicates that all destination
bands will be used.

Choosing a destination band subset will not affect the
number of bands in the output image of a read if no destination
image is specified; the created destination image will still
have the same number of bands as if this method had never been
called. If a different number of bands in the destination
image is desired, an image must be supplied using the

ImageReadParam.setDestination

method.

At the time of reading or writing, an

IllegalArgumentException

will be thrown by the
reader or writer if a value larger than the largest destination
band index has been specified, or if the number of source bands
and destination bands to be used differ. The

ImageReader.checkReadParamBandSettings

method may
be used to automate this test.

**Parameters:**
- destinationBands

- an array of integer band indices to be
used.

**Throws:**
- IllegalArgumentException

- if

destinationBands

contains a negative or duplicate value.

**See Also:**
- getDestinationBands()

,

IIOParam.getSourceBands()

,

ImageReader.checkReadParamBandSettings(javax.imageio.ImageReadParam, int, int)

---

#### public int[] getDestinationBands()

Returns the set of band indices where data will be placed.
If no value has been set,

null

is returned to
indicate that all destination bands will be used.

**Returns:**
- the indices of the destination bands to be used,
or

null

.

**See Also:**
- setDestinationBands(int[])

---

#### public boolean canSetSourceRenderSize()

Returns

true

if this reader allows the source
image to be rendered at an arbitrary size as part of the
decoding process, by means of the

setSourceRenderSize

method. If this method
returns

false

, calls to

setSourceRenderSize

will throw an

UnsupportedOperationException

.

**Returns:**
- true

if setting source rendering size is
supported.

**See Also:**
- setSourceRenderSize(java.awt.Dimension)

---

#### public void setSourceRenderSize​(
Dimension
size)
throws
UnsupportedOperationException

If the image is able to be rendered at an arbitrary size, sets
the source width and height to the supplied values. Note that
the values returned from the

getWidth

and

getHeight

methods on

ImageReader

are
not affected by this method; they will continue to return the
default size for the image. Similarly, if the image is also
tiled the tile width and height are given in terms of the default
size.

Typically, the width and height should be chosen such that
the ratio of width to height closely approximates the aspect
ratio of the image, as returned from

ImageReader.getAspectRatio

.

If this plug-in does not allow the rendering size to be
set, an

UnsupportedOperationException

will be
thrown.

To remove the render size setting, pass in a value of

null

for

size

.

**Parameters:**
- size

- a

Dimension

indicating the desired
width and height.

**Throws:**
- IllegalArgumentException

- if either the width or the
height is negative or 0.
- UnsupportedOperationException

- if image resizing
is not supported by this plug-in.

**See Also:**
- getSourceRenderSize()

,

ImageReader.getWidth(int)

,

ImageReader.getHeight(int)

,

ImageReader.getAspectRatio(int)

---

#### public
Dimension
getSourceRenderSize()

Returns the width and height of the source image as it
will be rendered during decoding, if they have been set via the

setSourceRenderSize

method. A

null

value indicates that no setting has been made.

**Returns:**
- the rendered width and height of the source image
as a

Dimension

.

**See Also:**
- setSourceRenderSize(java.awt.Dimension)

---

#### public void setSourceProgressivePasses​(int minPass,
int numPasses)

Sets the range of progressive passes that will be decoded.
Passes outside of this range will be ignored.

A progressive pass is a re-encoding of the entire image,
generally at progressively higher effective resolutions, but
requiring greater transmission bandwidth. The most common use
of progressive encoding is found in the JPEG format, where
successive passes include more detailed representations of the
high-frequency image content.

The actual number of passes to be decoded is determined
during decoding, based on the number of actual passes available
in the stream. Thus if

minPass + numPasses - 1

is
larger than the index of the last available passes, decoding
will end with that pass.

A value of

numPasses

of

Integer.MAX_VALUE

indicates that all passes from

minPass

forward should be read. Otherwise, the
index of the last pass (

i.e.

,

minPass + numPasses - 1

)
must not exceed

Integer.MAX_VALUE

.

There is no

unsetSourceProgressivePasses

method; the same effect may be obtained by calling

setSourceProgressivePasses(0, Integer.MAX_VALUE)

.

**Parameters:**
- minPass

- the index of the first pass to be decoded.
- numPasses

- the maximum number of passes to be decoded.

**Throws:**
- IllegalArgumentException

- if

minPass

is
negative,

numPasses

is negative or 0, or

numPasses

is smaller than

Integer.MAX_VALUE

but

minPass + numPasses - 1

is greater than

INTEGER.MAX_VALUE

.

**See Also:**
- getSourceMinProgressivePass()

,

getSourceMaxProgressivePass()

---

#### public int getSourceMinProgressivePass()

Returns the index of the first progressive pass that will be
decoded. If no value has been set, 0 will be returned (which is
the correct value).

**Returns:**
- the index of the first pass that will be decoded.

**See Also:**
- setSourceProgressivePasses(int, int)

,

getSourceNumProgressivePasses()

---

#### public int getSourceMaxProgressivePass()

If

getSourceNumProgressivePasses

is equal to

Integer.MAX_VALUE

, returns

Integer.MAX_VALUE

. Otherwise, returns

getSourceMinProgressivePass() +
getSourceNumProgressivePasses() - 1

.

**Returns:**
- the index of the last pass to be read, or

Integer.MAX_VALUE

.

---

#### public int getSourceNumProgressivePasses()

Returns the number of the progressive passes that will be
decoded. If no value has been set,

Integer.MAX_VALUE

will be returned (which is the
correct value).

**Returns:**
- the number of the passes that will be decoded.

**See Also:**
- setSourceProgressivePasses(int, int)

,

getSourceMinProgressivePass()

---

### Additional Sections

#### Class ImageReadParam

java.lang.Object

- javax.imageio.IIOParam
- - javax.imageio.ImageReadParam

javax.imageio.IIOParam

- javax.imageio.ImageReadParam

javax.imageio.ImageReadParam

**Direct Known Subclasses:** JPEGImageReadParam

,

TIFFImageReadParam

```java
public class
ImageReadParam

extends
IIOParam
```

A class describing how a stream is to be decoded. Instances of
this class or its subclasses are used to supply prescriptive
"how-to" information to instances of

ImageReader

.

An image encoded as part of a file or stream may be thought of
extending out in multiple dimensions: the spatial dimensions of
width and height, a number of bands, and a number of progressive
decoding passes. This class allows a contiguous (hyper)rectangular
subarea of the image in all of these dimensions to be selected for
decoding. Additionally, the spatial dimensions may be subsampled
discontinuously. Finally, color and format conversions may be
specified by controlling the

ColorModel

and

SampleModel

of the destination image, either by
providing a

BufferedImage

or by using an

ImageTypeSpecifier

.

An

ImageReadParam

object is used to specify how an
image, or a set of images, will be converted on input from
a stream in the context of the Java Image I/O framework. A plug-in for a
specific image format will return instances of

ImageReadParam

from the

getDefaultReadParam

method of its

ImageReader

implementation.

The state maintained by an instance of

ImageReadParam

is independent of any particular image
being decoded. When actual decoding takes place, the values set in
the read param are combined with the actual properties of the image
being decoded from the stream and the destination

BufferedImage

that will receive the decoded pixel
data. For example, the source region set using

setSourceRegion

will first be intersected with the
actual valid source area. The result will be translated by the
value returned by

getDestinationOffset

, and the
resulting rectangle intersected with the actual valid destination
area to yield the destination area that will be written.

The parameters specified by an

ImageReadParam

are
applied to an image as follows. First, if a rendering size has
been set by

setSourceRenderSize

, the entire decoded
image is rendered at the size given by

getSourceRenderSize

. Otherwise, the image has its
natural size given by

ImageReader.getWidth

and

ImageReader.getHeight

.

Next, the image is clipped against the source region
specified by

getSourceXOffset

,

getSourceYOffset

,

getSourceWidth

, and

getSourceHeight

.

The resulting region is then subsampled according to the
factors given in

IIOParam.setSourceSubsampling

. The first pixel,
the number of pixels per row, and the number of rows all depend
on the subsampling settings.
Call the minimum X and Y coordinates of the resulting rectangle
(

minX

,

minY

), its width

w

and its height

h

.

This rectangle is offset by
(

getDestinationOffset().x

,

getDestinationOffset().y

) and clipped against the
destination bounds. If no destination image has been set, the
destination is defined to have a width of

getDestinationOffset().x

+

w

, and a
height of

getDestinationOffset().y

+

h

so
that all pixels of the source region may be written to the
destination.

Pixels that land, after subsampling, within the destination
image, and that are written in one of the progressive passes
specified by

getSourceMinProgressivePass

and

getSourceNumProgressivePasses

are passed along to the
next step.

Finally, the source samples of each pixel are mapped into
destination bands according to the algorithm described in the
comment for

setDestinationBands

.

Plug-in writers may extend the functionality of

ImageReadParam

by providing a subclass that implements
additional, plug-in specific interfaces. It is up to the plug-in
to document what interfaces are available and how they are to be
used. Readers will silently ignore any extended features of an

ImageReadParam

subclass of which they are not aware.
Also, they may ignore any optional features that they normally
disable when creating their own

ImageReadParam

instances via

getDefaultReadParam

.

Note that unless a query method exists for a capability, it must
be supported by all

ImageReader

implementations
(

e.g.

source render size is optional, but subsampling must be
supported).

**See Also:** ImageReader

,

ImageWriter

,

ImageWriteParam

public class

ImageReadParam

extends

IIOParam

A class describing how a stream is to be decoded. Instances of
this class or its subclasses are used to supply prescriptive
"how-to" information to instances of

ImageReader

.

An image encoded as part of a file or stream may be thought of
extending out in multiple dimensions: the spatial dimensions of
width and height, a number of bands, and a number of progressive
decoding passes. This class allows a contiguous (hyper)rectangular
subarea of the image in all of these dimensions to be selected for
decoding. Additionally, the spatial dimensions may be subsampled
discontinuously. Finally, color and format conversions may be
specified by controlling the

ColorModel

and

SampleModel

of the destination image, either by
providing a

BufferedImage

or by using an

ImageTypeSpecifier

.

An

ImageReadParam

object is used to specify how an
image, or a set of images, will be converted on input from
a stream in the context of the Java Image I/O framework. A plug-in for a
specific image format will return instances of

ImageReadParam

from the

getDefaultReadParam

method of its

ImageReader

implementation.

The state maintained by an instance of

ImageReadParam

is independent of any particular image
being decoded. When actual decoding takes place, the values set in
the read param are combined with the actual properties of the image
being decoded from the stream and the destination

BufferedImage

that will receive the decoded pixel
data. For example, the source region set using

setSourceRegion

will first be intersected with the
actual valid source area. The result will be translated by the
value returned by

getDestinationOffset

, and the
resulting rectangle intersected with the actual valid destination
area to yield the destination area that will be written.

The parameters specified by an

ImageReadParam

are
applied to an image as follows. First, if a rendering size has
been set by

setSourceRenderSize

, the entire decoded
image is rendered at the size given by

getSourceRenderSize

. Otherwise, the image has its
natural size given by

ImageReader.getWidth

and

ImageReader.getHeight

.

Next, the image is clipped against the source region
specified by

getSourceXOffset

,

getSourceYOffset

,

getSourceWidth

, and

getSourceHeight

.

The resulting region is then subsampled according to the
factors given in

IIOParam.setSourceSubsampling

. The first pixel,
the number of pixels per row, and the number of rows all depend
on the subsampling settings.
Call the minimum X and Y coordinates of the resulting rectangle
(

minX

,

minY

), its width

w

and its height

h

.

This rectangle is offset by
(

getDestinationOffset().x

,

getDestinationOffset().y

) and clipped against the
destination bounds. If no destination image has been set, the
destination is defined to have a width of

getDestinationOffset().x

+

w

, and a
height of

getDestinationOffset().y

+

h

so
that all pixels of the source region may be written to the
destination.

Pixels that land, after subsampling, within the destination
image, and that are written in one of the progressive passes
specified by

getSourceMinProgressivePass

and

getSourceNumProgressivePasses

are passed along to the
next step.

Finally, the source samples of each pixel are mapped into
destination bands according to the algorithm described in the
comment for

setDestinationBands

.

Plug-in writers may extend the functionality of

ImageReadParam

by providing a subclass that implements
additional, plug-in specific interfaces. It is up to the plug-in
to document what interfaces are available and how they are to be
used. Readers will silently ignore any extended features of an

ImageReadParam

subclass of which they are not aware.
Also, they may ignore any optional features that they normally
disable when creating their own

ImageReadParam

instances via

getDefaultReadParam

.

Note that unless a query method exists for a capability, it must
be supported by all

ImageReader

implementations
(

e.g.

source render size is optional, but subsampling must be
supported).

An image encoded as part of a file or stream may be thought of
extending out in multiple dimensions: the spatial dimensions of
width and height, a number of bands, and a number of progressive
decoding passes. This class allows a contiguous (hyper)rectangular
subarea of the image in all of these dimensions to be selected for
decoding. Additionally, the spatial dimensions may be subsampled
discontinuously. Finally, color and format conversions may be
specified by controlling the

ColorModel

and

SampleModel

of the destination image, either by
providing a

BufferedImage

or by using an

ImageTypeSpecifier

.

An

ImageReadParam

object is used to specify how an
image, or a set of images, will be converted on input from
a stream in the context of the Java Image I/O framework. A plug-in for a
specific image format will return instances of

ImageReadParam

from the

getDefaultReadParam

method of its

ImageReader

implementation.

The state maintained by an instance of

ImageReadParam

is independent of any particular image
being decoded. When actual decoding takes place, the values set in
the read param are combined with the actual properties of the image
being decoded from the stream and the destination

BufferedImage

that will receive the decoded pixel
data. For example, the source region set using

setSourceRegion

will first be intersected with the
actual valid source area. The result will be translated by the
value returned by

getDestinationOffset

, and the
resulting rectangle intersected with the actual valid destination
area to yield the destination area that will be written.

The parameters specified by an

ImageReadParam

are
applied to an image as follows. First, if a rendering size has
been set by

setSourceRenderSize

, the entire decoded
image is rendered at the size given by

getSourceRenderSize

. Otherwise, the image has its
natural size given by

ImageReader.getWidth

and

ImageReader.getHeight

.

Next, the image is clipped against the source region
specified by

getSourceXOffset

,

getSourceYOffset

,

getSourceWidth

, and

getSourceHeight

.

The resulting region is then subsampled according to the
factors given in

IIOParam.setSourceSubsampling

. The first pixel,
the number of pixels per row, and the number of rows all depend
on the subsampling settings.
Call the minimum X and Y coordinates of the resulting rectangle
(

minX

,

minY

), its width

w

and its height

h

.

This rectangle is offset by
(

getDestinationOffset().x

,

getDestinationOffset().y

) and clipped against the
destination bounds. If no destination image has been set, the
destination is defined to have a width of

getDestinationOffset().x

+

w

, and a
height of

getDestinationOffset().y

+

h

so
that all pixels of the source region may be written to the
destination.

Pixels that land, after subsampling, within the destination
image, and that are written in one of the progressive passes
specified by

getSourceMinProgressivePass

and

getSourceNumProgressivePasses

are passed along to the
next step.

Finally, the source samples of each pixel are mapped into
destination bands according to the algorithm described in the
comment for

setDestinationBands

.

Plug-in writers may extend the functionality of

ImageReadParam

by providing a subclass that implements
additional, plug-in specific interfaces. It is up to the plug-in
to document what interfaces are available and how they are to be
used. Readers will silently ignore any extended features of an

ImageReadParam

subclass of which they are not aware.
Also, they may ignore any optional features that they normally
disable when creating their own

ImageReadParam

instances via

getDefaultReadParam

.

Note that unless a query method exists for a capability, it must
be supported by all

ImageReader

implementations
(

e.g.

source render size is optional, but subsampling must be
supported).

An

ImageReadParam

object is used to specify how an
image, or a set of images, will be converted on input from
a stream in the context of the Java Image I/O framework. A plug-in for a
specific image format will return instances of

ImageReadParam

from the

getDefaultReadParam

method of its

ImageReader

implementation.

The state maintained by an instance of

ImageReadParam

is independent of any particular image
being decoded. When actual decoding takes place, the values set in
the read param are combined with the actual properties of the image
being decoded from the stream and the destination

BufferedImage

that will receive the decoded pixel
data. For example, the source region set using

setSourceRegion

will first be intersected with the
actual valid source area. The result will be translated by the
value returned by

getDestinationOffset

, and the
resulting rectangle intersected with the actual valid destination
area to yield the destination area that will be written.

The parameters specified by an

ImageReadParam

are
applied to an image as follows. First, if a rendering size has
been set by

setSourceRenderSize

, the entire decoded
image is rendered at the size given by

getSourceRenderSize

. Otherwise, the image has its
natural size given by

ImageReader.getWidth

and

ImageReader.getHeight

.

Next, the image is clipped against the source region
specified by

getSourceXOffset

,

getSourceYOffset

,

getSourceWidth

, and

getSourceHeight

.

The resulting region is then subsampled according to the
factors given in

IIOParam.setSourceSubsampling

. The first pixel,
the number of pixels per row, and the number of rows all depend
on the subsampling settings.
Call the minimum X and Y coordinates of the resulting rectangle
(

minX

,

minY

), its width

w

and its height

h

.

This rectangle is offset by
(

getDestinationOffset().x

,

getDestinationOffset().y

) and clipped against the
destination bounds. If no destination image has been set, the
destination is defined to have a width of

getDestinationOffset().x

+

w

, and a
height of

getDestinationOffset().y

+

h

so
that all pixels of the source region may be written to the
destination.

Pixels that land, after subsampling, within the destination
image, and that are written in one of the progressive passes
specified by

getSourceMinProgressivePass

and

getSourceNumProgressivePasses

are passed along to the
next step.

Finally, the source samples of each pixel are mapped into
destination bands according to the algorithm described in the
comment for

setDestinationBands

.

Plug-in writers may extend the functionality of

ImageReadParam

by providing a subclass that implements
additional, plug-in specific interfaces. It is up to the plug-in
to document what interfaces are available and how they are to be
used. Readers will silently ignore any extended features of an

ImageReadParam

subclass of which they are not aware.
Also, they may ignore any optional features that they normally
disable when creating their own

ImageReadParam

instances via

getDefaultReadParam

.

Note that unless a query method exists for a capability, it must
be supported by all

ImageReader

implementations
(

e.g.

source render size is optional, but subsampling must be
supported).

The state maintained by an instance of

ImageReadParam

is independent of any particular image
being decoded. When actual decoding takes place, the values set in
the read param are combined with the actual properties of the image
being decoded from the stream and the destination

BufferedImage

that will receive the decoded pixel
data. For example, the source region set using

setSourceRegion

will first be intersected with the
actual valid source area. The result will be translated by the
value returned by

getDestinationOffset

, and the
resulting rectangle intersected with the actual valid destination
area to yield the destination area that will be written.

The parameters specified by an

ImageReadParam

are
applied to an image as follows. First, if a rendering size has
been set by

setSourceRenderSize

, the entire decoded
image is rendered at the size given by

getSourceRenderSize

. Otherwise, the image has its
natural size given by

ImageReader.getWidth

and

ImageReader.getHeight

.

Next, the image is clipped against the source region
specified by

getSourceXOffset

,

getSourceYOffset

,

getSourceWidth

, and

getSourceHeight

.

The resulting region is then subsampled according to the
factors given in

IIOParam.setSourceSubsampling

. The first pixel,
the number of pixels per row, and the number of rows all depend
on the subsampling settings.
Call the minimum X and Y coordinates of the resulting rectangle
(

minX

,

minY

), its width

w

and its height

h

.

This rectangle is offset by
(

getDestinationOffset().x

,

getDestinationOffset().y

) and clipped against the
destination bounds. If no destination image has been set, the
destination is defined to have a width of

getDestinationOffset().x

+

w

, and a
height of

getDestinationOffset().y

+

h

so
that all pixels of the source region may be written to the
destination.

Pixels that land, after subsampling, within the destination
image, and that are written in one of the progressive passes
specified by

getSourceMinProgressivePass

and

getSourceNumProgressivePasses

are passed along to the
next step.

Finally, the source samples of each pixel are mapped into
destination bands according to the algorithm described in the
comment for

setDestinationBands

.

Plug-in writers may extend the functionality of

ImageReadParam

by providing a subclass that implements
additional, plug-in specific interfaces. It is up to the plug-in
to document what interfaces are available and how they are to be
used. Readers will silently ignore any extended features of an

ImageReadParam

subclass of which they are not aware.
Also, they may ignore any optional features that they normally
disable when creating their own

ImageReadParam

instances via

getDefaultReadParam

.

Note that unless a query method exists for a capability, it must
be supported by all

ImageReader

implementations
(

e.g.

source render size is optional, but subsampling must be
supported).

The parameters specified by an

ImageReadParam

are
applied to an image as follows. First, if a rendering size has
been set by

setSourceRenderSize

, the entire decoded
image is rendered at the size given by

getSourceRenderSize

. Otherwise, the image has its
natural size given by

ImageReader.getWidth

and

ImageReader.getHeight

.

Next, the image is clipped against the source region
specified by

getSourceXOffset

,

getSourceYOffset

,

getSourceWidth

, and

getSourceHeight

.

The resulting region is then subsampled according to the
factors given in

IIOParam.setSourceSubsampling

. The first pixel,
the number of pixels per row, and the number of rows all depend
on the subsampling settings.
Call the minimum X and Y coordinates of the resulting rectangle
(

minX

,

minY

), its width

w

and its height

h

.

This rectangle is offset by
(

getDestinationOffset().x

,

getDestinationOffset().y

) and clipped against the
destination bounds. If no destination image has been set, the
destination is defined to have a width of

getDestinationOffset().x

+

w

, and a
height of

getDestinationOffset().y

+

h

so
that all pixels of the source region may be written to the
destination.

Pixels that land, after subsampling, within the destination
image, and that are written in one of the progressive passes
specified by

getSourceMinProgressivePass

and

getSourceNumProgressivePasses

are passed along to the
next step.

Finally, the source samples of each pixel are mapped into
destination bands according to the algorithm described in the
comment for

setDestinationBands

.

Plug-in writers may extend the functionality of

ImageReadParam

by providing a subclass that implements
additional, plug-in specific interfaces. It is up to the plug-in
to document what interfaces are available and how they are to be
used. Readers will silently ignore any extended features of an

ImageReadParam

subclass of which they are not aware.
Also, they may ignore any optional features that they normally
disable when creating their own

ImageReadParam

instances via

getDefaultReadParam

.

Note that unless a query method exists for a capability, it must
be supported by all

ImageReader

implementations
(

e.g.

source render size is optional, but subsampling must be
supported).

Next, the image is clipped against the source region
specified by

getSourceXOffset

,

getSourceYOffset

,

getSourceWidth

, and

getSourceHeight

.

The resulting region is then subsampled according to the
factors given in

IIOParam.setSourceSubsampling

. The first pixel,
the number of pixels per row, and the number of rows all depend
on the subsampling settings.
Call the minimum X and Y coordinates of the resulting rectangle
(

minX

,

minY

), its width

w

and its height

h

.

This rectangle is offset by
(

getDestinationOffset().x

,

getDestinationOffset().y

) and clipped against the
destination bounds. If no destination image has been set, the
destination is defined to have a width of

getDestinationOffset().x

+

w

, and a
height of

getDestinationOffset().y

+

h

so
that all pixels of the source region may be written to the
destination.

Pixels that land, after subsampling, within the destination
image, and that are written in one of the progressive passes
specified by

getSourceMinProgressivePass

and

getSourceNumProgressivePasses

are passed along to the
next step.

Finally, the source samples of each pixel are mapped into
destination bands according to the algorithm described in the
comment for

setDestinationBands

.

Plug-in writers may extend the functionality of

ImageReadParam

by providing a subclass that implements
additional, plug-in specific interfaces. It is up to the plug-in
to document what interfaces are available and how they are to be
used. Readers will silently ignore any extended features of an

ImageReadParam

subclass of which they are not aware.
Also, they may ignore any optional features that they normally
disable when creating their own

ImageReadParam

instances via

getDefaultReadParam

.

Note that unless a query method exists for a capability, it must
be supported by all

ImageReader

implementations
(

e.g.

source render size is optional, but subsampling must be
supported).

The resulting region is then subsampled according to the
factors given in

IIOParam.setSourceSubsampling

. The first pixel,
the number of pixels per row, and the number of rows all depend
on the subsampling settings.
Call the minimum X and Y coordinates of the resulting rectangle
(

minX

,

minY

), its width

w

and its height

h

.

This rectangle is offset by
(

getDestinationOffset().x

,

getDestinationOffset().y

) and clipped against the
destination bounds. If no destination image has been set, the
destination is defined to have a width of

getDestinationOffset().x

+

w

, and a
height of

getDestinationOffset().y

+

h

so
that all pixels of the source region may be written to the
destination.

Pixels that land, after subsampling, within the destination
image, and that are written in one of the progressive passes
specified by

getSourceMinProgressivePass

and

getSourceNumProgressivePasses

are passed along to the
next step.

Finally, the source samples of each pixel are mapped into
destination bands according to the algorithm described in the
comment for

setDestinationBands

.

Plug-in writers may extend the functionality of

ImageReadParam

by providing a subclass that implements
additional, plug-in specific interfaces. It is up to the plug-in
to document what interfaces are available and how they are to be
used. Readers will silently ignore any extended features of an

ImageReadParam

subclass of which they are not aware.
Also, they may ignore any optional features that they normally
disable when creating their own

ImageReadParam

instances via

getDefaultReadParam

.

Note that unless a query method exists for a capability, it must
be supported by all

ImageReader

implementations
(

e.g.

source render size is optional, but subsampling must be
supported).

This rectangle is offset by
(

getDestinationOffset().x

,

getDestinationOffset().y

) and clipped against the
destination bounds. If no destination image has been set, the
destination is defined to have a width of

getDestinationOffset().x

+

w

, and a
height of

getDestinationOffset().y

+

h

so
that all pixels of the source region may be written to the
destination.

Pixels that land, after subsampling, within the destination
image, and that are written in one of the progressive passes
specified by

getSourceMinProgressivePass

and

getSourceNumProgressivePasses

are passed along to the
next step.

Finally, the source samples of each pixel are mapped into
destination bands according to the algorithm described in the
comment for

setDestinationBands

.

Plug-in writers may extend the functionality of

ImageReadParam

by providing a subclass that implements
additional, plug-in specific interfaces. It is up to the plug-in
to document what interfaces are available and how they are to be
used. Readers will silently ignore any extended features of an

ImageReadParam

subclass of which they are not aware.
Also, they may ignore any optional features that they normally
disable when creating their own

ImageReadParam

instances via

getDefaultReadParam

.

Note that unless a query method exists for a capability, it must
be supported by all

ImageReader

implementations
(

e.g.

source render size is optional, but subsampling must be
supported).

Pixels that land, after subsampling, within the destination
image, and that are written in one of the progressive passes
specified by

getSourceMinProgressivePass

and

getSourceNumProgressivePasses

are passed along to the
next step.

Finally, the source samples of each pixel are mapped into
destination bands according to the algorithm described in the
comment for

setDestinationBands

.

Plug-in writers may extend the functionality of

ImageReadParam

by providing a subclass that implements
additional, plug-in specific interfaces. It is up to the plug-in
to document what interfaces are available and how they are to be
used. Readers will silently ignore any extended features of an

ImageReadParam

subclass of which they are not aware.
Also, they may ignore any optional features that they normally
disable when creating their own

ImageReadParam

instances via

getDefaultReadParam

.

Note that unless a query method exists for a capability, it must
be supported by all

ImageReader

implementations
(

e.g.

source render size is optional, but subsampling must be
supported).

Finally, the source samples of each pixel are mapped into
destination bands according to the algorithm described in the
comment for

setDestinationBands

.

Plug-in writers may extend the functionality of

ImageReadParam

by providing a subclass that implements
additional, plug-in specific interfaces. It is up to the plug-in
to document what interfaces are available and how they are to be
used. Readers will silently ignore any extended features of an

ImageReadParam

subclass of which they are not aware.
Also, they may ignore any optional features that they normally
disable when creating their own

ImageReadParam

instances via

getDefaultReadParam

.

Note that unless a query method exists for a capability, it must
be supported by all

ImageReader

implementations
(

e.g.

source render size is optional, but subsampling must be
supported).

Plug-in writers may extend the functionality of

ImageReadParam

by providing a subclass that implements
additional, plug-in specific interfaces. It is up to the plug-in
to document what interfaces are available and how they are to be
used. Readers will silently ignore any extended features of an

ImageReadParam

subclass of which they are not aware.
Also, they may ignore any optional features that they normally
disable when creating their own

ImageReadParam

instances via

getDefaultReadParam

.

Note that unless a query method exists for a capability, it must
be supported by all

ImageReader

implementations
(

e.g.

source render size is optional, but subsampling must be
supported).

Note that unless a query method exists for a capability, it must
be supported by all

ImageReader

implementations
(

e.g.

source render size is optional, but subsampling must be
supported).

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected boolean

canSetSourceRenderSize

true

if this

ImageReadParam

allows
the source rendering dimensions to be set.

protected

BufferedImage

destination

The current destination

BufferedImage

, or

null

if none has been set.

protected int[]

destinationBands

The set of destination bands to be used, as an array of

int

s.

protected int

minProgressivePass

The minimum index of a progressive pass to read from the
source.

protected int

numProgressivePasses

The maximum number of progressive passes to read from the
source.

protected

Dimension

sourceRenderSize

The desired rendering width and height of the source, if

canSetSourceRenderSize

is

true

, or

null

.

- Fields declared in class javax.imageio.

IIOParam

controller

,

defaultController

,

destinationOffset

,

destinationType

,

sourceBands

,

sourceRegion

,

sourceXSubsampling

,

sourceYSubsampling

,

subsamplingXOffset

,

subsamplingYOffset

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ImageReadParam

()

Constructs an

ImageReadParam

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

canSetSourceRenderSize

()

Returns

true

if this reader allows the source
image to be rendered at an arbitrary size as part of the
decoding process, by means of the

setSourceRenderSize

method.

BufferedImage

getDestination

()

Returns the

BufferedImage

currently set by the

setDestination

method, or

null

if none is set.

int[]

getDestinationBands

()

Returns the set of band indices where data will be placed.

int

getSourceMaxProgressivePass

()

If

getSourceNumProgressivePasses

is equal to

Integer.MAX_VALUE

, returns

Integer.MAX_VALUE

.

int

getSourceMinProgressivePass

()

Returns the index of the first progressive pass that will be
decoded.

int

getSourceNumProgressivePasses

()

Returns the number of the progressive passes that will be
decoded.

Dimension

getSourceRenderSize

()

Returns the width and height of the source image as it
will be rendered during decoding, if they have been set via the

setSourceRenderSize

method.

void

setDestination

​(

BufferedImage

destination)

Supplies a

BufferedImage

to be used as the
destination for decoded pixel data.

void

setDestinationBands

​(int[] destinationBands)

Sets the indices of the destination bands where data
will be placed.

void

setSourceProgressivePasses

​(int minPass,
int numPasses)

Sets the range of progressive passes that will be decoded.

void

setSourceRenderSize

​(

Dimension

size)

If the image is able to be rendered at an arbitrary size, sets
the source width and height to the supplied values.

- Methods declared in class javax.imageio.

IIOParam

activateController

,

getController

,

getDefaultController

,

getDestinationOffset

,

getDestinationType

,

getSourceBands

,

getSourceRegion

,

getSourceXSubsampling

,

getSourceYSubsampling

,

getSubsamplingXOffset

,

getSubsamplingYOffset

,

hasController

,

setController

,

setDestinationOffset

,

setDestinationType

,

setSourceBands

,

setSourceRegion

,

setSourceSubsampling

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

protected boolean

canSetSourceRenderSize

true

if this

ImageReadParam

allows
the source rendering dimensions to be set.

protected

BufferedImage

destination

The current destination

BufferedImage

, or

null

if none has been set.

protected int[]

destinationBands

The set of destination bands to be used, as an array of

int

s.

protected int

minProgressivePass

The minimum index of a progressive pass to read from the
source.

protected int

numProgressivePasses

The maximum number of progressive passes to read from the
source.

protected

Dimension

sourceRenderSize

The desired rendering width and height of the source, if

canSetSourceRenderSize

is

true

, or

null

.

- Fields declared in class javax.imageio.

IIOParam

controller

,

defaultController

,

destinationOffset

,

destinationType

,

sourceBands

,

sourceRegion

,

sourceXSubsampling

,

sourceYSubsampling

,

subsamplingXOffset

,

subsamplingYOffset

---

#### Field Summary

true

if this

ImageReadParam

allows
the source rendering dimensions to be set.

The current destination

BufferedImage

, or

null

if none has been set.

The set of destination bands to be used, as an array of

int

s.

The minimum index of a progressive pass to read from the
source.

The maximum number of progressive passes to read from the
source.

The desired rendering width and height of the source, if

canSetSourceRenderSize

is

true

, or

null

.

Fields declared in class javax.imageio.

IIOParam

controller

,

defaultController

,

destinationOffset

,

destinationType

,

sourceBands

,

sourceRegion

,

sourceXSubsampling

,

sourceYSubsampling

,

subsamplingXOffset

,

subsamplingYOffset

---

#### Fields declared in class javax.imageio. IIOParam

Constructor Summary

Constructors

Constructor

Description

ImageReadParam

()

Constructs an

ImageReadParam

.

---

#### Constructor Summary

Constructs an

ImageReadParam

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

canSetSourceRenderSize

()

Returns

true

if this reader allows the source
image to be rendered at an arbitrary size as part of the
decoding process, by means of the

setSourceRenderSize

method.

BufferedImage

getDestination

()

Returns the

BufferedImage

currently set by the

setDestination

method, or

null

if none is set.

int[]

getDestinationBands

()

Returns the set of band indices where data will be placed.

int

getSourceMaxProgressivePass

()

If

getSourceNumProgressivePasses

is equal to

Integer.MAX_VALUE

, returns

Integer.MAX_VALUE

.

int

getSourceMinProgressivePass

()

Returns the index of the first progressive pass that will be
decoded.

int

getSourceNumProgressivePasses

()

Returns the number of the progressive passes that will be
decoded.

Dimension

getSourceRenderSize

()

Returns the width and height of the source image as it
will be rendered during decoding, if they have been set via the

setSourceRenderSize

method.

void

setDestination

​(

BufferedImage

destination)

Supplies a

BufferedImage

to be used as the
destination for decoded pixel data.

void

setDestinationBands

​(int[] destinationBands)

Sets the indices of the destination bands where data
will be placed.

void

setSourceProgressivePasses

​(int minPass,
int numPasses)

Sets the range of progressive passes that will be decoded.

void

setSourceRenderSize

​(

Dimension

size)

If the image is able to be rendered at an arbitrary size, sets
the source width and height to the supplied values.

- Methods declared in class javax.imageio.

IIOParam

activateController

,

getController

,

getDefaultController

,

getDestinationOffset

,

getDestinationType

,

getSourceBands

,

getSourceRegion

,

getSourceXSubsampling

,

getSourceYSubsampling

,

getSubsamplingXOffset

,

getSubsamplingYOffset

,

hasController

,

setController

,

setDestinationOffset

,

setDestinationType

,

setSourceBands

,

setSourceRegion

,

setSourceSubsampling

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

Returns

true

if this reader allows the source
image to be rendered at an arbitrary size as part of the
decoding process, by means of the

setSourceRenderSize

method.

Returns the

BufferedImage

currently set by the

setDestination

method, or

null

if none is set.

Returns the set of band indices where data will be placed.

If

getSourceNumProgressivePasses

is equal to

Integer.MAX_VALUE

, returns

Integer.MAX_VALUE

.

Returns the index of the first progressive pass that will be
decoded.

Returns the number of the progressive passes that will be
decoded.

Returns the width and height of the source image as it
will be rendered during decoding, if they have been set via the

setSourceRenderSize

method.

Supplies a

BufferedImage

to be used as the
destination for decoded pixel data.

Sets the indices of the destination bands where data
will be placed.

Sets the range of progressive passes that will be decoded.

If the image is able to be rendered at an arbitrary size, sets
the source width and height to the supplied values.

Methods declared in class javax.imageio.

IIOParam

activateController

,

getController

,

getDefaultController

,

getDestinationOffset

,

getDestinationType

,

getSourceBands

,

getSourceRegion

,

getSourceXSubsampling

,

getSourceYSubsampling

,

getSubsamplingXOffset

,

getSubsamplingYOffset

,

hasController

,

setController

,

setDestinationOffset

,

setDestinationType

,

setSourceBands

,

setSourceRegion

,

setSourceSubsampling

---

#### Methods declared in class javax.imageio. IIOParam

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

- canSetSourceRenderSize

```java
protected boolean canSetSourceRenderSize
```

true

if this

ImageReadParam

allows
the source rendering dimensions to be set. By default, the
value is

false

. Subclasses must set this value
manually.

ImageReader

s that do not support setting of
the source render size should set this value to

false

.

- sourceRenderSize

```java
protected
Dimension
sourceRenderSize
```

The desired rendering width and height of the source, if

canSetSourceRenderSize

is

true

, or

null

.

ImageReader

s that do not support setting of
the source render size may ignore this value.

- destination

```java
protected
BufferedImage
destination
```

The current destination

BufferedImage

, or

null

if none has been set. By default, the value
is

null

.

- destinationBands

```java
protected int[] destinationBands
```

The set of destination bands to be used, as an array of

int

s. By default, the value is

null

,
indicating all destination bands should be written in order.

- minProgressivePass

```java
protected int minProgressivePass
```

The minimum index of a progressive pass to read from the
source. By default, the value is set to 0, which indicates
that passes starting with the first available pass should be
decoded.

Subclasses should ensure that this value is
non-negative.

- numProgressivePasses

```java
protected int numProgressivePasses
```

The maximum number of progressive passes to read from the
source. By default, the value is set to

Integer.MAX_VALUE

, which indicates that passes up
to and including the last available pass should be decoded.

Subclasses should ensure that this value is positive.
Additionally, if the value is not

Integer.MAX_VALUE

, then

minProgressivePass + numProgressivePasses - 1

should not exceed

Integer.MAX_VALUE

.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ImageReadParam

```java
public ImageReadParam()
```

Constructs an

ImageReadParam

.

============ METHOD DETAIL ==========

- Method Detail

- setDestination

```java
public void setDestination​(
BufferedImage
destination)
```

Supplies a

BufferedImage

to be used as the
destination for decoded pixel data. The currently set image
will be written to by the

read

,

readAll

, and

readRaster

methods, and
a reference to it will be returned by those methods.

Pixel data from the aforementioned methods will be written
starting at the offset specified by

getDestinationOffset

.

If

destination

is

null

, a
newly-created

BufferedImage

will be returned by
those methods.

At the time of reading, the image is checked to verify that
its

ColorModel

and

SampleModel

correspond to one of the

ImageTypeSpecifier

s
returned from the

ImageReader

's

getImageTypes

method. If it does not, the reader
will throw an

IIOException

.

**Parameters:** destination

- the BufferedImage to be written to, or

null

.
**See Also:** getDestination()

- getDestination

```java
public
BufferedImage
getDestination()
```

Returns the

BufferedImage

currently set by the

setDestination

method, or

null

if none is set.

**Returns:** the BufferedImage to be written to.
**See Also:** setDestination(java.awt.image.BufferedImage)

- setDestinationBands

```java
public void setDestinationBands​(int[] destinationBands)
```

Sets the indices of the destination bands where data
will be placed. Duplicate indices are not allowed.

A

null

value indicates that all destination
bands will be used.

Choosing a destination band subset will not affect the
number of bands in the output image of a read if no destination
image is specified; the created destination image will still
have the same number of bands as if this method had never been
called. If a different number of bands in the destination
image is desired, an image must be supplied using the

ImageReadParam.setDestination

method.

At the time of reading or writing, an

IllegalArgumentException

will be thrown by the
reader or writer if a value larger than the largest destination
band index has been specified, or if the number of source bands
and destination bands to be used differ. The

ImageReader.checkReadParamBandSettings

method may
be used to automate this test.

**Parameters:** destinationBands

- an array of integer band indices to be
used.
**Throws:** IllegalArgumentException

- if

destinationBands

contains a negative or duplicate value.
**See Also:** getDestinationBands()

,

IIOParam.getSourceBands()

,

ImageReader.checkReadParamBandSettings(javax.imageio.ImageReadParam, int, int)

- getDestinationBands

```java
public int[] getDestinationBands()
```

Returns the set of band indices where data will be placed.
If no value has been set,

null

is returned to
indicate that all destination bands will be used.

**Returns:** the indices of the destination bands to be used,
or

null

.
**See Also:** setDestinationBands(int[])

- canSetSourceRenderSize

```java
public boolean canSetSourceRenderSize()
```

Returns

true

if this reader allows the source
image to be rendered at an arbitrary size as part of the
decoding process, by means of the

setSourceRenderSize

method. If this method
returns

false

, calls to

setSourceRenderSize

will throw an

UnsupportedOperationException

.

**Returns:** true

if setting source rendering size is
supported.
**See Also:** setSourceRenderSize(java.awt.Dimension)

- setSourceRenderSize

```java
public void setSourceRenderSize​(
Dimension
size)
throws
UnsupportedOperationException
```

If the image is able to be rendered at an arbitrary size, sets
the source width and height to the supplied values. Note that
the values returned from the

getWidth

and

getHeight

methods on

ImageReader

are
not affected by this method; they will continue to return the
default size for the image. Similarly, if the image is also
tiled the tile width and height are given in terms of the default
size.

Typically, the width and height should be chosen such that
the ratio of width to height closely approximates the aspect
ratio of the image, as returned from

ImageReader.getAspectRatio

.

If this plug-in does not allow the rendering size to be
set, an

UnsupportedOperationException

will be
thrown.

To remove the render size setting, pass in a value of

null

for

size

.

**Parameters:** size

- a

Dimension

indicating the desired
width and height.
**Throws:** IllegalArgumentException

- if either the width or the
height is negative or 0.
**Throws:** UnsupportedOperationException

- if image resizing
is not supported by this plug-in.
**See Also:** getSourceRenderSize()

,

ImageReader.getWidth(int)

,

ImageReader.getHeight(int)

,

ImageReader.getAspectRatio(int)

- getSourceRenderSize

```java
public
Dimension
getSourceRenderSize()
```

Returns the width and height of the source image as it
will be rendered during decoding, if they have been set via the

setSourceRenderSize

method. A

null

value indicates that no setting has been made.

**Returns:** the rendered width and height of the source image
as a

Dimension

.
**See Also:** setSourceRenderSize(java.awt.Dimension)

- setSourceProgressivePasses

```java
public void setSourceProgressivePasses​(int minPass,
int numPasses)
```

Sets the range of progressive passes that will be decoded.
Passes outside of this range will be ignored.

A progressive pass is a re-encoding of the entire image,
generally at progressively higher effective resolutions, but
requiring greater transmission bandwidth. The most common use
of progressive encoding is found in the JPEG format, where
successive passes include more detailed representations of the
high-frequency image content.

The actual number of passes to be decoded is determined
during decoding, based on the number of actual passes available
in the stream. Thus if

minPass + numPasses - 1

is
larger than the index of the last available passes, decoding
will end with that pass.

A value of

numPasses

of

Integer.MAX_VALUE

indicates that all passes from

minPass

forward should be read. Otherwise, the
index of the last pass (

i.e.

,

minPass + numPasses - 1

)
must not exceed

Integer.MAX_VALUE

.

There is no

unsetSourceProgressivePasses

method; the same effect may be obtained by calling

setSourceProgressivePasses(0, Integer.MAX_VALUE)

.

**Parameters:** minPass

- the index of the first pass to be decoded.
**Parameters:** numPasses

- the maximum number of passes to be decoded.
**Throws:** IllegalArgumentException

- if

minPass

is
negative,

numPasses

is negative or 0, or

numPasses

is smaller than

Integer.MAX_VALUE

but

minPass + numPasses - 1

is greater than

INTEGER.MAX_VALUE

.
**See Also:** getSourceMinProgressivePass()

,

getSourceMaxProgressivePass()

- getSourceMinProgressivePass

```java
public int getSourceMinProgressivePass()
```

Returns the index of the first progressive pass that will be
decoded. If no value has been set, 0 will be returned (which is
the correct value).

**Returns:** the index of the first pass that will be decoded.
**See Also:** setSourceProgressivePasses(int, int)

,

getSourceNumProgressivePasses()

- getSourceMaxProgressivePass

```java
public int getSourceMaxProgressivePass()
```

If

getSourceNumProgressivePasses

is equal to

Integer.MAX_VALUE

, returns

Integer.MAX_VALUE

. Otherwise, returns

getSourceMinProgressivePass() +
getSourceNumProgressivePasses() - 1

.

**Returns:** the index of the last pass to be read, or

Integer.MAX_VALUE

.

- getSourceNumProgressivePasses

```java
public int getSourceNumProgressivePasses()
```

Returns the number of the progressive passes that will be
decoded. If no value has been set,

Integer.MAX_VALUE

will be returned (which is the
correct value).

**Returns:** the number of the passes that will be decoded.
**See Also:** setSourceProgressivePasses(int, int)

,

getSourceMinProgressivePass()

Field Detail

- canSetSourceRenderSize

```java
protected boolean canSetSourceRenderSize
```

true

if this

ImageReadParam

allows
the source rendering dimensions to be set. By default, the
value is

false

. Subclasses must set this value
manually.

ImageReader

s that do not support setting of
the source render size should set this value to

false

.

- sourceRenderSize

```java
protected
Dimension
sourceRenderSize
```

The desired rendering width and height of the source, if

canSetSourceRenderSize

is

true

, or

null

.

ImageReader

s that do not support setting of
the source render size may ignore this value.

- destination

```java
protected
BufferedImage
destination
```

The current destination

BufferedImage

, or

null

if none has been set. By default, the value
is

null

.

- destinationBands

```java
protected int[] destinationBands
```

The set of destination bands to be used, as an array of

int

s. By default, the value is

null

,
indicating all destination bands should be written in order.

- minProgressivePass

```java
protected int minProgressivePass
```

The minimum index of a progressive pass to read from the
source. By default, the value is set to 0, which indicates
that passes starting with the first available pass should be
decoded.

Subclasses should ensure that this value is
non-negative.

- numProgressivePasses

```java
protected int numProgressivePasses
```

The maximum number of progressive passes to read from the
source. By default, the value is set to

Integer.MAX_VALUE

, which indicates that passes up
to and including the last available pass should be decoded.

Subclasses should ensure that this value is positive.
Additionally, if the value is not

Integer.MAX_VALUE

, then

minProgressivePass + numProgressivePasses - 1

should not exceed

Integer.MAX_VALUE

.

---

#### Field Detail

canSetSourceRenderSize

```java
protected boolean canSetSourceRenderSize
```

true

if this

ImageReadParam

allows
the source rendering dimensions to be set. By default, the
value is

false

. Subclasses must set this value
manually.

ImageReader

s that do not support setting of
the source render size should set this value to

false

.

---

#### canSetSourceRenderSize

protected boolean canSetSourceRenderSize

true

if this

ImageReadParam

allows
the source rendering dimensions to be set. By default, the
value is

false

. Subclasses must set this value
manually.

ImageReader

s that do not support setting of
the source render size should set this value to

false

.

ImageReader

s that do not support setting of
the source render size should set this value to

false

.

sourceRenderSize

```java
protected
Dimension
sourceRenderSize
```

The desired rendering width and height of the source, if

canSetSourceRenderSize

is

true

, or

null

.

ImageReader

s that do not support setting of
the source render size may ignore this value.

---

#### sourceRenderSize

protected

Dimension

sourceRenderSize

The desired rendering width and height of the source, if

canSetSourceRenderSize

is

true

, or

null

.

ImageReader

s that do not support setting of
the source render size may ignore this value.

ImageReader

s that do not support setting of
the source render size may ignore this value.

destination

```java
protected
BufferedImage
destination
```

The current destination

BufferedImage

, or

null

if none has been set. By default, the value
is

null

.

---

#### destination

protected

BufferedImage

destination

The current destination

BufferedImage

, or

null

if none has been set. By default, the value
is

null

.

destinationBands

```java
protected int[] destinationBands
```

The set of destination bands to be used, as an array of

int

s. By default, the value is

null

,
indicating all destination bands should be written in order.

---

#### destinationBands

protected int[] destinationBands

The set of destination bands to be used, as an array of

int

s. By default, the value is

null

,
indicating all destination bands should be written in order.

minProgressivePass

```java
protected int minProgressivePass
```

The minimum index of a progressive pass to read from the
source. By default, the value is set to 0, which indicates
that passes starting with the first available pass should be
decoded.

Subclasses should ensure that this value is
non-negative.

---

#### minProgressivePass

protected int minProgressivePass

The minimum index of a progressive pass to read from the
source. By default, the value is set to 0, which indicates
that passes starting with the first available pass should be
decoded.

Subclasses should ensure that this value is
non-negative.

Subclasses should ensure that this value is
non-negative.

numProgressivePasses

```java
protected int numProgressivePasses
```

The maximum number of progressive passes to read from the
source. By default, the value is set to

Integer.MAX_VALUE

, which indicates that passes up
to and including the last available pass should be decoded.

Subclasses should ensure that this value is positive.
Additionally, if the value is not

Integer.MAX_VALUE

, then

minProgressivePass + numProgressivePasses - 1

should not exceed

Integer.MAX_VALUE

.

---

#### numProgressivePasses

protected int numProgressivePasses

The maximum number of progressive passes to read from the
source. By default, the value is set to

Integer.MAX_VALUE

, which indicates that passes up
to and including the last available pass should be decoded.

Subclasses should ensure that this value is positive.
Additionally, if the value is not

Integer.MAX_VALUE

, then

minProgressivePass + numProgressivePasses - 1

should not exceed

Integer.MAX_VALUE

.

Subclasses should ensure that this value is positive.
Additionally, if the value is not

Integer.MAX_VALUE

, then

minProgressivePass + numProgressivePasses - 1

should not exceed

Integer.MAX_VALUE

.

Constructor Detail

- ImageReadParam

```java
public ImageReadParam()
```

Constructs an

ImageReadParam

.

---

#### Constructor Detail

ImageReadParam

```java
public ImageReadParam()
```

Constructs an

ImageReadParam

.

---

#### ImageReadParam

public ImageReadParam()

Constructs an

ImageReadParam

.

Method Detail

- setDestination

```java
public void setDestination​(
BufferedImage
destination)
```

Supplies a

BufferedImage

to be used as the
destination for decoded pixel data. The currently set image
will be written to by the

read

,

readAll

, and

readRaster

methods, and
a reference to it will be returned by those methods.

Pixel data from the aforementioned methods will be written
starting at the offset specified by

getDestinationOffset

.

If

destination

is

null

, a
newly-created

BufferedImage

will be returned by
those methods.

At the time of reading, the image is checked to verify that
its

ColorModel

and

SampleModel

correspond to one of the

ImageTypeSpecifier

s
returned from the

ImageReader

's

getImageTypes

method. If it does not, the reader
will throw an

IIOException

.

**Parameters:** destination

- the BufferedImage to be written to, or

null

.
**See Also:** getDestination()

- getDestination

```java
public
BufferedImage
getDestination()
```

Returns the

BufferedImage

currently set by the

setDestination

method, or

null

if none is set.

**Returns:** the BufferedImage to be written to.
**See Also:** setDestination(java.awt.image.BufferedImage)

- setDestinationBands

```java
public void setDestinationBands​(int[] destinationBands)
```

Sets the indices of the destination bands where data
will be placed. Duplicate indices are not allowed.

A

null

value indicates that all destination
bands will be used.

Choosing a destination band subset will not affect the
number of bands in the output image of a read if no destination
image is specified; the created destination image will still
have the same number of bands as if this method had never been
called. If a different number of bands in the destination
image is desired, an image must be supplied using the

ImageReadParam.setDestination

method.

At the time of reading or writing, an

IllegalArgumentException

will be thrown by the
reader or writer if a value larger than the largest destination
band index has been specified, or if the number of source bands
and destination bands to be used differ. The

ImageReader.checkReadParamBandSettings

method may
be used to automate this test.

**Parameters:** destinationBands

- an array of integer band indices to be
used.
**Throws:** IllegalArgumentException

- if

destinationBands

contains a negative or duplicate value.
**See Also:** getDestinationBands()

,

IIOParam.getSourceBands()

,

ImageReader.checkReadParamBandSettings(javax.imageio.ImageReadParam, int, int)

- getDestinationBands

```java
public int[] getDestinationBands()
```

Returns the set of band indices where data will be placed.
If no value has been set,

null

is returned to
indicate that all destination bands will be used.

**Returns:** the indices of the destination bands to be used,
or

null

.
**See Also:** setDestinationBands(int[])

- canSetSourceRenderSize

```java
public boolean canSetSourceRenderSize()
```

Returns

true

if this reader allows the source
image to be rendered at an arbitrary size as part of the
decoding process, by means of the

setSourceRenderSize

method. If this method
returns

false

, calls to

setSourceRenderSize

will throw an

UnsupportedOperationException

.

**Returns:** true

if setting source rendering size is
supported.
**See Also:** setSourceRenderSize(java.awt.Dimension)

- setSourceRenderSize

```java
public void setSourceRenderSize​(
Dimension
size)
throws
UnsupportedOperationException
```

If the image is able to be rendered at an arbitrary size, sets
the source width and height to the supplied values. Note that
the values returned from the

getWidth

and

getHeight

methods on

ImageReader

are
not affected by this method; they will continue to return the
default size for the image. Similarly, if the image is also
tiled the tile width and height are given in terms of the default
size.

Typically, the width and height should be chosen such that
the ratio of width to height closely approximates the aspect
ratio of the image, as returned from

ImageReader.getAspectRatio

.

If this plug-in does not allow the rendering size to be
set, an

UnsupportedOperationException

will be
thrown.

To remove the render size setting, pass in a value of

null

for

size

.

**Parameters:** size

- a

Dimension

indicating the desired
width and height.
**Throws:** IllegalArgumentException

- if either the width or the
height is negative or 0.
**Throws:** UnsupportedOperationException

- if image resizing
is not supported by this plug-in.
**See Also:** getSourceRenderSize()

,

ImageReader.getWidth(int)

,

ImageReader.getHeight(int)

,

ImageReader.getAspectRatio(int)

- getSourceRenderSize

```java
public
Dimension
getSourceRenderSize()
```

Returns the width and height of the source image as it
will be rendered during decoding, if they have been set via the

setSourceRenderSize

method. A

null

value indicates that no setting has been made.

**Returns:** the rendered width and height of the source image
as a

Dimension

.
**See Also:** setSourceRenderSize(java.awt.Dimension)

- setSourceProgressivePasses

```java
public void setSourceProgressivePasses​(int minPass,
int numPasses)
```

Sets the range of progressive passes that will be decoded.
Passes outside of this range will be ignored.

A progressive pass is a re-encoding of the entire image,
generally at progressively higher effective resolutions, but
requiring greater transmission bandwidth. The most common use
of progressive encoding is found in the JPEG format, where
successive passes include more detailed representations of the
high-frequency image content.

The actual number of passes to be decoded is determined
during decoding, based on the number of actual passes available
in the stream. Thus if

minPass + numPasses - 1

is
larger than the index of the last available passes, decoding
will end with that pass.

A value of

numPasses

of

Integer.MAX_VALUE

indicates that all passes from

minPass

forward should be read. Otherwise, the
index of the last pass (

i.e.

,

minPass + numPasses - 1

)
must not exceed

Integer.MAX_VALUE

.

There is no

unsetSourceProgressivePasses

method; the same effect may be obtained by calling

setSourceProgressivePasses(0, Integer.MAX_VALUE)

.

**Parameters:** minPass

- the index of the first pass to be decoded.
**Parameters:** numPasses

- the maximum number of passes to be decoded.
**Throws:** IllegalArgumentException

- if

minPass

is
negative,

numPasses

is negative or 0, or

numPasses

is smaller than

Integer.MAX_VALUE

but

minPass + numPasses - 1

is greater than

INTEGER.MAX_VALUE

.
**See Also:** getSourceMinProgressivePass()

,

getSourceMaxProgressivePass()

- getSourceMinProgressivePass

```java
public int getSourceMinProgressivePass()
```

Returns the index of the first progressive pass that will be
decoded. If no value has been set, 0 will be returned (which is
the correct value).

**Returns:** the index of the first pass that will be decoded.
**See Also:** setSourceProgressivePasses(int, int)

,

getSourceNumProgressivePasses()

- getSourceMaxProgressivePass

```java
public int getSourceMaxProgressivePass()
```

If

getSourceNumProgressivePasses

is equal to

Integer.MAX_VALUE

, returns

Integer.MAX_VALUE

. Otherwise, returns

getSourceMinProgressivePass() +
getSourceNumProgressivePasses() - 1

.

**Returns:** the index of the last pass to be read, or

Integer.MAX_VALUE

.

- getSourceNumProgressivePasses

```java
public int getSourceNumProgressivePasses()
```

Returns the number of the progressive passes that will be
decoded. If no value has been set,

Integer.MAX_VALUE

will be returned (which is the
correct value).

**Returns:** the number of the passes that will be decoded.
**See Also:** setSourceProgressivePasses(int, int)

,

getSourceMinProgressivePass()

---

#### Method Detail

setDestination

```java
public void setDestination​(
BufferedImage
destination)
```

Supplies a

BufferedImage

to be used as the
destination for decoded pixel data. The currently set image
will be written to by the

read

,

readAll

, and

readRaster

methods, and
a reference to it will be returned by those methods.

Pixel data from the aforementioned methods will be written
starting at the offset specified by

getDestinationOffset

.

If

destination

is

null

, a
newly-created

BufferedImage

will be returned by
those methods.

At the time of reading, the image is checked to verify that
its

ColorModel

and

SampleModel

correspond to one of the

ImageTypeSpecifier

s
returned from the

ImageReader

's

getImageTypes

method. If it does not, the reader
will throw an

IIOException

.

**Parameters:** destination

- the BufferedImage to be written to, or

null

.
**See Also:** getDestination()

---

#### setDestination

public void setDestination​(

BufferedImage

destination)

Supplies a

BufferedImage

to be used as the
destination for decoded pixel data. The currently set image
will be written to by the

read

,

readAll

, and

readRaster

methods, and
a reference to it will be returned by those methods.

Pixel data from the aforementioned methods will be written
starting at the offset specified by

getDestinationOffset

.

If

destination

is

null

, a
newly-created

BufferedImage

will be returned by
those methods.

At the time of reading, the image is checked to verify that
its

ColorModel

and

SampleModel

correspond to one of the

ImageTypeSpecifier

s
returned from the

ImageReader

's

getImageTypes

method. If it does not, the reader
will throw an

IIOException

.

Pixel data from the aforementioned methods will be written
starting at the offset specified by

getDestinationOffset

.

If

destination

is

null

, a
newly-created

BufferedImage

will be returned by
those methods.

At the time of reading, the image is checked to verify that
its

ColorModel

and

SampleModel

correspond to one of the

ImageTypeSpecifier

s
returned from the

ImageReader

's

getImageTypes

method. If it does not, the reader
will throw an

IIOException

.

If

destination

is

null

, a
newly-created

BufferedImage

will be returned by
those methods.

At the time of reading, the image is checked to verify that
its

ColorModel

and

SampleModel

correspond to one of the

ImageTypeSpecifier

s
returned from the

ImageReader

's

getImageTypes

method. If it does not, the reader
will throw an

IIOException

.

At the time of reading, the image is checked to verify that
its

ColorModel

and

SampleModel

correspond to one of the

ImageTypeSpecifier

s
returned from the

ImageReader

's

getImageTypes

method. If it does not, the reader
will throw an

IIOException

.

getDestination

```java
public
BufferedImage
getDestination()
```

Returns the

BufferedImage

currently set by the

setDestination

method, or

null

if none is set.

**Returns:** the BufferedImage to be written to.
**See Also:** setDestination(java.awt.image.BufferedImage)

---

#### getDestination

public

BufferedImage

getDestination()

Returns the

BufferedImage

currently set by the

setDestination

method, or

null

if none is set.

setDestinationBands

```java
public void setDestinationBands​(int[] destinationBands)
```

Sets the indices of the destination bands where data
will be placed. Duplicate indices are not allowed.

A

null

value indicates that all destination
bands will be used.

Choosing a destination band subset will not affect the
number of bands in the output image of a read if no destination
image is specified; the created destination image will still
have the same number of bands as if this method had never been
called. If a different number of bands in the destination
image is desired, an image must be supplied using the

ImageReadParam.setDestination

method.

At the time of reading or writing, an

IllegalArgumentException

will be thrown by the
reader or writer if a value larger than the largest destination
band index has been specified, or if the number of source bands
and destination bands to be used differ. The

ImageReader.checkReadParamBandSettings

method may
be used to automate this test.

**Parameters:** destinationBands

- an array of integer band indices to be
used.
**Throws:** IllegalArgumentException

- if

destinationBands

contains a negative or duplicate value.
**See Also:** getDestinationBands()

,

IIOParam.getSourceBands()

,

ImageReader.checkReadParamBandSettings(javax.imageio.ImageReadParam, int, int)

---

#### setDestinationBands

public void setDestinationBands​(int[] destinationBands)

Sets the indices of the destination bands where data
will be placed. Duplicate indices are not allowed.

A

null

value indicates that all destination
bands will be used.

Choosing a destination band subset will not affect the
number of bands in the output image of a read if no destination
image is specified; the created destination image will still
have the same number of bands as if this method had never been
called. If a different number of bands in the destination
image is desired, an image must be supplied using the

ImageReadParam.setDestination

method.

At the time of reading or writing, an

IllegalArgumentException

will be thrown by the
reader or writer if a value larger than the largest destination
band index has been specified, or if the number of source bands
and destination bands to be used differ. The

ImageReader.checkReadParamBandSettings

method may
be used to automate this test.

A

null

value indicates that all destination
bands will be used.

Choosing a destination band subset will not affect the
number of bands in the output image of a read if no destination
image is specified; the created destination image will still
have the same number of bands as if this method had never been
called. If a different number of bands in the destination
image is desired, an image must be supplied using the

ImageReadParam.setDestination

method.

At the time of reading or writing, an

IllegalArgumentException

will be thrown by the
reader or writer if a value larger than the largest destination
band index has been specified, or if the number of source bands
and destination bands to be used differ. The

ImageReader.checkReadParamBandSettings

method may
be used to automate this test.

Choosing a destination band subset will not affect the
number of bands in the output image of a read if no destination
image is specified; the created destination image will still
have the same number of bands as if this method had never been
called. If a different number of bands in the destination
image is desired, an image must be supplied using the

ImageReadParam.setDestination

method.

At the time of reading or writing, an

IllegalArgumentException

will be thrown by the
reader or writer if a value larger than the largest destination
band index has been specified, or if the number of source bands
and destination bands to be used differ. The

ImageReader.checkReadParamBandSettings

method may
be used to automate this test.

At the time of reading or writing, an

IllegalArgumentException

will be thrown by the
reader or writer if a value larger than the largest destination
band index has been specified, or if the number of source bands
and destination bands to be used differ. The

ImageReader.checkReadParamBandSettings

method may
be used to automate this test.

getDestinationBands

```java
public int[] getDestinationBands()
```

Returns the set of band indices where data will be placed.
If no value has been set,

null

is returned to
indicate that all destination bands will be used.

**Returns:** the indices of the destination bands to be used,
or

null

.
**See Also:** setDestinationBands(int[])

---

#### getDestinationBands

public int[] getDestinationBands()

Returns the set of band indices where data will be placed.
If no value has been set,

null

is returned to
indicate that all destination bands will be used.

canSetSourceRenderSize

```java
public boolean canSetSourceRenderSize()
```

Returns

true

if this reader allows the source
image to be rendered at an arbitrary size as part of the
decoding process, by means of the

setSourceRenderSize

method. If this method
returns

false

, calls to

setSourceRenderSize

will throw an

UnsupportedOperationException

.

**Returns:** true

if setting source rendering size is
supported.
**See Also:** setSourceRenderSize(java.awt.Dimension)

---

#### canSetSourceRenderSize

public boolean canSetSourceRenderSize()

Returns

true

if this reader allows the source
image to be rendered at an arbitrary size as part of the
decoding process, by means of the

setSourceRenderSize

method. If this method
returns

false

, calls to

setSourceRenderSize

will throw an

UnsupportedOperationException

.

setSourceRenderSize

```java
public void setSourceRenderSize​(
Dimension
size)
throws
UnsupportedOperationException
```

If the image is able to be rendered at an arbitrary size, sets
the source width and height to the supplied values. Note that
the values returned from the

getWidth

and

getHeight

methods on

ImageReader

are
not affected by this method; they will continue to return the
default size for the image. Similarly, if the image is also
tiled the tile width and height are given in terms of the default
size.

Typically, the width and height should be chosen such that
the ratio of width to height closely approximates the aspect
ratio of the image, as returned from

ImageReader.getAspectRatio

.

If this plug-in does not allow the rendering size to be
set, an

UnsupportedOperationException

will be
thrown.

To remove the render size setting, pass in a value of

null

for

size

.

**Parameters:** size

- a

Dimension

indicating the desired
width and height.
**Throws:** IllegalArgumentException

- if either the width or the
height is negative or 0.
**Throws:** UnsupportedOperationException

- if image resizing
is not supported by this plug-in.
**See Also:** getSourceRenderSize()

,

ImageReader.getWidth(int)

,

ImageReader.getHeight(int)

,

ImageReader.getAspectRatio(int)

---

#### setSourceRenderSize

public void setSourceRenderSize​(

Dimension

size)
throws

UnsupportedOperationException

If the image is able to be rendered at an arbitrary size, sets
the source width and height to the supplied values. Note that
the values returned from the

getWidth

and

getHeight

methods on

ImageReader

are
not affected by this method; they will continue to return the
default size for the image. Similarly, if the image is also
tiled the tile width and height are given in terms of the default
size.

Typically, the width and height should be chosen such that
the ratio of width to height closely approximates the aspect
ratio of the image, as returned from

ImageReader.getAspectRatio

.

If this plug-in does not allow the rendering size to be
set, an

UnsupportedOperationException

will be
thrown.

To remove the render size setting, pass in a value of

null

for

size

.

Typically, the width and height should be chosen such that
the ratio of width to height closely approximates the aspect
ratio of the image, as returned from

ImageReader.getAspectRatio

.

If this plug-in does not allow the rendering size to be
set, an

UnsupportedOperationException

will be
thrown.

To remove the render size setting, pass in a value of

null

for

size

.

If this plug-in does not allow the rendering size to be
set, an

UnsupportedOperationException

will be
thrown.

To remove the render size setting, pass in a value of

null

for

size

.

To remove the render size setting, pass in a value of

null

for

size

.

getSourceRenderSize

```java
public
Dimension
getSourceRenderSize()
```

Returns the width and height of the source image as it
will be rendered during decoding, if they have been set via the

setSourceRenderSize

method. A

null

value indicates that no setting has been made.

**Returns:** the rendered width and height of the source image
as a

Dimension

.
**See Also:** setSourceRenderSize(java.awt.Dimension)

---

#### getSourceRenderSize

public

Dimension

getSourceRenderSize()

Returns the width and height of the source image as it
will be rendered during decoding, if they have been set via the

setSourceRenderSize

method. A

null

value indicates that no setting has been made.

setSourceProgressivePasses

```java
public void setSourceProgressivePasses​(int minPass,
int numPasses)
```

Sets the range of progressive passes that will be decoded.
Passes outside of this range will be ignored.

A progressive pass is a re-encoding of the entire image,
generally at progressively higher effective resolutions, but
requiring greater transmission bandwidth. The most common use
of progressive encoding is found in the JPEG format, where
successive passes include more detailed representations of the
high-frequency image content.

The actual number of passes to be decoded is determined
during decoding, based on the number of actual passes available
in the stream. Thus if

minPass + numPasses - 1

is
larger than the index of the last available passes, decoding
will end with that pass.

A value of

numPasses

of

Integer.MAX_VALUE

indicates that all passes from

minPass

forward should be read. Otherwise, the
index of the last pass (

i.e.

,

minPass + numPasses - 1

)
must not exceed

Integer.MAX_VALUE

.

There is no

unsetSourceProgressivePasses

method; the same effect may be obtained by calling

setSourceProgressivePasses(0, Integer.MAX_VALUE)

.

**Parameters:** minPass

- the index of the first pass to be decoded.
**Parameters:** numPasses

- the maximum number of passes to be decoded.
**Throws:** IllegalArgumentException

- if

minPass

is
negative,

numPasses

is negative or 0, or

numPasses

is smaller than

Integer.MAX_VALUE

but

minPass + numPasses - 1

is greater than

INTEGER.MAX_VALUE

.
**See Also:** getSourceMinProgressivePass()

,

getSourceMaxProgressivePass()

---

#### setSourceProgressivePasses

public void setSourceProgressivePasses​(int minPass,
int numPasses)

Sets the range of progressive passes that will be decoded.
Passes outside of this range will be ignored.

A progressive pass is a re-encoding of the entire image,
generally at progressively higher effective resolutions, but
requiring greater transmission bandwidth. The most common use
of progressive encoding is found in the JPEG format, where
successive passes include more detailed representations of the
high-frequency image content.

The actual number of passes to be decoded is determined
during decoding, based on the number of actual passes available
in the stream. Thus if

minPass + numPasses - 1

is
larger than the index of the last available passes, decoding
will end with that pass.

A value of

numPasses

of

Integer.MAX_VALUE

indicates that all passes from

minPass

forward should be read. Otherwise, the
index of the last pass (

i.e.

,

minPass + numPasses - 1

)
must not exceed

Integer.MAX_VALUE

.

There is no

unsetSourceProgressivePasses

method; the same effect may be obtained by calling

setSourceProgressivePasses(0, Integer.MAX_VALUE)

.

A progressive pass is a re-encoding of the entire image,
generally at progressively higher effective resolutions, but
requiring greater transmission bandwidth. The most common use
of progressive encoding is found in the JPEG format, where
successive passes include more detailed representations of the
high-frequency image content.

The actual number of passes to be decoded is determined
during decoding, based on the number of actual passes available
in the stream. Thus if

minPass + numPasses - 1

is
larger than the index of the last available passes, decoding
will end with that pass.

A value of

numPasses

of

Integer.MAX_VALUE

indicates that all passes from

minPass

forward should be read. Otherwise, the
index of the last pass (

i.e.

,

minPass + numPasses - 1

)
must not exceed

Integer.MAX_VALUE

.

There is no

unsetSourceProgressivePasses

method; the same effect may be obtained by calling

setSourceProgressivePasses(0, Integer.MAX_VALUE)

.

The actual number of passes to be decoded is determined
during decoding, based on the number of actual passes available
in the stream. Thus if

minPass + numPasses - 1

is
larger than the index of the last available passes, decoding
will end with that pass.

A value of

numPasses

of

Integer.MAX_VALUE

indicates that all passes from

minPass

forward should be read. Otherwise, the
index of the last pass (

i.e.

,

minPass + numPasses - 1

)
must not exceed

Integer.MAX_VALUE

.

There is no

unsetSourceProgressivePasses

method; the same effect may be obtained by calling

setSourceProgressivePasses(0, Integer.MAX_VALUE)

.

A value of

numPasses

of

Integer.MAX_VALUE

indicates that all passes from

minPass

forward should be read. Otherwise, the
index of the last pass (

i.e.

,

minPass + numPasses - 1

)
must not exceed

Integer.MAX_VALUE

.

There is no

unsetSourceProgressivePasses

method; the same effect may be obtained by calling

setSourceProgressivePasses(0, Integer.MAX_VALUE)

.

There is no

unsetSourceProgressivePasses

method; the same effect may be obtained by calling

setSourceProgressivePasses(0, Integer.MAX_VALUE)

.

getSourceMinProgressivePass

```java
public int getSourceMinProgressivePass()
```

Returns the index of the first progressive pass that will be
decoded. If no value has been set, 0 will be returned (which is
the correct value).

**Returns:** the index of the first pass that will be decoded.
**See Also:** setSourceProgressivePasses(int, int)

,

getSourceNumProgressivePasses()

---

#### getSourceMinProgressivePass

public int getSourceMinProgressivePass()

Returns the index of the first progressive pass that will be
decoded. If no value has been set, 0 will be returned (which is
the correct value).

getSourceMaxProgressivePass

```java
public int getSourceMaxProgressivePass()
```

If

getSourceNumProgressivePasses

is equal to

Integer.MAX_VALUE

, returns

Integer.MAX_VALUE

. Otherwise, returns

getSourceMinProgressivePass() +
getSourceNumProgressivePasses() - 1

.

**Returns:** the index of the last pass to be read, or

Integer.MAX_VALUE

.

---

#### getSourceMaxProgressivePass

public int getSourceMaxProgressivePass()

If

getSourceNumProgressivePasses

is equal to

Integer.MAX_VALUE

, returns

Integer.MAX_VALUE

. Otherwise, returns

getSourceMinProgressivePass() +
getSourceNumProgressivePasses() - 1

.

getSourceNumProgressivePasses

```java
public int getSourceNumProgressivePasses()
```

Returns the number of the progressive passes that will be
decoded. If no value has been set,

Integer.MAX_VALUE

will be returned (which is the
correct value).

**Returns:** the number of the passes that will be decoded.
**See Also:** setSourceProgressivePasses(int, int)

,

getSourceMinProgressivePass()

---

#### getSourceNumProgressivePasses

public int getSourceNumProgressivePasses()

Returns the number of the progressive passes that will be
decoded. If no value has been set,

Integer.MAX_VALUE

will be returned (which is the
correct value).

---

