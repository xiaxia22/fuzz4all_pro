# Class AreaAveragingScaleFilter

**Source:** `java.desktop\java\awt\image\AreaAveragingScaleFilter.html`

### Class Description

```java
public class
AreaAveragingScaleFilter

extends
ReplicateScaleFilter
```

An ImageFilter class for scaling images using a simple area averaging
algorithm that produces smoother results than the nearest neighbor
algorithm.

This class extends the basic ImageFilter Class to scale an existing
image and provide a source for a new image containing the resampled
image. The pixels in the source image are blended to produce pixels
for an image of the specified size. The blending process is analogous
to scaling up the source image to a multiple of the destination size
using pixel replication and then scaling it back down to the destination
size by simply averaging all the pixels in the supersized image that
fall within a given pixel of the destination image. If the data from
the source is not delivered in TopDownLeftRight order then the filter
will back off to a simple pixel replication behavior and utilize the
requestTopDownLeftRightResend() method to refilter the pixels in a
better way at the end.

It is meant to be used in conjunction with a FilteredImageSource
object to produce scaled versions of existing images. Due to
implementation dependencies, there may be differences in pixel values
of an image filtered on different platforms.

**All Implemented Interfaces:** ImageConsumer

,

Cloneable

---

### Field Details

*No entries found.*

### Constructor Details

#### public AreaAveragingScaleFilter​(int width,
int height)

Constructs an AreaAveragingScaleFilter that scales the pixels from
its source Image as specified by the width and height parameters.

**Parameters:**
- width

- the target width to scale the image
- height

- the target height to scale the image

---

### Method Details

#### public void setHints​(int hints)

Detect if the data is being delivered with the necessary hints
to allow the averaging algorithm to do its work.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose
pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

**Specified by:**
- setHints

in interface

ImageConsumer

**Overrides:**
- setHints

in class

ImageFilter

**Parameters:**
- hints

- a set of hints that the ImageConsumer uses to
process the pixels

**See Also:**
- ImageConsumer.setHints(int)

---

#### public void setPixels​(int x,
int y,
int w,
int h,

ColorModel
model,
byte[] pixels,
int off,
int scansize)

Combine the components for the delivered byte pixels into the
accumulation arrays and send on any averaged data for rows of
pixels that are complete. If the correct hints were not
specified in the setHints call then relay the work to our
superclass which is capable of scaling pixels regardless of
the delivery hints.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

**Specified by:**
- setPixels

in interface

ImageConsumer

**Overrides:**
- setPixels

in class

ReplicateScaleFilter

**Parameters:**
- x

- the X coordinate of the upper-left corner of the
area of pixels to be set
- y

- the Y coordinate of the upper-left corner of the
area of pixels to be set
- w

- the width of the area of pixels
- h

- the height of the area of pixels
- model

- the specified

ColorModel
- pixels

- the array of pixels
- off

- the offset into the

pixels

array
- scansize

- the distance from one row of pixels to the next in
the

pixels

array

**See Also:**
- ReplicateScaleFilter

---

#### public void setPixels​(int x,
int y,
int w,
int h,

ColorModel
model,
int[] pixels,
int off,
int scansize)

Combine the components for the delivered int pixels into the
accumulation arrays and send on any averaged data for rows of
pixels that are complete. If the correct hints were not
specified in the setHints call then relay the work to our
superclass which is capable of scaling pixels regardless of
the delivery hints.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

**Specified by:**
- setPixels

in interface

ImageConsumer

**Overrides:**
- setPixels

in class

ReplicateScaleFilter

**Parameters:**
- x

- the X coordinate of the upper-left corner of the
area of pixels to be set
- y

- the Y coordinate of the upper-left corner of the
area of pixels to be set
- w

- the width of the area of pixels
- h

- the height of the area of pixels
- model

- the specified

ColorModel
- pixels

- the array of pixels
- off

- the offset into the

pixels

array
- scansize

- the distance from one row of pixels to the next in
the

pixels

array

**See Also:**
- ReplicateScaleFilter

---

### Additional Sections

#### Class AreaAveragingScaleFilter

java.lang.Object

- java.awt.image.ImageFilter
- - java.awt.image.ReplicateScaleFilter
- - java.awt.image.AreaAveragingScaleFilter

java.awt.image.ImageFilter

- java.awt.image.ReplicateScaleFilter
- - java.awt.image.AreaAveragingScaleFilter

java.awt.image.ReplicateScaleFilter

- java.awt.image.AreaAveragingScaleFilter

java.awt.image.AreaAveragingScaleFilter

**All Implemented Interfaces:** ImageConsumer

,

Cloneable

```java
public class
AreaAveragingScaleFilter

extends
ReplicateScaleFilter
```

An ImageFilter class for scaling images using a simple area averaging
algorithm that produces smoother results than the nearest neighbor
algorithm.

This class extends the basic ImageFilter Class to scale an existing
image and provide a source for a new image containing the resampled
image. The pixels in the source image are blended to produce pixels
for an image of the specified size. The blending process is analogous
to scaling up the source image to a multiple of the destination size
using pixel replication and then scaling it back down to the destination
size by simply averaging all the pixels in the supersized image that
fall within a given pixel of the destination image. If the data from
the source is not delivered in TopDownLeftRight order then the filter
will back off to a simple pixel replication behavior and utilize the
requestTopDownLeftRightResend() method to refilter the pixels in a
better way at the end.

It is meant to be used in conjunction with a FilteredImageSource
object to produce scaled versions of existing images. Due to
implementation dependencies, there may be differences in pixel values
of an image filtered on different platforms.

**See Also:** FilteredImageSource

,

ReplicateScaleFilter

,

ImageFilter

public class

AreaAveragingScaleFilter

extends

ReplicateScaleFilter

An ImageFilter class for scaling images using a simple area averaging
algorithm that produces smoother results than the nearest neighbor
algorithm.

This class extends the basic ImageFilter Class to scale an existing
image and provide a source for a new image containing the resampled
image. The pixels in the source image are blended to produce pixels
for an image of the specified size. The blending process is analogous
to scaling up the source image to a multiple of the destination size
using pixel replication and then scaling it back down to the destination
size by simply averaging all the pixels in the supersized image that
fall within a given pixel of the destination image. If the data from
the source is not delivered in TopDownLeftRight order then the filter
will back off to a simple pixel replication behavior and utilize the
requestTopDownLeftRightResend() method to refilter the pixels in a
better way at the end.

It is meant to be used in conjunction with a FilteredImageSource
object to produce scaled versions of existing images. Due to
implementation dependencies, there may be differences in pixel values
of an image filtered on different platforms.

This class extends the basic ImageFilter Class to scale an existing
image and provide a source for a new image containing the resampled
image. The pixels in the source image are blended to produce pixels
for an image of the specified size. The blending process is analogous
to scaling up the source image to a multiple of the destination size
using pixel replication and then scaling it back down to the destination
size by simply averaging all the pixels in the supersized image that
fall within a given pixel of the destination image. If the data from
the source is not delivered in TopDownLeftRight order then the filter
will back off to a simple pixel replication behavior and utilize the
requestTopDownLeftRightResend() method to refilter the pixels in a
better way at the end.

It is meant to be used in conjunction with a FilteredImageSource
object to produce scaled versions of existing images. Due to
implementation dependencies, there may be differences in pixel values
of an image filtered on different platforms.

It is meant to be used in conjunction with a FilteredImageSource
object to produce scaled versions of existing images. Due to
implementation dependencies, there may be differences in pixel values
of an image filtered on different platforms.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.awt.image.

ReplicateScaleFilter

destHeight

,

destWidth

,

outpixbuf

,

srccols

,

srcHeight

,

srcrows

,

srcWidth

- Fields declared in class java.awt.image.

ImageFilter

consumer

- Fields declared in interface java.awt.image.

ImageConsumer

COMPLETESCANLINES

,

IMAGEABORTED

,

IMAGEERROR

,

RANDOMPIXELORDER

,

SINGLEFRAME

,

SINGLEFRAMEDONE

,

SINGLEPASS

,

STATICIMAGEDONE

,

TOPDOWNLEFTRIGHT

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AreaAveragingScaleFilter

​(int width,
int height)

Constructs an AreaAveragingScaleFilter that scales the pixels from
its source Image as specified by the width and height parameters.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

setHints

​(int hints)

Detect if the data is being delivered with the necessary hints
to allow the averaging algorithm to do its work.

void

setPixels

​(int x,
int y,
int w,
int h,

ColorModel

model,
byte[] pixels,
int off,
int scansize)

Combine the components for the delivered byte pixels into the
accumulation arrays and send on any averaged data for rows of
pixels that are complete.

void

setPixels

​(int x,
int y,
int w,
int h,

ColorModel

model,
int[] pixels,
int off,
int scansize)

Combine the components for the delivered int pixels into the
accumulation arrays and send on any averaged data for rows of
pixels that are complete.

- Methods declared in class java.awt.image.

ReplicateScaleFilter

setDimensions

,

setProperties

- Methods declared in class java.awt.image.

ImageFilter

clone

,

getFilterInstance

,

imageComplete

,

resendTopDownLeftRight

,

setColorModel

- Methods declared in class java.lang.

Object

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

ReplicateScaleFilter

destHeight

,

destWidth

,

outpixbuf

,

srccols

,

srcHeight

,

srcrows

,

srcWidth

- Fields declared in class java.awt.image.

ImageFilter

consumer

- Fields declared in interface java.awt.image.

ImageConsumer

COMPLETESCANLINES

,

IMAGEABORTED

,

IMAGEERROR

,

RANDOMPIXELORDER

,

SINGLEFRAME

,

SINGLEFRAMEDONE

,

SINGLEPASS

,

STATICIMAGEDONE

,

TOPDOWNLEFTRIGHT

---

#### Field Summary

Fields declared in class java.awt.image.

ReplicateScaleFilter

destHeight

,

destWidth

,

outpixbuf

,

srccols

,

srcHeight

,

srcrows

,

srcWidth

---

#### Fields declared in class java.awt.image. ReplicateScaleFilter

Fields declared in class java.awt.image.

ImageFilter

consumer

---

#### Fields declared in class java.awt.image. ImageFilter

Fields declared in interface java.awt.image.

ImageConsumer

COMPLETESCANLINES

,

IMAGEABORTED

,

IMAGEERROR

,

RANDOMPIXELORDER

,

SINGLEFRAME

,

SINGLEFRAMEDONE

,

SINGLEPASS

,

STATICIMAGEDONE

,

TOPDOWNLEFTRIGHT

---

#### Fields declared in interface java.awt.image. ImageConsumer

Constructor Summary

Constructors

Constructor

Description

AreaAveragingScaleFilter

​(int width,
int height)

Constructs an AreaAveragingScaleFilter that scales the pixels from
its source Image as specified by the width and height parameters.

---

#### Constructor Summary

Constructs an AreaAveragingScaleFilter that scales the pixels from
its source Image as specified by the width and height parameters.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

setHints

​(int hints)

Detect if the data is being delivered with the necessary hints
to allow the averaging algorithm to do its work.

void

setPixels

​(int x,
int y,
int w,
int h,

ColorModel

model,
byte[] pixels,
int off,
int scansize)

Combine the components for the delivered byte pixels into the
accumulation arrays and send on any averaged data for rows of
pixels that are complete.

void

setPixels

​(int x,
int y,
int w,
int h,

ColorModel

model,
int[] pixels,
int off,
int scansize)

Combine the components for the delivered int pixels into the
accumulation arrays and send on any averaged data for rows of
pixels that are complete.

- Methods declared in class java.awt.image.

ReplicateScaleFilter

setDimensions

,

setProperties

- Methods declared in class java.awt.image.

ImageFilter

clone

,

getFilterInstance

,

imageComplete

,

resendTopDownLeftRight

,

setColorModel

- Methods declared in class java.lang.

Object

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

Detect if the data is being delivered with the necessary hints
to allow the averaging algorithm to do its work.

Combine the components for the delivered byte pixels into the
accumulation arrays and send on any averaged data for rows of
pixels that are complete.

Combine the components for the delivered int pixels into the
accumulation arrays and send on any averaged data for rows of
pixels that are complete.

Methods declared in class java.awt.image.

ReplicateScaleFilter

setDimensions

,

setProperties

---

#### Methods declared in class java.awt.image. ReplicateScaleFilter

Methods declared in class java.awt.image.

ImageFilter

clone

,

getFilterInstance

,

imageComplete

,

resendTopDownLeftRight

,

setColorModel

---

#### Methods declared in class java.awt.image. ImageFilter

Methods declared in class java.lang.

Object

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

- AreaAveragingScaleFilter

```java
public AreaAveragingScaleFilter​(int width,
int height)
```

Constructs an AreaAveragingScaleFilter that scales the pixels from
its source Image as specified by the width and height parameters.

**Parameters:** width

- the target width to scale the image
**Parameters:** height

- the target height to scale the image

============ METHOD DETAIL ==========

- Method Detail

- setHints

```java
public void setHints​(int hints)
```

Detect if the data is being delivered with the necessary hints
to allow the averaging algorithm to do its work.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose
pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

**Specified by:** setHints

in interface

ImageConsumer
**Overrides:** setHints

in class

ImageFilter
**Parameters:** hints

- a set of hints that the ImageConsumer uses to
process the pixels
**See Also:** ImageConsumer.setHints(int)

- setPixels

```java
public void setPixels​(int x,
int y,
int w,
int h,

ColorModel
model,
byte[] pixels,
int off,
int scansize)
```

Combine the components for the delivered byte pixels into the
accumulation arrays and send on any averaged data for rows of
pixels that are complete. If the correct hints were not
specified in the setHints call then relay the work to our
superclass which is capable of scaling pixels regardless of
the delivery hints.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

**Specified by:** setPixels

in interface

ImageConsumer
**Overrides:** setPixels

in class

ReplicateScaleFilter
**Parameters:** x

- the X coordinate of the upper-left corner of the
area of pixels to be set
**Parameters:** y

- the Y coordinate of the upper-left corner of the
area of pixels to be set
**Parameters:** w

- the width of the area of pixels
**Parameters:** h

- the height of the area of pixels
**Parameters:** model

- the specified

ColorModel
**Parameters:** pixels

- the array of pixels
**Parameters:** off

- the offset into the

pixels

array
**Parameters:** scansize

- the distance from one row of pixels to the next in
the

pixels

array
**See Also:** ReplicateScaleFilter

- setPixels

```java
public void setPixels​(int x,
int y,
int w,
int h,

ColorModel
model,
int[] pixels,
int off,
int scansize)
```

Combine the components for the delivered int pixels into the
accumulation arrays and send on any averaged data for rows of
pixels that are complete. If the correct hints were not
specified in the setHints call then relay the work to our
superclass which is capable of scaling pixels regardless of
the delivery hints.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

**Specified by:** setPixels

in interface

ImageConsumer
**Overrides:** setPixels

in class

ReplicateScaleFilter
**Parameters:** x

- the X coordinate of the upper-left corner of the
area of pixels to be set
**Parameters:** y

- the Y coordinate of the upper-left corner of the
area of pixels to be set
**Parameters:** w

- the width of the area of pixels
**Parameters:** h

- the height of the area of pixels
**Parameters:** model

- the specified

ColorModel
**Parameters:** pixels

- the array of pixels
**Parameters:** off

- the offset into the

pixels

array
**Parameters:** scansize

- the distance from one row of pixels to the next in
the

pixels

array
**See Also:** ReplicateScaleFilter

Constructor Detail

- AreaAveragingScaleFilter

```java
public AreaAveragingScaleFilter​(int width,
int height)
```

Constructs an AreaAveragingScaleFilter that scales the pixels from
its source Image as specified by the width and height parameters.

**Parameters:** width

- the target width to scale the image
**Parameters:** height

- the target height to scale the image

---

#### Constructor Detail

AreaAveragingScaleFilter

```java
public AreaAveragingScaleFilter​(int width,
int height)
```

Constructs an AreaAveragingScaleFilter that scales the pixels from
its source Image as specified by the width and height parameters.

**Parameters:** width

- the target width to scale the image
**Parameters:** height

- the target height to scale the image

---

#### AreaAveragingScaleFilter

public AreaAveragingScaleFilter​(int width,
int height)

Constructs an AreaAveragingScaleFilter that scales the pixels from
its source Image as specified by the width and height parameters.

Method Detail

- setHints

```java
public void setHints​(int hints)
```

Detect if the data is being delivered with the necessary hints
to allow the averaging algorithm to do its work.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose
pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

**Specified by:** setHints

in interface

ImageConsumer
**Overrides:** setHints

in class

ImageFilter
**Parameters:** hints

- a set of hints that the ImageConsumer uses to
process the pixels
**See Also:** ImageConsumer.setHints(int)

- setPixels

```java
public void setPixels​(int x,
int y,
int w,
int h,

ColorModel
model,
byte[] pixels,
int off,
int scansize)
```

Combine the components for the delivered byte pixels into the
accumulation arrays and send on any averaged data for rows of
pixels that are complete. If the correct hints were not
specified in the setHints call then relay the work to our
superclass which is capable of scaling pixels regardless of
the delivery hints.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

**Specified by:** setPixels

in interface

ImageConsumer
**Overrides:** setPixels

in class

ReplicateScaleFilter
**Parameters:** x

- the X coordinate of the upper-left corner of the
area of pixels to be set
**Parameters:** y

- the Y coordinate of the upper-left corner of the
area of pixels to be set
**Parameters:** w

- the width of the area of pixels
**Parameters:** h

- the height of the area of pixels
**Parameters:** model

- the specified

ColorModel
**Parameters:** pixels

- the array of pixels
**Parameters:** off

- the offset into the

pixels

array
**Parameters:** scansize

- the distance from one row of pixels to the next in
the

pixels

array
**See Also:** ReplicateScaleFilter

- setPixels

```java
public void setPixels​(int x,
int y,
int w,
int h,

ColorModel
model,
int[] pixels,
int off,
int scansize)
```

Combine the components for the delivered int pixels into the
accumulation arrays and send on any averaged data for rows of
pixels that are complete. If the correct hints were not
specified in the setHints call then relay the work to our
superclass which is capable of scaling pixels regardless of
the delivery hints.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

**Specified by:** setPixels

in interface

ImageConsumer
**Overrides:** setPixels

in class

ReplicateScaleFilter
**Parameters:** x

- the X coordinate of the upper-left corner of the
area of pixels to be set
**Parameters:** y

- the Y coordinate of the upper-left corner of the
area of pixels to be set
**Parameters:** w

- the width of the area of pixels
**Parameters:** h

- the height of the area of pixels
**Parameters:** model

- the specified

ColorModel
**Parameters:** pixels

- the array of pixels
**Parameters:** off

- the offset into the

pixels

array
**Parameters:** scansize

- the distance from one row of pixels to the next in
the

pixels

array
**See Also:** ReplicateScaleFilter

---

#### Method Detail

setHints

```java
public void setHints​(int hints)
```

Detect if the data is being delivered with the necessary hints
to allow the averaging algorithm to do its work.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose
pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

**Specified by:** setHints

in interface

ImageConsumer
**Overrides:** setHints

in class

ImageFilter
**Parameters:** hints

- a set of hints that the ImageConsumer uses to
process the pixels
**See Also:** ImageConsumer.setHints(int)

---

#### setHints

public void setHints​(int hints)

Detect if the data is being delivered with the necessary hints
to allow the averaging algorithm to do its work.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose
pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose
pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

setPixels

```java
public void setPixels​(int x,
int y,
int w,
int h,

ColorModel
model,
byte[] pixels,
int off,
int scansize)
```

Combine the components for the delivered byte pixels into the
accumulation arrays and send on any averaged data for rows of
pixels that are complete. If the correct hints were not
specified in the setHints call then relay the work to our
superclass which is capable of scaling pixels regardless of
the delivery hints.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

**Specified by:** setPixels

in interface

ImageConsumer
**Overrides:** setPixels

in class

ReplicateScaleFilter
**Parameters:** x

- the X coordinate of the upper-left corner of the
area of pixels to be set
**Parameters:** y

- the Y coordinate of the upper-left corner of the
area of pixels to be set
**Parameters:** w

- the width of the area of pixels
**Parameters:** h

- the height of the area of pixels
**Parameters:** model

- the specified

ColorModel
**Parameters:** pixels

- the array of pixels
**Parameters:** off

- the offset into the

pixels

array
**Parameters:** scansize

- the distance from one row of pixels to the next in
the

pixels

array
**See Also:** ReplicateScaleFilter

---

#### setPixels

public void setPixels​(int x,
int y,
int w,
int h,

ColorModel

model,
byte[] pixels,
int off,
int scansize)

Combine the components for the delivered byte pixels into the
accumulation arrays and send on any averaged data for rows of
pixels that are complete. If the correct hints were not
specified in the setHints call then relay the work to our
superclass which is capable of scaling pixels regardless of
the delivery hints.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

setPixels

```java
public void setPixels​(int x,
int y,
int w,
int h,

ColorModel
model,
int[] pixels,
int off,
int scansize)
```

Combine the components for the delivered int pixels into the
accumulation arrays and send on any averaged data for rows of
pixels that are complete. If the correct hints were not
specified in the setHints call then relay the work to our
superclass which is capable of scaling pixels regardless of
the delivery hints.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

**Specified by:** setPixels

in interface

ImageConsumer
**Overrides:** setPixels

in class

ReplicateScaleFilter
**Parameters:** x

- the X coordinate of the upper-left corner of the
area of pixels to be set
**Parameters:** y

- the Y coordinate of the upper-left corner of the
area of pixels to be set
**Parameters:** w

- the width of the area of pixels
**Parameters:** h

- the height of the area of pixels
**Parameters:** model

- the specified

ColorModel
**Parameters:** pixels

- the array of pixels
**Parameters:** off

- the offset into the

pixels

array
**Parameters:** scansize

- the distance from one row of pixels to the next in
the

pixels

array
**See Also:** ReplicateScaleFilter

---

#### setPixels

public void setPixels​(int x,
int y,
int w,
int h,

ColorModel

model,
int[] pixels,
int off,
int scansize)

Combine the components for the delivered int pixels into the
accumulation arrays and send on any averaged data for rows of
pixels that are complete. If the correct hints were not
specified in the setHints call then relay the work to our
superclass which is capable of scaling pixels regardless of
the delivery hints.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

Note: This method is intended to be called by the

ImageProducer

of the

Image

whose pixels are being filtered. Developers using
this class to filter pixels from an image should avoid calling
this method directly since that operation could interfere
with the filtering operation.

---

